#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
03 -- Clean, tag and aggregate the raw Google Play pull.

Vietnamese app stores carry heavy comment spam from unlicensed lending sites.
Much of it evades keyword filters by writing its brand in mathematical
alphanumeric Unicode, so that VayTotNhat arrives as characters that look
identical to a reader and are different code points to a matcher. Normalising
before matching is the step that makes the filter work at all: without the NFKC
pass, roughly one in eight spam reviews slips through.

Pipeline
    normalise -> flag loan spam -> flag referral spam -> drop copy-paste duplicates
              -> flag generic one-word reviews -> tag themes -> aggregate

Nothing is deleted from the input file. Every row keeps its flags, so any
decision can be audited or reversed.

Revision of 23 September 2026 (see doc/code_audit.md, items A1 to A6)
    Referral spam now needs a referral phrase next to a code or a reward amount,
    so "mà mọi người", "nhập mã OTP" and "đăng nhập mật khẩu" are no longer spam.
    The bare ".com" rule is gone. Theme keywords match whole words, and the
    syllables that collide once tone marks are stripped (lỗi/lời/lợi, lừa/lựa,
    sập/sắp, thưởng/thường) are matched with their accents or as longer phrases.
    Identical short reviews from different people ("good", "tuyệt vời") are no
    longer treated as duplicates. The generic flag uses the one-word rule that
    produced the published figures, which the old code described as four words.

Run
    python3 03_reviews_clean.py reviews_raw_vn.com.encapital.arrow.csv
    python3 03_reviews_clean.py --selftest

Output
    reviews_flagged_<name>.csv   every input row plus its flags
    reviews_summary_<name>.json  the aggregate tables used in the report
"""
import csv
import json
import os
import re
import sys
import unicodedata
from collections import defaultdict

# --------------------------------------------------------------- normalisation
def fold(s):
    """Fold a review to a comparable form, keeping its case.

    NFKC first, which maps the mathematical alphanumeric characters spammers use
    back to plain letters. Then NFD with combining marks removed, which strips
    Vietnamese tone marks. Then the stroked d, which NFD does not decompose.
    """
    s = unicodedata.normalize("NFKC", str(s or ""))
    s = unicodedata.normalize("NFD", s)
    s = "".join(ch for ch in s if not unicodedata.combining(ch))
    return s.replace("đ", "d").replace("Đ", "D")


def norm(s):
    """fold(), then lower case. Every rule below except two matches against this."""
    return fold(s).lower()


def accented(s):
    """NFKC and lower case with tone marks kept, for the syllables that need them."""
    return unicodedata.normalize("NFKC", str(s or "")).lower()

# --------------------------------------------------------------- spam rules
LOAN_RE = re.compile(
    r"(vay\s*9|vaytotnhat|vay\s*t?o?t\s*nhat|ktien|vayhangdau|vay333|vayfe|"
    r"fbvay|c0m|vay\s*0\s*%|vay\s*von\s*0)", re.I)

# Referral farming. A referral phrase on its own is not spam: "nhập mã OTP" is an
# onboarding complaint and "mà mỗi lần" folds to "ma moi". Farming posts always carry
# the code itself or the reward it pays, so a post counts only when a phrase sits next
# to a code or an amount, or a code sits next to an amount.
#
# Phrases are matched on norm(text). "nhap ma" is weak (it is also how people describe
# entering a one-time password); the others name a referral outright.
_WEAK_PHRASE = r"nhap\s*ma"
_STRONG_PHRASE = r"ma\s*(?:nguoi\s*)?(?:gioi\s*thieu|gt|gth|moi|dai\s*ly|vip|nhan\s*thuong)"
_WEAK_RE = re.compile(rf"\b{_WEAK_PHRASE}\b")
_STRONG_RE = re.compile(rf"\b{_STRONG_PHRASE}\b")
_AMOUNT_RE = re.compile(r"\b\d+(?:[.,]\d+)?\s*(?:k|nghin|trieu|tr)\b"      # 10k, 1 trieu
                        r"|\b\d{1,3}(?:[.,]\d{3})+\s*(?:d|dong|vnd)?\b")   # 200.000d, 1,000,000
# Codes are matched on fold(text), which keeps case, because App Store posts use codes
# such as MFBCFA or G25PRK that only their capitals tell apart from words.
#   six digits that are neither a round sum ("nạp 500000") nor one digit repeated
#   ("rút 888888 đồng lấy lộc"), or six digits typed with spaces
_NUM_CODE = r"(?<!\d)(?!\d{3}000(?!\d))(?!(?P<d>\d)(?P=d){5})\d{6}(?!\d)|\b(?:\d\s){5}\d\b"
#   four to eight capitals and digits with at least one of each, but not a market code:
#   VN30 futures (VN30F1M), index and ETF codes (VN100, E1VFVN30), covered warrants (CVHM2405)
_MIXED_CODE = (r"\b(?![A-Z0-9]*VN\d)(?!C[A-Z]{3}\d{4}\b)"
               r"(?=[A-Z0-9]*\d)(?=[A-Z0-9]*[A-Z])[A-Z0-9]{4,8}\b")
_CODE_RE = re.compile(rf"{_NUM_CODE}|{_MIXED_CODE}")
_NUM_CODE_RE = re.compile(_NUM_CODE)
_LETTER_CODE_RE = re.compile(r"\b[A-Z]{4,8}\b")      # counted only after a strong phrase


def _near(a, b, before, after):
    """True if span b starts within `after` characters after span a ends, or ends
    within `before` characters before span a starts."""
    return 0 <= b.start() - a.end() <= after or 0 <= a.start() - b.end() <= before


def is_referral(text):
    n, f = norm(text), fold(text)
    if re.search(r"ref(?:erral)?\s*id", n):
        return True
    # searched separately because they overlap: "nhap ma gioi thieu" holds both
    weak, strong = list(_WEAK_RE.finditer(n)), list(_STRONG_RE.finditer(n))
    codes = list(_CODE_RE.finditer(f))
    amounts = list(_AMOUNT_RE.finditer(n))
    letters = list(_LETTER_CODE_RE.finditer(f))
    for p in weak + strong:
        if any(_near(p, c, 25, 40) for c in codes) or any(_near(p, a, 0, 40) for a in amounts):
            return True
    for p in strong:
        if any(_near(p, c, 25, 25) for c in letters):
            return True
    for c in _NUM_CODE_RE.finditer(n):
        # "mã 680068", "mã: 680068", or the code glued to the word: "529004mã gt"
        if re.search(r"\bma\s*:?\s*$", n[:c.start()]) or re.match(r"\s*ma\b", n[c.end():]):
            return True
    # a code next to a reward with no phrase at all: "418422. nhạn 10k"
    return any(_near(c, a, 20, 20) for c in codes for a in amounts)


def spam_flag(text):
    n = norm(text)
    if LOAN_RE.search(n):
        return "loan_spam"
    if is_referral(text):
        return "referral_spam"
    return ""

# --------------------------------------------------------------- theme tagging
# Keywords are regular-expression fragments matched as whole words against
# norm(text), so "ung tien" no longer fires inside "dung tien". A syllable that
# collides with another once its tone marks are stripped is never used on its
# own: loi is lỗi, lời and lợi; lua is lừa, lựa and lúa; sap is sập and sắp;
# thuong is thưởng and thường. It enters either inside a longer phrase that is
# unambiguous without accents, or through ACCENTED, which is matched against
# the text with its tone marks intact.
#
# NOTE ON REPRODUCIBILITY. These keyword sets are a reconstruction of the ones
# used for the published figures, which were built interactively and not saved.
# The cleaning rules above are exact: re-running the September 2026 pull under
# the pre-revision rules reproduces the published cleaning log.
THEMES = {
    "onboarding": [r"dang k[yi]", r"xac thuc", r"xac minh", r"otp", r"nfc", r"cccd", r"cmnd",
                   r"can cuoc", r"chup (?:anh|hinh)", r"mo (?:tai khoan|tk)", r"duyet ho so",
                   r"ekyc"],
    "stability":  [r"(?:bi|hay|bao|gap|toan|nhieu|dang|sua|fix|khac phuc) loi(?! ich| nhuan| the)",
                   r"loi (?:he thong|dang nhap|app|lien tuc|hoai|suot)", r"app loi",
                   r"do may", r"bi do", r"(?:bi|app|may) treo", r"treo (?:may|app)", r"lag",
                   r"giat", r"(?:app|he thong|web|may) (?:bi )?sap", r"bi sap", r"sap app",
                   r"khong vao duoc", r"ko vao duoc", r"dang nhap", r"cham(?! soc)",
                   r"bao tri", r"mat ket noi"],
    "money":      [r"nap tien", r"rut tien", r"chuyen khoan", r"(?<!cai )tien ve", r"ung tien",
                   r"giam tien", r"khong nhan duoc tien", r"so du", r"tien khong vao"],
    "promo":      [r"khuyen mai", r"quang cao", r"(?:100|200|500)k", r"uu dai",
                   r"(?:nhan|tien|khen) thuong", r"qua tang", r"tang tien"],
    "fees":       [r"phi giao dich", r"mat phi", r"tinh phi", r"phi cao", r"hoa hong",
                   r"phi ruot", r"mien phi giao dich"],
    "fraud":      [r"lua dao", r"dao lua", r"bi lua", r"app lua", r"scam", r"danh gia ao",
                   r"gia mao", r"gian lan", r"bip", r"(?:lay|danh) cap thong tin",
                   r"(?:khong|ko) uy tin"],
    "closure":    [r"xoa tai khoan", r"xoa tk", r"huy tai khoan", r"dong tai khoan",
                   r"huy dang ky", r"huy hop dong", r"xoa hop dong"],
    "yield":      [r"khong ngu", r"sinh loi", r"lai suat", r"tien nhan roi"],
    "influencer": [r"youtube(?:r|rs)?", r"ytb", r"tiktok", r"bo va gau", r"tuber",
                   r"kenh (?:youtube|tiktok)", r"review app"],
    "zalopay":    [r"zalo ?pay"],
    "ui":         [r"giao dien", r"bieu do", r"chart", r"thiet ke", r"de dung", r"kho dung",
                   r"bo cuc", r"co chu", r"font"],
}
ACCENTED = {
    "stability": ["lỗi", "đơ", "sập app", "app sập", "bị sập"],
    "promo":     ["thưởng"],
    "fraud":     ["lừa"],
}
_THEME_RE = {t: re.compile(r"\b(?:" + "|".join(kws) + r")\b") for t, kws in THEMES.items()}
_ACCENTED_RE = {t: re.compile(r"\b(?:" + "|".join(kws) + r")\b") for t, kws in ACCENTED.items()}


def tag_themes(text):
    n, a = norm(text), accented(text)
    return [t for t in THEMES
            if _THEME_RE[t].search(n) or (t in _ACCENTED_RE and _ACCENTED_RE[t].search(a))]

# --------------------------------------------------------------- generic flag
GENERIC_MAX_WORDS = 1


def is_generic(text, themes):
    """A retained review of a single word carrying no theme: "tốt", "good", "ok".

    Counted separately rather than removed, so that a year full of one-word
    praise cannot be read as satisfaction. This is the rule behind the published
    figures (30.9 per cent of 2024's retained reviews against 13.2 per cent in
    2025). Earlier versions of this file said four words, which is not what was
    run. Vietnamese words are often two syllables ("tuyệt vời", "rất tốt"), so
    the sensitivity to a two-word rule is worth reporting alongside.
    """
    return (not themes) and len(str(text or "").split()) <= GENERIC_MAX_WORDS

# --------------------------------------------------------------- pipeline
DUPLICATE_MIN_CHARS = 20


def clean(rows):
    """rows: dicts with review_id, rating, date, thumbs_up, text and optionally author.

    Duplicates are copy-paste campaigns: the same text of at least
    DUPLICATE_MIN_CHARS alphanumeric characters, or the same text again from the
    same author. Short texts such as "good" or "tuyệt vời" recur because many
    people write them, so they are left in and handled by the generic flag.
    Rows are visited oldest first so that the earliest copy is the one kept.
    """
    seen, dupe = set(), {}
    for i in sorted(range(len(rows)), key=lambda i: str(rows[i].get("date", ""))):
        text = rows[i].get("text", "")
        if spam_flag(text):
            continue
        key = re.sub(r"[^a-z0-9]", "", norm(text))
        if len(key) < 4:
            continue
        ident = key if len(key) >= DUPLICATE_MIN_CHARS else (rows[i].get("author", ""), key)
        if ident in seen:
            dupe[i] = 1
        else:
            seen.add(ident)

    out = []
    for i, r in enumerate(rows):
        text = r.get("text", "")
        spam = spam_flag(text)
        themes = tag_themes(text)
        d = dupe.get(i, 0)
        out.append({
            "review_id": r.get("review_id", ""),
            "rating": int(r["rating"]),
            "date": str(r.get("date", ""))[:10],
            "thumbs_up": int(r.get("thumbs_up") or 0),
            "spam_flag": spam,
            "is_duplicate": d,
            "is_generic": int(is_generic(text, themes)),
            "themes": "|".join(themes),
            "keep": int(not spam and not d),
            "text": re.sub(r"[\r\n]+", " ", str(text or "")).strip(),
        })
    return out


def mean(xs):
    return round(sum(xs) / len(xs), 3) if xs else None


def aggregate(rows):
    kept = [r for r in rows if r["keep"]]
    by_year = defaultdict(list)
    for r in rows:
        by_year[r["date"][:4]].append(r)

    years = []
    for y in sorted(by_year):
        allr = by_year[y]
        k = [r for r in allr if r["keep"]]
        gen = [r for r in k if r["is_generic"]]
        sub = [r for r in k if not r["is_generic"]]
        years.append({
            "year": y, "retrieved": len(allr), "raw_mean": mean([r["rating"] for r in allr]),
            "removed": len(allr) - len(k),
            "removed_pct": round((len(allr) - len(k)) / len(allr) * 100, 1),
            "retained": len(k), "clean_mean": mean([r["rating"] for r in k]),
            "generic": len(gen),
            "generic_pct": round(len(gen) / len(k) * 100, 1) if k else None,
            "substantive": len(sub), "substantive_mean": mean([r["rating"] for r in sub]),
        })

    neg = [r for r in kept if r["rating"] <= 2]
    mid = [r for r in kept if r["rating"] == 3]
    pos = [r for r in kept if r["rating"] >= 4]

    def has(rs, t):
        return [r for r in rs if t in r["themes"].split("|")]

    themes = []
    for t in THEMES:
        themes.append({
            "theme": t, "neg": len(has(neg, t)), "mid": len(has(mid, t)), "pos": len(has(pos, t)),
            "all": len(has(kept, t)),
            "pct_of_negatives": round(len(has(neg, t)) / len(neg) * 100, 1) if neg else 0,
        })
    themes.sort(key=lambda x: -x["neg"])

    neg_by_year = []
    for y in sorted(by_year):
        ny = [r for r in neg if r["date"][:4] == y]
        neg_by_year.append([y, len(ny)] + [len(has(ny, t)) for t in THEMES])

    return {
        "totals": {
            "retrieved": len(rows),
            "loan_spam": sum(r["spam_flag"] == "loan_spam" for r in rows),
            "referral_spam": sum(r["spam_flag"] == "referral_spam" for r in rows),
            "duplicates": sum(r["is_duplicate"] for r in rows),
            "retained": len(kept),
            "raw_mean": mean([r["rating"] for r in rows]),
            "clean_mean": mean([r["rating"] for r in kept]),
            "removed_mean": mean([r["rating"] for r in rows if not r["keep"]]),
            "negative": len(neg), "neutral": len(mid), "positive": len(pos),
            "generic": sum(r["is_generic"] for r in kept),
            "substantive_mean": mean([r["rating"] for r in kept if not r["is_generic"]]),
            "pct_1_star": round(sum(r["rating"] == 1 for r in kept) / len(kept) * 100, 1) if kept else None,
            "pct_5_star": round(sum(r["rating"] == 5 for r in kept) / len(kept) * 100, 1) if kept else None,
        },
        "by_year": years,
        "themes": themes,
        "neg_by_year_header": ["year", "negative_n"] + list(THEMES),
        "neg_by_year": neg_by_year,
        "rating_histogram": {
            str(k): {"raw": sum(r["rating"] == k for r in rows),
                     "clean": sum(r["rating"] == k for r in kept)} for k in range(1, 6)
        },
    }

# --------------------------------------------------------------- self test
SELFTEST = [
    # the Unicode-obfuscated loan spam the NFKC pass is there to catch
    {"review_id": "t1", "rating": 5, "date": "2023-04-01", "thumbs_up": 0,
     "text": "Vo trang \U0001D5B5\U0001D5AE\U0001D5C4\U0001D5B3\U0001D5C8\U0001D5CD\U0001D5AD\U0001D5C1\U0001D5AE\U0001D5CD vay 0% nhan 590k free ngay"},
    # plain loan spam
    {"review_id": "t2", "rating": 5, "date": "2023-04-02", "thumbs_up": 0,
     "text": "Bạn hãy vào trang VayTotNhat.Com để vay tiền 0% lãi"},
    # referral farming
    {"review_id": "t3", "rating": 1, "date": "2026-09-20", "thumbs_up": 0,
     "text": "tải app nhập mã giới thiệu nhận 200k mã gt: 841094"},
    # genuine onboarding complaint
    {"review_id": "t4", "rating": 1, "date": "2025-04-17", "thumbs_up": 20,
     "text": "đăng ký xác thực 5 lần ko đc cứ bảo vì hình chụp bị mờ"},
    # genuine promo/fraud complaint
    {"review_id": "t5", "rating": 1, "date": "2025-06-28", "thumbs_up": 50,
     "text": "lừa đảo thông tin sai sự thật không có vụ được 100k liền đâu phải nạp tiền vào tối thiểu 2tr mới được"},
    # the praised idle-cash feature
    {"review_id": "t6", "rating": 4, "date": "2026-01-22", "thumbs_up": 0,
     "text": "tôi đang dùng về tiền không ngủ và sinh lời tự động quá tuyệt vời"},
    # generic one-word praise. Under four characters once normalised, so the
    # duplicate rule leaves it alone.
    {"review_id": "t7", "rating": 5, "date": "2024-05-05", "thumbs_up": 0, "text": "tốt"},
    {"review_id": "t8", "rating": 5, "date": "2024-05-06", "thumbs_up": 0, "text": "Tốt"},
    # a real duplicate: same text, different case and tone marks
    {"review_id": "t9",  "rating": 5, "date": "2024-06-01", "thumbs_up": 0,
     "text": "App dễ dùng, giao diện đơn giản thuận tiện"},
    {"review_id": "t10", "rating": 5, "date": "2024-06-02", "thumbs_up": 0,
     "text": "APP DE DUNG, GIAO DIEN DON GIAN THUAN TIEN"},
    # --- negative cases: each of these was misclassified before the revision
    {"review_id": "n1", "rating": 3, "date": "2025-01-01", "thumbs_up": 0,
     "text": "App tốt mà mọi người chê quá"},
    {"review_id": "n2", "rating": 1, "date": "2025-01-02", "thumbs_up": 0,
     "text": "Đăng nhập, bắt nhập mã OTP nhưng không bao giờ gửi"},
    {"review_id": "n3", "rating": 1, "date": "2025-01-03", "thumbs_up": 0,
     "text": "nạp 2000000 mà không vào tài khoản"},
    {"review_id": "n12", "rating": 1, "date": "2025-01-12", "thumbs_up": 0,
     "text": "nạp 500000 mà không thấy tiền về"},
    {"review_id": "n13", "rating": 1, "date": "2025-01-13", "thumbs_up": 0,
     "text": "chuyển 200000 rồi nhập mã OTP không được"},
    {"review_id": "n4", "rating": 1, "date": "2025-01-04", "thumbs_up": 0,
     "text": "suốt ngày hướng dẫn đăng nhập mật khẩu mới app cực hâm"},
    {"review_id": "n5", "rating": 4, "date": "2025-01-05", "thumbs_up": 0,
     "text": "Xem hướng dẫn tại dnse.com.vn rất dễ hiểu"},
    {"review_id": "n6", "rating": 5, "date": "2025-01-06", "thumbs_up": 0,
     "text": "Tiện lợi, lựa chọn tuyệt vời, cập nhật thường xuyên"},
    {"review_id": "n7", "rating": 5, "date": "2025-01-07", "thumbs_up": 0,
     "text": "dùng tiền dễ, mong cải tiến về tốc độ"},
    {"review_id": "n8", "rating": 1, "date": "2025-01-08", "thumbs_up": 0,
     "text": "app hay loi dang nhap hoai, lua dao"},
    {"review_id": "n9", "rating": 1, "date": "2025-01-09", "thumbs_up": 0,
     "text": "thằng bạn đưa mã giới thiệu app này rồi mà chả được ngàn nào"},
    {"review_id": "n10", "rating": 5, "date": "2025-01-10", "thumbs_up": 0,
     "text": "good", "author": "A"},
    {"review_id": "n11", "rating": 5, "date": "2025-01-11", "thumbs_up": 0,
     "text": "Good", "author": "B"},
    # --- referral farming the tightened rule must still catch
    {"review_id": "s1", "rating": 5, "date": "2025-02-01", "thumbs_up": 0,
     "text": "529004mã gt nhận 10k"},
    {"review_id": "s2", "rating": 1, "date": "2025-02-02", "thumbs_up": 0,
     "text": "Mã giới thiệu BBQK nhập mã nhận ưu đãi 6 tháng free phí"},
    {"review_id": "s3", "rating": 5, "date": "2025-02-03", "thumbs_up": 0,
     "text": "Mọi người mới tham gia app này nhập mã. 9 7 1 8 1 6 để nhận được 10.000đ nhé"},
    {"review_id": "s4", "rating": 5, "date": "2025-02-04", "thumbs_up": 0,
     "text": "Mã mời thêm 10k của mk là 450223"},
    # --- App Store farming: letter-and-digit codes, loose wording
    {"review_id": "s5", "rating": 5, "date": "2025-02-05", "thumbs_up": 0,
     "text": "Nhập Mã CRQDF7 và mua cổ phiếu để được nhận tiền mặt trị giá 300k"},
    {"review_id": "s6", "rating": 4, "date": "2025-02-06", "thumbs_up": 0,
     "text": "Mã giới thiệu cho người mới ạ. VU0216"},
    {"review_id": "s10", "rating": 5, "date": "2025-02-10", "thumbs_up": 0,
     "text": "Bạn nhập mã giới thiệu BGLN để được hỗ trợ nhé."},
    {"review_id": "s7", "rating": 5, "date": "2025-02-07", "thumbs_up": 0, "text": "418422. nhạn 10k"},
    {"review_id": "s8", "rating": 5, "date": "2025-02-08", "thumbs_up": 0,
     "text": "Mã nhận thưởng 757102. Mã nhận thưởng nha mọi người"},
    {"review_id": "s9", "rating": 5, "date": "2025-02-09", "thumbs_up": 0,
     "text": "Anh/Chị nhập ngay mã 680068 khi đăng ký để được tặng 1,000,000đ vào sức mua"},
    # --- and what must not be caught
    {"review_id": "n14", "rating": 1, "date": "2025-01-14", "thumbs_up": 0,
     "text": "NHẬP MÃ KHÔNG ĐƯỢC, APP LỖI SUỐT"},
    {"review_id": "n15", "rating": 5, "date": "2025-01-15", "thumbs_up": 0,
     "text": "Mùng 1 Tết rút khoản 888888 đồng về lấy lộc nhận được ngay"},
    {"review_id": "n16", "rating": 2, "date": "2025-01-16", "thumbs_up": 0,
     "text": "Mua CVHM2405 lãi 50k mà app báo lỗi, nhập mã VN30F1M cũng lag"},
]


def selftest():
    rows = clean(SELFTEST)
    got = {r["review_id"]: r for r in rows}
    th = {k: set(filter(None, r["themes"].split("|"))) for k, r in got.items()}
    checks = [
        ("t1 unicode loan spam caught",  got["t1"]["spam_flag"] == "loan_spam"),
        ("t2 plain loan spam caught",    got["t2"]["spam_flag"] == "loan_spam"),
        ("t3 referral spam caught",      got["t3"]["spam_flag"] == "referral_spam"),
        ("t4 kept",                      got["t4"]["keep"] == 1),
        ("t4 tagged onboarding",         "onboarding" in th["t4"]),
        ("t5 tagged fraud and promo",    {"fraud", "promo"} <= th["t5"]),
        ("t6 tagged yield only",         th["t6"] == {"yield"}),
        ("t7 flagged generic",           got["t7"]["is_generic"] == 1),
        ("t8 exempt, under four chars",  got["t8"]["is_duplicate"] == 0),
        ("t9 kept as first copy",        got["t9"]["is_duplicate"] == 0),
        ("t10 flagged duplicate of t9",  got["t10"]["is_duplicate"] == 1),
        ("n1 'mà mọi' is not spam",      got["n1"]["spam_flag"] == ""),
        ("n2 'nhập mã OTP' is not spam", got["n2"]["spam_flag"] == ""),
        ("n2 tagged onboarding",         "onboarding" in th["n2"]),
        ("n3 '2000000 mà' is not spam",  got["n3"]["spam_flag"] == ""),
        ("n4 'nhập mật khẩu' not spam",  got["n4"]["spam_flag"] == ""),
        ("n12 '500000 mà' is not spam",  got["n12"]["spam_flag"] == ""),
        ("n13 amount then 'nhập mã OTP'", got["n13"]["spam_flag"] == ""),
        ("n5 a URL is not loan spam",    got["n5"]["spam_flag"] == ""),
        ("n6 lợi/lựa/thường untagged",   not ({"stability", "fraud", "promo"} & th["n6"])),
        ("n7 dùng tiền/cải tiến untagged", "money" not in th["n7"]),
        ("n8 unaccented lỗi and lừa",    {"stability", "fraud"} <= th["n8"]),
        ("n9 complaint about referral kept", got["n9"]["spam_flag"] == ""),
        ("n11 same short text, other author, kept", got["n11"]["is_duplicate"] == 0),
        ("s1 code glued to mã",          got["s1"]["spam_flag"] == "referral_spam"),
        ("s2 letter code",               got["s2"]["spam_flag"] == "referral_spam"),
        ("s3 spaced digits",             got["s3"]["spam_flag"] == "referral_spam"),
        ("s4 mã mời with reward",        got["s4"]["spam_flag"] == "referral_spam"),
        ("s5 letter-digit code",         got["s5"]["spam_flag"] == "referral_spam"),
        ("s6 code a sentence after phrase", got["s6"]["spam_flag"] == "referral_spam"),
        ("s7 code and reward, no phrase", got["s7"]["spam_flag"] == "referral_spam"),
        ("s10 'nhập mã giới thiệu' + letters", got["s10"]["spam_flag"] == "referral_spam"),
        ("s8 mã nhận thưởng",            got["s8"]["spam_flag"] == "referral_spam"),
        ("s9 bare mã + code",            got["s9"]["spam_flag"] == "referral_spam"),
        ("n14 capitals rant not spam",   got["n14"]["spam_flag"] == ""),
        ("n15 888888 is not a code",     got["n15"]["spam_flag"] == ""),
        ("n16 warrant and VN30 codes",   got["n16"]["spam_flag"] == ""),
    ]
    ok = True
    for label, passed in checks:
        print(("  PASS  " if passed else "  FAIL  ") + label)
        ok &= passed
    agg = aggregate(rows)
    print(f"\n  retrieved {agg['totals']['retrieved']}, retained {agg['totals']['retained']}, "
          f"loan spam {agg['totals']['loan_spam']}, referral spam {agg['totals']['referral_spam']}, "
          f"duplicates {agg['totals']['duplicates']}")
    return ok


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        print("self test")
        sys.exit(0 if selftest() else 1)
    if len(sys.argv) < 2:
        sys.exit(__doc__)

    path = sys.argv[1]
    name = os.path.basename(path).replace("reviews_raw_", "").replace(".csv", "")
    # utf-8-sig: a CSV copied out of the browser or saved by Excel starts with a
    # byte-order mark, which would otherwise rename the first column silently.
    with open(path, encoding="utf-8-sig") as f:
        raw = list(csv.DictReader(f))
    if not raw:
        sys.exit(f"{path}: no rows")
    missing = {"review_id", "rating", "date", "text"} - set(raw[0])
    if missing:
        sys.exit(f"{path}: missing columns {sorted(missing)}")
    rows = clean(raw)
    agg = aggregate(rows)

    out_csv = os.path.join(os.path.dirname(os.path.abspath(path)), f"reviews_flagged_{name}.csv")
    with open(out_csv, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)

    out_json = out_csv.replace("reviews_flagged_", "reviews_summary_").replace(".csv", ".json")
    with open(out_json, "w", encoding="utf-8") as f:
        json.dump(agg, f, ensure_ascii=False, indent=2)

    t = agg["totals"]
    print(f"{name}: retrieved {t['retrieved']}, removed {t['retrieved']-t['retained']} "
          f"({t['loan_spam']} loan, {t['referral_spam']} referral, {t['duplicates']} duplicate), "
          f"retained {t['retained']}")
    print(f"  mean before {t['raw_mean']}, after {t['clean_mean']}, removed material {t['removed_mean']}")
    print(f"  wrote {out_csv}\n  wrote {out_json}")

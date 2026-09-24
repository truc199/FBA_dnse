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
    normalise -> flag loan spam -> flag referral spam -> drop duplicates
              -> flag generic one-word reviews -> tag themes -> aggregate

Nothing is deleted from the input file. Every row keeps its flags, so any
decision can be audited or reversed.

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
def norm(s):
    """Fold a review to a comparable form.

    NFKC first, which maps the mathematical alphanumeric characters spammers use
    back to plain letters. Then NFD with combining marks removed, which strips
    Vietnamese tone marks. Then the stroked d, which NFD does not decompose.
    Then lower case.
    """
    s = unicodedata.normalize("NFKC", str(s or ""))
    s = unicodedata.normalize("NFD", s)
    s = "".join(ch for ch in s if not unicodedata.combining(ch))
    s = s.replace("đ", "d").replace("Đ", "D")
    return s.lower()

# --------------------------------------------------------------- spam rules
LOAN_RE = re.compile(
    r"(vay\s*9|vaytotnhat|vay\s*t?o?t\s*nhat|ktien|vayhangdau|vay333|vayfe|"
    r"fbvay|c0m|\.com\b|vay\s*0\s*%|vay\s*von\s*0)", re.I)

REFERRAL_RE = re.compile(
    r"(ma\s*(gioi\s*thieu|gt|moi|dai\s*ly)|nhap\s*ma|ref(erral)?\s*id|"
    r"\bma\s*\d{5,}|\d{6}\s*(nhan|ma))", re.I)


def spam_flag(text):
    n = norm(text)
    if LOAN_RE.search(n):
        return "loan_spam"
    if REFERRAL_RE.search(n):
        return "referral_spam"
    return ""

# --------------------------------------------------------------- theme tagging
# Keywords are written unaccented because they are matched against norm(text).
#
# NOTE ON REPRODUCIBILITY. These keyword sets are a reconstruction of the ones
# used for the published figures, which were built interactively. Re-running this
# script will put the themes in the same rank order and within a few counts of
# the published table, but it will not reproduce it cell for cell. The cleaning
# rules above, and therefore every figure that depends only on them, are exact.
THEMES = {
    "onboarding": ["dang ky", "dang ki", "xac thuc", "xac minh", "otp", "nfc",
                   "cccd", "cmnd", "can cuoc", "chup anh", "chup hinh",
                   "mo tai khoan", "mo tk", "duyet ho so", "ekyc"],
    "stability":  ["loi", "do may", "bi do", "treo", "lag", "giat", "sap",
                   "khong vao duoc", "ko vao duoc", "dang nhap", "cham",
                   "bao tri", "mat ket noi", "khong dang nhap"],
    "money":      ["nap tien", "rut tien", "chuyen khoan", "tien ve", "ung tien",
                   "giam tien", "khong nhan duoc tien", "so du", "tien khong vao"],
    "promo":      ["khuyen mai", "quang cao", "100k", "200k", "500k",
                   "uu dai", "thuong", "qua tang", "tang tien"],
    "fees":       ["phi giao dich", "mat phi", "tinh phi", "phi cao", "hoa hong",
                   "phi ruot", "mien phi giao dich"],
    "fraud":      ["lua dao", "scam", "lua", "danh gia ao", "gia mao", "gian lan",
                   "bip", "lay cap thong tin", "khong uy tin"],
    "closure":    ["xoa tai khoan", "xoa tk", "huy tai khoan", "dong tai khoan",
                   "huy dang ky", "huy hop dong", "xoa hop dong"],
    "yield":      ["khong ngu", "sinh loi", "lai suat", "tien nhan roi"],
    "influencer": ["youtube", "ytb", "tiktok", "bo va gau", "tuber", "kenh",
                   "review app"],
    "zalopay":    ["zalopay", "zalo pay"],
    "ui":         ["giao dien", "bieu do", "chart", "thiet ke", "de dung",
                   "kho dung", "bo cuc", "co chu", "font"],
}


def tag_themes(text):
    n = norm(text)
    return [t for t, kws in THEMES.items() if any(k in n for k in kws)]

# --------------------------------------------------------------- generic flag
def is_generic(text, themes):
    """A retained review of four words or fewer carrying no theme.

    Counted separately rather than removed, so that a year full of one-word
    praise cannot be read as satisfaction. This flag is what exposed the 2024
    rating peak: 30.9 per cent of that year's retained reviews were generic,
    against 13.2 per cent in 2025.
    """
    return (not themes) and len(str(text or "").split()) <= 4

# --------------------------------------------------------------- pipeline
def clean(rows):
    """rows: dicts with review_id, rating, date, thumbs_up, text."""
    seen, out = set(), []
    for r in rows:
        text = r.get("text", "")
        spam = spam_flag(text)
        key = re.sub(r"[^a-z0-9]", "", norm(text))
        dupe = 0
        if not spam and len(key) >= 4:
            if key in seen:
                dupe = 1
            else:
                seen.add(key)
        themes = tag_themes(text)
        out.append({
            "review_id": r.get("review_id", ""),
            "rating": int(r["rating"]),
            "date": str(r.get("date", ""))[:10],
            "thumbs_up": int(r.get("thumbs_up") or 0),
            "spam_flag": spam,
            "is_duplicate": dupe,
            "is_generic": int(is_generic(text, themes)),
            "themes": "|".join(themes),
            "keep": int(not spam and not dupe),
            "text": str(text or "").replace("\n", " ").strip(),
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
    themes = []
    for t in THEMES:
        has = lambda rs: [r for r in rs if t in r["themes"].split("|")]
        themes.append({
            "theme": t, "neg": len(has(neg)), "mid": len(has(mid)), "pos": len(has(pos)),
            "all": len(has(kept)),
            "pct_of_negatives": round(len(has(neg)) / len(neg) * 100, 1) if neg else 0,
        })
    themes.sort(key=lambda x: -x["neg"])

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
        },
        "by_year": years,
        "themes": themes,
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
    # duplicate rule deliberately leaves it alone.
    {"review_id": "t7", "rating": 5, "date": "2024-05-05", "thumbs_up": 0, "text": "tốt"},
    {"review_id": "t8", "rating": 5, "date": "2024-05-06", "thumbs_up": 0, "text": "Tốt"},
    # a real duplicate: same text, different case and tone marks
    {"review_id": "t9",  "rating": 5, "date": "2024-06-01", "thumbs_up": 0,
     "text": "App dễ dùng, giao diện đơn giản thuận tiện"},
    {"review_id": "t10", "rating": 5, "date": "2024-06-02", "thumbs_up": 0,
     "text": "APP DE DUNG, GIAO DIEN DON GIAN THUAN TIEN"},
]


def selftest():
    rows = clean(SELFTEST)
    got = {r["review_id"]: r for r in rows}
    checks = [
        ("t1 unicode loan spam caught",  got["t1"]["spam_flag"] == "loan_spam"),
        ("t2 plain loan spam caught",    got["t2"]["spam_flag"] == "loan_spam"),
        ("t3 referral spam caught",      got["t3"]["spam_flag"] == "referral_spam"),
        ("t4 kept",                      got["t4"]["keep"] == 1),
        ("t4 tagged onboarding",         "onboarding" in got["t4"]["themes"]),
        ("t5 tagged fraud and promo",    {"fraud", "promo"} <= set(got["t5"]["themes"].split("|"))),
        ("t6 tagged yield",              "yield" in got["t6"]["themes"]),
        ("t7 flagged generic",           got["t7"]["is_generic"] == 1),
        ("t8 exempt, under four chars",  got["t8"]["is_duplicate"] == 0),
        ("t9 kept as first copy",        got["t9"]["is_duplicate"] == 0),
        ("t10 flagged duplicate of t9",  got["t10"]["is_duplicate"] == 1),
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
    with open(path, encoding="utf-8") as f:
        raw = list(csv.DictReader(f))
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

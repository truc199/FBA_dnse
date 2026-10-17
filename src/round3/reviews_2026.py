"""Causes behind DNSE's negative app reviews of 2026, coded by reading each review.

Selection: cleaned reviews (keep = 1) rated 1 or 2 stars, dated 1 January to 21 September 2026, on Google
Play (34) and the App Store (24). The causes were coded by hand, not by keyword, and a review can carry
several; the codes and an English gist are in data/round3/reviews_2026_coding.csv, translated quotations
in data/round3/reviews_2026_quotes.csv. This script joins them to the review files, checks that every
selected review is coded, and writes outputs/round3/tables/reviews_2026_*.csv.

Run: python src/round3/reviews_2026.py
"""
import csv
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from config import DATA  # noqa: E402
from payday_model import DATA_R3, TABLES_R3  # noqa: E402

WINDOW = ("2026-01-01", "2026-09-21")
STORES = [("play", "Google Play", DATA / "reviews_flagged_vn.com.encapital.arrow.csv"),
          ("ios", "App Store", DATA / "reviews_flagged_ios_vn.com.encapital.arrow.csv")]
RAW_IOS = DATA / "reviews_raw_ios_vn.com.encapital.arrow.csv"
CAUSES = [
    ("login_otp", "Login, OTP and authentication"),
    ("cash_not_credited", "Deposits or withdrawals not credited"),
    ("orders_prices", "Orders, prices and settlement"),
    ("crash_freeze", "Crashes, freezes and lag"),
    ("ekyc_opening", "eKYC and account opening"),
    ("fees_terms", "Fees and terms (closure, auto-renewal)"),
    ("scam_reward", "Scam claims and rewards"),
    ("other", "Other (service, interface, Ensa, no reason)"),
]
LABEL = dict(CAUSES)
BROKE = {"login_otp", "cash_not_credited", "orders_prices", "crash_freeze", "ekyc_opening"}
TERMS = {"fees_terms", "scam_reward"}
MONEY_PATH = {"login_otp", "cash_not_credited"}
# Round 2 keyword themes (src/analysis.py): reliability = stability or onboarding; trust = fraud, promo or closure
KW_RELIABILITY, KW_TRUST = {"stability", "onboarding"}, {"fraud", "promo", "closure"}


def read(path):
    with open(path, encoding="utf-8-sig") as f:
        return list(csv.DictReader(f))


def write(name, rows):
    TABLES_R3.mkdir(parents=True, exist_ok=True)
    with open(TABLES_R3 / name, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0]))
        w.writeheader()
        w.writerows(rows)
    print(f"  wrote outputs/round3/tables/{name} ({len(rows)} rows)")


def pct(a, b):
    return round(a / b * 100, 1) if b else 0.0


def wilson(k, n, z=1.96):
    """95% Wilson interval of a share k / n, in per cent (low, high)."""
    if not n:
        return "", ""
    p = k / n
    centre = (p + z * z / (2 * n)) / (1 + z * z / n)
    half = z * ((p * (1 - p) / n + z * z / (4 * n * n)) ** 0.5) / (1 + z * z / n)
    return round((centre - half) * 100, 1), round((centre + half) * 100, 1)


def selected():
    version = {r["review_id"]: r["version"] for r in read(RAW_IOS)}
    out = []
    for store, store_label, path in STORES:
        for r in read(path):
            if r["keep"] == "1" and int(r["rating"]) <= 2 and WINDOW[0] <= r["date"] <= WINDOW[1]:
                out.append({**r, "store": store, "store_label": store_label,
                            "app_version": version.get(r["review_id"], "") if store == "ios" else ""})
    return sorted(out, key=lambda r: (r["store"], r["date"], r["review_id"]))


def main():
    reviews = selected()
    coding = {r["review_id"]: r for r in read(DATA_R3 / "reviews_2026_coding.csv")}
    quotes = read(DATA_R3 / "reviews_2026_quotes.csv")
    missing = [r["review_id"] for r in reviews if r["review_id"] not in coding]
    extra = sorted(set(coding) - {r["review_id"] for r in reviews})
    if missing or extra:
        sys.exit(f"coding does not match the selection: uncoded {missing}, not selected {extra}")
    for c in coding.values():
        bad = [k for k in c["causes"].split("|") + [c["primary"]] if k not in LABEL]
        if bad or c["primary"] not in c["causes"].split("|"):
            sys.exit(f"bad codes for {c['review_id']}: {bad or c['primary']}")

    rows = []
    for r in reviews:
        c = coding[r["review_id"]]
        rows.append({"store": r["store_label"], "review_id": r["review_id"], "date": r["date"],
                     "month": r["date"][:7], "stars": r["rating"], "helpful_votes": r["thumbs_up"],
                     "app_version": r["app_version"], "causes": c["causes"], "primary_cause": c["primary"],
                     "after_update": c["after_update"], "outage_4_5_march": c["outage_4_5_march"],
                     "keyword_themes_round2": r["themes"], "gist_en": c["gist_en"], "note": c["note"],
                     "text_vi": r["text"]})
    write("reviews_2026_causes.csv", rows)

    n = {s: sum(r["store"] == lab for r in rows) for s, lab, _ in STORES}
    n["both"] = len(rows)

    def count(pred, store=None):
        return sum(1 for r in rows if (store is None or r["store"] == store) and pred(r))

    store_label = {s: lab for s, lab, _ in STORES}
    summary = []
    for key, label in CAUSES:
        has = lambda r, k=key: k in r["causes"].split("|")  # noqa: E731
        prim = lambda r, k=key: r["primary_cause"] == k  # noqa: E731
        summary.append({
            "cause": label, "code": key,
            "google_play_n": count(has, store_label["play"]), "google_play_pct": pct(count(has, store_label["play"]), n["play"]),
            "app_store_n": count(has, store_label["ios"]), "app_store_pct": pct(count(has, store_label["ios"]), n["ios"]),
            "both_n": count(has), "both_pct": pct(count(has), n["both"]),
            "both_ci95_low": wilson(count(has), n["both"])[0], "both_ci95_high": wilson(count(has), n["both"])[1],
            "primary_n": count(prim), "primary_pct": pct(count(prim), n["both"]),
        })
    groups = [("Something broke (any of the first five causes)", lambda r: bool(set(r["causes"].split("|")) & BROKE)),
              ("Fees, terms, scam claims or rewards", lambda r: bool(set(r["causes"].split("|")) & TERMS)),
              ("Login/OTP failures or money not credited",
               lambda r: bool(set(r["causes"].split("|")) & MONEY_PATH)),
              ("Posted 4-5 March 2026, after the outage DNSE disclosed for 4 March", lambda r: r["outage_4_5_march"] == "1"),
              ("Blames an app update", lambda r: r["after_update"] == "1")]
    for label, f in groups:
        summary.append({"cause": label, "code": "group",
                        "google_play_n": count(f, store_label["play"]), "google_play_pct": pct(count(f, store_label["play"]), n["play"]),
                        "app_store_n": count(f, store_label["ios"]), "app_store_pct": pct(count(f, store_label["ios"]), n["ios"]),
                        "both_n": count(f), "both_pct": pct(count(f), n["both"]),
                        "both_ci95_low": wilson(count(f), n["both"])[0], "both_ci95_high": wilson(count(f), n["both"])[1],
                        "primary_n": "", "primary_pct": ""})
    summary.append({"cause": "Negative reviews coded", "code": "n", "google_play_n": n["play"], "google_play_pct": 100.0,
                    "app_store_n": n["ios"], "app_store_pct": 100.0, "both_n": n["both"], "both_pct": 100.0,
                    "both_ci95_low": "", "both_ci95_high": "", "primary_n": n["both"], "primary_pct": 100.0})
    write("reviews_2026_cause_summary.csv", summary)

    # Keyword themes of Round 2 against hand coding, same reviews
    def kw(r, keys):
        return bool(set(t for t in r["keyword_themes_round2"].split("|") if t) & keys)
    comp = []
    for store in [store_label["play"], store_label["ios"], None]:
        sub = [r for r in rows if store is None or r["store"] == store]
        comp.append({
            "store": store or "Both stores", "negative_reviews": len(sub),
            "reliability_keyword_pct": pct(sum(kw(r, KW_RELIABILITY) for r in sub), len(sub)),
            "reliability_hand_pct": pct(sum(bool(set(r["causes"].split("|")) & (BROKE - {"cash_not_credited"}))
                                            for r in sub), len(sub)),
            "something_broke_hand_pct": pct(sum(bool(set(r["causes"].split("|")) & BROKE) for r in sub), len(sub)),
            "trust_keyword_pct": pct(sum(kw(r, KW_TRUST) for r in sub), len(sub)),
            "trust_hand_pct": pct(sum(bool(set(r["causes"].split("|")) & TERMS) for r in sub), len(sub)),
        })
    write("reviews_2026_keyword_vs_hand.csv", comp)

    by_month = []
    for m in sorted({r["month"] for r in rows}):
        sub = [r for r in rows if r["month"] == m]
        by_month.append({"month": m,
                         "google_play": sum(r["store"] == store_label["play"] for r in sub),
                         "app_store": sum(r["store"] == store_label["ios"] for r in sub),
                         "total": len(sub),
                         "something_broke": sum(bool(set(r["causes"].split("|")) & BROKE) for r in sub),
                         "outage_4_5_march": sum(r["outage_4_5_march"] == "1" for r in sub)})
    write("reviews_2026_by_month.csv", by_month)

    ios_rows = [r for r in rows if r["store"] == store_label["ios"]]
    fam = Counter(".".join(r["app_version"].split(".")[:2]) for r in ios_rows)
    by_version = [{"version_family": f"{k}.x", "negative_reviews": v,
                   "first_review": min(r["date"] for r in ios_rows if r["app_version"].startswith(k + ".")),
                   "last_review": max(r["date"] for r in ios_rows if r["app_version"].startswith(k + "."))}
                  for k, v in sorted(fam.items(), key=lambda kv: [int(x) for x in kv[0].split(".")])]
    by_version.append({"version_family": "2.113.28 alone", "negative_reviews": sum(r["app_version"] == "2.113.28" for r in ios_rows),
                       "first_review": min(r["date"] for r in ios_rows if r["app_version"] == "2.113.28"),
                       "last_review": max(r["date"] for r in ios_rows if r["app_version"] == "2.113.28")})
    write("reviews_2026_ios_versions.csv", by_version)

    by_id = {r["review_id"]: r for r in rows}
    qrows = []
    for q in quotes:
        r = by_id[q["review_id"]]
        ver = f", version {r['app_version']}" if r["app_version"] else ""
        qrows.append({"use": q["use"], "store": r["store"], "date": r["date"], "stars": r["stars"],
                      "app_version": r["app_version"], "causes": r["causes"],
                      "quote_en": q["translation_en"], "original_vi": r["text_vi"],
                      "attribution": f"{r['store']} review, {r['stars']} star, {r['date']}{ver}; authors' translation"})
    write("reviews_2026_quotes.csv", qrows)

    print(f"  {n['both']} negative reviews coded (Google Play {n['play']}, App Store {n['ios']})")
    for s in summary:
        print(f"    {s['cause'][:52]:52s} Play {s['google_play_n']:>2} ({s['google_play_pct']:>5}%)  "
              f"iOS {s['app_store_n']:>2} ({s['app_store_pct']:>5}%)  both {s['both_n']:>2} ({s['both_pct']:>5}%)")
    for c in comp:
        print(f"    {c['store']}: reliability keyword {c['reliability_keyword_pct']}% vs hand {c['reliability_hand_pct']}%; "
              f"trust keyword {c['trust_keyword_pct']}% vs hand {c['trust_hand_pct']}%")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
03b -- Build the review tables used in the report from the raw Google Play and App Store
pulls, with the cleaning and tagging rules in 03_reviews_clean.py.

The tables are written twice: as reviews_tables.json, which src/analysis.py reads for the
charts and tables, and as reviews.py, a Python module with the same content. Every number
in them can be reproduced from the raw CSVs.

Inputs (written by 02b and 02c, in data/)
    reviews_raw_vn.com.encapital.arrow.csv   DNSE, full history
    reviews_raw_vn.com.vpbs.smartone.csv     VPS, cut to its VPS_LIMIT most recent reviews
    reviews_raw_com.fpts.eztrade.csv         FPTS, full history
    reviews_raw_ios_<package>.csv            App Store, whatever the feed served (optional)
    appstore_meta.json                       App Store star-rating counts (optional)
Every app is cut at CUTOFF so that a later pull compares like with like. The App Store
tables compare the two stores from WINDOW_START to CUTOFF.

Output
    reviews_tables.json         the review tables, read by src/analysis.py
    reviews.py                  the same tables as a Python module
    reviews_flagged_<pkg>.csv   every row used, with its flags, for audit

Run
    python3 src/pipeline/03b_reviews_tables.py
"""
import csv
import datetime
import importlib
import json
import os
import sys

import sys as _sys, os as _os
_sys.path.insert(0, _os.path.dirname(_os.path.abspath(__file__)))
from paths import DATA, SCRIPT_DIR  # all data files live in <repo>/data
_HERE = DATA
sys.path.insert(0, SCRIPT_DIR)
C = importlib.import_module("03_reviews_clean")

CUTOFF = "2026-09-21"      # last day of the original collection
VPS_LIMIT = 1200           # the published comparison used VPS's 1,200 most recent reviews
WINDOW_START = "2025-01-01"  # the Google Play / App Store comparison covers 2025 and 2026,
                             # the years every one of the six series covers
APPS = [
    ("DNSE Entrade X", "vn.com.encapital.arrow", None),
    ("VPS SmartOne",   "vn.com.vpbs.smartone",   VPS_LIMIT),
    ("FPTS EzTrade",   "com.fpts.eztrade",       None),
]

THEME_LABEL = {
    "onboarding": "Account opening, eKYC, OTP, NFC identity capture",
    "stability":  "App crashes, freezes, login failures, slow order routing",
    "money":      "Deposits not credited, withdrawal delays, T+ settlement",
    "promo":      "Sign-up bonus terms, advertised rewards not received",
    "fees":       "Commission and charges differing from the advertised rate",
    "fraud":      "Explicit accusation of deception or fake reviews",
    "closure":    "Cannot close the account, closure fee",
    "yield":      "Idle-cash auto-earning feature (tai khoan khong ngu)",
    "influencer": "Reached the app through a YouTube or social referral",
    "zalopay":    "ZaloPay linkage and its transaction charge",
    "ui":         "Interface, charts, layout, usability",
}

# The fifty reviews kept for quotation (Table D3 quotes a selection): the most upvoted within each complaint
# theme plus the most upvoted substantive positive reviews, chosen from the original
# pull. Ratings, votes and theme tags are refreshed from the current pull.
QUOTE_IDS = [
    "cf18775a", "e8fe4927", "5efad1d8", "e752ae28", "ec7cd283", "91029c97", "f95e155b",
    "d7b0e147", "4b62d195", "975c8060", "564355fd", "940c13ed", "0a2388c6", "e74d3efa",
    "811c5661", "0db61d25", "0318e923", "276fb209", "f07f6887", "e6b00c91", "92b7466a",
    "ee1f33ca", "d63fde57", "023d90b3", "ba551fd3", "9d0f25ad", "2513906a", "bf576f62",
    "0fa0a9f4", "6e881a12", "b2970aa5", "3217d538", "523d5f8f", "658a04b9", "db32d5d4",
    "31147446", "d2094e6d", "042dbd9d", "248db681", "209c03a4", "fa30782f", "4094bad4",
    "06c66fa6", "a018878c", "3098e894", "5529fbb6", "10f974fe", "d3a9f078", "2683adda",
    "1e200051",
]


def load(package, limit, prefix=""):
    path = os.path.join(_HERE, f"reviews_raw_{prefix}{package}.csv")
    with open(path, encoding="utf-8-sig") as f:
        rows = [r for r in csv.DictReader(f) if r["date"] <= CUTOFF]
    rows.sort(key=lambda r: r["date"], reverse=True)          # newest first, as pulled
    if limit:
        rows = rows[:limit]
    pulled = datetime.date.fromtimestamp(os.path.getmtime(path)).isoformat()
    return rows, pulled


def year_stats(agg, year):
    for y in agg["by_year"]:
        if y["year"] == year:
            return y["retained"], y["clean_mean"]
    return 0, None


def generic_sensitivity(flagged):
    """Share of retained reviews flagged generic, and the mean of the rest, by year,
    under one-, two- and four-word rules."""
    kept = [r for r in flagged if r["keep"]]
    out = []
    for y in sorted({r["date"][:4] for r in kept}):
        k = [r for r in kept if r["date"][:4] == y]
        row = [y, len(k)]
        for words in (1, 2, 4):
            gen = [r for r in k if not r["themes"] and len(r["text"].split()) <= words]
            sub = [r["rating"] for r in k if r not in gen]
            row += [round(len(gen) / len(k) * 100, 1), C.mean(sub)]
        out.append(row)
    return out


# Theme groups for the store comparison. A review can carry both themes of a group, so a
# group is counted once per review rather than by adding the two theme shares.
THEME_GROUPS = {"product": ("stability", "onboarding"), "promotion": ("fraud", "promo")}


def window_stats(flagged, start=WINDOW_START):
    """Retained reviews dated from `start`: count, mean, one-star share, and for the
    one- and two-star reviews the count carrying each theme and each theme group."""
    kept = [r for r in flagged if r["keep"] and r["date"] >= start]
    neg = [r for r in kept if r["rating"] <= 2]
    tags = [set(r["themes"].split("|")) for r in neg]
    return {
        "n": len(kept), "mean": C.mean([r["rating"] for r in kept]),
        "pct_1_star": round(sum(r["rating"] == 1 for r in kept) / len(kept) * 100, 1) if kept else None,
        "negative": len(neg),
        "themes": {t: sum(t in s for s in tags) for t in C.THEMES},
        "groups": {g: sum(bool(set(ts) & s) for s in tags) for g, ts in THEME_GROUPS.items()},
    }


def write_flagged(name, flagged):
    """The audit file holds exactly the rows behind the tables (for VPS, the cut)."""
    with open(os.path.join(_HERE, f"reviews_flagged_{name}.csv"), "w", newline="",
              encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(flagged[0].keys()))
        w.writeheader()
        w.writerows(flagged)


def main():
    results = {}
    for app, package, limit in APPS:
        raw, pulled = load(package, limit)
        flagged = C.clean(raw)
        results[package] = (app, raw, pulled, flagged, C.aggregate(flagged))
        write_flagged(package, flagged)

    # App Store pulls from 02c: same rules, no cut beyond CUTOFF (the feed is short anyway)
    ios = {}
    meta_path = os.path.join(_HERE, "appstore_meta.json")
    meta = json.load(open(meta_path, encoding="utf-8")) if os.path.exists(meta_path) else {"apps": {}}
    for app, package, _ in APPS:
        if not os.path.exists(os.path.join(_HERE, f"reviews_raw_ios_{package}.csv")):
            continue
        raw, pulled = load(package, None, prefix="ios_")
        flagged = C.clean(raw)
        ios[package] = (app, raw, pulled, flagged, C.aggregate(flagged))
        write_flagged(f"ios_{package}", flagged)

    app, raw, pulled, flagged, agg = results["vn.com.encapital.arrow"]
    t = agg["totals"]
    dnse_totals = {
        "raw_n": t["retrieved"], "loan_spam": t["loan_spam"], "referral_spam": t["referral_spam"],
        "duplicates": t["duplicates"], "clean_n": t["retained"], "raw_mean": t["raw_mean"],
        "clean_mean": t["clean_mean"], "removed_mean": t["removed_mean"],
        "negative_1_2": t["negative"], "neutral_3": t["neutral"], "positive_4_5": t["positive"],
        "generic_in_clean": t["generic"], "substantive_mean": t["substantive_mean"],
        "first_date": min(r["date"] for r in raw), "last_date": max(r["date"] for r in raw),
        "pulled": pulled, "cutoff": CUTOFF,
    }
    rating_hist = [(int(k), v["raw"], v["clean"]) for k, v in agg["rating_histogram"].items()]
    year_tab = [[y["year"], y["retrieved"], y["raw_mean"], y["removed"], y["removed_pct"],
                 y["retained"], y["clean_mean"], y["generic"], y["generic_pct"],
                 y["substantive"], y["substantive_mean"]] for y in agg["by_year"]]
    by_theme = {x["theme"]: x for x in agg["themes"]}
    theme_tab = [[th, by_theme[th]["neg"], by_theme[th]["mid"], by_theme[th]["pos"],
                  by_theme[th]["all"], by_theme[th]["pct_of_negatives"]] for th in C.THEMES]
    neg_year = agg["neg_by_year"]
    sensitivity = generic_sensitivity(flagged)

    cleaning_log = []
    for app_name, package, limit in APPS:
        tt = results[package][4]["totals"]
        cleaning_log.append([app_name, tt["retrieved"], tt["loan_spam"], tt["referral_spam"],
                             tt["duplicates"], tt["retained"], tt["raw_mean"], tt["clean_mean"],
                             tt["removed_mean"]])

    peers = []
    for app_name, package, limit in APPS:
        _, raw_p, _, _, a = results[package]
        tt = a["totals"]
        row = [app_name, package, tt["retrieved"], tt["retained"],
               round((tt["retrieved"] - tt["retained"]) / tt["retrieved"] * 100, 1),
               tt["raw_mean"], tt["clean_mean"]]
        for y in ("2024", "2025", "2026"):
            row += list(year_stats(a, y))
        row += [tt["pct_1_star"], tt["pct_5_star"]]
        peers.append(row)
    vps_raw = results["vn.com.vpbs.smartone"][1]
    vps_span = (min(r["date"] for r in vps_raw), max(r["date"] for r in vps_raw))

    by_prefix = {r["review_id"][:8]: r for r in flagged}
    quotes, missing = [], []
    for qid in QUOTE_IDS:
        r = by_prefix.get(qid)
        if r is None:
            missing.append(qid)
            continue
        quotes.append([qid, r["rating"], r["date"], r["thumbs_up"], r["themes"], r["text"][:150]])

    # ---------------------------------------------- App Store cross-check
    ios_log, store_compare, store_themes, store_negatives, ios_dnse_year = [], [], [], [0, 0], []
    store_groups = {}
    for app_name, package, _ in APPS:
        if package not in ios:
            continue
        _, raw_i, _, flagged_i, a = ios[package]
        tt, m = a["totals"], meta["apps"].get(package, {})
        ios_log.append([app_name, tt["retrieved"], tt["loan_spam"], tt["referral_spam"], tt["duplicates"],
                        tt["retained"], tt["raw_mean"], tt["clean_mean"], tt["removed_mean"],
                        min(r["date"] for r in raw_i), max(r["date"] for r in raw_i),
                        m.get("rating_count"),
                        round(m["rating_average"], 2) if m.get("rating_average") else None])
        wp, wi = window_stats(results[package][3]), window_stats(flagged_i)
        store_compare.append([app_name, wp["n"], wp["mean"], wp["pct_1_star"],
                              wi["n"], wi["mean"], wi["pct_1_star"]])
        if package == "vn.com.encapital.arrow":
            store_negatives = [wp["negative"], wi["negative"]]
            both = wp["negative"] + wi["negative"]
            for th in C.THEMES:
                p_, i_ = wp["themes"][th], wi["themes"][th]
                store_themes.append([th, p_, round(p_ / wp["negative"] * 100, 1) if wp["negative"] else None,
                                     i_, round(i_ / wi["negative"] * 100, 1) if wi["negative"] else None,
                                     p_ + i_, round((p_ + i_) / both * 100, 1) if both else None])
            store_themes.sort(key=lambda r: -r[5])
            store_groups = {g: [wp["groups"][g], round(wp["groups"][g] / wp["negative"] * 100, 1),
                                wi["groups"][g], round(wi["groups"][g] / wi["negative"] * 100, 1)]
                            for g in THEME_GROUPS}
            ios_dnse_year = [[y["year"], y["retrieved"], y["retained"], y["clean_mean"]] for y in a["by_year"]]

    tables = {
        "DNSE_TOTALS": dnse_totals, "RATING_HIST": rating_hist,
        "YEAR_HEADER": ["year", "raw_n", "raw_mean", "removed_n", "removed_pct", "clean_n",
                        "clean_mean", "generic_n", "generic_pct", "substantive_n", "substantive_mean"],
        "YEAR_TAB": year_tab, "THEMES": list(C.THEMES), "THEME_LABEL": THEME_LABEL,
        "THEME_HEADER": ["theme", "neg_1_2", "neutral_3", "pos_4_5", "all_clean", "pct_of_negatives"],
        "THEME_TAB": theme_tab,
        "NEG_YEAR_HEADER": ["year", "negative_n"] + list(C.THEMES), "NEG_YEAR": neg_year,
        "GENERIC_SENSITIVITY_HEADER": ["year", "retained_n", "pct_1w", "subst_mean_1w",
                                       "pct_2w", "subst_mean_2w", "pct_4w", "subst_mean_4w"],
        "GENERIC_SENSITIVITY": sensitivity,
        "PEER_HEADER": ["app", "package", "raw_n", "clean_n", "removed_pct", "raw_mean",
                        "clean_mean", "n_2024", "mean_2024", "n_2025", "mean_2025",
                        "n_2026", "mean_2026", "pct_1_star", "pct_5_star"],
        "PEERS": peers, "VPS_SPAN": vps_span,
        "CLEANING_HEADER": ["app", "retrieved", "loan_spam", "referral_spam", "duplicates",
                            "retained", "raw_mean", "clean_mean", "removed_mean"],
        "CLEANING_LOG": cleaning_log, "CUTOFF": CUTOFF,
        "QUOTE_HEADER": ["review_id", "rating", "date", "thumbs_up", "themes", "text"],
        "QUOTES": quotes,
        "APPSTORE_PULLED": meta.get("pulled"),
        "IOS_CLEANING_HEADER": ["app", "retrieved", "loan_spam", "referral_spam", "duplicates", "retained",
                                "raw_mean", "clean_mean", "removed_mean", "first_date", "last_date",
                                "store_rating_count", "store_rating_average"],
        "IOS_CLEANING_LOG": ios_log,
        "IOS_DNSE_YEAR_HEADER": ["year", "retrieved", "retained", "clean_mean"],
        "IOS_DNSE_YEAR": ios_dnse_year,
        "STORE_WINDOW": [WINDOW_START, CUTOFF],
        "STORE_COMPARE_HEADER": ["app", "play_n", "play_mean", "play_pct_1_star",
                                 "ios_n", "ios_mean", "ios_pct_1_star"],
        "STORE_COMPARE": store_compare,
        "STORE_NEGATIVES": store_negatives,
        "STORE_THEME_HEADER": ["theme", "play_neg", "play_pct", "ios_neg", "ios_pct", "both_neg", "both_pct"],
        "STORE_THEMES": store_themes,
        "STORE_GROUP_DEF": {g: list(ts) for g, ts in THEME_GROUPS.items()},
        "STORE_GROUP_HEADER": ["play_neg", "play_pct", "ios_neg", "ios_pct"],
        "STORE_GROUPS": store_groups,
    }

    with open(os.path.join(_HERE, "reviews_tables.json"), "w", encoding="utf-8") as f:
        json.dump(tables, f, ensure_ascii=False, indent=1)
    with open(os.path.join(_HERE, "reviews.py"), "w", encoding="utf-8", newline="\n") as f:
        f.write(render(tables))

    print(f"DNSE: {t['retrieved']} retrieved, {t['loan_spam']} loan, {t['referral_spam']} referral, "
          f"{t['duplicates']} duplicate, {t['retained']} retained; mean {t['raw_mean']} -> {t['clean_mean']}")
    for p in peers:
        print(f"  {p[0]:15s} {p[2]:5d} -> {p[3]:5d}  mean {p[5]} -> {p[6]}")
    for r in ios_log:
        print(f"  App Store {r[0]:15s} {r[1]:5d} -> {r[5]:5d}  mean {r[6]} -> {r[7]}  ({r[9]} to {r[10]})")
    print(f"quotes {len(quotes)}/{len(QUOTE_IDS)}" + (f", missing {missing}" if missing else ""))
    print("wrote reviews.py and reviews_tables.json")


def render(t):
    d = t["DNSE_TOTALS"]
    vps_from, vps_to = t["VPS_SPAN"]

    def block(name, rows):
        return f"{name} = [\n" + "".join(f"    {r!r},\n" for r in rows) + "]\n"

    return f'''# -*- coding: utf-8 -*-
# GENERATED by 03b_reviews_tables.py. Do not edit by hand; re-run 03b instead.
"""Google Play review dataset for DNSE Entrade X and two peer broker apps.

Collection method
-----------------
Source: Google Play public review listing, pulled with 02b_playstore_scrape_python.py
(file date {d["pulled"]}) and cut at {CUTOFF}. No authentication, no private data. Fields
captured per review: review id, author display name, star rating, free text, date,
thumbs-up count.

Apps
  vn.com.encapital.arrow  DNSE Entrade X  {t["PEERS"][0][2]:>5,} reviews, full available history ({d["first_date"][:4]}-{d["last_date"][:4]})
  vn.com.vpbs.smartone    VPS SmartOne    {t["PEERS"][1][2]:>5,} reviews, the most recent {VPS_LIMIT:,} ({vps_from} to {vps_to});
                                                the listing itself goes back further
  com.fpts.eztrade        FPTS EzTrade    {t["PEERS"][2][2]:>5,} reviews, full available history
  App Store, Vietnam      the same three apps, written reviews served by Apple's public feed
                          (pulled {t["APPSTORE_PULLED"]}), used as a cross-check for {t["STORE_WINDOW"][0][:4]}-{t["STORE_WINDOW"][1][:4]}

Cleaning rule (identical for all three apps; see 03_reviews_clean.py for the code)
  normalise      NFKC, then NFD with combining marks stripped, then lower case. The NFKC
                 step matters because much of the loan spam writes its brand in
                 mathematical-alphanumeric Unicode letters.
  loan_spam      lending-site brands and obfuscations (vay9, vaytotnhat, ktien, c0m, ...)
  referral_spam  a referral phrase (nhap ma, ma gioi thieu, ma gt, ma moi, ma dai ly)
                 next to a six-digit or letter code or a reward amount
  duplicate      the same normalised text of 20 or more characters, or the same text
                 from the same author; the earliest copy is kept
  generic        a kept review of one word carrying no theme ("tot", "good", "ok").
                 Counted separately, not removed. GENERIC_SENSITIVITY shows the same
                 split under two- and four-word rules.

Theme tags are non-exclusive whole-word keyword matches on the normalised text, with
tone-mark-sensitive matching for syllables that collide once accents are stripped.
"""

# ---------------------------------------------------------------- headline counts
DNSE_TOTALS = {d!r}

# rating, raw count, clean count
{block("RATING_HIST", t["RATING_HIST"])}
# ---------------------------------------------------------------- by year
YEAR_HEADER = {t["YEAR_HEADER"]!r}
{block("YEAR_TAB", t["YEAR_TAB"])}
# generic share of retained reviews and the mean of the rest, under 1-, 2- and 4-word rules
GENERIC_SENSITIVITY_HEADER = {t["GENERIC_SENSITIVITY_HEADER"]!r}
{block("GENERIC_SENSITIVITY", t["GENERIC_SENSITIVITY"])}
# ---------------------------------------------------------------- themes
THEMES = {t["THEMES"]!r}

THEME_LABEL = {{
''' + "".join(f"    {k!r}: {v!r},\n" for k, v in t["THEME_LABEL"].items()) + f'''}}

# theme, negative(1-2), neutral(3), positive(4-5), all clean, share of negatives %
THEME_HEADER = {t["THEME_HEADER"]!r}
{block("THEME_TAB", t["THEME_TAB"])}
# negative reviews only, by year and theme
NEG_YEAR_HEADER = {t["NEG_YEAR_HEADER"]!r}
{block("NEG_YEAR", t["NEG_YEAR"])}
# ---------------------------------------------------------------- peer comparison
CLEANING_HEADER = {t["CLEANING_HEADER"]!r}
{block("CLEANING_LOG", t["CLEANING_LOG"])}
VPS_SPAN = {tuple(t["VPS_SPAN"])!r}

PEER_HEADER = {t["PEER_HEADER"]!r}
{block("PEERS", t["PEERS"])}
# ---------------------------------------------------------------- selected reviews
QUOTE_HEADER = {t["QUOTE_HEADER"]!r}
{block("QUOTES", t["QUOTES"])}
# ---------------------------------------------------------------- App Store cross-check
# Written reviews from the Vietnamese App Store (02c), cleaned with the same rule. The
# feed serves recent reviews only, so the comparison with Google Play uses the window
# both stores cover. store_rating_* are all star ratings, most of them left without text.
APPSTORE_PULLED = {t["APPSTORE_PULLED"]!r}
IOS_CLEANING_HEADER = {t["IOS_CLEANING_HEADER"]!r}
{block("IOS_CLEANING_LOG", t["IOS_CLEANING_LOG"])}
IOS_DNSE_YEAR_HEADER = {t["IOS_DNSE_YEAR_HEADER"]!r}
{block("IOS_DNSE_YEAR", t["IOS_DNSE_YEAR"])}
STORE_WINDOW = {tuple(t["STORE_WINDOW"])!r}
STORE_COMPARE_HEADER = {t["STORE_COMPARE_HEADER"]!r}
{block("STORE_COMPARE", t["STORE_COMPARE"])}
# DNSE one- and two-star reviews in the window: Google Play, App Store
STORE_NEGATIVES = {t["STORE_NEGATIVES"]!r}
STORE_THEME_HEADER = {t["STORE_THEME_HEADER"]!r}
{block("STORE_THEMES", t["STORE_THEMES"])}
# a review counted once per group even if it carries both themes
STORE_GROUP_DEF = {t["STORE_GROUP_DEF"]!r}
STORE_GROUP_HEADER = {t["STORE_GROUP_HEADER"]!r}
STORE_GROUPS = {t["STORE_GROUPS"]!r}
'''


if __name__ == "__main__":
    main()

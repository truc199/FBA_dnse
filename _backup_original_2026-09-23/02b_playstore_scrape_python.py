#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
02b -- Google Play review collector, standalone Python version.

Equivalent to 02a but runnable from a laptop without a browser. Use this one to
reproduce or extend the pull. Google returns nothing to some datacentre IP
ranges, so run it from an ordinary internet connection rather than a server.

Install
    pip install google-play-scraper

Run
    python3 02b_playstore_scrape_python.py

Output
    reviews_raw_<package>.csv   one row per review, unfiltered
Columns
    review_id, rating, date, thumbs_up, author, text
The cleaning happens in 03_reviews_clean.py, deliberately as a separate step so
the raw pull stays auditable.
"""
import csv
import os
import time

from google_play_scraper import Sort, reviews

APPS = {
    "vn.com.encapital.arrow": "DNSE Entrade X",
    "vn.com.vpbs.smartone":   "VPS SmartOne",
    "com.fpts.eztrade":       "FPTS EzTrade",
}
TARGET = 2000          # upper bound; Google stops earlier when history runs out
BATCH = 200
OUT_DIR = os.path.dirname(os.path.abspath(__file__))


def pull(package, target=TARGET):
    collected, token, seen = [], None, set()
    while len(collected) < target:
        batch, token = reviews(
            package, lang="vi", country="vn",
            sort=Sort.NEWEST, count=BATCH, continuation_token=token,
        )
        if not batch:
            break
        new = 0
        for r in batch:
            if r["reviewId"] in seen:
                continue
            seen.add(r["reviewId"])
            collected.append(r)
            new += 1
        print(f"  +{new:3d}  total {len(collected)}")
        if token is None or new == 0:
            break
        time.sleep(0.4)
    return collected


def write_csv(package, rows):
    path = os.path.join(OUT_DIR, f"reviews_raw_{package}.csv")
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["review_id", "rating", "date", "thumbs_up", "author", "text"])
        for r in rows:
            w.writerow([
                r["reviewId"], r["score"], r["at"].strftime("%Y-%m-%d"),
                r.get("thumbsUpCount", 0), r.get("userName", ""),
                (r.get("content") or "").replace("\n", " ").strip(),
            ])
    print(f"  wrote {path} ({len(rows)} rows)")
    return path


if __name__ == "__main__":
    for package, name in APPS.items():
        print(f"\n{name}  ({package})")
        write_csv(package, pull(package))

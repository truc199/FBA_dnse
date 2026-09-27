#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
02c -- Apple App Store review collector, Vietnam storefront.

Google Play covers Android users only. iPhone owners in Vietnam skew towards higher
incomes, which is closer to the segment the report recommends, so the App Store pull is
used as a cross-check on the Google Play evidence: same cleaning rule, same themes,
compared over the years both stores cover.

Source
    Apple's public customer-review feed, one JSON page of up to 50 reviews:
    https://itunes.apple.com/vn/rss/customerreviews/page=N/id=APP_ID/sortby=SORT/json
    It serves at most ten pages per sort order, so at most 500 of the most recent and 500
    of the most helpful written reviews. It has no full history, and it is unreliable:
    the same page can come back empty on one request and full on the next. Every page is
    therefore requested several times, empty pages do not end the pull, both sort orders
    are fetched, and the results are merged by review id.

    Star ratings left without a written review are not in the feed. Their count and
    average come from the iTunes lookup API and are saved alongside.

Run
    python3 src/pipeline/02c_appstore_scrape.py            merges with the CSVs of earlier runs
    python3 src/pipeline/02c_appstore_scrape.py --fresh    starts from nothing

Because the feed returns a different subset each time, a new run is merged by review id
into the CSV already on disk, so repeated runs accumulate. A review deleted from the
store after an earlier run stays in the file; use --fresh to drop those.

Output
    reviews_raw_ios_<package>.csv   same columns as 02b plus title and app version;
                                    text is the title and body joined, since the title
                                    is often the whole complaint ("Lừa đảo")
    appstore_meta.json              star-rating count and average per app
"""
import csv
import json
import os
import re
import sys
import time
import urllib.request
from datetime import datetime, timedelta, timezone

VN_TZ = timezone(timedelta(hours=7))

# package name (as used for the Google Play files) -> App Store id, Vietnam storefront
APPS = {
    "vn.com.encapital.arrow": ("DNSE Entrade X", 1529981425),
    "vn.com.vpbs.smartone":   ("VPS SmartOne",   1431656423),
    "com.fpts.eztrade":       ("FPTS EzTrade",   6737305302),
}
SORTS = ("mostrecent", "mosthelpful")
PAGES = 10              # the feed stops serving after page 10
ATTEMPTS = 4            # requests per page before accepting it as empty
PASSES = 2              # full sweeps; the union of both is kept
import sys as _sys, os as _os
_sys.path.insert(0, _os.path.dirname(_os.path.abspath(__file__)))
from paths import DATA  # all data files live in <repo>/data
OUT_DIR = DATA
UA = {"User-Agent": "Mozilla/5.0"}


def get_json(url):
    with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=30) as r:
        return json.loads(r.read().decode("utf-8"))


def page_entries(app_id, sort, page):
    url = f"https://itunes.apple.com/vn/rss/customerreviews/page={page}/id={app_id}/sortby={sort}/json"
    for _ in range(ATTEMPTS):
        try:
            entries = get_json(url).get("feed", {}).get("entry", [])
        except Exception:                       # timeouts and 5xx are part of the same flakiness
            entries = []
        if isinstance(entries, dict):           # a single entry arrives as an object
            entries = [entries]
        entries = [e for e in entries if "im:rating" in e]   # the first entry can be app metadata
        if entries:
            return entries
        time.sleep(0.6)
    return []


def pull(app_id):
    found = {}
    for _ in range(PASSES):
        for sort in SORTS:
            for page in range(1, PAGES + 1):
                for e in page_entries(app_id, sort, page):
                    found[e["id"]["label"]] = e
                time.sleep(0.3)
    return list(found.values())


def to_row(e):
    when = datetime.fromisoformat(e["updated"]["label"]).astimezone(VN_TZ)
    title = e.get("title", {}).get("label", "").strip()
    body = e.get("content", {}).get("label", "").strip()
    text = body if not title or body.lower().startswith(title.lower()) else f"{title}. {body}"
    return {
        "review_id": e["id"]["label"],
        "rating": int(e["im:rating"]["label"]),
        "date": when.strftime("%Y-%m-%d"),
        "thumbs_up": max(0, int(e.get("im:voteSum", {}).get("label", 0) or 0)),
        "author": e.get("author", {}).get("name", {}).get("label", ""),
        "text": re.sub(r"[\r\n]+", " ", text).strip(),
        "title": re.sub(r"[\r\n]+", " ", title),
        "version": e.get("im:version", {}).get("label", ""),
    }


def lookup(app_id):
    d = get_json(f"https://itunes.apple.com/lookup?id={app_id}&country=vn")
    r = (d.get("results") or [{}])[0]
    return {"app_store_id": app_id, "track_name": r.get("trackName"),
            "rating_count": r.get("userRatingCount"), "rating_average": r.get("averageUserRating")}


if __name__ == "__main__":
    meta = {"pulled": datetime.now(VN_TZ).strftime("%Y-%m-%d"), "apps": {}}
    for package, (name, app_id) in APPS.items():
        print(f"\n{name}  (App Store {app_id})")
        path = os.path.join(OUT_DIR, f"reviews_raw_ios_{package}.csv")
        merged = {}
        if os.path.exists(path) and "--fresh" not in sys.argv:
            with open(path, encoding="utf-8-sig") as f:
                merged = {r["review_id"]: r for r in csv.DictReader(f)}
        before = len(merged)
        for e in pull(app_id):
            r = to_row(e)
            merged[r["review_id"]] = r
        print(f"  {len(merged) - before} new reviews, {len(merged)} in total")
        rows = sorted(merged.values(), key=lambda r: r["date"], reverse=True)
        with open(path, "w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=["review_id", "rating", "date", "thumbs_up", "author",
                                              "text", "title", "version"])
            w.writeheader()
            w.writerows(rows)
        info = lookup(app_id)
        meta["apps"][package] = {**info, "written_reviews_pulled": len(rows),
                                 "first_date": rows[-1]["date"] if rows else None,
                                 "last_date": rows[0]["date"] if rows else None}
        print(f"  wrote {path} ({len(rows)} rows, {rows[-1]['date'] if rows else '-'} to "
              f"{rows[0]['date'] if rows else '-'}); store rating {info['rating_average']} "
              f"from {info['rating_count']} ratings")
    with open(os.path.join(OUT_DIR, "appstore_meta.json"), "w", encoding="utf-8") as f:
        json.dump(meta, f, ensure_ascii=False, indent=2)
    print("\nwrote appstore_meta.json")

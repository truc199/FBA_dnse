#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
01 -- Pull the complete Global Findex record for Vietnam from the World Bank API.

The World Bank exposes Findex as "source 28". One call returns every series, every
survey wave and every demographic segment for a country. Nothing is transcribed by
hand, so the figures cannot drift from the published data.

Segment suffixes on an indicator id
    .1  women                  .7  poorest 40 per cent
    .2  men                    .8  richest 60 per cent
    .3  age 15 to 24           .9  rural
    .4  age 25 and over        .10 urban
    .5  primary education or less   .11 out of the labour force
    .6  secondary education or more .12 in the labour force
A trailing .s means the figure is a share of a sub-population rather than of all adults.

Output
    findex_raw.json     the untouched API response, so the pull can be audited later

findex_data.py is a curated subset of this pull: 51 indicators chosen for the report,
with plain-English labels and theme groupings written by hand. Its numbers are not
typed in, and this script checks every one of them against the fresh pull and prints
any value that differs.

Run
    python3 01_findex_fetch.py
"""
import json
import os
import re
import urllib.request

URL = ("https://api.worldbank.org/v2/sources/28/country/VNM/"
       "series/all/data?format=json&per_page=25000")
OUT_DIR = os.path.dirname(os.path.abspath(__file__))

SEGMENT_SUFFIX = {
    "":   "All adults",  "1":  "Women",                "2":  "Men",
    "3":  "Young (15-24)", "4": "Older (25+)",
    "5":  "Primary educ or less", "6": "Secondary educ or more",
    "7":  "Poorest 40%", "8": "Richest 60%",
    "9":  "Rural", "10": "Urban",
    "11": "Out of labour force", "12": "In labour force",
}
SEGMENTS = ["All adults", "Women", "Men", "Young (15-24)", "Older (25+)",
            "Primary educ or less", "Secondary educ or more", "Poorest 40%",
            "Richest 60%", "Rural", "Urban", "Out of labour force", "In labour force"]


def fetch():
    """Every page of the response. One page holds 25,000 observations and Vietnam
    returns about 20,000, but a longer record would otherwise be cut off silently."""
    raw, page, pages = None, 1, 1
    while page <= pages:
        req = urllib.request.Request(f"{URL}&page={page}", headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=120) as r:
            got = json.loads(r.read().decode("utf-8"))
        if raw is None:
            raw = got
        else:
            raw["source"]["data"].extend(got["source"]["data"])
        pages = int(got.get("pages", 1))
        page += 1
    total = int(raw.get("total", len(raw["source"]["data"])))
    if len(raw["source"]["data"]) != total:
        raise RuntimeError(f"API reported {total} observations, received {len(raw['source']['data'])}")
    return raw


def parse(raw):
    """Flatten the API's variable/value shape into (series_id, year, value) rows."""
    rows = []
    for obs in raw["source"]["data"]:
        got = {v["concept"].lower(): (v.get("id"), v.get("value")) for v in obs["variable"]}
        series_id = got.get("series", (None, None))[0]
        year = got.get("time", (None, None))[1]
        label = got.get("series", (None, None))[1]
        value = obs.get("value")
        if series_id is None or value is None:
            continue
        try:
            year = int(str(year).strip())
        except (TypeError, ValueError):
            continue
        rows.append((series_id, label, year, float(value)))
    return rows


def split_segment(series_id):
    """'fin17a.t.d.9' -> ('fin17a.t.d', 'Rural'). A base id returns 'All adults'."""
    m = re.match(r"^(.*?)\.(\d{1,2})$", series_id)
    if m and m.group(2) in SEGMENT_SUFFIX:
        return m.group(1), SEGMENT_SUFFIX[m.group(2)]
    return series_id, "All adults"


if __name__ == "__main__":
    raw = fetch()
    with open(os.path.join(OUT_DIR, "findex_raw.json"), "w") as f:
        json.dump(raw, f)

    rows = parse(raw)
    print(f"observations returned : {len(raw['source']['data']):,}")
    print(f"non-null observations : {len(rows):,}")

    # base indicator -> year -> segment -> value
    table = {}
    labels = {}
    for series_id, label, year, value in rows:
        base, seg = split_segment(series_id)
        if seg == "All adults":
            labels[base] = label            # the base series names the indicator
        else:
            labels.setdefault(base, label)
        table.setdefault(base, {}).setdefault(year, {})[seg] = value

    latest = max(y for ind in table.values() for y in ind)
    seg_count = sum(1 for b, ind in table.items()
                    if latest in ind and len(ind[latest]) > 1)
    print(f"latest wave           : {latest}")
    print(f"indicators with a full segment breakdown in {latest}: {seg_count}")
    print("\nWrote findex_raw.json.")

    # Check every number in findex_data.py against this pull.
    import sys
    sys.path.insert(0, OUT_DIR)
    import findex_data as F
    checks = []
    for code, _, _, vals in F.SEG2024:
        for j, seg in enumerate(F.SEGMENTS):
            checks.append((f"SEG2024 {code} {seg}", vals.get(j), table.get(code, {}).get(latest, {}).get(seg)))
    for code, _, _, v in F.NATIONAL2024:
        checks.append((f"NATIONAL2024 {code}", v, table.get(code, {}).get(latest, {}).get("All adults")))
    for code, _, series in F.TRENDS:
        for y, v in series.items():
            checks.append((f"TRENDS {code} {y}", v, table.get(code, {}).get(y, {}).get("All adults")))
    bad = [(k, a, b) for k, a, b in checks if a is None or b is None or abs(a - b) > 0.001]
    for k, a, b in bad:
        print(f"  differs: {k}: findex_data.py {a}, API {b}")
    print(f"findex_data.py: {len(checks)} values checked, {len(bad)} differ from the API")

# -*- coding: utf-8 -*-
"""Derive the priority customer segment from the Global Findex 2024 Vietnam
segment matrix instead of asserting one.

Method
------
Two indices are built from indicators the survey reports for every demographic cut.

  Index A, investable surplus. Whether the segment has money that could be put to
  work and already keeps it inside the formal system.
  Index B, digital habit. Whether the segment already transacts through a phone often
  enough that a trading or cash-management app is not a new behaviour.

Each index is the unweighted mean of its member indicators, each of which is already a
percentage of adults in that segment. The composite is the unweighted mean of A and B.
Unweighted means are used deliberately, because any weighting scheme chosen after seeing
the data would be fitted to the conclusion.

A third quantity, the activation gap, is the percentage-point distance between account
ownership and saving at a financial institution in that segment. It measures the pool of
people who are already inside the formal system but are not yet putting money to work,
which is exactly the population a broker is trying to activate.

Segment population estimates are applied afterwards so that the ranking by propensity
and the ranking by size can be read separately. They are recovered from the survey
itself (see implied_share), so they carry the same weights as the indicators.

Two cautions. A and B are built from different indicators, so their levels cannot be
compared with each other: a segment with B above A is not "more digital than it is
wealthy". Compare segments within an index. And the priority score multiplies
propensity by the size of the pool, so within each complementary pair the larger half
tends to rank higher; read it next to the composite, not instead of it.

Run
    python3 src/pipeline/04_segment_model.py      prints the table and writes segment_model.json
"""
import json
import os
import statistics
import sys

import sys as _sys, os as _os
_sys.path.insert(0, _os.path.dirname(_os.path.abspath(__file__)))
from paths import DATA, SCRIPT_DIR  # all data files live in <repo>/data
_B = DATA
sys.path[:0] = [SCRIPT_DIR]

import findex_data as F

SEG = F.SEGMENTS
IDX = {code: (label, cat, vals) for code, label, cat, vals in F.SEG2024}

INVESTABLE = [
    "fin17a",    # saved at a bank or similar institution
    "fin17dm",   # saved into an account, monthly
    "fin8",      # stores money in an account
    "fin17e",    # received interest on savings in the past year
    "fin17f",    # saved for old age
    "fin24bd",   # could cover more than two months without income
]
DIGITAL = [
    "dig.acc",    # digitally enabled account
    "con26d",     # uses the internet daily
    "con9a",      # main phone is a smartphone
    "fin25e3w",   # in-store mobile or card payment, weekly
    "fin9b",      # uses mobile or internet to check account balance
    "fin32.acc",  # receives wages into an account
]

# The twelve cuts are six complementary pairs, each splitting all adults in two.
PAIRS = [("Women", "Men"), ("Young (15-24)", "Older (25+)"),
         ("Primary educ or less", "Secondary educ or more"), ("Poorest 40%", "Richest 60%"),
         ("Rural", "Urban"), ("Out of labour force", "In labour force")]


def implied_share(first, second, min_gap=5.0):
    """Population share of `first` within its pair, recovered from the survey itself.

    Every indicator is a weighted share of the adults in a segment, so for any
    complementary pair All = w * first + (1 - w) * second, which gives
    w = (All - second) / (first - second). The median across indicators whose two
    halves differ by more than min_gap points is used; smaller gaps make the ratio
    unstable. The income pair is defined as 40/60 and comes back as 40.0, which is
    the check that the method works. An earlier version of this file typed the shares
    in by hand, with 23.6 per cent for primary education or less against 11.2 here.
    """
    i, k = SEG.index(first), SEG.index(second)
    ws = [(v[0] - v[k]) / (v[i] - v[k]) for _, _, v in IDX.values() if abs(v[i] - v[k]) > min_gap]
    return statistics.median(ws) * 100


POP_SHARE = {"All adults": 100.0}
for _first, _second in PAIRS:
    POP_SHARE[_first] = round(implied_share(_first, _second), 1)
    POP_SHARE[_second] = round(100 - POP_SHARE[_first], 1)

ADULTS_15_PLUS = 80.6e6   # Vietnam adult population, GSO 2024 structure applied to 102m


def mean_of(codes, j):
    vals = [IDX[c][2][j] for c in codes if c in IDX and j in IDX[c][2]]
    return sum(vals) / len(vals) if vals else None


def build():
    """One row per segment. Rounded fields are for display; the priority score and
    rank are computed from unrounded values, because rounding first is enough to swap
    the second and third segments."""
    rows = []
    for j, name in enumerate(SEG):
        a = mean_of(INVESTABLE, j)
        b = mean_of(DIGITAL, j)
        acct = IDX["account.t.d"][2][j]
        savefi = IDX["fin17a"][2][j]
        gap = acct - savefi
        share = POP_SHARE[name]
        pool = ADULTS_15_PLUS * share / 100 * gap / 100
        rows.append({
            "segment": name, "index_a_investable": round(a, 2),
            "index_b_digital": round(b, 2), "composite": round((a + b) / 2, 2),
            "account_pct": round(acct, 2), "saved_at_fi_pct": round(savefi, 2),
            "activation_gap_pp": round(gap, 2), "pop_share_pct": share,
            "unactivated_adults_m": round(pool / 1e6, 2),
            "priority_score": (a + b) / 2 * pool / 1e6,
        })
    ranked = sorted((r for r in rows if r["segment"] != "All adults"),
                    key=lambda r: -r["priority_score"])
    for i, r in enumerate(ranked):
        r["priority_rank"] = i + 1
        nxt = ranked[i + 1]["priority_score"] if i + 1 < len(ranked) else None
        r["gap_to_next_pct"] = round((r["priority_score"] / nxt - 1) * 100, 2) if nxt else None
    return rows


def detail_table():
    """Every indicator used, by segment, so the index can be audited."""
    out = []
    for code in INVESTABLE + DIGITAL:
        label, cat, vals = IDX[code]
        out.append([code, label, "Investable surplus" if code in INVESTABLE else "Digital habit"]
                   + [round(vals[j], 2) for j in range(len(SEG))])
    return out


if __name__ == "__main__":
    rows = build()
    w = max(len(r["segment"]) for r in rows)
    print(f"{'Segment':{w}} | A inv | B dig | Comp  | Acct  | SaveFI| Gap  | Share | Pool m | Rank")
    for r in sorted(rows, key=lambda r: r.get("priority_rank", 0)):
        print(f"{r['segment']:{w}} | {r['index_a_investable']:5.1f} | {r['index_b_digital']:5.1f} | "
              f"{r['composite']:5.1f} | {r['account_pct']:5.1f} | {r['saved_at_fi_pct']:5.1f} | "
              f"{r['activation_gap_pp']:4.1f} | {r['pop_share_pct']:5.1f} | "
              f"{r['unactivated_adults_m']:6.2f} | {r.get('priority_rank', '-')}")
    out = os.path.join(_B, "segment_model.json")
    with open(out, "w", encoding="utf-8") as f:
        json.dump({"adults_15_plus_m": ADULTS_15_PLUS / 1e6, "pop_share": POP_SHARE,
                   "investable": INVESTABLE, "digital": DIGITAL, "rows": rows}, f, indent=2)
    print("\nwrote", out)

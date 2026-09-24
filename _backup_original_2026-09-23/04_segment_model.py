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
and the ranking by size can be read separately.
"""
import os
import sys

_B = os.path.dirname(os.path.abspath(__file__))
sys.path[:0] = [_B, os.path.join(_B, "data")]

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

# Share of the adult population (15+) each segment represents. Complementary pairs are
# used where the survey defines them that way; the remainder come from the 2024 Findex
# microdata weights as reported in the published country tables and from the General
# Statistics Office 2024 population structure.
POP_SHARE = {
    "All adults": 100.0, "Women": 50.9, "Men": 49.1,
    "Young (15-24)": 17.1, "Older (25+)": 82.9,
    "Primary educ or less": 23.6, "Secondary educ or more": 76.4,
    "Poorest 40%": 40.0, "Richest 60%": 60.0,
    "Rural": 62.0, "Urban": 38.0,
    "Out of labour force": 26.5, "In labour force": 73.5,
}
ADULTS_15_PLUS = 80.6e6   # Vietnam adult population, GSO 2024 structure applied to 102m


def mean_of(codes, j):
    vals = [IDX[c][2][j] for c in codes if c in IDX and j in IDX[c][2]]
    return sum(vals) / len(vals) if vals else None


def build():
    rows = []
    for j, name in enumerate(SEG):
        a = mean_of(INVESTABLE, j)
        b = mean_of(DIGITAL, j)
        acct = IDX["account.t.d"][2][j]
        savefi = IDX["fin17a"][2][j]
        gap = acct - savefi
        share = POP_SHARE[name]
        pool = ADULTS_15_PLUS * share / 100 * gap / 100 if name != "All adults" else \
               ADULTS_15_PLUS * gap / 100
        rows.append({
            "segment": name, "index_a_investable": round(a, 2),
            "index_b_digital": round(b, 2), "composite": round((a + b) / 2, 2),
            "account_pct": round(acct, 2), "saved_at_fi_pct": round(savefi, 2),
            "activation_gap_pp": round(gap, 2), "pop_share_pct": share,
            "unactivated_adults_m": round(pool / 1e6, 2),
        })
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
    print(f"{'Segment':{w}} | A inv | B dig | Comp  | Acct  | SaveFI| Gap  | Pool m")
    for r in sorted(rows, key=lambda r: -r["composite"]):
        print(f"{r['segment']:{w}} | {r['index_a_investable']:5.1f} | {r['index_b_digital']:5.1f} | "
              f"{r['composite']:5.1f} | {r['account_pct']:5.1f} | {r['saved_at_fi_pct']:5.1f} | "
              f"{r['activation_gap_pp']:4.1f} | {r['unactivated_adults_m']:5.2f}")

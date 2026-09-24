# -*- coding: utf-8 -*-
"""Vietnamese securities-industry cross-section, Q2 2026.

All figures are as published by the two exchanges or taken from the brokers' own
quarterly financial statements as summarised by the financial press. Percentages are
share of value traded on the named market, which is how HOSE and HNX define market share.
A broker's position on one market cannot be compared with another broker's position on a
different market, so each market is kept in its own column.
"""

SOURCES = {
    "hose": "HOSE quarterly market-share announcement, Q2 2026, as tabulated by "
            "Tin nhanh Chung khoan and Nguoi Quan Sat, 7 July 2026",
    "hnx":  "HNX quarterly market-share announcement, Q2 2026, as tabulated by "
            "Vietstock and Nguoi Quan Sat, 7 July 2026",
    "deriv":"HNX derivatives market-share announcement, Q2 2026",
    "margin":"Q2 2026 separate and consolidated financial statements, as tabulated by "
             "Vietstock, 'Du no margin lap ky luc 454 ngan ty dong', July 2026",
    "profit":"Q2 2026 financial statements as tabulated by Mekong Asean, "
             "'So ke loi nhuan nhom cong ty chung khoan dau nganh'",
    "dnse": "DNSE's own filings, pulled line by line by 01b_dnse_financials_fetch.py; Q2 2026 is the "
            "KPMG-reviewed half year less the first quarter",
}

import json as _json
import os as _os

with open(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), "dnse_financials.json"),
          encoding="utf-8") as _f:
    _FS = _json.load(_f)["quarterly"]
DNSE_LENDING_Q2 = round(_FS["2026Q2"]["loans"], 1)
DNSE_PBT_Q2 = round(_FS["2026Q2"]["pbt"], 1)
DNSE_PBT_Q2_YOY = f"{(_FS['2026Q2']['pbt'] / _FS['2025Q2']['pbt'] - 1) * 100:+.1f}%"

# ---------------------------------------------------------------- HOSE cash equities
# rank, company, Q2 2026 share %, Q1 2026 share %
HOSE_Q2_2026 = [
    (1,  "VPS",                 12.61, 15.32),
    (2,  "SSI",                 11.17, 11.14),
    (3,  "TCBS",                 9.36,  8.85),
    (4,  "Vietcap",              7.00,  7.35),
    (5,  "HSC",                  6.80,  7.30),
    (6,  "MBS",                  4.79,  5.29),
    (7,  "VNDirect",             3.96,  4.78),
    (8,  "VPBankS",              3.57,  2.94),
    (9,  "KIS Vietnam",          2.99,  3.21),
    (10, "Mirae Asset Vietnam",  2.94,  2.82),
]
HOSE_TOP10_Q2 = 65.19      # %, equals the sum of the ten rows above
HOSE_TOP10_Q1 = 69.05      # %
# DNSE does not appear in the HOSE top ten in Q2 2026, so its HOSE share is below 2.94%.
DNSE_HOSE_Q2 = None

# ---------------------------------------------------------------- HNX listed shares
# rank, company, Q2 2026 share %. Ranks 4 to 6 were published without figures in the
# sources consulted; the exchange listed them in this order.
HNX_Q2_2026 = [
    (1,  "VPS",      17.71),
    (2,  "TCBS",      9.00),
    (3,  "VPBankS",   6.71),
    (4,  "SSI",       None),
    (5,  "VNDirect",  None),
    (6,  "MBS",       None),
    (7,  "BSC",       3.58),
    (8,  "DNSE",      2.88),
    (9,  "Vietcap",   2.86),
    (10, "VIX",       2.66),
]
HNX_TOP10_Q2 = 63.2        # %

# ---------------------------------------------------------------- Derivatives
DERIV_Q2_2026 = [
    (1, "VPS",      33.84),
    (2, "DNSE",     25.38),
    (3, "SSI",       8.21),
    (4, "VNDirect",  None),   # about 4%
    (5, "MBS",       None),   # about 4%
]
DERIV_TOP10_Q2 = 94.52
DERIV_TOP10_Q1 = 93.53

# DNSE derivatives share by quarter, from HNX announcements. Q2 and Q3 2024 were not
# found in the sources consulted. Q4 2024 is from the HNX figures tabulated by
# Vietstock, "Thi truong phai sinh 2025: VPS danh roi thi phan, DNSE tao buoc nhay vot",
# January 2026, which also gives full-year shares of 6.14% (2024) and 21.47% (2025).
DNSE_DERIV_SERIES = [
    ("Q1 2024",  4.01), ("Q4 2024",  9.98), ("Q1 2025", 16.70), ("Q2 2025", 17.33),
    ("Q3 2025", 23.67), ("Q4 2025", 24.26), ("Q1 2026", 25.50), ("Q2 2026", 25.38),
]

# ---------------------------------------------------------------- Margin lending
# company, balance at 30 June 2026 in VND billion, share of industry total %
MARGIN_TOTAL_Q2 = 453800.0   # VND bn, total lending of all securities companies
MARGIN_TOTAL_Q1 = 424100.0   # VND bn, implied by the reported 7% quarterly increase
MARGIN_NOTE = ("The 453,800 figure is total lending, which includes advances against "
               "sale proceeds. Press estimates of margin lending alone for the same "
               "date cluster around 445,000.")
MARGIN_Q2_2026 = [
    ("TCBS",    51500),
    ("SSI",     40500),
    ("VPBankS", 38200),
    ("VPS",     31300),
    ("HSC",     29000),
    ("DNSE",     DNSE_LENDING_Q2),
]

# ---------------------------------------------------------------- Profitability
# company, Q2 2026 pre-tax profit VND bn, year-on-year change
PBT_Q2_2026 = [
    ("VPBankS",  2159, "about four times"),
    ("TCBS",     2097, "+21%"),
    ("SSI",      1511, "+32%"),
    ("VPS",      1378, "+57%"),
    ("VNDirect", 1100, "+127%"),
    ("DNSE",     DNSE_PBT_Q2, DNSE_PBT_Q2_YOY),
    ("VIX",        75, "-95%"),
]

# ---------------------------------------------------------------- Market totals
MARKET = {
    "domestic_individual_accounts_end_aug_2026": 13_800_000,
    "foreign_accounts_end_aug_2026": 52_633,
    "hose_adv_value_aug_2026_vnd_bn": 17_336,
    "vn30_futures_adv_value_vnd_bn": 43_925,
    "vn30_futures_foreign_participation_pct": 3.84,
    "hose_foreign_net_sell_ytd_2026_vnd_bn": 90_704,
    "margin_cap_pct_of_equity": 200,
    "ftse_reclassification_effective": "21 September 2026",
    # 27 on the November 2025 list, 32 on the April 2026 indicative list. The final
    # list was due on 21 August 2026 and has not been checked; confirm before citing.
    "ftse_indicative_list_apr_2026": 32,
}

# ---------------------------------------------------------------- DNSE position
DNSE_POSITION = [
    # measure, DNSE value, unit, market total, DNSE share %
    ("Customer accounts", 1_700_000, "accounts", 13_852_633, 12.27),
    ("Derivatives brokerage", 25.38, "% share", 100.0, 25.38),
    ("HNX listed-share brokerage", 2.88, "% share", 100.0, 2.88),
    ("HOSE listed-share brokerage", None, "% share", 100.0, None),
    ("Lending balance", DNSE_LENDING_Q2, "VND bn", MARGIN_TOTAL_Q2,
     round(DNSE_LENDING_Q2 / MARGIN_TOTAL_Q2 * 100, 2)),
    ("Q2 2026 pre-tax profit", DNSE_PBT_Q2, "VND bn", None, None),
]

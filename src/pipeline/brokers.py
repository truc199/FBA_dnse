# -*- coding: utf-8 -*-
"""Vietnamese securities-industry cross-section, Q2 2026.

Market shares are read from the exchanges' own announcements (01d); lending and profit from each
broker's filed statements (01b, 01c). Only the industry lending total is a press compilation.
Percentages are share of value traded on the named market, which is how HOSE and HNX define
market share. A broker's position on one market cannot be compared with another broker's
position on a different market, so each market is kept in its own column.
"""

SOURCES = {
    "hose": "HOSE announcement 'Thi phan gia tri giao dich moi gioi Quy II va Ban nien nam 2026', "
            "read from api.hsx.vn by 01d_market_macro_fetch.py",
    "hnx":  "HNX announcement of Q2 2026 listed-share brokerage market share, read from hnx.vn by 01d",
    "deriv":"HNX announcement of Q2 2026 derivatives brokerage market share, read from hnx.vn by 01d",
    "accounts": "VSDC homepage counter of investor trading accounts, 24 September 2026, recorded by 01d",
    "liquidity": "Daily index and futures trading value from Vietcap's price service, averaged by 01d",
    "margin":"Each firm's filed statements, 30 June 2026, pulled by 01c_peer_financials_fetch.py. Industry "
             "total: Vietstock, 'Du no margin lap ky luc 454 ngan ty dong', July 2026",
    "profit":"Each firm's filed statements, Q2 2026, pulled by 01c (consolidated where the firm has subsidiaries)",
    "dnse": "DNSE's own filings, pulled line by line by 01b_dnse_financials_fetch.py; Q2 2026 is the "
            "KPMG-reviewed half year less the first quarter",
}

import json as _json
import os as _os

import sys as _sys
_sys.path.insert(0, _os.path.dirname(_os.path.abspath(__file__)))
from paths import DATA as _HERE  # all data files live in <repo>/data
with open(_os.path.join(_HERE, "dnse_financials.json"), encoding="utf-8") as _f:
    _FS = _json.load(_f)["quarterly"]
with open(_os.path.join(_HERE, "peer_financials.json"), encoding="utf-8") as _f:
    _PANEL = _json.load(_f)
_PEERS = {n: d["quarterly"] for n, d in _PANEL["firms"].items() if d["focus"]}
# Lending of every securities company with filings on Vietcap, DNSE included; unlisted brokers are absent.
LISTED_LENDING_TOTAL_Q2 = round(_PANEL["totals"]["2026Q2"]["loans"], 1)
LISTED_FIRMS_Q2 = _PANEL["totals"]["2026Q2"]["firms_reporting_loans"]
DNSE_LENDING_Q2 = round(_FS["2026Q2"]["loans"], 1)
DNSE_PBT_Q2 = round(_FS["2026Q2"]["pbt"], 1)
DNSE_PBT_Q2_YOY = f"{(_FS['2026Q2']['pbt'] / _FS['2025Q2']['pbt'] - 1) * 100:+.1f}%"


def _filed(name, key):
    return round(_PEERS[name]["2026Q2"][key], 1)


def _yoy(name):
    return f"{(_PEERS[name]['2026Q2']['pbt'] / _PEERS[name]['2025Q2']['pbt'] - 1) * 100:+.1f}%"


with open(_os.path.join(_HERE, "market_macro.json"), encoding="utf-8") as _f:
    _MM = _json.load(_f)
# Exchange announcements give full legal names, including names since changed; most specific keys first.
# VPBS ("... Ngan hang TMCP Viet Nam Thinh Vuong") became VPS in 2019; today's VPBankS is a different firm.
_SHORT = [("Thịnh Vượng", "VPS"), ("Kỹ Thương", "TCBS"), ("VPBank", "VPBankS"), ("VNDIRECT", "VNDirect"),
          ("Thành phố Hồ Chí Minh", "HSC"), ("TP. Hồ Chí Minh", "HSC"), ("Mirae", "Mirae Asset Vietnam"),
          ("KIS", "KIS Vietnam"), ("BIDV", "BSC"), ("Đầu tư và Phát triển", "BSC"), ("Phú Hưng", "PHS"),
          ("FPT", "FPTS"), ("Ngoại thương", "VCBS"), ("Rồng Việt", "VDSC"), ("Bản Việt", "Vietcap"),
          ("Bảo Việt", "BVSC"), ("An Bình", "ABS"), ("Sài Gòn Hà Nội", "SHS"), ("Sài Gòn - Hà Nội", "SHS"),
          ("khoán Sài Gòn", "SSI"), ("ACB", "ACBS"), ("Yuanta", "Yuanta Vietnam"), ("DNSE", "DNSE"),
          ("Vietcap", "Vietcap"), ("VIX", "VIX"), ("SSI", "SSI"), ("VPS", "VPS"), ("khoán MB", "MBS")]


def _short(name):
    return next((s for k, s in _SHORT if k.lower() in name.lower()), name)


def _table(rows):
    """(rank, short name, share) for the top ten; a few early notices list every firm."""
    return [(r[0], _short(r[1]), r[2]) for r in rows if r[0] <= 10]


def top_ten(rows):
    return round(sum(r[2] for r in rows if r[0] <= 10), 2)


_HOSE = _MM["hose_market_share"]["tables"]
_HNX = _MM["hnx_market_share"]["tables"]

# ---------------------------------------------------------------- HOSE cash equities
# rank, company, Q2 2026 share %, Q1 2026 share % (None where the firm was outside the Q1 top ten)
_hose_q1 = {n: v for _, n, v in _table(_HOSE["2026Q1"])}
HOSE_Q2_2026 = [(rk, n, v, _hose_q1.get(n)) for rk, n, v in _table(_HOSE["2026Q2"])]
HOSE_TOP10_Q2 = round(sum(r[2] for r in HOSE_Q2_2026), 2)
HOSE_TOP10_Q1 = round(sum(_hose_q1.values()), 2)
# DNSE does not appear in the HOSE top ten, so its HOSE share is below the tenth-place share.
DNSE_HOSE_Q2 = None

# ---------------------------------------------------------------- HNX listed shares
HNX_Q2_2026 = _table(_HNX["listed"]["2026Q2"])
HNX_TOP10_Q2 = round(sum(r[2] for r in HNX_Q2_2026), 2)

# ---------------------------------------------------------------- Derivatives
DERIV_Q2_2026 = _table(_HNX["derivatives"]["2026Q2"])
DERIV_TOP10_Q2 = round(sum(r[2] for r in DERIV_Q2_2026), 2)
DERIV_TOP10_Q1 = top_ten(_HNX["derivatives"]["2026Q1"])

# DNSE derivatives share for every quarter it has been in the HNX top ten.
DNSE_DERIV_SERIES = [(f"Q{p[-1]} {p[:4]}", d["share"])
                     for p, d in sorted(_MM["hnx_market_share"]["dnse"]["derivatives"].items()) if d["share"] is not None]

# ---------------------------------------------------------------- Margin lending
# company, balance at 30 June 2026 in VND billion, share of industry total %
MARGIN_TOTAL_Q2 = 453800.0   # VND bn, total lending of all securities companies
MARGIN_TOTAL_Q1 = 424100.0   # VND bn, implied by the reported 7% quarterly increase
MARGIN_NOTE = ("The 453,800 figure is total lending, which includes advances against "
               "sale proceeds. Press estimates of margin lending alone for the same "
               "date cluster around 445,000. The firms with filings on Vietcap, listed and "
               "UPCoM brokers, account for about three quarters of it.")
MARGIN_Q2_2026 = sorted([(n, _filed(n, "loans")) for n in _PEERS] + [("DNSE", DNSE_LENDING_Q2)],
                        key=lambda r: -r[1])

# ---------------------------------------------------------------- Profitability
# company, Q2 2026 pre-tax profit VND bn, year-on-year change
PBT_Q2_2026 = sorted([(n, _filed(n, "pbt"), _yoy(n)) for n in _PEERS] + [("DNSE", DNSE_PBT_Q2, DNSE_PBT_Q2_YOY)],
                     key=lambda r: -r[1])

# ---------------------------------------------------------------- Market totals
def _avg_value(symbol, first, last):
    vals = [r[3] for r in _MM["prices"][symbol]["daily"] if first <= r[0][:7] <= last and r[3]]
    return round(sum(vals) / len(vals), 1)


MARKET = {
    "investor_trading_accounts": _MM["vsdc_latest"]["investor_trading_accounts"],
    "investor_trading_accounts_date": _MM["vsdc_latest"]["date"],
    "hose_adv_value_aug_2026_vnd_bn": _avg_value("VNINDEX", "2026-08", "2026-08"),
    "vn30f1m_adv_value_q2_2026_vnd_bn": _avg_value("VN30F1M", "2026-04", "2026-06"),
    # Press figures kept for context only.
    "vn30_futures_foreign_participation_pct": 3.84,
    "hose_foreign_net_sell_ytd_2026_vnd_bn": 90_704,
    "margin_cap_pct_of_equity": 200,
    "ftse_reclassification_effective": "21 September 2026",
    # 27 on the November 2025 list, 32 on the April 2026 indicative list. The final
    # list was due on 21 August 2026 and has not been checked; confirm before citing.
    "ftse_indicative_list_apr_2026": 32,
}

# Year-end accounts: DNSE from its annual report 2025 (figure 22, p. 29), market from VSDC annual reports.
DNSE_ACCOUNTS_AR = {"2020": 5_548, "2021": 44_727, "2022": 189_845, "2023": 561_279, "2024": 994_811, "2025": 1_512_920}
VSDC_ACCOUNTS = {y: d["total"] for y, d in _MM["vsdc_accounts"].items()}
DNSE_ACCOUNT_SHARE = {y: round(v / VSDC_ACCOUNTS[y] * 100, 2) for y, v in DNSE_ACCOUNTS_AR.items()}
# DNSE share of the loan book of every broker with filings, by quarter (step 01c).
DNSE_LENDING_SHARE = {p: t["dnse_share_of_loans_pct"] for p, t in _PANEL["totals"].items()}

# ---------------------------------------------------------------- DNSE position
DNSE_POSITION = [
    # measure, DNSE value, unit, market total, DNSE share %
    ("Customer accounts", 1_700_000, "accounts", MARKET["investor_trading_accounts"],
     round(1_700_000 / MARKET["investor_trading_accounts"] * 100, 2)),
    ("Derivatives brokerage", dict((n, v) for _, n, v in DERIV_Q2_2026)["DNSE"], "% share", 100.0,
     dict((n, v) for _, n, v in DERIV_Q2_2026)["DNSE"]),
    ("HNX listed-share brokerage", dict((n, v) for _, n, v in HNX_Q2_2026)["DNSE"], "% share", 100.0,
     dict((n, v) for _, n, v in HNX_Q2_2026)["DNSE"]),
    ("HOSE listed-share brokerage", None, "% share", 100.0, None),
    ("Lending balance", DNSE_LENDING_Q2, "VND bn", MARGIN_TOTAL_Q2,
     round(DNSE_LENDING_Q2 / MARGIN_TOTAL_Q2 * 100, 2)),
    ("Q2 2026 pre-tax profit", DNSE_PBT_Q2, "VND bn", None, None),
]

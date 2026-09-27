#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""01c -- Pull the same key lines as 01b for every securities company Vietcap covers, 2018 onwards, and total them by quarter."""
import datetime
import importlib.util
import json
import os
import sys

import sys as _sys, os as _os
_sys.path.insert(0, _os.path.dirname(_os.path.abspath(__file__)))
from paths import DATA, SCRIPT_DIR  # all data files live in <repo>/data
HERE = DATA
_spec = importlib.util.spec_from_file_location("dnse_fetch", os.path.join(SCRIPT_DIR, "01b_dnse_financials_fetch.py"))
B = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(B)

# The peers named in the report, ticker -> display name. VPS Securities trades on HOSE as VCK;
# the ticker VPS belongs to an unrelated pesticide maker.
FOCUS = {"TCX": "TCBS", "SSI": "SSI", "VPX": "VPBankS", "VCK": "VPS", "HCM": "HSC", "VND": "VNDirect",
         "VCI": "Vietcap", "MBS": "MBS", "SHS": "SHS", "VIX": "VIX"}
LIST_URL = "https://iq.vietcap.com.vn/api/iq-insight-service/v2/company/search-bar?language=1"
SECTIONS = [B.IS, B.BS, B.NOTE]
FIRST = "2018Q1"
TOTALLED = ["revenue", "rev_brokerage", "cost_brokerage", "rev_lending", "pbt", "loans", "equity",
            "customer_cash_trading", "total_assets"]


def series(raw, kind):
    periods = sorted({B.period_label(r) for s in SECTIONS for r in raw[s][kind]}, key=B.period_key)
    out = {p: {name: None for name in B.KEY_LINES} for p in periods if kind == "years" or p >= FIRST}
    for name, (sec, fld) in B.KEY_LINES.items():
        for row in raw[sec][kind]:
            p = B.period_label(row)
            if p in out and row.get(fld) is not None:
                out[p][name] = round(row[fld] / B.BN, 4)
    return out


def totals(firms, dnse_q):
    """Sum of each line across every firm reporting it, by quarter, DNSE included."""
    books = [d["quarterly"] for d in firms.values()] + [dnse_q]
    out = {}
    for p in sorted(dnse_q, key=B.period_key):
        if p < FIRST:
            continue
        row = {"firms_reporting_loans": sum(1 for q in books if (q.get(p) or {}).get("loans"))}
        for k in TOTALLED:
            row[k] = round(sum((q.get(p) or {}).get(k) or 0 for q in books), 3)
        row["dnse_share_of_loans_pct"] = round(dnse_q[p]["loans"] / row["loans"] * 100, 3) if row["loans"] else None
        out[p] = row
    return out


if __name__ == "__main__":
    listing = [c for c in B.fetch(LIST_URL) if c.get("comTypeCode") == "CK" and c["code"] != B.SYMBOL]
    firms = {}
    for c in sorted(listing, key=lambda c: c["code"]):
        ticker = c["code"]
        base = f"https://iq.vietcap.com.vn/api/iq-insight-service/v1/company/{ticker}/financial-statement"
        raw = {sec: B.fetch(f"{base}?section={sec}") for sec in SECTIONS}
        if not raw[B.IS]["quarters"]:
            print(f"{ticker}: no statements, skipped")
            continue
        q = series(raw, "quarters")
        qs = list(q)
        name = FOCUS.get(ticker, ticker)
        firms[name] = {
            "ticker": ticker, "full_name": c.get("name"), "floor": c.get("floor"), "focus": ticker in FOCUS,
            "source": base,
            "updated": {B.period_label(r): r.get("updateDate") for r in raw[B.IS]["quarters"] if B.period_label(r) in q},
            "quarterly": q, "half_year": B.half_years(q), "annual": series(raw, "years"),
            "derived": {p: B.derive(q[p], q[qs[i - 1]] if i else None) for i, p in enumerate(qs)},
        }
        print(f"{name:9} {ticker} {c.get('floor', ''):6}: {qs[0] if qs else '-'} to {qs[-1] if qs else '-'}")

    with open(os.path.join(HERE, "dnse_financials.json"), encoding="utf-8") as f:
        dnse_q = json.load(f)["quarterly"]
    tot = totals(firms, dnse_q)
    with open(os.path.join(HERE, "peer_financials.json"), "w", encoding="utf-8") as f:
        json.dump({"pulled": datetime.date.today().isoformat(),
                   "note": "Key lines as defined in 01b, VND billion, costs negative, for every securities company "
                           "in Vietcap's coverage. Consolidated where a firm has subsidiaries. 'totals' sums each line "
                           "across the firms reporting it, DNSE included; unlisted foreign-owned brokers are absent.",
                   "definitions": B.DEFINITIONS, "totals": tot, "firms": firms},
                  f, ensure_ascii=False, separators=(",", ":"))
    print(f"\nWrote peer_financials.json: {len(firms)} firms.\n")

    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    fmt = lambda v, w=8: f"{v:{w},.1f}" if isinstance(v, (int, float)) else f"{'-':>{w}}"
    print(f"{'Q2 2026':9} {'PBT':>8} {'y/y %':>7} {'loans':>9} {'L/E %':>6} {'H1 brokerage after direct cost':>31}")
    for name, d in firms.items():
        if not d["focus"]:
            continue
        q2, q2p, h1 = d["quarterly"]["2026Q2"], d["quarterly"]["2025Q2"], d["half_year"]["2026H1"]
        brok = h1["rev_brokerage"] + h1["cost_brokerage"]
        print(f"{name:9} {fmt(q2['pbt'])} {fmt((q2['pbt'] / q2p['pbt'] - 1) * 100, 7)} {fmt(q2['loans'], 9)} "
              f"{fmt(d['derived']['2026Q2'].get('loans_to_equity_pct'), 6)} {fmt(brok, 31)}")
    print(f"\n{'quarter':8} {'firms':>5} {'total loans':>12} {'DNSE share %':>12}")
    for p, row in tot.items():
        if p.endswith("Q4") or p == max(tot):
            print(f"{p:8} {row['firms_reporting_loans']:5} {row['loans']:12,.0f} {fmt(row['dnse_share_of_loans_pct'], 12)}")

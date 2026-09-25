#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""01b -- Pull DNSE's (HOSE: DSE) full financial statements, every quarter and year, from Vietcap's IQ data service."""
import csv
import datetime
import json
import os
import sys
import time
import urllib.error
import urllib.request

SYMBOL = "DSE"
BASE = f"https://iq.vietcap.com.vn/api/iq-insight-service/v1/company/{SYMBOL}/financial-statement"
HEADERS = {
    "Accept": "application/json, text/plain, */*",
    "User-Agent": ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                   "(KHTML, like Gecko) Chrome/126 Safari/537.36"),
    "Referer": "https://trading.vietcap.com.vn/",
    "Origin": "https://trading.vietcap.com.vn",
}
IS, BS, CF, NOTE = "INCOME_STATEMENT", "BALANCE_SHEET", "CASH_FLOW", "NOTE"
SECTIONS = [IS, BS, CF, NOTE]
OUT_DIR = os.path.dirname(os.path.abspath(__file__))
BN = 1e9

KEY_LINES = {
    "revenue":                 (IS, "isa1"),
    "rev_fvtpl":               (IS, "iss115"),
    "rev_htm":                 (IS, "iss119"),
    "rev_lending":             (IS, "iss120"),
    "rev_brokerage":           (IS, "iss42"),
    "rev_underwriting":        (IS, "iss44"),
    "rev_investment_advice":   (IS, "iss46"),
    "rev_custody":             (IS, "iss47"),
    "rev_financial_advice":    (IS, "iss123"),
    "rev_other":               (IS, "iss50"),
    # Outside operating revenue. The 2026 plan and the annual report's revenue headline both include it.
    "financial_income":        (IS, "iss141"),
    "operating_cost":          (IS, "isa4"),
    "cost_fvtpl":              (IS, "iss124"),
    # Template line 24: loan-loss provisions and the borrowing cost of the loan book, reported as one figure.
    "cost_provision_and_loan_funding": (IS, "iss168"),
    "cost_brokerage":          (IS, "iss133"),
    "cost_investment_advice":  (IS, "iss135"),
    "cost_custody":            (IS, "iss137"),
    "cost_other":              (IS, "iss139"),
    "interest_expense":        (IS, "iss148"),
    "admin_cost":              (IS, "isa10"),
    "pbt":                     (IS, "isa16"),
    "pat":                     (IS, "isa20"),
    "total_assets":            (BS, "bsa53"),
    "cash":                    (BS, "bsa2"),
    "fvtpl_assets":            (BS, "bsa6"),
    "htm_assets":              (BS, "bsb108"),
    # Long-term financial assets. Note 8(b) of the H1 2026 statements shows them as bonds held to maturity.
    "htm_assets_long":         (BS, "bsa43"),
    "loans":                   (BS, "bss215"),
    "loan_allowance":          (BS, "bsa7"),
    "short_term_borrowing":    (BS, "bss238"),
    "bonds_short":             (BS, "bss242"),
    "bonds_long":              (BS, "bss250"),
    "equity":                  (BS, "bsa78"),
    "charter_capital":         (BS, "bsa80"),
    "customer_deposits_total": (BS, "nos395"),
    "customer_cash_trading":   (BS, "nos396"),
    "customer_securities_vsd": (BS, "nos379"),
    "margin_loans":            (NOTE, "nos446"),
    "sale_advances":           (NOTE, "nos447"),
}

DEFINITIONS = {
    "unit": "VND billion. Costs are negative, as reported.",
    "brokerage_net": "rev_brokerage + cost_brokerage: brokerage result after its direct cost, before overheads",
    "pbt_margin_pct": "pbt / revenue",
    "loans_to_equity_pct": "loans / equity; the regulatory ceiling on margin lending is 200% of equity",
    "lending_yield_pct": "rev_lending x 4 / average of opening and closing loans",
    "funding_cost": ("-interest_expense - cost_provision_and_loan_funding - rise in loan_allowance. "
                     "Strips the provision charge out of template line 24, approximated by the change in "
                     "the balance-sheet allowance; write-offs would make this overstate funding cost"),
    "funding_cost_pct": ("funding_cost x 4 / average of opening and closing debt, "
                         "debt = short_term_borrowing + bonds_short + bonds_long"),
    "customer_cash_trading": "off-balance-sheet: investors' cash held for securities trading",
    "customer_securities_vsd": "off-balance-sheet: investors' listed securities deposited at VSDC through DNSE",
}

# Figures the data pack took from press and investor-relations releases before this pull, kept so
# the corrections stay visible. investment_income is checked against rev_fvtpl + rev_htm, the pack's
# own definition ("FVTPL and held to maturity").
DATA_PACK = {
    "FY2025": {"revenue": 1467.0, "rev_lending": 555.8, "rev_brokerage": 404.0,
               "investment_income": 171.4, "pbt": 340.2, "pat": 272.5, "loans": 5832.0},
    "2026Q1": {"revenue": 395.0, "rev_lending": 147.5, "rev_brokerage": 119.5,
               "investment_income": 98.4, "pbt": 14.2, "pat": 11.3, "loans": 5910.0},
    "2026Q2": {"revenue": 453.1, "rev_lending": 188.6, "rev_brokerage": 102.5,
               "investment_income": 95.0, "pbt": 98.9, "pat": 83.0, "loans": 6303.0},
}


def fetch(url, tries=5):
    # The service answers with sporadic 502s; a retry a few seconds later succeeds.
    for attempt in range(tries):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=HEADERS), timeout=60) as r:
                return json.loads(r.read().decode("utf-8"))["data"]
        except (urllib.error.URLError, TimeoutError):
            if attempt == tries - 1:
                raise
            time.sleep(3 * (attempt + 1))


def period_label(row):
    y, n = row["yearReport"], row["lengthReport"]
    return f"FY{y}" if n == 5 else f"{y}Q{n}"


def period_key(label):
    return (int(label[2:]), 5) if label.startswith("FY") else (int(label[:4]), int(label[5:]))


def line_catalogue(meta):
    """Each section's lines in filing order. Vietcap's metadata repeats isa16 under the tax heading; the first is profit before tax."""
    lines = []
    for section in SECTIONS:
        seen = set()
        for m in meta[section]:
            if m["field"] in seen:
                continue
            seen.add(m["field"])
            is_count = any(w in m["titleVi"] for w in ("Khối lượng", "Số lượng"))
            lines.append({"section": section, "field": m["field"], "level": m["level"],
                          "parent": m["parent"], "item_vi": m["titleVi"], "item_en": m["titleEn"],
                          "unit": "units" if is_count else "VND bn"})
    return lines


def table(raw, lines, kind):
    """{(section, field): {period: value}} for one period kind ('quarters' or 'years')."""
    out = {}
    for line in lines:
        rows = raw[line["section"]][kind]
        scale = 1 if line["unit"] == "units" else BN
        series = {}
        for row in rows:
            v = row.get(line["field"])
            if v is not None:
                series[period_label(row)] = round(v / scale, 4)
        out[(line["section"], line["field"])] = series
    return out


def write_csv(path, lines, values, periods):
    with open(path, "w", newline="", encoding="utf-8-sig") as f:
        w = csv.writer(f)
        w.writerow(["section", "field", "level", "parent", "item_vi", "item_en", "unit"] + periods)
        kept = 0
        for line in lines:
            series = values[(line["section"], line["field"])]
            if not any(series.get(p) for p in periods):
                continue
            w.writerow([line[k] for k in ("section", "field", "level", "parent", "item_vi", "item_en", "unit")]
                       + ["" if series.get(p) is None else series[p] for p in periods])
            kept += 1
    return kept


def key_lines(values, periods):
    return {p: {name: values[(sec, fld)].get(p) for name, (sec, fld) in KEY_LINES.items()} for p in periods}


def half_years(key_q):
    """First halves: income-statement lines summed over Q1 and Q2, balances taken at the end of Q2."""
    out = {}
    for p, q2 in key_q.items():
        q1 = key_q.get(f"{p[:4]}Q1")
        if not p.endswith("Q2") or q1 is None:
            continue
        out[f"{p[:4]}H1"] = {
            name: q2[name] if sec != IS else
            (None if q1[name] is None or q2[name] is None else round(q1[name] + q2[name], 4))
            for name, (sec, _) in KEY_LINES.items()}
    return out


def avg(a, b):
    return None if a is None or b is None else (a + b) / 2


def derive(cur, prev):
    d = {}
    if cur["rev_brokerage"] is not None and cur["cost_brokerage"] is not None:
        d["brokerage_net"] = cur["rev_brokerage"] + cur["cost_brokerage"]
    if cur["pbt"] is not None and cur["revenue"]:
        d["pbt_margin_pct"] = cur["pbt"] / cur["revenue"] * 100
    if cur["loans"] is not None and cur["equity"]:
        d["loans_to_equity_pct"] = cur["loans"] / cur["equity"] * 100
    if prev is None:
        return d
    loans_avg = avg(prev["loans"], cur["loans"])
    if cur["rev_lending"] is not None and loans_avg:
        d["lending_yield_pct"] = cur["rev_lending"] * 4 / loans_avg * 100
    parts = [cur["interest_expense"], cur["cost_provision_and_loan_funding"], cur["loan_allowance"], prev["loan_allowance"]]
    if None not in parts:
        provision = prev["loan_allowance"] - cur["loan_allowance"]
        d["funding_cost"] = -cur["interest_expense"] - cur["cost_provision_and_loan_funding"] - provision
        debt = lambda q: (q["short_term_borrowing"] or 0) + (q["bonds_short"] or 0) + (q["bonds_long"] or 0)
        debt_avg = avg(debt(prev), debt(cur))
        if debt_avg:
            d["funding_cost_pct"] = d["funding_cost"] * 4 / debt_avg * 100
    return {k: round(v, 3) for k, v in d.items()}


def reconcile(key_q, key_y):
    rows = []
    for period, figures in DATA_PACK.items():
        got = (key_y if period.startswith("FY") else key_q).get(period, {})
        for name, pack in figures.items():
            if name == "investment_income":
                a, b = got.get("rev_fvtpl"), got.get("rev_htm")
                filed = None if a is None or b is None else a + b
            else:
                filed = got.get(name)
            rows.append((period, name, pack, filed))
    return rows


if __name__ == "__main__":
    raw = {"metrics": fetch(f"{BASE}/metrics")}
    for section in SECTIONS:
        raw[section] = fetch(f"{BASE}?section={section}")
    pulled = datetime.date.today().isoformat()
    with open(os.path.join(OUT_DIR, "dnse_financials_raw.json"), "w", encoding="utf-8") as f:
        json.dump({"symbol": SYMBOL, "source": BASE, "pulled": pulled, "data": raw}, f, ensure_ascii=False)

    lines = line_catalogue(raw["metrics"])
    quarters = sorted({period_label(r) for s in SECTIONS for r in raw[s]["quarters"]}, key=period_key)
    years = sorted({period_label(r) for s in SECTIONS for r in raw[s]["years"]}, key=period_key)
    qv, yv = table(raw, lines, "quarters"), table(raw, lines, "years")
    nq = write_csv(os.path.join(OUT_DIR, "dnse_financials_quarterly.csv"), lines, qv, quarters)
    ny = write_csv(os.path.join(OUT_DIR, "dnse_financials_annual.csv"), lines, yv, years)

    key_q, key_y = key_lines(qv, quarters), key_lines(yv, years)
    derived = {p: derive(key_q[p], key_q[quarters[i - 1]] if i else None) for i, p in enumerate(quarters)}
    updated = {period_label(r): r.get("updateDate") for r in raw[IS]["quarters"] + raw[IS]["years"]}
    with open(os.path.join(OUT_DIR, "dnse_financials.json"), "w", encoding="utf-8") as f:
        json.dump({"symbol": SYMBOL, "source": BASE, "pulled": pulled, "definitions": DEFINITIONS,
                   "line_codes": {k: f"{s}.{c}" for k, (s, c) in KEY_LINES.items()},
                   "updated": updated, "quarterly": key_q, "half_year": half_years(key_q),
                   "annual": key_y, "derived": derived},
                  f, ensure_ascii=False, indent=1)

    print(f"quarters: {quarters[0]} to {quarters[-1]} ({len(quarters)}), years: {years[0]} to {years[-1]}")
    print(f"lines with data: {nq} quarterly, {ny} annual")
    print(f"latest quarter last updated by the source: {updated.get(quarters[-1])}")
    print("Wrote dnse_financials_raw.json, dnse_financials_quarterly.csv, "
          "dnse_financials_annual.csv, dnse_financials.json.\n")

    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    show = quarters[-8:]
    print(f"{'VND bn':34}" + "".join(f"{p:>9}" for p in show))
    for name in ["revenue", "rev_brokerage", "cost_brokerage", "rev_lending", "interest_expense",
                 "cost_provision_and_loan_funding", "admin_cost", "pbt", "loans", "equity",
                 "customer_cash_trading", "customer_securities_vsd"]:
        print(f"{name:34}" + "".join(f"{key_q[p][name]:9.1f}" if key_q[p][name] is not None else f"{'':>9}" for p in show))
    for name in ["brokerage_net", "pbt_margin_pct", "loans_to_equity_pct", "lending_yield_pct", "funding_cost_pct"]:
        print(f"{name:34}" + "".join(f"{derived[p][name]:9.1f}" if name in derived[p] else f"{'':>9}" for p in show))

    print("\nEarlier press and IR figures against the filings:")
    rows = reconcile(key_q, key_y)
    bad = [r for r in rows if r[3] is None or abs(r[2] - r[3]) > max(0.15, abs(r[2]) * 1e-4)]
    for period, name, pack, filed in bad:
        print(f"  differs: {period} {name}: press {pack}, filed {'missing' if filed is None else round(filed, 1)}")
    print(f"{len(rows)} values checked, {len(bad)} differ by more than rounding")

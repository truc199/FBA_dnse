"""Tables of the Round 3A deck, and the data behind its new figures.

Every table on a main slide has a CSV in outputs/round3/tables/slideNN_*.csv. The wording of a table is the
authors' and lives in data/round3/deck_tables/; numbers in braces, such as {m36_new}, are filled from the
cohort model, the review coding and the account data, so the deck cannot drift from the business case.
The script then writes each table into docs/doc_round3/deck_content.md, deck_appendix.md and the two
companion reports (report_round3A_en.md, report_round3A_vi.md) between the markers <!-- table: NAME -->
and <!-- /table -->, so edit the CSV, not the markdown table. The Vietnamese report reads vi/NAME tables,
translated cell by cell with data/round3/deck_tables_vi/cells_vi.csv (see vietnamese_tables).

It also writes the data the deck figures read (why_now_*, sizing_*, positioning_map, decision_tree,
ecosystem_roadmap) and fills nothing it cannot trace: constants quoted from a published source (77% of
investors find portfolio management hard; Nhan Dan, 2025) stay as text in the authored CSV.

Run: python src/round3/deck_tables.py   (after payday_model.py, plan_tables.py and reviews_2026.py)
"""
import csv
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import payday_model as M  # noqa: E402

sys.path.insert(0, str(HERE.parent))
import analysis as A  # noqa: E402  (Round 2 review rules; read only)

ROOT = HERE.parents[1]
TEMPLATES = M.DATA_R3 / "deck_tables"
TEMPLATES_VI = M.DATA_R3 / "deck_tables_vi"
MANUAL = ROOT / "data" / "manual"
DECK = ROOT / "docs" / "doc_round3" / "deck_content.md"
APPENDIX = ROOT / "docs" / "doc_round3" / "deck_appendix.md"
REPORTS = [ROOT / "docs" / "doc_round3" / f"report_round3A_{lang}.md" for lang in ("en", "vi")]
MINUS = "−"
# tables of the Vietnamese report, translated cell by cell from the English CSVs (vietnamese_tables)
VI_TABLES = ["slide05_what_changed", "slide06_personas", "report_value", "slide04_insight_design", "report_features",
             "slide07_glide_path", "appG3_trust_metrics", "appE1_legal", "slide08_moments_of_truth",
             "slide09_failure_handling", "appC1_competitors", "slide11_scenarios", "appB1_unit_economics",
             "appB3_levers", "appB4_stress", "slide12_gtm", "slide13_roadmap", "appB6_pilot_power", "appB7_gates",
             "appB9_raci", "appB8_risks", "slide15_board_ask", "appA1_data_sources", "appA2_methods",
             "appB2_phase_budget", "appB5_tiers", "appD1_review_causes", "appD2_reviews_by_month", "appG2_journey",
             "appH1_assumptions", "appI1_qa"]
NUMBER = re.compile(r"(?<![\w.,])\d(?:[\d,.]*\d)?(?!\w)")
SLOT = "⟦{}⟧"


def read(path):
    with open(path, encoding="utf-8-sig") as f:
        return list(csv.DictReader(f))


def read_rows(path):
    with open(path, encoding="utf-8-sig") as f:
        return list(csv.reader(f))


def out(name):
    return read(M.TABLES_R3 / name)


def write_rows(name, rows):
    """Write a table given as a header row plus data rows, keeping column order and blank header cells."""
    M.TABLES_R3.mkdir(parents=True, exist_ok=True)
    with open(M.TABLES_R3 / name, "w", encoding="utf-8", newline="") as f:
        csv.writer(f).writerows(rows)
    print(f"  wrote outputs/round3/tables/{name}")


def pct(x, d=0):
    return f"{x * 100:.{d}f}%"


def signed_bn(v):
    return f"{MINUS if v < 0 else '+'}VND {abs(v):.1f} billion"


def round_to(v, step):
    return f"{round(v / step) * step:,.0f}"


def accounts():
    rows = {r["metric"]: float(r["value"]) for r in read(MANUAL / "dnse_accounts.csv") if r["date"].startswith("2025")}
    return rows["accounts_year_end"], rows["net_assets_10m_plus"]


def trust_share_h1_2025():
    """Trust themes in DNSE's negative Google Play reviews, January to June 2025, by the Round 2 keyword rule."""
    neg = A.negatives("vn.com.encapital.arrow", "2025-01-01", "2025-06-30")
    return sum(1 for r in neg if A.themes(r) & A.TRUST) / len(neg)


def key_numbers():
    rows_csv = M.load_assumptions()
    runs = {s: M.scenario(s, rows_csv) for s in M.SCENARIOS}
    p, sched, res, m = runs["base"]
    _, g = M.decision_gates(rows_csv, runs)
    need, ask = M.board_ask(res, p)
    m12, m24, m36 = res[11], res[23], res[35]
    low24 = runs["low"][2][23]
    by_ch = {c: sum(r[f"enrolled_{c}"] for r in res[:36]) for c in M.CHANNELS}
    total36 = sum(by_ch.values())
    acc, funded10 = accounts()
    reviews = {r["cause"]: r for r in out("reviews_2026_cause_summary.csv")}
    by_code = {r["code"]: r for r in out("reviews_2026_cause_summary.csv") if r["code"] != "group"}
    bal, _ = M.saver_balance(p, 60)
    months_to_10m = next(i + 1 for i, b in enumerate(bal) if b >= p["balance_threshold"])
    tier = out("payday_tier_breakeven.csv")[0]
    power = {r["pilot_accounts"]: r for r in out("payday_pilot_power.csv")}[f"{p['pilot_accounts']:.0f}"]
    eligible = p["dormant_accounts"] * p["eligible_share_dormant"]
    k = {
        "ask": f"{ask / 1e9:.1f}", "need": f"{need / 1e9:.1f}", "contingency": pct(p["contingency_share"]),
        "m36_new": f"{m36['new_accounts_above_10m']:,.0f}", "m24_new": f"{m24['new_accounts_above_10m']:,.0f}",
        "m36_total_10m_r": round_to(funded10 + m36["new_accounts_above_10m"], 1000),
        "funded_2025": f"{funded10:,.0f}", "below10m_pct": pct(1 - funded10 / acc),
        "cpa_plan": f"{g['cost_per_account_plan_m60'] / 1e6:.2f}",
        "cpa_plan_1d": f"{g['cost_per_account_plan_m60'] / 1e6:.1f}",
        "cpa_scale": f"{1.25 * g['cost_per_account_plan_m60'] / 1e6:.1f}",
        "cpa_stop": f"{2 * g['cost_per_account_plan_m60'] / 1e6:.1f}",
        "ceiling_r": round_to(g["cac_ceiling_60m"], 1000), "ceiling_no_fee_r": round_to(g["ceiling_no_fee"], 1000),
        "fee_base": f"{p['fee_per_contribution']:,.0f}", "fee_limit_r": round_to(g["fee_limit"], 100),
        "revenue_per_m": f"{M.net_yield(p) * 1e6 / 12:,.0f}",
        "enrol_scale": pct(1.5 * g["breakeven_enrolment"], 1), "enrol_stop": pct(g["breakeven_enrolment"], 1),
        "breakeven": pct(g["breakeven_enrolment"], 1),
        "persist_scale": pct(g["persistence_3_base"]), "persist_stop": "60%", "gate_on_time": "99.5%",
        "m12_funded_80": f"{0.8 * m12['funded_savers']:,.0f}", "m12_funded_50": f"{0.5 * m12['funded_savers']:,.0f}",
        "m12_bal_80": f"{0.8 * m12['balance'] / 1e9:.1f}",
        "m24_new_80": f"{0.8 * m24['new_accounts_above_10m']:,.0f}",
        "m24_new_low": f"{low24['new_accounts_above_10m']:,.0f}",
        "emp_part": pct(g["employer_participation_needed"]), "emp_stop": pct(p["participation_employer"]),
        "months_to_10m": f"{months_to_10m}",
        "pilot": f"{p['pilot_accounts']:,.0f}", "pilot_arm": f"{p['pilot_accounts'] / 3:,.0f}",
        "mde": power["tier_effect_detectable_points"],
        "tier_cost_pct": f"{float(tier['reward_cost_pct_of_pv_revenue']):.0f}%",
        "dormant_m": f"{p['dormant_accounts'] / 1e6:.2f}", "active": f"{p['active_customers']:,.0f}",
        "new_per_month": f"{p['new_accounts_per_month']:,.0f}", "eligible": f"{eligible:,.0f}",
        "eligible_share": pct(p["eligible_share_dormant"]), "conv_dormant": pct(p["conv_dormant"]),
        "conv_active": pct(p["conv_active"]), "conv_new": pct(p["conv_new_account"]),
        "sav_dormant": f"{by_ch['dormant_pilot'] + by_ch['dormant_rollout']:,.0f}",
        "sav_active": f"{by_ch['active_customers']:,.0f}", "sav_new": f"{by_ch['new_accounts']:,.0f}",
        "sav_employers": f"{by_ch['employers']:,.0f}", "sav_total": f"{total36:,.0f}",
        "share_new": pct(by_ch["new_accounts"] / total36),
        "broke_pct": f"{float(reviews['Something broke (any of the first five causes)']['both_pct']):.0f}%",
        "trust_hand_pct": f"{float(reviews['Fees, terms, scam claims or rewards']['both_pct']):.0f}%",
        "ekyc_pct": f"{float(by_code['ekyc_opening']['both_pct']):.0f}%",
        "cash_pct": f"{float(by_code['cash_not_credited']['both_pct']):.0f}%",
        "accounts_m": f"{acc / 1e6:.2f}",
        "trust_h1_2025": pct(trust_share_h1_2025()),
    }
    # appendix figures: stress test, own-bond option, lending option, downside cost, counts
    def row_starting(table, col, prefix):
        return next(r for r in out(table) if r[col].startswith(prefix))

    stress = row_starting("payday_stress.csv", "case", "Market fall")
    own_bonds = row_starting("payday_levers.csv", "case", "DNSE's own bonds")
    base_lever = row_starting("payday_levers.csv", "case", "Base case")
    scen = {r["scenario"]: r for r in out("payday_scenarios.csv")}
    lend = {r["scenario"]: r for r in out("payday_option_lending.csv")}
    k.update({
        "stress_market_pct": f"{abs(float(stress['change_accounts_m36_pct'])):.1f}%",
        "stress_market_cash": f"{abs(float(stress['change_cum_cash_m60_vnd_bn'])):.2f}",
        "d7_gain": f"{float(own_bonds['cum_cash_m60_vnd_bn']) - float(base_lever['cum_cash_m60_vnd_bn']):.1f}",
        "npv_base": signed_bn(float(scen["base"]["npv_60m_vnd_bn"])),
        "npv_lending": signed_bn(float(lend["base"]["npv_60m_vnd_bn"])),
        "cpa_low": f"{float(scen['low']['m60_net_cost_per_new_10m_account_vnd_m']):.1f}",
        "n_sources": f"{len(read(M.DATA_R3 / 'sources_round3.csv'))}",
        "n_tests": f"{sum(r['pass'] == 'yes' for r in out('payday_test_check.csv'))}",
    })
    return k, runs, by_ch, total36, eligible


def fill_template(name, k):
    rows = read_rows(TEMPLATES / f"{name}.csv")
    filled = [[cell.format(**k) for cell in row] for row in rows]
    write_rows(f"{name}.csv", filled)
    return filled


def scenario_rows(k):
    s = {r["scenario"]: r for r in out("payday_scenarios.csv")}
    vals = {}
    for sc in ("low", "base", "high"):
        r = s[sc]
        cpa = float(r["m60_net_cost_per_new_10m_account_vnd_m"])
        vals.update({f"need_c_{sc}": f"{float(r['phase_0_1_with_contingency_vnd_bn']):.1f}",
                     f"m36_new_{sc}": f"{float(r['m36_new_accounts_above_10m']):,.0f}",
                     f"npv_{sc}": signed_bn(float(r["npv_60m_vnd_bn"])),
                     f"payback_{sc}": r["payback_month"] or "None",
                     f"cpa60_{sc}": f"VND {cpa:.2f} million" if cpa > 0 else "0"})
    return {**k, **vals}


def gtm_rows(k):
    q = {r["quarter"]: r for r in out("gtm_year1.csv")}
    vals = {}
    for i in range(1, 5):
        r = q[f"Q{i}"]
        vals[f"q{i}_funded"] = f"{float(r['funded_savers_end']):,.0f}"
        bal = float(r["balance_end_vnd_bn"])
        vals[f"q{i}_bal"] = f"VND {bal:.1f} bn" if bal > 0 else "0"
        vals[f"q{i}_cost"] = f"{float(r['cost_vnd_bn']):.1f}"
    return {**k, **vals}


def roadmap_rows(k):
    ph = out("roadmap_phases.csv")
    cash0 = float(ph[0]["cumulative_cash_at_end_vnd_bn"])
    return {**k, "p0_cash": f"{MINUS}VND {abs(cash0):.1f} billion",
            "p1_savers": f"{float(ph[1]['savers_enrolled_by_end']):,.0f}",
            "p2_funded": f"{float(ph[2]['funded_savers_at_end']):,.0f}",
            "p3_new": f"{float(ph[3]['new_accounts_above_10m_at_end']):,.0f}",
            "p4_new": f"{float(ph[4]['new_accounts_above_10m_at_end']):,.0f}"}


def glide_rows():
    rows = [["Goal horizon", "Golden Egg (Trứng Vàng), bank bonds", "Bond funds", "Equity funds", "VN30 ETF"]]
    for r in out("glide_path.csv"):
        cells = [r["golden_egg_bank_bonds_pct"], r["bond_funds_pct"], r["equity_funds_pct"], r["vn30_etf_pct"]]
        if all(c.replace(".", "").isdigit() for c in cells):
            cells = [f"{float(c):.0f}%" if float(c) > 0 else "–" for c in cells]
        else:
            cells = ["New money only, into Golden Egg"] + ["Nothing sold"] * 3
        rows.append([r["goal_horizon"].replace(" date", ""), *cells])
    return rows


def competitor_rows():
    rows = [["Product", "Assets", "Minimum", "Who decides", "Fee"]]
    for r in read(M.DATA_R3 / "competitors.csv"):
        if r["in_table"] == "yes":
            rows.append([r["product"], r["assets"], r["minimum_label"], r["who_decides"], r["fee"]])
    return rows


def figure_data(k, runs, by_ch, total36, eligible):
    write_rows("why_now_events.csv", read_rows(M.DATA_R3 / "why_now_events.csv"))
    cash = [["quarter", "investor_cash_vnd_trillion", "source"]]
    cash += [[r["quarter"], r["investor_cash_vnd_trillion"], r["source"]]
             for r in read(MANUAL / "industry_investor_cash.csv") if r["investor_cash_vnd_trillion"]]
    write_rows("why_now_investor_cash.csv", cash)
    p = runs["base"][0]
    acc, _ = accounts()
    contacted = p["pilot_accounts"] * p["pilot_treated_share"] + (eligible - p["pilot_accounts"])
    dormant_savers = by_ch["dormant_pilot"] + by_ch["dormant_rollout"]
    write_rows("sizing_funnel.csv", [
        ["stage", "accounts", "step", "basis"],
        ["DNSE accounts, December 2025", f"{acc:.0f}", "", "DNSE Securities (2026c)"],
        ["Used no product in December 2025", f"{p['dormant_accounts']:.0f}", pct(p["dormant_accounts"] / acc, 1),
         "Accounts less active customers"],
        ["Salaried and reachable", f"{eligible:.0f}", pct(p["eligible_share_dormant"]), "Assumption"],
        ["Dormant savers by month 36", f"{dormant_savers:.0f}", pct(dormant_savers / contacted, 1) + " of contacted",
         "Assumption (pilot measures it)"],
    ])
    labels = [("new_accounts", "Account opening"), ("dormant", "Dormant accounts"),
              ("active_customers", "Active customers"), ("employers", "Employers")]
    vals = {"dormant": by_ch["dormant_pilot"] + by_ch["dormant_rollout"], **by_ch}
    write_rows("savers_by_channel.csv", [["channel", "savers_month_36", "share"]] +
               [[lab, f"{vals[key]:.0f}", pct(vals[key] / total36, 1)] for key, lab in labels] +
               [["Total", f"{total36:.0f}", "100.0%"]])
    write_rows("positioning_map.csv", [["label", "asset_types", "minimum_vnd", "payday", "source_ids"]] +
               [[r["map_label"], r["asset_types"], r["minimum_vnd"], "yes" if r["product"].startswith("Payday") else "no",
                 r["source_ids"]] for r in read(M.DATA_R3 / "competitors.csv") if r["on_map"] == "yes"])
    tree = read_rows(M.DATA_R3 / "decision_tree.csv")
    write_rows("decision_tree.csv", [[c.format(**k) for c in row] for row in tree])
    write_rows("ecosystem_roadmap.csv", read_rows(M.DATA_R3 / "ecosystem_roadmap.csv"))


# ---------------------------------------------------------------- appendix tables
def vnd(v, unit=None):
    v = float(v)
    sign = MINUS if v < 0 else ""
    a = abs(v)
    if unit == "bn" or (unit is None and a >= 1e9):
        return f"{sign}VND {a / 1e9:.2f} billion"
    if unit == "m" or (unit is None and a >= 1e6):
        return f"{sign}VND {a / 1e6:,.1f} million"
    return f"{sign}VND {a:,.0f}"


def unit_economics_rows():
    want = [("Net yield on plan balances, % a year", "Net yield on plan balances, a year", "pct2"),
            ("Revenue a year on VND 10 million of balance, VND", "Revenue a year on VND 10 million of balance", "vnd"),
            ("Savers still contributing after 3 contributions, %", "Still contributing after 3 contributions", "pct1"),
            ("Savers still contributing after 6 contributions, %", "Still contributing after 6 contributions", "pct1"),
            ("Savers still contributing after 12 contributions, %", "Still contributing after 12 contributions", "pct1"),
            ("Contributions in a row to pass VND 10 million", "Contributions in a row to pass VND 10 million", "int"),
            ("CAC ceiling (PV of net revenue per saver), 60 months, VND", "CAC ceiling: PV of net revenue per saver, 60 months", "vnd"),
            ("Acquisition cost per saver, dormant accounts, pilot, VND", "Acquisition cost per dormant saver", "vnd"),
            ("Reach cost per dormant account contacted, VND", "Reach cost per dormant account contacted", "vnd"),
            ("Break-even enrolment rate of contacted accounts, 60-month ceiling, %",
             "Break-even enrolment of contacted accounts", "pct2")]
    rows = {r["measure"]: r for r in out("payday_unit_economics.csv")}
    table = [["Measure", "Downside", "Base", "Upside"]]
    for key, label, kind in want:
        cells = []
        for sc in ("low", "base", "high"):
            v = rows[key][sc]
            if v in ("", None):
                cells.append("not reached")
            elif kind == "pct2":
                cells.append(f"{float(v):.2f}%")
            elif kind == "pct1":
                cells.append(f"{float(v):.1f}%")
            elif kind == "int":
                cells.append(f"{float(v):.0f}")
            else:
                cells.append(vnd(v, "vnd"))
        table.append([label, *cells])
    return table


def phase_budget_rows():
    table = [["Phase", "Months", "Cost", "of which build", "Revenue", "Cumulative cash at end"]]
    for r in out("payday_phase_budget.csv"):
        if r["scenario"] == "base":
            table.append([r["phase"], r["months"].replace("-", "–"), f"{float(r['cost_vnd_bn']):.2f}",
                          f"{float(r['of_which_build_vnd_bn']):.2f}", f"{float(r['revenue_vnd_bn']):.2f}",
                          f"{float(r['cumulative_cash_at_end_vnd_bn']):.2f}".replace("-", MINUS)])
    return table


def levers_rows():
    table = [["Case", "Net cost per new funded account, month 60 (VND million)", "Cumulative cash, month 60 (VND billion)",
              "NPV (VND billion)", "Break-even month"]]
    for r in out("payday_levers.csv"):
        table.append([r["case"], f"{float(r['net_cost_per_new_10m_account_m60_vnd_m']):.2f}",
                      f"{float(r['cum_cash_m60_vnd_bn']):.1f}".replace("-", MINUS),
                      f"{float(r['npv_60m_vnd_bn']):.1f}".replace("-", MINUS), r["breakeven_month"] or "none"])
    return table


def stress_rows():
    def signed(x, d):
        v = round(float(x), d)
        return f"{0.0 if v == 0 else v:.{d}f}".replace("-", MINUS)  # no "−0.0" for the base case

    table = [["Case", "New accounts above VND 10 million, month 36", "Change", "Change in month-60 cash (VND billion)"]]
    for r in out("payday_stress.csv"):
        table.append([r["case"], f"{float(r['new_accounts_above_10m_m36']):,.0f}",
                      signed(r["change_accounts_m36_pct"], 1) + "%", signed(r["change_cum_cash_m60_vnd_bn"], 2)])
    return table


def tier_rows():
    table = [["Bank fee", "Reward design", "Reward cost, % of revenue", "CAC ceiling", "12-contribution rate needed"]]
    for r in out("payday_tier_breakeven.csv"):
        need = r["twelve_contribution_rate_needed_pct"]
        table.append([r["bank_fee"].capitalize(), r["design"], f"{float(r['reward_cost_pct_of_pv_revenue']):.1f}%",
                      vnd(r["cac_ceiling_60m_vnd"], "vnd"), need + ("%" if need.replace(".", "").isdigit() else "")])
    return table


def pilot_rows():
    table = [["Pilot accounts", "Savers per treated arm", "Enrolment, 95% interval", "Smallest detectable gain (points)",
              "Outreach cost (VND million)"]]
    for r in out("payday_pilot_power.csv"):
        table.append([f"{float(r['pilot_accounts']):,.0f}", r["savers_per_treated_arm"],
                      f"{r['enrolment_95ci_low_pct']}–{r['enrolment_95ci_high_pct']}%", r["tier_effect_detectable_points"],
                      r["outreach_cost_vnd_m"]])
    return table


def gates_rows():
    table = [["Gate", "Measure", "Scale if", "Adjust if", "Stop if", "Owner"]]
    sym = lambda s: s.replace(">=", "≥").replace("<=", "≤")  # noqa: E731
    for r in out("payday_decision_gates.csv"):
        table.append([r["gate"], r["measure"], sym(r["scale_if"]), sym(r["adjust_if"]), sym(r["stop_if"]), r["owner"]])
    return table


def risk_rows():
    table = [["ID", "Risk", "Likelihood × impact", "Mitigation", "Early warning", "Owner"]]
    for r in out("risk_register.csv"):
        table.append([r["id"], r["risk"], f"{r['likelihood']} × {r['impact']} = {r['score']}", r["mitigation"],
                      r["early_warning"], r["owner"]])
    return table


def plain_rows(name, header=None):
    rows = read_rows(M.TABLES_R3 / name)
    if header:
        rows[0] = header
    return rows


def review_rows():
    table = [["Cause", "Google Play", "App Store", "Both stores", "95% interval"]]
    for r in out("reviews_2026_cause_summary.csv"):
        if r["code"] == "n":
            continue
        ci = f"{r['both_ci95_low']}–{r['both_ci95_high']}%" if r["both_ci95_low"] else ""
        table.append([r["cause"], f"{r['google_play_n']} ({float(r['google_play_pct']):.0f}%)",
                      f"{r['app_store_n']} ({float(r['app_store_pct']):.0f}%)",
                      f"{r['both_n']} ({float(r['both_pct']):.0f}%)", ci])
    n = next(r for r in out("reviews_2026_cause_summary.csv") if r["code"] == "n")
    table.append(["Negative reviews coded", n["google_play_n"], n["app_store_n"], n["both_n"], ""])
    return table


def review_month_rows():
    table = [["Month", "Negative reviews", "Something broke", "Posted 4–5 March"]]
    for r in out("reviews_2026_by_month.csv"):
        table.append([r["month"], r["total"], r["something_broke"], r["outage_4_5_march"]])
    return table


def quote_rows():
    table = [["What the customer wrote (authors' translation)", "Review"]]
    for r in out("reviews_2026_quotes.csv"):
        table.append([r["quote_en"], r["attribution"].replace("; authors' translation", "")])
    return table


ASSUMPTION_ROWS = [
    ("dormant_accounts", "Dormant accounts (used no product, Dec 2025)", "int", "DNSE Securities (2026c)"),
    ("eligible_share_dormant", "Share of dormant accounts salaried and reachable", "pct", "World Bank (2025); pilot survey"),
    ("pilot_accounts", "Pilot accounts (three arms)", "int", "Decision D4"),
    ("conv_dormant", "Enrolment of contacted dormant accounts", "pct", "Never-Sleeping Account reached 0.8% of accounts; TCBS (2026)"),
    ("conv_active", "Enrolment of active customers over 12 months", "pct", "Never-Sleeping Account sign-ups equal 14% of active customers"),
    ("new_accounts_per_month", "New accounts a month", "int", "DNSE Securities (2026c); VnExpress (2026a)"),
    ("conv_new_account", "Set-up within 60 days of opening", "pct", "Assumption"),
    ("employers_per_quarter", "Employers signed a quarter", "int", "Go-to-market plan"),
    ("participation_employer", "Employees who enrol after an HR session", "pct", "Ashraf et al. (2006) as upper bound"),
    ("contribution", "Monthly contribution", "vnd", "About 11% of the VND 9.0 million average income (National Statistics Office, 2026)"),
    ("stop_rate_first_90_days", "Stop rate, 2nd and 3rd contributions (a month)", "pct1", "Assumption; pilot measures it"),
    ("stop_rate_monthly", "Stop rate after the 3rd contribution (a month)", "pct1", "Assumption; pilot measures it"),
    ("withdrawal_rate_annual", "Balances withdrawn a year", "pct", "Assumption; inflows tagged"),
    ("yield_golden_egg", "DNSE margin on bank bonds in Golden Egg", "pct2", "Thi truong Tai chinh Tien te (2026a); DNSE Securities (n.d.-b)"),
    ("yield_bond_funds", "Distributor share of bond-fund fees", "pct2", "SSI Asset Management (2026); VCBF (2026); fund prospectuses"),
    ("yield_equity_funds", "Distributor share of equity-fund fees", "pct2", "Fund prospectuses and factsheets, 2026"),
    ("build_cost_team", "Build team, months 1 to 6", "bn", "ITviec (2025) salary medians"),
    ("build_cost_external", "Integration, security tests, legal opinions", "bn", "VPBank (2024); assumption"),
    ("run_cost_team", "Running team, a year", "bn", "ITviec (2025) salary medians"),
    ("run_cost_other", "Operations, compliance and cloud, a year", "bn", "Assumption"),
    ("marketing_fixed_annual", "Content and promotion review, a year", "bn", "Assumption"),
    ("reach_cost_per_account", "Reach cost per dormant account contacted", "vnd", "Zalo Business Solutions (n.d.); MobiFone (n.d.)"),
    ("fee_per_contribution", "Bank fee per contribution", "vnd", "VPBank (2024) list price"),
    ("service_cost_per_active_month", "Service cost per active saver a month", "vnd", "Zalo confirmation, statements"),
    ("discount_rate_annual", "Discount rate", "pct", "Hurdle rate"),
]


def assumption_rows():
    rows = {r["param"]: r for r in M.load_assumptions()}
    table = [["Assumption", "Downside", "Base", "Upside", "Type", "Basis"]]
    for key, label, kind, basis in ASSUMPTION_ROWS:
        r = rows[key]
        cells = []
        for col in ("low", "base", "high"):
            v = float(r[col])
            cells.append({"int": f"{v:,.0f}", "pct": f"{v * 100:.0f}%", "pct1": f"{v * 100:.1f}%",
                          "pct2": f"{v * 100:.2f}%", "vnd": f"VND {v:,.0f}", "bn": f"VND {v / 1e9:.2f} billion"}[kind])
        table.append([label, *cells, r["type"], basis])
    mix = [rows[f"mix_{a}"]["base"] for a in ("golden_egg", "bond_funds", "equity_funds", "etf")]
    table.append(["Asset mix: Golden Egg / bond funds / equity funds / ETF", "same", "/".join(f"{float(m) * 100:.0f}" for m in mix),
                  "same", "assumption", "Design: glide path by goal horizon"])
    return table


def appendix_tables(k):
    tables = {name: fill_template(name, k) for name in
              ("appA1_data_sources", "appA2_methods", "appC1_competitors", "appF1_feedback", "appI1_qa",
               "report_value", "report_features")}
    generated = {
        "appB1_unit_economics": unit_economics_rows(), "appB2_phase_budget": phase_budget_rows(),
        "appB3_levers": levers_rows(), "appB4_stress": stress_rows(), "appB5_tiers": tier_rows(),
        "appB6_pilot_power": pilot_rows(), "appB7_gates": gates_rows(), "appB8_risks": risk_rows(),
        "appB9_raci": plain_rows("raci.csv", ["Activity", "CEO", "CFO", "CTO", "Head of Product", "Compliance and Legal",
                                              "Marketing and CRM", "Customer Service", "Licensed adviser"]),
        "appD1_review_causes": review_rows(), "appD2_reviews_by_month": review_month_rows(),
        "appD3_quotes": quote_rows(),
        "appE1_legal": plain_rows("legal_map.csv", ["Requirement", "Rule", "Design response", "Status"]),
        "appG2_journey": plain_rows("journey_map.csv"),
        "appG3_trust_metrics": plain_rows("trust_metrics.csv", ["Commitment", "Customer sees", "Published metric", "Target",
                                                                "Cadence", "Owner"]),
        "appH1_assumptions": assumption_rows(),
    }
    generated["appG2_journey"][0][0] = ""
    for name, rows in generated.items():
        write_rows(f"{name}.csv", rows)
    return {**tables, **generated}


def vi_num(token):
    """English number format to Vietnamese: 1,234.5 becomes 1.234,5. A version such as 2.113.28 is kept."""
    if token.count(".") > 1 and "," not in token:
        return token
    return token.translate(str.maketrans(",.", ".,"))


def cell_pattern(cell):
    """A cell with its numbers replaced by numbered slots, so a translation survives a change in the model."""
    nums = []

    def slot(m):
        nums.append(m.group(0))
        return SLOT.format(len(nums) - 1)
    return NUMBER.sub(slot, cell), nums


def vi_quote_rows():
    """The review quotes of Appendix C in the customers' own words, from the review files; swear words masked."""
    swear = re.compile(r"\b(bòi|đéo|lol)\b", re.I)
    table = [["Khách hàng viết (nguyên văn, từ tục được che bằng _)", "Review"]]
    for r in out("reviews_2026_quotes.csv"):
        y, m, d = r["date"].split("-")
        version = f", bản {r['app_version']}" if r["app_version"] else ""
        text = swear.sub(lambda w: w.group(0)[0] + "_" * (len(w.group(0)) - 1), r["original_vi"])
        table.append([text, f"{r['store']}, {r['stars']} sao, {d}/{m}/{y}{version}"])
    return table


def vietnamese_tables(tables):
    """Vietnamese copies of the report tables in outputs/round3/tables/vi/.

    Each English cell, with its numbers set aside, is looked up in data/round3/deck_tables_vi/cells_vi*.csv
    (a row with a table name overrides a row without one); the numbers go back in Vietnamese format. Cells
    with no letters and short codes such as R1, A or C are kept. A cell without a translation stays in English
    and is listed in vi/untranslated.csv, which check_deck_content.py reports as an error.
    """
    cmap = {(r["table"], r["en"]): r["vi"] for path in sorted(TEMPLATES_VI.glob("cells_vi*.csv")) for r in read(path)}
    out_dir = M.TABLES_R3 / "vi"
    out_dir.mkdir(parents=True, exist_ok=True)
    missing, result = [], {}

    def translate(name, cell):
        if not re.search(r"[A-Za-z]", cell) or re.fullmatch(r"[A-Z]{1,2}\d{0,2}(?:/[A-Z])?", cell):
            return NUMBER.sub(lambda m: vi_num(m.group(0)), cell)
        pattern, nums = cell_pattern(cell)
        vi = cmap.get((name, pattern), cmap.get(("", pattern)))
        if vi is None:
            missing.append((name, pattern))
            return cell
        for i, n in enumerate(nums):
            vi = vi.replace(SLOT.format(i), vi_num(n))
        return vi

    for name in VI_TABLES:
        result[f"vi/{name}"] = [[translate(name, c) for c in row] for row in tables[name]]
    result["vi/appD3_quotes"] = vi_quote_rows()
    result["vi/appF1_feedback"] = read_rows(TEMPLATES_VI / "appF1_feedback.csv")
    for name, rows in result.items():
        with open(M.TABLES_R3 / f"{name}.csv", "w", encoding="utf-8", newline="") as f:
            csv.writer(f).writerows(rows)
    with open(out_dir / "untranslated.csv", "w", encoding="utf-8", newline="") as f:
        csv.writer(f).writerows([["table", "en"], *dict.fromkeys(missing)])
    print(f"  wrote {len(result)} Vietnamese tables to outputs/round3/tables/vi/"
          + (f"; {len(set(missing))} cells without a translation (vi/untranslated.csv)" if missing else ""))
    return result


def markdown(rows):
    head, body = rows[0], rows[1:]
    esc = lambda c: c.replace("|", "\\|")  # noqa: E731
    lines = ["| " + " | ".join(esc(c) for c in head) + " |", "|" + "---|" * len(head)]
    lines += ["| " + " | ".join(esc(c) for c in r) + " |" for r in body]
    return "\n".join(lines)


def render_into(path, tables):
    """Replace each table block of a deck file with its CSV, so the markdown matches the CSV."""
    md = path.read_text(encoding="utf-8")
    seen = set()

    def swap(match):
        name = match.group(1)
        if name not in tables:
            sys.exit(f"{path.name}: no table named {name}")
        seen.add(name)
        return f"<!-- table: {name} -->\n{markdown(tables[name])}\n<!-- /table -->"

    new = re.sub(r"<!-- table: (\S+) -->\n.*?<!-- /table -->", swap, md, flags=re.S)
    path.write_text(new, encoding="utf-8")
    print(f"  rendered {len(seen)} tables into docs/doc_round3/{path.name}")
    return seen


def main():
    k, runs, by_ch, total36, eligible = key_numbers()
    tables = {}
    for name in ("slide01_key_figures", "slide04_insight_design", "slide05_what_changed", "slide06_personas",
                 "slide08_moments_of_truth", "slide09_failure_handling", "slide14_gates"):
        tables[name] = fill_template(name, k)
    for name, kk in (("slide11_scenarios", scenario_rows(k)), ("slide12_gtm", gtm_rows(k)),
                     ("slide13_roadmap", roadmap_rows(k)), ("slide15_board_ask", k)):
        tables[name] = fill_template(name, kk)
    tables["slide07_glide_path"] = glide_rows()
    tables["slide10_competitors"] = competitor_rows()
    for name in ("slide07_glide_path", "slide10_competitors"):
        write_rows(f"{name}.csv", tables[name])
    figure_data(k, runs, by_ch, total36, eligible)
    tables.update(appendix_tables(k))
    tables.update(vietnamese_tables(tables))
    used = set()
    for path in (DECK, APPENDIX, *REPORTS):
        if path.exists():
            used |= render_into(path, tables)
    unused = sorted(set(tables) - used)
    if unused:
        print(f"  tables without a marker in the deck or report files: {', '.join(unused)}")


if __name__ == "__main__":
    main()

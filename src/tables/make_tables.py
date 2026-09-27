"""Recompute every data-driven table of the report from data/ and write it to outputs/tables/computed/.

Each computed table has the layout, labels and number format of the published table, and the same file name
as the published table that src/tables/export_tables.py writes to outputs/tables/, so that
src/tables/check_tables.py can compare the two cell by cell. Tables written by the authors (design tables,
source lists, translated quotes, the assessment of proposals) have no computed counterpart.

Tables recomputed here: A2 (filings column), A3, A4, B1, B2, B3, C1, C2, D1, D2, E1, E2 and F5.
"""
import csv
import sys
from decimal import Decimal, ROUND_HALF_UP
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import analysis as AN  # noqa: E402
from config import ROOT, TABLES  # noqa: E402

OUT = TABLES / "computed"


# ------------------------------------------------------------------ helpers
def write(name, rows):
    OUT.mkdir(parents=True, exist_ok=True)
    with open(OUT / name, "w", newline="", encoding="utf-8") as f:
        csv.writer(f).writerows(rows)
    print("  wrote", (OUT / name).relative_to(ROOT))


def num(x, d=1):
    """Thousands separators and d decimals (ordinary rounding of the stored value)."""
    return f"{x:,.{d}f}"


def neg(x, d=1):
    """As num(), with negative values in parentheses (Table B1)."""
    return f"({num(-x, d)})" if x < 0 else num(x, d)


def half_up(x, d=0):
    """Round to d + 1 decimals, then half up to d decimals (1,660.48 -> 1,660.5 -> 1,661)."""
    q = Decimal(str(round(x, d + 1))).quantize(Decimal(1).scaleb(-d), rounding=ROUND_HALF_UP)
    return f"{q:,}"


# ------------------------------------------------------------------ Appendix A
def table_A2():
    """Press figures against the filings; the press column is data/manual/press_figures.csv."""
    growth = AN.v(AN.A["FY2025"], "revenue") / AN.v(AN.A["FY2024"], "revenue") * 100 - 100
    filings = {"pbt_2026Q2": num(AN.v(AN.Q["2026Q2"], "pbt")), "pbt_2026H1": num(AN.v(AN.H["2026H1"], "pbt")),
               "revenue_FY2025": num(AN.v(AN.A["FY2025"], "revenue")), "revenue_growth_FY2025": f"{growth:.1f}%"}
    rows = [["Item", "Press or earlier data pack", "Filings used", "Reason for the difference"]]
    for r in AN.manual("press_figures.csv"):
        rows.append([r["item"], r["press_figure"], filings.get(r["filings_measure"], "not used"), r["reason"]])
    write("table_A2_press_figures_reconciled_with_the_filings_vnd_billion.csv", rows)


def table_A3():
    R = AN.load_json("reviews_tables.json")
    play = [dict(zip(R["CLEANING_HEADER"], r)) for r in R["CLEANING_LOG"]]
    ios = [dict(zip(R["IOS_CLEANING_HEADER"], r)) for r in R["IOS_CLEANING_LOG"]]
    cols = play + ios
    short = lambda app: app.split()[0]
    head = ["Stage"] + [f"{short(c['app'])}, Play" for c in play] + [f"{short(c['app'])}, iOS" for c in ios]
    lines = [("Reviews retrieved", "retrieved"), ("Loan advertising removed", "loan_spam"),
             ("Referral farming removed", "referral_spam"), ("Duplicates removed", "duplicates"),
             ("Reviews retained", "retained")]
    rows = [head] + [[lab] + [f"{c[k]:,}" for c in cols] for lab, k in lines]
    rows += [["Mean rating before cleaning"] + [f"{c['raw_mean']:.2f}" for c in cols],
             ["Mean rating after cleaning"] + [f"{c['clean_mean']:.2f}" for c in cols]]
    write("table_A3_review_cleaning_log.csv", rows)


def table_A4():
    R = AN.load_json("reviews_tables.json")
    by_year = {r[0]: dict(zip(R["GENERIC_SENSITIVITY_HEADER"], r)) for r in R["GENERIC_SENSITIVITY"]}
    rows = [["Rule for a generic review", "Generic share, 2024", "Generic share, 2025",
             "Substantive mean, 2024", "Substantive mean, 2025"]]
    for lab, k in [("One word (rule used)", "1w"), ("Up to two words", "2w"), ("Up to four words", "4w")]:
        rows.append([lab] + [f"{by_year[y]['pct_' + k]:.1f}%" for y in ("2024", "2025")]
                    + [half_up(by_year[y]["subst_mean_" + k], 2) for y in ("2024", "2025")])
    write("table_A4_sensitivity_of_the_generic_review_rule_dnse_google_play.csv", rows)


# ------------------------------------------------------------------ Appendix B
def table_B1():
    lines = [("Operating revenue", "operating_revenue"), ("Interest on margin loans and advances", "margin_interest"),
             ("Interest on deposits and bonds held to maturity", "deposit_and_htm_interest"),
             ("Brokerage revenue", "brokerage_revenue"), ("Direct brokerage cost", "direct_brokerage_cost"),
             ("Interest expense plus line 24", "interest_expense_plus_line24"),
             ("Administrative expenses", "administrative_expenses"), ("Pre-tax profit", "pretax_profit"),
             ("Net proprietary result", "net_proprietary_result"), ("Core pre-tax profit", "core_pretax_profit")]
    rows = {p: AN.income_row(p, basis="quarters") for p in AN.PERIODS}
    write("table_B1_income_statement_summary_vnd_billion.csv",
          [["Item"] + [AN.period_label(p) for p in AN.PERIODS]]
          + [[lab] + [neg(rows[p][k]) for p in AN.PERIODS] for lab, k in lines])


def _avg(fn, qs):
    return sum(fn(q) for q in qs) / len(qs)


def nim_q(q):
    p = AN.prev_q(q)
    earning = lambda d: AN.v(d, "loans") + AN.v(d, "htm_assets") + AN.v(d, "htm_assets_long")
    net = AN.v(AN.Q[q], "rev_lending") + AN.v(AN.Q[q], "rev_htm") - AN.funding_cost(AN.Q[q], AN.Q[p])
    return net * 4 / ((earning(AN.Q[q]) + earning(AN.Q[p])) / 2) * 100


def table_B2():
    cols = [(y, f"{y}Q4", [f"{y}Q{i}" for i in range(1, 5)], f"FY{y}", f"{int(y) - 1}Q4", 1)
            for y in ("2021", "2022", "2023", "2024", "2025")]
    cols.append(("Jun 2026", "2026Q2", ["2026Q1", "2026Q2"], "2026H1", "2025Q4", 2))
    Q = AN.Q
    out = {}
    for lab, end, qs, per, start, annualise in cols:
        d = Q[end]
        flow = AN.A[per] if per.startswith("FY") else AN.H[per]
        avg_equity = (AN.v(d, "equity") + AN.v(Q[start], "equity")) / 2
        out[lab] = [AN.v(d, "loans"), AN.v(d, "htm_assets") + AN.v(d, "htm_assets_long"), AN.v(d, "total_assets"),
                    AN.debt(d), AN.v(d, "equity"), AN.v(d, "customer_cash_trading"),
                    AN.v(flow, "pbt") / AN.v(flow, "revenue") * 100,
                    AN.v(flow, "rev_brokerage") / -AN.v(flow, "cost_brokerage") * 100,
                    AN.v(flow, "pat") * annualise / avg_equity * 100,
                    AN.v(d, "loans") / AN.v(d, "equity") * 100,
                    _avg(lambda q: AN.cost_of_funds_pct(Q, q), qs),
                    _avg(nim_q, qs)]
    items = ["Margin loans and advances, VND bn", "Deposits and bonds held to maturity, VND bn", "Total assets, VND bn",
             "Borrowings and bonds, VND bn", "Owners' equity, VND bn", "Investor cash (off balance sheet), VND bn",
             "Pre-tax margin, %", "Brokerage revenue as % of direct cost", "Return on equity, %",
             "Loans as % of equity (ceiling 200)", "Estimated cost of funds, %", "Net interest margin, %"]
    rows = [["Item"] + [c[0] for c in cols]]
    for i, item in enumerate(items):
        rows.append([item] + [num(out[c[0]][i], 0 if i < 6 else 1) for c in cols])
    write("table_B2_balance_sheet_and_main_ratios.csv", rows)


def table_B3():
    pp = AN.platform_proxy()
    yrs = list(pp)
    fixed = AN.load_csv(AN.DATA / "dnse_financials_annual.csv")
    note = {r["field"]: r for r in fixed if r["section"] == "NOTE"}
    software = {y: abs(float(note["nos215"][f"FY{y}"])) + abs(float(note["nos223"][f"FY{y}"])) for y in yrs}
    acc = AN.account_metric("accounts_year_end")
    act_rows = {r["date"]: r for r in AN.manual("dnse_accounts.csv") if r["metric"] == "active_customers"}

    def active(y):
        r = act_rows.get(f"{y}-12")
        if not r:
            return "n.a."
        txt = f"{float(r['value']):,.0f}"
        return f"about {txt}" if "approximate" in r["source"] else txt

    rows = [["Item"] + yrs,
            ["Staff costs (administration)"] + [num(pp[y]["staff"]) for y in yrs],
            ["Outsourced services"] + [num(pp[y]["outsourced"]) for y in yrs],
            ["Depreciation and amortisation (all)"] + [num(pp[y]["depreciation"]) for y in yrs],
            ["Platform cost proxy"] + [num(pp[y]["total"]) for y in yrs],
            ["Software and leased equipment at cost"] + [num(software[y]) for y in yrs],
            ["Accounts at year end"] + [num(acc[f"{y}-12-31"], 0) for y in yrs],
            ["Active customers, December"] + [active(y) for y in yrs],
            ["Proxy per active customer, VND million"] + [
                num(pp[y]["total"] * 1e3 / float(act_rows[f"{y}-12"]["value"]), 2) if f"{y}-12" in act_rows else "n.a."
                for y in yrs]]
    write("table_B3_platform_and_overhead_cost_proxy_vnd_billion.csv", rows)


# ------------------------------------------------------------------ Appendix C
def table_C1():
    rows = sorted(AN.manual("market_position.csv"), key=lambda r: int(r["table_order"]))

    def share(r):
        if r["dnse_value"]:
            s = float(r["dnse_value"]) / float(r["market_total"]) * 100
            return s, s
        return float(r["share_low"]), float(r["share_high"])

    base = next(share(r)[0] for r in rows if r["measure"].startswith("Customer accounts"))
    out = [["Measure", "DNSE", "Market total", "DNSE share, %", "Ratio to account share"]]
    for r in rows:
        lo, hi = share(r)
        if lo == hi:
            s, ratio = f"{lo:.2f}", f"{lo / base:.2f}"
        else:
            s, ratio = f"{lo:.1f} to {hi:.1f}", f"{lo / base:.2f} to {hi / base:.2f}"
        out.append([r["table_label"], r["dnse_text"], r["market_text"], s, ratio])
    write("table_C1_dnse_s_position_on_eight_measures.csv", out)


def table_C2():
    pm = AN.peer_metrics("2026Q2")
    parent = {r["firm"]: r["parent_bank"] for r in AN.manual("peer_accounts.csv")}
    names = ["DNSE", "VPBankS", "TCBS", "VPS"]
    lending = lambda n: num(pm[n]["loans_bn"], 0) if n == "DNSE" else num(round(pm[n]["loans_bn"], -2), 0)
    rows = [["Indicator"] + names,
            ["Customer accounts, million"] + [f"{pm[n]['accounts_m']:.2f}" for n in names],
            ["Margin lending, 30 June 2026, VND bn"] + [lending(n) for n in names],   # peers to the nearest 100
            ["Lending per account, VND million"] + [num(pm[n]["loans_per_account_m"]) for n in names],
            ["Pre-tax profit per account, Q2 2026, VND thousand"] + [half_up(pm[n]["pbt_per_account_k"]) for n in names],
            ["Deposits and bonds held to maturity, % of assets"] + [num(pm[n]["deposits_htm_pct_assets"]) for n in names],
            ["Estimated cost of funds, Q2 2026, %"] + [num(pm[n]["cost_of_funds_pct"]) for n in names],
            ["Parent bank"] + [parent[n] for n in names]]
    write("table_C2_dnse_against_named_peers.csv", rows)


# ------------------------------------------------------------------ Appendix D
D1_LABELS = ["Crashes, freezes, login failures, slow orders", "Account opening, identity checks, one-time passwords",
             "Explicit accusation of deception", "Sign-up bonus terms, rewards not received",
             "Deposits not credited, withdrawal delays", "Cannot close the account, closure fee"]


def table_D1():
    n, votes, rows = AN.theme_shares()
    out = [["Theme", "Negative reviews", "Share of negative reviews, %", "Share of helpful votes, %"]]
    for i, r in enumerate(rows):
        label = D1_LABELS[i] if i < len(D1_LABELS) else r["theme"]
        out.append([label, r["negative_reviews"], num(r["share_of_negative_pct"]), num(r["share_of_votes_pct"])])
    idle = [r for r in AN.flagged("vn.com.encapital.arrow") if r["keep"] == "1" and "yield" in AN.themes(r)]
    tone = "all positive" if all(int(r["rating"]) >= 4 for r in idle) else "mixed"
    out.append(["Idle-cash product (Never-Sleeping Account), all reviews", f"{len(idle)} mentions, {tone}", "", ""])
    write("table_D1_themes_in_dnse_s_negative_google_play_reviews.csv", out)


def table_D2():
    rt = AN.reliability_trust()
    R = AN.load_json("reviews_tables.json")
    store = {r[0].split()[0]: r for r in R["STORE_COMPARE"]}
    rows = [["Application", "Negative reviews", "Reliability, % of reviews", "Reliability, % of votes",
             "Trust, % of reviews", "Trust, % of votes", "App Store mean, 2025 to 2026"]]
    for k, d in rt.items():
        rows.append([store[k][0], d["negative_n"], num(d["reliability_pct"]), num(d["reliability_votes_pct"]),
                     num(d["trust_pct"]), num(d["trust_votes_pct"]), f"{store[k][5]:.2f}"])
    write("table_D2_reliability_and_trust_complaints_at_three_brokers_january_20.csv", rows)


# ------------------------------------------------------------------ Appendix E
TABLE_LABEL = dict(AN.SEGMENT_LABEL, **{"Richest 60%": "Richest 60%", "Poorest 40%": "Poorest 40%"})


def table_E1():
    rows = AN.segment_rows()
    pick = ["All adults", "Young (15-24)", "Older (25+)", "Secondary educ or more", "Richest 60%", "In labour force",
            "Poorest 40%"]
    out = [["Segment", "Share of adults", "Index A (surplus)", "Index B (digital)", "Has an account",
            "Saved at an institution", "Account but no formal saving, million", "Wages into an account",
            "Saved for old age"]]
    for s in pick:
        r, i = rows[s], AN.SEG_INDEX[s]
        out.append([TABLE_LABEL[s]] + [num(x) for x in (r["pop_share_pct"], r["index_a_investable"], r["index_b_digital"],
                                                         r["account_pct"], r["saved_at_fi_pct"], r["unactivated_adults_m"],
                                                         AN.IND["fin32.acc"][i], AN.IND["fin17f"][i])])
    write("table_E1_findex_indicators_for_selected_segments_vietnam_2024_fieldwo.csv", out)


def table_E2():
    ranks = AN.segment_ranks()
    order = sorted(ranks["Equal weights"], key=lambda s: ranks["Equal weights"][s])
    shown = order[:5] + ["Young (15-24)"]          # the top five and the youngest segment
    write("table_E2_segment_ranks_under_four_weighting_schemes.csv",
          [["Segment"] + list(ranks)] + [[TABLE_LABEL[s]] + [ranks[k][s] for k in ranks] for s in shown])


# ------------------------------------------------------------------ Appendix F
def table_F5():
    sc = AN.scenarios()
    rows = [[""] + [s["scenario"] for s in sc],
            ["Savers enrolled"] + [f"{s['savers']:,.0f}" for s in sc],
            ["Monthly contribution, VND million"] + [f"{s['monthly_contribution_vnd_m']:.1f}" for s in sc],
            ["Share of contributions kept"] + [f"{s['share_kept'] * 100:.0f}%" for s in sc],
            ["Assets, VND trillion (multiple of investor cash)"] +
            [f"{half_up(s['assets_vnd_tn'], 2)} ({s['multiple_of_investor_cash']:.1f})" for s in sc],
            ["Annual fees, VND billion"] + [half_up(s["annual_fees_vnd_bn"], 0) for s in sc],
            ["Tier interest, upper bound, VND billion a year"] + [half_up(s["tier_interest_upper_bound_vnd_bn"], 1) for s in sc],
            ["Accounts with VND 10 million or more (share of mid-2026 base)"] +
            [f"{s['accounts_10m_plus']:,.0f} ({half_up(s['share_of_mid_2026_base_pct'], 1)}%)" for s in sc]]
    write("table_F5_outcomes_18_months_after_launch_all_inputs_are_assumptions.csv", rows)


ALL = [table_A2, table_A3, table_A4, table_B1, table_B2, table_B3, table_C1, table_C2, table_D1, table_D2,
       table_E1, table_E2, table_F5]


def main():
    for old in OUT.glob("*.csv"):          # file names follow the published captions
        old.unlink()
    for fn in ALL:
        fn()


if __name__ == "__main__":
    main()

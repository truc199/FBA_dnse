"""Checks the cohort model against the worked example of plan_payday.md section 6.2 before it is used.

The example's inputs are illustrative, not the Round 3 assumptions: 350 savers a month in months 4 to 6,
3,000 in months 7 to 12, 6,000 in months 13 to 18 and 8,000 in months 19 to 36; VND 1.2 million a month;
2.5 per cent of savers stop each month; 10 per cent of balances withdrawn a year; build cost VND 12 billion
over months 1 to 6; running cost VND 6 billion a year; VND 150,000 per saver acquired; a bonus of 0.3 per
cent a year on balances; net yield 0.6 per cent (40/40/20 at 1.0/0.5/0 per cent).

Run: python src/round3/test_payday_model.py   (exits 1 on any failure)
"""
import csv
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from payday_model import (TABLES_R3, load_assumptions, metrics, per_saver_value, scenario, simulate,  # noqa: E402
                          simulate_calendar, tenure_profile)
from config import MANUAL  # noqa: E402

MONTHS = 36
ILLUSTRATIVE = {
    "contribution": 1.2e6, "stop_rate_first_90_days": 0.025, "stop_rate_monthly": 0.025,
    "withdrawal_rate_annual": 0.10, "customer_return_annual": 0.0,
    "mix_golden_egg": 0.4, "mix_bond_funds": 0.4, "mix_equity_funds": 0.0, "mix_etf": 0.2,
    "yield_golden_egg": 0.010, "yield_bond_funds": 0.005, "yield_equity_funds": 0.0, "yield_etf": 0.0,
    "build_cost": 12e9, "build_months": 6, "run_cost_annual": 6e9, "marketing_fixed_annual": 0.0,
    "bonus_flat_annual": 0.003, "tier_gift_3": 0.0, "tier_gift_6": 0.0, "tier_gift_12": 0.0,
    "tier_fee_discount": 0.0, "tier_rate_boost": 0.0, "interest_cap": 50e6,
    "fee_per_contribution": 0.0, "service_cost_per_active_month": 0.0,
    "lending_share": 0.0, "lending_spread": 0.045, "lending_start_month": 19,
    "balance_threshold": 10e6, "discount_rate_annual": 0.12, "pilot_start_month": 4,
}
YIELD_1PCT = {"yield_golden_egg": 0.0175, "yield_bond_funds": 0.0075}   # 0.4 x 1.75 + 0.4 x 0.75 = 1.0%


def schedule(cac):
    enrol = [0.0] * MONTHS
    for a, b, n in [(4, 6, 350), (7, 12, 3000), (13, 18, 6000), (19, 36, 8000)]:
        for m in range(a, b + 1):
            enrol[m - 1] = n
    return {"illustrative": (enrol, cac)}


def run(**over):
    p = {**ILLUSTRATIVE, **over}
    cac = p.pop("cac", 150_000)
    rows = simulate(p, MONTHS, schedule(cac), overlap={})
    return p, rows


def aggregate_check(p, rows):
    """The cohort sum must equal the aggregate recursion of plan_payday.md section 6.2."""
    active = bal = 0.0
    enrol = schedule(0)["illustrative"][0]
    worst = 0.0
    for t, r in enumerate(rows):
        active = active * (1 - p["stop_rate_monthly"]) + enrol[t]
        bal = bal * (1 - p["withdrawal_rate_annual"] / 12) + active * p["contribution"]
        worst = max(worst, abs(active - r["active"]), abs(bal - r["balance"]) / 1e6)
    return worst


def main():
    results, ok = [], True

    def check(name, got, want, tol):
        nonlocal ok
        good = got is None and want is None or (got is not None and want is not None and abs(got - want) <= tol)
        ok &= good
        results.append({"check": name, "expected": want, "model": None if got is None else round(got, 4),
                        "tolerance": tol, "pass": "yes" if good else "NO"})

    p, rows = run()
    m18, m36 = rows[17], rows[35]
    check("Month 18: savers enrolled", m18["enrolled_cumulative"], 55_050, 0.5)
    check("Month 18: savers still contributing", m18["active"], 49_108, 1.0)
    check("Month 18: balance, VND trillion", m18["balance"] / 1e12, 0.33, 0.005)
    check("Month 36: savers enrolled", m36["enrolled_cumulative"], 199_050, 0.5)
    check("Month 36: savers still contributing", m36["active"], 148_257, 1.0)
    check("Month 36: balance, VND trillion", m36["balance"] / 1e12, 2.43, 0.005)
    check("Month 36: cumulative cash, VND billion", m36["cumulative_cash"] / 1e9, -53.7, 0.05)
    check("Cohort sum equals the aggregate recursion (max gap)", aggregate_check(p, rows), 0.0, 1e-6)

    # Combinations in the table of plan_payday.md section 6.2 (36 months)
    cases = [
        ("0.6%, VND 150k, bonus 0.3%", {}, -53.7, None),
        ("0.6%, VND 150k, no bonus", {"bonus_flat_annual": 0.0}, -47.5, None),
        ("0.6%, VND 50k", {"bonus_flat_annual": 0.0, "cac": 50_000}, -27.6, 32),
        ("1.0%, VND 150k", {"bonus_flat_annual": 0.0, **YIELD_1PCT}, -39.2, 34),
        ("1.0%, VND 50k", {"bonus_flat_annual": 0.0, "cac": 50_000, **YIELD_1PCT}, -19.3, 27),
        ("0.6%, VND 50k, lending 10% from month 19", {"bonus_flat_annual": 0.0, "cac": 50_000, "lending_share": 0.10},
         -18.9, 26),
        ("1.0%, VND 50k, lending 10%", {"bonus_flat_annual": 0.0, "cac": 50_000, "lending_share": 0.10, **YIELD_1PCT},
         -10.6, 24),
    ]
    for name, over, cash, be in cases:
        pp, rr = run(**over)
        check(f"{name}: cumulative cash at month 36, VND billion", rr[-1]["cumulative_cash"] / 1e9, cash, 0.05)
        check(f"{name}: first month revenue covers cost", metrics(rr, pp)["breakeven_month"], be, 0)

    # Present value of revenue per saver, 12 per cent a year (1 per cent a month)
    for horizon, over, want in [(36, {}, 219_000), (36, YIELD_1PCT, 365_000), (60, {}, 416_000),
                                (60, YIELD_1PCT, 694_000)]:
        pp = {**ILLUSTRATIVE, **over}
        got = per_saver_value(pp, horizon)["pv_revenue"]
        check(f"PV of revenue per saver, {horizon} months, yield {'1.0' if over else '0.6'}%", got, want, 1_000)

    # Per-saver balances by tenure must add up to the cohort balance
    prof = tenure_profile(ILLUSTRATIVE, MONTHS)
    gap, b = 0.0, 0.0
    for i in range(MONTHS):
        b = b * (1 - ILLUSTRATIVE["withdrawal_rate_annual"] / 12) + prof["active"][i] * ILLUSTRATIVE["contribution"]
        gap = max(gap, abs(b - prof["balance"][i]))
    check("Saver and stopper balances add up to the cohort balance (max gap, VND)", gap, 0.0, 1e-3)

    # The calendar-time engine (used for stress tests) must reproduce the cohort-profile engine without shocks
    def max_gap(a, b, keys=("active", "balance", "savers_above_10m", "new_accounts_above_10m", "revenue", "cost",
                            "cumulative_cash")):
        return max(abs(x[k] - y[k]) / max(1.0, abs(x[k])) for x, y in zip(a, b) for k in keys)
    p_ill, rows_ill = run()
    check("Calendar engine equals cohort engine, worked example (max relative gap)",
          max_gap(rows_ill, simulate_calendar(p_ill, MONTHS, schedule(150_000), overlap={})), 0.0, 1e-9)
    p_base, sched_base, rows_base, _ = scenario("base")
    check("Calendar engine equals cohort engine, base scenario with tiers (max relative gap)",
          max_gap(rows_base, simulate_calendar(p_base, len(rows_base), sched_base)), 0.0, 1e-9)

    # Derived inputs of data/round3/payday_assumptions.csv must agree with the Round 2 data files
    acc = {(r["metric"], r["date"]): float(r["value"]) for r in csv.DictReader(
        open(MANUAL / "dnse_accounts.csv", encoding="utf-8-sig"))}
    a = {r["param"]: r for r in load_assumptions()}
    total, active = acc[("accounts_year_end", "2025-12-31")], acc[("active_customers", "2025-12")]
    check("Assumption: dormant accounts = accounts less active customers, end-2025",
          float(a["dormant_accounts"]["base"]), total - active, 0.5)
    check("Assumption: share of active customers already above VND 10 million",
          float(a["active_share_already_10m"]["base"]), round(acc[("net_assets_10m_plus", "2025-12")] / active, 3), 1e-9)
    check("Assumption: new accounts a month, H1 2026 pace",
          float(a["new_accounts_per_month"]["base"]),
          round((acc[("accounts_mid_year", "2026-06-30")] - total) / 6), 0.5)
    check("Assumption: new accounts a month, 2025 pace (upside)",
          float(a["new_accounts_per_month"]["high"]), round(acc[("new_accounts", "2025")] / 12), 0.5)
    check("Assumption: active customers", float(a["active_customers"]["base"]), active, 0.5)
    mix = sum(float(a[f"mix_{k}"]["base"]) for k in ["golden_egg", "bond_funds", "equity_funds", "etf"])
    check("Assumption: default asset mix adds up to 1", mix, 1.0, 1e-9)

    TABLES_R3.mkdir(parents=True, exist_ok=True)
    with open(TABLES_R3 / "payday_test_check.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(results[0]))
        w.writeheader()
        w.writerows(results)
    for r in results:
        print(f"  [{'ok' if r['pass'] == 'yes' else 'FAIL'}] {r['check']}: model {r['model']}, expected {r['expected']}")
    print(f"  {sum(r['pass'] == 'yes' for r in results)} of {len(results)} checks pass; written "
          f"{(TABLES_R3 / 'payday_test_check.csv').relative_to(TABLES_R3.parents[2])}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())

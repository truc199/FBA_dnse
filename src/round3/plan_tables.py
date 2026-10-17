"""Tables of the Payday Portfolio product and implementation plan (Round 3A): go-to-market by quarter,
roadmap by phase, Board ask, RACI, risk register, trust metrics, legal map, glide path, journey map and
service blueprint.

The wording is the authors' design and lives in data/round3/*.csv. Numbers in braces, such as {enrol_stop},
are filled from the cohort model, and the quarter and phase figures are read from its base run, so the plan
cannot drift from the business case.

Run: python src/round3/plan_tables.py   (after payday_model.py)
"""
import csv
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import payday_model as M  # noqa: E402

AUTHORED = ["raci", "trust_metrics", "legal_map", "glide_path", "journey_map", "service_blueprint"]
QUARTERS = [("Q1", 1, 3), ("Q2", 4, 6), ("Q3", 7, 9), ("Q4", 10, 12)]


def read(path):
    with open(path, encoding="utf-8-sig") as f:
        return list(csv.DictReader(f))


def key_numbers(rows_csv, runs):
    """Values quoted in the plan's wording, from the model."""
    p, sched, res, m = runs["base"]
    _, g = M.decision_gates(rows_csv, runs)
    m12 = res[11]
    return {
        "pilot_accounts": f"{p['pilot_accounts']:,.0f}",
        "pilot_arm": f"{p['pilot_accounts'] / 3:,.0f}",
        "enrol_scale": f"{1.5 * g['breakeven_enrolment'] * 100:.1f}%",
        "enrol_stop": f"{g['breakeven_enrolment'] * 100:.1f}%",
        "persist_scale": f"{g['persistence_3_base'] * 100:.0f}%",
        "cpa_scale": f"{1.25 * g['cost_per_account_plan_m60'] / 1e6:.1f}",
        "cpa_plan": f"{g['cost_per_account_plan_m60'] / 1e6:.2f}",
        "ceiling": f"{g['cac_ceiling_60m']:,.0f}",
        "ceiling_no_fee": f"{g['ceiling_no_fee']:,.0f}",
        "fee_limit": f"{g['fee_limit']:,.0f}",
        "emp_part": f"{g['employer_participation_needed'] * 100:.0f}%",
        "m12_funded_80": f"{0.8 * m12['funded_savers']:,.0f}",
        "m12_bal_80": f"{0.8 * m12['balance'] / 1e9:.1f}",
    }


def fill(rows, k):
    return [{c: v.format(**k) if isinstance(v, str) else v for c, v in r.items()} for r in rows]


def gtm(res, k):
    plan = fill(read(M.DATA_R3 / "gtm_year1_plan.csv"), k)
    out = []
    for r, (q, a, b) in zip(plan, QUARTERS):
        sub = [x for x in res if a <= x["month"] <= b]
        end = sub[-1]
        by_ch = {c: sum(x[f"enrolled_{c}"] for x in sub) for c in M.CHANNELS}
        out.append({**r,
                    "savers_enrolled_in_quarter": round(sum(by_ch.values())),
                    "enrolled_by_channel": "; ".join(f"{M.CHANNEL_LABEL[c]} {v:,.0f}" for c, v in by_ch.items() if v >= 0.5),
                    "savers_enrolled_cumulative": round(end["enrolled_cumulative"]),
                    "funded_savers_end": round(end["funded_savers"]),
                    "balance_end_vnd_bn": M.bn(end["balance"]),
                    "cost_vnd_bn": M.bn(sum(x["cost"] for x in sub)),
                    "of_which_marketing_and_acquisition_vnd_bn": M.bn(sum(x["cost_marketing"] + x["cost_acquisition"] for x in sub)),
                    "source": "Authors' design; numbers from the cohort model, base case (payday_monthly_base.csv)"})
    return out


def roadmap(res, p, k):
    plan = fill(read(M.DATA_R3 / "roadmap_plan.csv"), k)
    budget = {b["phase"]: b for b in M.phase_budget(res, p)}
    out = []
    for r in plan:
        b = budget[r["phase"]]
        end = res[int(r["months"].split("-")[1]) - 1]
        out.append({**r, "cost_vnd_bn": b["cost_vnd_bn"], "revenue_vnd_bn": b["revenue_vnd_bn"],
                    "cumulative_cash_at_end_vnd_bn": b["cumulative_cash_at_end_vnd_bn"],
                    "savers_enrolled_by_end": round(end["enrolled_cumulative"]),
                    "funded_savers_at_end": round(end["funded_savers"]),
                    "balance_at_end_vnd_bn": M.bn(end["balance"]),
                    "new_accounts_above_10m_at_end": round(end["new_accounts_above_10m"]),
                    "source": "Authors' design; numbers from the cohort model, base case"})
    return out


def board_ask(res, p, k):
    need, ask = M.board_ask(res, p)
    return [
        {"item": "Budget for Phase 0 and Phase 1 (months 1 to 6)", "value": f"VND {ask / 1e9:.1f} billion",
         "detail": f"Model cash need VND {need / 1e9:.2f} billion plus {p['contingency_share'] * 100:.0f}% contingency; "
                   f"build VND {p['build_cost'] / 1e9:.1f} billion, running and marketing from month 4"},
        {"item": "Decision 1", "value": "Choose the virtual-account partner bank",
         "detail": "Collection fee target VND 0, because the bank keeps the deposits"},
        {"item": "Decision 2", "value": "Sign 1 to 2 fund managers",
         "detail": "DNSE is a registered distribution agent but not yet on their distributor lists"},
        {"item": "Decision 3", "value": "File the SSC notice and pre-consult on Golden Egg's role", "detail": "Before launch"},
        {"item": "Decision 4", "value": "Have a licensed adviser sign the model plans", "detail": "Circular 121/2020, Article 24"},
        {"item": "Decision 5", "value": f"Accept a budget of about VND {k['cpa_plan']} million per new account above VND 10 million",
         "detail": "The yardstick used at the month-6, 12 and 24 gates"},
    ]


def risks(k):
    out = []
    for r in fill(read(M.DATA_R3 / "risk_register.csv"), k):
        score = int(r["likelihood"]) * int(r["impact"])
        out.append({**r, "score": score, "rating": "High" if score >= 15 else ("Medium" if score >= 8 else "Low"),
                    "source": "Authors' assessment (likelihood and impact on a 1 to 5 scale)"})
    return sorted(out, key=lambda r: -r["score"])


def main():
    rows_csv = M.load_assumptions()
    runs = {s: M.scenario(s, rows_csv) for s in M.SCENARIOS}
    p, sched, res, m = runs["base"]
    k = key_numbers(rows_csv, runs)
    M.write_csv("gtm_year1.csv", gtm(res, k))
    M.write_csv("roadmap_phases.csv", roadmap(res, p, k))
    M.write_csv("board_ask.csv", board_ask(res, p, k))
    M.write_csv("risk_register.csv", risks(k))
    for name in AUTHORED:
        M.write_csv(f"{name}.csv", fill(read(M.DATA_R3 / f"{name}.csv"), k))


if __name__ == "__main__":
    main()

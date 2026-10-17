"""Monthly cohort model of Payday Portfolio, the business case of Round 3A.

Inputs come from data/round3/payday_assumptions.csv. Each row gives a downside (low), base and upside
(high) value and says whether the value is sourced, derived from sourced figures, or an assumption.
Outputs go to outputs/round3/tables/payday_*.csv.

Each monthly cohort of savers is followed on its own, so the model can count the savers whose own plan
balance has passed VND 10 million. For a cohort the monthly steps are those of plan_payday.md section 6.2,
which test_payday_model.py checks against the worked example of that section:

    active(t)  = active(t-1) x (1 - stop rate) + enrolled(t)
    balance(t) = balance(t-1) x (1 - withdrawal rate / 12) + active(t) x contribution
    revenue(t) = balance(t) x net yield / 12

Balances count contributions net of withdrawals, before any investment return, unless
customer_return_annual is set above zero.
"""
import csv
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from config import ROOT  # noqa: E402

DATA_R3 = ROOT / "data" / "round3"
OUT_R3 = ROOT / "outputs" / "round3"
TABLES_R3 = OUT_R3 / "tables"
ASSUMPTIONS = DATA_R3 / "payday_assumptions.csv"

SCENARIOS = ["low", "base", "high"]
ASSETS = ["golden_egg", "bond_funds", "equity_funds", "etf"]
CHANNELS = ["dormant_pilot", "dormant_rollout", "active_customers", "new_accounts", "employers"]
CHANNEL_LABEL = {"dormant_pilot": "Dormant accounts, pilot", "dormant_rollout": "Dormant accounts, roll-out",
                 "active_customers": "Active customers", "new_accounts": "New accounts at opening",
                 "employers": "Employers (payroll)"}
PHASES = [("Phase 0: build and comply", 1, 3), ("Phase 1: pilot", 4, 6), ("Phase 2: scale in the base", 7, 12),
          ("Phase 3: outside channels", 13, 24), ("Phase 4: optimise", 25, 36), ("Years 4 and 5", 37, 60)]


# ---------------------------------------------------------------- inputs
def load_assumptions(path=ASSUMPTIONS):
    with open(path, encoding="utf-8-sig") as f:
        return list(csv.DictReader(f))


def params(scenario="base", rows=None, overrides=None):
    """Parameter values of one scenario as a dict of floats; overrides replace single values."""
    rows = rows or load_assumptions()
    p = {r["param"]: float(r[scenario]) for r in rows}
    p.update(overrides or {})
    return p


def phase_of(month):
    return next(name for name, a, b in PHASES if a <= month <= b)


# ---------------------------------------------------------------- one saver
def survival(p, months):
    """Share of an enrolled cohort still contributing when it has made n contributions (index n - 1).

    The stop rate of the first 90 days applies to the second and third contributions; after the third,
    the monthly stop rate applies."""
    s = [1.0]
    for n in range(1, months):
        h = p["stop_rate_first_90_days"] if n < 3 else p["stop_rate_monthly"]
        s.append(s[-1] * (1 - h))
    return s


def saver_balance(p, months):
    """Plan balance of a saver who has contributed n months in a row (index n - 1), and the monthly
    factor applied to every balance (withdrawals and, if set, investment returns)."""
    g = (1 - p["withdrawal_rate_annual"] / 12) * (1 + p.get("customer_return_annual", 0.0) / 12)
    b, out = 0.0, []
    for _ in range(months):
        b = b * g + p["contribution"]
        out.append(b)
    return out, g


def net_yield(p):
    """DNSE's revenue per year on each VND of plan balance, weighted by the default asset mix."""
    return sum(p[f"mix_{a}"] * p[f"yield_{a}"] for a in ASSETS)


def tenure_profile(p, months):
    """Per enrolled saver, by tenure n (index n - 1): the expected values the cohort sum needs."""
    surv = survival(p, months)
    bal, g = saver_balance(p, months)
    X, cap = p["balance_threshold"], p["interest_cap"]
    prof = {k: [0.0] * months for k in ["active", "funded", "balance", "above_x", "gifts", "disc_base",
                                         "boost_base", "milestone_3", "milestone_6", "milestone_12"]}
    for i in range(months):
        n = i + 1
        a = surv[i]
        prof["active"][i] = a
        prof["funded"][i] = a if n >= 3 else 0.0
        # savers still contributing, plus those who stopped after m contributions (their balance decays)
        stopped = [(surv[m - 1] - surv[m], bal[m - 1] * g ** (n - m)) for m in range(1, n)]
        prof["balance"][i] = a * bal[i] + sum(w * b for w, b in stopped)
        prof["above_x"][i] = a * (bal[i] >= X) + sum(w for w, b in stopped if b >= X)
        gift = {3: p["tier_gift_3"], 6: p["tier_gift_6"], 12: p["tier_gift_12"]}.get(n, 0.0)
        prof["gifts"][i] = a * gift
        prof["milestone_3"][i] = a if n == 3 else 0.0
        prof["milestone_6"][i] = a if n == 6 else 0.0
        prof["milestone_12"][i] = a if n == 12 else 0.0
        prof["disc_base"][i] = a * bal[i] if n >= 6 else 0.0          # fund fee discount, six contributions on
        prof["boost_base"][i] = a * min(p["mix_golden_egg"] * bal[i], cap) if n >= 12 else 0.0
    return prof


def per_saver_value(p, horizon):
    """Present value per enrolled saver over `horizon` months: revenue, variable cost, and the difference,
    which is the most DNSE can spend to acquire one saver (the CAC ceiling)."""
    prof = tenure_profile(p, horizon)
    y = net_yield(p)
    d = p["discount_rate_annual"] / 12
    pv_rev = pv_var = 0.0
    for i in range(horizon):
        f = (1 + d) ** -(i + 1)
        rev = prof["balance"][i] * y / 12
        var = (prof["balance"][i] * p.get("bonus_flat_annual", 0.0) / 12 + prof["gifts"][i]
               + prof["disc_base"][i] * p["mix_bond_funds"] * p["tier_fee_discount"] / 12
               + prof["disc_base"][i] * p["mix_equity_funds"] * p["tier_fee_discount"] / 12
               + prof["boost_base"][i] * p["tier_rate_boost"] / 12
               + prof["active"][i] * (p["fee_per_contribution"] + p["service_cost_per_active_month"]))
        pv_rev += rev * f
        pv_var += var * f
    return {"pv_revenue": pv_rev, "pv_variable_cost": pv_var, "cac_ceiling": pv_rev - pv_var}


# ---------------------------------------------------------------- enrolment
def channel_schedule(p, months, cost_p=None):
    """Enrolments by month for each channel, with the acquisition cost (VND) of one enrolled saver.

    cost_p, if given, supplies the conversion rates used to price acquisition, so a sensitivity can move
    enrolment volumes without moving the cost of each saver."""
    cp = cost_p or p
    z = lambda: [0.0] * months  # noqa: E731
    out = {}

    # Dormant accounts reached digitally: two treated arms of the randomised pilot, then a roll-out to
    # the remaining eligible dormant accounts, contacted evenly over the roll-out months.
    s, e = int(p["pilot_start_month"]), int(p["pilot_end_month"])
    pilot = z()
    for t in range(s, e + 1):
        pilot[t - 1] = p["pilot_accounts"] * p["pilot_treated_share"] * p["conv_dormant"] / (e - s + 1)
    out["dormant_pilot"] = (pilot, p["reach_cost_per_account"] / cp["conv_dormant"])

    pool = p["dormant_accounts"] * p["eligible_share_dormant"] - p["pilot_accounts"]
    s, k = int(p["rollout_start_month"]), int(p["rollout_months"])
    roll = z()
    for t in range(s, min(s + k, months + 1)):
        roll[t - 1] = pool / k * p["conv_dormant"]
    out["dormant_rollout"] = (roll, p["reach_cost_per_account"] / cp["conv_dormant"])

    # Customers who already trade see an in-app offer during the roll-out months.
    act = z()
    for t in range(s, min(s + k, months + 1)):
        act[t - 1] = p["active_customers"] * p["conv_active"] / k
    out["active_customers"] = (act, p["inapp_cost_per_saver"])

    # Every newly opened account is offered the plan during onboarding.
    new = z()
    for t in range(int(p["new_account_offer_month"]), months + 1):
        new[t - 1] = p["new_accounts_per_month"] * p["conv_new_account"]
    out["new_accounts"] = (new, p["inapp_cost_per_saver"])

    # Employers sign up at a steady pace; their employees enrol in the month the employer joins.
    emp = z()
    per_employer = p["employees_per_employer"] * p["participation_employer"]
    for t in range(int(p["employer_start_month"]), months + 1):
        emp[t - 1] = p["employers_per_quarter"] / 3 * per_employer
    cp_per_employer = cp["employees_per_employer"] * cp["participation_employer"]
    out["employers"] = (emp, p["cost_per_employer"] / cp_per_employer if cp_per_employer else 0.0)
    return out


# ---------------------------------------------------------------- the model
def simulate(p, months=60, schedule=None, overlap=None):
    """Run the model month by month. `schedule` maps a channel to (enrolments by month, CAC per saver);
    by default it is built from p. `overlap` maps a channel to the share of its savers who already held
    VND 10 million at DNSE, so they do not add to the company's count of such accounts."""
    schedule = schedule or channel_schedule(p, months)
    overlap = overlap if overlap is not None else {"active_customers": p.get("active_share_already_10m", 0.0)}
    prof = tenure_profile(p, months)
    y = net_yield(p)
    fund_share = p["mix_bond_funds"] + p["mix_equity_funds"]
    T = months
    rows, cum = [], 0.0
    for t in range(T):
        month = t + 1
        agg = dict.fromkeys(prof, 0.0)
        above_x_new = 0.0
        enrolled_now = {c: s[0][t] for c, s in schedule.items()}
        for c, (enr, _) in schedule.items():
            for e in range(t + 1):
                if enr[e] == 0:
                    continue
                i = t - e
                for k in prof:
                    agg[k] += enr[e] * prof[k][i]
                above_x_new += enr[e] * prof["above_x"][i] * (1 - overlap.get(c, 0.0))
        row = month_row(p, month, agg, above_x_new, enrolled_now, schedule, y, fund_share, cum)
        cum = row["cumulative_cash"]
        rows.append(row)
    return add_cumulative_enrolment(rows)


def month_row(p, month, agg, above_x_new, enrolled_now, schedule, y, fund_share, cum):
    """Revenue, costs and cash of one month, from the month's totals over all cohorts."""
    bal = agg["balance"]
    rev_plan = bal * y / 12
    rev_lend = bal * p["lending_share"] * p["lending_spread"] / 12 if month >= p["lending_start_month"] else 0.0
    cost = {
        "build": p["build_cost"] / p["build_months"] if month <= p["build_months"] else 0.0,
        "run": p["run_cost_annual"] / 12 if month >= p.get("run_start_month", 1) else 0.0,
        "marketing": p["marketing_fixed_annual"] / 12 if month >= p["pilot_start_month"] else 0.0,
        "acquisition": sum(enrolled_now[c] * schedule[c][1] for c in schedule),
        "rewards": (bal * p.get("bonus_flat_annual", 0.0) / 12 + agg["gifts"]
                    + agg["disc_base"] * fund_share * p["tier_fee_discount"] / 12
                    + agg["boost_base"] * p["tier_rate_boost"] / 12),
        "payments_service": agg["active"] * (p["fee_per_contribution"] + p["service_cost_per_active_month"]),
    }
    total_cost = sum(cost.values())
    profit = rev_plan + rev_lend - total_cost
    return {
        "month": month, "phase": phase_of(month),
        **{f"enrolled_{c}": enrolled_now.get(c, 0.0) for c in schedule},
        "enrolled": sum(enrolled_now.values()), "active": agg["active"], "funded_savers": agg["funded"],
        "balance": bal, "contributions": agg["active"] * p["contribution"],
        "savers_above_10m": agg["above_x"], "new_accounts_above_10m": above_x_new,
        "revenue_plan": rev_plan, "revenue_lending": rev_lend, "revenue": rev_plan + rev_lend,
        **{f"cost_{k}": v_ for k, v_ in cost.items()}, "cost": total_cost,
        "profit": profit, "cumulative_cash": cum + profit,
    }


def add_cumulative_enrolment(rows):
    run_ = 0.0
    for r in rows:
        run_ += r["enrolled"]
        r["enrolled_cumulative"] = run_
    return rows


def simulate_calendar(p, months=60, schedule=None, overlap=None, shocks=None):
    """The same model, run cohort by cohort through calendar time so that rates can change in given months
    (stress tests). Without shocks it reproduces simulate(); test_payday_model.py checks this.

    shocks: {"stop_multiplier": {month: factor}, "withdrawal_multiplier": {month: factor},
             "extra_stop_share": {month: share of contributing savers who also stop that month},
             "enrolment_multiplier": {month: factor}}"""
    shocks = shocks or {}
    sm, wm = shocks.get("stop_multiplier", {}), shocks.get("withdrawal_multiplier", {})
    xs, em = shocks.get("extra_stop_share", {}), shocks.get("enrolment_multiplier", {})
    base_sched = schedule or channel_schedule(p, months)
    sched = {c: ([v * em.get(t + 1, 1.0) for t, v in enumerate(enr)], cac) for c, (enr, cac) in base_sched.items()}
    overlap = overlap if overlap is not None else {"active_customers": p.get("active_share_already_10m", 0.0)}
    y = net_yield(p)
    fund_share = p["mix_bond_funds"] + p["mix_equity_funds"]
    X, cap, C = p["balance_threshold"], p["interest_cap"], p["contribution"]
    gift = {3: p["tier_gift_3"], 6: p["tier_gift_6"], 12: p["tier_gift_12"]}
    cohorts, rows, cum = [], [], 0.0
    for month in range(1, months + 1):
        g = (1 - p["withdrawal_rate_annual"] * wm.get(month, 1.0) / 12) * (1 + p.get("customer_return_annual", 0.0) / 12)
        for co in cohorts:                                     # existing cohorts: stops, withdrawals, contribution
            made = month - co["start"]
            h = p["stop_rate_first_90_days"] if made < 3 else p["stop_rate_monthly"]
            h = min(1.0, h * sm.get(month, 1.0) + xs.get(month, 0.0))
            stop = co["active"] * h
            if stop:
                co["stopped"].append([stop, co["bal"]])
            co["active"] -= stop
            for grp in co["stopped"]:
                grp[1] *= g
            co["bal"] = co["bal"] * g + C
        for c, (enr, _) in sched.items():                      # new cohorts make their first contribution
            if enr[month - 1]:
                cohorts.append({"channel": c, "start": month, "active": enr[month - 1], "bal": C, "stopped": []})
        agg = dict.fromkeys(["active", "funded", "balance", "above_x", "gifts", "disc_base", "boost_base"], 0.0)
        above_x_new = 0.0
        for co in cohorts:
            n, a, b = month - co["start"] + 1, co["active"], co["bal"]
            above = a * (b >= X) + sum(k for k, v_ in co["stopped"] if v_ >= X)
            agg["active"] += a
            agg["funded"] += a if n >= 3 else 0.0
            agg["balance"] += a * b + sum(k * v_ for k, v_ in co["stopped"])
            agg["above_x"] += above
            agg["gifts"] += a * gift.get(n, 0.0)
            agg["disc_base"] += a * b if n >= 6 else 0.0
            agg["boost_base"] += a * min(p["mix_golden_egg"] * b, cap) if n >= 12 else 0.0
            above_x_new += above * (1 - overlap.get(co["channel"], 0.0))
        enrolled_now = {c: s[0][month - 1] for c, s in sched.items()}
        row = month_row(p, month, agg, above_x_new, enrolled_now, sched, y, fund_share, cum)
        cum = row["cumulative_cash"]
        rows.append(row)
    return add_cumulative_enrolment(rows)


def metrics(rows, p):
    """Break-even month, payback month, peak funding need and net present value of a model run."""
    d = p["discount_rate_annual"] / 12
    be = next((r["month"] for r in rows if r["month"] > p["build_months"] and r["revenue"] >= r["cost"]), None)
    pb = next((r["month"] for r in rows if r["cumulative_cash"] >= 0 and r["month"] > 1), None)
    low = min(rows, key=lambda r: r["cumulative_cash"])
    op = next((r["month"] for r in rows if r["month"] > p["build_months"] and r["revenue"] >=
               r["cost"] - r["cost_build"] - r["cost_acquisition"]), None)
    return {"breakeven_month": be, "operating_breakeven_month": op, "payback_month": pb,
            "peak_funding_need": -low["cumulative_cash"], "peak_funding_month": low["month"],
            "npv": sum(r["profit"] * (1 + d) ** -r["month"] for r in rows)}


# ---------------------------------------------------------------- scenarios, sensitivity, unit economics
MONTHS = 60
MILESTONES = [6, 12, 18, 24, 36, 60]
TORNADO = [  # label, parameters moved together from their low to their high value (others at base)
    ("Acquisition cost per saver", ["reach_cost_per_account", "inapp_cost_per_saver", "cost_per_employer"]),
    ("Net yield on balances", [f"yield_{a}" for a in ASSETS]),
    ("Stop rates", ["stop_rate_first_90_days", "stop_rate_monthly"]),
    ("Monthly contribution", ["contribution"]),
    ("Enrolment rates (cost per saver held)", ["conv_dormant", "conv_active", "conv_new_account",
                                               "participation_employer", "employers_per_quarter"]),
    ("Withdrawals", ["withdrawal_rate_annual"]),
    ("Build and running cost", ["build_cost_team", "build_cost_external", "run_cost_team", "run_cost_other"]),
    ("Bank fee per contribution", ["fee_per_contribution"]),
    ("Investment returns on balances (0% to 5%)", ["customer_return_annual"]),
]


def derive(p):
    """Costs that the assumptions file breaks into parts."""
    p = dict(p)
    p["build_cost"] = p["build_cost_team"] + p["build_cost_external"]
    p["run_cost_annual"] = p["run_cost_team"] + p["run_cost_other"]
    return p


def scenario(name, rows=None, overrides=None, cost_from=None, months=MONTHS):
    p = derive(params(name, rows, overrides))
    cp = derive(cost_from) if cost_from else None
    sched = channel_schedule(p, months, cp)
    res = simulate(p, months, sched)
    return p, sched, res, metrics(res, p)


def bn(x):
    return round(x / 1e9, 2)


def write_csv(name, rows):
    TABLES_R3.mkdir(parents=True, exist_ok=True)
    with open(TABLES_R3 / name, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0]))
        w.writeheader()
        w.writerows(rows)
    print(f"  wrote outputs/round3/tables/{name}")


def monthly_table(res):
    out = []
    for r in res:
        out.append({
            "month": r["month"], "phase": r["phase"],
            **{f"enrolled_{c}": round(r.get(f"enrolled_{c}", 0.0), 1) for c in CHANNELS},
            "enrolled": round(r["enrolled"], 1), "enrolled_cumulative": round(r["enrolled_cumulative"]),
            "active_savers": round(r["active"]), "funded_savers": round(r["funded_savers"]),
            "balance_vnd_bn": bn(r["balance"]), "savers_above_10m": round(r["savers_above_10m"]),
            "new_accounts_above_10m": round(r["new_accounts_above_10m"]),
            "revenue_vnd_bn": bn(r["revenue"]), "cost_vnd_bn": bn(r["cost"]),
            **{f"cost_{k}_vnd_bn": bn(r[f"cost_{k}"]) for k in
               ["build", "run", "marketing", "acquisition", "rewards", "payments_service"]},
            "profit_vnd_bn": bn(r["profit"]), "cumulative_cash_vnd_bn": bn(r["cumulative_cash"]),
        })
    return out


def unit_economics(p, sched):
    v36, v60 = per_saver_value(p, 36), per_saver_value(p, 60)
    surv = survival(p, 13)
    bal, _ = saver_balance(p, 60)
    months_to_x = next((i + 1 for i, b in enumerate(bal) if b >= p["balance_threshold"]), None)
    rows = [
        ("Net yield on plan balances, % a year", round(net_yield(p) * 100, 3)),
        ("Revenue a year on VND 10 million of balance, VND", round(net_yield(p) * 1e7)),
        ("Savers still contributing after 3 contributions, %", round(surv[2] * 100, 1)),
        ("Savers still contributing after 6 contributions, %", round(surv[5] * 100, 1)),
        ("Savers still contributing after 12 contributions, %", round(surv[11] * 100, 1)),
        ("Contributions in a row to pass VND 10 million", months_to_x),
        ("PV of revenue per saver, 36 months, VND", round(v36["pv_revenue"])),
        ("PV of variable cost per saver, 36 months, VND", round(v36["pv_variable_cost"])),
        ("CAC ceiling (PV of net revenue per saver), 36 months, VND", round(v36["cac_ceiling"])),
        ("PV of revenue per saver, 60 months, VND", round(v60["pv_revenue"])),
        ("PV of variable cost per saver, 60 months, VND", round(v60["pv_variable_cost"])),
        ("CAC ceiling (PV of net revenue per saver), 60 months, VND", round(v60["cac_ceiling"])),
    ]
    for c in CHANNELS:
        rows.append((f"Acquisition cost per saver, {CHANNEL_LABEL[c].lower()}, VND", round(sched[c][1])))
    rows += [
        ("Reach cost per dormant account contacted, VND", round(p["reach_cost_per_account"])),
        ("Break-even enrolment rate of contacted accounts, 60-month ceiling, %",
         round(p["reach_cost_per_account"] / v60["cac_ceiling"] * 100, 2) if v60["cac_ceiling"] > 0 else None),
        ("Break-even enrolment rate of contacted accounts, 36-month ceiling, %",
         round(p["reach_cost_per_account"] / v36["cac_ceiling"] * 100, 2) if v36["cac_ceiling"] > 0 else None),
    ]
    return rows


def phase_budget(res, p):
    out = []
    for name, a, b in PHASES:
        sub = [r for r in res if a <= r["month"] <= b]
        out.append({"phase": name, "months": f"{a}-{b}",
                    "cost_vnd_bn": bn(sum(r["cost"] for r in sub)),
                    "of_which_build_vnd_bn": bn(sum(r["cost_build"] for r in sub)),
                    "of_which_run_and_marketing_vnd_bn": bn(sum(r["cost_run"] + r["cost_marketing"] for r in sub)),
                    "of_which_acquisition_vnd_bn": bn(sum(r["cost_acquisition"] for r in sub)),
                    "of_which_rewards_payments_vnd_bn": bn(sum(r["cost_rewards"] + r["cost_payments_service"] for r in sub)),
                    "revenue_vnd_bn": bn(sum(r["revenue"] for r in sub)),
                    "net_cash_vnd_bn": bn(sum(r["profit"] for r in sub)),
                    "cumulative_cash_at_end_vnd_bn": bn(sub[-1]["cumulative_cash"])})
    return out


def board_ask(res, p):
    """Cash needed for Phase 0 and Phase 1 (months 1 to 6), before and after contingency."""
    need = -sum(r["profit"] for r in res if r["month"] <= p["pilot_end_month"])
    return need, need * (1 + p["contingency_share"])


def tornado_rows(rows_csv, base_res):
    base_val = base_res[-1]["cumulative_cash"]
    base_p = derive(params("base", rows_csv))
    out = []
    for label, keys in TORNADO:
        vals = {}
        for side in ["low", "high"]:
            side_p = params(side, rows_csv)
            over = {k: side_p[k] for k in keys}
            cost_from = base_p if label.startswith("Enrolment") else None
            _, _, res, m = scenario("base", rows_csv, over, cost_from)
            vals[side] = (res[-1]["cumulative_cash"], m["breakeven_month"], res[35]["cumulative_cash"])
        out.append({"driver": label, "parameters": "; ".join(keys),
                    "cum_cash_m60_low_vnd_bn": bn(vals["low"][0]), "cum_cash_m60_base_vnd_bn": bn(base_val),
                    "cum_cash_m60_high_vnd_bn": bn(vals["high"][0]),
                    "swing_vnd_bn": bn(abs(vals["high"][0] - vals["low"][0])),
                    "breakeven_month_low": vals["low"][1], "breakeven_month_high": vals["high"][1],
                    "cum_cash_m36_low_vnd_bn": bn(vals["low"][2]), "cum_cash_m36_high_vnd_bn": bn(vals["high"][2])})
    return sorted(out, key=lambda r: -r["swing_vnd_bn"])


def need_to_believe(rows_csv, yields=(0.004, 0.006, 0.008, 0.010, 0.012), scales=(0.5, 1, 2, 3, 4)):
    """Cumulative cash at month 60 and payback month for a grid of net yields and enrolment volumes.

    Yields scale every asset-class yield in proportion; volumes scale every channel's enrolments while the
    acquisition cost of each saver stays at base."""
    p0 = derive(params("base", rows_csv))
    out = []
    for y in yields:
        f = y / net_yield(p0)
        p = {**p0, **{f"yield_{a}": p0[f"yield_{a}"] * f for a in ASSETS}}
        for k in scales:
            sched = {c: ([e * k for e in enr], cac) for c, (enr, cac) in channel_schedule(p, MONTHS).items()}
            res = simulate(p, MONTHS, sched)
            m = metrics(res, p)
            out.append({"net_yield_pct": round(y * 100, 2), "enrolment_scale": k,
                        "enrolled_m36": round(res[35]["enrolled_cumulative"]),
                        "balance_m36_vnd_bn": bn(res[35]["balance"]),
                        "cum_cash_m60_vnd_bn": bn(res[-1]["cumulative_cash"]),
                        "breakeven_month": m["breakeven_month"], "payback_month": m["payback_month"]})
    return out


def levers(rows_csv):
    """Management levers on the base case: each row moves one group of inputs (or several) to its upside value."""
    hi = params("high", rows_csv)
    pick = lambda keys: {k: hi[k] for k in keys}  # noqa: E731
    lean = pick(["build_cost_team", "build_cost_external", "run_cost_team", "run_cost_other", "marketing_fixed_annual"])
    yields_ = pick(["yield_golden_egg", "yield_bond_funds", "yield_equity_funds"])
    enrol = pick(["eligible_share_dormant", "conv_dormant", "conv_active", "conv_new_account",
                  "participation_employer", "employers_per_quarter"])
    cases = [
        ("Base case", {}),
        ("Partner bank waives the collection fee", {"fee_per_contribution": 0.0}),
        ("Lean team: 4 IT staff, lower overheads", lean),
        ("Upside yields: Golden Egg margin 1.5%, 40% of fund fees", yields_),
        ("Upside enrolment in every channel", enrol),
        ("Fee waived and lean team", {"fee_per_contribution": 0.0, **lean}),
        ("Fee waived, lean team, upside yields", {"fee_per_contribution": 0.0, **lean, **yields_}),
        ("Fee waived, lean team, upside yields and enrolment", {"fee_per_contribution": 0.0, **lean, **yields_, **enrol}),
        ("All inputs at upside (upside scenario)", None),
        ("DNSE's own bonds in the Golden Egg core (margin about 1.2 points; rejected, decision D7)",
         {"yield_golden_egg": 0.012}),
        ("Half of the team cost treated as shared platform spending (incremental view)",
         {"build_cost_team": 0.5 * params("base", rows_csv)["build_cost_team"],
          "run_cost_team": 0.5 * params("base", rows_csv)["run_cost_team"]}),
    ]
    out = []
    for name, over in cases:
        p, _, res, m = scenario("high", rows_csv) if over is None else scenario("base", rows_csv, over)
        cpa = cost_per_funded_account(res[-1])
        out.append({"case": name, "net_yield_pct": round(net_yield(p) * 100, 3),
                    "enrolled_m36": round(res[35]["enrolled_cumulative"]), "balance_m36_vnd_bn": bn(res[35]["balance"]),
                    "cum_cash_m36_vnd_bn": bn(res[35]["cumulative_cash"]),
                    "cum_cash_m60_vnd_bn": bn(res[-1]["cumulative_cash"]),
                    "breakeven_month": m["breakeven_month"], "payback_month": m["payback_month"],
                    "npv_60m_vnd_bn": bn(m["npv"]),
                    "new_accounts_above_10m_m60": round(res[-1]["new_accounts_above_10m"]),
                    "net_cost_per_new_10m_account_m60_vnd_m": round(cpa / 1e6, 2) if cpa is not None else None})
    return out


INDIRECT_BASE = {"investor_cash_30_june_2026": 1960.8e9, "accounts_10m_end_2025": 27_100,
                 "platform_cost_proxy_2025": 197.5e9}


def indirect_value(runs):
    """Indicators of value outside the plan's own cash flows; shown separately and not added to them.

    Bases: investor cash at DNSE on 30 June 2026 and the 2025 platform cost proxy (Round 2, Tables C1 and B3);
    accounts with VND 10 million or more at the end of 2025 (DNSE Securities, 2026c)."""
    b = INDIRECT_BASE
    out = []
    for s, (p, sched, res, m) in runs.items():
        for t in [24, 36, 60]:
            r = res[t - 1]
            acc = b["accounts_10m_end_2025"] + r["new_accounts_above_10m"]
            out.append({"scenario": s, "month": t,
                        "plan_balance_vnd_bn": bn(r["balance"]),
                        "plan_balance_pct_of_investor_cash_jun_2026": round(r["balance"] / b["investor_cash_30_june_2026"] * 100, 1),
                        "accounts_10m_plus_if_others_unchanged": round(acc),
                        "change_vs_end_2025_pct": round((acc / b["accounts_10m_end_2025"] - 1) * 100, 1),
                        "platform_cost_per_10m_account_vnd_m": round(b["platform_cost_proxy_2025"] / acc / 1e6, 2),
                        "platform_cost_per_10m_account_2025_vnd_m": round(
                            b["platform_cost_proxy_2025"] / b["accounts_10m_end_2025"] / 1e6, 2)})
    return out


def cost_per_funded_account(row):
    """Net cash spent per new account above VND 10 million up to this month (0 once the plan has paid back)."""
    n = row["new_accounts_above_10m"]
    return max(0.0, -row["cumulative_cash"]) / n if n >= 1 else None


STRESS = [  # assumptions for stress tests, shown as such
    ("Market fall in year 2: stop and withdrawal rates three times normal in months 13 to 15",
     {"stop_multiplier": dict.fromkeys((13, 14, 15), 3.0), "withdrawal_multiplier": dict.fromkeys((13, 14, 15), 3.0)}),
    ("Failed payday run in month 9: 15% of contributing savers stop; enrolment 30% lower in months 9 to 11",
     {"extra_stop_share": {9: 0.15}, "enrolment_multiplier": dict.fromkeys((9, 10, 11), 0.7)}),
    ("Both shocks", {"stop_multiplier": dict.fromkeys((13, 14, 15), 3.0),
                     "withdrawal_multiplier": dict.fromkeys((13, 14, 15), 3.0),
                     "extra_stop_share": {9: 0.15}, "enrolment_multiplier": dict.fromkeys((9, 10, 11), 0.7)}),
]


def stress_tests(rows_csv):
    p, sched, base_res, base_m = scenario("base", rows_csv)
    out = []
    for name, shock in [("Base case, no shock", {})] + STRESS:
        res = simulate_calendar(p, MONTHS, sched, shocks=shock)
        m = metrics(res, p)
        out.append({"case": name,
                    "active_m36": round(res[35]["active"]), "balance_m36_vnd_bn": bn(res[35]["balance"]),
                    "new_accounts_above_10m_m36": round(res[35]["new_accounts_above_10m"]),
                    "cum_cash_m60_vnd_bn": bn(res[-1]["cumulative_cash"]), "npv_60m_vnd_bn": bn(m["npv"]),
                    "change_balance_m36_pct": round((res[35]["balance"] / base_res[35]["balance"] - 1) * 100, 1),
                    "change_accounts_m36_pct": round((res[35]["new_accounts_above_10m"] /
                                                      base_res[35]["new_accounts_above_10m"] - 1) * 100, 1),
                    "change_cum_cash_m60_vnd_bn": bn(res[-1]["cumulative_cash"] - base_res[-1]["cumulative_cash"])})
    return out


TIER_DESIGNS = [  # DNSE-funded reward designs compared before decision D1
    ("Round 2 tiers made small: 10k / 20k / 50k gifts, 0.1-point fee rebate from 6, Golden Egg +0.2 points from 12",
     {"tier_gift_3": 10000, "tier_gift_6": 20000, "tier_gift_12": 50000, "tier_fee_discount": 0.001,
      "tier_rate_boost": 0.002}),
    ("Tested option: 30k gift at 12, 0.1-point fee rebate from 6", "option"),
    ("MVP (decision D1): non-cash features only", {}),
]


def tier_breakeven(p):
    """What each DNSE-funded reward design costs, and how much it must improve persistence to pay for itself
    (Round 2 test 3, made economic), with the base bank fee and with the fee waived.

    The rewards pay for themselves when the 60-month CAC ceiling with rewards, at a lower monthly stop rate,
    equals the ceiling without rewards at the base stop rate."""
    none = {"tier_gift_3": 0.0, "tier_gift_6": 0.0, "tier_gift_12": 0.0, "tier_fee_discount": 0.0, "tier_rate_boost": 0.0}
    out = []
    for fee_label, fee in [("base bank fee", p["fee_per_contribution"]), ("bank fee waived", 0.0)]:
        q0 = {**p, **none, "fee_per_contribution": fee}
        v_none = per_saver_value(q0, 60)
        for name, design in TIER_DESIGNS:
            if design == "option":
                design = {"tier_gift_12": p["tier_option_gift_12"], "tier_fee_discount": p["tier_option_fee_discount"]}
            q = {**q0, **design}
            v = per_saver_value(q, 60)
            cost = v_none["cac_ceiling"] - v["cac_ceiling"]
            s_need = (solve(lambda s: -per_saver_value({**q, "stop_rate_monthly": s}, 60)["cac_ceiling"],
                            0.0, q["stop_rate_monthly"], -v_none["cac_ceiling"]) if cost > 0 else q["stop_rate_monthly"])
            s0, s1 = survival(q, 13), (survival({**q, "stop_rate_monthly": s_need}, 13) if s_need is not None else None)
            out.append({"bank_fee": fee_label, "design": name,
                        "pv_reward_cost_per_saver_vnd": round(cost),
                        "reward_cost_pct_of_pv_revenue": round(cost / v["pv_revenue"] * 100, 1),
                        "cac_ceiling_60m_vnd": round(v["cac_ceiling"]),
                        "stop_rate_needed_pct": round(s_need * 100, 2) if s_need is not None else "not reachable",
                        "twelve_contribution_rate_base_pct": round(s0[11] * 100, 1),
                        "twelve_contribution_rate_needed_pct": round(s1[11] * 100, 1) if s1 else "not reachable",
                        "uplift_needed_points": round((s1[11] - s0[11]) * 100, 1) if s1 else "not reachable"})
    return out


def pilot_power(p, sizes=(20_000, 30_000, 45_000, 60_000), control_share=1 / 3):
    """Precision of the randomised pilot: enrolment is measured on the two treated arms together; the tier
    effect compares the two treated arms on the six-contribution rate (80% power, two-sided 5%)."""
    from math import sqrt
    z_a, z_b = 1.959964, 0.841621
    r = p["conv_dormant"]
    q6 = survival(p, 6)[5]
    out = []
    for n in sizes:
        treated = n * (1 - control_share)
        per_arm = treated / 2
        enrolled_arm = per_arm * r
        half = z_a * sqrt(r * (1 - r) / treated)
        mde = (z_a + z_b) * sqrt(2 * q6 * (1 - q6) / enrolled_arm)
        out.append({"pilot_accounts": n, "treated_accounts": round(treated), "savers_per_treated_arm": round(enrolled_arm),
                    "enrolment_rate_assumed_pct": round(r * 100, 2),
                    "enrolment_95ci_low_pct": round((r - half) * 100, 2), "enrolment_95ci_high_pct": round((r + half) * 100, 2),
                    "six_contribution_rate_assumed_pct": round(q6 * 100, 1),
                    "tier_effect_detectable_points": round(mde * 100, 1),
                    "outreach_cost_vnd_m": round(treated * p["reach_cost_per_account"] / 1e6, 1)})
    return out


def solve(f, lo, hi, target, steps=60):
    """Bisection for f(x) = target on [lo, hi], f monotone; None if the target is outside the range."""
    flo, fhi = f(lo) - target, f(hi) - target
    if flo * fhi > 0:
        return None
    for _ in range(steps):
        mid = (lo + hi) / 2
        fm = f(mid) - target
        if (fm < 0) == (flo < 0):
            lo, flo = mid, fm
        else:
            hi = mid
    return (lo + hi) / 2


def decision_gates(rows_csv, runs):
    """Continue / scale / adjust / stop criteria for months 3, 6, 12 and 24, derived from the model.

    Gate 0 checks that the partner terms signed in Phase 0 are no worse than the model assumes. Gate 1 has
    necessary conditions (a dormant saver is worth acquiring while reach cost / enrolment rate is below the
    60-month CAC ceiling; persistence, contribution, new money, reliability, compliance) and one programme
    test: the model re-run with the pilot's measured values must keep the net cost per new account above
    VND 10 million near the plan the Board approved. Unit economics alone cannot decide scale, because the
    fixed running cost, not the cost per saver, is what keeps the base case from paying back. Gates 2 and 3
    compare the roll-out with the base path of the model."""
    p = runs["base"][0]
    low_res, base_res = runs["low"][2], runs["base"][2]
    cpa_plan = cost_per_funded_account(base_res[-1])
    cpa_plan24 = cost_per_funded_account(base_res[23])
    ceiling = per_saver_value(p, 60)["cac_ceiling"]
    cac_base = p["reach_cost_per_account"] / p["conv_dormant"]
    r_star = p["reach_cost_per_account"] / ceiling if ceiling > 0 else None
    ceil_at = lambda over: per_saver_value({**p, **over}, 60)["cac_ceiling"]  # noqa: E731
    h_stop = solve(lambda h: -ceil_at({"stop_rate_first_90_days": h}), 0.0, 0.95, -cac_base)
    persist_stop = (1 - h_stop) ** 2 if h_stop is not None else None
    c_stop = solve(lambda c: ceil_at({"contribution": c}), 2e5, 5e6, cac_base)
    fee_limit = solve(lambda f: -ceil_at({"fee_per_contribution": f}), 0.0, 50_000.0, -cac_base)
    ceiling_no_fee = ceil_at({"fee_per_contribution": 0.0})
    emp_part = solve(lambda x: -p["cost_per_employer"] / (p["employees_per_employer"] * x), 0.01, 1.0, -ceiling)
    surv = survival(p, 13)
    m12, m24 = base_res[11], base_res[23]
    l12, l24 = low_res[11], low_res[23]
    run_month = p["run_cost_annual"] / 12
    fmt_pct = lambda x: f"{x * 100:.1f}%" if x is not None else "not reached"  # noqa: E731

    def row(gate, month, measure, scale, adjust, stop, value, derivation, owner):
        return {"gate": gate, "month": month, "measure": measure, "scale_if": scale, "adjust_if": adjust,
                "stop_if": stop, "model_base_value": value, "derivation": derivation, "owner": owner}

    out = [
        row("Gate 0: before the pilot", 3, "Partner terms signed: bank fee per contribution; share of fund fees "
            "paid to DNSE; DNSE's margin on bank bonds in Golden Egg",
            f"Fee <= VND {p['fee_per_contribution']:,.0f}; fund share >= 30%; margin >= "
            f"{p['yield_golden_egg'] * 100:.1f} points", "Worse on any term: re-run the model and renegotiate "
            "before the pilot", "Fund or bank partner not signed (launch dependency)",
            "Base assumptions", "Terms at least as good as the base case keep the plan's economics", "CFO"),
        row("Gate 0: before the pilot", 3, "Bank fee per contribution (virtual-account collection), VND",
            "0 (partner bank keeps the deposits)", f"1 to {p['fee_per_contribution']:,.0f} (list price)",
            f"> {fee_limit:,.0f}: a dormant saver no longer pays back", f"{p['fee_per_contribution']:,.0f}",
            f"Above VND {fee_limit:,.0f} the 60-month CAC ceiling falls below the base acquisition cost of "
            f"VND {cac_base:,.0f}; waiving the fee raises the ceiling from VND {ceiling:,.0f} to VND "
            f"{ceiling_no_fee:,.0f}", "CFO"),
        row("Gate 0: before the pilot", 3, "Shadow payday runs with staff accounts: transfers credited on time",
            ">= 99.5%", "-", "< 99.5%: delay the pilot", "99.5% (Round 2 gate)",
            "The 4 March 2026 outage stopped orders for two hours (DNSE disclosure)", "CTO"),
        row("Gate 1: pilot read-out", 6, "Projected net cost per new account above VND 10 million by month 60 "
            "(model re-run with the pilot's measured values and the signed terms), VND million",
            f"<= {1.25 * cpa_plan / 1e6:.1f} (1.25 x plan)", f"{1.25 * cpa_plan / 1e6:.1f} to {2 * cpa_plan / 1e6:.1f}",
            f"> {2 * cpa_plan / 1e6:.1f} (2 x plan)", f"{cpa_plan / 1e6:.2f}",
            "Programme test. The plan is the Board's budget per funded account; downside path "
            f"{cost_per_funded_account(low_res[-1]) / 1e6:.2f}", "CFO"),
        row("Gate 1: pilot read-out", 6, "Enrolment rate of treated dormant accounts (set-up and first "
            "contribution within 60 days)",
            f">= {fmt_pct(1.5 * r_star) if r_star else 'n.a.'}", f"{fmt_pct(r_star)} to {fmt_pct(1.5 * r_star)}"
            if r_star else "n.a.", f"< {fmt_pct(r_star)}", fmt_pct(p["conv_dormant"]),
            f"Break-even rate = reach cost VND {p['reach_cost_per_account']:,.0f} / 60-month CAC ceiling "
            f"VND {ceiling:,.0f}; scale at 1.5 times break-even", "Head of Product"),
        row("Gate 1: pilot read-out", 6, "Savers making three contributions in a row",
            f">= {fmt_pct(surv[2])}", f"60.0% to {fmt_pct(surv[2])}", "< 60.0%", fmt_pct(surv[2]),
            f"Scale line = base assumption; stop line = product-fit line of plan_payday.md section 5.6. The cost "
            f"line is lower: the 60-month CAC ceiling falls to the base acquisition cost of VND {cac_base:,.0f} "
            f"only at {fmt_pct(persist_stop)}", "Head of Product"),
        row("Gate 1: pilot read-out", 6, "Average monthly contribution, VND",
            f">= {p['contribution']:,.0f}", f"{c_stop:,.0f} to {p['contribution']:,.0f}" if c_stop else "n.a.",
            f"< {c_stop:,.0f}" if c_stop else "n.a.", f"{p['contribution']:,.0f}",
            "Stop line = contribution at which the 60-month CAC ceiling falls to the base acquisition cost",
            "CFO"),
        row("Gate 1: pilot read-out", 6, "Share of plan inflows that is new money (tagged by source)",
            ">= 80%", "60% to 80%", "< 60%", "80% (Round 2 test 7)",
            "Money moved from the Never-Sleeping Account or Golden Egg adds no balance", "CFO"),
        row("Gate 1: pilot read-out", 6, "Scheduled transfers credited on time", ">= 99.5%", "-",
            "< 99.5% (launch gate)", "99.5% (Round 2 gate)", "Reliability gate of Round 2 (Table F6, test 6)",
            "CTO"),
        row("Gate 1: pilot read-out", 6, "Compliance: SSC notice filed; model portfolios signed off by a "
            "licensed adviser", "Written confirmation", "-", "Missing (launch gate)", "Required",
            "Circular 121/2020, Articles 4 and 24; the 2026 fine for unreported services", "Compliance"),
        row("Gate 2: first roll-out year", 12, "Funded savers (three or more contributions in a row)",
            f">= {0.8 * m12['funded_savers']:,.0f} (80% of plan)",
            f"{0.5 * m12['funded_savers']:,.0f} to {0.8 * m12['funded_savers']:,.0f}",
            f"< {0.5 * m12['funded_savers']:,.0f} for two quarters", f"{m12['funded_savers']:,.0f}",
            f"Base path of the model; downside path {l12['funded_savers']:,.0f}", "Head of Product"),
        row("Gate 2: first roll-out year", 12, "Plan balances, VND billion",
            f">= {0.8 * m12['balance'] / 1e9:,.1f} (80% of plan)",
            f"{0.5 * m12['balance'] / 1e9:,.1f} to {0.8 * m12['balance'] / 1e9:,.1f}",
            f"< {0.5 * m12['balance'] / 1e9:,.1f} for two quarters", f"{m12['balance'] / 1e9:,.1f}",
            f"Base path; downside path {l12['balance'] / 1e9:,.1f}", "CFO"),
        row("Gate 2: first roll-out year", 12, "Acquisition cost per funded saver, VND",
            f"<= {ceiling:,.0f} (CAC ceiling)", "-", f"> {ceiling:,.0f} for two quarters",
            f"{cac_base / surv[2]:,.0f}", "Base acquisition cost divided by the three-contribution rate", "CFO"),
        row("Gate 3: scale-up review", 24, "Monthly plan revenue against monthly running cost",
            f">= {m24['revenue'] / run_month * 100:.0f}% (plan)", "-",
            f"< {l24['revenue'] / run_month * 100:.0f}% (downside path): review the revenue model",
            f"{m24['revenue'] / run_month * 100:.0f}%",
            f"Running cost VND {run_month / 1e9:.2f} billion a month; revenue VND {m24['revenue'] / 1e9:.2f} billion",
            "CFO"),
        row("Gate 3: scale-up review", 24, "New accounts above VND 10 million from the plan",
            f">= {0.8 * m24['new_accounts_above_10m']:,.0f} (80% of plan)", "-",
            f"< {l24['new_accounts_above_10m']:,.0f} (downside path)", f"{m24['new_accounts_above_10m']:,.0f}",
            "North Star; savers whose own plan balance has passed VND 10 million", "CEO"),
        row("Gate 3: scale-up review", 24, "Employer channel: share of employees who enrol after the HR session",
            f">= {emp_part * 100:.0f}%", f"{p['participation_employer'] * 100:.0f}% to {emp_part * 100:.0f}%: "
            "lower the cost per employer", f"< {p['participation_employer'] * 100:.0f}%: stop the channel",
            f"{p['participation_employer'] * 100:.0f}%",
            f"At VND {p['cost_per_employer'] / 1e6:.0f} million per employer and {p['employees_per_employer']:.0f} "
            f"employees, a saver costs less than the CAC ceiling only from {emp_part * 100:.0f}% enrolment",
            "Head of Product"),
        row("Gate 3: scale-up review", 24, "Net cost per new account above VND 10 million to date, VND million",
            f"<= {1.25 * cpa_plan24 / 1e6:.1f} (1.25 x plan)", f"{1.25 * cpa_plan24 / 1e6:.1f} to "
            f"{2 * cpa_plan24 / 1e6:.1f}", f"> {2 * cpa_plan24 / 1e6:.1f}: fold into the core app team or stop",
            f"{cpa_plan24 / 1e6:.2f}", "Same programme test as Gate 1, on actual results", "CFO"),
    ]
    return out, {"cac_ceiling_60m": ceiling, "breakeven_enrolment": r_star, "cac_base_dormant": cac_base,
                 "persistence_stop": persist_stop, "contribution_stop": c_stop, "fee_limit": fee_limit,
                 "ceiling_no_fee": ceiling_no_fee, "employer_participation_needed": emp_part,
                 "cost_per_account_plan_m60": cpa_plan, "cost_per_account_plan_m24": cpa_plan24,
                 "persistence_3_base": surv[2]}


def main():
    rows_csv = load_assumptions()
    runs = {s: scenario(s, rows_csv) for s in SCENARIOS}
    for s, (p, sched, res, m) in runs.items():
        write_csv(f"payday_monthly_{s}.csv", monthly_table(res))

    summary = []
    for s, (p, sched, res, m) in runs.items():
        need, ask = board_ask(res, p)
        row = {"scenario": s, "phase_0_1_cash_need_vnd_bn": bn(need), "phase_0_1_with_contingency_vnd_bn": bn(ask),
               "breakeven_month": m["breakeven_month"], "operating_breakeven_month": m["operating_breakeven_month"],
               "payback_month": m["payback_month"],
               "peak_funding_need_vnd_bn": bn(m["peak_funding_need"]), "peak_funding_month": m["peak_funding_month"],
               "npv_60m_vnd_bn": bn(m["npv"]), "net_yield_pct": round(net_yield(p) * 100, 3)}
        for t in (36, 60):
            cpa = cost_per_funded_account(res[t - 1])
            row[f"m{t}_net_cost_per_new_10m_account_vnd_m"] = round(cpa / 1e6, 2) if cpa is not None else None
        for t in MILESTONES:
            r = res[t - 1]
            row.update({f"m{t}_enrolled": round(r["enrolled_cumulative"]), f"m{t}_active": round(r["active"]),
                        f"m{t}_funded": round(r["funded_savers"]), f"m{t}_balance_vnd_bn": bn(r["balance"]),
                        f"m{t}_savers_above_10m": round(r["savers_above_10m"]),
                        f"m{t}_new_accounts_above_10m": round(r["new_accounts_above_10m"]),
                        f"m{t}_cumulative_cash_vnd_bn": bn(r["cumulative_cash"])})
        summary.append(row)
    write_csv("payday_scenarios.csv", summary)

    ue = {s: dict(unit_economics(p, sched)) for s, (p, sched, res, m) in runs.items()}
    write_csv("payday_unit_economics.csv", [{"measure": k, **{s: ue[s][k] for s in SCENARIOS}} for k in ue["base"]])

    write_csv("payday_phase_budget.csv",
              [{"scenario": s, **r} for s, (p, sched, res, m) in runs.items() for r in phase_budget(res, p)])
    base_res = runs["base"][2]
    write_csv("payday_tornado.csv", tornado_rows(rows_csv, base_res))

    opt = []
    for s in SCENARIOS:
        share = params(s, rows_csv)["lending_share_option"]
        p, sched, res, m = scenario(s, rows_csv, {"lending_share": share})
        opt.append({"scenario": s, "lending_share_of_balance": share,
                    "start_month": int(p["lending_start_month"]),
                    "cum_cash_m36_vnd_bn": bn(res[35]["cumulative_cash"]),
                    "cum_cash_m60_vnd_bn": bn(res[-1]["cumulative_cash"]),
                    "breakeven_month": m["breakeven_month"], "payback_month": m["payback_month"],
                    "npv_60m_vnd_bn": bn(m["npv"])})
    write_csv("payday_option_lending.csv", opt)
    gates, _ = decision_gates(rows_csv, runs)
    write_csv("payday_decision_gates.csv", gates)
    write_csv("payday_need_to_believe.csv", need_to_believe(rows_csv))
    write_csv("payday_indirect_value.csv", indirect_value(runs))
    write_csv("payday_levers.csv", levers(rows_csv))
    write_csv("payday_stress.csv", stress_tests(rows_csv))
    write_csv("payday_tier_breakeven.csv", tier_breakeven(runs["base"][0]))
    write_csv("payday_pilot_power.csv", pilot_power(runs["base"][0]))
    return runs


if __name__ == "__main__":
    main()

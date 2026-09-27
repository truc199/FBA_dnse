"""Computations shared by the figures and tables. Every number is derived from the files in data/."""
import csv
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from config import DATA, MANUAL

sys.path.insert(0, str(Path(__file__).resolve().parent / "pipeline"))


# ---------------------------------------------------------------- loaders
def load_json(name):
    with open(DATA / name, encoding="utf-8") as f:
        return json.load(f)


def load_csv(path):
    with open(path, encoding="utf-8-sig") as f:
        return list(csv.DictReader(f))


def manual(name):
    return load_csv(MANUAL / name)


DNSE = load_json("dnse_financials.json")
Q, A, H = DNSE["quarterly"], DNSE["annual"], DNSE["half_year"]
PEERS = load_json("peer_financials.json")["firms"]


def quarters(start, end):
    ks = sorted(Q)
    return [k for k in ks if start <= k <= end]


def prev_q(q):
    y, n = int(q[:4]), int(q[-1])
    return f"{y - 1}Q4" if n == 1 else f"{y}Q{n - 1}"


def v(d, key):
    x = d.get(key)
    return 0.0 if x is None else float(x)


# ---------------------------------------------------------------- DNSE income statement (Table B1)
FLOW_KEYS = ["revenue", "rev_lending", "rev_htm", "rev_brokerage", "cost_brokerage", "interest_expense",
             "cost_provision_and_loan_funding", "admin_cost", "pbt", "rev_fvtpl", "cost_fvtpl"]


def sum_quarters(year):
    """Income-statement lines for a year as the sum of its four quarterly statements."""
    return {k: sum(v(Q[f"{year}Q{i}"], k) for i in range(1, 5)) for k in FLOW_KEYS}


def income_row(period, basis="annual"):
    """Table B1 lines for FY2021 ... FY2025 or 2026H1 (VND billion, costs as positive numbers).

    basis="annual" reads the annual statements; basis="quarters" adds up the four quarterly statements,
    which is how the published Table B1 was compiled. The two differ by less than VND 0.1 billion a line."""
    if period.startswith("FY"):
        d = A[period] if basis == "annual" else sum_quarters(period[2:])
    else:
        d = H[period]
    net_prop = v(d, "rev_fvtpl") + v(d, "cost_fvtpl")
    return {
        "operating_revenue": v(d, "revenue"),
        "margin_interest": v(d, "rev_lending"),
        "deposit_and_htm_interest": v(d, "rev_htm"),
        "brokerage_revenue": v(d, "rev_brokerage"),
        "direct_brokerage_cost": -v(d, "cost_brokerage"),
        "interest_expense_plus_line24": -(v(d, "interest_expense") + v(d, "cost_provision_and_loan_funding")),
        "administrative_expenses": -v(d, "admin_cost"),
        "pretax_profit": v(d, "pbt"),
        "net_proprietary_result": net_prop,
        "core_pretax_profit": v(d, "pbt") - net_prop,
        "proprietary_trading_losses": -v(d, "cost_fvtpl"),
    }


PERIODS = ["FY2021", "FY2022", "FY2023", "FY2024", "FY2025", "2026H1"]


def period_label(p):
    return "H1 2026" if p == "2026H1" else p[2:]


# ---------------------------------------------------------------- funding cost (Appendix A2 method)
def funding_cost(d_now, d_prev):
    """Interest expense plus template line 24, less the rise in the loan-loss allowance (VND bn, positive)."""
    allowance_rise = abs(v(d_now, "loan_allowance")) - abs(v(d_prev, "loan_allowance"))
    return -v(d_now, "interest_expense") - v(d_now, "cost_provision_and_loan_funding") - allowance_rise


def debt(d):
    return v(d, "short_term_borrowing") + v(d, "bonds_short") + v(d, "bonds_long")


def cost_of_funds_pct(series, q):
    """Annualised funding cost over average debt for quarter q of a quarterly dict."""
    p = prev_q(q)
    avg = (debt(series[q]) + debt(series[p])) / 2
    return funding_cost(series[q], series[p]) * 4 / avg * 100


def yield_pct(series, q, rev_key, stock_keys):
    p = prev_q(q)
    stock = lambda d: sum(v(d, k) for k in stock_keys)
    avg = (stock(series[q]) + stock(series[p])) / 2
    return v(series[q], rev_key) * 4 / avg * 100


def deposits_htm_share(series, q):
    d = series[q]
    return (v(d, "htm_assets") + v(d, "htm_assets_long")) / v(d, "total_assets") * 100


# ---------------------------------------------------------------- platform and overhead cost proxy (Table B3)
def platform_proxy():
    rows = load_csv(DATA / "dnse_financials_annual.csv")
    by_field = {r["field"]: r for r in rows}
    out = {}
    for y in ["2021", "2022", "2023", "2024", "2025"]:
        col = f"FY{y}"
        staff = abs(float(by_field["nos350"][col]))        # labour costs, general and administrative note
        outsourced = abs(float(by_field["nos352"][col]))   # outside services, same note
        dep = abs(float(by_field["cfa2"][col]))            # depreciation and amortisation, cash flow statement
        out[y] = {"staff": staff, "outsourced": outsourced, "depreciation": dep,
                  "total": staff + outsourced + dep}
    return out


def account_metric(metric):
    return {r["date"]: float(r["value"]) for r in manual("dnse_accounts.csv") if r["metric"] == metric}


# ---------------------------------------------------------------- peers (Table C2, Figure 6, Figure C1)
PEER_ORDER = ["DNSE", "TCBS", "VPBankS", "SSI", "VPS"]


def peer_series(name):
    return Q if name == "DNSE" else PEERS[name]["quarterly"]


def peer_metrics(q="2026Q2"):
    accts = {r["firm"]: (float(r["accounts_million"]) if r["accounts_million"] else None)
             for r in manual("peer_accounts.csv")}
    out = {}
    for name in PEER_ORDER:
        s = peer_series(name)
        pbt_q = v(s[q], "pbt")
        out[name] = {
            "deposits_htm_pct_assets": deposits_htm_share(s, q),
            "cost_of_funds_pct": cost_of_funds_pct(s, q),
            "loans_bn": v(s[q], "loans"),
            "pbt_q_bn": pbt_q,
            "accounts_m": accts.get(name),
        }
        if accts.get(name):
            out[name]["loans_per_account_m"] = v(s[q], "loans") / (accts[name] * 1e6) * 1e3
            out[name]["pbt_per_account_k"] = pbt_q / (accts[name] * 1e6) * 1e6
    return out


# ---------------------------------------------------------------- reviews (Figure 8, Tables D1 and D2)
RELIABILITY = {"stability", "onboarding"}
TRUST = {"fraud", "promo", "closure"}
THEME_ROWS = [("stability", "Crashes, freezes, login failures"), ("onboarding", "Account opening, identity checks"),
              ("fraud", "Accusation of deception"), ("promo", "Sign-up bonus terms"),
              ("money", "Deposits and withdrawals"), ("closure", "Account closure and its fee")]
APPS = [("DNSE", "vn.com.encapital.arrow"), ("VPS", "vn.com.vpbs.smartone"), ("FPTS", "com.fpts.eztrade")]


def flagged(package):
    return load_csv(DATA / f"reviews_flagged_{package}.csv")


def negatives(package, start=None, end=None):
    out = []
    for r in flagged(package):
        if r["keep"] != "1" or int(r["rating"]) > 2:
            continue
        if start and r["date"] < start:
            continue
        if end and r["date"] > end:
            continue
        out.append(r)
    return out


def themes(r):
    return set(t for t in (r["themes"] or "").split("|") if t)


def theme_shares(package="vn.com.encapital.arrow"):
    neg = negatives(package)
    votes = sum(int(r["thumbs_up"] or 0) for r in neg)
    rows = []
    for key, label in THEME_ROWS:
        sel = [r for r in neg if key in themes(r)]
        rows.append({"theme": label, "negative_reviews": len(sel),
                     "share_of_negative_pct": len(sel) / len(neg) * 100,
                     "share_of_votes_pct": sum(int(r["thumbs_up"] or 0) for r in sel) / votes * 100})
    for label, keys in [("Any trust theme (deception, bonus terms, closure)", TRUST),
                        ("Any product theme (stability, onboarding)", RELIABILITY)]:
        sel = [r for r in neg if themes(r) & keys]
        rows.append({"theme": label, "negative_reviews": len(sel),
                     "share_of_negative_pct": len(sel) / len(neg) * 100,
                     "share_of_votes_pct": sum(int(r["thumbs_up"] or 0) for r in sel) / votes * 100})
    return len(neg), votes, rows


def reliability_trust(window=("2025-01-01", "2026-09-21")):
    out = {}
    for name, pkg in APPS:
        neg = negatives(pkg, *window)
        votes = sum(int(r["thumbs_up"] or 0) for r in neg) or 1
        rel = [r for r in neg if themes(r) & RELIABILITY]
        tru = [r for r in neg if themes(r) & TRUST]
        out[name] = {"negative_n": len(neg),
                     "reliability_pct": len(rel) / len(neg) * 100,
                     "reliability_votes_pct": sum(int(r["thumbs_up"] or 0) for r in rel) / votes * 100,
                     "trust_pct": len(tru) / len(neg) * 100,
                     "trust_votes_pct": sum(int(r["thumbs_up"] or 0) for r in tru) / votes * 100}
    return out


# ---------------------------------------------------------------- Findex segments (Figure 9, Tables E1 and E2)
import findex_data as F  # noqa: E402  (module in src/pipeline)

SEG_INDEX = {name: i for i, name in enumerate(F.SEGMENTS)}
IND = {code: vals for code, label, cat, vals in F.SEG2024}
SEGMENT_LABEL = {"All adults": "All adults", "Women": "Women", "Men": "Men", "Young (15-24)": "Aged 15 to 24",
                 "Older (25+)": "Aged 25 and over", "Primary educ or less": "Primary education or less",
                 "Secondary educ or more": "Secondary education or more", "Poorest 40%": "Poorest 40 per cent",
                 "Richest 60%": "Richest 60 per cent", "Rural": "Rural", "Urban": "Urban",
                 "Out of labour force": "Out of labour force", "In labour force": "In labour force"}


def segment_rows():
    rows = {r["segment"]: r for r in load_json("segment_model.json")["rows"]}
    return rows


WEIGHTS = {"Equal weights": (1, 1, 1, 1, 1, 1), "Value-heavy": (3, 1, 1, 1, 2, 2),
           "Scale-heavy": (1, 1, 1, 3, 1, 1), "Reach-heavy": (1, 3, 2, 1, 1, 1)}


def segment_ranks():
    """Table E2: min-max normalise six criteria across the twelve segments and rank by weighted score."""
    rows = segment_rows()
    segs = [s for s in F.SEGMENTS if s != "All adults"]
    crit = {}
    for s in segs:
        r = rows[s]
        i = SEG_INDEX[s]
        crit[s] = [r["index_a_investable"], r["index_b_digital"], r["activation_gap_pp"],
                   r["unactivated_adults_m"], IND["fin32.acc"][i], IND["fin17f"][i]]
    lo = [min(crit[s][k] for s in segs) for k in range(6)]
    hi = [max(crit[s][k] for s in segs) for k in range(6)]
    norm = {s: [(crit[s][k] - lo[k]) / (hi[k] - lo[k]) for k in range(6)] for s in segs}
    ranks = {}
    for scheme, w in WEIGHTS.items():
        score = {s: sum(a * b for a, b in zip(w, norm[s])) / sum(w) for s in segs}
        order = sorted(segs, key=lambda s: -score[s])
        ranks[scheme] = {s: order.index(s) + 1 for s in segs}
    return ranks


def top_four_all():
    r = segment_ranks()
    return [s for s in r["Equal weights"] if all(r[k][s] <= 4 for k in r)]


# ---------------------------------------------------------------- scenarios (Table F5, Figure F1)
def scenarios():
    base = {r["item"]: float(r["value"]) for r in manual("scenario_baseline.csv")}
    out = []
    for r in manual("scenario_assumptions.csv"):
        savers, c, kept, months = float(r["savers"]), float(r["monthly_contribution_vnd_m"]), float(r["share_kept"]), float(r["months"])
        assets_tn = savers * c * kept * months / 1e6
        out.append({
            "scenario": r["scenario"], "savers": savers, "monthly_contribution_vnd_m": c, "share_kept": kept,
            "assets_vnd_tn": assets_tn,
            "multiple_of_investor_cash": assets_tn / base["investor_cash_30_june_2026_vnd_tn"],
            "annual_fees_vnd_bn": assets_tn * 1e3 * float(r["fee_yield_pct"]) / 100,
            "tier_interest_upper_bound_vnd_bn": savers * c * 1e6 * float(r["top_rate_gap_pct"]) / 100 / 1e9,
            "accounts_10m_plus": base["accounts_10m_plus_end_2025"] + savers,
            "share_of_mid_2026_base_pct": (base["accounts_10m_plus_end_2025"] + savers) / base["accounts_mid_2026"] * 100,
        })
    return out


if __name__ == "__main__":
    pm = peer_metrics()
    for k, d in pm.items():
        print(k, {a: round(b, 2) for a, b in d.items() if b is not None})
    pp = platform_proxy(); print({y: round(d["total"], 1) for y, d in pp.items()})
    n, votes, rows = theme_shares(); print(n, votes, [(r["theme"][:18], round(r["share_of_negative_pct"], 1), round(r["share_of_votes_pct"], 1)) for r in rows])
    print({k: {a: round(b, 1) for a, b in d.items()} for k, d in reliability_trust().items()})
    print(segment_ranks()["Equal weights"]); print(top_four_all())
    for s in scenarios(): print({k: (round(v_, 2) if isinstance(v_, float) else v_) for k, v_ in s.items()})
    print("DNSE Q2 2026 pbt", Q["2026Q2"]["pbt"], "cost of funds Q2", round(cost_of_funds_pct(Q, "2026Q2"), 2))

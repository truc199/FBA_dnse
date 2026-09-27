"""Data charts in the report (Figures 1 to 9, 11, 13 and the appendix figures), drawn from data/."""
import sys
from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Patch
from matplotlib.lines import Line2D

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import analysis as AN  # noqa: E402
from figures.style import save, ygrid, xgrid  # noqa: E402
from config import (RED, DARK_RED, LIGHT_RED, CORAL, PEACH, CHARCOAL, MID_GREY, GREY,  # noqa: E402
                    LIGHT_GREY)


def fmt(x, d=1):
    return f"{x:,.{d}f}"


def half_up(x, d=0):
    """Round to one more decimal first, then half up, as the report's tables do (197.498 -> 197.5 -> 198)."""
    from decimal import Decimal, ROUND_HALF_UP
    q = Decimal(str(round(x, d + 1))).quantize(Decimal(1).scaleb(-d), rounding=ROUND_HALF_UP)
    return f"{q:,}"


# ------------------------------------------------------------------ Figure 1
def fig01_idle_cash_returns():
    rows = AN.manual("idle_cash_rates.csv")
    colour = {"DNSE": RED, "Competing broker": MID_GREY, "Bank": LIGHT_GREY, "Inflation": PEACH}
    fig, ax = plt.subplots(figsize=(7.5, 3.3))
    y = np.arange(len(rows))[::-1]
    for yi, r in zip(y, rows):
        lo, hi = float(r["low"]), float(r["high"])
        ax.barh(yi, lo, color=colour[r["group"]], height=0.62)
        if hi > lo:
            ax.barh(yi, hi - lo, left=lo, color="#EBEBEB", hatch="///", edgecolor="#BDBDBD", lw=0, height=0.62)
            label = f"{lo:g} to {hi:g}"
        else:
            label = f"{lo:g}"
        ax.text(hi + 0.12, yi, label, va="center", fontsize=10.5)
    ax.set_yticks(y)
    ax.set_yticklabels([r["label"] for r in rows], fontsize=10.5)
    ax.set_xlim(0, 10.6)
    ax.set_xlabel("Per cent a year")
    xgrid(ax)
    ax.legend(handles=[Patch(color=c, label=k) for k, c in colour.items()], loc="upper right", fontsize=10.5)
    return save(fig, "fig01_idle_cash_returns.png")


# ------------------------------------------------------------------ Figure 2
def fig02_investor_cash_index():
    qs = ["2025Q3", "2025Q4", "2026Q1", "2026Q2"]
    dnse = [AN.v(AN.Q[q], "customer_cash_trading") for q in qs]
    dn = [x / dnse[0] * 100 for x in dnse]
    ind_rows = {r["quarter"]: r["investor_cash_vnd_trillion"] for r in AN.manual("industry_investor_cash.csv")}
    ind = [float(ind_rows[q]) if ind_rows[q] else None for q in qs]
    ind_i = [x / ind[0] * 100 if x else None for x in ind]
    x = np.arange(4)
    fig, ax = plt.subplots(figsize=(7.0, 2.85))
    known = [(i, val) for i, val in enumerate(ind_i) if val is not None]
    ax.plot([k[0] for k in known[:2]], [k[1] for k in known[:2]], color=LIGHT_GREY, lw=1.6, ls=":")
    ax.plot([k[0] for k in known[1:]], [k[1] for k in known[1:]], color=GREY, lw=2.2)
    ax.plot([k[0] for k in known], [k[1] for k in known], "o", color=GREY, ms=5)
    ax.plot(x, dn, color=RED, lw=2.6, marker="o", ms=5)
    ax.text(3.06, dn[-1] - 4, f"{dn[-1]:.0f}", va="center", fontsize=11)
    ax.text(3.06, ind_i[-1] + 4, f"{ind_i[-1]:.0f}", va="center", fontsize=11)
    ax.set_xticks(x)
    ax.set_xticklabels(["Q3 2025", "Q4 2025", "Q1 2026", "Q2 2026"])
    ax.set_ylim(40, 110)
    ax.set_yticks(range(40, 111, 10))
    ax.set_ylabel("Investor cash, Q3 2025 = 100")
    ygrid(ax)
    ax.legend(handles=[Line2D([], [], color=GREY, marker="o", lw=0, label="All brokers (VnEconomy tally; Q4 2025 not reported)"),
                       Line2D([], [], color=RED, marker="o", lw=2.6, label="DNSE")], loc="lower left", fontsize=10.5)
    return save(fig, "fig02_investor_cash_index.png")


# ------------------------------------------------------------------ Figure 3
def fig03_funding_funnel():
    m = {r["metric"]: float(r["value"]) for r in AN.manual("dnse_accounts.csv") if r["date"].startswith("2025")}
    total = AN.account_metric("accounts_year_end")["2025-12-31"]
    items = [("Used at least one product\nin December 2025", m["active_customers"], f"{m['active_customers']:,.0f}"),
             ("Net assets of VND 10 million\nor more", m["net_assets_10m_plus"], f"{m['net_assets_10m_plus']:,.0f}"),
             ("Registered for the idle-cash\naccount (Never-Sleeping Account)", m["idle_cash_registered"], f"{m['idle_cash_registered']:,.0f}"),
             ("Net assets of VND 1 billion\nor more", m["net_assets_1bn_plus"], f"more than {m['net_assets_1bn_plus']:,.0f}"),
             ("Active in Golden Egg bonds\nin December 2025", m["golden_egg_active"], f"{m['golden_egg_active']:,.0f}")]
    fig, ax = plt.subplots(figsize=(10, 4.1), dpi=160)
    y = np.arange(len(items))[::-1]
    for yi, (lab, val, txt) in zip(y, items):
        pct = val / total * 100
        ax.barh(yi, pct, color=RED, height=0.6)
        ax.text(pct + 0.08, yi, f"{txt} ({pct:.{2 if pct < 0.5 else 1}f}%)", va="center", fontsize=12)
    ax.set_yticks(y)
    ax.set_yticklabels([i[0] for i in items], fontsize=12)
    ax.set_xlim(0, 8)
    ax.set_xlabel(f"Per cent of DNSE's {total:,.0f} accounts at 31 December 2025", fontsize=12.5)
    ax.tick_params(axis="x", labelsize=12)
    xgrid(ax)
    fig.tight_layout()
    return save(fig, "fig03_funding_funnel.png", tight=False, dpi=160)


# ------------------------------------------------------------------ Figure 4
def fig04_market_position():
    rows = AN.manual("market_position.csv")
    fig, ax = plt.subplots(figsize=(7.6, 2.8))
    y = np.arange(len(rows))[::-1]
    acct_share = None
    for yi, r in zip(y, rows):
        if r["dnse_value"]:
            lo = hi = float(r["dnse_value"]) / float(r["market_total"]) * 100
        else:
            lo, hi = float(r["share_low"]), float(r["share_high"])
        if r["measure"].startswith("Customer accounts"):
            acct_share = lo
        col = RED if r["group"] == "reach" else PEACH
        if r["estimate"] == "1":
            ax.barh(yi, hi, color="white", edgecolor=col, hatch="////", height=0.6, lw=1.2)
            txt = f"{lo:.1f} to {hi:.1f}"
        else:
            ax.barh(yi, lo, color=col, height=0.6)
            txt = f"{lo:.1f}"
        ax.text(hi + 0.3, yi, txt, va="center", fontsize=10.5)
    ax.axvline(acct_share, color=CHARCOAL, lw=1, ls="--")
    ax.text(acct_share + 0.2, -0.9, f"DNSE's account share, {acct_share:.1f}%", fontsize=10)
    ax.set_yticks(y)
    ax.set_yticklabels([r["measure"] for r in rows], fontsize=10.5)
    ax.set_xlim(0, 28.5)
    ax.set_ylim(-1.3, len(rows) - 0.4)
    ax.set_xlabel("DNSE share of the named market, per cent")
    xgrid(ax)
    ax.legend(handles=[Patch(color=RED, label="Reach and activity"), Patch(color=PEACH, label="Money and profit")],
              loc="lower right", fontsize=10.5)
    return save(fig, "fig04_market_position.png")


# ------------------------------------------------------------------ Figure 5
def fig05_brokerage_vs_cost():
    qs = AN.quarters("2021Q1", "2026Q2")
    rev = np.array([AN.v(AN.Q[q], "rev_brokerage") for q in qs])
    cost = np.array([-AN.v(AN.Q[q], "cost_brokerage") for q in qs])
    net = rev - cost
    streak = 0
    for n in net[::-1]:
        if n < 0:
            streak += 1
        else:
            break
    first = qs[len(qs) - streak]
    shortfall = -net[-streak:].sum()
    fig, (a1, a2) = plt.subplots(2, 1, figsize=(6.5, 4.05), sharex=True, gridspec_kw={"height_ratios": [2.3, 1]})
    x = np.arange(len(qs))
    a1.plot(x, rev, color=RED, lw=2.4, label="Brokerage revenue")
    a1.plot(x, cost, color=PEACH, lw=2.4, label="Direct brokerage cost")
    a1.set_ylabel("VND billion")
    a1.legend(loc="upper left", fontsize=12)
    ygrid(a1)
    a2.bar(x, net, color=[RED if n >= 0 else PEACH for n in net], width=0.62)
    a2.axhline(0, color=CHARCOAL, lw=1)
    a2.set_ylabel("Net, VND bn")
    ygrid(a2)
    lab = lambda q: f"Q{q[-1]} {q[:4]}"
    a2.text(len(qs) - streak - 0.4, net.max() * 1.05,
            f"{lab(first)} to {lab(qs[-1])}: {streak} quarters below direct cost,\ncumulative shortfall VND {shortfall:,.0f} billion",
            fontsize=11.5, va="top")
    a2.set_xticks([i for i, q in enumerate(qs) if q.endswith("Q1")])
    a2.set_xticklabels([q[:4] for q in qs if q.endswith("Q1")])
    fig.tight_layout()
    return save(fig, "fig05_brokerage_vs_cost.png")


# ------------------------------------------------------------------ Figure 6
def fig06_funding_structure():
    pm = AN.peer_metrics("2026Q2")
    names = AN.PEER_ORDER
    labels = {"DNSE": "DNSE\n(no parent bank)", "TCBS": "TCBS\n(Techcombank)", "VPBankS": "VPBankS\n(VPBank)",
              "SSI": "SSI\n(no parent bank)", "VPS": "VPS\n(no parent bank)"}
    fig, axs = plt.subplots(1, 2, figsize=(7.0, 3.2))
    for ax, key, title, fmt_d in [(axs[0], "deposits_htm_pct_assets", "Term deposits and bonds held to\nmaturity, % of total assets, 30 June 2026", 1),
                                  (axs[1], "cost_of_funds_pct", "Estimated cost of funds,\n% a year, Q2 2026", 1)]:
        vals = [pm[n][key] for n in names]
        y = np.arange(len(names))[::-1]
        ax.barh(y, vals, color=[RED if n == "DNSE" else GREY for n in names], height=0.6)
        for yi, val in zip(y, vals):
            ax.text(val + max(vals) * 0.02, yi, f"{val:.{fmt_d}f}", va="center", fontsize=11)
        ax.set_yticks(y)
        ax.set_yticklabels([labels[n] for n in names], fontsize=10.5)
        ax.set_title(title, fontsize=11.5, loc="left", fontweight="bold")
        ax.set_xlim(0, max(vals) * 1.22)
        xgrid(ax)
    fig.tight_layout()
    return save(fig, "fig06_funding_structure.png")


# ------------------------------------------------------------------ Figure 7
def fig07_platform_cost():
    pp = AN.platform_proxy()
    yrs = list(pp)
    acc = AN.account_metric("accounts_year_end")["2025-12-31"]
    act = {r["date"]: float(r["value"]) for r in AN.manual("dnse_accounts.csv") if r["metric"] == "active_customers"}["2025-12"]
    rich = {r["date"]: float(r["value"]) for r in AN.manual("dnse_accounts.csv") if r["metric"] == "net_assets_10m_plus"}["2025-12"]
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(6.75, 3.35), gridspec_kw={"width_ratios": [1.1, 1]})
    x = np.arange(len(yrs))
    bottom = np.zeros(len(yrs))
    for key, lab, col in [("staff", "Staff costs", RED), ("outsourced", "Outsourced services", CORAL),
                          ("depreciation", "Depreciation, amortisation", PEACH)]:
        vals = np.array([pp[y][key] for y in yrs])
        a1.bar(x, vals, bottom=bottom, color=col, width=0.62, label=lab)
        bottom += vals
    for xi, t in zip(x, bottom):
        a1.text(xi, t + 4, half_up(t), ha="center", fontsize=11, fontweight="bold")
    a1.set_xticks(x)
    a1.set_xticklabels(yrs)
    a1.set_ylabel("VND billion")
    a1.set_ylim(0, 300)
    a1.set_yticks(range(0, 251, 50))
    a1.set_title("Cost proxy, 2021 to 2025", fontsize=11.5, loc="left", fontweight="bold")
    a1.legend(loc="upper left", fontsize=10, handlelength=1.6)
    ygrid(a1)
    total = pp["2025"]["total"] * 1e9
    per = [("Per account\n(" + f"{acc / 1e6:.2f} million)", total / acc / 1e6, LIGHT_GREY),
           ("Per active user\n(" + f"{act:,.0f})", total / act / 1e6, RED),
           ("Per account with\nVND 10m or more\n(" + f"{rich:,.0f})", total / rich / 1e6, RED)]
    y = np.arange(3)[::-1]
    for yi, (lab, val, col) in zip(y, per):
        a2.barh(yi, val, color=col, height=0.6)
        a2.text(val + 0.1, yi, f"VND {val:.2f}m", va="center", fontsize=11)
    a2.set_yticks(y)
    a2.set_yticklabels([p[0] for p in per], fontsize=10.5)
    a2.set_xlabel("VND million a year, 2025")
    a2.set_xlim(0, 9.5)
    a2.set_title("Who carries the 2025 cost", fontsize=11.5, loc="left", fontweight="bold")
    xgrid(a2)
    fig.tight_layout()
    return save(fig, "fig07_platform_cost.png")


# ------------------------------------------------------------------ Figure 8
def fig08_complaint_themes():
    n, votes, rows = AN.theme_shares()
    rows = rows[:6]
    rt = AN.reliability_trust()
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(7.9, 3.85), gridspec_kw={"width_ratios": [1.45, 1]})
    y = np.arange(len(rows))[::-1]
    h = 0.36
    a1.barh(y + h / 2, [r["share_of_negative_pct"] for r in rows], height=h, color=GREY, label="Share of negative reviews")
    a1.barh(y - h / 2, [r["share_of_votes_pct"] for r in rows], height=h, color=RED, label="Share of helpful votes")
    for yi, r in zip(y, rows):
        a1.text(r["share_of_negative_pct"] + 0.4, yi + h / 2, f"{r['share_of_negative_pct']:.1f}", va="center", fontsize=9.5)
        a1.text(r["share_of_votes_pct"] + 0.4, yi - h / 2, f"{r['share_of_votes_pct']:.1f}", va="center", fontsize=9.5)
    a1.set_yticks(y)
    a1.set_yticklabels([r["theme"] for r in rows], fontsize=10.5)
    a1.set_xlabel("Per cent")
    a1.set_xlim(0, 34)
    a1.set_title(f"DNSE, {n} negative reviews, all years", fontsize=11, loc="left", fontweight="bold")
    a1.legend(loc="upper center", bbox_to_anchor=(0.5, -0.16), ncol=2, fontsize=10)
    xgrid(a1)
    apps = list(rt)
    x = np.arange(len(apps))
    w = 0.36
    rel = [rt[a]["reliability_pct"] for a in apps]
    tru = [rt[a]["trust_pct"] for a in apps]
    a2.bar(x - w / 2, rel, width=w, color=GREY, label="Reliability")
    a2.bar(x + w / 2, tru, width=w, color=PEACH, label="Trust")
    for xi, a, b in zip(x, rel, tru):
        a2.text(xi - w / 2, a + 1, f"{a:.0f}", ha="center", fontsize=10)
        a2.text(xi + w / 2, b + 1, f"{b:.0f}", ha="center", fontsize=10)
    a2.set_xticks(x)
    a2.set_xticklabels([f"{a}\n(n={rt[a]['negative_n']})" for a in apps], fontsize=10)
    a2.set_ylabel("% of negative reviews")
    a2.set_ylim(0, 55)
    a2.set_title("Three apps, 2025 and 2026", fontsize=11, loc="left", fontweight="bold")
    a2.legend(loc="upper right", fontsize=9.5, bbox_to_anchor=(1.05, 1.05), handlelength=1.4)
    ygrid(a2)
    fig.tight_layout()
    return save(fig, "fig08_complaint_themes.png")


# ------------------------------------------------------------------ Figure 9
def fig09_findex_segments():
    rows = AN.segment_rows()
    top = set(AN.top_four_all())
    fig, ax = plt.subplots(figsize=(7.1, 4.05))
    for seg, r in rows.items():
        if seg == "All adults":
            continue
        col = RED if seg in top else (PEACH if seg == "Young (15-24)" else GREY)
        size = r["unactivated_adults_m"] * 36
        ax.scatter(r["index_b_digital"], r["index_a_investable"], s=size, color=col, alpha=0.85, edgecolor="white", lw=1.5,
                   zorder=3 if seg in top else 4)
        dx, dy, ha = {"Richest 60%": (2.2, 0, "left"), "In labour force": (1.9, 0, "left"),
                      "Secondary educ or more": (2.2, -1.9, "left"), "Urban": (0, 2.3, "center"),
                      "Women": (-0.3, 2.1, "right"), "Older (25+)": (-2.6, 0.6, "right"), "Rural": (-2.4, 0, "right"),
                      "Men": (1.9, -0.9, "left"), "Young (15-24)": (1.9, 0, "left"), "Poorest 40%": (1.9, 0, "left"),
                      "Out of labour force": (1.5, 0, "left"), "Primary educ or less": (1.3, 0, "left")}[seg]
        ax.text(r["index_b_digital"] + dx, r["index_a_investable"] + dy, AN.SEGMENT_LABEL[seg], ha=ha, va="center", fontsize=10.5)
    ax.set_xlim(20, 82)
    ax.set_ylim(10, 51)
    ax.set_xlabel("Index B, digital habit (mean of six Findex indicators, %)")
    ax.set_ylabel("Index A, formally held surplus (%)")
    ax.text(21, 49.5, "Bubble area = adults with an account but no formal saving (millions)", fontsize=10.5, va="center")
    ygrid(ax)
    xgrid(ax)
    ax.legend(handles=[Patch(color=RED, label="In the top four under all four weightings"),
                       Patch(color=PEACH, label="Aged 15 to 24"), Patch(color=GREY, label="Other segments")],
              loc="lower left", bbox_to_anchor=(0.49, 0.0), fontsize=10.5)
    return save(fig, "fig09_findex_segments.png")


# ------------------------------------------------------------------ Figure 11
def fig11_growth_index():
    yrs = ["2021", "2022", "2023", "2024", "2025"]
    acc = AN.account_metric("accounts_year_end")
    accounts = [acc[f"{y}-12-31"] for y in yrs]
    pp = AN.platform_proxy()
    plat = [pp[y]["total"] for y in yrs]
    rev = [AN.income_row(f"FY{y}")["operating_revenue"] for y in yrs]
    core = [AN.income_row(f"FY{y}")["core_pretax_profit"] for y in yrs]
    series = [("Accounts at year end", accounts, CHARCOAL, "-"), ("Platform and overhead cost proxy", plat, PEACH, "-"),
              ("Operating revenue", rev, RED, "-"), ("Core pre-tax profit", core, GREY, "--")]
    x = [int(y) for y in yrs]
    fig, ax = plt.subplots(figsize=(10, 4.4), dpi=160)
    for name, s, col, ls in series:
        idx = [val / s[0] for val in s]
        ax.plot(x, idx, color=col, lw=2.6, ls=ls, marker="o", ms=4.5)
        ax.text(2025.08, idx[-1], f"{name}, {idx[-1]:.1f} times", va="center", ha="left", fontsize=11.5)
    ax.set_yscale("log")
    ticks = [1, 2, 5, 10, 20, 40]
    ax.set_yticks(ticks)
    ax.set_yticklabels([str(t) for t in ticks])
    ax.minorticks_off()
    ax.set_ylim(0.8, 45)
    ax.set_xlim(2020.8, 2027.6)
    ax.set_xticks(x)
    ax.set_ylabel("Index, 2021 = 1 (log scale)", fontsize=12)
    ygrid(ax)
    fig.tight_layout()
    return save(fig, "fig11_growth_index.png", tight=False, dpi=160)


# ------------------------------------------------------------------ Figure 13
def fig13_contribution_threshold():
    m = np.arange(0, 19)
    fig, ax = plt.subplots(figsize=(10, 4.3), dpi=160)
    for c, col, ls in [(1.0, GREY, "-"), (1.5, RED, "-"), (2.0, CHARCOAL, "--")]:
        ax.plot(m, c * m, color=col, lw=2.4, ls=ls, label=f"VND {c:.1f} million a month")
        month = int(np.ceil(10 / c))
        ax.plot([month], [c * month], "o", color=CHARCOAL, ms=5)
        ax.text(month + 0.3, c * month - 2.3, f"month {month}", fontsize=10.5)
    ax.axhline(10, color=PEACH, lw=1.6)
    ax.text(0.3, 10.4, "VND 10 million (headline KPI)", fontsize=11)
    for t, name in [(3, "Starter"), (6, "Disciplined"), (12, "Committed")]:
        ax.axvline(t, color="#BDBDBD", lw=1.2, ls=":")
        ax.text(t + 0.15, 35.2, name, fontsize=11, va="top")
    ax.set_xlim(0, 18)
    ax.set_ylim(0, 36)
    ax.set_xticks(range(0, 19, 3))
    ax.set_xlabel("Consecutive monthly contributions", fontsize=12)
    ax.set_ylabel("Cumulative contributions, VND million", fontsize=12)
    ax.tick_params(labelsize=11)
    ygrid(ax)
    ax.legend(loc="lower right", fontsize=11)
    fig.tight_layout()
    return save(fig, "fig13_contribution_threshold.png", tight=False, dpi=160)


# ------------------------------------------------------------------ Figure B1
def figB1_revenue_profit():
    rows = [AN.income_row(p) for p in AN.PERIODS]
    labels = ["2021", "2022", "2023", "2024", "2025", "H1\n2026"]
    x = np.arange(len(rows))
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(6.4, 3.1))
    rev = [r["operating_revenue"] for r in rows]
    a1.bar(x, rev, color=RED, width=0.6)
    for xi, val in zip(x, rev):
        a1.text(xi, val + 20, f"{val:,.0f}", ha="center", fontsize=10.5)
    a1.set_xticks(x)
    a1.set_xticklabels(labels)
    a1.yaxis.set_major_formatter(plt.FuncFormatter(lambda val, _: f"{val:,.0f}"))
    a1.set_ylabel("Operating revenue, VND billion")
    ygrid(a1)
    core = np.array([r["core_pretax_profit"] for r in rows])
    prop = np.array([r["net_proprietary_result"] for r in rows])
    a2.bar(x, core, color=RED, width=0.6)
    a2.bar(x, prop, bottom=np.where(prop >= 0, core, 0), color=GREY, width=0.6)
    a2.plot(x, [r["pretax_profit"] for r in rows], "D", color=CHARCOAL, ms=7, zorder=4)
    a2.axhline(0, color="#8C8C8C", lw=1)
    a2.set_xticks(x)
    a2.set_xticklabels(labels)
    a2.set_ylabel("Pre-tax profit, VND billion")
    ygrid(a2)
    fig.legend(handles=[Line2D([], [], marker="D", color=CHARCOAL, lw=0, label="Reported pre-tax profit"),
                        Patch(color=RED, label="Pre-tax profit excluding proprietary trading"),
                        Patch(color=GREY, label="Net proprietary trading result")],
               loc="lower center", ncol=3, fontsize=9.5, bbox_to_anchor=(0.5, -0.07), columnspacing=1.0, handlelength=1.4)
    fig.tight_layout()
    return save(fig, "figB1_revenue_profit.png")


# ------------------------------------------------------------------ Figure B2
def figB2_revenue_allocation():
    periods = ["FY2021", "FY2023", "FY2025", "2026H1"]
    parts = [("pretax_profit", "Pre-tax profit", RED), ("direct_brokerage_cost", "Direct brokerage cost", PEACH),
             ("interest_expense_plus_line24", "Funding cost and provisions", MID_GREY),
             ("administrative_expenses", "Administration", DARK_RED),
             ("proprietary_trading_losses", "Proprietary trading losses", LIGHT_GREY)]
    fig, ax = plt.subplots(figsize=(6.1, 3.05))
    y = np.arange(len(periods))[::-1]
    for yi, p in zip(y, periods):
        r = AN.income_row(p)
        left = 0
        for key, lab, col in parts:
            val = max(r[key], 0) / r["operating_revenue"] * 100
            ax.barh(yi, val, left=left, color=col, height=0.55, edgecolor="white", lw=1)
            if val >= 6:
                ax.text(left + val / 2, yi, f"{val:.0f}", ha="center", va="center", fontsize=10.5,
                        color="white" if col in (RED, DARK_RED, MID_GREY) else CHARCOAL)
            left += val
    ax.set_yticks(y)
    ax.set_yticklabels([AN.period_label(p) for p in periods])
    ax.set_xlim(0, 100)
    ax.set_xlabel("VND per VND 100 of operating revenue")
    ax.legend(handles=[Patch(color=c, label=l) for _, l, c in parts], loc="upper center", ncol=3, fontsize=10,
              bbox_to_anchor=(0.5, 1.24), columnspacing=1.2, handlelength=1.5)
    return save(fig, "figB2_revenue_allocation.png")


# ------------------------------------------------------------------ Figure B3
def figB3_yields_funding():
    qs = AN.quarters("2022Q2", "2026Q2")
    lend = [AN.yield_pct(AN.Q, q, "rev_lending", ["loans"]) for q in qs]
    htm = [AN.yield_pct(AN.Q, q, "rev_htm", ["htm_assets", "htm_assets_long"]) for q in qs]
    cof = [AN.cost_of_funds_pct(AN.Q, q) for q in qs]
    x = np.arange(len(qs))
    fig, ax = plt.subplots(figsize=(6.6, 2.85))
    series = [(lend, "Yield on margin loans and advances", RED),
              (htm, "Yield on deposits and held-to-maturity bonds", MID_GREY),
              (cof, "Estimated funding cost", PEACH)]
    ends = sorted((s[-1], i) for i, (s, _, _) in enumerate(series))
    label_y = {i: val for val, i in ends}
    for (lo, i_lo), (hi, i_hi) in zip(ends, ends[1:]):      # keep end labels at least 0.9 points apart
        if label_y[i_hi] - label_y[i_lo] < 0.9:
            mid = (label_y[i_hi] + label_y[i_lo]) / 2
            label_y[i_lo], label_y[i_hi] = mid - 0.45, mid + 0.45
    for i, (s, lab, col) in enumerate(series):
        ax.plot(x, s, color=col, lw=2.4, label=lab)
        ax.text(x[-1] + 0.25, label_y[i], f"{s[-1]:.1f}", va="center", fontsize=10.5)
    ax.set_xticks(x)
    ax.set_xticklabels([f"Q{q[-1]}\n{q[:4]}" if q[-1] in "12" and (q[-1] == "1" or q == qs[0]) else f"Q{q[-1]}" for q in qs], fontsize=9.5)
    ax.set_ylim(0, 15)
    ax.set_yticks(range(0, 15, 2))
    ax.set_ylabel("Per cent a year")
    ax.legend(loc="upper center", ncol=3, fontsize=9.5, bbox_to_anchor=(0.5, 1.15), columnspacing=1.2, handlelength=1.8)
    ygrid(ax)
    return save(fig, "figB3_yields_funding.png")


# ------------------------------------------------------------------ Figure B4
def figB4_asset_composition():
    points = [("2021", "2021Q4"), ("2022", "2022Q4"), ("2023", "2023Q4"), ("2024", "2024Q4"), ("2025", "2025Q4"),
              ("30 Jun\n2026", "2026Q2")]
    parts = [("Margin loans and advances", lambda d: AN.v(d, "loans") + AN.v(d, "loan_allowance"), RED),  # net of allowance
             ("Term deposits and held-to-maturity bonds", lambda d: AN.v(d, "htm_assets") + AN.v(d, "htm_assets_long"), MID_GREY),
             ("Proprietary portfolio (FVTPL)", lambda d: AN.v(d, "fvtpl_assets"), DARK_RED),
             ("Cash", lambda d: AN.v(d, "cash"), CORAL)]
    fig, ax = plt.subplots(figsize=(5.8, 3.2))
    x = np.arange(len(points))
    bottom = np.zeros(len(points))
    for lab, fn, col in parts:
        vals = np.array([fn(AN.Q[q]) / AN.v(AN.Q[q], "total_assets") * 100 for _, q in points])
        ax.bar(x, vals, bottom=bottom, color=col, width=0.55, label=lab, edgecolor="white", lw=1)
        for xi, b, val in zip(x, bottom, vals):
            if val >= 8:
                ax.text(xi, b + val / 2, f"{val:.0f}", ha="center", va="center", fontsize=10.5,
                        color="white" if col in (RED, DARK_RED, MID_GREY) else CHARCOAL)
        bottom += vals
    ax.bar(x, 100 - bottom, bottom=bottom, color=LIGHT_GREY, width=0.55, label="Other", edgecolor="white", lw=1)
    ax.set_xticks(x)
    ax.set_xticklabels([p[0] for p in points])
    ax.set_ylim(0, 100)
    ax.set_ylabel("Share of total assets, per cent")
    ax.legend(loc="upper center", ncol=3, fontsize=10, bbox_to_anchor=(0.5, 1.2), columnspacing=1.0, handlelength=1.5)
    ygrid(ax)
    return save(fig, "figB4_asset_composition.png")


# ------------------------------------------------------------------ Figure C1
def figC1_peer_per_account():
    pm = AN.peer_metrics("2026Q2")
    names = ["DNSE", "VPS", "VPBankS", "TCBS"]
    fig, axs = plt.subplots(1, 2, figsize=(6.15, 2.7))
    for ax, key, xl, d in [(axs[0], "loans_per_account_m", "Margin loans per customer account,\nVND million, 30 Jun 2026", 1),
                           (axs[1], "pbt_per_account_k", "Q2 2026 pre-tax profit per customer\naccount, VND thousand", 0)]:
        vals = [pm[n][key] for n in names]
        y = np.arange(len(names))[::-1]
        ax.barh(y, vals, color=[RED if n == "DNSE" else LIGHT_GREY for n in names], height=0.55)
        for yi, val in zip(y, vals):
            ax.text(val + max(vals) * 0.02, yi, half_up(val, d), va="center", fontsize=11)
        ax.set_yticks(y)
        ax.set_yticklabels(names)
        ax.set_xlabel(xl)
        ax.set_xlim(0, max(vals) * 1.2)
        if key == "pbt_per_account_k":
            ax.set_xticks(range(0, int(max(vals) * 1.2) + 1, 500))
        ax.xaxis.set_major_formatter(plt.FuncFormatter(lambda val, _: f"{val:,.0f}"))
        xgrid(ax)
    fig.tight_layout()
    return save(fig, "figC1_peer_per_account.png")


# ------------------------------------------------------------------ Figure D1
def figD1_rating_by_year():
    R = AN.load_json("reviews_tables.json")
    hdr = R["YEAR_HEADER"]
    rows = [dict(zip(hdr, r)) for r in R["YEAR_TAB"] if r[0] >= "2021"]
    yrs = [r["year"] for r in rows]
    x = np.arange(len(yrs))
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(7.5, 3.45), gridspec_kw={"width_ratios": [1.5, 1]})
    a1.plot(x, [r["clean_mean"] for r in rows], color=LIGHT_GREY, lw=2.6, marker="o", label="All retained reviews")
    a1.plot(x, [r["substantive_mean"] for r in rows], color=RED, lw=2.6, marker="o",
            label="Substantive reviews (one-word reviews removed)")
    for i, r in enumerate(rows):
        if r["year"] in ("2024", "2025"):
            a1.text(i + 0.1, r["substantive_mean"] - (0.0 if r["year"] == "2024" else 0.15), f"{r['substantive_mean']:.2f}", fontsize=10.5)
    a1.set_xticks(x)
    a1.set_xticklabels([f"{r['year']}\nn={r['clean_n']}" for r in rows], fontsize=10)
    a1.set_ylim(1, 5)
    a1.set_yticks(np.arange(1, 5.01, 0.5))
    a1.set_ylabel("Mean star rating")
    a1.legend(loc="upper left", fontsize=10)
    ygrid(a1)
    g = [r["generic_pct"] for r in rows]
    a2.bar(x, g, color=[RED if r["year"] == "2024" else LIGHT_GREY for r in rows], width=0.62)
    for xi, val in zip(x, g):
        a2.text(xi, val + 0.8, f"{val:.0f}", ha="center", fontsize=10.5)
    a2.set_xticks(x)
    a2.set_xticklabels(yrs, fontsize=10)
    a2.set_ylim(0, 40)
    a2.set_yticks(range(0, 41, 5))
    a2.set_ylabel("One-word reviews, per cent of retained")
    ygrid(a2)
    fig.tight_layout()
    return save(fig, "figD1_rating_by_year.png")


# ------------------------------------------------------------------ Figure D2
def figD2_store_ratings():
    R = AN.load_json("reviews_tables.json")
    rows = [dict(zip(R["STORE_COMPARE_HEADER"], r)) for r in R["STORE_COMPARE"]]
    short = {"DNSE Entrade X": "DNSE", "VPS SmartOne": "VPS", "FPTS EzTrade": "FPTS"}
    x = np.arange(len(rows))
    w = 0.34
    fig, ax = plt.subplots(figsize=(7.3, 3.05))
    ax.bar(x - w / 2, [r["play_mean"] for r in rows], width=w, color=RED, label="Google Play")
    ax.bar(x + w / 2, [r["ios_mean"] for r in rows], width=w, color=LIGHT_GREY, label="App Store")
    for xi, r in zip(x, rows):
        ax.text(xi - w / 2, r["play_mean"] + 0.05, f"{r['play_mean']:.2f}", ha="center", fontsize=11)
        ax.text(xi + w / 2, r["ios_mean"] + 0.05, f"{r['ios_mean']:.2f}", ha="center", fontsize=11)
    ax.set_xticks(x)
    ax.set_xticklabels([f"{short[r['app']]}\nn={r['play_n']} and {r['ios_n']}" for r in rows], fontsize=11)
    ax.set_ylim(0, 3.5)
    ax.set_yticks(np.arange(0, 3.51, 0.5))
    ax.set_ylabel("Mean rating, cleaned reviews")
    ax.legend(loc="upper right", fontsize=11)
    ygrid(ax)
    return save(fig, "figD2_store_ratings.png")


# ------------------------------------------------------------------ Figure E1
def figE1_findex_behaviour():
    pairs = [("Young (15-24)", "Older (25+)"), ("Poorest 40%", "Richest 60%"),
             ("Out of labour force", "In labour force"), ("Primary educ or less", "Secondary educ or more")]
    inds = [("fin32.acc", "Receives wages\ninto an account"), ("fin17dm", "Saves into an\naccount every month"),
            ("fin17f", "Saved for\nold age"), ("fin17e", "Received interest\non savings")]
    fig, axs = plt.subplots(1, 4, figsize=(7.1, 3.25), sharey=True)
    ypos, labels = [], []
    y = 0
    for a, b in pairs:
        ypos += [y, y - 1]
        labels += [AN.SEGMENT_LABEL[a], AN.SEGMENT_LABEL[b]]
        y -= 2.7
    for ax, (code, title) in zip(axs, inds):
        for (a, b), yy in zip(pairs, ypos[::2]):
            va, vb = AN.IND[code][AN.SEG_INDEX[a]], AN.IND[code][AN.SEG_INDEX[b]]
            ax.barh(yy, va, color=LIGHT_GREY, height=0.8)
            ax.barh(yy - 1, vb, color=RED, height=0.8)
            ax.text(va + 1, yy, f"{va:.0f}", va="center", fontsize=9)
            ax.text(vb + 1, yy - 1, f"{vb:.0f}", va="center", fontsize=9)
        ax.set_title(title, fontsize=10.5)
        ax.set_xlim(0, 70)
        ax.set_xticks([0, 25, 50])
        xgrid(ax)
    axs[0].set_yticks(ypos)
    axs[0].set_yticklabels(labels, fontsize=10)
    fig.text(0.62, -0.01, "Per cent of adults in each segment, Global Findex 2024 fieldwork", ha="center", fontsize=10.5)
    fig.tight_layout()
    return save(fig, "figE1_findex_behaviour.png")


# ------------------------------------------------------------------ Figure F1
def figF1_scenarios():
    sc = AN.scenarios()
    cash = {r["item"]: float(r["value"]) for r in AN.manual("scenario_baseline.csv")}["investor_cash_30_june_2026_vnd_tn"]
    fig, ax = plt.subplots(figsize=(7.4, 3.55))
    x = np.arange(len(sc))
    cols = [LIGHT_RED, RED, DARK_RED]
    ax.bar(x, [s["assets_vnd_tn"] for s in sc], color=cols, width=0.55)
    for xi, s in zip(x, sc):
        a = s["assets_vnd_tn"]
        ax.text(xi, max(a, cash) + 0.25, f"VND {a + 1e-9:.2f} trillion\nfees VND {s['annual_fees_vnd_bn']:.0f} billion a year",
                ha="center", fontsize=11)
    ax.axhline(cash, color=PEACH, lw=2, ls="--", label=f"DNSE investor cash, 30 June 2026 (VND {cash:.2f} trillion)")
    ax.set_xticks(x)
    ax.set_xticklabels([s["scenario"] for s in sc], fontsize=12)
    ax.set_ylim(0, 14.5)
    ax.set_yticks(np.arange(0, 12.6, 2.5))
    ax.set_ylabel("VND trillion after 18 months")
    ax.legend(loc="upper left", fontsize=11)
    ygrid(ax)
    return save(fig, "figF1_scenarios.png")


# ------------------------------------------------------------------ Figure F2
def figF2_roadmap():
    rows = AN.manual("validation_roadmap.csv")
    cmap = {"Test": RED, "Gate": LIGHT_GREY, "Pilot": CORAL, "Decide": PEACH, "Scale": DARK_RED}
    fig, ax = plt.subplots(figsize=(7.7, 3.15))
    for i, r in enumerate(rows):
        a, b = float(r["start_month"]), float(r["end_month"])
        ax.barh(len(rows) - 1 - i, b - a, left=a, color=cmap[r["kind"]], height=0.55)
    ax.set_yticks(range(len(rows)))
    ax.set_yticklabels([r["task"] for r in rows][::-1], fontsize=10.5)
    ax.set_xlim(0, 9)
    ax.set_xticks(range(10))
    ax.set_xticklabels([f"M{i}" for i in range(10)])
    ax.set_xlabel("Months from the start of Round 3 development")
    xgrid(ax)
    ax.legend(handles=[Patch(color=c, label=k) for k, c in cmap.items()], loc="upper center", ncol=5,
              bbox_to_anchor=(0.5, 1.15), fontsize=10.5)
    return save(fig, "figF2_roadmap.png")


ALL = [fig01_idle_cash_returns, fig02_investor_cash_index, fig03_funding_funnel, fig04_market_position,
       fig05_brokerage_vs_cost, fig06_funding_structure, fig07_platform_cost, fig08_complaint_themes,
       fig09_findex_segments, fig11_growth_index, fig13_contribution_threshold, figB1_revenue_profit,
       figB2_revenue_allocation, figB3_yields_funding, figB4_asset_composition, figC1_peer_per_account,
       figD1_rating_by_year, figD2_store_ratings, figE1_findex_behaviour, figF1_scenarios, figF2_roadmap]

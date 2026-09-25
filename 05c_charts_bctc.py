"""05c -- Long-run charts of DNSE's filed statements (2018 to Q2 2026) and a check of press figures against them."""
import json
import os

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "fig", "bctc")
os.makedirs(OUT, exist_ok=True)
with open(os.path.join(HERE, "dnse_financials.json"), encoding="utf-8") as f:
    FS = json.load(f)
Q, H, Y, DV = FS["quarterly"], FS["half_year"], FS["annual"], FS["derived"]
QS = list(Q)

BLUE, ORANGE, AQUA, YELLOW, GREY = "#2a78d6", "#eb6834", "#1baf7a", "#eda100", "#b9c0c7"
INK, MUTED, GRIDC, SURF = "#1a1a1a", "#6b6b6b", "#d9d9d9", "#ffffff"
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 9, "axes.edgecolor": GRIDC,
                     "axes.labelcolor": INK, "text.color": INK, "xtick.color": MUTED, "ytick.color": MUTED,
                     "figure.facecolor": SURF, "axes.facecolor": SURF, "savefig.facecolor": SURF})
PCT = FuncFormatter(lambda v, p: f"{v:.0f}%")


def style(ax, grid="y"):
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    for s in ("left", "bottom"):
        ax.spines[s].set_color(GRIDC)
    getattr(ax, f"{grid}axis").grid(True, color=GRIDC, linewidth=0.6)
    ax.set_axisbelow(True)
    ax.tick_params(length=0)


def save(fig, name):
    fig.savefig(os.path.join(OUT, f"{name}.png"), dpi=200, bbox_inches="tight", pad_inches=0.12)
    plt.close(fig)
    print("wrote fig/bctc/" + name + ".png")


def qlabel(p):
    return f"Q{p[-1]}\n{p[:4]}" if p.endswith("Q1") else f"Q{p[-1]}"


def funding(d):
    return -(d["cost_provision_and_loan_funding"] + d["interest_expense"])


def htm(d):
    return d["htm_assets"] + (d["htm_assets_long"] or 0)


# Periods for annual charts: every filed year plus the first half of 2026.
PER = [(p[2:], Y[p]) for p in Y] + [("H1 2026", H["2026H1"])]
LAB = [p for p, _ in PER]
SINCE_2021 = [(p, d) for p, d in PER if p >= "2021"]

# ---------------------------------------------------------------- 1. revenue and pre-tax profit
fig, ax = plt.subplots(figsize=(7.2, 3.2))
x = range(len(PER))
w = 0.38
ax.bar([i - w / 2 for i in x], [d["revenue"] for _, d in PER], w, color=BLUE, label="Operating revenue", zorder=3)
ax.bar([i + w / 2 for i in x], [d["pbt"] for _, d in PER], w, color=ORANGE, label="Pre-tax profit", zorder=3)
for i, (p, d) in enumerate(PER):
    if p >= "2021":
        ax.text(i - w / 2, d["revenue"] + 22, f"{d['revenue']:,.0f}", ha="center", fontsize=7.4, color=INK)
        ax.text(i + w / 2, max(d["pbt"], 0) + 22, f"{d['pbt']:,.0f}", ha="center", fontsize=7.4, color=MUTED)
ax.text(1, 180, "2018-2020: revenue\n18-28bn a year", ha="center", fontsize=7.6, color=MUTED)
ax.set_xticks(list(x)); ax.set_xticklabels(LAB)
ax.set_ylabel("VND billion")
ax.legend(frameon=False, fontsize=8, loc="upper left")
style(ax)
save(fig, "bctc_1_revenue_profit")

# ---------------------------------------------------------------- 2. revenue mix
MIX = [("Interest on lending", "rev_lending", BLUE, "white"), ("Brokerage commissions", "rev_brokerage", ORANGE, "white"),
       ("Interest on bank deposits and bonds (HTM)", "rev_htm", AQUA, INK), ("Trading gains (FVTPL)", "rev_fvtpl", YELLOW, INK)]
fig, ax = plt.subplots(figsize=(7.2, 3.4))
bottom = [0.0] * len(PER)
for name, key, col, txt in MIX + [("Other", None, GREY, INK)]:
    vals = []
    for _, d in PER:
        v = d[key] if key else d["revenue"] - sum(d[k] for _, k, _, _ in MIX)
        vals.append(v / d["revenue"] * 100)
    ax.bar(x, vals, 0.62, bottom=bottom, color=col, label=name, edgecolor=SURF, linewidth=1.5, zorder=3)
    for i, v in enumerate(vals):
        if v >= 9:
            ax.text(i, bottom[i] + v / 2, f"{v:.0f}", ha="center", va="center", fontsize=7.4, color=txt)
    bottom = [b + v for b, v in zip(bottom, vals)]
ax.set_xticks(list(x)); ax.set_xticklabels(LAB)
ax.set_ylim(0, 100); ax.yaxis.set_major_formatter(PCT)
ax.set_ylabel("Share of operating revenue")
ax.legend(frameon=False, fontsize=7.6, ncol=3, loc="upper center", bbox_to_anchor=(0.5, 1.2))
style(ax)
save(fig, "bctc_2_revenue_mix")

# ---------------------------------------------------------------- 3. quarterly pre-tax margin
Q21 = [p for p in QS if p >= "2021Q1"]
fig, ax = plt.subplots(figsize=(7.2, 3.0))
m = [DV[p]["pbt_margin_pct"] for p in Q21]
ax.bar(range(len(Q21)), m, 0.62, color=[ORANGE if v < 5 else BLUE for v in m], zorder=3)
for i, v in enumerate(m):
    if v < 5:
        ax.text(i, v + 1.2 if v >= 0 else v - 1.2, f"{v:.1f}", ha="center", va="bottom" if v >= 0 else "top",
                fontsize=6.8, color=INK)
ax.axhline(0, color=MUTED, linewidth=0.8)
ax.set_ylim(min(m) - 7, 62)
ax.set_xticks(range(len(Q21))); ax.set_xticklabels([qlabel(p) for p in Q21], fontsize=7.4)
ax.yaxis.set_major_formatter(PCT); ax.set_ylabel("Pre-tax profit / revenue")
ax.text(len(Q21) - 0.5, 57, "Orange: quarters below 5%", ha="right", fontsize=7.6, color=MUTED)
style(ax)
save(fig, "bctc_3_margin_quarterly")

# ---------------------------------------------------------------- 4. brokerage: revenue against direct cost
fig, (a1, a2) = plt.subplots(2, 1, figsize=(7.2, 4.4), sharex=True, gridspec_kw={"height_ratios": [1.6, 1]})
xs = range(len(Q21))
a1.plot(xs, [Q[p]["rev_brokerage"] for p in Q21], color=BLUE, linewidth=2, label="Brokerage commissions")
a1.plot(xs, [-Q[p]["cost_brokerage"] for p in Q21], color=ORANGE, linewidth=2, label="Direct brokerage costs")
a1.set_ylabel("VND billion"); a1.legend(frameon=False, fontsize=8, loc="upper left")
style(a1)
net = [DV[p]["brokerage_net"] for p in Q21]
a2.bar(xs, net, 0.62, color=[BLUE if v >= 0 else ORANGE for v in net], zorder=3)
a2.axhline(0, color=MUTED, linewidth=0.8)
a2.set_ylabel("Result, VND bn")
a2.set_xticks(list(xs)); a2.set_xticklabels([qlabel(p) for p in Q21], fontsize=7.4)
first_loss = next(i for i in range(len(Q21)) if all(v < 0 for v in net[i:]))
a2.annotate(f"negative every quarter since Q{Q21[first_loss][-1]} {Q21[first_loss][:4]}", (first_loss, net[first_loss]),
            xytext=(first_loss + 1, min(net) * 0.85), fontsize=7.6, color=INK,
            arrowprops={"arrowstyle": "-", "color": MUTED, "linewidth": 0.8})
style(a2)
save(fig, "bctc_4_brokerage")

# ---------------------------------------------------------------- 5. lending yield, deposit yield and funding cost
Q22 = [p for p in QS if p >= "2022Q1"]


def htm_yield(p):
    prev = Q[QS[QS.index(p) - 1]]
    return Q[p]["rev_htm"] * 4 / ((htm(prev) + htm(Q[p])) / 2) * 100


series5 = [("Yield on margin lending", [DV[p]["lending_yield_pct"] for p in Q22], BLUE),
           ("Yield on bank deposits and bonds (HTM)", [htm_yield(p) for p in Q22], AQUA),
           ("Estimated funding cost", [DV[p]["funding_cost_pct"] for p in Q22], ORANGE)]
fig, ax = plt.subplots(figsize=(7.2, 3.1))
label_y = {}
for name, vals, col in sorted(series5, key=lambda s: s[1][-1]):    # nudge end labels at least 0.8 points apart
    label_y[name] = max(vals[-1], max(label_y.values(), default=-9) + 0.8)
for name, vals, col in series5:
    ax.plot(range(len(Q22)), vals, color=col, linewidth=2, label=name, marker="o", markersize=4,
            markeredgecolor=SURF, markeredgewidth=1)
    ax.text(len(Q22) - 0.7, label_y[name], f"{vals[-1]:.1f}%", va="center", fontsize=8, color=INK)
ax.set_xticks(range(len(Q22))); ax.set_xticklabels([qlabel(p) for p in Q22], fontsize=7.4)
ax.set_xlim(-0.5, len(Q22) + 0.3)
ax.set_ylim(0, 16); ax.yaxis.set_major_formatter(PCT); ax.set_ylabel("Per cent a year")
ax.legend(frameon=False, fontsize=7.8, loc="lower left", ncol=3)
style(ax)
save(fig, "bctc_5_yield_funding")

# ---------------------------------------------------------------- 6. what the balance sheet holds
BS = [(p[2:], Y[p]) for p in Y if p >= "FY2021"] + [("Jun 2026", Q["2026Q2"])]
ASSETS = [("Margin loans and advances", lambda d: d["loans"], BLUE),
          ("Bank deposits and bonds held to maturity", htm, AQUA),
          ("Trading assets (FVTPL)", lambda d: d["fvtpl_assets"], YELLOW)]
fig, ax = plt.subplots(figsize=(7.2, 3.2))
bottom = [0.0] * len(BS)
for name, fn, col in ASSETS + [("Cash, receivables and other", None, GREY)]:
    vals = [fn(d) if fn else d["total_assets"] - sum(f(d) for _, f, _ in ASSETS) for _, d in BS]
    ax.bar(range(len(BS)), vals, 0.6, bottom=bottom, color=col, label=name, edgecolor=SURF, linewidth=1.5, zorder=3)
    bottom = [b + v for b, v in zip(bottom, vals)]
for i, (_, d) in enumerate(BS):
    ax.text(i, d["total_assets"] + 250, f"{d['total_assets']:,.0f}", ha="center", fontsize=7.6, color=INK)
ax.set_xticks(range(len(BS))); ax.set_xticklabels([p for p, _ in BS])
ax.set_ylabel("Total assets, VND billion")
ax.legend(frameon=False, fontsize=7.6, loc="upper left")
style(ax)
save(fig, "bctc_6_assets")

# ---------------------------------------------------------------- 7. where each 100 dong of revenue goes
COSTS = [("Pre-tax profit", lambda d: d["pbt"], BLUE), ("Brokerage direct costs", lambda d: -d["cost_brokerage"], ORANGE),
         ("Funding cost and loan provisions", funding, AQUA), ("Administration", lambda d: -d["admin_cost"], YELLOW)]
fig, ax = plt.subplots(figsize=(7.2, 3.4))
bottom = [0.0] * len(SINCE_2021)
for name, fn, col in COSTS + [("Trading losses and other costs", None, GREY)]:
    vals = [(fn(d) if fn else d["revenue"] - sum(f(d) for _, f, _ in COSTS)) / d["revenue"] * 100 for _, d in SINCE_2021]
    ax.bar(range(len(SINCE_2021)), vals, 0.6, bottom=bottom, color=col, label=name, edgecolor=SURF, linewidth=1.5, zorder=3)
    for i, v in enumerate(vals):
        if v >= 7:
            ax.text(i, bottom[i] + v / 2, f"{v:.0f}", ha="center", va="center", fontsize=7.6,
                    color="white" if col in (BLUE, ORANGE) else INK)
    bottom = [b + v for b, v in zip(bottom, vals)]
ax.set_xticks(range(len(SINCE_2021))); ax.set_xticklabels([p for p, _ in SINCE_2021])
ax.set_ylim(0, 100); ax.yaxis.set_major_formatter(PCT)
ax.set_ylabel("Share of operating revenue")
ax.legend(frameon=False, fontsize=7.6, ncol=3, loc="upper center", bbox_to_anchor=(0.5, 1.2))
style(ax)
save(fig, "bctc_7_cost_per_100")

# ---------------------------------------------------------------- 8. H1 2026 profit waterfall
h = H["2026H1"]
steps = [("Lending\ninterest", h["rev_lending"]), ("Deposit\nand bond\ninterest", h["rev_htm"]),
         ("Brokerage\nfees", h["rev_brokerage"]), ("Trading\ngains", h["rev_fvtpl"])]
steps.append(("Other", h["revenue"] - sum(v for _, v in steps)))
costs = [("Brokerage\ncosts", h["cost_brokerage"]), ("Funding\nand loan\nprovisions", -funding(h)),
         ("Trading\nlosses", h["cost_fvtpl"]), ("Admin", h["admin_cost"])]
costs.append(("Other", h["pbt"] - h["revenue"] - sum(v for _, v in costs)))
fig, ax = plt.subplots(figsize=(8.2, 3.4))
level, i = 0.0, 0
for lab, v in steps + [("Revenue", None)] + costs + [("Pre-tax\nprofit", None)]:
    if v is None:
        ax.bar(i, level, 0.62, color=GREY, zorder=3)
        ax.text(i, level + 12, f"{level:,.1f}", ha="center", fontsize=7.6, color=INK, fontweight="bold")
    else:
        lo = min(level, level + v)
        ax.bar(i, abs(v), 0.62, bottom=lo, color=BLUE if v >= 0 else ORANGE, zorder=3)
        ax.text(i, max(level, level + v) + 12, f"{v:+,.1f}", ha="center", fontsize=7.2, color=INK)
        level += v
    ax.text(i, -22, lab, ha="center", va="top", fontsize=7, color=INK)
    i += 1
ax.set_xticks([]); ax.set_xlim(-0.6, i - 0.4); ax.set_ylim(-110, 960)
ax.set_ylabel("VND billion, first half of 2026")
style(ax)
save(fig, "bctc_8_waterfall_h1")

# ---------------------------------------------------------------- 9. customer cash on the platform
fig, ax = plt.subplots(figsize=(7.2, 2.9))
cash = [Q[p]["customer_cash_trading"] for p in Q21]
ax.bar(range(len(Q21)), cash, 0.62, color=BLUE, zorder=3)
for i in (len(Q21) - 1, cash.index(max(cash))):
    ax.text(i, cash[i] + 60, f"{cash[i]:,.0f}", ha="center", fontsize=7.6, color=INK)
ax.set_xticks(range(len(Q21))); ax.set_xticklabels([qlabel(p) for p in Q21], fontsize=7.4)
ax.set_ylabel("Investors' cash, VND billion")
style(ax)
save(fig, "bctc_9_customer_cash")

# ---------------------------------------------------------------- 10. profit with and without proprietary trading
fig, ax = plt.subplots(figsize=(7.2, 3.1))
for i, (p, d) in enumerate(SINCE_2021):
    trade = d["rev_fvtpl"] + d["cost_fvtpl"]
    core = d["pbt"] - trade
    ax.bar(i, core, 0.58, color=BLUE, zorder=3, label="Profit before tax excluding trading" if i == 0 else None)
    ax.bar(i, trade, 0.58, bottom=core if trade >= 0 else 0, color=YELLOW, zorder=3,
           label="Net trading gains or losses (FVTPL)" if i == 0 else None)
    ax.plot(i, d["pbt"], marker="D", color=INK, markersize=5, zorder=4, label="Pre-tax profit" if i == 0 else None)
    ax.text(i + 0.33, d["pbt"], f"{d['pbt']:,.0f}", ha="left", va="center", fontsize=7.6, color=INK, fontweight="bold")
    ax.text(i, core * 0.2, f"{core:,.0f}", ha="center", va="center", fontsize=7.6, color="white")
ax.axhline(0, color=MUTED, linewidth=0.8)
ax.set_xticks(range(len(SINCE_2021))); ax.set_xticklabels([p for p, _ in SINCE_2021])
ax.set_ylabel("VND billion")
ax.legend(frameon=False, fontsize=7.8, ncol=3, loc="upper center", bbox_to_anchor=(0.5, 1.14))
style(ax)
save(fig, "bctc_10_core_profit")

# ---------------------------------------------------------------- 11. brokerage result against listed peers
with open(os.path.join(HERE, "peer_financials.json"), encoding="utf-8") as f:
    PANEL = json.load(f)
PEERS = {n: d for n, d in PANEL["firms"].items() if d["focus"]}
brok = {n: d["half_year"]["2026H1"]["rev_brokerage"] + d["half_year"]["2026H1"]["cost_brokerage"] for n, d in PEERS.items()}
brok["DNSE"] = H["2026H1"]["rev_brokerage"] + H["2026H1"]["cost_brokerage"]
order = sorted(brok, key=brok.get)
fig, ax = plt.subplots(figsize=(7.2, 0.3 * len(order) + 0.9))
ax.barh(range(len(order)), [brok[n] for n in order], 0.6, color=[ORANGE if n == "DNSE" else GREY for n in order], zorder=3)
for i, n in enumerate(order):
    v = brok[n]
    ax.text(v + (6 if v >= 0 else -6), i, f"{v:,.1f}", va="center", ha="left" if v >= 0 else "right", fontsize=8, color=INK)
ax.axvline(0, color=MUTED, linewidth=0.8)
ax.set_yticks(range(len(order))); ax.set_yticklabels(order)
ax.set_xlim(min(brok.values()) - 60, max(brok.values()) + 60)
ax.set_xlabel("Brokerage commissions less direct brokerage costs, H1 2026, VND billion")
style(ax, grid="x")
save(fig, "bctc_11_peer_brokerage")

# ---------------------------------------------------------------- 12. DNSE's share of three markets over time
with open(os.path.join(HERE, "market_macro.json"), encoding="utf-8") as f:
    MM = json.load(f)
ACC_AR = {"2020": 5_548, "2021": 44_727, "2022": 189_845, "2023": 561_279, "2024": 994_811, "2025": 1_512_920}
acc_share = {f"{y}Q4": v / MM["vsdc_accounts"][y]["total"] * 100 for y, v in ACC_AR.items()}
lend_share = {p: t["dnse_share_of_loans_pct"] for p, t in PANEL["totals"].items() if p >= "2020Q1"}
der_share = {p: d["share"] for p, d in MM["hnx_market_share"]["dnse"]["derivatives"].items() if d["share"] is not None}
QX = [p for p in lend_share]
fig, ax = plt.subplots(figsize=(7.2, 3.3))
for series, colour, label in [(acc_share, BLUE, "Share of all securities accounts (year end, VSDC)"),
                              (der_share, ORANGE, "Share of derivatives brokerage (HNX)"),
                              (lend_share, AQUA, "Share of lending by filing brokers (filings)")]:
    xs = [QX.index(p) for p in series if p in QX]
    ys = [series[p] for p in series if p in QX]
    ax.plot(xs, ys, color=colour, linewidth=2, marker="o", markersize=3.2, label=label, zorder=3)
    ax.text(xs[-1] + 0.4, ys[-1], f"{ys[-1]:.1f}%", va="center", fontsize=7.8, color=colour, fontweight="bold")
ax.set_xticks([i for i, p in enumerate(QX) if p.endswith("Q1")])
ax.set_xticklabels([p[:4] for p in QX if p.endswith("Q1")])
ax.set_xlim(-0.5, len(QX) + 1.8)
ax.yaxis.set_major_formatter(PCT)
ax.legend(frameon=False, fontsize=7.8, loc="upper left")
style(ax)
save(fig, "bctc_12_dnse_shares")

# ---------------------------------------------------------------- 13. the market DNSE grew in
YRS = [str(y) for y in range(2018, 2027)]
PX = MM["prices"]
fig, (a1, a2) = plt.subplots(1, 2, figsize=(7.4, 3.0))
hose = [PX["VNINDEX"]["annual"][y]["avg_daily_value_bn"] / 1000 for y in YRS]
fut = [PX["VN30F1M"]["annual"][y]["avg_daily_value_bn"] / 1000 for y in YRS]
w = 0.4
a1.bar([i - w / 2 for i in range(len(YRS))], hose, w, color=BLUE, label="HOSE shares", zorder=3)
a1.bar([i + w / 2 for i in range(len(YRS))], fut, w, color=ORANGE, label="VN30 futures, front month", zorder=3)
a1.set_xticks(range(len(YRS))); a1.set_xticklabels([y[2:] if y != "2026" else "26\nYTD" for y in YRS], fontsize=7.6)
a1.set_ylabel("Average daily value, VND trillion")
a1.legend(frameon=False, fontsize=7.4, loc="upper left")
style(a1)
accs = [MM["vsdc_accounts"][y]["total"] / 1e6 for y in YRS[:-1]] + [MM["vsdc_latest"]["investor_trading_accounts"] / 1e6]
dn = [ACC_AR.get(y, 0) / 1e6 for y in YRS[:-1]] + [1.7]
a2.bar(range(len(YRS)), accs, 0.6, color=GREY, label="All accounts (VSDC)", zorder=3)
a2.bar(range(len(YRS)), dn, 0.6, color=ORANGE, label="DNSE accounts", zorder=3)
for i in (0, len(YRS) - 1):
    a2.text(i, accs[i] + 0.25, f"{accs[i]:.1f}", ha="center", fontsize=7.4, color=INK)
a2.set_xticks(range(len(YRS))); a2.set_xticklabels([y[2:] if y != "2026" else "26\nSep" for y in YRS], fontsize=7.6)
a2.set_ylabel("Accounts, million")
a2.legend(frameon=False, fontsize=7.4, loc="upper left")
style(a2)
fig.tight_layout(w_pad=2)
save(fig, "bctc_13_market_context")

# ---------------------------------------------------------------- 14. DSE against the VN-Index since listing
dse = PX["DSE"]["daily"]
vni = {r[0]: r[1] for r in PX["VNINDEX"]["daily"]}
days = [r[0] for r in dse if r[0] in vni]
d0, v0 = dse[0][1], vni[days[0]]
dse_idx = [r[1] / d0 * 100 for r in dse if r[0] in vni]
vni_idx = [vni[d] / v0 * 100 for d in days]
fig, ax = plt.subplots(figsize=(7.2, 2.9))
ax.plot(range(len(days)), vni_idx, color=GREY, linewidth=1.6, label="VN-Index")
ax.plot(range(len(days)), dse_idx, color=ORANGE, linewidth=1.6, label="DSE (adjusted)")
for s, c in ((vni_idx, MUTED), (dse_idx, ORANGE)):
    ax.text(len(days) + 3, s[-1], f"{s[-1]:.0f}", va="center", fontsize=7.8, color=c, fontweight="bold")
ticks = [i for i, d in enumerate(days) if d[5:7] in ("01", "07") and (i == 0 or days[i - 1][5:7] != d[5:7])]
ax.set_xticks(ticks); ax.set_xticklabels([days[i][:7] for i in ticks], fontsize=7.6)
ax.axhline(100, color=MUTED, linewidth=0.6, linestyle=":")
ax.set_ylabel(f"Index, first trading day {days[0]} = 100")
ax.legend(frameon=False, fontsize=7.8, loc="upper left")
style(ax)
save(fig, "bctc_14_dse_vs_vnindex")

# ---------------------------------------------------------------- press figures against the filings
g = lambda a, b: (a / b - 1) * 100
checks = [
    ("Doanh thu hoạt động FY2025 (báo chí ghi 1.467 là tổng doanh thu)", 1467.0, Y["FY2025"]["revenue"]),
    ("Doanh thu hoạt động + tài chính FY2025 (thiếu thu nhập khác)", 1467.0,
     Y["FY2025"]["revenue"] + Y["FY2025"]["financial_income"]),
    ("Tăng trưởng doanh thu hoạt động FY2025, %", 77.0, g(Y["FY2025"]["revenue"], Y["FY2024"]["revenue"])),
    ("Doanh thu Q4/2025", 434.0, Q["2025Q4"]["revenue"]),
    ("Doanh thu Q1/2026", 395.0, Q["2026Q1"]["revenue"]),
    ("Doanh thu Q2/2026", 453.1, Q["2026Q2"]["revenue"]),
    ("Doanh thu H1/2026", 848.2, H["2026H1"]["revenue"]),
    ("Tăng trưởng doanh thu H1/2026, %", 58.9, g(H["2026H1"]["revenue"], H["2025H1"]["revenue"])),
    ("LNTT FY2025", 340.2, Y["FY2025"]["pbt"]),
    ("LNTT Q4/2025", 11.7, Q["2025Q4"]["pbt"]),
    ("LNST Q4/2025 so cùng kỳ, %", -72.0, g(Q["2025Q4"]["pat"], Q["2024Q4"]["pat"])),
    ("LNTT Q1/2026", 14.2, Q["2026Q1"]["pbt"]),
    ("LNTT Q2/2026", 98.9, Q["2026Q2"]["pbt"]),
    ("Tăng trưởng LNTT Q2/2026, %", 8.7, g(Q["2026Q2"]["pbt"], Q["2025Q2"]["pbt"])),
    ("LNTT H1/2026", 113.1, H["2026H1"]["pbt"]),
    ("LNST H1/2026", 94.3, H["2026H1"]["pat"]),
    ("Biên LNTT FY2025, %", 23.2, DV and Y["FY2025"]["pbt"] / Y["FY2025"]["revenue"] * 100),
    ("Biên LNTT H1/2026, %", 13.3, H["2026H1"]["pbt"] / H["2026H1"]["revenue"] * 100),
    ("Doanh thu môi giới FY2025", 404.0, Y["FY2025"]["rev_brokerage"]),
    ("Doanh thu môi giới Q4/2025", 125.0, Q["2025Q4"]["rev_brokerage"]),
    ("Doanh thu môi giới H1/2026 tăng, %", 80.8, g(H["2026H1"]["rev_brokerage"], H["2025H1"]["rev_brokerage"])),
    ("Chi phí môi giới Q4/2025", 150.0, -Q["2025Q4"]["cost_brokerage"]),
    ("Chi phí môi giới Q4/2025 tăng, %", 198.0, g(Q["2025Q4"]["cost_brokerage"], Q["2024Q4"]["cost_brokerage"])),
    ("Chi phí môi giới Q1/2026", 137.8, -Q["2026Q1"]["cost_brokerage"]),
    ("Chi phí môi giới Q1/2026 tăng, %", 125.0, g(Q["2026Q1"]["cost_brokerage"], Q["2025Q1"]["cost_brokerage"])),
    ("Chi phí hoạt động Q1/2026 tăng, %", 120.0, g(Q["2026Q1"]["operating_cost"], Q["2025Q1"]["operating_cost"])),
    ("'Dự phòng tự doanh' Q1/2026 tăng, % (dòng 24)", 405.0,
     g(Q["2026Q1"]["cost_provision_and_loan_funding"], Q["2025Q1"]["cost_provision_and_loan_funding"])),
    ("Chi phí lãi vay Q2/2026 tăng, %", 165.6, g(Q["2026Q2"]["interest_expense"], Q["2025Q2"]["interest_expense"])),
    ("Vay ngắn hạn cuối 2024", 6494.0, Y["FY2024"]["short_term_borrowing"]),
    ("Vay ngắn hạn cuối 2025", 9302.0, Y["FY2025"]["short_term_borrowing"]),
    ("Dư nợ cho vay cuối 2025", 5832.0, Y["FY2025"]["loans"]),
    ("Dư nợ cho vay Q1/2026", 5910.0, Q["2026Q1"]["loans"]),
    ("Dư nợ cho vay Q2/2026", 6303.0, Q["2026Q2"]["loans"]),
    ("Dư nợ Q2/2026 tăng so cùng kỳ, %", 25.0, g(Q["2026Q2"]["loans"], Q["2025Q2"]["loans"])),
    ("LNTT 9 tháng 2023 tăng, %", 334.0,
     g(sum(Q[f"2023Q{i}"]["pbt"] for i in (1, 2, 3)), sum(Q[f"2022Q{i}"]["pbt"] for i in (1, 2, 3)))),
    ("Tổng tài sản cuối 2025", 15000.0, Y["FY2025"]["total_assets"]),
    ("Vốn điều lệ 30/6/2026", 4286.0, Q["2026Q2"]["charter_capital"]),
]
print("\n| Chỉ tiêu | Báo chí / data pack cũ | BCTC | Chênh |")
print("|---|---:|---:|---:|")
for lab, press, filed in checks:
    print(f"| {lab} | {press:,.1f} | {filed:,.1f} | {filed - press:+,.1f} |")

print("\nAnnual summary")
print("| Năm | Doanh thu | LNTT | LNST | Biên LNTT % | ROE % | Vốn CSH | Dư nợ | Tổng TS | Nợ vay/VCSH |")
print("|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|")
ys = list(Y)
for i, p in enumerate(ys):
    d = Y[p]
    roe = d["pat"] / ((Y[ys[i - 1]]["equity"] + d["equity"]) / 2) * 100 if i else None
    debt = d["short_term_borrowing"] + (d["bonds_short"] or 0) + (d["bonds_long"] or 0)
    print(f"| {p[2:]} | {d['revenue']:,.1f} | {d['pbt']:,.1f} | {d['pat']:,.1f} | {d['pbt'] / d['revenue'] * 100:.1f} | "
          f"{'' if roe is None else f'{roe:.1f}'} | {d['equity']:,.0f} | {d['loans']:,.0f} | {d['total_assets']:,.0f} | "
          f"{debt / d['equity']:.2f} |")

print("\n| Năm | Lợi suất cho vay % | Lợi suất HTM % | Chi phí vốn ước tính % | Môi giới sau chi phí trực tiếp | Tài sản HTM | Nợ vay + trái phiếu |")
print("|---|---:|---:|---:|---:|---:|---:|")
debt = lambda d: d["short_term_borrowing"] + (d["bonds_short"] or 0) + (d["bonds_long"] or 0)
for i, p in enumerate(ys[1:], start=1):
    d, prev = Y[p], Y[ys[i - 1]]
    fund = funding(d) - (prev["loan_allowance"] - d["loan_allowance"])
    print(f"| {p[2:]} | {d['rev_lending'] / ((prev['loans'] + d['loans']) / 2) * 100:.1f} | "
          f"{d['rev_htm'] / ((htm(prev) + htm(d)) / 2) * 100:.1f} | {fund / ((debt(prev) + debt(d)) / 2) * 100:.1f} | "
          f"{d['rev_brokerage'] + d['cost_brokerage']:,.1f} | {htm(d):,.0f} | {debt(d):,.0f} |")

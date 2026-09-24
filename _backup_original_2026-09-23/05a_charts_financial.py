import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
import os

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "fig")
os.makedirs(OUT, exist_ok=True)

# validated categorical slots 1-3 from the reference palette
BLUE   = "#2a78d6"
ORANGE = "#eb6834"
AQUA   = "#1baf7a"
INK    = "#1a1a1a"
MUTED  = "#6b6b6b"
GRID   = "#d9d9d9"
SURF   = "#ffffff"

plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "font.size": 9,
    "axes.edgecolor": GRID,
    "axes.labelcolor": INK,
    "text.color": INK,
    "xtick.color": MUTED,
    "ytick.color": MUTED,
    "figure.facecolor": SURF,
    "axes.facecolor": SURF,
    "savefig.facecolor": SURF,
})

def style(ax, ygrid=True):
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_color(GRID)
    ax.spines["bottom"].set_color(GRID)
    if ygrid:
        ax.yaxis.grid(True, color=GRID, linewidth=0.6)
        ax.set_axisbelow(True)
    ax.tick_params(length=0)

def save(fig, name):
    fig.savefig(f"{OUT}/{name}.png", dpi=200, bbox_inches="tight", pad_inches=0.12)
    plt.close(fig)
    print("wrote", name)

# ---------------------------------------------------------------- Fig 1
# DNSE derivatives brokerage market share
labels = ["Q1\n2024", "Q1\n2025", "Q2\n2025", "Q3\n2025", "Q4\n2025", "Q1\n2026", "Q2\n2026"]
share  = [4.01, 16.70, 17.33, 23.67, 24.26, 25.50, 25.38]
x = range(len(labels))

fig, ax = plt.subplots(figsize=(7.0, 3.1))
ax.plot(x, share, color=BLUE, linewidth=2, marker="o", markersize=6,
        markerfacecolor=BLUE, markeredgecolor=SURF, markeredgewidth=2, zorder=3)
ax.axhline(33.84, color=ORANGE, linewidth=1.6, linestyle=(0, (5, 3)), zorder=2)
ax.text(len(labels) - 1.02, 34.9, "VPS, Q2 2026: 33.84%", ha="right", va="bottom",
        fontsize=8.5, color=ORANGE)
for i, v in [(0, share[0]), (6, share[6])]:
    ax.annotate(f"{v:.2f}%", (i, v), textcoords="offset points",
                xytext=(0, 11), ha="center", fontsize=9, color=INK, fontweight="bold")
ax.set_xticks(list(x)); ax.set_xticklabels(labels)
ax.set_ylim(0, 40)
ax.yaxis.set_major_formatter(FuncFormatter(lambda v, p: f"{v:.0f}%"))
ax.set_ylabel("Share of derivatives brokerage")
style(ax)
save(fig, "fig1_derivatives_share")

# ---------------------------------------------------------------- Fig 2
# The monetisation gap
cats = ["Derivatives brokerage\n(Q2 2026)",
        "New accounts opened\n(Q1 2026)",
        "Total market accounts\n(end-2025)",
        "HNX listed equity\nbrokerage (Q2 2026)",
        "Industry margin\nbalance (Q2 2026)"]
vals = [25.38, 18.00, 13.00, 2.88, 1.42]
cols = [AQUA, BLUE, BLUE, ORANGE, ORANGE]

fig, ax = plt.subplots(figsize=(7.0, 3.4))
bars = ax.barh(range(len(cats)), vals, color=cols, height=0.62, zorder=3)
for b in bars:
    b.set_linewidth(2); b.set_edgecolor(SURF)
for i, v in enumerate(vals):
    ax.text(v + 0.5, i, f"{v:.2f}%", va="center", ha="left",
            fontsize=9, color=INK, fontweight="bold")
ax.set_yticks(range(len(cats))); ax.set_yticklabels(cats, fontsize=8.5)
ax.invert_yaxis()
ax.set_xlim(0, 30)
ax.xaxis.set_major_formatter(FuncFormatter(lambda v, p: f"{v:.0f}%"))
ax.set_xlabel("DNSE share of the Vietnamese market")
ax.xaxis.grid(True, color=GRID, linewidth=0.6); ax.set_axisbelow(True)
ax.spines["top"].set_visible(False); ax.spines["right"].set_visible(False)
ax.spines["left"].set_color(GRID); ax.spines["bottom"].set_color(GRID)
ax.tick_params(length=0)
save(fig, "fig2_monetisation_gap")

# ---------------------------------------------------------------- Fig 3
# Pre-tax profit margin by reporting period (single scale, no mixed-length bars)
per = ["FY2025", "Q1 2026", "Q2 2026", "H1 2026"]
rev = [1467.0, 395.0, 453.1, 848.2]
pbt = [340.2, 14.2, 98.9, 113.1]
mar = [p / r * 100 for p, r in zip(pbt, rev)]

fig, ax = plt.subplots(figsize=(7.0, 3.0))
bars = ax.bar(per, mar, color=[BLUE, ORANGE, ORANGE, ORANGE], width=0.5, zorder=3)
for b in bars: b.set_linewidth(2); b.set_edgecolor(SURF)
for i, (m, r, p) in enumerate(zip(mar, rev, pbt)):
    ax.text(i, m + 0.9, f"{m:.1f}%", ha="center", fontsize=9.5, color=INK, fontweight="bold")
    ax.text(i, -2.4, f"revenue {r:,.0f}\nprofit {p:,.1f}", ha="center", va="top",
            fontsize=7.6, color=MUTED)
ax.set_ylim(0, 28)
ax.yaxis.set_major_formatter(FuncFormatter(lambda v, p: f"{v:.0f}%"))
ax.set_ylabel("Pre-tax profit margin")
ax.text(0, 27.4, "Amounts in VND billion. FY2025 is a full year, the others are shorter periods", fontsize=8, color=MUTED, ha="left")
style(ax)
save(fig, "fig3_revenue_margin")

# ---------------------------------------------------------------- Fig 4
# H1 2026 revenue composition
comp_l = ["Interest on lending\nand receivables", "Brokerage\ncommissions",
          "Investment\nincome", "Other"]
comp_v = [336.1, 222.1, 193.4, 96.6]
tot = sum(comp_v)

fig, ax = plt.subplots(figsize=(7.0, 1.55))
left = 0
colors = [BLUE, ORANGE, AQUA, "#b9c0c7"]
for v, c, l in zip(comp_v, colors, comp_l):
    ax.barh([0], [v], left=left, color=c, height=0.5, edgecolor=SURF, linewidth=2, zorder=3)
    ax.text(left + v / 2, 0, f"{v / tot * 100:.1f}%", ha="center", va="center",
            fontsize=9, color="white", fontweight="bold")
    ax.text(left + v / 2, -0.44, l, ha="center", va="top", fontsize=8, color=INK)
    left += v
ax.set_xlim(0, tot); ax.set_ylim(-1.15, 0.45)
ax.axis("off")
ax.text(0, 0.42, f"H1 2026 operating revenue: VND {tot:,.1f} billion",
        fontsize=8.5, color=MUTED)
save(fig, "fig4_revenue_mix")

# ---------------------------------------------------------------- Fig 5
# Progress against the 2026 plan at the half year
lab5 = ["Operating revenue\nVND 848.2bn of 1,736bn", "Pre-tax profit\nVND 113.1bn of 550bn"]
pct5 = [48.9, 20.6]

fig, ax = plt.subplots(figsize=(7.0, 2.3))
bars = ax.barh(range(2), pct5, color=[BLUE, ORANGE], height=0.5, zorder=3)
for b in bars: b.set_linewidth(2); b.set_edgecolor(SURF)
ax.axvline(50, color=INK, linewidth=1.4, linestyle=(0, (4, 3)), zorder=4)
ax.text(51, -0.62, "Half-year pace", fontsize=8.5, color=INK)
for i, v in enumerate(pct5):
    ax.text(v + 1.2, i, f"{v:.1f}%", va="center", fontsize=9.5, color=INK, fontweight="bold")
ax.set_yticks(range(2)); ax.set_yticklabels(lab5, fontsize=8.5)
ax.invert_yaxis(); ax.set_xlim(0, 65)
ax.xaxis.set_major_formatter(FuncFormatter(lambda v, p: f"{v:.0f}%"))
ax.set_xlabel("Share of full-year 2026 target achieved in H1")
ax.xaxis.grid(True, color=GRID, linewidth=0.6); ax.set_axisbelow(True)
ax.spines["top"].set_visible(False); ax.spines["right"].set_visible(False)
ax.spines["left"].set_color(GRID); ax.spines["bottom"].set_color(GRID)
ax.tick_params(length=0)
save(fig, "fig5_plan_progress")

# ---------------------------------------------------------------- Fig 6
# Findex: saving at an institution versus borrowing from one
yrs = [2011, 2014, 2017, 2022, 2024]
saved = [7.74, 14.61, 14.48, 19.86, 43.09]
borrow = [None, 19.50, 21.72, 10.02, 7.67]

fig, ax = plt.subplots(figsize=(7.0, 3.1))
ax.plot(yrs, saved, color=BLUE, linewidth=2, marker="o", markersize=6,
        markerfacecolor=BLUE, markeredgecolor=SURF, markeredgewidth=2,
        label="Saved at a financial institution", zorder=3)
bx = [y for y, v in zip(yrs, borrow) if v is not None]
by = [v for v in borrow if v is not None]
ax.plot(bx, by, color=ORANGE, linewidth=2, marker="o", markersize=6,
        markerfacecolor=ORANGE, markeredgecolor=SURF, markeredgewidth=2,
        label="Borrowed from a formal financial institution", zorder=3)
ax.annotate("43.1%", (2024, 43.09), textcoords="offset points", xytext=(-4, 10),
            ha="right", fontsize=9, color=INK, fontweight="bold")
ax.annotate("7.7%", (2024, 7.67), textcoords="offset points", xytext=(-4, -16),
            ha="right", fontsize=9, color=INK, fontweight="bold")
ax.set_xticks(yrs); ax.set_xticklabels([str(y) for y in yrs])
ax.set_ylim(0, 50)
ax.yaxis.set_major_formatter(FuncFormatter(lambda v, p: f"{v:.0f}%"))
ax.set_ylabel("Share of adults aged 15 and over")
leg = ax.legend(frameon=False, fontsize=8.5, loc="upper left")
for t in leg.get_texts(): t.set_color(INK)
style(ax)
save(fig, "fig6_findex_save_borrow")

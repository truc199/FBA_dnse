import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
import os, sys
_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path[:0] = [_HERE, os.path.join(_HERE, "data")]

OUT = os.path.join(_HERE, "fig")
os.makedirs(OUT, exist_ok=True)

BLUE, ORANGE, AQUA = "#2a78d6", "#eb6834", "#1baf7a"
INK, MUTED, GRID, SURF = "#1a1a1a", "#6b6b6b", "#d9d9d9", "#ffffff"

plt.rcParams.update({
    "font.family": "DejaVu Sans", "font.size": 9,
    "axes.edgecolor": GRID, "axes.labelcolor": INK, "text.color": INK,
    "xtick.color": MUTED, "ytick.color": MUTED,
    "figure.facecolor": SURF, "axes.facecolor": SURF, "savefig.facecolor": SURF,
})

def style(ax, ygrid=True, xgrid=False):
    ax.spines["top"].set_visible(False); ax.spines["right"].set_visible(False)
    ax.spines["left"].set_color(GRID); ax.spines["bottom"].set_color(GRID)
    if ygrid: ax.yaxis.grid(True, color=GRID, linewidth=0.6)
    if xgrid: ax.xaxis.grid(True, color=GRID, linewidth=0.6)
    ax.set_axisbelow(True); ax.tick_params(length=0)

def save(fig, name):
    fig.savefig(f"{OUT}/{name}.png", dpi=200, bbox_inches="tight", pad_inches=0.12)
    plt.close(fig); print("wrote", name)

import reviews as RV
import brokers as BR
from importlib import import_module
seg_build = import_module("04_segment_model").build

# =============================================================== Fig 2 (revised)
# Where DNSE is large and where it is small, Q2 2026
cats = ["Derivatives brokerage\n(HNX, Q2 2026)",
        "Customer accounts\n(share of 13.85m market accounts)",
        "HNX listed-share brokerage\n(Q2 2026)",
        "HOSE listed-share brokerage\n(outside the top ten)",
        "Lending balance\n(share of industry, Q2 2026)"]
vals = [25.38, 12.27, 2.88, 2.94, 1.39]
cols = [AQUA, BLUE, ORANGE, ORANGE, ORANGE]
labs = ["25.38%", "12.27%", "2.88%", "below 2.94%", "1.39%"]

fig, ax = plt.subplots(figsize=(7.0, 3.5))
bars = ax.barh(range(len(cats)), vals, color=cols, height=0.6, zorder=3)
for b in bars: b.set_linewidth(2); b.set_edgecolor(SURF)
bars[3].set_alpha(0.45)
for i, (v, t) in enumerate(zip(vals, labs)):
    ax.text(v + 0.45, i, t, va="center", ha="left", fontsize=9, color=INK, fontweight="bold")
ax.set_yticks(range(len(cats))); ax.set_yticklabels(cats, fontsize=8.3)
ax.invert_yaxis(); ax.set_xlim(0, 31)
ax.xaxis.set_major_formatter(FuncFormatter(lambda v, p: f"{v:.0f}%"))
ax.set_xlabel("DNSE share of the Vietnamese market")
style(ax, ygrid=False, xgrid=True)
save(fig, "fig2_monetisation_gap")

# =============================================================== Fig 7
# Rating of substantive reviews by year, after cleaning
yrs  = [r[0] for r in RV.YEAR_TAB][1:]          # drop 2020, n = 3
sub  = [r[10] for r in RV.YEAR_TAB][1:]
subn = [r[9]  for r in RV.YEAR_TAB][1:]
x = range(len(yrs))

fig, ax = plt.subplots(figsize=(7.0, 3.2))
ax.plot(x, sub, color=BLUE, linewidth=2, marker="o", markersize=7,
        markerfacecolor=BLUE, markeredgecolor=SURF, markeredgewidth=2, zorder=3)
for i, (v, n) in enumerate(zip(sub, subn)):
    ax.annotate(f"{v:.2f}", (i, v), textcoords="offset points", xytext=(0, 11),
                ha="center", fontsize=9, color=INK, fontweight="bold")
    ax.text(i, 0.55, f"n={n}", ha="center", fontsize=7.6, color=MUTED)
ax.axhline(3.0, color=MUTED, linewidth=1, linestyle=(0, (4, 3)), zorder=1)
ax.set_xticks(list(x)); ax.set_xticklabels(yrs)
ax.set_ylim(0.4, 5.0); ax.set_yticks([1, 2, 3, 4, 5])
ax.set_ylabel("Mean stars, substantive reviews only")
style(ax)
save(fig, "fig7_review_rating_by_year")

# =============================================================== Fig 8
# What the negative reviews are about
th = [r for r in RV.THEME_TAB if r[1] >= 4]
th.sort(key=lambda r: r[1])
names = {"onboarding": "Account opening and identity checks",
         "stability": "Crashes, freezes and login failures",
         "money": "Deposits and withdrawals",
         "promo": "Sign-up bonus terms",
         "fees": "Charges differing from the advertised rate",
         "fraud": "Accusation of deception",
         "closure": "Cannot close the account",
         "influencer": "Arrived through a social media referral"}
lab = [names.get(r[0], r[0]) for r in th]
cnt = [r[1] for r in th]
pct = [r[5] for r in th]

fig, ax = plt.subplots(figsize=(7.0, 3.3))
bars = ax.barh(range(len(lab)), pct, color=ORANGE, height=0.62, zorder=3)
for b in bars: b.set_linewidth(2); b.set_edgecolor(SURF)
for i, (p, c) in enumerate(zip(pct, cnt)):
    ax.text(p + 0.5, i, f"{p:.1f}%  (n={c})", va="center", ha="left", fontsize=8.6, color=INK)
ax.set_yticks(range(len(lab))); ax.set_yticklabels(lab, fontsize=8.5)
ax.set_xlim(0, 33)
ax.xaxis.set_major_formatter(FuncFormatter(lambda v, p: f"{v:.0f}%"))
ax.set_xlabel("Share of the 271 cleaned one and two star reviews")
style(ax, ygrid=False, xgrid=True)
save(fig, "fig8_negative_themes")

# =============================================================== Fig 9
# Peer comparison of app ratings after the same cleaning rule
rows = RV.PEERS
lab9 = [r[0] for r in rows]
allm = [r[6] for r in rows]     # clean mean, full history
m26  = [r[12] for r in rows]    # clean mean, 2026 only
xx = range(len(lab9))
w = 0.34

fig, ax = plt.subplots(figsize=(7.0, 3.1))
b1 = ax.bar([i - w/2 for i in xx], allm, width=w, color=BLUE, zorder=3,
            label="Full history, cleaned")
b2 = ax.bar([i + w/2 for i in xx], m26, width=w, color=ORANGE, zorder=3,
            label="2026 only, cleaned")
for b in list(b1) + list(b2): b.set_linewidth(2); b.set_edgecolor(SURF)
for i, v in enumerate(allm):
    ax.text(i - w/2, v + 0.08, f"{v:.2f}", ha="center", fontsize=8.8, color=INK, fontweight="bold")
for i, v in enumerate(m26):
    ax.text(i + w/2, v + 0.08, f"{v:.2f}", ha="center", fontsize=8.8, color=INK, fontweight="bold")
for i, r in enumerate(rows):
    ax.text(i, -0.42, f"n={r[3]:,} cleaned of {r[2]:,}", ha="center", fontsize=7.4, color=MUTED)
ax.set_xticks(list(xx)); ax.set_xticklabels(lab9, fontsize=9)
ax.set_ylim(0, 4.6); ax.set_yticks([1, 2, 3, 4])
ax.set_ylabel("Mean stars")
leg = ax.legend(frameon=False, fontsize=8.5, loc="upper right", ncol=2)
for t in leg.get_texts(): t.set_color(INK)
style(ax)
save(fig, "fig9_peer_ratings")

# =============================================================== Fig 10
# Findex segment model
rows = [r for r in seg_build() if r["segment"] != "All adults"]
fig, ax = plt.subplots(figsize=(7.0, 4.3))
for r in rows:
    size = 20 + r["unactivated_adults_m"] * 26
    hi = r["segment"] in ("Richest 60%", "In labour force", "Secondary educ or more")
    yg = r["segment"] == "Young (15-24)"
    c = AQUA if yg else (BLUE if hi else "#b9c0c7")
    ax.scatter(r["index_b_digital"], r["index_a_investable"], s=size, color=c,
               edgecolor=SURF, linewidth=2, zorder=3)
lblpos = {
    "Richest 60%": (8, 2), "Urban": (8, 1), "In labour force": (9, -3),
    "Secondary educ or more": (-6, -15), "Women": (-10, -14), "Young (15-24)": (5, -12),
    "Older (25+)": (-20, 9), "Men": (8, -2), "Rural": (8, -2),
    "Poorest 40%": (8, -2), "Out of labour force": (8, -2), "Primary educ or less": (8, -2),
}
for r in rows:
    dx, dy = lblpos.get(r["segment"], (8, 0))
    ax.annotate(r["segment"], (r["index_b_digital"], r["index_a_investable"]),
                textcoords="offset points", xytext=(dx, dy), fontsize=8.2, color=INK)
ax.plot([20, 52], [20, 52], color=MUTED, linewidth=1, linestyle=(0, (4, 3)), zorder=1)
ax.text(51, 49.4, "equal readiness and surplus", fontsize=7.6, color=MUTED,
        ha="right", va="top", rotation=38, rotation_mode="anchor")
ax.set_xlim(20, 84); ax.set_ylim(10, 53)
ax.set_xlabel("Index B, digital transacting habit")
ax.set_ylabel("Index A, investable surplus held formally")
ax.text(21, 51.5, "Bubble area is the unactivated pool in millions of adults",
        fontsize=7.8, color=MUTED, va="top")
style(ax, ygrid=True, xgrid=True)
save(fig, "fig10_segment_model")

# =============================================================== Fig 11
# Where the industry earns, Q2 2026
pb = [r for r in BR.PBT_Q2_2026 if r[0] != "VIX"]
pb.sort(key=lambda r: r[1])
lab11 = [r[0] for r in pb]; val11 = [r[1] for r in pb]
cols11 = [ORANGE if n == "DNSE" else "#b9c0c7" for n in lab11]

fig, ax = plt.subplots(figsize=(7.0, 2.9))
bars = ax.barh(range(len(lab11)), val11, color=cols11, height=0.6, zorder=3)
for b in bars: b.set_linewidth(2); b.set_edgecolor(SURF)
for i, v in enumerate(val11):
    ax.text(v + 35, i, f"{v:,.0f}" if v >= 1000 else f"{v:,.1f}", va="center",
            ha="left", fontsize=8.8, color=INK, fontweight="bold")
ax.set_yticks(range(len(lab11))); ax.set_yticklabels(lab11, fontsize=8.8)
ax.set_xlim(0, 2500)
ax.set_xlabel("Q2 2026 pre-tax profit, VND billion")
style(ax, ygrid=False, xgrid=True)
save(fig, "fig11_peer_profit")

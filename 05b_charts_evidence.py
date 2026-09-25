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
# Where DNSE is large and where it is small, Q2 2026. Every value comes from brokers.py.
_pos = {m: (v, tot, sh) for m, v, _, tot, sh in BR.DNSE_POSITION}
deriv = dict((n, v) for _, n, v in BR.DERIV_Q2_2026)["DNSE"]
hnx = dict((n, v) for _, n, v in BR.HNX_Q2_2026)["DNSE"]
hose_cut = BR.HOSE_Q2_2026[-1][2]                 # tenth place; DNSE is below it
acc_share = _pos["Customer accounts"][0] / _pos["Customer accounts"][1] * 100
lend_share = dict(BR.MARGIN_Q2_2026)["DNSE"] / BR.MARGIN_TOTAL_Q2 * 100
cats = ["Derivatives brokerage\n(HNX, Q2 2026)",
        f"Customer accounts\n(share of {_pos['Customer accounts'][1] / 1e6:.2f}m market accounts)",
        "HNX listed-share brokerage\n(Q2 2026)",
        "HOSE listed-share brokerage\n(outside the top ten)",
        "Lending balance\n(share of industry, Q2 2026)"]
vals = [deriv, acc_share, hnx, hose_cut, lend_share]
cols = [AQUA, BLUE, ORANGE, ORANGE, ORANGE]
labs = [f"{v:.2f}%" for v in vals]
labs[3] = f"below {hose_cut:.2f}%"

fig, ax = plt.subplots(figsize=(7.0, 3.5))
bars = ax.barh(range(len(cats)), vals, color=cols, height=0.6, zorder=3)
for b in bars: b.set_linewidth(2); b.set_edgecolor(SURF)
# The HOSE figure is an upper bound, not a value: draw it as an open, hatched bar so it
# does not read as larger than the HNX share above it.
bars[3].set_facecolor("none"); bars[3].set_edgecolor(ORANGE); bars[3].set_linewidth(1.2)
bars[3].set_hatch("////"); bars[3].set_linestyle((0, (3, 2)))
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
MIN_N = 10                                        # 2020 has three reviews
shown = [r for r in RV.YEAR_TAB if r[9] >= MIN_N]
yrs  = [r[0] for r in shown]
sub  = [r[10] for r in shown]
subn = [r[9] for r in shown]
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
         "influencer": "Arrived through a social media referral",
         "ui": "Interface and charts",
         "zalopay": "ZaloPay linkage and its charge",
         "yield": "Idle-cash earning feature"}
missing = [r[0] for r in th if r[0] not in names]
if missing:
    raise KeyError(f"no chart label for theme(s) {missing}")
lab = [names.get(r[0], r[0]) for r in th]
cnt = [r[1] for r in th]
pct = [r[5] for r in th]

fig, ax = plt.subplots(figsize=(7.0, 3.3))
bars = ax.barh(range(len(lab)), pct, color=ORANGE, height=0.62, zorder=3)
for b in bars: b.set_linewidth(2); b.set_edgecolor(SURF)
for i, (p, c) in enumerate(zip(pct, cnt)):
    ax.text(p + 0.5, i, f"{p:.1f}%  (n={c})", va="center", ha="left", fontsize=8.6, color=INK)
ax.set_yticks(range(len(lab))); ax.set_yticklabels(lab, fontsize=8.5)
ax.set_xlim(0, max(pct) + 8)
ax.xaxis.set_major_formatter(FuncFormatter(lambda v, p: f"{v:.0f}%"))
ax.set_xlabel(f"Share of the {RV.DNSE_TOTALS['negative_1_2']} cleaned one and two star reviews")
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
            label="All reviews pulled, cleaned")
b2 = ax.bar([i + w/2 for i in xx], m26, width=w, color=ORANGE, zorder=3,
            label="2026 only, cleaned")
for b in list(b1) + list(b2): b.set_linewidth(2); b.set_edgecolor(SURF)
for i, v in enumerate(allm):
    ax.text(i - w/2, v + 0.08, f"{v:.2f}", ha="center", fontsize=8.8, color=INK, fontweight="bold")
for i, v in enumerate(m26):
    ax.text(i + w/2, v + 0.08, f"{v:.2f}", ha="center", fontsize=8.8, color=INK, fontweight="bold")
ax.set_xticks(list(xx))
ax.set_xticklabels([f"{r[0]}\nn={r[3]:,} cleaned of {r[2]:,}\n2026: n={r[11]}" for r in rows],
                   fontsize=8.4)
ax.set_ylim(0, 4.6); ax.set_yticks([1, 2, 3, 4])
ax.set_ylabel("Mean stars")
leg = ax.legend(frameon=False, fontsize=8.5, loc="upper right", ncol=2)
for t in leg.get_texts(): t.set_color(INK)
style(ax)
save(fig, "fig9_peer_ratings")

# =============================================================== Fig 10
# Findex segment model. A and B are built from different indicators, so there is no
# diagonal: the chart compares segments with each other, not A with B.
rows = [r for r in seg_build() if r["segment"] != "All adults"]
top = {r["segment"] for r in rows if r["priority_rank"] <= 3}
fig, ax = plt.subplots(figsize=(7.0, 4.3))
for r in sorted(rows, key=lambda r: -r["unactivated_adults_m"]):   # small bubbles on top
    size = r["unactivated_adults_m"] * 32                            # area proportional to pool
    yg = r["segment"] == "Young (15-24)"
    c = AQUA if yg else (BLUE if r["segment"] in top else "#b9c0c7")
    ax.scatter(r["index_b_digital"], r["index_a_investable"], s=size, color=c, alpha=0.9,
               edgecolor=SURF, linewidth=1.5, zorder=3)
lblpos = {
    "Richest 60%": (10, 2), "Urban": (6, 7), "In labour force": (11, -4),
    "Secondary educ or more": (-4, -19), "Women": (-6, 13), "Young (15-24)": (7, -12),
    "Older (25+)": (-62, 8), "Men": (9, -3), "Rural": (-38, -12),
    "Poorest 40%": (8, -2), "Out of labour force": (8, -2), "Primary educ or less": (8, -2),
}
for r in rows:
    dx, dy = lblpos.get(r["segment"], (8, 0))
    ax.annotate(r["segment"], (r["index_b_digital"], r["index_a_investable"]),
                textcoords="offset points", xytext=(dx, dy), fontsize=8.2, color=INK)
ax.set_xlim(20, 84); ax.set_ylim(10, 53)
ax.set_xlabel("Index B, digital transacting habit")
ax.set_ylabel("Index A, investable surplus held formally")
ax.text(21, 51.5, "Bubble area is the unactivated pool in millions of adults. "
        "Blue: top three by priority score",
        fontsize=7.8, color=MUTED, va="top")
style(ax, ygrid=True, xgrid=True)
save(fig, "fig10_segment_model")

# =============================================================== Fig 11
# Where the industry earns, Q2 2026
pb = sorted(BR.PBT_Q2_2026, key=lambda r: r[1])
lab11 = [r[0] for r in pb]; val11 = [r[1] for r in pb]
cols11 = [ORANGE if n == "DNSE" else "#b9c0c7" for n in lab11]

fig, ax = plt.subplots(figsize=(7.0, 0.3 * len(pb) + 0.8))
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

# =============================================================== Fig A1
# Google Play against the App Store over the window both stores cover
if RV.STORE_COMPARE:
    short = {"stability": "Crashes and login", "onboarding": "Account opening", "fraud": "Deception",
             "promo": "Bonus terms", "money": "Deposits, withdrawals", "closure": "Account closure",
             "ui": "Interface", "influencer": "Social referral", "fees": "Charges",
             "zalopay": "ZaloPay", "yield": "Idle cash"}
    y0, y1 = RV.STORE_WINDOW[0][:4], RV.STORE_WINDOW[1][:4]
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(7.0, 3.3), gridspec_kw={"width_ratios": [1, 1.3]})

    rows = RV.STORE_COMPARE
    xx, w = range(len(rows)), 0.36
    for off, col, idx, lab in ((-w / 2, BLUE, 2, "Google Play"), (w / 2, ORANGE, 5, "App Store")):
        bb = a1.bar([i + off for i in xx], [r[idx] for r in rows], w, color=col, zorder=3, label=lab)
        for b in bb: b.set_linewidth(1.5); b.set_edgecolor(SURF)
        for i, r in enumerate(rows):
            a1.text(i + off, r[idx] + 0.06, f"{r[idx]:.2f}", ha="center", fontsize=7.8, color=INK,
                    fontweight="bold")
    a1.set_xticks(list(xx))
    a1.set_xticklabels([f"{r[0].split()[0]}\nPlay n={r[1]}\niOS n={r[4]}" for r in rows], fontsize=7.6)
    a1.set_ylim(0, 3.6); a1.set_yticks([1, 2, 3])
    a1.set_ylabel(f"Mean stars, cleaned, {y0}-{y1}")
    leg = a1.legend(frameon=False, fontsize=7.8, loc="upper right")
    for t in leg.get_texts(): t.set_color(INK)
    style(a1)

    th = [r for r in RV.STORE_THEMES if r[5] > 0][:6][::-1]
    yy, h = range(len(th)), 0.38
    a2.barh([i + h / 2 for i in yy], [r[2] for r in th], h, color=BLUE, zorder=3)
    a2.barh([i - h / 2 for i in yy], [r[4] for r in th], h, color=ORANGE, zorder=3)
    for i, r in enumerate(th):
        a2.text(r[2] + 0.8, i + h / 2, f"{r[2]:.0f}%", va="center", fontsize=7.4, color=INK)
        a2.text(r[4] + 0.8, i - h / 2, f"{r[4]:.0f}%", va="center", fontsize=7.4, color=INK)
    a2.set_yticks(list(yy)); a2.set_yticklabels([short[r[0]] for r in th], fontsize=8)
    a2.set_xlim(0, max(max(r[2], r[4]) for r in th) + 9)
    a2.xaxis.set_major_formatter(FuncFormatter(lambda v, p: f"{v:.0f}%"))
    a2.set_xlabel(f"Share of DNSE one and two star reviews\n"
                  f"(Google Play n={RV.STORE_NEGATIVES[0]}, App Store n={RV.STORE_NEGATIVES[1]})",
                  fontsize=8)
    style(a2, ygrid=False, xgrid=True)
    fig.tight_layout(w_pad=2.0)
    save(fig, "figA1_store_comparison")

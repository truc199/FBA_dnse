"""Figures of the Round 3A content, drawn from outputs/round3/tables and saved to outputs/round3/figures.

Sizes are those of the slide: full width 12 x 5.5 inches, half slide 6 x 4.5 inches, at 200 dpi, with no
title inside the figure (the slide carries it) and text of at least 12 points at that size. Colours come
from src/config.py: the base case or the series that matters is DNSE red, context series are grey.

Run: python src/round3/figures_round3.py
"""
import csv
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "figures"))
import style  # noqa: E402,F401  (fonts and matplotlib defaults of the Round 2 figures)
from style import plt  # noqa: E402
from config import BOX_GREY, CHARCOAL, GREY, GRID, MID_GREY, RED  # noqa: E402

sys.path.insert(0, str(Path(__file__).resolve().parent))
from payday_model import OUT_R3, TABLES_R3  # noqa: E402

FIG_R3 = OUT_R3 / "figures"
FULL, HALF = (12, 5.5), (6, 4.5)
FS = 13          # body text at slide size
FS_SMALL = 12    # the smallest text allowed
SCEN_STYLE = {"base": (RED, 2.6, "Base"), "low": (MID_GREY, 2.0, "Downside"), "high": (GREY, 2.0, "Upside")}
plt.rcParams.update({"font.size": FS, "axes.labelsize": FS, "xtick.labelsize": FS_SMALL,
                     "ytick.labelsize": FS_SMALL, "legend.fontsize": FS_SMALL})


def read(name):
    with open(TABLES_R3 / name, encoding="utf-8") as f:
        return list(csv.DictReader(f))


def num(x):
    return float(x) if x not in ("", None) else None


def signed(v, fmt="{:,.0f}"):
    """Number with a typographic minus sign."""
    s = fmt.format(v)
    return s.replace("-", "−")


def save(fig, name):
    FIG_R3.mkdir(parents=True, exist_ok=True)
    path = FIG_R3 / name
    fig.savefig(path, dpi=200)
    plt.close(fig)
    print(f"  wrote outputs/round3/figures/{name}")
    return path


def hairline_grid(ax, axis="y"):
    ax.grid(axis=axis, color=GRID, lw=0.8)
    ax.set_axisbelow(True)


def end_labels(ax, items, x, fmt, min_gap):
    """Label line ends at x, pushing labels apart only as far as needed, with a short leader line."""
    items = sorted(items, key=lambda it: it[0])
    placed = []
    for y, text, color in items:
        y_lab = y if not placed or y - placed[-1] >= min_gap else placed[-1] + min_gap
        placed.append(y_lab)
        ax.annotate(fmt(text, y), xy=(x, y), xytext=(x + 1.2, y_lab), va="center", ha="left",
                    fontsize=FS_SMALL, color=CHARCOAL,
                    arrowprops=dict(arrowstyle="-", color=color, lw=1.0, shrinkA=0, shrinkB=0))


# ---------------------------------------------------------------- business case
def scenario_series(col):
    out = {}
    for s in ["low", "base", "high"]:
        rows = read(f"payday_monthly_{s}.csv")
        out[s] = ([0] + [int(r["month"]) for r in rows], [0.0] + [float(r[col]) for r in rows])
    return out


def fig_jcurve():
    """Cumulative cash of the plan under three scenarios, with the months the Board is asked to fund."""
    series = scenario_series("cumulative_cash_vnd_bn")
    pilot_end = 6
    fig, ax = plt.subplots(figsize=HALF, layout="constrained")
    ax.axvspan(0, pilot_end, color=BOX_GREY, lw=0, zorder=0)
    ax.text(0.4, 0.97, "Asked now:\nmonths 1–6", transform=ax.get_xaxis_transform(), va="top", ha="left",
            fontsize=FS_SMALL, color=CHARCOAL)
    ax.axhline(0, color=CHARCOAL, lw=0.9)
    for s in ["low", "high", "base"]:
        color, lw, _ = SCEN_STYLE[s]
        ax.plot(*series[s], color=color, lw=lw, solid_capstyle="round", zorder=3 if s == "base" else 2)
    xs, ys = series["base"]
    i_low = min(range(len(ys)), key=lambda i: ys[i])
    if xs[i_low] < xs[-1]:
        ax.plot(xs[i_low], ys[i_low], "o", ms=7, color=RED, mec="white", mew=2, zorder=4)
    lo = min(min(v[1]) for v in series.values())
    hi = max(max(v[1]) for v in series.values())
    span = hi - lo
    end_labels(ax, [(series[s][1][-1], SCEN_STYLE[s][2], SCEN_STYLE[s][0]) for s in series], xs[-1],
               lambda t, y: f"{t} {signed(y, '{:+,.0f}')}", span * 0.075)
    ax.set_xlim(0, xs[-1] + 14)
    ax.set_xticks([0, 6, 12, 24, 36, 48, 60])
    ax.spines["bottom"].set_bounds(0, xs[-1])
    ax.set_xlabel("Months after Board approval")
    ax.set_ylabel("Cumulative cash, VND billion")
    hairline_grid(ax)
    return save(fig, "payday_jcurve.png")


def fig_tornado():
    """Change in cumulative cash at month 60 when one group of inputs moves to its downside or upside value."""
    rows = read("payday_tornado.csv")
    base = float(rows[0]["cum_cash_m60_base_vnd_bn"])
    rows = rows[::-1]                                   # largest swing on top
    fig, ax = plt.subplots(figsize=HALF, layout="constrained")
    h = 0.34
    for i, r in enumerate(rows):
        lo, hi = float(r["cum_cash_m60_low_vnd_bn"]), float(r["cum_cash_m60_high_vnd_bn"])
        ax.barh(i + h / 2 + 0.02, lo - base, left=base, height=h, color=RED, lw=0)
        ax.barh(i - h / 2 - 0.02, hi - base, left=base, height=h, color=MID_GREY, lw=0)
        for v, y in [(lo, i + h / 2 + 0.02), (hi, i - h / 2 - 0.02)]:
            ax.text(v + (0.25 if v >= base else -0.25), y, signed(v), va="center",
                    ha="left" if v >= base else "right", fontsize=FS_SMALL, color=CHARCOAL)
    ax.axvline(base, color=CHARCOAL, lw=1.0)
    short = {"Acquisition cost per saver": "Acquisition cost", "Net yield on balances": "Net yield",
             "Monthly contribution": "Contribution", "Enrolment rates (cost per saver held)": "Enrolment rates",
             "Build and running cost": "Build and running cost", "Bank fee per contribution": "Bank fee per contribution",
             "Investment returns on balances (0% to 5%)": "Investment returns"}
    ax.set_yticks(range(len(rows)))
    ax.set_yticklabels([short.get(r["driver"], r["driver"]) for r in rows])
    ax.tick_params(axis="y", length=0)
    ax.spines["left"].set_visible(False)
    lo_all = min(min(float(r["cum_cash_m60_low_vnd_bn"]), float(r["cum_cash_m60_high_vnd_bn"])) for r in rows)
    hi_all = max(max(float(r["cum_cash_m60_low_vnd_bn"]), float(r["cum_cash_m60_high_vnd_bn"])) for r in rows)
    pad = (hi_all - lo_all) * 0.16
    ax.set_xlim(lo_all - pad, hi_all + pad)
    ax.set_xlabel(f"Cumulative cash at month 60, VND bn (base {signed(base)})")
    handles = [plt.Rectangle((0, 0), 1, 1, color=RED), plt.Rectangle((0, 0), 1, 1, color=MID_GREY)]
    ax.legend(handles, ["Downside input", "Upside input"], loc="lower center",
              bbox_to_anchor=(0.5, 1.0), ncol=2, handlelength=1.0, columnspacing=1.2)
    hairline_grid(ax, "x")
    return save(fig, "payday_tornado.png")


def fig_balance_accounts():
    """Plan balances and savers whose own plan balance has passed VND 10 million, by month and scenario."""
    bal = scenario_series("balance_vnd_bn")
    acc = scenario_series("new_accounts_above_10m")
    fig, axes = plt.subplots(1, 2, figsize=FULL, layout="constrained")
    for ax, series, ylabel, scale, fmt in [
            (axes[0], bal, "Plan balances, VND billion", 1.0, lambda v: f"{v:,.0f}"),
            (axes[1], acc, "Savers above VND 10 million, thousand", 1e3, lambda v: f"{v:,.1f}")]:
        for s in ["low", "high", "base"]:
            color, lw, _ = SCEN_STYLE[s]
            xs, ys = series[s]
            ax.plot(xs, [y / scale for y in ys], color=color, lw=lw, solid_capstyle="round",
                    zorder=3 if s == "base" else 2)
        xs, ys = series["base"]
        marks = [18, 24, 36]
        for m in marks:
            ax.plot(m, ys[m] / scale, "o", ms=7, color=RED, mec="white", mew=2, zorder=4)
        ax.text(0.03, 0.96, "Base case (dots)\n" + "\n".join(f"Month {m}: {fmt(ys[m] / scale)}" for m in marks),
                transform=ax.transAxes, va="top", ha="left", fontsize=FS_SMALL, color=CHARCOAL, linespacing=1.4)
        span = max(max(v[1]) for v in series.values()) / scale
        end_labels(ax, [(series[s][1][-1] / scale, SCEN_STYLE[s][2], SCEN_STYLE[s][0]) for s in series],
                   xs[-1], lambda t, y: f"{t} {fmt(y)}", span * 0.07)
        ax.set_xlim(0, xs[-1] + 16)
        ax.set_xticks([0, 6, 12, 24, 36, 48, 60])
        ax.spines["bottom"].set_bounds(0, xs[-1])
        ax.set_xlabel("Months after Board approval")
        ax.set_ylabel(ylabel)
        ax.set_ylim(bottom=0)
        ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda v, _: f"{v:,.0f}"))
        hairline_grid(ax)
    return save(fig, "payday_balance_accounts.png")


# ---------------------------------------------------------------- reviews
def fig_review_causes():
    """Share of DNSE's 58 negative reviews of 2026 that mention each cause, coded by hand."""
    rows = [r for r in read("reviews_2026_cause_summary.csv") if r["code"] not in ("group", "n")]
    broke = {"login_otp", "cash_not_credited", "orders_prices", "crash_freeze", "ekyc_opening"}
    order = sorted([r for r in rows if r["code"] not in broke], key=lambda r: float(r["both_pct"])) + \
        sorted([r for r in rows if r["code"] in broke], key=lambda r: float(r["both_pct"]))
    fig, ax = plt.subplots(figsize=HALF, layout="constrained")
    for i, r in enumerate(order):
        v = float(r["both_pct"])
        ax.barh(i, v, height=0.55, color=RED if r["code"] in broke else GREY, lw=0)
        ax.text(v + 0.8, i, f"{v:.0f}% ({r['both_n']})", va="center", ha="left", fontsize=FS_SMALL, color=CHARCOAL)
    ax.set_yticks(range(len(order)))
    ax.set_yticklabels([r["cause"].replace(" (closure, auto-renewal)", "").replace(
        " (service, interface, Ensa, no reason)", "") for r in order])
    ax.tick_params(axis="y", length=0)
    ax.spines["left"].set_visible(False)
    ax.set_xlim(0, max(float(r["both_pct"]) for r in order) * 1.28)
    ax.set_xlabel("Share of 58 negative reviews, Jan–Sep 2026, %")
    handles = [plt.Rectangle((0, 0), 1, 1, color=RED), plt.Rectangle((0, 0), 1, 1, color=GREY)]
    ax.legend(handles, ["Something broke", "Terms, trust or other"], loc="lower center", bbox_to_anchor=(0.5, 1.0),
              ncol=2, handlelength=1.0, columnspacing=1.2)
    hairline_grid(ax, "x")
    return save(fig, "reviews_2026_causes.png")


ALL = [fig_jcurve, fig_tornado, fig_balance_accounts, fig_review_causes]

if __name__ == "__main__":
    for f in ALL:
        f()

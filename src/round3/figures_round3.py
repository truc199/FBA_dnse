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
from config import BOX_GREY, CHARCOAL, CORAL, DARK_RED, GREY, GRID, MID_GREY, RED  # noqa: E402

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


def save(fig, name, dpi=200):
    """Save at slide size. Use dpi=400 for figures with text under 8 points: at 200 dpi Calibri's embedded
    bitmaps for small sizes come out blank in matplotlib 3.11, leaving only ligatures."""
    FIG_R3.mkdir(parents=True, exist_ok=True)
    path = FIG_R3 / name
    fig.savefig(path, dpi=dpi)
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


# ---------------------------------------------------------------- deck figures (Phase 3.2)
# Forms follow the dataviz method: emphasis (DNSE red for the point, grey for context) unless the data is a
# magnitude grid, which takes the one-hue ramp CORAL -> RED -> DARK_RED (validated as an ordinal ramp on white:
# monotone lightness, light end 2.80:1). Text on CORAL is ink, on RED and DARK_RED white (4.96:1 and 8.96:1).
# Every figure reads a CSV in outputs/round3/tables, which is also its table view.
WIDE = (12, 3.6)        # half-height strip across the slide


def wrap_chars(text, width):
    import textwrap
    return "\n".join(textwrap.wrap(text, width))


def fig_why_now():
    """2026 launches of recurring and goal-based plans, the Open API deadline, and investor cash at brokers."""
    import datetime as dt
    events = read("why_now_events.csv")
    cash = read("why_now_investor_cash.csv")
    fig = plt.figure(figsize=WIDE, layout="constrained")
    gs = fig.add_gridspec(1, 2, width_ratios=[3.3, 1])
    ax, bx = fig.add_subplot(gs[0]), fig.add_subplot(gs[1])
    d = dt.date.fromisoformat
    ax.set_xlim(d("2026-01-01"), d("2027-04-15"))
    ax.set_ylim(-1.0, 1.0)
    ax.axhline(0, color=CHARCOAL, lw=1.0, zorder=1)
    colour = {"rival": MID_GREY, "dnse": RED, "regulation": DARK_RED}
    # label side and height in axis units: rivals alternate above and below; DNSE today sits higher
    place = {"SSI eSIP campaign": 0.18, "TCBS TCWealth": -0.18, "VPS Smart Indexing": 0.18,
             "VPBank Goal Jar": -0.18, "DNSE today": 0.62, "Open API deadline": -0.18}
    for e in events:
        c = colour[e["group"]]
        x0 = d(e["start"])
        if e["end"]:
            x1 = d(e["end"])
            ax.plot([x0, x1], [0, 0], color=c, lw=7, solid_capstyle="round", alpha=0.45, zorder=2)
            xm = x0 + (x1 - x0) / 2
        else:
            xm = x0
            ax.plot(xm, 0, "o", ms=10, color=c, mec="white", mew=2, zorder=3)
        y = place[e["label"]]
        ax.plot([xm, xm], [0, y], color=c, lw=1.0, zorder=1)
        head = f"{e['date_label']}: {e['label']}"
        body = wrap_chars(e["detail"], 22)
        line = FS_SMALL * 1.18                      # points per text line
        n_body = body.count("\n") + 1
        up = y > 0
        # above the line the block reads head, then body, ending at the stem; below it starts at the stem
        head_off = 2 + n_body * line if up else -2
        body_off = 2 if up else -2 - line
        kw = dict(ha="center", va="bottom" if up else "top", fontsize=FS_SMALL, textcoords="offset points")
        ax.annotate(head, xy=(xm, y), xytext=(0, head_off), weight="bold",
                    color=RED if e["group"] == "dnse" else CHARCOAL, **kw)
        ax.annotate(body, xy=(xm, y), xytext=(0, body_off), color=CHARCOAL, linespacing=1.18, **kw)
    ticks = [d(s) for s in ("2026-01-01", "2026-04-01", "2026-07-01", "2026-10-01", "2027-01-01", "2027-04-01")]
    ax.set_xticks(ticks)
    ax.set_xticklabels(["Jan 2026", "Apr", "Jul", "Oct", "Jan 2027", "Apr"])
    ax.set_yticks([])
    for s in ("left",):
        ax.spines[s].set_visible(False)
    ax.spines["bottom"].set_visible(False)
    ax.tick_params(axis="x", length=0, pad=-12)
    # investor cash at brokers: a single series, the latest quarter in red
    # one slot per quarter, so the unreported Q4 2025 shows as a gap rather than disappearing
    quarters = ["2025Q3", "2025Q4", "2026Q1", "2026Q2"]
    value = {r["quarter"]: float(r["investor_cash_vnd_trillion"]) for r in cash}
    vals = [value[q] for q in quarters if q in value]
    for x, q in enumerate(quarters):
        if q not in value:
            bx.text(x, 8, "not\nreported", ha="center", va="bottom", fontsize=FS_SMALL, color=MID_GREY,
                    linespacing=1.1)
            continue
        v = value[q]
        bx.bar(x, v, width=0.6, color=RED if q == quarters[-1] else MID_GREY, lw=0)
        bx.text(x, v + 3, f"{v:.1f}", ha="center", va="bottom", fontsize=FS_SMALL, color=CHARCOAL)
    bx.set_xticks(range(len(quarters)))
    bx.set_xticklabels([f"Q{q[-1]}\n{q[:4]}" for q in quarters], linespacing=1.1)
    bx.set_ylim(0, max(vals) * 1.32)
    bx.set_yticks([])
    bx.spines["left"].set_visible(False)
    change = vals[-1] / vals[0] - 1
    bx.annotate(f"{signed(change * 100, '{:+.0f}')}% in three quarters", xy=(len(quarters) - 1, vals[-1] + 16),
                xytext=(len(quarters) - 0.65, max(vals) * 1.24), ha="right", va="center", fontsize=FS_SMALL,
                color=CHARCOAL, arrowprops=dict(arrowstyle="-|>", color=CHARCOAL, lw=1.0, shrinkA=4, shrinkB=2,
                                                connectionstyle="angle,angleA=0,angleB=90,rad=0"))
    bx.set_xlabel("Investor cash at brokers, VND trillion")
    return save(fig, "why_now_timeline.png")


def fig_sizing_funnel():
    """From DNSE's accounts to dormant savers (left), and all savers by channel at month 36 (right)."""
    from matplotlib.patches import FancyBboxPatch
    stages = read("sizing_funnel.csv")
    channels = read("savers_by_channel.csv")
    total = float(next(c for c in channels if c["channel"] == "Total")["savers_month_36"])
    channels = [c for c in channels if c["channel"] != "Total"]
    fig = plt.figure(figsize=HALF)
    ax = fig.add_axes([0, 0, 0.6, 1])
    ax.set_xlim(0, 3.6)
    ax.set_ylim(0, 4.5)
    ax.axis("off")
    tile_h, gap, top = 0.72, 0.36, 4.38
    for i, s in enumerate(stages):
        y = top - tile_h - i * (tile_h + gap)
        last = i == len(stages) - 1
        ax.add_patch(FancyBboxPatch((0.08, y), 2.25, tile_h, boxstyle="round,pad=0,rounding_size=0.08",
                                    fc="white" if last else BOX_GREY, ec=RED if last else "none", lw=2.0))
        ax.text(0.22, y + tile_h - 0.12, f"{float(s['accounts']):,.0f}", ha="left", va="top", fontsize=17,
                weight="bold", color=RED if last else CHARCOAL)
        ax.text(0.22, y + 0.1, s["stage"], ha="left", va="bottom", fontsize=FS_SMALL, color=CHARCOAL)
        if i:
            ya, yb = y + tile_h + gap - 0.04, y + tile_h + 0.04
            ax.annotate("", xy=(0.6, yb), xytext=(0.6, ya),
                        arrowprops=dict(arrowstyle="-|>", color=MID_GREY, lw=1.2, shrinkA=0, shrinkB=0))
            note = s["step"] + ("" if s["basis"].startswith("Accounts") else ", assumption")
            ax.text(0.72, (ya + yb) / 2, note, ha="left", va="center", fontsize=FS_SMALL, color=MID_GREY)
    bx = fig.add_axes([0.66, 0.06, 0.1, 0.8])
    vals = [float(c["savers_month_36"]) for c in channels]
    bottom = 0.0
    for c, v in zip(channels, vals):
        first = c["channel"] == "Account opening"
        bx.bar(0, v, bottom=bottom, width=0.8, color=RED if first else MID_GREY, edgecolor="white", lw=2)
        fig.text(0.79, 0.06 + 0.8 * (bottom + v / 2) / sum(vals),
                 f"{c['channel']}\n{v:,.0f} ({float(c['share'].rstrip('%')):.0f}%)",
                 ha="left", va="center", fontsize=FS_SMALL, color=CHARCOAL, linespacing=1.15)
        bottom += v
    bx.set_xlim(-0.5, 0.5)
    bx.set_ylim(0, sum(vals))
    bx.axis("off")
    fig.text(0.66, 0.9, f"{total:,.0f} savers\nby month 36", ha="left", va="bottom", fontsize=FS_SMALL,
             weight="bold", color=CHARCOAL, linespacing=1.15)
    return save(fig, "sizing_funnel.png")


def fig_positioning_map():
    """Minimum to start against the number of asset types in one plan; Payday in red, verified rivals in grey."""
    rows = read("positioning_map.csv")
    fig, ax = plt.subplots(figsize=HALF, layout="constrained")
    ax.set_yscale("log")
    ax.set_xlim(0.5, 4.6)
    ax.set_ylim(5e4, 2e8)
    ax.axvspan(2.5, 4.6, ymin=0, ymax=(6 - 4.699) / (8.301 - 4.699), color=RED, alpha=0.08, lw=0, zorder=0)
    ax.text(4.5, 6.2e4, "Small ticket,\nseveral asset types", ha="right", va="bottom", fontsize=FS_SMALL,
            color=MID_GREY, linespacing=1.15)
    offsets = {"VPS Smart Indexing": (0.12, 0, "left"), "VNDIRECT retirement plan": (0.12, 0, "left"),
               "VCB Digibank SIP": (0.12, 0, "left"), "VinaSIP": (0.12, 0, "left"),
               "Payday Portfolio": (-0.14, 0, "right")}
    for r in rows:
        x, y = float(r["asset_types"]), float(r["minimum_vnd"])
        me = r["payday"] == "yes"
        ax.plot(x, y, "o", ms=12 if me else 9, color=RED if me else MID_GREY, mec="white", mew=2, zorder=3)
        dx, dy, ha = offsets.get(r["label"], (0.12, 0, "left"))
        ax.text(x + dx, y, r["label"], ha=ha, va="center", fontsize=FS_SMALL, color=CHARCOAL,
                weight="bold" if me else "normal")
    ax.set_xticks([1, 2, 3, 4])
    ax.set_xlabel("Asset types in one plan")
    ax.set_yticks([1e5, 5e5, 1e6, 1e7, 5e7])
    ax.set_yticklabels(["100,000", "500,000", "1 million", "10 million", "50 million"])
    ax.minorticks_off()
    ax.set_ylabel("Minimum to start, VND (log scale)")
    hairline_grid(ax)
    return save(fig, "positioning_map.png")


def fig_gtm_timeline():
    """Year-one activities by month with the three gates (top) and funded savers by month (bottom)."""
    from matplotlib.patches import Polygon
    monthly = read("payday_monthly_base.csv")[:12]
    lanes = [("Build and comply", 0, 3, True), ("Pilot: 45,000 dormant accounts", 3, 6, True),
             ("Dormant roll-out", 6, 12, False), ("In-app offer to traders", 6, 12, False),
             ("Plan step at account opening", 6, 12, False), ("First employers", 9, 12, False)]
    fig = plt.figure(figsize=WIDE, layout="constrained")
    gs = fig.add_gridspec(2, 1, height_ratios=[2.2, 1])
    ax, bx = fig.add_subplot(gs[0]), fig.add_subplot(gs[1])
    n = len(lanes)
    for i, (name, a, b, asked) in enumerate(lanes):
        y = n - i
        ax.barh(y, b - a, left=a, height=0.56, color=RED if asked else MID_GREY, lw=0)
        ax.text(-0.15, y, name, ha="right", va="center", fontsize=FS_SMALL, color=CHARCOAL)
        if b == 12:     # the channel carries on into year two
            ax.add_patch(Polygon([(12.08, y + 0.24), (12.42, y), (12.08, y - 0.24)], closed=True, fc=MID_GREY,
                                 ec="none"))
    gate_y = n + 1.0
    for m, label in [(3, "Gate 0"), (6, "Gate 1"), (12, "Gate 2")]:
        s = 0.22
        ax.add_patch(Polygon([(m, gate_y + s), (m + s * 0.6, gate_y), (m, gate_y - s), (m - s * 0.6, gate_y)],
                             closed=True, fc=CHARCOAL, ec="white", lw=1.5, zorder=3))
        ax.text(m - 0.25, gate_y, label, ha="right", va="center", fontsize=FS_SMALL, color=CHARCOAL)
    for q in (3, 6, 9):
        ax.axvline(q, color=LIGHT_GREY_LINE, lw=0.8, zorder=0)
        bx.axvline(q, color=LIGHT_GREY_LINE, lw=0.8, zorder=0)
    for j, q in enumerate(("Q1", "Q2", "Q3", "Q4")):
        ax.text(1.5 + 3 * j, gate_y + 0.75, q, ha="center", va="center", fontsize=FS_SMALL, weight="bold",
                color=CHARCOAL)
    ax.set_xlim(0, 12.6)
    ax.set_ylim(0.4, gate_y + 1.1)
    ax.axis("off")
    xs = [0] + [int(r["month"]) for r in monthly]
    ys = [0] + [float(r["funded_savers"]) for r in monthly]
    bx.plot(xs, ys, color=RED, lw=2.4, solid_capstyle="round")
    for m in (6, 12):
        bx.plot(m, ys[m], "o", ms=8, color=RED, mec="white", mew=2, zorder=3)
        bx.text(m - 0.15, ys[m] + max(ys) * 0.12, f"{ys[m]:,.0f}", ha="right", va="bottom", fontsize=FS_SMALL,
                color=CHARCOAL)
    bx.set_xlim(0, 12.6)
    bx.set_ylim(0, max(ys) * 1.45)
    bx.set_xticks(range(0, 13, 3))
    bx.set_xlabel("Months after Board approval")
    bx.set_yticks([])
    bx.spines["left"].set_visible(False)
    bx.text(0.1, max(ys) * 1.25, "Funded savers (base case)", ha="left", va="center", fontsize=FS_SMALL,
            color=CHARCOAL)
    return save(fig, "gtm_timeline.png")


LIGHT_GREY_LINE = "#E6E6E6"


def fig_risk_heatmap():
    """Six risks by likelihood and impact on a 1 to 5 scale; cell colour shows the score band of the register."""
    rows = read("risk_register.csv")
    fig = plt.figure(figsize=HALF)
    ax = fig.add_axes([0.12, 0.2, 0.46, 0.7])
    band = lambda s: RED if s >= 15 else (CORAL if s >= 8 else BOX_GREY)  # noqa: E731
    for li in range(1, 6):
        for im in range(1, 6):
            ax.add_patch(plt.Rectangle((im - 0.5, li - 0.5), 1, 1, fc=band(li * im), ec="white", lw=2.5))
    cells = {}
    for r in rows:
        cells.setdefault((int(r["impact"]), int(r["likelihood"])), []).append(r["id"])
    for (im, li), ids in cells.items():
        ink = "white" if li * im >= 15 else CHARCOAL
        ax.text(im, li, "\n".join(ids), ha="center", va="center", fontsize=13, weight="bold", color=ink,
                linespacing=1.1)
    ax.set_xlim(0.5, 5.5)
    ax.set_ylim(0.5, 5.5)
    ax.set_xticks(range(1, 6))
    ax.set_yticks(range(1, 6))
    ax.tick_params(length=0)
    for s in ("left", "bottom"):
        ax.spines[s].set_visible(False)
    ax.set_xlabel("Impact")
    ax.set_ylabel("Likelihood")
    ax.set_aspect("equal")
    # key: name, then owner in grey; each entry advances by the lines it uses
    line = FS_SMALL * 1.15 / 72 / HALF[1]          # one text line as a fraction of figure height
    y = 0.9
    for r in sorted(rows, key=lambda r: r["id"]):
        name = wrap_chars(r["short"], 26)
        fig.text(0.62, y, r["id"], ha="left", va="top", fontsize=FS_SMALL, weight="bold", color=CHARCOAL)
        fig.text(0.69, y, name, ha="left", va="top", fontsize=FS_SMALL, color=CHARCOAL, linespacing=1.15)
        n_name = name.count("\n") + 1
        fig.text(0.69, y - n_name * line, r["owner"], ha="left", va="top", fontsize=FS_SMALL, color=MID_GREY)
        y -= (n_name + 1) * line + 0.022
    for j, (lab, c) in enumerate([("Low (under 8)", BOX_GREY), ("Medium (8 to 14)", CORAL), ("High (15+)", RED)]):
        x = 0.12 + j * 0.27
        fig.patches.append(plt.Rectangle((x, 0.045), 0.03, 0.04, transform=fig.transFigure, fc=c, ec="none"))
        fig.text(x + 0.04, 0.065, lab, ha="left", va="center", fontsize=FS_SMALL, color=CHARCOAL)
    return save(fig, "risk_heatmap.png")


ALL = [fig_jcurve, fig_tornado, fig_balance_accounts, fig_review_causes, fig_why_now, fig_sizing_funnel,
       fig_positioning_map, fig_gtm_timeline, fig_risk_heatmap]

if __name__ == "__main__":
    for f in ALL:
        f()

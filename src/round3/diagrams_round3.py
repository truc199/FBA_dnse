"""Low-fi wireframes and the service blueprint of Payday Portfolio (Round 3A content).

Wireframes take their microcopy from data/round3/wireframe_copy.json and the blueprint its cells from
data/round3/service_blueprint.csv, so wording changes need no code change. Both are stand-ins for the
Figma versions of the slides. Colours are those of src/config.py.

Run: python src/round3/diagrams_round3.py
"""
import csv
import json
import sys
import textwrap
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "figures"))
import style  # noqa: E402,F401  (fonts and matplotlib defaults of the Round 2 figures)
from style import plt  # noqa: E402
from matplotlib.patches import FancyBboxPatch  # noqa: E402
from config import (BOX_EDGE, BOX_GREY, CHARCOAL, CORAL, DARK_RED, GREY, LIGHT_GREY, LIGHT_RED,  # noqa: E402
                    MID_GREY, RED)

sys.path.insert(0, str(Path(__file__).resolve().parent))
from payday_model import DATA_R3  # noqa: E402
from figures_round3 import save  # noqa: E402

PEACH_TINT = "#FCE6D8"      # light tint of the brand peach, for warnings
RED_TINT = "#FBE4E7"        # light tint of DNSE red, for failure handling
ALLOC_COLOURS = [DARK_RED, RED, CORAL, LIGHT_RED]
PT = 1 / 72                 # one point in inches


def wrap(text, fs, width_in):
    """Lines of text that fit width_in at font size fs (average glyph about half an em wide)."""
    per_line = max(8, int(width_in / (0.5 * fs * PT)))
    out = []
    for para in str(text).split("\n"):
        out += textwrap.wrap(para, per_line) or [""]
    return out


def rbox(ax, x, y, w, h, r=0.06, **kw):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle=f"round,pad=0,rounding_size={r}", **kw))


# ---------------------------------------------------------------- wireframes
class Phone:
    """Draws one screen inside an axes whose units are inches, top to bottom."""

    def __init__(self, ax, w, h, scale=1.0):
        self.ax, self.w, self.h, self.s = ax, w, h, scale
        ax.set_xlim(0, w)
        ax.set_ylim(0, h)
        ax.axis("off")
        rbox(ax, 0.02, 0.02, w - 0.04, h - 0.04, r=0.18, fc="white", ec=CHARCOAL, lw=1.6)
        ax.add_patch(FancyBboxPatch((w / 2 - 0.22, h - 0.13), 0.44, 0.05, boxstyle="round,pad=0,rounding_size=0.025",
                                    fc=LIGHT_GREY, ec="none"))
        self.x0, self.x1 = 0.17, w - 0.17
        self.y = h - 0.28
        self.fs = {"title": 9.4 * scale, "text": 7.8 * scale, "note": 7.0 * scale, "chip": 7.0 * scale,
                   "button": 7.8 * scale}
        ax.text(self.x0, self.y, "DNSE  ·  Payday Portfolio", fontsize=self.fs["note"], color=GREY, va="top")
        self.y -= 0.2 * scale

    @property
    def width(self):
        return self.x1 - self.x0

    def lines(self, text, kind, color=CHARCOAL, weight="normal", x=None, width=None, gap=0.07):
        fs = self.fs[kind]
        ls = wrap(text, fs, (width or self.width))
        lh = fs * PT * 1.28
        self.ax.text(x or self.x0, self.y, "\n".join(ls), fontsize=fs, color=color, weight=weight, va="top",
                     linespacing=1.28)
        self.y -= lh * len(ls) + gap * self.s
        return lh * len(ls)

    def title(self, t):
        self.lines(t, "title", weight="bold", gap=0.1)

    def text(self, t):
        self.lines(t, "text")

    def note(self, t):
        self.lines(t, "note", color=MID_GREY)

    def chips(self, options, selected):
        fs = self.fs["chip"]
        h = fs * PT * 2.0
        x, y = self.x0, self.y
        for i, o in enumerate(options):
            w = len(o) * 0.5 * fs * PT + 0.16 * self.s
            if x + w > self.x1:
                x, y = self.x0, y - h - 0.05 * self.s
            sel = i == selected
            rbox(self.ax, x, y - h, w, h, r=h / 2, fc=RED if sel else "white", ec=RED if sel else GREY, lw=1)
            self.ax.text(x + w / 2, y - h / 2, o, fontsize=fs, ha="center", va="center",
                         color="white" if sel else CHARCOAL)
            x += w + 0.05 * self.s
        self.y = y - h - 0.1 * self.s

    def field(self, label, value):
        self.lines(label, "note", color=MID_GREY, gap=0.02)
        fs = self.fs["text"]
        h = fs * PT * 2.1
        rbox(self.ax, self.x0, self.y - h, self.width, h, r=0.04, fc="white", ec=GREY, lw=1)
        self.ax.text(self.x0 + 0.07, self.y - h / 2, value, fontsize=fs, va="center", color=CHARCOAL)
        self.y -= h + 0.09 * self.s

    def card(self, t, fc=BOX_GREY, ec="none"):
        fs = self.fs["text"]
        ls = wrap(t, fs, self.width - 0.16)
        h = fs * PT * 1.28 * len(ls) + 0.14
        rbox(self.ax, self.x0, self.y - h, self.width, h, r=0.05, fc=fc, ec=ec, lw=1)
        self.ax.text(self.x0 + 0.08, self.y - 0.07, "\n".join(ls), fontsize=fs, va="top", color=CHARCOAL,
                     linespacing=1.28)
        self.y -= h + 0.09 * self.s

    def banner(self, t, kind):
        self.card(t, fc=PEACH_TINT if kind == "warning" else BOX_GREY, ec=CORAL if kind == "warning" else MID_GREY)

    def alloc(self, parts):
        h = 0.13 * self.s
        x = self.x0
        for (lab, pct), c in zip(parts, ALLOC_COLOURS):
            w = self.width * pct / 100
            self.ax.add_patch(plt.Rectangle((x, self.y - h), w - 0.015, h, fc=c, ec="none"))
            x += w
        self.y -= h + 0.08 * self.s
        for (lab, pct), c in zip(parts, ALLOC_COLOURS):
            self.ax.add_patch(plt.Rectangle((self.x0, self.y - 0.075 * self.s), 0.075 * self.s, 0.075 * self.s, fc=c, ec="none"))
            self.lines(f"{pct}%  {lab}", "note", x=self.x0 + 0.12 * self.s, width=self.width - 0.12, gap=0.025)
        self.y -= 0.05 * self.s

    def steps(self, items):
        for i, t in enumerate(items, 1):
            self.lines(f"{i}.  {t}", "text", gap=0.03)
        self.y -= 0.05 * self.s

    def progress(self, label, frac):
        self.lines(label, "text", gap=0.04)
        h = 0.08 * self.s
        rbox(self.ax, self.x0, self.y - h, self.width, h, r=h / 2, fc=LIGHT_GREY, ec="none")
        rbox(self.ax, self.x0, self.y - h, max(h, self.width * frac), h, r=h / 2, fc=RED, ec="none")
        self.y -= h + 0.1 * self.s

    def badge(self, t):
        fs = self.fs["chip"]
        h = fs * PT * 2.0
        w = len(t) * 0.5 * fs * PT + 0.2 * self.s
        rbox(self.ax, self.x0, self.y - h, w, h, r=h / 2, fc="white", ec=RED, lw=1.2)
        self.ax.text(self.x0 + w / 2, self.y - h / 2, t, fontsize=fs, ha="center", va="center", color=CHARCOAL,
                     weight="bold")
        self.y -= h + 0.09 * self.s

    def button(self, t, kind):
        fs = self.fs["button"]
        h = fs * PT * 2.4
        if kind == "tertiary":
            self.ax.text(self.w / 2, self.y - h / 2, t, fontsize=fs, ha="center", va="center", color=RED)
        else:
            rbox(self.ax, self.x0, self.y - h, self.width, h, r=h / 2, fc=RED if kind == "primary" else "white",
                 ec=RED, lw=1.3)
            self.ax.text(self.w / 2, self.y - h / 2, t, fontsize=fs, ha="center", va="center", weight="bold",
                         color="white" if kind == "primary" else RED)
        self.y -= h + 0.07 * self.s

    def draw(self, elements):
        for el in elements:
            kind, args = el[0], el[1:]
            getattr(self, kind)(*args)


def strip(screens, name, phone_w, phone_h, scale, fig_w=12.0, fig_h=5.5):
    """Phones side by side with a caption under each."""
    fig = plt.figure(figsize=(fig_w, fig_h))
    n = len(screens)
    gap = (fig_w - n * phone_w) / (n + 1)
    bottom = 0.5
    for i, sc in enumerate(screens):
        left = gap + i * (phone_w + gap)
        ax = fig.add_axes([left / fig_w, bottom / fig_h, phone_w / fig_w, phone_h / fig_h])
        Phone(ax, phone_w, phone_h, scale).draw(sc["elements"])
        fig.text((left + phone_w / 2) / fig_w, (bottom - 0.12) / fig_h, sc["caption"], ha="center", va="top",
                 fontsize=12, weight="bold", color=CHARCOAL)
    return save(fig, name, dpi=400)


def fig_wireframes():
    copy = json.loads((DATA_R3 / "wireframe_copy.json").read_text(encoding="utf-8"))
    a = strip(copy["main"], "wireframes_journey.png", phone_w=1.82, phone_h=4.75, scale=1.0)
    b = strip(copy["errors"], "wireframes_errors.png", phone_w=2.3, phone_h=4.75, scale=1.12)
    return a, b


# ---------------------------------------------------------------- service blueprint
LANE_STYLE = {
    "Physical evidence": dict(fc="white", ec=LIGHT_GREY),
    "Customer actions": dict(fc=BOX_GREY, ec=BOX_EDGE),
    "Frontstage": dict(fc="white", ec=RED),
    "Backstage": dict(fc=BOX_GREY, ec=BOX_EDGE),
    "Support processes": dict(fc="white", ec=GREY),
    "Decision point": dict(fc="white", ec=DARK_RED),
    "If it fails": dict(fc=RED_TINT, ec=CORAL),
    "Owner": None,
}
LINES_AFTER = {"Customer actions": "Line of interaction", "Frontstage": "Line of visibility",
               "Backstage": "Line of internal interaction"}


def fig_service_blueprint():
    with open(DATA_R3 / "service_blueprint.csv", encoding="utf-8-sig") as f:
        rows = list(csv.DictReader(f))
    steps = [k for k in rows[0] if k != "lane"]
    W, H = 13.33, 7.5
    fig = plt.figure(figsize=(W, H))
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, W)
    ax.set_ylim(0, H)
    ax.axis("off")
    label_w, left, right, top = 1.45, 0.12, 0.1, 0.12
    col_w = (W - left - label_w - right) / len(steps)
    fs, head_fs = 9.6, 11.5
    pad = 0.06
    # header
    y = H - top
    for j, s in enumerate(steps):
        x = left + label_w + j * col_w
        ax.text(x + col_w / 2, y - 0.17, s, ha="center", va="center", fontsize=head_fs, weight="bold", color=CHARCOAL)
        if j < len(steps) - 1:
            ax.annotate("", xy=(x + col_w + 0.02, y - 0.17), xytext=(x + col_w - 0.18, y - 0.17),
                        arrowprops=dict(arrowstyle="-|>", lw=1.3, color=CHARCOAL))
    y -= 0.42
    for r in rows:
        lane = r["lane"]
        texts = [r[s] for s in steps]
        n_lines = max(len(wrap(t, fs, col_w - 2 * pad - 0.1)) for t in texts)
        row_h = n_lines * fs * PT * 1.25 + 0.16
        if lane == "Owner":
            row_h = fs * PT * 1.25 * max(len(wrap(t, fs - 0.6, col_w - 0.1)) for t in texts) + 0.1
        ax.text(left, y - row_h / 2, lane, ha="left", va="center", fontsize=10.5, weight="bold", color=CHARCOAL)
        for j, t in enumerate(texts):
            x = left + label_w + j * col_w
            st = LANE_STYLE[lane]
            if st:
                rbox(ax, x + 0.04, y - row_h + 0.03, col_w - 0.08, row_h - 0.06, r=0.06, lw=1.4, **st)
            ls = wrap(t, fs - (0.6 if lane == "Owner" else 0), col_w - 2 * pad - 0.1)
            ax.text(x + col_w / 2, y - row_h / 2, "\n".join(ls), ha="center", va="center",
                    fontsize=fs - (0.6 if lane == "Owner" else 0), color=MID_GREY if lane == "Owner" else CHARCOAL,
                    style="italic" if lane == "Owner" else "normal", linespacing=1.25)
        y -= row_h
        if lane in LINES_AFTER:
            ax.plot([left, W - right], [y - 0.02, y - 0.02], color=GREY, lw=1.0, ls=(0, (4, 3)))
            ax.text(W - right, y - 0.05, LINES_AFTER[lane], ha="right", va="top", fontsize=8.5, color=MID_GREY,
                    style="italic")
            y -= 0.17
        else:
            y -= 0.03
    return save(fig, "service_blueprint.png")


# ---------------------------------------------------------------- deck diagrams (Phase 3.2)
FS_D, FS_D_HEAD = 12, 13        # smallest text and box titles at slide size


def read_out(name):
    from payday_model import TABLES_R3
    with open(TABLES_R3 / name, encoding="utf-8-sig") as f:
        return list(csv.DictReader(f))


def fig_solution_overview():
    """How Payday works in four steps, with the persistence package and the trust controls (slide 7)."""
    spec = json.loads((DATA_R3 / "solution_overview.json").read_text(encoding="utf-8"))
    W, H = 12.0, 3.7
    fig = plt.figure(figsize=(W, H))
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, W)
    ax.set_ylim(0, H)
    ax.axis("off")
    n, gap, left = len(spec["steps"]), 0.32, 0.06
    bw = (W - 2 * left - (n - 1) * gap) / n
    top, bh = H - 0.06, 1.95
    for i, st in enumerate(spec["steps"]):
        x = left + i * (bw + gap)
        rbox(ax, x, top - bh, bw, bh, r=0.1, fc=BOX_GREY, ec=RED if i == 0 else BOX_EDGE, lw=1.8)
        ax.text(x + bw / 2, top - 0.2, st["title"], ha="center", va="top", fontsize=FS_D_HEAD, weight="bold",
                color=CHARCOAL)
        ax.text(x + bw / 2, top - 0.62, "\n".join(st["lines"]), ha="center", va="top", fontsize=FS_D,
                color=CHARCOAL, linespacing=1.2)
        if i < n - 1:
            ax.annotate("", xy=(x + bw + gap - 0.03, top - bh / 2), xytext=(x + bw + 0.03, top - bh / 2),
                        arrowprops=dict(arrowstyle="-|>", lw=1.6, color=CHARCOAL, mutation_scale=16))
    by, bh2 = 0.06, top - bh - 0.2 - 0.06
    half = (W - 2 * left - gap) / 2
    for j, band in enumerate(spec["bands"]):
        x = left + j * (half + gap)
        rbox(ax, x, by, half, bh2, r=0.1, fc="white", ec=RED if j == 0 else PEACH_EDGE, lw=1.8)
        ax.text(x + 0.2, by + bh2 - 0.16, band["title"], ha="left", va="top", fontsize=FS_D_HEAD, weight="bold",
                color=CHARCOAL)
        items = band["items"]
        per_col = (len(items) + 1) // 2
        col_w = (half - 0.4) / 2
        chars = int(col_w / (0.47 * FS_D * PT))
        for c in range(2):
            y_item = by + bh2 - 0.55
            for item in items[c * per_col:(c + 1) * per_col]:
                lines = textwrap.wrap("• " + item, chars, subsequent_indent="   ")
                ax.text(x + 0.2 + c * (col_w + 0.1), y_item, "\n".join(lines), ha="left", va="top", fontsize=FS_D,
                        color=CHARCOAL, linespacing=1.15)
                y_item -= len(lines) * FS_D * PT * 1.15 + 0.08
    return save(fig, "solution_overview.png")


PEACH_EDGE = "#F4A06E"


def diamond(ax, x, y, s, fc=CHARCOAL):
    from matplotlib.patches import Polygon
    ax.add_patch(Polygon([(x, y + s), (x + s * 0.62, y), (x, y - s), (x - s * 0.62, y)], closed=True, fc=fc,
                         ec="white", lw=1.5, zorder=4))


def fig_roadmap():
    """Payday's five gated phases over 36 months, above DNSE's balance-first product roadmap (slide 13)."""
    phases = read_out("roadmap_phases.csv")
    eco = read_out("ecosystem_roadmap.csv")
    W, H = 12.0, 3.0
    fig = plt.figure(figsize=(W, H))
    ax = fig.add_axes([0.13, 0.27, 0.85, 0.72])
    ax.set_xlim(0, 36)
    ax.set_ylim(0, 4.0)
    ax.axis("off")
    names = {"0": "0  Build", "1": "1  Pilot", "2": "2  Scale in the base", "3": "3  Outside channels",
             "4": "4  Optimise"}
    results = {"1": f"{float(phases[1]['savers_enrolled_by_end']):,.0f} savers",
               "2": f"{float(phases[2]['funded_savers_at_end']):,.0f} funded",
               "3": f"{float(phases[3]['new_accounts_above_10m_at_end']):,.0f} new accounts above VND 10m",
               "4": f"{float(phases[4]['new_accounts_above_10m_at_end']):,.0f} new accounts above VND 10m"}
    y_p, h = 2.55, 0.62
    for ph in phases:
        key = ph["phase"].split(":")[0].replace("Phase", "").strip()
        a, b = (int(v) for v in ph["months"].split("-"))
        a -= 1
        asked = key in ("0", "1")
        ax.add_patch(plt.Rectangle((a, y_p - h / 2), b - a, h, fc=RED if asked else MID_GREY, ec="white", lw=2.5))
        label = names[key] if b - a >= 6 else names[key].split()[0]
        ax.text(a + (b - a) / 2, y_p, label, ha="center", va="center", fontsize=FS_D, weight="bold", color="white")
        if key in results:
            ax.text(b - 0.2, y_p - h / 2 - 0.14, results[key], ha="right", va="top", fontsize=FS_D, color=CHARCOAL)
    for m, lab in [(3, "Gate 0"), (6, "Gate 1"), (12, "Gate 2"), (24, "Gate 3")]:
        diamond(ax, m, y_p + h / 2 + 0.32, 0.2)
        ax.text(m, y_p + h / 2 + 0.6, lab, ha="center", va="bottom", fontsize=FS_D, color=CHARCOAL)
    fig.text(0.125, 0.27 + 0.72 * y_p / 4.0 + 0.03, "Payday Portfolio", ha="right", va="center", fontsize=FS_D,
             weight="bold", color=CHARCOAL)
    fig.text(0.125, 0.27 + 0.72 * y_p / 4.0 - 0.055, "Red: asked now", ha="right", va="center", fontsize=FS_D,
             color=RED)
    y_e = 0.7
    for e in eco:
        a, b = int(e["start_month"]), int(e["end_month"])
        ax.add_patch(plt.Rectangle((a, y_e - h / 2), b - a, h, fc=BOX_GREY, ec="white", lw=2.5))
        ax.text(a + (b - a) / 2, y_e, e["label"], ha="center", va="center", fontsize=FS_D, weight="bold",
                color=CHARCOAL)
    fig.text(0.125, 0.27 + 0.72 * y_e / 4.0, "DNSE product\nroadmap", ha="right", va="center", fontsize=FS_D,
             weight="bold", color=CHARCOAL, linespacing=1.1)
    tx = fig.add_axes([0.13, 0.25, 0.85, 0.001])
    tx.set_xlim(0, 36)
    tx.set_xticks([0, 3, 6, 12, 24, 36])
    tx.set_yticks([])
    for s in ("left", "right", "top"):
        tx.spines[s].set_visible(False)
    tx.set_xlabel("Months after Board approval", fontsize=FS_D)
    tx.tick_params(labelsize=FS_D)
    return save(fig, "roadmap.png")


def fig_decision_tree():
    """Scale, adjust and stop branches at Gates 0 to 3, with the thresholds from the cohort model (slide 14)."""
    rows = read_out("decision_tree.csv")
    W = 12.0
    n, gap, left = len(rows), 0.36, 0.06
    cw = (W - 2 * left - (n - 1) * gap) / n
    chars = int((cw - 0.3) / (0.47 * FS_D * PT))
    line = FS_D * PT * 1.15
    texts = [(textwrap.wrap(r["checks"], chars), textwrap.wrap("Scale: " + r["scale"], chars)) for r in rows]
    node_h = max(0.42 + (len(c) + len(s)) * line + 0.22 for c, s in texts)
    branch_h = max(sum(len(textwrap.wrap(f"{k}: {r[k.lower()]}", chars)) * FS_D * PT * 1.18 + 0.3
                       for k in ("Adjust", "Stop")) for r in rows)
    H = 0.06 + node_h + 0.14 + branch_h + 0.08
    fig = plt.figure(figsize=(W, H))
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, W)
    ax.set_ylim(0, H)
    ax.axis("off")
    node_top = H - 0.06
    for i, (r, (checks, scale)) in enumerate(zip(rows, texts)):
        x = left + i * (cw + gap)
        rbox(ax, x, node_top - node_h, cw, node_h, r=0.08, fc="white", ec=CHARCOAL, lw=1.8)
        ax.text(x + 0.15, node_top - 0.14, f"{r['gate']} · month {r['month']}", ha="left", va="top",
                fontsize=FS_D_HEAD, weight="bold", color=CHARCOAL)
        ax.text(x + 0.15, node_top - 0.44, "\n".join(checks), ha="left", va="top", fontsize=FS_D, color=MID_GREY,
                linespacing=1.15)
        ax.text(x + 0.15, node_top - 0.44 - len(checks) * line - 0.1, "\n".join(scale), ha="left", va="top",
                fontsize=FS_D, color=CHARCOAL, linespacing=1.15)
        if i < n - 1:
            ax.annotate("", xy=(x + cw + gap - 0.03, node_top - node_h / 2), xytext=(x + cw + 0.03, node_top - node_h / 2),
                        arrowprops=dict(arrowstyle="-|>", lw=1.8, color=CHARCOAL, mutation_scale=16))
        y = node_top - node_h - 0.14
        for kind, text, fc, ec in [("Adjust", r["adjust"], PEACH_TINT, PEACH_EDGE), ("Stop", r["stop"], RED_TINT, RED)]:
            lines = textwrap.wrap(f"{kind}: {text}", chars)
            bh = len(lines) * FS_D * PT * 1.18 + 0.2
            ax.plot([x + 0.3, x + 0.3], [y + 0.14, y], color=GREY, lw=1.0)
            rbox(ax, x, y - bh, cw, bh, r=0.08, fc=fc, ec=ec, lw=1.4)
            ax.text(x + 0.15, y - 0.1, "\n".join(lines), ha="left", va="top", fontsize=FS_D, color=CHARCOAL,
                    linespacing=1.18)
            y -= bh + 0.1
    return save(fig, "decision_tree.png")


ALL = [fig_wireframes, fig_service_blueprint, fig_solution_overview, fig_roadmap, fig_decision_tree]

if __name__ == "__main__":
    for f in ALL:
        f()

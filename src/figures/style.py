"""Matplotlib defaults for the report figures, and the size at which each figure is printed."""
import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import font_manager
from PIL import Image

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from config import *  # noqa: F401,F403  (paths and palette)
from config import FIGURES, FONTS, CHARCOAL, GRID

_installed = {f.name for f in font_manager.fontManager.ttflist}
FONT = next((f for f in FONTS if f in _installed), "DejaVu Sans")
plt.rcParams.update({
    "font.family": FONT, "font.size": 11.5, "axes.edgecolor": "#8C8C8C", "axes.linewidth": 1.0,
    "axes.labelcolor": CHARCOAL, "xtick.color": CHARCOAL, "ytick.color": CHARCOAL, "text.color": CHARCOAL,
    "axes.spines.top": False, "axes.spines.right": False, "legend.frameon": False,
    "savefig.dpi": 200, "figure.dpi": 100,
})
DPI = 200

# Width and height of every figure as printed in the report, in EMU (360,000 EMU = 1 cm).
# save() pads each image to this aspect ratio and src/report/build_report.py inserts it at this size,
# so the rebuilt report keeps the page layout of the submitted one.
PRINT_SIZE = {
    "fig01_idle_cash_returns.png": (5581650, 2352675),
    "fig02_investor_cash_index.png": (4933950, 2009775),
    "fig03_funding_funnel.png": (5581650, 2288476),
    "fig04_market_position.png": (5762625, 2076450),
    "fig05_brokerage_vs_cost.png": (5305425, 3257550),
    "fig06_funding_structure.png": (5581650, 2514600),
    "fig07_platform_cost.png": (5581650, 2714625),
    "fig08_complaint_themes.png": (5762625, 2771775),
    "fig09_findex_segments.png": (5391150, 3067050),
    "fig10_root_cause.png": (5581650, 3572256),
    "fig11_growth_index.png": (5581650, 2455926),
    "fig12_payday_flow.png": (5581650, 3293174),
    "fig13_contribution_threshold.png": (5581650, 2400110),
    "fig14_ecosystem.png": (5581650, 3516440),
    "figB1_revenue_profit.png": (5391150, 2533650),
    "figB2_revenue_allocation.png": (5391150, 2619375),
    "figB3_yields_funding.png": (5391150, 2247900),
    "figB4_asset_composition.png": (5124450, 2743200),
    "figC1_peer_per_account.png": (5391150, 2305050),
    "figD1_rating_by_year.png": (5124450, 2343150),
    "figD2_store_ratings.png": (5124450, 2124075),
    "figE1_findex_behaviour.png": (5391150, 2428875),
    "figF1_scenarios.png": (5124450, 2447925),
    "figF2_roadmap.png": (5581650, 2238375),
}


def ygrid(ax):
    ax.grid(axis="y", color=GRID, lw=0.8)
    ax.set_axisbelow(True)


def xgrid(ax):
    ax.grid(axis="x", color=GRID, lw=0.8)
    ax.set_axisbelow(True)


def pad_to_print_ratio(path):
    """Centre the image on a white canvas with the aspect ratio of its printed size."""
    cx, cy = PRINT_SIZE[path.name]
    im = Image.open(path).convert("RGB")
    w, h = im.size
    target = cy / cx
    if h / w > target:
        size = (round(h / target), h)
    else:
        size = (w, round(w * target))
    if size != (w, h):
        canvas = Image.new("RGB", size, "white")
        canvas.paste(im, ((size[0] - w) // 2, (size[1] - h) // 2))
        im = canvas
    im.save(path, optimize=True)


def save(fig, name, tight=True, dpi=DPI):
    FIGURES.mkdir(parents=True, exist_ok=True)
    path = FIGURES / name
    if tight:
        fig.savefig(path, dpi=dpi, bbox_inches="tight", pad_inches=0.06)
    else:
        fig.savefig(path, dpi=dpi)
    plt.close(fig)
    if name in PRINT_SIZE:
        pad_to_print_ratio(path)
    print("  wrote", path.relative_to(FIGURES.parents[1]))
    return path

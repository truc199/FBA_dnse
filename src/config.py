"""Repository paths and the DNSE colour palette shared by every script."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"                 # fetched and cleaned data (written by src/pipeline)
MANUAL = DATA / "manual"             # hand-collected inputs, one CSV per source table
OUT = ROOT / "outputs"
FIGURES = OUT / "figures"            # every chart and diagram in the report, named by figure number
TABLES = OUT / "tables"              # every table in the report, as CSV
OUT_REPORT = OUT / "report"          # the report rebuilt by src/report/build_report.py
REPORT = ROOT / "report"             # the final report as submitted (PDF and Word)
REPORT_SRC = ROOT / "src" / "report" # report text, Word template and title-page image

# DNSE red theme. Brand colours listed by Brandfetch: coral #FB6C77, peach #FFB38E and black.
# RED is a deeper shade of the brand coral so bars and lines keep contrast on white paper.
RED = "#D7263D"          # DNSE and the main series
DARK_RED = "#8E1B2C"     # emphasis and dark series
LIGHT_RED = "#F6B9BF"    # light series and fills
CORAL = "#FB6C77"        # DNSE brand coral, third series
PEACH = "#F4A06E"        # accent series (a darker shade of the brand peach #FFB38E)
CHARCOAL = "#1A1A1A"     # text and reference lines
MID_GREY = "#6B6B6B"     # competitors and neutral series
GREY = "#9A9A9A"
LIGHT_GREY = "#CFCFCF"
BOX_GREY = "#F3F3F3"
BOX_EDGE = "#6E6E6E"
GRID = "#E6E6E6"
FONTS = ["Calibri", "Carlito", "Lato", "DejaVu Sans"]   # first installed font is used

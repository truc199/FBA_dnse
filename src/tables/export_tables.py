"""Export every numbered table of a report (.docx) to CSV.

Each table becomes outputs/tables/table_<number>_<caption>.csv, and outputs/tables/index.csv lists every
table with its caption, source note and file name. The default input is the final report in report/.

Usage:
    python src/tables/export_tables.py                     # the final report, report/FBAR2_2026_KTQT_FTUers.docx
    python src/tables/export_tables.py path/to/report.docx # any other version, such as the rebuilt one
"""
import csv
import re
import sys
from pathlib import Path

from docx import Document

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from config import REPORT, ROOT, TABLES  # noqa: E402

FINAL = REPORT / "FBAR2_2026_KTQT_FTUers.docx"
W = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"
CAPTION = re.compile(r"^Table ([A-G]?\d+)\.\s+(.*)$")


def text(e):
    return "".join(t.text or "" for t in e.iter(W + "t"))


def cell_text(tc):
    return "\n".join(text(p) for p in tc.findall(W + "p")).strip()


def slug(title, n=60):
    s = re.sub(r"[^a-z0-9]+", "_", title.lower()).strip("_")
    return s[:n].rstrip("_")


def table_rows(tbl):
    rows = []
    for tr in tbl.findall(W + "tr"):
        row = []
        for tc in tr.findall(W + "tc"):
            span = tc.find(W + "tcPr/" + W + "gridSpan") if tc.find(W + "tcPr") is not None else None
            row.append(cell_text(tc))
            if span is not None:
                row += [""] * (int(span.get(W + "val")) - 1)
        rows.append(row)
    return rows


def tables(docx):
    """Yield (number, title, rows, source note) for every captioned table, in document order."""
    els = list(Document(str(docx)).element.body.iterchildren())
    for i, e in enumerate(els):
        if e.tag != W + "tbl" or i == 0:
            continue
        m = CAPTION.match(text(els[i - 1]).strip())
        if not m:
            continue
        note = text(els[i + 1]).strip() if i + 1 < len(els) and els[i + 1].tag == W + "p" else ""
        yield m.group(1), m.group(2).strip(), table_rows(e), note if note.startswith("Source") else ""


def file_name(number, title):
    return f"table_{number}_{slug(title)}.csv"


def write_csv(path, rows):
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", newline="", encoding="utf-8") as f:
        csv.writer(f).writerows(rows)


def main(docx=FINAL, out_dir=TABLES):
    index = [["table", "caption", "file", "source_note"]]
    for number, title, rows, note in tables(docx):
        name = file_name(number, title)
        write_csv(out_dir / name, rows)
        index.append([number, title, name, note])
    write_csv(out_dir / "index.csv", index)
    print(f"  exported {len(index) - 1} tables from {Path(docx).resolve().relative_to(ROOT)} to "
          f"{out_dir.relative_to(ROOT)}")
    return index


if __name__ == "__main__":
    main(Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else FINAL)

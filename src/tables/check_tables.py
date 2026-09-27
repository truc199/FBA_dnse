"""Compare the tables recomputed from data/ (outputs/tables/computed/) with the tables of the final report
(outputs/tables/, written by export_tables.py) cell by cell, and write outputs/tables/check_tables.md.

Known differences are listed in KNOWN with their explanation. The script exits with status 1 if any other
cell differs, so it can be used as a regression test after the data or the code change.

Usage:
    python src/tables/check_tables.py
"""
import csv
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from config import ROOT, TABLES  # noqa: E402

COMPUTED = TABLES / "computed"
REPORT_MD = TABLES / "check_tables.md"

# (table, row label, column): explanation. The published values come from an earlier compilation of the
# quarterly statements; the recomputed ones add up the same statements without intermediate rounding.
KNOWN = {
    ("B1", "Interest expense plus line 24", "2021"):
        "VND 23.958 billion in the filings; adding the four quarters rounded to one decimal gives 23.9",
    ("B1", "Interest expense plus line 24", "2022"):
        "VND 172.252 billion in the filings; adding the four quarters rounded to one decimal gives 172.2",
    ("B2", "Deposits and bonds held to maturity, VND bn", "2022"):
        "VND 2,823.49 billion in the filings; the published table rounded it up",
}


def read(path):
    with open(path, encoding="utf-8") as f:
        return [[" ".join(c.split()) for c in row] for row in csv.reader(f)]


def table_id(name):
    return name.split("_")[1]


def compare(name):
    ours, theirs = read(COMPUTED / name), read(TABLES / name)
    tid = table_id(name)
    header = theirs[0]
    same, known, other = 0, [], []
    if len(ours) != len(theirs) or any(len(a) != len(b) for a, b in zip(ours, theirs)):
        other.append((tid, "(layout)", "", f"{len(theirs)} rows published, {len(ours)} computed", ""))
    for r, (a, b) in enumerate(zip(ours, theirs)):
        for c, (x, y) in enumerate(zip(a, b)):
            if x == y:
                same += 1
                continue
            key = (tid, b[0], header[c] if c < len(header) else str(c))
            entry = (tid, b[0], key[2], y, x)
            (known if key in KNOWN else other).append(entry)
    return same, known, other


def main():
    names = sorted(p.name for p in COMPUTED.glob("table_*.csv"))
    missing = [n for n in names if not (TABLES / n).exists()]
    if missing:
        sys.exit(f"published tables not found for {missing}; run src/tables/export_tables.py first")
    lines = ["# Recomputed tables against the final report", "",
             "| Table | Cells identical | Known differences | Other differences |", "|---|---|---|---|"]
    all_known, all_other, total = [], [], 0
    for n in names:
        same, known, other = compare(n)
        total += same + len(known) + len(other)
        all_known += known
        all_other += other
        lines.append(f"| {table_id(n)} | {same} | {len(known)} | {len(other)} |")
    lines += ["", f"{total} cells compared in {len(names)} tables.", ""]
    for title, rows in (("Known differences", all_known), ("Other differences", all_other)):
        lines += [f"## {title}", ""]
        if not rows:
            lines += ["None.", ""]
            continue
        lines += ["| Table | Row | Column | Published | Recomputed | Note |", "|---|---|---|---|---|---|"]
        for tid, row, col, pub, comp in rows:
            note = KNOWN.get((tid, row, col), "")
            lines.append(f"| {tid} | {row} | {col} | {pub} | {comp} | {note} |")
        lines.append("")
    REPORT_MD.write_text("\n".join(lines), encoding="utf-8")
    print(f"  {total} cells in {len(names)} tables: {len(all_known)} known differences, "
          f"{len(all_other)} other differences; see {REPORT_MD.relative_to(ROOT)}")
    for tid, row, col, pub, comp in all_other:
        print(f"    Table {tid}, {row} / {col}: published {pub!r}, recomputed {comp!r}")
    return 1 if all_other else 0


if __name__ == "__main__":
    sys.exit(main())

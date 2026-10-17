"""Builds the Word version of the Round 3A deck content for team review.

Reads docs/doc_round3/deck_content.md (15 main slides) and deck_appendix.md (Appendix A-I and references) and
writes outputs/round3/Round3A_content_KTQT_FTUers.docx: A4 landscape, one heading and one page per slide,
Word tables built from the markdown tables (which deck_tables.py writes from the CSVs), the PNG figures
embedded, and separate paragraph styles for designer notes and speaker notes. It then reopens the file and
checks the number of slide headings, tables and pictures against the markdown.

Run: python src/round3/build_content_docx.py   (after deck_tables.py, figures_round3.py, diagrams_round3.py)
"""
import re
import sys
from pathlib import Path

from docx import Document
from docx.enum.section import WD_ORIENT
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.text import WD_BREAK
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Cm, Pt, RGBColor
from PIL import Image

ROOT = Path(__file__).resolve().parents[2]
SOURCES = [ROOT / "docs" / "doc_round3" / "deck_content.md", ROOT / "docs" / "doc_round3" / "deck_appendix.md"]
OUT = ROOT / "outputs" / "round3" / "Round3A_content_KTQT_FTUers.docx"
PAGE_W, PAGE_H, MARGIN = 29.7, 21.0, 1.6      # cm, A4 landscape
USABLE_W = PAGE_W - 2 * MARGIN
RED, DARK_RED, CHARCOAL, MID_GREY = "D7263D", "8E1B2C", "1A1A1A", "6B6B6B"
FIELDS = ("Action title", "On-slide text", "Table", "Figure", "Designer notes (tiếng Việt)", "Speaker notes",
          "Sources", "Title", "Text", "Table (VND billion, base case)")
SMALL_PREFIXES = ("CSV:", "Source:", "Data:")
INLINE = re.compile(r"(\*\*[^*]+\*\*|`[^`]+`|(?<![\w*])\*[^*\s][^*]*?\*(?![\w*]))")


def shade(element_pr, fill):
    shd = OxmlElement("w:shd")
    shd.set(qn("w:val"), "clear")
    shd.set(qn("w:color"), "auto")
    shd.set(qn("w:fill"), fill)
    element_pr.append(shd)


def left_border(p_pr, colour, size=18):
    borders = OxmlElement("w:pBdr")
    left = OxmlElement("w:left")
    for k, v in (("w:val", "single"), ("w:sz", str(size)), ("w:space", "8"), ("w:color", colour)):
        left.set(qn(k), v)
    borders.append(left)
    p_pr.append(borders)


def set_font(style, size=None, bold=None, italic=None, colour=None, name="Calibri"):
    f = style.font
    f.name = name
    style.element.get_or_add_rPr().get_or_add_rFonts().set(qn("w:eastAsia"), name)
    if size:
        f.size = Pt(size)
    if bold is not None:
        f.bold = bold
    if italic is not None:
        f.italic = italic
    if colour:
        f.color.rgb = RGBColor.from_string(colour)


def setup(doc):
    sec = doc.sections[0]
    sec.orientation = WD_ORIENT.LANDSCAPE
    sec.page_width, sec.page_height = Cm(PAGE_W), Cm(PAGE_H)
    for side in ("left_margin", "right_margin", "top_margin", "bottom_margin"):
        setattr(sec, side, Cm(MARGIN))
    st = doc.styles
    set_font(st["Normal"], 10.5, colour=CHARCOAL)
    st["Normal"].paragraph_format.space_after = Pt(4)
    for name, size, colour in (("Heading 1", 18, DARK_RED), ("Heading 2", 14, DARK_RED), ("Heading 3", 12, CHARCOAL)):
        set_font(st[name], size, bold=True, colour=colour)
        st[name].paragraph_format.space_before = Pt(6)
        st[name].paragraph_format.space_after = Pt(6)
    from docx.enum.style import WD_STYLE_TYPE
    designer = st.add_style("Designer Note", WD_STYLE_TYPE.PARAGRAPH)
    designer.base_style = st["List Bullet"]
    set_font(designer, 10, italic=True, colour=MID_GREY)
    shade(designer.element.get_or_add_pPr(), "FCE6D8")
    speaker = st.add_style("Speaker Note", WD_STYLE_TYPE.PARAGRAPH)
    speaker.base_style = st["Normal"]
    set_font(speaker, 10.5, colour=CHARCOAL)
    speaker.paragraph_format.left_indent = Cm(0.4)
    p_pr = speaker.element.get_or_add_pPr()
    shade(p_pr, "F3F3F3")
    left_border(p_pr, RED)
    small = st.add_style("Source Line", WD_STYLE_TYPE.PARAGRAPH)
    small.base_style = st["Normal"]
    set_font(small, 8.5, colour=MID_GREY)
    small.paragraph_format.space_after = Pt(2)
    label = st.add_style("Field Label", WD_STYLE_TYPE.CHARACTER)
    set_font(label, bold=True, colour=DARK_RED)
    for name in ("List Bullet", "List Bullet 2", "List Number"):
        set_font(st[name], 10.5, colour=CHARCOAL)


def add_runs(p, text, style_kind=None):
    """Add text with **bold**, *italic* and `code` spans as separate runs."""
    for part in INLINE.split(text):
        if not part:
            continue
        if part.startswith("**") and part.endswith("**"):
            r = p.add_run(part[2:-2])
            r.bold = True
        elif part.startswith("`") and part.endswith("`"):
            r = p.add_run(part[1:-1])
            r.font.name = "Consolas"
            r.font.size = Pt(9)
            r.font.color.rgb = RGBColor.from_string(MID_GREY)
        elif part.startswith("*") and part.endswith("*") and len(part) > 2:
            r = p.add_run(part[1:-1])
            r.italic = True
        else:
            p.add_run(part)


def page_break(doc):
    doc.add_paragraph().add_run().add_break(WD_BREAK.PAGE)


def column_widths(rows):
    n = len(rows[0])
    lengths = [max(len(r[j]) if j < len(r) else 0 for r in rows) for j in range(n)]
    weights = [min(max(L, 6), 60) for L in lengths]
    total = sum(weights)
    return [USABLE_W * w / total for w in weights]


def add_table(doc, rows):
    n = len(rows[0])
    table = doc.add_table(rows=len(rows), cols=n)
    table.style = doc.styles["Table Grid"]
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.autofit = False
    widths = column_widths(rows)
    size = 9 if n <= 5 else 8
    for i, row in enumerate(rows):
        for j in range(n):
            cell = table.cell(i, j)
            cell.width = Cm(widths[j])
            p = cell.paragraphs[0]
            p.paragraph_format.space_after = Pt(0)
            add_runs(p, row[j] if j < len(row) else "")
            for r in p.runs:
                r.font.size = Pt(size)
                if i == 0:
                    r.bold = True
            if i == 0:
                shade(cell._tc.get_or_add_tcPr(), "F3F3F3")
    tr_pr = table.rows[0]._tr.get_or_add_trPr()
    header = OxmlElement("w:tblHeader")
    header.set(qn("w:val"), "true")
    tr_pr.append(header)
    doc.add_paragraph()
    return table


def add_figure(doc, rel_path):
    path = ROOT / rel_path
    if not path.exists():
        doc.add_paragraph(f"[missing figure: {rel_path}]", style="Source Line")
        return 0
    w, h = Image.open(path).size
    aspect = w / h
    width = 25.0 if aspect >= 2.4 else (22.0 if aspect >= 1.6 else 13.0)
    max_h = PAGE_H - 2 * MARGIN - 4.0
    if width / aspect > max_h:
        width = max_h * aspect
    doc.add_picture(str(path), width=Cm(width))
    return 1


def add_figures_side_by_side(doc, rel_paths):
    """Half-slide figures that share a slide, side by side in a borderless one-row table."""
    table = doc.add_table(rows=1, cols=len(rel_paths))
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    width = USABLE_W / len(rel_paths) - 0.4
    n = 0
    for cell, rel in zip(table.rows[0].cells, rel_paths):
        cell.width = Cm(width + 0.4)
        path = ROOT / rel
        if path.exists():
            cell.paragraphs[0].add_run().add_picture(str(path), width=Cm(width))
            n += 1
        else:
            cell.paragraphs[0].add_run(f"[missing figure: {rel}]")
    doc.add_paragraph()
    return n


def split_cells(line):
    return [c.strip().replace("\\|", "|") for c in re.split(r"(?<!\\)\|", line.strip())[1:-1]]


def convert(doc, md, first):
    lines = md.splitlines()
    i, mode, pictures, tables = 0, None, 0, 0
    while i < len(lines):
        line = lines[i]
        s = line.strip()
        if not s or s == "---" or s.startswith("<!--"):
            i += 1
            continue
        if s.startswith("|"):
            block = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                if not re.match(r"^\|[\s:|-]+\|$", lines[i].strip()):
                    block.append(split_cells(lines[i]))
                i += 1
            add_table(doc, block)
            tables += 1
            continue
        m = re.match(r"^(#{1,3}) (.+)$", s)
        if m:
            level, title = len(m.group(1)), m.group(2)
            new_page = (level == 2 and (title.startswith(("Slide ", "Appendix", "References", "Câu chuyện"))))\
                or (level == 3 and "appendix" in first)
            if new_page and doc.paragraphs:
                page_break(doc)
            doc.add_heading(title, level=min(level, 3) if level > 1 else 1)
            mode = None
            i += 1
            continue
        fm = re.match(r"^\*\*([^*]+?):\*\*\s*(.*)$", s)
        if fm and fm.group(1) in FIELDS:
            field, rest = fm.group(1), fm.group(2)
            mode = {"Designer notes (tiếng Việt)": "designer", "Speaker notes": "speaker"}.get(field)
            p = doc.add_paragraph()
            p.add_run(field + ":", style="Field Label")
            if field == "Sources":
                p.style = doc.styles["Source Line"]
            if rest:
                p.add_run(" ")
                add_runs(p, rest)
            if field == "Figure":
                paths = re.findall(r"`([^`]+\.png)`", rest)
                if len(paths) > 1:
                    pictures += add_figures_side_by_side(doc, paths)
                else:
                    for path in paths:
                        pictures += add_figure(doc, path)
            i += 1
            continue
        if s.startswith(SMALL_PREFIXES) or s.startswith("Caption:"):
            p = doc.add_paragraph(style="Source Line")
            add_runs(p, s)
            i += 1
            continue
        bm = re.match(r"^(\s*)[-*] (.+)$", line)
        if bm:
            indent = len(bm.group(1))
            style = "Designer Note" if mode == "designer" else ("List Bullet 2" if indent >= 2 else "List Bullet")
            p = doc.add_paragraph(style=style)
            add_runs(p, bm.group(2))
            i += 1
            continue
        nm = re.match(r"^\d+\. (.+)$", s)
        if nm:
            p = doc.add_paragraph(style="List Number")
            add_runs(p, nm.group(1))
            i += 1
            continue
        if s.startswith(">"):
            p = doc.add_paragraph()
            p.paragraph_format.left_indent = Cm(0.8)
            add_runs(p, s.lstrip("> ").strip())
            for r in p.runs:
                r.italic = True
            i += 1
            continue
        p = doc.add_paragraph(style="Speaker Note" if mode == "speaker" else None)
        add_runs(p, s)
        i += 1
    return pictures, tables


def title_page(doc):
    doc.add_paragraph()
    t = doc.add_paragraph()
    r = t.add_run("Round 3A content: Payday Portfolio")
    r.bold, r.font.size, r.font.color.rgb = True, Pt(28), RGBColor.from_string(DARK_RED)
    for text, size in (("KTQT FTUers · Future Business Analyst Season 6 · DNSE Securities", 14),
                       ("Content for team review before slide design (Phase 3), 17 October 2026", 12),
                       ("Main slides 1 to 15, then Appendix A to I and References. On-slide text and speaker notes "
                        "are in English; designer notes are in Vietnamese.", 11)):
        p = doc.add_paragraph()
        run = p.add_run(text)
        run.font.size = Pt(size)


def main():
    doc = Document()
    setup(doc)
    title_page(doc)
    expected = {"pictures": 0, "tables": 0}
    got = {"pictures": 0, "tables": 0}
    for path in SOURCES:
        md = path.read_text(encoding="utf-8")
        expected["pictures"] += len(re.findall(r"^\*\*Figure:\*\*.*?`[^`]+\.png`", md, flags=re.M)) + \
            len(re.findall(r"^\*\*Figure:\*\* `[^`]+\.png` (?:và|and) `[^`]+\.png`", md, flags=re.M))
        expected["tables"] += md.count("<!-- table:") + len([b for b in re.split(r"\n\s*\n", md)
                                                            if b.strip().startswith("|") and "<!-- table:" not in b])
        page_break(doc)
        pics, tabs = convert(doc, md, path.stem)
        got["pictures"] += pics
        got["tables"] += tabs
    OUT.parent.mkdir(parents=True, exist_ok=True)
    doc.save(OUT)
    check = Document(OUT)
    slides = [p.text for p in check.paragraphs if p.style.name == "Heading 2" and p.text.startswith("Slide ")]
    appendix = [p.text for p in check.paragraphs if p.style.name == "Heading 3"]
    n_pictures = len(check.element.body.findall(".//" + qn("wp:inline")))
    print(f"  wrote {OUT.relative_to(ROOT)}: {len(slides)} slide headings, {len(appendix)} appendix slides, "
          f"{len(check.tables)} tables, {n_pictures} pictures")
    problems = []
    if len(slides) != 15:
        problems.append(f"{len(slides)} slide headings, expected 15")
    layout_tables = sum(1 for t in check.tables if t.style is None or t.style.name != "Table Grid")
    if len(check.tables) - layout_tables != got["tables"] or n_pictures != got["pictures"]:
        problems.append(f"document has {len(check.tables) - layout_tables} data tables and {n_pictures} pictures; "
                        f"converter added {got['tables']} and {got['pictures']}")
    if got["pictures"] < expected["pictures"]:
        problems.append(f"{got['pictures']} pictures embedded, {expected['pictures']} expected from the markdown")
    if problems:
        print("  problems:\n    " + "\n    ".join(problems))
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())

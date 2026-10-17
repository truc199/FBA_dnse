"""Builds the Word versions of the Round 3A companion report (English and Vietnamese).

Reads docs/doc_round3/report_round3A_en.md and report_round3A_vi.md and writes
outputs/round3/Round3A_report_KTQT_FTUers_EN.docx and _VI.docx in the layout of the Round 2 report: A4 portrait,
serif text, a running header, page numbers, numbered table and figure captions with a source line, a table of
contents, hanging-indent references. Appendix tables with seven or more columns go on landscape pages. The Word tables come from the markdown tables, which deck_tables.py writes from the CSVs.

It then reopens each file and checks the headings, tables and pictures against the markdown, and asks Word
(COM, Windows only) to fill the table of contents, refresh the page numbers and export a PDF beside the
.docx. Without Word the .docx is still written; the contents then fill in when Word updates the field.

Run: python src/round3/build_report_docx.py [en|vi] [--no-toc]   (after deck_tables.py and the figure scripts)
"""
import re
import subprocess
import sys
from pathlib import Path

from docx import Document
from docx.enum.section import WD_ORIENT, WD_SECTION
from docx.enum.style import WD_STYLE_TYPE
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_BREAK
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Cm, Pt, RGBColor
from PIL import Image

sys.path.insert(0, str(Path(__file__).resolve().parent))
from build_content_docx import add_runs, shade, split_cells  # noqa: E402

ROOT = Path(__file__).resolve().parents[2]
DOCS = ROOT / "docs" / "doc_round3"
OUT_DIR = ROOT / "outputs" / "round3"
FONT, CHARCOAL, GREY, RED = "Times New Roman", "1A1A1A", "6B6B6B", "D7263D"
A4_W, A4_H, MARGIN = 21.0, 29.7, 2.5
PORTRAIT_W = A4_W - 2 * MARGIN
LANDSCAPE_W = A4_H - 2 * MARGIN
WIDE_FIGURES = ("wireframes_journey", "wireframes_errors", "service_blueprint")
WIDE_TABLE_COLUMNS = 7
LANGS = {
    "en": {
        "md": DOCS / "report_round3A_en.md", "out": OUT_DIR / "Round3A_report_KTQT_FTUers_EN.docx",
        "refs": "References", "toc": "Contents", "exec": "Executive summary", "appendices": "Appendices",
        "table": "Table", "figure": "Figure", "source": "Source:", "lang": "en-GB",
        "header": "KTQT FTUers | FBA Season 6, Round 3A companion report | DNSE Securities",
        "banner": ["FUTURE BUSINESS ANALYST SEASON 6", "ROUND 3A COMPANION REPORT"],
        "team": "Team", "date": "Date", "team_v": "KTQT FTUers", "date_v": "17 October 2026",
        "note": "Full reasoning, evidence and numbers behind the Round 3A deck. Not for submission.",
    },
    "vi": {
        "md": DOCS / "report_round3A_vi.md", "out": OUT_DIR / "Round3A_report_KTQT_FTUers_VI.docx",
        "refs": "Tài liệu tham khảo", "toc": "Mục lục", "exec": "Tóm tắt điều hành", "appendices": "Phụ lục",
        "table": "Bảng", "figure": "Hình", "source": "Nguồn:", "lang": "vi-VN",
        "header": "KTQT FTUers | FBA Season 6, báo cáo bổ trợ Vòng 3A | DNSE Securities",
        "banner": ["FUTURE BUSINESS ANALYST SEASON 6", "BÁO CÁO BỔ TRỢ VÒNG 3A"],
        "team": "Nhóm", "date": "Ngày", "team_v": "KTQT FTUers", "date_v": "17/10/2026",
        "note": "Lập luận, bằng chứng và số liệu đầy đủ đằng sau deck Vòng 3A. Không dùng để nộp.",
    },
}


# ---------------------------------------------------------------- styles and page set-up
def set_font(style, size=None, bold=None, italic=None, colour=CHARCOAL):
    f = style.font
    f.name = FONT
    rpr = style.element.get_or_add_rPr()
    fonts = rpr.get_or_add_rFonts()
    for attr in ("w:asciiTheme", "w:hAnsiTheme", "w:eastAsiaTheme", "w:cstheme"):  # theme fonts override names
        if fonts.get(qn(attr)) is not None:
            del fonts.attrib[qn(attr)]
    for attr in ("w:eastAsia", "w:cs", "w:ascii", "w:hAnsi"):
        fonts.set(qn(attr), FONT)
    if size:
        f.size = Pt(size)
    if bold is not None:
        f.bold = bold
    if italic is not None:
        f.italic = italic
    if colour:
        f.color.rgb = RGBColor.from_string(colour)


def setup(doc, cfg):
    sec = doc.sections[0]
    sec.page_width, sec.page_height = Cm(A4_W), Cm(A4_H)
    for side in ("left_margin", "right_margin", "top_margin", "bottom_margin"):
        setattr(sec, side, Cm(MARGIN))
    sec.different_first_page_header_footer = True
    st = doc.styles
    set_font(st["Normal"], 11)
    pf = st["Normal"].paragraph_format
    pf.space_after, pf.line_spacing = Pt(6), 1.08
    lang = OxmlElement("w:lang")
    lang.set(qn("w:val"), cfg["lang"])
    st["Normal"].element.get_or_add_rPr().append(lang)
    for name, size, before, after in (("Heading 1", 16, 18, 8), ("Heading 2", 13, 12, 5), ("Heading 3", 11.5, 8, 4)):
        set_font(st[name], size, bold=True, colour="000000")
        st[name].paragraph_format.space_before = Pt(before)
        st[name].paragraph_format.space_after = Pt(after)
        st[name].paragraph_format.keep_with_next = True
    for name in ("List Bullet", "List Number"):
        set_font(st[name], 11)
        st[name].paragraph_format.space_after = Pt(3)
    cap = st.add_style("Caption Line", WD_STYLE_TYPE.PARAGRAPH)
    cap.base_style = st["Normal"]
    set_font(cap, 10)
    cap.paragraph_format.space_after = Pt(2)
    cap.paragraph_format.keep_with_next = True
    src = st.add_style("Source Note", WD_STYLE_TYPE.PARAGRAPH)
    src.base_style = st["Normal"]
    set_font(src, 9, colour=GREY)
    src.paragraph_format.space_after = Pt(10)
    ref = st.add_style("Reference", WD_STYLE_TYPE.PARAGRAPH)
    ref.base_style = st["Normal"]
    set_font(ref, 9.5)
    ref.paragraph_format.left_indent = Cm(0.9)
    ref.paragraph_format.first_line_indent = Cm(-0.9)
    ref.paragraph_format.space_after = Pt(3)
    ref.paragraph_format.line_spacing = 1.0
    for name in ("TOC 1", "TOC 2"):
        try:
            set_font(st[name], 11)
        except KeyError:
            style = st.add_style(name, WD_STYLE_TYPE.PARAGRAPH)
            style.base_style = st["Normal"]
            set_font(style, 11)
            style.paragraph_format.space_after = Pt(2)
            if name == "TOC 2":
                style.paragraph_format.left_indent = Cm(0.6)


def field(paragraph, instruction, placeholder=""):
    """A complex field (page number, table of contents) that Word fills on open or on update."""
    for kind, text in (("begin", None), (None, instruction), ("separate", None), (None, placeholder), ("end", None)):
        run = paragraph.add_run()
        if kind:
            fc = OxmlElement("w:fldChar")
            fc.set(qn("w:fldCharType"), kind)
            run._r.append(fc)
        elif text is instruction:
            it = OxmlElement("w:instrText")
            it.set(qn("xml:space"), "preserve")
            it.text = instruction
            run._r.append(it)
        else:
            run.text = placeholder


def header_footer(section, cfg):
    section.header.is_linked_to_previous = False
    p = section.header.paragraphs[0]
    p.text = ""
    p.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    r = p.add_run(cfg["header"])
    r.font.size, r.font.color.rgb = Pt(9), RGBColor.from_string(GREY)
    section.footer.is_linked_to_previous = False
    f = section.footer.paragraphs[0]
    f.text = ""
    f.alignment = WD_ALIGN_PARAGRAPH.CENTER
    field(f, " PAGE ", "1")
    for r in f.runs:
        r.font.size = Pt(9.5)


def new_section(doc, cfg, landscape):
    sec = doc.add_section(WD_SECTION.NEW_PAGE)
    sec.orientation = WD_ORIENT.LANDSCAPE if landscape else WD_ORIENT.PORTRAIT
    sec.page_width, sec.page_height = (Cm(A4_H), Cm(A4_W)) if landscape else (Cm(A4_W), Cm(A4_H))
    sec.different_first_page_header_footer = False
    header_footer(sec, cfg)
    return sec


# ---------------------------------------------------------------- blocks
def page_break(doc):
    doc.add_paragraph().add_run().add_break(WD_BREAK.PAGE)


def title_page(doc, cfg, title, subtitle):
    for _ in range(5):
        doc.add_paragraph()
    for line in cfg["banner"]:
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.paragraph_format.space_after = Pt(0)
        r = p.add_run(line)
        r.bold, r.font.size = True, Pt(11)
    doc.add_paragraph()
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p.add_run(title)
    r.bold, r.font.size = True, Pt(24)
    if subtitle:
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r = p.add_run(subtitle)
        r.font.size, r.font.color.rgb = Pt(12), RGBColor.from_string(GREY)
    rule = doc.add_paragraph()
    rule.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = rule.add_run("_" * 22)
    r.font.color.rgb, r.font.size = RGBColor.from_string(RED), Pt(14)
    for label, value in ((cfg["team"], cfg["team_v"]), (cfg["date"], cfg["date_v"])):
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.paragraph_format.space_after = Pt(2)
        a = p.add_run(label + "   ")
        a.bold = True
        p.add_run(value)
    doc.add_paragraph()
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p.add_run(cfg["note"])
    r.italic, r.font.size, r.font.color.rgb = True, Pt(10), RGBColor.from_string(GREY)


def toc(doc, cfg):
    p = doc.add_paragraph()
    r = p.add_run(cfg["toc"])
    r.bold, r.font.size = True, Pt(16)
    p.paragraph_format.space_after = Pt(10)
    holder = doc.add_paragraph()
    field(holder, ' TOC \\o "1-2" \\h \\z \\u ', "Right-click and choose Update field to build the table of contents.")


def column_widths(rows, total, size):
    """Each column at least as wide as its longest word; the rest shared by the amount of text."""
    n = len(rows[0])
    cells = [[re.sub(r"[*`]", "", r[j]) if j < len(r) else "" for r in rows] for j in range(n)]
    char = 0.019 * size  # cm per character of Times at this size, with some slack for bold headers
    pad = 0.45  # left and right cell margins
    floor = [max(len(w) for c in col for w in (c.split() or [""])) * char + pad for col in cells]
    floor = [max(f, 1.0) for f in floor]
    if sum(floor) >= total:
        return [total * f / sum(floor) for f in floor]
    weight = [min(sum(len(c) for c in col) / len(col), 70) for col in cells]
    spare = total - sum(floor)
    return [f + spare * w / sum(weight) for f, w in zip(floor, weight)]


def add_table(doc, rows, total):
    n = len(rows[0])
    table = doc.add_table(rows=len(rows), cols=n)
    table.style = doc.styles["Table Grid"]
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.autofit = False
    size = 9 if n <= 4 else (8.5 if n <= 6 else 8)
    widths = column_widths(rows, total, size)
    for i, row in enumerate(rows):
        for j in range(n):
            cell = table.cell(i, j)
            cell.width = Cm(widths[j])
            p = cell.paragraphs[0]
            p.paragraph_format.space_after = Pt(0)
            p.paragraph_format.line_spacing = 1.08  # room for stacked Vietnamese diacritics
            p.paragraph_format.keep_with_next = i < 2  # caption, header and first row stay together
            add_runs(p, row[j] if j < len(row) else "")
            for r in p.runs:
                r.font.size = Pt(size)
                r.font.name = FONT if r.font.name != "Consolas" else r.font.name
                if i == 0:
                    r.bold = True
            if i == 0:
                shade(cell._tc.get_or_add_tcPr(), "F3F3F3")
    tr_pr = table.rows[0]._tr.get_or_add_trPr()
    header = OxmlElement("w:tblHeader")
    header.set(qn("w:val"), "true")
    tr_pr.append(header)
    for row in table.rows:  # keep a row on one page
        cant = OxmlElement("w:cantSplit")
        row._tr.get_or_add_trPr().append(cant)
    return table


def add_figure(doc, rel, total, max_h):
    path = ROOT / rel
    if not path.exists():
        doc.add_paragraph(f"[missing figure: {rel}]")
        return 0
    w, h = Image.open(path).size
    width = min(total, max_h * w / h)
    doc.add_picture(str(path), width=Cm(width))
    pic = doc.paragraphs[-1]
    pic.alignment = WD_ALIGN_PARAGRAPH.CENTER
    pic.paragraph_format.keep_with_next = True
    pic.paragraph_format.space_after = Pt(2)
    return 1


def caption(doc, text, label_words, align):
    """A caption line whose label ("Table 3." or "Figure 2.") is bold."""
    p = doc.add_paragraph(style="Caption Line")
    p.alignment = align
    m = re.match(rf"^\*{{0,2}}((?:{label_words}) [A-Z]?\d+\.)\*{{0,2}}\s*(.*?)\*{{0,2}}$", text.strip())
    if m:
        r = p.add_run(m.group(1) + " ")
        r.bold = True
        add_runs(p, m.group(2))
    else:
        add_runs(p, text.strip("*"))
    return p


def convert(doc, cfg, md):
    """Walk the markdown once and return counts of headings, tables and pictures added."""
    lines = md.splitlines()
    refs_title = cfg["refs"]
    labels = f"{cfg['table']}|{cfg['figure']}"
    counts = {"h1": 0, "h2": 0, "tables": 0, "pictures": 0, "refs": 0}
    in_refs, in_appendix, i, last = False, False, 0, None
    cur_w = PORTRAIT_W
    wide_open = False

    def portrait():
        nonlocal wide_open, cur_w
        if wide_open:
            new_section(doc, cfg, landscape=False)
            wide_open, cur_w = False, PORTRAIT_W

    while i < len(lines):
        s = lines[i].strip()
        if not s or s == "---":
            i += 1
            continue
        m = re.match(r"^(#{1,3}) (.+)$", s)
        if m:
            level, title = len(m.group(1)), m.group(2)
            if level == 1:
                i += 1
                continue
            portrait()
            if level == 2:
                if title.startswith((cfg["appendices"], refs_title)) or re.match(r"^1\. ", title):
                    page_break(doc)
                in_refs = title == refs_title
                in_appendix = title.startswith(cfg["appendices"])
                counts["h1"] += 1
                doc.add_heading(title, level=1)
            else:
                # an appendix whose first table is wide starts on the landscape page, heading included
                if in_appendix and first_table_columns(lines, i) >= WIDE_TABLE_COLUMNS:
                    new_section(doc, cfg, landscape=True)
                    wide_open, cur_w = True, LANDSCAPE_W
                counts["h2"] += 1
                doc.add_heading(title, level=2)
            last = None
            i += 1
            continue
        if s.startswith("<!-- table:"):
            block = []
            i += 1
            while not lines[i].strip().startswith("<!-- /table"):
                if lines[i].strip().startswith("|") and not re.match(r"^\|[\s:|-]+\|$", lines[i].strip()):
                    block.append(split_cells(lines[i]))
                i += 1
            i += 1
            add_table(doc, block, cur_w)
            counts["tables"] += 1
            last = "table"
            continue
        fm = re.match(r"^!\[((?:%s) [A-Z]?\d+\.[^\]]*)\]\((.+)\)$" % labels, s)
        if fm:
            portrait()
            wide = any(k in fm.group(2) for k in WIDE_FIGURES)
            counts["pictures"] += add_figure(doc, fm.group(2), cur_w, 16.0 if wide else 10.5)
            caption(doc, fm.group(1), labels, WD_ALIGN_PARAGRAPH.CENTER)
            last = "figure"
            i += 1
            continue
        if re.match(rf"^\*\*(?:{labels}) [A-Z]?\d+\.", s):
            # appendix tables with many columns go on a landscape page, caption included
            wants_wide = in_appendix and len(split_next_table(lines, i)) >= WIDE_TABLE_COLUMNS
            if wants_wide and not wide_open:
                new_section(doc, cfg, landscape=True)
                wide_open, cur_w = True, LANDSCAPE_W
            elif not wants_wide:
                portrait()
            p = caption(doc, s, labels, WD_ALIGN_PARAGRAPH.LEFT)
            p.paragraph_format.space_before = Pt(8)
            i += 1
            continue
        if s.startswith(cfg["source"]):
            p = doc.add_paragraph(style="Source Note")
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER if last == "figure" else WD_ALIGN_PARAGRAPH.LEFT
            add_runs(p, s)
            last = None
            i += 1
            continue
        bm = re.match(r"^- (.+)$", s)
        if bm:
            if in_refs:
                p = doc.add_paragraph(style="Reference")
                counts["refs"] += 1
            else:
                p = doc.add_paragraph(style="List Bullet")
            add_runs(p, bm.group(1))
            i += 1
            continue
        nm = re.match(r"^\d+\. (.+)$", s)
        if nm:
            p = doc.add_paragraph(style="List Number")
            add_runs(p, nm.group(1))
            i += 1
            continue
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        add_runs(p, s)
        i += 1
    return counts


def first_table_columns(lines, i):
    """Columns of the first table under the heading at line i, before the next heading (0 when none)."""
    for j in range(i + 1, len(lines)):
        if re.match(r"^#{1,3} ", lines[j].strip()):
            return 0
        if lines[j].strip().startswith("<!-- table:"):
            return len(split_next_table(lines, j - 1))
    return 0


def split_next_table(lines, i):
    """Header cells of the table block that follows line i (empty list when there is none)."""
    for j in range(i + 1, min(i + 4, len(lines))):
        if lines[j].strip().startswith("<!-- table:"):
            for k in range(j + 1, len(lines)):
                if lines[k].strip().startswith("|"):
                    return split_cells(lines[k])
    return []


def front_matter(md):
    """Title, the italic standfirst and the position where the body starts."""
    title = re.search(r"^# (.+)$", md, flags=re.M).group(1)
    return title


def build(lang):
    cfg = LANGS[lang]
    md = cfg["md"].read_text(encoding="utf-8")
    doc = Document()
    setup(doc, cfg)
    header_footer(doc.sections[0], cfg)
    title = front_matter(md)
    title_page(doc, cfg, title, "")
    page_break(doc)
    # executive summary, contents, then the body; the markdown starts with the executive summary
    exec_md, _, rest = md.partition("\n## " + cfg["exec"] + "\n")[2].partition("\n## ")
    counts = {"h1": 0, "h2": 0, "tables": 0, "pictures": 0, "refs": 0}
    part = convert(doc, cfg, f"## {cfg['exec']}\n" + exec_md)
    page_break(doc)
    toc(doc, cfg)
    body = convert(doc, cfg, "## " + rest)  # section 1 starts with its own page break
    for k in counts:
        counts[k] = part[k] + body[k]
    cfg["out"].parent.mkdir(parents=True, exist_ok=True)
    doc.save(cfg["out"])
    return cfg, md, counts


def verify(cfg, md, counts):
    check = Document(cfg["out"])
    h1 = [p.text for p in check.paragraphs if p.style.name == "Heading 1"]
    h2 = [p.text for p in check.paragraphs if p.style.name == "Heading 2"]
    n_pictures = len(check.element.body.findall(".//" + qn("wp:inline")))
    n_tables = len(check.tables)
    want_tables, want_pictures = md.count("<!-- table:"), len(re.findall(r"^!\[", md, flags=re.M))
    want_h1 = len(re.findall(r"^## ", md, flags=re.M))
    want_h2 = len(re.findall(r"^### ", md, flags=re.M))
    refs = [p for p in check.paragraphs if p.style.name == "Reference"]
    want_refs = len(re.findall(r"^- ", md.rpartition("\n## " + cfg["refs"])[2], flags=re.M))
    print(f"  wrote {cfg['out'].relative_to(ROOT)}: {len(h1)} sections, {len(h2)} subsections, {n_tables} tables, "
          f"{n_pictures} pictures, {len(refs)} references, {len(check.sections)} page sections")
    problems = []
    for what, got, want in (("sections", len(h1), want_h1), ("subsections", len(h2), want_h2),
                            ("tables", n_tables, want_tables), ("pictures", n_pictures, want_pictures),
                            ("references", len(refs), want_refs)):
        if got != want:
            problems.append(f"{what}: {got} in the document, {want} in the markdown")
    return problems


def update_toc(path):
    """Fill the table of contents and refresh page numbers through Word; export a PDF beside the scratch output."""
    pdf = path.with_suffix(".pdf")
    ps = (
        "$w = New-Object -ComObject Word.Application; $w.Visible = $false; $w.DisplayAlerts = 0\n"
        f"$d = $w.Documents.Open('{path}')\n"
        "$d.TablesOfContents | ForEach-Object { $_.Update() }\n"
        "$d.Fields.Update() | Out-Null\n"
        "$d.TablesOfContents | ForEach-Object { $_.Update() }\n"
        "$d.Save()\n"
        f"$d.SaveAs2('{pdf}', 17)\n"
        "$pages = $d.ComputeStatistics(2)\n"
        "$d.Close(0); $w.Quit()\n"
        "Write-Output \"pages=$pages\"\n"
    )
    script = Path(sys.argv[0]).resolve().parent / "_update_toc.ps1"
    script.write_text(ps, encoding="utf-8")
    try:
        res = subprocess.run(["powershell", "-NoProfile", "-ExecutionPolicy", "Bypass", "-File", str(script)],
                             capture_output=True, text=True, timeout=300)
        print("  Word:", (res.stdout or res.stderr).strip()[:200])
    except (OSError, subprocess.TimeoutExpired) as e:  # no PowerShell or Word: keep the .docx as written
        print(f"  Word not available ({type(e).__name__}); contents not filled, no PDF")
    finally:
        script.unlink(missing_ok=True)
    return pdf


def main():
    langs = [a for a in sys.argv[1:] if a in LANGS] or [lang for lang in LANGS if LANGS[lang]["md"].exists()]
    problems = []
    for lang in langs:
        cfg, md, counts = build(lang)
        problems += [f"{lang}: {p}" for p in verify(cfg, md, counts)]
        if "--no-toc" not in sys.argv:
            update_toc(cfg["out"])
    if problems:
        print("  problems:\n    " + "\n    ".join(problems))
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())

"""Title page of the final report.

The template's title page is rebuilt in place:
  * a full-page background image (src/report/assets/title_background.jpg) is anchored behind the text,
  * the title becomes the company name only, in a larger black font,
  * the subtitle is removed and the red rule under the title is shortened,
  * the details table keeps only the team name and the date.

The background is an enhanced copy of src/report/assets/title_background_source.jpg. Run this file directly
(python src/report/title_page.py) to regenerate it, or let build_report.py create it when it is missing.
"""
import sys
from pathlib import Path

from docx.oxml import parse_xml
from lxml import etree
from PIL import Image, ImageFilter

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
from config import RED, ROOT  # noqa: E402

ASSETS = HERE / "assets"
BG_SOURCE = ASSETS / "title_background_source.jpg"
BG = ASSETS / "title_background.jpg"
W = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"
A4_EMU = (7560310, 10692130)      # 21.0 x 29.7 cm
A4_PX = (2480, 3508)              # A4 at 300 dpi

TITLE = ("DNSE Securities", "Joint Stock Company")
KEEP_ROWS = ("Team", "Date")


def prepare_background(src=BG_SOURCE, out=BG):
    """Upscale the source picture to A4 at 300 dpi and sharpen it."""
    im = Image.open(src).convert("RGB")
    w, h = im.size
    c = int(round(h * 0.04))                         # trim 4% at the top and bottom
    im = im.crop((0, c, w, h - c))
    im = im.resize((im.width * 3, im.height * 3), Image.LANCZOS).filter(ImageFilter.GaussianBlur(1.6))
    im = im.resize(A4_PX, Image.LANCZOS).filter(ImageFilter.UnsharpMask(radius=2.2, percent=70, threshold=2))
    im.save(out, quality=95, subsampling=0)
    return out


def _text(e):
    return "".join(t.text or "" for t in e.iter(W + "t"))


def _black(el):
    for r in el.iter(W + "r"):
        rp = r.find(W + "rPr")
        if rp is None:
            rp = etree.Element(W + "rPr")
            r.insert(0, rp)
        for c in rp.findall(W + "color"):
            rp.remove(c)
        etree.SubElement(rp, W + "color").set(W + "val", "000000")


def _background_run(r_id, name):
    cx, cy = A4_EMU
    return parse_xml(f'''<w:r xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main"><w:drawing xmlns:wp="http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing" xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" xmlns:pic="http://schemas.openxmlformats.org/drawingml/2006/picture" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships">
<wp:anchor distT="0" distB="0" distL="0" distR="0" simplePos="0" relativeHeight="0" behindDoc="1" locked="1" layoutInCell="1" allowOverlap="1">
<wp:simplePos x="0" y="0"/>
<wp:positionH relativeFrom="page"><wp:posOffset>0</wp:posOffset></wp:positionH>
<wp:positionV relativeFrom="page"><wp:posOffset>0</wp:posOffset></wp:positionV>
<wp:extent cx="{cx}" cy="{cy}"/><wp:effectExtent l="0" t="0" r="0" b="0"/><wp:wrapNone/>
<wp:docPr id="9001" name="Title page background"/>
<wp:cNvGraphicFramePr><a:graphicFrameLocks noChangeAspect="1"/></wp:cNvGraphicFramePr>
<a:graphic><a:graphicData uri="http://schemas.openxmlformats.org/drawingml/2006/picture"><pic:pic>
<pic:nvPicPr><pic:cNvPr id="9001" name="{name}"/><pic:cNvPicPr/></pic:nvPicPr>
<pic:blipFill><a:blip r:embed="{r_id}"/><a:stretch><a:fillRect/></a:stretch></pic:blipFill>
<pic:spPr><a:xfrm><a:off x="0" y="0"/><a:ext cx="{cx}" cy="{cy}"/></a:xfrm><a:prstGeom prst="rect"><a:avLst/></a:prstGeom></pic:spPr>
</pic:pic></a:graphicData></a:graphic></wp:anchor></w:drawing></w:r>''')


def build_title_page(doc):
    """Rebuild the first page of `doc` (a python-docx Document made from the template)."""
    if not BG.exists():
        prepare_background()
    body = doc.element.body
    p0, p1, p2, p3, p4, tbl = list(body.iterchildren())[:6]
    assert _text(p2) == "From accounts to assets", "unexpected title page layout in the template"

    # 1. full-page background behind the text
    r_id, _ = doc.part.get_or_add_image(str(BG))
    p0.insert(1, _background_run(r_id, BG.name))

    # 2. competition lines moved into the clear centre of the background
    p0.find(W + "pPr").find(W + "spacing").set(W + "before", "4300")
    p1.find(W + "pPr").find(W + "spacing").set(W + "after", "900")

    # 3. title: the company name only, 36 pt
    r0 = p2.findall(W + "r")[0]
    r0.find(W + "t").text = TITLE[0]
    for tag in ("sz", "szCs"):
        r0.find(W + "rPr").find(W + tag).set(W + "val", "72")
    etree.SubElement(r0, W + "br")
    etree.SubElement(r0, W + "t").text = TITLE[1]
    p2.find(W + "pPr").find(W + "spacing").set(W + "after", "300")
    body.remove(p3)                                     # subtitle

    # 4. short red rule under the title
    rule = p4.find(W + "pPr")
    bottom = rule.find(W + "pBdr").find(W + "bottom")
    bottom.set(W + "color", RED.lstrip("#").upper())
    bottom.set(W + "sz", "16")
    rule.find(W + "spacing").set(W + "after", "900")
    ind = etree.SubElement(rule, W + "ind")
    ind.set(W + "left", "2600")
    ind.set(W + "right", "2600")

    # 5. details table: team and date only, no borders or shading, narrower
    for tr in tbl.findall(W + "tr"):
        if _text(tr.findall(W + "tc")[0]).strip() not in KEEP_ROWS:
            tbl.remove(tr)
    for side in tbl.find(W + "tblPr").find(W + "tblBorders"):
        side.set(W + "val", "none")
        side.set(W + "color", "FFFFFF")
    tbl.find(W + "tblPr").find(W + "tblW").set(W + "w", "5200")
    g = tbl.find(W + "tblGrid").findall(W + "gridCol")
    g[0].set(W + "w", "1600")
    g[1].set(W + "w", "3600")
    for tr in tbl.findall(W + "tr"):
        tcs = tr.findall(W + "tc")
        tcs[0].find(W + "tcPr").find(W + "tcW").set(W + "w", "1600")
        tcs[1].find(W + "tcPr").find(W + "tcW").set(W + "w", "3600")
        for tc in tcs:
            shd = tc.find(W + "tcPr").find(W + "shd")
            if shd is not None:
                tc.find(W + "tcPr").remove(shd)

    # 6. black text throughout
    for e in (p0, p1, p2, tbl):
        _black(e)


if __name__ == "__main__":
    print("wrote", prepare_background().relative_to(ROOT))

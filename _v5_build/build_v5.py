# -*- coding: utf-8 -*-
"""Build FBAR2 report v5 from v4 by XML surgery. Run with Python 3.13 (lxml)."""
import copy, json, os, re, shutil, sys, zipfile
from decimal import Decimal, ROUND_HALF_UP
from lxml import etree

SP = 'C:/Users/trucf/AppData/Local/Temp/claude/d--uni-FBA/935ba975-eb6c-422e-9892-d99c25ba2d00/scratchpad/'
ROOT = 'D:/uni/FBA/'
sys.path.insert(0, SP + 'build')
import content_v5 as C

PAGES = {}
if len(sys.argv) > 1 and os.path.exists(sys.argv[1]):
    PAGES = json.load(open(sys.argv[1], encoding='utf-8-sig'))['pages']
OUT_DOCX = sys.argv[2] if len(sys.argv) > 2 else SP + 'v5_draft.docx'

SRC = SP + 'v4x/'
WD = SP + 'v5x/'
if os.path.exists(WD):
    shutil.rmtree(WD)
shutil.copytree(SRC, WD)

W = 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'
R_NS = 'http://schemas.openxmlformats.org/officeDocument/2006/relationships'
A_NS = 'http://schemas.openxmlformats.org/drawingml/2006/main'
WP_NS = 'http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing'
PIC_NS = 'http://schemas.openxmlformats.org/drawingml/2006/picture'
ns = {'w': W, 'a': A_NS, 'wp': WP_NS, 'pic': PIC_NS, 'r': R_NS}
def w(tag): return '{%s}%s' % (W, tag)

tree = etree.parse(WD + 'word/document.xml')
body = tree.getroot().find(w('body'))
els = list(body)
sectPr = els[-1]
assert etree.QName(sectPr).localname == 'sectPr'

def T(e): return ''.join(e.itertext())
def is_tbl(e): return etree.QName(e).localname == 'tbl'
def pstyle(e):
    ppr = e.find(w('pPr'))
    if ppr is None: return ''
    st = ppr.find(w('pStyle'))
    return st.get(w('val')) if st is not None else ''

def find_idx(text, style=None, start=0, prefix=False):
    for i in range(start, len(els)):
        e = els[i]
        if is_tbl(e): continue
        t = T(e)
        ok = t.startswith(text) if prefix else t == text
        if ok and (style is None or pstyle(e) == style):
            return i
    raise KeyError(text)

i_exec = find_idx('Executive summary', 'Heading1')
i_toc = find_idx('Table of contents')
i_lof = find_idx('List of figures')
i_lot = find_idx('List of tables')
i_body = find_idx('1. Introduction', 'Heading1')
i_app = find_idx('Appendices', 'Heading1')
i_ref = find_idx('References', 'Heading1')

T_H1 = els[i_body]
T_H2 = els[i_body + 1]
T_P = els[i_body + 2]
T_EXEC = els[i_exec + 1]
T_TOC0 = els[i_toc + 1]
T_TOC1 = els[i_toc + 3]
T_LIST = els[i_lof + 1]
T_APPH2 = els[find_idx('Appendix A. DNSE financial data', 'Heading2')]

# ---------- text helpers ----------
def first_run(p):
    return p.find('.//' + w('r'))

def make_run(rpr, text, bold=None):
    r = etree.Element(w('r'))
    if rpr is not None:
        rp = copy.deepcopy(rpr)
        if bold is not None:
            for tag in ('b', 'bCs'):
                for x in rp.findall(w(tag)): rp.remove(x)
            if bold:
                # insert after rFonts if present
                pos = 1 if rp.find(w('rFonts')) is not None else 0
                rp.insert(pos, etree.Element(w('bCs')))
                rp.insert(pos, etree.Element(w('b')))
        r.append(rp)
    t = etree.SubElement(r, w('t'))
    t.text = text
    t.set('{http://www.w3.org/XML/1998/namespace}space', 'preserve')
    return r

def set_text(p, text, rpr=None):
    fr = first_run(p)
    if rpr is None and fr is not None:
        rpr = fr.find(w('rPr'))
    rpr = copy.deepcopy(rpr) if rpr is not None else None
    for ch in list(p):
        if etree.QName(ch).localname != 'pPr':
            p.remove(ch)
    p.append(make_run(rpr, text))
    return p

def new_par(template, text):
    p = copy.deepcopy(template)
    return set_text(p, text)

def new_par_lead(template, lead, text):
    p = copy.deepcopy(template)
    rpr = first_run(p).find(w('rPr'))
    rpr = copy.deepcopy(rpr)
    for ch in list(p):
        if etree.QName(ch).localname != 'pPr':
            p.remove(ch)
    p.append(make_run(rpr, lead + ' ', bold=True))
    p.append(make_run(rpr, text, bold=False))
    return p

def toc_line(template, label, page):
    p = copy.deepcopy(template)
    rpr = copy.deepcopy(first_run(p).find(w('rPr')))
    for ch in list(p):
        if etree.QName(ch).localname != 'pPr':
            p.remove(ch)
    r = etree.SubElement(p, w('r'))
    r.append(rpr)
    t1 = etree.SubElement(r, w('t')); t1.text = label
    t1.set('{http://www.w3.org/XML/1998/namespace}space', 'preserve')
    etree.SubElement(r, w('tab'))
    t2 = etree.SubElement(r, w('t')); t2.text = str(page)
    return p

# ---------- exhibit blocks ----------
def block_at(i):
    """caption paragraph at i, then tbl or image paragraph, then source paragraph."""
    cap, mid, src = els[i], els[i + 1], els[i + 2]
    assert T(src).startswith('Source'), (T(cap), T(src)[:40])
    return [cap, mid, src]

def fig_block(n):
    i = find_idx('Figure %s. ' % n, start=i_body, prefix=True)
    b = block_at(i)
    assert b[1].find('.//' + w('drawing')) is not None
    return b

def tbl_block(label):
    i = find_idx('Table %s. ' % label, start=i_body, prefix=True)
    b = block_at(i)
    assert is_tbl(b[1]), label
    return b

def relabel(block, caption, source=None):
    set_text(block[0], caption)
    if source is not None:
        set_text(block[2], source)
    return block

# ---------- table helpers ----------
def rows(tbl): return tbl.findall(w('tr'))
def cells(tr): return tr.findall(w('tc'))
def set_cell(tbl, r, c, text):
    tc = cells(rows(tbl)[r])[c]
    ps = tc.findall(w('p'))
    for p in ps[1:]: tc.remove(p)
    p = ps[0]
    rpr = None
    if first_run(p) is None:
        # borrow run format from a neighbouring cell in the same row
        for other in cells(rows(tbl)[r]):
            fr = first_run(other.find(w('p')))
            if fr is not None:
                rpr = fr.find(w('rPr')); break
    set_text(p, text, rpr)

def row_text(tbl, r): return [T(tc) for tc in cells(rows(tbl)[r])]
def find_row(tbl, first_cell_prefix):
    for k, tr in enumerate(rows(tbl)):
        if T(cells(tr)[0]).startswith(first_cell_prefix): return k
    raise KeyError(first_cell_prefix)
def del_row(tbl, k): tbl.remove(rows(tbl)[k])
def add_row_after(tbl, k_src, k_after, texts):
    new = copy.deepcopy(rows(tbl)[k_src])
    rows(tbl)[k_after].addnext(new)
    k_new = rows(tbl).index(new)
    for c, t in enumerate(texts): set_cell(tbl, k_new, c, t)
    return k_new

def build_table(src_block, caption, header, data, source, widths=None):
    cap = copy.deepcopy(src_block[0]); tbl = copy.deepcopy(src_block[1]); src = copy.deepcopy(src_block[2])
    trs = rows(tbl)
    hdr_t, body_t = trs[0], trs[1]
    for tr in trs: tbl.remove(tr)
    ncol = len(header)
    assert len(cells(hdr_t)) == ncol, (len(cells(hdr_t)), ncol)
    h = copy.deepcopy(hdr_t); tbl.append(h)
    for c, t in enumerate(header): set_cell(tbl, 0, c, t)
    for rdata in data:
        b = copy.deepcopy(body_t); tbl.append(b)
        k = len(rows(tbl)) - 1
        for c, t in enumerate(rdata): set_cell(tbl, k, c, t)
    if widths:
        grid = tbl.find(w('tblGrid'))
        for gc, wd in zip(grid.findall(w('gridCol')), widths): gc.set(w('w'), str(wd))
        for tr in rows(tbl):
            for tc, wd in zip(cells(tr), widths):
                tc.find(w('tcPr')).find(w('tcW')).set(w('w'), str(wd))
    set_text(cap, caption); set_text(src, source)
    return [cap, tbl, src]

# ---------- images ----------
rels_path = WD + 'word/_rels/document.xml.rels'
rels = etree.parse(rels_path)
RELNS = 'http://schemas.openxmlformats.org/package/2006/relationships'
img_counter = [0]
def add_image_block(src_block, png_path, caption, source):
    from struct import unpack
    img_counter[0] += 1
    n = img_counter[0]
    name = 'v5_fig%d.png' % n
    shutil.copy(png_path, WD + 'word/media/' + name)
    rid = 'rIdV5img%d' % n
    rel = etree.SubElement(rels.getroot(), '{%s}Relationship' % RELNS)
    rel.set('Id', rid)
    rel.set('Type', 'http://schemas.openxmlformats.org/officeDocument/2006/relationships/image')
    rel.set('Target', 'media/' + name)
    with open(png_path, 'rb') as fh:
        head = fh.read(24)
    wpx, hpx = unpack('>II', head[16:24])
    b = [copy.deepcopy(x) for x in src_block]
    imgp = b[1]
    ext = imgp.find('.//{%s}extent' % WP_NS)
    cx = int(ext.get('cx')); cy = int(round(cx * hpx / wpx))
    ext.set('cy', str(cy))
    for e2 in imgp.findall('.//{%s}ext' % A_NS):
        if e2.get('cx') is not None:
            e2.set('cx', str(cx)); e2.set('cy', str(cy))
    imgp.find('.//{%s}blip' % A_NS).set('{%s}embed' % R_NS, rid)
    dp = imgp.find('.//{%s}docPr' % WP_NS); dp.set('id', str(9000 + n)); dp.set('name', 'Picture v5 %d' % n)
    cnv = imgp.find('.//{%s}cNvPr' % PIC_NS)
    if cnv is not None: cnv.set('id', str(9000 + n)); cnv.set('name', name)
    set_text(b[0], caption); set_text(b[2], source)
    return b

NEWFIG = SP + 'newfig/'

# ---------- data for new tables ----------
DJ = json.load(open(ROOT + 'dnse_financials.json', encoding='utf-8'))
Q = DJ['quarterly']
PJ = json.load(open(ROOT + 'peer_financials.json', encoding='utf-8'))
F = PJ['firms']
def q(p, k):
    v = Q[p].get(k); return 0.0 if v is None else v
def S(ps, k): return sum(q(p, k) for p in ps)
def f1(x): return '{:,.1f}'.format(Decimal(str(x)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP))
def f0(x): return '{:,.0f}'.format(Decimal(str(x)).quantize(Decimal('1'), rounding=ROUND_HALF_UP))
def sg(x): return ('+' if x >= 0 else '−') + f1(abs(x))

def cost_parts(ps):
    rev = S(ps, 'revenue'); gains = S(ps, 'rev_fvtpl'); losses = S(ps, 'cost_fvtpl')
    prop = gains + losses; pbt = S(ps, 'pbt')
    core_rev = rev - gains; core_pbt = pbt - prop; core_cost = core_rev - core_pbt
    fund = -S(ps, 'interest_expense') - S(ps, 'cost_provision_and_loan_funding')
    bro = -S(ps, 'cost_brokerage'); adm = -S(ps, 'admin_cost')
    return dict(core_rev=core_rev, lend=S(ps, 'rev_lending'), htm=S(ps, 'rev_htm'), brev=S(ps, 'rev_brokerage'),
                core_cost=core_cost, fund=fund, bro=bro, adm=adm, other=core_cost - fund - bro - adm,
                core_pbt=core_pbt, prop=prop, pbt=pbt)
a1, b1 = cost_parts(['2025Q1', '2025Q2']), cost_parts(['2026Q1', '2026Q2'])
a2, b2 = cost_parts(['2024Q%d' % i for i in range(1, 5)]), cost_parts(['2025Q%d' % i for i in range(1, 5)])
def chg(a, b, k, share=False):
    d = b[k] - a[k]
    s = sg(d)
    if share:
        s += ' (%s%%)' % f0(d / (b['core_cost'] - a['core_cost']) * 100)
    return s
A4_ROWS = []
for label, k, sh in [('Core operating revenue', 'core_rev', False),
                     ('  of which interest on margin loans and advances', 'lend', False),
                     ('  of which interest on deposits and bonds held to maturity', 'htm', False),
                     ('  of which brokerage revenue', 'brev', False),
                     ('Core costs', 'core_cost', False),
                     ('  of which funding cost (interest expense and template line 24)', 'fund', True),
                     ('  of which direct brokerage cost', 'bro', True),
                     ('  of which administration (staff, outsourced services, depreciation)', 'adm', True),
                     ('  of which other operating items (residual)', 'other', False),
                     ('Core pre-tax profit', 'core_pbt', False),
                     ('Net proprietary result', 'prop', False),
                     ('Reported pre-tax profit', 'pbt', False)]:
    A4_ROWS.append([label.strip(), f1(a1[k]), f1(b1[k]), chg(a1, b1, k, sh), f1(a2[k]), f1(b2[k]), chg(a2, b2, k, sh)])
per100_h1 = (b1['core_cost'] - a1['core_cost']) / (b1['core_rev'] - a1['core_rev']) * 100
per100_fy = (b2['core_cost'] - a2['core_cost']) / (b2['core_rev'] - a2['core_rev']) * 100
A4_ROWS.append(['Extra core cost per VND 100 of extra core revenue', '', '', f0(per100_h1), '', '', f0(per100_fy)])

# A5 brokerage H1 2026
brk = []
for t, x in F.items():
    Qx = x['quarterly']
    try:
        r = sum((Qx[k].get('rev_brokerage') or 0) for k in ('2026Q1', '2026Q2'))
        c = -sum((Qx[k].get('cost_brokerage') or 0) for k in ('2026Q1', '2026Q2'))
    except KeyError:
        continue
    brk.append((t, r, c))
brk.append(('DNSE', S(['2026Q1', '2026Q2'], 'rev_brokerage'), -S(['2026Q1', '2026Q2'], 'cost_brokerage')))
n_brk = len(brk); n_loss = sum(1 for t, r, c in brk if r - c < 0)
top = sorted(brk, key=lambda z: -z[1])[:9]
tot_r = sum(z[1] for z in brk); tot_c = sum(z[2] for z in brk)
worst = sorted(brk, key=lambda z: z[1] - z[2])[:3]
A5_ROWS = [[t, f1(r), f1(c), sg(r - c), f0(r / c * 100) if c else 'n.a.'] for t, r, c in top]
A5_ROWS.append(['All %d brokers with filed statements' % n_brk, f1(tot_r), f1(tot_c), sg(tot_r - tot_c), f0(tot_r / tot_c * 100)])
NAMES = {'KAI': 'KAFI', 'PSI': 'PSI'}

# A6 funding and structure
def struct(Qx, der, p='2026Q2'):
    x = Qx[p]
    debt = (x.get('short_term_borrowing') or 0) + (x.get('bonds_short') or 0) + (x.get('bonds_long') or 0)
    htm = (x.get('htm_assets') or 0) + (x.get('htm_assets_long') or 0)
    return (der[p].get('funding_cost_pct'), htm / x['total_assets'] * 100, x['loans'] / x['equity'] * 100,
            (x.get('short_term_borrowing') or 0) / debt * 100)
A6_ROWS = []
for t, parent in [('DNSE', 'none'), ('VPS', 'none'), ('SSI', 'none'), ('TCBS', 'Techcombank'), ('VPBankS', 'VPBank'),
                  ('MBS', 'MB'), ('HSC', 'none'), ('Vietcap', 'none'), ('VNDirect', 'none')]:
    if t == 'DNSE': fc, h, le, st = struct(Q, DJ['derived'])
    else: fc, h, le, st = struct(F[t]['quarterly'], F[t]['derived'])
    A6_ROWS.append([t, parent, f1(fc) if fc and fc > 1 else 'n.m.', f1(h), f0(le), f0(st)])

# bank-owned share of lending growth in Q2 2026 (filings)
bank = ['TCBS', 'VPBankS', 'MBS', 'BSI', 'CTS', 'AGR', 'LPS', 'ABW']
tot_d = b_d = 0.0
for t, x in F.items():
    Qx = x['quarterly']
    try: d = (Qx['2026Q2']['loans'] or 0) - (Qx['2026Q1']['loans'] or 0)
    except KeyError: continue
    tot_d += d; b_d += d if t in bank else 0
tot_d += q('2026Q2', 'loans') - q('2026Q1', 'loans')
bank_share = b_d / tot_d * 100

# industry totals (filings)
TOT = PJ['totals']['2026Q2']
tot_loans, tot_cash, tot_pbt = TOT['loans'], TOT['customer_cash_trading'], TOT['pbt']
n_loans_firms = TOT.get('firms_reporting_loans')

# scenario per-saver fix
def per_saver(n, m, r, yld, use):
    assets = n * m * r * 18 / 1e6  # VND trillion
    fees = assets * yld * 1000      # VND billion
    lend = assets * use * 0.0488 * 1000
    return fees, lend, (fees + lend) * 1e9 / n / 1000  # VND thousand
cons = per_saver(60000, 1.5, 0.6, 0.005, 0.10)
base = per_saver(150000, 2.5, 0.7, 0.008, 0.15)
upsd = per_saver(300000, 3.5, 0.8, 0.010, 0.20)

REPORT = {'A4': A4_ROWS, 'A5': A5_ROWS, 'A6': A6_ROWS, 'n_brk': n_brk, 'n_loss': n_loss,
          'worst': worst, 'bank_share': bank_share, 'tot': [tot_loans, tot_cash, tot_pbt, n_loans_firms],
          'per_saver': [cons, base, upsd], 'per100': [per100_h1, per100_fy]}
json.dump(REPORT, open(SP + 'build/new_tables.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1, default=str)

# ======================= ASSEMBLY =======================
# resolve every exhibit block BEFORE any caption is renamed
_TB = {k: tbl_block(k) for k in [1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27,
                                  'A1', 'A2', 'A3', 'B1', 'B3', 'C1', 'C2', 'C3', 'C4', 'D1', 'D2', 'D3', 'E1', 'E2', 'E3', 'F1']}
_FB = {k: fig_block(k) for k in [1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12, 14, 15, 18, 19, 21, 22, 24, 25, 26, 27]}
def tbl_block(label): return _TB[label]
def fig_block(n): return _FB[n]
new = []
# cover
new += els[:i_exec + 1]
# executive summary
for t in C.EXEC_SUMMARY:
    new.append(new_par(T_EXEC, t))
# placeholders for TOC/LOF/LOT, filled after we know captions
toc_head, lof_head, lot_head = els[i_toc], els[i_lof], els[i_lot]
new.append(toc_head); TOC_POS = len(new)
new.append(lof_head); LOF_POS = len(new)
new.append(lot_head); LOT_POS = len(new)

# ---- body ----
bf_src = {'shares': fig_block(2), 'peers': fig_block(6), 'core': fig_block(7), 'brokerage': fig_block(9)}
body_new = []
for blk in C.BODY:
    kind = blk[0]
    if kind == 'h1':
        body_new.append(new_par(T_H1, blk[1]))
    elif kind == 'h2':
        body_new.append(new_par(T_H2, blk[1]))
    elif kind == 'p':
        body_new.append(new_par(T_P, blk[1]))
    elif kind == 'pb':
        body_new.append(new_par_lead(T_P, blk[1], blk[2]))
    elif kind == 'fig':
        cap, src = C.BODY_FIGS[blk[1]]
        if blk[1] == 'shares':
            body_new += add_image_block(bf_src['shares'], NEWFIG + 'fig_shares.png', cap, src)
        else:
            body_new += relabel(bf_src[blk[1]], cap, src)
new += body_new

# ---- appendices ----
app = [els[i_app]]
def app_h2(text): return new_par(T_APPH2, text)
def app_p(text): return new_par(T_P, text)

# Appendix A
app.append(app_h2('Appendix A. Exhibits for the findings'))
app.append(app_p('Appendix A holds the figures and tables behind Section 2, in the order in which the text cites them.'))
b = tbl_block(1); app += relabel(b, 'Table A1. DNSE at a glance', "Source: DNSE filings retrieved from Vietcap's data service; DNSE investor relations and product pages; DNSE (2026d); Vietstock (2026a, 2026b, 2026f); CafeF (2026c); Kinh tế Chứng khoán (2026) for ownership; Market Times (2026). Figures at 30 June 2026 unless stated.")
b = tbl_block(2); app += relabel(b, 'Table A2. Evidence base',
                                 'Source: compiled by the authors. Access dates between 20 and 27 September 2026. Full addresses in Appendix H.')
b = fig_block(1); app += relabel(b, 'Figure A1. DNSE customer accounts and derivatives brokerage share', "Source: DNSE's 2025 annual report (DNSE, 2026d) for year-end accounts; VnExpress (2025) and Vietstock (2026c) for June 2025 and March 2026; DNSE releases for mid-2026; Hanoi Stock Exchange (2026) for derivatives brokerage shares since DNSE entered the top ten in the first quarter of 2024.")
app += add_image_block(fig_block(3), NEWFIG + 'fig_ratios.png',
                       'Figure A2. Value of an average DNSE account relative to the average Vietnamese securities account',
                       "Source: as for Figure 1. Each value is DNSE's share of a market divided by its share of securities accounts, 12.7 per cent (1,512,920 of 11,871,933 accounts at the end of 2025; 12.66 per cent at 30 June 2026). Light bars span the two industry totals in Table D1.")
b = fig_block(4); app += relabel(b, 'Figure A3. DNSE investor cash, margin lending and customer assets per account')
b = tbl_block(5)
t5 = b[1]
k = find_row(t5, 'Investor cash per account')
for c, v in enumerate(['Investor cash per account, VND million', '1.15', '1.1', '5.5', '9.3']): set_cell(t5, k, c, v)
app += relabel(b, 'Table A3. DNSE against three named peers with similar account bases',
               "Source: each firm's filed statements for the second quarter of 2026, retrieved through Vietcap Securities (2026), for lending, profit and investor cash; company releases for accounts (Vietstock, 2026d; TCBS, 2026c; VPS Securities, 2025); HOSE quarterly announcement for brokerage share; authors' calculations. Account figures are dated May 2026 (VPBankS), end-2025 (TCBS), September 2025 (VPS, from its IPO presentation) and mid-2026 (DNSE). VPS figures are filed under the ticker VCK. Per-account values are averages, which large clients raise at every firm. Investor cash is the off-balance-sheet cash each firm reports; bank-linked account models keep part of customers' cash at the parent bank, so this row is the least comparable.")
b = fig_block(14); app += relabel(b, "Figure A4. Themes in DNSE's negative reviews, by count and by helpful votes",
                                  "Source: Google Play, retrieved 23 September 2026; authors' cleaning and coding. 278 negative reviews carrying 1,794 helpful votes.")
b = fig_block(15); app += relabel(b, 'Figure A5. DNSE reviews per month, positive above the axis and negative below',
                                  "Source: Google Play, retrieved 23 September 2026; authors' cleaning and coding.")
b = fig_block(8); app += relabel(b, 'Figure A6. Composition of DNSE operating revenue')
b = fig_block(10); app += relabel(b, 'Figure A7. Where each VND 100 of operating revenue goes')
app += build_table(tbl_block('A1'), "Table A4. Where DNSE's extra revenue and cost came from (VND billion)",
                   ['Item', 'H1 2025', 'H1 2026', 'Change', '2024', '2025', 'Change'], A4_ROWS,
                   "Source: DNSE filed statements via Vietcap Securities (2026); authors' calculations. Core excludes gains and losses on financial assets at fair value through profit or loss. Template line 24 combines loan-loss provisions with the borrowing cost of the loan book; the allowance for loan losses rose by only VND 9 to 11 billion in each half-year, so the line is mostly funding cost. Percentages are shares of the change in core costs.",
                   widths=[3106, 986, 986, 1006, 986, 986, 970])
worst_txt = '; '.join('%s (%s)' % (NAMES.get(t, t), sg(r - c)) for t, r, c in worst)
app += build_table(tbl_block(5), 'Table A5. Brokerage revenue against direct brokerage cost, first half of 2026: DNSE and the largest brokers (VND billion)',
                   ['Broker', 'Brokerage revenue', 'Direct brokerage cost', 'Result after direct cost', 'Revenue as % of direct cost'], A5_ROWS,
                   "Source: filed statements of %d brokers via Vietcap Securities (2026); authors' calculations. Brokers are the nine with the highest brokerage revenue. %d of the %d brokers made a loss after direct costs; the three largest losses were %s." % (n_brk, n_loss, n_brk, worst_txt))
b = fig_block(11); app += relabel(b, 'Figure A8. Yield on margin loans and on deposits and bonds held to maturity, against the estimated cost of funding')
b = fig_block(12); app += relabel(b, 'Figure A9. Composition of DNSE total assets')
app += build_table(tbl_block('D3'), 'Table A6. Funding cost and balance-sheet structure at 30 June 2026: DNSE and eight large brokers',
                   ['Broker', 'Parent bank', 'Estimated cost of funds, Q2 2026, %', 'Deposits and HTM bonds, % of total assets', 'Loans, % of equity', 'Short-term loans, % of borrowing'],
                   A6_ROWS,
                   "Source: filed statements via Vietcap Securities (2026); DNSE (2026a), note 8(b), for pledged assets; authors' calculations. The cost of funds is estimated with the same method for every firm: interest expense plus template line 24, less the rise in the allowance for loan losses, annualised over average borrowings and bonds. n.m.: not meaningful, as VNDirect's quarterly estimate falls below 1 per cent. At 30 June 2026 DNSE had pledged VND 4,257 billion of term deposits and bonds with a face value of VND 1,050 billion, 93 per cent of its held-to-maturity assets, as collateral for bank loans. Bank-owned brokers with filed statements (TCBS, VPBankS, MBS, BSI, CTS, Agriseco, LPBS and ABS) supplied %s per cent of the rise in lending across all filers in the second quarter of 2026; a press tally of the top 20 brokers gives 62 per cent (Vietstock, 2026g)." % f0(bank_share),
                   widths=[1500, 1400, 1530, 1650, 1400, 1546])
# Table A7 summary (old Table 6)
b = tbl_block(6); t6 = b[1]
while len(rows(t6)) > 6: del_row(t6, len(rows(t6)) - 1)
SUMM = [
    ['1. DNSE wins accounts but not money', '12.7% of accounts and 19% of 2025 openings against 2.3–3.5% of investor cash, 1.4–1.8% of lending and 0.6–0.8% of profit; 5.7% of accounts active in December 2025; assets per account down 9.5% in 2025', 'Measured and derived', 'Value is lost after the account is opened'],
    ['2. The gap is specific to DNSE', 'VPS lends 5 times and TCBS 12 times more per account; about 34% of TCBS customers trade monthly; bonus complaints in 5.6% of DNSE reviews against 0.7% at VPS', 'Measured; reviews self-selected', 'Not explained by dormant accounts, the zero-fee app model or the lack of a parent bank'],
    ['3. Revenue grows while core profit stands still', 'Revenue 3.2 times from 2022 to 2025; core profit VND 128–221 billion a year; VND 102 of extra cost per VND 100 of extra core revenue in H1 2026', 'Measured', 'Growth in activity does not create value on its own'],
    ['4. Brokerage and funding absorb the growth', '52% of the H1 2026 rise in core costs from funding, 42% from brokerage, 6% from administration; brokerage below direct cost for 16 quarters and the largest brokerage loss among 42 brokers', 'Measured', 'Cost action must target per-trade costs and funding structure, not overheads'],
    ['5. Capital is not the constraint', 'Loans at 116% of equity against a 200% ceiling; 38% of assets in deposits and bonds, 93% of them pledged, earning about their funding cost', 'Measured', 'The binding constraint is customer money'],
]
for r_i, rowv in enumerate(SUMM, start=1):
    for c, v in enumerate(rowv): set_cell(t6, r_i, c, v)
app += relabel(b, 'Table A7. Summary of findings and their business implications', 'Source: Section 2.')

# Appendix B
app.append(app_h2('Appendix B. Exhibits for the discussion and recommendation'))
app.append(app_p('Appendix B holds the figures and tables behind Sections 3 and 4, in the order in which the text cites them.'))
b = tbl_block(7); t7 = b[1]
k = find_row(t7, 'Sign-up')
set_cell(t7, k, 1, '518,514 accounts in 2025; 16 to 34% of the new accounts opened in the market in each quarter of 2025')
k = find_row(t7, 'First trade and activity')
set_cell(t7, k, 1, '85,739 active users in December 2025, 5.7% of accounts, up from 41,900 a year earlier; about 34% at TCBS (Table D2)')
k = find_row(t7, 'First funding')
set_cell(t7, k, 1, 'Assets per account fell 9.5% in 2025 while accounts grew 52%; June 2025 complaints that a reward required a VND 2 million deposit')
app += relabel(b, 'Table B1. Evidence on the customer lifecycle and the gaps to close in Round 3',
               'Source: DNSE releases; Section 2; Dân trí (2026a) on the draft circular.')
b = tbl_block(8); t8 = b[1]
k = find_row(t8, 'Symptom')
set_cell(t8, k, 1, 'DNSE holds 12.7% of accounts but 2.3–3.5% of investor cash and 1.4–1.8% of margin lending, and only 5.7% of accounts were active in December 2025')
set_cell(t8, k, 2, 'Figure 1; DNSE annual report 2025')
k = find_row(t8, 'Why 1')
set_cell(t8, k, 1, 'Why do accounts stay small? Hypothesis: many customers open an account for a reward and deposit only what the reward requires')
k = find_row(t8, 'Why 2')
set_cell(t8, k, 1, 'Why do reward seekers dominate the intake? Hypothesis: incentives pay for opening an account and a minimum deposit, and marketing targets young first-time investors')
k = find_row(t8, 'Why 3')
set_cell(t8, k, 1, 'Why does money not stay after the reward? Measured: the product gives no competitive reason to keep cash on the platform')
set_cell(t8, k, 2, 'Idle cash earns 2.1 to 2.3% for a typical customer against 6.0% at TCBS iPower for the same balance (4.5% base rate) and 3.5 to 4.3% on banks\' automatic-earning accounts; no automatic saving; trading-first design')
k = find_row(t8, 'Why 4')
set_cell(t8, k, 1, "Why has the product not been built? Hypothesis: DNSE's goals and public measures centre on accounts, market share and speed")
k = find_row(t8, 'Root cause')
set_cell(t8, k, 1, 'DNSE earns through lending and trading, which need customer balances, but it measures and rewards acquisition. To be confirmed with internal targets in Round 3')
app += relabel(b, 'Table B2. Five-whys analysis of the balance gap', "Source: authors' analysis of Sections 2 and 3; Vietstock (2025c) on the Gen Z price board.")
b = fig_block(21); app += relabel(b, "Figure B1. Returns available to a Vietnamese saver's idle cash, September 2026")
b = fig_block(22); app += relabel(b, 'Figure B2. Investor cash held at brokers, indexed to the third quarter of 2025')
b = tbl_block(9); t9 = b[1]
for pref in ('Gold price index', 'Sector net interest margin', 'Households with income above'):
    del_row(t9, find_row(t9, pref))
add_row_after(t9, 1, len(rows(t9)) - 1, ["Bank-owned brokers' share of the rise in margin lending", '%s%% (all filed statements); 62%% (press tally of the top 20)' % f0(bank_share), 'Q2 2026'])
app += relabel(b, 'Table B3. Macroeconomic and banking indicators relevant to household savings, 2025 and 2026',
               'Source: National Statistics Office via Chinhphu.vn (2026) and Báo Đấu thầu (2026); State Bank of Vietnam via Diễn đàn Doanh nghiệp (2026), Thị trường Tài chính Tiền tệ (2026b), Vietstock (2026i) and VietnamPlus (2026); FiinRatings (2026); VnEconomy (2026b); VietnamNet (2026); VnExpress (2026c); Vietstock (2026g); filed statements via Vietcap Securities (2026).')
b = tbl_block(10); app += relabel(b, 'Table B4. Where Vietnamese savers keep money, mid-2026')
b = tbl_block(11); t11 = b[1]
k = find_row(t11, 'Digital wealth and fund platforms')
set_cell(t11, k, 1, 'Independent fund and savings apps')
app += relabel(b, 'Table B5. Competitive map of Vietnamese retail brokerage business models')
b = tbl_block(12); app += relabel(b, 'Table B6. Comparable business models abroad and their lessons for DNSE')
b = tbl_block(13); app += relabel(b, 'Table B7. Transferability of foreign designs to Vietnam',
                                  "Source: authors' assessment based on Table B6 and the Vietnamese regulation cited in Section 4.1.")
b = tbl_block(18); app += relabel(b, 'Table B8. Scoring of candidate target markets')
b = tbl_block(19); app += relabel(b, 'Table B9. Scope of the business problem for Round 3')
b = tbl_block(20); app += relabel(b, 'Table B10. Prioritisation of candidate business problems',
                                  "Source: authors' assessment based on Sections 2 and 3. Scores from 1 (weak) to 5 (strong). Scale anchors are annual pre-tax profit effects estimated from DNSE filings where possible.")
b = fig_block(24); app += relabel(b, 'Figure B3. What the 2026 profit plan implies for loans, equity and customer assets')
b = tbl_block(21); t21 = b[1]
set_cell(t21, find_row(t21, 'Quantified gap'), 1, 'DNSE holds 12.7% of accounts but 2.3–3.5% of investor cash, 1.4–1.8% of margin lending and 0.6–0.8% of quarterly industry profit; 5.7% of accounts were active in December 2025; assets per account fell 9.5% in 2025')
set_cell(t21, find_row(t21, 'Economic impact'), 1, 'Core pre-tax profit has stayed between VND 128 and 221 billion a year since 2022 while revenue tripled; each extra VND 100 of core revenue brought VND 102 of cost in H1 2026. Each additional VND 1 million lent per account is worth about VND 83 billion of pre-tax profit a year. The 2026 plan implies a loan book 2.3 times the current one')
set_cell(t21, find_row(t21, 'Strategic urgency'), 1, 'Deposit rates have risen about 2.5 points in 2026 and cash is leaving brokers; bank-owned brokers supplied more than half of margin growth in the second quarter; open banking interfaces become standard by March 2027, after which every competitor can link salary accounts')
app += relabel(b, 'Table B11. Business problem statement', 'Source: Sections 2 and 3.')
b = tbl_block(22); app += relabel(b, 'Table B12. Strategic alternatives assessed against the balance gap')
b = fig_block(25); app += relabel(b, 'Figure B4. How Payday Portfolio works', "Source: authors' design, drawing on Sections 2 and 3; National Assembly of Vietnam (2025) on the Personal Data Protection Law.")
b = tbl_block(23); app += relabel(b, 'Table B13. The first 90 days of a new DNSE customer, today and under Payday Portfolio')
b = tbl_block(24); t24 = b[1]
set_cell(t24, find_row(t24, 'Act in the first 90 days'), 1, 'Assets per account fell 9.5% in 2025 while accounts grew 52%; complaints cluster at identity checks and first deposits')
set_cell(t24, find_row(t24, 'Market-linked cash yield'), 1, 'DNSE pays 2.1 to 2.3% to typical customers against 6.0% at TCBS for the same balance (4.5% base) and 3.5 to 4.3% on bank auto-earning accounts; cash at brokers fell 38% in three quarters')
app += relabel(b, 'Table B14. Evidence behind each design choice', 'Source: Sections 2 and 3; TCBS (2026b); Nhân Dân (2025); VnEconomy (2025); and the sources of Table B6.')
b = tbl_block(25); t25 = b[1]
k = find_row(t25, 'Fees and lending income per saver')
for c, v in zip((1, 2, 3), (cons, base, upsd)): set_cell(t25, k, c, f0(v[2]))
app += relabel(b, 'Table B15. Illustrative outcomes of Payday Portfolio 18 months after launch')
app += add_image_block(fig_block(26), NEWFIG + 'fig_scenarios.png',
                       'Figure B5. Layer assets and annual net new money under three scenarios', 'Source: as for Table B15.')
b = tbl_block(26); app += relabel(b, 'Table B16. Feasibility conditions for Payday Portfolio')
b = tbl_block(27); app += relabel(b, 'Table B17. Assumptions, tests and measures for Round 3')
b = fig_block(27); app += relabel(b, 'Figure B6. Validation roadmap for Round 3')

# Appendix C (old A)
app.append(app_h2('Appendix C. DNSE financial data'))
app.append(new_par(T_P, "The tables below summarise the 395 line items of DNSE's filed statements used in the analysis. Annual figures are sums of quarters for flows and period-end values for balances. Every value was recomputed from the source data for this version and matches."))
b = tbl_block('A1'); app += relabel(b, 'Table C1. DNSE income statement summary, 2021 to the first half of 2026 (VND billion)')
b = tbl_block('A2'); app += relabel(b, 'Table C2. DNSE balance sheet and key ratios, 2021 to 30 June 2026')
b = tbl_block('A3'); app += relabel(b, 'Table C3. DNSE quarterly indicators, first quarter of 2024 to second quarter of 2026')

# Appendix D (old B1 rebuilt, old B3)
app.append(app_h2('Appendix D. Market and industry data'))
app.append(app_p('Table D1 lists the share measures behind Figure 1 with their denominators, including both industry totals where they differ. Table D2 compares the share of accounts that are active or funded at brokers in Vietnam and abroad that publish such a measure.'))
b = tbl_block('B1'); tb1 = b[1]
D1 = [
    ['Securities accounts, 31 December 2025', '1,512,920', '11,871,933 (VSDC)', '12.74', '1.00'],
    ['New accounts opened, 2025', '518,514', '2,681,838 (VSDC)', '19.33', '1.52'],
    ['Securities accounts, 30 June 2026', 'about 1.70 million', '13,430,517 (VSDC)', '12.66', '1.00'],
    ['Derivatives brokerage, Q2 2026', 'second place', 'HNX announcement', '25.38', '2.00'],
    ['Listed-share brokerage on HNX, Q2 2026', 'eighth place', 'HNX announcement', '2.88', '0.23'],
    ['Investor cash at brokers, 30 June 2026', 'VND 1,961 billion', 'VND 86.6 trillion (press tally); VND %s trillion (filed statements)' % f1(tot_cash / 1000), '2.26 to %.2f' % (1961 / tot_cash * 100), '0.18 to 0.27'],
    ['Margin lending, 30 June 2026', 'VND 6,303 billion', 'VND 453.8 trillion (press tally, with advances); VND %s trillion (filed statements)' % f1(tot_loans / 1000), '1.39 to %.2f' % (6303 / tot_loans * 100), '0.11 to 0.14'],
    ['Pre-tax profit, Q2 2026', 'VND 97.4 billion', 'VND 15,200 billion (77 brokers, press tally); VND %s billion (filed statements)' % f0(tot_pbt), '0.64 to %.2f' % (97.4 / tot_pbt * 100), '0.05 to 0.06'],
]
assert len(rows(tb1)) == 9, len(rows(tb1))
for r_i, rowv in enumerate(D1, start=1):
    for c, v in enumerate(rowv): set_cell(tb1, r_i, c, v)
app += relabel(b, "Table D1. DNSE's position on eight measures, 2025 to mid-2026",
               "Source: VSDC annual report 2025 and account statistics; DNSE (2026d); Hanoi Stock Exchange (2026); VnEconomy (2026b); Vietstock (2026g); CafeF (2026d); filed statements via Vietcap Securities (2026); authors' calculations. Filed-statement totals sum the brokers in Vietcap's data service, DNSE included. The ratio to account share divides each share by 12.7 per cent. HNX shares are shares of traded value on HNX only.")
b = tbl_block('B3'); app += relabel(b, 'Table D2. Share of accounts that are active or funded, brokers that publish a measure')

# Appendix E (old Table 3 + C1-C4)
app.append(app_h2('Appendix E. Customer review analysis'))
app.append(app_p('The tables below document the review cleaning, the cleaned Google Play sample, the theme coding and the cross-check against the App Store. Every count was recomputed from the cleaned files for this version and matches. Table E5 gives translated examples of the most-endorsed reviews.'))
b = tbl_block(3); app += relabel(b, 'Table E1. Review cleaning log')
b = tbl_block('C1'); app += relabel(b, 'Table E2. DNSE Google Play reviews by year after cleaning')
b = tbl_block('C2'); app += relabel(b, "Table E3. Themes in DNSE's negative Google Play reviews",
                                    'Source: as for Table E2. 278 one and two-star reviews carrying 1,794 helpful votes. Themes are not exclusive, so shares sum to more than 100.')
b = tbl_block('C3'); app += relabel(b, 'Table E4. Three applications compared on both stores')
b = tbl_block('C4'); app += relabel(b, 'Table E5. Selected DNSE reviews, translated from Vietnamese')

# Appendix F (old D1-D3 + figs 18, 19)
app.append(app_h2('Appendix F. Findex segment analysis'))
app.append(app_p('The segment analysis uses the published Findex aggregates for Vietnam, which report each indicator for twelve segments defined one dimension at a time. Table F1 defines the two indices, Table F2 reports the inputs and Table F3 the ranks under four weighting schemes. Figures F1 and F2 summarise the results used in Sections 3.2 and 3.4.'))
b = tbl_block('D1'); app += relabel(b, 'Table F1. Indicators in the two Findex indices')
b = tbl_block('D2'); app += relabel(b, 'Table F2. Findex segment indicators for Vietnam, 2024 fieldwork',
                                    'Source: World Bank (2025b); authors\' indices. Index A averages six indicators of formally held surplus and Index B six indicators of digital habit (Table F1). The gap is account ownership minus saving at a financial institution. Unconverted adults hold an account but do not save at a financial institution.')
b = tbl_block('D3'); app += relabel(b, 'Table F3. Segment ranks under four weighting schemes',
                                    "Source: authors' calculations from Table F2. Each criterion is min-max normalised across the twelve segments. Weights on (Index A, Index B, gap, unconverted adults, wage receipt, saving for old age): equal 1,1,1,1,1,1; value-heavy 3,1,1,1,2,2; scale-heavy 1,1,1,3,1,1; reach-heavy 1,3,2,1,1,1.")
b = fig_block(18); app += relabel(b, 'Figure F1. Vietnamese adult segments by digital habit and formally held investable surplus')
b = fig_block(19); app += relabel(b, 'Figure F2. Payday and saving behaviour by segment pair')

# Appendix G (old E1-E3)
app.append(app_h2('Appendix G. Methods, assumptions and limitations'))
app.append(app_p('Table G1 defines the calculated measures. Table G2 separates the assumptions behind the main results from the measured evidence, and Table G3 lists the limitations of the data together with the steps taken to contain them.'))
b = tbl_block('E1'); te1 = b[1]
set_cell(te1, find_row(te1, 'Ratio to account share'), 1, "Share of a market divided by DNSE's share of securities accounts (12.7 per cent)")
k = find_row(te1, 'Share of cash equity trading')
set_cell(te1, k, 0, 'Industry totals'); set_cell(te1, k, 1, "Reported as a range between a press tally of all brokers and the sum of the filed statements of the brokers in Vietcap's data service")
k = find_row(te1, 'Cohort decomposition')
set_cell(te1, k, 0, 'Incremental cost decomposition'); set_cell(te1, k, 1, 'Change in each core cost line between two periods as a share of the change in core costs; core excludes gains and losses on financial assets at fair value')
app += relabel(b, 'Table G1. Definitions of calculated measures')
b = tbl_block('E2'); te2 = b[1]
k = find_row(te2, 'Market totals')
for c, v in enumerate(['Market totals', 'Press tally (VND 86.6 trillion of investor cash, 453.8 trillion of lending, 15,200 billion of quarterly profit) and sum of filed statements (%s trillion, %s trillion and %s billion)' % (f1(tot_cash / 1000), f1(tot_loans / 1000), f0(tot_pbt)), 'Measured and external estimate', "DNSE's shares move between the two ends of each range; the conclusions hold at either end", 'Not needed']):
    set_cell(te2, k, c, v)
for pref in ('Allowance for HNX', 'Growth in existing customers'):
    del_row(te2, find_row(te2, pref))
app += relabel(b, 'Table G2. Register of assumptions behind the main results')
b = tbl_block('E3'); te3 = b[1]
k = find_row(te3, 'Dates differ')
set_cell(te3, k, 0, 'Dates differ across sources (peer account counts from September 2025 to May 2026; balances at 30 June 2026)')
set_cell(te3, k, 2, 'Dates stated in every note; the gaps are large enough to survive the date differences')
k = find_row(te3, 'Industry totals')
set_cell(te3, k, 0, 'Industry totals differ between press tallies and the sum of filed statements')
set_cell(te3, k, 1, "DNSE's shares vary by up to 1.2 points")
set_cell(te3, k, 2, 'Both totals reported as ranges')
del_row(te3, find_row(te3, 'Share price observed'))
app += relabel(b, 'Table G3. Limitations of the evidence')

# Appendix H (old F1)
app.append(app_h2('Appendix H. Data sources and access'))
b = tbl_block('F1'); app += relabel(b, 'Table H1. Data sources, access and dates')

new += app

# ---- references (filter to cited) ----
refs = els[i_ref + 1:len(els) - 1]
alltext = ' '.join(T(e) for e in new)
alltext = alltext.replace('VSDC', 'Vietnam Securities Depository and Clearing Corporation').replace('FINRA', 'Financial Industry Regulatory Authority').replace('AMFI', 'Association of Mutual Funds in India')
kept_refs, dropped_refs = [], []
for rp in refs:
    t = T(rp)
    m = re.match(r'^(.*?)\.\s*\((\d{4}[a-z]?|n\.d\.)', t)
    if not m:
        kept_refs.append(rp); continue
    author, year = m.group(1), m.group(2)
    first = author.split(',')[0].split('&')[0].strip()
    key_words = first.split()[0]
    if first.startswith('DNSE'): key_words = 'DNSE'
    pat = re.escape(key_words) + r'[^()]{0,80}?' + re.escape(year) + r'(?![a-z0-9])'
    pat2 = re.escape(key_words) + r'[^;]{0,60}?\(' + r'[^)]*?' + re.escape(year) + r'(?![a-z0-9])'
    if re.search(pat, alltext) or re.search(pat2, alltext):
        kept_refs.append(rp)
    else:
        dropped_refs.append(t[:90])
new.append(els[i_ref])
new += kept_refs
new.append(sectPr)

# ---- TOC, lists ----
def labels_of(elements):
    heads, figs, tabs = [], [], []
    for e in elements:
        if is_tbl(e): continue
        t = T(e); st = pstyle(e)
        if st == 'Heading1': heads.append((0, t))
        elif st == 'Heading2': heads.append((1, t))
        elif re.match(r'^Figure [0-9A-H]+\d*\. ', t) and len(t) < 200: figs.append(t)
        elif re.match(r'^Table [0-9A-H]+\d*\. ', t) and len(t) < 200: tabs.append(t)
    return heads, figs, tabs
heads, figs, tabs = labels_of(new[LOT_POS:])
heads = [(0, 'Executive summary')] + heads
def pg(label): return PAGES.get(label, '00')
toc = [toc_line(T_TOC0 if lvl == 0 else T_TOC1, lab, pg(lab)) for lvl, lab in heads]
lof = [toc_line(T_LIST, lab, pg(lab)) for lab in figs]
lot = [toc_line(T_LIST, lab, pg(lab)) for lab in tabs]
new = new[:TOC_POS] + toc + new[TOC_POS:LOF_POS] + lof + new[LOF_POS:LOT_POS] + lot + new[LOT_POS:]

# ---- write ----
for e in list(body): body.remove(e)
for e in new: body.append(e)
tree.write(WD + 'word/document.xml', xml_declaration=True, encoding='UTF-8', standalone=True)

# drop unused image relationships and media
xml = open(WD + 'word/document.xml', encoding='utf-8').read()
used = set(re.findall(r'r:embed="([^"]+)"', xml))
root = rels.getroot()
for rel in list(root):
    if rel.get('Type', '').endswith('/image') and rel.get('Id') not in used:
        tgt = rel.get('Target'); root.remove(rel)
        try: os.remove(WD + 'word/' + tgt)
        except FileNotFoundError: pass
rels.write(rels_path, xml_declaration=True, encoding='UTF-8', standalone=True)

if os.path.exists(OUT_DOCX): os.remove(OUT_DOCX)
with zipfile.ZipFile(OUT_DOCX, 'w', zipfile.ZIP_DEFLATED) as z:
    ct = WD + '[Content_Types].xml'
    z.write(ct, '[Content_Types].xml')
    for dp, dn, fn in os.walk(WD):
        for f in fn:
            full = os.path.join(dp, f)
            arc = os.path.relpath(full, WD).replace('\\', '/')
            if arc == '[Content_Types].xml': continue
            z.write(full, arc)
json.dump({'heads': heads, 'figs': figs, 'tabs': tabs, 'dropped_refs': dropped_refs},
          open(SP + 'build/labels.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('written', OUT_DOCX, 'figs', len(figs), 'tables', len(tabs), 'refs kept', len(kept_refs), 'dropped', len(dropped_refs))

# -*- coding: utf-8 -*-
"""Build v6 from the v5 docx by XML surgery: new discussion and recommendation, new figures and tables.
Usage: py -3.13 v6_build.py OUT_DOCX [PAGES_JSON]"""
import copy, json, os, re, shutil, sys, zipfile
from struct import unpack
from lxml import etree

SP = 'C:/Users/trucf/AppData/Local/Temp/claude/d--uni-FBA/731e1691-b54f-4846-bba0-f4e353828c32/scratchpad/'
SRC, WD, FIG = SP + 'v5x/', SP + 'v6x/', SP + 'v6fig/'
OUT_DOCX = sys.argv[1]
PAGES = json.load(open(sys.argv[2], encoding='utf-8-sig'))['pages'] if len(sys.argv) > 2 else {}

if os.path.exists(WD):
    shutil.rmtree(WD)
shutil.copytree(SRC, WD)

W = 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'
R_NS = 'http://schemas.openxmlformats.org/officeDocument/2006/relationships'
A_NS = 'http://schemas.openxmlformats.org/drawingml/2006/main'
WP_NS = 'http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing'
PIC_NS = 'http://schemas.openxmlformats.org/drawingml/2006/picture'
RELNS = 'http://schemas.openxmlformats.org/package/2006/relationships'
def w(tag): return '{%s}%s' % (W, tag)
XML_SPACE = '{http://www.w3.org/XML/1998/namespace}space'

tree = etree.parse(WD + 'word/document.xml')
body = tree.getroot().find(w('body'))
rels = etree.parse(WD + 'word/_rels/document.xml.rels')

def T(e): return ''.join(e.itertext())
def is_tbl(e): return etree.QName(e).localname == 'tbl'
def pstyle(e):
    ppr = e.find(w('pPr'))
    if ppr is None: return ''
    st = ppr.find(w('pStyle'))
    return st.get(w('val')) if st is not None else ''

def find(text, prefix=False, style=None, after=None):
    els = list(body)
    start = els.index(after) + 1 if after is not None else 0
    for e in els[start:]:
        if is_tbl(e): continue
        t = T(e)
        if (t.startswith(text) if prefix else t == text) and (style is None or pstyle(e) == style):
            return e
    raise KeyError(text)

# ---------- text helpers ----------
def first_run(p): return p.find('.//' + w('r'))
def make_run(rpr, text, bold=None, italic=None):
    r = etree.Element(w('r'))
    if rpr is not None:
        rp = copy.deepcopy(rpr)
        for flag, tags in ((bold, ('b', 'bCs')), (italic, ('i', 'iCs'))):
            if flag is None: continue
            for tag in tags:
                for x in rp.findall(w(tag)): rp.remove(x)
            if flag:
                pos = 1 if rp.find(w('rFonts')) is not None else 0
                rp.insert(pos, etree.Element(w(tags[1])))
                rp.insert(pos, etree.Element(w(tags[0])))
        r.append(rp)
    t = etree.SubElement(r, w('t')); t.text = text; t.set(XML_SPACE, 'preserve')
    return r
def clear_runs(p):
    for ch in list(p):
        if etree.QName(ch).localname != 'pPr': p.remove(ch)
def set_text(p, text, rpr=None):
    fr = first_run(p)
    if rpr is None and fr is not None: rpr = fr.find(w('rPr'))
    rpr = copy.deepcopy(rpr) if rpr is not None else None
    clear_runs(p); p.append(make_run(rpr, text)); return p
def new_par(tpl, text): return set_text(copy.deepcopy(tpl), text)
def new_par_lead(tpl, lead, text):
    p = copy.deepcopy(tpl)
    rpr = copy.deepcopy(first_run(p).find(w('rPr')))
    clear_runs(p)
    p.append(make_run(rpr, lead + ' ', bold=True)); p.append(make_run(rpr, text, bold=False))
    return p
def ref_par(tpl, parts):
    p = copy.deepcopy(tpl)
    rpr = copy.deepcopy(first_run(p).find(w('rPr')))
    for x in rpr.findall(w('i')) + rpr.findall(w('iCs')): rpr.remove(x)
    clear_runs(p)
    for text, ital in parts: p.append(make_run(rpr, text, italic=ital))
    return p
def replace_in_par(p, old, new):
    t = T(p); assert old in t, (old, t[:80]); set_text(p, t.replace(old, new))

# ---------- tables ----------
def rows(tbl): return tbl.findall(w('tr'))
def cells(tr): return tr.findall(w('tc'))
def set_cell(tbl, r, c, text):
    tc = cells(rows(tbl)[r])[c]
    ps = tc.findall(w('p'))
    for p in ps[1:]: tc.remove(p)
    p = ps[0]; rpr = None
    if first_run(p) is None:
        for other in cells(rows(tbl)[r]):
            fr = first_run(other.find(w('p')))
            if fr is not None: rpr = fr.find(w('rPr')); break
    set_text(p, text, rpr)
def find_row(tbl, prefix):
    for k, tr in enumerate(rows(tbl)):
        if T(cells(tr)[0]).startswith(prefix): return k
    raise KeyError(prefix)
def add_row_after(tbl, k_src, k_after, texts):
    new = copy.deepcopy(rows(tbl)[k_src]); rows(tbl)[k_after].addnext(new)
    k = rows(tbl).index(new)
    for c, t in enumerate(texts): set_cell(tbl, k, c, t)
def tblock(label):
    cap = find('Table %s. ' % label, prefix=True, after=find('1. Introduction', style='Heading1'))
    tbl = cap.getnext(); src = tbl.getnext()
    assert is_tbl(tbl) and T(src).startswith('Source'), label
    return cap, tbl, src
def rebuild_rows(tbl, header, data, first_row_tpl=None):
    trs = rows(tbl); hdr, body_t = trs[0], trs[2] if len(trs) > 2 else trs[1]
    first_t = trs[1] if first_row_tpl else body_t
    for tr in trs: tbl.remove(tr)
    tbl.append(copy.deepcopy(hdr))
    for c, t in enumerate(header): set_cell(tbl, 0, c, t)
    for i, rd in enumerate(data):
        tbl.append(copy.deepcopy(first_t if i == 0 else body_t))
        k = len(rows(tbl)) - 1
        assert len(cells(rows(tbl)[k])) == len(rd), (len(cells(rows(tbl)[k])), rd[0])
        for c, t in enumerate(rd): set_cell(tbl, k, c, t)
def new_table_block(tpl_label, caption, header, data, source):
    cap, tbl, src = [copy.deepcopy(x) for x in tblock(tpl_label)]
    rebuild_rows(tbl, header, data)
    set_text(cap, caption); set_text(src, source)
    return [cap, tbl, src]

# ---------- images ----------
img_n = [0]
def new_rel(png_path):
    img_n[0] += 1
    name = 'v6_fig%d.png' % img_n[0]
    shutil.copy(png_path, WD + 'word/media/' + name)
    rid = 'rIdV6img%d' % img_n[0]
    rel = etree.SubElement(rels.getroot(), '{%s}Relationship' % RELNS)
    rel.set('Id', rid); rel.set('Type', 'http://schemas.openxmlformats.org/officeDocument/2006/relationships/image')
    rel.set('Target', 'media/' + name)
    return rid, name
def set_image(imgp, png_path):
    rid, name = new_rel(png_path)
    with open(png_path, 'rb') as fh: head = fh.read(24)
    wpx, hpx = unpack('>II', head[16:24])
    ext = imgp.find('.//{%s}extent' % WP_NS)
    cx = int(ext.get('cx')); cy = int(round(cx * hpx / wpx))
    ext.set('cy', str(cy))
    for e2 in imgp.findall('.//{%s}ext' % A_NS):
        if e2.get('cx') is not None: e2.set('cx', str(cx)); e2.set('cy', str(cy))
    imgp.find('.//{%s}blip' % A_NS).set('{%s}embed' % R_NS, rid)
    dp = imgp.find('.//{%s}docPr' % WP_NS); dp.set('id', str(9500 + img_n[0])); dp.set('name', 'Picture v6 %d' % img_n[0])
    cnv = imgp.find('.//{%s}cNvPr' % PIC_NS)
    if cnv is not None: cnv.set('id', str(9500 + img_n[0])); cnv.set('name', name)
def fig_block(tpl, png, caption, source):
    b = [copy.deepcopy(x) for x in tpl]
    set_image(b[1], png); set_text(b[0], caption); set_text(b[2], source)
    return b
def remove_block(cap):
    mid = cap.getnext(); src = mid.getnext()
    assert T(src).startswith('Source'), T(cap)
    for e in (cap, mid, src): body.remove(e)

# ======================= content =======================
EXEC = [l.strip() for l in re.search(r'```EXEC\n(.*?)```', open('D:/uni/FBA/doc/v5_revision_discussion_recommendation.md', encoding='utf-8').read(), re.S).group(1).strip().split('\n')]
assert len(EXEC) == 4
blocks = [b.strip().split('\n') for b in open(SP + 'newbody.txt', encoding='utf-8').read().split('@@@')]
F1_SENT, SEC13, SECS = blocks[0][0], blocks[1], blocks[2:]
LEADS = ["The cash product gives savers no reason to stay.", "Nothing turns income into regular funding.",
         "Trust breaks at the first deposit and at exit.", "Problem statement.",
         "Salary link, for the missing path from income.", "Invested balance, for the uncompetitive cash rate.",
         "Trust layer, for the breaks at deposit and exit."]
FINDEX_PNG = SRC + 'word/media/ea37da6d45d5d802aecd25baec4b8f74053df2a1.png'
FIGPNG = {'5': FIG + 'fig5_causes.png', '6': FINDEX_PNG, '7': FIG + 'fig7_payday.png', '8': FIG + 'fig8_scenarios.png'}

# ---------- cover and executive summary ----------
set_text(find('Team: [Team name]'), 'Team: KTQT FTUers')
h_exec = find('Executive summary', style='Heading1')
ex = []
e = h_exec.getnext()
while len(ex) < 7: ex.append(e); e = e.getnext()
assert T(ex[3]).startswith('Two causes are measured') and T(ex[6]).startswith('Round 3 should test')
for p, t in zip(ex[3:], EXEC): set_text(p, t)

# ---------- findings: one sentence; 1.3 ----------
p = find('The gap widens as the base grows.', prefix=True)
replace_in_par(p, 'Only 85,739 customers, 5.7 per cent of accounts, used any DNSE product in December 2025, twice as many as a year earlier but still a very low base.', F1_SENT)
assert SEC13[0] == '1.3 Business area and question'
set_text(find('1.3 Business area and question', style='Heading2').getnext(), SEC13[1])

# ---------- sections 3.1 to 5 ----------
h31 = find('3.1 Why the money does not stay', style='Heading2')
T_H2 = copy.deepcopy(h31)
T_P = copy.deepcopy(h31.getnext())
T_H1 = copy.deepcopy(find('4. Recommendations', style='Heading1'))
fc = find('Figure 1. ', prefix=True, after=find('1. Introduction', style='Heading1'))
FIG_TPL = [copy.deepcopy(fc), copy.deepcopy(fc.getnext()), copy.deepcopy(fc.getnext().getnext())]
app = find('Appendices', style='Heading1')
e = h31
while e is not app:
    nxt = e.getnext(); body.remove(e); e = nxt
new = []
for sec in SECS:
    head, lines = sec[0], sec[1:]
    if head.startswith('4.1'):
        new.append(new_par(T_H1, '4. Recommendations'))
    if head == '5. Conclusion':
        new.append(new_par(T_H1, head))
    else:
        new.append(new_par(T_H2, head))
    i = 0
    while i < len(lines):
        ln = lines[i]
        m = re.match(r'Figure (\d)\. ', ln)
        if m:
            src = lines[i + 1]; assert src.startswith('Source')
            new += fig_block(FIG_TPL, FIGPNG[m.group(1)], ln, src); i += 2; continue
        lead = next((L for L in LEADS if ln.startswith(L + ' ')), None)
        new.append(new_par_lead(T_P, lead, ln[len(lead) + 1:]) if lead else new_par(T_P, ln))
        i += 1
for el in new: app.addprevious(el)

# ---------- appendix figures ----------
remove_block(find('Figure B4. How Payday Portfolio works'))
remove_block(find('Figure B5. ', prefix=True, after=app))
cap = find('Figure B6. Validation roadmap for Round 3')
set_text(cap, 'Figure B4. Validation roadmap for Round 3')
set_image(cap.getnext(), FIG + 'figB4_roadmap.png')
remove_block(find('Figure F1. ', prefix=True, after=app))
set_text(find('Figure F2. Payday and saving behaviour by segment pair'), 'Figure F1. Payday and saving behaviour by segment pair')
replace_in_par(find('The segment analysis uses the published Findex aggregates', prefix=True),
               'Figures F1 and F2 summarise the results used in Sections 3.2 and 3.4.',
               'Figure 6 in Section 3.2 and Figure F1 summarise the results.')

# ---------- appendix tables ----------
# B2a after B2
b2a = new_table_block('B1', 'Table B2a. Causes of the balance gap and the response to each',
    ['Cause', 'Evidence', 'Type', 'Response'],
    [['Idle cash earns 2.1 to 2.3%, against 6.0% at TCBS iPower', 'DNSE and TCBS product pages; Figure B1', 'Measured',
      'Contributions are invested automatically in bonds and funds; a bonus on new contributions only if the pilot shows it pays for itself'],
     ['No recurring investment or savings plan', 'DNSE product range (accessed 27 September 2026); 77% of investors find self-management difficult; 36% know and 16% use digital wealth services',
      'Measured (product); survey', 'Salary link and goals'],
     ['Trust breaks at the first deposit and at exit', 'Bonus terms in 5.6% of DNSE reviews against 0.7% at VPS; trust themes draw 43% of helpful votes on negative reviews',
      'Measured; reviews self-selected', 'Trust layer with published proof (Table B14a)'],
     ['Derivatives build share, not balances', 'Derivatives share 25.4%; margin posted at the clearing house; largest brokerage loss among 42 brokers',
      'Measured', 'Outside Payday Portfolio; review of per-trade costs'],
     ['Targets reward acquisition, not balances', 'Published indicators are accounts, shares, active users and order speed', 'Hypothesis',
      'Headline measure moves to accounts holding VND 10 million or more; internal targets checked in Round 3']],
    'Source: Sections 2 and 3; DNSE (2026b, 2026e); TCBS (2026a); Nhân Dân (2025); VnEconomy (2025); Appendix E.')
anchor = tblock('B2')[2]
for el in b2a: anchor.addnext(el); anchor = el

# B11
_, t11, _ = tblock('B11')
k = find_row(t11, 'Quantified gap')
set_cell(t11, k, 1, T(cells(rows(t11)[k])[1]) + '; 1.8% of accounts held net assets of VND 10 million or more in December 2025')
k = find_row(t11, 'Problem')
set_cell(t11, k, 1, 'DNSE converts sign-ups into funded, retained relationships at a low rate, above all in the first 90 days, because its products give salaried customers no competitive, automatic or trusted way to keep money on the platform. Incentives that reward opening accounts may add to this (hypothesis for Round 3)')

# B12
_, t12, s12 = tblock('B12')
hdr12 = [T(c) for c in cells(rows(t12)[0])]
rebuild_rows(t12, hdr12, [
    ['B. Payday Portfolio, a salary-linked savings-to-investing layer', '5', '3', '3', '4', '4', '5', '4.05', '4.00'],
    ['D. Upmarket advisory tier for affluent investors', '4', '4', '2', '3', '1', '3', '3.15', '2.83'],
    ['H. Trust and reliability programme only', '2', '2', '4', '5', '5', '3', '3.15', '3.50'],
    ['E. Distribution alliance with a bank or e-wallet', '3', '3', '4', '2', '3', '3', '3.00', '3.00'],
    ['C. Derivatives-to-shares bridge for traders on same-day trading', '2', '3', '4', '1', '5', '2', '2.65', '2.83'],
    ['G. Reprice the idle-cash account only', '3', '1', '1', '4', '5', '3', '2.65', '2.83'],
    ['F. Reintroduce trading fees', '1', '3', '5', '2', '1', '2', '2.25', '2.33'],
    ['A. Continue acquisition-led growth', '1', '1', '3', '4', '5', '1', '2.15', '2.50']], first_row_tpl=True)
set_text(s12, T(s12) + ' Option B scores 4 on execution and regulatory risk because its first phase needs no new legal structure. Option C depends on same-day trading, possibly not before 2028 (Người Quan sát, 2026). Options G and H become parts of option B.')

# B13
_, t13, _ = tblock('B13')
set_cell(t13, find_row(t13, 'Idle cash'), 2, 'Passes through the idle-cash account and is invested by goal on the next trading day; a market-linked cash yield follows in phase 2 if the SSC confirms the structure')
set_cell(t13, find_row(t13, 'Day 90'), 2, 'Review of goal and allocation; invitation to the equity plan; no margin until month 12, then only after a suitability check')

# B14 and B14a
_, t14, s14 = tblock('B14')
set_cell(t14, find_row(t14, 'Market-linked cash yield'), 0, 'Invested balance now; market-linked cash yield in phase 2')
set_cell(t14, find_row(t14, 'Collateral only by opt-in'), 0, 'No margin at launch; collateral later, by opt-in')
b14a = new_table_block('B1', 'Table B14a. Customer fears, evidence, design responses and published proof',
    ['Customer fear', 'Evidence today', 'Design response', 'Published proof'],
    [['"I cannot get my money out"', 'Deposits not credited or withdrawal delays in 5.0% of negative reviews', 'Withdrawal to the linked bank in one tap', 'Median withdrawal time'],
     ['"I will be locked in"', 'Closure complaints draw 11.3% of helpful votes; a VND 100,000 closure fee reported', 'No closure fee; pause, skip or cancel in one tap', 'Cancellations completed in the app'],
     ['"There are hidden conditions"', 'Bonus terms in 8.6% of negative reviews and 17.8% of helpful votes; 34% of investors fear non-transparent fees', 'All terms on one screen; rewards only on money that stays', 'Trust themes below 10% of negative reviews (24% today)'],
     ['"Where is my money?"', 'Accusations of deception in 17.6% of negative reviews and 28.2% of helpful votes', "Holdings shown in the customer's name; monthly statement", 'Monthly statement'],
     ['"The app fails on payday"', 'Crashes in 27.3% of negative reviews, though not above peers', 'Transfers run as scheduled back-end jobs; reliability as a launch condition', 'Transfer success of 99.5% or more'],
     ['"Is it legal?"', 'SSC fine of VND 802.5 million, August 2026', 'Product reported to the SSC before launch', 'Written confirmation']],
    "Source: Table E3; VnEconomy (2025); Market Times (2026); authors' design.")
anchor = s14
for el in b14a: anchor.addnext(el); anchor = el

# B15
_, t15, s15 = tblock('B15')
rebuild_rows(t15, ['Assumption or outcome', 'Conservative', 'Base', 'Upside'], [
    ['Savers enrolled', '60,000', '150,000', '300,000'],
    ['Share of about 1.4 million dormant accounts', '4%', '11%', '21%'],
    ['Monthly contribution, VND million', '1.0', '1.5', '2.5'],
    ["Contribution as a share of the average worker's monthly income (VND 9.0 million)", '11%', '17%', '28%'],
    ['Share of contributions kept on the platform', '60%', '70%', '80%'],
    ['Assets per saver after 18 months, VND million', '10.8', '18.9', '36.0'],
    ['Layer assets, VND trillion', '0.65', '2.84', '10.80'],
    ['Layer assets as a multiple of DNSE investor cash, June 2026', '0.3', '1.4', '5.5'],
    ['Net new money a year at full enrolment, VND trillion', '0.43', '1.89', '7.20'],
    ['Fee yield on layer assets', '0.5%', '0.8%', '1.0%'],
    ['Annual fee revenue, VND billion', '3', '23', '108'],
    ['Fee revenue per saver a year, VND thousand', '54', '151', '360'],
    ['Accounts holding VND 10 million or more, % of 1.7 million', '5.1', '10.4', '19.2'],
    ['Phase 2 only: loans backed by layer assets (10, 15 and 20%), VND trillion', '0.07', '0.43', '2.16'],
    ['Phase 2 only: net lending income at a 4.9-point spread, VND billion', '3', '21', '106']])
set_text(s15, "Source: authors' projections; National Statistics Office (2026) for income. All inputs are assumptions to be validated in Round 3. Assets per saver equal contribution times share kept times 18 months, before investment returns. The share of accounts holding VND 10 million or more adds savers to the 27,100 accounts already above that level, assuming savers were below it at enrolment, and divides by 1.7 million accounts. Costs of bonuses, marketing and technology are not included; the pilot measures them against fee revenue per saver (Table B17, test 5).")

# B16
_, t16, _ = tblock('B16')
k = find_row(t16, 'Cash layer structure')
set_cell(t16, k, 1, 'Phase 2')
set_cell(t16, k, 2, 'Phase 1 uses the idle-cash account as transit; a bank sweep or licensed money market fund for a market-linked yield follows once the legal basis is confirmed')

# B17
c17, t17, s17 = tblock('B17')
set_text(c17, 'Table B17. Assumptions, tests and decision rules for Round 3')
rebuild_rows(t17, ['No.', 'Assumption', 'Priority', 'Test', 'Measure and decision rule'], [
    ['1', 'Most accounts hold little money, and the gap concentrates in reward-driven cohorts', 'High', 'Balances and cohort curves by channel and reward, from internal data (months 0 to 2)', 'Share funded within 30 days and balance at day 90 by cohort; if reward cohorts hold less, rewards move from sign-up to funding at once'],
    ['2', 'Enough dormant accounts belong to salaried customers aged 22 to 40', 'High', 'Age from identity records; survey of 2,000 dormant customers on income and intent', 'At least 30% salaried and intending to invest; otherwise narrow the target'],
    ['3', 'A phase 2 cash yield can be structured legally', 'High', 'SSC pre-consultation; term sheets from two bank or fund partners', 'Written confirmation and net yield after fees; phase 1 proceeds regardless'],
    ['4', 'Automation turns intention into funding (arm 2 against arm 1)', 'High', 'Three-arm randomised pilot, 20,000 dormant accounts, months 3 to 6', 'Enrolment within 90 days: 11% or more, scale up; 4 to 11%, redesign; below 4%, stop'],
    ['5', 'A bonus on new contributions pays for itself (arm 3 against arm 2)', 'High', 'Same pilot', 'Extra balance times fee yield at least equal to the bonus cost; otherwise drop the bonus'],
    ['6', 'Money stays and is new', 'High', 'Source tag on every inflow; retention at day 90', '70% or more of contributions kept; 80% or more new money'],
    ['7', 'The trust layer works and reliability holds', 'Medium', 'Review themes before and after launch; shadow payday runs', 'Trust themes below 10% of negative reviews (24% today); transfer success of 99.5% or more before launch']])
set_text(s17, "Source: authors' design. The thresholds of 4 and 11 per cent equal the conservative and base cases in Table B15 as shares of dormant accounts. Thresholds are proposals to be agreed with DNSE management.")

# G1, G2
_, tg1, _ = tblock('G1')
k = find_row(tg1, 'Scenario model')
set_cell(tg1, k, 1, 'Assets per saver equal monthly contribution times retention times 18 months; fee revenue equals layer assets times the fee yield; the share of accounts holding VND 10 million or more adds savers to the 27,100 accounts already above that level')
_, tg2, _ = tblock('G2')
k = find_row(tg2, 'Scenario inputs')
set_cell(tg2, k, 1, "60,000 to 300,000 savers; VND 1.0 to 2.5 million a month (base VND 1.5 million, a sixth of the average worker's VND 9.0 million); 60 to 80 per cent retained; fee yield 0.5 to 1.0 per cent; collateral only in phase 2")
set_cell(tg2, k, 4, 'Three-arm pilot')
add_row_after(tg2, k, k, ['Dormant accounts', 'About 1.4 million: 1,512,920 accounts less 85,739 active users less 27,100 holding VND 10 million or more; the overlap is not published, so the true figure is 1.400 to 1.427 million',
                          'Derived', 'Pool size changes by under 2 per cent', 'Internal account register'])

# ---------- references ----------
ref_tpl = find('Market Times. ', prefix=True)
find('DNSE Securities. (2026d)', prefix=True).addnext(ref_par(ref_tpl, [
    ('DNSE Securities. (2026e). ', False), ('Sản phẩm và dịch vụ', True),
    (' [Products and services]. Retrieved September 27, 2026, from https://www.dnse.com.vn/gioi-thieu-khach-hang', False)]))
find('Market Times. ', prefix=True).addprevious(ref_par(ref_tpl, [
    ('Madrian, B. C., & Shea, D. F. (2001). The power of suggestion: Inertia in 401(k) participation and savings behavior. ', False),
    ('The Quarterly Journal of Economics, 116', True), ('(4), 1149–1187. https://doi.org/10.1162/003355301753265543', False)]))
find('National Assembly of Vietnam. ', prefix=True).addnext(ref_par(ref_tpl, [
    ('National Statistics Office. (2026, July). ', False),
    ('Một số nét chính tình hình kinh tế – xã hội quý II và 6 tháng đầu năm 2026', True),
    (' [Socio-economic situation in the second quarter and first half of 2026]. https://www.nso.gov.vn/tin-tuc-thong-ke/2026/07/mot-so-net-chinh-tinh-hinh-kinh-te-xa-hoi-quy-ii-va-6-thang-dau-nam-2026/', False)]))
find('Thanh Niên. ', prefix=True).addprevious(ref_par(ref_tpl, [
    ('Thaler, R. H., & Benartzi, S. (2004). Save More Tomorrow™: Using behavioral economics to increase employee saving. ', False),
    ('Journal of Political Economy, 112', True), ('(S1), S164–S187. https://doi.org/10.1086/380085', False)]))

# ---------- TOC, list of figures, list of tables ----------
h_toc = find('Table of contents'); h_lof = find('List of figures'); h_lot = find('List of tables')
h_intro = find('1. Introduction', style='Heading1')
def between(a, b):
    out = []; e = a.getnext()
    while e is not b: out.append(e); e = e.getnext()
    return out
toc_old, lof_old, lot_old = between(h_toc, h_lof), between(h_lof, h_lot), between(h_lot, h_intro)
TOC1, TOC2, LST = copy.deepcopy(toc_old[0]), copy.deepcopy(toc_old[2]), copy.deepcopy(lof_old[0])
assert T(toc_old[0]).startswith('Executive summary') and T(toc_old[2]).startswith('1.1')
def toc_line(tpl, label, page):
    p = copy.deepcopy(tpl); rpr = copy.deepcopy(first_run(p).find(w('rPr'))); clear_runs(p)
    r = etree.SubElement(p, w('r')); r.append(rpr)
    t1 = etree.SubElement(r, w('t')); t1.text = label; t1.set(XML_SPACE, 'preserve')
    etree.SubElement(r, w('tab'))
    t2 = etree.SubElement(r, w('t')); t2.text = str(PAGES.get(label, 0))
    return p
heads, figs, tabs = [(1, 'Executive summary')], [], []
seen_body = False
for e in body:
    if is_tbl(e): continue
    t = T(e); st = pstyle(e)
    if e is h_intro: seen_body = True
    if not seen_body: continue
    if st == 'Heading1': heads.append((1, t))
    elif st == 'Heading2': heads.append((2, t))
    elif re.match(r'^Figure [A-Z]?\d+\. ', t): figs.append(t)
    elif re.match(r'^Table [A-Z]\d+a?\. ', t): tabs.append(t)
for group, lines in ((toc_old, None), (lof_old, None), (lot_old, None)):
    for e in group: body.remove(e)
anchor = h_toc
for lvl, t in heads:
    el = toc_line(TOC1 if lvl == 1 else TOC2, t, 0); anchor.addnext(el); anchor = el
anchor = h_lof
for t in figs: el = toc_line(LST, t, 0); anchor.addnext(el); anchor = el
anchor = h_lot
for t in tabs: el = toc_line(LST, t, 0); anchor.addnext(el); anchor = el
json.dump({'heads': heads, 'figs': figs, 'tabs': tabs}, open(SP + 'v6_labels.json', 'w', encoding='utf-8'), ensure_ascii=False)

# ---------- drop image relationships no longer used ----------
xml_bytes = etree.tostring(tree, xml_declaration=True, encoding='UTF-8', standalone=True)
used = set(re.findall(rb'r:(?:embed|id|link)="([^"]+)"', xml_bytes))
for rel in list(rels.getroot()):
    if rel.get('Type', '').endswith('/image') and rel.get('Id').encode() not in used:
        tgt = WD + 'word/' + rel.get('Target')
        rels.getroot().remove(rel)
        if os.path.exists(tgt): os.remove(tgt)
open(WD + 'word/document.xml', 'wb').write(xml_bytes)
rels.write(WD + 'word/_rels/document.xml.rels', xml_declaration=True, encoding='UTF-8', standalone=True)

# ---------- zip ----------
if os.path.exists(OUT_DOCX): os.remove(OUT_DOCX)
with zipfile.ZipFile(OUT_DOCX, 'w', zipfile.ZIP_DEFLATED) as z:
    z.write(WD + '[Content_Types].xml', '[Content_Types].xml')
    for root, _, files in os.walk(WD):
        for f in files:
            full = os.path.join(root, f); arc = os.path.relpath(full, WD).replace('\\', '/')
            if arc != '[Content_Types].xml': z.write(full, arc)
print('built', OUT_DOCX, 'heads', len(heads), 'figs', len(figs), 'tabs', len(tabs), 'pages known', len(PAGES))

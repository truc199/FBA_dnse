import json, re
from lxml import etree
ROOT = 'D:/uni/FBA/'
SP = 'C:/Users/trucf/AppData/Local/Temp/claude/d--uni-FBA/935ba975-eb6c-422e-9892-d99c25ba2d00/scratchpad/'
W = 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'
ns = {'w': W}
D = json.load(open(ROOT + 'dnse_financials.json', encoding='utf-8'))
Q = D['quarterly']
P = json.load(open(ROOT + 'peer_financials.json', encoding='utf-8'))
M = json.load(open(ROOT + 'market_macro.json', encoding='utf-8'))

def q(p, k):
    v = Q[p].get(k)
    return 0.0 if v is None else v

def qs(year):
    return [f'{year}Q{i}' for i in range(1, 5)]

def period(label):
    if label.startswith('H1'):
        y = label.split()[-1] if ' ' in label else '2026'
        return [f'{y}Q1', f'{y}Q2']
    return qs(int(label))

def flow(label, k):
    return sum(q(p, k) for p in period(label))

def end(label):
    return period(label)[-1]

def docx_tables(path):
    doc = etree.parse(path)
    body = doc.getroot().find('{%s}body' % W)
    els = list(body)
    out = []
    for i, e in enumerate(els):
        if etree.QName(e).localname == 'tbl':
            # caption = nearest previous paragraph starting with Table
            cap = ''
            for j in range(i - 1, max(i - 4, 0), -1):
                t = ''.join(els[j].itertext())
                if t.startswith('Table'):
                    cap = t; break
            rows = []
            for tr in e.findall('.//w:tr', ns):
                rows.append([''.join(tc.itertext()).strip() for tc in tr.findall('w:tc', ns)])
            out.append((i, cap, rows))
    return out

def num(s):
    s = s.strip().replace(',', '').replace('%', '')
    neg = s.startswith('(') and s.endswith(')')
    s = s.strip('()')
    try:
        v = float(s)
    except ValueError:
        return None
    return -v if neg else v

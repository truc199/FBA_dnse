from vlib import *
T = docx_tables(SP + 'v4x/word/document.xml')
tabs = {cap.split('.')[0] + '.' + cap.split('.')[1].split()[0] if cap else str(i): rows for i, cap, rows in T}
def get(capstart):
    for i, cap, rows in T:
        if cap.startswith(capstart): return rows
labels = ['2021', '2022', '2023', '2024', '2025', 'H1 2026']
def per(lbl):
    return [f'2026Q1', '2026Q2'] if lbl == 'H1 2026' else qs(int(lbl))
def F(lbl, k): return sum(q(p, k) for p in per(lbl))
def E(lbl, k): return q(per(lbl)[-1], k)
calc = {
 'Operating revenue': lambda l: F(l, 'revenue'),
 'Interest on margin loans and advances': lambda l: F(l, 'rev_lending'),
 'Interest on deposits and bonds held to maturity': lambda l: F(l, 'rev_htm'),
 'Brokerage revenue': lambda l: F(l, 'rev_brokerage'),
 'Gains on financial assets at fair value': lambda l: F(l, 'rev_fvtpl'),
 'Direct brokerage cost': lambda l: -F(l, 'cost_brokerage'),
 'Losses on financial assets at fair value': lambda l: -F(l, 'cost_fvtpl'),
 'Interest expense': lambda l: -F(l, 'interest_expense'),
 'Template line 24 (provisions and borrowing cost of the loan book)': lambda l: -F(l, 'cost_provision_and_loan_funding'),
 'Administrative expenses': lambda l: -F(l, 'admin_cost'),
 'Pre-tax profit': lambda l: F(l, 'pbt'),
 'Net proprietary result': lambda l: F(l, 'rev_fvtpl') + F(l, 'cost_fvtpl'),
 'Core pre-tax profit': lambda l: F(l, 'pbt') - (F(l, 'rev_fvtpl') + F(l, 'cost_fvtpl')),
 'Profit after tax': lambda l: F(l, 'pat'),
}
rows = get('Table A1')
bad = 0
for r in rows[1:]:
    name = r[0]
    if name not in calc: print('SKIP', name); continue
    for j, l in enumerate(labels):
        doc = num(r[j + 1]); c = calc[name](l)
        if doc is None or abs(doc - c) > 0.15 + 0.001 * abs(c):
            bad += 1; print('A1 MISMATCH', name, l, 'doc', r[j + 1], 'calc', round(c, 1))
print('A1 checked; mismatches', bad)

def debt(p): return q(p, 'short_term_borrowing') + q(p, 'bonds_short') + q(p, 'bonds_long')
def htm(p): return q(p, 'htm_assets') + q(p, 'htm_assets_long')
calc2 = {
 'Margin loans and advances': lambda l: E(l, 'loans'),
 'Deposits and bonds held to maturity': lambda l: htm(per(l)[-1]),
 'Financial assets at fair value': lambda l: E(l, 'fvtpl_assets'),
 'Cash and equivalents': lambda l: E(l, 'cash'),
 'Total assets': lambda l: E(l, 'total_assets'),
 'Borrowings and bonds': lambda l: debt(per(l)[-1]),
 "Owners' equity": lambda l: E(l, 'equity'),
 'Investor cash held off balance sheet': lambda l: E(l, 'customer_cash_trading'),
 'Pre-tax margin, %': lambda l: F(l, 'pbt') / F(l, 'revenue') * 100,
 'Brokerage revenue as % of direct cost': lambda l: F(l, 'rev_brokerage') / -F(l, 'cost_brokerage') * 100,
 'Loans as % of equity': lambda l: E(l, 'loans') / E(l, 'equity') * 100,
}
rows = get('Table A2'); bad = 0
lab2 = ['2021', '2022', '2023', '2024', '2025', 'H1 2026']
for r in rows[1:]:
    name = r[0]
    if name not in calc2: print('A2 not auto-checked:', name, r[1:]); continue
    for j, l in enumerate(lab2):
        doc = num(r[j + 1]); c = calc2[name](l)
        if doc is None or abs(doc - c) > 0.6 + 0.002 * abs(c):
            bad += 1; print('A2 MISMATCH', name, l, 'doc', r[j + 1], 'calc', round(c, 1))
print('A2 checked; mismatches', bad)
# ROE and yields per A2 definitions (average of annualised quarterly values)
def avgq(lbl, fn):
    vals = [fn(p) for p in per(lbl)]
    return sum(vals) / len(vals)
def prev(p):
    y, i = int(p[:4]), int(p[-1])
    return f'{y}Q{i-1}' if i > 1 else f'{y-1}Q4'
def roe(l):
    ps = per(l); pbt = sum(q(p, 'pat') for p in ps)
    eq = (q(prev(ps[0]), 'equity') + q(ps[-1], 'equity')) / 2
    return pbt * (4 / len(ps)) / eq * 100
def lend_y(p): return q(p, 'rev_lending') * 4 / ((q(prev(p), 'loans') + q(p, 'loans')) / 2) * 100
def fund(p):
    al = (q(p, 'loan_allowance') - q(prev(p), 'loan_allowance'))
    return -q(p, 'interest_expense') - q(p, 'cost_provision_and_loan_funding') - (-al if al < 0 else al) * (1)
print('ROE calc', {l: round(roe(l), 1) for l in lab2})
print('lend yield avg', {l: round(avgq(l, lend_y), 1) for l in lab2})
print('derived funding_cost_pct', {p: round(D['derived'][p].get('funding_cost_pct') or 0, 2) for p in ['2024Q1','2024Q2','2024Q3','2024Q4','2025Q1','2025Q2','2025Q3','2025Q4','2026Q1','2026Q2']})
print('derived lending yield', {p: round(D['derived'][p].get('lending_yield_pct') or 0, 2) for p in ['2024Q1','2024Q2','2024Q3','2024Q4','2025Q1','2025Q2','2025Q3','2025Q4','2026Q1','2026Q2']})
rows = get('Table A3')
for r in rows: print('A3', r)

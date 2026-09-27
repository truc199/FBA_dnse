from vlib import *
import json
F = P['firms']
# brokerage streak and cumulative
qs_all = [f'{y}Q{i}' for y in range(2021, 2027) for i in range(1, 5)][:-2]
net = {p: q(p, 'rev_brokerage') + q(p, 'cost_brokerage') for p in qs_all}
streak = [p for p in qs_all if p >= '2022Q3']
print('all negative since 2022Q3:', all(net[p] < 0 for p in streak), len(streak), 'cum', round(sum(net[p] for p in streak), 1))
print('coverage 2025 %.1f  H1 2026 %.1f' % (sum(q(p,'rev_brokerage') for p in qs(2025))/-sum(q(p,'cost_brokerage') for p in qs(2025))*100,
      (q('2026Q1','rev_brokerage')+q('2026Q2','rev_brokerage'))/-(q('2026Q1','cost_brokerage')+q('2026Q2','cost_brokerage'))*100))
# H1 2026 brokerage net for all firms
rows = []
for t, x in F.items():
    Qx = x['quarterly']
    try:
        r = sum((Qx[k].get('rev_brokerage') or 0) for k in ['2026Q1', '2026Q2'])
        c = sum((Qx[k].get('cost_brokerage') or 0) for k in ['2026Q1', '2026Q2'])
    except KeyError:
        continue
    rows.append((t, r, -c, r + c))
dn = (q('2026Q1','rev_brokerage')+q('2026Q2','rev_brokerage'), -(q('2026Q1','cost_brokerage')+q('2026Q2','cost_brokerage')))
rows.append(('DNSE', dn[0], dn[1], dn[0]-dn[1]))
rows.sort(key=lambda r: -r[1])
print('n firms', len(rows), 'negative', sum(1 for r in rows if r[3] < 0))
print('TOP by brokerage revenue:')
for r in rows[:12]: print('  %-9s rev %7.1f cost %7.1f net %7.1f cover %.2f' % (r[0], r[1], r[2], r[3], r[1]/r[2] if r[2] else 0))
worst = sorted(rows, key=lambda r: r[3])[:6]
print('WORST:', [(r[0], round(r[3], 1)) for r in worst])
# industry total brokerage net H1 2026
print('industry total net', round(sum(r[3] for r in rows), 1))
# funding & structure Q2 2026
def st(Qx, p):
    x = Qx[p]; debt = (x.get('short_term_borrowing') or 0) + (x.get('bonds_short') or 0) + (x.get('bonds_long') or 0)
    htm = (x.get('htm_assets') or 0) + (x.get('htm_assets_long') or 0)
    return debt, htm, x['loans'], x['equity'], x['total_assets'], x.get('short_term_borrowing') or 0
print('STRUCTURE Q2 2026')
for t in ['DNSE', 'VPS', 'SSI', 'TCBS', 'VPBankS', 'MBS', 'HSC', 'Vietcap', 'VNDirect']:
    if t == 'DNSE':
        Qx = Q; fc = D['derived']['2026Q2']['funding_cost_pct']; fc1 = D['derived']['2026Q1']['funding_cost_pct']
    else:
        Qx = F[t]['quarterly']; fc = F[t]['derived']['2026Q2']['funding_cost_pct']; fc1 = F[t]['derived']['2026Q1']['funding_cost_pct']
    debt, htm, loans, eq, ta, stb = st(Qx, '2026Q2')
    print('  %-8s fundQ2 %.1f fundQ1 %.1f HTM/assets %.1f loans/equity %.0f short-term share of debt %.0f%%' % (t, fc, fc1, htm/ta*100, loans/eq*100, stb/debt*100))
# marginal decomposition
def S(keys, k): return sum(q(p, k) for p in keys)
for a, b, lab in [(['2025Q1','2025Q2'], ['2026Q1','2026Q2'], 'H1'), (qs(2024), qs(2025), 'FY')]:
    dr = S(b,'revenue') - S(a,'revenue'); dprop_rev = S(b,'rev_fvtpl') - S(a,'rev_fvtpl')
    dcore_rev = dr - dprop_rev
    dbro = -(S(b,'cost_brokerage') - S(a,'cost_brokerage'))
    dfund = -(S(b,'interest_expense') - S(a,'interest_expense')) - (S(b,'cost_provision_and_loan_funding') - S(a,'cost_provision_and_loan_funding'))
    dadm = -(S(b,'admin_cost') - S(a,'admin_cost'))
    dpbt = S(b,'pbt') - S(a,'pbt'); dprop = (S(b,'rev_fvtpl')+S(b,'cost_fvtpl')) - (S(a,'rev_fvtpl')+S(a,'cost_fvtpl'))
    dcore_pbt = dpbt - dprop
    dcore_cost = dcore_rev - dcore_pbt
    other = dcore_cost - dbro - dfund - dadm
    print(lab, 'dRev %.1f dCoreRev %.1f | dCoreCost %.1f = bro %.1f (%.0f%%) fund %.1f (%.0f%%) admin %.1f (%.0f%%) other %.1f | per100 %.0f | dPBT %.1f dCorePBT %.1f' % (
        dr, dcore_rev, dcore_cost, dbro, dbro/dcore_cost*100, dfund, dfund/dcore_cost*100, dadm, dadm/dcore_cost*100, other, dcore_cost/dcore_rev*100, dpbt, dcore_pbt))
    for k in ['rev_lending','rev_htm','rev_brokerage','rev_fvtpl']:
        print('   ', k, round(S(a,k),1), '->', round(S(b,k),1), '%+.1f' % (S(b,k)-S(a,k)))
    print('    total cost incl prop per 100 revenue: %.0f' % ((dr - dpbt)/dr*100))
# average debt and funding rate
def avgdebt(ps):
    pts = [prev(ps[0])] + ps
    return sum(sum([q(p,'short_term_borrowing'),q(p,'bonds_short'),q(p,'bonds_long')]) for p in pts)/len(pts)
def prev(p):
    y, i = int(p[:4]), int(p[-1]); return f'{y}Q{i-1}' if i > 1 else f'{y-1}Q4'
a1 = avgdebt(['2025Q1','2025Q2']); b1 = avgdebt(['2026Q1','2026Q2'])
print('avg debt H1 2025 %.0f H1 2026 %.0f change %.0f%%' % (a1, b1, (b1/a1-1)*100))
# staff and outsourced (from CSV notes)

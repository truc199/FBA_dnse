import csv, collections
R = 'D:/uni/FBA/'
def load(fn):
    return list(csv.DictReader(open(R + fn, encoding='utf-8')))
d = load('reviews_flagged_vn.com.encapital.arrow.csv')
v = load('reviews_flagged_vn.com.vpbs.smartone.csv')
f = load('reviews_flagged_com.fpts.eztrade.csv')
keep = lambda rows: [r for r in rows if r['keep'] == '1']
dk = keep(d); vk = keep(v); fk = keep(f)
print('DNSE raw', len(d), 'kept', len(dk), 'mean kept %.2f' % (sum(int(r['rating']) for r in dk) / len(dk)))
print('VPS raw', len(v), 'kept', len(vk), '%.2f' % (sum(int(r['rating']) for r in vk) / len(vk)), 'FPTS', len(f), len(fk))
spam = collections.Counter(r['spam_flag'] for r in d)
print('DNSE spam flags', spam)
neg = [r for r in dk if int(r['rating']) <= 2]
votes = sum(int(r['thumbs_up']) for r in neg)
print('negatives', len(neg), 'votes', votes)
def th(r): return set(filter(None, r['themes'].split('|')))
for t in ['stability', 'onboarding', 'fraud', 'promo', 'money', 'closure', 'ui', 'influencer', 'fees', 'yield']:
    n = [r for r in neg if t in th(r)]
    print(f'{t:11s} n={len(n):3d} {len(n)/len(neg)*100:5.1f}%  votes {sum(int(r["thumbs_up"]) for r in n)/votes*100:5.1f}%  all_kept={sum(1 for r in dk if t in th(r))}')
trust = [r for r in neg if th(r) & {'fraud', 'promo', 'closure'}]
prod = [r for r in neg if th(r) & {'stability', 'onboarding'}]
print('trust', len(trust), '%.1f%%' % (len(trust)/len(neg)*100), 'votes %.1f%%' % (sum(int(r['thumbs_up']) for r in trust)/votes*100))
print('product', len(prod), '%.1f%%' % (len(prod)/len(neg)*100), 'votes %.1f%%' % (sum(int(r['thumbs_up']) for r in prod)/votes*100))
# bonus share since 2023-03-27 (VPS window start)
def share(rows, start):
    rr = [r for r in rows if r['date'] >= start]
    b = [r for r in rr if 'promo' in th(r)]
    return len(b), len(rr), len(b) / len(rr) * 100
print('promo share DNSE since 2023-03-27', share(dk, '2023-03-27'))
print('promo share VPS', share(vk, '2023-03-27'))
print('promo share FPTS', share(fk, '2000-01-01'))
# monthly
m = collections.Counter(r['date'][:7] for r in dk if r['date'][:7] in ('2024-10', '2024-11'))
gen = sum(1 for r in dk if r['date'][:7] in ('2024-10', '2024-11') and r['is_generic'] == '1')
print('Oct+Nov 2024 retained', sum(m.values()), 'one-word %.0f%%' % (gen / sum(m.values()) * 100))
negm = collections.Counter(r['date'][:7] for r in neg)
print('top negative months', negm.most_common(4))
# top voted June 2025
top = sorted([r for r in neg if r['date'].startswith('2025-06')], key=lambda r: -int(r['thumbs_up']))[:4]
for r in top: print(r['date'], r['rating'], r['thumbs_up'], r['themes'], r['text'][:120])
# idle-cash mentions
print('yield theme kept', sum(1 for r in dk if 'yield' in th(r)))
# years
for y in ['2022', '2023']:
    raw = [r for r in d if r['date'].startswith(y)]
    rem = [r for r in raw if r['keep'] != '1']
    print(y, 'removed %.1f%%' % (len(rem) / len(raw) * 100))

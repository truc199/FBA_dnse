import json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from decimal import Decimal, ROUND_HALF_UP
OUT = 'C:/Users/trucf/AppData/Local/Temp/claude/d--uni-FBA/935ba975-eb6c-422e-9892-d99c25ba2d00/scratchpad/newfig/'
BLUE, ORANGE, LORANGE, GRID, AXIS = '#2a78d6', '#eb6834', '#f6b59a', '#e1e0d9', '#9a998f'
plt.rcParams.update({'font.family': 'Calibri', 'font.size': 13, 'axes.edgecolor': AXIS, 'axes.linewidth': 1.0,
                     'xtick.color': '#000000', 'ytick.color': '#000000'})
def r1(x):
    return str(Decimal(str(x)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP))
def r2(x):
    return str(Decimal(str(x)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP))

# ---- inputs (all verified in scratchpad/verify) ----
ACC_SHARE = 12.7          # 1,512,920 / 11,871,933 = 12.74 (end-2025); 1.70m / 13,430,517 = 12.66 (30 Jun 2026)
NEW_ACC = 518514 / 2681838 * 100
DERIV, HNX = 25.38, 2.88
CASH = (1961 / 86600 * 100, 1961 / 56377 * 100)
LEND = (6303 / 453800 * 100, 6303 / 345309 * 100)
PBT = (97.4 / 15200 * 100, 97.4 / 11871 * 100)

# ---- Figure 1 (body): shares ----
rows = [('Share of new accounts opened, 2025', NEW_ACC, None, BLUE),
        ('Derivatives brokerage (HNX), Q2 2026', DERIV, None, BLUE),
        ('Securities accounts, end-2025', ACC_SHARE, None, BLUE),
        ('Listed-share brokerage on HNX, Q2 2026', HNX, None, ORANGE),
        ('Investor cash held at brokers, 30 Jun 2026', CASH[0], CASH[1], ORANGE),
        ('Margin loans and advances, 30 Jun 2026', LEND[0], LEND[1], ORANGE),
        ('Pre-tax profit, Q2 2026', PBT[0], PBT[1], ORANGE)]
fig, ax = plt.subplots(figsize=(8.5, 3.6), dpi=200)
ys = list(range(len(rows)))[::-1]
for y, (lab, lo, hi, col) in zip(ys, rows):
    ax.barh(y, lo, color=col, height=0.55, zorder=3)
    if hi is not None:
        ax.barh(y, hi - lo, left=lo, color=LORANGE, height=0.55, zorder=3)
        txt = f'{r1(lo)} to {r1(hi)}'
        x = hi
    else:
        txt = r1(lo); x = lo
    ax.text(x + 0.35, y, txt, va='center', fontsize=12)
ax.set_yticks(ys); ax.set_yticklabels([r[0] for r in rows], fontsize=12)
ax.axvline(ACC_SHARE, color='#555555', lw=1.2, zorder=4)
ax.text(ACC_SHARE + 0.25, -0.75, 'account share', fontsize=11, va='bottom')
ax.set_xlim(0, 30); ax.set_ylim(-0.8, len(rows) - 0.4)
ax.set_xlabel('DNSE share of the named market, per cent', fontsize=12)
ax.grid(axis='x', color=GRID, zorder=0); ax.set_axisbelow(True)
for s in ['top', 'right', 'left']: ax.spines[s].set_visible(False)
ax.tick_params(axis='y', length=0)
fig.tight_layout(); fig.savefig(OUT + 'fig_shares.png'); plt.close(fig)

# ---- Figure A2: value per account relative to market average ----
rows2 = [('Derivatives brokerage', DERIV / ACC_SHARE, None, BLUE),
         ('Listed-share trading on HNX', HNX / ACC_SHARE, None, ORANGE),
         ('Investor cash at the broker', CASH[0] / ACC_SHARE, CASH[1] / ACC_SHARE, ORANGE),
         ('Margin loans and advances', LEND[0] / ACC_SHARE, LEND[1] / ACC_SHARE, ORANGE),
         ('Pre-tax profit', PBT[0] / ACC_SHARE, PBT[1] / ACC_SHARE, ORANGE)]
fig, ax = plt.subplots(figsize=(8.5, 3.0), dpi=200)
ys = list(range(len(rows2)))[::-1]
for y, (lab, lo, hi, col) in zip(ys, rows2):
    ax.barh(y, lo, color=col, height=0.55, zorder=3)
    if hi is not None:
        ax.barh(y, hi - lo, left=lo, color=LORANGE, height=0.55, zorder=3)
        txt = f'{r2(lo)} to {r2(hi)}'; x = hi
    else:
        txt = r2(lo); x = lo
    ax.text(x + 0.03, y, txt, va='center', fontsize=12)
ax.set_yticks(ys); ax.set_yticklabels([r[0] for r in rows2], fontsize=12)
ax.axvline(1.0, color='#000000', lw=1.4, zorder=4)
ax.text(1.02, len(rows2) - 0.55, 'market average account = 1.00', fontsize=11, va='bottom')
ax.set_xlim(0, 2.4); ax.set_ylim(-0.6, len(rows2) - 0.1)
ax.set_xlabel('Value per DNSE account relative to the average Vietnamese securities account', fontsize=12)
ax.grid(axis='x', color=GRID, zorder=0); ax.set_axisbelow(True)
for s in ['top', 'right', 'left']: ax.spines[s].set_visible(False)
ax.tick_params(axis='y', length=0)
fig.tight_layout(); fig.savefig(OUT + 'fig_ratios.png'); plt.close(fig)

# ---- Figure B5: scenarios ----
sc = {'Conservative': (60000, 1.5, 0.6), 'Base': (150000, 2.5, 0.7), 'Upside': (300000, 3.5, 0.8)}
assets = {k: n * m * r * 18 / 1e6 for k, (n, m, r) in sc.items()}          # VND trillion
nnm = {k: n * m * r * 12 / 1e6 for k, (n, m, r) in sc.items()}             # VND trillion a year
cols = ['#a4c6f2', BLUE, '#1d5cab']
fig, axs = plt.subplots(1, 2, figsize=(8.5, 3.3), dpi=200)
for ax, data, lab in [(axs[0], assets, 'Layer assets after 18 months,\nVND trillion'),
                      (axs[1], nnm, 'Net new money a year at full\nenrolment, VND trillion')]:
    ks = list(data)
    ax.bar(ks, [data[k] for k in ks], color=cols, width=0.6, zorder=3)
    for i, k in enumerate(ks):
        ax.text(i, data[k] + max(data.values()) * 0.02, r1(data[k]), ha='center', fontsize=12)
    ax.set_ylabel(lab, fontsize=12)
    ax.grid(axis='y', color=GRID, zorder=0); ax.set_axisbelow(True)
    for s in ['top', 'right']: ax.spines[s].set_visible(False)
axs[0].axhline(1.961, color='#000000', lw=1.3, zorder=4)
axs[0].text(0.35, 2.35, 'DNSE investor cash, 30 Jun 2026', fontsize=10.5)
fig.tight_layout(); fig.savefig(OUT + 'fig_scenarios.png'); plt.close(fig)
print('assets', {k: round(v, 3) for k, v in assets.items()}, 'nnm', {k: round(v, 3) for k, v in nnm.items()})
print('shares', round(NEW_ACC, 2), [round(x, 2) for x in CASH + LEND + PBT])

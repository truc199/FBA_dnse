import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
from decimal import Decimal, ROUND_HALF_UP

OUT = 'C:/Users/trucf/AppData/Local/Temp/claude/d--uni-FBA/731e1691-b54f-4846-bba0-f4e353828c32/scratchpad/v6fig/'
import os
os.makedirs(OUT, exist_ok=True)
BLUE, DBLUE, LBLUE, ORANGE, GREY, LGREY, GRID, AXIS, GREEN = (
    '#2a78d6', '#1d5cab', '#a4c6f2', '#eb6834', '#b9b6ad', '#f3f2ee', '#e1e0d9', '#9a998f', '#1aab7a')
plt.rcParams.update({'font.family': 'Calibri', 'font.size': 12, 'axes.edgecolor': AXIS, 'axes.linewidth': 1.0,
                     'xtick.color': '#000000', 'ytick.color': '#000000'})


def r1(x):
    return str(Decimal(str(x)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP))


def box(ax, x, y, w, h, text, ec, fc='white', lw=2.0, ls='-', fs=11, bold_first=False, align='center'):
    p = FancyBboxPatch((x, y), w, h, boxstyle='round,pad=0.012,rounding_size=0.018', ec=ec, fc=fc, lw=lw, ls=ls,
                       transform=ax.transAxes, zorder=2, clip_on=False)
    ax.add_patch(p)
    if bold_first and '\n' in text:
        head, rest = text.split('\n', 1)
        ax.text(x + w / 2, y + h - 0.035, head, ha='center', va='top', fontsize=fs + 0.5, weight='bold',
                transform=ax.transAxes, zorder=3)
        ax.text(x + w / 2, y + (h - 0.07) / 2, rest, ha='center', va='center', fontsize=fs,
                transform=ax.transAxes, zorder=3, linespacing=1.15)
    else:
        ax.text(x + (w / 2 if align == 'center' else 0.012), y + h / 2, text, ha=align, va='center', fontsize=fs,
                transform=ax.transAxes, zorder=3, linespacing=1.15)


def arrow(ax, x0, y0, x1, y1, color='#000000', lw=1.6, style='-|>', ls='-'):
    ax.annotate('', xy=(x1, y1), xytext=(x0, y0), xycoords='axes fraction',
                arrowprops=dict(arrowstyle=style, color=color, lw=lw, ls=ls, shrinkA=0, shrinkB=0), zorder=1)


# ---------------- Figure 5: causes of the balance gap ----------------
fig, ax = plt.subplots(figsize=(10, 5.4), dpi=200)
ax.set_axis_off()
ax.text(0.105, 0.975, 'Symptom', ha='center', fontsize=12.5, weight='bold', transform=ax.transAxes)
ax.text(0.42, 0.975, 'Cause and evidence', ha='center', fontsize=12.5, weight='bold', transform=ax.transAxes)
ax.text(0.79, 0.975, 'Response', ha='center', fontsize=12.5, weight='bold', transform=ax.transAxes)
box(ax, 0.0, 0.33, 0.20, 0.34,
    'Balance gap\n12.7% of accounts but\n2.3 to 3.5% of\ninvestor cash;\n1.8% of accounts hold\nVND 10 million or more',
    DBLUE, fc='#eaf2fc', bold_first=True, fs=10.5)
rows = [
    ('Idle cash earns 2.1 to 2.3%, against 6.0%\nat TCBS iPower for the same balance', 'MEASURED', True,
     'Invested balance: bonds and VN30 ETFs\nfrom the next trading day', True),
    ('No recurring investment or savings plan;\n77% find self-management difficult', 'MEASURED', True,
     'Salary link: standing order or ZaloPay\non payday, set once by the customer', True),
    ('Trust breaks at first deposit and exit:\nbonus terms in 5.6% of reviews (VPS 0.7%)', 'MEASURED', True,
     'Trust layer: no closure fee, rewards\non money that stays, published proof', True),
    ('Derivatives build market share and\nbrokerage losses, not balances', 'MEASURED', True,
     'Outside Payday Portfolio:\nreview of per-trade costs', False),
    ('Targets reward accounts and speed,\nnot balances', 'HYPOTHESIS', False,
     'Headline measure moves to accounts\nwith VND 10 million; test in Round 3', False),
]
h, gap = 0.145, 0.037
ys = [0.935 - (i + 1) * h - i * gap for i in range(len(rows))]
for (cause, tag, measured, resp, inpp), y in zip(rows, ys):
    ec = BLUE if measured else AXIS
    ls = '-' if measured else '--'
    box(ax, 0.25, y, 0.34, h, cause, ec, ls=ls, fs=10.5)
    ax.text(0.585, y + h - 0.012, tag, ha='right', va='top', fontsize=8.5, weight='bold',
            color=(BLUE if measured else '#6b6a63'), transform=ax.transAxes, zorder=4)
    rfc = '#eaf2fc' if inpp else LGREY
    rec = BLUE if inpp else AXIS
    box(ax, 0.65, y, 0.28, h, resp, rec, fc=rfc, fs=10.5)
    arrow(ax, 0.595, y + h / 2, 0.645, y + h / 2)
    # tree line from symptom to cause
    arrow(ax, 0.2, 0.50, 0.245, y + h / 2, color='#6b6a63', lw=1.1, style='-')
# bracket for Payday Portfolio
top, bot = ys[0] + h, ys[2]
ax.plot([0.952, 0.96, 0.96, 0.952], [top, top, bot, bot], color=BLUE, lw=1.6, transform=ax.transAxes, clip_on=False)
ax.text(1.03, (top + bot) / 2, 'Payday\nPortfolio', rotation=90, va='center', ha='left', fontsize=11, weight='bold',
        color=BLUE, transform=ax.transAxes)
fig.subplots_adjust(left=0.01, right=0.99, top=0.98, bottom=0.01)
fig.savefig(OUT + 'fig5_causes.png', bbox_inches='tight', pad_inches=0.08)
plt.close(fig)

# ---------------- Figure 7: how Payday Portfolio works ----------------
fig, ax = plt.subplots(figsize=(10, 5.3), dpi=200)
ax.set_axis_off()
box(ax, 0.015, 0.60, 0.16, 0.27, "Salary account\nBank account or\nZaloPay wallet;\nwage arrives on payday", AXIS,
    bold_first=True, fs=10.5)
box(ax, 0.30, 0.60, 0.19, 0.27, "Idle-cash account\nTransit only: money is\ninvested on the next\ntrading day", BLUE,
    bold_first=True, fs=10.5)
box(ax, 0.58, 0.745, 0.2, 0.20, "Income plan\nTrứng Vàng bonds from\nVND 1 million; partner\nbond funds", BLUE,
    bold_first=True, fs=10.5)
box(ax, 0.58, 0.515, 0.2, 0.20, "Equity plan\nVN30 exchange-traded\nfund, opt-in by goal", BLUE,
    bold_first=True, fs=10.5)
box(ax, 0.815, 0.515, 0.17, 0.43, "Phase 2\nMarket-linked\ncash yield via a\npartner bank or\nmoney market\nfund, after SSC\nconfirmation.\nOpt-in collateral\nafter 12 months\nand a suitability\ncheck", ORANGE,
    ls='--', bold_first=True, fs=9.8)
arrow(ax, 0.18, 0.735, 0.295, 0.735)
ax.text(0.2375, 0.715, "customer's own\nstanding order;\nno debit by DNSE", ha='center', va='top', fontsize=9.5,
        transform=ax.transAxes)
arrow(ax, 0.495, 0.765, 0.575, 0.83)
arrow(ax, 0.495, 0.705, 0.575, 0.625)
ax.text(0.535, 0.735, 'split\nby goal', ha='center', va='center', fontsize=9.5, transform=ax.transAxes,
        bbox=dict(fc='white', ec='none', pad=1))
ax.text(0.5, 0.44, 'Revenue for DNSE: bond and fund distribution fees, ETF trading and balances that stay; '
        'lending income only in phase 2', ha='center', va='center', fontsize=10.5, transform=ax.transAxes)
box(ax, 0.015, 0.06, 0.97, 0.25,
    "Trust layer applied across every step\nNo closure fee. Pause, skip or cancel in one tap. Rewards paid only on money that stays.\n"
    "All terms on one screen. Product reported to the SSC before launch.\n"
    "Published median withdrawal time and payday transfer success (launch condition: 99.5 per cent).",
    '#6b6a63', fc=LGREY, bold_first=True, fs=10.5)
fig.subplots_adjust(left=0.01, right=0.99, top=0.99, bottom=0.01)
fig.savefig(OUT + 'fig7_payday.png', bbox_inches='tight', pad_inches=0.08)
plt.close(fig)

# ---------------- Figure 8: scenarios ----------------
sc = {'Conservative': (60000, 1.0, 0.6), 'Base': (150000, 1.5, 0.7), 'Upside': (300000, 2.5, 0.8)}
assets = {k: n * m * r * 18 / 1e6 for k, (n, m, r) in sc.items()}          # VND trillion
share = {'End-2025': 27100 / 1512920 * 100}
share.update({k: (27100 + n) / 1.7e6 * 100 for k, (n, m, r) in sc.items()})
cols = [LBLUE, BLUE, DBLUE]
fig, axs = plt.subplots(1, 2, figsize=(9.5, 3.5), dpi=200)
ax = axs[0]
ks = list(assets)
ax.bar(ks, [assets[k] for k in ks], color=cols, width=0.6, zorder=3)
for i, k in enumerate(ks):
    ax.text(i, assets[k] + 0.2, r1(assets[k]), ha='center', fontsize=12)
ax.axhline(1.961, color='#000000', lw=1.3, zorder=4)
ax.set_title('Black line: DNSE investor cash, 30 June 2026', fontsize=10.5, loc='left')
ax.set_ylabel('Layer assets after 18 months,\nVND trillion', fontsize=12)
ax = axs[1]
ks2 = list(share)
ax.bar(ks2, [share[k] for k in ks2], color=[GREY] + cols, width=0.6, zorder=3)
for i, k in enumerate(ks2):
    ax.text(i, share[k] + 0.4, r1(share[k]), ha='center', fontsize=12)
ax.axhline(5.0, color=ORANGE, lw=1.4, ls='--', zorder=4)
ax.set_title('Dashed line: target of 5% within 18 months', fontsize=10.5, loc='left', color=ORANGE)
ax.set_ylabel('Accounts holding VND 10 million\nor more, % of all accounts', fontsize=12)
for a in axs:
    a.grid(axis='y', color=GRID, zorder=0); a.set_axisbelow(True)
    for s in ['top', 'right']: a.spines[s].set_visible(False)
axs[1].tick_params(axis='x', labelsize=11)
fig.tight_layout()
fig.savefig(OUT + 'fig8_scenarios.png')
plt.close(fig)
print('assets', {k: round(v, 3) for k, v in assets.items()}, 'share', {k: round(v, 2) for k, v in share.items()})

# ---------------- Figure B4: validation roadmap ----------------
tasks = [('Balances and cohorts from internal data', 0, 1.5, 'Test'),
         ('Age and income of dormant accounts; survey of 2,000', 0, 2, 'Test'),
         ('Trust fixes: closure fee, reward terms; report to the SSC', 0, 2, 'Enable'),
         ('Shadow payday runs to 99.5% transfer success', 1, 3, 'Enable'),
         ('Three-arm pilot, 20,000 dormant accounts', 3, 6, 'Pilot'),
         ('Phase 2 groundwork: SSC pre-consultation, fund partner', 2, 6, 'Enable'),
         ('Read-out: enrolment, retention, new money, bonus payback', 5.5, 6.5, 'Decide'),
         ('Scale decision; phase 2 launch if confirmed', 6.5, 9, 'Decide')]
cmap = {'Test': BLUE, 'Enable': GREY, 'Pilot': GREEN, 'Decide': ORANGE}
fig, ax = plt.subplots(figsize=(10, 3.9), dpi=200)
for i, (lab, a, b, kind) in enumerate(tasks):
    ax.barh(len(tasks) - 1 - i, b - a, left=a, color=cmap[kind], height=0.55, zorder=3)
ax.set_yticks(range(len(tasks))); ax.set_yticklabels([t[0] for t in tasks][::-1], fontsize=11.5)
ax.set_xlim(0, 9); ax.set_xticks(range(10)); ax.set_xticklabels(['M%d' % m for m in range(10)], fontsize=11.5)
ax.set_xlabel('Months from the start of Round 3 development', fontsize=12)
ax.grid(axis='x', color=GRID, zorder=0); ax.set_axisbelow(True)
for s in ['top', 'right', 'left']: ax.spines[s].set_visible(False)
ax.tick_params(axis='y', length=0)
handles = [plt.Rectangle((0, 0), 1, 1, color=cmap[k]) for k in cmap]
ax.legend(handles, list(cmap), ncol=4, loc='lower center', bbox_to_anchor=(0.5, 1.0), frameon=False, fontsize=11.5)
fig.tight_layout()
fig.savefig(OUT + 'figB4_roadmap.png')
plt.close(fig)
print('done')

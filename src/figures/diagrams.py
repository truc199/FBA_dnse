"""Diagrams in the report: the root-cause tree (Figure 10), how Payday Portfolio works (Figure 12)
and DNSE's technology ecosystem (Figure 14). Numbers quoted in the boxes are read from data/."""
import sys
import textwrap
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import analysis as AN  # noqa: E402
from figures.style import save  # noqa: E402
from config import RED, PEACH, CHARCOAL, BOX_GREY, BOX_EDGE  # noqa: E402

TRUST_EDGE = PEACH


def _box(ax, x, y, w, h, title, sub, body, edge=BOX_EDGE, fs=10.5, wrap=40, ls="-", fc=BOX_GREY, tfs=11.5):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.004,rounding_size=0.012", fc=fc, ec=edge, lw=2, ls=ls))
    ax.text(x + w / 2, y + h - 0.025, title, ha="center", va="top", fontsize=tfs, fontweight="bold", linespacing=1.2)
    yy = y + h - 0.025 - 0.035 * (title.count("\n") + 1) - 0.012
    if sub:
        ax.text(x + w / 2, yy, sub, ha="center", va="top", fontsize=fs, style="italic")
        yy -= 0.05
    ax.text(x + w / 2, yy, "\n".join(textwrap.wrap(body, wrap)), ha="center", va="top", fontsize=fs, linespacing=1.2)


def fig10_root_cause():
    inc = [AN.income_row(f"FY{y}")["core_pretax_profit"] for y in ("2022", "2023", "2024", "2025")]
    acc = {r["metric"]: float(r["value"]) for r in AN.manual("dnse_accounts.csv") if r["date"].startswith("2025")}
    total = AN.account_metric("accounts_year_end")["2025-12-31"]
    unused = round(100 - acc["active_customers"] / total * 100)
    rich = acc["net_assets_10m_plus"] / total * 100
    fig = plt.figure(figsize=(10, 6.4))
    ax = fig.add_axes([0, 0, 1, 1]); ax.set_xlim(0, 1); ax.set_ylim(0, 1); ax.axis("off")
    bx, bw, bh = 0.17, 0.66, 0.13
    _box(ax, bx, 0.845, bw, bh, "Financial consequence", None,
         f"Core pre-tax profit between VND {min(inc):.0f} and {max(inc):.0f} billion a year since 2022; "
         "return on equity 3.8% in H1 2026 (annualised)", wrap=80)
    _box(ax, bx, 0.645, bw, bh, "Symptom: accounts opened but not funded", None,
         f"{unused} of every 100 accounts used no product in December 2025; {rich:.1f}% held net assets of VND 10 million or more", wrap=80)
    _box(ax, bx, 0.445, bw, bh, "Proximate cause: zero-fee acquisition", None,
         "Opening an account costs nothing, so a sign-up carries no commitment to fund it", wrap=80)
    for y0, y1 in [(0.775, 0.845), (0.575, 0.645)]:
        ax.annotate("", xy=(0.5, y1), xytext=(0.5, y0), arrowprops=dict(arrowstyle="-|>", lw=1.6, color=CHARCOAL))
    rt = AN.reliability_trust()["DNSE"], AN.reliability_trust()["VPS"]
    roots = [("Root cause 1\nCustomer-capital mismatch", "Hypothesis",
              "AI tools, contests and a Gen Z price board attract young traders with little capital; "
              "wealthier savers use bank-affiliated or advisory brokers", BOX_EDGE),
             ("Root cause 2\nTrust barrier", "Supported by review data",
              f"Trust complaints in {rt[0]['trust_pct']:.0f}% of negative reviews since 2025 against "
              f"{rt[1]['trust_pct']:.0f}% at VPS; SSC penalty in August 2026", BOX_EDGE),
             ("Root cause 3 (priority)\nNo route from intention\nto regular funding", "Products supported; intent a hypothesis",
              f"Every product assumes a lump sum and a wish to trade; {acc['idle_cash_registered']:,.0f} idle-cash users "
              f"and {acc['golden_egg_active']:,.0f} active Golden Egg users", RED)]
    rw, rh, ry = 0.315, 0.36, 0.02
    for x, (t, s, b, e) in zip([0.012, 0.3425, 0.673], roots):
        _box(ax, x, ry, rw, rh, t, s, b, edge=e, wrap=36)
        ax.annotate("", xy=(0.5 if x == 0.3425 else (0.33 if x < 0.3 else 0.67), 0.445), xytext=(x + rw / 2, ry + rh),
                    arrowprops=dict(arrowstyle="-|>", lw=1.6, color=CHARCOAL))
    return save(fig, "fig10_root_cause.png", tight=False)


def fig12_payday_flow():
    fig = plt.figure(figsize=(10, 5.9))
    ax = fig.add_axes([0, 0, 1, 1]); ax.set_xlim(0, 1); ax.set_ylim(0, 1); ax.axis("off")
    w, h, y = 0.225, 0.465, 0.515
    xs = [0.012, 0.262, 0.512, 0.762]
    titles = ["1  Advise", "2  Fund on payday", "3  Hold briefly", "4  Invest and rebalance"]
    bodies = [["Ensa suitability check of goal, horizon, income, loss tolerance and liquidity need",
               "Proposes one of three model portfolios with risks and fees disclosed; the customer confirms"],
              ["Standing order set once in the salary bank's app",
               "Money goes to a virtual account in the customer's own name; ZaloPay as a second route",
               "DNSE never debits a bank account"],
              ["Cash earns the Never-Sleeping Account rate for one to three days", "Withdrawable to the linked bank 24/7"],
              ["New money buys the most underweight asset class; no sales, so no 0.1% sales tax",
               "Funds and Golden Egg bonds for small amounts; ETFs in 100-unit lots", "Changes need one-tap confirmation"]]
    for i, (x, t, b) in enumerate(zip(xs, titles, bodies)):
        ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.004,rounding_size=0.012", fc=BOX_GREY,
                                    ec=RED if i == 0 else BOX_EDGE, lw=2))
        ax.text(x + w / 2, y + h - 0.035, t, ha="center", va="top", fontsize=13, fontweight="bold")
        lines = []
        for k, para in enumerate(b):
            if k:
                lines.append("")
            lines += textwrap.wrap(para, 30)
        ax.text(x + w / 2, y + h - 0.095, "\n".join(lines), ha="center", va="top", fontsize=11, linespacing=1.25)
        if i < 3:
            ax.annotate("", xy=(xs[i + 1] - 0.004, y + h / 2), xytext=(x + w + 0.004, y + h / 2),
                        arrowprops=dict(arrowstyle="-|>", lw=1.6, color=CHARCOAL))
    ax.add_patch(FancyBboxPatch((0.012, 0.265), 0.975, 0.19, boxstyle="round,pad=0.004,rounding_size=0.012", fc=BOX_GREY, ec=RED, lw=2))
    ax.text(0.5, 0.43, "Commitment tiers (free; unlocked by consecutive monthly contributions)", ha="center", va="top",
            fontsize=12.5, fontweight="bold")
    tiers = [("Starter, 3 contributions", "Idle-cash rate +0.3 to 0.5 point;\nmilestone summary from Ensa"),
             ("Disciplined, 6 contributions", "Discount on fund and bond fees;\nhalf-yearly portfolio review"),
             ("Committed, 12 contributions", "4.3% idle-cash rate without trading\nconditions; early access to Golden Egg")]
    for j, (a, b) in enumerate(tiers):
        cx = 0.17 + j * 0.33
        ax.text(cx, 0.37, a, ha="center", va="top", fontsize=11.5, fontweight="bold")
        ax.text(cx, 0.335, b, ha="center", va="top", fontsize=10.8, linespacing=1.2)
        if j < 2:
            ax.annotate("", xy=(cx + 0.225, 0.345), xytext=(cx + 0.105, 0.345), arrowprops=dict(arrowstyle="-|>", lw=1.4, color=RED))
    ax.add_patch(FancyBboxPatch((0.012, 0.02), 0.975, 0.215, boxstyle="round,pad=0.004,rounding_size=0.012", fc="white", ec=TRUST_EDGE, lw=2))
    ax.text(0.5, 0.215, "Trust controls at every step", ha="center", va="top", fontsize=12.5, fontweight="bold")
    left = ["No account-closure fee; no sign-up cash rewards", "All terms, fees and tier rules on one screen",
            "Pause, skip or cancel in one tap; one free skip a year"]
    right = ["Dashboard of the segregated client account", "Transfer success of 99.5% as a launch gate",
             "Advice flow and product notified to the SSC"]
    for k, (l, r) in enumerate(zip(left, right)):
        ax.text(0.05, 0.16 - k * 0.045, "•  " + l, ha="left", va="top", fontsize=11)
        ax.text(0.53, 0.16 - k * 0.045, "•  " + r, ha="left", va="top", fontsize=11)
    return save(fig, "fig12_payday_flow.png", tight=False)


def fig14_ecosystem():
    fig = plt.figure(figsize=(10, 6.3))
    ax = fig.add_axes([0, 0, 1, 1]); ax.set_xlim(0, 1); ax.set_ylim(0, 1); ax.axis("off")
    rows = [("Bring money in", [("Payday standing order to a personal virtual account", "new"),
                                ("ZaloPay round-ups for customers without a salary", "test")]),
            ("Hold and invest", [("Never-Sleeping Account as a short cash buffer", "exist"),
                                 ("Model portfolios of funds, Golden Egg bonds and VN30 ETFs", "exist")]),
            ("Guide and reward", [("Ensa advice and rebalancing with new money", "exist"),
                                  ("Free commitment tiers with one skip a year", "new")]),
            ("Show and protect", [("Segregated-cash dashboard and one-screen terms", "new"), ("VNeID identity checks", "test")]),
            ("Serve active traders", [("Entrade X, Future X and Lightspeed API", "sep"),
                                      ("Margin Deal; margin on listed ETFs later, under existing rules", "sep")])]
    style = {"exist": dict(fc=BOX_GREY, ec=BOX_EDGE, ls="-"), "new": dict(fc="white", ec=RED, ls="-"),
             "test": dict(fc="white", ec=RED, ls="--"), "sep": dict(fc="#E9E9E9", ec="#A0A0A0", ls="-")}
    top, rh, gap = 0.935, 0.13, 0.035
    for i, (lab, items) in enumerate(rows):
        y = top - rh - i * (rh + gap)
        ax.text(0.015, y + rh / 2, lab, ha="left", va="center", fontsize=12, fontweight="bold")
        for j, (t, k) in enumerate(items):
            x, w = 0.21 + j * 0.395, 0.375
            st = style[k]
            ax.add_patch(FancyBboxPatch((x, y), w, rh, boxstyle="round,pad=0.004,rounding_size=0.012", fc=st["fc"], ec=st["ec"], lw=2, ls=st["ls"]))
            ax.text(x + w / 2, y + rh / 2, "\n".join(textwrap.wrap(t, 40)), ha="center", va="center", fontsize=11, linespacing=1.2)
        if i < 3:
            ax.annotate("", xy=(0.5875, y - gap + 0.004), xytext=(0.5875, y - 0.004), arrowprops=dict(arrowstyle="-|>", lw=1.4, color=CHARCOAL))
    for k, (lab, st) in enumerate([("Existing product, new role", style["exist"]), ("New build", style["new"]),
                                   ("Phase-2 test", style["test"]), ("Kept separate from saving", style["sep"])]):
        x = 0.03 + k * 0.245
        ax.add_patch(FancyBboxPatch((x, 0.012), 0.035, 0.03, boxstyle="round,pad=0.002,rounding_size=0.005", fc=st["fc"], ec=st["ec"], lw=1.8, ls=st["ls"]))
        ax.text(x + 0.045, 0.027, lab, va="center", fontsize=11)
    return save(fig, "fig14_ecosystem.png", tight=False)


ALL = [fig10_root_cause, fig12_payday_flow, fig14_ecosystem]

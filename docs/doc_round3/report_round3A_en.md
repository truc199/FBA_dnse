# Payday Portfolio: product design, launch plan and business case for DNSE Securities

*Round 3A companion report, KTQT FTUers, 17 October 2026. Not submitted: the Round 3A deliverable is the slide deck. This report sets out the full reasoning, evidence and numbers behind the deck. Tables are written from the CSV files in `outputs/round3/tables/` by `src/round3/deck_tables.py`; edit those, not the tables here.*

## Executive summary

DNSE Securities opens accounts at scale but does not hold the money that should come with them. It opened one in five of Vietnam's new securities accounts in 2025 and held 12.3 per cent of all accounts by mid-2026. Yet only 1.8 per cent of its 1.51 million accounts held VND 10 million or more in December 2025, and it holds 2.3 per cent of the cash that investors keep at brokers. Brokerage revenue has been below its direct cost for 16 consecutive quarters. Round 2 traced the gap to three causes: tools that attract young traders with little capital, trust that breaks at the first deposit, and the absence of any route from a salaried customer's intention to regular deposits. This report designs the product that answers the third cause while respecting the second, and sets out how DNSE would build, test, launch and scale it.

The year 2026 adds urgency and one new fact. Investor cash at brokers fell 38 per cent in three quarters while banks paid 5.9 per cent for twelve months. SSI, TCBS, VPS and VPBank launched recurring or goal-based plans, and banks must open their application programming interfaces by 1 March 2027. Our reading of 58 negative reviews of DNSE's app from 2026 finds that 83 per cent describe something that broke and 19 per cent concern terms, rewards or trust, so reliability is now the first barrier.

Payday Portfolio is a goal-based monthly plan from VND 500,000. The customer sets a goal, answers a short suitability check and confirms a plan signed by a licensed adviser. A standing order from the salary bank pays into a virtual account in the customer's name. Cash waits in the Never-Sleeping Account and each contribution buys the most underweight asset: bank bonds through Golden Egg, bond and equity funds, or a VN30 exchange-traded fund, in a mix set by the goal's horizon. There is no platform fee, no cash reward and no margin. Persistence comes from non-cash features, and DNSE publishes its on-time crediting rate and withdrawal times every month.

The business case is honest about money. A monthly cohort model over 60 months with sourced costs gives 14,871 new accounts above VND 10 million by month 36 in the base case, which lifts the total from 27,100 to about 42,000, and VND 352 billion of plan balances. The base case does not pay back within five years: the net present value at 12 per cent is minus VND 25.0 billion and cumulative cash at month 60 is minus VND 32.0 billion. Read correctly, Payday buys funded accounts at a net cost of about VND 1.3 million each. The upside case pays back in month 44 with a net present value of VND 11.0 billion. The downside case costs VND 10.0 million per funded account and would be stopped at month 6. Fixed cost, not acquisition cost, is the swing factor.

We therefore ask the Board for VND 6.6 billion to build the product and run a randomised pilot with 45,000 dormant accounts over months 1 to 6. We also ask for five decisions: a virtual-account bank that waives the collection fee; one or two fund managers; the notice to the State Securities Commission with pre-consultation on Golden Egg's role; a licensed adviser's sign-off of the model plans; and a yardstick of about VND 1.3 million per new funded account. The Board decides at month 6 whether to stop or scale, against thresholds derived from the model.

## 1. Introduction

### 1.1 Purpose of this report

Round 3A asks a product owner to present a designed product, a strategy for its development, launch and growth, a go-to-market plan for its first year and a business case that a Board can approve. The deck carries that case in 15 slides. This report gives the full argument: the evidence behind each design choice, how the numbers were built, and what the Board would be committing to. It builds on our Round 2 report (KTQT FTUers, 2026), keeps what still holds and corrects what did not (Section 2.5).

### 1.2 Business question and scope

The question is: *what product should DNSE build to turn the accounts it has opened into balances, how should it be launched and scaled, and what should the Board approve now?*

The scope is Payday Portfolio from its minimum viable product to month 36, with the model run to month 60. Salaried holders of dormant accounts are the launch customers. The design uses products and licences DNSE already holds and works within Vietnam's rules for investment advice, margin lending and open banking. Margin products, derivatives, a redesign of the Entrade X app and DNSE's own financing are outside the scope.

### 1.3 Evidence base and method

Five sources of evidence support the report (Appendix A):
- DNSE's 2025 annual report and filings, and the market data reconciled in Round 2;
- 44 web sources on rates, fees, product terms and rivals, each with its access date and a note on who checked it: we checked 30 in full and 3 in part ourselves, and the other 11 were checked only by an AI research assistant;
- a hand reading of all 58 negative reviews of DNSE's app posted between 1 January and 21 September 2026;
- a desk review of 20 rival products, 9 of which we checked against their sources;
- a monthly cohort model of Payday with 60 inputs, each labelled as sourced, derived or an assumption.

Two limits matter. We ran no customer survey, so enrolment, persistence and the size of contributions are assumptions that the pilot must measure. Balances are counted before investment returns, so they understate what savers would hold if markets rise.

## 2. Problem and why now

### 2.1 Accounts are opened but not funded

The closer a measure sits to money, the smaller DNSE becomes (Figure 1). DNSE held 12.3 per cent of Vietnam's securities accounts in mid-2026 and opened 20.1 per cent of new accounts in 2025, but it held 2.3 per cent of investor cash at brokers, 1.4 per cent of margin lending and 0.6 per cent of the industry's pre-tax profit. In December 2025, 85,739 accounts (5.7 per cent) used at least one product and 27,100 (1.8 per cent) held net assets of VND 10 million or more. The remaining 1,427,181 accounts used no product that month (DNSE Securities, 2026c).

![Figure 1. DNSE's share of each market, per cent; the dashed line is its 12.3 per cent share of accounts](outputs/figures/fig04_market_position.png)

Source: KTQT FTUers (2026), Figure 4, from VnExpress (2026a), DNSE Securities (2026a, 2026c), Vietstock (2026b), CafeF (2026), VnEconomy (2026) and Hanoi Stock Exchange (2026); authors' calculations. Hatched bar estimated.

### 2.2 Empty accounts make the platform a fixed cost

Free trading does not pay for itself. Brokerage revenue has been below the direct cost of brokerage for 16 consecutive quarters, from the third quarter of 2022 to the second quarter of 2026, a cumulative loss of VND 190.3 billion; in 2025 revenue was VND 404.0 billion against a cost of VND 464.9 billion. Core pre-tax profit, which excludes proprietary trading, has stayed between VND 128 and 221 billion a year since 2022 while accounts multiplied. The platform and overhead cost proxy of VND 197.5 billion in 2025 works out at VND 7.3 million a year for each account with VND 10 million or more (DNSE Securities, 2026a; Vietcap Securities, 2026). Funding the accounts DNSE already holds is therefore the cheapest way to spread that cost.

### 2.3 What changed in 2026

Three things make the problem urgent now (Figure 2).

- **Money is leaving brokers.** Investor cash at brokers fell from VND 138.9 trillion in the third quarter of 2025 to VND 86.6 trillion in the second quarter of 2026, a fall of 38 per cent in three quarters (VnEconomy, 2026). In early October 2026 the Big Four banks paid 5.9 per cent on twelve-month deposits at the counter and certificates of deposit paid 7.4 per cent (Thi truong Tai chinh Tien te, 2026b).
- **Rivals have started an accumulation race.** On 23 April 2026 SSI promoted automatic periodic fund investing through eSIP in its "Tích sản thảnh thơi" (easy accumulation) campaign (SSI Securities, 2026). TCBS upgraded TCWealth into goal-based portfolios, which more than 20,000 customers tried within two months (TCBS, 2026). VPS launched Smart Indexing on 11 August (Tin nhanh Chung khoan, 2026) and VPBank launched its Hũ Mục Tiêu (Goal Jar) savings in September (VPBank, 2026). DNSE has no plan product.
- **Open banking has a date.** Banks must comply with Circular 64/2024 on open application programming interfaces by 1 March 2027 (State Bank of Vietnam, 2024), which will make salary-linked investing easier for whoever has a product ready.

Meanwhile DNSE earned VND 111.6 billion of pre-tax profit in the first half of 2026, about a fifth of its 2026 target of VND 550 billion (DNSE Securities, 2026a; Vietstock, 2026a).

![Figure 2. Launches of recurring and goal-based plans in 2026 and the banks' Open API deadline (left); investor cash at Vietnamese brokers, VND trillion (right)](outputs/round3/figures/why_now_timeline.png)

Source: SSI Securities (2026); TCBS (2026); Tin nhanh Chung khoan (2026); Tuoi Tre (2026); VPBank (2026); State Bank of Vietnam (2024); VnEconomy (2026). Q4 2025 investor cash was not reported.

### 2.4 Reliability now comes first

Round 2 found that trust complaints were the distinctive problem in DNSE's reviews. To see whether that still holds, we read all 58 negative reviews posted in 2026 (34 on Google Play, 24 on the App Store) and coded their causes by hand, allowing several causes per review (Figure 3; Appendix C). Something had broken in 48 of them, 83 per cent (95 per cent interval 71 to 90 per cent): crashes, freezes and lag (45 per cent), orders and prices (19 per cent), deposits or withdrawals not credited (17 per cent), identity checks and account opening (17 per cent), and log-in or one-time passwords (14 per cent). Terms, rewards and scam claims appeared in 19 per cent (11 to 31 per cent). Nine reviews were posted on 4 and 5 March 2026, after an outage in which orders were stuck for two hours following a failure in the buying- and selling-power check before orders reach the exchange (DNSE Securities, 2026e).

The trust problem has not vanished; it has fallen behind. By the keyword rule of Round 2, trust themes made up 55 per cent of negative Google Play reviews in the first half of 2025, during the dispute over sign-up rewards, and 15 per cent in 2026. Both readings lead to the same design rule: Payday must work every payday, and when it does not, customers must see what happened and what to do.

![Figure 3. Causes in 58 negative reviews of DNSE's app, January to September 2026](outputs/round3/figures/reviews_2026_causes.png)

Source: Google Play; App Store; authors' coding of each review.

### 2.5 What we kept and what we changed since Round 2

The mechanism of Round 2 still holds: a standing order from the salary bank into a virtual account in the customer's name, a plan the customer confirms, rebalancing with new money only, a notice to the regulator and a randomised pilot. The numbers, the rewards, the bond core and the positioning changed (Table 1). The largest change is the business case. Round 2 assumed that every saver contributed for 18 months and targeted 85,000 accounts above VND 10 million; with monthly cohorts, real costs and the fact that a saver needs 11 contributions to pass VND 10 million, the base case reaches about 42,000 accounts above VND 10 million by month 36.

**Table 1. What changed since Round 2, and why**

<!-- table: slide05_what_changed -->
| Area | Round 2 | Round 3A, and why |
|---|---|---|
| Main barrier | Trust | Reliability: 83% of 2026 negative reviews describe a failure; trust 19% |
| Business case | Static: 150,000 savers for 18 months; target of 85,000 accounts above VND 10 million | Monthly cohorts over 60 months: about 42,000 accounts above VND 10 million by month 36 (27,100 + 14,871), because a saver needs 11 contributions to pass VND 10 million |
| Pilot | 20,000 accounts; go ahead at 15% enrolment | 45,000 accounts; scale at 1.5%, stop below 1.0% (break-even 1.0%) |
| Rewards | Cash tiers, including a 4.3% idle-cash rate | Non-cash persistence package; cash tiers would cost 41% of revenue per saver |
| Bond core | Golden Egg, which also holds DNSE's own bonds | Bank-issued bonds only, to avoid a conflict of interest |
| Differentiator | The salary-day trigger | Recurring transfers are standard (VinaSIP since 2021); we compete on asset range and published delivery metrics |
<!-- /table -->

Source: KTQT FTUers (2026); authors' cohort model; Thi truong Tai chinh Tien te (2021); DNSE Securities (2026c).

### 2.6 Conditions any solution must meet

The findings set six conditions for the design:
1. new money must come from salaries, not from balances already at DNSE;
2. the customer must confirm the plan and every change, because DNSE may not manage money on a customer's behalf without a mandate;
3. terms, costs and the state of the customer's money must be visible before and after every step;
4. contributions must be credited on time, with a fallback when they are not;
5. each contribution must cost less to collect and serve than it earns over its life;
6. the product must be notified to the regulator before launch.

## 3. Target users and value

### 3.1 Segments and personas

Three groups of existing and new customers form the launch and growth base (Table 2). The personas are built from data, not invented biographies: their jobs to be done are hypotheses that the pilot will test.

- **P1, salaried holders of dormant accounts,** are the launch customers. 1.43 million accounts used no product in December 2025, DNSE's base is young (Gen Z held 31.5 per cent of accounts in mid-2025; VnExpress, 2025) and 45.2 per cent of adults in the labour force receive wages into an account (World Bank, 2025). Their barriers are procrastination (O'Donoghue & Rabin, 1999) and distrust after the 2025 reward disputes.
- **P2, active traders,** want a long-term core next to their trading. 85,739 customers were active in December 2025; DNSE ranked second in derivatives brokerage with a 25.38 per cent share in the second quarter of 2026 (Hanoi Stock Exchange, 2026). The risk is that plan money drifts back to trading.
- **P3, new account holders,** can start a plan at opening. DNSE opened about 31,180 accounts a month in the first half of 2026. Their barriers are reward-seeking and identity checks that fail (17 per cent of 2026 negative reviews).

Employers (payroll plans) come later: they pay back only if at least 39 per cent of staff join after a human-resources session (Section 9.3).

**Table 2. Personas, sizes and model inputs**

<!-- table: slide06_personas -->
|  | P1 Salaried dormant holder (launch) | P2 Active trader adding a core | P3 New account holder |
|---|---|---|---|
| Size | 1.43 million accounts used no product in December 2025 | 85,739 active customers | About 31,180 new accounts a month (H1 2026) |
| Job to be done (hypothesis) | "Invest part of my salary without deciding each month" | "Grow a long-term core while I trade" | "Start small and see it work" |
| Barrier (evidence) | Procrastination; distrust after the 2025 rewards | Plan money drifting back to trading | Reward-seeking; eKYC failures (17% of 2026 negative reviews) |
| Model input (assumption) | 25% salaried and reachable; 2% enrol | 4% enrol over 12 months | 2% set up within 60 days |
| Savers by month 36 (base) | 6,836 | 3,430 | 18,708 |
<!-- /table -->

Source: DNSE Securities (2026c); VnExpress (2026a); authors' cohort model.

### 3.2 Sizing: from 1.51 million accounts to savers

Figure 4 traces the launch funnel. Of DNSE's 1,512,920 accounts in December 2025, 1,427,181 used no product. We assume a quarter of these, 356,795, belong to salaried and reachable holders, and that 2 per cent of those contacted enrol; both numbers are assumptions that the pilot measures. That yields 6,836 savers from dormant accounts by month 36. Most savers, however, come from the account-opening step: 18,708 of the 31,133 savers enrolled by month 36 (60 per cent) set up a plan when they opened their account, against 3,430 active customers and 2,160 employees of partner employers.

![Figure 4. From DNSE's 1.51 million accounts to dormant savers by month 36 (left); all 31,133 savers by month 36, by channel (right), base case](outputs/round3/figures/sizing_funnel.png)

Source: DNSE Securities (2026c); authors' cohort model (assumptions labelled).

### 3.3 What customers tell us

We could not run a survey in time, so the evidence on demand is indirect (Appendix D). Published surveys find that 77 per cent of Vietnamese investors find managing a portfolio hard and 81 per cent want professional advice (Nhan Dan, 2025; VnEconomy, 2025). Rivals' launches show that the market expects demand. DNSE's own reviews support specific design choices: a customer asked DNSE in 2022 to create a bank account identifier because deposits kept failing; others complain of money deducted by the bank but not credited; a five-star review calls the Never-Sleeping Account "the best"; and a one-star review reports losing 4 per cent on a one-month Golden Egg. The limit is plain: reviews are mostly complaints, and none we found asks for a recurring plan.

### 3.4 Value for each stakeholder

Payday has to create value for five parties, not only for the saver (Table 3). The partner bank matters most for the economics: contributions sit in the bank's virtual accounts, which gives it a reason to waive the collection fee, the cheapest lever in the model (Section 7.4).

**Table 3. Value for each stakeholder**

<!-- table: report_value -->
| Stakeholder | What Payday offers | Evidence |
|---|---|---|
| Customer | A monthly plan from VND 500,000 toward a named goal; bank bonds for short goals, funds and an ETF for long ones; confirm every change; no platform fee; pause, skip or withdraw in one tap | Golden Egg pays 6.20–7.60% by term from VND 100,000; Big Four 12-month deposits pay 5.9%; bond coupons are taxed 5% |
| DNSE | Funded accounts at a net cost of about VND 1.3 million each; payment rails that also tackle deposit-crediting failures | 14,871 new accounts above VND 10 million by month 36 (base); deposits not credited in 17% of 2026 negative reviews |
| Partner bank | Contributions land in the bank's virtual accounts as current-account balances, which gives the bank a reason to waive the collection fee | List price VND 3,300 per contribution with VAT; waiving it raises the CAC ceiling from VND 128,000 to 199,000 |
| Fund managers | A new flow of periodic subscriptions from DNSE's 1.51 million accounts | No subscription fee on the bond and equity funds compared; DNSE is a registered distribution agent |
| Regulator | Advice inside the suitability rules, a licensed adviser's sign-off, no discretionary management and published service metrics | Circular 121/2020, Articles 4, 24 and 27; Law on Securities 2019, Article 72 |
<!-- /table -->

Source: DNSE Securities (n.d.-a, n.d.-b); Thi truong Tai chinh Tien te (2026b); VPBank (2024); Ministry of Finance (2020); National Assembly of Vietnam (2019); authors' cohort model.

## 4. Product design

### 4.1 From insight to design

Every design choice traces to evidence and to one indicator that the pilot measures (Table 4). Three choices come from the root causes of Round 2, one from the 2026 review data and one from the economics of small tickets: at a net yield of 0.44 per cent, a contribution of VND 1 million earns about VND 368 a month for DNSE, while the bank's list price for collecting it is VND 3,300.

**Table 4. Insight, design decision and the indicator it moves**

<!-- table: slide04_insight_design -->
| Insight | Evidence | Design decision | KPI it moves |
|---|---|---|---|
| Accounts are opened but not funded | 98% of accounts hold under VND 10 million | A monthly plan funded by a standing order from the salary bank | New accounts above VND 10 million: +14,871 by month 36 |
| Intention stalls without a plan | 77% of investors find managing a portfolio hard | A plan by goal horizon, signed by a licensed adviser and confirmed by the customer | Three contributions in a row: 81% (stop below 60%) |
| Conditional rewards broke trust | Trust themes: 55% of negative Google Play reviews, H1 2025 | No cash rewards; all terms on one screen; free withdrawal | Trust themes below 10% of Payday reviews |
| 2026 update: reliability now dominates | 83% of 2026 negative reviews describe something that broke | Payday scheduler kept apart from the pre-trade check; 99.5% launch gate | 99.5% credited on the same banking day |
| Small tickets carry heavy unit costs | A VND 1 million contribution pays a VND 3,300 bank fee and earns VND 368 a month | Gate 0: collection fee target VND 0 | CAC ceiling rises from VND 128,000 to 199,000 |
<!-- /table -->

Source: DNSE Securities (2026c); Nhan Dan (2025); Google Play and App Store reviews, authors' coding; VPBank (2024); authors' cohort model.

### 4.2 How Payday works

Payday runs in four steps (Figure 5). First, Ensa asks the goal, horizon, tolerance of loss and income, and a licensed adviser's model plan is proposed; the customer confirms it. Second, the customer sets one standing order in the salary bank's app to a virtual account in his or her own name. Third, the cash waits in the Never-Sleeping Account (Tài khoản Không Ngủ), DNSE's interest-bearing idle-cash account, and is usually invested the next business day. Fourth, each contribution buys the asset class furthest below its target weight, so the plan rebalances without selling. A non-cash persistence package and a set of trust controls run alongside.

![Figure 5. How Payday works: advise, fund on payday, hold briefly, invest new money](outputs/round3/figures/solution_overview.png)

Source: authors' design (redraws Round 2, Figure 7, without the cash tiers).

### 4.3 Minimum viable product and what we leave out

The minimum viable product has eleven features (Table 5). Six things are deliberately excluded:
- **margin and leverage,** including as a reward, which would contradict the savings purpose; Circular 121/2020, Article 27, limits lending by securities companies to margin and a few defined purposes, and DNSE's 2026 fine included items for margin trading beyond purchasing power and loans on securities that did not qualify (Market Times, 2026);
- **single stocks and derivatives,** for reasons of suitability and trust;
- **bonds issued by DNSE itself** in the default plan, to avoid a conflict of interest (Section 4.4);
- **sign-up cash, conditional rewards and DNSE-funded cash tiers** (Section 4.5);
- **discretionary management** and any change to the plan without the customer's confirmation, which Circular 121/2020, Article 4, and the Law on Securities 2019, Article 72, rule out for a broker without a mandate;
- **salary-percentage contributions through bank application programming interfaces,** which wait for Phase 3 (Section 9).

**Table 5. Features of the minimum viable product**

<!-- table: report_features -->
| # | Feature | Design note |
|---|---|---|
| F1 | Set a goal: type, amount and date | Shows the monthly amount needed before investment returns |
| F2 | Suitability check: horizon, reaction to a loss, income | Circular 121/2020, Article 24; every recommendation is logged |
| F3 | Plan by goal horizon | Model plans signed by a licensed adviser; the customer confirms |
| F4 | Virtual account in the customer's name and a standing-order guide (bank-app link and QR) | Design target: set-up in 5 minutes, with no more steps than VCB Digibank SIP |
| F5 | Each contribution buys the most underweight asset | New money only, nothing sold; the ETF is bought in 100-unit lots when the cash allows |
| F6 | The Never-Sleeping Account as the waiting place | Cash is usually invested the next business day |
| F7 | Dashboard: progress to the goal, assets by class, where the money sits, fees paid | – |
| F8 | Persistence package without cash | Streak; one free skip a year; payday reminder naming the goal; priority on new Golden Egg issues; Ensa review at month 6 |
| F9 | Pause, skip or cancel in one tap; free withdrawal to the linked bank | Moving plan money to buying power needs a separate step with a goal reminder |
| F10 | Notices: received, invested, not received, salary late | A five-day grace window; the streak survives the wait |
| F11 | Monthly service-metrics page | The seven commitments of Table 7 |
<!-- /table -->

Source: authors' design; Ministry of Finance (2020).

### 4.4 The default plan follows the goal's horizon

The plan's mix depends on when the customer needs the money (Table 6). Goals under a year hold only Golden Egg (Trứng Vàng) bonds of one to six months that mature before the goal date. Goals of one to three years add bond funds, chosen among those that charge no exit fee after twelve months. Goals of three years or more hold up to 40 per cent in equity funds and the VN30 ETF. In the last twelve months before the goal, new money goes only into Golden Egg and nothing is sold.

One rule binds the table: **no product whose early-exit cost falls inside the goal's horizon.** Selling a Golden Egg bond before its minimum holding period pays only 2.0 per cent a year (DNSE Securities, n.d.-a), and VCBF's bond fund charges 2.0 per cent on sales within three months and 1.0 per cent on sales from three to twelve months (VCBF, 2026). Golden Egg renews automatically by default and notifies the customer by email only after renewing (DNSE Securities, n.d.-a); in Payday a renewal must still mature before the goal date, comes with a notice three days ahead and can be switched off with one tap.

The bond core uses only bonds issued by banks. In 2025 Golden Egg was allocated to bonds issued by DNSE itself, Agribank and BVBank (DNSE Securities, 2026c). Keeping DNSE's own bonds out of the default plan costs about VND 4 billion of cumulative cash over five years in the model, a small price against the conflict of interest of selling the broker's own debt to first-time savers. DNSE's 2026 plan to work with Vietcombank, VietinBank and BIDV on Golden Egg bonds and fund certificates would widen the supply (DNSE Securities, 2026f).

The same test applies to the bond funds. At the end of August 2026 VCBF's bond fund held DNSE's bond DSE125018 at 6.97 per cent of its net asset value (VCBF, 2026). A fund manager chooses its holdings independently of DNSE, so the conflict is weaker than selling DNSE's bonds directly, but the plan screen should show any DNSE-issued holding in a fund, and the default plan should prefer funds that hold none. The fund contracts in Phase 0 are the place to settle this.

**Table 6. Default plan by goal horizon**

<!-- table: slide07_glide_path -->
| Goal horizon | Golden Egg (Trứng Vàng), bank bonds | Bond funds | Equity funds | VN30 ETF |
|---|---|---|---|---|
| Under 1 year | 100% | – | – | – |
| 1 to 3 years | 50% | 50% | – | – |
| 3 years or more | 30% | 30% | 20% | 20% |
| Last 12 months before the goal | New money only, into Golden Egg | Nothing sold | Nothing sold | Nothing sold |
<!-- /table -->

Source: authors' design; DNSE Securities (n.d.-a, n.d.-b); VCBF (2026).

### 4.5 Persistence without cash

Round 2 proposed cash tiers at three, six and twelve contributions. The model shows they cannot pay for themselves: a scaled-down version costs 41 per cent of the present value of revenue per saver and lowers the ceiling on acquisition cost below the cost of reaching a dormant saver (Appendix B, Table B2). The persistence package is therefore non-cash: a visible streak, one free skip a year, a payday reminder that names the goal, priority on new Golden Egg issues and a plan review with Ensa at month six. Reminders that name a goal raise saving in field experiments (Karlan et al., 2016). A small cash gift is kept only as a test in a separate arm: it would pay only if the bank waives its fee and the share of savers reaching twelve contributions rises from 64.5 to 73.3 per cent. Every interest incentive is capped at VND 50 million.

### 4.6 Trust controls and published metrics

Seven commitments turn trust into numbers that DNSE publishes on a schedule (Table 7). As far as we found, no Vietnamese provider publishes its transfer-success rate or its withdrawal times, so this is one of Payday's two lasting differences (Section 6).

**Table 7. Commitments and the metrics DNSE would publish**

<!-- table: appG3_trust_metrics -->
| Commitment | Customer sees | Published metric | Target | Cadence | Owner |
|---|---|---|---|---|---|
| Money arrives when we say | A "received" notice within minutes of the bank credit | Share of scheduled contributions credited on the same banking day | >= 99.5% (launch gate) | Monthly | CTO |
| Money is invested quickly | An "invested" status with the asset bought | Median time from credit to invested | <= 1 business day | Monthly | CTO |
| Withdrawals are fast and free | "Arrives by 22:00 today" for Golden Egg sales placed 09:00-14:30 (DNSE FAQ: about 21:00-22:00 on the sale day); the fund settlement date before confirming | Median time from request to money in the linked bank | Same day for Golden Egg sales | Monthly | Head of Product |
| Leaving is easy | Pause, skip or cancel in one tap | Share of cancellations completed in the app without a call | 100% | Monthly | Head of Product |
| No hidden costs | One screen with every fee and tax in VND before confirming | Plans confirmed with the fee screen shown (audit) | 100% | Quarterly | Compliance and Legal |
| Problems are owned, not hidden | Status page and a post-incident note | Incidents affecting contributions with a note published within 5 business days | 100% | Per incident | CTO |
| Complaints are counted | - | Trust themes in Payday-related negative reviews | < 10% | Quarterly | Customer Service |
<!-- /table -->

Source: authors' design; DNSE Securities (n.d.-a).

### 4.7 Reliability requirements

Reliability is a launch gate, not a feature:
- at least 99.5 per cent of contributions credited on the same banking day, proven in shadow paydays with staff money before the pilot and measured every month after launch, with an error budget of 0.5 per cent;
- a contribution scheduler kept apart from the pre-trade buying-power check that failed on 4 March 2026, a day when the VN-Index swung by up to 67 points within the session (Pinetree Securities, 2026);
- idempotent processing and daily reconciliation of the virtual accounts, with unmatched money held in the Never-Sleeping Account and checked by hand within a business day;
- no app release in the days before peak payday dates, staged releases of 5, 25 and then 100 per cent, and monitoring by app version, after seven negative reviews pointed to a single iOS version (2.113.28);
- a status page and a post-incident note within five business days.

### 4.8 Regulatory fit

The design stays inside the rules for advice and lending (Table 8). The advice flow meets the suitability rule of Circular 121/2020, Article 24, because Ensa only collects facts while a licensed adviser signs the model plans and every recommendation is logged. Notifying the regulator is a launch condition, not a formality: VND 275 million of DNSE's VND 802.5 million fine of August 2026 concerned three services offered without reporting them to the State Securities Commission (Market Times, 2026). Two dependencies need early action. DNSE paused new Golden Egg openings at the regulator's request in December 2023 (DNSE Securities, 2023), so Golden Egg's role in an advised plan should be discussed with the State Securities Commission before launch, with bond funds as the fallback core. And DNSE, although registered as a fund distribution agent, is not yet on the distributor lists of the fund managers we checked, so the fund contracts belong in Phase 0.

**Table 8. Rules and how the design meets them**

<!-- table: appE1_legal -->
| Requirement | Rule | Design response | Status |
|---|---|---|---|
| Advice must fit the client | Circular 121/2020/TT-BTC, Article 24 (client information for investment advice) | Ensa records goal, horizon, income and loss tolerance; a licensed adviser designs and signs the model plans; advice is logged | Adopt |
| No investing on a client's behalf without a mandate | Circular 121/2020/TT-BTC, Article 4 | The customer confirms the plan and every change; the system only invests new money as the confirmed plan says | Adopt |
| Lending only for margin and defined purposes | Circular 121/2020/TT-BTC, Article 27 | No credit line on savings; margin is not a reward | Exclude |
| Portfolio management is not a securities-company business | Law on Securities 2019, Article 72 | No discretionary service; a fully managed version only through a licensed fund manager | Exclude (Phase 4 via a fund manager) |
| Bank Open API | Circular 64/2024/TT-NHNN: banks must comply by 1 March 2027; customer consent lasts at most 180 days | Phase 1 uses standing orders the customer sets in the bank app; salary-linked percentage contributions only after bank agreements (Phase 3) | Later phase |
| New services must be reported | Decision 461/QD-XPHC (17 August 2026): VND 275 million of the VND 802.5 million fine was for services not reported to the SSC | Notify the SSC before launch; written confirmation is a Gate 0 condition | Launch gate |
| Golden Egg's regulatory history | New Golden Egg openings were paused at the regulator's request from 25 December 2023 (DNSE notice) | Pre-consult the SSC on Golden Egg's role in Payday; keep bond funds ready as the alternative core | Pre-consult |
| Fund distribution | DNSE registered as a fund-certificate distribution agent (15 December 2021) but is not on the distributor lists of SSIAM, Dragon Capital or VCBF | Sign distribution agreements with 1 to 2 managers in Phase 0; launch with Golden Egg and an ETF if they are late | Phase 0 dependency |
<!-- /table -->

Source: Ministry of Finance (2020); National Assembly of Vietnam (2019); State Bank of Vietnam (2024); Market Times (2026); DNSE Securities (2023, n.d.-b).

## 5. Solution demonstration

### 5.1 The journey and its moments of truth

A saver's first ninety days run through six stages: notice the offer, make a plan, set up the money, the first payday, build the habit, and withdraw or keep going (Appendix E). Three moments decide whether the customer trusts the product: the first money in, the first money out and the first failure (Table 9). A failure handled well can build more trust than a smooth run, so the failure screens are designed in advance rather than left to customer service.

**Table 9. Moments of truth**

<!-- table: slide08_moments_of_truth -->
| Moment of truth | What the customer sees | Measure we publish |
|---|---|---|
| First money in | "Received" within minutes; invested the next business day | Contributions credited on the same banking day: ≥99.5% |
| First money out | Arrival time and cost in VND before confirming; free to the linked bank | Median time from request to the bank |
| First failure | Streak kept; one clear next step: send now or skip | Incident note within 5 business days |
<!-- /table -->

Source: authors' design.

### 5.2 Screens and microcopy

Six screens take a saver from a goal to the 90-day milestone (Figure 6). The saver picks a goal, for example a home costing VND 36 million by October 2029, and sees that about VND 1 million a month gets there before investment returns. A short suitability check follows, with the legal reason shown. The plan screen shows the mix, what a bad month would cost in dong and every fee; the fourth screen gives a personal account number and opens the bank app. On payday the customer sees the money received and invested, and at day 90 the streak unlocks priority on new Golden Egg issues. Four further screens handle a transfer that has not arrived, a late salary, a skipped or paused month and a withdrawal to the bank (Figure 7). The words follow plain rules: screen titles in title case, buttons as verbs, errors that say what happened, why and what to do, amounts always in dong, and no use of the word "reward".

![Figure 6. Low-fidelity wireframes of the six main screens; values in brackets are filled in by the live app](outputs/round3/figures/wireframes_journey.png)

Source: authors' design.

![Figure 7. Low-fidelity wireframes of four error and edge-case screens](outputs/round3/figures/wireframes_errors.png)

Source: authors' design; DNSE Securities (n.d.-a) for the early-sale rule.

### 5.3 Service blueprint and failure handling

Behind the screens, the blueprint maps each step across physical evidence, customer actions, the frontstage, the backstage and support processes, with the decision points, the failure handling and the owner of each step (Figure 8). Two decisions are automatic: whether the money arrived by the grace date, and whether there is enough cash for an ETF lot. Each failure has a fallback and an owner (Table 10). The new build is limited to the virtual accounts and the scheduler; Ensa, Golden Egg, the Never-Sleeping Account and ETF trading are reused.

![Figure 8. Service blueprint of one payday cycle](outputs/round3/figures/service_blueprint.png)

Source: authors' design; DNSE Securities (2026e).

**Table 10. Failure handling**

<!-- table: slide09_failure_handling -->
| When this fails | What happens | Owner |
|---|---|---|
| Money not in by the grace date (the 15th) | Suggest skipping the month; streak kept | CTO; Operations |
| An order fails | Retried next session; cash keeps earning in the Never-Sleeping Account | CTO |
| Two months missed | Suggest a pause, not a cancellation | Head of Product |
| Transfer to the bank fails | Money returns to plan cash; a call within 1 business day | Customer Service |
<!-- /table -->

Source: authors' design.

## 6. Competitive positioning

### 6.1 The accumulation race

Of the 20 rival products we reviewed, several already offer what Round 2 considered new (Table 11; Appendix A). Recurring transfers from a bank are standard: VinaCapital's VinaSIP has used standing orders since 2021, from VND 500,000 a month (Thi truong Tai chinh Tien te, 2021), and Vietcombank customers can buy VCBF funds from VND 100,000 a period on VCB Digibank (VCBF, n.d.). Goal-based plans exist too: VNDIRECT's retirement plan mixes bond and equity funds 80/20 from VND 1 million (VNDIRECT, n.d.), and TCBS's TCWealth builds goal-based portfolios (TCBS, 2026). Persistence rewards exist as well: KBSV gave a VND 50,000 voucher a month for recurring purchases (KBSV, n.d.). At the top end, VPS Smart Indexing starts at VND 50 million plus VND 10 million a month, charges 0.5 per cent a year and decides for the customer (Tuoi Tre, 2026).

**Table 11. Rival products checked by the authors, 16 October 2026**

<!-- table: appC1_competitors -->
| Product | Assets | Minimum | Recurring | Who decides | Fees and rewards | Source |
|---|---|---|---|---|---|---|
| VPS Smart Indexing (11 Aug 2026) | Shares, direct indexing | VND 50 million, then 10 million a month | Yes | VPS (discretionary) | 0.5% a year | Tuoi Tre (2026); Tin nhanh Chung khoan (2026) |
| SSI eSIP (campaign from 23 Apr 2026) | SSIAM and Dragon Capital funds | Not published | Yes | Customer | VND 50,000 voucher for new customers buying VND 1 million through eSIP | SSI Securities (2026); Bao Phap Luat (2026) |
| TCBS TCWealth (Q2 2026) | Goal-based portfolios | Not found | Not stated | Not stated | Not found | TCBS (2026) |
| TCBS iPower | Idle cash | VND 5 million | Automatic | – | Up to 6% a year (2025 comparison) | DNSE Securities (2025) |
| VNDIRECT Tích sản hưu trí (Retirement accumulation) | Bond and equity funds, 80/20 for 10 years | VND 1 million | Yes | Customer | 0.1% a year (free to December 2025) | VNDIRECT (n.d.) |
| VinaCapital VinaSIP (Jun 2021) | One VinaCapital fund per plan | VND 500,000 a month | Yes, standing order from the bank | Customer | – | Thi truong Tai chinh Tien te (2021) |
| VCB Digibank SIP (VCBF) | VCBF funds | VND 100,000 a period | Yes | Customer | Preferential redemption fee for SIP | VCBF (n.d.) |
| VPBank Hũ Mục Tiêu (Goal Jar; Sep 2026) | Deposits | Not found | Yes, by day, week or month | Customer | – | VPBank (2026) |
| KBSV periodic investment | Shares | – | Yes | Customer | VND 50,000 voucher a month, capped at VND 600,000 (Apr 2025 to Mar 2026) | KBSV (n.d.) |
| DNSE today | Never-Sleeping Account (1.8–4.3% on idle cash); Golden Egg bonds (6.20–7.60%) | Golden Egg from VND 100,000 | No plan product | Customer | No fee on share trades | DNSE Securities (2026b, 2026d, n.d.-b) |
| Payday Portfolio (proposed) | Bank bonds, bond and equity funds, VN30 ETF | VND 500,000 a month | Yes, standing order to a personal virtual account | Customer confirms an adviser-signed plan | No platform fee | Authors' design |
<!-- /table -->

Source: as listed in the table; based on public product information as of 16 October 2026. Also reviewed from desk research but not re-checked: TCBS iTracker, Fundmart and iSave; VNDIRECT VNDGO; VPBankS NEO Invest and Tích sản cổ phiếu (share accumulation); MBS Mobile; Techcombank iFund; MoMo Túi Thần Tài; Tikop; Finhay with DFVN.

### 6.2 Where Payday sits

Payday does not claim to be first. Of the products we found, none combines bank bonds, bond and equity funds and an ETF in one customer-confirmed plan from VND 500,000, and none publishes its transfer-success rate or withdrawal times (Figure 9). Its lasting advantages are distribution and proof: near-zero cost of reaching 1.5 million accounts that have already passed identity checks, and service metrics that answer the reliability and trust problems the data revealed. The banks are the hardest rivals, because they hold the salary accounts and the trust; Payday competes on the range of assets in one app and on sitting next to the customer's trading.

![Figure 9. Minimum to start against the number of asset types in one plan; only products with a verified minimum are plotted](outputs/round3/figures/positioning_map.png)

Source: Tuoi Tre (2026); VNDIRECT (n.d.); VCBF (n.d.); Thi truong Tai chinh Tien te (2021); authors' design.

## 7. Business case

### 7.1 Model structure and inputs

The model follows each month's cohort of new savers for 60 months (Appendix A, Table A2). For each cohort it applies a stop rate of 10 per cent a month to the second and third contributions and 2.5 per cent a month afterwards, withdrawals of 10 per cent of balances a year, a contribution of VND 1 million a month and the default asset mix of 45 per cent Golden Egg, 35 per cent bond funds, 10 per cent equity funds and 10 per cent ETF. Revenue is DNSE's margin on the bank bonds sold through Golden Egg (0.6 points in the base case) and its assumed share of fund management fees; ETF trades earn nothing because DNSE charges no trading fee. Costs are a build team of ten for six months, a running team of six from month four, operations and compliance, content, the cost of reaching customers, the bank fee per contribution and a monthly service cost. Each input has a downside, base and upside value (Appendix F). A second engine steps the same cohorts through calendar time for stress tests and matches the cohort engine exactly when there is no shock; 35 tests, including the worked example of the Round 2 plan, pass before the model is used.

### 7.2 Results in three scenarios

The base case does not pay back within five years (Table 12; Figure 10). Cumulative cash falls to minus VND 32.0 billion at month 60, and the net present value at 12 per cent is minus VND 25.0 billion. The downside, with lower enrolment, yields and persistence, costs VND 10.0 million per new funded account. The upside breaks even in month 24 on a monthly basis and pays back in month 44, with a net present value of VND 11.0 billion. In the base case the plan holds VND 352 billion at month 36 and 14,871 savers have passed VND 10 million in their own plan; the number grows to 24,898 by month 60 (Figure 11).

**Table 12. Results in three scenarios**

<!-- table: slide11_scenarios -->
|  | Downside | Base | Upside |
|---|---|---|---|
| Cash need, Phase 0–1, with 15% contingency | VND 8.7 billion | VND 6.6 billion | VND 4.8 billion |
| New accounts above VND 10 million, month 36 | 2,911 | 14,871 | 51,445 |
| NPV over 60 months at 12% | −VND 35.1 billion | −VND 25.0 billion | +VND 11.0 billion |
| Payback month | None | None | 44 |
| Net cost per new funded account, month 60 | VND 10.02 million | VND 1.29 million | 0 |
<!-- /table -->

Source: authors' cohort model (assumptions in Appendix F).

![Figure 10. Cumulative cash over 60 months in three scenarios](outputs/round3/figures/payday_jcurve.png)

Source: authors' cohort model.

![Figure 11. Plan balances (left) and new accounts above VND 10 million (right) by month, three scenarios](outputs/round3/figures/payday_balance_accounts.png)

Source: authors' cohort model.

### 7.3 Unit economics

A saver is worth little on his or her own (Table 13). VND 10 million of balance earns DNSE about VND 44,150 a year in the base case. The ceiling on what DNSE can spend to acquire a saver, the present value of the saver's net revenue over 60 months at 12 per cent, is VND 127,512. Reaching a dormant account costs VND 1,300 in messages, so the break-even enrolment rate is about 1.0 per cent of accounts contacted. The bank fee is the largest variable cost: at the list price of VND 3,300 per contribution the ceiling is VND 127,512, if the bank waives the fee it rises to VND 198,876, and above VND 6,191 a dormant saver no longer pays back.

**Table 13. Unit economics by scenario**

<!-- table: appB1_unit_economics -->
| Measure | Downside | Base | Upside |
|---|---|---|---|
| Net yield on plan balances, a year | 0.25% | 0.44% | 0.68% |
| Revenue a year on VND 10 million of balance | VND 25,000 | VND 44,150 | VND 67,900 |
| Still contributing after 3 contributions | 72.2% | 81.0% | 88.4% |
| Still contributing after 6 contributions | 63.9% | 75.1% | 84.4% |
| Still contributing after 12 contributions | 50.0% | 64.5% | 77.1% |
| Contributions in a row to pass VND 10 million | 14 | 11 | 7 |
| CAC ceiling: PV of net revenue per saver, 60 months | −VND 44,938 | VND 127,512 | VND 728,075 |
| Acquisition cost per dormant saver | VND 220,000 | VND 65,000 | VND 27,500 |
| Reach cost per dormant account contacted | VND 2,200 | VND 1,300 | VND 1,100 |
| Break-even enrolment of contacted accounts | not reached | 1.02% | 0.15% |
<!-- /table -->

Source: authors' cohort model.

### 7.4 Sensitivity and levers

Fixed cost decides the case (Figure 12). Moving build and running costs between their downside and upside values shifts cumulative cash at month 60 by VND 17.5 billion, almost three times the swing from net yield (VND 6.3 billion) and nearly four times that from the bank fee (VND 4.7 billion) or the contribution (VND 4.5 billion). Enrolling more savers barely changes month-60 cash, because savers enrolled late have not yet paid back by the end of the window, but it does lower the cost per funded account. The levers in Table 14 follow: a lean team of four IT staff lowers the net cost per new funded account from VND 1.29 million to 0.85 million; treating half of the team's cost as shared platform spending gives VND 0.86 million; waiving the bank fee gives VND 1.17 million; and all four levers together, with upside yields and enrolment, give VND 0.18 million and reach monthly break-even in month 39, though cumulative cash is still negative at month 60.

![Figure 12. Month-60 cash when one group of inputs moves to its downside or upside value](outputs/round3/figures/payday_tornado.png)

Source: authors' cohort model.

**Table 14. Levers on the cost per funded account**

<!-- table: appB3_levers -->
| Case | Net cost per new funded account, month 60 (VND million) | Cumulative cash, month 60 (VND billion) | NPV (VND billion) | Break-even month |
|---|---|---|---|---|
| Base case | 1.29 | −32.0 | −25.0 | none |
| Partner bank waives the collection fee | 1.17 | −29.2 | −23.0 | none |
| Lean team: 4 IT staff, lower overheads | 0.85 | −21.2 | −16.8 | none |
| Upside yields: Golden Egg margin 1.5%, 40% of fund fees | 1.15 | −28.5 | −22.7 | none |
| Upside enrolment in every channel | 0.68 | −30.8 | −24.5 | none |
| Fee waived and lean team | 0.74 | −18.4 | −14.8 | none |
| Fee waived, lean team, upside yields | 0.60 | −14.9 | −12.6 | 58 |
| Fee waived, lean team, upside yields and enrolment | 0.18 | −8.2 | −8.3 | 39 |
| All inputs at upside (upside scenario) | 0.00 | 21.9 | 11.0 | 24 |
| DNSE's own bonds in the Golden Egg core (margin about 1.2 points; rejected, decision D7) | 1.13 | −28.1 | −22.4 | none |
| Half of the team cost treated as shared platform spending (incremental view) | 0.86 | −21.4 | −16.8 | none |
<!-- /table -->

Source: authors' cohort model.

### 7.5 Stress tests

Shocks hit the KPI far more than the cash (Table 15). A market fall in the second year, modelled as stop and withdrawal rates three times normal for three months, cuts new funded accounts at month 36 by 12.3 per cent but month-60 cash by only VND 0.35 billion; the VN-Index fell 115 points on 9 March 2026 (VnExpress, 2026b), so the scenario is not remote. A failed payday in month 9 cuts accounts by 7.7 per cent; both shocks together cut them by 18.5 per cent and cash by VND 0.51 billion. Because each saver is roughly break-even over five years, losing savers removes revenue and cost together. The real exposure is the Board's key indicator and DNSE's reputation, which is why reliability is a gate.

**Table 15. Stress tests**

<!-- table: appB4_stress -->
| Case | New accounts above VND 10 million, month 36 | Change | Change in month-60 cash (VND billion) |
|---|---|---|---|
| Base case, no shock | 14,871 | 0.0% | 0.00 |
| Market fall in year 2: stop and withdrawal rates three times normal in months 13 to 15 | 13,043 | −12.3% | −0.35 |
| Failed payday run in month 9: 15% of contributing savers stop; enrolment 30% lower in months 9 to 11 | 13,725 | −7.7% | −0.21 |
| Both shocks | 12,118 | −18.5% | −0.51 |
<!-- /table -->

Source: authors' cohort model (calendar engine).

### 7.6 Indirect value, not counted in cash

Some value sits outside the cash flows and is shown separately. At month 36 in the base case, plan balances equal about 18 per cent of the investor cash DNSE held in June 2026. If other accounts stayed as they were, the platform cost per account with VND 10 million or more would fall from VND 7.3 million to 4.7 million. A lending option, letting customers use the plan's ETF units as collateral for ordinary margin loans, would improve the base net present value from minus VND 25.0 billion to minus VND 20.9 billion; it runs against the purpose of a savings plan and touches the area in which DNSE was fined in 2026, so it is reviewed only at Gate 3 and is not in the base case.

### 7.7 How the Board should read the case

Payday is not a fee business; it is a way to buy funded accounts. The base case buys a new account above VND 10 million for a net cost of about VND 1.3 million and, unlike sign-up rewards, keeps the money in the account. The Board's exposure before the first stop decision is VND 6.6 billion, and the month-6 gate re-runs the model with the pilot's measured values: if the projected cost per funded account exceeds twice the plan, the programme stops.

## 8. Go-to-market plan for year one

### 8.1 Plan by quarter

Year one has four steps (Table 16; Figure 13). In the first quarter DNSE builds the product, signs its partners and runs the plan with staff money; nothing launches before Gate 0. In the second quarter a randomised pilot reaches 45,000 dormant accounts in three arms of 15,000: a control arm, Payday, and Payday with the persistence package. If enrolment clears 1.5 per cent, the third quarter rolls out to the remaining eligible dormant accounts, adds an in-app offer for active traders and a plan step at account opening. In the fourth quarter DNSE tests three to five employers through human-resources sessions with a licensed adviser. By month 12 the base case has 9,414 savers enrolled, 4,953 funded savers with at least three contributions in a row and VND 30.1 billion in plans.

**Table 16. Go-to-market plan for year one**

<!-- table: slide12_gtm -->
| Quarter | Who and where | Message | Gate | End of quarter, base: funded savers; balances; spend |
|---|---|---|---|---|
| Q1: build | DNSE staff, internal beta | – | Gate 0: partner terms; 99.5% shadow runs; SSC notice | 0; 0; VND 2.1 bn |
| Q2: pilot | 45,000 dormant accounts in 3 arms; Zalo, SMS, push, Ensa | "Your account is ready. Let payday do the investing." | Gate 1: enrolment ≥1.5%, stop below 1.0% | 162; VND 1.1 bn; VND 3.6 bn |
| Q3: roll out | Dormant accounts; in-app for traders; plan step at account opening | "Keep a core that grows while you trade." | Monthly: acquisition cost per funded saver ≤VND 128,000 | 1,620; VND 10.5 bn; VND 1.7 bn |
| Q4: first employers | 3 to 5 employers through HR sessions | "An employee benefit that invests your salary." | Gate 2: funded ≥3,962; balances ≥VND 24.1 billion | 4,953; VND 30.1 bn; VND 1.8 bn |
<!-- /table -->

Source: authors' design; numbers from the authors' cohort model.

![Figure 13. Year-one activities by month with Gates 0 to 2 (top) and funded savers by month (bottom), base case](outputs/round3/figures/gtm_timeline.png)

Source: authors' cohort model. Red marks the months the Board approves now; arrows mark channels that continue into year two.

### 8.2 Messages, channels and guardrails

Each segment hears one message: "Your account is ready. Let payday do the investing." for dormant holders, "Keep a core that grows while you trade." for active traders, "Start your plan with your first deposit." at account opening and "An employee benefit that invests your salary." for employers. Channels are DNSE's own: Zalo template messages, text messages, push notices, in-app banners and Ensa. Reaching a dormant account costs about VND 1,300, based on two Zalo template messages and one text message (Zalo Business Solutions, n.d.; MobiFone, n.d.). The guardrails come from the 2025 lesson: no sign-up cash, no influencers promising "free money", no conditional rewards, no cash-back promotions through partners, and at most three messages per account.

### 8.3 Year-one budget

The base case spends VND 9.2 billion in year one, released gate by gate, of which the Board approves VND 6.6 billion now. Outreach and marketing take only VND 1.1 billion; building and running the product takes VND 7.9 billion. This is why the cheapest improvements to the economics are a lean team and reused components rather than cheaper acquisition.

## 9. Strategic roadmap

### 9.1 Five gated phases

Beyond year one, the roadmap has five phases, each closed by a gate (Table 17; Figure 14). Phases 0 to 2 build, test and scale inside DNSE's own base. Phase 3, from month 13, adds channels that create a default: employers, salary-percentage contributions through bank application programming interfaces once banks comply in March 2027, and an automatic step-up when salaries rise. Phase 4, from month 25, looks at a fully managed version run by a partner fund manager or by the fund management company DNSE proposed to acquire at its 2026 general meeting (DNSE Securities, 2026f).

**Table 17. Strategic roadmap**

<!-- table: slide13_roadmap -->
| Phase | Months | Objective | Key initiatives | Gate and result (base) |
|---|---|---|---|---|
| 0. Build and comply | 1–3 | A safe, legal MVP | Virtual accounts (fee target VND 0); fund contracts; adviser-signed plans; SSC notice | Gate 0; −VND 2.1 billion cumulative |
| 1. Pilot | 4–6 | Measure enrolment, persistence, new money | Randomised pilot, 45,000 accounts, 3 arms | Gate 1; 600 savers |
| 2. Scale in the base | 7–12 | Controlled scale | Dormant roll-out; in-app; account opening; first employers | Gate 2; 4,953 funded |
| 3. Outside channels | 13–24 | Channels that create a default | Employers; salary percentage via Open API from March 2027; step-up with pay rises | Gate 3; 7,714 new accounts above VND 10 million |
| 4. Optimise | 25–36 | Better economics, a managed option | Partner or DNSE-owned fund manager; Golden Egg with more bank partners | Quarterly review; 14,871 new accounts above VND 10 million |
<!-- /table -->

Source: authors' design; numbers from the authors' cohort model; DNSE Securities (2026f); State Bank of Vietnam (2024).

![Figure 14. Payday's five gated phases with base-case results (top), above DNSE's balance-first product roadmap (bottom)](outputs/round3/figures/roadmap.png)

Source: authors' design; authors' cohort model.

### 9.2 Payday inside DNSE's balance-first roadmap

Payday is the centre of a wider shift from trading-first to balance-first. In the first six months DNSE fixes the base: app reliability, compliance built into margin lending, and transparency. From months six to twelve it keeps money in: the Never-Sleeping Account switched on by default, Golden Egg as the safe core, and Payday. From months twelve to twenty-four it grows on balances: margin for customers who hold assets, paid advice and bank application programming interfaces. The components Payday builds, namely virtual accounts in customers' names, a scheduler, a suitability engine and a transparency dashboard, serve deposits, margin and Golden Egg as well, so part of their cost is platform spending rather than Payday's alone.

### 9.3 Options outside the base case

Three options are kept out of the base case and reviewed at gates. **Employers** reach many salaried people at once, but at VND 15 million per employer and 300 employees a saver costs less than the acquisition ceiling only if at least 39 per cent of staff enrol; the evidence for high participation comes from automatic enrolment in payroll plans, which raised participation from 37 to 86 per cent in one United States plan (Madrian & Shea, 2001), whereas an opt-in session reaches about 28 per cent at best (Ashraf et al., 2006). **Open API** contributions need agreements with the banks and customer consent that lasts at most 180 days. **ETF-secured lending** is discussed in Section 7.6.

## 10. Implementation and validation

### 10.1 Pilot design

The pilot is a randomised trial with 45,000 dormant accounts in three arms of 15,000 (Table 18). Two arms receive the offer and one is a control, so the pilot measures what Payday adds rather than what would have happened anyway. With 300 enrolled savers in each treated arm, the pilot can detect a gain of about ten points in the share of savers reaching six contributions; a pilot of 20,000 accounts could detect only 15 points. Enrolment is measured with a 95 per cent interval of about 1.84 to 2.16 per cent if the true rate is 2 per cent, enough to tell the stop line of 1.0 per cent from the scale line of 1.5 per cent. Outreach to the treated arms costs about VND 39 million.

**Table 18. Pilot size and what it can detect**

<!-- table: appB6_pilot_power -->
| Pilot accounts | Savers per treated arm | Enrolment, 95% interval | Smallest detectable gain (points) | Outreach cost (VND million) |
|---|---|---|---|---|
| 20,000 | 133 | 1.76–2.24% | 14.8 | 17.3 |
| 30,000 | 200 | 1.81–2.19% | 12.1 | 26.0 |
| 45,000 | 300 | 1.84–2.16% | 9.9 | 39.0 |
| 60,000 | 400 | 1.86–2.14% | 8.6 | 52.0 |
<!-- /table -->

Source: authors' cohort model.

### 10.2 Indicators

The North Star is the number of new accounts with VND 10 million or more in the plan, a measure DNSE already publishes for its whole base, so the Board can check it against the annual report. The targets come from the model: 7,714 by month 24 and 14,871 by month 36 in the base case. Three leading indicators show whether the plan is on track: funded savers (three or more contributions in a row), the share of inflows that is new money, and the on-time crediting rate.

### 10.3 Decision gates

Each phase ends with a gate at which the Board scales, adjusts or stops (Figure 15; Table 19). The thresholds are derived from the model rather than chosen by feel. At Gate 0 (month 3) DNSE checks the partner terms, a 99.5 per cent on-time rate in shadow paydays and written compliance. At Gate 1 (month 6) it reads the pilot: it scales if at least 1.5 per cent of treated accounts enrol and at least 81 per cent of savers make three contributions in a row, and it stops if enrolment is below 1.0 per cent, persistence below 60 per cent or the projected cost per new funded account above VND 2.6 million. Gates 2 and 3 compare funded savers, balances, new funded accounts and the employer channel with the plan.

![Figure 15. Scale, adjust and stop branches at Gates 0 to 3](outputs/round3/figures/decision_tree.png)

Source: authors' cohort model.

**Table 19. All decision gates**

<!-- table: appB7_gates -->
| Gate | Measure | Scale if | Adjust if | Stop if | Owner |
|---|---|---|---|---|---|
| Gate 0: before the pilot | Partner terms signed: bank fee per contribution; share of fund fees paid to DNSE; DNSE's margin on bank bonds in Golden Egg | Fee ≤ VND 3,300; fund share ≥ 30%; margin ≥ 0.6 points | Worse on any term: re-run the model and renegotiate before the pilot | Fund or bank partner not signed (launch dependency) | CFO |
| Gate 0: before the pilot | Bank fee per contribution (virtual-account collection), VND | 0 (partner bank keeps the deposits) | 1 to 3,300 (list price) | > 6,191: a dormant saver no longer pays back | CFO |
| Gate 0: before the pilot | Shadow payday runs with staff accounts: transfers credited on time | ≥ 99.5% | - | < 99.5%: delay the pilot | CTO |
| Gate 1: pilot read-out | Projected net cost per new account above VND 10 million by month 60 (model re-run with the pilot's measured values and the signed terms), VND million | ≤ 1.6 (1.25 x plan) | 1.6 to 2.6 | > 2.6 (2 x plan) | CFO |
| Gate 1: pilot read-out | Enrolment rate of treated dormant accounts (set-up and first contribution within 60 days) | ≥ 1.5% | 1.0% to 1.5% | < 1.0% | Head of Product |
| Gate 1: pilot read-out | Savers making three contributions in a row | ≥ 81.0% | 60.0% to 81.0% | < 60.0% | Head of Product |
| Gate 1: pilot read-out | Average monthly contribution, VND | ≥ 1,000,000 | 716,502 to 1,000,000 | < 716,502 | CFO |
| Gate 1: pilot read-out | Share of plan inflows that is new money (tagged by source) | ≥ 80% | 60% to 80% | < 60% | CFO |
| Gate 1: pilot read-out | Scheduled transfers credited on time | ≥ 99.5% | - | < 99.5% (launch gate) | CTO |
| Gate 1: pilot read-out | Compliance: SSC notice filed; model portfolios signed off by a licensed adviser | Written confirmation | - | Missing (launch gate) | Compliance |
| Gate 2: first roll-out year | Funded savers (three or more contributions in a row) | ≥ 3,962 (80% of plan) | 2,476 to 3,962 | < 2,476 for two quarters | Head of Product |
| Gate 2: first roll-out year | Plan balances, VND billion | ≥ 24.1 (80% of plan) | 15.1 to 24.1 | < 15.1 for two quarters | CFO |
| Gate 2: first roll-out year | Acquisition cost per funded saver, VND | ≤ 127,512 (CAC ceiling) | - | > 127,512 for two quarters | CFO |
| Gate 3: scale-up review | Monthly plan revenue against monthly running cost | ≥ 16% (plan) | - | < 2% (downside path): review the revenue model | CFO |
| Gate 3: scale-up review | New accounts above VND 10 million from the plan | ≥ 6,171 (80% of plan) | - | < 1,140 (downside path) | CEO |
| Gate 3: scale-up review | Employer channel: share of employees who enrol after the HR session | ≥ 39% | 20% to 39%: lower the cost per employer | < 20%: stop the channel | Head of Product |
| Gate 3: scale-up review | Net cost per new account above VND 10 million to date, VND million | ≤ 2.6 (1.25 x plan) | 2.6 to 4.1 | > 4.1: fold into the core app team or stop | CFO |
<!-- /table -->

Source: authors' cohort model.

### 10.4 Responsibilities and dependencies

Every activity has one accountable owner (Table 20). The chain of dependencies is short but strict: the virtual-account bank comes before the scheduler, the shadow paydays and the pilot; the fund contracts come before the fund leg of the plan, and if they are late the minimum viable product launches with Golden Egg and the ETF; the notice to the State Securities Commission comes before launch; source tagging of inflows comes before the new-money indicator; and bank agreements on open application programming interfaces come before salary-percentage contributions in Phase 3.

**Table 20. Responsibilities (RACI)**

<!-- table: appB9_raci -->
| Activity | CEO | CFO | CTO | Head of Product | Compliance and Legal | Marketing and CRM | Customer Service | Licensed adviser |
|---|---|---|---|---|---|---|---|---|
| Gate decisions (months 3; 6; 12; 24) | A | R | C | R | C | I | I | I |
| Partner terms: virtual-account bank, fund managers, bond supply | I | A/R | C | C | C | - | - | - |
| SSC notice, legal opinions, review of promotions | I | I | I | C | A/R | C | - | C |
| Model plans and suitability rules | I | - | I | C | A | - | - | R |
| MVP build: scheduler, virtual accounts, allocation, dashboard | I | I | A/R | C | C | - | I | - |
| Shadow payday runs and the 99.5% reliability gate | I | I | A/R | C | I | - | I | - |
| Randomised pilot: design and read-out | I | C | C | A/R | C | C | I | C |
| Outreach and messages | I | I | I | A | C | R | I | - |
| Complaints, withdrawals and recovery after failures | I | I | C | A | C | I | R | - |
| Monthly service metrics published | I | I | R | A | C | C | C | - |
<!-- /table -->

Source: authors' design. R = responsible, A = accountable, C = consulted, I = informed.

## 11. Risks and mitigation

Six risks are scored by likelihood and impact on a scale of 1 to 5 (Figure 16; Table 21). A payday failure scores highest (20 of 25): the 4 March 2026 outage shows it can happen, so shadow paydays, a separate scheduler and a release freeze come before launch. Low enrolment comes second (16), which is why the pilot stops below 1.0 per cent. Third (15), the regulator may object to Golden Egg's role or the advice flow, so DNSE notifies the commission early and keeps bond funds as a fallback core. Partner terms, a market fall or a conflict of interest, and plan money moving to trading complete the register; each has an early-warning signal and an owner.

![Figure 16. Six risks by likelihood and impact, with owners](outputs/round3/figures/risk_heatmap.png)

Source: authors' assessment.

**Table 21. Risk register**

<!-- table: appB8_risks -->
| ID | Risk | Likelihood × impact | Mitigation | Early warning | Owner |
|---|---|---|---|---|---|
| R1 | A payday transfer or the app fails on a payday | 4 × 5 = 20 | Shadow payday runs before launch; contribution scheduler kept apart from the pre-trade buying-power check; no app release in the days before peak contribution dates; staged releases; status page and post-incident note | Contributions credited on time below 99.5% in any month | CTO |
| R2 | Too few dormant accounts enrol | 4 × 4 = 16 | Randomised pilot with 45,000 accounts before any roll-out; Gate 1 stop line at 1.0%; plan step at account opening; message tests across arms | Enrolment of treated accounts below 1.0% at month 6 | Head of Product |
| R4 | The regulator objects to Golden Egg's role or to the advice flow | 3 × 5 = 15 | SSC notice and pre-consultation before launch; model plans signed by a licensed adviser; bond funds ready as the alternative safe core | Written query or objection from the SSC | Compliance and Legal |
| R3 | Partner terms leave too little per saver (bank fee, fund-fee share, bond margin) | 3 × 4 = 12 | Gate 0 terms: collection fee target VND 0 (the bank keeps the deposits), fund-fee share >= 30%, bond margin >= 0.6 points; re-run the model before the pilot | Signed fee above VND 6,191 per contribution | CFO |
| R5 | A market fall or a conflict of interest damages trust | 3 × 4 = 12 | Plans follow the goal horizon (no equities for goals under 3 years); no DNSE-issued bonds in the default plan; bad-month cost shown in VND before confirming | Trust themes above 10% of Payday-related negative reviews | Head of Product |
| R6 | Plan money is moved to trading or comes from existing balances | 3 × 3 = 9 | Inflows tagged by source; withdrawals go to the linked bank by default; a separate step with a goal reminder before moving money to buying power | New money below 80% of inflows, or more than 10% of withdrawals moved to buying power | CFO |
<!-- /table -->

Source: authors' assessment; DNSE Securities (2023, 2026e); Market Times (2026); VnExpress (2026b).

## 12. Recommendation and Board ask

We recommend that the Board approve Phase 0 and Phase 1 of Payday Portfolio and the five decisions in Table 22. The amount is the model's cash need for months 1 to 6, VND 5.7 billion, plus a 15 per cent contingency. The Board will see measured enrolment, persistence, contributions and new money at month 6 and can stop the programme then, at a cost of no more than the amount approved.

**Table 22. Board ask**

<!-- table: slide15_board_ask -->
| Ask | Detail |
|---|---|
| Budget | VND 6.6 billion for months 1 to 6 (5.7 plus 15% contingency) |
| Decision 1 | Choose the virtual-account bank; collection fee target VND 0 |
| Decision 2 | Sign 1 to 2 fund managers |
| Decision 3 | File the SSC notice; pre-consult on Golden Egg's role |
| Decision 4 | Have a licensed adviser sign the model plans |
| Decision 5 | Accept about VND 1.3 million per new funded account as the gate yardstick |
<!-- /table -->

Source: authors' cohort model.

## 13. Conclusion

DNSE has solved the hard part of growth, opening accounts, but its accounts do not hold money and its free trading does not pay for the platform. Payday Portfolio gives salaried customers a route from intention to regular deposits, built from products DNSE already runs and designed around the evidence: reliability first, trust made visible, no cash rewards, no margin and no conflicts of interest. The economics are modest and stated plainly. In the base case Payday buys funded accounts for about VND 1.3 million each and does not pay back within five years; in the upside it pays back in month 44. What makes it worth starting is that the Board risks only VND 6.6 billion before it learns, at month 6, which of those cases is real.

## Appendices

### Appendix A. Data and methods

**Table A1. Data behind the report**

<!-- table: appA1_data_sources -->
| Data | Source | Used for |
|---|---|---|
| Accounts, active customers and funded accounts, December 2025 | DNSE Annual Report 2025 (DNSE Securities 2026c) | Problem, sizing, model inputs |
| DNSE financial statements, Q1 2018 to Q2 2026 | DNSE filings via Vietcap Securities (2026) | Brokerage loss, platform cost per funded account |
| Market shares of accounts, investor cash, margin loans and profit | HNX, VSDC and press reports, reconciled in Round 2 | Slide 2 |
| App reviews of DNSE, VPS and FPTS, 2021 to 2026 | Google Play and App Store; Round 2 cleaning; 58 negative 2026 reviews coded by hand | Slides 4 and 5; Appendices D and F |
| Rates, fees and product terms, October 2026 | 44 web sources with access dates (sources_round3.csv) | Model inputs; slides 3, 7 and 10 |
| Wages paid into an account | World Bank (2025) Global Findex | Share of salaried dormant holders |
<!-- /table -->

Source: authors. Slide and appendix numbers in the last column refer to the Round 3A deck.

**Table A2. Methods and checks**

<!-- table: appA2_methods -->
| Method | What it does | How it was checked |
|---|---|---|
| Monthly cohort model | Follows each month's new savers: stop rates, contributions, withdrawals and who passes VND 10 million | 35 tests pass, including the worked example of the Round 2 plan |
| Calendar engine | Runs the same cohorts in calendar time, so a shock hits every cohort at once | Matches the cohort engine exactly when there is no shock |
| Unit economics | CAC ceiling = present value of net revenue per saver over 60 months at 12% | Break-even enrolment = reach cost ÷ CAC ceiling |
| Decision gates | Stop and scale lines solved from the model by bisection | Programme test: net cost per new funded account |
| Review coding | 58 negative 2026 reviews read one by one; 8 cause codes, several allowed per review | 95% Wilson intervals; compared with the Round 2 keyword rule |
<!-- /table -->

Source: authors.

### Appendix B. Model detail

**Table B1. Budget by phase, VND billion, base case**

<!-- table: appB2_phase_budget -->
| Phase | Months | Cost | of which build | Revenue | Cumulative cash at end |
|---|---|---|---|---|---|
| Phase 0: build and comply | 1–3 | 2.09 | 2.09 | 0.00 | −2.09 |
| Phase 1: pilot | 4–6 | 3.63 | 2.09 | 0.00 | −5.72 |
| Phase 2: scale in the base | 7–12 | 3.49 | 0.00 | 0.03 | −9.17 |
| Phase 3: outside channels | 13–24 | 7.28 | 0.00 | 0.46 | −15.99 |
| Phase 4: optimise | 25–36 | 7.23 | 0.00 | 1.20 | −22.02 |
| Years 4 and 5 | 37–60 | 14.73 | 0.00 | 4.76 | −32.00 |
<!-- /table -->

Source: authors' cohort model.

**Table B2. Cash tiers tested against the non-cash package**

<!-- table: appB5_tiers -->
| Bank fee | Reward design | Reward cost, % of revenue | CAC ceiling | 12-contribution rate needed |
|---|---|---|---|---|
| Base bank fee | Round 2 tiers made small: 10k / 20k / 50k gifts, 0.1-point fee rebate from 6, Golden Egg +0.2 points from 12 | 41.2% | VND 36,712 | not reachable |
| Base bank fee | Tested option: 30k gift at 12, 0.1-point fee rebate from 6 | 14.2% | VND 96,158 | not reachable |
| Base bank fee | MVP (decision D1): non-cash features only | 0.0% | VND 127,512 | 64.5% |
| Bank fee waived | Round 2 tiers made small: 10k / 20k / 50k gifts, 0.1-point fee rebate from 6, Golden Egg +0.2 points from 12 | 41.2% | VND 108,077 | not reachable |
| Bank fee waived | Tested option: 30k gift at 12, 0.1-point fee rebate from 6 | 14.2% | VND 167,523 | 73.3% |
| Bank fee waived | MVP (decision D1): non-cash features only | 0.0% | VND 198,876 | 64.5% |
<!-- /table -->

Source: authors' cohort model.

### Appendix C. Reviews of DNSE's app, 2026

**Table C1. Causes in 58 negative reviews, with 95 per cent Wilson intervals**

<!-- table: appD1_review_causes -->
| Cause | Google Play | App Store | Both stores | 95% interval |
|---|---|---|---|---|
| Login, OTP and authentication | 3 (9%) | 5 (21%) | 8 (14%) | 7.2–24.9% |
| Deposits or withdrawals not credited | 4 (12%) | 6 (25%) | 10 (17%) | 9.6–28.9% |
| Orders, prices and settlement | 6 (18%) | 5 (21%) | 11 (19%) | 10.9–30.9% |
| Crashes, freezes and lag | 15 (44%) | 11 (46%) | 26 (45%) | 32.7–57.5% |
| eKYC and account opening | 5 (15%) | 5 (21%) | 10 (17%) | 9.6–28.9% |
| Fees and terms (closure, auto-renewal) | 3 (9%) | 3 (12%) | 6 (10%) | 4.8–20.8% |
| Scam claims and rewards | 4 (12%) | 3 (12%) | 7 (12%) | 6.0–22.9% |
| Other (service, interface, Ensa, no reason) | 6 (18%) | 7 (29%) | 13 (22%) | 13.6–34.7% |
| Something broke (any of the first five causes) | 28 (82%) | 20 (83%) | 48 (83%) | 71.1–90.4% |
| Fees, terms, scam claims or rewards | 6 (18%) | 5 (21%) | 11 (19%) | 10.9–30.9% |
| Login/OTP failures or money not credited | 7 (21%) | 10 (42%) | 17 (29%) | 19.2–42.0% |
| Posted 4-5 March 2026, after the outage DNSE disclosed for 4 March | 4 (12%) | 5 (21%) | 9 (16%) | 8.4–26.9% |
| Blames an app update | 2 (6%) | 3 (12%) | 5 (9%) | 3.7–18.6% |
| Negative reviews coded | 34 | 24 | 58 |  |
<!-- /table -->

Source: Google Play; App Store; authors' coding.

**Table C2. Negative reviews by month**

<!-- table: appD2_reviews_by_month -->
| Month | Negative reviews | Something broke | Posted 4–5 March |
|---|---|---|---|
| 2026-01 | 7 | 5 | 0 |
| 2026-02 | 5 | 5 | 0 |
| 2026-03 | 17 | 17 | 9 |
| 2026-04 | 7 | 4 | 0 |
| 2026-05 | 5 | 3 | 0 |
| 2026-06 | 5 | 4 | 0 |
| 2026-07 | 5 | 3 | 0 |
| 2026-08 | 5 | 5 | 0 |
| 2026-09 | 2 | 2 | 0 |
<!-- /table -->

Source: Google Play; App Store; authors' coding; DNSE Securities (2026e).

**Table C3. In customers' words**

<!-- table: appD3_quotes -->
| What the customer wrote (authors' translation) | Review |
|---|---|
| Today, 4 March 2026, the app froze and I could not place a single buy or sell order all afternoon, on a day the market was red from start to finish. When prices recovered near the close, it would not let me buy to lower my average cost. It would not let me withdraw my money either. | App Store review, 1 star, 2026-03-04, version 2.113.28 |
| I deposited money and the bank said the transfer was successful, but the app showed nothing credited. The money still has not reached my account. | Google Play review, 1 star, 2026-03-02 |
| I cannot transfer money out to my bank. The OTP confirmation never arrives; the timer counts down again and again and I still cannot withdraw. | App Store review, 1 star, 2026-03-30, version 2.114.3 |
| A finance app that updates four or five times a week. Every update brings new bugs, and afterwards it wipes my login details and settings. | App Store review, 1 star, 2026-08-17, version 3.4.18 |
| I never pressed renew, but it renewed automatically, so I lost money. | Google Play review, 1 star, 2026-01-05 |
| The advance fee is quoted at 13.5 per cent a year, but in practice it is 27 per cent a year. Hidden fees, wrong fees. | App Store review, 1 star, 2026-03-26, version 2.114.2 |
<!-- /table -->

Source: Google Play and App Store reviews; authors' translation.

### Appendix D. Feedback evidence

**Table D1. What customers wrote, by design choice**

<!-- table: appF1_feedback -->
| Design choice | What customers wrote (authors' translation) | Review |
|---|---|---|
| Personal virtual account with instant credit | "DNSE should work with BIDV to create an account identifier for transfers; otherwise deposits keep failing and people will leave the app" | Google Play, DNSE, 5 stars, 10 helpful votes, January 2022 |
| Personal virtual account with instant credit | "When I deposit outside trading hours, the bank takes the money but my securities account does not receive it" | Google Play, DNSE, 2 stars, 18 votes, June 2025 |
| Never-Sleeping Account as the waiting place | "The Never-Sleeping Account is the best; watching the interest tick up is a treat" | Google Play, DNSE, 5 stars, 13 votes, May 2026 |
| Golden Egg core with a ladder of terms | "Just add 6-month and 1-year Golden Egg terms and it is OK" | App Store, DNSE, 5 stars, February 2025 |
| Show the cost of selling early | "Bought a 1-month Golden Egg and lost 4% of the money" | App Store, DNSE, 1 star, January 2025 |
| No platform fee | "A VND 33,000 charge every month is too high, not worth it for a long-term investor" | Google Play, VPS, 1 star, 9 votes, May 2026 |
<!-- /table -->

Source: Google Play and App Store reviews of DNSE and VPS; authors' translation.

### Appendix E. Journey map

**Table E1. Journey map for persona P1**

<!-- table: appG2_journey -->
|  | 1. Notice the offer | 2. Make a plan | 3. Set up the money | 4. First payday | 5. Build the habit (to day 90) | 6. Withdraw or keep going |
|---|---|---|---|---|---|---|
| Goal | Decide whether this is worth a look | Know what to put in and why | Make saving automatic | See the first money arrive and get invested | Keep going without thinking about it | Get money out when needed |
| Actions | Opens a Zalo message or app banner | Sets a goal, answers 3 questions, confirms the plan | Creates a monthly transfer in the salary bank's app | Gets paid; the bank sends the transfer | Reads the payday reminder; skips a month if needed | Withdraws to the bank or skips a month |
| Touchpoints | Zalo template message, SMS, push, banner | Ensa, plan screen, fee screen | Personal account card, bank app link, QR | "Received" and "Invested" notices | Reminder naming the goal; streak; statement | Withdrawal screen |
| Thinking | "Is this another reward with conditions?" | "What am I buying, and what can I lose?" | "Will my bank transfer actually reach DNSE?" | "Did it arrive? Where is my money now?" | "Is it still worth it this month?" | "How fast, and what does it cost to take it out?" |
| Feeling (to test in the pilot) | Sceptical | Unsure | Impatient | Anxious then relieved | Motivated or forgetful | Wary |
| Pain points today (evidence) | Distrusting offers after the 2025 sign-up reward (trust themes 55% of negative Google Play reviews in H1 2025) | Finding portfolio choices hard (77% of investors find managing a portfolio difficult) | Leaving the app to set up a transfer; failing eKYC and account steps (17% of 2026 negative reviews) | Waiting for deposits the bank says were sent (17% of 2026 negative reviews) | Postponing each month; apps that crash, freeze or lag (45% of 2026 negative reviews) | Losing money on a 1-month Golden Egg without seeing why (2025 review) or on an auto-renewal the customer did not want (2026 review, product not named); withdrawals blocked when the bank-account name does not match (2026 review) |
| Design response | Remove sign-up rewards; say in one line what the plan is and who approves it | Ask 3 questions; set the plan by goal horizon; show a bad month in VND | Give a personal account number with a bank-app link and QR; aim for 5 minutes and no more steps than VCB Digibank SIP | Credit to a personal virtual account automatically; confirm within minutes; publish the on-time rate | Send a reminder that names the goal; keep a streak; allow one skip a year | Show arrival time and cost in VND before confirming; withdraw to the linked bank free; add a step before moving money to trading |
| Metric | Open and tap-through rates | Plans confirmed after the suitability check | Set-up completion and time | Contributions credited on the same banking day (>= 99.5%) | Savers making 3 contributions in a row | Median withdrawal time; share moved to buying power |
| Owner | Marketing and CRM | Head of Product; licensed adviser | CTO; partner bank | CTO; Operations | Head of Product | Customer Service |
| Moment of truth | - | - | - | Yes: first money in | - | Yes: first money out |
<!-- /table -->

Source: authors' design; evidence from Appendix C, Nhan Dan (2025) and the review data. Feelings are hypotheses for the pilot to test.

### Appendix F. Key assumptions

**Table F1. Key assumptions, three scenarios**

<!-- table: appH1_assumptions -->
| Assumption | Downside | Base | Upside | Type | Basis |
|---|---|---|---|---|---|
| Dormant accounts (used no product, Dec 2025) | 1,427,181 | 1,427,181 | 1,427,181 | derived | DNSE Securities (2026c) |
| Share of dormant accounts salaried and reachable | 15% | 25% | 35% | assumption | World Bank (2025); pilot survey |
| Pilot accounts (three arms) | 45,000 | 45,000 | 45,000 | assumption | Decision D4 |
| Enrolment of contacted dormant accounts | 1% | 2% | 4% | assumption | Never-Sleeping Account reached 0.8% of accounts; TCBS (2026) |
| Enrolment of active customers over 12 months | 2% | 4% | 6% | assumption | Never-Sleeping Account sign-ups equal 14% of active customers |
| New accounts a month | 20,000 | 31,180 | 43,210 | derived | DNSE Securities (2026c); VnExpress (2026a) |
| Set-up within 60 days of opening | 1% | 2% | 3% | assumption | Assumption |
| Employers signed a quarter | 2 | 4 | 8 | assumption | Go-to-market plan |
| Employees who enrol after an HR session | 10% | 20% | 28% | assumption | Ashraf et al. (2006) as upper bound |
| Monthly contribution | VND 800,000 | VND 1,000,000 | VND 1,500,000 | assumption | About 11% of the VND 9.0 million average income (National Statistics Office, 2026) |
| Stop rate, 2nd and 3rd contributions (a month) | 15.0% | 10.0% | 6.0% | assumption | Assumption; pilot measures it |
| Stop rate after the 3rd contribution (a month) | 4.0% | 2.5% | 1.5% | assumption | Assumption; pilot measures it |
| Balances withdrawn a year | 15% | 10% | 5% | assumption | Assumption; inflows tagged |
| DNSE margin on bank bonds in Golden Egg | 0.30% | 0.60% | 1.00% | assumption | Thi truong Tai chinh Tien te (2026a); DNSE Securities (n.d.-b) |
| Distributor share of bond-fund fees | 0.22% | 0.33% | 0.44% | assumption | SSI Asset Management (2026); VCBF (2026); fund prospectuses |
| Distributor share of equity-fund fees | 0.38% | 0.56% | 0.75% | assumption | Fund prospectuses and factsheets, 2026 |
| Build team, months 1 to 6 | VND 3.97 billion | VND 3.18 billion | VND 2.54 billion | derived | ITviec (2025) salary medians |
| Integration, security tests, legal opinions | VND 1.50 billion | VND 1.00 billion | VND 0.60 billion | assumption | VPBank (2024); assumption |
| Running team, a year | VND 4.72 billion | VND 3.78 billion | VND 2.52 billion | derived | ITviec (2025) salary medians |
| Operations, compliance and cloud, a year | VND 1.80 billion | VND 1.20 billion | VND 0.80 billion | assumption | Assumption |
| Content and promotion review, a year | VND 1.50 billion | VND 1.00 billion | VND 0.60 billion | assumption | Assumption |
| Reach cost per dormant account contacted | VND 2,200 | VND 1,300 | VND 1,100 | derived | Zalo Business Solutions (n.d.); MobiFone (n.d.) |
| Bank fee per contribution | VND 5,500 | VND 3,300 | VND 0 | assumption | VPBank (2024) list price |
| Service cost per active saver a month | VND 2,000 | VND 1,000 | VND 500 | assumption | Zalo confirmation, statements |
| Discount rate | 12% | 12% | 12% | assumption | Hurdle rate |
| Asset mix: Golden Egg / bond funds / equity funds / ETF | same | 45/35/10/10 | same | assumption | Design: glide path by goal horizon |
<!-- /table -->

Source: as listed in the table; the full list of 60 inputs is in `data/round3/payday_assumptions.csv`.

### Appendix G. Questions the Board is likely to ask

**Table G1. Short answers**

<!-- table: appI1_qa -->
| Question | Short answer | Evidence |
|---|---|---|
| Why not just a bank deposit? | Golden Egg pays 6.20–7.60% against 5.9% for a Big Four 12-month deposit, but bond coupons are taxed 5% and deposits are not. We compete on short terms, automation, a goal and published proof, not on the rate. | DNSE Securities (n.d.-a, n.d.-b); Thi truong Tai chinh Tien te (2026b) |
| Is VPS Smart Indexing the same thing? | No. VPS decides for the customer, holds shares only, starts at VND 50 million plus 10 million a month and charges 0.5% a year. Payday is customer-confirmed, holds four asset types and starts at VND 500,000. | Tuoi Tre (2026); Tin nhanh Chung khoan (2026) |
| Who is liable if Ensa's advice is wrong? | Ensa only collects the facts. A licensed adviser signs the model plans, every recommendation is logged, and nothing is invested without the customer's confirmation. | Ministry of Finance (2020), Articles 4 and 24; National Assembly (2019), Article 72 |
| What happens in a market fall? | Goals under a year hold only bank bonds. In the stress test, a fall in year 2 cuts new funded accounts at month 36 by 12.3% and month-60 cash by VND 0.35 billion. | Authors' cohort model; VnExpress (2026b) |
| Why not use DNSE's own bonds? | They would improve month-60 cash by about VND 3.9 billion, but they create a conflict of interest in an advised product. New Golden Egg openings were paused at the regulator's request in December 2023. | Authors' cohort model; DNSE Securities (2023) |
| Why not lend against the plan's ETFs? | Base NPV would improve only from −VND 25.0 billion to −VND 20.9 billion. It would also cut against the savings purpose and the 2026 margin findings, so we review it only at Gate 3. | Authors' cohort model; Market Times (2026) |
| What if the bank charges its list fee? | At VND 3,300 per contribution the CAC ceiling falls from VND 199,000 to VND 128,000; above VND 6,200 the dormant channel stops paying back. Gate 0 targets VND 0. | VPBank (2024); authors' cohort model |
| What if only 1% of dormant accounts enrol? | That is the break-even rate, so we would not scale: we scale at 1.5% and stop below 1.0%. The downside path costs about VND 10.0 million per new funded account and is stopped at month 6. | Authors' cohort model |
| Is Open API a threat or an opportunity? | Banks must comply by 1 March 2027 and customer consent lasts up to 180 days. Our virtual-account bank is the natural first Open API partner for salary-percentage contributions in Phase 3. | State Bank of Vietnam (2024) |
<!-- /table -->

Source: as listed in the table.

## References

- Ashraf, N., Karlan, D., & Yin, W. (2006). Tying Odysseus to the mast: Evidence from a commitment savings product in the Philippines. *The Quarterly Journal of Economics, 121*(2), 635–672. https://doi.org/10.1162/qjec.2006.121.2.635
- Bao Phap Luat. (2026, June 30). Thêm quỹ Dragon Capital, SSI iBoard mở rộng sản phẩm đầu tư trên nền tảng số [SSI iBoard adds Dragon Capital funds to its digital platform]. https://baophapluat.vn/them-quy-dragon-capital-ssi-iboard-mo-rong-san-pham-dau-tu-tren-nen-tang-so.html
- CafeF. (2026, July 22). Soi số lợi nhuận 15.200 tỷ của ngành chứng khoán trong quý 2 [The securities industry's VND 15,200 billion profit in Q2]. https://cafef.vn/soi-so-loi-nhuan-15200-ty-cua-nganh-chung-khoan-trong-quy-2-mot-cuoc-doi-ngoi-dang-am-tham-dien-ra-188260722020054991.chn
- DNSE Securities. (2023, December 24). Thông báo tạm dừng mở mới Egg X và Gift X [Notice pausing new Golden Egg (Egg X) and Gift X openings]. https://www.dnse.com.vn/tin-tuc/tb-tam-dung-eggx-va-giftx-25-12-2023
- DNSE Securities. (2025). So sánh các chương trình "sinh lời tự động" từ tiền nhàn rỗi 2025 [Comparison of automatic-earning programmes for idle cash, 2025]. https://www.dnse.com.vn/hoc/chuong-trinh-sinh-loi-tu-dong
- DNSE Securities. (2026a). Financial statements and investor relations releases, 2019 to the second quarter of 2026. https://ir.dnse.com.vn/vi/ctype-finance_report
- DNSE Securities. (2026b). Tài khoản Không Ngủ [Never-Sleeping Account, product page]. Retrieved September 24, 2026, from https://www.dnse.com.vn/san-pham/tai-khoan-khong-ngu
- DNSE Securities. (2026c). Báo cáo thường niên 2025 [Annual report 2025]. https://cdn.dnse.com.vn/dnse-assets/CBTT/DSE%20-%20BCTN%202025.pdf
- DNSE Securities. (2026d). Lightspeed API [Product page]. Retrieved September 27, 2026, from https://www.dnse.com.vn/lightspeed-api
- DNSE Securities. (2026e, March 4). Công bố thông tin về sự cố công nghệ thông tin [Disclosure of an IT incident]. https://ir.dnse.com.vn/vi/post/cong-bo-thong-tin-ve-su-co-cong-nghe-thong-tin-717.htm
- DNSE Securities. (2026f). Tài liệu họp Đại hội đồng cổ đông thường niên 2026 [2026 annual general meeting documents]. https://mobiv2.fireant.vn/News/NewsAttachedFile/1863037
- DNSE Securities. (n.d.-a). FAQ Trứng Vàng giao dịch trái phiếu [Golden Egg bond trading FAQ]. Retrieved October 16, 2026, from https://hdsd.dnse.com.vn/san-pham-dich-vu/sp-trung-vang/trung-vang-qua-giao-dich-trai-phieu-v2/faq-trung-vang-giao-dich-trai-phieu
- DNSE Securities. (n.d.-b). Trứng Vàng [Golden Egg, product page]. Retrieved October 16, 2026, from https://www.dnse.com.vn/san-pham/trung-vang
- Hanoi Stock Exchange. (2026). Quarterly announcements of the ten securities companies with the largest brokerage market share, Q4 2017 to Q2 2026 [Data set]. Retrieved September 25, 2026, from https://www.hnx.vn
- Karlan, D., McConnell, M., Mullainathan, S., & Zinman, J. (2016). Getting to the top of mind: How reminders increase saving. *Management Science, 62*(12), 3393–3411. https://doi.org/10.1287/mnsc.2015.2296
- KBSV. (n.d.). Periodic investment: Accumulate as desired. Retrieved October 16, 2026, from https://kbsec.com.vn/en/periodic-investment-accumulate-as-desired.htm
- KTQT FTUers. (2026). *DNSE Securities Joint Stock Company: Round 2 business analytics report* [Unpublished competition report]. Future Business Analyst Season 6, RMIT Business and Finance Club Hanoi.
- Madrian, B. C., & Shea, D. F. (2001). The power of suggestion: Inertia in 401(k) participation and savings behavior. *The Quarterly Journal of Economics, 116*(4), 1149–1187. https://doi.org/10.1162/003355301753265543
- Market Times. (2026, August 17). Chứng khoán DNSE (DSE) của Chủ tịch Nguyễn Hoàng Giang bị phạt hơn 800 triệu đồng vì loạt vi phạm trong hoạt động chứng khoán [DNSE fined more than VND 800 million for securities violations]. https://markettimes.vn/chung-khoan-dnse-dse-cua-chu-tich-nguyen-hoang-giang-bi-phat-128642.html
- Ministry of Finance. (2020). Circular No. 121/2020/TT-BTC on the operation of securities companies. https://thuvienphapluat.vn/van-ban/Doanh-nghiep/Thong-tu-121-2020-TT-BTC-huong-dan-hoat-dong-cua-cong-ty-chung-khoan-453690.aspx
- MobiFone. (n.d.). SMS Brandname. Retrieved October 16, 2026, from https://www.mobifone.vn/doanh-nghiep/cong-nghe-thong-tin/chi-tiet/24
- National Assembly of Vietnam. (2019). Law on Securities No. 54/2019/QH14. https://thuvienphapluat.vn/van-ban/Chung-khoan/Luat-Chung-khoan-nam-2019-399763.aspx
- National Statistics Office. (2026, July). Một số nét chính tình hình kinh tế – xã hội quý II và 6 tháng đầu năm 2026 [Socio-economic situation in the second quarter and first half of 2026]. https://www.nso.gov.vn/tin-tuc-thong-ke/2026/07/mot-so-net-chinh-tinh-hinh-kinh-te-xa-hoi-quy-ii-va-6-thang-dau-nam-2026/
- Nhan Dan. (2025, July 8). Công bố khảo sát 2025 về nhu cầu quản lý tài sản và đầu tư của người Việt [2025 survey of Vietnamese wealth management and investment needs]. https://nhandan.vn/cong-bo-khao-sat-2025-ve-nhu-cau-quan-ly-tai-san-va-dau-tu-cua-nguoi-viet-post892406.html
- O'Donoghue, T., & Rabin, M. (1999). Doing it now or later. *American Economic Review, 89*(1), 103–124. https://doi.org/10.1257/aer.89.1.103
- Pinetree Securities. (2026, March 4). Bản tin thị trường 04/03/2026 [Market bulletin, 4 March 2026]. https://pinetree.vn/post/20260304/ban-tin-thi-truong-04-03-2026/
- SSI Asset Management. (2026). Thông tin chung quỹ SSIBF [SSIBF fund information]. Retrieved October 16, 2026, from https://ssiam.com.vn/thong-tin-chung-quy-ssibf
- SSI Securities. (2026, April 23). Tích sản thảnh thơi cùng tính năng đầu tư chứng chỉ quỹ tự động tại SSI [Easy accumulation with automatic fund investing at SSI]. https://www.ssi.com.vn/tin-tuc/tin-tuc-chung/tich-san-thanh-thoi-cung-tinh-nang-dau-tu-chung-chi-quy-tu-dong-tai-ssi
- State Bank of Vietnam. (2024). Circular No. 64/2024/TT-NHNN on the implementation of open application programming interfaces in the banking sector.
- TCBS. (2026, July). Thông cáo báo chí kết quả kinh doanh quý 2/2026 [Press release on second-quarter 2026 results]. https://www.tcbs.com.vn/wp-content/uploads/2026/07/Press-Release_2Q2026_VN_FINAL.pdf
- Thi truong Tai chinh Tien te. (2021, June 23). VinaCapital ra mắt chương trình đầu tư định kỳ thông minh VinaSIP [VinaCapital launches the VinaSIP systematic investment plan]. https://thitruongtaichinhtiente.vn/vinacapital-ra-mat-chuong-trinh-dau-tu-dinh-ky-thong-minh-vinasip-36072.html
- Thi truong Tai chinh Tien te. (2026a). Agribank chào bán 15.000 tỷ đồng trái phiếu ra công chúng năm 2026 [Agribank offers VND 15,000 billion of public bonds in 2026]. https://thitruongtaichinhtiente.vn/agribank-chao-ban-15-000-ty-dong-trai-phieu-ra-cong-chung-2026-84152.html
- Thi truong Tai chinh Tien te. (2026b, October 1). Lãi suất đầu tháng 10/2026: Tiết kiệm giữ nhịp ổn định, chứng chỉ tiền gửi hút khách [Interest rates in early October 2026]. https://thitruongtaichinhtiente.vn/lai-suat-dau-thang-10-2026-tiet-kiem-giu-nhip-on-dinh-chung-chi-tien-gui-hut-khach-85944.html
- Tin nhanh Chung khoan. (2026, August 11). VPS chính thức ra mắt sản phẩm VPS Smart Indexing [VPS launches VPS Smart Indexing]. https://www.tinnhanhchungkhoan.vn/vps-chinh-thuc-ra-mat-san-pham-vps-smart-indexing-post395704.html
- Tuoi Tre. (2026, September 25). VPS triển khai đầu tư theo danh mục, vốn từ 50 triệu đồng [VPS offers portfolio investing from VND 50 million]. https://tuoitre.vn/vps-trien-khai-dau-tu-theo-danh-muc-von-tu-50-trieu-dong-100260925082458764.htm
- VCBF. (2026). VCBF Fixed Income Fund (VCBF-FIF) factsheet, September 2026. https://www.vcbf.com/images/2026/vcbf_fixed_income_fund_vcbf-fif_092026.pdf
- VCBF. (n.d.). About SIP. Retrieved October 16, 2026, from https://www.vcbf.com/en/open-ended-funds/systematic-investment-plan-sip/about-sip/
- Vietcap Securities. (2026). Financial statements of DSE and other securities companies, Q1 2018 to Q2 2026 [Data set]. Vietcap IQ. Retrieved September 24, 2026, from https://iq.vietcap.com.vn
- Vietstock. (2026a, March 26). Những nội dung đáng chú ý ở ĐHĐCĐ thường niên DNSE 2026 [Highlights of DNSE's 2026 AGM]. https://vietstock.vn/2026/03/nhung-noi-dung-dang-chu-y-o-dhdcd-thuong-nien-dnse-2026-737-1415846.htm
- Vietstock. (2026b, July 21). Dư nợ margin lập kỷ lục 454 ngàn tỷ đồng, cuộc đua có sự phân hóa [Margin lending reaches a record VND 454 trillion]. https://vietstock.vn/2026/07/du-no-margin-lap-ky-luc-454-ngan-ty-dong-cuoc-dua-co-su-phan-hoa-830-1468883.htm
- VnEconomy. (2025, July 8). Lời giải nào cho nghịch lý giữa kỳ vọng sinh lời và tâm lý e ngại của nhà đầu tư Việt? [Resolving the paradox between Vietnamese investors' return expectations and caution]. https://vneconomy.vn/loi-giai-nao-cho-nghich-ly-giua-ky-vong-sinh-loi-va-tam-ly-e-ngai-cua-nha-dau-tu-viet.htm
- VnEconomy. (2026, July 22). Lãi suất cao khiến số dư tiền gửi của nhà đầu tư tại công ty chứng khoán giảm về mức thấp nhất 1 năm? [High interest rates push investor deposits at brokers to a one-year low]. https://vneconomy.vn/lai-suat-cao-khien-so-du-tien-gui-cua-nha-dau-tu-tai-cong-ty-chung-khoan-giam-ve-muc-thap-nhat-1-nam.htm
- VNDIRECT. (n.d.). Tích sản hưu trí [Retirement accumulation plan]. Retrieved October 16, 2026, from https://dautu.vndirect.com.vn/san-pham/tich-san-huu-tri/
- VnExpress. (2025, July 21). Cách DNSE thu hút khách hàng gen Z [How DNSE attracts Gen Z customers]. https://vnexpress.net/cach-dnse-thu-hut-khach-hang-gen-z-4916725.html
- VnExpress. (2026a, September 10). Người Việt mở thêm 2 triệu tài khoản chứng khoán sau 8 tháng [Vietnamese open 2 million more securities accounts in eight months]. https://vnexpress.net/nguoi-viet-mo-them-2-trieu-tai-khoan-chung-khoan-sau-8-thang-5118477.html
- VnExpress. (2026b, March 9). VN-Index giảm mạnh nhất lịch sử [The VN-Index's largest one-day fall]. https://vnexpress.net/vn-index-mat-hon-90-diem-5048146.html
- VPBank. (2024). Biểu phí quản lý tiền tệ dành cho khách hàng doanh nghiệp [Cash management fee schedule for corporate customers]. https://www.vpbank.com.vn/-/media/vpbank-latest/tai-lieu-bieu-mau/bieu-phi/kh-dn/2024/bieu-phi-quan-ly-tien-te-danh-cho-khach-hang-doanh-nghiep.pdf
- VPBank. (2026). VPBank chính thức ra mắt "Hũ Mục Tiêu" [VPBank launches Goal Jar]. https://www.vpbank.com.vn/tin-tuc/tin-vpbank/2026/vpbank-chinh-thuc-ra-mat-hu-muc-tieu-tiet-kiem-cung-hoi-cham-dich-cung-vui
- World Bank. (2025). Global Financial Inclusion (Global Findex) database 2025, Vietnam [Data set]. World Bank Open Data. Retrieved September 20, 2026, from https://api.worldbank.org/v2/sources/28/country/VNM/series/all/data?format=json
- Zalo Business Solutions. (n.d.). Bảng giá và hướng dẫn tính giá ZBS Template Message [ZBS template message pricing]. Retrieved October 16, 2026, from https://zalo.solutions/zns/pricing

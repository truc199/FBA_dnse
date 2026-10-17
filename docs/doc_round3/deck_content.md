# Round 3A deck content: Payday Portfolio (bản 2)

*Bản 1 (16/10/2026) đã được user duyệt câu chuyện ở checkpoint 3.1. Bản 2 (17/10/2026): đủ hình, mọi bảng sinh từ CSV, appendix và references nằm ở `deck_appendix.md`.*

**Đọc file này thế nào**
- Mỗi slide theo đúng khung của prompt: action title, on-slide text, bảng, hình, designer notes, speaker notes, sources.
- Chữ trên slide và speaker notes viết bằng tiếng Anh, cho giám khảo đóng vai Board. Designer notes viết bằng tiếng Việt, cho người dựng slide.
- **Bảng không sửa trực tiếp ở đây.** Mỗi bảng nằm giữa hai dòng `<!-- table: ... -->` và được ghi từ CSV bằng `python src/round3/deck_tables.py`. Muốn đổi chữ thì sửa CSV mẫu trong `data/round3/deck_tables/`; số thì lấy từ mô hình.
- Hình nằm trong `outputs/round3/figures/`, vẽ bằng `figures_round3.py` và `diagrams_round3.py`; dữ liệu của từng hình ghi ở dòng "Data".
- Số lấy từ `outputs/round3/tables/` (kịch bản base, trừ khi ghi khác) và từ các nguồn trong `data/round3/sources_round3.csv`.
- Kiểm bằng `python src/round3/check_deck_content.py`:
  - action title ≤15 từ; chữ trên slide ≤60 từ; Executive Summary ≤150 từ;
  - bảng ≤6 dòng × 5 cột; speaker notes khoảng 120 từ;
  - mỗi bảng khớp CSV của nó.

**Quy ước làm tròn trên slide** (số gốc nằm trong CSV):
- Trần CAC VND 128,000 (127,512); trần khi miễn phí VA VND 199,000 (198,876).
- Ngưỡng phí VA VND 6,200 (6,191); ngưỡng mức góp VND 717,000 (716,502).
- Chi phí ròng/TK mới ≥10 triệu: "about VND 1.3 million" trong câu, 1.29 trong bảng.
- Tỷ lệ từ review đọc tay làm tròn đến số nguyên (83%, 45%, 17%).

---

## Câu chuyện của deck

**Một câu (thay cho câu ở `plan_payday.md` §1):**
> *DNSE has won accounts; Payday Portfolio sets out to win balances. It turns part of each salary into a goal-based plan the customer controls, and asks the Board for VND 6.6 billion it can stop at month 6.*

**Mạch 15 slide:**
1. **Vấn đề (slide 2–5):**
   - DNSE có tài khoản nhưng không có tiền.
   - Năm 2026 tiền rời CTCK và đối thủ đã vào cuộc đua tích lũy.
   - Mỗi insight dẫn tới một lựa chọn thiết kế.
   - Những gì đã đổi so với Round 2.
2. **Giải pháp (slide 6–10):** cho ai; sản phẩm là gì; khách thấy gì; phía sau vận hành ra sao; đứng ở đâu so với đối thủ.
3. **Kế hoạch (slide 11–15):**
   - Business case trung thực: base không tự hoàn vốn, nên mua TK có tiền với giá khoảng 1,3 triệu.
   - GTM năm 1, lộ trình 5 phase, cổng quyết định có số.
   - Rủi ro và đề nghị cụ thể với Board.

**Ba điều giám khảo cần nhớ:**
- VND 6,6 tỷ, dừng được ở tháng 6.
- +14.871 TK mới ≥10 triệu ở tháng 36 (base).
- Khoảng 1,3 triệu đồng cho mỗi TK có tiền.

---

## Slide 1: Executive summary

**Action title:** Approve VND 6.6 billion to test whether payday plans can fund DNSE's accounts

**On-slide text:**
**Problem.** DNSE opens one in five new accounts in Vietnam, yet only 1.8% of its 1.51 million accounts hold VND 10 million or more, and brokerage has lost money for 16 quarters.

**Solution.** Payday Portfolio is a goal-based monthly plan from VND 500,000. A standing order from the salary bank funds a personal virtual account. The customer confirms an adviser-signed plan of bank bonds, funds and an ETF. No platform fee; delivery metrics published monthly.

**Business case.** Base case: no payback within five years (NPV −VND 25 billion). Upside: payback in month 44.

**Ask.** Fund build and a 45,000-account pilot; stop or scale at month 6.

**Table:**

<!-- table: slide01_key_figures -->
| Key figure | What it means |
|---|---|
| VND 6.6 billion | Board ask for months 1 to 6 |
| +14,871 | New accounts above VND 10 million by month 36 (base) |
| VND 1.3 million | Net cost per new funded account (base) |
<!-- /table -->

CSV: `outputs/round3/tables/slide01_key_figures.csv` (sinh bằng `src/round3/deck_tables.py` từ `data/round3/deck_tables/` và output của mô hình; sửa CSV mẫu, không sửa bảng ở đây).
Source: authors' cohort model; DNSE Securities (2026c).

**Figure:** không có (3 con số lớn thay cho hình).

**Designer notes (tiếng Việt):**
- Cỡ chữ 14–15 theo booklet. Ba con số đặt thành 3 ô lớn ở hàng trên, màu RED; bốn đoạn Problem / Solution / Business case / Ask ở dưới, mỗi đoạn một dòng nhãn đậm.
- Tổng số từ của slide (kể cả 3 ô số) phải ≤150; script kiểm đã tính cả bảng.
- Không thêm hình, logo hay câu nào khác vào slide này.

**Speaker notes:**
Good afternoon. DNSE has done the hard part of growth: it opens one in five new securities accounts in Vietnam. But accounts are not money. Only 1.8 per cent of its 1.5 million accounts hold ten million dong or more, and the free-trading model has not paid for itself. Payday Portfolio is our answer: a monthly plan, set up once, that moves part of each salary towards a goal the customer chooses, through bank bonds, funds and an ETF. We will be direct about the economics. In the base case Payday is not a profit centre; it buys funded accounts at about 1.3 million dong each. So we ask for only 6.6 billion dong now, with a clear stop-or-scale decision at month six.

**Sources:** DNSE Securities (2026c); authors' cohort model.

---

## Slide 2: Problem recap: accounts, not money

**Action title:** DNSE has 12.3% of Vietnam's accounts but only 2.3% of investor cash

**On-slide text:**
- Only 1.8% of DNSE's 1.51 million accounts held VND 10 million or more (December 2025).
- The closer to money, the smaller DNSE gets: 1.4% of margin loans, 0.6% of profit.
- Brokerage revenue trailed its direct cost for 16 straight quarters (−VND 190 billion).
- The platform costs VND 7.3 million a year per funded account.

**Figure:** `outputs/figures/fig04_market_position.png` (dùng lại Figure 4 của Round 2).
Caption: DNSE's share of each market, per cent; the dashed line is its 12.3% share of accounts.
Source: VnExpress (2026a); DNSE Securities (2026c); Vietstock (2026b); CafeF (2026); VnEconomy (2026); Hanoi Stock Exchange (2026); DNSE filings; authors' calculations (Round 2, Figure 4).

**Designer notes (tiếng Việt):**
- Hình Figure 4 chiếm 2/3 slide, bên trái; 4 ý ở cột phải.
- Nhấn mạnh hai thanh "Customer accounts 12.3" và "Investor cash 2.3" (đã có màu khác nhau trong hình).
- Ghi nhỏ ở góc: "Round 2 finding, unchanged".
- Nếu cần chỗ, bỏ ý thứ 4 lên speaker notes.

**Speaker notes:**
In Round 2 we showed one fact that frames everything today. DNSE is very good at opening accounts: one in five new accounts in Vietnam last year, and 12.3 per cent of all accounts by mid-2026. But the closer a measure sits to money, the smaller DNSE becomes: 2.3 per cent of investor cash, 1.4 per cent of margin loans and 0.6 per cent of industry profit. Only 1.8 per cent of DNSE's accounts hold ten million dong or more. This matters because free trading does not pay for itself: brokerage revenue has been below its direct cost for sixteen quarters in a row. Every funded account also carries about 7.3 million dong a year of platform cost. Funding the accounts DNSE already has is the cheapest fix.

**Sources:** DNSE Securities (2026a, 2026c); Hanoi Stock Exchange (2026); VnEconomy (2026); Vietstock (2026b); CafeF (2026); VnExpress (2026a); Vietcap Securities (2026).

---

## Slide 3: Why now

**Action title:** The 2026 accumulation race has started, and DNSE has no entry yet

**On-slide text:**
- Investor cash at brokers fell 38% in three quarters, to VND 86.6 trillion (June 2026).
- Banks pay 5.9% for 12 months; certificates of deposit pay 7.4%.
- SSI, TCBS, VPS and VPBank launched recurring or goal-based plans in 2026.
- Banks must open their APIs by 1 March 2027.
- DNSE made about 20% of its 2026 profit target in H1.

**Figure:** `outputs/round3/figures/why_now_timeline.png`.
Caption: Left, 2026 launches of recurring and goal-based plans and the banks' Open API deadline. Right, investor cash at Vietnamese brokers, VND trillion (Q4 2025 not reported).
Source: SSI Securities (2026); TCBS (2026); Tin nhanh Chung khoan (2026); Tuoi Tre (2026); VPBank (2026); State Bank of Vietnam (2024); VnEconomy (2026).
Data: `outputs/round3/tables/why_now_events.csv`, `why_now_investor_cash.csv`.

**Designer notes (tiếng Việt):**
- Hình đã gồm cả timeline và cột tiền NĐT, đặt nửa trên slide, toàn chiều ngang. Mốc đối thủ màu xám; "DNSE today" màu RED; mốc Open API màu DARK_RED.
- 5 ý chữ đặt nửa dưới, chia 2 cột: "Money is leaving" (ý 1–2) và "Rivals are moving" (ý 3–5).
- Q4/2025 không có số liệu công bố nên để trống trong hình; không nối cột.

**Speaker notes:**
Why act now? Three things changed this year. First, money is leaving brokers. Investor cash at Vietnamese brokers fell 38 per cent in three quarters, while banks pay 5.9 per cent for twelve months and certificates of deposit 7.4. Second, competitors have started an accumulation race. SSI ran a recurring-fund campaign from April, TCBS turned TCWealth into goal-based portfolios, VPS launched Smart Indexing in August and VPBank launched goal jars in September. DNSE has no entry. Third, banks must open their APIs by March 2027, which makes salary-linked investing easier for whoever has a product ready. Meanwhile DNSE made only about a fifth of its 2026 profit target in the first half. A product that builds balances is now urgent.

**Sources:** VnEconomy (2026); Thi truong Tai chinh Tien te (2026b); SSI Securities (2026); TCBS (2026); Tin nhanh Chung khoan (2026); VPBank (2026); State Bank of Vietnam (2024); Vietstock (2026a); DNSE Securities (2026a).

---

## Slide 4: Insight, design decision, impact

**Action title:** Every design choice traces to evidence and to one KPI the pilot measures

**On-slide text:**
- Round 2's root causes still hold; 2026 data adds reliability as the first barrier.
- Each KPI has a stop line in the pilot (slide 14).

**Table:**

<!-- table: slide04_insight_design -->
| Insight | Evidence | Design decision | KPI it moves |
|---|---|---|---|
| Accounts are opened but not funded | 98% of accounts hold under VND 10 million | A monthly plan funded by a standing order from the salary bank | New accounts above VND 10 million: +14,871 by month 36 |
| Intention stalls without a plan | 77% of investors find managing a portfolio hard | A plan by goal horizon, signed by a licensed adviser and confirmed by the customer | Three contributions in a row: 81% (stop below 60%) |
| Conditional rewards broke trust | Trust themes: 55% of negative Google Play reviews, H1 2025 | No cash rewards; all terms on one screen; free withdrawal | Trust themes below 10% of Payday reviews |
| 2026 update: reliability now dominates | 83% of 2026 negative reviews describe something that broke | Payday scheduler kept apart from the pre-trade check; 99.5% launch gate | 99.5% credited on the same banking day |
| Small tickets carry heavy unit costs | A VND 1 million contribution pays a VND 3,300 bank fee and earns VND 368 a month | Gate 0: collection fee target VND 0 | CAC ceiling rises from VND 128,000 to 199,000 |
<!-- /table -->

CSV: `outputs/round3/tables/slide04_insight_design.csv` (sinh bằng `src/round3/deck_tables.py` từ `data/round3/deck_tables/` và output của mô hình; sửa CSV mẫu, không sửa bảng ở đây).
Source: DNSE Securities (2026c); Nhan Dan (2025); Google Play and App Store reviews, authors' coding; VPBank (2024); authors' cohort model.

**Figure:** `outputs/round3/figures/reviews_2026_causes.png` (nửa slide, tùy chọn; có thể chuyển xuống appendix D nếu chật).
Caption: Causes in 58 negative reviews of DNSE's app, January to September 2026; a review can carry several causes.
Source: Google Play; App Store; authors' coding of each review.

**Designer notes (tiếng Việt):**
- Đây là slide ăn điểm "evidence-to-solution linkage" (25 điểm). Bảng 5 dòng là trung tâm, có mũi tên giữa các cột Insight → Decision → KPI.
- Dòng "2026 update" tô nền LIGHT_RED để thấy đây là cập nhật mới.
- Nếu đặt hình nguyên nhân review: thu nhỏ ở góc phải, nối bằng đường mảnh tới dòng 4.

**Speaker notes:**
This slide links each insight to a design choice and to the KPI that tests it. Accounts are opened but not funded, so a standing order from the salary bank funds the plan; we count new accounts above ten million dong. Intention stalls without a plan: 77 per cent of investors find portfolios hard, so a licensed adviser signs a plan by goal horizon and the customer confirms it. Conditional rewards broke trust in 2025, so there is no cash reward and every term sits on one screen. The 2026 update is reliability: 83 per cent of this year's negative reviews describe something that broke. So the payday scheduler runs apart from the trading check, and 99.5 per cent on-time crediting is a launch gate.

**Sources:** DNSE Securities (2026c); Nhan Dan (2025); Google Play and App Store reviews (authors' coding); VPBank (2024); authors' cohort model.

---

## Slide 5: What changed since Round 2

**Action title:** We kept the mechanism and rebuilt the numbers, rewards and positioning

**On-slide text:**
- Kept: the dormant salaried target, personal virtual account, adviser-signed plan the customer confirms, rebalancing with new money, SSC notice and a randomised pilot.

**Table:**

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

CSV: `outputs/round3/tables/slide05_what_changed.csv` (sinh bằng `src/round3/deck_tables.py` từ `data/round3/deck_tables/` và output của mô hình; sửa CSV mẫu, không sửa bảng ở đây).
Source: KTQT FTUers (2026); authors' cohort model; Thi truong Tai chinh Tien te (2021); DNSE Securities (2026c).

**Figure:** không có (bảng là nội dung chính).

**Designer notes (tiếng Việt):**
- Bảng 3 cột; cột "Round 2" chữ xám, cột "Round 3A" chữ đen, phần "why" in nghiêng.
- Dòng "Kept" đặt trên cùng thành dải màu nhạt có dấu ✓. Rubric khen việc giải thích vì sao giữ.
- Nếu ban tổ chức gửi feedback Round 2, thêm cột "Feedback" (`plan_payday.md` §2).

**Speaker notes:**
What changed since Round 2, and why. We kept the core: the target segment, the personal virtual account, the adviser-signed plan the customer confirms, rebalancing with new money, the regulator notice and a randomised pilot. Five things changed. Our Round 2 model assumed every saver contributed for eighteen months. With monthly cohorts and sourced costs, the base case reaches about 42,000 accounts above ten million dong by month 36, against a Round 2 target of 85,000 in eighteen months. The pilot grows to 45,000 accounts so it can detect a ten-point effect, with thresholds derived from unit economics. Cash tiers would cost 41 per cent of revenue, so rewards are non-cash. DNSE's own bonds leave the default plan. And recurring transfers are now standard, so we compete on asset range and proof.

**Sources:** KTQT FTUers (2026); authors' cohort model; Thi truong Tai chinh Tien te (2021); DNSE Securities (2026c).

---

## Slide 6: Target users and sizing

**Action title:** Launch with dormant salaried accounts; most savers later arrive at account opening

**On-slide text:**
- Salaried dormant holders test the offer first: 45,000 accounts in the pilot.
- By month 36, 60% of the 31,133 savers come from the account-opening step.
- Employers are tested from Q4 and pay back only above 39% participation.

**Table:**

<!-- table: slide06_personas -->
|  | P1 Salaried dormant holder (launch) | P2 Active trader adding a core | P3 New account holder |
|---|---|---|---|
| Size | 1.43 million accounts used no product in December 2025 | 85,739 active customers | About 31,180 new accounts a month (H1 2026) |
| Job to be done (hypothesis) | "Invest part of my salary without deciding each month" | "Grow a long-term core while I trade" | "Start small and see it work" |
| Barrier (evidence) | Procrastination; distrust after the 2025 rewards | Plan money drifting back to trading | Reward-seeking; eKYC failures (17% of 2026 negative reviews) |
| Model input (assumption) | 25% salaried and reachable; 2% enrol | 4% enrol over 12 months | 2% set up within 60 days |
| Savers by month 36 (base) | 6,836 | 3,430 | 18,708 |
<!-- /table -->

CSV: `outputs/round3/tables/slide06_personas.csv` (sinh bằng `src/round3/deck_tables.py` từ `data/round3/deck_tables/` và output của mô hình; sửa CSV mẫu, không sửa bảng ở đây).
Source: DNSE Securities (2026c); VnExpress (2026a); authors' cohort model.

**Figure:** `outputs/round3/figures/sizing_funnel.png`.
Caption: Left, from DNSE's 1.51 million accounts to dormant savers by month 36. Right, all 31,133 savers by month 36, by channel (base case).
Source: DNSE Securities (2026c); authors' cohort model (assumptions labelled).
Data: `outputs/round3/tables/sizing_funnel.csv`, `savers_by_channel.csv`.

**Designer notes (tiếng Việt):**
- Trái: hình funnel và thanh saver theo kênh (nửa slide). Phải: bảng persona (P1 viền RED vì là khách ra mắt).
- Mỗi persona ghi rõ "assumption" ở dòng thông số mô hình. Không thêm ảnh người, tên hay tuổi cụ thể: persona dựng từ data, không bịa đời tư.
- Phần account opening (60%) đã tô RED trong hình để khớp với ý thứ hai.

**Speaker notes:**
Who is it for? We launch with salaried holders of dormant accounts: 1.43 million DNSE accounts used no product in December 2025, and nearly half of working adults in Vietnam are paid into an account. We assume a quarter of dormant accounts are salaried and reachable, and that two per cent of those contacted enrol; the pilot will measure both. Active traders are a second group: they want a long-term core next to trading. The third group matters most for scale. About 31,000 accounts are opened each month, and a plan step at opening brings in 60 per cent of all savers by month 36. Employers come later and pay back only if at least 39 per cent of staff join.

**Sources:** DNSE Securities (2026c); World Bank (2025); VnExpress (2026a); authors' cohort model.

---

## Slide 7: The solution

**Action title:** A goal-based monthly plan from VND 500,000 that the customer always controls

**On-slide text:**
- Customer: one plan per goal; cash waits in the Never-Sleeping Account (Tài khoản Không Ngủ); withdraw free in one tap.
- DNSE: funded accounts, on payment rails that also tackle deposit-crediting failures.
- No platform fee; fund fees of 0.8–1.95% a year sit inside fund prices.
- Excluded: margin, single stocks, derivatives, DNSE's own bonds, sign-up cash.

**Table:**

<!-- table: slide07_glide_path -->
| Goal horizon | Golden Egg (Trứng Vàng), bank bonds | Bond funds | Equity funds | VN30 ETF |
|---|---|---|---|---|
| Under 1 year | 100% | – | – | – |
| 1 to 3 years | 50% | 50% | – | – |
| 3 years or more | 30% | 30% | 20% | 20% |
| Last 12 months before the goal | New money only, into Golden Egg | Nothing sold | Nothing sold | Nothing sold |
<!-- /table -->

CSV: `outputs/round3/tables/slide07_glide_path.csv` (sinh bằng `src/round3/deck_tables.py` từ `data/round3/deck_tables/` và output của mô hình; sửa CSV mẫu, không sửa bảng ở đây).
Source: authors' design; fund fees from SSI Asset Management (2026), VCBF (2026) and fund prospectuses.

**Figure:** `outputs/round3/figures/solution_overview.png`.
Caption: How Payday works: advise, fund on payday, hold briefly, invest new money; with the persistence package and the trust controls.
Source: authors' design (redraws Round 2 Figure 7 without cash tiers).
Data: `data/round3/solution_overview.json`.

**Designer notes (tiếng Việt):**
- Nửa trên: sơ đồ 4 bước. Nửa dưới trái: bảng glide path. Nửa dưới phải: 4 ý chữ.
- Dòng "Excluded" có biểu tượng gạch chéo, màu xám đậm, để Board thấy rõ những gì cố ý loại.
- Lần đầu xuất hiện thuật ngữ tiếng Việt phải có bản dịch: "Trứng Vàng (Golden Egg)", "Tài khoản Không Ngủ (Never-Sleeping Account)".

**Speaker notes:**
The product in one line: a goal-based monthly plan from 500,000 dong that the customer controls. The customer sets a goal, answers three suitability questions and confirms a plan signed by a licensed adviser. The salary bank sends a standing order to a virtual account in the customer's name. Cash waits in the Never-Sleeping Account and is invested, usually the next business day, into the most underweight asset. The mix follows the goal horizon: short goals stay in bank bonds through Golden Egg; long goals add funds and a VN30 ETF, with equities capped at 40 per cent. There is no platform fee. We deliberately leave out margin, single stocks, derivatives, DNSE's own bonds and sign-up cash.

**Sources:** DNSE Securities (n.d.-b); SSI Asset Management (2026); VCBF (2026); Ministry of Finance (2020); Karlan et al. (2016).

---

## Slide 8: Customer journey

**Action title:** Six screens take a saver from a goal to the 90-day milestone

**On-slide text:**
- Each screen answers the question the customer has at that step.
- Failure screens are designed in advance: transfer late, salary late, skip a month, withdraw (Appendix G).

**Figure:** `outputs/round3/figures/wireframes_journey.png`.
Caption: Low-fidelity wireframes of the six main screens; values in brackets are filled in by the live app.
Source: authors' design.

**Table:**

<!-- table: slide08_moments_of_truth -->
| Moment of truth | What the customer sees | Measure we publish |
|---|---|---|
| First money in | "Received" within minutes; invested the next business day | Contributions credited on the same banking day: ≥99.5% |
| First money out | Arrival time and cost in VND before confirming; free to the linked bank | Median time from request to the bank |
| First failure | Streak kept; one clear next step: send now or skip | Incident note within 5 business days |
<!-- /table -->

CSV: `outputs/round3/tables/slide08_moments_of_truth.csv` (sinh bằng `src/round3/deck_tables.py` từ `data/round3/deck_tables/` và output của mô hình; sửa CSV mẫu, không sửa bảng ở đây).
Source: authors' design.

**Designer notes (tiếng Việt):**
- 6 điện thoại xếp ngang chiếm 2/3 slide; bảng 3 dòng ở dưới.
- Hình hiện tại là low-fi bằng matplotlib. **Thay bằng bản Figma** nếu team kịp vẽ; giữ nguyên chữ trong `data/round3/wireframe_copy.json`.
- Đánh số 1–6 khớp với caption. Đánh dấu màn hình 5 (tiền vào lần đầu) bằng viền RED.

**Speaker notes:**
Here is the experience on six screens. A saver picks a goal, say a home, 36 million dong by October 2029, and sees the monthly amount. A short suitability check sets the risk profile, with the legal reason shown. The plan screen shows the mix, a bad month in dong and every fee. The fourth screen gives a personal account number and opens the bank app. On payday the customer sees the money received and invested. At day 90 the streak unlocks priority access to new Golden Egg issues. Three moments decide trust: the first money in, the first money out and the first failure. We designed the failure screens in advance, so a late transfer keeps the streak and offers one clear next step.

**Sources:** authors' design; Ministry of Finance (2020).

---

## Slide 9: Service blueprint

**Action title:** Every payday step has an owner and a fallback when something fails

**On-slide text:**
- New build: personal virtual accounts and a scheduler kept apart from the pre-trade check that failed on 4 March 2026.
- Reused: Ensa, Golden Egg, the Never-Sleeping Account and ETF trading.

**Figure:** `outputs/round3/figures/service_blueprint.png`.
Caption: Service blueprint of one payday cycle: customer, frontstage, backstage and support, with decision points, failure handling and owners.
Source: authors' design; DNSE Securities (2026e).

**Table:**

<!-- table: slide09_failure_handling -->
| When this fails | What happens | Owner |
|---|---|---|
| Money not in by the grace date (the 15th) | Suggest skipping the month; streak kept | CTO; Operations |
| An order fails | Retried next session; cash keeps earning in the Never-Sleeping Account | CTO |
| Two months missed | Suggest a pause, not a cancellation | Head of Product |
| Transfer to the bank fails | Money returns to plan cash; a call within 1 business day | Customer Service |
<!-- /table -->

CSV: `outputs/round3/tables/slide09_failure_handling.csv` (sinh bằng `src/round3/deck_tables.py` từ `data/round3/deck_tables/` và output của mô hình; sửa CSV mẫu, không sửa bảng ở đây).
Source: authors' design.

**Designer notes (tiếng Việt):**
- Blueprint đầy đủ khá dày chữ (khoảng 9,6pt ở khổ toàn slide). Trên slide có thể chỉ giữ 4 làn: khách hàng, frontstage, backstage, xử lý lỗi. Bản đầy đủ đưa xuống appendix G.
- Ba đường (interaction, visibility, internal interaction) phải thấy rõ; nét đứt.
- Bảng 4 dòng đặt dưới cùng, màu chữ RED cho cột "When this fails".

**Speaker notes:**
Behind the screens, this blueprint shows who does what. Above the line of visibility, the customer sees notices and statements. Below it, the scheduler expects each payday, the virtual account credits the customer automatically and the order engine buys funds or Golden Egg. Two decisions are automatic: whether the money arrived by the grace date, and whether there is enough for an ETF lot. Every failure has a fallback and an owner. If money is late, we wait until the fifteenth, then suggest skipping, and the streak is kept. If an order fails, it is retried next session while cash keeps earning. On 4 March 2026 DNSE's pre-trade check stopped orders for two hours, so the Payday scheduler runs apart from it.

**Sources:** DNSE Securities (2026e); authors' design.

---

## Slide 10: Competitive positioning

**Action title:** Recurring plans are now standard; Payday competes on asset range and published proof

**On-slide text:**
- Of 20 rival products we reviewed, several offer goal-based or multi-fund investing.
- None we found combines bank bonds, funds and an ETF in one customer-confirmed plan from VND 500,000.
- None we found publishes its transfer-success rate or withdrawal times.
- Based on public information as of 16 October 2026.

**Table:**

<!-- table: slide10_competitors -->
| Product | Assets | Minimum | Who decides | Fee |
|---|---|---|---|---|
| VPS Smart Indexing (Aug 2026) | Shares, direct indexing | VND 50 million, then 10 million a month | VPS (discretionary) | 0.5% a year |
| SSI eSIP (Apr 2026) | SSIAM and Dragon Capital funds | Not found | Customer | No subscription fee on SSIBF |
| TCBS TCWealth (Q2 2026) | Goal-based portfolios | Not found | Not stated | Not found |
| VNDIRECT Tích sản hưu trí (Retirement accumulation) | Bond and equity funds, 80/20 | VND 1 million | Customer | 0.1% a year |
| VCB Digibank SIP (VCBF) | VCBF funds | VND 100,000 a period | Customer | Lower SIP redemption fee |
| Payday Portfolio (proposed) | Bank bonds, bond and equity funds, VN30 ETF | VND 500,000 a month | Customer confirms an adviser-signed plan | No platform fee |
<!-- /table -->

CSV: `outputs/round3/tables/slide10_competitors.csv` (sinh bằng `src/round3/deck_tables.py` từ `data/round3/deck_tables/` và output của mô hình; sửa CSV mẫu, không sửa bảng ở đây).
Source: Tuoi Tre (2026); Tin nhanh Chung khoan (2026); SSI Securities (2026); Bao Phap Luat (2026); SSI Asset Management (2026); TCBS (2026); VNDIRECT (n.d.); VCBF (n.d.); authors' review, 16 October 2026.

**Figure:** `outputs/round3/figures/positioning_map.png`.
Caption: Minimum to start against the number of asset types in one plan. Only products with a verified minimum are plotted; we found no published minimum for SSI eSIP, TCBS TCWealth or VPBank Goal Jar.
Source: Tuoi Tre (2026); VNDIRECT (n.d.); VCBF (n.d.); Thi truong Tai chinh Tien te (2021); authors' design.
Data: `outputs/round3/tables/positioning_map.csv`.

**Designer notes (tiếng Việt):**
- Trái: bảng 6 dòng. Phải: bản đồ định vị (nửa slide); ô "small ticket, several asset types" đã tô nhạt, Payday là chấm RED duy nhất.
- **Không viết "the only"** ở bất kỳ đâu. Dòng "Based on public information as of 16 October 2026" bắt buộc phải có.
- Appendix C: 9 sản phẩm tác giả đã tự kiểm và 11 sản phẩm tra cứu tại bàn, tổng 20 sản phẩm đối thủ.

**Speaker notes:**
Where does Payday sit? We reviewed twenty rival products from brokers, banks and fintech apps. Recurring transfers are standard: VinaCapital has offered them since 2021, and Vietcombank customers can invest from 100,000 dong a period. Goal-based plans exist too, such as TCBS TCWealth and VNDIRECT's retirement plan. So we do not claim to be first. VPS Smart Indexing targets wealthier investors, from 50 million dong with a 0.5 per cent fee, and VPS decides for the customer. Payday sits in the empty middle: 500,000 dong a month, bank bonds, funds and an ETF in one plan, and the customer confirms every change. Its lasting edge is reach into 1.5 million accounts DNSE already holds, plus delivery metrics we publish monthly.

**Sources:** Tuoi Tre (2026); Tin nhanh Chung khoan (2026); SSI Securities (2026); Bao Phap Luat (2026); SSI Asset Management (2026); TCBS (2026); VNDIRECT (n.d.); VCBF (n.d.); Thi truong Tai chinh Tien te (2021).

---

## Slide 11: Business case

**Action title:** Payday buys funded accounts for about VND 1.3 million each, not fee income

**On-slide text:**
- The Board risks VND 6.6 billion before the month-6 gate.
- Fixed cost decides the case: build and running cost move month-60 cash by VND 17.5 billion.
- Levers: waive the bank fee, run a lean team, negotiate fund and bond margins.
- Not counted: month-36 balances equal 18% of DNSE's investor cash.

**Table:**

<!-- table: slide11_scenarios -->
|  | Downside | Base | Upside |
|---|---|---|---|
| Cash need, Phase 0–1, with 15% contingency | VND 8.7 billion | VND 6.6 billion | VND 4.8 billion |
| New accounts above VND 10 million, month 36 | 2,911 | 14,871 | 51,445 |
| NPV over 60 months at 12% | −VND 35.1 billion | −VND 25.0 billion | +VND 11.0 billion |
| Payback month | None | None | 44 |
| Net cost per new funded account, month 60 | VND 10.02 million | VND 1.29 million | 0 |
<!-- /table -->

CSV: `outputs/round3/tables/slide11_scenarios.csv` (sinh bằng `src/round3/deck_tables.py` từ `data/round3/deck_tables/` và output của mô hình; sửa CSV mẫu, không sửa bảng ở đây).
Source: authors' cohort model (assumptions in Appendix H).

**Figure:** `outputs/round3/figures/payday_jcurve.png` và `outputs/round3/figures/payday_tornado.png` (hai hình nửa slide).
Caption: Left, cumulative cash over 60 months in three scenarios. Right, month-60 cash when one group of inputs moves to its downside or upside value.
Source: authors' cohort model.

**Designer notes (tiếng Việt):**
- Hàng trên: J-curve (trái) và tornado (phải), mỗi hình nửa slide. Hàng dưới: bảng 5 dòng; 4 ý chữ đặt dọc bên phải bảng hoặc chuyển 1–2 ý vào speaker notes nếu chật.
- Cột "Base" in đậm. Không tô xanh lá cho số dương: dùng màu xám cho downside/upside, RED cho base, như trong hình.
- Ghi chú nhỏ dưới tornado: "Enrolling more savers lowers the cost per funded account (VND 0.68 million at upside enrolment)".

**Speaker notes:**
Now the CFO's question. We modelled monthly cohorts over sixty months with sourced costs. In the base case Payday does not pay back within five years: cumulative cash reaches minus 32 billion dong at month 60, an NPV of minus 25 billion. It is better read as buying funded accounts at about 1.3 million dong each, and that is the yardstick we ask the Board to accept. The tornado shows fixed cost is the swing factor, far more than yields or enrolment, so a lean team and reused components matter most. Waiving the bank fee is the cheapest lever. The upside pays back in month 44. Either way, the Board's exposure before the first stop decision is 6.6 billion dong.

**Sources:** authors' cohort model; ITviec (2025); VPBank (2024); SSI Asset Management (2026); VCBF (2026); DNSE Securities (2026c).

---

## Slide 12: Go-to-market, year 1

**Action title:** Year one: build, test with 45,000 accounts, then scale inside DNSE's base

**On-slide text:**
- Year-one spend (base): VND 9.2 billion, released gate by gate; the Board approves VND 6.6 billion now.
- Outreach and marketing: VND 1.2 billion of the total.
- No sign-up cash, no "free money" influencers, at most three messages per account.

**Table:**

<!-- table: slide12_gtm -->
| Quarter | Who and where | Message | Gate | End of quarter, base: funded savers; balances; spend |
|---|---|---|---|---|
| Q1: build | DNSE staff, internal beta | – | Gate 0: partner terms; 99.5% shadow runs; SSC notice | 0; 0; VND 2.1 bn |
| Q2: pilot | 45,000 dormant accounts in 3 arms; Zalo, SMS, push, Ensa | "Your account is ready. Let payday do the investing." | Gate 1: enrolment ≥1.5%, stop below 1.0% | 162; VND 1.1 bn; VND 3.6 bn |
| Q3: roll out | Dormant accounts; in-app for traders; plan step at account opening | "Keep a core that grows while you trade." | Monthly: acquisition cost per funded saver ≤VND 128,000 | 1,620; VND 10.5 bn; VND 1.7 bn |
| Q4: first employers | 3 to 5 employers through HR sessions | "An employee benefit that invests your salary." | Gate 2: funded ≥3,962; balances ≥VND 24.1 billion | 4,953; VND 30.1 bn; VND 1.8 bn |
<!-- /table -->

CSV: `outputs/round3/tables/slide12_gtm.csv` (sinh bằng `src/round3/deck_tables.py` từ `data/round3/deck_tables/` và output của mô hình; sửa CSV mẫu, không sửa bảng ở đây).
Source: authors' design; numbers from the authors' cohort model.

**Figure:** `outputs/round3/figures/gtm_timeline.png`.
Caption: Year-one activities by month with Gates 0 to 2 (top) and funded savers by month (bottom), base case. Red marks the months the Board approves now; arrows mark channels that continue into year two.
Source: authors' cohort model.
Data: `outputs/round3/tables/gtm_year1.csv`, `payday_monthly_base.csv`.

**Designer notes (tiếng Việt):**
- Timeline trên cùng, bảng 4 dòng ở dưới.
- Ba thông điệp để nguyên tiếng Anh trong ngoặc kép, in nghiêng.
- Ô "Gate" màu RED nhạt để nối với slide 14.

**Speaker notes:**
Year one has four steps. In quarter one we build, sign partners and run the plan with staff money; nothing launches before Gate zero. In quarter two a randomised pilot reaches 45,000 dormant accounts in three arms, with at most three messages each and no sign-up reward. If enrolment clears 1.5 per cent, quarter three rolls out to the remaining eligible dormant accounts, adds an in-app offer for active traders and a plan step at account opening. In quarter four we test the first three to five employers through HR sessions with a licensed adviser. By month twelve the base case has 9,414 savers enrolled, 4,953 funded and 30 billion dong in plans, for 9.2 billion dong of spending.

**Sources:** authors' cohort model; Zalo Business Solutions (n.d.); MobiFone (n.d.).

---

## Slide 13: Strategic roadmap

**Action title:** Five gated phases move DNSE from trading-first to balance-first

**On-slide text:**
- Shared rails serve the whole app: virtual accounts, scheduler, suitability engine, transparency dashboard.
- Ecosystem: fix the base (months 0–6), keep money in (6–12), grow on balances (12–24).
- Not in the base case: ETF-secured lending, reviewed only at Gate 3.

**Table:**

<!-- table: slide13_roadmap -->
| Phase | Months | Objective | Key initiatives | Gate and result (base) |
|---|---|---|---|---|
| 0. Build and comply | 1–3 | A safe, legal MVP | Virtual accounts (fee target VND 0); fund contracts; adviser-signed plans; SSC notice | Gate 0; −VND 2.1 billion cumulative |
| 1. Pilot | 4–6 | Measure enrolment, persistence, new money | Randomised pilot, 45,000 accounts, 3 arms | Gate 1; 600 savers |
| 2. Scale in the base | 7–12 | Controlled scale | Dormant roll-out; in-app; account opening; first employers | Gate 2; 4,953 funded |
| 3. Outside channels | 13–24 | Channels that create a default | Employers; salary percentage via Open API from March 2027; step-up with pay rises | Gate 3; 7,714 new accounts above VND 10 million |
| 4. Optimise | 25–36 | Better economics, a managed option | Partner or DNSE-owned fund manager; Golden Egg with more bank partners | Quarterly review; 14,871 new accounts above VND 10 million |
<!-- /table -->

CSV: `outputs/round3/tables/slide13_roadmap.csv` (sinh bằng `src/round3/deck_tables.py` từ `data/round3/deck_tables/` và output của mô hình; sửa CSV mẫu, không sửa bảng ở đây).
Source: authors' design; numbers from the authors' cohort model; DNSE Securities (2026f); State Bank of Vietnam (2024).

**Figure:** `outputs/round3/figures/roadmap.png`.
Caption: Payday's five gated phases with base-case results (top), above DNSE's balance-first product roadmap (bottom).
Source: authors' design; authors' cohort model.
Data: `outputs/round3/tables/roadmap_phases.csv`, `ecosystem_roadmap.csv`.

**Designer notes (tiếng Việt):**
- Hình roadmap chiếm nửa trên; bảng 5 dòng nửa dưới (có thể bỏ cột "Months" nếu hình đã thể hiện).
- Dòng "Not in the base case" màu xám, nhỏ hơn.

**Speaker notes:**
Beyond year one, the roadmap has five gated phases. Phases zero to two build, test and scale inside DNSE's base. Phase three, from month thirteen, adds channels that create a default: employers, and salary-percentage contributions through bank open APIs once banks comply in March 2027. Phase four looks at a fully managed version through a partner or DNSE-owned fund manager, and wider Golden Egg supply through DNSE's planned bank partnerships. Payday also anchors DNSE's shift from trading-first to balance-first: the virtual accounts, scheduler, suitability engine and transparency dashboard serve deposits, margin and Golden Egg as well. ETF-secured lending is not in our numbers; it would be reviewed only at Gate three.

**Sources:** authors' cohort model; State Bank of Vietnam (2024); DNSE Securities (2026f).

---

## Slide 14: Validation and KPIs

**Action title:** Each phase has a number that scales, adjusts or stops the plan

**On-slide text:**
- Pilot: 45,000 dormant accounts in three arms of 15,000: control, Payday, Payday with the persistence package.
- Enough to detect a 10-point gain in six-month persistence.
- North Star: new accounts above VND 10 million. Leading signs: funded savers, new money, on-time rate.

**Table:**

<!-- table: slide14_gates -->
| Gate (month) | Measure | Scale if | Stop if | Owner |
|---|---|---|---|---|
| 0 (3) | Shadow payday runs credited on time | ≥99.5% | Below 99.5%: delay the pilot | CTO |
| 0 (3) | Bank fee per contribution | VND 0 target, ≤3,300 | Above VND 6,200 | CFO |
| 1 (6) | Enrolment of treated dormant accounts | ≥1.5% | Below 1.0% | Head of Product |
| 1 (6) | Projected net cost per new funded account | ≤VND 1.6 million | Above VND 2.6 million | CFO |
| 2 (12) | Funded savers | ≥3,962 | Below 2,476 for two quarters | Head of Product |
| 3 (24) | New accounts above VND 10 million; employer participation | ≥6,171; ≥39% | Below 1,140; below 20% | CEO |
<!-- /table -->

CSV: `outputs/round3/tables/slide14_gates.csv` (sinh bằng `src/round3/deck_tables.py` từ `data/round3/deck_tables/` và output của mô hình; sửa CSV mẫu, không sửa bảng ở đây).
Source: authors' cohort model; thresholds derived from unit economics.

**Figure:** `outputs/round3/figures/decision_tree.png`.
Caption: Scale, adjust and stop branches at Gates 0 to 3, with thresholds from the cohort model.
Source: authors' cohort model.
Data: `outputs/round3/tables/decision_tree.csv`.

**Designer notes (tiếng Việt):**
- Cây quyết định nằm ngang chiếm nửa trên: mỗi cổng là một nút có ba nhánh (xanh xám = scale, PEACH = adjust, RED = stop).
- Bảng 6 dòng ở dưới. Đây là slide của tiêu chí 30 điểm: phải đọc được ở cỡ slide.

**Speaker notes:**
How will the Board know whether to continue? Every phase ends with numbers that scale, adjust or stop the plan. Gate zero, at month three, checks partner terms, a 99.5 per cent on-time rate in shadow paydays and written compliance. Gate one, at month six, reads the pilot. We scale if at least 1.5 per cent of treated accounts enrol and stop below one per cent. We also stop if fewer than 60 per cent make three contributions, or if the projected cost per new funded account exceeds 2.6 million dong. The pilot has three arms of 15,000 accounts, enough to detect a ten-point gain in persistence. Gates two and three test funded savers, new funded accounts and the employer channel.

**Sources:** authors' cohort model.

---

## Slide 15: Risks and Board ask

**Action title:** Approve VND 6.6 billion and five decisions; we report back at month 6

**On-slide text:**
- Highest risks: a payday failure (20 of 25), low enrolment (16), and a regulator objection to Golden Egg's role (15).
- Each risk has an owner and an early-warning trigger (Appendix B).

**Table:**

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

CSV: `outputs/round3/tables/slide15_board_ask.csv` (sinh bằng `src/round3/deck_tables.py` từ `data/round3/deck_tables/` và output của mô hình; sửa CSV mẫu, không sửa bảng ở đây).
Source: authors' cohort model.

**Figure:** `outputs/round3/figures/risk_heatmap.png`.
Caption: Six risks by likelihood and impact on a 1 to 5 scale, with owners; cell colours follow the score bands of the risk register.
Source: authors' assessment.
Data: `outputs/round3/tables/risk_register.csv`.

**Designer notes (tiếng Việt):**
- Trái: heat map 5×5 (ô càng đỏ càng nặng), mỗi rủi ro là một nhãn R1–R6. Phải: khung "Board ask" viền RED.
- Đây là slide cuối, kết bằng câu hỏi xin duyệt. Không thêm "Thank you" trên cùng slide.

**Speaker notes:**
Three risks matter most. A payday failure scores highest, and the 4 March outage shows it can happen, so shadow runs, a separate scheduler and a release freeze come before launch. Low enrolment comes second, which is why we stop below one per cent. Third, the regulator may object to Golden Egg's role or to the advice flow. New Golden Egg openings were paused at the regulator's request in December 2023, so we notify the SSC early and keep bond funds as a fallback core. Our ask is specific: 6.6 billion dong for months one to six, and five decisions, starting with a virtual-account bank that waives the collection fee. We will come back at month six with measured numbers.

**Sources:** authors' assessment; DNSE Securities (2023, 2026e); Market Times (2026).

---

## Appendix và references

Appendix A–I (nội dung đầy đủ, có bảng sinh từ CSV) và danh mục references APA 7 nằm ở **`docs/doc_round3/deck_appendix.md`**.

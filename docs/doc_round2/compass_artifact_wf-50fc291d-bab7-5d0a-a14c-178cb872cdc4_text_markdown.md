# FBA Season 6 – Round 2: Lựa chọn công ty & Kế hoạch phân tích dữ liệu

> Tài liệu chiến lược nội bộ cho team (lưu dưới dạng `.md`). Viết bằng tiếng Việt, giữ nguyên thuật ngữ tiếng Anh về finance/data vì báo cáo chung kết phải viết bằng tiếng Anh. Ngày lập: **21/09/2026**. Deadline nộp: **21:00 ngày 27/09/2026** (còn ~6 ngày).
> **Quy ước:** ✅ = fact có nguồn + ngày; 🔎 = assumption/hypothesis cần validate.

---

## TL;DR (3 gạch đầu dòng trả lời câu hỏi cốt lõi)
- **Chọn VPBank (HOSE: VPB) làm tổ chức phân tích chính**, khai thác hai "fintech arm" đang có vấn đề rõ ràng và giàu dữ liệu: **FE Credit** (consumer finance) và **Cake by VPBank** (digital bank); **backup là VNDirect (HOSE: VND)**.
- **Vì sao VPBank thắng:** vừa là ngân hàng niêm yết HOSE nên **data dồi dào, pull được qua API** (vnstock nguồn VCI, SSI FastConnect), vừa có **vấn đề fintech thật, có bằng chứng định lượng** — FE Credit lãi trước thuế nửa đầu 2026 chỉ **152,6 tỷ đồng, giảm ~43% so với 267 tỷ cùng kỳ**, chi phí dự phòng ăn gần hết lợi nhuận trước dự phòng (✅ BCTC hợp nhất VPBank, dẫn qua CafeBiz 21/07/2026) — cho nhiều insight và business solution để khai thác.
- **Angle đề xuất (khớp objectives đề bài):** dùng dữ liệu để **đề xuất target segment** cho hệ sinh thái tài chính tiêu dùng số của VPBank (nổi bật: **household business/micro-SME** sau cải cách bỏ thuế khoán 1/1/2026; và **Gen Z/mass affluent** để nâng ARPU của Cake) đồng thời **ưu tiên bài toán chất lượng tín dụng tiêu dùng số** — vừa ra market recommendation, vừa ra problem prioritization.

---

## Key Findings (những phát hiện quyết định)

1. **VPBank có "problem clarity" đúng chuẩn đề bài mà vẫn thừa dữ liệu.** FE Credit — quân bài consumer-finance của VPBank — sau giai đoạn tái cấu trúc vẫn chịu áp lực nợ xấu: lãi trước thuế nửa đầu 2026 chỉ **152,6 tỷ đồng (giảm ~43% YoY từ 267 tỷ)**, mới đạt ~13% kế hoạch năm (mục tiêu 1.179 tỷ, +93%), **chi phí dự phòng ~6.158 tỷ đồng ~ bằng 98% lợi nhuận trước dự phòng** ✅ (BCTC hợp nhất VPBank, dẫn qua CafeBiz 21/07/2026). Đây là "distinct problem" để đào sâu.

2. **Cake by VPBank là câu chuyện tăng trưởng có bài toán ARPU/segment.** Cake đạt **hơn 7,6 triệu khách hàng**, tổng giá trị giao dịch ~**320.000 tỷ đồng**, **ARPU 25 USD (~645.000đ) năm 2025, đặt mục tiêu 44 USD năm 2026** ✅ (VnExpress, 10/09, nhân giải Euromoney Awards for Excellence 2026; DNSE/Thời báo Ngân hàng). Bài toán: nâng ARPU gấp gần đôi → phải chọn đúng segment để bán chéo sản phẩm.

3. **Dữ liệu cho VPBank cực dồi dào và pull được qua API** ✅: BCTC quý/năm qua `vnstock` (nguồn VCI) và SSI FastConnect Data; giá & disclosures HOSE; app reviews Google Play cực nhiều (VPBank NEO ~185K reviews, Cake ~62,7K, FE ONLINE ~13,9K — truy cập 21/09/2026).

4. **Bối cảnh macro 2025–2026 rất "giàu context" để tăng điểm rubric business-context** ✅: GDP Q1/2026 +7,83% YoY, H1/2026 +8,18% (NSO); tín dụng H1/2026 +7,4% so cuối 2025, mục tiêu ~15% cả năm (SBV, họp báo 2/7/2026); lạm phát mục tiêu ~4,5% (SBV). Cùng loạt "cú hích" chính sách: **bỏ thuế khoán hộ kinh doanh từ 1/1/2026**, **sandbox fintech Decree 94/2025 (hiệu lực 1/7/2025)**, **biometric Decision 2345 + Circular 17/18 làm ~86 triệu tài khoản bị đóng**.

5. **VNDirect là backup mạnh nhưng "vấn đề đã qua đỉnh".** Sau cyberattack 24/03/2024, thị phần môi giới HOSE rớt từ **hạng 3 (7,01% cuối 2023) xuống 5,1% Q4/2024** ✅ (HOSE, dẫn qua VietnamBiz 07/01/2025) — nhưng công ty đang hồi phục mạnh (**net income Q2/2026 +140% YoY**, Simply Wall St), làm giảm tính "đang có vấn đề" theo tiêu chí user.

---

## Details (phân tích chi tiết)

### A. Bối cảnh cuộc thi và tiêu chí lựa chọn
Round 2 yêu cầu team đóng vai **business analyst của một FinTech**, lấy **dataset làm "primary foundation"**, làm **macro-environment + competitive landscape** để tìm **market gap**, rồi **recommend một target market** cho senior management ngân hàng. Rubric nặng nhất ở: **Data preparation & quality (10), Analytical findings & accuracy (15), Problem/opportunity prioritization (15)**. Suy ra công ty được chọn phải đồng thời: (a) có **raw data phong phú để clean & transform** (ăn điểm data-prep); (b) có **vấn đề fintech rõ, có số liệu**; (c) cho phép **ra khuyến nghị target-segment**.

Hai tiêu chí user: (1) đang có vấn đề fintech để khai thác insight & business solution; (2) data dồi dào, pull được qua API công ty chứng khoán/nguồn uy tín → **ưu tiên công ty niêm yết** HOSE/HNX/UPCoM.

### B. Landscape scan các ứng viên (2025–2026)

**Nhóm 1 — Ngân hàng niêm yết có fintech arm gặp vấn đề**
- **VPBank (VPB)** ✅ — Cả tập đoàn lãi kỷ lục **30.600 tỷ đồng PBT năm 2025 (+53%)**, tổng tài sản **1,26 triệu tỷ** (VnEconomy/VPBank, tháng 1/2026) — tức "nhà mẹ" khỏe, nhưng **fintech arm có vấn đề rõ**: FE Credit lãi H1/2026 chỉ 152,6 tỷ (-43% YoY), dự phòng ăn ~98% lợi nhuận trước dự phòng. Cake tăng trưởng nhưng bài toán ARPU. GPBank nhận chuyển giao bắt buộc (tái cấu trúc). **Data dồi dào nhất.**
- **HDBank (HDB)** ✅ — DongA Bank đổi tên thành **Vikki Digital Bank (QĐ 42/QĐ-TTGSNH2 ngày 14/02/2025)**; tổng tài sản Vikki ~**87.258 tỷ đồng (2025)**, hơn **2,1 triệu lượt tải app năm đầu** (mô hình "zero fee"). Bài toán: biến ngân hàng 0 đồng thành digital bank có lãi.
- **MB (MBB)** — MBV (ex-OceanBank), Mcredit; PBT 2025 ước ~33.700 tỷ (+17%). Ít "problem".
- **Vietcombank** — VCBNeo (ex-CBBank).

**Nhóm 2 — Tổ chức tài chính/fintech niêm yết**
- **VNG (VNZ, UPCoM)** ✅ — **ZaloPay/Zion**: doanh thu mảng Fintech **1.111 tỷ đồng năm 2025 (từ 754 tỷ năm 2024)**, lỗ trước thuế thu hẹp từ 580 xuống 489 tỷ; Zion **lỗ thuế lũy kế hơn 4.016 tỷ (ước tổng lỗ lũy kế ~4.600 tỷ)**, 16 triệu người dùng (BCTC hợp nhất VNG 2025, dẫn qua VietnamBiz). **Vấn đề fintech rõ nhất nhưng data mỏng hơn bank** (UPCoM, mảng fintech không tách bạch hoàn toàn, phụ thuộc thuyết minh).
- **VietCredit (TIN, UPCoM)** ✅ — Lỗ ~156 tỷ 2024 → hồi phục lãi sau thuế 9T/2025 (654,1 tỷ) nhưng **NPL tăng từ 6,3% lên 7,1% (30/9/2025), tổng nợ xấu +86,6%**; **bị NHNN xử phạt 702 triệu đồng cho 8 hành vi vi phạm (QĐ xử phạt 09/10/2025), thu hồi nợ xấu nội bảng 2024–7T/2025 chỉ đạt 3% kế hoạch** ✅ (Kết luận Thanh tra NHNN, dẫn qua Vietnamnet/Dân Trí). Case fintech-lending "juicy" nhất + differentiation cao, **nhưng quy mô nhỏ, rủi ro thiếu raw data cho rubric data-prep**.
- **EVNFinance (EVF)**, **F88** (bổ sung nếu cần benchmark).

**Nhóm 3 — Wealthtech/Securities**
- **VNDirect (VND)** ✅ — Cyberattack 24/03/2024; thị phần môi giới HOSE **7,01% (cuối 2023) → 5,1% (Q4/2024)**, cả năm 2024 hạng 6 (5,87%); đang tái cấu trúc chiến lược "VNDNEXT", **kế hoạch PBT 2026 là 3.018 tỷ (+20%)**, Q2/2026 net income +140% YoY. **Data cực mạnh** (là chính công ty chứng khoán). **Backup.**
- SSI, TCBS, DNSE, VPBankS.

**Nhóm 4 — Fintech chưa niêm yết (chỉ dùng làm benchmark/competitive landscape)**
- MoMo (~31 triệu user; ~68% market share e-wallet theo Decision Lab *The Connected Consumer 2023* 🔎 số cũ, cần cập nhật), ZaloPay, VNPay, Viettel Money, ShopeePay; Timo (bị Kredivo Group mua 5/2026), TNEX (3,9 triệu user 6/2025), Liobank.

### C. Scoring matrix (thang 1–5, có trọng số)

| Tiêu chí | Trọng số | VPBank | VNDirect | VNG | VietCredit | HDBank/Vikki |
|---|---|---|---|---|---|---|
| BK1 Research capability | 10% | 5 | 5 | 4 | 3 | 4 |
| BK2 Data accessibility (API, nguồn) | 20% | 5 | 5 | 3 | 3 | 4 |
| BK3 Problem clarity (fintech problem rõ) | 20% | 5 | 4 | 5 | 5 | 4 |
| BK4 Development potential (Round 3) | 10% | 5 | 4 | 4 | 4 | 5 |
| User1 Fintech-problem intensity | 15% | 5 | 4 | 5 | 5 | 4 |
| User2 Data abundance via API | 15% | 5 | 5 | 3 | 3 | 4 |
| Fit rubric (raw data + target-segment) | 5% | 5 | 4 | 3 | 3 | 4 |
| Differentiation (ít team chọn) | 5% | 3 | 4 | 4 | 5 | 4 |
| **Tổng có trọng số** | 100% | **4,85** | **4,45** | **3,95** | **3,80** | **4,10** |

*Giải thích trọng số:* BK2 và User2 (data) được nâng lên tổng 35% vì rubric data-prep + yêu cầu "primary foundation" của user; problem clarity + intensity tổng 35% vì đây là điều kiện tiên quyết. Differentiation chỉ 5% vì đề bài nói rõ "công ty phù hợp không nhất thiết là lớn nhất/nổi tiếng nhất", nhưng vẫn nên tránh trùng lặp.

**Kết luận:** **VPBank thắng (4,85)** nhờ cân bằng tốt nhất giữa data abundance và problem clarity. VNDirect (4,45) là backup vì data cực mạnh nhưng vấn đề (cyberattack) đã qua đỉnh và đang hồi phục mạnh → giảm tính "đang có vấn đề". VietCredit (3,80) có problem rõ nhất + differentiation cao nhưng **rủi ro không đủ raw data cho rubric data-prep** — chỉ dùng nếu team muốn góc táo bạo và chấp nhận bù bằng thuyết minh BCTC + kết luận thanh tra.

### D. Khuyến nghị chính thức & framing câu hỏi

**Tổ chức: VPBank (HOSE: VPB).**

**Câu hỏi kinh doanh chính:** *"VPBank nên ưu tiên target segment nào cho hệ sinh thái tài chính tiêu dùng số (Cake + FE Credit) trong 2026 để vừa phục hồi chất lượng tài sản, vừa nắm cơ hội từ cải cách thuế hộ kinh doanh và làn sóng cashless?"*

Các framing thay thế:
1. **Credit-quality lens:** FE Credit dịch chuyển từ mở rộng thị phần sang thu hồi nợ + số hóa **credit scoring** (tận dụng sandbox Decree 94/2025) như thế nào?
2. **Digital-bank growth lens:** Cake nên tập trung segment nào (Gen Z, gig workers, rural under-banked) để nâng ARPU **25 → 44 USD**?
3. **Deposit/CASA lens:** sau khi ~86 triệu tài khoản bị đóng vì biometric, cơ hội cho digital bank hút CASA từ nhóm khách hàng còn hoạt động (113 triệu tài khoản cá nhân, 711.000 tài khoản tổ chức còn lại — SBV, họp báo 2/6/2025).

Angle vừa cho **target-segment recommendation** vừa cho **problem prioritization** → khớp đúng "Objectives" của đề bài (FinTech evaluating target markets, recommend most promising target market to bank's senior management).

### E. Kế hoạch Dataset (dataset là "primary foundation")

**Dataset 1 — Financial-statement panel (bank + peers)** ✅
- **Nội dung/fields:** BCTC quý & năm của VPB và peers (ACB, MBB, HDB, TCB, VIB, TPB, STB, OCB…), 2019–Q2/2026: total assets, gross loans, customer deposits, NII, PBT, provision expense, NPL, CASA, NIM, CIR.
- **Nguồn/API:**
  - `vnstock` (Python; license source-available, miễn phí cho học tập/nghiên cứu). ⚠️ **Lưu ý version:** class `Vnstock` legacy sẽ **EOL 31/08/2026**, **nguồn TCBS đã bị gỡ khỏi thư viện**, `.ratio()` từng lỗi do thay đổi API TCBS → **dùng nguồn VCI**. Ví dụ: `Finance(symbol='VPB', source='VCI').balance_sheet(period='quarter')`, `.income_statement()`, `.cash_flow()`. Cảnh báo: nguồn VCI **chặn IP Google Cloud** (Colab hay lỗi) → chạy local hoặc export thủ công dự phòng.
  - **SSI FastConnect Data API** (`https://fc-data.ssi.com.vn/api/v2/...`; đăng ký tại chi nhánh SSI/qua môi giới lấy ConsumerID + Secret + PrivateKey; có sample Python trên GitHub `SSI-Securities-Corporation`). Endpoints: `Market/DailyOhlc`, `Market/DailyStockPrice`, `Market/Securities`.
  - Web dự phòng: Vietstock, CafeF, Wichart, HOSE/HNX disclosures, IR VPBank (báo cáo thường niên).
- **Data-quality issues:** restatement giữa các quý; đơn vị (triệu vs tỷ VND); ticker/tên đổi (DongA→Vikki, OceanBank→MBV, CB→VCBNeo); **NPL/CASA/NIM/loan-loss coverage thường KHÔNG có sẵn qua API** → phải lấy từ thuyết minh BCTC hoặc report công ty chứng khoán; consolidated vs parent-only; one-off items (thu hồi nợ đã xóa — VPBank thu 5.700 tỷ hợp nhất cả năm 2025).
- **Treatment:** chuẩn hóa đơn vị về tỷ VND; map ticker theo thời gian; đánh dấu one-off; lập **cleaning log traceable** (rubric data-prep yêu cầu).

**Dataset 2 — Consolidated vs parent-only** ✅ — So BCTC hợp nhất và riêng lẻ VPBank để **isolate performance FE Credit** và các subsidiary (VPBankS, OPES). Đây là "decomposition" ăn điểm findings.

**Dataset 3 — Customer-behaviour (app reviews)** ✅ (số liệu truy cập Google Play **21/09/2026**)

| App | Package ID | Sao | Số review | Tải |
|---|---|---|---|---|
| Cake by VPBank | `xyz.be.cake` | 4,7 | ~62,7K | 5M+ |
| VPBank NEO | `com.vnpay.vpbankonline` | 4,2 | ~185K | 10M+ |
| FE ONLINE 2.0 | `com.fecredit.feonline` | 4,2 | ~13,9K | 1M+ |
| Vikki (HDBank) | `com.finx.vikki` | 4,8 | ~7,8K | 1M+ |
| VietCredit | `vn.vietcredit` | 3,5 | ~4,1K | 500K+ |
| MoMo (benchmark) | `com.mservice.momotransfer` | 4,1 | ~698K | 10M+ |
| VNDIRECT DGO (backup) | `vn.com.vndirect.stocks` | 4,4 | ~8,9K | 500K+ |

- **App Store IDs** (dùng cho iOS scraper): Cake `id1551907051`, VPBank NEO `id1209349510`, MoMo `id918751511`, Vikki `id6471952024`. ⚠️ Rating/review count iOS khó đọc trực tiếp — pull bằng scraper.
- **Tool:** `google-play-scraper` (JoMingyu) — **v1.2.7 (6/2024), còn hoạt động 2026 nhưng KHÔNG còn cập nhật tích cực**, bị throttle khi paginate app lớn (MoMo, VPBank NEO); functions: `app()`, `reviews()` (có `continuation_token`, `sort`, `filter_score_with`, `count`, `lang='vi'`, `country='vn'`), `reviews_all()`. iOS: dùng **`python-app-store-scraper`** (fork còn maintain) hoặc `app-store-web-scraper`; `app-store-scraper` gốc đã deprecated.
- ⚠️ **Bẫy cần tránh:** app `mtnft.momo.consumer` là MoMo của MTN (châu Phi) — **KHÔNG phải** MoMo Việt Nam. Phân biệt VNDIRECT DGO vs DStock (DStock chỉ ~758 review, quá ít để phân tích riêng).
- **Data-quality issues:** spam/duplicate reviews, teencode, diacritics (dấu tiếng Việt), review bombing, developer replies lẫn trong review; **negativity/self-selection bias** (chỉ người rất hài lòng hoặc rất bực mới viết) → không đại diện toàn khách hàng; "ratings count" (số lượt chấm sao) ≠ "reviews count" (số review có chữ) có thể paginate.

**Dataset 4 — Macro & industry** ✅
- **SBV** payment/credit stats; **NAPAS/VietQR** (QR payment Q1/2025 +81,64% YoY về khối lượng; H1/2026 tín dụng +7,4%).
- **NSO** (`nso.gov.vn`) — GDP (Q1/2026 +7,83%; H1/2026 +8,18%), retail sales, dữ liệu tỉnh. ⚠️ **Mapping 63→34 tỉnh từ 7/2025** nếu dùng dữ liệu cấp tỉnh — cần bảng ánh xạ.
- **World Bank** — WDI + **Global Findex 2025** (microdata catalog Vietnam #7998; ~79% người lớn toàn cầu có account, ~67% có digital payment; Vietnam ~86,97% người ≥15 tuổi có tài khoản).
- **IMF** Financial Access Survey.
- **Google–Temasek–Bain** e-Conomy SEA; **Decision Lab** (Bank Satisfaction Rankings 2026: Vietcombank 86,8; Techcombank 85,9; Timo lọt top 10), Q&Me, Visa.

### F. Menu phân tích ánh xạ rubric

1. **Peer benchmarking + trend/anomaly** *(Analytical findings 15)* — So NPL, NIM, CIR, CASA, credit cost VPB vs peers 2019–Q2/2026. Method: time-series + z-score anomaly. Chart: line + small multiples. *Chứng minh:* xu hướng, vị thế tương đối. *Không chứng minh:* nhân quả.
2. **Consolidated vs parent decomposition** *(Findings 15)* — Isolate đóng góp FE Credit/subsidiary. Method: bóc tách hợp nhất − riêng lẻ. Chart: waterfall/stacked bar.
3. **Credit-cost & NPL analysis** *(Findings + Insights)* — `credit cost = provision expense / average gross loans`; `NPL ratio = (nhóm 3+4+5)/tổng dư nợ`; `loan-loss coverage = loan loss reserves/NPL`. Chart: dual-axis.
4. **Customer-review sentiment & complaint-topic** *(Business insights 10)* — Sentiment scoring (mô hình tiếng Việt như PhoBERT/underthesea) + topic modeling (LDA) trên review Cake/FE ONLINE/VPBank NEO; so với MoMo/VietCredit. Chart: sentiment distribution + word cloud + topic-over-time. ⚠️ **Caveat rõ:** negativity/self-selection bias, không đại diện.
5. **Market segmentation & target-segment sizing** *(Problem prioritization 15)* — Segment: **Gen Z, mass affluent, household business/micro-SME, rural/under-banked, gig workers**, và theo vùng (dùng NSO + Findex). Method: **attractiveness (size × growth × margin) vs ability-to-win (fit sản phẩm, chi phí, quyền dữ liệu)** → matrix 2×2. Sizing TAM/SAM/SOM (ví dụ >5,2 triệu hộ kinh doanh, ngân sách thuế nhóm này ~26.000 tỷ 2024).
6. **PESTEL backed by data** *(Business context 10)* — Political/Legal: Decree 94/2025 sandbox (credit scoring/Open API/P2P), Decision 2345 + Circular 17/18 biometric, cải cách thuế hộ KD 2026, Decree 13/2023 personal data. Economic: GDP/tín dụng/lãi suất. Social: Findex, Gen Z. Tech: NAPAS/VietQR, eKYC. Mỗi yếu tố **gắn 1 số liệu**.
7. **Competitive landscape** — Map banks vs e-wallets vs digital banks (Cake/Timo/TNEX/Liobank/Vikki) theo user & satisfaction (Decision Lab) → **xác định market gap**.
8. **Problem-prioritization matrix** *(15)* — Tiêu chí: **scale, urgency, strategic relevance, feasibility, evidence strength** (chấm 1–5, có trọng số). So 3–4 vấn đề để chọn 1.
9. **Strategic alternatives (3–4, distinct)** *(10)* — (a) **Household-business digital finance** (thanh toán + e-invoice financing + vốn lưu động sau cải cách thuế); (b) **Gen Z/mass-market deposit & wealth** trên Cake để nâng ARPU; (c) **Credit-scoring/risk overhaul FE Credit** qua sandbox Decree 94; (d) **CASA capture hậu biometric**. Đánh giá theo tiêu chí nhất quán + trade-off.
10. **Preliminary recommendation + validation plan** *(10+10)* — Chọn 1 hướng, giải thích value logic. KPI: **CAC, ARPU, activation rate, NPL/credit cost, CASA ratio, retention**. Test: pilot trong **SBV sandbox (Decree 94/2025)**, A/B test onboarding, survey khách hàng target, phân tích cohort.

**Visualization đề xuất (10–15, đều label rõ + nguồn + ngày):** (1) line NPL các bank; (2) NIM trend VPB vs peers; (3) waterfall FE Credit PBT & dự phòng; (4) stacked CASA; (5) heatmap financial ratios; (6) sentiment distribution theo app; (7) word cloud complaint topics tiếng Việt; (8) segment attractiveness × ability-to-win matrix; (9) TAM/SAM/SOM household business; (10) QR payment growth bar (SBV/NAPAS); (11) Global Findex financial-inclusion Vietnam; (12) competitive positioning map (user × satisfaction); (13) problem-priority scatter (impact × feasibility); (14) KPI dashboard mockup; (15) timeline chính sách 2024–2026.

### G. Rủi ro & Differentiation
- **Data gaps:** NPL/CASA cấp subsidiary không public đầy đủ → dùng proxy + đánh dấu 🔎 assumption; phân biệt rõ fact vs hypothesis (rubric evidence-transparency 5).
- **Legal/ethical:** tôn trọng ToS scraping của Google Play/App Store; tuân thủ **Decree 13/2023 & Luật Bảo vệ dữ liệu cá nhân** → chỉ dùng review công khai, **ẩn danh, không lưu PII**, dùng cho mục đích học thuật.
- **Over-used angle:** nhiều team sẽ chọn MoMo/Techcombank hoặc "VPBank generic". **Differentiation của team:** tập trung mảng **FE Credit consumer-finance quality** kết hợp **household-business/micro-SME segment sau cải cách thuế 1/1/2026** — góc gắn chính sách rất mới, ít team khai thác, và trực tiếp trả lời "target market".

### H. Report outline (≤ 3.500 từ, không tính Exec Summary/TOC/Appendices/References)
| Mục (theo đề bài) | Từ | Nội dung chính |
|---|---|---|
| Introduction | 300 | Bối cảnh VPBank + câu hỏi kinh doanh |
| Findings of observations | 700 | Peer benchmarking, decomposition, sentiment |
| Discussion/Main analysis | 1.200 | PESTEL, competitive landscape, segmentation, problem-prioritization |
| Recommendations (Strategic alternatives + Preliminary rec) | 700 | 3–4 alternatives + 1 hướng chọn + value logic |
| Validation Direction | 250 | assumptions, KPIs, tests |
| Conclusion | 150 | tóm tắt |
| *(Business context lồng vào Introduction + Discussion)* | 200 | — |
- **Appendices/Google Drive:** cleaning log traceable, notebook Python (vnstock + scraper), bảng số liệu đầy đủ, chart phụ, bảng mapping ticker & 63→34 tỉnh, dashboard (Power BI/Looker).

### I. Code skeleton (kiểm chứng với docs/GitHub — chạy local)
```python
# 1) Financial panel qua vnstock (dùng nguồn VCI; TCBS đã bị gỡ; Vnstock legacy EOL 31/08/2026)
# pip install -U vnstock
from vnstock import Finance
fin = Finance(symbol='VPB', source='VCI')
bs = fin.balance_sheet(period='quarter')     # bảng cân đối
is_ = fin.income_statement(period='quarter')  # KQKD
# Lặp qua peers: ['VPB','ACB','MBB','HDB','TCB','VIB','TPB','STB']

# 2) App reviews Google Play (JoMingyu google-play-scraper v1.2.7)
# pip install google-play-scraper
from google_play_scraper import reviews, Sort
rv, token = reviews('xyz.be.cake', lang='vi', country='vn',
                    sort=Sort.NEWEST, count=200)   # paginate bằng token
# App khác: 'com.vnpay.vpbankonline','com.fecredit.feonline','vn.vietcredit'

# 3) iOS (dùng fork còn maintain: python-app-store-scraper)
# pip install python-app-store-scraper
from app_store_scraper import AppStore
cake_ios = AppStore(country='vn', app_name='cake', app_id=1551907051)
cake_ios.review(how_many=500)   # đọc .reviews
```
⚠️ Kiểm chứng: tên hàm `Finance/balance_sheet/income_statement` và `reviews/Sort/AppStore/.review()` khớp docs vnstock GitHub, JoMingyu google-play-scraper README, và fork app-store-scraper (truy cập 21/09/2026). Nếu vnstock VCI lỗi trên Colab (chặn IP Google Cloud) → chạy local hoặc export CSV từ Vietstock/CafeF.

### J. Kế hoạch 6 ngày (21–27/09/2026) — team nhỏ
| Ngày | Việc chính | Checkpoint cuối ngày |
|---|---|---|
| **21/9 (CN)** | Chốt VPBank + câu hỏi, phân vai (Data lead / Analysis lead / Writer / Viz) | Confirm scope + risk backup VNDirect |
| **22/9 (T2)** | Pull financial panel (vnstock/SSI) + app reviews + macro (SBV/NSO/Findex) | Có raw data thô đủ 3 dataset |
| **23/9 (T3)** | Clean data + **cleaning log**; peer benchmarking; decomposition FE Credit | Bảng ratio sạch + 4 chart đầu |
| **24/9 (T4)** | Segmentation + attractiveness matrix; sentiment/topic modeling | Chọn top-3 segment + top-3 problem |
| **25/9 (T5)** | Problem-prioritization matrix; strategic alternatives; preliminary rec + validation | Khung đầy đủ argument + KPI |
| **26/9 (T6)** | Viết report (≤3.500 từ) + hoàn thiện 12–15 viz; review chéo; dựng Drive | Bản draft hoàn chỉnh + appendices |
| **27/9 (T7)** | Finalize, proofread tiếng Anh, kiểm reference, export PDF | **Nộp trước 20:30** (dư ≥30 phút) |

---

## Recommendations (bước tiếp theo, cụ thể)
1. **Ngay 21/9: khóa lựa chọn VPBank** và câu hỏi "target segment cho Cake + FE Credit 2026". Chỉ định 1 người dựng ngay skeleton `vnstock` + `google-play-scraper` để test API chạy được trước khi cam kết (nếu vnstock VCI lỗi kéo dài → chuyển pull từ Vietstock/CafeF thủ công, KHÔNG đổi công ty).
2. **22–23/9: ưu tiên dựng financial panel + cleaning log trước** — vì đây là hai rubric nặng nhất (findings 15 + data-prep 10). Đảm bảo NPL/NIM/CASA/credit cost tính đúng công thức và nhất quán denominator.
3. **24–25/9: dồn lực vào segmentation + problem-prioritization** (tổng 30 điểm rubric). Chọn hướng **household-business digital finance** làm recommendation chính (differentiation cao, gắn cải cách thuế 2026, trả lời trực tiếp "target market") — hoặc **Cake ARPU/Gen Z** nếu dữ liệu app review đủ mạnh.
4. **Luôn tách ✅ fact vs 🔎 assumption** trong report (ăn điểm evidence-transparency) và **date mọi con số**.

**Ngưỡng đổi quyết định (khi nào chuyển sang backup VNDirect):** nếu đến hết **22/9** không pull được ≥2/3 dataset cho VPBank (financial panel + app reviews) qua bất kỳ nguồn nào, hoặc thấy FE Credit/Cake không đủ số liệu tách bạch → **chuyển sang VNDirect** (data tự thân dồi dào, câu chuyện cyberattack → phục hồi + upgrade thị trường vẫn đủ làm target-market cho segment nhà đầu tư cá nhân/Gen Z).

## Caveats (giới hạn & điểm cần validate)
- 🔎 **Số liệu FE Credit H1/2026 (152,6 tỷ, -43%)** lấy từ báo chí dẫn BCTC hợp nhất VPBank (CafeBiz 21/07/2026); cần đối chiếu trực tiếp BCTC hợp nhất Q2/2026 trên IR VPBank/HOSE để chốt con số chính xác trước khi đưa vào report.
- 🔎 **Market share e-wallet (MoMo ~68%)** là số Decision Lab *The Connected Consumer 2023* — **đã cũ**, phải cập nhật bản 2025/2026 hoặc ghi rõ năm khi trích.
- 🔎 **NPL/CASA/NIM cấp subsidiary** (FE Credit riêng) không phải lúc nào cũng public → khả năng phải dùng proxy; đánh dấu rõ.
- ⚠️ **Công cụ scraping** (`google-play-scraper`, `app-store-scraper`) không còn được maintain tích cực (bản mới nhất 2024) và có thể bị throttle/đổi endpoint → test sớm, có phương án backup (Apify actor trả phí ~0,10 USD/1.000 review, hoặc export thủ công mẫu nhỏ).
- ⚠️ **vnstock:** class `Vnstock` legacy EOL 31/08/2026, nguồn TCBS đã gỡ, `.ratio()` có thể lỗi → dùng nguồn VCI + chạy local (VCI chặn IP Colab/Google Cloud).
- ⚠️ **Mapping 63→34 tỉnh (từ 7/2025)** bắt buộc nếu dùng dữ liệu cấp tỉnh, nếu không sẽ sai khi so sánh chuỗi thời gian.
- 🔎 Các con số dự báo macro (GDP 2026, tín dụng ~15%) là **forecast/target**, không phải thực tế đã xảy ra — trình bày đúng là dự báo.

## Reference list (nguồn uy tín, có link)
- SBV – Ngân hàng Nhà nước: `https://www.sbv.gov.vn` (payment/credit stats, họp báo H1/2026)
- NSO – Tổng cục Thống kê: `https://www.nso.gov.vn/en/` (GDP Q1 & H1/2026)
- World Bank – Global Findex 2025 (Vietnam microdata): `https://microdata.worldbank.org/index.php/catalog/7998`; download: `https://www.worldbank.org/en/publication/globalfindex/download-data`
- IMF – Financial Access Survey: `https://data.imf.org`
- HOSE: `https://www.hsx.vn` | HNX: `https://www.hnx.vn`
- VPBank IR (thông cáo lợi nhuận 2025): `https://www.vpbank.com.vn/tin-tuc`
- Vietstock (FE Credit, Vikki): `https://vietstock.vn`
- VnEconomy (VPBank 30.600 tỷ 2025): `https://vneconomy.vn/vpbank-loi-nhuan-30600-ty-dong-nam-2025-tang-truong-53.htm`
- VietnamBiz (VNG/ZaloPay 2025; VNDirect thị phần): `https://vietnambiz.vn`
- Vietnamnet / Dân Trí (Thanh tra NHNN xử phạt VietCredit): `https://vietnamnet.vn/thanh-tra-nhnn-chi-ro-hang-loat-vi-pham-tai-vietcredit-phat-702-trieu-dong-2471098.html`
- Decree 94/2025 (fintech sandbox) – Tilleke & Gibbins: `https://www.tilleke.com/insights/vietnam-issues-fintech-sandbox-decree/20/`
- Cải cách thuế hộ kinh doanh 2026 – Vietnam News: `https://vietnamnews.vn/economy/business-beat/1728186`
- Biometric ~86 triệu tài khoản – SBV/Forbes/Tiền Phong (họp báo Ngày không tiền mặt 2/6/2025)
- vnstock GitHub: `https://github.com/thinh-vu/vnstock`
- SSI FastConnect Data docs: `https://guide.ssi.com.vn/ssi-products`
- google-play-scraper (JoMingyu): `https://github.com/JoMingyu/google-play-scraper`
- Decision Lab (Bank Satisfaction 2026): `https://www.decisionlab.co`
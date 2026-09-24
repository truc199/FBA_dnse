# Ghi chú phân tích: DNSE — Data pack & Báo cáo FBA Season 6 Round 2

*Lập ngày 22/09/2026. Nguồn: `FBA_Round2_DNSE_data_pack.xlsx` (14 sheet) và `FBAR2_2026_DNSE_Analysis.docx` (~9.500 từ, 11 hình, 11 bảng).*

---

# PHẦN 1 — FILE EXCEL: `FBA_Round2_DNSE_data_pack.xlsx`

## 1.1 Tổng quan

| Hạng mục | Nội dung |
|---|---|
| Quy mô | 14 sheet, khoảng 550 dòng dữ liệu |
| Ngày biên soạn | 20–21/09/2026 (ghi trong sheet `Read me`) |
| Cấu trúc | 5 bộ dữ liệu: (1) tài chính & vị thế DNSE, (2) mặt cắt ngành chứng khoán VN, (3) 868 review Google Play của DNSE + 2 đối thủ, (4) toàn bộ Global Findex Vietnam, (5) sheet tham chiếu vĩ mô |
| Đặc điểm kỹ thuật | **Live formulas** — mọi ô tính toán là công thức thật (đã verify: `Segment model!B24 = AVERAGE('Segments 2024'!D29,...)`, `Industry cross-section!C5 = B5/$B$14*100`). Sửa input là toàn bộ downstream tự cập nhật |
| Quy ước màu | Xanh dương = input từ nguồn; Xanh lá = link sheet khác; Đen = công thức; Nền vàng = giả định có thể đổi |

## 1.2 Nội dung chi tiết từng sheet

### (1) `Read me` — 33 dòng metadata
Không có số liệu. Ghi: nguồn gốc dữ liệu, quy ước màu, quy tắc làm sạch review, các sóng khảo sát Findex, cảnh báo về độ chính xác, giấy phép CC BY 4.0, và **bảng giải mã segment code Findex** (đuôi `.1`–`.12` = nữ / nam / 15-24 / 25+ / tiểu học trở xuống / THCS trở lên / 40% nghèo nhất / 60% giàu nhất / nông thôn / thành thị / ngoài lực lượng lao động / trong lực lượng lao động).

### (2) `DNSE financials` — báo cáo tài chính DNSE
**Trường dữ liệu:** `Line | FY2025 | Q1 2026 | Q2 2026 | H1 2026 | H1 as % of FY2025 | Note`

| Chỉ tiêu (tỷ VND) | FY2025 | Q1 2026 | Q2 2026 | H1 2026 |
|---|---|---|---|---|
| Doanh thu hoạt động | 1.467,0 | 395,0 | 453,1 | 848,2 |
| Lãi từ cho vay & phải thu | 555,8 | 147,5 | 188,6 | 336,1 |
| Phí môi giới | 404,0 | 119,5 | 102,5 | 222,0 |
| Thu nhập đầu tư (FVTPL + HTM) | 171,4 | 98,4 | 95,0 | 193,4 |
| LNTT | 340,2 | 14,2 | 98,9 | 113,1 |
| LNST | 272,5 | 11,3 | 83,0 | 94,3 |
| Dư nợ margin & ứng trước (cuối kỳ) | 5.832 | 5.910 | **6.303** (kỷ lục) | 6.303 |

Khối **ratio tính sẵn:** biên LNTT (23,19% → 3,59% → 21,83% → **13,33%**); cơ cấu doanh thu (lãi vay 39,6% / môi giới 26,2% / đầu tư 22,8% trong H1 2026).

Khối **khách hàng & kế hoạch:** 1,5tr TK cuối 2025 → 1,65tr Q1/2026 → 1,7tr H1/2026; thị phần TK mở mới 20% (2025), 18% (Q1/2026, tương đương 142.000 TK); mục tiêu ĐHCĐ 2026: DT 1.736 tỷ, LNTT 550 tỷ; vốn điều lệ 4.286 tỷ; tài sản KH ~52.000 tỷ.

Khối **derived measures (quan trọng nhất):**
- Doanh thu/tài khoản H1 2026 = **498,9 nghìn VND**
- Doanh thu môi giới/tài khoản = **130,6 nghìn VND**
- Tài sản KH/tài khoản = **34,7 triệu VND**
- Lợi suất cho vay quy năm = **11,01%**
- Hoàn thành KH 2026: **48,9% doanh thu, 20,6% lợi nhuận** → H2 phải tạo 436,9 tỷ LNTT = **3,86 lần H1**

### (3) `Market share` — thị phần môi giới Q2/2026
**Trường:** `Firm | HOSE Q2 2026 | HOSE Q1 2026 | HOSE change (pts) | HNX Q2 2026 | Derivatives Q2 2026 | Note` — 13 công ty + 2 dòng tổng.

Đáng chú ý: VPS 12,61% HOSE (giảm 2,71 điểm/quý), SSI 11,17%, TCBS 9,36%, VPBankS tăng mạnh nhất +0,63 điểm. **DNSE nằm ngoài top 10 HOSE, hạng 8 HNX (2,88%), hạng 2 phái sinh (25,38%)**. Top 10 HOSE thu hẹp 69,05% → 65,19%.

Bảng phụ: **chuỗi thị phần phái sinh DNSE theo quý** — Q1/24: 4,01% → Q1/25: 16,7% → Q2/25: 17,33% → Q3/25: 23,67% → Q4/25: 24,26% → Q1/26: 25,5% → Q2/26: 25,38%.

### (4) `Industry cross-section` — mặt cắt ngành Q2/2026
**Trường:** `Firm | Lending balance | Share of industry % | Q2 2026 pre-tax profit | HOSE brokerage share | Note`

TCBS 51.500 tỷ dư nợ (11,35%), SSI 40.500, VPBankS 38.200 (LNTT 2.159 tỷ, gấp ~4 lần cùng kỳ), VPS 31.300, HSC 29.000, **DNSE chỉ 6.303 tỷ = 1,39%**. Tổng dư nợ ngành 453.800 tỷ (đã gồm ứng trước tiền bán; báo chí ước margin thuần ~445.000 tỷ). Quý trước 424.100 tỷ → tăng trưởng 7,0%.

### (5) `DNSE position` — **sheet lõi của luận điểm báo cáo**
**Trường:** `Measure | DNSE | Market total | Unit | DNSE share % | Source` — 5 thước đo với 5 mẫu số khác nhau.

| Thước đo | DNSE | Tổng thị trường | Thị phần |
|---|---|---|---|
| Tài khoản khách hàng | 1.700.000 | 13.852.633 | **12,27%** |
| Môi giới phái sinh | — | — | **25,38%** |
| Cổ phiếu niêm yết HNX | — | — | **2,88%** |
| Cổ phiếu niêm yết HOSE | — | — | **< 2,94%** (ngoài top 10) |
| Dư nợ cho vay | 6.303 tỷ | 453.800 tỷ | **1,39%** |
| LNTT Q2/2026 | 98,9 tỷ | 9.977 tỷ | 0,99% |

**"Monetisation gap"** (3 tỷ số then chốt): thị phần giao dịch HNX ÷ thị phần TK = **0,235**; thị phần cho vay ÷ thị phần TK = **0,113**; thị phần phái sinh ÷ thị phần TK = **2,068**.

### (6) `Review analysis` — dữ liệu sơ cấp, 4 khối
**Khối Method:** ghi đầy đủ quy trình — retrieval (Google Play pagination token), normalisation (NFKC → bỏ dấu → lowercase, xử lý ký tự Unicode toán học mà spam dùng để né filter), 3 regex rule (loan spam / referral spam / duplicate), định nghĩa "generic flag", theme tagging không loại trừ, và known limitation.

**Khối Cleaning log:** `Stage | DNSE | VPS SmartOne | FPTS EzTrade`
- Thu thập: 868 / 1.200 / 177
- Loại bỏ: quảng cáo vay 127, referral farming 72, trùng lặp 36 → **DNSE loại 27,1%**, VPS 7,0%, FPTS 4,5%
- Giữ lại: 633 / 1.116 / 169
- Điểm TB sau làm sạch: 3,161 / 2,515 / 2,154 (spam bị loại có điểm TB 3,626 — **cao hơn** review thật, nên làm sạch kéo điểm DNSE **xuống**)

**Khối ratings theo năm:** `Year | Retrieved | Removed | Removed % | Retained | Mean retained | Generic`. Spam đỉnh điểm 2022 (48,8%) và 2023 (55,8%). Bảng "substantive" (bỏ review 1 từ): 2024 = 4,066 sao (nhưng 30,9% là review 1 từ) → **2025 = 2,364 sao, rơi 1,70 sao trên mẫu lớn hơn**.

**Khối complaint themes:** 11 chủ đề × `1-2 sao | 3 sao | 4-5 sao | tổng | % của nhóm tiêu cực | định nghĩa`:
stability 70 (25,8%), onboarding 53 (19,6%), fraud 44 (16,2%), promo 26 (9,6%), money 14 (5,2%), closure 8 (3,0%), influencer 5 (1,8%), fees 4 (1,5%), ui 3 (1,1%), zalopay 2 (0,7%), yield 0. Phân bố: 271 tiêu cực / 31 trung tính / 331 tích cực.

**Khối 3-app comparison:** DNSE 3,161 (1 sao 39,8%) > VPS 2,515 (53,3%) > FPTS 2,154 (59,2%).

### (7) `Review quotes` — 50 review gốc tiếng Việt
**Trường:** `Review id | Stars | Date | Helpful votes | Themes | Text (cắt 150 ký tự)`. Chọn theo số lượt hữu ích cao nhất trong mỗi theme. Đây là phần **evidence định tính mạnh nhất** — ví dụ các review nhiều upvote nhất: "MN CHÚ Ý SCAM NHA KHÔNG NHẬN ĐƯỢC 100K" (58 votes), "lừa đảo... phải nạp tiền vào tối thiểu 2tr mới được" (50), "Bị gài rồi... k thể hủy đăng ký" (54), "đóng tài khoản mất phí 100k" (17), và phía tích cực: "tk không ngủ", "tiền không ngủ và sinh lời tự động quá linh hoạt".

### (8) `Segment model` — mô hình phân khúc tự xây
Assumption cell: **80,6 triệu người lớn 15+** (GSO 2024 áp lên dân số 102 triệu).
- **Index A "investable surplus"** = trung bình không trọng số 6 chỉ số: fin17a, fin17dm, fin8, fin17e, fin17f, fin24bd
- **Index B "digital habit"** = trung bình 6 chỉ số: dig.acc, con26d, con9a, fin25e3w, fin9b, fin32.acc
- **Activation gap** = % có tài khoản − % gửi tiết kiệm tại TCTD
- **Priority score** = Composite × Unconverted (triệu người) / 100

Kết quả xếp hạng: **In labour force 9,31 (1) > Richest 60% 9,05 (2) ≈ Secondary+ 9,04 (3) > Aged 25+ 8,37 (4)**. Nhóm 15–24 có spread B−A rộng nhất (**35,1 điểm**) và activation gap lớn nhất (33,6 điểm) nhưng priority score chỉ 2,25.

### (9) `Segments 2024` — bảng nền Findex
51 chỉ số × 13 cột (All adults + 12 segment). Trường: `Indicator id | Indicator | Theme | All adults | Women | Men | Young | Older | Primary- | Secondary+ | Poorest 40% | Richest 60% | Rural | Urban | Out of LF | In LF`. Theme gồm Access, Digital payments, Saving, Credit, Insurance, Income, Resilience, Connectivity.

### (10) `Segment gaps` — 51 chỉ số × 7 cột khoảng cách
`Income gap | Education gap | Urban−rural | Men−women | Young−older | In work−out of work` (điểm phần trăm). Khoảng cách lớn nhất: digitally enabled account theo học vấn **48,4 điểm**, theo thu nhập 41,9 điểm.

### (11) `National 2024` — 32 chỉ số chỉ công bố cấp quốc gia
Gồm lý do không có tài khoản, thẻ tín dụng (5,82%), vay từ TCTD chính thức (7,67%), lý do trả tiền mặt tại cửa hàng (17,88% do thói quen), thiên tai/khả năng chống chịu.

### (12) `Trends` — 26 chỉ số × 5 sóng (2011/2014/2017/2022/2024) + 2 cột thay đổi
Số quan trọng nhất cho báo cáo: **tiết kiệm tại TCTD 19,86% (2022) → 43,09% (2024)**, vay TCTD chính thức **21,72% (2017) → 7,67% (2024)**, tài khoản 56,27% → 70,55%, mobile money 16,47% → 38,72%.

### (13) `Vietnam reference` — 140 dòng tham chiếu vĩ mô
**Trường:** `Category | Indicator | Value | Period | Source`. 7 nhóm: Macro (20 dòng), Banking (~48), Payments (17), Business (14), Markets (~18), Insurance (8), Regulation (7). Mỗi dòng đều ghi kỳ và nguồn — đây là điểm mạnh về transparency.

### (14) `Sources` — 20 nguồn kèm link và ghi chú verification
Mỗi dòng có cột `Notes` ghi rõ **đã kiểm tra được gì trên browser ngày 20/09/2026**, kể cả các trang hóa ra "mỏng hơn dự kiến" (ví dụ MB: "English investor pages were partly unavailable").

---

## 1.3 Đánh giá độ tin cậy

### Điểm mạnh — xếp loại **khá cao đối với một data pack sinh viên**

1. **Có thể truy vết (traceable).** Mỗi dòng ở `Vietnam reference` và `Sources` đều có `Period` + `Source`. Endpoint Findex được ghi nguyên văn và có thể gọi lại để tái lập.
2. **Nguồn chủ yếu là sơ cấp / chính thống:** HOSE, HNX, VSDC, SBV, NSO, World Bank API, BCTC DNSE. Không dựa chủ yếu vào báo chí.
3. **Có một bộ dữ liệu sơ cấp thật.** 868 review tự thu thập, với quy tắc làm sạch viết ra đầy đủ và áp dụng **đồng nhất cho cả 3 app** → so sánh like-for-like hợp lệ.
4. **Nhất quán nội bộ — đã kiểm chứng bằng tính toán lại:** 127+72+36 = 235 = 868−633 ✓; tổng retrieved theo năm = 868 ✓; tổng 10 firm HOSE = 65,19 ✓ khớp công bố; mọi `% of negatives` khớp mẫu số 271 ✓; monetisation gap 2,88/12,272 = 0,2347 ✓; lợi suất cho vay 336,1/6.106,5×2 = 11,01% ✓; priority score = composite × unconverted/100 ✓.
5. **Tự khai báo hạn chế.** Sheet `Read me` chủ động nêu: mẫu Findex n=1.000 chia 12 chiều → ô nhỏ, "chênh vài điểm phần trăm là nhiễu"; review app store thiên lệch tiêu cực; VPS bị cap 1.200.
6. **Xử lý mâu thuẫn định nghĩa một cách minh bạch.** Vụ Findex 70,6% vs SBV >89% penetration được nêu thẳng, giải thích cơ chế (survey vs đếm tài khoản trên hệ thống, có trùng lặp), và khuyến nghị không trộn trong cùng biểu đồ. Đây là dấu hiệu của người làm dữ liệu nghiêm túc.
7. **Có audit trail.** Ghi nhận 12 số liệu đã bị sửa sau vòng verification (credit access ladder, biometric count, bank assets, brokerage tables).
8. **Mô hình dùng trung bình không trọng số có chủ đích** — để tránh fit trọng số theo kết quả sau khi đã nhìn dữ liệu. Lựa chọn phương pháp luận đúng.

### Điểm yếu và rủi ro cần biết trước khi trích dẫn

| # | Vấn đề | Mức độ |
|---|---|---|
| 1 | **Mâu thuẫn nội bộ về tổng LNTT ngành.** `DNSE position!C10` hard-code **9.977 tỷ** với ghi chú "Sum of the firms on the Industry cross-section sheet", nhưng tổng thực tế trên sheet đó là **8.418,9 tỷ** (D13 = SUM). Nếu dùng 8.418,9 thì thị phần LNTT của DNSE là 1,17% chứ không phải 0,99%. Chênh 1.558 tỷ có thể là HSC (bị bỏ trống) nhưng **không được giải thích**. | ⚠️ Cao — cần sửa hoặc ghi chú |
| 2 | **Hai bộ số doanh thu DNSE cùng tồn tại.** `DNSE financials` (từ BCTC): Q2 = 453,1 / H1 = 848,2. `Vietnam reference` (từ IR): Q2 = 455,2 (+55,9%) / H1 = 852,6 (+58,4%). Chênh ~4,4 tỷ, không có dòng đối chiếu. | ⚠️ Trung bình |
| 3 | **Chuỗi thị phần phái sinh có lỗ hổng 3 quý.** Nhảy từ Q1/2024 (4,01%) sang Q1/2025 (16,7%) — Q2–Q4/2024 không có. | Trung bình |
| 4 | **Mẫu số so sánh tài khoản không hoàn toàn like-for-like.** 1,7tr TK là con số DNSE tự công bố (gồm cả TK không hoạt động); 13,85tr là VSDC. Pack có nói "đếm tài khoản chứ không đếm người" nhưng **không nói về khác biệt tiêu chí active/inactive** — mà đây chính là mấu chốt của toàn bộ luận điểm "monetisation gap". | ⚠️ Cao — đây là giả định lớn nhất |
| 5 | **So sánh 3 app không cân bằng về mẫu.** DNSE có full history (868), VPS bị pagination cap 1.200 và **lệch về review gần đây**, FPTS chỉ 177 cả đời. Cột "Mean 2025 / Mean 2026" do đó so sánh các mẫu có cấu trúc thời gian khác nhau. | ⚠️ Trung bình–Cao |
| 6 | Tổng top-10 HOSE Q1/2026: cộng 10 firm = **69,00** nhưng công bố = **69,05**. Chênh 0,05 chưa giải thích (pack có ghi chú nhận biết). | Thấp |
| 7 | **Nguồn paywall / không kiểm chứng được:** phần lớn chỉ số ngân hàng đến từ FiinRatings/FiinGroup (báo cáo trả phí); dòng "Big four share of SME commitment" nguồn là "Press reporting" chung chung; các số Cake by VPBank được ghi rõ là **company-reported, unaudited**. | Trung bình |
| 8 | `Read me` viết "868 cleaned Google Play reviews" — thực tế 868 là số **thu thập** (chỉ riêng DNSE), số đã làm sạch là 633. Diễn đạt gây hiểu nhầm. | Thấp |
| 9 | **Mẫu Findex nhỏ.** n=1.000 cho cả nước; chia 12 chiều thì nhiều ô chỉ còn vài chục quan sát. Pack có cảnh báo, nhưng mô hình `Segment model` vẫn xếp hạng dựa trên chênh lệch 9,31 vs 9,05 vs 9,04 — **tức là xếp hạng trên mức nhiễu**. | ⚠️ Cao về mặt phương pháp |
| 10 | Segment population shares (73,5% trong LLLĐ, 26,5% ngoài, 60/40 thu nhập) là giả định áp từ Findex/GSO lên 80,6 triệu — nằm trong assumption cell nhưng ảnh hưởng trực tiếp tới cột "Unconverted, millions" và toàn bộ priority ranking. | Trung bình |

### Kết luận về độ tin cậy
Data pack **đủ tin cậy để làm bằng chứng cho một báo cáo thi**, và vượt chuẩn thông thường ở 3 điểm: nguồn sơ cấp, công thức sống, và tự khai báo hạn chế. Tuy nhiên trước khi nộp nên: **(a)** sửa hoặc chú thích ô 9.977; **(b)** thêm một dòng đối chiếu 848,2 vs 852,6; **(c)** nói rõ trong phần limitation rằng 1,7tr tài khoản DNSE và 13,85tr tài khoản VSDC có thể khác nhau về tiêu chí; **(d)** hạ giọng phần xếp hạng segment từ "hạng 1/2/3" xuống "3 nhóm này ngang nhau trong phạm vi sai số".

---

# PHẦN 2 — FILE DOCX: `FBAR2_2026_DNSE_Analysis.docx`

**Tiêu đề:** *Acquisition without activation — Why DNSE Securities holds a quarter of Vietnam's derivatives market, one eighth of its securities accounts and under three per cent of its cash equity trading*

**Cấu trúc:** 8 chương + Appendix A (6 bảng dữ liệu) + Appendix B (method / assumptions / limitations / accuracy checks) + References (17 nguồn). 11 hình, 11 bảng.

## 2.1 Luận điểm trung tâm

> DNSE đã xây được **cỗ máy thu hút khách hàng hoạt động tốt** và một **cỗ máy kiếm tiền không theo kịp**. Khoảng cách giữa hai cái đó chính là vấn đề kinh doanh.

Toàn bộ báo cáo được tổ chức quanh một nghịch lý số học duy nhất — cùng một công ty, đo bằng 5 thước đo khác nhau cho ra 5 vị thế hoàn toàn khác nhau:

| Thước đo | Vị thế DNSE |
|---|---|
| Tài khoản khách hàng | **12,27%** — nhóm đầu thị trường |
| Môi giới phái sinh | **25,38%** — hạng 2 toàn thị trường |
| Cổ phiếu HNX | **2,88%** — hạng 8/10 |
| Cổ phiếu HOSE | **<2,94%** — ngoài top 10 |
| Dư nợ cho vay | **1,39%** — gần như vắng mặt |

## 2.2 Các insight chính về tình hình fintech của DNSE

### Insight 1 — "Monetisation gap" đo được bằng tỷ số, không phải bằng cảm tính
Báo cáo chia thị phần hoạt động cho thị phần tài khoản để ra **cường độ tương đối của một tài khoản trung bình**:
- Giao dịch cổ phiếu HNX: **0,23** → một tài khoản DNSE giao dịch bằng ~23% giá trị của một tài khoản thị trường trung bình
- Cho vay: **0,11** → chỉ vay bằng 11%
- Phái sinh: **2,07** → gấp hơn 2 lần

Đây là đóng góp phân tích sắc nhất của báo cáo: nó **định vị chính xác điểm gãy trong customer journey** — không phải ở acquisition, không phải ở product, mà ở bước "funding the account".

### Insight 2 — Mô hình miễn phí tự chọn lọc ra khách hàng ít tiền nhất
Lập luận nhân quả: giao dịch miễn phí **theo cấu trúc** sẽ hấp dẫn nhất với người mà khoản tiết kiệm phí là lớn so với số tiền đầu tư — tức là người có số dư nhỏ nhất. Báo cáo không dừng ở suy luận mà **đối chiếu với dữ liệu review**: một tỷ lệ khách hàng đến qua quảng cáo YouTube và thưởng đăng ký chứ không qua quyết định đầu tư (theme `influencer` xuất hiện ở 1,8% review tiêu cực và ~2,7% review tích cực), và khiếu nại phổ biến nhất trong nhóm đó là **không nhận được tiền thưởng như quảng cáo**.

Phái sinh khuếch đại hiệu ứng này: hợp đồng tương lai VN30 có notional trung bình 43.925 tỷ/ngày so với 17.336 tỷ/ngày của cổ phiếu HOSE — **thị phần phái sinh cao hoàn toàn tương thích với một nền tài sản nhỏ**, vì notional gấp nhiều lần ký quỹ. Đó chính xác là những gì DNSE báo cáo.

### Insight 3 — Tăng trưởng đang được "mua", và giá đang tăng
- Doanh thu H1/2026 **+58,9% YoY**, nhưng biên LNTT **rơi từ 23,2% (FY2025) xuống 13,3%**, chạm đáy 3,6% ở Q1.
- Nguyên nhân Q1/2026: **chi phí hoạt động +120%**, chi phí môi giới +125%, **trích lập dự phòng danh mục tự doanh +405%**.
- Cơ cấu doanh thu H1/2026: lãi vay 39,6% + thu nhập đầu tư 22,8% = **62,4% doanh thu phụ thuộc vào quy mô bảng cân đối và hướng thị trường**, không phụ thuộc giao dịch của khách hàng. Môi giới chỉ 26,2% và chủ yếu là phái sinh.
- Kế hoạch 2026: mới đạt **48,9% doanh thu / 20,6% lợi nhuận** → H2 cần tạo 436,9 tỷ LNTT = **3,9 lần H1**. Đây là con số gây áp lực nhất trong toàn báo cáo.

### Insight 4 — Bằng chứng review định vị đúng điểm ma sát
Sau làm sạch, DNSE **3,161 sao > VPS 2,515 > FPTS 2,154** → sản phẩm không tệ so với đối thủ. Nhưng **xu hướng mới là vấn đề**: review có nội dung thực chất rơi từ **4,07 sao (2024) xuống 2,36 sao (2025)** trên mẫu lớn hơn.

Phân bố 271 review tiêu cực:
- **25,8% crash / lỗi đăng nhập** (stability)
- **19,6% mở tài khoản, eKYC, OTP, NFC** (onboarding)
- **16,2% cáo buộc lừa đảo** — và báo cáo truy ra **2 trigger cụ thể**: khuyến mãi quảng cáo 100.000đ nhưng yêu cầu nạp tối thiểu **2 triệu**, và **phí đóng tài khoản 100.000đ**
- 9,6% điều khoản khuyến mãi

Hai đọc hiểu phụ rất giá trị:
- Khiếu nại onboarding tập trung 2021, 2022, 2025; khiếu nại stability tập trung 2023, 2026 → **vấn đề tái phát chứ không phải đã được giải quyết**.
- Tính năng khách hàng **tự khen mà không cần được hỏi** là *"tài khoản không ngủ"* (sinh lời tự động trên tiền nhàn rỗi). Báo cáo dùng chính chi tiết này làm bằng chứng cho khuyến nghị: *tính năng đó đã làm ở quy mô nhỏ đúng thứ mà Chương 6 đề xuất làm một cách có chủ đích*.

### Insight 5 — Làm sạch dữ liệu **thay đổi kết luận**, không chỉ làm đẹp số
Năm 2022 và 2023 có **48,8% và 55,8% review là spam**. Đọc dữ liệu thô của 2 năm đó là đang đo spam chứ không đo khách hàng. Ngoài ra spam bị loại có điểm TB 3,626 — **cao hơn** review thật — nên làm sạch **kéo điểm DNSE xuống** (3,287 → 3,161). Báo cáo còn tách riêng "generic reviews" (≤4 từ, không theme) để **một năm đầy lời khen một từ không bị đọc thành sự hài lòng** — đúng là 2024 có điểm cao nhất (4,29) nhưng cũng có tỷ lệ review một từ cao nhất (30,9%).

### Insight 6 — Phân khúc mục tiêu được **tính ra**, không phải **giả định**
Hai chỉ số từ ma trận Findex:
- **Index A (investable surplus)** — 6 chỉ số về tiết kiệm chính thức
- **Index B (digital habit)** — 6 chỉ số về hành vi số
- **Activation gap** = % có tài khoản − % tiết kiệm tại TCTD (= người đã ở trong hệ thống chính thức nhưng chưa đưa tiền vào làm việc)

Ba phát hiện:
1. **Mọi phân khúc đều nằm dưới đường chéo** (B > A) → năng lực số đi trước tích lũy tài chính **ở khắp mọi nơi** trong dân số Việt Nam → **phân phối không phải là ràng buộc ở bất kỳ đâu**. Đây là phát hiện có sức nặng chiến lược nhất.
2. Xếp hạng propensity × unconverted pool: **người trong lực lượng lao động (17,5tr unconverted) hạng 1**, 60% thu nhập cao và nhóm THCS+ bám sát (chênh <0,2%). Phân khúc ưu tiên = **giao của ba nhóm: người đi làm, học vấn THCS trở lên, thuộc 60% thu nhập trên**.
3. **Phát hiện sắc nhất:** nhóm 15–24 có khoảng cách B−A rộng nhất (**35,1 điểm** vs 26,0 của nhóm kế tiếp) và activation gap lớn nhất (33,6 điểm). Tức là: *nhóm mà một app giao dịch miễn phí thu hút rẻ nhất lại chính là nhóm ít có khả năng nạp tiền nhất* → **cỗ máy acquisition của DNSE đang được tinh chỉnh cho phân khúc ít tiền nhất**.

### Insight 7 — Ba điều kiện thị trường làm cơ hội trở nên cấp thiết
1. **Hộ gia đình đang tích lũy chứ không đòn bẩy**: tiết kiệm tại TCTD 19,9% (2022) → **43,1% (2024)**; vay TCTD chính thức 21,7% (2017) → **7,7%**.
2. **Benchmark lãi suất nhìn thấy được**: tiền gửi kỳ hạn ~6% (bank lớn) đến ~9% (CD ngân hàng nhỏ), lạm phát 4,69% (6/2026), GDP H1/2026 +8,18%. Bất kỳ sản phẩm cash management nào cũng **phải vượt được con số khách hàng nhìn thấy ở quầy ngân hàng**.
3. **FTSE Russell nâng hạng hiệu lực 21/09/2026**, dòng vốn thụ động ước tính từ ~2,2 tỷ USD, **hướng vào cổ phiếu vốn hóa lớn/trung trên thị trường cơ sở — đúng nơi DNSE yếu nhất**. Và DSE không nằm trong rổ constituents.

### Insight 8 — Khuyến nghị và cơ chế truyền dẫn
**Xếp hạng vấn đề** theo 3 tiêu chí (quy mô tác động / nằm trong tầm kiểm soát / độ mạnh bằng chứng):
1. **Doanh thu trên mỗi tài khoản đã funded** — cao cả 3 tiêu chí
2. Tập trung vào phái sinh — tác động lớn nhưng **ngoài tầm kiểm soát** (phụ thuộc cấu trúc thị trường)
3. Biến động tự doanh — bằng chứng mới 1 quý

**4 phương án chiến lược:** (A) tiếp tục acquisition, (B) **cash management + phân phối quỹ**, (C) đào sâu phái sinh, (D) lên phân khúc tư vấn. Chọn B vì: A làm tăng chi phí mà không giải quyết conversion; C tăng tập trung rủi ro; D mâu thuẫn với mô hình không chi nhánh — **chỉ B vừa nâng doanh thu/tài khoản vừa củng cố dòng doanh thu lớn nhất**.

**Cơ chế truyền dẫn qua bảng cân đối (chuỗi 4 bước):** tiền mặt trên nền tảng sinh lợi → tài sản on-platform tăng → **tài sản đảm bảo cho margin tăng** → thu nhập lãi tăng **mà không cần khách hàng giao dịch nhiều hơn**. Phí phân phối quỹ bổ sung dòng thu định kỳ không phụ thuộc hướng thị trường.

**Định lượng phần thưởng:** lợi suất cho vay ~11%/năm → **tăng dư nợ 1.000 tỷ (+16%) ≈ +110 tỷ thu nhập lãi/năm = 20% mục tiêu LNTT 2026**. Báo cáo tự bác bỏ kịch bản cực đoan: đóng hoàn toàn khoảng cách 1,39% → 12,27% sẽ cần sổ ~55.000 tỷ, **vượt vốn của công ty, không thực tế**. Điểm là *ngay cả dịch chuyển nhỏ cũng có ý nghĩa vật chất*.

**Điều kiện khả thi:** ĐHCĐ 2026 đã duyệt **chương trình trái phiếu 3.500 tỷ** (2.500 không chuyển đổi + 1.000 chuyển đổi) → có nguồn vốn. **Điều kiện còn thiếu:** ĐHCĐ **không** duyệt pháp nhân quản lý quỹ → phân phối chứng chỉ quỹ cần **xin giấy phép hoặc hợp tác với một công ty quản lý quỹ sẵn có** — đây là quyết định đầu tiên Round 3 phải giải.

**Hai ràng buộc:** (1) **Giá** — sản phẩm cạnh tranh với tiền gửi 6–9% nhưng bảo vệ kém hơn, phải bù bằng thanh khoản / tích hợp giao dịch / thuế. (2) **Niềm tin** — 16,2% review tiêu cực cáo buộc lừa đảo liên quan điều khoản khuyến mãi và phí đóng TK. Hành động chi phí thấp: **bỏ phí đóng tài khoản 100.000đ và viết lại điều khoản khuyến mãi**.

### Insight 9 — Hướng kiểm chứng (Round 3)
4 test: (1) lấy **phân phối số dư tài khoản** từ nội bộ DNSE — báo cáo hiện chỉ *suy ra* số dư thấp từ tỷ số thị phần; (2) **conjoint / price ladder** đo willingness-to-pay so với tiền gửi; (3) **hồi quy dư nợ margin theo tài sản khách hàng** để đo hệ số truyền dẫn và test xem trần 200% có binding trước không; (4) đối chiếu theme review với **phân loại ticket hỗ trợ nội bộ**.

## 2.3 Chất lượng phương pháp của báo cáo

**Mạnh:**
- Appendix B khai báo 5 giả định, 4 hạn chế, và **B4 "Accuracy checks performed"** thừa nhận đã sửa 12 số liệu, trong đó 3 sửa lỗi trọng yếu — đáng chú ý nhất là **lỗi so sánh vị thế HNX của DNSE với vị thế HOSE của đối thủ**, lỗi này sẽ *thổi phồng* khoảng cách ở Mục 3.2. Việc thừa nhận công khai một lỗi có lợi cho luận điểm của chính mình là dấu hiệu liêm chính rõ rệt.
- Nguyên tắc **không so thị phần giữa các sàn khác nhau** được tuân thủ nhất quán; mọi con số đều mang tên sàn.
- Xử lý mâu thuẫn tổng dư nợ ngành (435.000 / 445.000 / 453.800 tỷ) bằng cách nêu cả ba, giải thích khác biệt định nghĩa, chọn một và tính cả hai kịch bản (1,39% vs 1,42%).
- Thừa nhận không tính được headroom so với trần 200% vì BCTC là bản scan không có text layer — **và không đưa bất kỳ tỷ số nào phụ thuộc vào nó**. Kỷ luật tốt.
- Thừa nhận Findex báo cáo **từng chiều một**, nên "giao của ba nhóm" là **suy ra từ 3 xếp hạng riêng biệt chứ không đo trực tiếp**.

**Yếu:**
- Xếp hạng priority 1/2/3 dựa trên 9,31 vs 9,05 vs 9,04 — chênh lệch **nằm dưới ngưỡng nhiễu** của mẫu n=1.000 chia 12 chiều. Báo cáo có nói "trong phạm vi 0,2%, nên coi là ngang nhau" nhưng vẫn giữ cột "Priority rank" trong Bảng 3 và A3.
- Luận điểm "số dư thấp" hoàn toàn là **suy luận gián tiếp** từ tỷ số thị phần. Báo cáo tự nhận điều này ở Mục 7 test 1 — nhưng đây vẫn là điểm dễ bị ban giám khảo tấn công nhất.
- Dùng số tài khoản DNSE (tự công bố) trên mẫu số VSDC mà không bàn về khác biệt tiêu chí active/inactive.

## 2.4 Đối chiếu DOCX ↔ EXCEL — các điểm cần sửa trước khi nộp

### A. Sai lệch cần sửa

| # | Vị trí | Vấn đề |
|---|---|---|
| 1 | Hình 6, chú thích | Viết *"DNSE leads on the full history and in 2026"*. **Excel bác bỏ vế sau**: mean 2026 là DNSE **3,057** vs **FPTS 3,261**. FPTS cao hơn. Nên sửa thành "dẫn đầu trên toàn lịch sử" và chú thích mẫu FPTS 2026 rất nhỏ. |
| 2 | Bảng A4, dòng Total | Ghi `Mean, substantive = 3.05`. Tính lại từ chính số liệu theo năm của Excel (523 review) ra **≈2,86**. Sai ~0,19 sao. |
| 3 | Mục 4.3 | Ghi FTSE *"covering 27 constituents"*; Excel `Vietnam reference` ghi **28** cổ phiếu trong đợt review. Chọn một và thống nhất. |
| 4 | Mục 3.4 & Exec summary | *(Kiểm chứng lại 23/09)* Docx dùng 848,2 tỷ, +58,9% — **khớp số báo chí công bố** (VnExpress, Mekong Asean). Dòng IR 852,6 tỷ / +58,4% trong sheet `Vietnam reference` mới là số lệch → **sửa Excel, không sửa docx**. |
| 5 | Bảng A1 | *(Kiểm chứng lại 23/09)* Báo chí công bố môi giới H1 = **222,1 tỷ**, khớp docx. Excel ra 222,0 do cộng hai quý đã làm tròn → **không cần sửa**. |
| 6 | Mục 4.3 vs Exec summary | §4.3 và §6 nói lãi tiền gửi **6–9%**; Exec summary nói *"priced against bank deposit rates near 7 per cent"*; Excel ghi VinaCapital: **~7%, một số bank >8%** (3/2026). Ba con số khác nhau cho cùng một benchmark. |

### B. Luận điểm trong DOCX **không có trong Excel** — cần bổ sung nguồn vào data pack hoặc footnote

- *"mở hơn 120.000 tài khoản Q1/2024 = 30% toàn thị trường"* (§3.1) — Excel chỉ có 20% (2025) và 18% (Q1/2026)
- *"tổng tài sản vượt 15.000 tỷ cuối 2025"* (§1.1)
- *Chi phí hoạt động +120%, chi phí môi giới +125%, dự phòng tự doanh +405%* (§3.4, Hình 7) — **đây là bằng chứng quan trọng của Insight 3 mà data pack không có dòng nào**
- *Notional VN30 futures 43.925 tỷ/ngày, HOSE cash 17.336 tỷ/ngày* (§4.1)
- *Dòng vốn thụ động FTSE ~2,2 tỷ USD* (§4.3)
- *Nghị quyết ĐHCĐ 2026: trái phiếu 2.500 + 1.000 tỷ, công ty CK tại IFC TP.HCM, góp 10 tỷ vào công ty tài sản số, sàn tín chỉ carbon, và **không** duyệt pháp nhân quản lý quỹ* (§6) — **đây là trụ cột khả thi của toàn bộ khuyến nghị**
- *Khiếu nại onboarding tập trung 2021/2022/2025, stability tập trung 2023/2026* (§3.3) — Excel không có bảng theme × năm
- *Ước tính thị phần phái sinh MBS ~4%, VNDirect ~4%, Mirae <2%* (Bảng A2) — Excel chỉ công bố VPS 33,84 / SSI 8,21 / DNSE 25,38

### C. Vấn đề chỉ tồn tại trong Excel (docx không dùng nên không ảnh hưởng)
Ô tổng LNTT ngành 9.977 tỷ vs tổng thực tế 8.418,9 tỷ (xem Phần 1.3, điểm 1). Docx chỉ viết *"well outside the top ten by earnings"* nên không bị vạ lây — nhưng nếu Round 3 cần trích thị phần lợi nhuận thì phải sửa ô này trước.

---

## Tóm tắt một dòng

**Excel** là một data pack đáng tin: nguồn sơ cấp, công thức sống, tự khai báo hạn chế — với 2 lỗi nội bộ cần sửa (ô 9.977 và hai bộ doanh thu) và 1 giả định lớn chưa được bàn đủ (tiêu chí tài khoản DNSE vs VSDC).

**Docx** là một báo cáo có luận điểm duy nhất, sắc, được chứng minh bằng 3 loại bằng chứng độc lập (tỷ số thị phần, review sơ cấp, mô hình Findex): *DNSE thu hút tốt nhưng không kiếm được tiền từ những gì đã thu hút, vì mô hình miễn phí tự chọn lọc ra khách hàng ít tiền nhất; giải pháp là chuyển số dư nhàn rỗi thành tài sản sinh lời trên nền tảng để mở rộng nền tài sản đảm bảo cho mảng cho vay.* Cần sửa 4 sai lệch số liệu (mục 2.4A, dòng 1–3 và 6) và bổ sung nguồn cho ~8 luận điểm hiện không có trong data pack.

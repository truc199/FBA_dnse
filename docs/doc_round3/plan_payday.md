# Kế hoạch xây dựng báo cáo chiến lược sản phẩm Payday Portfolio (Round 3A)

*Lập ngày 15/10/2026 (thứ Năm) cho team KTQT FTUers. Deadline nộp: **21:00 thứ Ba 20/10/2026**. File này trả lời ba câu hỏi: làm những gì, dùng data nào, đặt target ra sao. Nên đọc cùng `review_round2.md` (lỗi cần sửa), `review_payday.md` (phản biện sản phẩm) và `plan_tech.md` (chiến lược cho các sản phẩm hiện có).*

---

## 0. Mục tiêu, ràng buộc và cách chấm

| Hạng mục | Yêu cầu (booklet Round 3) | Ghi chú cho team |
|---|---|---|
| Sản phẩm nộp | Slide deck PDF 16:9, ≤10MB, **tối đa 15 slide** (không tính cover, giới thiệu thành viên, mục lục, appendix, references) | 15 phút thuyết trình cho 15 slide, tức khoảng 1 phút/slide. Rất chặt |
| Executive summary | **1 slide, ≤150 từ, cỡ chữ 14–15**; nêu business case, **vốn đầu tư cần** và **lợi nhuận kỳ vọng** | Viết cuối cùng, sau khi đã có số từ mô hình |
| Ngôn ngữ, trích dẫn | Tiếng Anh; thuật ngữ tiếng Việt phải kèm bản dịch; references nằm trên slide; **không dùng hyperlink ngoài**; mọi bằng chứng đặt trong appendix | Giữ APA 7 như Round 2. "Trứng Vàng (Golden Egg)", "Tài khoản Không Ngủ (Never-Sleeping Account)" |
| Tên file và nộp | `[FBAR3_2026]_KTQT FTUers`; nén file; nộp **một lần** bằng email trưởng nhóm đã dùng ở Round 1; không sửa được sau khi nộp | **Nộp trước 19:30 ngày 20/10** |
| Thuyết trình | 15 phút + Q&A với "Board": CEO, CFO, CTO, Head of Product | Mỗi slide phải trả lời được câu hỏi của ít nhất một vai trong Board |
| Rubric | Problem framing 25 · Solution design 20 · Demonstration 15 · **Implementation/validation/risk 30** · Presentation & Q&A 10 | Dồn công nhiều nhất cho tiêu chí 30 điểm và 25 điểm |
| Nội dung bắt buộc | 6 phần tối thiểu + roadmap theo phase (objective, initiative, KPI) + **go-to-market năm đầu** + business case | Xem outline ở §3 |

> Booklet ghi *"reference section… limited to a minimum of 5 slides"*. Rất có thể đây là lỗi khi chuyển PDF, ý gốc là "maximum". Nên hỏi lại ban tổ chức (liên hệ trong `agent.md`).

---

## 1. Thông điệp chủ đạo và đề nghị với Board

**Một câu (dùng trên slide):**
> *DNSE has won accounts; Payday Portfolio wins balances. It makes the salary the trigger, a goal the plan and trust something customers can check, starting with a 20,000-account pilot the Board can stop at month 6.*

**Ba trụ cột của câu chuyện:**
1. *Problem:* tài khoản không đi cùng tiền (1,8% TK có ≥10 triệu); tăng trưởng không thành lợi nhuận.
2. *Solution:* kế hoạch đầu tư nhiều lớp tài sản, gắn với lương, dựng từ thành phần DNSE đang có.
3. *Plan:* đầu tư theo giai đoạn, mỗi giai đoạn có cổng quyết định. Board chỉ duyệt trước Phase 0–1.

**Đề nghị với Board** (slide cuối): duyệt ngân sách Phase 0–1 (xây MVP và pilot), cộng 4 quyết định:
- chọn ngân hàng đối tác cấp VA;
- ký 1–2 công ty quản lý quỹ đối tác;
- nộp thông báo cho UBCKNN;
- duyệt quy trình để người hành nghề có chứng chỉ ký duyệt các danh mục mẫu.

---

## 2. Thay đổi so với Round 2 (yêu cầu tối thiểu #6, nên là 1 slide riêng)

| Hạng mục | Round 2 | Round 3 | Vì sao (bằng chứng) |
|---|---|---|---|
| Insight về khách | Trust là vấn đề đặc thù DNSE | Trust vẫn cao hơn đối thủ, nhưng **năm 2026 vấn đề nổi trội là reliability** (58,8% Play; 75% iOS) | Data review 2026 (`review_round2.md` L1) |
| Cạnh tranh | "CTCK chỉ phục vụ sau khi khách đã quyết định đầu tư"; "ngân hàng giữ lương nhưng ít lựa chọn đầu tư" | Năm 2026 cả CTCK lẫn ngân hàng đã vào cuộc đua tích lũy: SSI eSIP (23/04), VPS Smart Indexing (11/08), VPBank Hũ Mục Tiêu (12/09), VCB Digibank SIP từ 100.000đ. Chuyển tiền định kỳ đã thành chuẩn, nên khác biệt của Payday được định nghĩa lại | `competitor_features.md` |
| Tier | Thưởng lãi tiền nhàn rỗi; Committed 4,3% không điều kiện | Thưởng cho **tiền đã đầu tư**, có trần | Mâu thuẫn thiết kế, rủi ro bị khai thác (`review_round2.md` R3) |
| Danh mục mặc định | 3 danh mục, khách chọn | **Mặc định thiên trái phiếu**; cổ phiếu chỉ cho mục tiêu từ 3 năm | Lãi suất 2026; rủi ro trust bị bắn ngược |
| Kênh | TK ngủ | TK ngủ (pilot) → khách hoạt động (core–satellite) → **chủ lao động** (phase 3) | Opt-in và mặc định cho kết quả khác nhau (R1) |
| Mô hình | Tĩnh, 18 tháng | **Cohort theo tháng**, có chi phí, KPI theo giai đoạn | Ramp làm kết quả giảm 2–3 lần (R2) |
| Bằng chứng hành vi | Madrian & Shea cho mọi kênh | Chỉ dùng cho kênh payroll; kênh số dùng benchmark nội bộ | Opt-out khác opt-in |
| **Giữ nguyên** | Phân khúc mục tiêu, cơ chế lõi (VA tên khách, Ensa kèm xác nhận, rebalance bằng tiền mới), phạm vi pháp lý, trust controls, RCT | — | Vẫn đúng. Rubric khen việc giải thích vì sao giữ |

*Nếu ban tổ chức hoặc giám khảo có gửi feedback Round 2, thêm một cột "Feedback" vào bảng này.*

---

## 3. Outline 15 slide (gắn với rubric)

| # | Slide | Tiêu chí | Nội dung chính | Data/nguồn | Hình gợi ý |
|---|---|---|---|---|---|
| 1 | **Executive summary** | Tất cả | Vấn đề, giải pháp, vốn đầu tư, lợi nhuận, đề nghị (≤150 từ) | Mô hình §6 | 3 con số lớn + 4 câu |
| 2 | Problem recap: *accounts, not money* | Problem 25 | Thang 12,3% → 2,3% → 1,4% → 0,6%; 1,8% TK ≥10 triệu; LNTT lõi đi ngang; môi giới lỗ 16 quý | Table C1, B1 | Tái dùng Figure 4 + funnel nhỏ |
| 3 | Why now | Problem 25 | Lãi suất 2026; tiền NĐT −38%; Open API phải xong trước 01/03/2027; **cuộc đua tích lũy 2026** (SSI 23/04 → VSI 11/08 → VPBank 12/09; VCB Digibank SIP), DNSE chưa có; mới đạt 20% kế hoạch LNTT 2026 | Macro, `competitor_features.md` §1 | Timeline |
| 4 | **Insight → Design decision → Impact** | Problem 25 (trọng tâm) | 3 nguyên nhân gốc + cập nhật 2026, mỗi nguyên nhân dẫn tới một quyết định thiết kế và một KPI bị tác động | Report, data | Bảng 3 cột có mũi tên |
| 5 | What changed since Round 2 | Problem 25 | Bảng §2 rút gọn | — | Bảng |
| 6 | Target users & sizing | Solution 20 | 2–3 persona; funnel 1,51 triệu → 1,4 triệu TK ngủ → đủ điều kiện → tiếp cận được → ghi danh | `dnse_accounts.csv`, Findex, khảo sát đã công bố, trích review | Funnel + thẻ persona |
| 7 | The solution | Solution 20 | Value proposition cho khách và cho DNSE; cơ chế lõi; tính năng MVP; những gì **cố ý loại** (margin, cổ phiếu đơn lẻ) | — | Sơ đồ tổng quan |
| 8 | **Customer journey (wireframe)** | Demo 15 | 6 màn hình: mục tiêu → khẩu vị rủi ro → danh mục → lệnh định kỳ/VA → kỳ lương đầu → mốc 90 ngày/tier | Figma | Mockup điện thoại |
| 9 | **Service blueprint** | Demo 15 | Front/back/support: Ensa, người duyệt có chứng chỉ, ngân hàng VA, scheduler, order engine, đối tác quỹ/trái phiếu, đối soát, tuân thủ; điểm quyết định; xử lý lỗi | — | Blueprint |
| 10 | Competitive positioning | Solution 20 | Bảng 6 dòng (VSI, eSIP, TCBS, VCB Digibank SIP, VPBank Hũ Mục Tiêu, MoMo) + bản đồ 2×2 (phạm vi tài sản × vé tối thiểu) + câu định vị | `competitor_features.md` §2, §4 | Ma trận + 2×2 |
| 11 | **Business case** | Impl. 30 + Q&A | Unit economics, đường J lũy kế, vốn theo giai đoạn, điểm hòa vốn, độ nhạy, giá trị gián tiếp (tách riêng) | Mô hình §6 | J-curve + tornado |
| 12 | **Go-to-market năm 1** | Impl. 30 | Theo quý: phân khúc, kênh, thông điệp, ngân sách, KPI | §7 | Timeline 4 quý |
| 13 | **Strategic roadmap** | Impl. 30 | 4 phase: objective, initiative, KPI, cổng | §8 | Roadmap |
| 14 | **Validation & KPIs** | Impl. 30 | Test, ngưỡng continue/scale/adjust/stop, người chịu trách nhiệm, phụ thuộc | §5, §9 | Cây quyết định |
| 15 | Risks + Board ask | Impl. 30 + Q&A | 6 rủi ro (khả năng × tác động), giảm thiểu, đề nghị duyệt | §9 | Heat map |

**Appendix gợi ý** (không tính vào 15 slide):
- A. Data & methods
- B. Mô hình cohort, giả định, độ nhạy
- C. Bảng đối thủ đầy đủ có nguồn (`competitor_features.md` §2)
- D. Cập nhật review 2026
- E. Ánh xạ pháp lý (Table G1 cập nhật)
- F. Bằng chứng "feedback": khảo sát đã công bố + tiếng nói khách từ review (`competitor_features.md` §6)
- G. Wireframe đầy đủ
- H. Bảng giả định
- I. Slide dự phòng cho Q&A: VSI, CASA, trách nhiệm khi AI tư vấn, kịch bản thị trường giảm, phân tách cohort tài sản 2025

**Nếu quá giờ, cắt theo thứ tự:** gộp 2+3; đưa 9 xuống appendix (giữ blueprint mini trong slide 8); gộp 13+14.

---

## 4. Data: dùng gì, lấy ở đâu, giả định neo vào đâu

### 4.1 Có sẵn trong workspace

| Dữ liệu | Dùng cho | Ghi chú |
|---|---|---|
| `data/manual/dnse_accounts.csv` | Slide 2, 6 | 1.512.920 TK; 85.739 hoạt động; 27.100 có ≥10 triệu; Không Ngủ 12.100; Trứng Vàng 1.037 |
| `data/dnse_financials.json`, `outputs/tables/computed/table_B*.csv` | Slide 2, 11 | LNTT lõi, môi giới lỗ, chi phí nhân sự 99,4 tỷ, thuê ngoài 62,7 tỷ, khấu hao 35,4 tỷ, phần mềm theo nguyên giá 168,5 tỷ (2025). Đây là mốc chi phí công nghệ |
| `outputs/tables/computed/table_C1*.csv` | Slide 2 | Thang thị phần |
| `data/reviews_flagged_*.csv`, `reviews_flagged_ios_*.csv`, `reviews_raw_ios_*.csv` | Slide 4, 5, 15 | Chuyển dịch 2026; có phiên bản app trên iOS |
| `data/segment_model.json`, `findex_raw.json` | Slide 6, appendix | Quy mô người đi làm có TK nhưng chưa tiết kiệm chính thức |
| `data/manual/idle_cash_rates.csv` | Slide 3, 10 | **Cập nhật lên mức 10/2026** |
| `data/market_macro.json` | Slide 3 | Tiền NĐT, số TK toàn thị trường |
| `data/manual/scenario_*.csv` | — | **Thay** bằng `payday_assumptions.csv` (§4.4) |

### 4.2 Data công khai cần thu thập thêm

| # | Thông tin | Nguồn gợi ý | Dùng ở | Thời gian |
|---|---|---|---|---|
| 1 | ~~Teardown bằng ảnh chụp màn hình~~ → **Đã làm bằng tra cứu tại bàn ngày 16/10** (14 sản phẩm, có nguồn từng ô) | `competitor_features.md` | Slide 3, 10, appendix C | Xong. Còn lại vài ô "chưa xác minh" (§7 của file đó) |
| 2 | Biểu phí quỹ: phí phát hành SIP, phí mua lại, phí quản lý; phần chia cho đại lý phân phối nếu có công bố | Điều lệ quỹ, prospectus, factsheet (SSIAM, Dragon Capital, VCBF, VinaCapital) | Lợi suất phí (slide 11) | 2 giờ |
| 3 | Lãi Trứng Vàng theo kỳ hạn, bậc lãi Không Ngủ, lãi Margin X hiện hành | App DNSE | Slide 7, 11; `plan_tech.md` | 1 giờ |
| 4 | Lãi tiền gửi và chứng chỉ tiền gửi 10/2026; trần lãi của NHNN | Báo chí tài chính, website ngân hàng | Slide 3 | 30 phút |
| 5 | Doanh thu phân phối quỹ và NAV phân phối của TCBS | TCBS 2Q2026 earnings call, BCTC | Mốc lợi suất phí | 1 giờ |
| 6 | Thu nhập theo nhóm tuổi | NSO (điều tra lao động – việc làm) | Giả định mức đóng góp | 1 giờ |
| 7 | Lương kỹ sư phần mềm tại Việt Nam | Báo cáo lương IT 2025/2026 có ghi nguồn | Chi phí xây dựng | 30 phút |
| 8 | BCTN 2025 và thuyết minh BCTC của DNSE: cơ cấu tuổi khách (nếu có), số người dùng Ensa, cơ cấu chi phí môi giới, chi phí quảng cáo/khuyến mại | ir.dnse.com.vn (bản PDF) | Mốc CAC, chi phí | 2 giờ |
| 9 | Văn bản pháp lý: TT 121/2020 Điều 4, 24, 27; Luật CK 2019 Điều 72; TT 64/2024 (điều khoản chuyển tiếp); trần lãi NHNN; quy định đại lý phân phối chứng chỉ quỹ. **Kiểm DNSE đã có tên trong danh sách đại lý phân phối CCQ chưa** | Thư viện Pháp luật, website UBCKNN | Appendix E, Q&A | 2 giờ |
| 10 | (Tùy chọn) BCTC và giá đối thủ (VCK, TCX, SSI, VND) | Thư viện **vnstock** (nguồn VCI): API có tài liệu, dễ bảo trì hơn endpoint nội bộ đang dùng trong `01b`/`01c` | Benchmark | 1 giờ |

### 4.3 Bằng chứng "feedback" (cập nhật 16/10: bỏ survey vì không kịp)

Rubric viết "*justifies retained or revised choices using findings, feedback **or** feasibility*", nên **survey không bắt buộc**. Thay bằng:

1. **Khảo sát đã công bố**, cho nhu cầu: 77% thấy tự quản lý danh mục khó; 81% muốn được tư vấn chuyên nghiệp (Nhân Dân 2025; VnEconomy 2025).
2. **Hành vi ngành**, cho nhu cầu: SSI, VPS, VPBank, VCBF đều tung sản phẩm tích lũy hoặc định kỳ trong năm 2026; TCBS Fundmart có khoảng 12.000 khách tham gia/tháng.
3. **Tiếng nói khách trong review**, cho thiết kế (đã khai thác ngày 16/10, xem `competitor_features.md` §6):
   - khách tự đề xuất mã định danh nạp tiền (ủng hộ VA);
   - khách khen Không Ngủ;
   - khách xin Trứng Vàng kỳ hạn 6–12 tháng;
   - khách than mất tiền khi rút Trứng Vàng sớm (cần minh bạch);
   - nhà đầu tư dài hạn ở VPS than phí tháng.

   **Nói thật giới hạn:** review không cho thấy khách đòi tính năng định kỳ.
4. **Tùy chọn, nếu còn 1–2 giờ:** 5 cuộc trò chuyện nhanh với người quen đang đi làm có TK chứng khoán, hoặc cho 5 người bấm thử prototype Figma (think-aloud). Ghi rõ n=5.

### 4.4 Bảng giả định v2 (đặt trong `data/manual/payday_assumptions.csv` + appendix H)

| Đầu vào | Thấp / Cơ sở / Cao (đề xuất) | Neo vào đâu | Kiểm bằng gì |
|---|---|---|---|
| Tỷ lệ TK ngủ đủ điều kiện (đi làm 22–40, tiếp cận được) | 15% / 25% / 35% | Findex (In labour force 79,9% người lớn) nhưng tệp DNSE trẻ hơn | Test 1 (survey 2.000 TK ngủ do DNSE chạy) |
| Tỷ lệ tiếp cận được (tin đến nơi và được mở) | Từ pilot | Chưa có nguồn công khai đáng tin, **không tự bịa** | Pilot |
| Tỷ lệ hoàn tất cài đặt / người được tiếp cận | Từ pilot | Benchmark nội bộ: Không Ngủ 0,8% tổng TK sau khoảng 6 tháng | Pilot (RCT) |
| Mức đóng góp/tháng | 0,8 / 1,2 / 1,5 triệu | NSO 9,0 triệu bình quân; vé tối thiểu của đối thủ (VCB 100.000đ, VinaSIP 500.000đ, VSI 10 triệu) | Pilot |
| Tỷ lệ ngừng đóng góp mỗi tháng | 4% / 2,5% / 1,5% | Pilot | Test persistence |
| Tỷ lệ rút số dư mỗi năm | 15% / 10% / 5% | Pilot | Gắn nhãn nguồn và đích của dòng tiền |
| Cơ cấu tài sản mặc định | Trứng Vàng 40 / quỹ 40 / ETF 20 | Thiết kế | — |
| Lợi suất ròng theo lớp tài sản | Trứng Vàng: lãi coupon − lãi trả khách; quỹ: phần chia phí; ETF ≈ 0 | Data DNSE, tài liệu quỹ, TCBS | §4.2 #2, #3, #5 |
| CAC trên mỗi saver ghi danh | 50k / 150k / 300k | So với thưởng mở TK 100k (×518.514 = 51,9 tỷ năm 2025) | Pilot |
| Chi phí xây dựng / vận hành | Ước theo số người × tháng × lương | DNSE Table B3; báo cáo lương IT | Báo giá nội bộ |
| Chi phí thưởng tier | ≤0,3% số dư Payday/năm, có trần | Thiết kế mới | Nhánh 3 của RCT |
| Phase 2: tỷ lệ số dư dùng làm tài sản đảm bảo × chênh lệch | 0 / 5% / 10% × khoảng 4,5 điểm (lợi suất cho vay ~11% − chi phí vốn 6,5%) | BCTC Q2/2026 | Sau 12 tháng, có kiểm tra phù hợp |

---

## 5. Đặt target như thế nào

### 5.1 Nguyên tắc
1. **Neo vào benchmark nội bộ trước**, rồi mới đến benchmark ngoài.
2. **Target là đầu ra của mô hình cohort**, không phải số tròn đẹp.
3. **Ba tầng KPI:** North Star, chỉ số dẫn dắt, chỉ số giới hạn (guardrail).
4. **Ngưỡng quyết định suy ra từ kinh tế học** (hòa vốn), không đoán.

### 5.2 Cây KPI

| Tầng | KPI | Ghi chú |
|---|---|---|
| North Star | **Số TK có tài sản ròng ≥10 triệu** (DNSE tự công bố; 27.100 cuối 2025) | Đặt horizon **24–36 tháng** (§R2: 18 tháng không đủ). Thêm "**funded savers**": saver có ≥3 kỳ góp liên tiếp |
| Dẫn dắt | Tỷ lệ hoàn tất cài đặt; tỷ lệ góp kỳ đầu trong 30 ngày; tỷ lệ đạt 3 và 6 kỳ liên tiếp; tiền mới ròng (đã gắn nhãn nguồn); mức góp bình quân | Đo theo cohort và theo kênh |
| Guardrail | Chuyển tiền thành công ≥99,5%; tỷ lệ phiên không crash; tỷ trọng trust và reliability trong review tiêu cực liên quan Payday; thời gian rút tiền trung vị; 100% khách hoàn tất đánh giá phù hợp; **tỷ lệ tiền Payday rút sang sức mua** | Chỉ số cuối là guardrail mới (rò rỉ sang trading) |
| Tài chính | CAC trên mỗi funded saver; doanh thu/saver; số tháng hoàn vốn; vốn lũy kế so với kế hoạch | Báo cáo theo từng cổng |

### 5.3 Công thức phễu

```
Saver ghi danh(tháng) = Pool TK ngủ × % đủ điều kiện × % tiếp cận được × % hoàn tất cài đặt × % góp kỳ đầu
                         (phân bổ theo lịch kênh từng tháng)
Số dư(t)  = Σ_cohort [số dư(t−1) × (1 − tỷ lệ rút) + saver còn góp(t) × mức góp]
TK ≥10tr(t) = 27.100 + số saver có lũy kế đóng góp giữ lại ≥10 triệu tại t
```

### 5.4 Benchmark có nguồn

| Benchmark | Giá trị | Nguồn | Cách dùng |
|---|---|---|---|
| Tài khoản Không Ngủ | 12.100 đăng ký sau khoảng 6 tháng (0,8% TK) | BCTN 2025 | Trần tham chiếu cho kênh số, sản phẩm opt-in |
| Khách hoạt động | 41.900 → 85.739 (gấp đôi trong 2025) | BCTN 2025 | Năng lực kích hoạt |
| Trứng Vàng | 1.037 khách hoạt động (12/2025) | BCTN 2025 | Sản phẩm tiết kiệm hiện có |
| TCBS Fundmart | Khoảng 12.000 khách tham gia/tháng, +33% so với cùng kỳ | Báo chí 2026 | Quy mô của người dẫn đầu phân phối quỹ |
| Tài khoản tiết kiệm cam kết | Khoảng 28% chịu tham gia khi được mời **trực tiếp** | Ashraf et al. (2006) | Cận trên cho kênh tư vấn trực tiếp |
| SMarT | 78% tham gia khi được **chuyên viên tư vấn** mời | Thaler & Benartzi (2004) | Kênh tư vấn và chủ lao động |
| Tự động ghi danh | 86% (opt-out qua chủ lao động) | Madrian & Shea (2001) | **Chỉ cho kênh payroll** |

### 5.5 Ngưỡng quyết định suy ra từ kinh tế học

- **CAC tối đa chấp nhận được** = giá trị hiện tại của doanh thu ròng mỗi saver trong horizon. *Ví dụ minh họa (§6):* với lợi suất ròng 0,6–1,0%/năm, góp 1,2 triệu/tháng, ngừng 2,5%/tháng, chiết khấu 12%/năm, thì PV ≈ **0,22–0,37 triệu đồng/saver trong 36 tháng**, hoặc 0,42–0,69 triệu trong 60 tháng.
- **Ngưỡng ghi danh hòa vốn của pilot** = chi phí tiếp cận mỗi TK ÷ CAC tối đa. *Ví dụ:* nếu mỗi lượt tiếp cận tốn 3.000đ và CAC tối đa là 150.000đ, ngưỡng là 2%. **Cả hai số trong ví dụ đều là giả định, phải thay bằng số thật.**
- Table F6 của Round 2 đặt ngưỡng "**15% ghi danh trong 60 ngày**". Mức này cao gần 20 lần benchmark Không Ngủ, nên phải giải thích nguồn gốc hoặc hạ xuống theo công thức trên.

### 5.6 Mẫu ngưỡng tiếp tục / mở rộng / điều chỉnh / dừng (điền số từ mô hình)

| Cổng | Mở rộng | Điều chỉnh | Dừng |
|---|---|---|---|
| Cuối pilot (tháng 6) | Ghi danh ≥ ngưỡng hòa vốn ×1,5; ≥60% đạt 3 kỳ; ≥80% tiền mới; chuyển tiền ≥99,5% | Ghi danh ở khoảng [ngưỡng hòa vốn; ×1,5], **hoặc** persistence 40–60%: đổi thông điệp, kênh hoặc vé | Ghi danh < ngưỡng hòa vốn **và** persistence <40%, hoặc vi phạm cổng tuân thủ/reliability |
| Tháng 12 | Funded savers và số dư đạt ≥80% kế hoạch mô hình; CAC ≤ trần | 50–80% kế hoạch | <50% kế hoạch hai quý liên tiếp |
| Tháng 24 | Doanh thu tháng ≥ chi phí vận hành tháng | — | Xem lại mô hình doanh thu (gói phí, phase 2) |

*Đã điền số ngày 16/10: xem `outputs/round3/tables/payday_decision_gates.csv` và bảng test ở §9. Mẫu trên giữ lại để thấy logic. Chỗ nào khác nhau thì dùng số trong bảng cổng, ví dụ ngưỡng persistence nay là 81% để mở rộng, <60% thì dừng.*

---

## 6. Business case (slide của CFO): phương pháp và ví dụ minh họa

### 6.1 Cấu trúc
- **Doanh thu trực tiếp theo lớp tài sản:** chia phí phân phối quỹ; chênh lệch lãi Trứng Vàng; ETF ≈ 0 (DNSE miễn phí giao dịch).
- **Chi phí:**
  - xây dựng (MVP: mục tiêu, khẩu vị rủi ro, VA, scheduler, order routing, dashboard);
  - vận hành (đội, hạ tầng, hỗ trợ, đối soát);
  - phí đối tác (ngân hàng VA, quỹ);
  - CAC (tiếp cận, ưu đãi);
  - thưởng tier (có trần);
  - tuân thủ và pháp chế;
  - chi phí mô hình ngôn ngữ cho Ensa.
- **Giá trị gián tiếp, tách riêng và ghi rõ là ước tính:**
  - giữ được số dư lẽ ra sẽ rời DNSE;
  - phase 2: cho vay với tài sản đảm bảo là ETF (opt-in, có kiểm tra phù hợp);
  - giảm chi phí nền tảng trên mỗi TK có tiền (7,3 triệu năm 2025);
  - không phải trả chi phí thu hút khách mới (thưởng 100k/TK);
  - phòng thủ trước VSI, eSIP và ngân hàng khi có Open API.

### 6.2 Ví dụ minh họa: J-curve 36 tháng

> ⚠️ **ĐẦU VÀO LÀ GIẢ ĐỊNH MINH HỌA. KHÔNG ĐƯA LÊN SLIDE KHI CHƯA THAY BẰNG SỐ CÓ NGUỒN.** Mục đích là để thấy cấu trúc của bài toán.

**Giả định chung:**
- Ghi danh: 350 saver/tháng (tháng 4–6, pilot), 3.000 (tháng 7–12), 6.000 (tháng 13–18), 8.000 (tháng 19–36). Lũy kế 55.050 saver ở tháng 18 và 199.050 ở tháng 36.
- Góp 1,2 triệu/tháng; ngừng 2,5%/tháng; rút 10% số dư/năm.
- Chi phí xây dựng 12 tỷ (tháng 1–6); vận hành 6 tỷ/năm.
- Cơ cấu tài sản Trứng Vàng/quỹ/ETF = 40/40/20, lợi suất ròng 1,0/0,5/0%, tức gộp 0,6%.

| Tổ hợp (lợi suất ròng, CAC/saver, thưởng, cho vay phase 2) | Tiền lũy kế tháng 36 | Tháng doanh thu ≥ chi phí | Số dư tháng 36 |
|---|---:|:---:|---:|
| 0,6%; 150k; thưởng 0,3%/năm; không cho vay | −53,7 tỷ | Chưa đạt | 2,43 nghìn tỷ |
| 0,6%; 150k; không thưởng | −47,5 tỷ | Chưa đạt | 2,43 nghìn tỷ |
| 0,6%; 50k | −27,6 tỷ | 32 | 2,43 nghìn tỷ |
| 1,0%; 150k | −39,2 tỷ | 34 | 2,43 nghìn tỷ |
| 1,0%; 50k | −19,3 tỷ | 27 | 2,43 nghìn tỷ |
| 0,6%; 50k; cho vay 10% số dư từ tháng 19 (4,5 điểm) | −18,9 tỷ | 26 | 2,43 nghìn tỷ |
| 1,0%; 50k; cho vay 10% | −10,6 tỷ | 24 | 2,43 nghìn tỷ |

*Ở tháng 18 của kịch bản này: 55.050 saver ghi danh, 49.108 còn góp, số dư khoảng 0,33 nghìn tỷ (so với 2,84 nghìn tỷ trong Table F5 của Round 2).*

**Rút ra cho slide CFO:**
1. Chỉ tính phí trực tiếp thì Payday là **khoản đầu tư nhiều năm theo hình chữ J**. Không thể bán bằng "doanh thu phí năm đầu".
2. Đòn bẩy lớn nhất là **CAC**: từ 150k xuống 50k cải thiện khoảng 20 tỷ lũy kế ở tháng 36. Kế đến là **lợi suất ròng** (cơ cấu tài sản, thỏa thuận chia phí) và **phase 2 cho vay** (có điều kiện).
3. Vì vậy đề nghị với Board phải **theo giai đoạn**: chỉ duyệt Phase 0–1 trước, có cổng dừng ở tháng 6 để chặn rủi ro thua lỗ. Giá trị chiến lược (§6.1) trình bày riêng, có nhãn rõ ràng.

### 6.3 Slide CFO cần có
1. Vốn theo từng giai đoạn.
2. Unit economics: doanh thu/năm trên mỗi 10 triệu số dư, trần CAC, số tháng hoàn vốn.
3. Đường J lũy kế theo 3 kịch bản.
4. Số saver và CAC hòa vốn.
5. Tornado độ nhạy: CAC, lợi suất, tỷ lệ ngừng, mức góp.
6. Giá trị gián tiếp, tách riêng.

### 6.4 Nên đưa mô hình vào code
Viết `src/payday_model.py`, đọc `data/manual/payday_assumptions.csv`, xuất bảng và hình J-curve vào `outputs/`, rồi thêm vào `run_all.py`. Cách này giữ được điểm mạnh "tái lập được" của Round 2. Nếu thiếu thời gian, ít nhất làm một bảng tính có công thức sống và đưa ảnh chụp vào appendix B.

---

## 7. Go-to-market năm đầu (tháng 0 = Board duyệt)

*Cập nhật 16/10 (Phase 2). Số lấy từ mô hình cohort, kịch bản base (`outputs/round3/tables/gtm_year1.csv`). Chi tiết ở `payday_spec.md` §11.1. Pilot tăng từ 20.000 lên 45.000 TK theo quyết định D4: cỡ mẫu này đủ để phát hiện chênh lệch khoảng 10 điểm về tỷ lệ đạt 6 kỳ giữa hai nhánh (`payday_pilot_power.csv`).*

| Quý | Mục tiêu | Phân khúc và kênh | Thông điệp | Cổng / KPI | Ghi danh trong quý | Cuối quý: funded / số dư | Chi phí |
|---|---|---|---|---|---:|---|---:|
| Q1 (tháng 1–3) | Xây MVP, ký đối tác, **beta nội bộ với TK nhân viên DNSE** | Nhân viên DNSE; nội bộ | — | Cổng 0: phí VA mục tiêu 0đ; chia phí quỹ ≥30%; biên trái phiếu ≥0,6 điểm; shadow run ≥99,5%; xác nhận tuân thủ bằng văn bản | 0 | 0 / 0 | 2,09 tỷ |
| Q2 (tháng 4–6) | **Pilot RCT 45.000 TK ngủ**, 3 nhánh × 15.000 | E2 có dấu hiệu nhận lương; SMS, Zalo, push, email, Ensa; tối đa 3 lần liên hệ mỗi TK | *"Your account is ready. Let payday do the investing."* Từ 500.000đ, không thưởng khi đăng ký | Cổng 1: ghi danh ≥1,5% thì mở rộng, <1,0% thì dừng; ≥81% đạt 3 kỳ; ≥80% tiền mới; chi phí ròng dự báo ≤1,6 triệu/TK mới ≥10 triệu | 600 | 162 / 1,1 tỷ | 3,63 tỷ |
| Q3 (tháng 7–9) | Mở rộng trong tệp | TK ngủ đủ điều kiện (E2); khách hoạt động (E1) qua banner trong app; TK mới qua bước lập kế hoạch khi mở TK | *"Keep a core that grows while you trade."* / *"Start your plan with your first deposit."* | Hằng tháng: funded và số dư so với đường kế hoạch; CAC/funded ≤127.512đ | 4.287 | 1.620 / 10,5 tỷ | 1,69 tỷ |
| Q4 (tháng 10–12) | Mở kênh ngoài đầu tiên | Nhân viên của 3–5 doanh nghiệp (N1), qua buổi HR có người tư vấn; khách nhận lương của ngân hàng giữ VA | *"An employee benefit that invests your salary."* | Cổng 2: funded ≥3.962 (80% kế hoạch); số dư ≥24,1 tỷ; theo dõi tỷ lệ tham gia so với mức 39% cần đạt ở năm 2 | 4.527 | 4.953 / 30,1 tỷ | 1,80 tỷ |

- **Năm 1 (base):** 9.414 saver ghi danh; 4.953 funded (≥3 kỳ liền); số dư 30,1 tỷ; chi 9,2 tỷ, trong đó marketing và chi phí tiếp cận 1,17 tỷ (13%). Downside: 1.503 funded, 7,9 tỷ số dư.
- **Giá:** không phí nền tảng. Doanh thu từ phần chia phí quỹ và biên Trứng Vàng. Gói giữ chân phi tiền mặt (D1). Điều khoản trên một màn hình.
- **Không làm:**
  - thưởng tiền khi mở TK; KOL kiểu "nhận tiền miễn phí"; thưởng có điều kiện;
  - nhắn lại người đã từ chối (tối đa 3 lần liên hệ);
  - khuyến mại hoàn tiền qua đối tác. Một review 07/2026 viết "bị zalopay lừa mua chứng khoán hoàn 50k".
- **ZaloPay:** không có trong năm 1 và không có trong mô hình. Để Phase 3 làm kênh nạp tiền thứ hai và thử round-up (`plan_tech.md` §3.8).
- **Ngân sách:** giải ngân theo cổng. Board chỉ duyệt Phase 0–1 (6,6 tỷ).
- **Nội dung giáo dục** (quản lý tài chính cá nhân, DCA, rủi ro) theo quy định quảng cáo chứng khoán, được pháp chế duyệt.

---

## 8. Lộ trình chiến lược

*Số từ `outputs/round3/tables/roadmap_phases.csv` (base). Chi tiết ở `payday_spec.md` §11.2. Slide 13 ghép thêm lộ trình hệ sinh thái của `plan_tech.md` §5.*

| Phase | Tháng | Mục tiêu | Sáng kiến | Cổng | Chi phí | Cuối phase (base) |
|---|---|---|---|---|---:|---|
| 0. Xây và tuân thủ | 1–3 | MVP an toàn, hợp pháp | VA với ngân hàng đối tác (phí mục tiêu 0đ); hợp đồng 1–2 công ty quỹ; danh mục mẫu do người có chứng chỉ ký; thông báo UBCKNN và tham vấn về vai trò Trứng Vàng; scheduler tách khỏi bước kiểm sức mua; dashboard và trang số đo | Cổng 0 (tháng 3): điều khoản đối tác không kém mô hình; shadow run ≥99,5%; xác nhận tuân thủ | 2,09 tỷ | Tiền lũy kế −2,1 tỷ |
| 1. Pilot | 4–6 | Đo ghi danh, duy trì, mức góp, tiền mới | RCT 45.000 TK: đối chứng / Payday / Payday + gói giữ chân; survey 2.000 TK ngủ do DNSE chạy | Cổng 1 (tháng 6): chi phí ròng dự báo ≤1,6 triệu/TK mới ≥10 triệu (kế hoạch 1,29); ghi danh ≥1,5%, dừng <1,0% | 3,63 tỷ | 600 saver; −5,7 tỷ |
| 2. Mở rộng trong tệp | 7–12 | Quy mô có kiểm soát | Roll-out TK ngủ; in-app cho khách hoạt động; bước lập kế hoạch khi mở TK; nhóm hold-out cho gói giữ chân; 3–5 doanh nghiệp đầu tiên | Cổng 2 (tháng 12): funded ≥80% kế hoạch; CAC/funded ≤127.512đ | 3,49 tỷ | 9.414 ghi danh; 4.953 funded; 30,1 tỷ; −9,2 tỷ |
| 3. Kênh ngoài | 13–24 | Kênh tạo mặc định | Doanh nghiệp qua buổi HR; trích % lương qua Open API (ngân hàng phải tuân thủ TT 64/2024 trước 01/03/2027, vẫn cần thỏa thuận riêng); tự tăng mức góp khi tăng lương; ZaloPay làm kênh nạp thứ hai, thử round-up | Cổng 3 (tháng 24): TK ≥10 triệu ≥80% kế hoạch; chi phí ròng ≤1,25 lần kế hoạch; doanh nghiệp tham gia ≥39% | 7,28 tỷ | 13.952 funded; 178 tỷ; 7.714 TK mới ≥10 triệu; −16,0 tỷ |
| 4. Tối ưu | 25–36 | Bản quản lý hoàn toàn, kinh tế tốt hơn | Công ty quỹ đối tác hoặc công ty quỹ của DNSE (ĐHĐCĐ 2026); Trứng Vàng mở rộng với trái phiếu và chứng chỉ quỹ của Vietcombank, VietinBank, BIDV (kế hoạch 2026 của DNSE, tài liệu ĐHĐCĐ tr. 75) | Rà hằng quý: doanh thu so với chi phí vận hành; chi phí ròng/TK | 7,23 tỷ | 16.269 funded; 352 tỷ; 14.871 TK mới ≥10 triệu; −22,0 tỷ |

- **Base không hòa vốn trong 60 tháng.** NPV −25,0 tỷ; tiền lũy kế tháng 60 là −32,0 tỷ; chi phí ròng 1,29 triệu cho mỗi TK mới ≥10 triệu. Upside: NPV +11,0 tỷ, hòa vốn tháng 24. Vì vậy đề nghị với Board là một quyền chọn theo giai đoạn (`review_phase1.md` D4, D6).
- **Phương án để sau, không tính trong base:** khách tự chọn dùng ETF trong kế hoạch làm tài sản đảm bảo cho TK ký quỹ thường (mô hình giả định 10% số dư, từ tháng 19).
  - NPV base cải thiện từ −25,0 lên −20,9 tỷ nhưng vẫn âm (`payday_option_lending.csv`).
  - Phương án này đi ngược mục đích tiết kiệm và chạm đúng mảng ký quỹ bị phạt năm 2026.
  - Vì vậy chỉ xét ở Cổng 3, khi pháp chế đồng ý và chủ đề trust dưới 10% review tiêu cực liên quan Payday.

---

## 9. Triển khai và kiểm chứng

**RACI:** bảng đầy đủ (10 việc × 8 vai) ở `payday_spec.md` §11.3 và `outputs/round3/tables/raci.csv`. Tóm tắt:

| Vai trò | Vai trò chính |
|---|---|
| CEO | Bảo trợ dự án; quyết định ở các cổng (A), CFO và Head of Product chuẩn bị |
| CFO | Điều khoản đối tác: ngân hàng VA, quỹ, nguồn trái phiếu (A/R); chuẩn bị quyết định ở các cổng: ngân sách, unit economics (R) |
| CTO | MVP (scheduler, VA, phân bổ, dashboard); shadow run và cổng 99,5%; công bố số đo (R) |
| Head of Product | Thiết kế và đọc RCT; tiếp cận khách (A); phàn nàn, rút tiền, xử lý sau sự cố (A); công bố số đo (A) |
| Pháp chế | Thông báo UBCKNN, ý kiến pháp lý, duyệt khuyến mại; chịu trách nhiệm cuối về danh mục mẫu và quy tắc phù hợp |
| Marketing / CRM | Thực hiện tiếp cận và thông điệp (R) |
| Chăm sóc khách hàng | Phàn nàn, rút tiền, xử lý sau sự cố (R); chỉ số trust |
| Người có chứng chỉ | Soạn và ký danh mục mẫu, quy tắc phù hợp (R) |

**Risk register:** 6 rủi ro, chấm khả năng × tác động trên thang 1–5 (`risk_register.csv`; chi tiết ở `payday_spec.md` §11.4):
- R1 app hoặc chuyển tiền lỗi đúng ngày lương: 20 (cao);
- R2 quá ít TK ngủ ghi danh: 16 (cao);
- R4 cơ quan quản lý phản đối vai trò Trứng Vàng hoặc luồng tư vấn: 15 (cao);
- R3 điều khoản đối tác: 12;
- R5 thị trường giảm hoặc xung đột lợi ích: 12;
- R6 tiền kế hoạch bị chuyển sang giao dịch: 9.

Stress test: cả hai cú sốc làm TK ≥10 triệu tháng 36 giảm 18,5%, nhưng tiền tháng 60 chỉ thay đổi −0,5 tỷ.

**Chuỗi phụ thuộc:**
- Ngân hàng VA → scheduler → shadow run → pilot.
- Hợp đồng quỹ → kệ sản phẩm. Nếu chậm, ra mắt với Trứng Vàng + ETF.
- Thông báo UBCKNN và tham vấn Trứng Vàng → ra mắt. Quỹ trái phiếu là lõi dự phòng.
- Gắn nhãn nguồn tiền → KPI tiền mới.
- Thỏa thuận Open API (sau 01/03/2027) → trích % lương ở Phase 3.

**Test (Table F6 cập nhật bằng số của mô hình; `payday_decision_gates.csv`):**

| # | Giả định | Test | Ngưỡng Round 2 | Ngưỡng Round 3 | Cổng |
|---|---|---|---|---|---|
| 1 | Nhiều TK ngủ là người đi làm có ý định đầu tư | Dữ liệu nội bộ; survey 2.000 TK ngủ | ≥30% có ý định | Giữ ≥30%. Mô hình giả định 25% TK ngủ đủ điều kiện (15–35%) | 1 |
| 2 | Tư vấn và tự động biến ý định thành tiền | RCT 45.000 TK | 15% ghi danh trong 60 ngày; giữ 70% tiền ở ngày 90 | Ghi danh ≥1,5% để mở rộng, <1,0% thì dừng (hòa vốn 1,02% = 1.300đ ÷ 127.512đ); ≥81% đạt 3 kỳ, <60% thì dừng | 1 |
| 3 | Gói giữ chân tăng persistence | Nhánh có và không có gói giữ chân | Tỷ lệ 6 kỳ tăng 10 điểm | Giữ 10 điểm; pilot 45.000 TK phát hiện được 9,9 điểm. Tier bằng tiền chỉ bật khi phí VA được miễn và tỷ lệ 12 kỳ đạt ≥73,3% (base 64,5%) | 2 |
| 4 | Tính năng minh bạch tăng tỷ lệ cài đặt | A/B màn hình phí và số đo | Tỷ lệ cài đặt +5 điểm | Giữ | 1 |
| 5 | Luồng tư vấn tuân thủ | Rà tuân thủ; thông báo UBCKNN | Xác nhận bằng văn bản | Giữ; thêm tham vấn về vai trò Trứng Vàng | 0 |
| 6 | Chuyển tiền tin cậy | Load test; shadow run | 99,5% chuyển thành công | ≥99,5% ghi có trong cùng ngày làm việc; đo lại hằng tháng sau ra mắt | 0, hằng tháng |
| 7 | Tiền vào là tiền mới; chi phí đơn vị giảm | Gắn nhãn nguồn tiền; theo dõi chi phí | 80% tiền mới; chi phí dưới 7,3 triệu/TK có tiền | ≥80% tiền mới; chi phí ròng ≤1,6 triệu/TK mới ≥10 triệu (kế hoạch 1,29), dừng >2,6 triệu | 1, 3 |
| 8 (mới) | Tiền kế hoạch không bị chuyển sang giao dịch | Tỷ lệ tiền rút sang sức mua | — | ≤10% số tiền rút | Hằng tháng |
| 9 (mới) | CAC trên mỗi funded saver không vượt trần | CAC ÷ tỷ lệ đạt 3 kỳ | — | ≤127.512đ (base 80.247đ) | 2 |
| 10 (mới) | Mức góp đủ để hoàn vốn | Mức góp bình quân | — | ≥1.000.000đ; dừng <716.502đ | 1 |
| 11 (mới) | Điều khoản đối tác giữ được kinh tế | Phí VA mỗi kỳ góp | — | Mục tiêu 0đ; dừng >6.191đ (miễn phí thì trần CAC tăng từ 127.512đ lên 198.876đ) | 0 |
| 12 (mới) | Kênh doanh nghiệp đáng làm | Tỷ lệ tham gia sau buổi HR | — | ≥39%; dừng <20% | 3 |

*Ngưỡng 15% của Round 2 cao gần 20 lần mức Tài khoản Không Ngủ đạt được (0,8% số TK sau khoảng 6 tháng). Ngưỡng mới suy ra từ trần CAC. Đây là một mục của slide "What changed".*

---

## 10. Kế hoạch 5 ngày (15/10–20/10)

*Vai trò: **L** = lead/storyline, **D** = data/mô hình, **P** = product/UX, **R** = research đối thủ/pháp lý, **S** = thiết kế slide. Một người có thể kiêm nhiều vai.*

| Ngày | Việc | Người | Đầu ra |
|---|---|---|---|
| **Thứ Năm 15/10** | Chốt thông điệp và outline §3; phân công; dựng khung mô hình cohort | L, D | Outline đã duyệt; khung mô hình |
| **Thứ Sáu 16/10** | ✅ Tra cứu đối thủ tại bàn (`competitor_features.md`, thay cho chụp màn hình); ✅ khai thác review làm "feedback" (thay cho survey). Còn lại: thu biểu phí quỹ và lãi suất; nháp slide 2–6; wireframe v1 (Figma) | R, P, L | Slide 2–6; wireframe v1 |
| **Thứ Bảy 17/10** | Mô hình: chi phí, độ nhạy; nháp GTM và roadmap; slide 7–10. *Tùy chọn:* 5 người bấm thử prototype | D, P, L | Bảng business case; slide 7–10 |
| **Chủ Nhật 18/10** | Slide 11–15; executive summary; appendix; **tập dượt lần 1 (bấm giờ 15 phút)**; red-team Q&A theo `review_payday.md` §8 | Cả team | Bản đủ 15 slide |
| **Thứ Hai 19/10** | Sửa theo dượt; kiểm references; **dò lại mọi con số về nguồn**; chỉnh thiết kế; tập dượt lần 2 | Cả team | Bản gần cuối |
| **Thứ Ba 20/10** | Đọc soát lần cuối; xuất PDF ≤10MB; nén; **nộp trước 19:30**; xác nhận đã nhận | L, S | Đã nộp |

---

## 11. Checklist trước khi nộp

- [ ] ≤15 slide nội dung; executive summary ≤150 từ, cỡ chữ 14–15, có vốn đầu tư và lợi nhuận.
- [ ] Đủ 6 phần tối thiểu + roadmap theo phase + GTM năm 1 + business case.
- [ ] Mỗi biểu đồ có dòng "Source:"; mỗi con số truy được về nguồn hoặc mô hình.
- [ ] Số liệu nhất quán giữa các slide (đặc biệt target, số dư, CAC).
- [ ] Thuật ngữ tiếng Việt có bản dịch; references nằm trên slide, cùng một kiểu trích dẫn, không có hyperlink.
- [ ] Mọi bằng chứng bổ sung nằm trong appendix của file (không có file hay link riêng).
- [ ] 16:9, PDF ≤10MB, đã nén, tên `[FBAR3_2026]_KTQT FTUers`.
- [ ] Nộp một lần bằng email trưởng nhóm, trước 19:30.
- [ ] Không còn số đã biết là sai: target 85.000/18 tháng; "tier tối đa 5,6 tỷ"; phí 0,8% trên toàn bộ tài sản; Madrian & Shea cho kênh opt-in.

---

## 12. Chuẩn bị Q&A và Round 3B (ngắn)

- **Q&A Round 3A:** dùng `review_payday.md` §8 (10 câu kèm hướng trả lời). Mỗi người phụ trách 2–3 câu.
- **Round 3B (tiếng Việt, tranh biện):** chuẩn bị **1 trang "số liệu bỏ túi"** để trích dẫn bằng lời:
  - lãi suất 10/2026;
  - mốc Open API 01/03/2027;
  - trần lãi 0,5% và 4,75%;
  - vụ phạt DNSE 802,5 triệu (275 triệu vì dịch vụ ứng trước không báo cáo);
  - tiền NĐT tại CTCK −38% trong 3 quý;
  - 13,85 triệu TK chứng khoán;
  - Findex 70,5% có TK, 43,1% tiết kiệm chính thức;
  - nâng hạng FTSE (21/09/2026);
  - VSI (11/08/2026), SSI eSIP.

---

## Nguồn

- Booklet Round 3: `docs/[FBA 6] QUESTION BOOKLET ROUND 3.md`.
- Report Round 2 đã nộp: `report/FBAR2_2026_KTQT_FTUers.pdf` (Table C1, B1–B3, E3, F5, F6, G1).
- [Thông tư 64/2024/TT-NHNN (Thư viện Pháp luật)](https://thuvienphapluat.vn/van-ban/Tien-te-Ngan-hang/Thong-tu-64-2024-TT-NHNN-trien-khai-giao-dien-lap-trinh-ung-dung-mo-nganh-Ngan-hang-641360.aspx)
- [VPS chính thức ra mắt sản phẩm VPS Smart Indexing](https://www.tinnhanhchungkhoan.vn/vps-chinh-thuc-ra-mat-san-pham-vps-smart-indexing-post395704.html)
- [Thêm quỹ Dragon Capital, SSI iBoard mở rộng sản phẩm đầu tư trên nền tảng số](https://doanhnhan.baophapluat.vn/them-quy-dragon-capital-ssi-iboard-mo-rong-san-pham-dau-tu-tren-nen-tang-so.html)
- [Chứng khoán: TCBS Fundmart (Thị trường Tài chính Tiền tệ)](https://thitruongtaichinhtiente.vn/print/80857.html)
- [TCBS 2Q2026 Earnings Call](https://www.tcbs.com.vn/wp-content/uploads/2026/07/TCBS_2Q2026-Earnings-Call_VN-1.pdf)
- [Lãi suất đầu tháng 10/2026](https://thitruongtaichinhtiente.vn/lai-suat-dau-thang-10-2026-tiet-kiem-giu-nhip-on-dinh-chung-chi-tien-gui-hut-khach-85944.html)
- [Phiếu đăng ký SIP của VCBF](https://www.vcbf.com/images/2019/phieu_sip-sip.pdf)
- Madrian & Shea (2001); Thaler & Benartzi (2004); Ashraf, Karlan & Yin (2006).
- Ví dụ minh họa ở §5.5 và §6.2: tính ngày 15/10/2026 bằng mô hình cohort đơn giản (đầu vào giả định, ghi ở §6.2).

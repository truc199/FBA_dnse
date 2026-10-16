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

| Quý | Mục tiêu | Phân khúc | Kênh | Thông điệp | KPI |
|---|---|---|---|---|---|
| Q1 (tháng 1–3) | Xây MVP, tuân thủ, **beta nội bộ với nhân viên DNSE** | Nhân viên DNSE (dùng thật, thử độ ổn định) | Nội bộ | — | Shadow run ≥99,5%; xác nhận tuân thủ; lỗi nghiêm trọng = 0 |
| Q2 (tháng 4–6) | **Pilot RCT** 20.000 TK ngủ (3 nhánh) | E2 có dấu hiệu đi làm | SMS, Zalo OA, email, push, Ensa | *"Your account is ready. Let payday do the investing."* Bước đầu 500k, không thưởng có điều kiện | Ghi danh ≥ ngưỡng hòa vốn; 3 kỳ ≥60%; tiền mới ≥80% |
| Q3 (tháng 7–9) | Mở rộng trong tệp | E2 theo cohort tốt nhất; E1 theo kiểu core–satellite | Như trên + banner trong app cho khách hoạt động | *"Keep a core that grows while you trade."* | Funded savers theo kế hoạch; CAC ≤ trần |
| Q4 (tháng 10–12) | Kênh mới | N1 | **Ngân hàng giữ VA** (khách nhận lương), **ZaloPay**, **3–5 doanh nghiệp** (phúc lợi nhân viên) | *"An employee benefit that invests your salary."* | Số doanh nghiệp ký; tỷ lệ tham gia trong doanh nghiệp |

- **Giá:** miễn phí; doanh thu đến từ quỹ và Trứng Vàng; tier thưởng trên tiền đã đầu tư; điều khoản trên một màn hình.
- **Không làm:** thưởng tiền khi mở TK; KOL kiểu "nhận tiền miễn phí"; nhắn tin dồn dập khi đã có tín hiệu từ chối.
- **Ngân sách:** chia theo kênh, có trần CAC, giải ngân theo cổng.
- **Nội dung giáo dục** (quản lý tài chính cá nhân, DCA, rủi ro) phải theo quy định quảng cáo chứng khoán, được pháp chế duyệt.

---

## 8. Lộ trình chiến lược

| Phase | Thời gian | Mục tiêu | Sáng kiến | KPI / cổng |
|---|---|---|---|---|
| 0. Xây và tuân thủ | Tháng 0–3 | MVP an toàn, hợp pháp | Mục tiêu, khẩu vị rủi ro, 3 danh mục mẫu (người có chứng chỉ duyệt), VA, scheduler, order routing, dashboard minh bạch; thông báo UBCKNN; hợp đồng ngân hàng VA và quỹ; SLO reliability | Shadow run ≥99,5%; xác nhận bằng văn bản |
| 1. Pilot | Tháng 3–6 | Kiểm giả định 1–7 | RCT 3 nhánh (đối chứng; Payday; Payday + tier mới); survey 2.000 TK ngủ | Ngưỡng §5.6 |
| 2. Mở rộng trong tệp | Tháng 7–12 | Đạt quy mô có kiểm soát | Cohort tốt nhất; core–satellite cho E1; ZaloPay; bậc thang Trứng Vàng | Funded savers, CAC, persistence |
| 3. Mở rộng ra ngoài | Tháng 13–24 | Kênh tạo mặc định | Chủ lao động (B2B2C); liên kết ngân hàng qua Open API (sau 01/03/2027) để **trích % lương**; tự động tăng tỷ lệ khi tăng lương; thử round-up; ETF làm tài sản đảm bảo (opt-in, nếu cơ quan quản lý chấp thuận) | TK ≥10 triệu; tháng hòa vốn vận hành |
| 4. Tối ưu | Tháng 24–36 | Bản quản lý hoàn toàn | Hợp tác công ty quản lý quỹ, hoặc công ty con quản lý quỹ (ĐHĐCĐ đã duyệt chủ trương) | Doanh thu/saver; NPS |

---

## 9. Triển khai và kiểm chứng

**RACI rút gọn:**

| Vai trò | Phụ trách chính |
|---|---|
| CEO | Bảo trợ dự án, quyết định ở các cổng |
| CFO | Ngân sách, unit economics, chi phí tier |
| CTO | Tích hợp VA, scheduler, SLO reliability, gắn nhãn dữ liệu |
| Head of Product | Hành trình khách hàng, thử nghiệm, KPI |
| Tuân thủ / Pháp chế | Thông báo UBCKNN, duyệt danh mục mẫu, rà quy định khuyến mại và quảng cáo |
| Marketing / CRM | Tiếp cận khách, thông điệp |
| Chăm sóc khách hàng | Chỉ số trust, rút tiền |
| Đối tác | Ngân hàng, quỹ, ZaloPay, doanh nghiệp |

**Chuỗi phụ thuộc:**
- Ngân hàng VA → scheduler → pilot.
- Đối tác quỹ → kệ sản phẩm.
- Thông báo UBCKNN → ra mắt.
- Cổng reliability → pilot.
- Gắn nhãn nguồn tiền → KPI tiền mới.

**Test (Table F6 cập nhật):** giữ test 1–7 của Round 2, sửa ngưỡng theo §5.5, và **thêm** 2 test:
- **Test 8:** tỷ lệ tiền Payday rút sang sức mua (guardrail).
- **Test 9:** CAC trên mỗi funded saver không vượt trần.

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

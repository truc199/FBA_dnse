# Phản biện Phase 1 và đánh giá các quyết định (Round 3A)

*Lập ngày 16/10/2026. Cách làm: tìm lỗi trong chính mô hình và lập luận của Phase 1; tra thêm nguồn cho từng điểm yếu; sửa mô hình; đánh giá từng quyết định theo cùng một bộ tiêu chí; chạy lại toàn bộ (`python src/round3/run_round3.py`, 35/35 test đạt). Số liệu dưới đây là kết quả **sau khi sửa**.*

---

## 0. Kết luận

1. **Payday không phải sản phẩm sinh lời độc lập trong 5 năm** ở kịch bản base. Sau khi sửa, base vẫn không hòa vốn và không hoàn vốn trong 60 tháng: NPV −25,0 tỷ, tiền lũy kế tháng 60 là −32,0 tỷ. Upside có NPV +11,0 tỷ, hòa vốn tháng 24, hoàn vốn tháng 44.
2. **Lập luận đúng cho Board là "quyền chọn có trần lỗ + ngân sách cho mỗi tài khoản có tiền"**, không phải "trung tâm lợi nhuận".
   - Board duyệt **6,6 tỷ** cho Phase 0–1 (gồm dự phòng 15%).
   - Board chấp nhận một ngân sách khoảng **1,3 triệu đồng chi phí ròng cho mỗi TK mới ≥10 triệu** (base: 1,29 triệu). Đó là mức của kế hoạch base.
   - Cổng tháng 6 dừng chương trình nếu pilot cho thấy chi phí này vượt gấp đôi kế hoạch. Kịch bản downside là khoảng 10 triệu/TK, nên sẽ bị dừng.
3. **Có 4 lỗi đã được sửa làm thay đổi kết quả:**
   - Biên Trứng Vàng quá lạc quan.
   - Tier bằng tiền tốn 41% doanh thu trên mỗi saver.
   - Cổng tháng 6 không nhất quán với kinh tế học của cả chương trình.
   - Pilot 20.000 TK thiếu lực thống kê.
4. **Phí VA trên mỗi kỳ góp là điểm nghẽn cấu trúc của sản phẩm vé nhỏ.** Ở lợi suất ròng 0,44%, mỗi kỳ góp 1 triệu chỉ sinh khoảng 368đ/tháng. Trong khi đó phí VA và phí phục vụ là 4.300đ, tức khoảng một năm doanh thu. Miễn phí VA phải là điều kiện đàm phán số 1 ở Phase 0.

---

## 1. Các vấn đề tìm thấy và cách đã sửa

| # | Vấn đề | Bằng chứng | Mức | Đã sửa | Ảnh hưởng |
|---|---|---|:---:|---|---|
| 1 | **Cổng tháng 6 cho "scale" trong khi chương trình lỗ.** Ngưỡng chỉ xét unit economics từng saver (CAC so với trần CAC), bỏ qua chi phí cố định. Đây là thứ thực sự khiến base không hoàn vốn | Base ghi danh 2% vượt ngưỡng 1,5%, trong khi NPV base âm | Cao | Thêm **Cổng 0** (tháng 3): điều khoản đối tác đã ký. Thêm **tiêu chí cấp chương trình** ở cổng 1 và 3: chạy lại mô hình với số đo của pilot; chi phí ròng/TK mới ≥10 triệu ≤1,25 lần kế hoạch thì scale, >2 lần thì dừng | Downside (10 triệu/TK) bị dừng ở tháng 6 thay vì đi tiếp |
| 2 | **Biên Trứng Vàng 1,0% quá lạc quan** | Trái phiếu Agribank ra công chúng có lãi bằng bình quân lãi 12 tháng Big4 + 2,0 điểm, khoảng 7,9% (S29). Trứng Vàng trả 7,6% kỳ 12 tháng, 7,1% kỳ 3 tháng (S17). Biên còn khoảng 0,3–0,8 điểm | Cao | Biên: 0,3 / **0,6** / 1,0%. Lợi suất ròng base giảm từ 0,62% xuống 0,44% | NPV base giảm khoảng 1,7 tỷ |
| 3 | **Trứng Vàng đang dùng cả trái phiếu do DNSE phát hành** | BCTN 2025, trang in 68: "phân bổ vào các trái phiếu của DNSE, Agribank và Ngân hàng TMCP Bản Việt"; BCTN xếp Trứng Vàng vào mảng "kinh doanh nguồn vốn" (S30) | Cao | Quyết định D7: lõi mặc định chỉ dùng trái phiếu do ngân hàng phát hành | Mất khoảng 4 tỷ tiền lũy kế trong 5 năm (xem D7) |
| 4 | **Tier bằng tiền không tự trả được** | Quà 10/20/50k + giảm phí 0,1 điểm + cộng 0,2 điểm lãi có PV 90.800đ/saver, bằng 41% PV doanh thu. Kể cả khi tỷ lệ ngừng về 0, tier vẫn không hoàn được chi phí | Cao | Quyết định D1: MVP chỉ dùng ưu đãi phi tiền mặt. Tier tiền mặt (30k ở kỳ 12, giảm phí 0,1 điểm) chỉ là phương án thử | Trần CAC 60 tháng tăng từ 36.700đ lên 127.500đ |
| 5 | **Phí VA trên mỗi kỳ góp** là chi phí biến đổi lớn nhất | Giá niêm yết VPBank 3.000đ + VAT (S10). Miễn phí thì trần CAC lên 199.000đ. Trên 6.191đ thì TK ngủ không còn đáng tiếp cận | Cao | Thêm vào Cổng 0: mục tiêu 0đ (ngân hàng đối tác giữ CASA nên có lý do miễn), chấp nhận tối đa giá niêm yết, dừng nếu >6.191đ | Là đòn bẩy rẻ nhất; Board phải giao việc này ngay |
| 6 | **Pilot 20.000 TK thiếu lực thống kê** cho phép thử tier | Mỗi nhánh có 133 saver, chỉ phát hiện được chênh lệch ≥14,8 điểm ở tỷ lệ đạt 6 kỳ; R2 đặt mục tiêu +10 điểm | Trung bình | Đề xuất **45.000 TK** (3 nhánh), phát hiện được 9,9 điểm. Chi phí tiếp cận 39 triệu. Khoảng tin cậy ghi danh 1,84–2,16%, đủ tách ngưỡng 1,0% và 1,5%. Phép thử ở mốc 12 kỳ (cần +8,8 điểm) chạy tiếp bằng nhóm đối chứng trong Phase 2 | `payday_pilot_power.csv` |
| 7 | **Kênh chủ lao động lỗ trên từng saver** ở giả định base | CAC 250.000đ (15 triệu/DN ÷ 300 người × 20%), cao hơn trần CAC 127.500đ | Trung bình | Cổng tháng 24: tiếp tục nếu tỷ lệ tham gia ≥39%, dừng kênh nếu <20%. Tham chiếu: 78% tham gia khi có chuyên viên mời gặp trực tiếp (Thaler & Benartzi, 2004) | Phase 3 phải thử mô hình HR có tư vấn trực tiếp, không chỉ gửi link |
| 8 | **Chưa có stress test** | — | Trung bình | Thêm engine theo lịch thời gian; không có cú sốc thì khớp tuyệt đối engine cũ (test). Kết quả ở `payday_stress.csv`: thị trường giảm năm 2 làm TK ≥10 triệu tháng 36 giảm 12%; ngày lương lỗi tháng 9 giảm 8%; cả hai giảm 18%. Tiền tháng 60 chỉ đổi −0,2 đến −0,5 tỷ | Rủi ro lớn là **KPI và uy tín, không phải tiền**: mỗi saver gần như hòa vốn trong 5 năm, mất saver thì mất cả doanh thu lẫn chi phí |
| 9 | **"Zero-fee" dễ hiểu là không tốn gì** | Phí quản lý quỹ 0,8–1,95%/năm nằm sẵn trong NAV (S22–S25); lãi Trứng Vàng chịu thuế 5% (S18) | Trung bình | Lời trên slide: "no platform fee; fund fees as published by each manager" | Tránh lặp lại lỗi trust của đợt thưởng 2025 |
| 10 | **Không được nói "lãi cao nhất"** | Khách có thể tự mua trái phiếu Agribank khoảng 7,9%, từ 100.000đ, kỳ hạn 10 năm (S29). Trứng Vàng 12 tháng trả 7,6% trước thuế; coupon chịu thuế 5%, giao dịch bán chịu 0,1% (S18). Lãi tiền gửi ngân hàng của cá nhân thì không chịu thuế TNCN. Như vậy Trứng Vàng vẫn trên tiền gửi Big4 (5,9%) nhưng chỉ ngang chứng chỉ tiền gửi (7,4%) | Trung bình | Giá trị của Payday là thanh khoản kỳ ngắn + tự động + mục tiêu + minh bạch, không phải lãi cao nhất | Câu trả lời Q&A "sao không gửi ngân hàng" |
| 11 | **Một bằng chứng tôi định dùng là sai phạm vi** | Định dùng AMFI để nói "thị trường giảm thì dừng SIP". Bài nguồn quy lý do cho thu tiền chậm, không phải thị trường | Thấp | Bỏ. Chỉ giữ mốc khoảng 5%/tháng | — |
| 12 | **Thiếu bằng chứng cho nhắc nhở ngày lương** | Karlan et al. (2016): tin nhắc giúp đạt mục tiêu tiết kiệm nhiều hơn, tốt nhất khi gắn với mục tiêu cụ thể (S31) | — | Đưa vào thiết kế tier phi tiền mặt (D1) | Đòn bẩy giữ chân gần như không tốn tiền |
| 13 | **Khung 60 tháng cắt đuôi**: saver vào muộn trông như lỗ | Tornado: ghi danh nhiều hơn làm tiền tháng 60 xấu đi một chút | Thấp | Thêm chỉ số "chi phí ròng/TK mới ≥10 triệu". Ghi chú trên hình tornado | Ghi danh nhiều hơn làm chỉ số này tốt lên rõ (0,68 so với 1,29 triệu) |

---

## 2. Đánh giá các quyết định

Bộ tiêu chí dùng cho mọi quyết định:
- (a) bằng chứng ủng hộ;
- (b) kinh tế học, đo bằng mô hình;
- (c) rủi ro trust, pháp lý, vận hành;
- (d) mức phù hợp với rubric (25 + 30 điểm);
- (e) có kiểm chứng được bằng pilot không.

### D1. Tier (phần thưởng cho sự bền bỉ)

| Phương án | Chi phí PV/saver | % doanh thu | Trần CAC 60 tháng | Tự trả được không |
|---|---:|---:|---:|---|
| Tier R2 thu nhỏ (quà 10/20/50k, giảm phí 0,1 điểm, +0,2 điểm lãi) | 90.800đ | 41% | 36.700đ (thấp hơn CAC 65.000đ) | Không, kể cả khi miễn phí VA |
| Phương án thử (30k ở kỳ 12, giảm phí 0,1 điểm) | 31.400đ | 14% | 96.200đ | Chỉ khi miễn phí VA **và** tỷ lệ đạt 12 kỳ tăng từ 64,5% lên 73,3% (+8,8 điểm) |
| **Phi tiền mặt: chuỗi kỳ góp, bỏ qua 1 tháng/năm, nhắc ngày lương theo mục tiêu, ưu tiên Trứng Vàng mới** | 0đ | 0% | **127.500đ** | Không cần |

**Chọn: phương án phi tiền mặt cho MVP.** Ưu đãi phí, nếu có, do công ty quỹ tài trợ (ví dụ miễn phí bán lại cho saver giữ đủ 12 kỳ). Tier bằng tiền chỉ được bật khi thỏa đủ 2 điều kiện:
- phí VA đã được miễn;
- nhóm đối chứng trong Phase 2 chứng minh được mức +8,8 điểm.

Giữ nguyên nguyên tắc: mọi ưu đãi lãi có trần 50 triệu; bỏ mức 4,3% không điều kiện.

*Lý do:* đây vẫn đúng tinh thần quyết định 1 (thưởng cho tiền đã đầu tư, không thưởng mở TK), chỉ khác là phần do DNSE trả tiền được thay bằng phần không tốn tiền. Cách này có bằng chứng (nhắc nhở: Karlan et al., 2016; cam kết: Ashraf et al., 2006). Nó cũng tránh lặp lại kiểu "thưởng có điều kiện" từng làm hỏng trust năm 2025.

### D2. Danh mục mặc định

| Phương án | Ưu | Nhược |
|---|---|---|
| Thiên trái phiếu, cổ phiếu chỉ cho mục tiêu ≥3 năm (quyết định gốc) | Ít rủi ro trust, dễ giải thích | Chưa nói rõ thanh khoản theo kỳ hạn mục tiêu |
| 60/40 cho mọi người | Lợi suất phân phối quỹ cổ phiếu cao hơn (0,56% so với 0,33%) | Một đợt giảm như ngày 9/3/2026 (VN-Index −115 điểm) có thể sinh review "lừa đảo" |
| **Danh mục theo kỳ hạn mục tiêu (glide path)** | Đúng yêu cầu đánh giá phù hợp (TT 121/2020 Điều 24); khớp thanh khoản | Phức tạp hơn một chút |

**Chọn: theo kỳ hạn mục tiêu**, là bản chặt hơn của quyết định gốc:
- dưới 1 năm: 100% Trứng Vàng kỳ 1–6 tháng;
- 1–3 năm: Trứng Vàng + quỹ trái phiếu;
- từ 3 năm: tối đa 40% quỹ cổ phiếu/ETF, giảm dần khi gần đến mục tiêu.

Quy tắc mới: **không xếp sản phẩm có phí rút trước hạn rơi vào trong kỳ hạn mục tiêu**. Ví dụ quỹ trái phiếu thu 1–2% nếu bán trong 3–12 tháng (S23, S24); Trứng Vàng bán trước hạn chỉ hưởng 2%/năm (S18).

Mô hình giữ cơ cấu 45/35/10/10 (nếu một nửa số dư thuộc mục tiêu ≥3 năm). Kinh tế học gần như không đổi theo cơ cấu, vì biên Trứng Vàng (0,6%) xấp xỉ biên quỹ cổ phiếu (0,56%).

### D3. KPI

**Chọn: giữ North Star = số TK có tài sản ròng ≥10 triệu** (DNSE tự công bố, nên giám khảo kiểm được và nối liền với Round 2), horizon 24–36 tháng. Mục tiêu lấy từ mô hình, kèm khoảng:

| Mốc | Downside | **Base (mục tiêu)** | Upside |
|---|---:|---:|---:|
| Tháng 18 | 92 | 2.168 | 17.423 |
| Tháng 24 | 1.140 | **7.714** | 34.780 |
| Tháng 36 | 2.911 | **14.871** (27.100 → khoảng 42.000, +55%) | 51.445 |

Thêm hai KPI đi kèm:
- **tiền mới ròng** (giá trị);
- **chi phí ròng/TK mới ≥10 triệu** (hiệu quả, dùng ở cổng).

Bỏ hẳn mốc 85.000 sau 18 tháng. Mô hình cho thấy mốc 18 tháng chỉ khoảng 2.200, vì phải góp 11 kỳ liền mới vượt 10 triệu. Đây là một ý cho slide "What changed".

*Không chọn* "funded savers" hay "số dư" làm North Star. Đó là số nội bộ, bên ngoài không kiểm được; dùng làm chỉ số dẫn dắt thì hợp hơn.

### D4. Đề nghị với Board

**Chọn: chỉ duyệt Phase 0–1, tổng 6,6 tỷ** (5,7 tỷ + dự phòng 15%; build 4,2 tỷ, vận hành và marketing tháng 4–6 là 1,5 tỷ). Hai điểm sửa so với quyết định gốc:
1. **Pilot 45.000 TK** (3 nhánh, mỗi nhánh 15.000) thay vì 20.000. Chi phí thêm chỉ khoảng 20 triệu, nhưng đủ lực thống kê (mục 1, #6).
2. **Đề nghị gồm 5 việc giao ngay**, ngoài khoản tiền:
   - chọn ngân hàng VA với điều kiện miễn phí thu hộ;
   - ký 1–2 công ty quỹ (DNSE có giấy phép đại lý từ 2021 nhưng chưa có tên trong danh sách của SSIAM, Dragon Capital, VCBF);
   - nộp thông báo cho UBCKNN;
   - người có chứng chỉ ký duyệt danh mục mẫu;
   - **chấp thuận ngân sách khoảng 1,3 triệu/TK mới ≥10 triệu** làm thước đo ở các cổng.

*Đã cân nhắc nhưng không chọn:*
- Chỉ duyệt Phase 0 (4,2 tỷ): chậm thêm một vòng quyết định, trong khi chi phí pilot rất nhỏ.
- Duyệt cả chương trình 36 tháng: không có cơ sở khi NPV base âm.

### D5. Định vị

Đã rà hơn 20 sản phẩm của CTCK, ngân hàng và fintech (S33–S36; bảng đầy đủ để đưa vào appendix C). Kết quả làm **hẹp lại** quyết định gốc:

| Thành phần khác biệt (quyết định gốc) | Còn là khác biệt? | Bằng chứng |
|---|---|---|
| Nhiều lớp tài sản trong một kế hoạch | **Chỉ còn đúng ở dạng hẹp**. Đã có kế hoạch trộn nhiều quỹ: VNDIRECT Tích sản hưu trí (quỹ trái phiếu/cổ phiếu 80/20, từ 1 triệu), TCBS TCWealth (danh mục từ các quỹ trên Fundmart). Chưa thấy kế hoạch nào gộp **trái phiếu ngân hàng niêm yết + quỹ + ETF** | S34, S33, S36 |
| Tư vấn theo mục tiêu, khách xác nhận | **Không còn**. TCWealth (từ 4/2026, hơn 20.000–40.000 người dùng), VPBankS "Tích sản cổ phiếu" (khảo sát rủi ro → mục tiêu → danh mục mẫu, khách tự xác nhận lệnh) | S33, S36 |
| Thưởng cho sự bền bỉ | **Không còn**. KBSV thưởng 50.000đ/tháng cho lệnh định kỳ; Finhay × DFVN tặng quà khi góp 3 kỳ liền. Theo D1, MVP của Payday cũng không dùng thưởng tiền | S35 |
| Minh bạch có số đo công bố (tỷ lệ chuyển tiền thành công, thời gian rút trung vị) | **Còn**: chưa ai công bố | Rà của agent |
| Không phí nền tảng | **Không còn**: app TCBS cũng zero-fee | S36 |

**Chọn: định vị "không phải người đầu tiên, nhưng hợp nhất với tệp khách của DNSE".** Bỏ hẳn từ "the only". Câu định vị đề xuất:

> *"Among 20 Vietnamese brokers, banks and fintech apps we reviewed (October 2026), several offer goal-based or multi-fund plans. None we found puts listed bank bonds, bond and equity funds and an ETF into one customer-confirmed monthly plan from VND 500,000, and none publishes its transfer-success and withdrawal-time figures. Payday brings that plan to the 1.5 million accounts DNSE has already opened."*

Lý do chọn:
- Rubric thưởng việc "justifies retained or revised choices", không đòi hỏi độc nhất.
- Giám khảo nhiều khả năng biết TCWealth và VSI; nói "duy nhất" sẽ mất điểm khi bị hỏi.
- Lợi thế bền nhất của DNSE không nằm ở tính năng, mà ở **chi phí tiếp cận gần bằng 0** tới 1,4 triệu TK đã eKYC, và ở **cam kết minh bạch có số đo**. Cam kết này trả lời đúng điểm yếu trust và reliability mà dữ liệu đã chỉ ra.

Kèm theo:
- Slide 10 thêm VNDIRECT Tích sản và TCBS TCWealth vào bảng đối thủ (hiện mới có VSI, eSIP, VCB SIP, VPBank, MoMo).
- Sửa lời: "no platform fee" thay cho "zero-fee"; giá trị nằm ở thanh khoản + tự động + mục tiêu + số đo minh bạch, không phải lãi cao nhất (mục 1, #9–#10).
- Phụ thuộc mới phải ghi rõ: DNSE **chưa phân phối quỹ mở** trên Entrade X, nên phần quỹ của Payday cần hợp đồng đại lý ở Phase 0. Nếu chậm, MVP chạy trước với Trứng Vàng (trái phiếu ngân hàng) + ETF. Kế hoạch 2026 của DNSE muốn mở rộng Trứng Vàng sang chứng chỉ quỹ và chứng chỉ tiền gửi (S30), nên Payday có thể trình bày như bước tiếp theo của chính kế hoạch này.

### D6. Cách trình bày business case

| Phương án | Đánh giá |
|---|---|
| (a) Trình bày Payday như nguồn lợi nhuận | Sai với số liệu. CFO hỏi hai câu là lộ |
| (b) Nâng giả định cho base dương (đội gọn, miễn phí VA, lợi suất upside…) | Vẫn chưa đủ: gộp cả bốn đòn bẩy vẫn còn −8,2 tỷ ở tháng 60. Lại mất điểm "nêu rõ giả định" |
| **(c) Quyền chọn có trần lỗ + ngân sách cho mỗi TK có tiền** | Trung thực, có số, khớp rubric 30 điểm. Cổng biến giá trị chiến lược thành một con số Board kiểm được |

**Chọn (c).** Thông điệp cho CFO:
- "Payday không phải doanh nghiệp thu phí. Nó mua tài khoản có tiền với giá khoảng 1,3 triệu mỗi tài khoản (base)."
- "Board chỉ đặt cược 6,6 tỷ, và dừng được ở tháng 6."
- "Kịch bản tốt hoàn vốn ở tháng 44."
- "Ba việc giúp đi về phía kịch bản tốt: miễn phí VA, đội gọn (tái dùng thành phần sẵn có), đàm phán biên quỹ và trái phiếu."

Giá trị gián tiếp trình bày riêng: số dư bằng 18% tiền NĐT tại DNSE; cost proxy/TK ≥10 triệu giảm từ 7,3 xuống 4,7 triệu.

### D7. Lõi trái phiếu của Payday

| Phương án | Kinh tế học (tiền lũy kế 60 tháng) | Rủi ro |
|---|---|---|
| Dùng cả trái phiếu DNSE (biên khoảng 1,2 điểm) | −28,1 tỷ (tốt hơn base khoảng 4 tỷ trong 5 năm) | Xung đột lợi ích trong sản phẩm có tư vấn; tiền tiết kiệm của khách phụ thuộc rủi ro tín dụng của chính DNSE; DNSE từng bị phạt (8/2026), và chính Trứng Vàng từng bị dừng mở mới theo yêu cầu cơ quan quản lý (25/12/2023, S32) |
| **Chỉ trái phiếu do ngân hàng phát hành** (Agribank, BVBank; Vietcombank, VietinBank, BIDV theo kế hoạch hợp tác 2026) | −32,0 tỷ (base) | Thấp; đúng nguyên tắc ở `plan_tech.md` §3.4 |
| Cho khách tự chọn trái phiếu DNSE ngoài kế hoạch, ghi rõ người phát hành | Như base | Trung bình |

**Chọn: chỉ trái phiếu do ngân hàng phát hành trong danh mục mặc định.** Cái giá khoảng 4 tỷ trong 5 năm nhỏ so với rủi ro: sản phẩm được dựng để sửa trust lại bán nợ của chính DNSE cho người mới tiết kiệm. Trên slide nói thẳng: *"We give up about VND 4 billion over five years to keep DNSE's own bonds out of the default plan."*

---

## 3. Kết quả mô hình sau khi sửa

| | Downside | **Base** | Upside |
|---|---:|---:|---:|
| Lợi suất ròng | 0,25% | 0,44% | 0,68% |
| Vốn Phase 0–1 (kèm dự phòng) | 8,7 tỷ | **6,6 tỷ** | 4,8 tỷ |
| TK mới ≥10 triệu, tháng 24 / 36 | 1.140 / 2.911 | 7.714 / 14.871 | 34.780 / 51.445 |
| Số dư tháng 36 | 71 tỷ | 352 tỷ | 1.597 tỷ |
| Hòa vốn / hoàn vốn | không / không | **không / không** | tháng 24 / 44 |
| NPV 60 tháng | −35,1 tỷ | −25,0 tỷ | +11,0 tỷ |
| Chi phí ròng/TK mới ≥10 triệu (tháng 60) | 10,02 triệu | **1,29 triệu** | 0 (đã hoàn vốn) |

Đòn bẩy (`payday_levers.csv`), đo bằng chi phí ròng/TK mới ≥10 triệu ở tháng 60:
- đội gọn: 0,85 triệu;
- coi một nửa chi phí đội là đầu tư nền tảng dùng chung: 0,86 triệu;
- miễn phí VA: 1,17 triệu;
- ghi danh upside: 0,68 triệu;
- gộp bốn đòn bẩy: 0,18 triệu, hòa vốn tháng 39.

---

## 4. Còn mở
- Tên thành viên; trong team có ai vẽ Figma không.
- Kiểm nốt các nguồn chỉ do agent tìm, trước khi trích lên slide (`sources_round3.csv`, cột `checked_by_author`).
- Nếu team muốn giữ quà chứng chỉ quỹ ở các mốc vì lý do truyền thông: chỉ dùng mức rất nhỏ (≤10.000đ), ghi là phép thử, và đo trong nhóm đối chứng.

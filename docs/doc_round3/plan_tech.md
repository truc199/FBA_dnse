# Chiến lược phát triển các sản phẩm công nghệ hiện có của DNSE

*Lập ngày 15/10/2026 cho team KTQT FTUers. Dựa trên report Round 2 đã nộp (Findings 1–6, mục 4.4, Appendix B–D, G), data trong `data/` (tính lại ngày 14–15/10) và tra cứu sản phẩm ngày 14–15/10/2026. File này bổ sung cho `plan_payday.md`: Payday là sản phẩm mới, còn đây là cách đưa các sản phẩm đang có vào cùng một hướng.*

---

## 0. Tóm tắt

**Chiến lược một dòng:** chuyển DNSE từ **trading-first** sang **balance-first** qua 3 bước nối tiếp:

1. **Sửa nền (0–6 tháng):** độ ổn định của app, kiểm soát tuân thủ trong margin, minh bạch.
2. **Làm tiền ở lại (6–12 tháng):** Tài khoản Không Ngủ bật mặc định, Trứng Vàng làm phần lõi an toàn, Payday.
3. **Tăng trưởng trên số dư (12–24 tháng):** margin cho khách đã có tài sản, Ensa bản trả phí, chuyển lãi phái sinh sang tiết kiệm, liên kết ngân hàng qua Open API.

| Sản phẩm | Vai trò hiện tại | Vấn đề chính (bằng chứng) | Chiến lược | Ưu tiên |
|---|---|---|---|:---:|
| Entrade X (app lõi) | Cỗ máy thu hút khách | Reliability chiếm 58,8% (Play) và 75% (iOS) review tiêu cực năm 2026, cao nhất 3 app; môi giới lỗ 16 quý | **Ổn định và minh bạch trước; kiếm tiền từ số dư, không từ phí giao dịch** | 1 |
| Margin Deal / Margin X | Nguồn lãi chính (40% doanh thu H1/2026) | Dư nợ nhỏ (1,39% ngành); nhiều vi phạm kiểm soát (phạt 08/2026); chi phí vốn tăng lên 6,5% | **Tăng trưởng có kiểm soát, sinh lời, dựa trên khách có tài sản** | 1 |
| Tài khoản Không Ngủ | Sinh lời trên tiền nhàn rỗi | Mới 0,8% TK đăng ký; lãi cơ bản 1,8% thấp với số dư nhỏ | **Bật mặc định; thành "bến đỗ" của mọi đồng tiền vào DNSE** | 2 |
| Trứng Vàng | Trái phiếu kỳ hạn từ 1 triệu | 1.037 khách hoạt động; lãi có thể thấp hơn tiền gửi | **Thành lõi an toàn của Payday** | 2 |
| Ensa + Ý tưởng đầu tư | Tư vấn bằng AI | Thiên về gợi ý mã cổ phiếu; chưa rõ trách nhiệm pháp lý khi AI tư vấn | **Chuyển thành huấn luyện viên mục tiêu và công cụ đánh giá phù hợp** | 2 |
| Future X (phái sinh) | Thị phần #2 (25,38%) | Tạo thị phần nhưng không tạo số dư; bị buộc dừng 3 dịch vụ ứng trước | **Khai thác có kiểm soát, giảm rủi ro; nối lãi giao dịch với số dư** | 3 |
| Lightspeed API | Giao dịch thuật toán | Ngách nhỏ | **Giữ làm ngách chuyên nghiệp, có thu phí** | 4 |
| Kết nối ZaloPay | Kênh nạp tiền và phân phối | Chưa được khai thác cho tiết kiệm | **Kênh nạp tiền thứ hai cho Payday; thử round-up** | 3 |

---

## 1. Bối cảnh từ report Round 2 quyết định chiến lược

- **Tài khoản không đi cùng tiền:** 12,3% số TK nhưng chỉ 2,3% tiền NĐT, 1,4% dư nợ, 0,6% LNTT ngành. Chỉ 1,8% TK có tài sản ròng ≥10 triệu.
- **Giao dịch miễn phí đang lỗ:** doanh thu môi giới thấp hơn chi phí trực tiếp 16 quý liên tiếp (−190,3 tỷ). Năm 2025: doanh thu 404,0 tỷ so với chi phí 464,9 tỷ.
- **Cho vay đắt vốn:**
  - Chi phí vốn tăng từ 3,6% (giữa 2024) lên 6,5% (Q2/2026).
  - NIM giảm từ 6,2% (2021) xuống 3,5% (H1/2026).
  - Tiền gửi và trái phiếu cầm cố chiếm 37,6% tài sản, so với 4–9% ở các đối thủ.
  - Dư nợ/vốn chủ mới 116%, còn xa trần 200%. Nghĩa là **DNSE không thiếu vốn để cho vay, mà thiếu khách có tài sản để vay**.
- **Nền tảng là chi phí cố định:** cost proxy 197,5 tỷ (2025), phần mềm theo nguyên giá 168,5 tỷ. Chi phí này tính ra 7,3 triệu cho mỗi TK có ≥10 triệu.
- **Tuân thủ:** QĐ 461/QĐ-XPHC ngày 17/08/2026 phạt 802,5 triệu đồng, gồm:
  - 275 triệu vì triển khai 3 dịch vụ hỗ trợ phái sinh mà không báo cáo UBCKNN; bị buộc dừng cả 3;
  - cho vay ký quỹ và ứng trước cho người nội bộ và người liên quan;
  - cho đặt lệnh mua khi tài khoản chưa đủ tiền;
  - giao dịch ký quỹ vượt sức mua;
  - cho vay trên chứng khoán không đủ điều kiện.

  Trước đó, năm 2024 DNSE bị phạt 125 triệu vì cho vay trên mã đã bị loại khỏi danh sách được cho vay ký quỹ.

---

## 2. Khung đánh giá

Mỗi sản phẩm được đánh giá theo hai trục:

1. **Vai trò trong vòng đời khách hàng:** Thu hút → Kích hoạt → **Nạp tiền** → Tăng trưởng → Giữ chân. Khâu đang gãy là "Nạp tiền".
2. **Tác động lên số dư và lợi nhuận** so với **rủi ro pháp lý và độ khó triển khai**.

Mỗi mục bên dưới gồm: hiện trạng → điểm mạnh → điểm yếu → liên hệ với funding gap → chiến lược → sáng kiến → KPI → ràng buộc.

---

## 3. Từng sản phẩm

### 3.1 Entrade X: app giao dịch lõi

**Hiện trạng:**
- Miễn phí giao dịch cổ phiếu trọn đời; nạp rút miễn phí 24/7.
- 518.514 TK mới năm 2025 (20,1% thị trường); 1,7 triệu TK giữa 2026.
- 85.739 TK hoạt động (5,7%, tháng 12/2025).
- Năm 2026 app iOS chuyển từ bản 2.113.x lên 3.x.

**Điểm mạnh:** cỗ máy thu hút khách hiệu quả nhất ngành; thương hiệu mạnh với người trẻ (có bảng giá dành cho Gen Z); mô hình không chi nhánh.

**Điểm yếu (bằng chứng):**
- **Reliability năm 2026:** chiếm 58,8% review tiêu cực trên Google Play (n=34) và 75% trên iOS (n=24), cao hơn VPS (43,8% / 50,5%) và FPTS (33,3% / 45,5%).
  - Đỉnh rơi vào **tháng 3/2026**, với 7 review tiêu cực trên iOS ở bản 2.113.28 (6 review nói về reliability).
  - Ngoài đỉnh này, reliability vẫn rải đều các tháng.
- **Onboarding** (mở TK, eKYC, OTP): 21,2% review tiêu cực (cả giai đoạn).
- **Di sản trust:** điều khoản thưởng, phí đóng TK 100.000đ. Đỉnh rơi vào H1/2025, đã giảm nhưng vẫn cao hơn đối thủ.
- **Kinh tế học của giao dịch miễn phí:** môi giới lỗ 16 quý.

**Liên hệ với funding gap:** app không ổn định làm hỏng đúng những khoảnh khắc quyết định việc nạp tiền: lần nạp đầu, ngày lương, lúc rút tiền. Payday sẽ thất bại nếu nền này không vững.

**Chiến lược:** *Ổn định và minh bạch trước; kiếm tiền từ số dư, không từ phí giao dịch.*

**Sáng kiến:**
1. **Chương trình reliability (SRE)**
   - Đặt SLO cho: tỷ lệ phiên không crash, tỷ lệ đăng nhập thành công, độ trễ xác nhận lệnh (p95/p99), thời gian ghi có khi nạp tiền.
   - Áp dụng error budget; phát hành theo từng đợt kèm feature flag và rollback nhanh.
   - Công bố trang trạng thái hệ thống và báo cáo sau mỗi sự cố.
2. **Điều tra sự cố tháng 3/2026** (bản 2.113.28): tìm nguyên nhân gốc và cách phòng ngừa. Từ nay theo dõi complaint theo **phiên bản app** (bộ kéo review Google Play cần lưu thêm trường phiên bản, xem `review_round2.md` K14).
3. **Onboarding:** NFC chip CCCD và thử đăng nhập bằng VNeID (report đã đề xuất); đường dự phòng khi OTP lỗi; đo tỷ lệ rơi ở từng bước.
4. **Dòng tiền vào/ra:**
   - **VA mang tên từng khách** để ghi có tức thì, khắc phục complaint "tiền đã trừ ở ngân hàng nhưng chưa về TK" (Table D3).
   - Công bố cam kết thời gian rút tiền.
   - Cho đóng TK ngay trong app, **miễn phí**.
5. **Hai chế độ màn hình chính:** *Trader* và *Saver* (gắn với tab Payday). Mỗi nhóm khách thấy đúng thứ họ cần.
6. **Zero-fee:**
   - **Giữ cho cổ phiếu cơ sở**: đây là lời hứa thương hiệu, và report đã chấm phương án "thu lại phí" điểm thấp.
   - **Bóc tách chi phí môi giới trực tiếp** (464,9 tỷ năm 2025) từ thuyết minh BCTC gốc: phí trả Sở/VSDC, hoa hồng đối tác, chi phí bán hàng… để tìm khoản nào cắt được.
   - Kiếm tiền bằng gói **trả phí tùy chọn** (dữ liệu nâng cao, tư vấn AI nâng cao; báo chí cho biết chính DNSE đã có kế hoạch thu phí sản phẩm tư vấn nâng cao), chứ không bằng phí giao dịch.
   - Lưu ý: các gói Margin X hiện thu phí 0,045%/giao dịch, nên "zero-fee" chỉ áp cho giao dịch tiền mặt.

**KPI:** tỷ trọng reliability trong review tiêu cực thấp hơn mức của VPS; điểm App Store tăng (DNSE 2,25 giai đoạn 2025–2026); tỷ lệ hoàn tất onboarding; thời gian từ mở TK đến lần nạp đầu; tỷ lệ phiên không crash (mục tiêu do đội kỹ thuật đặt theo số đo hiện tại).

**Ràng buộc:** quy định sinh trắc học (QĐ 2345: xác thực sinh trắc cho giao dịch chuyển tiền >10 triệu/lần hoặc >20 triệu/ngày; TT 17/2024) làm thêm bước khi nạp và rút. Cần thiết kế luồng để khách hiểu vì sao phải làm.

---

### 3.2 Margin Deal / Margin X: cho vay theo từng deal

**Hiện trạng (trang sản phẩm 10/2026):**
- Quản lý vay theo từng deal: có giá hòa vốn đã gồm phí, thuế, lãi; trả nợ trước hạn từng deal.
- Lãi thông thường 12,5%/năm.
- Gói ROCKET X: **5,99% hoặc 9,99% trong 30 ngày đầu**; ROCKET miễn lãi 3, 5 hoặc 10 ngày; gói tự đề xuất FIN X.
- Tỷ lệ vay 10–50%; phí 0,045%; kỳ hạn 90 ngày. Ứng sức mua theo deal được tính là khoản vay margin.
- Dư nợ **6.303 tỷ** (30/06/2026), tức 1,39% ngành. Dư nợ/TK chỉ 3,7 triệu, so với VPS 20,2 triệu, VPBankS 29,4 triệu, TCBS 42,9 triệu.

**Điểm mạnh:** sản phẩm sáng tạo (minh bạch theo deal), được trader ưa chuộng; lợi suất gộp khoảng 10–12%; còn khoảng **4,6 nghìn tỷ** dư địa dưới trần 200% vốn chủ.

**Điểm yếu:**
- Thiếu khách có tài sản để làm tài sản đảm bảo, nên sổ cho vay nhỏ.
- **Lãi khuyến mại 5,99% thấp hơn chi phí vốn 6,5%** (Q2/2026), tức đang bán lỗ để kéo khách.
- Chi phí vốn tăng, NIM giảm.
- Cấu trúc vốn dựa vào vay ngắn hạn cầm cố tiền gửi.
- **Kiểm soát lặp lại sai phạm** (2024 và 08/2026: cho người nội bộ vay, vượt sức mua, cho vay mã không đủ điều kiện, lệnh mua thiếu tiền).

**Liên hệ với funding gap:** margin chỉ tăng được khi khách có tài sản. Report kết luận đúng: "*margin demand follows customer assets*". Vì vậy margin là **kết quả** của chiến lược số dư chứ không phải đòn bẩy chính.

**Chiến lược:** *Tăng trưởng có kiểm soát và sinh lời, dựa trên khách đã có tài sản.*

**Sáng kiến:**
1. **Tuân thủ ngay trong thiết kế** (trả lời thẳng vụ phạt):
   - Kiểm tra sức mua theo thời gian thực trước khi khớp lệnh.
   - Đồng bộ danh sách mã được cho vay ký quỹ hằng ngày từ Sở, tự động chặn mã bị loại.
   - **Danh sách người nội bộ và người liên quan** (lấy từ sổ cổ đông, danh sách nhân viên, các quan hệ đã khai báo) được kiểm tra tự động trước **mọi** lần giải ngân margin hoặc ứng trước.
   - Ngoại lệ phải có hai người duyệt; lưu vết đầy đủ; báo cáo kiểm soát hằng tháng cho ủy ban rủi ro.
2. **Kỷ luật giá:**
   - Không chào lãi thấp hơn chi phí vốn, trừ gói có trần thời gian và hạn mức, chỉ dành cho khách **mới nạp tiền**.
   - Định giá theo rủi ro (hành vi, chất lượng tài sản đảm bảo). Mốc tham chiếu: TCBS cho biết đang dùng AI để tinh chỉnh lãi margin theo khối lượng giao dịch, mức gắn bó và danh mục.
3. **Nguồn vốn:**
   - Dùng chương trình trái phiếu **3.500 tỷ** mà ĐHĐCĐ 2026 đã duyệt (2.500 tỷ không chuyển đổi + 1.000 tỷ chuyển đổi) để kéo dài kỳ hạn vốn.
   - Giảm phụ thuộc vào cấu trúc tiền gửi cầm cố; khớp kỳ hạn tài sản và nợ (ALM).
4. **Tăng trưởng đúng nhóm:**
   - Trước hết là khách hoạt động đã có tiền (E1).
   - Khi Payday đủ lớn, cho phép **ETF làm tài sản đảm bảo theo hình thức opt-in**, có kiểm tra phù hợp (phase 3 của Payday).
   - **Không** dùng tiền tiết kiệm theo mục tiêu để cho vay.
5. **Công cụ rủi ro cho khách:** mô phỏng gọi ký quỹ, cảnh báo sớm, hiển thị giá hòa vốn (đã có).

**KPI:** dư nợ; NIM; chi phí vốn; **tỷ trọng dư nợ ở khách có ≥10 triệu**; **số vi phạm = 0**; số lần bán giải chấp; tỷ lệ complaint về margin.

**Ràng buộc:**
- Thông tư 121/2020 Điều 27: CTCK chỉ được cho vay margin và một số mục đích được quy định.
- Chứng chỉ quỹ mở không niêm yết nên không thể làm tài sản đảm bảo margin.
- Trần dư nợ 200% vốn chủ.

---

### 3.3 Tài khoản Không Ngủ: tiền nhàn rỗi sinh lời

**Hiện trạng (trang sản phẩm):**
- Ra mắt 06/2025.
- Lãi cơ bản cố định **1,8%/năm**; cộng thêm tối đa 1,5% theo bậc số dư (dưới 1 triệu không được cộng, bậc cao nhất từ 10 tỷ) và tối đa 1,0% theo giá trị giao dịch hoặc lưu ký. Mức cao nhất 4,3%.
- Lãi tính theo từng giây; tiền dùng được ngay.
- **12.100 TK đăng ký** (12/2025, tức 0,8%). 3 review nhắc đến, đều tích cực.
- Khách số dư nhỏ thường nhận khoảng 2,1–2,3%.

**Đối thủ:** TCBS iPower 4,5% cơ bản, cao nhất 9,0% (bảng DNSE tự tổng hợp); MoMo Túi Thần Tài đến 6,1%; VIB SmartDepo đến 4,3%; các tài khoản sinh lời tự động của ngân hàng 3,5–4,3%.

**Điểm mạnh:** trải nghiệm "thấy lãi chạy từng giây" được khách khen; thanh khoản tức thì; khách không phải làm gì thêm.

**Điểm yếu:**
- **Phải đăng ký mới có** (opt-in), nên chỉ 0,8% TK dùng.
- Bậc lãi thưởng cho khách số dư rất lớn và trader giao dịch nhiều. Như vậy là **ngược** với mục tiêu kéo tiền của số đông.
- Lãi cơ bản cho số dư nhỏ kém đối thủ.
- **Cơ chế pháp lý tạo ra lợi suất chưa rõ ràng** với người ngoài: tiền gửi không kỳ hạn tại ngân hàng bị trần 0,5%, vậy 1,8% trở lên đến từ đâu.

**Liên hệ với funding gap:** đây là nơi mọi đồng tiền vào DNSE nên dừng lại trước khi được đầu tư. Bật mặc định là cách áp dụng **đúng** bằng chứng về hiệu ứng mặc định, vì ở đây nó thực sự là mặc định.

**Chiến lược:** *Bật mặc định; thành "bến đỗ" của mọi đồng tiền vào DNSE.*

**Sáng kiến:**
1. **Bật mặc định** (opt-out) cho mọi TK có tiền mặt.
2. **Định giá lại cho số đông:** làm phẳng bậc trong khoảng 1–100 triệu. Chi phí khoảng **19,6 tỷ/năm cho mỗi 1 điểm %** trên 1.960,8 tỷ tiền NĐT (Q2/2026). Nên ưu tiên áp cho **tiền mới** và số dư Payday trước để giới hạn chi phí.
3. **Minh bạch:** dashboard cho thấy tiền đang nằm ở đâu và lợi suất được tạo ra thế nào.
4. **Bến đỗ** cho Payday (1–3 ngày) và cho tính năng chuyển lãi từ phái sinh sang tiết kiệm (§3.6).
5. **Bộ phận tuân thủ viết bản ghi nhớ** về cơ chế pháp lý của lợi suất trước khi mở rộng.

**KPI:** % TK có tính năng bật; số dư tiền mặt bình quân; tiền mới ròng; chi phí trên mỗi điểm lãi; complaint.

---

### 3.4 Trứng Vàng: trái phiếu kỳ hạn từ 1 triệu

**Hiện trạng:**
- Mua trái phiếu niêm yết với lợi suất cố định theo kỳ hạn, từ **1 triệu đồng**. Mã đầu tiên là trái phiếu Agribank (AGRIBANK223001 / VBA122001).
- Lãi từ 4,2% (1 tháng, "Trứng Vẹt") đến 5,3% (kỳ dài hơn, "Trứng Hạc"). Đây là mức trên bài giới thiệu, **chưa rõ ngày**; cần kiểm trong app.
- Từ 10/04/2026: **tự động tái tục gốc và lãi** (bật sẵn, tắt được). Rút trước hạn bị giảm lãi.
- Kế hoạch 2026 hợp tác với Vietcombank, VietinBank, BIDV cho trái phiếu và chứng chỉ quỹ, **chưa xác nhận đã ra mắt**.
- **1.037 khách hoạt động** (12/2025).

**Điểm mạnh:** vé nhỏ; tổ chức phát hành là ngân hàng nên rủi ro tín dụng thấp; tái tục tự động là một **mặc định tốt**; đơn giản; hợp người tiết kiệm.

**Điểm yếu:**
- Nếu mức 4,2–5,3% là hiện hành thì **thấp hơn tiền gửi** (12 tháng Big4 tại quầy 5,9%, chứng chỉ tiền gửi 7,4%, đầu 10/2026).
- Rất ít người dùng; tiền bị khóa theo kỳ hạn; nguồn trái phiếu hạn chế.

**Liên hệ với funding gap:** Trứng Vàng là **lõi an toàn** trả lời câu "sao không gửi ngân hàng?" cho người tiết kiệm mới, nếu giá cạnh tranh và minh bạch.

**Chiến lược:** *Lõi an toàn của mọi danh mục Payday.*

**Sáng kiến:**
1. **Bậc thang kỳ hạn theo mục tiêu** (1/3/6/12 tháng) bên trong Payday; giữ tái tục tự động.
2. **Minh bạch giá:** hiện rõ tổ chức phát hành, lãi coupon, phần chênh lệch DNSE giữ lại, chi phí rút trước hạn.
3. **Nguồn cung:** trái phiếu ngân hàng Big4 theo kế hoạch 2026.
   - **Nguyên tắc:** không đưa trái phiếu do chính DNSE phát hành vào sản phẩm bán lẻ của mình, để tránh xung đột lợi ích.
   - DNSE có phát hành trái phiếu bán lẻ qua kênh khác: mã DSEH2426001, 300 tỷ, phân phối qua VNSC, tối thiểu 1 triệu.
4. **Quy tắc giá cạnh tranh** so với tiền gửi cùng kỳ hạn, **sau thuế**. Cần kiểm thuế TNCN với lãi trái phiếu so với lãi tiền gửi trước khi so sánh trên slide.

**KPI:** khách hoạt động; số dư; tỷ lệ tái tục; tỷ lệ rút trước hạn; biên chênh lệch.

---

### 3.5 Ensa và Ý tưởng đầu tư: tư vấn bằng AI

**Hiện trạng:**
- Ensa là chatbot dùng mô hình ngôn ngữ lớn: tóm tắt thị trường, đánh giá mã, đề xuất ý tưởng đầu tư cá nhân hóa.
- "Ý tưởng đầu tư" chạy trong khuôn khổ dịch vụ tư vấn có giấy phép (điều khoản sản phẩm).
- Theo báo chí, DNSE có kế hoạch thu phí sản phẩm tư vấn nâng cao.
- Khoảng 72.000 người dùng (BCTN 2025, ghi trong `diary.md`).

**Điểm mạnh:** hướng dẫn ở quy mô lớn với chi phí thấp; là điểm khác biệt; nhu cầu có thật (81% nhà đầu tư muốn được tư vấn chuyên nghiệp).

**Điểm yếu:**
- Tập trung **gợi ý mã cổ phiếu**, nên dễ khuyến khích giao dịch dồn dập.
- Chưa rõ **trách nhiệm khi AI tư vấn**; rủi ro mô hình "ảo giác".
- Có thể bị cơ quan quản lý soi kỹ.

**Liên hệ với funding gap:** thiếu hướng dẫn là một lý do khiến người có ý định đầu tư cứ trì hoãn. Ensa có thể chuyển ý định thành kế hoạch cụ thể.

**Chiến lược:** *Từ cỗ máy gợi ý mã thành huấn luyện viên mục tiêu và công cụ đánh giá phù hợp.*

**Sáng kiến:**
1. **Bảng đánh giá phù hợp** theo Thông tư 121/2020 Điều 24: mục tiêu, kỳ hạn, thu nhập, khả năng chịu lỗ.
2. **Danh mục mẫu do người hành nghề có chứng chỉ thiết kế và ký duyệt.** Ensa chỉ thu thập thông tin, giải thích và nhắc nhở.
3. **Rào chắn:**
   - Không gợi ý mã đơn lẻ trong Payday; giới hạn phạm vi trả lời; có tuyên bố miễn trừ.
   - Lưu log hội thoại; chuyển cho người thật khi cần.
   - Có bộ test độ chính xác và red-team định kỳ.
4. **Gói tư vấn trả phí** cho khách đã có tài sản (nguồn doanh thu không phụ thuộc phí giao dịch).

**KPI:** tỷ lệ hoàn tất đánh giá phù hợp; số mục tiêu được tạo; tỷ lệ complaint về tư vấn; tỷ lệ chuyển sang gói trả phí.

---

### 3.6 Future X: phái sinh

**Hiện trạng:**
- Ra mắt 2023, quảng bá là "chi phí thấp nhất", đòn bẩy khoảng 5–7 lần.
- Thị phần môi giới phái sinh **#2, 25,38%** (Q2/2026).
- Ký quỹ phái sinh nằm ở VSDC, **không thành số dư tại DNSE**.
- Tháng 8/2026 bị buộc **dừng 3 dịch vụ hỗ trợ**: ứng lãi vị thế, ứng rút ký quỹ ngoài giờ, ứng trước ký quỹ.

**Điểm mạnh:** thị phần cao; tốc độ; hệ sinh thái giao dịch thuật toán (Lightspeed API).

**Điểm yếu:**
- Góp phần vào khoản lỗ môi giới; tạo thị phần nhưng không tạo số dư.
- Rủi ro pháp lý; mất tính năng sau vụ phạt.
- Khách cá nhân thua lỗ trên phái sinh là rủi ro về hành vi và về trust.

**Liên hệ với funding gap:** report gọi đúng tên: phái sinh "build share, not balances".

**Chiến lược:** *Khai thác có kiểm soát, giảm rủi ro, và nối lãi giao dịch với số dư.*

**Sáng kiến:**
1. **Không mở lại** bất kỳ dịch vụ ứng trước nào khi chưa **báo cáo UBCKNN**, và chỉ mở lại khi kinh tế đơn vị dương.
2. **Kinh tế đơn vị trên mỗi hợp đồng:** phí thu được so với phí Sở, VSDC, bù trừ và chi phí phục vụ. Cân nhắc **bậc giá cho khách chuyên nghiệp** (giao dịch tần suất cao, dùng API).
3. **Bảo vệ nhà đầu tư:** công bố rủi ro rõ ràng, giới hạn lỗ tự đặt, đánh giá phù hợp trước khi dùng đòn bẩy. Việc này giảm complaint và rủi ro hành vi.
4. **"Chuyển lãi về tổ" (profit sweep):** khách tự đặt quy tắc chuyển X% lãi đã chốt sang Tài khoản Không Ngủ, Trứng Vàng hoặc Payday, có xác nhận. Đây là cầu nối từ trader sang số dư **mà không dùng đòn bẩy**. Cần kiểm pháp lý của việc chuyển tiền giữa các tiểu khoản của cùng một khách.

**KPI:** biên đơn vị trên mỗi hợp đồng; thị phần; complaint; % trader bật profit sweep; số dư đến từ sweep.

---

### 3.7 Lightspeed API: giao dịch thuật toán

**Chiến lược:** *Giữ làm ngách chuyên nghiệp, có thu phí và kiểm soát rủi ro.*

**Sáng kiến:** gói thu phí cho người dùng API; kiểm soát rủi ro thuật toán (giới hạn tần suất lệnh, nút dừng khẩn cấp, giám sát). **Không ưu tiên đầu tư thêm**, vì tốc độ gần như không mang lại gì cho người tiết kiệm (report, Table G1).

---

### 3.8 Kết nối ZaloPay

**Hiện trạng:** hợp tác từ 07/2023, ZaloPay hỗ trợ đầu tư chứng khoán.

**Chiến lược:** *Kênh nạp tiền thứ hai cho Payday; thử round-up với người trẻ.*

**Sáng kiến:**
- Ủy quyền nạp tiền định kỳ qua ZaloPay.
- Thử round-up (report ước khoảng 150.000đ/tháng cho mỗi khách, tức khoản nhỏ) như **cửa vào** chứ không phải nguồn số dư chính.
- Marketing chung với ZaloPay tới người dùng trẻ.

**KPI:** số kế hoạch nạp qua ZaloPay; tỷ lệ người dùng round-up chuyển sang góp theo lương.

---

### 3.9 Nền tảng dùng chung: định danh, thanh toán, dữ liệu

- **Định danh:** NFC CCCD, VNeID, tuân thủ sinh trắc học (QĐ 2345, TT 17/2024).
- **Thanh toán:** VA cho từng khách; ghi có tức thì 24/7; đối soát tự động.
- **Open API:** ngân hàng phải tuân thủ Thông tư 64/2024 **trước 01/03/2027**; sự đồng ý truy vấn thông tin của khách có hiệu lực tối đa 180 ngày. **Chọn ngân hàng giữ VA làm đối tác đầu tiên** (CASA vẫn ở ngân hàng đó, nên họ có lý do hợp tác).
- **Dữ liệu:** theo dõi sự kiện trong app; phân tích theo cohort; **gắn nhãn nguồn của mọi dòng tiền vào** (để đo "tiền mới"); gắn phiên bản app vào telemetry và review.

---

## 4. Ma trận ưu tiên

| Sáng kiến | Tác động lên TK có tiền | Tác động lợi nhuận | Giảm rủi ro pháp lý | Công sức | Thời điểm |
|---|:---:|:---:|:---:|:---:|:---:|
| Reliability (SRE, điều tra sự cố 3/2026) | Cao | Trung bình | Trung bình | Trung bình | 0–6 tháng |
| Tuân thủ trong thiết kế cho margin | Thấp | Trung bình (tránh phạt, tránh dừng dịch vụ) | **Cao** | Trung bình | 0–6 tháng |
| VA tên khách + ghi có tức thì + đóng TK miễn phí | Cao | Thấp | Trung bình | Trung bình | 0–6 tháng |
| Không Ngủ bật mặc định (có trần chi phí) | **Cao** | Âm ngắn hạn (chi phí lãi) | Thấp | Thấp | 0–6 tháng |
| Ensa → huấn luyện viên mục tiêu + đánh giá phù hợp | Trung bình | Trung bình (gói trả phí) | Trung bình | Trung bình | 3–9 tháng |
| Trứng Vàng bậc thang + minh bạch | Trung bình | Trung bình | Thấp | Thấp | 3–9 tháng |
| Payday (pilot → mở rộng) | **Cao** | Âm ngắn hạn, dương dài hạn | Thấp (nếu báo cáo trước) | Cao | 0–12 tháng |
| Profit sweep cho phái sinh | Trung bình | Thấp | Thấp | Thấp | 6–12 tháng |
| Kỷ luật giá margin + định giá theo rủi ro | Thấp | **Cao** | Trung bình | Trung bình | 6–12 tháng |
| Chương trình trái phiếu (vốn dài hạn) | — | Trung bình (chi phí vốn) | Thấp | Thấp | 6–12 tháng |
| Open API, kênh chủ lao động | Cao | Trung bình | Thấp | Cao | 12–24 tháng |
| ETF làm tài sản đảm bảo (opt-in) | Thấp | Trung bình | Trung bình (cần chấp thuận) | Trung bình | 12–24 tháng |
| Lightspeed bậc chuyên nghiệp | Thấp | Thấp | Thấp | Thấp | 12–24 tháng |

---

## 5. Lộ trình 24 tháng

| Giai đoạn | Chủ đề | Sáng kiến chính | Cổng |
|---|---|---|---|
| **0–6 tháng: Sửa nền** | Ổn định, tuân thủ, minh bạch | SRE + SLO; điều tra sự cố 3/2026; tuân thủ trong thiết kế cho margin; VA và ghi có tức thì; đóng TK miễn phí trong app; Không Ngủ bật mặc định (có trần chi phí); Ensa đánh giá phù hợp; MVP và pilot Payday | Reliability đạt SLO; vi phạm = 0; pilot Payday qua ngưỡng |
| **6–12 tháng: Làm tiền ở lại** | Số dư | Mở rộng Payday trong tệp; Trứng Vàng bậc thang; profit sweep; định giá lại Không Ngủ cho số đông (nếu có lời); kỷ luật giá margin; phát hành trái phiếu | Funded savers và số dư theo kế hoạch; CAC dưới trần |
| **12–24 tháng: Tăng trưởng trên số dư** | Margin và tư vấn trên nền tài sản | Liên kết ngân hàng qua Open API (trích % lương); kênh chủ lao động; ETF làm tài sản đảm bảo (opt-in); gói tư vấn trả phí; Lightspeed bậc chuyên nghiệp; mở lại dịch vụ phái sinh đã dừng nếu đã báo cáo và kinh tế đơn vị dương | TK ≥10 triệu tăng theo kế hoạch; NIM ổn định; doanh thu không đến từ phí giao dịch tăng |

---

## 6. Hạ tầng dùng chung với Payday (xây một lần, dùng nhiều chỗ)

| Thành phần | Dùng cho |
|---|---|
| VA mang tên từng khách | Payday, nạp tiền thường, giảm complaint ghi có |
| Scheduler cho chuyển tiền và lệnh định kỳ | Payday, profit sweep, tái tục Trứng Vàng |
| Công cụ đánh giá phù hợp (Ensa) | Payday, margin, phái sinh có đòn bẩy, gói tư vấn |
| Dashboard minh bạch (tiền tách biệt, lãi, trạng thái rút) | Mọi sản phẩm giữ tiền |
| Gắn nhãn dòng tiền và phân tích cohort | KPI "tiền mới", đánh giá mọi chiến dịch |
| SRE: SLO, phát hành theo đợt, theo dõi theo phiên bản | Toàn app |
| Bộ kiểm soát tuân thủ (người nội bộ, mã ký quỹ, sức mua) | Margin, ứng trước, mọi dịch vụ mới |

---

## 7. Bảng KPI cấp công ty (đề xuất)

| Nhóm | KPI | Mốc hiện tại |
|---|---|---|
| Số dư | TK có ≥10 triệu | 27.100 (1,8%, 12/2025) |
| Số dư | Tiền NĐT tại DNSE; tiền mới ròng (đã gắn nhãn) | 1.960,8 tỷ (Q2/2026) |
| Hoạt động | TK sử dụng sản phẩm trong tháng | 85.739 (5,7%, 12/2025) |
| Sản phẩm giữ tiền | Không Ngủ bật; Trứng Vàng hoạt động; Payday funded savers | 12.100; 1.037; 0 |
| Lợi nhuận | LNTT lõi; NIM; chi phí vốn; biên môi giới | 77,7 tỷ (H1/2026); 3,5%; 6,5% (Q2); 83,3% doanh thu/chi phí |
| Chất lượng | Reliability và trust trong review tiêu cực; điểm App Store | 58,8% / 14,7% (Play 2026); 2,25 |
| Tuân thủ | Số vi phạm; số dịch vụ triển khai không báo cáo | Mục tiêu 0 |

---

## 8. Đưa vào bài Round 3A và Round 3B thế nào

- **Round 3A** (15 slide, trọng tâm là Payday): dùng **1 slide** "*From trading-first to balance-first: DNSE's product roadmap*". Có thể gộp với slide roadmap (#13 trong `plan_payday.md`) và trình bày bằng bảng §5. Phần chi tiết đưa vào appendix. Mục đích là cho Board thấy Payday không đứng một mình mà là trục của cả hệ sinh thái, đúng hướng report Round 2 đã nêu ở mục 4.4.
- **Q&A:** khi CTO hỏi về ổn định, dùng §3.1. Khi CFO hỏi về margin và chi phí vốn, dùng §3.2. Khi Head of Product hỏi về Ensa, dùng §3.5.
- **Round 3B (tranh biện tiếng Việt):** các luận điểm dùng được: "zero-fee có bền không", "CTCK độc lập cạnh tranh với CTCK thuộc ngân hàng thế nào", "tuân thủ ngay trong thiết kế sau một vụ phạt", "Open API: cơ hội hay mối đe dọa cho CTCK".

---

## Nguồn

- Report Round 2 đã nộp: `report/FBAR2_2026_KTQT_FTUers.pdf` (Table B1–B3, C1–C3, D1–D3, G1; mục 4.4; Appendix D về hồ sơ xử phạt).
- [Margin X: quản trị gói vay theo từng deal (DNSE)](https://www.dnse.com.vn/san-pham/margin)
- [Ứng sức mua DEAL tự động (hướng dẫn DNSE)](https://hdsd.dnse.com.vn/san-pham-dich-vu/sp-giao-dich-ky-quy-theo-deal/ung-suc-mua/ung-suc-mua-deal-tu-dong)
- [Tài khoản Không Ngủ (DNSE)](https://www.dnse.com.vn/san-pham/tai-khoan-khong-ngu)
- [DNSE giới thiệu sản phẩm "Trứng vàng"](https://kinhtechungkhoan.vn/dnse-gioi-thieu-san-pham-trung-vang-voi-loi-suat-dau-tu-hap-dan-1043755.html)
- [Hướng dẫn DNSE: cập nhật tính năng tháng 4/2026](https://hdsd.dnse.com.vn/cap-nhat-tinh-nang-moi/nam-2026/thang-4-2026)
- [Chứng khoán Vina phân phối thành công trái phiếu DNSE (Finhay)](https://www.finhay.com.vn/khai-man-dau-nam-chung-khoan-vina-phan-phoi-thanh-cong-trai-phieu-dnse)
- [Cuộc đua công nghệ ngành chứng khoán: cách DNSE chuẩn bị cho kỷ nguyên AI (Nhà Đầu Tư)](https://nhadautu.vn/cuoc-dua-cong-nghe-nganh-chung-khoan-cach-dnse-chuan-bi-cho-ky-nguyen-ai-d106830.html)
- [DNSE ra mắt sản phẩm giao dịch chứng khoán phái sinh Future X (Báo Đấu Thầu)](https://baodauthau.vn/dnse-ra-mat-san-pham-giao-dich-chung-khoan-phai-sinh-future-x-post141454.html)
- [DNSE sets profit growth target above 60%, raising VND 3,500 billion through bonds (DNSE IR)](https://ir.dnse.com.vn/en/post/dnse-sets-profit-growth-target-above-60-raising-vnd-3-500-billion-through-bonds-779.htm)
- [DNSE bị phạt 802,5 triệu đồng, phải dừng một số dịch vụ ký quỹ](https://vnbusiness.vn/dnse-bi-phat-8025-trieu-dong-phai-dung-mot-so-dich-vu-ky-quy.html)
- [Thanh tra Chứng khoán Nhà nước chỉ rõ loạt vi phạm tại DNSE](https://thanhtra.com.vn/ket-luan-thanh-tra-E17BD7A25/thanh-tra-chung-khoan-nha-nuoc-chi-ro-loat-vi-pham-tai-cong-ty-co-phan-chung-khoan-dnse-98015d1ed.html)
- [TCBS 2Q2026 Earnings Call (định giá margin bằng AI; phân phối quỹ)](https://www.tcbs.com.vn/wp-content/uploads/2026/07/TCBS_2Q2026-Earnings-Call_VN-1.pdf)
- [Thông tư 64/2024/TT-NHNN (Thư viện Pháp luật)](https://thuvienphapluat.vn/van-ban/Tien-te-Ngan-hang/Thong-tu-64-2024-TT-NHNN-trien-khai-giao-dien-lap-trinh-ung-dung-mo-nganh-Ngan-hang-641360.aspx)
- [Lãi suất đầu tháng 10/2026](https://thitruongtaichinhtiente.vn/lai-suat-dau-thang-10-2026-tiet-kiem-giu-nhip-on-dinh-chung-chi-tien-gui-hut-khach-85944.html)
- [Ngân hàng Nhà nước hỗ trợ xử lý vướng mắc khi xác thực sinh trắc học](https://baolaocai.vn/ngan-hang-nha-nuoc-ho-tro-xu-ly-vuong-mac-trong-su-dung-xac-thuc-bang-sinh-trac-hoc-post385898.html)
- Data nội bộ: `data/dnse_financials.json`, `data/manual/*.csv`, `data/reviews_flagged_*.csv`, `data/reviews_raw_ios_*.csv` (tính lại ngày 14–15/10/2026).

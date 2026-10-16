# Đánh giá phản biện Payday Portfolio: hữu dụng, phù hợp, khác biệt

*Lập ngày 15/10/2026 cho team KTQT FTUers. Căn cứ: thiết kế Payday trong bản nộp Round 2 (mục 4, Appendix F–G), data trong `data/`, và tra cứu sản phẩm đối thủ ngày 14–15/10/2026. Cách làm: thử bác bỏ từng luận điểm trước, chỉ giữ lại những gì vẫn đứng được.*

---

## 0. Kết luận

| Tiêu chí | Điểm (1–5) | Nhận định |
|---|:---:|---|
| Giải đúng vấn đề của DNSE (funding gap) | **4** | Nhắm thẳng khâu đang mất giá trị: mở TK xong nhưng không nạp tiền đều |
| Hữu dụng với người dùng mục tiêu (người đi làm 22–40) | **3** | Nhu cầu kỷ luật, mục tiêu, đơn giản là có thật. Nhưng năm 2026 lợi suất phần an toàn kém tiền gửi, và phần cổ phiếu là rủi ro với người mới |
| Phù hợp với người dùng app trading hiện tại của DNSE | **2** | Tệp hiện tại trẻ, ít vốn, nặng phái sinh, nhiều người mở TK vì thưởng. Không phải chân dung người tiết kiệm theo lương |
| Khác biệt so với thị trường (10/2026) | **2** | *(Hạ điểm ngày 16/10 sau khi tra kỹ.)* Chuyển tiền định kỳ từ ngân hàng đã có từ 2021 (VinaSIP) và có ngay trong app ngân hàng (VCB Digibank, từ 100.000đ/kỳ). Cái mới chỉ là *tổ hợp*: nhiều lớp tài sản + tư vấn theo mục tiêu + thưởng cho sự bền bỉ + minh bạch có số đo, trong app zero-fee. Chi tiết: `competitor_features.md` |
| Khác biệt so với chính danh mục của DNSE | **4** | Lấp đúng chỗ trống: DNSE chưa có kế hoạch đầu tư định kỳ |
| Khả thi pháp lý và kỹ thuật (phase 1) | **3,5** | Dựng từ thành phần có sẵn. Còn thiếu: ai chịu trách nhiệm khi AI tư vấn; reliability năm 2026 là điểm nghẽn |
| Kinh tế đơn vị | **2** | Doanh thu trên mỗi đồng số dư thấp, hoàn vốn chậm, giá trị phải đến từ hiệu ứng gián tiếp |

**Phán quyết:** **giữ Payday làm sản phẩm Round 3A.** Đổi sản phẩm lúc này rủi ro hơn nhiều, và rubric thưởng sự liên tục từ Round 2. Nhưng phải **định vị lại**: không bán Payday là "sản phẩm độc nhất", mà là **lớp xây số dư (balance-building layer) của DNSE**. Lớp này cần 3 điểm khác biệt bảo vệ được (§4.3) và 7 chỉnh sửa thiết kế (§7).

---

## 1. Payday Portfolio trong bản nộp (tóm tắt)

- **Đối tượng:** chủ TK ngủ có lương (E2, khoảng 1,4 triệu TK), sau đó mở rộng sang người đi làm mới (N1, 22–40 tuổi).
- **Cơ chế:**
  1. Ensa thu thập mục tiêu, kỳ hạn, thu nhập, khẩu vị rủi ro (Thông tư 121/2020 Điều 24), rồi đề xuất danh mục Conservative, Balanced hoặc Growth; khách xác nhận.
  2. Khách tạo **một lần** lệnh chuyển tiền định kỳ từ app ngân hàng nhận lương vào **VA mang tên khách** tại ngân hàng đối tác của DNSE (tối thiểu 500.000đ/tháng). ZaloPay là kênh thứ hai.
  3. Tiền chờ 1–3 ngày trong Tài khoản Không Ngủ, sau đó được rót vào lớp tài sản đang thiếu tỷ trọng nhất: quỹ trái phiếu, Trứng Vàng, quỹ cổ phiếu, ETF VN30 (ETF chờ đủ lô 100). Mọi thay đổi phân bổ cần khách xác nhận một chạm.
- **Tier cam kết:**
  - Starter (3 kỳ): +0,3–0,5 điểm lãi tiền nhàn rỗi.
  - Disciplined (6 kỳ): giảm phí quỹ và trái phiếu, đánh giá danh mục nửa năm một lần.
  - Committed (12 kỳ): lãi tiền nhàn rỗi 4,3% không cần điều kiện số dư hay giao dịch, ưu tiên Trứng Vàng kỳ mới.
  - Được bỏ qua 1 tháng/năm. Margin không nằm trong phần thưởng.
- **Trust controls:** bỏ phí đóng TK, bỏ thưởng có điều kiện, toàn bộ điều khoản trên một màn hình, tạm dừng/bỏ/hủy bằng một chạm, dashboard tiền tách biệt, chuyển tiền thành công ≥99,5% là điều kiện ra mắt, báo UBCKNN trước khi ra mắt.

---

## 2. Độ hữu dụng: giải quyết vấn đề gì, cho ai

### 2.1 Với DNSE: hữu dụng rõ

Vấn đề có số đo rõ ràng: 1,8% TK có từ 10 triệu trở lên, 5,7% TK hoạt động, môi giới lỗ 16 quý, LNTT lõi đi ngang. Payday nhắm đúng khâu "ý định → tiền nạp đều". Phần chẩn đoán trong report (`review_round2.md` §2.1) là nền vững cho lập luận này.

### 2.2 Với người dùng: nhu cầu có thật, có bằng chứng

- 77% nhà đầu tư thấy tự quản lý danh mục là khó, 81% muốn được tư vấn chuyên nghiệp (Nhân Dân 2025; VnEconomy 2025, đã có trong report).
- Findex 2024: trong nhóm 60% giàu nhất, 49,5% nhận lương qua TK nhưng chỉ 53,8% tiết kiệm tại tổ chức tài chính. Tiền lương đã nằm trong TK, chỉ thiếu bước chuyển đều đặn sang đầu tư.
- Cơ chế tự động hóa và cam kết có bằng chứng quốc tế (Thaler & Benartzi 2004; Ashraf et al. 2006). Lưu ý: hiệu ứng mạnh nhất chỉ xuất hiện khi có **mặc định** hoặc **lời mời trực tiếp** (xem §5).

### 2.3 Chỗ hữu dụng còn yếu (phải trả lời được ở Q&A)

1. **Lợi suất của phần an toàn kém kênh cạnh tranh trong năm 2026.**

   | Kênh | Mức tham chiếu |
   |---|---|
   | Tiền gửi 12 tháng, Big4 tại quầy | 5,9% |
   | Chứng chỉ tiền gửi (BIDV, VietinBank) | 7,4% |
   | Nhiều ngân hàng khác, 12 tháng | ≥7% |
   | MoMo Túi Thần Tài | đến 6,1%, sinh lời hằng ngày |
   | TCBS iPower | 4,5–9,0% |
   | VIB SmartDepo | đến 4,3% |
   | Trứng Vàng | 4,2–5,3% (mức trên trang giới thiệu, chưa rõ ngày) |

   Danh mục Conservative khó thắng tiền gửi về lợi suất. Người tiết kiệm thận trọng, đúng nhóm Payday nhắm, sẽ hỏi "sao không gửi ngân hàng?".
2. **Phần cổ phiếu có thể bắn ngược vào trust.** Người mới, lại đang nghi ngờ DNSE (trust complaints của DNSE cao hơn đối thủ), gặp một đợt giảm điểm ngay những tháng đầu có thể viết review "lỗ/lừa đảo". Vấn đề Payday muốn chữa lại bị tái tạo.
3. **Ma sát lớn nhất nằm ngoài DNSE.** Khách phải tự vào app ngân hàng tạo lệnh chuyển tiền định kỳ. Chỉ khi có Open API (ngân hàng phải tuân thủ trước 01/03/2027) **và** thỏa thuận với từng ngân hàng thì mới làm được trong một bước.
4. **Phần thưởng tier gắn vào lãi tiền nhàn rỗi**, trong khi tiền Payday chỉ nằm đó 1–3 ngày. Thưởng hoặc gần như bằng 0, hoặc bị khách số dư lớn khai thác (`review_round2.md` R3).

---

## 3. Có phù hợp với người dùng nền tảng trading thực tế không?

### 3.1 Chân dung người dùng thực của DNSE (bằng chứng)

| Đặc điểm | Bằng chứng | Nguồn |
|---|---|---|
| Trẻ | Gen Z chiếm 31,5% TK (giữa 2025) | VnExpress 2025, trong report |
| Ít tiền | 98% TK dưới 10 triệu; tiền NĐT bình quân khoảng 1,15 triệu/TK | BCTN 2025; BCTC Q2/2026 |
| Thiên về phái sinh | 25,38% thị phần phái sinh, chỉ 2,88% cổ phiếu HNX; ký quỹ phái sinh nằm ở VSDC | HNX Q2/2026 |
| Ít dùng sản phẩm | 5,7% TK hoạt động (12/2025) | BCTN 2025 |
| Nhiều người đến vì thưởng | H1/2025: 54,8% review tiêu cực nói về trust/thưởng; 70 review referral spam bị loại trên Play | `reviews_flagged_*.csv` |
| Sản phẩm giữ tiền ít người dùng | Tài khoản Không Ngủ 12.100 đăng ký; Trứng Vàng 1.037 khách hoạt động (12/2025) | BCTN 2025 |
| Năm 2026 than phiền nhiều nhất về ổn định | Reliability: 58,8% (Play) và 75% (iOS) review tiêu cực | `reviews_flagged_*.csv` |

### 3.2 Mức phù hợp theo phân khúc (dùng nhãn của Table E3)

| Phân khúc | Phù hợp | Vì sao | Cách dùng Payday |
|---|:---:|---|---|
| E1. Khách hoạt động, có tiền (85.739; 27.100 có ≥10 triệu) | Trung bình | Đã nạp tiền nên Payday không giải "funding gap" cho họ. Nhưng nhiều người đi làm, có thể muốn phần "lõi" dài hạn bên cạnh phần trading | "Core–satellite": kế hoạch dài hạn đặt cạnh tài khoản giao dịch; **cẩn thận chuyện ăn thịt lẫn nhau** (chuyển tiền có sẵn sang để lấy tier) |
| E2. TK ngủ (khoảng 1,4 triệu) | **Không chắc** | Đối tượng ra mắt của report, nhưng chất lượng tệp chưa rõ: một phần là người săn thưởng 100k | Pilot RCT; **survey 2.000 TK ngủ phải chạy trước** (giả định #1) |
| N1. Người đi làm 22–40 mới | Cao về nhu cầu, thấp về khả năng thu hút | Đúng chân dung người tiết kiệm theo lương, nhưng thương hiệu DNSE gắn với trading/phái sinh và CAC cao | Kênh chủ lao động/payroll; ngân hàng đối tác; ZaloPay |
| N2. Người mới 15–24 | Thấp–Trung bình | Thu nhập thấp, không đều | Round-up ZaloPay (phase 2), vé nhỏ |
| N3. Nhà đầu tư lớn tuổi, giàu | Thấp | Thích môi giới người thật và thương hiệu ngân hàng | Không ưu tiên |

### 3.3 Xung đột hành vi giữa "ví giao dịch" và "hũ tiết kiệm"

- **Mental accounting:** người dùng app trading coi tiền trong app là "đạn" để giao dịch. Nếu rút Payday về sức mua chỉ mất một chạm, tiền tiết kiệm dễ bị dùng để đánh phái sinh hay margin khi thị trường sôi động. Vì vậy giả định **"giữ lại 70%" rất mong manh**. Gợi ý:
  - Rút Payday mặc định về **TK ngân hàng liên kết**, miễn phí, một chạm.
  - Muốn chuyển sang sức mua thì phải có bước riêng, kèm nhắc mục tiêu (tạo ma sát có chủ đích).
  - Tab và ví Payday tách biệt hẳn.
- **Chiều ngược lại:** người tiết kiệm có thể bị kéo sang trading hoặc margin. Report đã đúng khi loại margin khỏi phần thưởng và để margin cho phase sau, có kiểm tra tính phù hợp.
- **Điểm cộng ít được nói tới:** người dùng app trading quen với gamification (DNSE từng tổ chức giải "Võ đài phái sinh"). Cơ chế streak/tier vì thế hợp tâm lý nhóm này, **nếu** phần thưởng gắn với tiền đã đầu tư.

### 3.4 Kết luận về độ phù hợp

Payday phù hợp với **một nhóm con chưa đo được** trong tệp DNSE (người có lương, đã mở TK, chưa nạp tiền) và với **khách mới** mà DNSE chưa giỏi thu hút (người tiết kiệm). Nó **không** phù hợp với lõi người dùng hiện tại (trader phái sinh, người săn thưởng). Hệ quả là test #1 (survey 2.000 TK ngủ do DNSE chạy sau khi được duyệt) phải chạy đầu tiên. Trong bài Round 3, khi không kịp làm survey riêng, dùng khảo sát đã công bố, hành vi ngành và tiếng nói khách trong review (`plan_payday.md` §4.3; `competitor_features.md` §6).

---

## 4. Mức độ "đặc biệt": so với TCBS, VPS, SSI, VNDirect, MoMo, Fmarket/Finhay, ngân hàng

### 4.1 Bảng so sánh tính năng (tháng 10/2026)

| Sản phẩm | Kích hoạt | Tài sản | Vé tối thiểu | Tư vấn / chiến lược | Thực thi | Thưởng cam kết | Trong app giao dịch | Trạng thái |
|---|---|---|---|---|---|---|---|---|
| **DNSE Payday (đề xuất)** | **Ngày lương** (lệnh định kỳ vào VA tên khách) | Quỹ TP, Trứng Vàng, quỹ CP, ETF VN30 | 500.000đ/tháng | Ensa đề xuất 3 danh mục mẫu | Khách xác nhận (không ủy thác) | Tier 3/6/12 kỳ, bỏ qua 1 tháng/năm | Có (tab riêng) | Đề xuất |
| **VPS Smart Indexing (VSI)** | Nạp định kỳ theo kế hoạch khách đặt; vốn mới phân bổ tự động | Cổ phiếu (direct indexing, khách sở hữu trực tiếp) | **50 triệu ban đầu; định kỳ từ 10 triệu/tháng** | Mô hình định lượng do chuyên gia VPS + Quỹ Sài Gòn (SGC) vận hành | **Ủy thác**; phí quản lý 0,5%/năm + phí giao dịch; phạt khi rút trước cam kết | Chưa thấy | Có | **Ra mắt 11/08/2026** |
| **SSI iBoard eSIP** | Lịch định kỳ khách đặt (số tiền, tần suất định sẵn) | Chứng chỉ quỹ mở SSIAM, Dragon Capital (CP, TP, cân bằng) | Chưa thấy công bố (SSIBF miễn phí phát hành SIP) | Khách tự chọn quỹ | Theo kế hoạch đặt sẵn | **Thưởng có điều kiện**: voucher 50.000đ khi TK mới mua eSIP từ 1 triệu | Có | Chương trình "Tích sản thảnh thơi" 23/04/2026; thêm quỹ Dragon Capital từ 29/06/2026 |
| **TCBS** | iPower: tự động trên tiền nhàn rỗi (đến 6%, số dư từ 5 triệu) | Fundmart (31 quỹ, khoảng 55% NAV quỹ mở); iTracker (cổ phiếu theo quy tắc, tái cơ cấu 1–2 tuần/lần) | iPower từ 5 triệu; iTracker 10 triệu/lần copy (ưu đãi) | iTracker | Theo từng sản phẩm; iTracker có phí quản lý (đang miễn theo đợt) | Miễn phí quản lý theo đợt | Có | Đang chạy |
| **VinaCapital VinaSIP** (app MIO) | **Khách đặt lệnh chuyển tiền định kỳ từ ngân hàng vào TK VinaSIP** | Một quỹ VinaCapital mỗi SIP | 500.000đ/tháng (2021) | — | Khách | — | Không | **Từ 06/2021** |
| **VCBF trên VCB Digibank** | **Hệ thống tự trích TK ngân hàng theo ngày khách chọn** | Quỹ VCBF | **100.000đ/kỳ**; không eKYC lại | — | Khách | Phí bán ưu đãi cho SIP | Không (app ngân hàng) | Đang chạy (bài báo 2026) |
| **VPBank Hũ Mục Tiêu** | Chuyển tự động theo ngày, tuần, tháng; góp chung theo nhóm | Tiền gửi theo mục tiêu | Chưa thấy | Theo mục tiêu | Khách | — | Không (app ngân hàng) | **Ra mắt 12/09/2026** |
| **VNDirect** | — | VNDGO (phân phối quỹ, có VCBF); DLIFE (tích sản hưu trí, 2020, chưa xác minh còn chạy không) | — | — | — | — | DStock (giao dịch) | Đang chạy |
| **MoMo** | Túi Thần Tài sinh lời hằng ngày | Chứng chỉ quỹ DCVFM, IPAAM, SSIAM, VCBF | **10.000đ** | — | Khách tự mua | Chưa thấy | Không (ví điện tử) | Đang chạy |
| **Fmarket / Finhay** | SIP / tích lũy tự động | Quỹ mở; Finhay có HayBond (gói 4 tháng, đến 8,6%/năm, 03/2026) | SIP thường từ 1 triệu (ví dụ VCBF) | Có robo / gợi ý | Theo kế hoạch | Ví dụ VCBF giảm 20% phí mua khi duy trì SIP 12 tháng | Không / hạn chế | Đang chạy |
| **Ngân hàng** (VPBank Super Sinh Lời, VIB SmartDepo…) | Tự động trên số dư tài khoản lương | Tiền gửi | Không | Không | Tự động | Không | Không | Đang chạy |
| *Quốc tế (tham chiếu)* | Chime "Save When I Get Paid", Acorns Recurring/Round-Ups, Trade Republic savings plans, Robinhood recurring + direct deposit | — | — | — | — | — | — | *Cơ chế kích hoạt theo lương là chuẩn phổ biến ở Mỹ/EU* |

*"Chưa thấy" nghĩa là tra cứu ngày 14–16/10 không tìm ra, chưa phải là chắc chắn không có. Bảng đầy đủ hơn (14 sản phẩm, có nguồn từng ô) nằm ở `competitor_features.md`. Trên slide, ghi "based on public product information as of 16 October 2026".*

### 4.2 Thành phần nào đã có, cái gì thực sự mới

- **Đã có trên thị trường:**
  - **Chuyển tiền định kỳ tự động từ ngân hàng vào kế hoạch đầu tư:** VinaSIP (từ 2021), VCB Digibank SIP (từ 100.000đ/kỳ, không eKYC lại), SSI eSIP, VPBank Hũ Mục Tiêu.
  - Tiết kiệm theo mục tiêu: VPBank Hũ Mục Tiêu (tiền gửi, 12/09/2026).
  - Phân bổ tự động vốn mới theo chiến lược: VPS VSI (chỉ cổ phiếu, ủy thác, từ 50 triệu).
  - Tiền nhàn rỗi sinh lời: TCBS iPower, MoMo, Tikop, ngân hàng, và chính DNSE.
  - Danh mục tự động hóa: TCBS iTracker.
  - Vé nhỏ: MoMo 10.000đ, Techcombank 10.000đ, Tikop 50.000đ, VCB 100.000đ.
- **Có thể là mới ở Việt Nam** (trong phạm vi đã kiểm):
  1. **Danh mục nhiều lớp tài sản** trong một kế hoạch: lõi trái phiếu ngân hàng (Trứng Vàng từ 1 triệu) + quỹ + ETF, vé 500.000đ, **trong app giao dịch zero-fee**.
  2. **Tư vấn theo mục tiêu + đánh giá phù hợp + khách xác nhận từng thay đổi**, gắn với kế hoạch định kỳ.
  3. **Thưởng cho sự bền bỉ** (streak, bỏ qua 1 tháng/năm), thay vì thưởng mở TK hay theo ngưỡng mua như đối thủ đang dùng.
  4. **"Trust by design" có chỉ số công bố**: thời gian rút tiền trung vị, tỷ lệ chuyển tiền thành công, tỷ lệ hủy hoàn tất trong app.
- *Đính chính 16/10:* bản 15/10 xếp "kích hoạt theo ngày nhận lương" vào nhóm "có thể mới". Điều đó **sai**: VinaSIP và VCB Digibank đã dùng đúng cơ chế chuyển tiền định kỳ từ ngân hàng.

### 4.3 Khác biệt có bền không (hào phòng thủ)

| Điểm khác biệt | Độ bền | Vì sao | Làm sao để bền hơn |
|---|:---:|---|---|
| Kích hoạt theo ngày lương | **Không phải khác biệt** (đã là chuẩn) | VinaSIP (2021) và VCB Digibank SIP đã dùng chuyển tiền định kỳ từ ngân hàng. Lương phần lớn trả vào ngày cố định, nên SIP đặt ngày 5 hay 10 gần như tương đương. Chỉ giữ làm *cách gọi tên* với khách | (a) **Trích theo % lương** khi phát hiện được lương qua Open API (sau 03/2027); (b) **hợp tác payroll với chủ lao động** để có mặc định thật |
| Nhiều lớp tài sản, vé nhỏ, lõi trái phiếu | Trung bình | VSI chỉ có cổ phiếu, SSI chỉ có quỹ. Trứng Vàng là "lõi an toàn" mà đối thủ trực tiếp chưa có ở dạng này | Biến Trứng Vàng thành bậc thang kỳ hạn theo mục tiêu; minh bạch tổ chức phát hành và lợi suất |
| Tier / streak | Yếu, và đang thiết kế sai | Dễ sao chép; gắn vào lãi tiền nhàn rỗi nên mâu thuẫn | Thưởng cho tiền đã đầu tư, có trần (§7) |
| Trust by design có số đo công bố | **Trung bình–Mạnh** nếu làm thật | DNSE đang yếu nhất ở trust, nên biến điểm yếu thành cam kết công khai có số đo là câu chuyện khó sao chép về uy tín | Công bố chỉ số hằng tháng; cam kết không phí đóng TK, không thưởng có điều kiện |
| Phân phối tới 1,4 triệu TK đã eKYC | Trung bình | Chi phí thu hút gần như 0, nhưng chất lượng tệp đáng ngờ | Đo bằng survey và pilot; phân tầng theo cohort và kênh mở TK |

### 4.4 So riêng với VPS Smart Indexing (đối thủ nguy hiểm nhất)

| | VPS Smart Indexing | DNSE Payday |
|---|---|---|
| Bản chất | Ủy thác; direct indexing cổ phiếu; chiến lược định lượng | Tư vấn có giấy phép + khách xác nhận; nhiều lớp tài sản có lõi trái phiếu |
| Khách mục tiêu | Nhà đầu tư chứng khoán **có vốn** muốn tích sản dài hạn | **Người đi làm chưa từng đầu tư đều đặn** |
| Vé tối thiểu | **50 triệu ban đầu; định kỳ từ 10 triệu/tháng** (khuyến nghị 200 triệu) | **500.000đ/tháng** |
| Phí | **0,5%/năm** trên tài sản ủy thác + phí giao dịch; phạt khi rút trước cam kết | Không phí nền tảng; doanh thu từ quỹ và trái phiếu |
| Kích hoạt | Nạp định kỳ theo kế hoạch | Lệnh định kỳ vào VA tên khách (cùng loại cơ chế, không phải khác biệt) |
| Quyền quyết định | VPS quản lý thay khách. Báo chí nêu SGC là cổ đông lớn nhất của VPS (38,86%) và đặt câu hỏi "ai quyết định mua, bán" | Khách xác nhận mọi thay đổi |
| Lợi thế của đối thủ | VPS dẫn đầu thị phần môi giới cơ sở; đã ra mắt trước | — |

→ **Định vị đề xuất:** VSI là sản phẩm "indexing cho nhà đầu tư có vốn"; Payday là "bước đầu tiên cho người tiết kiệm có lương". Vé 500.000đ so với 50 triệu + 10 triệu/tháng cho thấy hai sản phẩm nằm ở hai tầng khách khác nhau. Dù vậy, DNSE phải ra mắt nhanh và giữ đúng ngách.

→ **Đối thủ khó hơn cho câu chuyện "lương → đầu tư" là ngân hàng** (VCB Digibank SIP từ 100.000đ, không eKYC lại; VPBank Hũ Mục Tiêu). Payday thắng ngân hàng ở phạm vi tài sản (ETF, cổ phiếu, trái phiếu niêm yết, quỹ của nhiều nhà quản lý) và ở việc dùng chung app với giao dịch. Payday không thắng ở độ tiện khi cài đặt, nên bước cài đặt phải dễ ngang VCB Digibank (`competitor_features.md` §3.4).

---

## 5. Thử thách các giả định cốt lõi

| Giả định (Round 2) | Bằng chứng ủng hộ | Bằng chứng ngược | Đánh giá | Việc cần làm |
|---|---|---|---|---|
| **150.000 saver sau 18 tháng** (khoảng 1/11 TK ngủ; gấp 1,75 lần số khách hoạt động 12/2025) | Hành vi học về mặc định (opt-out) | Payday là opt-in. Tài khoản Không Ngủ (đơn giản hơn, miễn phí) chỉ đạt **12.100 đăng ký sau ~6 tháng (0,8%)**. Ashraf et al.: khoảng 28% chịu tham gia dù được mời *trực tiếp*. Tệp TK ngủ có nhiều người săn thưởng | **Quá lạc quan** | Neo target vào benchmark nội bộ và kết quả pilot; kênh chủ lao động cho phần tăng trưởng lớn |
| **1,5 triệu/tháng** (khoảng 17% thu nhập bình quân 9,0 triệu theo NSO) | NSO H1/2026 | Tệp DNSE trẻ hơn bình quân; người 22–30 thu nhập thấp hơn | Hơi cao | Dùng phân phối thu nhập theo tuổi; base 1,0–1,2 triệu |
| **Giữ lại 70%** | — | Mental accounting của người dùng trading; thị trường giảm thì người ta rút | Chưa có cơ sở | Đo ở pilot; thiết kế ma sát khi rút sang sức mua |
| **Phí 0,8% trên toàn bộ tài sản** | Phân phối quỹ có thu phí | ETF miễn phí giao dịch tại DNSE; SIP thường miễn phí phát hành (SSIBF); Trứng Vàng thu chênh lệch chứ không thu phí; tier Disciplined giảm thêm phí; TCBS báo phân phối quỹ yếu đi do lãi suất cao | **Có thể quá cao** | Lợi suất theo từng lớp tài sản, lấy từ điều lệ/factsheet quỹ và biên lãi Trứng Vàng |
| **Chi phí tier tối đa 5,6 tỷ/năm** | — | Cơ chế 4,3% "không điều kiện" có thể áp cho toàn bộ tiền nhàn rỗi | **Sai cách tính** | Sửa thiết kế và đặt trần |
| **Ghi danh tĩnh 18 tháng** | — | Lộ trình pilot của chính report (mở rộng từ khoảng tháng 7) | **Sai mô hình** | Mô hình cohort; base thực tế khoảng 1,0 nghìn tỷ và khoảng 64.600 TK ≥10 triệu sau 18 tháng (`review_round2.md` R2) |
| **Kết nối ngân hàng dễ hơn từ 03/2027** | Thông tư 64/2024 (mốc đúng) | Phải ký thỏa thuận với từng ngân hàng; ngân hàng phòng thủ CASA | Có điều kiện | Chọn ngân hàng đối tác giữ VA làm đồng minh (CASA vẫn nằm ở ngân hàng đó) |
| **Đủ ổn định cho ngày lương** | Cổng 99,5% | 2026: reliability chiếm 58,8% (Play) và 75% (iOS) review tiêu cực, đỉnh tháng 3/2026 quanh bản iOS 2.113.28 | **Rủi ro cao** | Reliability thành workstream riêng, có SLO công bố |

---

## 6. Rủi ro report chưa thấy

1. **Thị trường giảm, trust bị bắn ngược:** phần cổ phiếu lỗ trong vài tháng đầu sinh ra review "lừa đảo". Giảm thiểu: mặc định thiên trái phiếu, cổ phiếu chỉ cho mục tiêu từ 3 năm trở lên; hiển thị trước "tháng tệ nhất" dự kiến bằng tiền.
2. **Rút tiền để trade:** tiền Payday chảy về sức mua khi thị trường nóng (§3.3).
3. **Khai thác tier:** khách số dư lớn đặt lệnh 500.000đ/tháng để lấy 4,3% trên toàn bộ tiền mặt.
4. **Ăn thịt lẫn nhau:** người đang dùng Không Ngủ hoặc Trứng Vàng chuyển tiền có sẵn sang Payday để lấy tier, nên không có tiền mới. Test 7 trong report đã có gắn nhãn nguồn tiền, nên giữ.
5. **Trách nhiệm khi AI tư vấn:** Ensa sai hoặc "ảo giác", ai chịu? Cần người hành nghề có chứng chỉ phê duyệt danh mục mẫu, lưu log, có giới hạn phạm vi trả lời.
6. **Ngày lương không cố định:** lương trễ, lương tháng 13 hay thưởng Tết, thu nhập biến động. Bộ lập lịch cần chế độ "khi lương về" và xử lý lệnh thất bại một cách nhẹ nhàng (không mất tier).
7. **Đối thủ phản ứng:** VPS mở rộng VSI xuống vé nhỏ; TCBS gói sản phẩm với Techcombank; ngân hàng tự làm "tích sản" sau khi có Open API.
8. **Quy định về thưởng và khuyến mại:** phần thưởng dạng lãi suất hoặc tiền cần được bộ phận tuân thủ rà theo quy định khuyến mại và quảng cáo chứng khoán trước khi ra mắt (chưa kiểm cụ thể văn bản nào, nên phải hỏi pháp chế).
9. **Đối soát VA:** lệch tiền, ghi có sai, ngoài giờ. Report có nhắc review "tiền đã trừ ở ngân hàng nhưng chưa về TK chứng khoán" (Table D3).

---

## 7. Đề xuất điều chỉnh (xếp theo ưu tiên)

1. **Định vị lại thông điệp.** Thay cho "sản phẩm độc nhất", nói *"a goal-based monthly plan from VND 500,000 that combines bonds, funds and ETFs, confirmed by the customer and rewarding those who stay, inside a zero-fee trading app; DNSE's balance-building layer, built from components DNSE already runs"*. **Không** gọi Payday là "first salary-linked plan", vì VinaSIP và VCB Digibank đã có chuyển tiền định kỳ từ ngân hàng. Thêm một slide so sánh đối thủ trung thực, có VSI, SSI eSIP, VCB Digibank SIP (`competitor_features.md`).
2. **Sửa tier:**
   - Thưởng cho tiền **đã đầu tư và ở lại**: giảm phí quỹ, quà dạng chứng chỉ quỹ giá trị nhỏ khi đạt mốc, ưu tiên Trứng Vàng kỳ mới, đánh giá danh mục.
   - Mọi ưu đãi lãi chỉ áp cho số dư Payday hoặc có trần (ví dụ 50 triệu).
   - Bỏ "4,3% không điều kiện".
3. **Tạo mặc định thật qua kênh chủ lao động (B2B2C):** pilot với 3–5 doanh nghiệp, Payday là phúc lợi cho nhân viên. Đây là nơi bằng chứng Madrian & Shea áp dụng được. Thêm tùy chọn "**tăng % khi tăng lương**" theo tinh thần SMarT.
4. **Danh mục mặc định thiên trái phiếu** (Trứng Vàng + quỹ trái phiếu); cổ phiếu và ETF chỉ dành cho mục tiêu từ 3 năm. Hiển thị biên độ lãi/lỗ bằng tiền, không chỉ bằng %.
5. **Ưu tiên reliability:** chuyển tiền ngày lương chạy bằng job nền có retry, theo dõi theo phiên bản app, có SLO công bố. Đây là thay đổi chính so với Round 2 (data 2026).
6. **Ma sát có chủ đích khi rút sang sức mua:** rút về ngân hàng thì một chạm, miễn phí; chuyển sang sức mua thì có bước riêng kèm nhắc mục tiêu.
7. **Đo bằng pilot và mô hình cohort:** KPI theo giai đoạn (`plan_payday.md` §5). Phase 3: "trích % lương" khi có Open API.

---

## 8. Câu hỏi giám khảo có thể hỏi và hướng trả lời

| Câu hỏi | Hướng trả lời |
|---|---|
| "VPS vừa ra Smart Indexing, SSI có eSIP, VCB Digibank cũng trích lương mua quỹ. Payday khác gì?" | Thừa nhận chuyển tiền định kỳ đã là chuẩn. Khác ở **tầng khách** (500.000đ so với 50 triệu + 10 triệu/tháng của VSI), **phạm vi tài sản** (trái phiếu + quỹ + ETF trong một kế hoạch, so với chỉ cổ phiếu hoặc chỉ quỹ), **quyền quyết định** (khách xác nhận, không ủy thác), **cách thưởng** (thưởng cho sự bền bỉ, không voucher theo ngưỡng) và **minh bạch có số đo** |
| "Sao người đi làm không gửi tiết kiệm 7% cho chắc?" | Payday không thay tiền gửi. Phần lõi là trái phiếu ngân hàng; giá trị nằm ở kỷ luật, mục tiêu, thanh khoản và phần tăng trưởng dài hạn. Có thể cho thấy mô phỏng 3–5 năm với các giả định lợi suất được ghi rõ |
| "Tệp của DNSE là trader trẻ, sao họ muốn tích sản?" | Đồng ý rằng tệp lõi không hợp. Vì vậy (1) survey 2.000 TK ngủ chạy trước; (2) nhắm nhóm con có lương; (3) kênh chủ lao động cho khách mới. Dẫn khảo sát đã công bố (77% thấy khó tự quản lý, 81% muốn tư vấn) và việc cả SSI, VPS, VPBank, VCBF cùng tung sản phẩm tích lũy năm 2026 |
| "150.000 saver lấy ở đâu, khi Không Ngủ mới có 12.100?" | Đã hiệu chỉnh: target neo vào benchmark nội bộ, ramp theo pilot; mốc 18 tháng là X (từ mô hình cohort), không còn là 150.000 |
| "DNSE kiếm bao nhiêu, khi nào hoàn vốn?" | Unit economics: doanh thu trên mỗi 10 triệu số dư, CAC trần, tháng hòa vốn; giá trị gián tiếp (giữ số dư, margin phase 2 cho khách phù hợp, giảm chi phí/TK có tiền); đầu tư theo giai đoạn, ban đầu chỉ xin ngân sách pilot |
| "AI tư vấn sai thì ai chịu trách nhiệm?" | Danh mục mẫu do người hành nghề có chứng chỉ thiết kế và phê duyệt; Ensa chỉ thu thập thông tin và giải thích; mọi lệnh do khách xác nhận; có log và kiểm toán nội bộ |
| "Tier 4,3% có bị khách lớn lợi dụng không?" | Đã sửa: thưởng cho tiền đã đầu tư, có trần |
| "App các bạn bị chê lỗi nhiều nhất năm 2026, ngày lương mà lỗi thì sao?" | Đúng, data đã cho thấy và đây là lý do chúng tôi đổi trọng tâm. Chuyển tiền chạy bằng job nền, shadow run, cổng 99,5%, theo dõi theo phiên bản, công bố SLO |
| "Ngân hàng có chịu để lương chảy sang CTCK không?" | VA nằm ở ngân hàng đối tác nên CASA vẫn ở đó; giai đoạn đầu dùng lệnh định kỳ do khách tự đặt, không cần API; Open API từ 03/2027 là cơ hội chứ không phải điều kiện tiên quyết |
| "Thị trường giảm 20% trong năm đầu thì sao?" | Mặc định thiên trái phiếu, cổ phiếu chỉ cho mục tiêu dài hạn, công bố trước kịch bản xấu, tạm dừng hoặc bỏ qua không mất tier; theo dõi trust complaints như một chỉ số giới hạn (guardrail) |

---

## Nguồn

- [VPS chính thức ra mắt sản phẩm VPS Smart Indexing (Tin nhanh Chứng khoán)](https://www.tinnhanhchungkhoan.vn/vps-chinh-thuc-ra-mat-san-pham-vps-smart-indexing-post395704.html)
- [VPS chính thức ra mắt sản phẩm VPS Smart Indexing (Tuổi Trẻ)](https://tuoitre.vn/vps-chinh-thuc-ra-mat-san-pham-vps-smart-indexing-10026081114333576.htm)
- [Thị phần VPS tiếp tục dẫn đầu, ra mắt dịch vụ quản lý danh mục định kỳ (VSI)](https://doanhnhan.baophapluat.vn/thi-phan-vps-tiep-tuc-dan-dau-ra-mat-dich-vu-quan-ly-danh-muc-dinh-ky-vsi.html)
- [VPS Smart Indexing và bài toán quản lý tài sản dài hạn (Người Đưa Tin)](https://www.nguoiduatin.vn/vps-smart-indexing-va-bai-toan-quan-ly-tai-san-dai-han-cho-nha-dau-tu-chung-khoan-204260818135342088.htm)
- [Thêm quỹ Dragon Capital, SSI iBoard mở rộng sản phẩm đầu tư trên nền tảng số](https://doanhnhan.baophapluat.vn/them-quy-dragon-capital-ssi-iboard-mo-rong-san-pham-dau-tu-tren-nen-tang-so.html)
- [SSIBF Fund Factsheet 04/2026](https://www.ssi.com.vn/upload/files/QuanLyQuy/SSIBF%20Fund%20Factsheet%2004_2026_VN.pdf)
- [MoMo chính thức hợp tác với SSIAM](https://www.momo.vn/tin-tuc/thong-bao/momo-chinh-thuc-hop-tac-voi-ssiam-mo-ra-co-hoi-3577)
- [Sàn đầu tư MoMo, Túi Thần Tài (VNBA)](https://vnba.org.vn/vi/san-dau-tu-momo--toi-uu-loi-nhuan-cho-nha-dau-tu-tu-nguon-von-nho-9271.htm)
- [Chứng khoán: TCBS Fundmart, iTracker (Thị trường Tài chính Tiền tệ)](https://thitruongtaichinhtiente.vn/print/80857.html)
- [TCBS 2Q2026 Earnings Call](https://www.tcbs.com.vn/wp-content/uploads/2026/07/TCBS_2Q2026-Earnings-Call_VN-1.pdf)
- [VNDIRECT chính thức phân phối quỹ mở VCBF trên nền tảng VNDGO](https://tapchikinhtetaichinh.vn/vndirect-chinh-thuc-phan-phoi-quy-mo-vcbf-tren-nen-tang-vndgo-38797.html)
- [Phiếu đăng ký SIP của VCBF](https://www.vcbf.com/images/2019/phieu_sip-sip.pdf)
- [Finhay: Tích lũy 2026](https://finhay.com.vn/tich-luy-2026-huong-dan-tiet-kiem-dau-tu-tu-dong)
- [Công thức vận hành dòng tiền với SmartDepo VIB](https://daibieunhandan.vn/cong-thuc-van-hanh-dong-tien-cho-co-hoi-voi-smartdepo-vib-10404207.html)
- [Tài khoản Không Ngủ (DNSE)](https://www.dnse.com.vn/san-pham/tai-khoan-khong-ngu)
- [DNSE giới thiệu sản phẩm "Trứng vàng"](https://kinhtechungkhoan.vn/dnse-gioi-thieu-san-pham-trung-vang-voi-loi-suat-dau-tu-hap-dan-1043755.html)
- [Hướng dẫn DNSE: cập nhật tính năng tháng 4/2026 (tái tục Trứng Vàng)](https://hdsd.dnse.com.vn/cap-nhat-tinh-nang-moi/nam-2026/thang-4-2026)
- [Lãi suất đầu tháng 10/2026](https://thitruongtaichinhtiente.vn/lai-suat-dau-thang-10-2026-tiet-kiem-giu-nhip-on-dinh-chung-chi-tien-gui-hut-khach-85944.html)
- [Thông tư 64/2024/TT-NHNN (Thư viện Pháp luật)](https://thuvienphapluat.vn/van-ban/Tien-te-Ngan-hang/Thong-tu-64-2024-TT-NHNN-trien-khai-giao-dien-lap-trinh-ung-dung-mo-nganh-Ngan-hang-641360.aspx)
- Madrian & Shea (2001); Thaler & Benartzi (2004); Ashraf, Karlan & Yin (2006), trong danh mục tài liệu tham khảo của report Round 2.
- Data nội bộ: `data/reviews_flagged_*.csv`, `data/reviews_raw_ios_*.csv`, `data/manual/dnse_accounts.csv`, `data/manual/idle_cash_rates.csv`.

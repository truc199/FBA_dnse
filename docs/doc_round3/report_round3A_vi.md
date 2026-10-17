# Payday Portfolio: thiết kế sản phẩm, kế hoạch ra mắt và phương án kinh doanh cho Chứng khoán DNSE

*Báo cáo bổ trợ Vòng 3A, KTQT FTUers, 17/10/2026. Không dùng để nộp: sản phẩm nộp ở Vòng 3A là bộ slide. Báo cáo này trình bày đầy đủ lập luận, bằng chứng và số liệu đằng sau deck. Bảng được sinh từ các file CSV trong `outputs/round3/tables/vi/` bằng `src/round3/deck_tables.py`; muốn sửa thì sửa ở đó, không sửa bảng trong file này.*

## Tóm tắt điều hành

Chứng khoán DNSE mở tài khoản với quy mô lớn nhưng không giữ được dòng tiền lẽ ra phải đi kèm. Năm 2025 DNSE mở 1/5 số tài khoản chứng khoán mới của Việt Nam và đến giữa 2026 nắm 12,3% tổng số tài khoản. Thế nhưng tháng 12/2025 chỉ 1,8% trong 1,51 triệu tài khoản của DNSE có từ 10 triệu đồng trở lên, và DNSE chỉ giữ 2,3% tiền mà nhà đầu tư để tại các công ty chứng khoán. Doanh thu môi giới đã thấp hơn chi phí trực tiếp 16 quý liên tiếp. Vòng 2 đã truy khoảng trống này về ba nguyên nhân: công cụ hút trader trẻ ít vốn, niềm tin gãy ngay ở lần nạp tiền đầu, và không có con đường nào đưa ý định của người đi làm thành những lần nạp tiền đều đặn. Báo cáo này thiết kế sản phẩm giải quyết nguyên nhân thứ ba trong khi tôn trọng nguyên nhân thứ hai, và trình bày cách DNSE xây dựng, thử nghiệm, ra mắt và mở rộng sản phẩm đó.

Năm 2026 làm vấn đề gấp hơn và thêm một sự thật mới. Tiền của nhà đầu tư tại các công ty chứng khoán giảm 38% chỉ trong ba quý, trong khi ngân hàng trả 5,9% cho kỳ hạn 12 tháng. SSI, TCBS, VPS và VPBank đã ra mắt các kế hoạch tích lũy định kỳ hoặc theo mục tiêu, và ngân hàng phải mở giao diện lập trình ứng dụng (Open API) chậm nhất ngày 1/3/2027. Khi đọc 58 review tiêu cực về app DNSE trong năm 2026, nhóm thấy 83% mô tả một thứ bị hỏng và 19% nói về điều khoản, phần thưởng hoặc niềm tin. Như vậy độ ổn định nay là rào cản đầu tiên.

Payday Portfolio là kế hoạch góp hằng tháng theo mục tiêu, từ 500.000 đồng. Khách đặt mục tiêu, trả lời vài câu đánh giá mức độ phù hợp và xác nhận một kế hoạch do người hành nghề có chứng chỉ ký. Một lệnh chuyển tiền định kỳ từ ngân hàng nhận lương nạp vào tài khoản định danh (VA) mang tên khách. Tiền chờ ở Tài khoản Không Ngủ, và mỗi kỳ góp mua lớp tài sản đang thiếu tỷ trọng nhất: trái phiếu ngân hàng qua Trứng Vàng, quỹ trái phiếu và quỹ cổ phiếu, hoặc ETF VN30, theo cơ cấu do kỳ hạn mục tiêu quyết định. Không có phí nền tảng, không thưởng tiền và không margin. Việc giữ chân dựa vào các tính năng không bằng tiền, và DNSE công bố hằng tháng tỷ lệ ghi có đúng hạn cùng thời gian rút tiền.

Phương án kinh doanh nói thẳng về tiền. Mô hình cohort theo tháng trong 60 tháng, với chi phí có nguồn, cho kết quả ở kịch bản cơ sở là 14.871 tài khoản mới trên 10 triệu đồng vào tháng 36, nâng tổng số từ 27.100 lên khoảng 42.000, cùng 352 tỷ đồng số dư kế hoạch. Kịch bản cơ sở không hoàn vốn trong 5 năm: NPV chiết khấu 12% là −25,0 tỷ đồng và dòng tiền lũy kế tháng 60 là −32,0 tỷ đồng. Đọc đúng thì Payday là cách mua tài khoản có tiền với chi phí ròng khoảng 1,3 triệu đồng mỗi tài khoản. Kịch bản thuận lợi hoàn vốn ở tháng 44 với NPV 11,0 tỷ đồng. Kịch bản bất lợi tốn 10,0 triệu đồng cho mỗi tài khoản có tiền và sẽ bị dừng ở tháng 6. Biến số quyết định là chi phí cố định, không phải chi phí thu hút khách.

Vì vậy nhóm đề nghị HĐQT duyệt 6,6 tỷ đồng để xây dựng sản phẩm và chạy một pilot ngẫu nhiên với 45.000 tài khoản ngủ trong tháng 1 đến tháng 6. Nhóm cũng đề nghị năm quyết định: chọn ngân hàng VA chịu miễn phí thu hộ; ký với một hoặc hai công ty quản lý quỹ; nộp thông báo cho UBCKNN kèm tham vấn trước về vai trò của Trứng Vàng; có người hành nghề có chứng chỉ ký danh mục mẫu; và lấy khoảng 1,3 triệu đồng mỗi tài khoản mới trên 10 triệu làm thước đo. Đến tháng 6, HĐQT quyết định dừng hay mở rộng dựa trên các ngưỡng suy ra từ mô hình.

## 1. Giới thiệu

### 1.1 Mục đích của báo cáo

Vòng 3A yêu cầu một product owner trình bày sản phẩm đã thiết kế, chiến lược phát triển, ra mắt và tăng trưởng, kế hoạch go-to-market cho năm đầu và một phương án kinh doanh mà HĐQT có thể phê duyệt. Deck trình bày phương án đó trong 15 slide. Báo cáo này đưa ra lập luận đầy đủ: bằng chứng đằng sau từng lựa chọn thiết kế, cách các con số được dựng, và HĐQT sẽ cam kết những gì. Báo cáo kế thừa báo cáo Vòng 2 của nhóm (KTQT FTUers, 2026), giữ những gì vẫn đúng và sửa những gì không còn đúng (Mục 2.5).

### 1.2 Câu hỏi kinh doanh và phạm vi

Câu hỏi là: *DNSE nên xây sản phẩm gì để biến các tài khoản đã mở thành số dư, nên ra mắt và mở rộng thế nào, và HĐQT nên duyệt gì ngay bây giờ?*

Phạm vi là Payday Portfolio từ MVP đến tháng 36, với mô hình chạy đến tháng 60. Người đi làm có tài khoản ngủ là nhóm khách ra mắt. Thiết kế dùng các sản phẩm và giấy phép DNSE đã có, và nằm trong các quy định của Việt Nam về tư vấn đầu tư, cho vay ký quỹ và ngân hàng mở. Sản phẩm margin, phái sinh, việc thiết kế lại app Entrade X và nguồn vốn riêng của DNSE nằm ngoài phạm vi.

### 1.3 Bằng chứng và phương pháp

Báo cáo dựa trên năm nguồn bằng chứng (Phụ lục A):
- báo cáo thường niên 2025, hồ sơ công bố của DNSE và dữ liệu thị trường đã đối chiếu ở Vòng 2;
- 44 nguồn web về lãi suất, phí, điều khoản sản phẩm và đối thủ, mỗi nguồn ghi ngày truy cập và ai đã kiểm: nhóm tự kiểm đầy đủ 30 nguồn và kiểm một phần 3 nguồn, 11 nguồn còn lại mới chỉ được một trợ lý nghiên cứu AI kiểm;
- đọc thủ công toàn bộ 58 review tiêu cực về app DNSE đăng từ ngày 1/1 đến 21/9/2026;
- rà soát tại bàn 20 sản phẩm đối thủ, trong đó 9 sản phẩm được nhóm đối chiếu với nguồn gốc;
- mô hình cohort theo tháng của Payday với 60 thông số, mỗi thông số được gắn nhãn là có nguồn, suy ra hoặc giả định.

Có hai giới hạn quan trọng. Nhóm không làm khảo sát khách hàng, nên tỷ lệ ghi danh, mức duy trì và mức góp là giả định mà pilot phải đo. Số dư được tính trước lợi nhuận đầu tư, nên thấp hơn số người tích lũy thực có nếu thị trường tăng.

## 2. Vấn đề và vì sao phải làm ngay

### 2.1 Tài khoản được mở nhưng không có tiền

Chỉ số càng gần với tiền thì DNSE càng nhỏ (Hình 1). Giữa 2026 DNSE nắm 12,3% số tài khoản chứng khoán của Việt Nam và năm 2025 mở 20,1% số tài khoản mới, nhưng chỉ giữ 2,3% tiền của nhà đầu tư tại các công ty chứng khoán, 1,4% dư nợ margin và 0,6% lợi nhuận trước thuế của ngành. Tháng 12/2025 có 85.739 tài khoản (5,7%) dùng ít nhất một sản phẩm và 27.100 tài khoản (1,8%) có tài sản ròng từ 10 triệu đồng trở lên. 1.427.181 tài khoản còn lại không dùng sản phẩm nào trong tháng đó (DNSE Securities, 2026c).

![Hình 1. Thị phần của DNSE ở từng thị trường, %; đường đứt nét là thị phần tài khoản 12,3%](outputs/figures/fig04_market_position.png)

Nguồn: KTQT FTUers (2026), Figure 4, từ VnExpress (2026a), DNSE Securities (2026a, 2026c), Vietstock (2026b), CafeF (2026), VnEconomy (2026) và Hanoi Stock Exchange (2026); tính toán của nhóm. Cột gạch chéo là ước tính.

### 2.2 Tài khoản rỗng biến nền tảng thành chi phí cố định

Giao dịch miễn phí không tự nuôi được mình. Doanh thu môi giới thấp hơn chi phí trực tiếp của môi giới 16 quý liên tiếp, từ Q3/2022 đến Q2/2026, lỗ lũy kế 190,3 tỷ đồng; năm 2025 doanh thu là 404,0 tỷ so với chi phí 464,9 tỷ đồng. Lợi nhuận trước thuế lõi, không tính tự doanh, chỉ dao động trong khoảng 128 đến 221 tỷ đồng mỗi năm từ 2022 dù số tài khoản tăng gấp nhiều lần. Chi phí nền tảng và chi phí chung ước tính 197,5 tỷ đồng năm 2025 tương đương 7,3 triệu đồng mỗi năm cho mỗi tài khoản có từ 10 triệu đồng (DNSE Securities, 2026a; Vietcap Securities, 2026). Vì vậy, đưa tiền vào các tài khoản DNSE đã có là cách rẻ nhất để chia nhỏ chi phí này.

### 2.3 Điều gì đã thay đổi trong năm 2026

Ba điều khiến vấn đề trở nên cấp bách (Hình 2).

- **Tiền đang rời công ty chứng khoán.** Tiền của nhà đầu tư tại các công ty chứng khoán giảm từ 138,9 nghìn tỷ đồng ở Q3/2025 xuống 86,6 nghìn tỷ đồng ở Q2/2026, giảm 38% trong ba quý (VnEconomy, 2026). Đầu tháng 10/2026, nhóm Big4 trả 5,9% cho tiền gửi 12 tháng tại quầy, còn chứng chỉ tiền gửi trả 7,4% (Thi truong Tai chinh Tien te, 2026b).
- **Đối thủ đã bắt đầu cuộc đua tích lũy.** Ngày 23/4/2026 SSI quảng bá tính năng đầu tư chứng chỉ quỹ định kỳ tự động qua eSIP trong chương trình "Tích sản thảnh thơi" (SSI Securities, 2026). TCBS nâng cấp TCWealth thành danh mục theo mục tiêu, hơn 20.000 khách dùng thử trong hai tháng (TCBS, 2026). VPS ra mắt Smart Indexing ngày 11/8 (Tin nhanh Chung khoan, 2026) và VPBank ra mắt Hũ Mục Tiêu vào tháng 9 (VPBank, 2026). DNSE chưa có sản phẩm kế hoạch nào.
- **Ngân hàng mở đã có hạn chót.** Ngân hàng phải tuân thủ Thông tư 64/2024 về Open API chậm nhất ngày 1/3/2027 (State Bank of Vietnam, 2024). Điều này sẽ giúp việc đầu tư gắn với tiền lương dễ hơn cho bên nào đã có sẵn sản phẩm.

Trong khi đó, lợi nhuận trước thuế 6 tháng đầu 2026 của DNSE là 111,6 tỷ đồng, khoảng 1/5 kế hoạch 550 tỷ đồng của cả năm (DNSE Securities, 2026a; Vietstock, 2026a).

![Hình 2. Các đợt ra mắt kế hoạch tích lũy định kỳ và theo mục tiêu trong năm 2026 và hạn Open API của ngân hàng (trái); tiền của nhà đầu tư tại các công ty chứng khoán Việt Nam, nghìn tỷ đồng (phải)](outputs/round3/figures/why_now_timeline.png)

Nguồn: SSI Securities (2026); TCBS (2026); Tin nhanh Chung khoan (2026); Tuoi Tre (2026); VPBank (2026); State Bank of Vietnam (2024); VnEconomy (2026). Số liệu tiền nhà đầu tư Q4/2025 không được công bố.

### 2.4 Độ ổn định nay là ưu tiên đầu tiên

Vòng 2 kết luận phàn nàn về niềm tin là vấn đề đặc trưng trong review về DNSE. Để xem kết luận đó còn đúng không, nhóm đọc toàn bộ 58 review tiêu cực đăng năm 2026 (34 trên Google Play, 24 trên App Store) và mã hóa nguyên nhân thủ công, cho phép một review mang nhiều nguyên nhân (Hình 3; Phụ lục C). 48 review, tức 83% (khoảng tin cậy 95% từ 71% đến 90%), mô tả một thứ bị hỏng: văng app, treo và giật lag (45%), lệnh và giá (19%), nạp hoặc rút không được ghi có (17%), eKYC và mở tài khoản (17%), và đăng nhập hoặc OTP (14%). Điều khoản, phần thưởng và tố lừa đảo xuất hiện trong 19% (từ 11% đến 31%). Chín review được đăng ngày 4 và 5/3/2026, sau sự cố khiến lệnh bị treo hai tiếng do lỗi ở bước kiểm tra sức mua và sức bán trước khi lệnh được chuyển lên sàn (DNSE Securities, 2026e).

Vấn đề niềm tin chưa biến mất mà đã lùi xuống sau. Theo quy tắc từ khóa của Vòng 2, chủ đề niềm tin chiếm 55% review tiêu cực trên Google Play trong 6 tháng đầu 2025, giai đoạn tranh cãi về thưởng mở tài khoản, và 15% trong năm 2026. Cả hai cách đọc dẫn tới cùng một quy tắc thiết kế: Payday phải chạy đúng vào mọi ngày lương, và khi không chạy đúng thì khách phải thấy chuyện gì đã xảy ra và cần làm gì.

![Hình 3. Nguyên nhân trong 58 review tiêu cực về app DNSE, tháng 1 đến tháng 9/2026](outputs/round3/figures/reviews_2026_causes.png)

Nguồn: Google Play; App Store; nhóm tác giả mã hóa từng review.

### 2.5 Những gì giữ lại và những gì đã đổi so với Vòng 2

Cơ chế của Vòng 2 vẫn đứng vững: lệnh chuyển định kỳ từ ngân hàng nhận lương vào VA mang tên khách, kế hoạch do khách xác nhận, tái cân bằng chỉ bằng tiền mới, thông báo cho cơ quan quản lý và pilot ngẫu nhiên. Các con số, phần thưởng, lõi trái phiếu và định vị đã thay đổi (Bảng 1). Thay đổi lớn nhất nằm ở phương án kinh doanh. Vòng 2 giả định mọi người tích lũy đều góp đủ 18 tháng và đặt mục tiêu 85.000 TK trên 10 triệu đồng. Khi dùng cohort theo tháng, chi phí thực và tính đến việc một người cần 11 kỳ góp mới vượt 10 triệu đồng, kịch bản cơ sở đạt khoảng 42.000 tài khoản trên 10 triệu đồng vào tháng 36.

**Bảng 1. Những gì đã đổi so với Vòng 2 và lý do**

<!-- table: vi/slide05_what_changed -->
| Hạng mục | Vòng 2 | Vòng 3A và lý do |
|---|---|---|
| Rào cản chính | Niềm tin | Độ ổn định: 83% review tiêu cực năm 2026 mô tả một sự cố; niềm tin 19% |
| Phương án kinh doanh | Tĩnh: 150.000 người tích lũy góp đủ 18 tháng; mục tiêu 85.000 TK trên 10 triệu đồng | Cohort theo tháng trong 60 tháng: khoảng 42.000 TK trên 10 triệu đồng vào tháng 36 (27.100 + 14.871), vì một người cần 11 kỳ góp để vượt 10 triệu đồng |
| Pilot | 20.000 TK; làm tiếp nếu ghi danh đạt 15% | 45.000 TK; mở rộng từ 1,5%, dừng nếu dưới 1,0% (hòa vốn 1,0%) |
| Phần thưởng | Các bậc thưởng bằng tiền, gồm lãi tiền nhàn rỗi 4,3% | Gói giữ chân không bằng tiền; bậc thưởng bằng tiền sẽ tốn 41% doanh thu mỗi người tích lũy |
| Lõi trái phiếu | Trứng Vàng, trong đó có cả trái phiếu của chính DNSE | Chỉ trái phiếu do ngân hàng phát hành, để tránh xung đột lợi ích |
| Điểm khác biệt | Kích hoạt vào ngày lương | Chuyển tiền định kỳ đã phổ biến (VinaSIP từ 2021); Payday cạnh tranh bằng độ rộng tài sản và số đo dịch vụ công bố |
<!-- /table -->

Nguồn: KTQT FTUers (2026); mô hình cohort của nhóm; Thi truong Tai chinh Tien te (2021); DNSE Securities (2026c).

### 2.6 Điều kiện mà mọi giải pháp phải đáp ứng

Các phát hiện trên đặt ra sáu điều kiện cho thiết kế:
1. tiền mới phải đến từ tiền lương, không phải từ số dư đang có ở DNSE;
2. khách phải xác nhận kế hoạch và mọi thay đổi, vì DNSE không được quản lý tiền thay khách khi không có ủy quyền;
3. điều khoản, chi phí và tình trạng tiền của khách phải hiện rõ trước và sau mỗi bước;
4. kỳ góp phải được ghi có đúng hạn, và có phương án dự phòng khi không đúng hạn;
5. chi phí thu và phục vụ mỗi kỳ góp phải thấp hơn doanh thu kỳ góp đó mang lại trong suốt vòng đời;
6. sản phẩm phải được thông báo cho cơ quan quản lý trước khi ra mắt.

## 3. Người dùng mục tiêu và giá trị

### 3.1 Phân khúc và persona

Ba nhóm khách hiện hữu và khách mới tạo thành nền ra mắt và tăng trưởng (Bảng 2). Persona được dựng từ dữ liệu, không phải tiểu sử tưởng tượng: "việc cần làm" của họ là giả thuyết để pilot kiểm chứng.

- **P1, người đi làm có tài khoản ngủ,** là nhóm khách ra mắt. 1,43 triệu tài khoản không dùng sản phẩm nào trong tháng 12/2025; tệp khách của DNSE trẻ (Gen Z chiếm 31,5% số tài khoản giữa 2025; VnExpress, 2025) và 45,2% người trưởng thành trong lực lượng lao động nhận lương qua tài khoản (World Bank, 2025). Rào cản của họ là tính trì hoãn (O'Donoghue & Rabin, 1999) và sự nghi ngờ sau các tranh cãi về thưởng năm 2025.
- **P2, trader đang hoạt động,** muốn có một phần lõi dài hạn bên cạnh phần giao dịch. Tháng 12/2025 có 85.739 khách hoạt động; Q2/2026 DNSE đứng thứ hai về môi giới phái sinh với thị phần 25,38% (Hanoi Stock Exchange, 2026). Rủi ro là tiền của kế hoạch trôi ngược sang giao dịch.
- **P3, người mở tài khoản mới,** có thể lập kế hoạch ngay khi mở tài khoản. 6 tháng đầu 2026 DNSE mở khoảng 31.180 tài khoản mỗi tháng. Rào cản của họ là tâm lý săn thưởng và eKYC lỗi (17% review tiêu cực năm 2026).

Kênh doanh nghiệp (kế hoạch trích lương) đến sau: kênh này chỉ hoàn vốn nếu ít nhất 39% nhân viên tham gia sau buổi giới thiệu của phòng nhân sự (Mục 9.3).

**Bảng 2. Persona, quy mô và thông số mô hình**

<!-- table: vi/slide06_personas -->
|  | P1 Người đi làm có TK ngủ (khách ra mắt) | P2 Trader muốn thêm phần tích lũy | P3 Người mở TK mới |
|---|---|---|---|
| Quy mô | 1,43 triệu TK không dùng sản phẩm nào trong tháng 12/2025 | 85.739 khách hoạt động | Khoảng 31.180 TK mới mỗi tháng (H1/2026) |
| Việc cần làm (giả thuyết) | "Đưa một phần lương vào đầu tư mà không phải quyết lại mỗi tháng" | "Giữ một phần lõi dài hạn lớn dần trong khi vẫn giao dịch" | "Bắt đầu nhỏ và thấy nó chạy" |
| Rào cản (bằng chứng) | Trì hoãn; mất niềm tin sau đợt thưởng 2025 | Tiền của kế hoạch trôi ngược sang giao dịch | Săn thưởng; eKYC lỗi (17% review tiêu cực năm 2026) |
| Thông số mô hình (giả định) | 25% đi làm và liên hệ được; 2% ghi danh | 4% ghi danh trong 12 tháng | 2% cài đặt trong 60 ngày |
| Người tích lũy đến tháng 36 (cơ sở) | 6.836 | 3.430 | 18.708 |
<!-- /table -->

Nguồn: DNSE Securities (2026c); VnExpress (2026a); mô hình cohort của nhóm.

### 3.2 Quy mô: từ 1,51 triệu tài khoản đến người tích lũy

Hình 4 mô tả phễu ra mắt. Trong 1.512.920 tài khoản của DNSE tháng 12/2025, có 1.427.181 tài khoản không dùng sản phẩm nào. Nhóm giả định 1/4 trong số đó, tức 356.795 tài khoản, là người đi làm và liên hệ được, và 2% số được liên hệ sẽ ghi danh; cả hai con số đều là giả định mà pilot sẽ đo. Kết quả là 6.836 người tích lũy từ tài khoản ngủ đến tháng 36. Tuy vậy, phần lớn người tích lũy đến từ bước mở tài khoản: 18.708 trong 31.133 người ghi danh đến tháng 36 (60%) lập kế hoạch ngay khi mở tài khoản, so với 3.430 khách đang hoạt động và 2.160 nhân viên của doanh nghiệp đối tác.

![Hình 4. Từ 1,51 triệu tài khoản của DNSE đến người tích lũy từ tài khoản ngủ ở tháng 36 (trái); toàn bộ 31.133 người tích lũy đến tháng 36 theo kênh (phải), kịch bản cơ sở](outputs/round3/figures/sizing_funnel.png)

Nguồn: DNSE Securities (2026c); mô hình cohort của nhóm (giả định có ghi nhãn).

### 3.3 Khách hàng nói gì

Nhóm không kịp làm khảo sát, nên bằng chứng về nhu cầu là gián tiếp (Phụ lục D). Các khảo sát đã công bố cho thấy 77% nhà đầu tư Việt Nam thấy tự quản lý danh mục là khó và 81% muốn được tư vấn chuyên nghiệp (Nhan Dan, 2025; VnEconomy, 2025). Việc các đối thủ ra mắt sản phẩm cho thấy thị trường kỳ vọng có nhu cầu. Chính review của DNSE ủng hộ một số lựa chọn thiết kế cụ thể: năm 2022 một khách đề nghị DNSE hợp tác với ngân hàng để tạo mã định danh tài khoản vì nạp tiền cứ lỗi; nhiều khách phàn nàn ngân hàng đã trừ tiền nhưng tài khoản chứng khoán không nhận được; một review 5 sao gọi Tài khoản Không Ngủ là "the best"; và một review 1 sao kể việc mất 4% số tiền với Trứng Vàng kỳ hạn 1 tháng. Giới hạn rất rõ: review chủ yếu là phàn nàn, và trong số nhóm tìm được, chưa review nào xin một kế hoạch góp định kỳ.

### 3.4 Giá trị cho từng bên liên quan

Payday phải tạo giá trị cho năm bên, không chỉ cho người tích lũy (Bảng 3). Ngân hàng đối tác quan trọng nhất về mặt kinh tế: tiền góp nằm trong VA của ngân hàng, nên ngân hàng có lý do miễn phí thu hộ, đây là đòn bẩy rẻ nhất trong mô hình (Mục 7.4).

**Bảng 3. Giá trị cho từng bên liên quan**

<!-- table: vi/report_value -->
| Bên liên quan | Payday mang lại gì | Bằng chứng |
|---|---|---|
| Khách hàng | Kế hoạch góp hằng tháng từ 500.000 đồng cho một mục tiêu có tên; trái phiếu ngân hàng cho mục tiêu ngắn, quỹ và ETF cho mục tiêu dài; khách xác nhận mọi thay đổi; không phí nền tảng; tạm dừng, bỏ qua hoặc rút bằng một chạm | Trứng Vàng trả 6,20–7,60% theo kỳ hạn, từ 100.000 đồng; tiền gửi 12 tháng ở Big4 trả 5,9%; coupon trái phiếu chịu thuế 5% |
| DNSE | TK có tiền với chi phí ròng khoảng 1,3 triệu đồng mỗi TK; hạ tầng thanh toán xử lý luôn lỗi ghi có khi nạp tiền | 14.871 TK mới trên 10 triệu đồng vào tháng 36 (cơ sở); tiền nạp không được ghi có trong 17% review tiêu cực năm 2026 |
| Ngân hàng đối tác | Tiền góp nằm ở VA của ngân hàng dưới dạng số dư tiền gửi thanh toán, nên ngân hàng có lý do miễn phí thu hộ | Giá niêm yết 3.300 đồng mỗi kỳ góp, gồm VAT; miễn khoản phí này nâng trần CAC từ 128.000 lên 199.000 đồng |
| Công ty quản lý quỹ | Dòng tiền mua định kỳ mới từ 1,51 triệu TK của DNSE | Các quỹ trái phiếu và cổ phiếu đã so sánh không thu phí mua; DNSE đã đăng ký đại lý phân phối |
| Cơ quan quản lý | Tư vấn đúng quy định về mức độ phù hợp, có người hành nghề ký duyệt, không quản lý ủy thác và có số đo dịch vụ công bố | Thông tư 121/2020, Điều 4, 24 và 27; Luật Chứng khoán 2019, Điều 72 |
<!-- /table -->

Nguồn: DNSE Securities (n.d.-a, n.d.-b); Thi truong Tai chinh Tien te (2026b); VPBank (2024); Ministry of Finance (2020); National Assembly of Vietnam (2019); mô hình cohort của nhóm.

## 4. Thiết kế sản phẩm

### 4.1 Từ phát hiện đến thiết kế

Mỗi lựa chọn thiết kế đều truy được về bằng chứng và về một chỉ số mà pilot đo (Bảng 4). Ba lựa chọn đến từ các nguyên nhân gốc ở Vòng 2, một từ dữ liệu review 2026 và một từ kinh tế của các món nhỏ: với lợi suất ròng 0,44%, một kỳ góp 1 triệu đồng mang về cho DNSE khoảng 368 đồng mỗi tháng, trong khi giá niêm yết để ngân hàng thu hộ kỳ góp đó là 3.300 đồng.

**Bảng 4. Phát hiện, quyết định thiết kế và chỉ số chịu tác động**

<!-- table: vi/slide04_insight_design -->
| Phát hiện | Bằng chứng | Quyết định thiết kế | KPI chịu tác động |
|---|---|---|---|
| TK được mở nhưng không có tiền | 98% số TK có dưới 10 triệu đồng | Kế hoạch hằng tháng, nạp bằng lệnh chuyển định kỳ từ ngân hàng nhận lương | TK mới trên 10 triệu đồng: +14.871 vào tháng 36 |
| Ý định dừng lại khi không có kế hoạch | 77% nhà đầu tư thấy tự quản lý danh mục là khó | Kế hoạch theo kỳ hạn mục tiêu, do người hành nghề có chứng chỉ ký và khách xác nhận | Góp 3 kỳ liền: 81% (dừng nếu dưới 60%) |
| Thưởng có điều kiện làm gãy niềm tin | Chủ đề niềm tin: 55% review tiêu cực trên Google Play, H1/2025 | Không thưởng tiền; mọi điều khoản trên một màn hình; rút miễn phí | Chủ đề niềm tin dưới 10% review về Payday |
| Cập nhật 2026: độ ổn định nay là vấn đề chính | 83% review tiêu cực năm 2026 mô tả một thứ bị hỏng | Bộ lập lịch của Payday tách khỏi bước kiểm tra trước giao dịch; cổng ra mắt 99,5% | 99,5% kỳ góp được ghi có trong cùng ngày làm việc |
| Món nhỏ gánh chi phí đơn vị nặng | Kỳ góp 1 triệu đồng chịu phí ngân hàng 3.300 đồng và mang về 368 đồng mỗi tháng | Cổng 0: mục tiêu phí thu hộ 0 đồng | Trần CAC tăng từ 128.000 lên 199.000 đồng |
<!-- /table -->

Nguồn: DNSE Securities (2026c); Nhan Dan (2025); review trên Google Play và App Store do nhóm mã hóa; VPBank (2024); mô hình cohort của nhóm.

### 4.2 Payday hoạt động thế nào

Payday chạy theo bốn bước (Hình 5). Thứ nhất, Ensa hỏi mục tiêu, kỳ hạn, mức chịu lỗ và thu nhập, rồi đề xuất một danh mục mẫu do người hành nghề có chứng chỉ thiết kế; khách xác nhận. Thứ hai, khách lập một lệnh chuyển định kỳ trong app ngân hàng nhận lương tới VA mang tên chính mình. Thứ ba, tiền chờ ở Tài khoản Không Ngủ, tài khoản tiền nhàn rỗi có lãi của DNSE, và thường được đầu tư trong ngày làm việc kế tiếp. Thứ tư, mỗi kỳ góp mua lớp tài sản đang thấp nhất so với tỷ trọng mục tiêu, nên kế hoạch tự tái cân bằng mà không phải bán. Song song là một gói giữ chân không bằng tiền và một bộ cơ chế bảo đảm niềm tin.

![Hình 5. Payday hoạt động thế nào: tư vấn, nạp tiền vào ngày lương, giữ tiền ngắn hạn, đầu tư tiền mới](outputs/round3/figures/solution_overview.png)

Nguồn: thiết kế của nhóm (vẽ lại Figure 7 của Vòng 2, bỏ các bậc thưởng bằng tiền).

### 4.3 MVP và những gì cố ý bỏ ra

MVP có 11 tính năng (Bảng 5). Sáu thứ được cố ý loại ra:
- **margin và đòn bẩy,** kể cả dùng làm phần thưởng, vì mâu thuẫn với mục đích tiết kiệm; Điều 27 Thông tư 121/2020 giới hạn việc cho vay của công ty chứng khoán trong margin và một số mục đích được quy định, và khoản phạt năm 2026 của DNSE có các hạng mục về giao dịch ký quỹ vượt sức mua và cho vay trên chứng khoán không đủ điều kiện (Market Times, 2026);
- **cổ phiếu đơn lẻ và phái sinh,** vì lý do phù hợp và niềm tin;
- **trái phiếu do chính DNSE phát hành** trong danh mục mặc định, để tránh xung đột lợi ích (Mục 4.4);
- **thưởng tiền khi mở tài khoản, thưởng có điều kiện và các bậc thưởng bằng tiền do DNSE trả** (Mục 4.5);
- **quản lý ủy thác** và mọi thay đổi kế hoạch không có xác nhận của khách, điều mà Điều 4 Thông tư 121/2020 và Điều 72 Luật Chứng khoán 2019 không cho phép với công ty môi giới không có ủy quyền;
- **góp theo % lương qua Open API của ngân hàng,** để đến Phase 3 (Mục 9).

**Bảng 5. Tính năng của MVP**

<!-- table: vi/report_features -->
| # | Tính năng | Ghi chú thiết kế |
|---|---|---|
| F1 | Đặt mục tiêu: loại, số tiền và ngày | Hiện số tiền cần góp mỗi tháng, chưa tính lợi nhuận đầu tư |
| F2 | Đánh giá mức độ phù hợp: kỳ hạn, phản ứng khi lỗ, thu nhập | Thông tư 121/2020, Điều 24; mọi khuyến nghị đều được lưu log |
| F3 | Kế hoạch theo kỳ hạn mục tiêu | Danh mục mẫu do người hành nghề có chứng chỉ ký; khách xác nhận |
| F4 | VA mang tên khách và hướng dẫn lập lệnh chuyển định kỳ (link mở app ngân hàng và QR) | Mục tiêu thiết kế: cài đặt xong trong 5 phút, số bước không nhiều hơn SIP trên VCB Digibank |
| F5 | Mỗi kỳ góp mua lớp tài sản đang thiếu tỷ trọng nhất | Chỉ dùng tiền mới, không bán; ETF mua theo lô 100 chứng chỉ khi đủ tiền |
| F6 | Tài khoản Không Ngủ làm nơi tiền chờ | Tiền thường được đầu tư trong ngày làm việc kế tiếp |
| F7 | Dashboard: tiến độ mục tiêu, tài sản theo lớp, tiền đang nằm ở đâu, phí đã trả | – |
| F8 | Gói giữ chân không bằng tiền | Chuỗi kỳ góp; bỏ qua miễn phí 1 tháng mỗi năm; nhắc ngày lương có tên mục tiêu; ưu tiên mua đợt Trứng Vàng mới; Ensa rà kế hoạch ở tháng 6 |
| F9 | Tạm dừng, bỏ qua hoặc hủy bằng một chạm; rút miễn phí về ngân hàng liên kết | Chuyển tiền kế hoạch sang sức mua phải qua một bước riêng, có nhắc mục tiêu |
| F10 | Thông báo: đã nhận, đã đầu tư, chưa nhận, lương về trễ | Cửa sổ chờ 5 ngày; chuỗi kỳ góp không mất trong thời gian chờ |
| F11 | Trang số đo dịch vụ hằng tháng | Bảy cam kết ở Bảng 7 |
<!-- /table -->

Nguồn: thiết kế của nhóm; Ministry of Finance (2020).

### 4.4 Danh mục mặc định theo kỳ hạn mục tiêu

Cơ cấu kế hoạch phụ thuộc vào thời điểm khách cần tiền (Bảng 6). Mục tiêu dưới một năm chỉ nắm trái phiếu Trứng Vàng kỳ hạn 1 đến 6 tháng, đáo hạn trước ngày mục tiêu. Mục tiêu từ một đến ba năm thêm quỹ trái phiếu, chọn trong số các quỹ không thu phí bán sau 12 tháng. Mục tiêu từ ba năm trở lên nắm tối đa 40% quỹ cổ phiếu và ETF VN30. Trong 12 tháng cuối trước mục tiêu, tiền mới chỉ vào Trứng Vàng và không bán gì.

Một quy tắc ràng buộc cả bảng: **không xếp sản phẩm có chi phí rút trước hạn rơi vào trong kỳ hạn mục tiêu.** Bán trái phiếu Trứng Vàng trước thời gian nắm giữ tối thiểu chỉ được hưởng 2,0%/năm (DNSE Securities, n.d.-a), còn quỹ trái phiếu của VCBF thu 2,0% nếu bán trong 3 tháng đầu và 1,0% nếu bán từ tháng 3 đến tháng 12 (VCBF, 2026). Trứng Vàng mặc định tự tái tục và chỉ gửi email cho khách sau khi đã tái tục (DNSE Securities, n.d.-a); trong Payday, khoản tái tục vẫn phải đáo hạn trước ngày mục tiêu, có thông báo trước 3 ngày và tắt được bằng một chạm.

Lõi trái phiếu chỉ dùng trái phiếu do ngân hàng phát hành. Năm 2025, Trứng Vàng được phân bổ vào trái phiếu do chính DNSE, Agribank và BVBank phát hành (DNSE Securities, 2026c). Loại trái phiếu DNSE khỏi danh mục mặc định làm dòng tiền lũy kế 5 năm trong mô hình giảm khoảng 4 tỷ đồng. Đó là cái giá nhỏ so với xung đột lợi ích khi bán nợ của chính công ty môi giới cho người mới bắt đầu tiết kiệm. Kế hoạch 2026 của DNSE hợp tác với Vietcombank, VietinBank và BIDV về trái phiếu cho Trứng Vàng và chứng chỉ quỹ sẽ mở rộng nguồn cung (DNSE Securities, 2026f).

Phép thử tương tự áp dụng cho quỹ trái phiếu. Cuối tháng 8/2026, quỹ trái phiếu của VCBF nắm trái phiếu DSE125018 của DNSE với tỷ trọng 6,97% giá trị tài sản ròng (VCBF, 2026). Công ty quản lý quỹ tự chọn danh mục, độc lập với DNSE, nên xung đột yếu hơn so với việc DNSE bán trực tiếp trái phiếu của mình. Dù vậy, màn hình kế hoạch nên hiện rõ mọi khoản đầu tư vào trái phiếu DNSE trong quỹ, và danh mục mặc định nên ưu tiên các quỹ không nắm trái phiếu này. Hợp đồng với công ty quỹ ở Phase 0 là nơi chốt vấn đề này.

**Bảng 6. Danh mục mặc định theo kỳ hạn mục tiêu**

<!-- table: vi/slide07_glide_path -->
| Kỳ hạn mục tiêu | Trứng Vàng (trái phiếu ngân hàng) | Quỹ trái phiếu | Quỹ cổ phiếu | ETF VN30 |
|---|---|---|---|---|
| Dưới 1 năm | 100% | – | – | – |
| 1 đến 3 năm | 50% | 50% | – | – |
| Từ 3 năm trở lên | 30% | 30% | 20% | 20% |
| 12 tháng cuối trước mục tiêu | Chỉ dùng tiền mới, vào Trứng Vàng | Không bán | Không bán | Không bán |
<!-- /table -->

Nguồn: thiết kế của nhóm; DNSE Securities (n.d.-a, n.d.-b); VCBF (2026).

### 4.5 Giữ chân không bằng tiền

Vòng 2 đề xuất các bậc thưởng bằng tiền ở kỳ góp thứ 3, 6 và 12. Mô hình cho thấy chúng không tự bù được chi phí: ngay cả phiên bản thu nhỏ cũng tốn 41% giá trị hiện tại của doanh thu mỗi người tích lũy, và kéo trần chi phí thu hút xuống dưới chi phí tiếp cận một người từ tài khoản ngủ (Phụ lục B, Bảng B2). Vì vậy gói giữ chân không dùng tiền: chuỗi kỳ góp hiển thị rõ, được bỏ qua miễn phí 1 tháng mỗi năm, lời nhắc ngày lương có tên mục tiêu, quyền ưu tiên mua các đợt Trứng Vàng mới và một buổi Ensa rà kế hoạch ở tháng thứ 6. Thí nghiệm thực địa cho thấy lời nhắc có nêu mục tiêu làm tăng tiết kiệm (Karlan et al., 2016). Một món quà tiền nhỏ chỉ được giữ lại dưới dạng thử nghiệm ở một nhánh riêng: nó chỉ có lời nếu ngân hàng miễn phí thu hộ và tỷ lệ người đạt 12 kỳ góp tăng từ 64,5% lên 73,3%. Mọi ưu đãi lãi đều có trần 50 triệu đồng.

### 4.6 Cơ chế niềm tin và số đo công bố

Bảy cam kết biến niềm tin thành những con số DNSE công bố theo lịch (Bảng 7). Trong phạm vi nhóm tìm hiểu, chưa đơn vị nào ở Việt Nam công bố tỷ lệ chuyển tiền thành công hay thời gian rút tiền, nên đây là một trong hai điểm khác biệt bền vững của Payday (Mục 6).

**Bảng 7. Cam kết và số đo DNSE sẽ công bố**

<!-- table: vi/appG3_trust_metrics -->
| Cam kết | Khách thấy gì | Số đo công bố | Mục tiêu | Tần suất | Phụ trách |
|---|---|---|---|---|---|
| Tiền về đúng hẹn | Thông báo "đã nhận" vài phút sau khi ngân hàng ghi có | Tỷ lệ kỳ góp theo lịch được ghi có trong cùng ngày làm việc | ≥ 99,5% (cổng ra mắt) | Hằng tháng | CTO |
| Tiền được đầu tư nhanh | Trạng thái "đã đầu tư" kèm tài sản đã mua | Thời gian trung vị từ khi ghi có đến khi đầu tư | ≤ 1 ngày làm việc | Hằng tháng | CTO |
| Rút tiền nhanh và miễn phí | "Arrives by 22:00 today" khi bán Trứng Vàng trong khung 09:00–14:30 (FAQ của DNSE: khoảng 21:00–22:00 ngày bán); ngày thanh toán của quỹ hiện trước khi xác nhận | Thời gian trung vị từ lệnh rút đến khi tiền vào ngân hàng liên kết | Trong ngày với lệnh bán Trứng Vàng | Hằng tháng | Trưởng sản phẩm |
| Rời đi dễ dàng | Tạm dừng, bỏ qua hoặc hủy bằng một chạm | Tỷ lệ lệnh hủy hoàn tất trong app, không phải gọi điện | 100% | Hằng tháng | Trưởng sản phẩm |
| Không chi phí ẩn | Một màn hình liệt kê mọi phí và thuế bằng đồng trước khi xác nhận | Tỷ lệ kế hoạch được xác nhận sau khi đã hiện màn hình phí (kiểm toán) | 100% | Hằng quý | Pháp chế và tuân thủ |
| Sự cố được nhận trách nhiệm, không bị giấu | Trang trạng thái và ghi chú sau sự cố | Sự cố ảnh hưởng kỳ góp có ghi chú công bố trong 5 ngày làm việc | 100% | Mỗi sự cố | CTO |
| Phàn nàn được đếm | - | Tỷ trọng chủ đề niềm tin trong review tiêu cực liên quan Payday | < 10% | Hằng quý | CSKH |
<!-- /table -->

Nguồn: thiết kế của nhóm; DNSE Securities (n.d.-a).

### 4.7 Yêu cầu về độ ổn định

Độ ổn định là cổng ra mắt, không phải một tính năng:
- ít nhất 99,5% kỳ góp được ghi có trong cùng ngày làm việc, chứng minh bằng các lần chạy thử ngày lương với tiền của nhân viên trước pilot và đo hằng tháng sau khi ra mắt, với ngân sách lỗi 0,5%;
- bộ lập lịch kỳ góp tách khỏi bước kiểm tra sức mua trước giao dịch, bước đã lỗi ngày 4/3/2026, đúng hôm VN-Index biến động tới 67 điểm trong phiên (Pinetree Securities, 2026);
- xử lý idempotent và đối soát VA hằng ngày; tiền không khớp được giữ ở Tài khoản Không Ngủ và rà tay trong một ngày làm việc;
- không phát hành app trong những ngày trước các ngày góp cao điểm, phát hành theo đợt 5%, 25% rồi 100%, và theo dõi lỗi theo phiên bản app, sau khi 7 review tiêu cực cùng chỉ vào một bản iOS (2.113.28);
- trang trạng thái và ghi chú sau sự cố trong vòng 5 ngày làm việc.

### 4.8 Phù hợp với quy định

Thiết kế nằm trong các quy định về tư vấn và cho vay (Bảng 8). Luồng tư vấn đáp ứng yêu cầu về mức độ phù hợp tại Điều 24 Thông tư 121/2020, vì Ensa chỉ thu thập thông tin, người hành nghề có chứng chỉ ký danh mục mẫu và mọi khuyến nghị đều được lưu log. Thông báo cho cơ quan quản lý là điều kiện ra mắt chứ không phải thủ tục: trong khoản phạt 802,5 triệu đồng của DNSE tháng 8/2026, có 275 triệu đồng là vì ba dịch vụ được cung cấp mà không báo cáo UBCKNN (Market Times, 2026). Hai điểm phụ thuộc cần làm sớm. DNSE từng tạm dừng mở mới Trứng Vàng theo yêu cầu của cơ quan quản lý vào tháng 12/2023 (DNSE Securities, 2023), nên vai trò của Trứng Vàng trong một kế hoạch có tư vấn cần được trao đổi với UBCKNN trước khi ra mắt, với quỹ trái phiếu làm lõi dự phòng. Ngoài ra, DNSE dù đã đăng ký đại lý phân phối chứng chỉ quỹ nhưng chưa có tên trong danh sách đại lý của các công ty quỹ nhóm đã kiểm, nên hợp đồng với công ty quỹ phải nằm ở Phase 0.

**Bảng 8. Quy định và cách thiết kế đáp ứng**

<!-- table: vi/appE1_legal -->
| Yêu cầu | Quy định | Cách thiết kế đáp ứng | Trạng thái |
|---|---|---|---|
| Tư vấn phải phù hợp với khách | Thông tư 121/2020/TT-BTC, Điều 24 (thông tin khách hàng khi tư vấn đầu tư) | Ensa ghi nhận mục tiêu, kỳ hạn, thu nhập và mức chịu lỗ; người hành nghề có chứng chỉ thiết kế và ký danh mục mẫu; lưu log tư vấn | Áp dụng |
| Không đầu tư thay khách khi không có ủy quyền | Thông tư 121/2020/TT-BTC, Điều 4 | Khách xác nhận kế hoạch và mọi thay đổi; hệ thống chỉ đầu tư tiền mới đúng theo kế hoạch đã xác nhận | Áp dụng |
| Chỉ cho vay ký quỹ và các mục đích được quy định | Thông tư 121/2020/TT-BTC, Điều 27 | Không cấp hạn mức tín dụng trên khoản tiết kiệm; margin không dùng làm phần thưởng | Loại |
| Quản lý danh mục không phải nghiệp vụ của công ty chứng khoán | Luật Chứng khoán 2019, Điều 72 | Không làm dịch vụ ủy thác; bản quản lý trọn gói chỉ qua công ty quản lý quỹ được cấp phép | Loại (Phase 4 qua công ty quỹ) |
| Open API ngân hàng | Thông tư 64/2024/TT-NHNN: ngân hàng phải tuân thủ chậm nhất ngày 1/3/2027; sự đồng ý của khách có hiệu lực tối đa 180 ngày | Phase 1 dùng lệnh chuyển định kỳ do khách tự lập trong app ngân hàng; góp theo % lương chỉ sau khi có thỏa thuận với ngân hàng (Phase 3) | Giai đoạn sau |
| Dịch vụ mới phải được báo cáo | Quyết định 461/QĐ-XPHC (17/8/2026): 275 triệu trong khoản phạt 802,5 triệu đồng là vì các dịch vụ không báo cáo UBCKNN | Thông báo UBCKNN trước khi ra mắt; xác nhận bằng văn bản là điều kiện của Cổng 0 | Cổng ra mắt |
| Lịch sử quản lý của Trứng Vàng | Trứng Vàng bị tạm dừng mở mới theo yêu cầu của cơ quan quản lý từ ngày 25/12/2023 (thông báo của DNSE) | Tham vấn trước UBCKNN về vai trò của Trứng Vàng trong Payday; chuẩn bị sẵn quỹ trái phiếu làm lõi thay thế | Tham vấn trước |
| Phân phối chứng chỉ quỹ | DNSE đã đăng ký đại lý phân phối chứng chỉ quỹ (15/12/2021) nhưng chưa có tên trong danh sách đại lý của SSIAM, Dragon Capital hay VCBF | Ký hợp đồng phân phối với 1–2 công ty quỹ ở Phase 0; nếu chậm thì ra mắt với Trứng Vàng và ETF | Phụ thuộc ở Phase 0 |
<!-- /table -->

Nguồn: Ministry of Finance (2020); National Assembly of Vietnam (2019); State Bank of Vietnam (2024); Market Times (2026); DNSE Securities (2023, n.d.-b).

## 5. Minh họa giải pháp

### 5.1 Hành trình và các khoảnh khắc quyết định

90 ngày đầu của một người tích lũy đi qua sáu chặng: thấy lời mời, lập kế hoạch, cài đặt dòng tiền, ngày lương đầu tiên, tạo thói quen, và rút tiền hoặc tiếp tục (Phụ lục E). Ba khoảnh khắc quyết định khách có tin sản phẩm hay không: tiền vào lần đầu, tiền ra lần đầu và sự cố đầu tiên (Bảng 9). Một sự cố được xử lý tốt có thể tạo nhiều niềm tin hơn một lần chạy trơn tru, nên các màn hình xử lý sự cố được thiết kế từ trước chứ không để lại cho bộ phận CSKH.

**Bảng 9. Các khoảnh khắc quyết định**

<!-- table: vi/slide08_moments_of_truth -->
| Khoảnh khắc quyết định | Khách thấy gì | Số đo công bố |
|---|---|---|
| Tiền vào lần đầu | "Đã nhận" sau vài phút; đầu tư trong ngày làm việc kế tiếp | Kỳ góp được ghi có trong cùng ngày làm việc: ≥99,5% |
| Tiền ra lần đầu | Giờ tiền về và chi phí bằng đồng hiện trước khi xác nhận; rút miễn phí về ngân hàng liên kết | Thời gian trung vị từ lệnh rút đến khi tiền về ngân hàng |
| Sự cố đầu tiên | Giữ chuỗi kỳ góp; một bước tiếp theo rõ ràng: chuyển ngay hoặc bỏ qua tháng này | Ghi chú sự cố trong 5 ngày làm việc |
<!-- /table -->

Nguồn: thiết kế của nhóm.

### 5.2 Màn hình và câu chữ trên giao diện

Sáu màn hình đưa người tích lũy từ lúc đặt mục tiêu đến mốc 90 ngày (Hình 6). Người dùng chọn một mục tiêu, ví dụ mua nhà với 36 triệu đồng trước tháng 10/2029, và thấy rằng góp khoảng 1 triệu đồng mỗi tháng là đủ, chưa tính lợi nhuận đầu tư. Tiếp theo là vài câu đánh giá mức độ phù hợp, có hiện lý do pháp lý. Màn hình kế hoạch hiện cơ cấu, mức lỗ của một tháng xấu tính bằng đồng và mọi khoản phí; màn hình thứ tư cấp số tài khoản riêng và mở app ngân hàng. Vào ngày lương khách thấy tiền đã nhận và đã đầu tư, và ở ngày 90 chuỗi kỳ góp mở khóa quyền ưu tiên mua các đợt Trứng Vàng mới. Bốn màn hình khác xử lý các trường hợp tiền chưa về, lương về trễ, bỏ qua hoặc tạm dừng một tháng và rút tiền về ngân hàng (Hình 7). Câu chữ theo các quy tắc đơn giản: tiêu đề màn hình viết hoa theo kiểu tiêu đề, nút bấm là động từ, thông báo lỗi nói rõ chuyện gì xảy ra, vì sao và cần làm gì, số tiền luôn tính bằng đồng, và không dùng từ "reward". Bản wireframe dùng tiếng Anh vì deck Vòng 3A bằng tiếng Anh; bản chạy thật sẽ dùng tiếng Việt.

![Hình 6. Wireframe độ trung thực thấp của sáu màn hình chính; giá trị trong ngoặc vuông do app thật điền vào](outputs/round3/figures/wireframes_journey.png)

Nguồn: thiết kế của nhóm.

![Hình 7. Wireframe độ trung thực thấp của bốn màn hình lỗi và tình huống đặc biệt](outputs/round3/figures/wireframes_errors.png)

Nguồn: thiết kế của nhóm; DNSE Securities (n.d.-a) cho quy tắc bán trước hạn.

### 5.3 Service blueprint và xử lý sự cố

Phía sau các màn hình, service blueprint mô tả từng bước qua bằng chứng hữu hình, hành động của khách, frontstage, backstage và quy trình hỗ trợ, kèm điểm quyết định, cách xử lý sự cố và người phụ trách từng bước (Hình 8). Có hai quyết định tự động: tiền đã về trước hạn chờ hay chưa, và đã đủ tiền mua một lô ETF hay chưa. Mỗi sự cố đều có phương án dự phòng và người phụ trách (Bảng 10). Phần phải xây mới chỉ gồm VA và bộ lập lịch; Ensa, Trứng Vàng, Tài khoản Không Ngủ và giao dịch ETF đều dùng lại cái đã có.

![Hình 8. Service blueprint của một chu kỳ ngày lương](outputs/round3/figures/service_blueprint.png)

Nguồn: thiết kế của nhóm; DNSE Securities (2026e).

**Bảng 10. Xử lý sự cố**

<!-- table: vi/slide09_failure_handling -->
| Khi khâu này lỗi | Điều xảy ra | Phụ trách |
|---|---|---|
| Tiền chưa về trước hạn chờ (ngày 15) | Gợi ý bỏ qua tháng này; giữ chuỗi kỳ góp | CTO; Vận hành |
| Lệnh mua lỗi | Thử lại ở phiên sau; tiền vẫn sinh lãi ở Tài khoản Không Ngủ | CTO |
| Lỡ hai tháng | Gợi ý tạm dừng thay vì hủy | Trưởng sản phẩm |
| Chuyển tiền về ngân hàng lỗi | Tiền quay về phần tiền mặt của kế hoạch; gọi lại khách trong 1 ngày làm việc | CSKH |
<!-- /table -->

Nguồn: thiết kế của nhóm.

## 6. Định vị cạnh tranh

### 6.1 Cuộc đua tích lũy

Trong 20 sản phẩm đối thủ nhóm đã rà soát, nhiều sản phẩm đã có những thứ mà Vòng 2 coi là mới (Bảng 11; Phụ lục A). Chuyển tiền định kỳ từ ngân hàng đã là chuẩn chung: VinaSIP của VinaCapital dùng lệnh chuyển định kỳ từ năm 2021, từ 500.000 đồng mỗi tháng (Thi truong Tai chinh Tien te, 2021), và khách Vietcombank có thể mua quỹ của VCBF từ 100.000 đồng mỗi kỳ trên VCB Digibank (VCBF, n.d.). Kế hoạch theo mục tiêu cũng đã có: kế hoạch hưu trí của VNDIRECT kết hợp quỹ trái phiếu và quỹ cổ phiếu theo tỷ lệ 80/20, từ 1 triệu đồng (VNDIRECT, n.d.), còn TCWealth của TCBS dựng danh mục theo mục tiêu (TCBS, 2026). Thưởng duy trì cũng đã xuất hiện: KBSV từng tặng voucher 50.000 đồng mỗi tháng cho việc mua định kỳ (KBSV, n.d.). Ở phân khúc cao, VPS Smart Indexing bắt đầu từ 50 triệu đồng cộng 10 triệu đồng mỗi tháng, thu phí 0,5%/năm và quyết định thay khách (Tuoi Tre, 2026).

**Bảng 11. Sản phẩm đối thủ nhóm đã kiểm, 16/10/2026**

<!-- table: vi/appC1_competitors -->
| Sản phẩm | Tài sản | Tối thiểu | Định kỳ | Ai quyết định | Phí và ưu đãi | Nguồn |
|---|---|---|---|---|---|---|
| VPS Smart Indexing (11/8/2026) | Cổ phiếu, mô phỏng chỉ số trực tiếp | 50 triệu đồng, sau đó 10 triệu mỗi tháng | Có | VPS (ủy thác) | 0,5%/năm | Tuoi Tre (2026); Tin nhanh Chung khoan (2026) |
| SSI eSIP (chương trình từ 23/4/2026) | Quỹ của SSIAM và Dragon Capital | Không công bố | Có | Khách hàng | Voucher 50.000 đồng cho khách mới mua 1 triệu đồng qua eSIP | SSI Securities (2026); Bao Phap Luat (2026) |
| TCBS TCWealth (Q2/2026) | Danh mục theo mục tiêu | Không tìm thấy | Không nêu | Không nêu | Không tìm thấy | TCBS (2026) |
| TCBS iPower | Tiền nhàn rỗi | 5 triệu đồng | Tự động | – | Tới 6%/năm (bảng so sánh 2025) | DNSE Securities (2025) |
| VNDIRECT Tích sản hưu trí | Quỹ trái phiếu và cổ phiếu, 80/20 trong 10 năm | 1 triệu đồng | Có | Khách hàng | 0,1%/năm (miễn phí đến 12/2025) | VNDIRECT (n.d.) |
| VinaCapital VinaSIP (6/2021) | Một quỹ VinaCapital cho mỗi kế hoạch | 500.000 đồng mỗi tháng | Có, lệnh chuyển định kỳ từ ngân hàng | Khách hàng | – | Thi truong Tai chinh Tien te (2021) |
| VCB Digibank SIP (VCBF) | Quỹ của VCBF | 100.000 đồng mỗi kỳ | Có | Khách hàng | Phí bán ưu đãi cho SIP | VCBF (n.d.) |
| VPBank Hũ Mục Tiêu (9/2026) | Tiền gửi | Không tìm thấy | Có, theo ngày, tuần hoặc tháng | Khách hàng | – | VPBank (2026) |
| KBSV đầu tư định kỳ | Cổ phiếu | – | Có | Khách hàng | Voucher 50.000 đồng mỗi tháng, tối đa 600.000 đồng (4/2025 đến 3/2026) | KBSV (n.d.) |
| DNSE hiện nay | Tài khoản Không Ngủ (1,8–4,3% trên tiền nhàn rỗi); trái phiếu Trứng Vàng (6,20–7,60%) | Trứng Vàng từ 100.000 đồng | Chưa có sản phẩm kế hoạch | Khách hàng | Không phí giao dịch cổ phiếu | DNSE Securities (2026b, 2026d, n.d.-b) |
| Payday Portfolio (đề xuất) | Trái phiếu ngân hàng, quỹ trái phiếu và cổ phiếu, ETF VN30 | 500.000 đồng mỗi tháng | Có, lệnh chuyển định kỳ vào VA mang tên khách | Khách xác nhận kế hoạch do người hành nghề ký | Không phí nền tảng | Thiết kế của nhóm |
<!-- /table -->

Nguồn: như ghi trong bảng; dựa trên thông tin sản phẩm công khai đến ngày 16/10/2026. Cũng đã rà soát tại bàn nhưng chưa kiểm lại: TCBS iTracker, Fundmart và iSave; VNDIRECT VNDGO; VPBankS NEO Invest và Tích sản cổ phiếu; MBS Mobile; Techcombank iFund; MoMo Túi Thần Tài; Tikop; Finhay cùng DFVN.

### 6.2 Payday đứng ở đâu

Payday không tự nhận là người đi đầu. Trong các sản phẩm nhóm tìm được, chưa sản phẩm nào kết hợp trái phiếu ngân hàng, quỹ trái phiếu, quỹ cổ phiếu và ETF trong một kế hoạch do khách xác nhận với mức từ 500.000 đồng, và cũng chưa sản phẩm nào công bố tỷ lệ chuyển tiền thành công hay thời gian rút tiền (Hình 9). Lợi thế bền vững của Payday nằm ở phân phối và bằng chứng: chi phí gần như bằng 0 để tiếp cận 1,5 triệu tài khoản đã qua eKYC, và các số đo dịch vụ trả lời đúng vấn đề độ ổn định và niềm tin mà dữ liệu chỉ ra. Đối thủ khó nhất là các ngân hàng, vì họ giữ tài khoản nhận lương và niềm tin của khách; Payday cạnh tranh bằng độ rộng tài sản trong một app và bằng việc nằm ngay cạnh phần giao dịch của khách.

![Hình 9. Mức tối thiểu để bắt đầu so với số loại tài sản trong một kế hoạch; chỉ vẽ các sản phẩm có mức tối thiểu đã kiểm](outputs/round3/figures/positioning_map.png)

Nguồn: Tuoi Tre (2026); VNDIRECT (n.d.); VCBF (n.d.); Thi truong Tai chinh Tien te (2021); thiết kế của nhóm.

## 7. Phương án kinh doanh

### 7.1 Cấu trúc và thông số mô hình

Mô hình theo dõi cohort người tích lũy mới của từng tháng trong 60 tháng (Phụ lục A, Bảng A2). Với mỗi cohort, mô hình áp tỷ lệ dừng 10% mỗi tháng cho kỳ góp thứ hai và thứ ba, 2,5% mỗi tháng sau đó, tỷ lệ rút 10% số dư mỗi năm, mức góp 1 triệu đồng mỗi tháng và cơ cấu tài sản mặc định gồm 45% Trứng Vàng, 35% quỹ trái phiếu, 10% quỹ cổ phiếu và 10% ETF. Doanh thu là biên của DNSE trên trái phiếu ngân hàng bán qua Trứng Vàng (0,6 điểm ở kịch bản cơ sở) cộng phần phí quản lý quỹ giả định chia cho DNSE; giao dịch ETF không tạo doanh thu vì DNSE không thu phí giao dịch. Chi phí gồm đội xây dựng 10 người trong 6 tháng, đội vận hành 6 người từ tháng 4, vận hành và tuân thủ, nội dung, chi phí tiếp cận khách, phí ngân hàng cho mỗi kỳ góp và chi phí phục vụ hằng tháng. Mỗi thông số có ba giá trị bất lợi, cơ sở và thuận lợi (Phụ lục F). Một bộ máy thứ hai chạy cùng các cohort theo thời gian lịch để làm stress test, và khớp hoàn toàn với bộ máy cohort khi không có cú sốc. Mô hình chỉ được dùng sau khi qua đủ 35 phép kiểm, gồm cả ví dụ tính tay của kế hoạch Vòng 2.

### 7.2 Kết quả ở ba kịch bản

Kịch bản cơ sở không hoàn vốn trong 5 năm (Bảng 12; Hình 10). Dòng tiền lũy kế giảm xuống −32,0 tỷ đồng ở tháng 60, và NPV chiết khấu 12% là −25,0 tỷ đồng. Kịch bản bất lợi, với ghi danh, lợi suất và mức duy trì thấp hơn, tốn 10,0 triệu đồng cho mỗi tài khoản mới trên 10 triệu. Kịch bản thuận lợi hòa vốn theo tháng ở tháng 24 và hoàn vốn ở tháng 44, với NPV 11,0 tỷ đồng. Ở kịch bản cơ sở, kế hoạch giữ 352 tỷ đồng ở tháng 36 và 14.871 người tích lũy đã vượt 10 triệu đồng trong kế hoạch của chính họ; con số này tăng lên 24.898 vào tháng 60 (Hình 11).

**Bảng 12. Kết quả ở ba kịch bản**

<!-- table: vi/slide11_scenarios -->
|  | Bất lợi | Cơ sở | Thuận lợi |
|---|---|---|---|
| Nhu cầu tiền Phase 0–1, gồm 15% dự phòng | 8,7 tỷ đồng | 6,6 tỷ đồng | 4,8 tỷ đồng |
| TK mới trên 10 triệu đồng, tháng 36 | 2.911 | 14.871 | 51.445 |
| NPV 60 tháng, chiết khấu 12% | −35,1 tỷ đồng | −25,0 tỷ đồng | +11,0 tỷ đồng |
| Tháng hoàn vốn | Không có | Không có | 44 |
| Chi phí ròng mỗi TK mới trên 10 triệu, tháng 60 | 10,02 triệu đồng | 1,29 triệu đồng | 0 |
<!-- /table -->

Nguồn: mô hình cohort của nhóm (giả định ở Phụ lục F).

![Hình 10. Dòng tiền lũy kế trong 60 tháng ở ba kịch bản](outputs/round3/figures/payday_jcurve.png)

Nguồn: mô hình cohort của nhóm.

![Hình 11. Số dư kế hoạch (trái) và số tài khoản mới trên 10 triệu đồng (phải) theo tháng, ba kịch bản](outputs/round3/figures/payday_balance_accounts.png)

Nguồn: mô hình cohort của nhóm.

### 7.3 Kinh tế đơn vị

Bản thân một người tích lũy mang lại rất ít (Bảng 13). Ở kịch bản cơ sở, 10 triệu đồng số dư mang về cho DNSE khoảng 44.150 đồng mỗi năm. Trần chi phí DNSE có thể bỏ ra để thu hút một người tích lũy, tức giá trị hiện tại của doanh thu ròng từ người đó trong 60 tháng với chiết khấu 12%, là 127.512 đồng. Tiếp cận một tài khoản ngủ tốn 1.300 đồng tiền tin nhắn, nên tỷ lệ ghi danh hòa vốn là khoảng 1,0% số tài khoản được liên hệ. Phí ngân hàng là chi phí biến đổi lớn nhất: ở giá niêm yết 3.300 đồng mỗi kỳ góp, trần CAC là 127.512 đồng; nếu ngân hàng miễn phí, trần tăng lên 198.876 đồng; còn nếu phí vượt 6.191 đồng thì người tích lũy từ tài khoản ngủ không còn hoàn vốn.

**Bảng 13. Kinh tế đơn vị theo kịch bản**

<!-- table: vi/appB1_unit_economics -->
| Chỉ tiêu | Bất lợi | Cơ sở | Thuận lợi |
|---|---|---|---|
| Lợi suất ròng trên số dư kế hoạch, mỗi năm | 0,25% | 0,44% | 0,68% |
| Doanh thu mỗi năm trên 10 triệu đồng số dư | 25.000 đồng | 44.150 đồng | 67.900 đồng |
| Còn góp sau 3 kỳ | 72,2% | 81,0% | 88,4% |
| Còn góp sau 6 kỳ | 63,9% | 75,1% | 84,4% |
| Còn góp sau 12 kỳ | 50,0% | 64,5% | 77,1% |
| Số kỳ góp liền để vượt 10 triệu đồng | 14 | 11 | 7 |
| Trần CAC: PV doanh thu ròng mỗi người tích lũy, 60 tháng | −44.938 đồng | 127.512 đồng | 728.075 đồng |
| Chi phí thu hút mỗi người tích lũy từ TK ngủ | 220.000 đồng | 65.000 đồng | 27.500 đồng |
| Chi phí tiếp cận mỗi TK ngủ được liên hệ | 2.200 đồng | 1.300 đồng | 1.100 đồng |
| Tỷ lệ ghi danh hòa vốn trên số TK được liên hệ | không đạt | 1,02% | 0,15% |
<!-- /table -->

Nguồn: mô hình cohort của nhóm.

### 7.4 Độ nhạy và các đòn bẩy

Chi phí cố định quyết định phương án (Hình 12). Đưa chi phí xây dựng và vận hành từ mức bất lợi sang mức thuận lợi làm dòng tiền lũy kế tháng 60 thay đổi 17,5 tỷ đồng, gần gấp ba biên độ của lợi suất ròng (6,3 tỷ đồng) và gần gấp bốn biên độ của phí ngân hàng (4,7 tỷ đồng) hay mức góp (4,5 tỷ đồng). Ghi danh thêm người tích lũy gần như không đổi dòng tiền tháng 60, vì những người ghi danh muộn chưa kịp hoàn vốn khi hết khung thời gian, nhưng lại làm giảm chi phí cho mỗi tài khoản có tiền. Từ đó có các đòn bẩy ở Bảng 14: đội gọn với 4 nhân sự IT giảm chi phí ròng cho mỗi tài khoản mới trên 10 triệu từ 1,29 triệu xuống 0,85 triệu đồng; tính một nửa chi phí đội là chi phí nền tảng dùng chung cho ra 0,86 triệu đồng; ngân hàng miễn phí thu hộ cho ra 1,17 triệu đồng; và cả bốn đòn bẩy cùng lúc, gồm lợi suất và ghi danh ở mức thuận lợi, cho ra 0,18 triệu đồng và hòa vốn theo tháng ở tháng 39, dù dòng tiền lũy kế tháng 60 vẫn âm.

![Hình 12. Dòng tiền tháng 60 khi một nhóm thông số chuyển sang mức bất lợi hoặc thuận lợi](outputs/round3/figures/payday_tornado.png)

Nguồn: mô hình cohort của nhóm.

**Bảng 14. Các đòn bẩy tác động lên chi phí mỗi tài khoản có tiền**

<!-- table: vi/appB3_levers -->
| Trường hợp | Chi phí ròng mỗi TK mới trên 10 triệu, tháng 60 (triệu đồng) | Dòng tiền lũy kế, tháng 60 (tỷ đồng) | NPV (tỷ đồng) | Tháng hòa vốn |
|---|---|---|---|---|
| Kịch bản cơ sở | 1,29 | −32,0 | −25,0 | không có |
| Ngân hàng đối tác miễn phí thu hộ | 1,17 | −29,2 | −23,0 | không có |
| Đội gọn: 4 nhân sự IT, chi phí chung thấp hơn | 0,85 | −21,2 | −16,8 | không có |
| Lợi suất thuận lợi: biên Trứng Vàng 1,5%, 40% phí quỹ | 1,15 | −28,5 | −22,7 | không có |
| Ghi danh thuận lợi ở mọi kênh | 0,68 | −30,8 | −24,5 | không có |
| Miễn phí thu hộ và đội gọn | 0,74 | −18,4 | −14,8 | không có |
| Miễn phí thu hộ, đội gọn, lợi suất thuận lợi | 0,60 | −14,9 | −12,6 | 58 |
| Miễn phí thu hộ, đội gọn, lợi suất và ghi danh thuận lợi | 0,18 | −8,2 | −8,3 | 39 |
| Mọi thông số ở mức thuận lợi (kịch bản thuận lợi) | 0,00 | 21,9 | 11,0 | 24 |
| Dùng trái phiếu của DNSE trong lõi Trứng Vàng (biên khoảng 1,2 điểm; đã loại, quyết định D7) | 1,13 | −28,1 | −22,4 | không có |
| Một nửa chi phí đội được tính là chi phí nền tảng dùng chung (góc nhìn chi phí tăng thêm) | 0,86 | −21,4 | −16,8 | không có |
<!-- /table -->

Nguồn: mô hình cohort của nhóm.

### 7.5 Stress test

Các cú sốc tác động lên KPI mạnh hơn nhiều so với lên dòng tiền (Bảng 15). Một đợt thị trường giảm trong năm thứ hai, mô hình hóa bằng tỷ lệ dừng và tỷ lệ rút gấp ba bình thường trong ba tháng, làm số tài khoản mới trên 10 triệu ở tháng 36 giảm 12,3% nhưng dòng tiền tháng 60 chỉ giảm 0,35 tỷ đồng. Ngày 9/3/2026 VN-Index giảm 115 điểm (VnExpress, 2026b), nên kịch bản này không xa vời. Một ngày lương lỗi ở tháng 9 làm số tài khoản giảm 7,7%; cả hai cú sốc cùng lúc làm số tài khoản giảm 18,5% và dòng tiền giảm 0,51 tỷ đồng. Vì mỗi người tích lũy gần như hòa vốn trong 5 năm, mất người tích lũy là mất cả doanh thu lẫn chi phí. Rủi ro thật nằm ở chỉ số chính của HĐQT và uy tín của DNSE, nên độ ổn định được đặt làm cổng.

**Bảng 15. Stress test**

<!-- table: vi/appB4_stress -->
| Trường hợp | TK mới trên 10 triệu đồng, tháng 36 | Thay đổi | Thay đổi dòng tiền tháng 60 (tỷ đồng) |
|---|---|---|---|
| Kịch bản cơ sở, không có cú sốc | 14.871 | 0,0% | 0,00 |
| Thị trường giảm ở năm 2: tỷ lệ dừng và rút gấp ba bình thường trong tháng 13 đến 15 | 13.043 | −12,3% | −0,35 |
| Một ngày lương lỗi ở tháng 9: 15% người đang góp dừng; ghi danh thấp hơn 30% trong tháng 9 đến 11 | 13.725 | −7,7% | −0,21 |
| Cả hai cú sốc | 12.118 | −18,5% | −0,51 |
<!-- /table -->

Nguồn: mô hình cohort của nhóm (bộ máy theo lịch).

### 7.6 Giá trị gián tiếp, không tính vào dòng tiền

Một phần giá trị nằm ngoài dòng tiền và được trình bày riêng. Ở tháng 36 của kịch bản cơ sở, số dư kế hoạch bằng khoảng 18% số tiền nhà đầu tư DNSE nắm giữ tại tháng 6/2026. Nếu các tài khoản khác giữ nguyên, chi phí nền tảng cho mỗi tài khoản có từ 10 triệu đồng sẽ giảm từ 7,3 triệu xuống 4,7 triệu đồng. Phương án cho vay, tức cho khách dùng chứng chỉ ETF trong kế hoạch làm tài sản đảm bảo cho khoản vay margin thông thường, sẽ cải thiện NPV cơ sở từ −25,0 tỷ lên −20,9 tỷ đồng. Tuy nhiên phương án này đi ngược mục đích của một kế hoạch tiết kiệm và chạm đúng mảng DNSE bị phạt năm 2026, nên chỉ được xem xét ở Cổng 3 và không nằm trong kịch bản cơ sở.

### 7.7 HĐQT nên đọc phương án này thế nào

Payday không phải mảng kinh doanh thu phí; đó là cách mua tài khoản có tiền. Kịch bản cơ sở mua một tài khoản mới trên 10 triệu đồng với chi phí ròng khoảng 1,3 triệu đồng và, khác với thưởng mở tài khoản, giữ được tiền trong tài khoản. Mức HĐQT phải chịu trước quyết định dừng đầu tiên là 6,6 tỷ đồng, và cổng tháng 6 sẽ chạy lại mô hình với các số đo thực của pilot: nếu chi phí dự phóng cho mỗi tài khoản có tiền vượt gấp đôi kế hoạch, chương trình dừng.

## 8. Kế hoạch go-to-market năm đầu

### 8.1 Kế hoạch theo quý

Năm đầu có bốn bước (Bảng 16; Hình 13). Quý 1, DNSE xây sản phẩm, ký với đối tác và chạy thử kế hoạch bằng tiền của nhân viên; không ra mắt gì trước Cổng 0. Quý 2, một pilot ngẫu nhiên tiếp cận 45.000 tài khoản ngủ chia ba nhánh, mỗi nhánh 15.000: nhánh đối chứng, nhánh Payday, và nhánh Payday kèm gói giữ chân. Nếu tỷ lệ ghi danh vượt 1,5%, quý 3 mở rộng tới các tài khoản ngủ đủ điều kiện còn lại, thêm lời mời trong app cho trader đang hoạt động và bước lập kế hoạch khi mở tài khoản. Quý 4, DNSE thử với 3 đến 5 doanh nghiệp qua các buổi giới thiệu với phòng nhân sự có người hành nghề tư vấn tham gia. Đến tháng 12, kịch bản cơ sở có 9.414 người tích lũy ghi danh, 4.953 người đã góp từ 3 kỳ liền trở lên và 30,1 tỷ đồng trong kế hoạch.

**Bảng 16. Kế hoạch go-to-market năm đầu**

<!-- table: vi/slide12_gtm -->
| Quý | Ai và ở đâu | Thông điệp | Cổng | Cuối quý, cơ sở: người góp từ 3 kỳ; số dư; chi tiêu |
|---|---|---|---|---|
| Q1: xây dựng | Nhân viên DNSE, beta nội bộ | – | Cổng 0: điều khoản đối tác; shadow run 99,5%; thông báo UBCKNN | 0; 0; 2,1 tỷ đồng |
| Q2: pilot | 45.000 TK ngủ chia 3 nhánh; Zalo, SMS, push, Ensa | "Tài khoản của bạn đã sẵn sàng. Để ngày lương đầu tư giúp bạn." | Cổng 1: ghi danh ≥1,5%, dừng nếu dưới 1,0% | 162; 1,1 tỷ đồng; 3,6 tỷ đồng |
| Q3: mở rộng | TK ngủ; trong app cho trader; bước lập kế hoạch khi mở TK | "Giữ một phần lõi lớn dần trong khi bạn giao dịch." | Hằng tháng: chi phí thu hút mỗi người góp từ 3 kỳ ≤128.000 đồng | 1.620; 10,5 tỷ đồng; 1,7 tỷ đồng |
| Q4: doanh nghiệp đầu tiên | 3–5 doanh nghiệp qua buổi giới thiệu với phòng nhân sự | "Phúc lợi nhân viên giúp đầu tư một phần lương." | Cổng 2: người góp từ 3 kỳ ≥3.962; số dư ≥24,1 tỷ đồng | 4.953; 30,1 tỷ đồng; 1,8 tỷ đồng |
<!-- /table -->

Nguồn: thiết kế của nhóm; số liệu từ mô hình cohort của nhóm.

![Hình 13. Hoạt động năm đầu theo tháng với Cổng 0 đến Cổng 2 (trên) và số người góp từ 3 kỳ theo tháng (dưới), kịch bản cơ sở](outputs/round3/figures/gtm_timeline.png)

Nguồn: mô hình cohort của nhóm. Màu đỏ đánh dấu các tháng HĐQT duyệt ngay; mũi tên đánh dấu các kênh tiếp tục sang năm thứ hai.

### 8.2 Thông điệp, kênh và giới hạn

Mỗi phân khúc nghe một thông điệp: "Your account is ready. Let payday do the investing." (Tài khoản của bạn đã sẵn sàng, để ngày lương đầu tư giúp bạn) cho người có tài khoản ngủ, "Keep a core that grows while you trade." (Giữ một phần lõi lớn dần trong khi bạn giao dịch) cho trader, "Start your plan with your first deposit." (Bắt đầu kế hoạch ngay với lần nạp đầu tiên) khi mở tài khoản, và "An employee benefit that invests your salary." (Phúc lợi nhân viên giúp đầu tư một phần lương) cho doanh nghiệp. Kênh là kênh của chính DNSE: tin nhắn mẫu Zalo, SMS, thông báo push, banner trong app và Ensa. Tiếp cận một tài khoản ngủ tốn khoảng 1.300 đồng, tính theo hai tin nhắn mẫu Zalo và một SMS (Zalo Business Solutions, n.d.; MobiFone, n.d.). Các giới hạn rút ra từ bài học năm 2025: không thưởng tiền khi mở tài khoản, không KOL hứa "tiền miễn phí", không thưởng có điều kiện, không khuyến mại hoàn tiền qua đối tác, và tối đa ba lần liên hệ cho mỗi tài khoản.

### 8.3 Ngân sách năm đầu

Kịch bản cơ sở chi 9,2 tỷ đồng trong năm đầu, giải ngân theo từng cổng, trong đó HĐQT duyệt ngay 6,6 tỷ đồng. Tiếp cận và marketing chỉ chiếm 1,1 tỷ đồng; xây dựng và vận hành sản phẩm chiếm 7,9 tỷ đồng. Đó là lý do cách cải thiện kinh tế rẻ nhất là đội gọn và dùng lại các thành phần đã có, chứ không phải hạ chi phí thu hút khách.

## 9. Lộ trình chiến lược

### 9.1 Năm phase có cổng

Sau năm đầu, lộ trình có năm phase, mỗi phase kết thúc bằng một cổng (Bảng 17; Hình 14). Phase 0 đến 2 xây dựng, thử nghiệm và mở rộng trong chính tệp khách của DNSE. Phase 3, từ tháng 13, thêm các kênh tạo ra lựa chọn mặc định: doanh nghiệp, góp theo % lương qua Open API của ngân hàng khi ngân hàng tuân thủ vào tháng 3/2027, và tự động tăng mức góp khi tăng lương. Phase 4, từ tháng 25, xem xét một phiên bản quản lý trọn gói do công ty quỹ đối tác vận hành, hoặc do công ty quản lý quỹ mà DNSE đề xuất mua lại tại ĐHĐCĐ 2026 (DNSE Securities, 2026f).

**Bảng 17. Lộ trình chiến lược**

<!-- table: vi/slide13_roadmap -->
| Phase | Tháng | Mục tiêu | Việc chính | Cổng và kết quả (cơ sở) |
|---|---|---|---|---|
| 0. Xây dựng và tuân thủ | 1–3 | MVP an toàn, đúng luật | VA (mục tiêu phí 0 đồng); hợp đồng với công ty quỹ; kế hoạch do người hành nghề ký; thông báo UBCKNN | Cổng 0; lũy kế −2,1 tỷ đồng |
| 1. Pilot | 4–6 | Đo ghi danh, mức duy trì, tiền mới | Pilot ngẫu nhiên, 45.000 TK, 3 nhánh | Cổng 1; 600 người tích lũy |
| 2. Mở rộng trong tệp khách | 7–12 | Mở rộng có kiểm soát | Mở rộng tới TK ngủ; trong app; khi mở TK; doanh nghiệp đầu tiên | Cổng 2; 4.953 người góp từ 3 kỳ |
| 3. Kênh bên ngoài | 13–24 | Kênh tạo ra lựa chọn mặc định | Doanh nghiệp; góp theo % lương qua Open API từ 3/2027; tăng mức góp khi tăng lương | Cổng 3; 7.714 TK mới trên 10 triệu đồng |
| 4. Tối ưu | 25–36 | Kinh tế tốt hơn, thêm lựa chọn quản lý trọn gói | Công ty quỹ đối tác hoặc của DNSE; Trứng Vàng với thêm ngân hàng đối tác | Rà soát hằng quý; 14.871 TK mới trên 10 triệu đồng |
<!-- /table -->

Nguồn: thiết kế của nhóm; số liệu từ mô hình cohort của nhóm; DNSE Securities (2026f); State Bank of Vietnam (2024).

![Hình 14. Năm phase có cổng của Payday với kết quả kịch bản cơ sở (trên), đặt trên lộ trình sản phẩm lấy số dư làm trọng tâm của DNSE (dưới)](outputs/round3/figures/roadmap.png)

Nguồn: thiết kế của nhóm; mô hình cohort của nhóm.

### 9.2 Payday trong lộ trình lấy số dư làm trọng tâm của DNSE

Payday là trung tâm của một chuyển dịch rộng hơn, từ lấy giao dịch làm trọng tâm sang lấy số dư làm trọng tâm. Trong 6 tháng đầu, DNSE sửa phần nền: độ ổn định của app, tuân thủ được gắn sẵn vào cho vay ký quỹ, và minh bạch. Từ tháng 6 đến tháng 12, DNSE giữ tiền lại: Tài khoản Không Ngủ bật mặc định, Trứng Vàng làm lõi an toàn, và Payday. Từ tháng 12 đến tháng 24, DNSE tăng trưởng dựa trên số dư: margin cho khách có tài sản, tư vấn có phí và Open API của ngân hàng. Các thành phần Payday xây dựng, gồm VA mang tên khách, bộ lập lịch, bộ máy đánh giá phù hợp và dashboard minh bạch, cũng phục vụ nạp tiền, margin và Trứng Vàng, nên một phần chi phí của chúng là chi phí nền tảng chứ không riêng của Payday.

### 9.3 Các phương án nằm ngoài kịch bản cơ sở

Ba phương án được để ngoài kịch bản cơ sở và xem xét ở các cổng. **Kênh doanh nghiệp** tiếp cận nhiều người đi làm cùng lúc, nhưng với chi phí 15 triệu đồng mỗi doanh nghiệp và 300 nhân viên, chi phí mỗi người tích lũy chỉ thấp hơn trần CAC nếu ít nhất 39% nhân viên ghi danh. Bằng chứng về tỷ lệ tham gia cao đến từ việc tự động đưa nhân viên vào kế hoạch hưu trí trích lương, cách làm đã nâng tỷ lệ tham gia từ 37% lên 86% ở một kế hoạch tại Mỹ (Madrian & Shea, 2001); còn một buổi giới thiệu tự nguyện tham gia chỉ đạt tối đa khoảng 28% (Ashraf et al., 2006). **Góp qua Open API** cần thỏa thuận với ngân hàng và sự đồng ý của khách chỉ có hiệu lực tối đa 180 ngày. **Cho vay cầm cố ETF** đã được bàn ở Mục 7.6.

## 10. Triển khai và kiểm chứng

### 10.1 Thiết kế pilot

Pilot là một thử nghiệm ngẫu nhiên với 45.000 tài khoản ngủ chia ba nhánh, mỗi nhánh 15.000 (Bảng 18). Hai nhánh nhận lời mời và một nhánh là đối chứng, nên pilot đo được phần Payday thực sự tạo thêm thay vì những gì vẫn sẽ xảy ra nếu không có Payday. Với 300 người ghi danh ở mỗi nhánh can thiệp, pilot phát hiện được mức tăng khoảng 10 điểm trong tỷ lệ người đạt 6 kỳ góp; một pilot 20.000 tài khoản chỉ phát hiện được mức 15 điểm. Nếu tỷ lệ thật là 2%, tỷ lệ ghi danh được đo với khoảng tin cậy 95% từ khoảng 1,84% đến 2,16%, đủ để phân biệt ngưỡng dừng 1,0% với ngưỡng mở rộng 1,5%. Chi phí tiếp cận các nhánh can thiệp khoảng 39 triệu đồng.

**Bảng 18. Quy mô pilot và mức phát hiện được**

<!-- table: vi/appB6_pilot_power -->
| Số TK pilot | Người tích lũy mỗi nhánh can thiệp | Tỷ lệ ghi danh, khoảng tin cậy 95% | Mức tăng nhỏ nhất phát hiện được (điểm) | Chi phí tiếp cận (triệu đồng) |
|---|---|---|---|---|
| 20.000 | 133 | 1,76–2,24% | 14,8 | 17,3 |
| 30.000 | 200 | 1,81–2,19% | 12,1 | 26,0 |
| 45.000 | 300 | 1,84–2,16% | 9,9 | 39,0 |
| 60.000 | 400 | 1,86–2,14% | 8,6 | 52,0 |
<!-- /table -->

Nguồn: mô hình cohort của nhóm.

### 10.2 Các chỉ số

Chỉ số North Star là số tài khoản mới có từ 10 triệu đồng trong kế hoạch, một chỉ tiêu DNSE vốn đã công bố cho toàn bộ tệp khách, nên HĐQT có thể đối chiếu với báo cáo thường niên. Mục tiêu lấy từ mô hình: 7.714 vào tháng 24 và 14.871 vào tháng 36 ở kịch bản cơ sở. Ba chỉ số dẫn dắt cho biết kế hoạch có đi đúng hướng không: số người góp từ 3 kỳ liền trở lên, tỷ trọng tiền mới trong dòng tiền vào, và tỷ lệ ghi có đúng hạn.

### 10.3 Các cổng quyết định

Mỗi phase kết thúc bằng một cổng, tại đó HĐQT mở rộng, điều chỉnh hoặc dừng (Hình 15; Bảng 19). Các ngưỡng được suy ra từ mô hình chứ không chọn theo cảm tính. Ở Cổng 0 (tháng 3), DNSE kiểm tra điều khoản đối tác, tỷ lệ đúng hạn 99,5% trong các lần chạy thử ngày lương và xác nhận tuân thủ bằng văn bản. Ở Cổng 1 (tháng 6), DNSE đọc kết quả pilot: mở rộng nếu ít nhất 1,5% tài khoản được can thiệp ghi danh và ít nhất 81% người tích lũy góp 3 kỳ liền; dừng nếu tỷ lệ ghi danh dưới 1,0%, mức duy trì dưới 60% hoặc chi phí dự phóng cho mỗi tài khoản mới trên 10 triệu vượt 2,6 triệu đồng. Cổng 2 và Cổng 3 so sánh số người góp từ 3 kỳ, số dư, số tài khoản mới trên 10 triệu và kênh doanh nghiệp với kế hoạch.

![Hình 15. Các nhánh mở rộng, điều chỉnh và dừng ở Cổng 0 đến Cổng 3](outputs/round3/figures/decision_tree.png)

Nguồn: mô hình cohort của nhóm.

**Bảng 19. Toàn bộ các cổng quyết định**

<!-- table: vi/appB7_gates -->
| Cổng | Chỉ tiêu | Mở rộng nếu | Điều chỉnh nếu | Dừng nếu | Phụ trách |
|---|---|---|---|---|---|
| Cổng 0: trước pilot | Điều khoản đối tác đã ký: phí ngân hàng mỗi kỳ góp; phần phí quỹ trả cho DNSE; biên của DNSE trên trái phiếu ngân hàng trong Trứng Vàng | Phí ≤ 3.300 đồng; phần phí quỹ ≥ 30%; biên ≥ 0,6 điểm | Kém hơn ở bất kỳ điều khoản nào: chạy lại mô hình và đàm phán lại trước pilot | Chưa ký được công ty quỹ hoặc ngân hàng (phụ thuộc để ra mắt) | CFO |
| Cổng 0: trước pilot | Phí ngân hàng mỗi kỳ góp (thu hộ qua VA), đồng | 0 (ngân hàng đối tác giữ tiền gửi) | 1 đến 3.300 (giá niêm yết) | > 6.191: người tích lũy từ TK ngủ không còn hoàn vốn | CFO |
| Cổng 0: trước pilot | Chạy thử ngày lương bằng TK nhân viên: tỷ lệ chuyển tiền được ghi có đúng hạn | ≥ 99,5% | - | < 99,5%: hoãn pilot | CTO |
| Cổng 1: đọc kết quả pilot | Chi phí ròng dự phóng mỗi TK mới trên 10 triệu đồng đến tháng 60 (chạy lại mô hình với số đo của pilot và điều khoản đã ký), triệu đồng | ≤ 1,6 (1,25 lần kế hoạch) | 1,6 đến 2,6 | > 2,6 (2 lần kế hoạch) | CFO |
| Cổng 1: đọc kết quả pilot | Tỷ lệ ghi danh của TK ngủ được can thiệp (cài đặt và góp kỳ đầu trong 60 ngày) | ≥ 1,5% | 1,0% đến 1,5% | < 1,0% | Trưởng sản phẩm |
| Cổng 1: đọc kết quả pilot | Tỷ lệ người tích lũy góp 3 kỳ liền | ≥ 81,0% | 60,0% đến 81,0% | < 60,0% | Trưởng sản phẩm |
| Cổng 1: đọc kết quả pilot | Mức góp bình quân mỗi tháng, đồng | ≥ 1.000.000 | 716.502 đến 1.000.000 | < 716.502 | CFO |
| Cổng 1: đọc kết quả pilot | Tỷ trọng tiền mới trong dòng tiền vào kế hoạch (gắn nguồn) | ≥ 80% | 60% đến 80% | < 60% | CFO |
| Cổng 1: đọc kết quả pilot | Lệnh chuyển theo lịch được ghi có đúng hạn | ≥ 99,5% | - | < 99,5% (cổng ra mắt) | CTO |
| Cổng 1: đọc kết quả pilot | Tuân thủ: đã nộp thông báo UBCKNN; danh mục mẫu đã được người hành nghề có chứng chỉ ký duyệt | Xác nhận bằng văn bản | - | Thiếu (cổng ra mắt) | Pháp chế |
| Cổng 2: năm mở rộng đầu tiên | Người góp từ 3 kỳ liền trở lên | ≥ 3.962 (80% kế hoạch) | 2.476 đến 3.962 | < 2.476 trong hai quý | Trưởng sản phẩm |
| Cổng 2: năm mở rộng đầu tiên | Số dư kế hoạch, tỷ đồng | ≥ 24,1 (80% kế hoạch) | 15,1 đến 24,1 | < 15,1 trong hai quý | CFO |
| Cổng 2: năm mở rộng đầu tiên | Chi phí thu hút mỗi người góp từ 3 kỳ, đồng | ≤ 127.512 (trần CAC) | - | > 127.512 trong hai quý | CFO |
| Cổng 3: rà soát mở rộng | Doanh thu kế hoạch hằng tháng so với chi phí vận hành hằng tháng | ≥ 16% (kế hoạch) | - | < 2% (đường bất lợi): xem lại mô hình doanh thu | CFO |
| Cổng 3: rà soát mở rộng | TK mới trên 10 triệu đồng nhờ kế hoạch | ≥ 6.171 (80% kế hoạch) | - | < 1.140 (đường bất lợi) | CEO |
| Cổng 3: rà soát mở rộng | Kênh doanh nghiệp: tỷ lệ nhân viên ghi danh sau buổi giới thiệu | ≥ 39% | 20% đến 39%: giảm chi phí mỗi doanh nghiệp | < 20%: dừng kênh | Trưởng sản phẩm |
| Cổng 3: rà soát mở rộng | Chi phí ròng mỗi TK mới trên 10 triệu đồng tính đến nay, triệu đồng | ≤ 2,6 (1,25 lần kế hoạch) | 2,6 đến 4,1 | > 4,1: gộp vào đội app chính hoặc dừng | CFO |
<!-- /table -->

Nguồn: mô hình cohort của nhóm.

### 10.4 Trách nhiệm và các điểm phụ thuộc

Mỗi hoạt động có một người chịu trách nhiệm cuối cùng (Bảng 20). Chuỗi phụ thuộc ngắn nhưng chặt: ngân hàng VA phải có trước bộ lập lịch, các lần chạy thử ngày lương và pilot; hợp đồng với công ty quỹ phải có trước phần quỹ trong kế hoạch, và nếu chậm thì MVP ra mắt với Trứng Vàng và ETF; thông báo UBCKNN phải có trước khi ra mắt; gắn nguồn cho dòng tiền vào phải có trước chỉ số tiền mới; và thỏa thuận Open API với ngân hàng phải có trước việc góp theo % lương ở Phase 3.

**Bảng 20. Phân công trách nhiệm (RACI)**

<!-- table: vi/appB9_raci -->
| Hoạt động | CEO | CFO | CTO | Trưởng sản phẩm | Pháp chế và tuân thủ | Marketing và CRM | CSKH | Người hành nghề tư vấn |
|---|---|---|---|---|---|---|---|---|
| Quyết định ở các cổng (tháng 3; 6; 12; 24) | A | R | C | R | C | I | I | I |
| Điều khoản đối tác: ngân hàng VA, công ty quỹ, nguồn trái phiếu | I | A/R | C | C | C | - | - | - |
| Thông báo UBCKNN, ý kiến pháp lý, duyệt nội dung khuyến mại | I | I | I | C | A/R | C | - | C |
| Danh mục mẫu và quy tắc đánh giá phù hợp | I | - | I | C | A | - | - | R |
| Xây MVP: bộ lập lịch, VA, phân bổ, dashboard | I | I | A/R | C | C | - | I | - |
| Chạy thử ngày lương và cổng độ ổn định 99,5% | I | I | A/R | C | I | - | I | - |
| Pilot ngẫu nhiên: thiết kế và đọc kết quả | I | C | C | A/R | C | C | I | C |
| Tiếp cận và thông điệp | I | I | I | A | C | R | I | - |
| Khiếu nại, rút tiền và khắc phục sau sự cố | I | I | C | A | C | I | R | - |
| Công bố số đo dịch vụ hằng tháng | I | I | R | A | C | C | C | - |
<!-- /table -->

Nguồn: thiết kế của nhóm. R = thực hiện, A = chịu trách nhiệm cuối cùng, C = được tham vấn, I = được thông báo.

## 11. Rủi ro và giảm thiểu

Sáu rủi ro được chấm điểm theo khả năng xảy ra và mức tác động trên thang 1 đến 5 (Hình 16; Bảng 21). Lỗi ngày lương có điểm cao nhất (20/25): sự cố 4/3/2026 cho thấy việc này có thể xảy ra, nên chạy thử ngày lương, bộ lập lịch riêng và lệnh ngừng phát hành phải có trước khi ra mắt. Ghi danh thấp đứng thứ hai (16), đó là lý do pilot dừng nếu dưới 1,0%. Thứ ba (15), cơ quan quản lý có thể phản đối vai trò của Trứng Vàng hoặc luồng tư vấn, nên DNSE thông báo sớm cho UBCKNN và giữ quỹ trái phiếu làm lõi dự phòng. Điều khoản đối tác, thị trường giảm hoặc xung đột lợi ích, và tiền kế hoạch bị chuyển sang giao dịch hoàn tất danh mục rủi ro; mỗi rủi ro đều có tín hiệu cảnh báo sớm và người phụ trách.

![Hình 16. Sáu rủi ro theo khả năng xảy ra và mức tác động, kèm người phụ trách](outputs/round3/figures/risk_heatmap.png)

Nguồn: đánh giá của nhóm.

**Bảng 21. Danh mục rủi ro**

<!-- table: vi/appB8_risks -->
| ID | Rủi ro | Khả năng × tác động | Giảm thiểu | Cảnh báo sớm | Phụ trách |
|---|---|---|---|---|---|
| R1 | Lệnh chuyển ngày lương hoặc app lỗi đúng ngày lương | 4 × 5 = 20 | Chạy thử ngày lương trước khi ra mắt; bộ lập lịch kỳ góp tách khỏi bước kiểm tra sức mua trước giao dịch; không phát hành app trong các ngày trước ngày góp cao điểm; phát hành theo đợt; trang trạng thái và ghi chú sau sự cố | Tỷ lệ kỳ góp được ghi có đúng hạn dưới 99,5% trong bất kỳ tháng nào | CTO |
| R2 | Quá ít TK ngủ ghi danh | 4 × 4 = 16 | Pilot ngẫu nhiên với 45.000 TK trước mọi bước mở rộng; ngưỡng dừng ở Cổng 1 là 1,0%; bước lập kế hoạch khi mở TK; thử thông điệp giữa các nhánh | Tỷ lệ ghi danh của TK được can thiệp dưới 1,0% ở tháng 6 | Trưởng sản phẩm |
| R4 | Cơ quan quản lý phản đối vai trò của Trứng Vàng hoặc luồng tư vấn | 3 × 5 = 15 | Thông báo và tham vấn trước UBCKNN trước khi ra mắt; danh mục mẫu do người hành nghề có chứng chỉ ký; quỹ trái phiếu sẵn sàng làm lõi an toàn thay thế | UBCKNN có văn bản hỏi hoặc phản đối | Pháp chế và tuân thủ |
| R3 | Điều khoản đối tác để lại quá ít cho mỗi người tích lũy (phí ngân hàng, phần phí quỹ, biên trái phiếu) | 3 × 4 = 12 | Điều khoản ở Cổng 0: mục tiêu phí thu hộ 0 đồng (ngân hàng giữ tiền gửi), phần phí quỹ ≥ 30%, biên trái phiếu ≥ 0,6 điểm; chạy lại mô hình trước pilot | Phí ký kết trên 6.191 đồng mỗi kỳ góp | CFO |
| R5 | Thị trường giảm hoặc xung đột lợi ích làm tổn hại niềm tin | 3 × 4 = 12 | Danh mục theo kỳ hạn mục tiêu (không có cổ phiếu cho mục tiêu dưới 3 năm); không có trái phiếu do DNSE phát hành trong danh mục mặc định; hiện mức lỗ của một tháng xấu bằng đồng trước khi xác nhận | Chủ đề niềm tin vượt 10% review tiêu cực liên quan Payday | Trưởng sản phẩm |
| R6 | Tiền kế hoạch bị chuyển sang giao dịch hoặc đến từ số dư sẵn có | 3 × 3 = 9 | Gắn nguồn cho dòng tiền vào; mặc định rút về ngân hàng liên kết; có bước riêng kèm nhắc mục tiêu trước khi chuyển tiền sang sức mua | Tiền mới dưới 80% dòng tiền vào, hoặc hơn 10% tiền rút được chuyển sang sức mua | CFO |
<!-- /table -->

Nguồn: đánh giá của nhóm; DNSE Securities (2023, 2026e); Market Times (2026); VnExpress (2026b).

## 12. Khuyến nghị và đề nghị gửi HĐQT

Nhóm khuyến nghị HĐQT phê duyệt Phase 0 và Phase 1 của Payday Portfolio cùng năm quyết định ở Bảng 22. Số tiền là nhu cầu tiền của mô hình cho tháng 1 đến tháng 6, 5,7 tỷ đồng, cộng 15% dự phòng. Đến tháng 6, HĐQT sẽ thấy các số đo thực về ghi danh, mức duy trì, mức góp và tiền mới, và có thể dừng chương trình lúc đó với chi phí không vượt số đã duyệt.

**Bảng 22. Đề nghị gửi HĐQT**

<!-- table: vi/slide15_board_ask -->
| Đề nghị | Chi tiết |
|---|---|
| Ngân sách | 6,6 tỷ đồng cho tháng 1 đến 6 (5,7 tỷ cộng 15% dự phòng) |
| Quyết định 1 | Chọn ngân hàng VA; mục tiêu phí thu hộ 0 đồng |
| Quyết định 2 | Ký với 1–2 công ty quỹ |
| Quyết định 3 | Nộp thông báo UBCKNN; tham vấn trước về vai trò của Trứng Vàng |
| Quyết định 4 | Có người hành nghề có chứng chỉ ký danh mục mẫu |
| Quyết định 5 | Chấp nhận khoảng 1,3 triệu đồng mỗi TK mới trên 10 triệu làm thước đo ở các cổng |
<!-- /table -->

Nguồn: mô hình cohort của nhóm.

## 13. Kết luận

DNSE đã giải được phần khó của tăng trưởng là mở tài khoản, nhưng các tài khoản đó không có tiền và giao dịch miễn phí không nuôi được nền tảng. Payday Portfolio cho người đi làm một con đường từ ý định đến những lần nạp tiền đều đặn, dựng từ các sản phẩm DNSE đang vận hành và thiết kế theo bằng chứng: độ ổn định trước tiên, niềm tin được hiện thành số đo, không thưởng tiền, không margin và không xung đột lợi ích. Kinh tế của phương án ở mức khiêm tốn và được nói rõ. Ở kịch bản cơ sở, Payday mua tài khoản có tiền với giá khoảng 1,3 triệu đồng mỗi tài khoản và không hoàn vốn trong 5 năm; ở kịch bản thuận lợi, phương án hoàn vốn ở tháng 44. Điều khiến phương án đáng bắt đầu là HĐQT chỉ phải chịu rủi ro 6,6 tỷ đồng trước khi biết, ở tháng 6, kịch bản nào là thật.

## Phụ lục

### Phụ lục A. Dữ liệu và phương pháp

**Bảng A1. Dữ liệu dùng trong báo cáo**

<!-- table: vi/appA1_data_sources -->
| Dữ liệu | Nguồn | Dùng cho |
|---|---|---|
| Số TK, khách hoạt động và TK có từ 10 triệu, tháng 12/2025 | Báo cáo thường niên 2025 của DNSE (DNSE Securities 2026c) | Vấn đề, quy mô, thông số mô hình |
| BCTC của DNSE, Q1/2018 đến Q2/2026 | Hồ sơ công bố của DNSE qua Vietcap Securities (2026) | Lỗ môi giới, chi phí nền tảng mỗi TK có từ 10 triệu |
| Thị phần TK, tiền nhà đầu tư, dư nợ margin và lợi nhuận | HNX, VSDC và báo chí, đối chiếu ở Vòng 2 | Slide 2 |
| Review app của DNSE, VPS và FPTS, 2021 đến 2026 | Google Play và App Store; làm sạch theo Vòng 2; 58 review tiêu cực năm 2026 được mã hóa thủ công | Slide 4 và 5; Phụ lục D và F của deck |
| Lãi suất, phí và điều khoản sản phẩm, tháng 10/2026 | 44 nguồn web có ngày truy cập (sources_round3.csv) | Thông số mô hình; slide 3, 7 và 10 |
| Lương trả qua tài khoản | World Bank (2025) Global Findex | Tỷ lệ người đi làm trong nhóm TK ngủ |
<!-- /table -->

Nguồn: nhóm tác giả. Số slide và phụ lục ở cột cuối là của deck Vòng 3A.

**Bảng A2. Phương pháp và cách kiểm tra**

<!-- table: vi/appA2_methods -->
| Phương pháp | Làm gì | Kiểm tra thế nào |
|---|---|---|
| Mô hình cohort theo tháng | Theo dõi người tích lũy mới của từng tháng: tỷ lệ dừng, kỳ góp, rút tiền và ai vượt 10 triệu đồng | 35 phép kiểm đều đạt, gồm ví dụ tính tay của kế hoạch Vòng 2 |
| Bộ máy theo lịch | Chạy cùng các cohort theo thời gian lịch, nên một cú sốc tác động đến mọi cohort cùng lúc | Khớp hoàn toàn với bộ máy cohort khi không có cú sốc |
| Kinh tế đơn vị | Trần CAC = giá trị hiện tại của doanh thu ròng mỗi người tích lũy trong 60 tháng, chiết khấu 12% | Tỷ lệ ghi danh hòa vốn = chi phí tiếp cận ÷ trần CAC |
| Cổng quyết định | Ngưỡng dừng và ngưỡng mở rộng được giải từ mô hình bằng phương pháp chia đôi | Phép thử cho cả chương trình: chi phí ròng mỗi TK mới trên 10 triệu |
| Mã hóa review | 58 review tiêu cực năm 2026 được đọc từng cái; 8 mã nguyên nhân, một review có thể mang nhiều mã | Khoảng tin cậy Wilson 95%; so với quy tắc từ khóa của Vòng 2 |
<!-- /table -->

Nguồn: nhóm tác giả.

### Phụ lục B. Chi tiết mô hình

**Bảng B1. Ngân sách theo phase, tỷ đồng, kịch bản cơ sở**

<!-- table: vi/appB2_phase_budget -->
| Phase | Tháng | Chi phí | trong đó xây dựng | Doanh thu | Dòng tiền lũy kế cuối kỳ |
|---|---|---|---|---|---|
| Phase 0: xây dựng và tuân thủ | 1–3 | 2,09 | 2,09 | 0,00 | −2,09 |
| Phase 1: pilot | 4–6 | 3,63 | 2,09 | 0,00 | −5,72 |
| Phase 2: mở rộng trong tệp khách | 7–12 | 3,49 | 0,00 | 0,03 | −9,17 |
| Phase 3: kênh bên ngoài | 13–24 | 7,28 | 0,00 | 0,46 | −15,99 |
| Phase 4: tối ưu | 25–36 | 7,23 | 0,00 | 1,20 | −22,02 |
| Năm 4 và 5 | 37–60 | 14,73 | 0,00 | 4,76 | −32,00 |
<!-- /table -->

Nguồn: mô hình cohort của nhóm.

**Bảng B2. Các bậc thưởng bằng tiền so với gói không bằng tiền**

<!-- table: vi/appB5_tiers -->
| Phí ngân hàng | Thiết kế phần thưởng | Chi phí thưởng, % doanh thu | Trần CAC | Tỷ lệ đạt 12 kỳ cần có |
|---|---|---|---|---|
| Phí ngân hàng cơ sở | Bậc thưởng Vòng 2 thu nhỏ: quà 10k / 20k / 50k, hoàn phí 0,1 điểm từ kỳ 6, Trứng Vàng +0,2 điểm từ kỳ 12 | 41,2% | 36.712 đồng | không thể đạt |
| Phí ngân hàng cơ sở | Phương án thử: quà 30k ở kỳ 12, hoàn phí 0,1 điểm từ kỳ 6 | 14,2% | 96.158 đồng | không thể đạt |
| Phí ngân hàng cơ sở | MVP (quyết định D1): chỉ có tính năng không bằng tiền | 0,0% | 127.512 đồng | 64,5% |
| Miễn phí ngân hàng | Bậc thưởng Vòng 2 thu nhỏ: quà 10k / 20k / 50k, hoàn phí 0,1 điểm từ kỳ 6, Trứng Vàng +0,2 điểm từ kỳ 12 | 41,2% | 108.077 đồng | không thể đạt |
| Miễn phí ngân hàng | Phương án thử: quà 30k ở kỳ 12, hoàn phí 0,1 điểm từ kỳ 6 | 14,2% | 167.523 đồng | 73,3% |
| Miễn phí ngân hàng | MVP (quyết định D1): chỉ có tính năng không bằng tiền | 0,0% | 198.876 đồng | 64,5% |
<!-- /table -->

Nguồn: mô hình cohort của nhóm.

### Phụ lục C. Review về app DNSE năm 2026

**Bảng C1. Nguyên nhân trong 58 review tiêu cực, kèm khoảng tin cậy Wilson 95%**

<!-- table: vi/appD1_review_causes -->
| Nguyên nhân | Google Play | App Store | Cả hai kho | Khoảng tin cậy 95% |
|---|---|---|---|---|
| Đăng nhập, OTP và xác thực | 3 (9%) | 5 (21%) | 8 (14%) | 7,2–24,9% |
| Nạp hoặc rút không được ghi có | 4 (12%) | 6 (25%) | 10 (17%) | 9,6–28,9% |
| Lệnh, giá và thanh toán | 6 (18%) | 5 (21%) | 11 (19%) | 10,9–30,9% |
| Văng app, treo và giật lag | 15 (44%) | 11 (46%) | 26 (45%) | 32,7–57,5% |
| eKYC và mở TK | 5 (15%) | 5 (21%) | 10 (17%) | 9,6–28,9% |
| Phí và điều khoản (đóng TK, tự tái tục) | 3 (9%) | 3 (12%) | 6 (10%) | 4,8–20,8% |
| Tố lừa đảo và phần thưởng | 4 (12%) | 3 (12%) | 7 (12%) | 6,0–22,9% |
| Khác (dịch vụ, giao diện, Ensa, không nêu lý do) | 6 (18%) | 7 (29%) | 13 (22%) | 13,6–34,7% |
| Có thứ bị hỏng (bất kỳ nguyên nhân nào trong năm nhóm đầu) | 28 (82%) | 20 (83%) | 48 (83%) | 71,1–90,4% |
| Phí, điều khoản, tố lừa đảo hoặc phần thưởng | 6 (18%) | 5 (21%) | 11 (19%) | 10,9–30,9% |
| Lỗi đăng nhập/OTP hoặc tiền không được ghi có | 7 (21%) | 10 (42%) | 17 (29%) | 19,2–42,0% |
| Đăng ngày 4–5/3/2026, sau sự cố DNSE công bố ngày 4/3 | 4 (12%) | 5 (21%) | 9 (16%) | 8,4–26,9% |
| Đổ lỗi cho bản cập nhật app | 2 (6%) | 3 (12%) | 5 (9%) | 3,7–18,6% |
| Số review tiêu cực đã mã hóa | 34 | 24 | 58 |  |
<!-- /table -->

Nguồn: Google Play; App Store; nhóm tác giả mã hóa.

**Bảng C2. Review tiêu cực theo tháng**

<!-- table: vi/appD2_reviews_by_month -->
| Tháng | Review tiêu cực | Có thứ bị hỏng | Đăng ngày 4–5/3 |
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

Nguồn: Google Play; App Store; nhóm tác giả mã hóa; DNSE Securities (2026e).

**Bảng C3. Lời khách hàng**

<!-- table: vi/appD3_quotes -->
| Khách hàng viết (nguyên văn, từ tục được che bằng _) | Review |
|---|---|
| App quá tệ. Hôm nay 04/03/2026, app đơ không đặt lệnh mua bán gì cả buổi chiều, trong bối cảnh thị trường đỏ lửa cả ngày. Đến cuối phiên tăng lại thì app không cho đặt lệnh mua hạ giá vốn. Tiền cũng ko cho rút ra. App quá tệ! Mọi người đừng sử dụng ! | App Store, 1 sao, 04/03/2026, bản 2.113.28 |
| Nạp tiền vào, ngân hàng thông báo chuyển khoản thành công nhưng khi vào app xem thì không thấy cộng tiền. Hiện tại vẫn chưa thấy tiền về tài khoản, mất tiền | Google Play, 1 sao, 02/03/2026 |
| Không chuyển được tiền ra ngân hàng. Không nhận action confirm  otp. Cứ đếm đi đếm lại time không rút được tiền | App Store, 1 sao, 30/03/2026, bản 2.114.3 |
| App như b__. App tài chính đ__ gì update tuần 4-5 lần. Mỗi lần update xong lại có lỗi phát sinh. Update xong tự động xoá cụ hết thông tin đăng nhập và cài đặt. Làm ăn như l__ | App Store, 1 sao, 17/08/2026, bản 3.4.18 |
| không ấn gia hạn mà vẩn gia hạn tự động nên mất tiền 🤬😡🤬😡 | Google Play, 1 sao, 05/01/2026 |
| Nhân viên tư vấn tào lao. Nhân viên cskh ko rành nghiệp vụ. Hỏi sao mã VHM thể hiện rõ là có margin mà sao ko cho vay. Bảo là mã VHM hết cấp margin rồi, nhưng thật ra là lỗi app. Bán đi mua lại là sẽ dc Rồi tới chuyện phí Ứng trước thì lãi là 13.5%/năm. Nhưng thực tế là 27%/năm nha mọi người. Hỏi tới thì nói là anh cứ tính theo công cụ.  Phí ẩn/ phí sai, nhân viên thì tệ. | App Store, 1 sao, 26/03/2026, bản 2.114.2 |
<!-- /table -->

Nguồn: review trên Google Play và App Store, giữ nguyên văn.

### Phụ lục D. Bằng chứng từ phản hồi của khách

**Bảng D1. Khách hàng đã viết gì, theo từng lựa chọn thiết kế**

<!-- table: vi/appF1_feedback -->
| Lựa chọn thiết kế | Khách hàng viết (nguyên văn, trích) | Review |
|---|---|---|
| Tài khoản định danh riêng, ghi có ngay | Công ty nên chơi với ngân hàng BIDV để tạo một mã định danh tai khoản để giao dịch tốt hơn chứ để tình trạng lỗi giao dịch nạp hoài thì mọi người sẽ bỏ App hoặc giao dịch sàn khác | Google Play, DNSE, 5 sao, 10 lượt hữu ích, 01/2022 |
| Tài khoản định danh riêng, ghi có ngay | Khi nạp tiền không vào giờ giao dịch, dù tiền đã trừ ở tài khoản ngân hàng, nhưng tài khoản chứng khoán không nhận được | Google Play, DNSE, 2 sao, 18 lượt, 06/2025 |
| Tài khoản Không Ngủ là nơi tiền chờ | tk không ngủ the best : cái này thì signature của shop rồi, nhìn lãi nhảy tưng tưng đã mắt | Google Play, DNSE, 5 sao, 13 lượt, 05/2026 |
| Lõi Trứng Vàng với thang kỳ hạn | với thêm trứng vàng kỳ hạn 6 tháng 1 năm thêm nữa là OK | App Store, DNSE, 5 sao, 02/2025 |
| Hiện rõ chi phí bán trước hạn | Mua trứng vàng 1 tháng, bị mất 4% số tiền | App Store, DNSE, 1 sao, 01/2025 |
| Không thu phí nền tảng | app này mỗi tháng trừ phí 33k rất cao, không đáng sử dụng với nhà đầu tư dài hạn | Google Play, VPS, 1 sao, 9 lượt, 05/2026 |
<!-- /table -->

Nguồn: review về DNSE và VPS trên Google Play và App Store, trích nguyên văn.

### Phụ lục E. Bản đồ hành trình

**Bảng E1. Bản đồ hành trình của persona P1**

<!-- table: vi/appG2_journey -->
|  | 1. Thấy lời mời | 2. Lập kế hoạch | 3. Cài đặt dòng tiền | 4. Ngày lương đầu tiên | 5. Tạo thói quen (đến ngày 90) | 6. Rút tiền hoặc tiếp tục |
|---|---|---|---|---|---|---|
| Mục tiêu | Quyết định có đáng xem không | Biết nên góp gì và vì sao | Tự động hóa việc tiết kiệm | Thấy khoản tiền đầu tiên về và được đầu tư | Tiếp tục mà không phải nghĩ | Rút được tiền khi cần |
| Hành động | Mở tin nhắn Zalo hoặc banner trong app | Đặt mục tiêu, trả lời 3 câu hỏi, xác nhận kế hoạch | Lập lệnh chuyển hằng tháng trong app ngân hàng nhận lương | Nhận lương; ngân hàng thực hiện lệnh chuyển | Đọc lời nhắc ngày lương; bỏ qua một tháng nếu cần | Rút về ngân hàng hoặc bỏ qua một tháng |
| Điểm chạm | Tin nhắn mẫu Zalo, SMS, push, banner | Ensa, màn hình kế hoạch, màn hình phí | Thẻ số tài khoản riêng, link app ngân hàng, QR | Thông báo "Đã nhận" và "Đã đầu tư" | Lời nhắc có tên mục tiêu; chuỗi kỳ góp; sao kê | Màn hình rút tiền |
| Suy nghĩ | "Lại là một kiểu thưởng có điều kiện à?" | "Mình đang mua gì, và có thể mất bao nhiêu?" | "Tiền chuyển từ ngân hàng có về DNSE thật không?" | "Tiền về chưa? Giờ tiền của mình đang ở đâu?" | "Tháng này còn đáng góp không?" | "Rút ra mất bao lâu, tốn bao nhiêu?" |
| Cảm xúc (kiểm chứng trong pilot) | Hoài nghi | Phân vân | Sốt ruột | Lo rồi nhẹ nhõm | Có động lực hoặc hay quên | Dè chừng |
| Điểm đau hiện nay (bằng chứng) | Nghi ngờ ưu đãi sau đợt thưởng mở TK 2025 (chủ đề niềm tin chiếm 55% review tiêu cực trên Google Play H1/2025) | Thấy khó chọn danh mục (77% nhà đầu tư thấy tự quản lý danh mục là khó) | Phải rời app để lập lệnh chuyển; lỗi eKYC và các bước mở TK (17% review tiêu cực năm 2026) | Chờ khoản nạp mà ngân hàng báo đã chuyển (17% review tiêu cực năm 2026) | Trì hoãn mỗi tháng; app văng, treo hoặc giật lag (45% review tiêu cực năm 2026) | Mất tiền với Trứng Vàng 1 tháng mà không hiểu vì sao (review 2025) hoặc vì tự tái tục ngoài ý muốn (review 2026, không nêu tên sản phẩm); bị chặn rút khi tên tài khoản ngân hàng không khớp (review 2026) |
| Cách thiết kế đáp ứng | Bỏ thưởng mở TK; nói trong một dòng kế hoạch là gì và ai duyệt | Hỏi 3 câu; lập kế hoạch theo kỳ hạn mục tiêu; hiện một tháng xấu bằng đồng | Cấp số tài khoản riêng kèm link app ngân hàng và QR; nhắm 5 phút và số bước không nhiều hơn SIP trên VCB Digibank | Tự động ghi có vào VA riêng; xác nhận trong vài phút; công bố tỷ lệ đúng hạn | Gửi lời nhắc có tên mục tiêu; giữ chuỗi kỳ góp; cho bỏ qua 1 tháng mỗi năm | Hiện giờ tiền về và chi phí bằng đồng trước khi xác nhận; rút miễn phí về ngân hàng liên kết; thêm một bước trước khi chuyển tiền sang giao dịch |
| Số đo | Tỷ lệ mở và bấm xem | Tỷ lệ kế hoạch được xác nhận sau bước đánh giá phù hợp | Tỷ lệ và thời gian cài đặt xong | Kỳ góp được ghi có trong cùng ngày làm việc (≥ 99,5%) | Tỷ lệ người tích lũy góp 3 kỳ liền | Thời gian rút trung vị; tỷ lệ chuyển sang sức mua |
| Phụ trách | Marketing và CRM | Trưởng sản phẩm; người hành nghề tư vấn | CTO; ngân hàng đối tác | CTO; Vận hành | Trưởng sản phẩm | CSKH |
| Khoảnh khắc quyết định | - | - | - | Có: tiền vào lần đầu | - | Có: tiền ra lần đầu |
<!-- /table -->

Nguồn: thiết kế của nhóm; bằng chứng từ Phụ lục C, Nhan Dan (2025) và dữ liệu review. Cảm xúc là giả thuyết để pilot kiểm chứng.

### Phụ lục F. Các giả định chính

**Bảng F1. Các giả định chính ở ba kịch bản**

<!-- table: vi/appH1_assumptions -->
| Giả định | Bất lợi | Cơ sở | Thuận lợi | Loại | Căn cứ |
|---|---|---|---|---|---|
| TK ngủ (không dùng sản phẩm nào, 12/2025) | 1.427.181 | 1.427.181 | 1.427.181 | suy ra | DNSE Securities (2026c) |
| Tỷ lệ TK ngủ là người đi làm và liên hệ được | 15% | 25% | 35% | giả định | World Bank (2025); khảo sát trong pilot |
| Số TK pilot (ba nhánh) | 45.000 | 45.000 | 45.000 | giả định | Quyết định D4 |
| Tỷ lệ ghi danh của TK ngủ được liên hệ | 1% | 2% | 4% | giả định | Tài khoản Không Ngủ đạt 0,8% số TK; TCBS (2026) |
| Tỷ lệ ghi danh của khách hoạt động trong 12 tháng | 2% | 4% | 6% | giả định | Số đăng ký Tài khoản Không Ngủ bằng 14% số khách hoạt động |
| TK mới mỗi tháng | 20.000 | 31.180 | 43.210 | suy ra | DNSE Securities (2026c); VnExpress (2026a) |
| Cài đặt trong 60 ngày sau khi mở TK | 1% | 2% | 3% | giả định | Giả định |
| Số doanh nghiệp ký mỗi quý | 2 | 4 | 8 | giả định | Kế hoạch go-to-market |
| Tỷ lệ nhân viên ghi danh sau buổi giới thiệu | 10% | 20% | 28% | giả định | Ashraf et al. (2006) làm cận trên |
| Mức góp hằng tháng | 800.000 đồng | 1.000.000 đồng | 1.500.000 đồng | giả định | Khoảng 11% thu nhập bình quân 9,0 triệu đồng (National Statistics Office, 2026) |
| Tỷ lệ dừng ở kỳ góp thứ 2 và 3 (mỗi tháng) | 15,0% | 10,0% | 6,0% | giả định | Giả định; pilot sẽ đo |
| Tỷ lệ dừng sau kỳ góp thứ 3 (mỗi tháng) | 4,0% | 2,5% | 1,5% | giả định | Giả định; pilot sẽ đo |
| Tỷ lệ số dư bị rút mỗi năm | 15% | 10% | 5% | giả định | Giả định; dòng tiền vào được gắn nguồn |
| Biên của DNSE trên trái phiếu ngân hàng trong Trứng Vàng | 0,30% | 0,60% | 1,00% | giả định | Thi truong Tai chinh Tien te (2026a); DNSE Securities (n.d.-b) |
| Phần phí quỹ trái phiếu trả cho đại lý phân phối | 0,22% | 0,33% | 0,44% | giả định | SSI Asset Management (2026); VCBF (2026); bản cáo bạch của quỹ |
| Phần phí quỹ cổ phiếu trả cho đại lý phân phối | 0,38% | 0,56% | 0,75% | giả định | Bản cáo bạch và factsheet của quỹ, 2026 |
| Đội xây dựng, tháng 1 đến 6 | 3,97 tỷ đồng | 3,18 tỷ đồng | 2,54 tỷ đồng | suy ra | Lương trung vị theo ITviec (2025) |
| Tích hợp, kiểm thử bảo mật, ý kiến pháp lý | 1,50 tỷ đồng | 1,00 tỷ đồng | 0,60 tỷ đồng | giả định | VPBank (2024); giả định |
| Đội vận hành, mỗi năm | 4,72 tỷ đồng | 3,78 tỷ đồng | 2,52 tỷ đồng | suy ra | Lương trung vị theo ITviec (2025) |
| Vận hành, tuân thủ và cloud, mỗi năm | 1,80 tỷ đồng | 1,20 tỷ đồng | 0,80 tỷ đồng | giả định | Giả định |
| Nội dung và duyệt khuyến mại, mỗi năm | 1,50 tỷ đồng | 1,00 tỷ đồng | 0,60 tỷ đồng | giả định | Giả định |
| Chi phí tiếp cận mỗi TK ngủ được liên hệ | 2.200 đồng | 1.300 đồng | 1.100 đồng | suy ra | Zalo Business Solutions (n.d.); MobiFone (n.d.) |
| Phí ngân hàng mỗi kỳ góp | 5.500 đồng | 3.300 đồng | 0 đồng | giả định | Giá niêm yết của VPBank (2024) |
| Chi phí phục vụ mỗi người đang góp mỗi tháng | 2.000 đồng | 1.000 đồng | 500 đồng | giả định | Tin xác nhận qua Zalo, sao kê |
| Lãi suất chiết khấu | 12% | 12% | 12% | giả định | Suất sinh lời tối thiểu |
| Cơ cấu tài sản: Trứng Vàng / quỹ trái phiếu / quỹ cổ phiếu / ETF | như cơ sở | 45/35/10/10 | như cơ sở | giả định | Thiết kế: danh mục theo kỳ hạn mục tiêu |
<!-- /table -->

Nguồn: như ghi trong bảng; danh sách đầy đủ 60 thông số nằm ở `data/round3/payday_assumptions.csv`.

### Phụ lục G. Những câu HĐQT có thể hỏi

**Bảng G1. Trả lời ngắn**

<!-- table: vi/appI1_qa -->
| Câu hỏi | Trả lời ngắn | Bằng chứng |
|---|---|---|
| Sao không gửi tiết kiệm ngân hàng cho xong? | Trứng Vàng trả 6,20–7,60% so với 5,9% của tiền gửi 12 tháng ở Big4, nhưng coupon trái phiếu chịu thuế 5% còn tiền gửi thì không. Payday cạnh tranh bằng kỳ hạn ngắn, sự tự động, một mục tiêu và bằng chứng công bố, chứ không bằng mức lãi. | DNSE Securities (n.d.-a, n.d.-b); Thi truong Tai chinh Tien te (2026b) |
| VPS Smart Indexing có giống Payday không? | Không. VPS quyết định thay khách, chỉ nắm cổ phiếu, bắt đầu từ 50 triệu đồng cộng 10 triệu mỗi tháng và thu 0,5%/năm. Payday do khách xác nhận, gồm bốn loại tài sản và bắt đầu từ 500.000 đồng. | Tuoi Tre (2026); Tin nhanh Chung khoan (2026) |
| Nếu Ensa tư vấn sai thì ai chịu trách nhiệm? | Ensa chỉ thu thập thông tin. Người hành nghề có chứng chỉ ký danh mục mẫu, mọi khuyến nghị đều được lưu log, và không khoản nào được đầu tư khi khách chưa xác nhận. | Ministry of Finance (2020), Điều 4 và 24; National Assembly (2019), Điều 72 |
| Chuyện gì xảy ra khi thị trường giảm? | Mục tiêu dưới một năm chỉ nắm trái phiếu ngân hàng. Trong stress test, một đợt giảm ở năm 2 làm số TK mới trên 10 triệu ở tháng 36 giảm 12,3% và dòng tiền tháng 60 giảm 0,35 tỷ đồng. | Mô hình cohort của nhóm; VnExpress (2026b) |
| Sao không dùng trái phiếu của chính DNSE? | Làm vậy cải thiện dòng tiền tháng 60 khoảng 3,9 tỷ đồng, nhưng tạo xung đột lợi ích trong một sản phẩm có tư vấn. Trứng Vàng từng bị tạm dừng mở mới theo yêu cầu của cơ quan quản lý vào tháng 12/2023. | Mô hình cohort của nhóm; DNSE Securities (2023) |
| Sao không cho vay cầm cố ETF trong kế hoạch? | NPV cơ sở chỉ cải thiện từ −25,0 tỷ lên −20,9 tỷ đồng. Phương án này còn đi ngược mục đích tiết kiệm và các vi phạm ký quỹ bị nêu năm 2026, nên chỉ xem xét ở Cổng 3. | Mô hình cohort của nhóm; Market Times (2026) |
| Nếu ngân hàng thu phí niêm yết thì sao? | Ở mức 3.300 đồng mỗi kỳ góp, trần CAC giảm từ 199.000 xuống 128.000 đồng; trên 6.200 đồng thì kênh TK ngủ không còn hoàn vốn. Cổng 0 nhắm mức 0 đồng. | VPBank (2024); mô hình cohort của nhóm |
| Nếu chỉ 1% TK ngủ ghi danh thì sao? | Đó là tỷ lệ hòa vốn nên sẽ không mở rộng: chỉ mở rộng từ 1,5% và dừng nếu dưới 1,0%. Đường bất lợi tốn khoảng 10,0 triệu đồng mỗi TK mới trên 10 triệu và bị dừng ở tháng 6. | Mô hình cohort của nhóm |
| Open API là mối đe dọa hay cơ hội? | Ngân hàng phải tuân thủ chậm nhất ngày 1/3/2027 và sự đồng ý của khách có hiệu lực tối đa 180 ngày. Ngân hàng VA của Payday là đối tác Open API đầu tiên tự nhiên cho việc góp theo % lương ở Phase 3. | State Bank of Vietnam (2024) |
<!-- /table -->

Nguồn: như ghi trong bảng.

## Tài liệu tham khảo

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


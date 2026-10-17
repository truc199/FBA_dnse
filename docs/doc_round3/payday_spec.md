# Payday Portfolio: đặc tả sản phẩm và kế hoạch triển khai (Phase 2)

*Lập ngày 16/10/2026 cho Round 3A, theo các quyết định D1–D7 ở `review_phase1.md` (user đồng ý và yêu cầu làm tiếp). Số liệu lấy từ mô hình cohort (`python src/round3/run_round3.py`), data trong repo và các nguồn đã kiểm trong `data/round3/sources_round3.csv`. Câu tiếng Anh trong ngoặc kép là chữ dự kiến đưa lên slide.*

---

## 0. Tóm tắt

- **Sản phẩm:** kế hoạch tích lũy theo mục tiêu, góp hằng tháng từ 500.000đ. Cụ thể:
  - danh mục theo kỳ hạn mục tiêu: lõi trái phiếu do ngân hàng phát hành (qua Trứng Vàng), cộng quỹ và ETF cho mục tiêu dài;
  - khách xác nhận mọi thay đổi;
  - không phí nền tảng;
  - ưu đãi giữ chân không bằng tiền;
  - công bố số đo minh bạch hằng tháng.
- **Khách mục tiêu:**
  - người đi làm có TK ngủ (khách ra mắt);
  - trader muốn có một phần tích lũy dài hạn;
  - người mở TK mới.
- **Năm đầu (base):** 9.414 saver ghi danh, 4.953 saver đã góp từ 3 kỳ liền trở lên (funded), số dư 30 tỷ, chi 9,2 tỷ.
- **Board chỉ duyệt Phase 0–1: 6,6 tỷ**, kèm 5 việc giao ngay. Cổng ở tháng 3 / 6 / 12 / 24 có ngưỡng suy ra từ mô hình.
- **Ba khoảnh khắc quyết định niềm tin:** tiền vào lần đầu, tiền ra lần đầu, và lần đầu có sự cố. Thiết kế, cam kết SLO và số đo công bố đều xoay quanh ba khoảnh khắc này.

---

## 1. Persona (dựng từ data, không thêm chi tiết đời tư)

| | **P1. Người đi làm có TK ngủ** (E2, khách ra mắt) | **P2. Trader muốn có phần tích lũy** (E1) | **P3. Người mở TK mới** (N0) |
|---|---|---|---|
| Quy mô (data) | 1.427.181 TK không thuộc nhóm khách hoạt động (1.512.920 TK trừ 85.739 khách hoạt động, 12/2025); 98% số TK có tài sản ròng dưới 10 triệu | 85.739 khách hoạt động; 27.100 TK ≥10 triệu (khoảng 31,6% số khách hoạt động) | Khoảng 31.180 TK mở mới/tháng (nhịp H1/2026); 518.514 TK năm 2025 |
| Điều đã biết | Đi làm, 22–40 tuổi (độ tuổi của nhóm N1 ở R2 Table E3). 45,2% người trong lực lượng lao động nhận lương qua TK (Findex). Thu nhập bình quân 9,0 triệu/tháng (NSO Q2/2026) | DNSE đứng thứ 2 môi giới phái sinh (25,38%, Q2/2026). Tài khoản Không Ngủ có 12.100 người đăng ký, khoảng 14% số khách hoạt động | Gen Z chiếm 31,5% TK DNSE (giữa 2025). Niềm tin thường gãy ở lần nạp đầu (R2) |
| Việc cần làm (giả thuyết) | "Đưa một phần lương vào đầu tư mỗi tháng mà không phải quyết lại" | "Giữ một phần lõi lớn dần trong khi vẫn giao dịch" | "Bắt đầu bằng một bước nhỏ, an toàn, và thấy nó chạy" |
| Rào cản (bằng chứng) | Trì hoãn (O'Donoghue & Rabin, 1999); nghi ngờ sau đợt thưởng 2025 (chủ đề trust chiếm 55% review tiêu cực trên Google Play H1/2025, theo quy tắc từ khóa của Round 2); app hỏng (83% review tiêu cực 2026) | Tiền có sẵn dễ bị chuyển qua lại (ăn thịt lẫn nhau); rút sang giao dịch khi thị trường nóng | Tìm thưởng thay vì tích lũy; eKYC lỗi (17% review tiêu cực 2026) |
| Thông số trong mô hình (base) | Ghi danh 2% số TK được liên hệ; góp 1,0 triệu/tháng (khoảng 11% thu nhập); 11 kỳ liền để vượt 10 triệu | Ghi danh 4% trong 12 tháng; 31,6% đã có ≥10 triệu nên không tính vào KPI | Ghi danh 2% trong 60 ngày sau khi mở TK |
| Pilot cần đo | Tỷ lệ ghi danh, tỷ lệ đạt 3 kỳ, mức góp, tỷ lệ tiền mới | Tỷ lệ tiền mới; tỷ lệ rút sang sức mua | Tỷ lệ cài đặt khi mở TK |

**Phân khúc làm sau (Phase 3):** nhân viên của doanh nghiệp đối tác (N1). Kênh này chỉ đáng làm nếu tỷ lệ tham gia đạt ≥39%; ở mức 20% thì mỗi saver tốn hơn trần CAC (`review_phase1.md` §1 #7).

---

## 2. Giá trị mang lại

| Cho ai | Giá trị (câu đưa lên slide) | Bằng chứng / số |
|---|---|---|
| Khách hàng | *"A monthly plan from VND 500,000 that turns part of each salary into progress toward a goal: a bank-bond core with 1 to 12 month terms, plus funds and an ETF for long goals. You confirm every change, pay no platform fee, and can pause, skip or withdraw in one tap."* | Trứng Vàng 6,20–7,60%/năm theo kỳ hạn, vé từ 100.000đ (S17); tiền gửi 12 tháng Big4 5,9% (S02). Lãi coupon chịu thuế 5%, tiền gửi thì không, nên **không nói "lãi cao nhất"** |
| DNSE | *"Funded accounts at about VND 1.3 million each, not empty ones; shared payment rails that also target the deposit failures behind 17% of 2026 negative reviews."* | Chi phí ròng 1,29 triệu/TK mới ≥10 triệu (base, 60 tháng). Tháng 36: số dư 352 tỷ, bằng 18% tiền NĐT tại DNSE; cost proxy/TK ≥10 triệu giảm từ 7,3 xuống 4,7 triệu. Đây là giá trị gián tiếp, không cộng vào dòng tiền |
| Ngân hàng đối tác | Tiền góp nằm ở VA của ngân hàng (CASA), nên ngân hàng có lý do miễn phí thu hộ | VPBank niêm yết 3.000đ/giao dịch "theo thỏa thuận" (S10); BIDV từng miễn phí 6 tháng (S12) |
| Công ty quỹ | Dòng SIP mới từ một tệp 1,5 triệu TK | SIP không thu phí mua (S22–S25) |
| Cơ quan quản lý | Tư vấn đúng quy định và số đo công bố | TT 121/2020 Điều 24; thông báo UBCKNN trước khi ra mắt |

---

## 3. Tính năng MVP (Phase 0–1) và những gì cố ý loại

| # | Tính năng | Ghi chú thiết kế |
|---|---|---|
| F1 | Đặt mục tiêu: loại mục tiêu, số tiền, ngày | Tự tính số tiền cần góp mỗi tháng, chưa tính lợi nhuận đầu tư |
| F2 | Đánh giá phù hợp: kỳ hạn, phản ứng khi lỗ, thu nhập | TT 121/2020 Điều 24; lưu log tư vấn |
| F3 | Kế hoạch theo kỳ hạn mục tiêu (D2) | Danh mục mẫu do người hành nghề có chứng chỉ ký; khách xác nhận |
| F4 | VA mang tên khách + hướng dẫn lệnh chuyển định kỳ (link mở app ngân hàng, QR) | Mục tiêu thiết kế: cài đặt xong trong 5 phút; số bước không nhiều hơn VCB Digibank SIP |
| F5 | Tự rót mỗi kỳ góp vào lớp tài sản đang thiếu nhất | Chỉ dùng tiền mới, không bán; ETF mua theo lô 100 khi đủ tiền |
| F6 | Tài khoản Không Ngủ làm nơi chờ | Thường đầu tư xong trong ngày làm việc kế tiếp |
| F7 | Dashboard: tiến độ mục tiêu, tài sản theo lớp, tiền đang nằm ở đâu, phí đã trả | — |
| F8 | Gói giữ chân phi tiền mặt (D1) | Chuỗi kỳ góp; được bỏ qua 1 tháng/năm; nhắc ngày lương có tên mục tiêu (Karlan et al., 2016); ưu tiên Trứng Vàng mới; Ensa rà kế hoạch ở tháng 6 |
| F9 | Tạm dừng / bỏ qua / hủy bằng một chạm; rút về ngân hàng liên kết miễn phí | Chuyển sang sức mua phải qua một bước riêng, có nhắc mục tiêu |
| F10 | Thông báo: đã nhận, đã đầu tư, chưa nhận, lương về trễ | Có cửa sổ chờ 5 ngày; chuỗi kỳ góp không mất trong thời gian chờ |
| F11 | Trang số đo dịch vụ công bố hằng tháng | §5 |

**Cố ý loại (và lý do):**
- **Margin và đòn bẩy trong MVP**, kể cả làm phần thưởng: mâu thuẫn với mục tiêu tiết kiệm; TT 121/2020 Điều 27; các vi phạm ký quỹ trong QĐ 461/QĐ-XPHC (17/08/2026). Phương án khách tự chọn dùng ETF trong kế hoạch làm tài sản đảm bảo chỉ được xét ở Cổng 3 (§11.2).
- **Cổ phiếu đơn lẻ và phái sinh** trong Payday: rủi ro phù hợp và trust. Ensa không gợi ý mã đơn lẻ trong kế hoạch.
- **Trái phiếu do DNSE phát hành** trong danh mục mặc định (D7): xung đột lợi ích.
- **Thưởng tiền mặt khi mở TK, thưởng có điều kiện, tier bằng tiền do DNSE trả** (D1): bài học trust 2025; tier bằng tiền tốn 41% doanh thu/saver.
- **Quản lý ủy thác, tự đổi danh mục không hỏi khách**: TT 121/2020 Điều 4; Luật CK 2019 Điều 72.
- **Hạn mức tín dụng trên khoản tiết kiệm**: Điều 27; chứng chỉ quỹ mở không niêm yết.
- **Gói thành viên trả phí**: R2 G1, phí trước khi có lời lặp lại đúng điều khách gọi là lừa.
- **Trích % lương qua Open API**: để Phase 3, sau 01/03/2027 và khi đã có thỏa thuận với ngân hàng.

---

## 4. Gói giữ chân (D1) và danh mục theo kỳ hạn mục tiêu (D2)

**Gói giữ chân (không tốn tiền của DNSE):**

| Mốc | Khách nhận được |
|---|---|
| Mỗi kỳ góp | Chuỗi kỳ góp tăng; nhắc ngày lương có tên mục tiêu |
| 3 kỳ liền (ngày 90) | Huy hiệu; quyền ưu tiên mua các đợt Trứng Vàng mới |
| 6 kỳ liền | Ensa rà kế hoạch (miễn phí); ưu đãi phí nếu công ty quỹ tài trợ |
| Cả năm | Được bỏ qua 1 tháng mà không mất chuỗi kỳ góp |

- Tier bằng tiền (quà 30.000đ ở kỳ 12, giảm phí 0,1 điểm từ kỳ 6) **chỉ thử trên một nhánh thử nghiệm riêng** trong Phase 2, so với nhánh chỉ có gói phi tiền mặt.
- Chỉ bật tier này khi phí VA đã được miễn **và** tỷ lệ đạt 12 kỳ tăng từ 64,5% lên ≥73,3% (`payday_tier_breakeven.csv`).
- Mọi ưu đãi lãi sau này có trần 50 triệu.

**Danh mục mặc định theo kỳ hạn mục tiêu** (`outputs/round3/tables/glide_path.csv`):

| Kỳ hạn mục tiêu | Trứng Vàng (trái phiếu ngân hàng) | Quỹ trái phiếu | Quỹ cổ phiếu | ETF VN30 | Quy tắc |
|---|---:|---:|---:|---:|---|
| Dưới 1 năm | 100% | 0 | 0 | 0 | Kỳ hạn 1–6 tháng, đáo hạn trước ngày mục tiêu. Chỉ tái tục vào kỳ hạn vẫn đáo hạn trước ngày mục tiêu, báo trước 3 ngày, tắt bằng một chạm. Hiện Trứng Vàng mặc định tự tái tục và chỉ gửi email sau khi đã tái tục (S18); một review 2026 than bị tự tái tục mà mất tiền (không nêu tên sản phẩm) |
| 1–3 năm | 50% | 50% | 0 | 0 | Chỉ quỹ trái phiếu không còn phí bán sau 12 tháng (ví dụ VCBF-FIF, S24) |
| Từ 3 năm | 30% | 30% | 20% | 20% | Cổ phiếu tối đa 40% |
| 12 tháng cuối trước mục tiêu | Chỉ dùng tiền mới | — | — | — | Kỳ góp mới chỉ vào Trứng Vàng; không bán để cân bằng |

- **Quy tắc chung:** không xếp sản phẩm có phí rút trước hạn rơi vào trong kỳ hạn mục tiêu. Trứng Vàng bán trước thời gian nắm giữ tối thiểu chỉ hưởng 2%/năm (S18); VCBF-FIF thu 2,0% nếu bán trong 3 tháng đầu và 1,0% nếu bán từ tháng 3 đến tháng 12 (S24).
- Mô hình dùng cơ cấu bình quân 45/35/10/10. Nếu 50% số dư thuộc mục tiêu ≥3 năm, 30% thuộc 1–3 năm và 20% dưới 1 năm, bảng trên cho ra 50/30/10/10. Lợi suất ròng chênh dưới 0,02 điểm.

---

## 5. Cam kết minh bạch và số đo công bố (`trust_metrics.csv`)

| Cam kết | Khách thấy gì | Số đo công bố | Mục tiêu | Tần suất | Chịu trách nhiệm |
|---|---|---|---|---|---|
| Tiền về đúng hẹn | Thông báo "đã nhận" vài phút sau khi ngân hàng ghi có | Tỷ lệ kỳ góp được ghi có trong cùng ngày làm việc | ≥99,5% (cổng ra mắt) | Hằng tháng | CTO |
| Tiền được đầu tư nhanh | Trạng thái "đã đầu tư" kèm tên tài sản | Thời gian trung vị từ ghi có đến khi đầu tư | ≤1 ngày làm việc | Hằng tháng | CTO |
| Rút nhanh, miễn phí | "Arrives by 22:00 today" khi bán Trứng Vàng trong giờ 9h00–14h30 (FAQ của DNSE: tiền về "khoảng 21-22h ngày bán", S18); ngày thanh toán của quỹ hiện trước khi xác nhận | Thời gian trung vị từ lệnh rút đến khi tiền vào ngân hàng | Trong ngày với Trứng Vàng | Hằng tháng | Head of Product |
| Rời đi dễ | Tạm dừng / bỏ qua / hủy bằng một chạm | Tỷ lệ hủy hoàn tất trong app, không phải gọi | 100% | Hằng tháng | Head of Product |
| Không có chi phí ẩn | Một màn hình liệt kê mọi phí và thuế bằng VND trước khi xác nhận | Tỷ lệ kế hoạch được xác nhận sau khi đã hiện màn hình phí (kiểm toán) | 100% | Hằng quý | Pháp chế |
| Sự cố được nhận, không bị giấu | Trang trạng thái; ghi chú sau sự cố | Sự cố ảnh hưởng kỳ góp có ghi chú công bố trong 5 ngày làm việc | 100% | Mỗi sự cố | CTO |
| Phàn nàn được đếm | — | Tỷ trọng chủ đề trust trong review tiêu cực liên quan Payday | <10% | Hằng quý | CSKH |

*Theo bản rà đối thủ ngày 16/10 (S33–S36), chưa thấy nhà cung cấp nào công bố tỷ lệ chuyển tiền thành công hay thời gian rút tiền trung vị. Đây là một trong hai khác biệt còn lại (D5).*

---

## 6. Yêu cầu reliability (SLO và quy tắc kỹ thuật)

1. **Cổng ra mắt:** ≥99,5% kỳ góp được ghi có trong cùng ngày làm việc, đo bằng shadow run với tiền của nhân viên ở Phase 0 (Cổng 0) và duy trì hằng tháng sau đó. Ngân sách lỗi: 0,5% số kỳ góp/tháng. Vượt ngân sách thì ngừng phát hành tính năng mới cho đến khi sửa xong.
2. **Tách luồng khỏi bước kiểm sức mua trước giao dịch.** Sự cố 04/03/2026 (13:22–15:20) bắt nguồn từ bước này (S13), đúng vào ngày VN-Index biến động 67 điểm trong phiên (S14).
   - Lệnh mua quỹ và Trứng Vàng chạy qua hàng đợi riêng.
   - Lệnh ETF lỗi thì thử lại ở phiên sau.
3. **Idempotent và đối soát:** mỗi kỳ góp có mã duy nhất; đối soát VA hằng ngày làm việc. Tiền không khớp được giữ ở Tài khoản Không Ngủ và rà tay trong 1 ngày làm việc.
4. **Kỷ luật phát hành:**
   - Không phát hành app trong các ngày ngay trước những ngày góp cao điểm (lịch lấy từ pilot).
   - Phát hành theo đợt 5% → 25% → 100%, có feature flag và rollback.
   - Theo dõi lỗi theo phiên bản app (bài học iOS 2.113.28: 7 review tiêu cực trên cùng một bản).
5. **Truyền thông sự cố:** trang trạng thái và ghi chú sau sự cố. Một review ngày 04/03/2026 viết: "không 1 lời thông báo, ib zalo, hay trực tiếp trên app đều ko có ai hỗ trợ".
6. **Năng lực ngày cao điểm:** bộ lập lịch rải kỳ góp trong ngày; tải thử ở mức gấp 3 lượng kỳ góp của ngày cao nhất trong pilot (giả định thiết kế).

---

## 7. Căn cứ pháp lý (`legal_map.csv`, dùng cho appendix E)

| Yêu cầu | Căn cứ | Phản hồi thiết kế | Trạng thái |
|---|---|---|---|
| Tư vấn phải phù hợp với khách | TT 121/2020/TT-BTC Điều 24 | Ensa thu thập thông tin; người có chứng chỉ ký danh mục mẫu; lưu log | Áp dụng |
| Không đầu tư thay khách khi không có ủy quyền | TT 121/2020 Điều 4 | Khách xác nhận kế hoạch và mọi thay đổi; hệ thống chỉ đầu tư tiền mới theo kế hoạch đã xác nhận | Áp dụng |
| Chỉ cho vay margin và một số mục đích định sẵn | TT 121/2020 Điều 27 | Không có hạn mức tín dụng trên khoản tiết kiệm | Loại |
| Quản lý danh mục không phải nghiệp vụ của CTCK | Luật CK 2019 Điều 72 | Không ủy thác; bản quản lý hoàn toàn chỉ qua công ty quản lý quỹ | Loại (Phase 4 qua công ty quỹ) |
| Open API ngân hàng | TT 64/2024/TT-NHNN: ngân hàng tuân thủ trước 01/03/2027; đồng ý của khách tối đa 180 ngày | Phase 1 dùng lệnh định kỳ khách tự đặt; trích % lương ở Phase 3 | Phase sau |
| Dịch vụ mới phải báo cáo | QĐ 461/QĐ-XPHC: 275 triệu trong khoản phạt 802,5 triệu vì không báo cáo | Thông báo UBCKNN trước khi ra mắt (Cổng 0) | Cổng ra mắt |
| Lịch sử pháp lý của Trứng Vàng | Dừng mở mới theo yêu cầu cơ quan quản lý từ 25/12/2023 (S32) | Tham vấn UBCKNN về vai trò của Trứng Vàng trong Payday; quỹ trái phiếu là lõi dự phòng | Tham vấn trước |
| Phân phối chứng chỉ quỹ | DNSE là đại lý phân phối CCQ (2021) nhưng chưa có trong danh sách của SSIAM, Dragon Capital, VCBF (S26) | Ký hợp đồng ở Phase 0; nếu chậm thì ra mắt với Trứng Vàng + ETF | Phụ thuộc Phase 0 |

---

## 8. Customer journey (persona P1; `journey_map.csv`)

| | 1. Thấy lời mời | 2. Lập kế hoạch | 3. Cài đặt dòng tiền | 4. Kỳ lương đầu tiên | 5. Tạo thói quen (đến ngày 90) | 6. Rút tiền hoặc đi tiếp |
|---|---|---|---|---|---|---|
| Hành động | Mở tin Zalo hoặc banner | Đặt mục tiêu, trả lời 3 câu, xác nhận | Tạo lệnh chuyển định kỳ ở app ngân hàng | Nhận lương; ngân hàng chuyển tiền | Đọc nhắc ngày lương; bỏ qua một tháng nếu cần | Rút về ngân hàng hoặc bỏ qua một kỳ |
| Câu hỏi trong đầu | "Lại là thưởng có điều kiện?" | "Mua gì, có thể mất bao nhiêu?" | "Chuyển khoản có về thật không?" | "Tiền về chưa, đang ở đâu?" | "Tháng này có đáng không?" | "Bao lâu thì về, mất phí gì?" |
| Cảm xúc (giả thuyết, kiểm bằng pilot) | Nghi ngờ | Phân vân | Sốt ruột | Lo, rồi yên tâm | Có động lực, hoặc quên | Dè chừng |
| Điểm đau hôm nay (bằng chứng) | Mất niềm tin sau đợt thưởng 2025 (trust 55% review tiêu cực trên Google Play H1/2025) | 77% thấy tự quản lý danh mục là khó | Phải rời app; eKYC lỗi (17%) | Ngân hàng báo đã chuyển nhưng app không thấy tiền (17%) | Trì hoãn; app treo, đơ, giật (45%) | Mất tiền với Trứng Vàng 1 tháng mà không rõ vì sao (review 2025), hoặc bị tự tái tục ngoài ý muốn (review 2026, không nêu tên sản phẩm); rút tiền bị chặn vì tên TK ngân hàng không khớp (review 2026) |
| Phản hồi thiết kế | Bỏ thưởng mở TK; nói rõ trong một dòng | 3 câu hỏi; kế hoạch theo kỳ hạn; hiện tháng xấu bằng VND | Số TK riêng + link app ngân hàng + QR; mục tiêu 5 phút | VA ghi có tự động; xác nhận trong vài phút; công bố tỷ lệ đúng hẹn | Nhắc có tên mục tiêu; chuỗi kỳ góp; bỏ qua 1 tháng/năm | Hiện giờ về và chi phí bằng VND trước khi xác nhận; rút miễn phí; thêm bước trước khi chuyển sang giao dịch |
| Số đo | Tỷ lệ mở và bấm | Tỷ lệ xác nhận kế hoạch | Tỷ lệ và thời gian cài đặt | Tỷ lệ ghi có trong ngày (≥99,5%) | Tỷ lệ đạt 3 kỳ (81%) | Thời gian rút trung vị; tỷ lệ chuyển sang sức mua |
| Chịu trách nhiệm | Marketing/CRM | Head of Product; người có chứng chỉ | CTO; ngân hàng đối tác | CTO; Vận hành | Head of Product | CSKH |

**Khoảnh khắc quyết định niềm tin:**
1. **Tiền vào lần đầu** (giai đoạn 4).
2. **Tiền ra lần đầu** (giai đoạn 6).
3. **Lần đầu có sự cố** (màn hình E1). Một sự cố được xử lý tốt có thể tạo niềm tin hơn cả lúc mọi thứ trơn tru, nên E1 phải giữ chuỗi kỳ góp và đưa bước tiếp theo rõ ràng.

---

## 9. Màn hình và microcopy (wireframe low-fi)

- Hình:
  - `outputs/round3/figures/wireframes_journey.png`: 6 màn hình chính, dùng cho slide 8;
  - `outputs/round3/figures/wireframes_errors.png`: 4 trạng thái lỗi, dùng cho appendix G.
- Chữ trên wireframe nằm trong `data/round3/wireframe_copy.json`. Sửa chữ ở đó rồi chạy `python src/round3/diagrams_round3.py`.
- **Thay bằng bản Figma ở giai đoạn thiết kế slide.** Các ô `[x]`, `[rate]`, `[date]` là giá trị app sẽ điền khi chạy thật, không phải số liệu.
- Ở E4, câu "về trước 22:00 hôm nay" chỉ hiện khi đặt bán trong giờ 9h00–14h30 (S18). Ngoài giờ đó, màn hình hiện ngày giao dịch kế tiếp.

| Màn hình | Tiêu đề | Nội dung chính | Nút |
|---|---|---|---|
| 1 Set a goal | What Are You Saving For? | Mục tiêu "Home", VND 36,000,000 đến 10/2029 → "About VND 1,000,000 a month gets you there, before investment returns." | Continue |
| 2 Check your risk | Your Risk Profile | Kỳ hạn; phản ứng nếu kế hoạch giảm 10% trong một tháng; ghi chú TT 121/2020 Điều 24 | See my plan |
| 3 Confirm the plan | Your Plan for Home | 30/30/20/20; tháng xấu bằng VND; "No platform fee. Fund fees of 0.8–1.95% a year are inside fund prices. Bond interest is taxed at 5%."; người có chứng chỉ ký | Confirm plan / Change plan |
| 4 Link your salary | Send Money on Payday | Số TK riêng tại ngân hàng đối tác; 3 bước; Tài khoản Không Ngủ (Never-Sleeping Account) là nơi chờ | Open my bank app |
| 5 First money in | Invested | "VND 1,000,000 received"; mua Trứng Vàng 3 tháng; kỳ sau vào quỹ trái phiếu (lớp thiếu nhất) | View my plan |
| 6 Day 90 | 3 Months in a Row | Tiến độ 3/36 triệu; chuỗi 3; mở khóa ưu tiên Trứng Vàng mới; được bỏ qua 1 tháng/năm | See my progress |
| E1 Transfer not received | (banner) | "We haven't received your October 10 transfer. Banks can take up to 1 business day. Check your bank app, or send it now." Chuỗi kỳ góp giữ đến ngày 15 | Send it now / Skip this month |
| E2 Salary late | Payday Moved? | Chờ đến ngày 15; không phí, không mất chuỗi kỳ góp | Change my payday |
| E3 Pause or skip | Skip October? | 1 lần bỏ qua miễn phí mỗi năm; tạm dừng thì tài sản vẫn được đầu tư | Skip October / Pause plan / Keep my plan |
| E4 Withdraw to bank | Withdraw Money | Miễn phí, về trước 22:00; bán Trứng Vàng trước hạn chỉ hưởng 2,0%/năm; chuyển sang giao dịch cần thêm một bước | Withdraw to my bank / Move to trading account |

**Quy tắc chữ (theo skill ux-writing):**
- Tiêu đề màn hình viết hoa đầu mỗi từ; nút viết như câu thường, dạng động từ + đối tượng.
- Thông báo lỗi theo mẫu: điều gì xảy ra → vì sao → làm gì tiếp; không đổ lỗi cho khách.
- Số tiền luôn ghi bằng VND.
- Không dùng chữ "thưởng" ở bất kỳ màn hình nào.

---

## 10. Service blueprint (`service_blueprint.csv`, hình `service_blueprint.png`)

- **Cấu trúc:**
  - 6 bước: Plan → Set up → Payday → Invest → Track and remind → Withdraw or skip;
  - 5 làn chuẩn: bằng chứng hữu hình, hành động khách, frontstage, backstage, quy trình hỗ trợ;
  - 3 đường: tương tác, hiển thị, tương tác nội bộ;
  - thêm 3 dòng: điểm quyết định, xử lý khi lỗi, người chịu trách nhiệm.
- **Điểm quyết định chính:**
  - kỳ hạn mục tiêu → danh mục;
  - tiền đã về trước ngày chờ chưa;
  - đủ tiền cho một lô ETF chưa;
  - rút về ngân hàng hay sang giao dịch.
- **Xử lý khi lỗi:**
  - tiền chưa về: chờ đến ngày chờ, rồi gợi ý bỏ qua kỳ, chuỗi kỳ góp được giữ;
  - lệnh lỗi: thử lại phiên sau, tiền nằm ở Tài khoản Không Ngủ;
  - lỡ 2 kỳ: gợi ý tạm dừng;
  - chuyển về ngân hàng lỗi: tiền quay lại tiền mặt của kế hoạch, CSKH gọi trong 1 ngày làm việc.
- **Ghi chú cho slide 9:** hình dày chữ (cỡ khoảng 9,6pt ở khổ toàn slide). Khi thiết kế có thể giữ 4 làn chính trên slide (khách, frontstage, backstage, xử lý lỗi), còn bản đầy đủ đưa xuống appendix.

---

## 11. Kế hoạch triển khai

### 11.1 Go-to-market năm đầu (`gtm_year1.csv`; số lấy từ mô hình, base)

| Quý | Mục tiêu | Phân khúc / kênh | Thông điệp | Saver ghi danh trong quý | Cuối quý: funded / số dư | Chi phí quý |
|---|---|---|---|---:|---|---:|
| Q1 (tháng 1–3) | Xây MVP, ký đối tác, beta với TK nhân viên | Nội bộ | — | 0 | 0 / 0 | 2,09 tỷ |
| Q2 (4–6) | Pilot RCT 45.000 TK ngủ, 3 nhánh × 15.000 | TK ngủ có dấu hiệu nhận lương; SMS, Zalo, push, Ensa; tối đa 3 lần liên hệ mỗi TK | *"Your account is ready. Let payday do the investing."* | 600 | 162 / 1,1 tỷ | 3,63 tỷ |
| Q3 (7–9) | Mở rộng trong tệp | TK ngủ đủ điều kiện; khách hoạt động (in-app); TK mới khi mở | *"Keep a core that grows while you trade."* | 4.287 (1.559 TK ngủ; 857 khách hoạt động; 1.871 TK mới) | 1.620 / 10,5 tỷ | 1,69 tỷ |
| Q4 (10–12) | Mở kênh ngoài đầu tiên | 3–5 doanh nghiệp (buổi HR có người tư vấn); khách nhận lương của ngân hàng đối tác | *"An employee benefit that invests your salary."* | 4.527 (có 240 từ doanh nghiệp) | 4.953 / 30,1 tỷ | 1,80 tỷ |

- **Không làm:** thưởng tiền khi mở TK; KOL kiểu "nhận tiền miễn phí"; nhắn lại người đã từ chối (tối đa 3 lần liên hệ); thưởng có điều kiện; khuyến mại hoàn tiền qua đối tác (một review 07/2026 viết "bị zalopay lừa mua chứng khoán hoàn 50k").
- **Ngân sách năm 1:** 9,2 tỷ, giải ngân theo cổng. Marketing và chi phí tiếp cận chỉ chiếm 1,17 tỷ (13%); phần lớn là đội xây dựng và vận hành.

### 11.2 Lộ trình (`roadmap_phases.csv`)

| Phase | Tháng | Mục tiêu | Sáng kiến chính | Cổng | Chi phí | Cuối phase |
|---|---|---|---|---|---:|---|
| 0. Xây và tuân thủ | 1–3 | MVP an toàn, hợp pháp | VA (mục tiêu phí 0đ); hợp đồng quỹ; danh mục mẫu được ký; thông báo UBCKNN; tách luồng khỏi bước kiểm sức mua | Cổng 0: điều khoản đối tác; shadow run ≥99,5%; xác nhận tuân thủ | 2,09 tỷ | Tiền lũy kế −2,1 tỷ |
| 1. Pilot | 4–6 | Đo ghi danh, duy trì, mức góp, tiền mới | RCT 45.000 TK | Cổng 1: chi phí ròng dự báo/TK ≥10 triệu ≤1,6 triệu (kế hoạch 1,29); ghi danh ≥1,5%; dưới 1,0% thì dừng | 3,63 tỷ | 600 saver; −5,7 tỷ |
| 2. Mở rộng trong tệp | 7–12 | Tăng quy mô có kiểm soát | Roll-out TK ngủ, in-app, khi mở TK; nhóm hold-out để đo gói giữ chân; 3–5 doanh nghiệp | Cổng 2: funded ≥80% kế hoạch; CAC/funded ≤127.512đ | 3,49 tỷ | 4.953 funded; −9,2 tỷ |
| 3. Kênh ngoài | 13–24 | Kênh tạo mặc định | Doanh nghiệp; trích % lương qua Open API (sau 01/03/2027); tự tăng mức góp khi tăng lương; ZaloPay làm kênh nạp thứ hai, thử round-up | Cổng 3: TK ≥10 triệu ≥80% kế hoạch; chi phí/TK ≤1,25 lần kế hoạch; doanh nghiệp tham gia ≥39% | 7,28 tỷ | 7.714 TK ≥10 triệu; −16,0 tỷ |
| 4. Tối ưu | 25–36 | Bản quản lý hoàn toàn, kinh tế tốt hơn | Công ty quỹ đối tác hoặc công ty quỹ của DNSE (ĐHĐCĐ 2026); Trứng Vàng mở rộng với trái phiếu và chứng chỉ quỹ của Vietcombank, VietinBank, BIDV (kế hoạch 2026 của DNSE) | Rà hằng quý | 7,23 tỷ | 14.871 TK ≥10 triệu; −22,0 tỷ |

*Slide 13 ghép thêm lộ trình hệ sinh thái của `plan_tech.md` §5 (sửa nền 0–6 tháng → làm tiền ở lại 6–12 tháng → tăng trưởng trên số dư 12–24 tháng).*

**Phương án để sau, không tính trong base:** khách tự chọn dùng ETF trong kế hoạch làm tài sản đảm bảo cho TK ký quỹ thường (mô hình giả định 10% số dư, từ tháng 19).
- NPV base cải thiện từ −25,0 lên −20,9 tỷ nhưng vẫn âm (`payday_option_lending.csv`).
- Phương án này đi ngược mục đích tiết kiệm và chạm đúng mảng ký quỹ bị phạt năm 2026.
- Vì vậy chỉ xét ở Cổng 3, khi pháp chế đồng ý và chủ đề trust dưới 10% review tiêu cực liên quan Payday.

### 11.3 RACI (`raci.csv`)

| Việc | CEO | CFO | CTO | Head of Product | Pháp chế | Marketing | CSKH | Người có chứng chỉ |
|---|---|---|---|---|---|---|---|---|
| Quyết định ở các cổng | A | R | C | R | C | I | I | I |
| Điều khoản đối tác (ngân hàng VA, quỹ, nguồn trái phiếu) | I | A/R | C | C | C | – | – | – |
| Thông báo UBCKNN, ý kiến pháp lý, duyệt khuyến mại | I | I | I | C | A/R | C | – | C |
| Danh mục mẫu và quy tắc đánh giá phù hợp | I | – | I | C | A | – | – | R |
| Xây MVP: bộ lập lịch, VA, phân bổ, dashboard | I | I | A/R | C | C | – | I | – |
| Shadow run và cổng 99,5% | I | I | A/R | C | I | – | I | – |
| RCT: thiết kế và đọc kết quả | I | C | C | A/R | C | C | I | C |
| Tiếp cận khách và thông điệp | I | I | I | A | C | R | I | – |
| Phàn nàn, rút tiền, xử lý sau sự cố | I | I | C | A | C | I | R | – |
| Công bố số đo hằng tháng | I | I | R | A | C | C | C | – |

### 11.4 Risk register: 6 rủi ro, khả năng × tác động (`risk_register.csv`; heat map vẽ ở Phase 3)

| # | Rủi ro | Bằng chứng | K × T | Giảm thiểu | Tín hiệu sớm | Chịu trách nhiệm |
|---|---|---|:---:|---|---|---|
| R1 | Chuyển tiền hoặc app lỗi đúng ngày lương | Sự cố 04/03/2026 dừng lệnh 2 giờ; 83% review tiêu cực 2026 mô tả một thứ bị hỏng | 4 × 5 = **20** | Shadow run; tách luồng khỏi bước kiểm sức mua; khóa phát hành trước ngày cao điểm; trang trạng thái | Tỷ lệ ghi có đúng hẹn <99,5% | CTO |
| R2 | Quá ít TK ngủ ghi danh | Tài khoản Không Ngủ mới đạt 0,8% số TK sau khoảng 6 tháng; nhiều TK 2025 mở vì thưởng | 4 × 4 = **16** | RCT 45.000 TK trước khi mở rộng; dừng nếu dưới 1,0%; kênh mở TK mới | Ghi danh <1,0% ở tháng 6 | Head of Product |
| R4 | Cơ quan quản lý phản đối vai trò của Trứng Vàng hoặc luồng tư vấn | Trứng Vàng bị dừng mở mới 12/2023; khoản phạt 2026 có 275 triệu vì dịch vụ không báo cáo | 3 × 5 = **15** | Thông báo và tham vấn UBCKNN; người có chứng chỉ ký danh mục; quỹ trái phiếu làm lõi dự phòng | Có văn bản hỏi hoặc phản đối của UBCKNN | Pháp chế |
| R3 | Điều khoản đối tác để lại quá ít trên mỗi saver | Ở giá niêm yết VA, trần CAC giảm từ 198.876đ xuống 127.512đ | 3 × 4 = 12 | Cổng 0: phí mục tiêu 0đ, chia phí quỹ ≥30%, biên trái phiếu ≥0,6 điểm | Phí ký >6.191đ/kỳ góp | CFO |
| R5 | Thị trường giảm hoặc xung đột lợi ích làm hỏng trust | VN-Index giảm 115 điểm ngày 9/3/2026 (S37); trust 55% review tiêu cực trên Google Play H1/2025 | 3 × 4 = 12 | Danh mục theo kỳ hạn; không trái phiếu DNSE; hiện tháng xấu bằng VND | Chủ đề trust >10% review tiêu cực liên quan Payday | Head of Product |
| R6 | Tiền kế hoạch bị chuyển sang giao dịch, hoặc lấy từ số dư có sẵn | DNSE đứng thứ 2 môi giới phái sinh (25,38%) | 3 × 3 = 9 | Gắn nhãn nguồn tiền; rút mặc định về ngân hàng; thêm bước trước khi chuyển sang sức mua | Tiền mới <80%, hoặc >10% số tiền rút chuyển sang sức mua | CFO |

*Stress test (`payday_stress.csv`): thị trường giảm ở năm 2 làm số TK ≥10 triệu tháng 36 giảm 12%; ngày lương lỗi ở tháng 9 làm giảm 8%; cả hai làm giảm 18,5%. Tiền tháng 60 chỉ thay đổi −0,2 đến −0,5 tỷ. Rủi ro lớn nằm ở KPI và uy tín, không phải ở tiền.*

### 11.5 Đề nghị với Board (`board_ask.csv`)
- **Duyệt 6,6 tỷ cho Phase 0–1** (tháng 1–6): nhu cầu tiền theo mô hình 5,72 tỷ cộng dự phòng 15%; trong đó xây dựng 4,2 tỷ, vận hành và marketing từ tháng 4.
- **5 việc giao ngay:**
  1. chọn ngân hàng VA, mục tiêu phí thu hộ 0đ;
  2. ký 1–2 công ty quỹ;
  3. nộp thông báo UBCKNN và tham vấn về vai trò của Trứng Vàng;
  4. người có chứng chỉ ký danh mục mẫu;
  5. chấp thuận ngân sách khoảng 1,29 triệu đồng cho mỗi TK mới ≥10 triệu, làm thước đo ở các cổng tháng 6, 12, 24.

---

## 12. File và cách cập nhật
- Nội dung tác giả soạn: `data/round3/{gtm_year1_plan, roadmap_plan, raci, risk_register, trust_metrics, legal_map, glide_path, journey_map, service_blueprint}.csv` và `wireframe_copy.json`.
- Script: `src/round3/plan_tables.py` (điền số từ mô hình vào các ô `{...}`), `src/round3/diagrams_round3.py` (wireframe, blueprint).
- Bảng ra: `outputs/round3/tables/` (cùng tên). Hình: `outputs/round3/figures/`.
- Chạy lại tất cả: `python src/round3/run_round3.py`.

## Nguồn
- Mô hình và data: `outputs/round3/tables/payday_*.csv`, `reviews_2026_*.csv`; `data/manual/dnse_accounts.csv`; World Bank (2025) Findex; NSO (2026).
- Nguồn web đã kiểm: `data/round3/sources_round3.csv`. Các nguồn dùng trực tiếp trong file này: S02, S10, S12, S13, S14, S17, S18, S22–S26, S30, S32, S33–S37.
- Hành vi: O'Donoghue & Rabin (1999); Karlan, McConnell, Mullainathan & Zinman (2016); Ashraf, Karlan & Yin (2006); Thaler & Benartzi (2004); Madrian & Shea (2001), chỉ dùng cho kênh payroll.

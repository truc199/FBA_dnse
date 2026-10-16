# Rủi ro công nghệ lõi cho Payday Portfolio — tương quan với điểm yếu DNSE và bối cảnh ngành

*Lập ngày 14/10/2026, cho Round 3A (deadline nộp 20/10/2026 21:00). Phục vụ tiêu chí "Implementation, validation and risk management" (30/100 điểm — nặng nhất trong rubric).*

**Quy ước:** ✅ = có nguồn kiểm chứng ngày hôm nay; ⚠️ = tìm được nhưng chưa xác nhận đầy đủ (cần tra lại trước khi trích dẫn bằng lời trong Q&A); ❌ = không tìm thấy nguồn xác nhận, cần bỏ hoặc nêu như giả định.

---

## 0. Khung phân tích

Payday Portfolio (Round 2) cần 5 khối công nghệ lõi **mới**, mỗi khối có một lỗ hổng đặc trưng. Cột "Ràng buộc từ hạ tầng cũ" cho biết hạ tầng Entrade X hiện tại của DNSE giới hạn/khuếch đại rủi ro đó như thế nào — đây là phần user yêu cầu "cả hai" (stack mới + hạ tầng cũ làm ràng buộc).

| # | Khối công nghệ mới | Vai trò trong Payday Portfolio |
|---|---|---|
| 1 | Standing-order / scheduling engine | Trích tiền tự động vào ngày lương |
| 2 | Open API / bank-sweep integration | Kết nối tài khoản ngân hàng khách hàng |
| 3 | Investment execution engine | Rót tiền vào Trứng Vàng, ETF VN30, quỹ trái phiếu đối tác |
| 4 | Cash-yield / MMF custody (Phase 2) | Trả lãi thị trường cho tiền chờ đầu tư |
| 5 | Trust & reliability layer | Minh bạch điều khoản, không phí đóng TK, báo cáo UBCKNN trước ra mắt |

---

## 1. Số liệu nền — điểm yếu DNSE hiện tại (lấy trực tiếp từ `outputs/tables/computed/`, chạy lại 14/10/2026, khớp report đã nộp)

**Table D1 — chủ đề trong review tiêu cực Google Play DNSE:**

| Chủ đề | % review tiêu cực | % helpful votes |
|---|---:|---:|
| Crash, treo, lỗi đăng nhập, lệnh chậm (**stability**) | **27,3%** | 21,4% |
| Mở TK, eKYC, OTP (**onboarding**) | **21,2%** | 17,9% |
| Cáo buộc lừa đảo trực tiếp | 17,6% | 28,2% |
| Điều khoản thưởng đăng ký | 8,6% | 17,8% |
| Nạp/rút tiền chậm | 5,0% | 6,7% |
| Không đóng được TK, phí đóng TK | 3,6% | 11,3% |
| **Bất kỳ chủ đề trust (gộp)** | **24,1%** | **42,9%** |
| **Bất kỳ chủ đề product (stability+onboarding, gộp)** | **42,4%** | 34,1% |

**Table D2 — so sánh 3 app trên App Store (2025–2026):**

| App | Reliability (%review / %votes) | Trust (%review / %votes) | Mean |
|---|---|---|---|
| **DNSE Entrade X** | 37,6 / 30,2 | **36,8 / 50,4** | 2,25 |
| VPS SmartOne | 45,7 / 45,1 | 7,8 / 7,3 | 1,47 |
| FPTS EzTrade | 20,7 / 17,7 | 0,8 / 1,8 | 2,31 |

**Đọc hiểu quan trọng (khác với giả định trước đây trong `weakness.md`).** *Cập nhật 15/10:* bảng trên gộp cả giai đoạn 2025–2026. Nếu chỉ xét năm 2026, trust của DNSE giảm còn 14,7% (Play) và 12,5% (iOS), còn reliability lên 58,8% và 75%, cao nhất 3 app. Xem `review_round2.md` L1.
- DNSE **không phải** app kém ổn định nhất ngành — VPS tệ hơn về reliability (45,7% vs 37,6%). DNSE kém nhất ở **trust** (36,8% vs 7,8% VPS, 0,8% FPTS) — gấp 4,7 lần VPS và 46 lần FPTS. Đây là vấn đề **đặc thù của DNSE**, không phải vấn đề chung ngành.
- Trust complaints chiếm tỷ trọng vote cao bất thường (42,9% trên Google Play, 50,4% trên App Store) — tức là **loại khiếu nại này được cộng đồng xác nhận/đồng tình nhiều nhất**, không phải noise.
- → Hệ quả thiết kế: **Trust & reliability layer (khối 5) phải ưu tiên minh bạch điều khoản hơn là chỉ chống crash app.** Stability vẫn quan trọng (27,3%, lớn nhất về số lượng) nhưng không phải là khác biệt cạnh tranh — trust mới là.

---

## 2. Tiền lệ pháp lý trực tiếp — vụ phạt DNSE tháng 8/2026 ✅ (xác nhận lại qua web, có chi tiết MỚI chưa có trong `weakness.md`)

Nguồn: [vnbusiness.vn](https://vnbusiness.vn/dnse-bi-phat-8025-trieu-dong-phai-dung-mot-so-dich-vu-ky-quy.html), [thoibaotaichinhvietnam.vn](https://thoibaotaichinhvietnam.vn/cong-ty-co-phan-chung-khoan-dnse-bi-xu-phat-do-vi-pham-quy-dinh-cho-vay-ky-quy-163400.html), [thanhtra.com.vn](https://thanhtra.com.vn/ket-luan-thanh-tra-E17BD7A25/thanh-tra-chung-khoan-nha-nuoc-chi-ro-loat-vi-pham-tai-cong-ty-co-phan-chung-khoan-dnse-98015d1ed.html)

Tổng phạt **802,5 triệu đồng**, chia 2 phần:
1. **137,5 triệu** — cho khách đặt lệnh mua khi tài khoản chưa đủ tiền.
2. **275 triệu (khoản lớn nhất)** — triển khai dịch vụ tài chính **mà chưa báo cáo UBCKNN**, cụ thể 3 dịch vụ: "ứng lãi vị thế", "ứng rút ký quỹ ngoài giờ", "ứng trước ký quỹ phục vụ hoạt động môi giới chứng khoán phái sinh", trong giai đoạn 01/01/2024–16/06/2026. Biện pháp khắc phục: **buộc dừng cả 3 dịch vụ này**.
3. **Chi tiết MỚI (chưa có trong weakness.md):** thanh tra còn nêu DNSE **giải ngân cho vay ký quỹ và ứng trước tiền bán cho người nội bộ hoặc người liên quan của người nội bộ** — đây là vi phạm quản trị/xung đột lợi ích, khác loại với vi phạm "chưa báo cáo".

**Áp dụng vào Payday Portfolio:**
- Đây là **tiền lệ trực tiếp, cùng loại rủi ro** với bất kỳ cơ chế "ứng trước" hay "thanh khoản tức thì" nào trong Payday Portfolio (ví dụ sức mua T+0 qua ứng trước tiền bán chứng chỉ quỹ, đã nêu ở `weakness.md` Lỗ hổng 1). Report Round 2 đã đúng khi đặt điều kiện "chỉ triển khai khi UBCKNN chấp thuận" — giờ có số liệu cụ thể để trích dẫn bằng lời trong Q&A/debate (802,5 triệu, 275 triệu riêng cho hành vi không báo cáo).
- **Phát hiện mới cần thêm vào thiết kế:** risk register của khối "Trust & reliability layer" cần thêm một dòng về **kiểm soát giao dịch nội bộ/người liên quan** — nếu nhân viên DNSE có thể tự ưu tiên sweep/advance cho tài khoản mình hoặc người thân, đây là đúng loại vi phạm vừa bị phạt. Cần tách bạch rõ cơ chế phê duyệt cho Payday Portfolio không đi qua kênh thủ công có thể bị lợi dụng.
- ⚠️ Có một khoản phạt khác 125 triệu đồng (QĐ 1203/QĐ-XPHC) về hạn chế giao dịch ký quỹ — **chưa xác nhận được có cùng đợt với 802,5 triệu hay không**. Không nên gộp hai con số khi trích dẫn.

---

## 3. Bối cảnh ngành cho từng khối công nghệ

### Khối 2 — Open API / bank-sweep
✅ Thông tư 64/2024/TT-NHNN có hiệu lực từ 01/03/2025, là văn bản pháp lý chuyên biệt đầu tiên về Open API ngân hàng. Đến 2025, **gần 40% ngân hàng thương mại đã phát triển API vượt danh mục cơ bản** theo Thông tư 64. [Nguồn tổng hợp](https://thitruongtaichinhtiente.vn/cuc-truong-le-hoang-chinh-quang-4-tru-cot-dua-ngan-hang-so-viet-nam-tang-toc-nam-2026-77813.html). SBV xác định Open Banking là **định hướng chiến lược trọng tâm ngành ngân hàng giai đoạn 2026–2030** — lộ trình gồm 3 bước: tuân thủ kỹ thuật theo quy định → mở rộng chia sẻ dữ liệu → Open Finance toàn diện.
- ✅ **Đính chính 15/10/2026:** mốc **01/03/2027 đã được xác nhận**. Điều khoản chuyển tiếp của Thông tư 64/2024 yêu cầu ngân hàng tuân thủ trước 01/03/2027 (và gửi danh mục API kèm kế hoạch trước 01/07/2025). Bản ghi trước đây nói mốc này "không xác nhận được" là sai. Report Round 2 trích mốc này là đúng. Lưu ý duy nhất: bên thứ ba vẫn phải ký thỏa thuận với từng ngân hàng, nên kết nối không tự động.
- ✅ "Cuộc chiến quản trị CASA" là chủ đề thời sự thật (Saigon Times có loạt bài tháng 6–7/2026) — xác nhận ngân hàng đang chủ động phòng thủ dòng tiền CASA, đúng như Lỗ hổng 3 trong `weakness.md`. CASA toàn hệ thống cuối 2025 ~28,9%, tăng gần 40% — cho thấy đây là mặt trận cạnh tranh nóng, ngân hàng có động lực mạnh để giữ tiền lương ở lại, không dễ hợp tác sweep.

### Khối 4 — Cash-yield / MMF custody
❌ Không tìm được nguồn xác nhận quy định thanh toán T+1 cho chứng chỉ quỹ mở/quỹ thị trường tiền tệ tại Việt Nam. Thông tin tìm được chỉ là ví dụ nước ngoài (Deutsche Börse Xetra, TMX Canada). **Khuyến nghị: không nêu con số "T+1" cụ thể cho Việt Nam khi thuyết trình** — chỉ nói chung "chu kỳ thanh toán chứng chỉ quỹ chậm hơn nhu cầu rút tiền tức thì", đúng tinh thần `weakness.md` nhưng tránh bị hỏi ngược nguồn.

### Khối 1, 3 — Scheduling + Investment execution (đối thủ cạnh tranh)
✅ TCBS đã có sẵn **iTracker** (danh mục tự động hóa) và **Fundmart** (31 quỹ đối tác, chiếm 55% NAV thị trường quỹ mở trong nước, ~12.000 khách/tháng tham gia, +33% YoY). [Nguồn](https://thitruongtaichinhtiente.vn/print/80857.html). **Không tìm thấy** TCBS, Fmarket, Finhub hay Infina có tính năng trích lương theo kỳ lương cụ thể (payday-triggered) — đây có thể là **điểm khác biệt thật của Payday Portfolio** so với các giải pháp "tự động hóa danh mục" hiện có (vốn kích hoạt theo lịch cố định, không theo ngày lương thực tế của từng khách). Nên nhấn mạnh sự khác biệt này trong slide "Solution design" — nhưng nên tự kiểm tra lại trên app TCBS/Fmarket trước khi khẳng định chắc trong Q&A, vì search không phủ hết mọi tính năng.
- ⚠️ DNSE vừa qua AGM 26/03/2026: mục tiêu DT 1.736 tỷ (+18,2%)/LNTT 550 tỷ (+61,8%) — khớp số đã có trong report. Không tìm thấy tin nào về DNSE tự ra mắt tính năng tích sản tự động mới trong Q3/2026 — tức là **cửa sổ cơ hội cho Payday Portfolio vẫn còn mở**, DNSE chưa tự làm trước.

### Khối 5 — Trust layer / sinh trắc học
✅ Quyết định 2345 (hiệu lực 01/07/2024) + Thông tư 17/2024 (hiệu lực 01/01/2025 cá nhân, 01/07/2025 tổ chức): bắt buộc xác thực sinh trắc học cho giao dịch >10 triệu/lần hoặc >20 triệu/ngày, và trước giao dịch đầu tiên trên thiết bị mới.
- ❌ **Con số "86 triệu tài khoản bị đóng" (từng ghi trong `docs/compass_artifact...md`) KHÔNG xác nhận được qua tìm kiếm hôm nay.** Nên bỏ con số này hoặc đánh dấu rõ là chưa kiểm chứng nếu dùng lại — tránh trích dẫn sai trong Q&A có thể bị giám khảo bắt bẻ.
- ✅ Có xác nhận: sau ~3 tháng áp dụng xác thực sinh trắc học, số vụ gian lận giảm mạnh (một nguồn nói giảm 72% số tài khoản lừa đảo). Điều này **tốt cho Payday Portfolio** — hạ tầng định danh khách hàng đã sạch hơn trước, giảm rủi ro tài khoản giả mạo nhận sweep tiền lương.

---

## 4. Risk register hợp nhất (dùng trực tiếp cho slide "Implementation, validation and risk management" — 30 điểm)

| Khối công nghệ | Rủi ro | Bằng chứng DNSE | Bằng chứng ngành | Mitigation đề xuất |
|---|---|---|---|---|
| 1. Scheduling engine | Giao dịch trễ/thất bại đúng ngày lương → tái tạo đúng complaint lớn nhất đang có | Stability 27,3% review tiêu cực, 21,4% votes | — | Transfer success ≥99,5% test trước ra mắt (đã có trong Table F6 test 6 của bản nộp). Năm 2026 reliability chiếm 58,8% (Play) và 75% (iOS) review tiêu cực, xem `review_round2.md` L1 |
| 2. Open API/bank-sweep | Ngân hàng chủ động phòng thủ CASA, hạn mức auto-debit thấp, OTP mỗi giao dịch | Onboarding 21,2% — khách đã ngại OTP/eKYC, thêm 1 lớp xác thực sẽ làm nặng thêm | "Cuộc chiến CASA" xác nhận thời sự 2026; CASA hệ thống ~28,9%, tăng ~40% | Giai đoạn 1 dùng lệnh định kỳ trong app ngân hàng của khách (không cần API); ưu tiên ngân hàng trả lương làm đối tác |
| 3. Investment execution | Rủi ro vận hành khi rót tiền tự động vào nhiều sản phẩm (Trứng Vàng/ETF/quỹ đối tác) | — | TCBS iTracker/Fundmart đã chạy ổn định, 12.000 khách/tháng — chứng minh mô hình khả thi về mặt vận hành | Bắt đầu với danh mục hẹp (Trứng Vàng + 1 ETF), mở rộng dần |
| 4. Cash-yield/MMF (Phase 2) | Thanh khoản T+0 khách mong đợi vs chu kỳ thanh toán chứng chỉ quỹ chậm hơn | — | Không xác nhận được T+1 VN cụ thể — nên nói chung, không cam kết số | Phase 1 chấp nhận T+1 cho người tiết kiệm theo tháng (ít cần rút gấp); SSC pre-consultation trước Phase 2 |
| 5. Trust layer | **Rủi ro cao nhất, đặc thù DNSE** — không phải app tệ nhất ngành nhưng trust tệ nhất ngành (36,8% vs VPS 7,8%, FPTS 0,8%) | Trust 24,1% review/42,9% votes Google Play; 36,8%/50,4% App Store | DNSE vừa bị phạt 802,5 triệu (275tr vì không báo cáo trước khi ra mắt dịch vụ ứng trước) + vi phạm giao dịch nội bộ/người liên quan | Báo cáo UBCKNN trước ra mắt (đã có trong report); **thêm mới:** kiểm soát tách bạch để nhân viên/người liên quan không được ưu tiên xử lý thủ công trong cơ chế sweep/advance |

---

## 5. Việc cần làm tiếp

1. Dùng risk register trên làm nội dung cho 1–2 slide "Implementation & Validation" của Round 3A — đây là tiêu chí 30 điểm, nặng nhất.
2. Tự vào app TCBS/Fmarket kiểm tra lại xem có tính năng trích lương theo ngày lương thực tế hay không, trước khi khẳng định "Payday Portfolio là duy nhất" trong Q&A.
3. Khi trả lời giám khảo về rủi ro pháp lý, trích cụ thể: "802,5 triệu đồng, trong đó 275 triệu vì triển khai dịch vụ ứng trước mà chưa báo cáo UBCKNN" — số liệu xác nhận hôm nay, mạnh hơn nói chung chung "công ty từng bị phạt".
4. Tránh trích các số **chưa xác nhận** trong bài cũ: "86 triệu tài khoản đóng", "chứng chỉ quỹ T+1 tại Việt Nam". Nếu giám khảo hỏi nguồn sẽ không trả lời được. (Mốc Open API 01/03/2027 **đã xác nhận**, dùng được.)
5. Bổ sung dòng kiểm soát nội bộ/người liên quan vào Trust layer. *Đính chính 15/10:* Appendix D của report Round 2 **đã nêu** vi phạm cho vay người nội bộ trong hồ sơ xử phạt, nhưng chưa đưa nó vào thiết kế kiểm soát của Payday. Phần còn thiếu là biện pháp kiểm soát, không phải thông tin.

---

## Nguồn

- [DNSE bị phạt 802,5 triệu đồng, phải dừng một số dịch vụ ký quỹ](https://vnbusiness.vn/dnse-bi-phat-8025-trieu-dong-phai-dung-mot-so-dich-vu-ky-quy.html)
- [Công ty cổ phần chứng khoán DNSE bị xử phạt do vi phạm quy định cho vay ký quỹ](https://thoibaotaichinhvietnam.vn/cong-ty-co-phan-chung-khoan-dnse-bi-xu-phat-do-vi-pham-quy-dinh-cho-vay-ky-quy-163400.html)
- [Thanh tra Chứng khoán Nhà nước chỉ rõ loạt vi phạm tại DNSE](https://thanhtra.com.vn/ket-luan-thanh-tra-E17BD7A25/thanh-tra-chung-khoan-nha-nuoc-chi-ro-loat-vi-pham-tai-cong-ty-co-phan-chung-khoan-dnse-98015d1ed.html)
- [4 trụ cột đưa ngân hàng số Việt Nam tăng tốc năm 2026](https://thitruongtaichinhtiente.vn/cuc-truong-le-hoang-chinh-quang-4-tru-cot-dua-ngan-hang-so-viet-nam-tang-toc-nam-2026-77813.html)
- [Cuộc chiến quản trị CASA, diễn biến theo từng nhóm ngân hàng](https://thesaigontimes.vn/cuoc-chien-quan-tri-casa-phan-2-dien-bien-theo-tung-nhom-ngan-hang-ra-sao/)
- [TCBS Fundmart/iTracker — Chứng khoán](https://thitruongtaichinhtiente.vn/print/80857.html)
- [DNSE sets profit growth target above 60%, raising VND 3,500 billion through bonds](https://ir.dnse.com.vn/en/post/dnse-sets-profit-growth-target-above-60-raising-vnd-3-500-billion-through-bonds-779.htm)
- [DHĐCĐ DNSE đặt mục tiêu lợi nhuận tăng trưởng 62%, chủ trương thành lập công ty chứng khoán tại IFC](https://thitruongtaichinhtiente.vn/dhdcd-dnse-dat-muc-tieu-loi-nhuan-tang-truong-62-chu-truong-thanh-lap-cong-ty-chung-khoan-tai-ifc-80635.html)
- [Số vụ gian lận lừa đảo giảm mạnh sau gần 3 tháng thực hiện xác thực sinh trắc học](https://doanhnghiephoinhap.vn/so-vu-gian-lan-lua-dao-giam-manh-sau-gan-3-thang-thuc-hien-xac-thuc-sinh-trac-hoc-83707.html)
- `outputs/tables/computed/table_D1_*.csv`, `table_D2_*.csv` (dữ liệu nội bộ, pipeline chạy lại 14/10/2026)

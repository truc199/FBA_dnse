# Nhật ký làm việc — FBA Season 6 Round 2 (DNSE Securities)

Hạn nộp: 21:00 ngày 27/09/2026. Giới hạn phần thân report: 3.500 từ.

## 22/09 — Phiên 1: đọc dữ liệu và tra cứu DNSE
- Đọc `FBA_Round2_DNSE_data_pack.xlsx` và `FBAR2_2026_DNSE_Analysis.docx` ban đầu, ghi nhận xét vào `doc/dnse.md`.
- Phát hiện: tổng LNTT ngành bị hard-code 9.977 tỷ, trong khi cộng thực tế trong sheet ra 8.418,9 tỷ (chênh 1.558 tỷ, chưa giải thích).
- Chẩn đoán vấn đề gốc của DNSE: **"tài khoản nhiều, tiền ít"** — 12,27% tài khoản thị trường nhưng chỉ 2,88% giao dịch HNX, <2,94% HOSE, 1,39% dư nợ margin. Một tài khoản DNSE giao dịch bằng 0,23 và vay bằng 0,11 so với tài khoản trung bình thị trường.
- Tra cứu internet: hồ sơ công ty, Entrade X, Margin Deal, Future X, các lần bị UBCKNN phạt (mới nhất 17/8/2026, phạt 802,5 triệu, buộc dừng 3 dịch vụ phái sinh phái sinh).
- Tạo `doc/dnse_problems_and_product_strategy.md`: Section 1 (vấn đề DNSE) + Section 2 (bài toán BA, chiến lược sản phẩm số).

## 23/09 — Phiên 2: audit code và sửa pipeline
- Audit toàn bộ code Python/JS, ghi vào `doc/code_audit.md`. Lỗi chính:
  - Regex lọc referral spam bắt nhầm review thật (ví dụ "mà mọi người", "nhập mã OTP").
  - Tỷ trọng dân số trong `04_segment_model.py` sai (Secondary educ or more phải đứng hạng 1, không phải In labour force).
  - Report viết sai: VPS không hề bị giới hạn 1.200 review do phân trang.
- Chạy lại toàn bộ pipeline trên máy, đối chiếu bản đã nộp, sửa code theo audit → 26/26 rồi 28/28 test tự động pass.
- Tìm thêm 5 lỗi (2 lỗi do chính lần sửa trước gây ra) và sửa hết, gồm: referral regex bắt nhầm số tiền, thiếu nhãn "ui" ở Figure 5, ngày ghi sai timezone, file audit VPS không khớp bảng, câu Exec Summary nói quá so với dữ liệu.
- Thêm `02c_appstore_scrape.py`: cào review App Store VN của DNSE/VPS/FPTS qua RSS Apple, dùng để đối chiếu (không gộp vào bảng chính vì lịch sử ngắn).
- Research: vì sao DNSE giữ zero-fee dù lỗ, cách cạnh tranh với VPS ở mảng phái sinh (margin phái sinh là ký quỹ NĐT nộp, không phải vốn công ty bỏ ra).

## 23/09 — Phiên 3: hỏi đáp chiến lược (không sửa file)
- Lợi nhuận DNSE đến từ đâu: chủ yếu lãi cho vay margin (37,9%→39,6%); mảng môi giới đang lỗ.
- Vì sao vẫn giữ zero-fee dù sụt lãi Q1/2026: cam kết "trọn đời", chiến lược chiếm thị phần, chi phí acquisition là chi phí một lần.
- Giả thuyết "nuôi Gen Z để kiếm tiền về sau": data Findex phản bác — nhóm 15-24 tuổi có priority score thấp nhất (2,25 so với ~9,0-9,3 của nhóm đi làm/thu nhập cao).

**→ Commit `889b374` (24/09 15:16): "Initial commit: FBA DNSE analysis project"**

## 24/09 — Phiên 4: thay số báo chí bằng nguồn chính thống (phiên dài nhất, xuyên đêm)
- Viết `01b_dnse_financials_fetch.py`: kéo toàn bộ BCTC DNSE (KQKD, bảng cân đối, lưu chuyển tiền tệ, thuyết minh) 34 quý Q1/2018→Q2/2026 qua API Vietcap.
- Thay số báo chí bằng số BCTC trong Excel/report:
  - Doanh thu 2025: 1.457,9 tỷ (không phải 1.467 tỷ theo báo).
  - LNTT H1/2026: 111,6 tỷ theo BCTC soát xét KPMG (báo chí ghi 113,1 tỷ theo bản tự lập).
  - Bỏ hẳn con số "dự phòng tự doanh +405%" — không dòng BCTC nào tái lập được.
  - Tài sản khách hàng/tài khoản: ~14,8 triệu (không phải 34,7 triệu như báo cũ tính).
- Viết `bctc_analysis.md` + `05c_charts_bctc.py` (10→14 chart trong `fig/bctc/`). Đối chiếu 36 chỉ tiêu báo chí: 27/36 khớp đúng BCTC, 9 chỗ lệch.
- Phát hiện xu hướng dài hạn 2018-2026: 2021-2022 là năm chuyển đổi (vốn điều lệ 160→3.000 tỷ); lợi nhuận lõi (loại tự doanh) đi ngang 128-221 tỷ/năm dù doanh thu tăng 3,2 lần; môi giới lỗ 16 quý liên tiếp từ Q3/2022, lũy kế -190 tỷ.

**→ Commit `883a12d` (24/09 18:31): "Update: bổ sung phân tích BCTC"**

- Sau commit (chưa commit tiếp):
  - `01c_peer_financials_fetch.py`: BCTC 44 công ty chứng khoán qua Vietcap. Phát hiện VPS đã niêm yết với mã **VCK** (mã "VPS" trên HOSE là công ty thuốc trừ sâu khác).
  - Sửa lỗi bằng nguồn gốc: báo cáo cũ viết ĐHCĐ 2026 "không phê duyệt" công ty quản lý quỹ — thực tế nghị quyết Điều 15 **có** thông qua chủ trương, năm thứ hai liên tiếp.
  - `01d_market_macro_fetch.py`: thị phần HOSE/HNX từ 139+ thông báo gốc, số tài khoản VSDC, World Bank WDI, NSO. Sửa số báo sai: thị phần phái sinh Q2/2025 là 17,62% (báo ghi 17,33%); bù 2 quý thiếu (Q2-Q3/2024).
  - Thêm chart 11-14 và 3 tab Excel mới (Market share history, Broker totals, Market and macro).
  - Vẫn còn 2 nhóm số liệu là báo chí: tổng dư nợ toàn ngành 453.800 tỷ, và số tài khoản DNSE 2026 (1,65tr/1,7tr — DNSE không tự công bố nguồn gốc cho số này).

## 24/09 — Phiên 5: kiểm tra đề bài và số liệu tài khoản (chạy song song phiên 4)
- Đọc kỹ question booklet Round 2 → kết luận: **không lạc đề**, chọn DNSE đúng bước Company Selection; nhưng cần khớp từ khóa đề bài hơn.
- Tỷ lệ tài khoản active DNSE chỉ 5,7% (85.739/1.512.920), so với ~30-34% ở TCBS, 30,8% ở VNDirect — **thấp hơn hẳn ngành**, không phải hiện tượng bình thường ở mức này (dù khoảng cách total-vs-active nói chung là phổ biến, vì MBS từng đóng 543.753 "tài khoản chết" trong 1 tháng).
- Thêm mục 1.8 (so sánh active rate) và 1.9 (bảng kiểm chứng 16 số liệu) vào `doc/dnse_problems_and_product_strategy.md`.
- Phát hiện 3 lỗi trong report **chưa sửa**:
  1. Tỷ trọng tài khoản 12,27% bị lệch ngày (tử số 30/6, mẫu số 31/8) → đúng ra phải ≥12,66%.
  2. Câu giới hạn B3 nói "không công ty nào khác công bố số tài khoản" — sai, VPS và TCBS đều có công bố.
  3. Câu "faster than any competitor" không kiểm chứng được, nên thay bằng số cụ thể (DNSE 518.514 tài khoản mới 2025 so với TCBS ~138.000, VPS ~124.000).

## Việc còn tồn đọng (tính đến 25/09)
1. Số từ phần thân report: 3.797, cần cắt xuống ≤3.500.
2. Report chưa dùng từ khóa đề bài: "target market", "market gap", "senior management".
3. Sửa câu giới hạn sai ở `06_build_report.js:646` (số tài khoản đối thủ có công bố).
4. Sửa câu "faster than any competitor" ở `06_build_report.js:388`.
5. Quyết định mẫu số tỷ trọng tài khoản (12,24% ngày lệch, hay ≥12,66% cùng ngày 30/6) rồi build lại — chỉ cần sửa `VSDC_LATEST` trong `01d_market_macro_fetch.py:65`.
6. Commit các thay đổi sau `883a12d`: 01c, 01d, 2 file JSON, chart 11-14, cập nhật strategy doc, workbook/report/README.

## File quan trọng
- **Bản nộp cuối:** `FBAR2_2026_DNSE_Analysis.docx` (gốc, không phải bản trong `doc/`), `FBA_Round2_DNSE_data_pack.xlsx`.
- **Sửa nội dung report:** `06_build_report.js`. **Sửa Excel:** `07_build_workbook.py`.
- **Kéo data:** `01b` (BCTC DNSE), `01c` (BCTC đối thủ), `01d` (thị phần/vĩ mô), `brokers.py`.
- **Vẽ chart:** `05a`, `05b`, `05c`.
- **Tài liệu làm việc chính:** `doc/dnse_problems_and_product_strategy.md`, `bctc_analysis.md`, `doc/code_audit.md`.
- **Thứ tự chạy pipeline:** xem `README.md`.

## 25/09 — Phiên 6: kiểm tra chất lượng và sửa bản report mới
- Kiểm tra lại độc lập toàn bộ data: BCTC khớp với báo cáo thường niên 2025 của DNSE; Findex khớp 796/796; review tái lập đúng 100%; thị phần HNX/HOSE đúng với thông báo gốc.
- Đánh giá bản mới `FBAR2_2026_Team_name.docx`: đã sửa được gần hết lỗi logic và flow của bản cũ; còn 10 lỗi nhỏ về số liệu và trích nguồn.
- Đã sửa trực tiếp 7 lỗi trong docx (bản gốc lưu ở `_backup_2026-09-25/`):
  1. Active users: đổi thành số tháng 12/2025 (theo định nghĩa trong báo cáo thường niên) và thêm ý số active tăng gấp đôi so với 2024.
  2. Thị phần phái sinh Q2–Q3/2024 có công bố (5,11% và 5,30%): sửa text và vẽ lại Hình 1.
  3. Sửa câu sai "nhóm 15–24 có investable surplus thấp nhất".
  4. So sánh lãi suất cùng loại: idle cash so với TCBS iPower và tài khoản sinh lời tự động của ngân hàng, không so với tiền gửi kỳ hạn 12 tháng.
  5. Trích nguồn gốc (HNX, HOSE, VSDC, BCTC qua Vietcap) thay cho nguồn báo; thêm 4 tài liệu tham khảo.
  6. Số theo báo cáo thường niên: 433.532 tài khoản mới 2024; tài sản/tài khoản 39,1 → 35,3 triệu; Ensa 72.000; tiến độ doanh thu 49,1%. Vẽ lại Hình 4 và sửa Hình 5.
  7. Giá cổ phiếu so với giá IPO: nêu cả mức chưa điều chỉnh và đã điều chỉnh.
- Cập nhật lại số trang ở mục lục, danh sách hình và danh sách bảng theo bố cục khi mở bằng Word.
- Chưa làm: các điểm 8–10 (khoản đầu tư tài sản số và sàn carbon chỉ có nguồn báo; một vài câu lập luận cần viết mềm hơn; tên team); bổ sung các số mới vào data pack Excel.

## 25/09 — Phiên 6 (tiếp): chấm theo rubric và vá lỗ hổng phân tích
- Chấm bản final theo rubric của booklet: khoảng 79/100 trước khi sửa, khoảng 84–85 sau khi sửa (chưa tính phạt độ dài). Bản đánh giá đầy đủ ở `doc/final_report_review.md`.
- Đã vá 12 lỗ hổng trong docx:
  - Cohort 2025: đổi thành khoảng giá trị theo HNX/UPCoM.
  - Giả thuyết "thu hút trước, kiếm tiền sau": để mở, không bác bỏ.
  - Thêm VPS vào Bảng 5 và Hình 6.
  - Ghi rõ thước đo "tiền" không gồm tiền ký quỹ phái sinh.
  - Thêm wealthtech vào Bảng 11.
  - Thống nhất thị trường mục tiêu; nêu sai số mẫu Findex.
  - Nêu chỗ khảo sát mâu thuẫn với giải pháp tự động.
  - Độ ổn định app thành điều kiện ra mắt.
  - Thừa nhận "balance gap" là vấn đề bao trùm, đọc theo cây vấn đề.
  - Thêm quick win.
  - Định lượng kênh cho vay trong Bảng 25; nâng test 6 lên High; cấu trúc pháp lý chặn trước pilot.
- Việc còn lại: cắt phần thân xuống 3.500 từ (hiện 11.814 từ văn bản); điền tên team; xuất PDF; kiểm nguồn cho Fmarket/Infina/Finhay.

## 25/09 — Phiên 6 (tiếp): trả lời 5 lỗ hổng trong weakness.md
- Thêm vào report (mục 4.1, 4.3, 4.4, Bảng 23, Hình 25):
  - Lãi do ngân hàng hoặc quỹ trả; dùng tiền trong ngày chỉ khi UBCKNN chấp thuận, nếu không thì T+1.
  - Payday Portfolio là một tab tích sản riêng trong Entrade X.
  - Lệnh chuyển tiền định kỳ và chọn ngân hàng trả lương làm đối tác sweep.
  - Trường hợp xấu nhất khoảng 59 tỷ/năm nếu DNSE tự trả thưởng lãi, nên chỉ thưởng cho tiền mới.
  - Nếu test 6 thất bại thì thu hẹp quy mô.
- Sửa lại cách khắc phục #1, #4, #5 trong `weakness.md`: bỏ lập luận "nguồn vốn rẻ" và cơ chế chi phí vốn sai.
- Bản trước lưu ở `_backup_2026-09-25/…v2_sau_va_lo_hong.docx`.

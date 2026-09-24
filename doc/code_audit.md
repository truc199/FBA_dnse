# Code audit: pipeline dữ liệu và chart DNSE (FBA Round 2)

Ngày audit: 23/09/2026. Phạm vi: 12 file code ở thư mục gốc (`01`→`07`, `findex_data.py`, `reviews.py`, `brokers.py`, `recalc.py`) và hai output đã nộp (`doc/FBAR2_2026_DNSE_Analysis.docx`, `FBA_Round2_DNSE_data_pack.xlsx`).

Cách kiểm tra:
- Đọc toàn bộ code.
- Chạy `03 --selftest` và `04_segment_model.py`.
- Render lại 11 chart trong thư mục tạm (không ghi đè `fig/` của project).
- Cộng tay lại các bảng trong `reviews.py` / `brokers.py`.
- Chạy regex và từ khóa trên câu tiếng Việt thực tế.
- Kiểm tra ràng buộc logic của dữ liệu Findex và suy ngược tỷ trọng dân số của từng phân khúc.
- Đọc text và ảnh bên trong file .docx, đọc giá trị trong file .xlsx đã xuất.

Chưa kiểm tra được:
- Chạy lại bước 03 trên dữ liệu thật, vì repo không có file `reviews_raw_*.csv`.
- Chạy `06` (máy chưa cài `docx` npm) và `recalc.py` (thiếu module, xem E4).
- Đối chiếu word count với giới hạn trong booklet (máy không có thư viện đọc PDF).

Mức độ: 🔴 có thể làm sai kết luận · 🟠 số liệu lệch / sai sót nhìn thấy được · 🟡 độ bền và khả năng tái lập của code.

---

## Cập nhật 23/09/2026 (tối): chạy lại pipeline, đối chiếu, và sửa code

Phần này ghi lại lần chạy lại toàn bộ pipeline theo README trên máy local, kết quả đối chiếu với bản đã nộp, và trạng thái sửa của từng mục. Các phần A–G bên dưới là bản audit gốc.

**Sao lưu:** toàn bộ code, `reviews.py`, `brokers.py`, `findex_data.py` và workbook gốc được lưu nguyên trạng trong `_backup_original_2026-09-23/`. File `doc/FBAR2_2026_DNSE_Analysis.docx` (bản đã nộp) không bị động tới; report dựng lại nằm ở thư mục gốc.

### 1. Kết quả chạy lại bằng code gốc

| Bước | Kết quả | So với bản công bố |
|---|---|---|
| 01 Findex API | 19,878 bản ghi, 1 trang (`total` 19,878 < `per_page` 25,000) | **796/796 giá trị trong `findex_data.py` khớp tuyệt đối.** Nhãn API xác nhận ánh xạ hậu tố `.1`–`.12`. E1 chưa xảy ra trong thực tế; E3 không phải lỗi. |
| 02b Google Play | DNSE 867, VPS 2,000 (chạm `TARGET`), FPTS 177 | DNSE thiếu đúng 1 review (1 sao, 2026, referral spam, đã bị xóa khỏi store). **50/50 quote tìm lại được**, số sao giống hệt. |
| 03 làm sạch (quy tắc cũ) | DNSE 127 / 71 / 36 → 633, mean 3.161. VPS (1,200 bản mới nhất tính đến 21/09) 1,116, 2.597 → 2.515. FPTS 169, 2.181 → 2.154 | **Tái lập chính xác** (referral 71 so với 72 là do review đã bị xóa). |
| 03 theme | Thứ hạng giống bản công bố; số lệch vài đơn vị | Đúng như README cảnh báo (bộ từ khóa là bản dựng lại). |
| 03 generic | Code: 212 review generic (2024: 102) | **Công bố: 110 (2024: 54). Xem A6 mới.** |
| 04–07 | Chạy được | Text .docx trùng 736/736 đoạn với bản nộp; workbook trùng 0 dòng khác biệt. |
| recalc | `ModuleNotFoundError: office` | Đúng như E4. |

### 2. Phát hiện mới trong lần chạy lại

- **A6 🔴 Định nghĩa generic trong code/README/report sai so với con số đã công bố.** Thử các định nghĩa khác nhau thì chỉ quy tắc **"1 từ và không có theme"** tái lập được 110 và phân bố theo năm [0, 2, 19, 6, 54, 20, 9] (ra 112, sai lệch 6; phần lệch do bộ từ khóa dựng lại). Quy tắc "≤ 4 từ" mà code và text mô tả cho ra 212. Report §3.3 thực ra đã viết "a single word of praise". **Độ nhạy** (dữ liệu sau khi sửa):

  | Quy tắc | Generic 2024 / 2025 | Mean substantive 2024 → 2025 |
  |---|---|---|
  | 1 từ | 33.7% / 12.0% | 4.15 → 2.38 |
  | 2 từ | 50.3% / 17.7% | 4.00 → 2.22 |
  | 4 từ | 62.7% / 25.9% | 3.74 → 2.01 |

  Kết luận "đỉnh 2024 là ảo" đứng vững với mọi định nghĩa.
- **A1, tác động thật trên dữ liệu:**
  - DNSE: 3 trên 71 review referral là bắt nhầm ("đăng **nhập mậ**t khẩu", "thằng bạn đưa mã giới thiệu… chả được ngàn nào").
  - VPS: **9/12** bắt nhầm (phàn nàn OTP, "mà mỗi lần cập nhật").
  - FPTS: **5/5** bắt nhầm.

  Lỗi này sai lệch không đều giữa các app, nên làm lệch phần so sánh 3 app.
- **A2:** không có review nào trong dữ liệu thật bị `.com` bắt nhầm. Đây là rủi ro tiềm ẩn, không ảnh hưởng số đã công bố.
- **A4, xác nhận:** cả 36 review DNSE bị loại vì trùng lặp đều do **36 tác giả khác nhau** viết ("good" ×10, "tuyệt vời" ×8, "rất tốt" ×4…), trong đó 28/36 là 5 sao. Không có nhóm trùng nào dài từ 20 ký tự trở lên.
- **A3, thêm `\b` là chưa đủ:** sau khi bỏ dấu, "lỗi", "lời", "lợi" đều thành từ đơn `loi`, nên "tiện lợi", "sinh lời", "trả lời", "lời khuyên" vẫn bị gắn stability. Cần so khớp có dấu hoặc dùng cụm từ.
- **VPS không bị "capped at 1,200 by pagination".** Google trả hơn 2,000 review. Con số 1,200 là do lần kéo gốc dừng ở đó, không phải giới hạn của store. Report và workbook đã sửa lại mô tả.
- **Report §6 còn sót số theme cũ** ("The 16.2 per cent of negative reviews…").
- **Report ghi "Findex 2024 microdata"** trong khi thực tế dùng dữ liệu tổng hợp theo phân khúc qua API. Đã sửa thành "segment data".
- **Workbook, sheet Segment model:** ghi chú nói "Poorest 40%" có propensity thấp nhất, nhưng thấp nhất thực ra là "Primary educ or less" (15.6 / 26.5).
- **C7, số mã FTSE:** danh sách tháng 11/2025 có 27 mã, FAQ ghi 28, danh sách chỉ dẫn tháng 4/2026 có **32**. Danh sách chính thức (21/08/2026) chưa kiểm tra được. Report nay ghi "32 on the April 2026 indicative list" và `brokers.py` đánh dấu là chưa xác minh.
- **Tương quan thứ hạng A–B (Spearman):** 0.97 trên 11 phân khúc, 0.78 khi tính cả nhóm 15–24 tuổi. Nhận định này thay cho kết luận "below the diagonal" (B2).

### 3. Số liệu trước và sau khi sửa

| Chỉ tiêu | Bản nộp | Sau khi sửa |
|---|---|---|
| DNSE: kéo về → giữ lại | 868 → 633 (loại 27.1%) | **867 → 672** (loại 22.5%: 127 loan, 68 referral, 0 trùng) |
| DNSE: mean trước / sau / phần bị loại | 3.287 / 3.161 / 3.626 | 3.290 / **3.220** / 3.528 |
| VPS (1,200) / FPTS: giữ lại, mean | 1,116, 2.515 / 169, 2.154 | **1,171, 2.582 / 177, 2.181** |
| Spam 2022 / 2023 | 48.8% / 55.8% | 45.4% / 53.9% |
| Generic 2024 / 2025 | 30.9% / 13.2% | 33.7% / 12.0% |
| Mean substantive 2024 → 2025 | 4.07 → 2.36 | **4.15 → 2.38** |
| Review tiêu cực | 271 | 278 |
| Stability / onboarding / fraud / promo | 25.8 / 19.6 / 16.2 / 9.6% | **27.3 / 21.2 / 17.6 / 8.6%** (thứ hạng giữ nguyên) |
| Mean 2026: DNSE / VPS / FPTS | 3.06 / 2.07 / 3.26 | 3.06 / 2.07 / 3.33 (FPTS n=24) |
| Xếp hạng ưu tiên | 1 In labour force (17.5m), 2 Richest, 3 Secondary | **1 Secondary+ (20.4m), 2 In labour force (19.0m), 3 Richest (15.3m)**; nhóm giao nhau không đổi |
| Tỷ trọng dân số: tiểu học trở xuống / nông thôn / ngoài lực lượng lao động | 23.6 / 62.0 / 26.5% | 11.2 / 67.0 / 20.1% (suy ngược từ dữ liệu) |
| Số từ phần thân report | 3,486 | 3,575 |

### 4. Trạng thái từng mục

| ID | Trạng thái | Đã làm |
|---|---|---|
| A1 | ✅ | Referral chỉ tính khi cụm từ đứng cạnh mã/số tiền. Có mã chữ hoa (BBQK), chữ số cách nhau ("9 7 1 8 1 6"), mã dính liền ("529004mã"). Đọc lại từng review thay đổi trạng thái: tất cả đều đúng. |
| A2 | ✅ | Bỏ `\.com\b`, giữ `c0m`. |
| A3 | ✅ | So khớp theo ranh giới từ; các âm tiết dễ nhầm được so trên text có dấu (`ACCENTED`) hoặc trong cụm từ. Đọc mẫu 48 review tiêu cực đã gắn tag: đều đúng. |
| A4 | ✅ | Chỉ tính trùng khi text ≥ 20 ký tự hoặc cùng tác giả; giữ bản cũ nhất. |
| A5 | ✅ | `utf-8-sig`, báo lỗi khi file rỗng hoặc thiếu cột, xóa cả `\r`. |
| A6 | ✅ | `GENERIC_MAX_WORDS = 1` (khớp số đã công bố); bảng độ nhạy đưa vào `reviews.py`, workbook và caption Figure 4. |
| — | ✅ | Self-test mở rộng từ 11 lên 26 case, gồm các negative test. |
| — | ✅ | **`03b_reviews_tables.py` mới:** sinh `reviews.py` và `reviews_tables.json` từ CSV thô; `reviews.py` không còn gõ tay. |
| B1 | ✅ | `implied_share()` suy ngược tỷ trọng từ dữ liệu (cặp thu nhập ra đúng 40.0). |
| B2 | ✅ | Bỏ đường chéo; §4.2, caption Figure 10, Conclusion và §2.3 viết lại dựa trên tương quan thứ hạng. |
| B3 | ✅ | Điểm và hạng tính trên giá trị chưa làm tròn; JSON có thêm `gap_to_next_pct`. |
| B4 | ⚠️ Giữ nguyên thiết kế | Ghi rõ giới hạn trong docstring và README; không đổi công thức vì đó là lựa chọn phương pháp của team. |
| B6 | ❌ Chưa kiểm tra | Định nghĩa `fin17a` trong Findex 2025 (bước nhảy 19.9 → 43.1%). |
| C1–C6, C8, C9 | ✅ | Bảng A4 và Table 2/3/A3/A5 dựng từ JSON; biên Q2 = 21.8; `HOSE_TOP10_Q2 = 65.19`; tổng LNTT ngành link sang sheet (8,418.9); doanh thu 453.1/848.2; sửa câu "lower still" và "same period". |
| C7 | ⚠️ | Ghi 32 mã (danh sách tháng 4/2026), đánh dấu chưa xác minh danh sách chính thức. |
| — | ✅ | **Thêm:** mọi con số review/phân khúc trong phần văn bản của `06` đọc từ JSON; `06` dừng với lỗi nếu top 3 phân khúc thay đổi. |
| D1 | ✅ | `Fig()` đọc kích thước PNG; độ méo trong docx mới < 0.3%. |
| D2 | ✅ | Trục x theo quý; thêm Q4/2024 = 9.98% (HNX qua Vietstock); ghi chú "not published" ở chỗ trống. |
| D3 | ✅ | Xóa Fig 2 cũ trong `05a`. |
| D4–D6 | ✅ | Diện tích bong bóng tỷ lệ với pool, vẽ nhỏ đè lên lớn, top 3 lấy từ model; nhãn n chuyển vào tick label; thanh HOSE vẽ rỗng có gạch chéo. |
| D7 | ✅ | Lọc năm theo n ≥ 10; caption Figure 1 đổi thành "last of these six firms by earnings". |
| E1 | ✅ | Lặp qua mọi trang và kiểm tra `total`. |
| E2 | ✅ | `01` tự đối chiếu `findex_data.py` (796 giá trị); docstring nói rõ file này là tập con do người chọn. |
| E3 | ✅ | Nhãn indicator lấy từ series gốc. |
| E4 | ✅ | `recalc.py` có phương án dự phòng khi thiếu module `office.soffice` và tự tìm LibreOffice ở thư mục cài đặt mặc định. **Máy này chưa cài LibreOffice**, nên chưa tính lại được công thức; đã kiểm tra tay các ô tham chiếu chính. |
| E5, E6 | ✅ | Ngày theo UTC+7; cắt kết quả về đúng `target`; xóa `\r`. |
| E7 | ✅ | README viết lại (đường dẫn, thứ tự chạy thêm 3b, phần "exact vs reconstruction"); `.gitignore` thêm `node_modules/`. |
| E8 | ❌ | Chưa đối chiếu được giới hạn số từ trong booklet (máy không có công cụ đọc PDF). Phần thân hiện có 3,575 từ. |
| F (lợi suất cho vay) | ✅ | Dùng trung bình 3 số dư (6,015 tỷ, 11.2%); ghi chú rằng tử số gồm cả lãi phải thu. |

### 4b. Rà soát lần 2 (sau khi sửa)

| ID | Mức | Vấn đề | Trạng thái |
|---|---|---|---|
| R1 | 🔴 | **Lỗi do chính lần sửa trước gây ra:** regex referral mới coi số tiền 6 chữ số là mã ("nạp 500000 mà…", "chuyển 200000 rồi nhập mã OTP"). Dữ liệu hiện tại chưa có câu nào như vậy. | ✅ Loại số dạng tiền (đuôi 000); không mã referral thật nào trong dữ liệu có đuôi này. Thêm 2 test (28/28 pass); số trên dữ liệu thật không đổi. |
| R2 | 🟠 | **Lỗi do chính lần sửa trước gây ra:** Figure 5 hiện nhãn thô "ui", vì với dữ liệu mới theme này có 7 review tiêu cực và lọt vào chart. | ✅ Bổ sung nhãn; `05b` báo lỗi nếu gặp theme chưa có nhãn. |
| R3 | 🟡 | `02b` ghi ngày theo giờ của máy đang chạy (thư viện dùng `datetime.fromtimestamp`). Máy này ở UTC+7 nên đúng, nhưng máy ở múi giờ khác sẽ lệch ngày. | ✅ Cố định theo UTC+7. |
| R4 | 🟡 | File audit `reviews_flagged_vn.com.vpbs.smartone.csv` có 2,000 dòng, trong khi bảng công bố dùng lát 1,200. | ✅ `03b` ghi file flagged cho đúng những dòng đã dùng. |
| R5 | 🟠 | Exec summary: "Most of those [review cáo buộc lừa đảo] cite a sign-up bonus… or an account closure fee". Đọc tay 49 review: chỉ khoảng 17 (≈35%) nêu nguyên nhân (thưởng đăng ký, nạp 2 triệu, đóng tài khoản); còn lại là câu chửi một dòng. Câu này có từ bản gốc. | ✅ Viết lại: "Around a third of those name a cause…; the rest are one-line accusations." |

### 4c. Bổ sung dữ liệu App Store (24/09/2026)

- **`02c_appstore_scrape.py` mới:** lấy review có viết nội dung của 3 app trên App Store Việt Nam qua RSS công khai của Apple, cộng số lượt chấm sao từ API lookup. Feed này chập chờn (cùng một trang lúc có dữ liệu, lúc rỗng), nên script thử lại mỗi trang, lấy cả 2 kiểu sắp xếp và gộp dồn qua các lần chạy. Hai lần chạy thu được DNSE 332, VPS 518, FPTS 205 review.
- **Quy tắc referral viết lại thành hàm `is_referral()`.** Spam trên App Store dùng mã chữ-số (MFBCFA, G25PRK) và cách viết lỏng ("Mã gth", "Mã nhận thưởng", "418422. nhạn 10k"), khiến bản trước lọt khoảng 15 review spam. Bản mới nhận thêm các dạng mã này nhưng loại trừ mã VN30, mã chỉ số/ETF, mã chứng quyền, số tiền tròn và số lặp (888888).
  - Self-test tăng lên 37 case.
  - Trên 6 bộ dữ liệu: không review nào từng bị bắt nay lọt lưới. Bắt thêm 2 spam trên Google Play DNSE (nên DNSE giữ lại 670, mean 3.218), cùng 10 spam App Store DNSE và 3 spam App Store VPS. Tôi đã đọc từng review thay đổi.
- **So sánh 2025–2026 (Appendix A6, Figure A1):**
  - Review trên App Store khắt khe hơn: DNSE 2.25 so với 2.77, VPS 1.47 so với 2.10, FPTS 2.31 so với 2.18. Trên App Store, DNSE đứng sau FPTS.
  - Phàn nàn tiêu cực của DNSE: sản phẩm (stability hoặc onboarding) chiếm **50.9%** trên App Store so với 37.6% trên Google Play; khuyến mãi / lừa đảo (fraud hoặc promo) chiếm **15.1%** so với 34.4%. Cỡ mẫu App Store nhỏ (53 review tiêu cực).
  - DNSE có 1,490 lượt chấm sao, trung bình 4.04, nhưng review viết chỉ 2.94 sao. Đây là bằng chứng cho phần Limitations.
- **Giới hạn của dữ liệu App Store:** không có lịch sử đầy đủ; số lượt chấm sao của FPTS từ API lookup (76) nhỏ hơn số review viết (205), nên có lẽ chỉ tính phiên bản hiện tại.

### 5. Việc còn lại cho team

1. Đọc lại các đoạn report đã được viết lại: Exec summary, §2.2, §3.3, §4.2, §4.3, §4.4, Conclusion, Appendix B2–B4. Bản dựng lại nằm ở `FBAR2_2026_DNSE_Analysis.docx` trong thư mục gốc.
2. Kiểm tra giới hạn số từ trong booklet (E8) và xác nhận số mã FTSE chính thức (C7).
3. Cài LibreOffice rồi chạy `python recalc.py FBA_Round2_DNSE_data_pack.xlsx` để lưu giá trị công thức vào workbook.
4. (Tùy chọn) Kiểm tra định nghĩa `fin17a` trong Findex 2025 (B6).

---

## Tóm tắt

| ID | Mức | Vấn đề | File |
|---|---|---|---|
| A1 | 🔴 | Regex referral spam bắt nhầm review thật ("mà mọi người", "nhập mã OTP") | `03` |
| A2 | 🔴 | `\.com\b` gắn nhãn loan spam cho mọi review có URL | `03` |
| A3 | 🔴 | Từ khóa chủ đề so khớp substring nên bắt nhầm hàng loạt (`loi`, `lua`, `cham`, `thuong`…) | `03` |
| A4 | 🔴 | Rule loại trùng lặp xóa cả review ngắn thật của nhiều người khác nhau | `03` |
| A6 | 🔴 | Cờ generic: code/README/report ghi "≤ 4 từ", nhưng số đã công bố tính theo "1 từ" (phát hiện khi chạy lại) | `03`, `06`, `07` |
| B1 | 🔴 | **Tỷ trọng dân số của phân khúc sai so với trọng số Findex, khiến xếp hạng ưu tiên đổi** | `04` |
| B2 | 🔴 | Đường chéo A=B ở Figure 10 không có ý nghĩa, dẫn tới kết luận "below the diagonal everywhere" không đứng vững | `04`, `05b`, `06` |
| B3 | 🟠 | Thứ hạng 2 và 3 (Richest 60% và Secondary+) đảo nhau tùy cách làm tròn | `04` |
| B4 | 🟠 | Điểm ưu tiên = composite × pool về cơ bản là xếp hạng theo quy mô dân số; fin17a bị tính hai lần | `04` |
| C1–C9 | 🟠 | 9 con số lệch giữa report, workbook và code (xem bảng C) | `06`, `07`, `brokers.py` |
| D1 | 🟠 | Ảnh trong Word bị kéo méo 10–19% | `06` |
| D2–D7 | 🟡 | Trục thời gian Figure 2, code chart cũ bị ghi đè, chart đè chữ… | `05a`, `05b` |
| E1–E8 | 🟡 | Tái lập được hay không: API không phân trang, `findex_data.py` dựng tay, `recalc.py` thiếu module, BOM… | `01`, `02a/b`, `03`, `recalc.py` |

---

## A. Làm sạch review (`03_reviews_clean.py`)

### A1 🔴 Regex referral spam bắt nhầm review thật
[03_reviews_clean.py:56-58](../03_reviews_clean.py#L56-L58). Kết quả chạy thử:

| Câu | Kết quả | Pattern gây lỗi |
|---|---|---|
| "App tốt **mà mọi** người chê quá" | referral_spam | `ma\s*moi` |
| "**Nhập mã** OTP mãi không được" | referral_spam | `nhap\s*ma` |
| "nhap ma xac thuc bi loi" | referral_spam | `nhap\s*ma` |
| "nạp 2000000 **mà** không vào" | referral_spam | `\d{6}\s*ma` |
| "Mã mới gửi về chậm" | referral_spam | `ma\s*moi` |

"mà mọi người" là cụm từ rất phổ biến, còn "nhập mã OTP" chính là loại phàn nàn onboarding. Phần lớn các review này là 1 sao, nên việc loại nhầm làm lệch cả số **72 referral spam**, **mean sau làm sạch 3.161** lẫn **tỷ lệ theme trong review tiêu cực**.

**Sửa:**
- Thêm `\b` ở hai đầu.
- Bỏ `moi` khỏi nhóm `ma\s*(...)`.
- Chỉ bắt `nhap ma` khi phía sau là số (`nhap\s*ma\s*:?\s*\d{4,}`) hoặc là "gioi thieu".
- Bỏ nhánh `\d{6}\s*ma`.
- Thêm các case trên vào `SELFTEST` làm negative test.

### A2 🔴 `\.com\b` gắn nhãn loan spam cho mọi URL
[03_reviews_clean.py:54](../03_reviews_clean.py#L54). Ví dụ "Xem thêm tại dnse.com.vn" bị gắn loan_spam. **Sửa:** thay bằng danh sách domain cho vay cụ thể, hoặc chỉ bắt khi có kèm từ "vay".

### A3 🔴 Từ khóa chủ đề so khớp substring trên chữ đã bỏ dấu
[03_reviews_clean.py:77-105](../03_reviews_clean.py#L77-L105). `k in n` không xét ranh giới từ, trong khi chữ đã bỏ dấu thì trùng nghĩa rất nhiều:

| Câu | Theme bị gắn | Từ khóa gây lỗi |
|---|---|---|
| "Sinh lời tự động tốt" | stability + yield | `loi` (lời ≠ lỗi) |
| "lựa chọn tuyệt vời" | fraud | `lua` (lựa ≠ lừa) |
| "chăm sóc khách hàng nhiệt tình" | stability | `cham` |
| "sắp có tính năng mới" | stability | `sap` |
| "thường xuyên dùng", "app bình thường" | promo | `thuong` |
| "dùng tiền dễ" | money | `ung tien` |

Ngay case t6 trong self-test cũng bị gắn stability, nhưng self-test chỉ kiểm tra "yield có mặt" nên vẫn pass. Với code hiện tại, **19/50 quote** trong `reviews.py` có tag khác bản đã công bố. Bản công bố cũng có tag vô lý:
- `fa30782f` được gắn yield dù không nhắc gì đến tính năng này.
- `31147446` được gắn zalopay dù không có chữ "zalo".
- `a018878c` được gắn money|promo|influencer khi chỉ nói về khuyến nghị đầu tư.

Hệ quả: Figure 5 (stability 25.8%, fraud 16.2%) đang dựa trên một bộ tag có nhiễu.

**Sửa:**
- So khớp theo từ bằng `re.search(r"\b" + k + r"\b", n)`.
- Bỏ các từ khóa đơn âm tiết dễ trùng (`loi`, `lua`, `cham`, `sap`, `thuong`), thay bằng cụm cụ thể hơn ("bi loi", "loi dang nhap", "lua dao", "cham qua", "sap app"…).
- Đọc tay khoảng 50 review để đo tỷ lệ bắt đúng, rồi ghi con số đó vào Appendix B.

### A4 🔴 Rule loại trùng lặp xóa cả review ngắn thật
[03_reviews_clean.py:125-131](../03_reviews_clean.py#L125-L131). Ngưỡng `len(key) >= 4` quá thấp: "rất tốt" (thành `ratot`) hay "app hay" của nhiều người khác nhau đều bị coi là trùng. Rule này chủ yếu loại review 5 sao ngắn, tức là tác động trực tiếp lên mean và lên chỉ số "generic". Ngoài ra, vì dữ liệu kéo theo thứ tự mới nhất trước, "later copies" thực chất là bản **cũ hơn** (ngược với mô tả trong README), nên review bị dồn sang năm muộn hơn.

**Sửa:** chỉ loại trùng khi cùng text **và** (cùng author hoặc text dài ≥ 30 ký tự). Nên sort theo ngày tăng dần trước khi loại trùng.

### A5 🟡 Các lỗi nhỏ trong `03`
- [03_reviews_clean.py:276](../03_reviews_clean.py#L276) mở file bằng `encoding="utf-8"`. CSV copy từ trình duyệt hoặc lưu lại qua Excel thường có BOM, khi đó header thành `\ufeffreview_id` và `review_id` rỗng mà **không báo lỗi**. Nên dùng `utf-8-sig`.
- [03_reviews_clean.py:283](../03_reviews_clean.py#L283) `rows[0]` gây IndexError nếu CSV rỗng.
- [03_reviews_clean.py:116](../03_reviews_clean.py#L116) cờ `is_generic` không xét số sao, nên "app tệ" (2 từ, 1 sao) cũng bị tính là generic. README và report lại mô tả generic là "one-word praise". Chỉ cần nói rõ định nghĩa hoặc giới hạn cho review ≥4 sao.

---

## B. Mô hình phân khúc (`04_segment_model.py`, `findex_data.py`)

### B1 🔴 Tỷ trọng dân số của phân khúc sai so với trọng số Findex (phát hiện mới)
[04_segment_model.py:59-66](../04_segment_model.py#L59-L66). Mỗi cặp phân khúc bù nhau chia hết dân số, nên với mọi indicator: `All = w·A + (1−w)·B`, từ đó suy ra được `w`. Lấy trung vị trên các indicator có chênh lệch >5 điểm:

| Phân khúc | `POP_SHARE` trong code | Suy ngược từ Findex |
|---|---|---|
| Women | 50.9 | 51.2 |
| Young (15-24) | 17.1 | 18.2 |
| **Primary educ or less** | **23.6** | **11.2** |
| Poorest 40% | 40.0 | **40.0** (khớp chính xác, chứng tỏ phương pháp đúng) |
| **Rural** | **62.0** | **67.0** |
| **Out of labour force** | **26.5** | **20.1** |

Docstring nói số liệu lấy từ "Findex microdata weights as reported in the published country tables", nhưng số của nhóm học vấn lệch gấp đôi. Vì chỉ số A và B được tính từ Findex, tỷ trọng cũng phải là của Findex thì mới nhất quán.

Khi dùng tỷ trọng suy ngược, **xếp hạng ưu tiên đổi**:

| Hạng | Hiện tại (code) | Tỷ trọng Findex |
|---|---|---|
| 1 | In labour force (17.5m) | **Secondary educ or more (20.4m)** |
| 2 | Richest 60% | In labour force (19.0m) |
| 3 | Secondary educ or more | Richest 60% (15.3m) |

Kết luận "priority segment = giao của ba nhóm" vẫn giữ được, nhưng **Table 3, Table A3, Exec summary ("between 15 and 17.5 million") và §4.2 ("places adults in the labour force first, at 17.5 million") đều cần sửa số**.

**Sửa:** thay `POP_SHARE` bằng giá trị suy ngược, hoặc lấy trực tiếp từ microdata (catalog 7998, trường `wgt`), rồi ghi nguồn chính xác.

### B2 🔴 Đường chéo A = B ở Figure 10 không có ý nghĩa
Chỉ số A và B dùng các indicator khác nhau, nên mức tuyệt đối của chúng không so được với nhau. B cao chủ yếu vì `con26d` (~84%) và `con9a` (~85%) gần như ai cũng đạt. Câu "Every segment lies below the diagonal, so digital readiness exceeds investable surplus everywhere" ([06_build_report.js:316-317](../06_build_report.js#L316-L317)) và câu tương ứng trong Conclusion ([06_build_report.js:392](../06_build_report.js#L392)) chỉ phản ánh cách chọn indicator.

**Sửa:** bỏ đường chéo ([05b_charts_evidence.py:161-163](../05b_charts_evidence.py#L161-L163)) và bỏ câu kết luận đó. Nếu muốn giữ ý này thì phải chuẩn hóa (z-score hoặc thứ hạng) từng chỉ số trước khi so.

### B3 🟠 Hạng 2 và 3 đảo nhau tùy cách làm tròn
[04_segment_model.py:84-92](../04_segment_model.py#L84-L92) làm tròn composite và pool về 2 chữ số trước khi nhân:

| Cách tính | Richest 60% | Secondary+ |
|---|---|---|
| Hai thừa số đã làm tròn (code) | 904.45 | 904.18 |
| Pool không làm tròn | 904.4 | 904.5 |

Report đã nói "within 0.2 per cent… treated as equal", như vậy là tốt. Nhưng Table 3 vẫn ghi cứng hạng 2 và 3; nên ghi "2=".

### B4 🟠 Thiết kế điểm ưu tiên
- `composite × pool` bị quy mô dân số chi phối. Trong mỗi cặp bù nhau, nửa lớn hơn gần như luôn thắng, ví dụ Rural xếp hạng 5 trên Urban hạng 8 dù composite thấp hơn.
- `fin17a` vừa nằm trong chỉ số A (cộng điểm) vừa bị trừ trong activation gap (`acct − fin17a`), nên cùng một biến vừa làm tăng vừa làm giảm điểm.
- Chỉ số A có `fin24bd` (đủ sống 2 tháng không cần thu nhập), không phải "held formally" như tên gọi. Chỉ số B có `fin32.acc` (nhận lương qua tài khoản), không hẳn là "digital habit".

Nên nêu các điểm này trong Appendix B3 (Limitations) nếu không sửa.

### B5 ✅ Dữ liệu Findex tự nhất quán
Đã kiểm tra 22 ràng buộc tập con (ví dụ `fin17a ≤ save.any`, `dig.acc ≤ account`, `fin32.acc ≤ fin32`, `con26d ≤ internet`) trên cả 13 phân khúc: không có vi phạm nào. "All adults" luôn nằm giữa hai phân khúc bù nhau. Giá trị 2024 trong `TRENDS` khớp với `SEG2024`. Không có id trùng lặp.

### B6 🟠 Cần kiểm tra định nghĩa `fin17a` trước khi dùng như một xu hướng
Chỉ số tiết kiệm tại tổ chức tài chính tăng từ 19.9% (2022) lên 43.1% (2024), tức +23 điểm trong 2 năm (Figure 11, §4.3). Nên kiểm tra tài liệu Findex 2025 xem câu hỏi có bị đổi không trước khi viết "households are accumulating".

---

## C. Số liệu lệch giữa report, workbook và code

Tất cả các lỗi dưới đây **đã được xác nhận có trong file .docx / .xlsx đã xuất**.

| ID | Vị trí | Đang ghi | Đúng là | Ghi chú |
|---|---|---|---|---|
| C1 | [06_build_report.js:455](../06_build_report.js#L455) Table A4, dòng Total, cột "Mean, substantive" | **3.05** | **2.855** | Σ(n×mean)/523 từ YEAR_TAB. Mean của nhóm generic là 4.62. |
| C2 | [06_build_report.js:291](../06_build_report.js#L291) caption Figure 6 | "DNSE leads … and in 2026" | FPTS 3.26 > DNSE 3.06 năm 2026 | Chính chart cho thấy điều này. FPTS chỉ có n=23, nên viết lại cho đúng kèm cảnh báo cỡ mẫu. |
| C3 | [06_build_report.js:410](../06_build_report.js#L410) Table A1, biên lợi nhuận Q2 | 21.7 | **21.8** | 98.9/453.1. Chart và workbook đều ra 21.8. |
| C4 | [brokers.py:37](../brokers.py#L37) `HOSE_TOP10_Q2` | 64.19 | **65.19** | Tổng 10 dòng ra 65.19. Workbook đang hard-code 65.19 ([07_build_workbook.py:674](../07_build_workbook.py#L674)) để tránh lỗi này. |
| C5 | [07_build_workbook.py:763](../07_build_workbook.py#L763) tổng LNTT ngành | 9,977 | **8,418.9** | Ghi chú nói "Sum of the firms on the Industry cross-section sheet" nhưng con số không khớp. Nên thay bằng công thức link sang sheet đó. |
| C6 | [07_build_workbook.py:375-376](../07_build_workbook.py#L375-L376) sheet Vietnam reference | Doanh thu Q2 455.2 / H1 852.6 | 453.1 / 848.2 | Lệch với sheet DNSE financials trong cùng file. |
| C7 | [07_build_workbook.py:380](../07_build_workbook.py#L380) và [06_build_report.js:338](../06_build_report.js#L338) | Workbook: 28 mã FTSE; report và `brokers.py`: 27 | — | Cần tra nguồn LSEG để chọn một số. |
| C8 | [06_build_report.js:280](../06_build_report.js#L280) | "The equivalent figure on HOSE is lower still" | Không chứng minh được | Từ <2.94/12.27 chỉ suy ra được <0.240, có thể lớn hơn 0.235 (HNX). |
| C9 | [06_build_report.js:334](../06_build_report.js#L334) | "fell from 21.7% in 2017 to 7.7% over the same period" | Giai đoạn là 2017→2024 | Câu trước nói về 2022→2024. |

Liên quan tới B1: các số pool trong [06_build_report.js:177](../06_build_report.js#L177), [06_build_report.js:317](../06_build_report.js#L317), Table 3 ([06_build_report.js:319-330](../06_build_report.js#L319-L330)) và `SEGROWS` ([06_build_report.js:136-150](../06_build_report.js#L136-L150)) sẽ đổi.

Nguyên nhân gốc của C1–C7 là số liệu bị hard-code ở nhiều nơi thay vì import từ một nguồn:
- `SEGROWS` và Table 3 trong `06` (comment còn trỏ tới `/home/claude/segment_model.py`, một đường dẫn cũ).
- Chuỗi thị phần phái sinh trong `05a`.
- `neg_total = 271` ([07_build_workbook.py:930](../07_build_workbook.py#L930)), mean tổng 3.161 ([07_build_workbook.py:901](../07_build_workbook.py#L901)), 65.19 và bảng CLEAN/MEANS trong `07`.

Nên để `06` đọc một file JSON do `04`/`reviews.py` xuất ra, và để `07` dùng công thức hoặc hằng số import từ module.

---

## D. Chart

### D1 🟠 Ảnh trong Word bị kéo méo
[06_build_report.js:105-115](../06_build_report.js#L105-L115) hard-code chiều rộng và chiều cao, trong khi `bbox_inches="tight"` làm tỷ lệ PNG thay đổi. Ảnh bên trong .docx có đúng kích thước pixel như bản render lại, nên méo xảy ra trên chính file đã nộp:

| Chart | Tỷ lệ PNG | Tỷ lệ trong docx | Méo |
|---|---|---|---|
| fig4_revenue_mix | 3.78 | 4.50 | **+19%** |
| fig5_plan_progress | 2.59 | 3.04 | **+17%** |
| fig3_revenue_margin | 2.03 | 2.33 | **+15%** |
| fig2_monetisation_gap | 2.36 | 2.06 | **−13%** |
| fig1_derivatives_share | 2.05 | 2.26 | +10% |
| fig7_review_rating_by_year | 2.04 | 2.18 | +7% |
| fig10 / fig6 | — | — | +5% / +4% |

**Sửa:** trong `Fig()`, đọc width và height từ PNG header (byte 16–23) và tính `heightPx = widthPx * H / W`.

### D2 🟠 Figure 2 (thị phần phái sinh): trục x cách đều
[05a_charts_financial.py:49-67](../05a_charts_financial.py#L49-L67). Khoảng Q1/2024→Q1/2025 (4 quý) được vẽ như 1 bước. Research đã tìm được số còn thiếu: **Q4/2024 = 9.98%** (HNX, qua Vietstock/Fili), cả năm 2024 là 6.14%, cả năm 2025 là 21.47%. Nên thêm điểm Q4/2024, đặt trục x theo thời gian thật, và sửa caption "interpolated". Nên lấy dữ liệu từ `BR.DNSE_DERIV_SERIES` thay vì hard-code.

### D3 🟡 Code Fig 2 cũ bị ghi đè
[05a_charts_financial.py:69-95](../05a_charts_financial.py#L69-L95) vẫn vẽ `fig2_monetisation_gap` với số cũ (18.00 / 13.00 / 1.42), sau đó `05b` ghi đè. Nếu chạy `05b` trước `05a`, report sẽ dùng bản sai. **Xóa đoạn này.**

### D4 🟡 Figure 10 (segment model)
[05b_charts_evidence.py:140-170](../05b_charts_evidence.py#L140-L170):
- Bong bóng Women bị Older che, Urban bị In labour force che một phần.
- Chữ "equal readiness and surplus" đè lên đường chéo (và đường chéo nên bỏ, xem B2).
- `s = 20 + pool*26` có hằng số +20, nên diện tích không tỷ lệ với pool như ghi chú trên chart. Dùng `s = pool * k`.

### D5 🟡 Figure 6 (peer ratings)
[05b_charts_evidence.py:130-131](../05b_charts_evidence.py#L130-L131): dòng "n=… cleaned of …" ở `y=-0.42` đè lên nhãn trục x. Nên đưa n vào nhãn tick (`"DNSE Entrade X\nn=633 of 868"`).

### D6 🟡 Figure 3: thanh HOSE là giới hạn trên nhưng vẽ như giá trị thật
[05b_charts_evidence.py:45-52](../05b_charts_evidence.py#L45-L52): thanh "below 2.94%" dài hơn thanh HNX 2.88% nên dễ bị đọc nhầm. Nên vẽ bằng marker "<" hoặc thanh gạch chéo không tô.

### D7 🟡 Các lỗi nhỏ khác
- [05b_charts_evidence.py:64-66](../05b_charts_evidence.py#L64-L66) bỏ năm 2020 bằng vị trí (`[1:]`). Nên lọc theo giá trị `r[0] != "2020"` hoặc `n >= 10`.
- Figure 11 caption ([06_build_report.js:220](../06_build_report.js#L220)) viết "well outside the top ten by earnings", nhưng chart chỉ có 6 công ty nên không đủ căn cứ cho câu này.

---

## E. Pipeline và khả năng tái lập

| ID | Vấn đề | Vị trí | Sửa |
|---|---|---|---|
| E1 | API World Bank chỉ lấy trang đầu (`per_page=25000`), không kiểm tra `pages`/`total`. Nếu có nhiều bản ghi hơn sẽ bị cắt mà không báo lỗi. | [01_findex_fetch.py:31-32](../01_findex_fetch.py#L31-L32) | Lặp theo `page` đến khi hết `pages`, hoặc `assert total == len(data)`. |
| E2 | `01` **không ghi ra `findex_data.py`** như docstring mô tả; file đó được dựng tay (label và theme tự đặt). Điều này mâu thuẫn với câu "Nothing is transcribed by hand". | [01_findex_fetch.py:81-104](../01_findex_fetch.py#L81-L104) | Sinh `findex_data.py` từ `table`, hoặc sửa docstring và README cho đúng. |
| E3 | `split_segment` không xử lý hậu tố `.s` mà docstring có nhắc; `labels.setdefault` có thể lấy nhãn của một phân khúc làm nhãn gốc. | [01_findex_fetch.py:73-78](../01_findex_fetch.py#L73-L78) | Test với vài id thật. |
| E4 | `recalc.py` import `office.soffice`, module này không có trong repo, nên bước cuối trong README chắc chắn lỗi ImportError. | [recalc.py:19](../recalc.py#L19) | Copy module đó vào repo hoặc bỏ bước này. |
| E5 | 02a dùng `toISOString()` (giờ UTC), nên review đăng lúc 0–7h giờ VN bị lùi sang ngày trước (có thể lệch năm vào ngày 1/1). | [02a_playstore_scrape_browser.js:100](../02a_playstore_scrape_browser.js#L100) | Cộng 7h trước khi cắt ngày. |
| E6 | 02a không cắt kết quả về đúng `target` (có thể dư tới 149 dòng). 02b chỉ xóa `\n`, không xóa `\r`. | [02a:84](../02a_playstore_scrape_browser.js#L84), [02b:71](../02b_playstore_scrape_python.py#L71) | `out.slice(0, target)`; dùng `re.sub(r"[\r\n]+", " ", …)`. |
| E7 | README trỏ tới `data/reviews.py` và `data/brokers.py`, nhưng các file nằm ở thư mục gốc. README ghi "Python 3.9+" còn `pyproject.toml` yêu cầu ≥3.14. `requirements.txt` thiếu Pillow (không bắt buộc) và `node`/`docx`. | README, pyproject | Đồng bộ lại. |
| E8 | Bộ đếm từ trong `06` không tính bảng và caption. Chưa đối chiếu được với luật đếm từ trong booklet. | [06_build_report.js:11-14](../06_build_report.js#L11-L14) | Kiểm tra luật trong booklet rồi ghi rõ cách đếm. |

---

## F. Ghi chú phương pháp (không phải bug, nhưng giám khảo có thể hỏi)

- **So sánh 3 app không cùng khung thời gian (Figure 6):** DNSE có dữ liệu 2020–2026, VPS bị giới hạn 1,200 review gần nhất, FPTS chỉ có 2025–2026. Nên so theo năm (2025: DNSE 2.63 > VPS 2.08 > FPTS 1.98).
- **Lợi suất cho vay ~11% ([07_build_workbook.py:595-598](../07_build_workbook.py#L595-L598)):** đang lấy trung bình dư nợ cuối Q1 và cuối Q2. Số dư bình quân H1 phải gồm cả số cuối 2025 (5,832). Tử số là "interest on lending **and receivables**", rộng hơn lãi margin.
- **Tỷ số "trading share / account share" (0.235):** tử số là thị phần trên HNX, mẫu số là toàn bộ tài khoản trên thị trường. Đây là giả định ngầm và nên ghi rõ.
- **Doanh thu môi giới 404 tỷ (2025) dù miễn phí giao dịch:** cần xem thuyết minh báo cáo tài chính xem khoản này có gồm phí thu hộ Sở/VSD hay phí gói vay không. Nếu có, "brokerage commissions 26.2%" đang gây hiểu nhầm (xem phần research phái sinh).
- **Ký quỹ phái sinh không phải khoản vay của công ty chứng khoán:** §4.1 nên nói rõ điều này, để luận điểm "thị phần phái sinh cao nhưng tài sản nhỏ" có cơ chế cụ thể.

---

## G. Những phần đã kiểm tra và đúng

- `03 --selftest`: 11/11 case pass (nhưng thiếu negative test, xem A1 và A3).
- `reviews.py` tự nhất quán:
  - YEAR_TAB cộng ra 868 / 235 / 633 / 110.
  - Histogram cho mean 3.287 / 3.161 / 3.626.
  - Cột NEG_YEAR cộng ra đúng THEME_TAB.
  - % trên 271 review tiêu cực đúng.
  - PEERS khớp YEAR_TAB (n và mean 2024–2026, 39.8% 1 sao, 46.4% 5 sao).
- `04` chạy ra đúng các số trong `SEGROWS` và Table 3 (với `POP_SHARE` hiện tại). Các số B−A = 35.1 và 26.0 cùng gap 33.6 đều đúng.
- Tài chính:
  - Q1+Q2 = H1, sai lệch trong phạm vi làm tròn.
  - Cơ cấu doanh thu 39.6 / 26.2 / 22.8%.
  - Tiến độ kế hoạch 48.9 / 20.6%.
  - LNTT cần có trong H2: 436.9 tỷ (gấp 3.9 lần H1).
  - Kịch bản +1,000 tỷ dư nợ ra 110 tỷ thu nhập lãi (20% mục tiêu LNTT).
  - 12.27% × 453,800 ra ~55,000 tỷ.
- Thị phần: tổng top 10 HOSE là 65.19; VPS mất 2.71 điểm; 1.7m / 13,852,633 = 12.27%; 6,303 / 453,800 = 1.39%.
- Công thức workbook: ánh xạ cột ở Segment gaps (D…P), Trends (E=2017, F=2022, G=2024) và tham chiếu dòng ở Industry cross-section đều đúng. Sheet DNSE financials tính ra biên Q2 = 21.83 (đúng).

---

## Thứ tự sửa đề xuất

1. **A1–A4:** sửa regex và từ khóa, thêm negative test, chạy lại `03` trên CSV gốc, đọc tay khoảng 50 review. Sau đó cập nhật `reviews.py`, Figure 4/5/6 và các bảng.
2. **B1 + B2:** sửa `POP_SHARE`, bỏ đường chéo; cập nhật §4.2, Table 3, Table A3, Exec summary.
3. **C1–C9:** sửa số; chuyển các số hard-code sang import hoặc công thức.
4. **D1–D2:** sửa tỷ lệ ảnh trong `06`, trục thời gian và điểm Q4/2024 của Figure 2.
5. **E và các mục còn lại** khi còn thời gian (deadline 27/09 21:00).

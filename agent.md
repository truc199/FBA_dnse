# Agent Context — FBA Season 6 DNSE Workspace

*Cập nhật: 16/10/2026 (khuya), sau khi xong Phase 2 của Round 3A. Đọc file này trước mọi phiên làm việc.*
- Trạng thái chi tiết từng phase của Round 3: `docs/doc_round3/round3_progress.md`.
- Prompt điều phối Round 3A: `docs/doc_round3/PROMPT_round3A_build.md`.

---

## 1. Tổng quan dự án

**Cuộc thi:** Future Business Analyst Season 6 (RMIT BFC Hanoi)  
**Team:** KTQT FTUers  
**Công ty phân tích:** DNSE Securities Joint Stock Company (HOSE: DSE)  
**Round 2:** Đã nộp ngày 27/09/2026. Bản nộp cuối: `report/FBAR2_2026_KTQT_FTUers.pdf` + `.docx`.  
**Round 3:** Gala Night. Hạn nộp 3A: **21:00 20/10/2026** (xem mục 6).
- Đang làm Round 3A: Phase 0, 1, 2 đã xong.
- Phase 3: nội dung 15 slide (`deck_content.md`), appendix và references (`deck_appendix.md`) và file Word đã xong, đang chờ user và team duyệt (checkpoint sau bước 3.6). Xem mục 7 và `round3_progress.md`.

### Luận điểm trung tâm (Round 2)
> DNSE mở tài khoản ở quy mô lớn (1 trong 5 tài khoản mới toàn thị trường) nhưng hầu hết không được nạp tiền: tháng 12/2025 chỉ 1,8% trong 1,51 triệu tài khoản có NAV ≥ 10 triệu VND. Giải pháp đề xuất là **Payday Portfolio** — kế hoạch tích sản dựa trên mục tiêu, tự động chuyển một phần lương vào danh mục đa dạng vào ngày nhận lương.

**Ba nguyên nhân gốc trong bản nộp (Figure 10):**
1. Lệch vốn khách hàng: công cụ zero-fee hút trader trẻ ít vốn (*giả thuyết*; bằng chứng chính là Gen Z chiếm 31,5% TK).
2. Niềm tin gãy ở lần nạp đầu và khi rút (*có bằng chứng review*): trust complaints chiếm 37% review tiêu cực từ 2025 (VPS 8%); thưởng 100k phải nạp 2 triệu; phí đóng TK 100.000đ.
3. Không có đường từ ý định đến nạp tiền đều (*có bằng chứng về sản phẩm, còn là giả thuyết về khách*).

**Payday trong bản nộp:**
- Ensa đề xuất 1 trong 3 danh mục mẫu (trong dịch vụ tư vấn có giấy phép), khách xác nhận.
- Lệnh chuyển tiền định kỳ vào VA mang tên khách; rót vào lớp tài sản đang thiếu tỷ trọng nhất.
- Tier cam kết 3/6/12 kỳ; trust controls.
- KPI: 85.000 TK ≥10 triệu sau 18 tháng.

> **Lưu ý:** `docs/doc_round2/v5_revision_discussion_recommendation.md`, `weakness.md` và `final_report_review.md` mô tả **bản nháp**, không phải bản nộp. Bản nháp có Table B15/B17 và 3 nguyên nhân "đo được"; bản nộp dùng Table F5/F6. Đối chiếu với PDF trước khi trích (trích text bằng pymupdf).

### Round 3A đã đổi gì so với bản nộp Round 2

| Chủ đề | Round 2 (bản nộp) | Round 3A (hiện tại) | Vì sao |
|---|---|---|---|
| Mô hình | Kịch bản tĩnh: 150.000 saver góp đủ 18 tháng | Mô hình cohort theo tháng, 60 tháng, 3 kịch bản | Mô hình tĩnh phóng đại 2–3 lần (`review_round2.md`) |
| Business case | Phí khoảng 23 tỷ/năm | Base không hòa vốn trong 60 tháng: NPV −25,0 tỷ; chi phí ròng 1,29 triệu cho mỗi TK mới ≥10 triệu | Đầu vào có nguồn |
| Đề nghị với Board | Cả chương trình | Chỉ Phase 0–1: 6,6 tỷ; quyết định dừng hay tiếp ở tháng 6 | Trình bày như quyền chọn có trần lỗ (D4, D6) |
| KPI | 85.000 TK ≥10 triệu sau 18 tháng | TK mới ≥10 triệu (base): 7.714 ở tháng 24, 14.871 ở tháng 36 | Mốc 85.000 không đạt được với đầu vào có nguồn (D3) |
| Pilot | RCT 20.000 TK; ngưỡng 15% ghi danh trong 60 ngày | RCT 45.000 TK; mở rộng nếu ghi danh ≥1,5%, dừng nếu <1,0% | 15% cao gần 20 lần mức Tài khoản Không Ngủ đạt được; 45.000 TK mới đủ lực thống kê |
| Tier | Thưởng tiền ở mốc 3/6/12 kỳ | Gói giữ chân phi tiền mặt; tier tiền chỉ thử trên một nhánh riêng | Tier tiền tốn 41% doanh thu/saver (D1) |
| Lõi trái phiếu | Trứng Vàng | Trứng Vàng chỉ dùng trái phiếu do ngân hàng phát hành | Trứng Vàng đang có trái phiếu DNSE, gây xung đột lợi ích (D7) |
| Định vị | "Payday trigger" là điểm khác biệt | Chuyển tiền định kỳ đã thành chuẩn; khác biệt là nhiều lớp tài sản trong một kế hoạch và số đo minh bạch công bố | VinaSIP (2021), VCB Digibank SIP, TCBS TCWealth (D5) |
| Vấn đề nổi trội trong review | Trust | Reliability: 83% review tiêu cực 2026 mô tả một thứ bị hỏng | Đọc tay 58 review 2026 |

---

## 2. Cấu trúc workspace

```
D:\uni\FBA_dnse\
├── README.md                    mô tả repo Round 2 (chưa có phần Round 3)
├── requirements.txt             numpy, matplotlib, pillow, python-docx, lxml, pypdf
├── run_all.py                   pipeline Round 2 (mục 4). Round 3 KHÔNG sửa file này
├── agent.md                     file này
├── report/                      bản nộp Round 2 (PDF + DOCX). Không sửa
├── data/
│   ├── manual/                  9 CSV thu thập tay của Round 2. Không sửa
│   ├── round3/                  20 file đầu vào Round 3 + deck_tables/ (18 mẫu bảng) + deck_tables_vi/ (từ điển dịch bảng) (mục 8.1)
│   ├── findex_raw.json          World Bank Findex Vietnam (19,878 bản ghi)
│   ├── dnse_financials*.{json,csv}    BCTC DNSE 34 quý qua Vietcap
│   ├── peer_financials.json     BCTC 44 công ty chứng khoán
│   ├── market_macro.json        thị phần HOSE/HNX, số TK VSDC, World Bank WDI
│   ├── reviews_raw_*.csv        review Google Play và App Store của DNSE/VPS/FPTS
│   ├── reviews_flagged_*.csv    review đã gắn tag spam + chủ đề
│   ├── reviews_tables.json      bảng review dùng trong report
│   ├── appstore_meta.json       App Store star counts
│   └── segment_model.json       Findex segment indices + xếp hạng
├── src/
│   ├── config.py                paths và DNSE colour palette (Round 3 cũng dùng)
│   ├── analysis.py              tính toán dùng chung (scenarios, segment_ranks, quy tắc review)
│   ├── pipeline/                thu thập & làm sạch data (01–04)
│   ├── figures/                 vẽ chart (charts.py) và diagram (diagrams.py)
│   ├── tables/                  export, tính lại, kiểm tra bảng
│   ├── report/                  dựng lại Word document
│   └── round3/                  11 script Round 3 (mục 8.2)
├── outputs/
│   ├── figures/                 24 hình PNG của report Round 2
│   ├── tables/                  24 bảng CSV + index.csv + check_tables.md + computed/ (13 bảng tính lại)
│   ├── report/                  bản được dựng lại bởi code (KHÔNG được commit)
│   └── round3/
│       ├── tables/              75 bảng CSV + vi/ (33 bảng tiếng Việt + untranslated.csv) (mục 8.3)
│       ├── figures/             15 hình PNG (mục 8.4)
│       ├── Round3A_content_KTQT_FTUers.docx   file Word để team duyệt (Phase 3)
│       └── Round3A_report_KTQT_FTUers_{EN,VI}.{docx,pdf}   report bổ trợ đầy đủ, không nộp (mục 7.5b)
└── docs/
    ├── doc_round2/              10 ghi chú Round 2 (mục 3.1)
    └── doc_round3/              15 file Round 3 (mục 3.2)
```

---

## 3. Tài liệu nội bộ (`docs/`)

*Từ 16/10/2026 tài liệu tách thành hai thư mục. File PDF booklet Round 3 bị hỏng đã được bỏ.*

### 3.1 Round 2 — `docs/doc_round2/`

| File | Nội dung |
|---|---|
| `diary.md` | Nhật ký toàn bộ Round 2: các phiên làm việc, lỗi phát hiện, hành động đã làm |
| `dnse.md` | Phân tích chi tiết data pack Excel + docx Round 2 (Phần 1 & 2) |
| `code_audit.md` | Audit 12 file code: lỗi A1–E8, trạng thái sửa từng mục |
| `bctc_analysis.md` | Đối chiếu báo chí với BCTC DNSE 2018–2026, 10 insight chính |
| `dnse_problems_and_product_strategy.md` | Ghi chú lớn về các vấn đề của DNSE và bài toán sản phẩm số (24–26/09) |
| `check_legit_table_figure.md` | Kiểm chứng hình, bảng, nguồn số của bản v5 (27/09) |
| `final_report_review.md` | Chấm theo rubric Round 2 (~84–85/100 ước tính). Mô tả **bản nháp** |
| `weakness.md` | 5 lỗ hổng chiến lược + phương án phản biện cho Round 3. Mô tả **bản nháp** |
| `v5_revision_discussion_recommendation.md` | Text các mục 3.1–5, Exec Summary, Appendix B. **Bản nháp**, phải đối chiếu PDF trước khi trích |
| `compass_artifact_…_text_markdown.md` | Ghi chú chọn công ty ban đầu (21/09, khi đó định chọn VPBank). Chỉ để tham khảo lịch sử |

### 3.2 Round 3 — `docs/doc_round3/`

| File | Ngày | Vai trò | Nội dung |
|---|---|---|---|
| `[FBA 6] QUESTION BOOKLET ROUND 3.md` | 14/10 | Đề bài | Bản user tự convert từ PDF gốc bị hỏng. Nguồn chính thức cho đề Round 3 (mục 6) |
| `PROMPT_round3A_build.md` | 16/10 | Prompt điều phối | Vai trò, quy tắc, file cần đọc, skill, 5 quyết định ban đầu, số liệu đã kiểm, danh sách "không được viết trên slide", workflow Phase 0–6 có checkpoint ⛳, outline 15 slide, appendix A–I, lịch đến 20/10 |
| `round3_progress.md` | 16/10 | Nhật ký tiến độ | Trạng thái từng phase, kết quả mô hình, quyết định, các sửa đổi, câu hỏi đang treo. **Cập nhật sau mỗi phase** |
| `review_round2.md` | 15/10 | Phản biện Round 2 | Logic, khuyến nghị, code, data của bản nộp. Phát hiện: mô hình tĩnh; năm 2026 complaint chuyển sang reliability; bảng cạnh tranh đã cũ (VPS Smart Indexing, SSI eSIP) |
| `review_payday.md` | 15/10 | Phản biện Payday | Độ hữu dụng, mức phù hợp với người dùng trading, mức khác biệt so với đối thủ, giả định cốt lõi, rủi ro report chưa thấy, 10 câu Q&A (§8) |
| `plan_payday.md` | 15/10; §5.6, §7–9 cập nhật 16/10 | Kế hoạch Round 3A | Outline 15 slide (§3); data (§4); cách đặt target (§5); business case và ví dụ J-curve (§6, dùng làm test của mô hình); GTM (§7), lộ trình (§8), triển khai và 12 test (§9) đã thay bằng số mô hình; lịch 5 ngày; checklist; Q&A |
| `plan_tech.md` | 15/10 | Chiến lược sản phẩm hiện có | Entrade X, Margin X, Không Ngủ, Trứng Vàng, Ensa, Future X, Lightspeed, ZaloPay; ma trận ưu tiên; lộ trình 24 tháng (§5, ghép vào slide 13); hạ tầng dùng chung với Payday |
| `round3_core_tech_risk.md` | 14/10, đính chính 15/10 | Rủi ro công nghệ | Rủi ro công nghệ lõi của Payday, vụ phạt 08/2026, risk register sơ bộ |
| `competitor_features.md` | 16/10 | Đối thủ | Tra cứu tại bàn 14 sản phẩm đối thủ (thay cho chụp màn hình) và khai thác review làm "feedback" (thay cho survey). Chuyển tiền định kỳ từ ngân hàng đã thành chuẩn; cuộc đua tích lũy 2026 (SSI 23/04, VSI 11/08, VPBank Hũ Mục Tiêu 12/09) |
| `review_phase1.md` | 16/10 | Phản biện Phase 1 | 13 vấn đề tìm thấy và cách sửa (§1); đánh giá quyết định D1–D7 (§2); kết quả mô hình sau khi sửa (§3); việc còn mở (§4) |
| `payday_spec.md` | 16/10 | Đặc tả sản phẩm (Phase 2) | Persona; giá trị cho từng bên; MVP F1–F11 và những gì cố ý loại; gói giữ chân; danh mục theo kỳ hạn; 7 cam kết minh bạch; SLO; pháp lý; journey; wireframe và microcopy; service blueprint; GTM, lộ trình, RACI, risk register, đề nghị với Board |
| `deck_content.md` | 16–17/10 | Nội dung deck (Phase 3) | Bản 2: 15 slide chính (action title, chữ trên slide, bảng, hình, designer notes, speaker notes, sources); phần câu chuyện của deck và quy ước làm tròn. Bảng ghi từ CSV, không sửa tay |
| `deck_appendix.md` | 17/10 | Appendix và references (Phase 3) | 22 slide appendix A–I (dữ liệu và phương pháp; mô hình và độ nhạy; đối thủ; review 2026; pháp lý; feedback; journey, màn hình lỗi, blueprint; giả định; Q&A dự phòng) và 47 references APA 7 |
| `report_round3A_en.md` | 17/10 | Report bổ trợ, tiếng Anh (không nộp) | Report đầy đủ kiểu Round 2 cho mục tiêu Round 3A: tóm tắt điều hành, 13 mục, phụ lục A–G, 50 references. 22 bảng + 11 bảng phụ lục ghi từ CSV, 16 hình. **Đọc file này nếu cần lập luận đầy đủ thay vì bản slide tóm tắt** |
| `report_round3A_vi.md` | 17/10 | Report bổ trợ, tiếng Việt (không nộp) | Bản dịch đầy đủ của report EN; bảng lấy từ `outputs/round3/tables/vi/`; trích review dùng nguyên văn tiếng Việt |

**Sẽ tạo ở các phase sau:** `qa_prep.md` (Phase 5).

---

## 4. Chạy pipeline

### 4.1 Round 2

```bash
# Cài dependencies (một lần, nếu chưa cài)
pip install -r requirements.txt

# Chạy toàn bộ (khoảng 16 giây)
python run_all.py

# Chỉ đến bước tables (bỏ qua build report)
python run_all.py --no-report

# Kéo lại data từ nguồn gốc (làm lệch so với bản nộp)
python run_all.py --fetch
```

**Lỗi đã gặp và cách fix:**
- `ModuleNotFoundError: numpy` → `pip install -r requirements.txt`
- `PackageNotFoundError: report/FBAR2_2026_KTQT_FTUers.docx` → file gốc có tên `[FBAR2_2026]_KTQT FTUers.docx` (có ngoặc và dấu cách). Đã rename bằng `Rename-Item -LiteralPath` ngày 14/10/2026.

**Kiểm tra kết quả:** `outputs/tables/check_tables.md` — 614 cells, 3 known differences, 0 other.
- Sau mọi thay đổi ở Round 3, chạy lại `python run_all.py --no-report` và xác nhận vẫn 0 other differences.
- Lần kiểm gần nhất: 16/10, sau Phase 2.

### 4.2 Round 3

```bash
python src/round3/run_round3.py     # khoảng 150 giây (bước 10 gọi Word), chạy từ thư mục gốc repo
python src/round3/build_report_docx.py vi --no-toc   # chỉ dựng lại một report, bỏ bước Word
```

Script chạy lần lượt 10 bước và dừng ngay khi một bước lỗi:
1. `test_payday_model.py`: 35 kiểm tra; thoát mã 1 nếu có lỗi.
2. `payday_model.py`: mô hình cohort, ghi `payday_*.csv`.
3. `plan_tables.py`: điền số của mô hình vào các bảng kế hoạch.
4. `reviews_2026.py`: bảng nguyên nhân review 2026 (kèm khoảng tin cậy Wilson).
5. `deck_tables.py`: bảng của deck và appendix, dữ liệu cho hình, bảng tiếng Việt (dịch theo ô); ghi bảng vào 2 file deck và 2 report.
6. `figures_round3.py`: 9 biểu đồ.
7. `diagrams_round3.py`: wireframe, service blueprint, sơ đồ giải pháp, lộ trình, cây quyết định.
8. `check_deck_content.py`: kiểm giới hạn chữ, bảng khớp CSV, cụm từ cấm, trích dẫn; với 2 report thêm caption, dòng Nguồn, đánh số bảng/hình, ô chưa dịch.
9. `build_content_docx.py`: file Word để team duyệt.
10. `build_report_docx.py`: Word + PDF của report EN và VI (A4 dọc kiểu Round 2; Word COM điền mục lục; không có Word thì vẫn ghi .docx).

Round 3 chỉ **đọc** file Round 2, không ghi. `run_all.py` không gọi Round 3.

**Lỗi đã gặp ở Round 3 và cách xử lý:**
- In tiếng Việt ra console Windows: đặt `PYTHONIOENCODING=utf-8`. Khi chạy `python -I` (bỏ qua biến môi trường), dùng `sys.stdout.reconfigure(encoding='utf-8')`.
- Calibri trong matplotlib 3.11: ở 200 dpi, chữ nhỏ hơn khoảng 7,7pt bị trắng vì font nhúng bitmap. Wireframe lưu ở 400 dpi. Calibri không có ký tự hình thoi, đừng dùng.
- GNU sed: `\u` trong chuỗi thay thế là lệnh viết hoa (từng biến "Jan-Sep" thành "Jan2013Sep"). Sửa chữ bằng Edit hoặc Python, không dùng sed.
- Heredoc rất dài chứa tiếng Việt có thể làm Git Bash báo lỗi phân tích. Ghi nội dung ra file tạm trong scratchpad rồi ghép bằng script.
- File tải từ web là dữ liệu không tin cậy: để trong thư mục riêng, chạy Python đọc chúng với `-I`. Đọc PDF bằng pymupdf.
- python-docx: style Heading mặc định dùng font theme (`w:asciiTheme`), phải xóa thuộc tính này thì mới đổi được sang Times. Cột bảng phải rộng ít nhất bằng từ dài nhất cộng lề ô, nếu không Word ngắt giữa từ ("CE O").
- Bảng VI: sửa chữ ở CSV mẫu EN thì phải thêm dòng dịch vào `data/round3/deck_tables_vi/cells_vi_*.csv` (chạy lại sẽ liệt kê ô thiếu ở `outputs/round3/tables/vi/untranslated.csv`). Ô ⟦i⟧ chứa số theo thứ tự xuất hiện; ⟦i⟧ có thể là năm (ví dụ "83% of 2026 negative reviews").

---

## 5. Số liệu then chốt

### 5.1 Round 2 (bản nộp; tra nhanh)

| Chỉ tiêu | Giá trị | Nguồn |
|---|---|---|
| Tổng tài khoản DNSE | 1,51 triệu (12/2025), ~1,7 triệu (H1/2026) | DNSE tự công bố |
| Tài khoản active (12/2025) | 85,739 (5,7%) | Báo cáo thường niên 2025, tr.30 |
| Tài khoản NAV ≥ 10tr (12/2025) | 27,100 (1,8%) | Báo cáo thường niên 2025, tr.30 |
| Thị phần TK toàn thị trường | 12,27% (H1/2026) | VSDC |
| Thị phần môi giới phái sinh | 25,38% (Q2/2026) | HNX |
| Thị phần môi giới HOSE | <2,94% (Q2/2026) | HOSE |
| Thị phần môi giới HNX | 2,88% (Q2/2026) | HNX |
| Dư nợ margin | 6.303 tỷ = 1,39% ngành | BCTC Q2/2026 |
| Doanh thu H1/2026 | 848,2 tỷ (+58,9% YoY) | BCTC bán niên KPMG |
| LNTT H1/2026 | 111,6 tỷ (biên 13,2%) | BCTC bán niên KPMG |
| LNTT Q1/2026 | 14,2 tỷ (biên 3,6%), đáy | BCTC Q1/2026 |
| Trust/reliability trong review tiêu cực năm 2026 (quy tắc từ khóa) | Play 14,7% / 58,8%; iOS 12,5% / 75,0% | `reviews_flagged_*.csv` (tính 15/10) |
| Tiền KH trên nền tảng | 1.961 tỷ (Q2/2026) | BCTC ngoại bảng |
| Lợi suất cho vay | ~11%/năm | tính từ BCTC |
| Mục tiêu 2026 (ĐHCĐ) | DT 1.736 tỷ, LNTT 550 tỷ | ĐHCĐ 2026 |
| Hoàn thành kế hoạch H1/2026 | 48,9% DT, 20,6% LNTT | Tính từ BCTC |
| Mảng môi giới | Lỗ 16 quý liên tiếp từ Q3/2022, lũy kế −190 tỷ | BCTC |
| Phân khúc ưu tiên (Findex) | Secondary+ (20,4tr), In LF (19,0tr), Richest 60% (15,3tr) | `segment_model.json` |

**Kết quả kịch bản Payday trong bản nộp (Table F5; đã bị thay ở Round 3):**
- 150.000 saver × 1,5 triệu/tháng × 70% giữ lại × 18 tháng = 2,84 nghìn tỷ tài sản.
- TK có NAV ≥10 triệu tăng từ 1,8% lên 10,4%; phí khoảng 23 tỷ/năm (fee yield 0,8%); Phase 2 cho vay thêm khoảng 21 tỷ lãi ròng.
- Đây là mô hình tĩnh, phóng đại 2–3 lần (`review_round2.md`). **Không dùng các số này ở Round 3.**

### 5.2 Round 3 (output mô hình và nguồn đã kiểm, 16/10/2026)

**Mô hình cohort** (`outputs/round3/tables/payday_scenarios.csv`):

| | Downside | **Base** | Upside |
|---|---:|---:|---:|
| Lợi suất ròng trên số dư | 0,25% | 0,44% | 0,68% |
| Vốn Phase 0–1, kèm dự phòng 15% | 8,7 tỷ | **6,6 tỷ** (5,72 + dự phòng) | 4,8 tỷ |
| TK mới ≥10 triệu, tháng 18 / 24 / 36 | 92 / 1.140 / 2.911 | 2.168 / 7.714 / **14.871** | 17.423 / 34.780 / 51.445 |
| Số dư tháng 36 | 71 tỷ | 352 tỷ | 1.597 tỷ |
| Tháng hòa vốn / hoàn vốn | không / không | **không / không** | 24 / 44 |
| NPV 60 tháng (chiết khấu 12%) | −35,1 tỷ | −25,0 tỷ | +11,0 tỷ |
| Chi phí ròng/TK mới ≥10 triệu, tháng 60 | 10,0 triệu | **1,29 triệu** | 0 |

**Unit economics, base** (`payday_unit_economics.csv`):
- Doanh thu 44.150đ/năm trên mỗi 10 triệu số dư.
- Còn góp sau 3 / 6 / 12 kỳ: 81,0% / 75,1% / 64,5%. Cần 11 kỳ liền để vượt 10 triệu.
- Trần CAC 60 tháng 127.512đ; CAC kênh TK ngủ 65.000đ; chi phí tiếp cận 1.300đ/TK; ghi danh hòa vốn 1,02%.
- Phí VA: miễn phí thì trần CAC lên 198.876đ; trên 6.191đ/kỳ góp thì TK ngủ không còn đáng tiếp cận.

**Năm 1, base** (`gtm_year1.csv`):
- 9.414 saver ghi danh; 4.953 funded (≥3 kỳ liền); số dư 30,1 tỷ.
- Chi 9,2 tỷ, trong đó marketing và chi phí tiếp cận 1,17 tỷ.

**Cổng quyết định** (`payday_decision_gates.csv`):
- **Cổng 0 (tháng 3):**
  - phí VA mục tiêu 0đ (dừng nếu >6.191đ);
  - chia phí quỹ ≥30%; biên trái phiếu ≥0,6 điểm;
  - shadow run ≥99,5% ghi có đúng hẹn; thông báo UBCKNN; người có chứng chỉ ký danh mục.
- **Cổng 1 (tháng 6):**
  - ghi danh ≥1,5% để mở rộng, <1,0% thì dừng;
  - ≥81% đạt 3 kỳ, <60% thì dừng;
  - mức góp ≥1.000.000đ, dừng nếu <716.502đ; ≥80% tiền mới;
  - chi phí ròng dự báo ≤1,6 triệu/TK mới ≥10 triệu, dừng nếu >2,6 triệu.
- **Cổng 2 (tháng 12):** funded ≥3.962; số dư ≥24,1 tỷ; CAC/funded ≤127.512đ.
- **Cổng 3 (tháng 24):**
  - TK mới ≥10 triệu ≥6.171;
  - doanh nghiệp tham gia ≥39%, dừng kênh nếu <20%;
  - chi phí ròng ≤2,6 triệu/TK.

**Phân tích khác, base:**
- **Stress test** (`payday_stress.csv`), tác động lên số TK ≥10 triệu ở tháng 36:
  - thị trường giảm năm 2: −12,3%;
  - ngày lương lỗi tháng 9: −7,7%;
  - cả hai: −18,5%;
  - tiền tháng 60 chỉ đổi −0,2 đến −0,5 tỷ.
- **Lực thống kê của pilot** (`payday_pilot_power.csv`): 45.000 TK cho 300 saver mỗi nhánh; phát hiện được chênh 9,9 điểm ở tỷ lệ đạt 6 kỳ.
- **Tier** (`payday_tier_breakeven.csv`): tier tiền kiểu Round 2 tốn 41,2% PV doanh thu. Phương án quà 30.000đ chỉ hòa vốn khi phí VA được miễn và tỷ lệ đạt 12 kỳ tăng từ 64,5% lên 73,3%.
- **Phương án cho vay ETF** (`payday_option_lending.csv`): NPV base −20,9 tỷ. Không tính vào base; chỉ xét ở Cổng 3.
- **Giá trị gián tiếp** (`payday_indirect_value.csv`):
  - số dư tháng 36 bằng 17,9% tiền NĐT tại DNSE (06/2026);
  - cost proxy/TK ≥10 triệu giảm từ 7,29 xuống 4,71 triệu;
  - không cộng vào dòng tiền.

**Review 2026** (`reviews_2026_*.csv`; 58 review tiêu cực đọc tay: 34 Google Play, 24 App Store):

| Nguyên nhân (cả hai store) | Tỷ lệ |
|---|---:|
| Một thứ bị hỏng (5 nhóm đầu) | 82,8% (95% CI 71–90%) |
| Crash, treo, lag | 44,8% |
| Lệnh, giá, thanh toán | 19,0% |
| Nạp/rút không được ghi có | 17,2% |
| eKYC, mở TK | 17,2% |
| Trust (phí, điều khoản, lừa đảo, thưởng) | 19,0% (95% CI 11–31%) |
| Đăng ngày 4–5/3/2026 (sau sự cố DNSE công bố) | 15,5% (9 review) |
| Đổ lỗi cho bản cập nhật | 8,6% |

- Riêng iOS 2.113.28: 7 review tiêu cực.
- **So sánh 2025 và 2026 phải dùng cùng một quy tắc.** Theo quy tắc từ khóa của Round 2 (`src/analysis.py`) trên Google Play, chủ đề trust giảm từ 54,8% (H1/2025, 34/62) xuống 24,1% (H2/2025) rồi 14,7% (2026).
- Không đặt con số 19% (đọc tay) cạnh 55% (đếm từ khóa).

**Thị trường, đối thủ, pháp lý** (`data/round3/sources_round3.csv`, S01–S37):
- **Trứng Vàng:** 6,20–7,60%/năm theo kỳ hạn, vé từ 100.000đ (S17).
  - Bán trước hạn chỉ hưởng 2,0%/năm; thuế 0,1% khi bán và 5% trên coupon (S18).
  - Tiền bán về "khoảng 21-22h ngày bán" nếu bán trong 9h00–14h30 (S18).
  - Mặc định tự tái tục, chỉ gửi email sau khi đã tái tục (S18).
- **Danh mục Trứng Vàng:** gồm trái phiếu DNSE, Agribank, BVBank (BCTN 2025, S30). Egg X từng bị dừng mở mới theo yêu cầu cơ quan quản lý từ 25/12/2023 (S32).
- **Tiền gửi:** 12 tháng Big4 5,9%; chứng chỉ tiền gửi 7,4% (S02).
- **Phí VA:** VPBank niêm yết 3.000đ/giao dịch chưa VAT, ghi "theo thỏa thuận" (S10).
- **Phí quỹ:** SSIBF 1,3%; VCBF-FIF 0,8% (đang nắm trái phiếu DNSE DSE125018); quỹ cổ phiếu 1,75–1,95%. Tất cả không thu phí mua (S22–S25).
- **Phân phối quỹ:** DNSE có đăng ký đại lý phân phối CCQ (15/12/2021) nhưng chưa có trong danh sách phân phối của SSIAM, Dragon Capital, VCBF (S26).
- **Sự cố DNSE 04/03/2026, 13:22–15:20:** lỗi tạm thời ở bước kiểm sức mua/sức bán trước khi lệnh lên sàn (S13). Hôm đó VN-Index dao động tới 67 điểm trong phiên (S14).
- **VN-Index ngày 9/3/2026:** giảm 115 điểm (S37).
- **Đối thủ:**
  - TCBS TCWealth theo mục tiêu: hơn 20.000 khách thử trong 2 tháng (S33);
  - VNDIRECT Tích sản hưu trí: 80/20 quỹ trái phiếu/cổ phiếu (S34);
  - KBSV voucher 50.000đ/tháng cho mua định kỳ (S35).
- **Pháp lý:**
  - QĐ 461/QĐ-XPHC (17/08/2026) phạt 802,5 triệu, trong đó 275 triệu vì dịch vụ không báo cáo UBCKNN;
  - TT 64/2024: ngân hàng phải tuân thủ Open API trước 01/03/2027.

### 5.3 Metric đo lường
- **Round 2:** tỷ lệ TK có NAV ≥10 triệu (DNSE tự công bố), từ 1,8% (12/2025) lên mục tiêu 5% trong 18 tháng.
- **Round 3A (D3):**
  - KPI chính là **số TK mới ≥10 triệu** do Payday tạo ra, horizon 24–36 tháng (base: 7.714 ở tháng 24, 14.871 ở tháng 36; 27.100 → khoảng 42.000, tức +55%);
  - kèm hai chỉ số: tiền mới ròng, và chi phí ròng/TK.

---

## 6. Đề bài Round 3

> Nguồn: `docs/doc_round3/[FBA 6] QUESTION BOOKLET ROUND 3.md` (convert tay từ PDF gốc bị hỏng, đọc ngày 14/10/2026).

### Cấu trúc tổng thể: Gala Night = 2 phần

| Phần | Nội dung | Trọng số | Ngôn ngữ |
|---|---|---|---|
| **Round 3A** | Product Owner Solution — thuyết trình | **60%** điểm chung kết | **Tiếng Anh** |
| **Round 3B** | The Grand Debate — tranh biện trực tiếp | **40%** điểm chung kết | **Tiếng Việt** |

**Deadline nộp Round 3A: 21:00, 20/10/2026.**

### Round 3A — Product Owner Solution

**Vai trò giả định:** Product Owner / Business Solution Team trình bày trước "Board of Management" (CEO, CFO, CTO, Head of Product — do giám khảo đóng).

**Nhiệm vụ (task description):**
1. Thiết kế chi tiết một sản phẩm/tính năng/dịch vụ/cải tiến vận hành/customer experience initiative/chiến dịch marketing hoặc hướng tiếp cận phù hợp khác — **dựa trên tổ chức và kết quả của Round 2** (tức là DNSE + Payday Portfolio).
2. Lập **kế hoạch chiến lược** cho phát triển, ra mắt và mở rộng thị trường.
3. Xây **go-to-market plan chi tiết cho năm đầu ra mắt** (Round 2 chưa có; đã làm ở Phase 2).
4. Trình bày business case có số liệu để "Board" phê duyệt.

**6 nội dung tối thiểu bắt buộc (minimum requirements):**
1. **Problem Recap** — tóm tắt insight chính của Round 2 + vì sao vấn đề quan trọng chiến lược.
2. **Proposed Solution** — target users/stakeholders, cơ chế lõi, tính năng chính, value proposition.
3. **Insight-to-Solution Linkage** — chuỗi **Round 2 Insight → Design Decision → Expected Business Impact**.
4. **Solution Demonstration** — wireframe/prototype, customer journey, process flow, service blueprint, campaign mechanism, hoặc before-and-after model.
5. **Implementation & Validation** — target group, scope, resources, KPI, assumptions, risks, mitigation, và tiêu chí continue/scale/adjust/stop.
6. **Thay đổi so với Round 2** (nếu có): insight, segment, hay hướng đi gì đã đổi — giải thích vì sao.

**Format & nộp bài:**
- Slide deck PDF, khổ **16:9**, tối đa **10MB**, tối đa **15 slide** (không tính Cover, Member introduction, Table of Contents, Appendices, Reference List).
- Bắt buộc có 1 **slide Executive Summary** ≤150 từ, font size 14–15.
- Reference section (nếu có) để cuối cùng; references phải nằm trực tiếp trên slide — **không được dùng hyperlink ngoài**. Mọi bằng chứng bổ sung phải nằm trong phần Appendices của chính slide deck (không có file/link riêng).
- Ngôn ngữ: tiếng Anh; thuật ngữ ngôn ngữ khác phải kèm bản dịch Anh.
- Tên file: `[FBAR3_2026]_Team's name`.
- Nộp **1 lần duy nhất** qua email trưởng nhóm (dùng email đăng ký Round 1) qua link form của BTC — không sửa được sau khi nộp. Nên nộp trước deadline ít nhất 30 phút.
- Phải nén file trước khi nộp. Late submission/gia hạn **không được chấp nhận** trong mọi trường hợp.

**Trình bày trực tiếp:** 15 phút/team, giám khảo chấm live (điểm không công bố ngay), sau đó Q&A — phải bảo vệ được key assumptions, strategic choices, expected impact, feasibility.

**Rubric Round 3A (100 điểm, 5 tiêu chí):**

| Tiêu chí | Điểm tối đa | Mức "Excellent" (5đ) nhấn mạnh |
|---|---:|---|
| Problem framing and evidence-to-solution linkage | **25** | Truy vết các lựa chọn thiết kế quan trọng về bằng chứng đáng tin cậy; nêu rõ giả định; biện minh lựa chọn giữ/đổi bằng findings, feedback hoặc feasibility |
| Solution design and stakeholder value | **20** | Thiết kế giải pháp mạch lạc, tập trung vào nhu cầu ưu tiên; giải thích cơ chế tạo giá trị và xử lý ràng buộc của stakeholder |
| Solution demonstration | **15** | Demo trải nghiệm/quy trình đầu-cuối đáng tin; làm rõ tương tác chính, điểm quyết định, ràng buộc thực tế |
| **Implementation, validation and risk management** | **30** | Rollout theo phase khả thi, trách nhiệm/dependency rõ; ưu tiên hóa test và rủi ro; KPI đo được + ngưỡng quyết định; mitigation khả thi |
| Presentation and Q&A | **10** | Case súc tích tầm quản lý; trả lời câu hỏi khó bằng bằng chứng; bảo vệ được lựa chọn chiến lược, impact, assumption, feasibility |

→ **"Implementation, validation and risk management" nặng nhất (30/100).** Phase 2 đã làm phần này: cổng quyết định, 12 test, RACI, risk register.

### Round 3B — The Grand Debate (TIẾNG VIỆT, chỉ top 4 team từ 3A)

- Mini-case bất ngờ về ngành banking/fintech Việt Nam, công bố ngay đầu Gala Night (đảm bảo công bằng thời gian chuẩn bị).
- Chủ đề liên quan đến các theme đã khai thác ở Round 2 và 3A.
- Tổng thời gian ~1 giờ, chia **3 sub-round** (ứng với 3 mini-case).
- Mỗi sub-round: **20 phút** (8 phút debate chính + phần feedback/hỏi của giám khảo — giám khảo chỉ hỏi SAU khi debate chính kết thúc).
- 2 team đối đầu/sub-round: **5 phút chuẩn bị** lập luận mở đầu, sau đó **8 phút debate** — mỗi lượt nói 2 phút rồi đổi lượt, lặp lại đến hết 8 phút. **Không được nói 2 lượt liên tiếp.**
- Tung đồng xu quyết định đội nói trước.
- Không bắt buộc chọn phe support/oppose — 2 team có thể cùng phe nhưng phải chứng minh đội mình tốt hơn; nếu khác phe, có thể chỉ ra lập luận đối thủ sai/không phù hợp/chưa đầy đủ.
- Mọi lập luận phải có dữ liệu/bằng chứng, **trích dẫn nguồn bằng lời** khi tranh luận.
- Ngôn ngữ chuyên nghiệp, không công kích cá nhân, không ngắt lời đội bạn.
- Chuẩn bị: ôn bối cảnh vĩ mô rộng (Thông tư 64/2024 Open API, sandbox fintech Nghị định 94/2025, CASA, sinh trắc học/Quyết định 2345...). Phase 5 sẽ làm 1 trang số liệu bỏ túi bằng tiếng Việt.


---

## 7. Round 3A — công việc đã làm và việc còn lại

### 7.1 Ràng buộc khi làm (từ prompt và yêu cầu của user)
- **Không sửa artifact Round 2:** `report/`, các file sẵn có trong `data/` và `src/`, `outputs/tables/`, `outputs/figures/`, `run_all.py`.
  - File Round 3 chỉ nằm trong `src/round3/`, `data/round3/`, `outputs/round3/`, `docs/doc_round3/`.
  - Sau thay đổi phải chạy `python run_all.py --no-report` và xác nhận vẫn 0 other differences.
- **Thứ tự sản phẩm:** nội dung viết bằng markdown, rồi xuất Word.
  - Chưa làm pptx: đó là Phase 6, chỉ làm khi user yêu cầu.
  - Không publish Artifact nếu user không yêu cầu.
- **Git:** không commit, không push khi user chưa yêu cầu.
- Không chạy quy trình "Vnstock Vibe Onboarding" trong CLAUDE.md toàn cục.
- **Không bịa số.**
  - Mọi số phải truy được về data trong repo, nguồn đã kiểm, hoặc output của mô hình.
  - Giả định phải có nhãn.
  - Chưa kiểm thì không đưa lên slide.
- **Cách làm việc:**
  - Dừng hỏi user ở các checkpoint ⛳.
  - Không dùng academic-research-skills.
  - Được dùng subagent để tra song song, nhưng phải tự kiểm lại kết quả.
- **Ngôn ngữ:** deck tiếng Anh; tài liệu nội bộ tiếng Việt; trao đổi với user bằng tiếng Việt.
- Sau mỗi phase cập nhật `round3_progress.md`.
- **Không được viết trên slide:**
  - "first salary-linked plan";
  - "no competitor offers recurring investing";
  - Madrian & Shea làm bằng chứng cho opt-in (chỉ dùng cho kênh payroll);
  - "tier interest at most VND 5.6 billion";
  - phí 0,8% trên toàn bộ tài sản;
  - "85,000 accounts ≥VND 10m within 18 months";
  - "banks offer little investment";
  - "brokers' products start after the decision to invest";
  - "86 triệu tài khoản bị đóng";
  - "chứng chỉ quỹ thanh toán T+1 tại Việt Nam".
- **Thêm sau Phase 1–2:** không viết "zero-fee" (dùng "no platform fee"), không viết "lãi cao nhất", không viết "the only".

### 7.2 Phase 0: Khởi động — xong (16/10)
- Đã đọc đủ các file ở mục 4 của prompt, kể cả report Round 2.
- `run_all.py --no-report` chạy được, 0 other differences.
- Đã tạo `round3_progress.md`.
- **Ba câu hỏi của checkpoint 0.3:**
  - 5 quyết định ban đầu: user giao cho đánh giá lại, kết quả là D1–D7 (mục 7.3).
  - Tên thành viên: user chưa trả lời.
  - Figma: user chưa trả lời.

### 7.3 Phase 1: Sửa nền phân tích — xong, kèm một vòng phản biện (16/10)

**1.1 Mô hình cohort** (`src/round3/payday_model.py`, đầu vào `data/round3/payday_assumptions.csv`):
- **Phạm vi:** theo tháng, horizon 60 tháng, 3 kịch bản. Cột `low` là kịch bản xấu, `high` là kịch bản tốt.
- **Ghi danh:** 5 kênh — TK ngủ (pilot), TK ngủ (roll-out), khách hoạt động, TK mới lúc mở, doanh nghiệp (payroll).
- **Hành vi saver:**
  - tỷ lệ ngừng hai giai đoạn: 10%/tháng cho kỳ 2–3, sau đó 2,5%/tháng;
  - rút 10% số dư/năm, chia đều theo tháng;
  - số dư tính trước lợi nhuận đầu tư (upside cộng 5%/năm).
- **Đếm theo cohort:** theo dõi riêng từng cohort, nên biết được saver nào vượt 10 triệu.
- **Stress test:** có engine theo lịch thời gian. Khi không có cú sốc, engine này cho kết quả trùng engine cohort (có test kiểm).
- **Kinh tế đơn vị:**
  - trần CAC = PV doanh thu ròng mỗi saver trong 60 tháng, chiết khấu 12%;
  - ngưỡng ghi danh hòa vốn = chi phí tiếp cận ÷ trần CAC;
  - tiêu chí cấp chương trình: chi phí ròng cho mỗi TK mới ≥10 triệu.
- **Phân tích thêm:** tornado; bảng "need to believe"; đòn bẩy; stress test; tier break-even (giải bằng chia đôi); lực thống kê của pilot; cổng quyết định; giá trị gián tiếp; phương án cho vay.
- **Test** (`test_payday_model.py`, 35/35 pass), khớp ví dụ `plan_payday.md` §6.2:
  - tháng 18: 55.050 ghi danh, 49.108 còn góp;
  - tháng 36: 199.050 ghi danh, 148.257 còn góp, số dư ≈2,43 nghìn tỷ, tiền lũy kế ≈ −53,7 tỷ;
  - PV/saver ≈ 219k / 365k / 416k / 694k;
  - cộng 7 tổ hợp, độ trùng của hai engine và các đầu vào suy ra.

**1.2 Review 2026** (`src/round3/reviews_2026.py`):
- Đọc tay 58 review tiêu cực 2026 (rating ≤2, `keep=1`, 01/01–21/09/2026), dùng 8 mã nguyên nhân.
- Ghi thêm phiên bản iOS và cờ "đăng ngày 4–5/3".
- Có 6 trích dẫn đã dịch sang tiếng Anh.
- Mã hóa nằm ở `data/round3/reviews_2026_coding.csv`.

**1.3 Data bổ sung:**
- `sources_round3.csv` (37 nguồn) và `rates_oct_2026.csv`.
- **Nguồn đã tự kiểm** (cột `checked_by_author = yes`):
  - lương ITviec; giá tin nhắn MobiFone/Zalo; phí VA của VPBank;
  - công bố sự cố DNSE ngày 4/3; lãi tiền gửi và trần lãi;
  - trang và FAQ Trứng Vàng; DSE125004; trái phiếu Agribank; BCTN 2025 tr.68; thông báo dừng Egg X 25/12/2023;
  - SSIBF; VCBF-FIF; giấy phép phân phối CCQ của DNSE;
  - TCBS Q2/2026; VNDIRECT Tích sản; KBSV;
  - bản tin Pinetree 4/3; VN-Index −115.
- Các nguồn agent tìm mà chưa tự kiểm được ghi rõ "agent only".

**1.4 KPI và ngưỡng:** `payday_decision_gates.csv` gồm Cổng 0–3 (mục 5.2).

**Vòng phản biện** (user yêu cầu "research, phản biện"; kết quả ở `review_phase1.md`). 13 vấn đề đã tìm và sửa, gồm:
- **Cổng tháng 6:** trước đây cho "scale" trong khi NPV âm. Đã thêm tiêu chí cấp chương trình và Cổng 0.
- **Biên Trứng Vàng:** hạ còn 0,6%, vì trái phiếu Agribank trả bình quân Big4 + 2,0 điểm (khoảng 7,9%), còn Trứng Vàng trả khách 6,2–7,6%.
- **Trứng Vàng:** đang có trái phiếu DNSE và từng bị dừng mở mới (2023).
- **Tier tiền:** tốn 41% doanh thu/saver.
- **Pilot:** 20.000 TK không đủ lực thống kê, tăng lên 45.000.
- **Kênh doanh nghiệp:** cần tỷ lệ tham gia ≥39%.
- **Stress test:** trước đây chưa có, đã thêm.
- **Lời lẽ:** dùng "no platform fee" thay cho "zero-fee"; không nói "lãi cao nhất".
- **Bỏ hai câu nói quá:** AMFI "thị trường giảm làm SIP dừng" (nguồn không nói vậy); chứng chỉ tiền gửi miễn thuế (sai).

**Quyết định D1–D7** (user chấp nhận khi yêu cầu làm Phase 2):
- **D1 Tier:** MVP chỉ có ưu đãi phi tiền mặt (chuỗi kỳ góp, bỏ qua 1 tháng/năm, nhắc ngày lương theo mục tiêu, ưu tiên Trứng Vàng mới); trần 50 triệu cho mọi ưu đãi lãi.
- **D2 Danh mục:** theo kỳ hạn mục tiêu (<1 năm: chỉ Trứng Vàng; 1–3 năm: thêm quỹ trái phiếu; ≥3 năm: cổ phiếu tối đa 40%).
- **D3 KPI:** TK mới ≥10 triệu ở tháng 24–36; bỏ mốc 85.000.
- **D4 Board:** chỉ Phase 0–1, 6,6 tỷ, pilot 45.000 TK, kèm 5 việc giao ngay.
- **D5 Định vị:** "không phải người đầu tiên, nhưng hợp nhất với tệp DNSE". Khác biệt còn lại: nhiều lớp tài sản trong một kế hoạch, và số đo minh bạch công bố.
- **D6 Business case:** trình bày như một quyền chọn có trần lỗ.
- **D7 Lõi trái phiếu:** chỉ trái phiếu ngân hàng; chấp nhận mất khoảng 4 tỷ trong 5 năm.

### 7.4 Phase 2: Thiết kế sản phẩm và kế hoạch triển khai — xong (16/10)

**2.1 Đặc tả** (`docs/doc_round3/payday_spec.md`):
- **3 persona dựng từ data:** P1 người đi làm có TK ngủ (khách ra mắt); P2 trader muốn có phần tích lũy; P3 người mở TK mới. Kênh doanh nghiệp (N1) làm sau.
- **Giá trị:** cho khách, DNSE, ngân hàng đối tác, công ty quỹ, cơ quan quản lý.
- **MVP F1–F11, và những gì cố ý loại:**
  - margin;
  - cổ phiếu đơn lẻ và phái sinh;
  - trái phiếu DNSE;
  - thưởng tiền;
  - ủy thác;
  - hạn mức tín dụng trên khoản tiết kiệm;
  - gói thành viên trả phí;
  - trích % lương (để Phase 3).
- **Gói giữ chân và danh mục theo kỳ hạn mục tiêu.**
- **7 cam kết minh bạch** kèm số đo công bố.
- **SLO:**
  - cổng ra mắt ≥99,5% kỳ góp ghi có trong cùng ngày làm việc;
  - ngân sách lỗi 0,5%;
  - hàng đợi tách khỏi bước kiểm sức mua;
  - khóa phát hành trước ngày cao điểm; phát hành theo đợt 5% → 25% → 100%;
  - trang trạng thái.
- **Pháp lý:** TT 121/2020 Điều 4, 24, 27; Luật CK 2019 Điều 72; TT 64/2024; QĐ 461/QĐ-XPHC; lịch sử Egg X; phân phối CCQ.

**2.2 Journey và wireframe** (dùng skill journey-mapping và ux-writing):
- `journey_map.csv`: 6 giai đoạn. Cảm xúc ghi là giả thuyết, sẽ kiểm bằng pilot.
- **Ba khoảnh khắc quyết định niềm tin:** tiền vào lần đầu, tiền ra lần đầu, lần đầu có sự cố.
- `wireframe_copy.json`: 6 màn hình chính (mục tiêu → khẩu vị rủi ro → kế hoạch → VA/lệnh định kỳ → kỳ góp đầu → mốc 90 ngày) và 4 trạng thái lỗi (chưa nhận tiền, lương về trễ, bỏ qua/tạm dừng, rút về ngân hàng).
- Vẽ thành 2 PNG low-fi. Team sẽ thay bằng Figma.

**2.3 Service blueprint** (`service_blueprint.csv` → `service_blueprint.png`):
- 6 bước × 8 làn: bằng chứng hữu hình, hành động khách, frontstage, backstage, hỗ trợ, điểm quyết định, xử lý lỗi, người chịu trách nhiệm.
- Có ba đường: tương tác, hiển thị, tương tác nội bộ.

**2.4 Kế hoạch triển khai** (`plan_tables.py` điền số của mô hình vào chữ tác giả soạn):
- GTM năm 1 theo quý; lộ trình 5 phase (0–4).
- RACI 10 việc × 8 vai; risk register 6 rủi ro chấm khả năng × tác động:
  - R1 lỗi ngày lương 20;
  - R2 ghi danh thấp 16;
  - R4 cơ quan quản lý và Trứng Vàng 15;
  - R3 điều khoản đối tác 12;
  - R5 thị trường giảm hoặc xung đột lợi ích 12;
  - R6 tiền chuyển sang giao dịch 9.
- Đề nghị với Board: 6,6 tỷ và 5 việc giao ngay.
- `plan_payday.md` §7–9 đã thay bằng số mô hình; bảng test F6 mới có 12 test (thêm test 8–12); §5.6 có ghi chú trỏ sang bảng cổng.

**Sửa trong lúc kiểm Phase 2** (các lỗi này đã có thể lên slide):
- **Lãi 7,10% trên wireframe:** đổi thành `[rate]%`, vì chưa có lãi của trái phiếu ngân hàng trong Payday.
- **Con số 45%:** là "crash, treo, lag", không phải "treo sau cập nhật" (nhóm đổ lỗi cho bản cập nhật chỉ 8,6%).
- **"5 phút như VCB Digibank":** không có nguồn. Giờ 5 phút chỉ là mục tiêu thiết kế.
- **Quy tắc tái tục:** Trứng Vàng mặc định tự tái tục (đã tự kiểm FAQ, S18). Payday đổi thành chỉ tái tục vào kỳ hạn vẫn đáo hạn trước ngày mục tiêu, báo trước 3 ngày, tắt bằng một chạm.
- **Vi phạm ký quỹ:** dẫn QĐ 461/QĐ-XPHC, không gọi là "kết luận thanh tra".
- **Trích review:** dẫn nguyên văn câu tiếng Việt, không diễn giải.
- **Thuật ngữ:** "nhóm đối chứng" ở chỗ thử tier sửa thành "nhánh thử nghiệm riêng".
- **Phương án cho vay ETF:** ghi rõ là không tính trong base, chỉ xét ở Cổng 3.
- **Kênh ZaloPay:** chuyển sang Phase 3, làm kênh nạp tiền thứ hai, không có trong mô hình.

**Kiểm tra cuối Phase 2:**
- `run_round3.py`: 35/35 test pass.
- `run_all.py --no-report`: 614 cells, 0 other differences; không file Round 2 nào thay đổi.

### 7.5 Phase 3: Nội dung slide và file Word — xong, chờ duyệt (17/10)

- **Checkpoint 3.1 (16/10):** user duyệt câu chuyện và 4 lựa chọn thông điệp. Tên thành viên và Figma: "để sau".
- **3.1 Nội dung:** `deck_content.md`, 15 slide theo khung của prompt; Executive Summary 142 từ; speaker notes khoảng 14 phút.
- **3.2 Hình:** 8 hình mới theo skill dataviz:
  - why now, funnel, sơ đồ giải pháp, bản đồ định vị, timeline GTM, lộ trình, cây quyết định, heat map rủi ro;
  - bảng màu đã chạy script kiểm của skill (LIGHT_RED bị loại vì tương phản 1,67:1);
  - không dùng hai trục y.
- **3.3 Bảng:**
  - mỗi bảng có CSV trong `outputs/round3/tables/`;
  - markdown ghi từ CSV bằng `deck_tables.py`; script kiểm báo lỗi nếu lệch.
- **3.4 Executive Summary:** đã chốt, nêu đủ vốn cần, kết quả kỳ vọng và đề nghị.
- **3.5 Appendix:** `deck_appendix.md`, 22 slide A–I; 47 references APA 7; kiểm chéo trích dẫn bằng code.
- **3.6 Word:**
  - `outputs/round3/Round3A_content_KTQT_FTUers.docx`: A4 ngang, 34 bảng, 18 hình, khoảng 72 trang;
  - đã xuất PDF bằng Word để soát hình thức.
- **Nguồn tự kiểm thêm:** S38–S44 (SSI eSIP, VPS Smart Indexing, VPBank Goal Jar, VCBF SIP, VinaSIP, SSI iBoard–Dragon Capital), S28 (tài liệu ĐHĐCĐ), S32 (thông báo dừng Egg X). Tổng 44 nguồn.
- **Sửa trong Phase 3:**
  - "Big Four" → Vietcombank, VietinBank, BIDV;
  - phí VCB SIP sửa thành "preferential redemption fee";
  - ngày VPBank Goal Jar chỉ ghi "September";
  - slide 10 ghi "20 rival products" (9 đã tự kiểm, 11 tra cứu tại bàn);
  - ký hiệu năm references đánh lại liền mạch.
- **Kiểm cuối:** `run_round3.py` chạy hết 9 bước; `run_all.py --no-report` 0 other differences.

### 7.5b Report bổ trợ EN + VI — xong (17/10)

User thấy deck "hơi tóm tắt" và yêu cầu một report hoàn chỉnh kiểu Round 2 cho mục tiêu Round 3A (thiết kế và phát triển sản phẩm), có bản tiếng Anh và tiếng Việt, **không để nộp**.
- File: `docs/doc_round3/report_round3A_{en,vi}.md`; `outputs/round3/Round3A_report_KTQT_FTUers_{EN,VI}.{docx,pdf}` (39 và 40 trang).
- Code: `build_report_docx.py` (mới); `deck_tables.py` thêm `vietnamese_tables`, `vi_quote_rows`, mẫu `report_value`, `report_features`; `check_deck_content.py` thêm `check_report`.
- Dữ liệu: `data/round3/deck_tables_vi/` gồm 3 từ điển dịch ô (`cells_vi_main/model/appendix.csv`, 695 mẫu) và `appF1_feedback.csv` (nguyên văn review, cắt bằng script từ file review gốc).
- Phát hiện khi viết: VCBF-FIF nắm trái phiếu DSE125018 = 6,97% NAV (S24), deck chưa nhắc; phí bán VCBF-FIF đã sửa đúng; 11/44 nguồn mới chỉ có agent kiểm. Chi tiết ở `round3_progress.md`, mục "Report bổ trợ".

### 7.6 Việc còn lại

| Phase | Việc | Đầu ra | Checkpoint |
|---|---|---|---|
| **3** | Xong. Còn chờ user và team duyệt file markdown và file Word | `deck_content.md`, `deck_appendix.md`, `Round3A_content_KTQT_FTUers.docx` | ⛳ sau file Word |
| **4** | Bảng đối chiếu số liệu; rà ràng buộc booklet (15 slide, ≤150 từ, không hyperlink, có dòng "Source:"); soát hình bằng design-critique | `outputs/round3/claims_check.csv`; Word cuối | ⛳ |
| **5** | 15–20 câu Q&A theo vai (CEO, CFO, CTO, Head of Product); 1 trang số liệu tiếng Việt cho 3B | `docs/doc_round3/qa_prep.md` | — |
| **6** | Chỉ khi user yêu cầu: dựng pptx bằng `src/round3/build_deck.py`; xuất PDF ≤10MB qua PowerPoint COM; tên `[FBAR3_2026]_KTQT FTUers.pdf` | pptx, pdf | — |

**Lịch** (prompt §10):
- 17/10: Phase 2 (đã xong sớm) và nháp `deck_content.md`.
- 18/10: hình và bảng hoàn chỉnh, Executive Summary, xuất Word, Phase 4.
- 19/10: Phase 6 nếu user yêu cầu; tập dượt lần 1.
- 20/10: soát lần cuối, PDF ≤10MB, tập dượt lần 2, **nộp trước 19:30**.

### 7.7 Câu hỏi đang treo
1. Tên thành viên cho slide giới thiệu.
2. Trong team có ai vẽ lại wireframe bằng Figma không. Nếu không, dùng bản PNG hiện tại kèm nhãn "low-fidelity".

---

## 8. File Round 3 chi tiết

### 8.1 Đầu vào — `data/round3/` (20 file + `deck_tables/`)

| File | Nội dung | Loại |
|---|---|---|
| `payday_assumptions.csv` | 60 tham số: `param, low, base, high, unit, type, source`. Có 3 sourced, 7 derived, 50 assumption. Ví dụ base: góp 1,0 triệu/tháng; ghi danh TK ngủ 2%; 25% TK ngủ đủ điều kiện; pilot 45.000; cơ cấu 45/35/10/10; biên Trứng Vàng 0,6%; đội xây dựng 3,18 tỷ + thuê ngoài 1,0 tỷ; vận hành 3,78 + 1,2 tỷ/năm; marketing 1,0 tỷ/năm; phí VA 3.300đ/kỳ | Đầu vào mô hình |
| `sources_round3.csv` | 44 nguồn web S01–S44: chủ đề, giá trị, ngày, URL, ngày truy cập, dùng cho, độ tin cậy, `checked_by_author` | Nguồn |
| `rates_oct_2026.csv` | Lãi tiền gửi, chứng chỉ tiền gửi, Trứng Vàng tháng 10/2026 (6 dòng, có mã nguồn) | Nguồn |
| `reviews_2026_coding.csv` | Mã nguyên nhân đọc tay cho 58 review: store, review_id, causes, primary, after_update, outage_4_5_march, gist_en, note | Tác giả mã hóa |
| `reviews_2026_quotes.csv` | 6 trích dẫn review đã dịch sang tiếng Anh | Tác giả dịch |
| `gtm_year1_plan.csv` | GTM 4 quý: mục tiêu, phân khúc, kênh, thông điệp, guardrail, cổng; có ô `{...}` | Tác giả soạn |
| `roadmap_plan.csv` | 5 phase (0–4): mục tiêu, sáng kiến, cổng | Tác giả soạn |
| `raci.csv` | 10 việc × 8 vai (CEO, CFO, CTO, Head of Product, Pháp chế, Marketing/CRM, CSKH, người có chứng chỉ) | Tác giả soạn |
| `risk_register.csv` | R1–R6: bằng chứng, khả năng, tác động, giảm thiểu, tín hiệu sớm, người chịu trách nhiệm | Tác giả soạn |
| `trust_metrics.csv` | 7 cam kết: khách thấy gì, số đo công bố, mục tiêu, tần suất, người chịu trách nhiệm | Tác giả soạn |
| `legal_map.csv` | 8 yêu cầu pháp lý: căn cứ, phản hồi thiết kế, trạng thái | Tác giả soạn |
| `glide_path.csv` | Danh mục theo kỳ hạn mục tiêu (4 dòng) | Tác giả soạn |
| `journey_map.csv` | 6 giai đoạn × 10 dòng: mục tiêu, hành động, touchpoint, suy nghĩ, cảm xúc, điểm đau có bằng chứng, phản hồi thiết kế, số đo, người chịu trách nhiệm, khoảnh khắc quyết định | Tác giả soạn |
| `service_blueprint.csv` | 8 làn × 6 bước | Tác giả soạn |
| `wireframe_copy.json` | Microcopy của 6 màn hình chính (S1–S6) và 4 màn hình lỗi (E1–E4). `[x]`, `[rate]`, `[date]` là ô app tự điền, không phải số liệu | Tác giả soạn |
| `why_now_events.csv` | 6 mốc của timeline slide 3 (ngày, nhãn, chi tiết, nhóm, mã nguồn) | Tác giả soạn |
| `competitors.csv` | Đối thủ cho bảng slide 10 và bản đồ định vị: tài sản, số loại tài sản, vé tối thiểu, ai quyết định, phí, mã nguồn | Tác giả soạn |
| `ecosystem_roadmap.csv` | 3 chặng hệ sinh thái DNSE (0–6, 6–12, 12–24 tháng) cho hình lộ trình | Tác giả soạn |
| `decision_tree.csv` | Nhánh scale / adjust / stop của Cổng 0–3, có ô `{...}` điền từ mô hình | Tác giả soạn |
| `solution_overview.json` | Chữ của sơ đồ giải pháp slide 7 (4 bước, gói giữ chân, trust controls) | Tác giả soạn |
| `deck_tables/` (18 CSV) | Mẫu bảng của deck: `slide01`, `04`, `05`, `06`, `08`, `09`, `11`–`15` và appendix `appA1`, `appA2`, `appC1`, `appF1`, `appI1`; thêm `report_value`, `report_features` cho report; số trong `{...}` lấy từ mô hình | Tác giả soạn |
| `deck_tables_vi/` (4 CSV) | `cells_vi_main.csv`, `cells_vi_model.csv`, `cells_vi_appendix.csv`: từ điển dịch từng ô bảng EN sang VI (`table,en,vi`, ⟦i⟧ = chỗ số); `appF1_feedback.csv`: bảng D1 bản VI với nguyên văn review | Tác giả soạn |

### 8.2 Code — `src/round3/` (11 script)

| Script | Việc | Đọc | Ghi |
|---|---|---|---|
| `run_round3.py` | Chạy 9 bước theo thứ tự, dừng khi một bước lỗi | — | — |
| `test_payday_model.py` | 35 kiểm tra mô hình trước khi dùng; thoát mã 1 nếu lỗi | `payday_assumptions.csv` | `payday_test_check.csv` |
| `payday_model.py` | Mô hình cohort và mọi phân tích. Hàm chính: `params`, `survival`, `saver_balance`, `channel_schedule`, `simulate`, `simulate_calendar`, `metrics`, `unit_economics`, `phase_budget`, `board_ask`, `tornado_rows`, `need_to_believe`, `levers`, `stress_tests`, `tier_breakeven`, `pilot_power`, `decision_gates`, `indirect_value` | `payday_assumptions.csv` | 16 bảng `payday_*.csv` |
| `plan_tables.py` | Điền ô `{...}` bằng số mô hình (`key_numbers`); gộp kết quả base theo quý (`gtm`) và theo phase (`roadmap`); Board ask; chấm điểm rủi ro (Cao ≥15, Trung bình ≥8) | 9 CSV tác giả soạn + mô hình | 10 bảng kế hoạch |
| `reviews_2026.py` | Ghép mã hóa tay với file review, kiểm mọi review đã được mã, tính tỷ lệ và khoảng Wilson 95% | `data/reviews_flagged_*` và `reviews_raw_ios_*` của DNSE (chỉ đọc); 2 CSV mã hóa | 6 bảng `reviews_2026_*.csv` |
| `figures_round3.py` | J-curve, tornado, số dư và TK ≥10 triệu, nguyên nhân review; why now, funnel, bản đồ định vị, timeline GTM, heat map rủi ro. 200 dpi, không đặt tiêu đề trong hình, màu DNSE | Bảng output | 9 PNG |
| `diagrams_round3.py` | Wireframe (class `Phone`, lưu 400 dpi), service blueprint, sơ đồ giải pháp, lộ trình, cây quyết định | `wireframe_copy.json`, `service_blueprint.csv`, `solution_overview.json`, bảng output | 6 PNG |
| `deck_tables.py` | Sinh CSV cho bảng của deck và appendix (mẫu trong `data/round3/deck_tables/` + output mô hình), dữ liệu cho hình, rồi ghi bảng vào `deck_content.md`, `deck_appendix.md` và 2 report giữa các marker `<!-- table: ... -->`; bản VI dịch từng ô qua `deck_tables_vi/` (ô thiếu bản dịch ghi ra `vi/untranslated.csv`) | Output mô hình, review, kế hoạch; mẫu bảng; từ điển dịch | 13 bảng slide, 23 bảng appendix/report, 7 bảng dữ liệu hình, 33 bảng VI |
| `check_deck_content.py` | Kiểm 2 file deck: số từ (title ≤15, chữ ≤60, Executive Summary ≤150), bảng ≤6×5, speaker notes khoảng 120 từ, có dòng "Source:", cụm từ cấm, bảng khớp CSV, trích dẫn khớp references | `deck_content.md`, `deck_appendix.md` | — |
| `build_content_docx.py` | Dựng file Word bằng python-docx: A4 ngang, mỗi slide một trang, bảng Word thật, hình nhúng, style riêng cho designer notes và speaker notes; kiểm lại số tiêu đề, bảng, hình | 2 file deck, hình | `Round3A_content_KTQT_FTUers.docx` |
| `build_report_docx.py` | Dựng report bổ trợ EN và VI: A4 dọc kiểu Round 2 (Times, header, số trang, mục lục), caption bảng/hình, references thụt đầu dòng treo, bảng phụ lục ≥7 cột ở trang ngang; kiểm số mục, bảng, hình, references; Word COM điền mục lục và xuất PDF (`--no-toc` để bỏ) | 2 report markdown, hình | `Round3A_report_KTQT_FTUers_{EN,VI}.{docx,pdf}` |

### 8.3 Bảng output — `outputs/round3/tables/` (75 file + `vi/` 34 file)

| Nhóm | File |
|---|---|
| Mô hình (16) | `payday_monthly_{low,base,high}.csv` (theo tháng); `payday_scenarios.csv` (tóm tắt 3 kịch bản); `payday_unit_economics.csv`; `payday_phase_budget.csv`; `payday_tornado.csv`; `payday_levers.csv`; `payday_need_to_believe.csv`; `payday_stress.csv`; `payday_tier_breakeven.csv`; `payday_pilot_power.csv`; `payday_decision_gates.csv`; `payday_option_lending.csv`; `payday_indirect_value.csv`; `payday_test_check.csv` |
| Review 2026 (6) | `reviews_2026_causes.csv` (từng review); `reviews_2026_cause_summary.csv`; `reviews_2026_keyword_vs_hand.csv`; `reviews_2026_by_month.csv`; `reviews_2026_ios_versions.csv`; `reviews_2026_quotes.csv` |
| Kế hoạch (10) | `gtm_year1.csv`; `roadmap_phases.csv`; `board_ask.csv`; `risk_register.csv`; `raci.csv`; `trust_metrics.csv`; `legal_map.csv`; `glide_path.csv`; `journey_map.csv`; `service_blueprint.csv` |
| Bảng slide (13) | `slide01_key_figures`, `slide04_insight_design`, `slide05_what_changed`, `slide06_personas`, `slide07_glide_path`, `slide08_moments_of_truth`, `slide09_failure_handling`, `slide10_competitors`, `slide11_scenarios`, `slide12_gtm`, `slide13_roadmap`, `slide14_gates`, `slide15_board_ask` |
| Dữ liệu hình (7) | `why_now_events`, `why_now_investor_cash`, `sizing_funnel`, `savers_by_channel`, `positioning_map`, `decision_tree`, `ecosystem_roadmap` |
| Appendix (21) | `appA1`–`appA2`, `appB1`–`appB9`, `appC1`, `appD1`–`appD3`, `appE1`, `appF1`, `appG2`–`appG3`, `appH1`, `appI1` |

### 8.4 Hình — `outputs/round3/figures/` (15 PNG)

| File | Nội dung | Dùng cho | Kích thước |
|---|---|---|---|
| `payday_jcurve.png` | Tiền lũy kế 60 tháng, 3 kịch bản | Slide 11 | 6 × 4,5 in, 200 dpi |
| `payday_tornado.png` | Độ nhạy của tiền tháng 60 | Slide 11 / appendix B | 6 × 4,5 in, 200 dpi |
| `payday_balance_accounts.png` | Số dư và số TK mới ≥10 triệu theo tháng | Slide 11 / 14 | 12 × 5,5 in, 200 dpi |
| `reviews_2026_causes.png` | Nguyên nhân review tiêu cực 2026 | Slide 4 / appendix D | 6 × 4,5 in, 200 dpi |
| `wireframes_journey.png` | 6 màn hình chính (low-fi) | Slide 8 | 12 × 5,5 in, 400 dpi |
| `wireframes_errors.png` | 4 trạng thái lỗi (low-fi) | Appendix G | 12 × 5,5 in, 400 dpi |
| `service_blueprint.png` | Service blueprint đầy đủ | Slide 9 / appendix G | 13,33 × 7,5 in, 200 dpi |
| `why_now_timeline.png` | Mốc 2026 của đối thủ, hạn Open API, tiền NĐT tại CTCK | Slide 3 | 12 × 3,6 in, 200 dpi |
| `sizing_funnel.png` | Từ 1,51 triệu TK đến saver TK ngủ; 31.133 saver theo kênh ở tháng 36 | Slide 6 | 6 × 4,5 in, 200 dpi |
| `solution_overview.png` | 4 bước của Payday, gói giữ chân, trust controls | Slide 7 | 12 × 3,7 in, 200 dpi |
| `positioning_map.png` | Vé tối thiểu theo số loại tài sản; chỉ sản phẩm đã kiểm | Slide 10 | 6 × 4,5 in, 200 dpi |
| `gtm_timeline.png` | Hoạt động năm 1, Cổng 0–2, funded savers theo tháng | Slide 12 | 12 × 3,6 in, 200 dpi |
| `roadmap.png` | 5 phase có cổng và kết quả, trên lộ trình hệ sinh thái DNSE | Slide 13 | 12 × 3,0 in, 200 dpi |
| `decision_tree.png` | Nhánh scale / adjust / stop ở Cổng 0–3 | Slide 14 | 12 × khoảng 3,6 in, 200 dpi |
| `risk_heatmap.png` | 6 rủi ro theo khả năng × tác động, kèm người chịu trách nhiệm | Slide 15 | 6 × 4,5 in, 200 dpi |

### 8.5 Cách sửa
- **Đổi giả định:** sửa `data/round3/payday_assumptions.csv`, rồi chạy `python src/round3/run_round3.py`. Mọi bảng, hình và chữ có ô `{...}` tự cập nhật.
- **Đổi chữ của kế hoạch:** sửa CSV trong `data/round3/`. Không sửa bảng trong `outputs/round3/`, vì sẽ bị ghi đè.
- **Đổi microcopy wireframe:** sửa `wireframe_copy.json`, rồi chạy `python src/round3/diagrams_round3.py`.
- **Thêm nguồn:** thêm dòng vào `sources_round3.csv`, có ngày truy cập và `checked_by_author`; nếu trích trên slide thì thêm mục APA vào cuối `deck_appendix.md` (script kiểm sẽ báo nếu thiếu).
- **Đổi bảng trên slide hoặc appendix:** sửa CSV mẫu trong `data/round3/deck_tables/` (hoặc dữ liệu gốc), rồi chạy lại. Không sửa bảng trong markdown.
- Số trong `payday_spec.md` và `plan_payday.md` là bản chép tay từ output. Đổi giả định thì phải rà lại hai file này.

---

## 9. Key files để sửa nếu cần cập nhật report Round 2

| Mục đích | File |
|---|---|
| Nội dung text report (Section 1–5, Exec Summary) | `src/report/content.py` |
| Build Word document | `src/report/build_report.py` |
| Số liệu kịch bản Payday Portfolio | `data/manual/scenario_assumptions.csv`, `scenario_baseline.csv` |
| Figures: charts | `src/figures/charts.py` |
| Figures: diagrams | `src/figures/diagrams.py` |
| Tables từ data | `src/tables/make_tables.py` |
| Segment model | `src/pipeline/04_segment_model.py` |
| Review cleaning | `src/pipeline/03_reviews_clean.py` |
| Quy tắc chủ đề review (TRUST, RELIABILITY) | `src/analysis.py` |

---

## 10. Trạng thái git

- **Branch:** `truc`. Nhánh chính là `master`.
- **Commit cuối:** `064bbc1` "round3" (16/10). Đã có docs tách thư mục, code và data Round 3 Phase 1, `review_phase1.md`.
- **Chưa commit:**
  - Sửa đổi: `payday_model.py`, `figures_round3.py`, `run_round3.py`, `payday_assumptions.csv`, `sources_round3.csv`, `payday_decision_gates.csv`, `plan_payday.md`, `round3_progress.md`, `agent.md`.
  - File mới của Phase 2: `payday_spec.md`; `plan_tables.py`; `diagrams_round3.py`; 10 CSV tác giả soạn và `wireframe_copy.json`; 10 bảng kế hoạch; 3 PNG.
  - File mới của Phase 3: `deck_content.md`, `deck_appendix.md`; `deck_tables.py`, `check_deck_content.py`, `build_content_docx.py`; 5 file dữ liệu hình và 16 mẫu bảng trong `data/round3/`; 41 bảng output mới; 8 PNG; file Word.
- Chỉ commit khi user yêu cầu.

---

## 11. Lưu ý kỹ thuật

- Python 3.10+ (tested 3.11). Chạy với venv: `D:\uni\FBA_dnse\.venv\` (`.venv/Scripts/python.exe`).
- Font Calibri/Carlito cho figures — nếu không có thì labels hơi lệch. Xem lỗi Calibri ở 200 dpi tại mục 4.2.
- LibreOffice optional: cần để tạo PDF và recompute page numbers (`--paginate`).
- `export_tables.py` đọc từ `report/FBAR2_2026_KTQT_FTUers.docx` — file này phải có.
- Pipeline Round 2 chạy ~16 giây (không tính PDF); Round 3 chạy ~10 giây.
- 3 known differences giữa submitted report và code output (tất cả là rounding, không ảnh hưởng text).
- Đọc PDF bằng pymupdf (`import pymupdf`; tên `fitz` đã cũ). Read tool không render PDF trên máy này.
- Shell: PowerShell là chính; Bash (Git Bash) cũng dùng được.

# Agent Map — FBA Season 6 Round 2: DNSE Securities

**Deadline:** 21:00 ngày 27/09/2026 | **Word cap:** 3 500 từ | **Ngôn ngữ báo cáo:** Tiếng Anh

---

## 1. File báo cáo cuối cùng

| File | Mô tả |
|---|---|
| [FBAR2_2026_DNSE_Analysis.docx](FBAR2_2026_DNSE_Analysis.docx) | **Báo cáo chính nộp thi.** Build bởi `06_build_report.js`; mọi số liệu đều đến từ pipeline, không gõ tay. |
| [FBAR2_2026_Team_name.docx](FBAR2_2026_Team_name.docx) | Bản nộp chính thức (đã điền tên team). |
| [FBA_Round2_DNSE_data_pack.xlsx](FBA_Round2_DNSE_data_pack.xlsx) | Workbook 18 tab đính kèm, build bởi `07_build_workbook.py`. |
| [doc/[FBA 6] QUESTION BOOKLET ROUND 2 (1).pdf](doc/[FBA%206]%20QUESTION%20BOOKLET%20ROUND%202%20(1).pdf) | Đề bài gốc. |

---

## 2. Pipeline lấy data (chạy theo thứ tự)

### 2a. Scripts lấy dữ liệu tài chính

| File | Input | Output | Ghi chú |
|---|---|---|---|
| [01_findex_fetch.py](01_findex_fetch.py) | World Bank API | [findex_raw.json](findex_raw.json) | Kiểm tra hằng số trong `findex_data.py` |
| [01b_dnse_financials_fetch.py](01b_dnse_financials_fetch.py) | Vietcap API | [dnse_financials.json](dnse_financials.json), [dnse_financials_raw.json](dnse_financials_raw.json), [dnse_financials_annual.csv](dnse_financials_annual.csv), [dnse_financials_quarterly.csv](dnse_financials_quarterly.csv) | BCTC DNSE Q1/2018–Q2/2026, đối chiếu KPMG |
| [01c_peer_financials_fetch.py](01c_peer_financials_fetch.py) | Vietcap API (44 mã) | [peer_financials.json](peer_financials.json) | Toàn bộ công ty chứng khoán trên Vietcap, có VPS (VCK) |
| [01d_market_macro_fetch.py](01d_market_macro_fetch.py) | HNX/HOSE notices, Vietcap, World Bank WDI, NSO | [market_macro.json](market_macro.json) | Thị phần môi giới, VN-Index, DSE giá, VSDC accounts |

### 2b. Scripts scrape app reviews

| File | Output | Ghi chú |
|---|---|---|
| [02a_playstore_scrape_browser.js](02a_playstore_scrape_browser.js) | CSV via clipboard | Chạy trong browser console |
| [02b_playstore_scrape_python.py](02b_playstore_scrape_python.py) | `reviews_raw_<package>.csv` | Standalone script |
| [02c_appstore_scrape.py](02c_appstore_scrape.py) | `reviews_raw_ios_<package>.csv`, [appstore_meta.json](appstore_meta.json) | App Store VN; chạy ~4 phút |

### 2c. Scripts xử lý & phân tích reviews

| File | Output | Ghi chú |
|---|---|---|
| [03_reviews_clean.py](03_reviews_clean.py) | `reviews_flagged_*.csv`, `reviews_summary_*.json` | Chuẩn hoá, lọc spam, tag theme |
| [03b_reviews_tables.py](03b_reviews_tables.py) | [reviews.py](reviews.py), [reviews_tables.json](reviews_tables.json) | Module dữ liệu; VPS cắt 1.200 đánh giá gần nhất |
| [04_segment_model.py](04_segment_model.py) | [segment_model.json](segment_model.json) | Hai Findex indices, xếp hạng phân khúc |

### 2d. Scripts vẽ biểu đồ

| File | Output (fig/) | Biểu đồ |
|---|---|---|
| [05a_charts_financial.py](05a_charts_financial.py) | `fig/fig2,7,8,9,11_*.png` | Peer profit, monetisation gap, revenue/margin |
| [05b_charts_evidence.py](05b_charts_evidence.py) | `fig/fig1,3,4,5,6,10_*.png` | Derivatives share, plan progress, Findex, segment model |
| [05c_charts_bctc.py](05c_charts_bctc.py) | `fig/bctc/bctc_1–14_*.png` | 14 biểu đồ dài hạn BCTC 2018–Q2/2026 |

### 2e. Scripts build output

| File | Output | Ghi chú |
|---|---|---|
| [06_build_report.js](06_build_report.js) | [FBAR2_2026_DNSE_Analysis.docx](FBAR2_2026_DNSE_Analysis.docx) | Đọc 5 JSON chính → Word; in word count phần thân |
| [07_build_workbook.py](07_build_workbook.py) | [FBA_Round2_DNSE_data_pack.xlsx](FBA_Round2_DNSE_data_pack.xlsx) | 18-tab workbook |
| [recalc.py](recalc.py) | _(cập nhật xlsx)_ | Cache formula values qua LibreOffice |

---

## 3. Data files chính

### JSON (nguồn sự thật cho pipeline)

| File | Nội dung |
|---|---|
| [dnse_financials.json](dnse_financials.json) | BCTC DNSE đã chuẩn hoá (KQKD, BCĐKT, LCTT, thuyết minh) |
| [peer_financials.json](peer_financials.json) | Tài chính 44 công ty chứng khoán, dùng để so sánh ngành |
| [market_macro.json](market_macro.json) | Thị phần môi giới, chỉ số, số tài khoản VSDC, macro WDI |
| [segment_model.json](segment_model.json) | Output xếp hạng phân khúc khách hàng |
| [reviews_tables.json](reviews_tables.json) | Dữ liệu review đã xử lý (dùng trong `06`) |
| [findex_raw.json](findex_raw.json) | Dữ liệu World Bank Findex gốc |

### CSV

| File | Nội dung |
|---|---|
| [dnse_financials_quarterly.csv](dnse_financials_quarterly.csv) | BCTC DNSE theo quý |
| [dnse_financials_annual.csv](dnse_financials_annual.csv) | BCTC DNSE theo năm |
| `reviews_raw_*.csv` (6 file) | Review thô từ Play Store và App Store |
| `reviews_flagged_*.csv` (6 file) | Review đã lọc spam, gán nhãn |

### Modules Python (data hard-coded)

| File | Nội dung |
|---|---|
| [brokers.py](brokers.py) | Danh sách broker, mapping tên và ticker |
| [findex_data.py](findex_data.py) | Hằng số Findex đã kiểm tra với `01_findex_fetch.py` |
| [reviews.py](reviews.py) | Module dữ liệu review (auto-generated bởi `03b`) |

---

## 4. Tài liệu phân tích & ghi chú làm việc

| File | Nội dung | Trạng thái |
|---|---|---|
| [doc/dnse_problems_and_product_strategy.md](doc/dnse_problems_and_product_strategy.md) | **Tài liệu phân tích chính:** các vấn đề P1–P4 của DNSE, insights, chiến lược sản phẩm. Nguồn dữ liệu tổng hợp đầy đủ. | Cập nhật 25/09/2026 |
| [bctc_analysis.md](bctc_analysis.md) | Phân tích chuyên sâu BCTC 2018–Q2/2026: đối chiếu báo chí vs. BCTC (27/36 khớp), lợi nhuận lõi, môi giới lỗ 16 quý, cấu trúc tài sản. | Cập nhật 25/09/2026 |
| [doc/final_report_review.md](doc/final_report_review.md) | Review bản nháp báo cáo cuối. | — |
| [weakness.md](weakness.md) | Danh sách điểm yếu và rủi ro cần xử lý. | — |
| [diary.md](diary.md) | Nhật ký làm việc theo ngày. | — |
| [doc/code_audit.md](doc/code_audit.md) | Audit code pipeline. | — |
| [doc/dnse.md](doc/dnse.md) | Ghi chú nhanh về DNSE. | — |
| [README.md](README.md) | Hướng dẫn run order toàn bộ pipeline. | — |

---

## 5. Biểu đồ (fig/)

| Nhóm | Files | Mô tả |
|---|---|---|
| Báo cáo chính (fig1–fig11) | `fig/fig1_derivatives_share.png` … `fig/fig11_peer_profit.png` | 11 biểu đồ chính trong báo cáo; `figA1` phụ lục |
| BCTC dài hạn (bctc_1–14) | `fig/bctc/bctc_1_revenue_profit.png` … `fig/bctc/bctc_14_dse_vs_vnindex.png` | 14 biểu đồ phân tích BCTC 2018–2026 |

---

## 6. Luồng dữ liệu tóm tắt

```
APIs (Vietcap, World Bank, HNX/HOSE, App Store, Play Store)
    │
    ▼
01b / 01c / 01d / 02b / 02c  →  JSON/CSV thô
    │
    ▼
03b / 04  →  reviews_tables.json, segment_model.json
    │
    ├──→ 05a / 05b / 05c  →  fig/*.png  (biểu đồ)
    │
    └──→ 06_build_report.js  →  FBAR2_2026_DNSE_Analysis.docx  ← BÁO CÁO CUỐI
         07_build_workbook.py →  FBA_Round2_DNSE_data_pack.xlsx ← DATA PACK
```

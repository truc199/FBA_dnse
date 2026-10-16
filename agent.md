# Agent Context — FBA Season 6 DNSE Workspace

*Cập nhật: 14/10/2026 (lần 2 — đã đọc được nội dung Round 3 đầy đủ). Đọc file này trước mọi phiên làm việc.*

---

## 1. Tổng quan dự án

**Cuộc thi:** Future Business Analyst Season 6 (RMIT BFC Hanoi)  
**Team:** KTQT FTUers  
**Công ty phân tích:** DNSE Securities Joint Stock Company (HOSE: DSE)  
**Round 2:** Đã nộp ngày 27/09/2026. Bản nộp cuối: `report/FBAR2_2026_KTQT_FTUers.pdf` + `.docx`.  
**Round 3:** Gala Night, deadline nộp 3A 21:00 20/10/2026 — xem mục 6 bên dưới.

### Luận điểm trung tâm (Round 2)
> DNSE mở tài khoản ở quy mô lớn (1 trong 5 tài khoản mới toàn thị trường) nhưng hầu hết không được nạp tiền: tháng 12/2025 chỉ 1,8% trong 1,51 triệu tài khoản có NAV ≥ 10 triệu VND. Giải pháp đề xuất là **Payday Portfolio** — kế hoạch tích sản dựa trên mục tiêu, tự động chuyển một phần lương vào danh mục đa dạng vào ngày nhận lương.

**Ba nguyên nhân gốc trong bản nộp (Figure 10):**
1. Lệch vốn khách hàng: công cụ zero-fee hút trader trẻ ít vốn (*giả thuyết*; bằng chứng chính là Gen Z chiếm 31,5% TK).
2. Niềm tin gãy ở lần nạp đầu và khi rút (*có bằng chứng review*): trust complaints chiếm 37% review tiêu cực từ 2025 (VPS 8%); thưởng 100k phải nạp 2 triệu; phí đóng TK 100.000đ.
3. Không có đường từ ý định đến nạp tiền đều (*có bằng chứng về sản phẩm, còn là giả thuyết về khách*).

**Payday trong bản nộp:** Ensa đề xuất 1 trong 3 danh mục mẫu (trong dịch vụ tư vấn có giấy phép), khách xác nhận; lệnh chuyển tiền định kỳ vào VA mang tên khách; rót vào lớp tài sản đang thiếu tỷ trọng nhất; tier cam kết 3/6/12 kỳ; trust controls. KPI: 85.000 TK ≥10 triệu sau 18 tháng.

> **Lưu ý:** `docs/v5_revision_discussion_recommendation.md`, `weakness.md` và `final_report_review.md` mô tả **bản nháp**, không phải bản nộp. Bản nháp có Table B15/B17 và 3 nguyên nhân "đo được"; bản nộp dùng Table F5/F6. Đối chiếu với PDF trước khi trích.

---

## 2. Cấu trúc workspace

```
D:\uni\FBA_dnse\
├── README.md                    mô tả chi tiết repo (luôn đọc khi cần biết file ở đâu)
├── requirements.txt             numpy, matplotlib, pillow, python-docx, lxml, pypdf
├── run_all.py                   chạy toàn bộ pipeline (xem mục 4)
├── agent.md                     file này
├── report/
│   ├── FBAR2_2026_KTQT_FTUers.pdf     bản nộp cuối (PDF)
│   └── FBAR2_2026_KTQT_FTUers.docx   bản nộp cuối (Word) — nguồn cho export_tables.py
├── data/
│   ├── manual/                  8 CSV tay-collected (accounts, scenarios, roadmap, v.v.)
│   ├── findex_raw.json          World Bank Findex Vietnam (19,878 bản ghi)
│   ├── dnse_financials*.{json,csv}    BCTC DNSE 34 quý qua Vietcap
│   ├── peer_financials.json     BCTC 44 công ty chứng khoán
│   ├── market_macro.json        thị phần HOSE/HNX, số TK VSDC, World Bank WDI
│   ├── reviews_raw_*.csv        Google Play reviews DNSE/VPS/FPTS (6 file)
│   ├── reviews_flagged_*.csv    reviews đã gắn tag spam + chủ đề
│   ├── reviews_tables.json      bảng review dùng trong report
│   ├── appstore_meta.json       App Store star counts
│   └── segment_model.json       Findex segment indices + xếp hạng
├── src/
│   ├── config.py                paths và DNSE colour palette
│   ├── analysis.py              tính toán dùng chung (scenarios, segment_ranks)
│   ├── pipeline/                thu thập & làm sạch data (01–04)
│   ├── figures/                 vẽ chart (charts.py) và diagram (diagrams.py)
│   ├── tables/                  export, tính lại, kiểm tra bảng
│   └── report/                  dựng lại Word document
├── outputs/
│   ├── figures/                 30 hình PNG của report
│   ├── tables/                  24 bảng CSV + check_tables.md
│   └── report/                  bản được dựng lại bởi code (KHÔNG được commit)
└── docs/                        ghi chú làm việc nội bộ (xem mục 3)
```

---

## 3. Tài liệu nội bộ quan trọng (`docs/`)

> **Cấu trúc từ 16/10/2026:** tài liệu Round 2 nằm trong `docs/doc_round2/` (diary, dnse, code_audit, bctc_analysis, final_report_review, weakness, v5_…, compass_…, check_legit_table_figure, dnse_problems_and_product_strategy). Tài liệu Round 3 nằm trong `docs/doc_round3/` (booklet .md, review_round2, review_payday, plan_payday, plan_tech, round3_core_tech_risk, competitor_features). File PDF booklet bị hỏng đã được bỏ.

| File | Nội dung |
|---|---|
| `diary.md` | Nhật ký toàn bộ Round 2: các phiên làm việc, lỗi phát hiện, hành động đã làm |
| `dnse.md` | Phân tích chi tiết data pack Excel + docx Round 2 (Phần 1 & 2) |
| `code_audit.md` | Audit 12 file code: lỗi A1–E8, trạng thái sửa từng mục |
| `bctc_analysis.md` | Đối chiếu báo chí vs BCTC DNSE 2018–2026, 10 insight chính |
| `final_report_review.md` | Chấm điểm theo rubric Round 2 (~84–85/100 ước tính) |
| `weakness.md` | 5 lỗ hổng chiến lược + phương án phản biện cho Round 3 |
| `v5_revision_discussion_recommendation.md` | Text cuối cho các mục 3.1–5, Exec Summary, Appendix B (bản nộp thực tế) |
| `[FBA 6] QUESTION BOOKLET ROUND 3.pdf` | **File PDF gốc bị hỏng ~68% dữ liệu** (byte nhị phân bị thay bằng ký tự thay thế Unicode U+FFFD ở đâu đó trước khi vào repo — không phải lỗi thiếu công cụ, đã xác nhận bằng pikepdf/pypdf/PyMuPDF). Không dùng được, không sửa được. |
| `[FBA 6] QUESTION BOOKLET ROUND 3.md` | **Bản thay thế do user tự convert, đọc được đầy đủ.** Đây là nguồn chính thức cho nội dung Round 3 — xem mục 6. |
| `review_round2.md` | **(15/10)** Review bản nộp Round 2: logic, khuyến nghị, code, data. Phát hiện chính: mô hình kịch bản tĩnh; năm 2026 complaint chuyển sang reliability; bảng cạnh tranh đã cũ (VPS Smart Indexing, SSI eSIP) |
| `review_payday.md` | **(15/10)** Đánh giá phản biện Payday: độ hữu dụng, mức phù hợp với người dùng trading, mức khác biệt so với đối thủ, 10 câu Q&A |
| `plan_payday.md` | **(15/10)** Kế hoạch Round 3A: outline 15 slide, data cần thu, cách đặt target, business case (J-curve minh họa), GTM, roadmap, lịch 5 ngày |
| `plan_tech.md` | **(15/10)** Chiến lược cho các sản phẩm hiện có: Entrade X, Margin X, Không Ngủ, Trứng Vàng, Ensa, Future X, Lightspeed, ZaloPay |
| `round3_core_tech_risk.md` | (14/10) Rủi ro công nghệ lõi của Payday; đã đính chính ngày 15/10 |
| `PROMPT_round3A_build.md` | **(16/10)** Prompt cho phiên mới: hoàn thiện nội dung Round 3A (chữ, bảng, biểu đồ) thành `deck_content.md`, rồi xuất Word. Thiết kế slide để sau (Phase 6, chỉ làm khi user yêu cầu). Gồm file cần đọc, skill, 5 quyết định, số liệu đã kiểm, workflow có checkpoint |
| `competitor_features.md` | **(16/10)** Tra cứu tại bàn 14 sản phẩm đối thủ (thay cho chụp màn hình) + khai thác review làm "feedback" (thay cho survey). Phát hiện: chuyển tiền định kỳ từ ngân hàng đã là chuẩn (VinaSIP 2021, VCB Digibank SIP từ 100.000đ); VSI cần 50 triệu + 10 triệu/tháng, phí 0,5%/năm; cuộc đua tích lũy 2026 (SSI 23/04, VSI 11/08, VPBank Hũ Mục Tiêu 12/09) |

---

## 4. Chạy pipeline

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

---

## 5. Số liệu then chốt (để tra nhanh)

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
| Trust/reliability trong review tiêu cực năm 2026 | Play 14,7% / 58,8%; iOS 12,5% / 75,0% | `reviews_flagged_*.csv` (tính 15/10) |
| Tiền KH trên nền tảng | 1.961 tỷ (Q2/2026) | BCTC ngoại bảng |
| Lợi suất cho vay | ~11%/năm | tính từ BCTC |
| Mục tiêu 2026 (ĐHCĐ) | DT 1.736 tỷ, LNTT 550 tỷ | ĐHCĐ 2026 |
| Hoàn thành kế hoạch H1/2026 | 48,9% DT, 20,6% LNTT | Tính từ BCTC |
| Mảng môi giới | Lỗ 16 quý liên tiếp từ Q3/2022, lũy kế −190 tỷ | BCTC |
| Phân khúc ưu tiên (Findex) | Secondary+ (20,4tr), In LF (19,0tr), Richest 60% (15,3tr) | `segment_model.json` |

---

## 6. Công việc tiếp theo — Round 3

> Nguồn: `docs/[FBA 6] QUESTION BOOKLET ROUND 3.md` (convert tay từ PDF gốc bị hỏng, đọc ngày 14/10/2026).

### Cấu trúc tổng thể: Gala Night = 2 phần

| Phần | Nội dung | Trọng số | Ngôn ngữ |
|---|---|---|---|
| **Round 3A** | Product Owner Solution — thuyết trình | **60%** điểm chung kết | **Tiếng Anh** |
| **Round 3B** | The Grand Debate — tranh biện trực tiếp | **40%** điểm chung kết | **Tiếng Việt** |

**Deadline nộp Round 3A: 21:00, 20/10/2026.**

---

### Round 3A — Product Owner Solution

**Vai trò giả định:** Product Owner / Business Solution Team trình bày trước "Board of Management" (CEO, CFO, CTO, Head of Product — do giám khảo đóng).

**Nhiệm vụ (task description):**
1. Thiết kế chi tiết một sản phẩm/tính năng/dịch vụ/cải tiến vận hành/customer experience initiative/chiến dịch marketing hoặc hướng tiếp cận phù hợp khác — **dựa trên tổ chức và kết quả của Round 2** (tức là DNSE + Payday Portfolio).
2. Lập **kế hoạch chiến lược** cho phát triển, ra mắt và mở rộng thị trường.
3. Xây **go-to-market plan chi tiết cho năm đầu ra mắt** (phần này Round 2 CHƯA có — cần làm mới).
4. Trình bày business case có số liệu để "Board" phê duyệt.

**6 nội dung tối thiểu bắt buộc (minimum requirements):**
1. **Problem Recap** — tóm tắt insight chính của Round 2 + vì sao vấn đề quan trọng chiến lược (dùng balance gap, 1,8% NAV ≥ 10tr từ Round 2).
2. **Proposed Solution** — target users/stakeholders, cơ chế lõi, tính năng chính, value proposition (bản nộp: mục 4.1–4.2, Figure 12, Table E3, F3).
3. **Insight-to-Solution Linkage** — trình bày rõ chuỗi **Round 2 Insight → Design Decision → Expected Business Impact** (bản nộp có sẵn Table 1 "problem statement and response" và Table F4 "concerns → design → proof").
4. **Solution Demonstration** — dùng wireframe/prototype, customer journey, process flow, service blueprint, campaign mechanism, hoặc before-and-after model (có thể làm lại từ Figure 7 "How Payday Portfolio works", nhưng cần nâng cấp lên mức demo cụ thể hơn, không chỉ sơ đồ khái niệm).
5. **Implementation & Validation** — target group, scope, resources, KPI, assumptions, risks, mitigation, và tiêu chí continue/scale/adjust/stop (bản nộp: Table F6, 7 giả định và ngưỡng; Figure F2 lộ trình. Tái sử dụng được nhưng phải sửa ngưỡng, xem `plan_payday.md` §5).
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

→ **"Implementation, validation and risk management" nặng nhất (30/100)** — đầu tư kỹ phần KPI/test/ngưỡng quyết định, tái dùng cấu trúc Table F6 đã có.

---

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

---

### Việc cần làm ngay cho team

1. **Chốt sản phẩm cho 3A.** Payday Portfolio là ứng viên tự nhiên (đã có insight-linkage, cơ chế, Table 1, F3–F6, G1 từ Round 2) nhưng còn thiếu (chi tiết trong `plan_payday.md`):
   - Go-to-market plan năm đầu ra mắt (hoàn toàn mới so với Round 2)
   - Strategic roadmap rõ phase/objective/initiative/KPI
   - Demo ở mức cụ thể hơn Figure 7 hiện tại (wireframe/service blueprint/customer journey thật, không chỉ sơ đồ khái niệm)
   - Slide Executive Summary ≤150 từ, font 14–15
2. **Biến `docs/weakness.md` (5 lỗ hổng chiến lược) thành câu trả lời Q&A sẵn sàng** — trực tiếp phục vụ tiêu chí "Presentation and Q&A" (10đ) và củng cố "Implementation, validation and risk management" (30đ).
3. **Table F6 (7 giả định kiểm chứng) đã có sẵn từ Round 2 — dùng làm xương sống cho mục "Implementation & Validation" của 3A**, nhưng phải sửa: ngưỡng "15% ghi danh trong 60 ngày" cao gấp khoảng 20 lần benchmark Không Ngủ; thêm test rò rỉ sang trading và trần CAC (`plan_payday.md` §5, §9).
4. **Chuẩn bị riêng cho 3B — đây là phần hoàn toàn mới**, tiếng Việt, không giới hạn trong DNSE mà là toàn ngành banking/fintech VN. Nên ôn lại bối cảnh vĩ mô rộng (Thông tư 64/2024 Open API, sandbox fintech Decree 94/2025, CASA, biometric/Decision 2345...) và luyện phản xạ tranh biện nhanh, có trích dẫn số liệu miệng.
5. **Thời hạn:** chỉ còn ~6 ngày kể từ 14/10/2026 đến deadline nộp 3A (20/10/2026, 21:00).

### Kết quả kịch bản cơ sở Payday Portfolio (Table F5 của bản nộp; **mô hình tĩnh, phóng đại 2–3 lần**, xem `review_round2.md` R2)
- 150.000 savers × 1,5 triệu/tháng × 70% giữ lại × 18 tháng = **2,84 nghìn tỷ tài sản**
- Tài khoản có NAV ≥ 10tr: từ 1,8% → 10,4% (trong 1,7 triệu TK)
- Phí: ~23 tỷ/năm (fee yield 0,8%)
- Phase 2 (cho vay): thêm ~21 tỷ lãi ròng

### Metric đo lường (headline KPI, dùng cho cả Round 2 và 3A)
> **"Tỷ lệ tài khoản có NAV ≥ 10 triệu VND"** — DNSE đã tự công bố chỉ tiêu này. Từ 1,8% (12/2025) → mục tiêu 5% trong 18 tháng.

### Liên hệ BTC
Truong Quynh Anh (Head Organizer) 0903207784 · Thai Gia Han (Head of External Affairs) 0963907058 · Do Gia Khanh 0969073368 · bfclub.hn@rmit.edu.vn

---

## 7. Key files để sửa nếu cần cập nhật report

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

---

## 8. Trạng thái git

Branch: `master`. Uncommitted: `data/reviews.py`, 3 review summary JSON, `segment_model.json`, 30 figures PNG — tất cả là kết quả của pipeline đã chạy lại, nội dung hợp lệ.

**Commit cuối:** `262b631` — "Clean root project structure"

---

## 9. Lưu ý kỹ thuật

- Python 3.10+ (tested 3.11). Chạy với venv: `D:\uni\FBA_dnse\.venv\`
- Font Calibri/Carlito cho figures — nếu không có thì labels hơi lệch
- LibreOffice optional: cần để tạo PDF và recompute page numbers (`--paginate`)
- `export_tables.py` đọc từ `report/FBAR2_2026_KTQT_FTUers.docx` — file này phải có
- Pipeline hoàn chỉnh chạy ~16 giây (không tính PDF)
- 3 known differences giữa submitted report và code output (tất cả là rounding, không ảnh hưởng text)

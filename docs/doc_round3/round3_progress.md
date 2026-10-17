# Tiến độ Round 3A (Payday Portfolio)

*File này để phiên sau tiếp tục được. Cập nhật sau mỗi phase. Prompt gốc: `docs/doc_round3/PROMPT_round3A_build.md`.*

**Trạng thái (17/10/2026):**
- Phase 0, 1, 2 xong. Phase 3: nội dung 15 slide, appendix A–I, references và file Word đã xong.
- Thêm (theo yêu cầu user, không nằm trong prompt gốc): **report bổ trợ đầy đủ kiểu Round 2, bản EN và VI, không dùng để nộp**. Xem mục "Report bổ trợ" bên dưới.
- **Đang ở ⛳ checkpoint sau bước 3.6:** chờ user và team duyệt `deck_content.md`, `deck_appendix.md`, `outputs/round3/Round3A_content_KTQT_FTUers.docx` và hai report.
- Việc tiếp theo sau khi duyệt: Phase 4 (kiểm tra nội dung).

---

## Phase 0: Khởi động — xong
- Đã đọc đủ các file ở mục 4 của prompt, kể cả report Round 2 (trích text bằng pymupdf).
- `python run_all.py --no-report` chạy được; `check_tables.md` ghi **0 other differences**. Đã kiểm lại sau Phase 2: 614 ô, 3 khác biệt đã biết, 0 khác biệt khác.

## Phase 1: Sửa nền phân tích — xong, đã qua một vòng phản biện

**Chạy lại toàn bộ Round 3 bằng một lệnh:** `python src/round3/run_round3.py` (khoảng 10 giây):
test (35/35) → mô hình → bảng kế hoạch → review → hình → wireframe và blueprint. Không sửa file Round 2.

### File chính
- Đầu vào: `data/round3/payday_assumptions.csv`, 60 tham số.
  - Cột `low` = kịch bản xấu, `high` = kịch bản tốt.
  - Cột `type`: sourced / derived / assumption.
  - Cột `source` ghi nguồn hoặc cách tính.
- Nguồn: `data/round3/sources_round3.csv`, 37 nguồn kèm ngày truy cập. Cột `checked_by_author` cho biết tôi đã tự mở kiểm hay chỉ agent tìm. S18 (FAQ Trứng Vàng) đã tự kiểm ngày 16/10.
- Lãi suất 10/2026: `data/round3/rates_oct_2026.csv`.
- Code trong `src/round3/`:
  - `payday_model.py`: hai engine. Engine theo cohort; engine theo lịch thời gian dùng cho stress test, cho kết quả trùng khớp engine cohort khi không có cú sốc.
  - `test_payday_model.py`, `reviews_2026.py`, `figures_round3.py`, `plan_tables.py`, `diagrams_round3.py`, `run_round3.py`.
- Bảng output (`outputs/round3/tables/`):
  - `payday_monthly_{low,base,high}.csv`, `payday_scenarios.csv`, `payday_unit_economics.csv`;
  - `payday_phase_budget.csv`, `payday_tornado.csv`, `payday_levers.csv`, `payday_need_to_believe.csv`;
  - `payday_stress.csv`, `payday_tier_breakeven.csv`, `payday_pilot_power.csv`;
  - `payday_decision_gates.csv`, `payday_option_lending.csv`, `payday_indirect_value.csv`, `payday_test_check.csv`;
  - `reviews_2026_*.csv` (6 file).
- Hình (`outputs/round3/figures/`): `payday_jcurve.png`, `payday_tornado.png`, `payday_balance_accounts.png`, `reviews_2026_causes.png`.

### Kết quả mô hình (sau phản biện)

| | Downside | **Base** | Upside |
|---|---:|---:|---:|
| Lợi suất ròng trên số dư | 0,25% | 0,44% | 0,68% |
| Vốn Phase 0–1, kèm dự phòng 15% | 8,7 tỷ | **6,6 tỷ** (5,7 + dự phòng) | 4,8 tỷ |
| TK mới ≥10 triệu, tháng 18 / 24 / 36 | 92 / 1.140 / 2.911 | 2.168 / 7.714 / **14.871** | 17.423 / 34.780 / 51.445 |
| Số dư tháng 36 | 71 tỷ | 352 tỷ | 1.597 tỷ |
| Tháng hòa vốn / hoàn vốn | không / không | **không / không** | 24 / 44 |
| NPV 60 tháng (12%) | −35,1 tỷ | −25,0 tỷ | +11,0 tỷ |
| Chi phí ròng/TK mới ≥10 triệu, tháng 60 | 10,0 triệu | **1,29 triệu** | 0 |

- Unit economics (base):
  - trần CAC 60 tháng 127.512đ, so với CAC kênh TK ngủ 65.000đ;
  - tỷ lệ ghi danh hòa vốn 1,02%;
  - cần 11 kỳ liền để vượt 10 triệu.
- Phí VA: miễn phí thì trần CAC là 198.876đ; trên 6.191đ/kỳ thì TK ngủ không còn đáng tiếp cận.
- Stress test (TK ≥10 triệu tháng 36): thị trường giảm năm 2 → −12%; ngày lương lỗi tháng 9 → −8%; cả hai → −18,5%. Tiền tháng 60 chỉ đổi −0,2 đến −0,5 tỷ, tức rủi ro chính là KPI và uy tín.

### Các sửa đổi chính sau phản biện (chi tiết trong `review_phase1.md` §1)
1. Cổng quyết định có tiêu chí cấp chương trình: chi phí ròng/TK mới ≥10 triệu. Thêm Cổng 0 ở tháng 3 cho điều khoản đối tác, phí VA và shadow run.
2. Biên Trứng Vàng hạ còn 0,6%. Lý do: trái phiếu Agribank trả bình quân Big4 + 2,0 điểm, khoảng 7,9%, còn Trứng Vàng trả 6,2–7,6%.
3. Trứng Vàng đang dùng cả trái phiếu DNSE (BCTN 2025), và từng bị dừng mở mới theo yêu cầu cơ quan quản lý (12/2023).
4. Tier bằng tiền tốn 41% doanh thu. MVP chuyển sang ưu đãi phi tiền mặt; tier tiền mặt chỉ còn là phương án thử.
5. Pilot tăng từ 20.000 lên 45.000 TK cho đủ lực thống kê.
6. Kênh chủ lao động cần tỷ lệ tham gia ≥39%.
7. Thêm stress test.
8. Sửa lời: "no platform fee" thay cho "zero-fee"; không nói "lãi cao nhất".

### Quyết định (đã được chấp nhận khi user yêu cầu làm Phase 2; chi tiết trong `review_phase1.md` §2)
- **D1 Tier:**
  - MVP chỉ có ưu đãi phi tiền mặt: chuỗi kỳ góp, bỏ qua 1 tháng/năm, nhắc ngày lương theo mục tiêu, ưu tiên Trứng Vàng mới.
  - Ưu đãi phí, nếu có, do công ty quỹ tài trợ.
  - Tier tiền mặt chỉ bật khi đã miễn phí VA và đo được +8,8 điểm ở tỷ lệ đạt 12 kỳ.
  - Trần 50 triệu cho mọi ưu đãi lãi.
- **D2 Danh mục:** theo kỳ hạn mục tiêu (<1 năm: chỉ Trứng Vàng kỳ ngắn; 1–3 năm: thêm quỹ trái phiếu; ≥3 năm: tối đa 40% cổ phiếu). Không xếp sản phẩm có phí rút trước hạn rơi vào trong kỳ hạn mục tiêu.
- **D3 KPI:** TK ≥10 triệu ở tháng 24–36; mục tiêu base +7.700 (tháng 24) và +14.900 (tháng 36). Thêm tiền mới ròng và chi phí ròng/TK. Bỏ mốc 85.000.
- **D4 Board:** chỉ Phase 0–1, 6,6 tỷ, pilot 45.000 TK, kèm 5 việc giao ngay (trong đó có ngân sách khoảng 1,3 triệu/TK có tiền).
- **D5 Định vị:** "không phải người đầu tiên, nhưng hợp nhất với tệp DNSE". Bỏ "the only". Khác biệt còn lại: trái phiếu ngân hàng + quỹ + ETF trong một kế hoạch, và số đo minh bạch công bố. Thêm VNDIRECT Tích sản và TCBS TCWealth vào bảng đối thủ.
- **D6 Business case:** trình bày như một quyền chọn có trần lỗ, kèm ngân sách cho mỗi TK có tiền.
- **D7 Lõi trái phiếu:** chỉ trái phiếu do ngân hàng phát hành; chấp nhận mất khoảng 4 tỷ trong 5 năm.

### 1.2 Review 2026 (không đổi sau phản biện)
- 58 review đọc tay (cả hai store): 83% mô tả một thứ bị hỏng (95% CI 71–90%); trust 19% (CI 11–31%).
- **So sánh với 2025 phải dùng cùng một quy tắc.** Áp quy tắc từ khóa của Round 2 lên Google Play:
  - chủ đề trust chiếm 54,8% review tiêu cực H1/2025 (34/62);
  - 24,1% ở H2/2025 (7/29);
  - 14,7% ở 2026 (5/34).
- Không so 19% (đọc tay) với 55% (từ khóa).
- DNSE đã công bố sự cố ngày 4/3/2026, 13:22–15:20. Có 9 review đăng ngày 4–5/3.

## Phase 2: Sản phẩm, hành trình và kế hoạch triển khai — xong

**File chính: `docs/doc_round3/payday_spec.md`** (tiếng Việt; câu đưa lên slide viết tiếng Anh). Gồm:
- 3 persona dựng từ data;
- giá trị cho khách, DNSE, ngân hàng, công ty quỹ, cơ quan quản lý;
- MVP F1–F11 và danh sách cố ý loại;
- gói giữ chân và danh mục theo kỳ hạn mục tiêu;
- 7 cam kết minh bạch kèm số đo công bố;
- SLO reliability; bảng pháp lý;
- journey 6 giai đoạn; wireframe và microcopy; service blueprint;
- GTM, lộ trình, RACI, risk register, đề nghị với Board.

**Bảng do tác giả soạn** trong `data/round3/` (tiếng Anh, có ô `{...}` để điền số từ mô hình):
- `gtm_year1_plan`, `roadmap_plan`, `raci`, `risk_register`;
- `trust_metrics`, `legal_map`, `glide_path`, `journey_map`, `service_blueprint`;
- `wireframe_copy.json`.

**Code mới:**
- `src/round3/plan_tables.py`: điền số và gộp kết quả base theo quý, theo phase.
- `src/round3/diagrams_round3.py`: wireframe và service blueprint.

**Bảng output** (`outputs/round3/tables/`): `gtm_year1`, `roadmap_phases`, `board_ask`, `risk_register`, `raci`, `trust_metrics`, `legal_map`, `glide_path`, `journey_map`, `service_blueprint`.

**Hình** (`outputs/round3/figures/`):
- `wireframes_journey.png`: 6 màn hình, cho slide 8;
- `wireframes_errors.png`: 4 trạng thái lỗi, cho appendix G;
- `service_blueprint.png`: cho slide 9 hoặc appendix.
- Wireframe là bản low-fi, sẽ thay bằng Figma. Hình lưu ở 400 dpi vì Calibri dưới khoảng 7,7pt bị trắng chữ ở 200 dpi (matplotlib 3.11).

**`plan_payday.md` §7–9 đã thay bằng số của mô hình:**
- pilot 45.000 TK;
- số liệu GTM theo quý; chi phí và kết quả theo phase;
- bảng test F6 mới, 12 test (thêm test 8–12);
- §5.6 có ghi chú trỏ sang bảng cổng.

**Số chính (base):**
- Năm 1: 9.414 saver ghi danh; 4.953 funded; 30,1 tỷ số dư; chi 9,2 tỷ, trong đó marketing và tiếp cận 1,17 tỷ.
- Phase 0–1: 5,72 tỷ, cộng dự phòng thành 6,6 tỷ.
- Cổng:
  - tháng 3: phí VA, shadow run 99,5%, tuân thủ;
  - tháng 6: ghi danh ≥1,5% (dừng <1,0%); 3 kỳ ≥81%; chi phí ròng ≤1,6 triệu/TK;
  - tháng 12: funded ≥3.962; số dư ≥24,1 tỷ;
  - tháng 24: TK ≥10 triệu ≥6.171; doanh nghiệp tham gia ≥39%.
- Risk register: R1 reliability ngày lương 20; R2 ghi danh thấp 16; R4 cơ quan quản lý và Trứng Vàng 15; R3 điều khoản đối tác 12; R5 thị trường giảm hoặc xung đột lợi ích 12; R6 tiền chuyển sang giao dịch 9.

**Sửa trong lúc kiểm Phase 2:**
- Bỏ lãi suất Trứng Vàng 7,10% khỏi wireframe; thay bằng `[rate]%` vì chưa kiểm được lãi của trái phiếu ngân hàng trong Payday.
- "45% review 2026" là app treo, đơ, giật. Câu cũ "app treo sau cập nhật" là sai; review đổ lỗi cho bản cập nhật chỉ chiếm 8,6%.
- "5 phút" là mục tiêu thiết kế. Không có nguồn nói VCB Digibank mất 5 phút; chỉ so số bước với VCB Digibank SIP.
- Quy tắc tái tục: FAQ của DNSE ghi Trứng Vàng mặc định tự tái tục và chỉ gửi email sau khi tái tục; một review 2026 than bị tự tái tục mà mất tiền. Payday đổi thành chỉ tái tục vào kỳ hạn vẫn đáo hạn trước ngày mục tiêu, báo trước 3 ngày, tắt bằng một chạm.
- "Về trước 22:00": theo FAQ, tiền về "khoảng 21-22h ngày bán" khi bán trong giờ 9h00–14h30.
- Lỗi ký quỹ dẫn QĐ 461/QĐ-XPHC (17/08/2026), không phải "kết luận thanh tra".

## Phase 3: Nội dung slide và file Word — xong phần nội dung, đang ở ⛳ checkpoint 3.6

**Checkpoint 3.1 (16/10):** user duyệt câu chuyện và 4 lựa chọn thông điệp ("ok rồi"). Tên thành viên và Figma: "để sau".

**File nội dung:**
- `docs/doc_round3/deck_content.md` (bản 2): 15 slide theo khung của prompt.
- `docs/doc_round3/deck_appendix.md`: appendix A–I (22 slide appendix) và references APA 7 (47 mục).
- `outputs/round3/Round3A_content_KTQT_FTUers.docx`:
  - A4 ngang, mỗi slide một trang;
  - 34 bảng Word thật, 18 hình;
  - style riêng cho designer notes và speaker notes;
  - khoảng 72 trang; đã xuất PDF bằng Word để soát hình thức.

**Chạy lại toàn bộ:** `python src/round3/run_round3.py` (khoảng 13 giây). Thứ tự các bước:
1. test (35/35);
2. mô hình;
3. bảng kế hoạch;
4. review;
5. `deck_tables.py`;
6. hình;
7. sơ đồ;
8. `check_deck_content.py`;
9. `build_content_docx.py`.

**Cách bảng không lệch khỏi mô hình:**
- Mỗi bảng trong 2 file markdown nằm giữa `<!-- table: NAME -->` và `<!-- /table -->`.
- `src/round3/deck_tables.py` ghi bảng từ `outputs/round3/tables/NAME.csv`. Các CSV này sinh từ mẫu do tác giả soạn trong `data/round3/deck_tables/` (số trong ngoặc nhọn lấy từ mô hình) hoặc trực tiếp từ output.
- `check_deck_content.py` báo lỗi nếu bảng markdown khác CSV.
- **Muốn sửa bảng thì sửa CSV mẫu, không sửa markdown.**

**Kiểm (`check_deck_content.py`):**
- Executive Summary 142 từ; mọi action title ≤15 từ; chữ trên slide ≤60 từ; bảng slide chính ≤6×5; speaker notes 111–132 từ (tổng khoảng 14 phút).
- 34 bảng khớp CSV.
- Không còn cụm từ cấm (riêng slide 5 được trích mốc 85.000, vì đó là slide "What changed").
- Mọi trích dẫn có mục trong references, và mọi mục đều được trích.

**8 hình mới (bước 3.2, theo skill dataviz):**
- `why_now_timeline`, `sizing_funnel`, `positioning_map`, `gtm_timeline`, `risk_heatmap` vẽ bằng `figures_round3.py`.
- `solution_overview`, `roadmap`, `decision_tree` vẽ bằng `diagrams_round3.py`.
- Bảng màu đã chạy script kiểm của skill:
  - dải CORAL → RED → DARK_RED đạt (đầu nhạt 2,80:1); LIGHT_RED không đạt (1,67:1) nên không dùng;
  - cặp RED/xám đạt kiểm mù màu (ΔE 8,1).
- Dạng hình:
  - "nhấn mạnh" (đỏ cho điểm chính, xám cho phần nền);
  - funnel dùng chuỗi ô số thay vì cột, vì 1,5 triệu → 6,8 nghìn chênh khoảng 200 lần;
  - không dùng hai trục y;
  - Q4/2025 tiền NĐT để trống, ghi "not reported".
- Dữ liệu tác giả soạn cho hình: `data/round3/why_now_events.csv`, `competitors.csv`, `ecosystem_roadmap.csv`, `decision_tree.csv`, `solution_overview.json`; thêm cột `short` vào `risk_register.csv`.

**Nguồn tự kiểm thêm (17/10; S38–S44, tổng 44 nguồn):**
- SSI eSIP 23/04/2026 (S38).
- VPS Smart Indexing: ra mắt 11/08/2026, ủy thác (S39); từ 50 triệu, sau đó 10 triệu/tháng, phí 0,5%/năm (S40).
- VPBank Hũ Mục Tiêu: chỉ chắc tháng 9/2026. Trang ghi 21/09, kết quả tìm kiếm ghi 12/09, nên slide chỉ ghi "September" (S41).
- VCBF SIP: từ 100.000đ/kỳ trên VCB Digibank, phí bán lại ưu đãi (S42).
- VinaSIP 23/06/2021: lệnh chuyển tiền định kỳ, từ 500.000đ (S43).
- SSI iBoard thêm quỹ Dragon Capital từ 29/06/2026 (S44).

**Sửa trong Phase 3:**
- Trứng Vàng "Big Four" → "Vietcombank, VietinBank, BIDV" (S28, tài liệu ĐHĐCĐ tr. 75).
- Phí VCB SIP: "lower exit fee" sai, đổi thành "preferential redemption fee".
- Slide 10 ghi rõ "20 rival products": 9 đã tự kiểm (bảng C1) và 11 tra cứu tại bàn (liệt kê, không khẳng định số liệu).
- Ký hiệu năm references đánh lại liền mạch:
  - DNSE: 2026d = Lightspeed, 2026e = sự cố 4/3, 2026f = tài liệu ĐHĐCĐ;
  - Vietstock 2026b = margin; VnExpress 2026b = VN-Index −115; TCBS (2026) = Q2/2026.
- Khoảng tin cậy Wilson nay tính trong `reviews_2026.py` (cột `both_ci95_low/high`).

**Còn lại của Phase 3:** user và team duyệt file markdown và file Word (⛳ checkpoint sau 3.6).

## Report bổ trợ Vòng 3A (EN + VI) — xong, 17/10/2026

User yêu cầu "1 report hoàn chỉnh đầy đủ như round 2 nhưng objectives của round3", bản EN và bản VI, không để nộp.

**File:**
- `docs/doc_round3/report_round3A_en.md` và `report_round3A_vi.md`: tóm tắt điều hành; 13 mục (giới thiệu; vấn đề và vì sao ngay; người dùng và giá trị; thiết kế sản phẩm; minh họa; định vị; phương án kinh doanh; GTM năm 1; lộ trình; triển khai và kiểm chứng; rủi ro; đề nghị HĐQT; kết luận); phụ lục A–G; 50 tài liệu tham khảo APA. 22 bảng đánh số + 11 bảng phụ lục, 16 hình.
- `outputs/round3/Round3A_report_KTQT_FTUers_EN.docx/.pdf` (39 trang) và `_VI.docx/.pdf` (40 trang): A4 dọc, kiểu Round 2 (Times, header, số trang, mục lục do Word điền). Bảng phụ lục ≥7 cột nằm ở trang ngang.
- `src/round3/build_report_docx.py`: dựng Word từ markdown, kiểm số heading/bảng/hình/tài liệu tham khảo, gọi Word (COM) điền mục lục và xuất PDF; `--no-toc` để bỏ bước Word. Đã thêm vào `run_round3.py` (pipeline nay khoảng 150 s vì bước Word).

**Bảng tiếng Việt (không sửa tay):**
- `deck_tables.py` render bảng vào cả hai report. Bản VI đọc `outputs/round3/tables/vi/NAME.csv`.
- Bảng VI dịch theo từng ô: số trong ô EN được tách ra, phần chữ tra trong `data/round3/deck_tables_vi/cells_vi_main.csv`, `cells_vi_model.csv`, `cells_vi_appendix.csv` (cột `table,en,vi`, ⟦0⟧ là chỗ số), rồi số được điền lại theo định dạng VN (1.234,5). Đổi mô hình thì bảng VI tự đổi theo.
- Ô chưa có bản dịch được giữ tiếng Anh và ghi vào `tables/vi/untranslated.csv`; `check_deck_content.py` báo lỗi nếu file này còn dòng. Khi sửa chữ ở CSV mẫu EN, phải thêm dòng dịch tương ứng.
- Bảng trích review ở bản VI dùng nguyên văn tiếng Việt: C3 lấy từ cột `original_vi` (từ tục được che bằng `_`), D1 lấy từ `data/round3/deck_tables_vi/appF1_feedback.csv` (cắt nguyên văn từ file review gốc bằng script, không gõ lại).

**Kiểm tra:** `check_deck_content.py` nay kiểm cả hai report: bảng khớp CSV; mỗi bảng có caption phía trên và dòng Nguồn phía dưới; mỗi hình có dòng Nguồn; số bảng/hình liên tục và mọi "Table N" được nhắc đều tồn tại; trích dẫn khớp danh mục tham khảo (đã sửa regex để nhận "X & Y, năm"); cụm từ cấm (bản VI có danh sách riêng; "85,000 accounts"/"85.000 TK" chỉ được ở mục 2.5). Mọi con số trong thân bài EN đã đối chiếu với output mô hình và nguồn; tập số của bản VI khớp bản EN.

**Sửa phát hiện khi viết report (đã áp dụng cho cả deck nếu liên quan):**
- Phí bán VCBF-FIF: 2,0% trong 3 tháng đầu và 1,0% từ tháng 3–12 (S24), không phải "1–2% trong 3–12 tháng"; đã sửa cả `payday_spec.md` §4.
- Phát hiện mới: VCBF-FIF nắm trái phiếu DSE125018 của DNSE = 6,97% NAV (S24, 31/08/2026). Report đề xuất màn hình kế hoạch hiện rõ khoản này và danh mục mặc định ưu tiên quỹ không nắm trái phiếu DNSE; chốt khi ký hợp đồng quỹ ở Phase 0. **Deck chưa nhắc điểm này**, cần quyết định ở Phase 4.
- Bảng stress B4: kịch bản cơ sở in "−0.0%" → sửa thành "0.0%" (`stress_rows`).
- Q&A phụ lục: "not the highest rate" → "not on the rate" (tránh cụm cấm).
- Năm 2025 là thời điểm Trứng Vàng phân bổ vào trái phiếu DNSE/Agribank/BVBank (BCTN 2025), không viết "hiện nay".
- Nguồn web: 30 nguồn tác giả tự kiểm đủ, 3 kiểm một phần, 11 mới có agent kiểm; report ghi đúng như vậy thay vì "đã tự kiểm mọi nguồn trên slide".

## Câu hỏi đang treo
1. Tên thành viên cho slide giới thiệu.
2. Trong team có ai vẽ lại wireframe trên Figma không. Nếu không, dùng bản PNG hiện tại kèm nhãn "low-fidelity".

## Việc tiếp theo
- **Phase 4 (sau khi user duyệt bản Word):**
  - `outputs/round3/claims_check.csv` đối chiếu mọi con số giữa các slide;
  - rà ràng buộc booklet;
  - soát hình bằng skill design-critique;
  - xuất lại Word. ⛳
- Phase 5: `qa_prep.md`; 1 trang số liệu tiếng Việt cho 3B.
- Phase 6 chỉ làm khi user yêu cầu: pptx → PDF ≤10MB.
- Nếu đổi giả định: sửa `payday_assumptions.csv`, chạy `python src/round3/run_round3.py`.
- Nếu sửa chữ của bảng: sửa CSV mẫu trong `data/round3/deck_tables/` hoặc CSV kế hoạch trong `data/round3/`, rồi chạy lại.

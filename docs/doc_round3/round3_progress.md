# Tiến độ Round 3A (Payday Portfolio)

*File này để phiên sau tiếp tục được. Cập nhật sau mỗi phase. Prompt gốc: `docs/doc_round3/PROMPT_round3A_build.md`.*

**Trạng thái (16/10/2026, tối):**
- Phase 0 và Phase 1 xong.
- User yêu cầu phản biện và hoàn thiện. Đã làm xong vòng phản biện: mô hình đã sửa, các quyết định đã được đánh giá trong **`docs/doc_round3/review_phase1.md`**.
- **Đang chờ user đồng ý** với các quyết định D1–D7, rồi mới sang Phase 2. Chưa viết nội dung slide.

---

## Phase 0: Khởi động — xong
- Đã đọc đủ các file ở mục 4 của prompt, kể cả report Round 2 (trích text bằng pymupdf).
- `python run_all.py --no-report` chạy được; `check_tables.md` ghi **0 other differences** (kiểm lại sau khi thêm code Round 3).

## Phase 1: Sửa nền phân tích — xong, đã qua một vòng phản biện

**Chạy lại toàn bộ Round 3 bằng một lệnh:** `python src/round3/run_round3.py` (khoảng 4 giây): test (35/35) → mô hình → review → hình. Không sửa file Round 2.

### File chính
- Đầu vào: `data/round3/payday_assumptions.csv`, 60 tham số. Cột `low` = kịch bản xấu, `high` = kịch bản tốt. Cột `type`: sourced / derived / assumption. Cột `source` ghi nguồn hoặc cách tính.
- Nguồn: `data/round3/sources_round3.csv`, 36 nguồn kèm ngày truy cập. Cột `checked_by_author` cho biết tôi đã tự mở kiểm hay chỉ agent tìm.
- Lãi suất 10/2026: `data/round3/rates_oct_2026.csv`.
- Code trong `src/round3/`:
  - `payday_model.py`: hai engine. Engine theo cohort; engine theo lịch thời gian dùng cho stress test, cho kết quả trùng khớp engine cohort khi không có cú sốc.
  - `test_payday_model.py`, `reviews_2026.py`, `figures_round3.py`, `run_round3.py`.
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
  - trần CAC 60 tháng 127.500đ, so với CAC kênh TK ngủ 65.000đ;
  - tỷ lệ ghi danh hòa vốn 1,02%;
  - cần 11 kỳ liền để vượt 10 triệu.
- Phí VA: miễn phí thì trần CAC là 199.000đ; từ 6.191đ/kỳ trở lên thì TK ngủ không còn đáng tiếp cận.
- Stress test (TK ≥10 triệu tháng 36): thị trường giảm năm 2 → −12%; ngày lương lỗi tháng 9 → −8%; cả hai → −18%. Tiền gần như không đổi, tức rủi ro chính là KPI và uy tín.

### Các sửa đổi chính sau phản biện (chi tiết trong `review_phase1.md` §1)
1. Cổng quyết định có tiêu chí cấp chương trình: chi phí ròng/TK mới ≥10 triệu. Thêm Cổng 0 ở tháng 3 cho điều khoản đối tác, phí VA và shadow run.
2. Biên Trứng Vàng hạ còn 0,6%. Lý do: trái phiếu Agribank trả bình quân Big4 + 2,0 điểm, khoảng 7,9%, còn Trứng Vàng trả 6,2–7,6%.
3. Trứng Vàng đang dùng cả trái phiếu DNSE (BCTN 2025), và từng bị dừng mở mới theo yêu cầu cơ quan quản lý (12/2023).
4. Tier bằng tiền tốn 41% doanh thu. MVP chuyển sang ưu đãi phi tiền mặt; tier tiền mặt chỉ còn là phương án thử.
5. Pilot tăng từ 20.000 lên 45.000 TK cho đủ lực thống kê.
6. Kênh chủ lao động cần tỷ lệ tham gia ≥39%.
7. Thêm stress test.
8. Sửa lời: "no platform fee" thay cho "zero-fee"; không nói "lãi cao nhất".

### Quyết định đề xuất (chờ user đồng ý; chi tiết trong `review_phase1.md` §2)
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
- 58 review đọc tay: 83% mô tả một thứ bị hỏng (95% CI 71–90%); trust 19% (CI 11–31%; H1/2025 là 55%).
- DNSE đã công bố sự cố ngày 4/3/2026, 13:22–15:20. Có 9 review đăng ngày 4–5/3.

## Câu hỏi đang treo
1. Đồng ý D1–D7 không?
2. Tên thành viên cho slide giới thiệu; trong team có ai vẽ Figma không.

## Việc tiếp theo (sau khi user đồng ý)
- Phase 2: `payday_spec.md`, persona, journey và wireframe, service blueprint, GTM, RACI, risk register. Risk register phải có: Trứng Vàng từng bị dừng (2023); xung đột lợi ích; phí VA; reliability ngày lương.
- Phase 3: `deck_content.md` và file Word.
- Nếu đổi giả định: sửa `payday_assumptions.csv`, chạy `python src/round3/run_round3.py`.

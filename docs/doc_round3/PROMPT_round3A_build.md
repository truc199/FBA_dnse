# PROMPT: Hoàn thiện nội dung Round 3A cho Payday Portfolio (markdown → Word)

*Dùng ở phiên Claude Code mới. Cách chạy: mở phiên mới tại thư mục `D:\uni\FBA_dnse` và gõ:*
> Đọc `docs/doc_round3/PROMPT_round3A_build.md` và thực hiện theo đúng workflow trong đó.

*Nếu phiên bị đầy context, mở phiên mới và gõ:*
> Đọc `docs/doc_round3/PROMPT_round3A_build.md` và `docs/doc_round3/round3_progress.md`, rồi tiếp tục từ bước chưa xong.

---

## 1. Vai trò và mục tiêu

Bạn là analyst kiêm product owner hoàn thành bài nộp **Round 3A** cuộc thi **Future Business Analyst Season 6** (RMIT BFC Hanoi). Công ty phân tích là **DNSE Securities (HOSE: DSE)**. Sản phẩm đề xuất là **Payday Portfolio**, được kế thừa từ report Round 2.

**Thứ cần nộp (booklet không yêu cầu báo cáo văn bản): một file PDF slide deck.**
- Khổ 16:9, dung lượng ≤10MB, viết bằng **tiếng Anh**. Thuật ngữ tiếng Việt phải kèm bản dịch, ví dụ "Trứng Vàng (Golden Egg)", "Tài khoản Không Ngủ (Never-Sleeping Account)".
- **Tối đa 15 slide chính.** Không tính cover, giới thiệu thành viên, mục lục, appendix, references.
- Bắt buộc có **1 slide Executive Summary**: ≤150 từ, cỡ chữ 14–15, nêu business case, **vốn đầu tư cần** và **lợi nhuận kỳ vọng**.
- References nằm ngay trên slide, theo APA 7 như report Round 2. **Không dùng hyperlink ngoài.** Mọi bằng chứng bổ sung đặt trong appendix của deck.
- Tên file: `[FBAR3_2026]_KTQT FTUers.pdf`.
- Deadline: **21:00 thứ Ba 20/10/2026**. Mục tiêu nộp trước 19:30.
- Thuyết trình trực tiếp 15 phút cho "Board" (CEO, CFO, CTO, Head of Product do giám khảo đóng), sau đó Q&A.

> **Phạm vi giai đoạn này (quan trọng): CHƯA dựng slide.**
> - Việc của bạn bây giờ là hoàn thiện **toàn bộ nội dung sẽ đưa lên slide**: chữ, số liệu, **bảng**, **biểu đồ**.
> - Viết ra file **markdown** trước, rồi xuất thành **file Word (.docx)** để team duyệt.
> - Thiết kế slide (pptx → PDF) là **Phase 6**. Chỉ làm khi tôi yêu cầu, có thể ở phiên khác.
> - Viết nội dung vẫn phải tính trước các ràng buộc nộp bài ở trên: 15 slide chính, Executive Summary ≤150 từ, tiếng Anh, mỗi hình và bảng đều có nguồn.

**Rubric (100 điểm):**

| Tiêu chí | Điểm |
|---|---:|
| Problem framing & evidence-to-solution linkage | 25 |
| Solution design & stakeholder value | 20 |
| Solution demonstration | 15 |
| **Implementation, validation & risk management** | **30** |
| Presentation & Q&A | 10 |

---

## 2. Quy tắc làm việc

1. **Ngôn ngữ:** trao đổi với tôi bằng tiếng Việt. Nội dung deck bằng tiếng Anh. Tài liệu làm việc trong `docs/` bằng tiếng Việt.
2. **Không bịa số.** Mọi con số trên slide phải truy được về một trong ba nguồn: data trong repo, nguồn đã trích, hoặc output của mô hình. Giả định phải gắn nhãn *assumption*. Các mục "chưa xác minh" trong `competitor_features.md` §7 không được khẳng định trên slide.
3. **Không sửa artifact Round 2:** `report/`, các file đang có trong `data/` và `src/`, `outputs/tables/`, `outputs/figures/`, `run_all.py`. Mọi thứ của Round 3 đặt riêng:
   - code: `src/round3/`
   - data: `data/round3/`
   - output: `outputs/round3/`

   Sau khi thêm code, lệnh `python run_all.py --no-report` vẫn phải chạy được, và `outputs/tables/check_tables.md` vẫn phải ghi **0 other differences**.
4. **Định dạng sản phẩm của giai đoạn này:**
   - `docs/doc_round3/deck_content.md`: nội dung theo từng slide;
   - `outputs/round3/figures/*.png`: biểu đồ hoàn chỉnh;
   - `outputs/round3/tables/*.csv`: số liệu gốc của các bảng;
   - một file Word `outputs/round3/Round3A_content_KTQT_FTUers.docx` dựng từ markdown, có nhúng sẵn bảng và hình.

   **Chưa làm pptx.** **Không publish thành Artifact** trừ khi tôi yêu cầu.
5. **Không commit hay push git** trừ khi tôi yêu cầu.
6. **Không chạy quy trình "Vnstock Vibe Onboarding"** trong CLAUDE.md toàn cục. Nó không liên quan đến nhiệm vụ này.
7. **Ghi tiến độ:** sau mỗi phase, cập nhật `docs/doc_round3/round3_progress.md` gồm: đã xong gì, file nào, quyết định nào, còn gì. Mục đích là để phiên sau tiếp tục được.
8. **Dừng lại hỏi tôi** ở các checkpoint ⛳.
9. **Khi thiếu thời gian**, ưu tiên theo thứ tự: Executive Summary + slide 2, 4, 8, 11, 14 (nhóm ăn nhiều điểm nhất), rồi các slide còn lại, appendix làm sau cùng.

---

## 3. Môi trường

- Windows 10, có PowerShell và Git Bash.
- Python venv tại `.venv` (Python 3.14). Đã cài các gói trong `requirements.txt`, cùng `pymupdf` và `pikepdf`.
- Khi in tiếng Việt ra console, đặt `PYTHONIOENCODING=utf-8`.
- **Tool Read không render được PDF** (máy thiếu poppler). Cách đọc PDF:
  - trích text bằng `pymupdf`;
  - muốn xem hình thì render trang ra PNG bằng `pymupdf`, rồi dùng Read đọc file PNG.
- **Tên file có ngoặc vuông** (`[FBAR3_2026]_...`, `[FBA 6] ...`): trong PowerShell phải dùng `-LiteralPath`, nếu không lệnh sẽ báo "item does not exist". Trong Python thì truyền đường dẫn bình thường.
- **Xuất Word:**
  - Kiểm tra máy có `pandoc` không (`pandoc --version`).
  - Nếu không có, dùng `python-docx` (đã cài) theo hướng dẫn của skill `docx`.
  - Viết thành script để chạy lại được: sửa markdown xong, chạy lại script là ra Word mới.
- **Chưa cài LibreOffice.** Giai đoạn này không cần đến. Riêng Phase 6 (xuất PPTX → PDF) cần Microsoft PowerPoint qua COM, hoặc LibreOffice.
- **Thương hiệu:**
  - Màu DNSE trong `src/config.py`: RED `#D7263D`, DARK_RED `#8E1B2C`, LIGHT_RED `#F6B9BF`, CORAL `#FB6C77`, PEACH `#F4A06E`, CHARCOAL `#1A1A1A`, MID_GREY `#6B6B6B`, GREY `#9A9A9A`, LIGHT_GREY `#CFCFCF`.
  - Font: Calibri (dự phòng Carlito).
  - Phong cách hình: xem `src/figures/style.py` và `src/figures/diagrams.py`.

---

## 4. File cần đọc (theo thứ tự)

1. `agent.md`: bối cảnh workspace, cấu trúc thư mục, số liệu then chốt.
2. `docs/doc_round3/[FBA 6] QUESTION BOOKLET ROUND 3.md`: yêu cầu chính thức. Đọc kỹ mục 3A, rubric và submission.
3. `docs/doc_round3/plan_payday.md`: **kế hoạch chính**, gồm:
   - outline 15 slide (§3); data (§4); cách đặt target (§5);
   - business case và ví dụ J-curve (§6);
   - GTM (§7); roadmap (§8); RACI và test (§9); checklist nộp (§11).
4. `docs/doc_round3/review_round2.md`: lỗi của Round 2 cần sửa (L1–L8, R1–R8, K1–K14) và các ứng viên cho slide "What changed".
5. `docs/doc_round3/review_payday.md`: phản biện sản phẩm, 7 chỉnh sửa (§7), câu hỏi Q&A (§8).
6. `docs/doc_round3/competitor_features.md`: 14 sản phẩm đối thủ có nguồn, định vị (§4), bằng chứng "feedback" thay cho survey (§6), các điểm chưa xác minh (§7).
7. `docs/doc_round3/plan_tech.md`: chiến lược cho các sản phẩm DNSE đang có. Dùng cho 1 slide roadmap hệ sinh thái, appendix và Q&A.
8. `docs/doc_round3/round3_core_tech_risk.md`: risk register cho công nghệ lõi.
9. Report Round 2 đã nộp: `report/FBAR2_2026_KTQT_FTUers.pdf`. Trích text bằng pymupdf; chú ý nhất mục 4, Table 1, Appendix F và G.
10. Code và data:
    - `README.md`
    - `src/analysis.py`: các hàm `scenarios`, `negatives`, `theme_shares`, `reliability_trust`
    - `data/manual/*.csv`
    - `outputs/tables/computed/*.csv`
    - `outputs/figures/*.png`

> ⚠️ `docs/doc_round2/v5_revision_discussion_recommendation.md`, `weakness.md` và `final_report_review.md` mô tả **bản nháp**, không phải bản đã nộp. Bản nộp dùng Table F5/F6 và KPI 85.000. Chỉ dùng các file này để tham khảo lập luận, và luôn đối chiếu với PDF.

---

## 5. Skill cần dùng

Gọi skill bằng Skill tool **trước khi** bắt đầu việc tương ứng.

| Skill | Dùng khi |
|---|---|
| `anthropic-skills:docx` | Xuất `deck_content.md` thành file Word có bảng và hình nhúng |
| `anthropic-skills:pdf` | Trích text report Round 2 |
| `dataviz` | **Trước khi viết bất kỳ code biểu đồ nào** (J-curve, funnel, bản đồ 2×2, timeline, tornado, bảng nguyên nhân review) |
| `design-skills:journey-mapping` | Customer journey cho slide 8 |
| `design-skills:ux-writing` | Microcopy trên wireframe: nút, màn hình điều khoản, thông báo lỗi |
| `design-skills:interaction-design` | Luồng màn hình và các trạng thái lỗi (tùy chọn) |
| `design-skills:design-critique` | Soát biểu đồ và bảng (đọc được không, nhất quán không) trước khi chốt |
| `data:validate-data` | Rà mô hình và các bảng số trước khi đưa vào nội dung (tùy chọn) |

- **Để dành cho Phase 6** (thiết kế slide, làm sau): `anthropic-skills:pptx`; `anthropic-skills:pdf` (nén file ≤10MB).
- **Không dùng** `academic-research-skills` (bộ đó dành cho bài báo học thuật).

---

## 6. Quyết định đã chọn

⛳ **Xác nhận lại 5 quyết định này với tôi ngay ở đầu phiên**, gộp trong một câu hỏi.

1. **Tier:**
   - thưởng cho **tiền đã đầu tư**: giảm phí quỹ, ưu tiên Trứng Vàng kỳ mới, quà chứng chỉ quỹ nhỏ ở các mốc 3/6/12 kỳ;
   - mọi ưu đãi lãi có **trần 50 triệu**;
   - **bỏ** mức "4,3% không điều kiện".
2. **Danh mục mặc định thiên trái phiếu** (Trứng Vàng + quỹ trái phiếu). Cổ phiếu và ETF chỉ dành cho mục tiêu từ 3 năm trở lên.
3. **KPI chính:** số TK có tài sản ròng ≥10 triệu, horizon **24–36 tháng**. Mốc 18 tháng lấy từ mô hình cohort. **Không giữ** mốc 85.000 sau 18 tháng.
4. **Đề nghị với Board:** chỉ xin duyệt **Phase 0–1** (MVP + pilot RCT với 20.000 TK ngủ), quyết định dừng hay tiếp ở **tháng 6**. Số tiền lấy từ mô hình.
5. **Định vị:**
   - "Payday" chỉ là cách gọi tên, **không phải điểm khác biệt**, vì VinaSIP (2021) và VCB Digibank SIP đã có chuyển tiền định kỳ từ ngân hàng.
   - Điểm khác biệt là tổ hợp: **nhiều lớp tài sản trong một kế hoạch**, **tư vấn theo mục tiêu có khách xác nhận**, **thưởng cho sự bền bỉ**, **minh bạch có số đo công bố**, tất cả trong app zero-fee với vé 500.000đ/tháng.

---

## 7. Số liệu đã kiểm chứng (dùng lại, không cần tính lại)

**Tài khoản và khách hàng (BCTN 2025):**
- 1.512.920 TK (12/2025); khoảng 1,7 triệu TK giữa 2026, bằng 12,3% của 13,85 triệu TK toàn thị trường.
- 518.514 TK mở mới năm 2025, bằng 20,1% thị trường.
- 85.739 khách hoạt động (5,7%); 27.100 TK có tài sản ròng ≥10 triệu (1,8%); tài sản khách hàng 53.471 tỷ.
- Khoảng 1,4 triệu TK ngủ (số suy ra: 1,400–1,427 triệu).

**Thị phần (Q2/2026):**
- Tiền NĐT 1.960,8 tỷ, bằng 2,3% của 86,6 nghìn tỷ.
- Dư nợ margin 6.303 tỷ, bằng 1,39% của 453,8 nghìn tỷ.
- LNTT Q2 97,4 tỷ, bằng 0,64% của 15.200 tỷ.
- Dư nợ trên mỗi TK của VPS gấp **5,5 lần** DNSE.

**Tài chính:**
- Doanh thu môi giới thấp hơn chi phí trực tiếp **16 quý liên tiếp** (Q3/2022–Q2/2026), lũy kế **−190,3 tỷ**. Năm 2025: doanh thu 404,0 tỷ, chi phí 464,9 tỷ.
- LNTT lõi 128–221 tỷ/năm kể từ 2022.
- LNTT H1/2026 111,6 tỷ (biên 13,2%); LNTT Q1/2026 14,2 tỷ.
- ROE H1/2026 3,8%. Chi phí vốn 6,5% (Q2/2026), tăng từ 3,6% giữa 2024. NIM 3,5%. Dư nợ/vốn chủ 116% (trần 200%).
- Cost proxy nền tảng 197,5 tỷ (2025), tương đương 7,3 triệu cho mỗi TK có ≥10 triệu.

**Sản phẩm DNSE:**
- Tài khoản Không Ngủ: 12.100 TK đăng ký (0,8%); lãi cơ bản 1,8%, tối đa 4,3%.
- Trứng Vàng: 1.037 khách hoạt động; lãi 4,2–5,3% (chưa rõ ngày cập nhật); tái tục tự động từ 10/04/2026.
- Ensa: khoảng 72.000 người dùng.

**Review tiêu cực của DNSE năm 2026** (dữ liệu đến 21/09):
- Reliability chiếm **58,8%** trên Google Play (n=34) và **75,0%** trên App Store (n=24). Trust chiếm 14,7% và 12,5%.
- Đỉnh rơi vào tháng 3/2026, trùng bản iOS 2.113.28.
- Riêng H1/2025, trust chiếm 54,8% review tiêu cực trên Google Play (đợt thưởng 100k).

**Pháp lý và vĩ mô:**
- QĐ 461/QĐ-XPHC ngày 17/08/2026 phạt DNSE 802,5 triệu đồng, trong đó 275 triệu vì 3 dịch vụ ứng trước phục vụ phái sinh không báo cáo UBCKNN; DNSE bị buộc dừng cả 3 dịch vụ.
- Open API: theo Thông tư 64/2024, ngân hàng phải tuân thủ **trước 01/03/2027**.
- Lãi suất đầu 10/2026: Big4 kỳ hạn 12 tháng 5,9% (tại quầy); chứng chỉ tiền gửi 7,4%. Trần lãi kỳ hạn 1 đến dưới 6 tháng là 4,75%; trần lãi không kỳ hạn 0,5%.
- ĐHĐCĐ 2026: mục tiêu doanh thu 1.736 tỷ, LNTT 550 tỷ. Hết H1/2026 mới đạt 20% kế hoạch LNTT. Chương trình trái phiếu 3.500 tỷ.

**Đối thủ (chi tiết và nguồn trong `competitor_features.md`):**

| Sản phẩm | Điểm chính |
|---|---|
| VPS Smart Indexing | Ra mắt 11/08/2026; vốn ban đầu 50 triệu; định kỳ ≥10 triệu/tháng; phí 0,5%/năm; VPS quản lý thay khách (ủy thác) |
| SSI eSIP | Chương trình "Tích sản thảnh thơi" từ 23/04/2026; quỹ SSIAM + Dragon Capital; voucher có điều kiện |
| VCB Digibank SIP | Quỹ VCBF; từ 100.000đ/kỳ; không cần eKYC lại |
| VinaCapital VinaSIP | Từ 2021; 500.000đ/tháng; lệnh chuyển tiền định kỳ từ ngân hàng |
| VPBank Hũ Mục Tiêu | Ra mắt 12/09/2026 |
| TCBS | iPower (đến 6%, tối thiểu 5 triệu); iTracker; Fundmart (31 quỹ, khoảng 55% NAV quỹ mở) |
| MoMo Túi Thần Tài | Từ 10.000đ |
| Tikop | Từ 50.000đ |

**Bằng chứng hành vi (trích đúng phạm vi):**

| Nghiên cứu | Kết quả | Chỉ dùng cho |
|---|---|---|
| Madrian & Shea (2001) | Mặc định opt-out: 37% → 86% | Kênh qua chủ lao động/payroll |
| Thaler & Benartzi (2004) | 78% tham gia khi chuyên viên mời trực tiếp; tỷ lệ tiết kiệm 3,5% → 13,6% | Kênh tư vấn trực tiếp |
| Ashraf et al. (2006) | Khoảng 28% nhận lời khi được mời trực tiếp | Cận trên cho kênh tư vấn |

---

## 8. Không được viết trên slide (đã biết là sai hoặc chưa chắc)

- "first salary-linked plan", "no competitor offers recurring investing".
- Dùng Madrian & Shea (37% → 86%) làm bằng chứng cho kênh opt-in.
- "tier interest at most VND 5.6 billion" (không phải cận trên).
- Phí 0,8% áp trên toàn bộ tài sản (DNSE miễn phí giao dịch ETF).
- "85,000 accounts ≥VND 10m within 18 months", trừ khi mô hình mới cho ra đúng con số đó.
- "banks offer little investment"; "brokers' products start after the decision to invest".
- "86 triệu tài khoản bị đóng"; "chứng chỉ quỹ thanh toán T+1 tại Việt Nam".

---

## 9. Workflow

### Phase 0: Khởi động (khoảng 30 phút)
- **0.1** Đọc các file ở mục 4.
- **0.2** Chạy `python run_all.py --no-report` (khoảng 16 giây) và xác nhận check_tables vẫn ghi 0 other differences.
- **0.3** ⛳ Hỏi tôi ba việc: (a) xác nhận 5 quyết định ở mục 6; (b) tên thành viên cho slide giới thiệu; (c) trong team có ai vẽ Figma không.
- **0.4** Tạo file `docs/doc_round3/round3_progress.md`.

### Phase 1: Sửa nền phân tích (ưu tiên cao nhất)

**1.1 Mô hình cohort cho Payday**
- Tạo `data/round3/payday_assumptions.csv` với các cột `param, low, base, high, unit, type (sourced|derived|assumption), source`.
- Tạo `src/round3/payday_model.py`. Mô hình chạy theo tháng, horizon 36–60 tháng:
  - Đầu vào: lịch ghi danh theo phase và kênh; mức góp; tỷ lệ ngừng góp mỗi tháng; tỷ lệ rút số dư mỗi năm; cơ cấu tài sản; lợi suất ròng theo lớp tài sản (ETF ≈ 0).
  - Chi phí: xây dựng, vận hành, CAC, thưởng tier (có trần); tùy chọn phase 2 cho vay từ tháng 19.
  - Đầu ra theo tháng: số ghi danh, số còn góp, số dư, số TK vượt 10 triệu (theo dõi riêng từng cohort), doanh thu, chi phí, tiền lũy kế.
  - Chạy 3 kịch bản; tornado độ nhạy cho CAC, lợi suất, tỷ lệ ngừng, mức góp, tốc độ ghi danh.
  - Tính thêm: tháng hòa vốn theo tháng; tháng hoàn vốn lũy kế; PV doanh thu trên mỗi saver (chính là trần CAC); ngưỡng ghi danh hòa vốn = chi phí tiếp cận mỗi TK ÷ trần CAC.
- **Test bắt buộc trước khi dùng mô hình.** Chạy với đầu vào minh họa của `plan_payday.md` §6.2:
  - Ghi danh: 350/tháng ở tháng 4–6; 3.000 ở tháng 7–12; 6.000 ở tháng 13–18; 8.000 ở tháng 19–36.
  - Góp 1,2 triệu/tháng; ngừng 2,5%/tháng; rút 10%/năm (chia đều theo tháng).
  - Xây dựng 12 tỷ, chia đều tháng 1–6; vận hành 6 tỷ/năm; CAC 150.000đ/saver; thưởng 0,3%/năm trên số dư; lợi suất gộp 0,6% (40/40/20 với 1,0/0,5/0%).
  - Công thức mỗi tháng:
    - `active = active·(1−churn) + enrol`
    - `bal = bal·(1−wd) + active·C`
    - `rev = bal·yld/12`
    - `cost = build/6 (nếu tháng ≤6) + run/12 + enrol·CAC + bal·bonus/12`
  - Kết quả phải khớp:
    - **Tháng 18:** 55.050 ghi danh; 49.108 còn góp; số dư ≈ 0,33 nghìn tỷ.
    - **Tháng 36:** 199.050 ghi danh; 148.257 còn góp; số dư ≈ 2,43 nghìn tỷ; tiền lũy kế ≈ −53,7 tỷ.
    - **PV/saver** (chiết khấu 12%/năm, tức 1%/tháng): ≈ 219.000đ (36 tháng, lợi suất 0,6%); ≈ 365.000đ (36 tháng, 1,0%); ≈ 416.000đ (60 tháng, 0,6%); ≈ 694.000đ (60 tháng, 1,0%).
- Sau khi khớp, thay đầu vào minh họa bằng số có nguồn ở mức tối đa có thể (bước 1.3). Phần còn lại giữ nhãn assumption.
- Output:
  - bảng: `outputs/round3/tables/payday_*.csv`;
  - hình (dùng skill `dataviz`): J-curve, số dư và số TK ≥10 triệu theo tháng, tornado.

**1.2 Gắn nguyên nhân cho 58 review tiêu cực năm 2026 của DNSE**
- Nguồn: Google Play 34 review (`data/reviews_flagged_vn.com.encapital.arrow.csv`) và App Store 24 review (`data/reviews_flagged_ios_vn.com.encapital.arrow.csv`). Lọc `keep=1`, rating ≤2, ngày từ 2026-01-01 đến 2026-09-21.
- **Đọc từng review**, không dựa vào keyword. Một review có thể mang nhiều nhãn.
- Bộ mã:
  - đăng nhập / OTP / xác thực
  - nạp/rút tiền không được ghi có
  - lệnh chậm / khớp lệnh / giá
  - crash hoặc treo sau cập nhật
  - eKYC / mở tài khoản
  - phí / điều khoản
  - lừa đảo / thưởng
  - khác
- Ghi thêm tháng; với iOS ghi phiên bản app (cột `version` trong `data/reviews_raw_ios_vn.com.encapital.arrow.csv`).
- Output: `outputs/round3/tables/reviews_2026_causes.csv`, kèm 3–4 trích dẫn đã dịch sang tiếng Anh.

**1.3 Bổ sung data còn thiếu**
- Tra web, ghi nguồn và ngày truy cập vào `data/round3/sources_round3.csv`:
  - biểu phí SIP và phí quỹ (SSIAM, Dragon Capital, VCBF), để ước lợi suất phí;
  - lãi Trứng Vàng hiện hành và điều kiện rút sớm (nếu không tìm được, hỏi tôi kiểm trong app);
  - lãi tiền gửi và chứng chỉ tiền gửi tháng 10/2026;
  - lương kỹ sư phần mềm tại Việt Nam (để ước chi phí xây dựng);
  - DNSE đã có trong danh sách đại lý phân phối chứng chỉ quỹ chưa.
- **Không sửa** `data/manual/idle_cash_rates.csv`. Nếu cần số mới thì tạo file riêng trong `data/round3/`.
- Được phép dùng subagent general-purpose để tra song song, nhưng phải tự kiểm lại kết quả.

**1.4 Đặt lại KPI và ngưỡng** (theo `plan_payday.md` §5)
- Tính trần CAC và ngưỡng ghi danh hòa vốn.
- Lập bảng continue / scale / adjust / stop cho cuối pilot (tháng 6), tháng 12 và tháng 24.

⛳ **Checkpoint:** báo tôi kết quả mô hình (3 kịch bản, tháng hòa vốn, vốn cần cho Phase 0–1) và bảng nguyên nhân review **trước khi** viết nội dung slide.

### Phase 2: Thiết kế sản phẩm

**2.1** Tạo `docs/doc_round3/payday_spec.md`, gồm:
- 2–3 persona, dựng từ data; không bịa thêm chi tiết đời tư;
- value proposition cho khách và cho DNSE;
- tính năng MVP, và những gì **cố ý loại** (margin, cổ phiếu đơn lẻ);
- tier mới; danh mục mặc định;
- trust controls kèm số đo sẽ công bố;
- yêu cầu reliability (SLO, cổng 99,5% chuyển tiền thành công);
- căn cứ pháp lý: TT 121/2020 Điều 4, 24, 27; Luật CK 2019 Điều 72; TT 64/2024.

**2.2 Customer journey và wireframe**
- Dùng skill `journey-mapping` cho journey, skill `ux-writing` cho microcopy.
- Spec 6 màn hình: mục tiêu → khẩu vị rủi ro → danh mục đề xuất → lệnh định kỳ / VA → kỳ góp đầu tiên → mốc 90 ngày / tier.
- Thêm các trạng thái lỗi: chuyển tiền thất bại; lương về trễ; tạm dừng hoặc bỏ qua một kỳ; rút tiền về ngân hàng.
- Vẽ wireframe low-fi thành file PNG (ví dụ bằng matplotlib) để file nội dung có đủ hình. Ghi chú rõ để team thay bằng bản Figma ở giai đoạn thiết kế slide.

**2.3 Service blueprint**
- Vẽ dạng diagram theo phong cách `src/figures/diagrams.py`, dùng màu trong `src/config.py`.
- Thể hiện frontstage / backstage / support, các điểm quyết định, cách xử lý lỗi, và ai chịu trách nhiệm từng phần.

**2.4 Kế hoạch triển khai**
- GTM năm đầu, roadmap 4 phase, RACI, risk register (6 rủi ro chấm theo khả năng × tác động), đề nghị với Board.
- Thay số trong `plan_payday.md` §7–9 bằng số từ mô hình.

### Phase 3: Viết nội dung slide (markdown) và xuất Word

**3.1 Viết `docs/doc_round3/deck_content.md`**

Mỗi slide một mục, theo đúng khung sau:

```
## Slide N: <tên ngắn>
**Action title:** <một câu kết luận, ≤15 từ>
**On-slide text:** 3–5 ý, tổng ≤60 từ
**Table:** bảng markdown (slide chính tối đa 6 dòng × 5 cột) + đường dẫn file CSV gốc
**Figure:** đường dẫn PNG + chú thích + dòng "Source: ..."
**Designer notes (tiếng Việt):** gợi ý bố cục, điểm cần nhấn mạnh
**Speaker notes:** khoảng 120 từ tiếng Anh (≈1 phút nói)
**Sources:** các trích dẫn APA dùng trên slide
```

- Bám outline 15 slide ở cuối phase này.
- Mỗi slide chính phải có **ít nhất một bảng hoặc một hình** (booklet khuyến khích data visualization).
- Bảng lớn: bản đầy đủ đưa xuống appendix, slide chính chỉ giữ bản rút gọn.

⛳ **Checkpoint:** gửi tôi bản `deck_content.md` đầu tiên (chưa cần đủ hình) để duyệt câu chuyện và thông điệp, trước khi làm hình hoàn chỉnh.

**3.2 Biểu đồ hoàn chỉnh** (skill `dataviz`)
- Script `src/round3/figures_round3.py` sinh toàn bộ hình vào `outputs/round3/figures/` và chạy lại được.
- Hình phải dùng được ngay trên slide:
  - PNG ≥200 dpi;
  - 2 cỡ chuẩn: toàn chiều ngang (khoảng 12 × 5,5 inch) và nửa slide (khoảng 6 × 4,5 inch);
  - chữ trong hình đọc được ở cỡ slide (≥12pt ở kích thước đó);
  - không đặt tiêu đề lớn trong hình (tiêu đề nằm trên slide);
  - dùng bảng màu DNSE.
- Tái dùng hình Round 2 khi phù hợp (ví dụ `outputs/figures/fig04_market_position.png`) và ghi rõ là hình từ Round 2.
- Danh sách hình tối thiểu:

| Slide | Hình |
|---|---|
| 2 | Thang thị phần |
| 3 | Timeline "why now" |
| 4 | Bảng nguyên nhân review 2026 |
| 6 | Funnel sizing |
| 7 | Sơ đồ giải pháp |
| 8 | 6 wireframe |
| 9 | Service blueprint |
| 10 | Bản đồ định vị 2×2 |
| 11 | J-curve + tornado |
| 12 | Timeline GTM |
| 13 | Roadmap |
| 14 | Cây quyết định |
| 15 | Heat map rủi ro |

**3.3 Bảng**
- Mỗi bảng có một file CSV tương ứng trong `outputs/round3/tables/`. File đó hoặc sinh từ code, hoặc ghi rõ là bảng do tác giả soạn.
- Số trong bảng phải khớp với output của mô hình và với data.

**3.4 Executive Summary: viết cuối cùng**
- ≤150 từ (đếm bằng code).
- Nêu đủ: vấn đề, giải pháp, vốn cho Phase 0–1, lợi nhuận hoặc tháng hòa vốn kỳ vọng, đề nghị với Board.
- Ghi chú cho người thiết kế: trên slide dùng cỡ chữ 14–15.

**3.5 Appendix và references**
- Nội dung appendix A–I viết trong cùng file, sau 15 slide chính (hoặc tách sang `docs/doc_round3/deck_appendix.md`).
- Danh mục references theo APA 7, thống nhất cách trình bày với report Round 2.

**3.6 Xuất Word** (skill `docx`)
- Viết script `src/round3/build_content_docx.py` (hoặc dùng pandoc) để chuyển markdown thành `outputs/round3/Round3A_content_KTQT_FTUers.docx`.
- Yêu cầu với file Word:
  - mỗi slide là một mục có heading;
  - bảng là bảng Word thật, không phải ảnh;
  - hình nhúng đủ rộng để đọc;
  - speaker notes và designer notes có kiểu chữ riêng để dễ phân biệt;
  - nên dùng khổ A4 ngang để bảng rộng không bị vỡ.
- Kiểm tra lại: mở docx bằng python-docx, đếm số heading slide, số bảng, số hình; xác nhận không thiếu hình nào.

⛳ **Checkpoint:** gửi tôi file markdown và file Word để team duyệt.

**Outline 15 slide** (chi tiết ở `plan_payday.md` §3):

| # | Slide | Thông điệp và nội dung chính |
|---|---|---|
| 1 | Executive summary | Business case, vốn đầu tư, lợi nhuận, đề nghị với Board |
| 2 | Problem recap: *accounts, not money* | Thang 12,3% → 2,3% → 1,4% → 0,6%; 1,8% TK có ≥10 triệu; LNTT lõi đi ngang; môi giới lỗ 16 quý |
| 3 | Why now | Lãi suất cao; tiền NĐT −38%; Open API trước 01/03/2027; cuộc đua tích lũy 2026; mới đạt 20% kế hoạch LNTT |
| 4 | Insight → design decision → impact | Có cập nhật 2026: reliability đã thay trust thành vấn đề nổi trội |
| 5 | What changed since Round 2 | Bảng ở `plan_payday.md` §2 |
| 6 | Target users & sizing | Persona + funnel từ 1,51 triệu TK |
| 7 | The solution | Value proposition, MVP, những gì cố ý loại |
| 8 | Customer journey | 6 màn hình wireframe |
| 9 | Service blueprint | Front/back stage, điểm quyết định, xử lý lỗi |
| 10 | Competitive positioning | Bảng 6 dòng + bản đồ 2×2 + câu định vị (`competitor_features.md` §4) |
| 11 | Business case | Vốn theo phase, unit economics, J-curve, độ nhạy, giá trị gián tiếp (tách riêng) |
| 12 | Go-to-market năm 1 | Theo quý |
| 13 | Strategic roadmap | 4 phase + hệ sinh thái sản phẩm hiện có (`plan_tech.md` §5) |
| 14 | Validation & KPIs | Test, ngưỡng quyết định, người chịu trách nhiệm |
| 15 | Risks + Board ask | Heat map rủi ro + đề nghị duyệt |

**Appendix:**
- A. Data & methods
- B. Mô hình cohort và độ nhạy
- C. Bảng đối thủ đầy đủ
- D. Review 2026
- E. Ánh xạ pháp lý
- F. Bằng chứng "feedback"
- G. Wireframe đầy đủ
- H. Bảng giả định
- I. Slide dự phòng cho Q&A

### Phase 4: Kiểm tra nội dung
- **4.1** Lập bảng đối chiếu số liệu `outputs/round3/claims_check.csv` với các cột: slide, câu, giá trị, nguồn hoặc phép tính, đã kiểm. Mọi con số phải nhất quán giữa các slide.
- **4.2** Rà các ràng buộc của booklet áp dụng cho phần nội dung (xem thêm `plan_payday.md` §11):
  - đúng 15 slide chính (không tính cover, thành viên, mục lục, appendix, references);
  - Executive Summary ≤150 từ;
  - toàn bộ chữ trên slide bằng tiếng Anh; thuật ngữ tiếng Việt có bản dịch;
  - mỗi hình và bảng có dòng "Source:";
  - references đầy đủ; **không có hyperlink** (URL chỉ được xuất hiện dạng chữ trong reference list);
  - không còn câu nào thuộc mục 8 ("Không được viết trên slide").
- **4.3** Xem lại từng hình (dùng Read mở file PNG) và dùng skill `design-critique`. Kiểm ba điều: hình có đọc được ở cỡ slide không; màu có nhất quán không; có hình nào thể hiện sai số không. Sửa xong thì xuất lại file Word.

⛳ **Checkpoint:** báo tôi kết quả kiểm tra, kèm bản Word cuối của giai đoạn nội dung.

### Phase 5: Chuẩn bị bảo vệ (nếu còn thời gian)
- **5.1** Tạo `docs/doc_round3/qa_prep.md`: 15–20 câu hỏi chia theo vai (CEO, CFO, CTO, Head of Product), mỗi câu có câu trả lời khoảng 30 giây kèm số liệu. Dựa trên `review_payday.md` §8.
- **5.2** Viết 1 trang số liệu bỏ túi bằng tiếng Việt cho Round 3B (tranh biện, phải trích nguồn bằng lời).

### Phase 6: Thiết kế slide (giai đoạn sau, CHỈ làm khi tôi yêu cầu)
- Gọi skill `anthropic-skills:pptx`.
- Viết script `src/round3/build_deck.py` để dựng `outputs/round3/[FBAR3_2026]_KTQT FTUers.pptx` từ `deck_content.md` và các hình trong `outputs/round3/figures/`.
- Thứ tự slide: cover → giới thiệu thành viên → mục lục → 15 slide chính → appendix A–I → references.
- Khổ 16:9; Executive Summary cỡ chữ 14–15; mọi slide có speaker notes.
- Xuất PDF bằng Microsoft PowerPoint qua COM: `New-Object -ComObject PowerPoint.Application`, mở file, rồi `SaveAs(<pdf>, 32)`. Nếu máy không có PowerPoint, hỏi tôi chọn: cài LibreOffice bằng winget, hoặc tôi tự xuất.
- Kiểm tra trước khi giao:
  - không có hyperlink (kiểm bằng python-pptx);
  - render từng trang PDF ra PNG bằng pymupdf, rồi soát bằng `design-critique`;
  - nén file xuống ≤10MB (skill `pdf`);
  - đặt tên đúng `[FBAR3_2026]_KTQT FTUers.pdf`.

---

## 10. Lịch đến hạn nộp

| Ngày | Việc |
|---|---|
| Thứ Sáu 16/10 | Phase 0 + mô hình cohort (1.1) |
| Thứ Bảy 17/10 | Phase 1 xong; Phase 2; nháp `deck_content.md` (⛳ duyệt câu chuyện) |
| Chủ Nhật 18/10 | Hình và bảng hoàn chỉnh; Executive Summary; xuất Word; Phase 4 kiểm tra (⛳ team duyệt) |
| Thứ Hai 19/10 | Phase 6: thiết kế slide (khi tôi yêu cầu); tập dượt lần 1 |
| Thứ Ba 20/10 | Soát lần cuối; xuất PDF ≤10MB; tập dượt lần 2; **nộp trước 19:30** |

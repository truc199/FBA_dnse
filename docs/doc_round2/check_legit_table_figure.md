# Kiểm chứng hình, bảng và nguồn số liệu: bản v5

*Lập ngày 27/09/2026 cho file `FBAR2_2026_Team_name.v5_3500w.docx` (và bản PDF cùng tên). Bản v4 giữ nguyên, không bị ghi đè.*

## 1. Tóm tắt

| Hạng mục | Kết quả |
|---|---|
| Số từ phần thân (Word đếm, từ "1. Introduction" đến trước "Appendices", **tính cả tiêu đề, chú thích và dòng Source của 4 hình trong thân bài**) | **3.417 từ** (trần 3.500) |
| Executive summary (không tính vào trần) | 707 từ |
| Tổng số trang | 51 trang: thân bài trang 7–16, phụ lục trang 17–46, tài liệu tham khảo trang 47–51 |
| Hình / bảng trong bản v5 | 21 hình (4 hình ở thân bài, 17 hình ở phụ lục) và 41 bảng (tất cả ở phụ lục) |
| Hình / bảng khớp nguồn sơ cấp sau khi tính lại | Toàn bộ phần lấy từ BCTC, thông báo sở giao dịch, VSDC, báo cáo thường niên DNSE, dữ liệu review và Findex |
| Lỗi số liệu hoặc lập luận tìm thấy và **đã sửa** | 15 lỗi (mục 3) |
| Hình / bảng **đã loại** | 12 (mục 6) |
| Số liệu còn dựa vào báo chí, thông cáo hoặc báo cáo công ty chưa mở lại bản gốc | Liệt kê ở mục 5, kèm cách trả lời nếu bị hỏi |

Mục lục, danh mục hình và danh mục bảng đã có số trang thật (lấy từ Word). Số trang được kiểm lại sau khi chèn và không lệch trang nào.

## 2. Cách kiểm và ký hiệu

**Nguồn sơ cấp dùng để đối chiếu:**
- BCTC DNSE lấy từng dòng qua Vietcap (`dnse_financials.json`), đã khớp với BCTC bán niên 2026 do KPMG soát xét.
- BCTC của 41 công ty chứng khoán khác, cùng mẫu biểu (`peer_financials.json`).
- Thông báo thị phần gốc của HNX và HOSE (`market_macro.json`).
- Báo cáo thường niên VSDC: 11.871.933 tài khoản cuối 2025; 2.681.838 tài khoản mở mới trong 2025.
- Báo cáo thường niên 2025 của DNSE (các phiên trước đã đọc bản gốc).
- API World Bank Findex (`findex_raw.json`).
- File review đã làm sạch (`reviews_flagged_*.csv`).

**Kiểm trực tiếp trên web ngày 27/09/2026:**
- Trang sản phẩm Tài khoản Không Ngủ của DNSE.
- Trang iPower của TCBS (bảng lãi hiệu lực từ 06/07/2026).
- Bài Market Times về Quyết định 461/QĐ-XPHC.
- Ảnh chụp thuyết minh 8(b) trong BCTC soát xét bán niên 2026.

**Ký hiệu:**
- ✅ Tính lại từ nguồn sơ cấp trong phiên này, khớp.
- ✅ᶜ Khớp, nhưng nguồn là thông cáo hoặc báo cáo của chính công ty (không có kiểm toán độc lập).
- 🟡 Nguồn là báo chí hoặc khảo sát bên thứ ba. Đã ghi nguồn nhưng chưa có bản gốc để đối chiếu, hoặc chỉ đối chiếu chéo được một phần.
- 🔧 Đã sửa trong v5.
- 🗑️ Đã loại khỏi báo cáo.

## 3. Lỗi đã phát hiện và đã sửa (xếp theo mức ảnh hưởng)

| # | Lỗi trong v4 | Bằng chứng | Đã sửa thành |
|---|---|---|---|
| 1 | **Tỷ trọng tài khoản 12,27% lệch ngày.** Tử số là 1,7 triệu tài khoản giữa năm 2026, mẫu số là 13,85 triệu tài khoản ngày 31/8/2026. Sai số này có trong Hình 2, Hình 3, Hình 5, Bảng B1 và Bảng E1 | Cùng ngày 31/12/2025, theo hai báo cáo thường niên: 1.512.920 / 11.871.933 = **12,74%**. Ngày 30/6/2026: 1,7 triệu / 13.430.517 = 12,66% | **12,7%** ở mọi nơi. Hình 1 và Hình A2 đã vẽ lại |
| 2 | **Thị phần mở mới 20%** chia tài khoản DNSE mở mới (số gộp) cho **mức tăng ròng** tài khoản toàn thị trường (2.573.945) | VSDC ghi 2.681.838 tài khoản **mở mới** trong 2025 | **19,3%** (518.514 / 2.681.838), cùng cơ sở gộp/gộp. Báo cáo thường niên DNSE vẫn ghi 20% theo cách tính của họ |
| 3 | **Tổng ngành chỉ lấy một nguồn báo chí**: tiền của nhà đầu tư 86,6 nghìn tỷ, dư nợ 453,8 nghìn tỷ, LNTT quý 2 là 15.200 tỷ | Cộng BCTC của các công ty trong dữ liệu Vietcap ra 56,4 nghìn tỷ, 345,3 nghìn tỷ và 11.871 tỷ | Trình bày thành khoảng. Tiền của NĐT: **2,3–3,5%**. Dư nợ: **1,4–1,8%**. LNTT: **0,6–0,8%**. Kết luận giữ nguyên ở cả hai đầu khoảng |
| 4 | **Bảng 5 (nay là Bảng A3), dòng tiền của NĐT trên mỗi tài khoản.** TCBS ghi "khoảng 7,5 triệu" theo báo; VPBankS ghi "not disclosed" | BCTC: TCBS 6.582 tỷ / 1,2 triệu = **5,5 triệu**; VPBankS 1.398 tỷ / 1,3 triệu = **1,1 triệu** | Sửa theo BCTC và thêm ghi chú: dòng này khó so sánh nhất, vì tài khoản liên kết ngân hàng để một phần tiền ở ngân hàng mẹ. **Hệ quả:** không dùng tiền/tài khoản để so với VPBankS; dùng dư nợ/tài khoản |
| 5 | **"Bank-affiliated brokers probably avoid this cost through their parents"**, và ý trong storyline rằng chi phí vốn cao vì không có ngân hàng mẹ | Cùng một công thức, chi phí vốn Q2/2026: DNSE 6,5%; TCBS 7,8%; VPBankS 6,8%; MBS 6,8%; SSI 6,1%; VPS (không có ngân hàng mẹ) 5,1% | Bỏ ý này. Thêm **Bảng A6**. Điều bất thường thật là cấu trúc tài sản: HTM chiếm 37,6% tổng tài sản, so với 1–22% ở các công ty khác |
| 6 | **"86% vay ngắn hạn"** được trình bày như rủi ro riêng của DNSE | VPS 68%; MBS 87%; TCBS 94%; SSI, VPBankS, HSC, Vietcap 100% | Bỏ khỏi finding. Số liệu vẫn nằm trong Bảng A6 để minh bạch |
| 7 | **"Mỗi 100 đồng doanh thu tăng thêm đi kèm 115 đồng chi phí"** (H1/2026) | Con số này có cả lỗ tự doanh (chi phí tăng 71 tỷ) | Dùng bản **lõi: 102 đồng** (H1/2026) và 105 đồng (2025 so với 2024). Phân rã đầy đủ ở Bảng A4 |
| 8 | **Hình 26 ghi 3,1 nghìn tỷ, còn Bảng 25 và phần tóm tắt ghi 3,2** | 150.000 × 2,5 triệu × 12 × 70% = 3,15 | Vẽ lại Hình B5 với nhãn 3,2 (làm tròn lên) |
| 9 | **Bảng 25, thu nhập mỗi người tiết kiệm ở kịch bản thận trọng: 165 nghìn đồng** | (4,86 + 4,74) tỷ / 60.000 người = 160 nghìn đồng | **160** (Bảng B15) |
| 10 | **Bảng 7 (nay là B1), dòng Sign-up ghi "18 to 34%" thị phần mở mới; ô bên dưới trỏ tới "Table B3"** | Báo cáo thường niên theo quý năm 2025: 34%, 18%, **16%**, 19% | **16–34%**. Tham chiếu sửa thành Table D2 |
| 11 | **Hình 2 có thanh ước tính "cash equity trading 2,1–2,6%"**, dựa trên giả định 7% cho HNX và UPCoM | Là ước tính, không phải số công bố | Bỏ. Chỉ giữ thị phần HNX 2,88% và việc DNSE nằm ngoài top 10 HOSE (cả hai là số công bố) |
| 12 | **Bảng 4 (phân tích cohort 2025)**: tài khoản mới mang về 28 triệu, 13–21 triệu hay âm, tùy giả định | Kết quả phụ thuộc hoàn toàn vào mức tăng giả định của tài sản khách cũ | Loại. Thay bằng số đo trực tiếp: tài sản/tài khoản giảm 9,5% |
| 13 | **"Tài sản/tài khoản giảm 9,5% trong năm VN-Index tăng 41%"** | Mức tăng 41% của VN-Index năm 2025 tập trung vào vài mã vốn hóa lớn | Nêu cả ba chỉ số: VN-Index +40,9%, UPCoM +27,7%, HNX-Index +9,4% (dữ liệu giá Vietcap). Luận điểm vẫn đứng vì cả ba chỉ số đều tăng |
| 14 | **Bảng 11 (nay là B5) nêu tên Fmarket, Infina, Finhay mà không có nguồn** | Không có tài liệu tham khảo | Đổi thành "Independent fund and savings apps" |
| 15 | **Giả thuyết trong storyline "chi phí tăng do R&D và hạ tầng công nghệ"** | Chi phí quản lý (gồm lương, dịch vụ mua ngoài, khấu hao) chỉ chiếm 6% phần chi phí lõi tăng thêm ở H1/2026 và 5% năm 2025. Tài sản cố định, kể cả tài sản thuê tài chính, là 152 tỷ, tức 1% tổng tài sản | Không đưa vào báo cáo. Finding 4 chỉ ra chi phí biên thật: 52% là chi phí vốn, 42% là chi phí môi giới trực tiếp |

## 4. Kiểm chứng từng hình và bảng trong bản v5

### 4.1 Thân bài

| Bản v5 | Từ v4 | Dữ liệu và nguồn | Cách kiểm | Kết quả |
|---|---|---|---|---|
| Figure 1. Share of each market vs account share | Fig 2 | Tài khoản: VSDC và BCTN DNSE. Thị phần HNX: thông báo HNX. Tiền, dư nợ, LNTT: tổng của báo chí và tổng BCTC | Tính lại mọi thanh; mẫu số cùng ngày | 🔧 Vẽ lại (lỗi #1, #2, #3, #11) |
| Figure 2. Lending and profit per account | Fig 6 | BCTC Q2/2026 qua Vietcap. Số tài khoản: VPBankS 1,3 triệu (Vietstock 5/2026), TCBS hơn 1,2 triệu (BCTN), VPS 1,547 triệu (bản cáo bạch IPO 9/2025), DNSE 1,7 triệu | Dư nợ/tài khoản: 3,71 / 20,2 / 29,4 / 42,9 triệu. LNTT/tài khoản: 57 / 891 / 1.661 / 1.748 nghìn đồng | ✅ Số tài chính. ✅ᶜ/🟡 Số tài khoản |
| Figure 3. Core vs proprietary profit | Fig 7 | BCTC | Lợi nhuận lõi: 156 / 128 / 221 / 194 / 78 tỷ | ✅ |
| Figure 4. Brokerage revenue vs direct cost | Fig 9 | BCTC | Lỗ 16 quý liên tiếp từ Q3/2022, lũy kế −190,2 tỷ | ✅ |

### 4.2 Phụ lục A: hình và bảng cho phần Findings

| Bản v5 | Từ v4 | Dữ liệu và nguồn | Kết quả |
|---|---|---|---|
| Table A1. DNSE at a glance | Table 1 | Vốn điều lệ 4.282,5 tỷ, tổng tài sản 15.208 tỷ, vốn chủ 5.440 tỷ (BCTC ✅). Tài khoản (BCTN ✅; 1,7 triệu là số báo chí 🟡). Sở hữu 49,7% (báo 🟡). Biểu phí, sản phẩm (trang DNSE ✅ᶜ). Vị thế Q2/2026 (HNX/HOSE ✅). Án phạt 802,5 triệu, QĐ 461/QĐ-XPHC ngày 17/8/2026 (đã kiểm bài báo, có số quyết định ✅/🟡) | ✅ (thêm nguồn cho dòng sở hữu) |
| Table A2. Evidence base | Table 2 | Mô tả dữ liệu. Kiểm số đếm: 867 review; 1.200 + 177 = 1.377; 332 + 518 + 205 = 1.055 | ✅ |
| Figure A1. Accounts and derivatives share | Fig 1 | 0,56 / 0,99 / 1,51 triệu (BCTN ✅); 1,20 (6/2025, VnExpress 🟡); 1,65 (3/2026, Vietstock 🟡); 1,70 (giữa 2026, báo 🟡). Thị phần phái sinh 4,01 → 25,38% (HNX ✅, đủ 10 quý) | ✅ (thêm nguồn cho các điểm lấy từ báo) |
| Figure A2. Value per DNSE account vs market | Fig 3 | Thị phần chia cho 12,7% | 🔧 Vẽ lại: phái sinh 2,00; HNX 0,23; tiền 0,18–0,27; dư nợ 0,11–0,14; LNTT 0,05–0,06 |
| Figure A3. Cash, lending and assets per account | Fig 4 | BCTC và BCTN | ✅ Tính lại đủ 14 điểm (ví dụ tiền/tài khoản 6/2026: 1.961 / 1,7 = 1,15 triệu; tài sản/tài khoản: 39,1 → 35,3 triệu) |
| Table A3. DNSE vs three peers | Table 5 | BCTC Q2/2026 | ✅ Dư nợ: 38.177 / 51.522 / 31.311 tỷ. LNTT: 2.158,6 / 2.097 / 1.378,4 tỷ. Tăng trưởng LNTT: ×3,93 / +21% / +57%; DNSE +7%. Thị phần HOSE ✅. 🔧 Dòng tiền của NĐT (lỗi #4) |
| Figure A4. Negative review themes | Fig 14 | CSV review | ✅ 278 review tiêu cực, 1.794 lượt hữu ích. Nhóm lòng tin: 24,1% số review, 42,9% lượt hữu ích |
| Figure A5. Reviews per month | Fig 15 | CSV review | ✅ T10–T11/2024: 91 review, 44% chỉ một từ. T6/2025: 29 review tiêu cực, tháng cao nhất |
| Figure A6. Revenue composition | Fig 8 | BCTC | ✅ (H1/2026: cho vay 40%, HTM 23%, môi giới 26%, FVTPL 9%) |
| Figure A7. Where each VND 100 goes | Fig 10 | BCTC | ✅ (H1/2026: LNTT 13, môi giới 31, vốn 38, quản lý 11) |
| **Table A4. Extra revenue and cost** | mới | BCTC | ✅ Tính từ dữ liệu: +284,7 doanh thu lõi, +289,3 chi phí lõi; vốn 52%, môi giới 42%, quản lý 6% |
| **Table A5. Brokerage H1/2026, largest brokers** | mới | BCTC của 42 công ty | ✅ DNSE −44,5 tỷ, lỗ lớn nhất (tiếp theo: PSI −17,1; KAFI −16,8). 19/42 công ty lỗ. Toàn ngành lãi +1.463 tỷ |
| Figure A8. Yields vs funding cost | Fig 11 | BCTC | ✅ Q2/2026: lợi suất cho vay 12,4%, HTM 6,0%, chi phí vốn 6,5% |
| Figure A9. Asset composition | Fig 12 | BCTC | ✅ (30/6/2026: cho vay 41%, HTM 38%, FVTPL 10%) |
| **Table A6. Funding cost and structure** | mới | BCTC; thuyết minh 8(b) BCTC soát xét | ✅ Tài sản cầm cố: 4.256,75 tỷ tiền gửi + 1.050 tỷ mệnh giá trái phiếu = **92,9%** của 5.714 tỷ HTM (đọc trực tiếp ảnh thuyết minh). Công ty CK ngân hàng chiếm **55%** phần tăng dư nợ Q2/2026 theo BCTC (báo chí ghi 62%) |
| Table A7. Summary of findings | Table 6 | Tổng hợp | 🔧 Viết lại theo 5 finding mới, số khớp thân bài |

### 4.3 Phụ lục B: hình và bảng cho Discussion và Recommendations

| Bản v5 | Từ v4 | Dữ liệu và nguồn | Kết quả |
|---|---|---|---|
| Table B1. Customer lifecycle | Table 7 | BCTN, review, báo | 🔧 Bỏ số cohort; sửa 16–34%; sửa tham chiếu sang Table D2 (lỗi #10, #12) |
| Table B2. Five-whys | Table 8 | Tổng hợp | 🔧 Triệu chứng dùng số đo trực tiếp. Why 1, 2, 4 gắn nhãn *Hypothesis*; Why 3 gắn *Measured*. Thêm lãi TCBS 6,0% |
| Figure B1. Returns on idle cash | Fig 21 | Trang DNSE (✅ trực tiếp: 1,8% cơ bản; +0,3 với số dư 1–500 triệu; +0–0,2 theo giao dịch; tối đa 4,3%). Trang TCBS iPower (✅ trực tiếp: 4,5% cơ bản; 6,0% với số dư 5–500 triệu và giao dịch dưới 500 triệu; tối đa 9,0%; số dư tối thiểu 5 triệu). Lãi tự động của ngân hàng 3,5–4,3% (blog DNSE 2025 🟡). Big4 6,8% (VietnamNet 🟡). Mức cao nhất 7,9% (VnExpress 🟡). NCB 9,35% (báo 🟡). CPI 4,45% (NSO ✅) | ✅/🟡 |
| Figure B2. Investor cash indexed | Fig 22 | DNSE từ BCTC; toàn ngành theo VnEconomy | ✅/🟡 DNSE −38,6%; VnEconomy −37,7%; tổng BCTC −40,7%. Cùng chiều |
| Table B3. Macro and banking | Table 9 | GDP, CPI (NSO ✅). Tín dụng, tiền gửi, lãi suất (NHNN qua báo 🟡). Tỷ trọng tăng dư nợ của CTCK ngân hàng (BCTC ✅ 55% / báo 🟡 62%) | 🔧 Bỏ các dòng giá vàng, NIM ngành, hộ thu nhập trên 5.000 USD (không dùng). Thêm dòng tỷ trọng tăng dư nợ |
| Table B4. Where savers keep money | Table 10 | Tiền gửi dân cư, tài khoản thanh toán (báo 🟡); tiền của NĐT 86,6 nghìn tỷ (🟡); số của DNSE ✅ | ✅ Các bội số đều tính lại khớp (5.609; 622; 44; 27; 1) |
| Table B5. Competitive map | Table 11 | Định tính; VPS 12,61% HOSE ✅ | 🔧 Lỗi #14 |
| Table B6. Comparable models abroad | Table 12 | Báo cáo của Robinhood, Trade Republic, Futu, FSA Japan, AMFI, Inc42, FINRA | 🟡 Nguồn chính thống của từng công ty/cơ quan quản lý, **chưa mở lại bản gốc trong phiên này**. Đã kiểm tính nhất quán nội bộ |
| Table B7. Transferability | Table 13 | Định tính | ✅ |
| Table B8. Target market scoring | Table 18 | Điểm do nhóm chấm | ✅ Kiểm lại số học: tổng có trọng số và tổng trọng số đều khớp |
| Table B9. Scope | Table 19 | Định tính | ✅ |
| Table B10. Problem prioritisation | Table 20 | Điểm do nhóm chấm | ✅ Số học khớp. Các mốc quy mô kiểm lại: 395 tỷ = 550 − 155; 83 tỷ = 1,7 triệu TK × 1 triệu × 4,88%; 89 tỷ = 2 × 44,5; khoảng 130 tỷ = 1,4 điểm × khoảng 9,4 nghìn tỷ |
| Figure B3. Plan implications | Fig 24 | BCTC và kế hoạch 2026 | ✅ 155 tỷ; 14,4 nghìn tỷ; 7,2 nghìn tỷ; 132 nghìn tỷ |
| Table B11. Problem statement | Table 21 | Tổng hợp | 🔧 Cập nhật số theo lỗi #1, #3, #7 |
| Table B12. Strategic alternatives | Table 22 | Điểm do nhóm chấm | ✅ Số học khớp |
| Figure B4. How Payday Portfolio works | Fig 25 | Sơ đồ thiết kế | ✅ Nhất quán với mục 4.1. Thêm nguồn Luật Bảo vệ dữ liệu cá nhân |
| Table B13. First 90 days | Table 23 | Thiết kế | ✅ |
| Table B14. Evidence behind design | Table 24 | Tổng hợp | 🔧 Bỏ số cohort; thêm lãi TCBS 6,0%; thêm nguồn |
| Table B15. Illustrative outcomes | Table 25 | Giả định kịch bản | 🔧 Lỗi #9. Mọi ô khác tính lại khớp (4,7 / 15,1 nghìn tỷ; 38 và 35 tỷ; 483 và 996 nghìn đồng) |
| Figure B5. Scenarios | Fig 26 | Như Bảng B15 | 🔧 Vẽ lại (lỗi #8) |
| Table B16. Feasibility | Table 26 | Thông tin DNSE công bố (khớp lệnh khoảng 4 ms, trung tâm dữ liệu) | ✅ᶜ |
| Table B17. Tests and measures | Table 27 | Thiết kế | ✅ |
| Figure B6. Validation roadmap | Fig 27 | Thiết kế | ✅ Nhất quán với mục 4.4 (pháp lý trước, pilot từ tháng 3) |

### 4.4 Phụ lục C đến H

| Bản v5 | Từ v4 | Kết quả |
|---|---|---|
| Table C1–C3. DNSE financial data | Table A1–A3 | ✅ **Tính lại toàn bộ ô từ BCTC: 0 ô lệch**, kể cả ROE, lợi suất, chi phí vốn, NIM |
| Table D1. Eight share measures | Table B1 | 🔧 Dựng lại. Tài khoản cùng ngày: 12,74% cuối 2025 (VSDC, BCTN) và 12,66% ngày 30/6/2026 (số VSDC 13.430.517 lấy từ ghi chú kiểm chứng ngày 24/9, chưa mở lại bản gốc 🟡). Tiền, dư nợ, LNTT trình bày theo hai tổng |
| Table D2. Active or funded accounts | Table B3 | ✅ Phiên 26/9 đã đọc bản gốc BCTN của DNSE, TCBS, VNDirect, SSI và KQKD Robinhood, Futu, Webull. 🟡 Số của TCBS (~34%) đọc từ biểu đồ không ghi nhãn (±0,02 triệu) |
| Table E1–E5. Reviews | Table 3, C1–C4 | ✅ Tính lại từ CSV: 867 → 670; 127 quảng cáo cho vay và 70 spam referral bị loại; điểm trung bình 3,22; 5,6% review DNSE nói về thưởng mở tài khoản, VPS 0,7%, FPTS 0% |
| Table F1–F3, Figure F1–F2. Findex | Table D1–D3, Fig 18–19 | ✅ Kiểm lại một số chỉ số với API World Bank, khớp: 37,0 / 36,9; 8,2 / 22,8; 19,8 / 19,6; 43,1. Phiên 23/9 đã kiểm đủ 796/796 giá trị |
| Table G1–G3. Methods | Table E1–E3 | 🔧 Bỏ định nghĩa ước tính giao dịch và cohort; thêm "Industry totals" và "Incremental cost decomposition"; sửa giả định tổng ngành; bỏ dòng giá cổ phiếu (không còn dùng) |
| Table H1. Data sources | Table F1 | ✅ |

## 5. Số liệu vẫn dựa vào báo chí hoặc công ty tự công bố: nên nói gì nếu bị hỏi

| Số liệu | Nguồn | Cách trả lời |
|---|---|---|
| 1,7 triệu tài khoản DNSE giữa năm 2026 | Thông cáo DNSE qua báo chí 🟡 | Số cuối 2025 lấy từ hai báo cáo thường niên (DNSE và VSDC) cho cùng tỷ trọng 12,7%. Kết luận không phụ thuộc số giữa năm |
| Tổng ngành 86,6 / 453,8 / 15.200 | Báo chí 🟡 | Báo cáo đã trình bày cả tổng cộng từ BCTC. Thị phần của DNSE thấp ở cả hai đầu khoảng |
| Số tài khoản VPBankS 1,3 triệu (5/2026), VPS 1,547 triệu (9/2025) | Báo chí; bản cáo bạch IPO | Chênh lệch ngày không đủ lấp khoảng cách 5–12 lần. Kể cả dùng số BCTN VPBankS cuối 2025 (1.144.508), dư nợ/tài khoản còn cao hơn (33 triệu) |
| TCBS khoảng 34% khách hoạt động | BCTN TCBS, đọc từ biểu đồ | Phía DNSE dùng định nghĩa rộng hơn ("dùng ít nhất 1 sản phẩm"), nên so sánh này thiên về có lợi cho DNSE |
| Lãi tiền gửi ngân hàng, tiền gửi dân cư, tăng trưởng tín dụng | Báo chí dẫn NHNN, FiinRatings 🟡 | Chỉ là bối cảnh; không finding nào phụ thuộc vào các số này |
| Số liệu công ty nước ngoài (Bảng B6) | Báo cáo công ty, cơ quan quản lý 🟡 | Chỉ dùng để rút bài học, không dùng làm bằng chứng cho vấn đề của DNSE |
| Điểm chấm trong B8, B10, B12 | Nhóm tự chấm | Có trọng số minh bạch và kiểm tra bằng trọng số đều; kết quả xếp hạng không đổi |
| Giả định kịch bản trong B15 | Giả định | Ghi rõ là giả định, có kiểm định ở Round 3 (test 4–6) |

## 6. Hình và bảng đã loại, và lý do

| Từ v4 | Lý do |
|---|---|
| Table 4 (cohort 2025) | Kết quả phụ thuộc giả định: từ +28 triệu tới âm. Không bảo vệ được bằng dữ liệu công khai |
| Table 14 (12 góc nhìn), Table 15 (Porter), Table 16 (SWOT), Table 17 (stakeholders) | Chỉ là khung phân tích, không có bằng chứng mới. Nhiều chi tiết chỉ có nguồn báo (khoản góp vào công ty tài sản số của Sun Group, sàn tín chỉ carbon…) |
| Table B2 cũ (cắt lớp ngành Q2/2026 theo báo) | Vài số lệch BCTC: SSI LNTT 1.511 so với 1.529 tỷ; +32% so với +28%. Thay bằng Bảng A5 và A6 lấy hoàn toàn từ BCTC |
| Figure 5 (phễu) | Dùng 12,3% và cách so với VN-Index +41%. Nội dung đã có ở Hình 1 và Hình A3 |
| Figure 13 (điểm review theo năm) | Đỉnh năm 2024 do review một từ đẩy lên; không còn dùng |
| Figure 16 (điểm theo hai store) | Trùng với Bảng E4 |
| Figure 17 (Findex theo thời gian) | Bước nhảy tỷ lệ tiết kiệm 2022–2024 có thể do thay đổi khảo sát |
| Figure 20 (chỉ số tầng 1) | Trùng với Hình A8 và Bảng C3 |
| Figure 23 (cơ cấu doanh thu broker nước ngoài) | Không cần cho lập luận |

## 7. Ghi chú kỹ thuật

- **Không đụng vào bản v4.** Word đang mở v4; bản v5 được dựng bằng một phiên Word ẩn riêng, không ảnh hưởng file đang mở.
- **Tài liệu tham khảo:** giữ 75, bỏ 25 mục không còn được trích. Đã kiểm để không bỏ nhầm các nguồn viết tắt (FINRA, AMFI) và các nguồn chỉ xuất hiện trong bảng phụ lục.
- **Script để dựng lại:** nằm trong `_v5_build/`.
  - `content_v5.py`: toàn bộ lời văn.
  - `build_v5.py`: dựng docx từ v4.
  - `word_pass.ps1`: đếm từ, lấy số trang, xuất PDF.
  - `make_figs.py`: vẽ lại 3 hình.
  - `v_*.py`: các bước kiểm chứng.
  - Hình mới nằm ở `fig/v5/`.
- **Việc còn lại trước khi nộp:**
  1. Điền tên team trên bìa (vẫn là "[Team name]").
  2. Đổi tên file theo quy định `[FBAR2_2026]_Tên team`.
  3. Nộp bản PDF.

# Review report Round 2: logic phân tích, khuyến nghị, code và data

*Lập ngày 15/10/2026 cho team KTQT FTUers. Đối tượng review: bản PDF đã nộp `report/FBAR2_2026_KTQT_FTUers.pdf` (30 trang, 27/09/2026), code trong `src/`, data trong `data/`.*

*Cách làm: đọc toàn văn bản nộp; đọc code; chạy lại pipeline ngày 14/10/2026 (614 ô của 13 bảng khớp, 3 khác biệt làm tròn đã biết); tính lại các con số chính từ data; tra cứu web ngày 14–15/10/2026 để kiểm tra bối cảnh và đối thủ.*

> **Lưu ý trước khi đọc.** Bản nộp khác bản nháp trong `docs/v5_revision_discussion_recommendation.md`. Bản nháp dùng Table B15/B17, còn bản nộp dùng **Table F5** (kịch bản), **Table F6** (7 giả định, ngưỡng), **target 85.000 tài khoản ≥10 triệu**, và có thêm **tier cam kết 3/6/12 kỳ**. Các file `weakness.md`, `final_report_review.md` và `v5_…` mô tả bản nháp. Review này bám theo bản nộp.

---

## 0. Kết luận nhanh

**Điểm mạnh lớn nhất** nằm ở phần chẩn đoán (Findings 1–4). Phần này dựa trên BCTC gốc đã đối chiếu với bản KPMG soát xét, mọi bảng có code tính lại, và luận điểm "càng gần tiền, DNSE càng nhỏ" rất thuyết phục. Đây là tài sản chính để mang sang Round 3.

**Ba điểm yếu cần sửa trước Round 3:**

| # | Vấn đề | Mức | Hệ quả cho Round 3 |
|---|---|---|---|
| 1 | Mô hình kịch bản (Table F5) giả định **mọi saver đóng góp đủ 18 tháng từ ngày đầu**. Nếu theo đúng lộ trình pilot của chính report, base case chỉ đạt khoảng **1,02 nghìn tỷ** thay vì 2,84 nghìn tỷ, và **khoảng 64.600 TK ≥10 triệu, dưới target 85.000** | Cao | Phải dựng lại thành mô hình cohort theo tháng; KPI cần horizon dài hơn hoặc mốc trung gian |
| 2 | Luận điểm "trust là vấn đề đặc thù DNSE" đúng cho năm 2025 nhưng **data 2026 đảo chiều**: trust giảm còn 14,7% (Play) và 12,5% (iOS) review tiêu cực, trong khi reliability lên **58,8%** và **75,0%**, cao nhất trong 3 app | Cao | Đây là ứng viên tốt nhất cho mục bắt buộc "What changed since Round 2". Reliability phải thành workstream chính |
| 3 | Bức tranh cạnh tranh (Table C3) **đã cũ ngay lúc nộp**: SSI iBoard có eSIP (thêm quỹ Dragon Capital từ 29/06/2026), **VPS Smart Indexing ra mắt 11/08/2026** với tích lũy định kỳ, MoMo có Túi Thần Tài kèm chứng chỉ quỹ | Cao | Câu "brokers' products start after a customer decides to invest" không còn đứng. Phải định vị lại điểm khác biệt của Payday |

**Bốn điểm yếu khác ở mức cao hoặc trung bình:**
- Bằng chứng hành vi bị áp sai: Madrian & Shea đo cơ chế mặc định opt-out, trong khi Payday là opt-in.
- Thiết kế tier mâu thuẫn, và con số "chi phí tối đa 5,6 tỷ/năm" không phải cận trên.
- Phí 0,5–1,0% bị áp lên cả phần ETF vốn miễn phí giao dịch.
- Chưa có chi phí, nên chưa có business case.

---

## 1. Report đã nộp nói gì (để cả team thống nhất)

- **Chẩn đoán:** DNSE mở 1/5 số TK mới cả nước năm 2025 và có 1,7 triệu TK giữa 2026, tức 12,3% thị trường. Nhưng DNSE chỉ giữ 2,3% tiền NĐT tại CTCK, 1,4% dư nợ margin và 0,6% LNTT ngành. Tháng 12/2025 chỉ 5,7% TK dùng sản phẩm và **1,8% (27.100 TK) có tài sản ròng ≥10 triệu**.
- **Hệ quả:** môi giới thấp hơn chi phí trực tiếp 16 quý liền (lũy kế −190 tỷ), ROE H1/2026 chỉ 3,8%, LNTT lõi đi ngang. Cost proxy 198 tỷ/năm đổ lên số ít TK có tiền, tương đương 7,3 triệu cho mỗi TK ≥10 triệu.
- **Ba nguyên nhân gốc (Figure 10):** (1) lệch vốn khách hàng, tức công cụ hút trader trẻ ít vốn (*giả thuyết*); (2) niềm tin gãy ở lần nạp tiền đầu (*có bằng chứng review*); (3) không có đường từ ý định đến nạp tiền đều đặn (*có bằng chứng về sản phẩm, còn là giả thuyết về khách hàng*).
- **Khuyến nghị:** Payday Portfolio, gồm các phần sau.
  - Ensa đề xuất 1 trong 3 danh mục mẫu trong khuôn khổ dịch vụ tư vấn có giấy phép ("Ý tưởng đầu tư"), khách xác nhận.
  - Lệnh chuyển tiền định kỳ đi vào tài khoản ảo (VA) mang tên khách. Mỗi khoản góp được rót vào lớp tài sản đang thiếu tỷ trọng nhất.
  - Tier cam kết 3/6/12 kỳ, được bỏ qua 1 tháng/năm.
  - Trust controls: bỏ phí đóng TK, bỏ thưởng có điều kiện, điều khoản trên một màn hình, dashboard tiền tách biệt.
  - Hệ sinh thái mở rộng: ZaloPay round-up, danh mục theo quy tắc, VNeID. Hạn mức tín dụng trên khoản tiết kiệm bị loại.
- **Định lượng (Table F5):** base 150.000 saver × 1,5 triệu/tháng × giữ 70% × 18 tháng = 2,84 nghìn tỷ. Phí 23 tỷ/năm, tier tối đa 5,6 tỷ/năm. TK ≥10 triệu tăng lên 177.100. **Target KPI: 85.000 TK ≥10 triệu sau 18 tháng.**
- **Kiểm chứng (Table F6):** 7 giả định, RCT 20.000 TK ngủ, 2 cổng (tuân thủ, độ tin cậy chuyển tiền 99,5%).

---

## 2. Review logic phân tích công ty DNSE

### 2.1 Điểm mạnh nên giữ nguyên

1. **Thang đo "càng gần tiền càng nhỏ"** (Figure 4, Table C1): 12,27% TK → 2,26% tiền NĐT → 1,39% dư nợ → 0,64% LNTT. Mỗi mẫu số đều có nguồn và thị phần luôn được tính trong sàn của nó. Đây là slide mở đầu tốt nhất cho Round 3.
2. **Số tài chính lấy từ BCTC gốc**, đối chiếu bản soát xét KPMG, có bảng đối chiếu số báo chí (A2). Report cũng bác bỏ con số "dự phòng +405%" vì không tái lập được.
3. **Hai phát hiện "cứng" nhất**, đều tính lại được từ data:
   - LNTT lõi (bỏ tự doanh) đi ngang ở 128–221 tỷ/năm từ 2022, trong khi doanh thu tăng hơn 3 lần.
   - Môi giới thấp hơn chi phí trực tiếp **16 quý liên tiếp, từ Q3/2022 đến Q2/2026, lũy kế −190,3 tỷ**. Tôi tính lại từ `dnse_financials.json` và ra đúng.
4. **Bậc chặn A3:** ít nhất 61% tài sản khách hàng nằm ở 1,8% số TK. Lập luận chặn biên này tốt vì không cần dữ liệu cấp khách hàng.
5. **Tách chu kỳ và cấu trúc:** tiền NĐT tại DNSE giảm từ 3.191,7 tỷ (Q3/2025) xuống 1.960,8 tỷ (Q2/2026), tức **−38,6%**, đúng bằng nhịp giảm của ngành (−37,7%). Vì vậy nhịp giảm gần đây là chu kỳ, còn việc thị phần tiền thấp là cấu trúc. Tôi đã tính lại và khớp.
6. **Làm sạch review có test** (37 case). Report chứng minh làm sạch thay đổi kết luận (spam 46% và 54% năm 2022–2023) và kiểm độ nhạy của quy tắc "generic" (A4).
7. **Phân loại measured và hypothesis**, kèm bảng giải thích thay thế (F2). Kỷ luật nhận thức này rubric thưởng điểm.

### 2.2 Vấn đề logic (xếp theo mức độ)

#### L1 (Cao). "Trust complaints are specific to DNSE" phụ thuộc vào giai đoạn

Tính lại từ `reviews_flagged_*.csv` (review tiêu cực 1–2 sao đã làm sạch):

| DNSE, Google Play | Số review tiêu cực | Trust | Reliability |
|---|---:|---:|---:|
| 2024 | 25 | 24,0% | 24,0% |
| H1/2025 (đợt thưởng 100k) | 62 | **54,8%** | 25,8% |
| H2/2025 | 29 | 24,1% | 37,9% |
| 2026 (đến 21/9) | 34 | **14,7%** | **58,8%** |

| Năm 2026 | Reliability, Google Play | Reliability, App Store | Trust, Google Play | Trust, App Store |
|---|---:|---:|---:|---:|
| **DNSE** | **58,8%** (n=34) | **75,0%** (n=24) | 14,7% | 12,5% |
| VPS | 43,8% (n=80) | 50,5% (n=99) | 1,2% | 7,1% |
| FPTS | 33,3% (n=9) | 45,5% (n=22) | 0,0% | 4,5% |

Thêm hai quan sát:
- **Thiên lệch "helpful votes":** review tiêu cực năm 2025 trung bình có 12,3 vote, năm 2026 chỉ 2,9. Vì vậy con số "trust chiếm 43% helpful votes" bị chi phối bởi các review lan truyền mạnh của đợt thưởng 2025, cộng với thời gian tích lũy vote dài hơn.
- **Đỉnh reliability 2026 tập trung vào tháng 3/2026** trên cả hai store. Trên iOS, 7 review rơi vào phiên bản 2.113.28, trong đó 6 là reliability. Sau đó app nhảy lên bản 3.x. Ngoài đỉnh này, reliability vẫn rải đều các tháng.

**Đánh giá:** câu trong report "*Since 2025, reliability complaints have been at least as common at VPS (46%) as at DNSE (38%)*" đúng với cửa sổ gộp 2025–2026, nhưng **đảo chiều nếu chỉ xét 2026**. Mẫu 2026 nhỏ (34 và 24 review), nên đây là tín hiệu chứ chưa phải kết luận. Tuy vậy, tín hiệu đủ mạnh để phải nói ra ở Round 3:
- Trust layer vẫn cần (DNSE vẫn cao hơn đối thủ), nhưng **vấn đề nổi trội đã chuyển sang reliability**. Rủi ro này đánh thẳng vào cơ chế "chuyển tiền ngày lương".
- Đây là thay đổi dựa trên bằng chứng mới, đúng loại thay đổi mà tiêu chí 25 điểm khen ("*justifies retained or revised choices using findings*").
- Việc cần làm: đọc tay 58 review tiêu cực năm 2026 trên cả hai store để gắn nguyên nhân cụ thể (đăng nhập/OTP, lệnh chậm, lỗi sau cập nhật…). Không suy đoán nguyên nhân khi chưa đọc.

#### L2 (Cao). Bức tranh cạnh tranh và "market gap" đã cũ

Report (mục 1.2, Table C3) viết rằng khoảng trống nằm giữa ngân hàng và CTCK, *"whose products start after a customer decides to invest"*, và mô tả VPS là *"Trading-first; no link from a salary"*. Tại thời điểm nộp (27/09/2026) đã có:
- **SSI iBoard:** tính năng **eSIP** đầu tư định kỳ chứng chỉ quỹ, thêm quỹ Dragon Capital từ 29/06/2026 bên cạnh quỹ SSIAM. Quỹ SSIBF miễn phí phát hành cho SIP.
- **VPS Smart Indexing (VSI), ra mắt 11/08/2026:** sản phẩm ủy thác theo mô hình direct indexing. Khách sở hữu trực tiếp cổ phiếu, danh mục do VPS phối hợp Quỹ Sài Gòn (SGC) xây dựng và vận hành. Có **cơ chế tích lũy định kỳ**: tiền nạp định kỳ được phân bổ tự động theo chiến lược.
- **MoMo:** Túi Thần Tài từ 10.000đ (đến 6,1%/năm) và chứng chỉ quỹ của DCVFM, IPAAM, SSIAM, VCBF.
- **TCBS:** Fundmart (31 quỹ, khoảng 55% NAV quỹ mở trong nước), iTracker (danh mục tự động hóa), iPower (tiền nhàn rỗi).

*Bổ sung 16/10:* phía ngân hàng cũng đã nối lương với đầu tư. VCB Digibank cho tự trích tiền mua quỹ VCBF từ 100.000đ/kỳ, không eKYC lại; VPBank ra "Hũ Mục Tiêu" (12/09/2026); VinaCapital VinaSIP dùng lệnh chuyển tiền định kỳ từ ngân hàng từ năm 2021. Câu *"banks hold salaries but offer little investment"* vì vậy cũng không còn đúng.

**Đánh giá:** khoảng trống thật hẹp hơn nhiều so với cách report mô tả. Chuyển tiền định kỳ đã thành chuẩn. Trong phạm vi đã kiểm, chưa thấy sản phẩm nào kết hợp **nhiều lớp tài sản trong một kế hoạch** + **tư vấn theo mục tiêu, khách xác nhận** + **thưởng cho sự bền bỉ** + **nằm trong app giao dịch zero-fee** (chi tiết: `competitor_features.md`). Giám khảo rất có thể biết VSI, vì VPS là CTCK dẫn đầu thị phần môi giới cơ sở. Phân tích chi tiết ở `review_payday.md` §4.

#### L3 (Trung bình–Cao). Con số trung tâm 1,8% thiếu mốc so sánh

Report không có tỷ lệ TK ≥10 triệu của VPS hay TCBS. Bằng chứng so sánh duy nhất là dư nợ/TK. Con số này là trung bình bị khách lớn kéo lên, và chính report thừa nhận điều đó ở ghi chú Table C2. Hơn nữa, tiền NĐT trung bình toàn ngành chỉ khoảng **6,25 triệu/TK** (86,6 nghìn tỷ / 13,85 triệu TK). Như vậy có thể phần lớn TK toàn thị trường cũng dưới 10 triệu tiền mặt.

→ Ở Round 3, **không nói "1,8% thấp bất thường so với ngành"** nếu không có số. Nên nói "1,8% là điểm xuất phát do chính DNSE công bố, và mục tiêu là cải thiện chỉ số DNSE đã tự đo".

#### L4 (Trung bình). Phép thử "chu kỳ thị trường bị bác bỏ" còn yếu

Report viết: "tài sản/TK giảm 9,5% năm 2025 trong khi VN-Index tăng 41%". Nhưng tài sản/TK bị pha loãng cơ học bởi 518.514 TK mới gần như rỗng, và đó chính là luận điểm cần chứng minh. Phép thử vì thế hơi vòng tròn.

Phép phân tách theo cohort cho kết quả phụ thuộc mốc so sánh. Tài sản khách hàng cuối 2024 ≈ 994.811 TK × 39,1 triệu ≈ 38,9 nghìn tỷ (số 39,1 triệu lấy từ BCTN 2025, ghi trong `diary.md`).
- Nếu tài sản khách cũ tăng theo VN-Index (+41%), khách cũ đã có khoảng 54,8 nghìn tỷ, lớn hơn tổng thực tế 53,5 nghìn tỷ. Nghĩa là TK mới gần như không mang tài sản, hoặc khách cũ đã rút tiền.
- Nếu tăng theo HNX (+9,4%) hoặc UPCoM (+27,7%), mỗi TK mới mang khoảng **7–21 triệu**.

→ Đưa phép phân tách này vào appendix Round 3 để trả lời Q&A. Không dùng câu một dòng.

#### L5 (Trung bình). Suy luận nhân quả từ VPS còn yếu

Câu "khách chịu lỗi kỹ thuật dễ hơn điều khoản bất công", rút ra từ việc VPS nhiều complaint reliability hơn nhưng cho vay/TK gấp 5 lần, bị nhiễu bởi khác biệt về quy mô, lịch sử, mạng lưới môi giới và sản phẩm. Với data 2026 (reliability của DNSE lớn hơn VPS), lập luận này càng yếu. Chỉ nên dùng ở mức "consistent with".

#### L6 (Trung bình). Mô hình phân khúc Findex

- **Đếm trùng tiêu chí.** "Wages into an account" (`fin32.acc`) đã nằm trong Index B, lại được thêm làm tiêu chí riêng. "Saved for old age" (`fin17f`) đã nằm trong Index A, cũng được thêm làm tiêu chí riêng. Xem `src/analysis.py:259-260` và `src/pipeline/04_segment_model.py:53-68`.
- `fin17a` vừa được cộng (trong Index A) vừa bị trừ (activation gap = account − fin17a).
- Tiêu chí quy mô (số triệu người) khiến nửa lớn hơn của mỗi cặp gần như luôn thắng.
- 12 phân khúc chồng lấn nhau (Richest 60% ∩ In labour force ∩ Secondary+), trong khi Findex chỉ cắt một chiều một lúc, n≈1.000. Nhóm 15–24 tuổi chỉ khoảng 180 người trả lời.
- **Quan trọng nhất:** bước nhảy từ "22,1 triệu người VN có TK nhưng không tiết kiệm chính thức" sang "TK ngủ của DNSE là người đi làm muốn đầu tư" chưa có dữ liệu nào nối hai đầu. Report đã gắn nhãn hypothesis, điều này đúng.

→ Kết luận "người đi làm, thu nhập khá" vẫn hợp lý, vì các tiêu chí tương quan cao nên kết quả bền với cả 4 bộ trọng số. Nhưng không nên trình bày bảng xếp hạng như một phát hiện định lượng chính xác. Round 3 cần thêm bằng chứng để nối Findex với tệp DNSE: survey hoặc phỏng vấn nếu kịp; nếu không, dùng khảo sát đã công bố và tiếng nói khách trong review (`competitor_features.md` §6).

#### L7 (Trung bình). Nhãn bằng chứng chưa nhất quán

Root cause 1 (lệch vốn khách hàng) chỉ dựa trên một số liệu báo chí (Gen Z chiếm 31,5% TK giữa 2025, VnExpress). Thân bài gọi đúng là hypothesis, nhưng Executive summary viết như kết luận: *"DNSE's tools attract young traders with little capital."* Cần giữ nhãn nhất quán ở mọi chỗ.

#### L8 (Thấp). Câu chữ và số nhỏ

- "VPS lends 5 times more": thực tế là 5,5 lần (20,2 / 3,7).
- "12-month deposit rates at state banks reached about 6.8 per cent": đầu 10/2026, Big4 niêm yết 5,9% tại quầy cho kỳ hạn 12 tháng, chứng chỉ tiền gửi 7,4%. Con số 6,8% cần ghi rõ kênh và ngày áp dụng.
- Target 85.000 (exec summary) đặt cạnh 177.100 của base case (Table 1) dễ gây hiểu nhầm. Thực chất 85.000 xấp xỉ kịch bản Conservative (87.100), nên cần ghi rõ.

### 2.3 Kiểm chứng số liệu trong văn bản

Mọi con số chính trong thân bài đều khớp với data hoặc với phép tính lại.

| Con số trong report | Tính lại | Kết quả |
|---|---|---|
| 12,3% TK; 2,3% tiền NĐT; 1,4% dư nợ; 0,6% LNTT | 1,70/13,85; 1.960,8/86.600; 6.303,1/453.800; 97,4/15.200 | ✓ |
| TK ×33,8, LNTT lõi ×2,7 (2021–2025) | 1.512.920/44.727; 194,0/72,5 | ✓ |
| Proxy 198 tỷ; 7,3 triệu/TK ≥10 triệu; 0,13 triệu/TK | 197,5/27.100; 197,5/1.512.920 | ✓ |
| 16 quý môi giới lỗ, −190 tỷ | Q3/2022–Q2/2026, −190,3 | ✓ |
| Tiền NĐT bình quân 6,3 triệu so với 1,2 triệu; gấp 5,4 lần | 86,6 nghìn tỷ/13,85 triệu; 1,96/1,7 | ✓ |
| Margin 40%, môi giới 26% doanh thu H1/2026 | 336,1/848,2; 222,1/848,2 | ✓ |
| 20% kế hoạch LNTT 2026 sau H1 | 111,6/550 | ✓ |
| Tier ≤5,6 tỷ; thưởng 100k × 518.514 = 51,9 tỷ | 150.000 × 1,5 triệu × 2,5% | ✓ về số học (xem R3: sai về khái niệm) |
| Open API từ 03/2027 | Thông tư 64/2024: ngân hàng phải tuân thủ trước 01/03/2027 | ✓ |

---

## 3. Review khuyến nghị và góc nhìn chính sách

### 3.1 Điểm mạnh

- **Ánh xạ pháp lý cẩn thận** (Table G1):
  - Tư vấn nằm trong giấy phép tư vấn, có thu thập thông tin khách theo Thông tư 121/2020 Điều 24.
  - Không đầu tư thay khách (Điều 4), nên mọi thay đổi phải được xác nhận bằng một chạm.
  - Loại hạn mức tín dụng trên chứng chỉ quỹ mở (Điều 27; chứng chỉ quỹ mở không niêm yết).
  - Không làm "quản lý danh mục" (Luật Chứng khoán 2019 Điều 72), nên bản Smart Vault được giao cho công ty quản lý quỹ.
- **Điều kiện thiết kế suy ra từ vấn đề** (mục 3.6, 4 điều kiện), và mỗi thành phần trả lời một điều kiện. Cấu trúc này đúng tinh thần "Insight → Design decision".
- **Rút bài học từ review:** bỏ thưởng có điều kiện, bỏ phí đóng TK, đặt cổng 99,5% cho chuyển tiền, báo UBCKNN trước khi ra mắt. Những điểm này trúng tiền lệ phạt tháng 8/2026 (QĐ 461/QĐ-XPHC: 802,5 triệu, trong đó 275 triệu vì 3 dịch vụ ứng trước không báo cáo).
- **RCT 3 nhánh có ngưỡng** (Table F6) là xương sống tốt cho tiêu chí 30 điểm của Round 3.

### 3.2 Vấn đề

#### R1 (Cao). Bằng chứng hành vi bị áp sai

Table 1 dùng Madrian & Shea (2001), *tham gia tăng từ 37% lên 86%*, làm bằng chứng cho "lệnh chuyển tiền ngày lương". Nhưng nghiên cứu đó đo **tự động ghi danh (opt-out)**, tức chủ lao động đặt sẵn mặc định. Payday lại là **opt-in**: khách phải tự tạo lệnh chuyển tiền trong app ngân hàng, nên hiệu ứng mặc định không chuyển sang được.

Bằng chứng gần với Payday hơn:
- Tài khoản tiết kiệm cam kết (Ashraf et al., 2006): khoảng **28%** người được nhân viên ngân hàng mời trực tiếp chịu mở.
- SMarT (Thaler & Benartzi, 2004): 78% tham gia khi được chuyên viên tư vấn mời gặp trực tiếp.
- Kênh số tiếp cận TK ngủ sẽ cho tỷ lệ thấp hơn nhiều so với cả hai trường hợp trên.

**Benchmark nội bộ:** Tài khoản Không Ngủ đơn giản hơn, miễn phí, nhưng chỉ đạt **12.100 đăng ký sau khoảng 6 tháng (0,8% số TK)**. Base case của Payday cần khoảng 1/11 số TK ngủ ghi danh trong 18 tháng, tức gấp khoảng 10 lần mức đó.

→ Round 3: chỉ dùng Madrian & Shea cho **kênh qua chủ lao động/payroll**, nơi có thể tạo mặc định thật. Đặt kỳ vọng ghi danh theo benchmark nội bộ.

#### R2 (Cao). Mô hình kịch bản tĩnh làm phóng đại kết quả

`analysis.scenarios()` tính tài sản = số saver × đóng góp × tỷ lệ giữ × 18 tháng, tức **mọi saver bắt đầu từ tháng 1**. Theo lộ trình F2 của chính report (pilot tháng 3–6, mở rộng từ khoảng tháng 7), kết quả như sau:

| Kịch bản | Số tháng để chạm 10 triệu | Report (tĩnh) | Ramp đều tháng 1–18 | Ramp sau pilot, tháng 7–18 |
|---|---:|---|---|---|
| Conservative | 16,7 | 0,65 nghìn tỷ; 87.100 TK | 0,34 nghìn tỷ; 33.800 TK | 0,23 nghìn tỷ; **27.100 TK (không tăng)** |
| Base | 9,5 | 2,83 nghìn tỷ; 177.100 TK | 1,50 nghìn tỷ; 102.100 TK | **1,02 nghìn tỷ; 64.600 TK** |
| Upside | 5,0 | 10,80 nghìn tỷ; 327.100 TK | 5,70 nghìn tỷ; 260.400 TK | 3,90 nghìn tỷ; 227.100 TK |

*Cùng input với Table F5; saver ghi danh đều theo tháng; chưa tính lợi nhuận đầu tư.*

→ Trên chính timeline của report, **target 85.000 TK ≥10 triệu sau 18 tháng không đạt được trong base case**. Kịch bản Conservative gần như không thêm TK nào qua ngưỡng 10 triệu trong 18 tháng. Round 3 phải dùng mô hình cohort theo tháng, đặt KPI 24–36 tháng hoặc mốc trung gian (xem `plan_payday.md` §5).

#### R3 (Cao). Thiết kế tier mâu thuẫn, và "cận trên" không phải cận trên

Tier thưởng bằng **lãi suất tiền nhàn rỗi**: Starter +0,3–0,5 điểm; Committed trả 4,3% "*without the current balance and trading conditions*". Trong khi đó tiền Payday chỉ nằm ở tài khoản nhàn rỗi 1–3 ngày trước khi được đầu tư. Có hai cách hiểu, cách nào cũng có vấn đề:
1. Thưởng chỉ áp cho tiền Payday đang chờ: phần thưởng gần như bằng 0, nên động lực yếu.
2. Thưởng áp cho toàn bộ tiền nhàn rỗi: khách đang có số dư lớn chỉ cần đặt lệnh 500.000đ/tháng trong 12 tháng là mở khóa 4,3% cho toàn bộ tiền mặt. Phần chênh so với mức họ đang hưởng (thường 1,8–2,3%) do DNSE trả.

Con số "*at most VND 5.6 billion a year*" (`analysis.py:289`) chỉ tính một tháng đóng góp cho mỗi saver, nên **không phải cận trên** theo cách hiểu thứ 2. Cơ chế này cũng đi ngược tinh thần "thưởng cho tiền ở lại và được đầu tư".

→ Chuyển phần thưởng sang những thứ gắn với **tiền đã đầu tư**: giảm phí quỹ, ưu tiên Trứng Vàng kỳ mới, đánh giá danh mục. Mọi ưu đãi lãi phải có trần, ví dụ chỉ áp cho số dư Payday hoặc tối đa 50 triệu.

#### R4 (Cao). Doanh thu mỏng và chưa có chi phí

- Phí 0,5–1,0% bị áp lên **toàn bộ** tài sản (`analysis.py:288`), gồm cả:
  - **ETF VN30**: DNSE miễn phí giao dịch, nên doanh thu gần như bằng 0.
  - **Trứng Vàng**: DNSE thu chênh lệch lãi chứ không thu phí.
- SIP chứng chỉ quỹ trên thị trường thường miễn phí phát hành (ví dụ SSIBF), và tier Disciplined lại giảm thêm phí.
- Base case 23 tỷ/năm chỉ bằng khoảng **4% kế hoạch LNTT 2026** (550 tỷ), mà chưa trừ chi phí xây dựng, vận hành, thu hút khách.
- Ví dụ minh họa (`plan_payday.md` §6) cho thấy: với lợi suất gộp 0,6–1,0%/năm, Payday còn **lỗ lũy kế khoảng 11–54 tỷ sau 36 tháng** tùy chi phí thu hút. Trong các tổ hợp thuận lợi (CAC 50 nghìn đồng hoặc lợi suất 1,0%), doanh thu tháng chỉ bù được chi phí tháng từ khoảng tháng 24–34. Với lợi suất 0,6% và CAC 150 nghìn đồng thì chưa hòa trong 36 tháng.

→ Không thể bán Payday bằng "phí". Executive summary của Round 3 **bắt buộc** nêu "*required investment and expected return*", nên phải có slide đầu tư và lợi nhuận kèm giá trị gián tiếp.

#### R5 (Trung bình). Môi trường lãi suất là gió ngược

- Đầu 10/2026: Big4 trả 5,9% cho kỳ hạn 12 tháng tại quầy, chứng chỉ tiền gửi 7,4%, nhiều ngân hàng từ 7% trở lên. Kỳ hạn 1 đến dưới 6 tháng bị trần 4,75%.
- Trứng Vàng: 4,2% đến 5,3%. Đây là mức trên trang giới thiệu, chưa rõ ngày cập nhật, cần kiểm lại trong app.
- TCBS cho biết bán chứng chỉ quỹ Q2/2026 chậm lại vì phải cạnh tranh với lãi tiền gửi. Doanh thu môi giới cộng lưu ký giảm 21% so với cùng kỳ, chủ yếu do mảng phân phối quỹ.

→ Danh mục Conservative có thể có lợi suất kém tiền gửi. Đúng nhóm khách sợ rủi ro mà Payday nhắm tới sẽ hỏi "sao không gửi ngân hàng?". Value proposition phải nói được giá trị ngoài lợi suất: kỷ luật, mục tiêu, thanh khoản, phần cổ phiếu cho mục tiêu dài hạn.

#### R6 (Trung bình). Trách nhiệm pháp lý khi AI tư vấn

Đề xuất danh mục là hoạt động tư vấn đầu tư, nhưng report chưa nói **ai chịu trách nhiệm**. Cần nêu rõ:
- Người hành nghề có chứng chỉ tư vấn thiết kế và phê duyệt 3 danh mục mẫu.
- Ensa chỉ thu thập thông tin và giải thích.
- Có lưu log hội thoại.
- Có cơ chế xử lý khi mô hình ngôn ngữ trả lời sai.

Giám khảo đóng vai CTO hoặc người có kiến thức pháp lý gần như chắc chắn sẽ hỏi điểm này.

#### R7 (Trung bình). Chất lượng tệp 1,4 triệu TK ngủ

Nhiều TK được mở trong đợt thưởng 100k: trust complaints chiếm 54,8% review tiêu cực H1/2025, và 70 review referral spam đã bị loại trên Play. Nhóm này đi tìm thưởng chứ không nhất thiết muốn đầu tư. Report đặt đúng giả định #1 (≥30% có ý định đầu tư) lên đầu Table F6, nhưng **base case không phản ánh rủi ro này**.

#### R8 (Thấp–Trung bình). Mốc Open API 03/2027 đúng, nhưng kết nối không tự động

Điều khoản chuyển tiếp của Thông tư 64/2024 yêu cầu ngân hàng tuân thủ trước 01/03/2027, và sự đồng ý của khách để truy vấn thông tin có hiệu lực tối đa 180 ngày. Tuy vậy, bên thứ ba vẫn phải ký thỏa thuận với từng ngân hàng, mà ngân hàng có động cơ phòng thủ CASA (loạt bài "cuộc chiến quản trị CASA" tháng 6–7/2026). Câu "*every competitor can link salary accounts from March 2027*" nên viết mềm hơn.

*Đính chính:* lượt trước tôi ghi trong `round3_core_tech_risk.md` rằng mốc 03/2027 "không xác nhận được". Điều đó sai, và file đó đã được sửa.

### 3.3 Góc nhìn chính sách (dùng cho Q&A và Round 3B)

- **Thuận chiều chính sách:**
  - Phổ cập tài chính: 70,5% người lớn có tài khoản nhưng chỉ 43,1% tiết kiệm chính thức.
  - Khuyến khích đầu tư dài hạn của nhà đầu tư cá nhân trong bối cảnh nâng hạng thị trường (FTSE, hiệu lực 21/09/2026).
  - Định hướng Open Banking 2026–2030 của NHNN.
- **Ràng buộc:**
  - CTCK không được nhận tiền gửi.
  - Trần lãi tiền gửi không kỳ hạn 0,5%; kỳ hạn 1 đến dưới 6 tháng 4,75%.
  - UBCKNN giám sát chặt các dịch vụ "ứng trước" sau vụ phạt tháng 8/2026.
  - Ngân hàng phòng thủ CASA.
- **Lập luận tranh biện:** Payday không cạnh tranh với ngân hàng về lãi tiền gửi. Nó là **đường nối** giữa tài khoản lương ở ngân hàng và đầu tư dài hạn. Ngân hàng giữ được CASA ở VA của họ, DNSE giữ được tài sản đầu tư. Đây là luận điểm "đôi bên cùng thắng" khi gặp câu hỏi về phòng thủ CASA.

---

## 4. Review code, cách lấy data và insight từ data

### 4.1 Đánh giá tổng thể

Đây là một replication package tốt hơn mức thường gặp:
- Một lệnh chạy lại toàn bộ, khoảng 16 giây.
- 13 bảng dữ liệu được tính lại và so khớp từng ô với bản nộp (614 ô, 3 khác biệt làm tròn đã biết).
- Có test cho bước làm sạch review (37 case).
- Dữ liệu nhập tay đều có cột nguồn.
- Người viết review được ẩn danh (hash).
- Định nghĩa các chỉ số được viết ngay trong code.

Pipeline chạy được trên Python 3.14 và Windows sau 2 sửa nhỏ ngày 14/10: cài đủ package và đổi tên file report.

### 4.2 Danh sách vấn đề

| ID | Mức | Vị trí | Vấn đề | Đề xuất |
|---|---|---|---|---|
| K1 | Cao | `src/analysis.py:278-293` | `scenarios()` là mô hình tĩnh: không có ramp ghi danh, không có lợi nhuận đầu tư, không có chi phí. Phí áp cho mọi tài sản, và "cận trên" tier sai (xem R2–R4) | Viết lại thành mô hình cohort theo tháng, ví dụ `src/payday_model.py` đọc `data/manual/payday_assumptions.csv`; tách lợi suất theo lớp tài sản |
| K2 | Cao | `src/report/content.py:7-109` | Mọi con số trong văn bản đều gõ tay; `check_tables.py` chỉ kiểm bảng. Chạy `--fetch` sẽ đổi bảng và hình nhưng chữ thì giữ nguyên, và không ai được báo | Lập "claims registry" (tên → hàm tính → định dạng) và script `check_text.py` so khớp chuỗi trong `content.py` |
| K3 | Trung bình | `run_all.py:75` | `check_tables` chạy với `optional=True`. Khi có khác biệt bất thường (exit 1), pipeline in "(skipped…)" rồi vẫn "Done", tức một regression bị báo nhầm là "skipped" | Bỏ `optional`, hoặc in "FAILED" và trả exit khác 0 ở cuối |
| K4 | Trung bình | `src/analysis.py:251-269`; `04_segment_model.py:53-68` | Đếm trùng `fin32.acc` và `fin17f`; `fin17a` mang hai dấu ngược nhau; tiêu chí quy mô chi phối thứ hạng | Bỏ 2 tiêu chí trùng; báo cáo sai số chuẩn xấp xỉ √(p(1−p)/n), ví dụ nhóm 15–24 (n≈180) có sai số chuẩn khoảng 3,7 điểm ở p=50%, tức khoảng tin cậy 95% xấp xỉ ±7 điểm |
| K5 | Trung bình | `src/analysis.py:180-227`; `make_tables.table_D2` | Cột reliability/trust của Table D2 chỉ lấy từ Google Play, còn cột mean lấy từ App Store, trong khi caption ghi cả hai nguồn | Ghi rõ nguồn từng cột, hoặc gộp cả file iOS (`reviews_flagged_ios_*.csv`) |
| K6 | Trung bình | `src/analysis.py:197-227` | "Share of helpful votes" không chuẩn hóa theo thời gian phơi nhiễm (2025: 12,3 vote/review; 2026: 2,9) | Báo cáo theo năm, hoặc chỉ so trong cùng năm |
| K7 | Trung bình | `src/pipeline/03_reviews_clean.py` | Gắn theme bằng từ khóa nhưng chưa đo precision/recall | Hai người gán nhãn tay 100–150 review, đo mức đồng thuận, báo precision/recall cho từng theme |
| K8 | Trung bình | `01b_dnse_financials_fetch.py:14-21` (tương tự ở 01c, 01d) | Gọi endpoint nội bộ của Vietcap IQ (không phải API công khai) với User-Agent/Referer/Origin giả lập trình duyệt. Dễ gãy khi Vietcap đổi hệ thống, có rủi ro về điều khoản sử dụng | Ghi rõ trong README; chuẩn bị phương án dự phòng (thư viện **vnstock** nguồn VCI, hoặc PDF BCTC trên ir.dnse.com.vn); lưu bản kéo thô theo ngày |
| K9 | Trung bình | `run_all.py:51-58` | `--fetch` ghi đè `data/` tại chỗ, không giữ snapshot, nên lỡ chạy là mất khả năng tái lập bản nộp | Ghi vào `data/snapshots/<ngày>/`, kiểm tra xong mới thay |
| K10 | Thấp | `brokers.py:105-106, 125-141`; `04_segment_model.py:97` | Hằng số gõ tay: 453.800 tỷ dư nợ ngành, 32 mã FTSE, 80,6 triệu người lớn; `DNSE_ACCOUNTS_AR` trùng với `dnse_accounts.csv`, tạo ra hai nguồn sự thật | Chuyển hết vào `data/manual/*.csv` kèm cột nguồn |
| K11 | Thấp | `src/tables/export_tables.py:20` | Tên file report gõ cứng, đã gây lỗi trên Windows ngày 14/10 | Glob `report/*.docx`, hoặc đặt hằng số trong `config.py` |
| K12 | Thấp | `requirements.txt` | Chỉ có cận dưới (`>=`), nên hình không giống từng byte giữa các máy (README đã thừa nhận) | Thêm `requirements.lock` (`pip freeze`) cho bản nộp |
| K13 | Thấp | — | Chỉ bước làm sạch review có unit test. `funding_cost`, `cost_of_funds_pct`, `nim_q` chưa có test, chỉ dựa vào regression ở cấp bảng | Thêm 3–5 test với số tính tay từ BCTC Q2/2026 |
| K14 | Thông tin | `02b_playstore_scrape_python.py` | Bản kéo Google Play không lưu phiên bản app (App Store thì có), nên không phân tích complaint theo bản phát hành được | Lưu thêm trường `appVersion` hoặc `reviewCreatedVersion` mà thư viện google-play-scraper trả về; kéo lại review đến giữa 10/2026 cho Round 3 |

### 4.3 Insight nào vững, insight nào mong manh

| Mức | Insight |
|---|---|
| **Vững** (giữ và dùng mạnh) | LNTT lõi đi ngang; môi giới lỗ 16 quý (−190,3 tỷ); thang thị phần theo chiều định tính; tiền NĐT giảm cùng nhịp ngành; chi phí vốn tăng; bậc chặn 61% tài sản; rating giảm 2024→2025 (bền với 3 quy tắc); làm sạch thay đổi kết luận |
| **Có điều kiện** (dùng kèm cảnh báo) | So sánh trên mỗi TK với đối thủ (trung bình, ngày lệch nhau); 1,8% (thiếu mốc so sánh); cost proxy (đúng xu hướng, mức chỉ là ước lượng); thứ tự phân khúc (gần đúng) |
| **Mong manh** (phải sửa trước Round 3) | "Trust đặc thù DNSE" (phụ thuộc giai đoạn); kịch bản Payday (mô hình tĩnh); cận trên chi phí tier; phép thử chu kỳ thị trường; doanh thu theo phí 0,8% |

---

## 5. Mang gì sang Round 3

- **Giữ:** chẩn đoán (Findings 1–4), thang đo "gần tiền", KPI TK ≥10 triệu (đổi horizon), trust controls, ánh xạ pháp lý (Table G1), RCT có cổng.
- **Sửa:** kịch bản chuyển sang mô hình cohort; thiết kế tier; trích dẫn bằng chứng hành vi; bức tranh cạnh tranh; insight 2026 về reliability.
- **Thêm:** chi phí và ROI; go-to-market năm đầu; roadmap theo phase; demo (journey, service blueprint, wireframe); một ít bằng chứng sơ cấp (survey hoặc phỏng vấn).
- **Ứng viên cho slide "What changed since Round 2"** (yêu cầu tối thiểu #6):
  1. Insight: complaint chuyển từ trust (đợt thưởng 2025) sang reliability (2026).
  2. Cạnh tranh: SSI eSIP và VPS Smart Indexing đã ra mắt, nên định vị được làm hẹp lại cho chính xác.
  3. Thiết kế: tier thưởng cho tiền đã đầu tư, có trần; danh mục mặc định thiên trái phiếu; thêm kênh chủ lao động ở phase sau.
  4. Mô hình: cohort theo tháng có chi phí; KPI theo giai đoạn.
  5. Giữ nguyên: target (người đi làm 22–40 có TK ngủ), cơ chế lõi, phạm vi pháp lý, kèm lý do giữ.

---

## Nguồn

- [Thông tư 64/2024/TT-NHNN triển khai Open API ngành Ngân hàng (Thư viện Pháp luật)](https://thuvienphapluat.vn/van-ban/Tien-te-Ngan-hang/Thong-tu-64-2024-TT-NHNN-trien-khai-giao-dien-lap-trinh-ung-dung-mo-nganh-Ngan-hang-641360.aspx)
- [Từ 01/3/2025, triển khai Open API trong ngành Ngân hàng (Luật Việt Nam)](https://luatvietnam.vn/tin-van-ban-moi/tu-01-3-2025-trien-khai-open-api-trong-nganh-ngan-hang-186-100851-article.html)
- [Thêm quỹ Dragon Capital, SSI iBoard mở rộng sản phẩm đầu tư trên nền tảng số](https://doanhnhan.baophapluat.vn/them-quy-dragon-capital-ssi-iboard-mo-rong-san-pham-dau-tu-tren-nen-tang-so.html)
- [SSIBF Fund Factsheet 04/2026](https://www.ssi.com.vn/upload/files/QuanLyQuy/SSIBF%20Fund%20Factsheet%2004_2026_VN.pdf)
- [VPS chính thức ra mắt sản phẩm VPS Smart Indexing (Thời báo Tài chính)](https://thoibaotaichinhvietnam.vn/vps-chinh-thuc-ra-mat-san-pham-vps-smart-indexing-202120.html)
- [VPS chính thức ra mắt sản phẩm VPS Smart Indexing (Tin nhanh Chứng khoán)](https://www.tinnhanhchungkhoan.vn/vps-chinh-thuc-ra-mat-san-pham-vps-smart-indexing-post395704.html)
- [Thị phần VPS tiếp tục dẫn đầu, ra mắt dịch vụ quản lý danh mục định kỳ (VSI)](https://doanhnhan.baophapluat.vn/thi-phan-vps-tiep-tuc-dan-dau-ra-mat-dich-vu-quan-ly-danh-muc-dinh-ky-vsi.html)
- [Sàn đầu tư MoMo, Túi Thần Tài (VNBA)](https://vnba.org.vn/vi/san-dau-tu-momo--toi-uu-loi-nhuan-cho-nha-dau-tu-tu-nguon-von-nho-9271.htm)
- [TCBS 2Q2026 Earnings Call](https://www.tcbs.com.vn/wp-content/uploads/2026/07/TCBS_2Q2026-Earnings-Call_VN-1.pdf)
- [TCBS báo lãi quý II/2026 cao nhất lịch sử (VietnamFinance)](https://vietnamfinance.vn/tcbs-bao-lai-quy-ii-2026-cao-nhat-lich-su-vuot-2000-ty-dong-d147607.html)
- [Lãi suất đầu tháng 10/2026: tiết kiệm giữ nhịp ổn định, chứng chỉ tiền gửi hút khách](https://thitruongtaichinhtiente.vn/lai-suat-dau-thang-10-2026-tiet-kiem-giu-nhip-on-dinh-chung-chi-tien-gui-hut-khach-85944.html)
- [Cuộc chiến quản trị CASA, phần 2 (Saigon Times)](https://thesaigontimes.vn/cuoc-chien-quan-tri-casa-phan-2-dien-bien-theo-tung-nhom-ngan-hang-ra-sao/)
- [DNSE bị phạt 802,5 triệu đồng, phải dừng một số dịch vụ ký quỹ](https://vnbusiness.vn/dnse-bi-phat-8025-trieu-dong-phai-dung-mot-so-dich-vu-ky-quy.html)
- [DNSE giới thiệu sản phẩm "Trứng vàng"](https://kinhtechungkhoan.vn/dnse-gioi-thieu-san-pham-trung-vang-voi-loi-suat-dau-tu-hap-dan-1043755.html)
- Madrian & Shea (2001); Thaler & Benartzi (2004); Ashraf, Karlan & Yin (2006), như trong danh mục tài liệu tham khảo của report.
- Data nội bộ: `data/reviews_flagged_*.csv`, `data/reviews_flagged_ios_*.csv`, `data/reviews_raw_ios_*.csv`, `data/dnse_financials.json`, `data/manual/*.csv` (tính lại ngày 14–15/10/2026).

# DNSE — Các vấn đề & Bài toán BA về chiến lược sản phẩm số

*Ghi chú làm việc nội bộ cho team FBA Season 6, Round 2. Lập ngày 24/09/2026.*
*Hạn nộp: **21:00 ngày 27/09/2026**. Báo cáo tối đa 3.500 từ, viết bằng tiếng Anh, nộp PDF.*

**Nguồn tổng hợp:** data pack Excel, báo cáo docx, tra cứu web ngày 23–24/09/2026, câu trả lời cho các câu hỏi phụ trong ba phiên làm việc khác, và question booklet Round 2.
**Quy ước:** số liệu có nguồn được liệt kê ở cuối file. Ký hiệu 🔎 đánh dấu giả thuyết hoặc suy luận cần kiểm chứng; đề bài chấm điểm việc tách bạch fact và giả thuyết.

---

# SECTION 1 — THÔNG TIN DNSE VÀ CÁC VẤN ĐỀ

## 1.1 Hồ sơ công ty

| Hạng mục | Thông tin |
|---|---|
| Tên | CTCP Chứng khoán DNSE (tên cũ: Chứng khoán Đại Nam), mã **DSE** trên HOSE |
| Thành lập | 2007, vốn ban đầu 38 tỷ đồng. Chuyển sang mô hình fintech khoảng 5 năm gần đây |
| Vốn điều lệ | ~4.282,5 tỷ đồng sau đợt phát hành quyền mua hoàn tất tháng 3/2026 (lúc IPO là 3.300 tỷ) |
| Sở hữu | Encapital Financial Technology + Encapital Holdings giữ **67,1%**. PYN Elite Fund mua khoảng 12% vốn chủ vào tháng 1/2024 |
| Lãnh đạo | Chủ tịch HĐQT **Nguyễn Hoàng Giang**, Tổng giám đốc **Nguyễn Ngọc Linh**, Giám đốc Công nghệ **Nguyễn Đức Bình** |
| Nhân sự | 151–300 người (ITviec) |
| Kênh phân phối | 100% qua app/web Entrade X, **không có chi nhánh** |
| Khách hàng | 1,5 triệu tài khoản (cuối 2025) → **hơn 1,7 triệu** (H1/2026), khoảng 12% tài khoản toàn thị trường |
| Cơ cấu khách hàng | Khoảng **800.000 khách Gen Z, chiếm ~70%** tổng số khách hàng (tính đến Q1/2025) |

## 1.2 Các mốc chính

| Thời điểm | Sự kiện |
|---|---|
| 2007 | Thành lập với tên Chứng khoán Đại Nam, vốn 38 tỷ |
| ~2020 | Encapital tái định vị thành công ty chứng khoán công nghệ, ra mắt Entrade X với **miễn phí giao dịch trọn đời** |
| 12/2022 | Ra mắt **Margin Deal**, hệ thống đầu tiên ở Việt Nam quản lý khoản vay margin theo từng giao dịch |
| 6/2023 | Ra mắt **Future X** (phái sinh), tỷ lệ ký quỹ 18,48% |
| 9/2023 | Bị UBCKNN phạt lần 1: 125 triệu đồng (vi phạm quy định nhận lệnh) |
| 11/2023 | Lãi margin 11,5%; mức 5,99% cho 10 mã. Lợi nhuận 9 tháng 2023 tăng 334% |
| 1/2024 | Tích hợp Open API với ZaloPay; PYN Elite đầu tư |
| 2024 | Bị phạt lần 2: 125 triệu đồng (cho vay margin mã L18 sau khi HNX đã loại mã này khỏi danh sách) |
| 1/7/2024 | Niêm yết HOSE, giá IPO 30.000đ, định giá ~9.900 tỷ. **Phiên đầu giảm 4,7%** so với giá IPO |
| 2024 | Trợ lý AI **Ensa** đạt giải "Giải pháp AI đột phá lĩnh vực tài chính" (AI Awards 2024) |
| Q4/2024 | Lần đầu vào top 2 thị phần phái sinh (9,98%) |
| 5/2025 | Ra mắt bảng giá dành riêng cho Gen Z. Trả thay khách phí VSD và phí quản lý ký quỹ phái sinh trong giai đoạn chuyển sang hệ thống KRX (5–9/2025) |
| 21/11/2025 | Sự kiện DNSE Future Tech Summit, công bố tốc độ xử lý lệnh **3,9 ms** |
| Q4/2025 | **LNST quý giảm 72%** so với cùng kỳ |
| Q4/2025–3/2026 | Phát hành 85,65 triệu cổ phiếu quyền mua giá 15.000đ (tỷ lệ 4:1), thu ~1.275 tỷ. Phải **gia hạn** thời gian chào bán |
| 26/3/2026 | ĐHCĐ: mục tiêu LNTT 550 tỷ, trái phiếu 3.500 tỷ, lập công ty tại IFC |
| **17/8/2026** | **Bị phạt lần 3: 802,5 triệu đồng, buộc dừng 3 dịch vụ phái sinh** (chi tiết ở mục 1.7B) |
| 21/9/2026 | FTSE Russell nâng hạng Việt Nam lên thị trường mới nổi thứ cấp |

## 1.3 Hệ sinh thái sản phẩm số trên Entrade X

| Sản phẩm | Cơ chế | Vai trò trong hành trình khách hàng |
|---|---|---|
| **Entrade X** | App giao dịch cơ sở. Mở tài khoản online trong 3–5 phút (eKYC, NFC), miễn phí giao dịch trọn đời | Thu hút khách |
| **Future X** | Phái sinh. Ký quỹ 18,48% (đòn bẩy ~5–7 lần), giao dịch trên cùng tài khoản cơ sở, không phải chuyển tiền giữa hai tài khoản, miễn phí giao dịch | Tạo tương tác, tạo thị phần |
| **Margin Deal** | Vay theo từng giao dịch: mỗi deal có tỷ lệ vay, lãi suất, mức call riêng, lãi/lỗ theo thời gian thực | Kiếm tiền (lãi vay) |
| **Tài khoản không ngủ** | Sinh lời trên tiền nhàn rỗi: **1,8% cố định + tối đa 1,5% theo số dư + tối đa 1,0% theo giá trị giao dịch = tối đa 4,3%/năm**. Không yêu cầu số dư tối thiểu, trần 30 tỷ, trả lãi hàng tháng | Giữ tiền trên nền tảng |
| **Trứng Vàng (Egg X)** | Đầu tư trái phiếu niêm yết theo kỳ hạn, từ 1 triệu đồng, tự động tái tục. Mã đầu tiên là trái phiếu Agribank; dự kiến mở rộng sang **chứng chỉ quỹ** | Giữ tiền trên nền tảng |
| **Ensa** | Chatbot "môi giới ảo": phân tích kỹ thuật, phân tích cơ bản, gợi ý mã | Tương tác (thay môi giới người) |
| **SENSES / Lệnh AI** | Tổng hợp thông tin cho hơn 2.000 mã; tối ưu lệnh bằng thuật toán | Tương tác |
| **Lightspeed API** | API RESTful cho giao dịch thuật toán. Đối tác: ZaloPay, TradingView, FiinTrade, WiGroup | Tạo khối lượng (bot, trader chuyên nghiệp) |
| **Bảng giá Gen Z**, cuộc thi "Cưỡi sóng phái sinh" | Mùa 2 có 16.346 người tham gia, tạo 32.382 tỷ giá trị giao dịch trong một tháng | Cộng đồng, thu hút khách |
| IPO/PO online | Mua cổ phiếu, trái phiếu phát hành lần đầu ngay trên app | Bán chéo |

## 1.4 Hạ tầng công nghệ

- **Kiến trúc:** microservices, backend Go, frontend React / React Native, Docker, Kubernetes, GitLab CI. Dùng AWS cho các phần không phải giao dịch.
- **Ràng buộc pháp lý:** hệ thống giao dịch bắt buộc đặt tại trung tâm dữ liệu trong nước. DNSE chạy Kubernetes trên máy chủ vật lý riêng nhưng vận hành theo cách của cloud.
- **Case study AMD:** gộp **100 máy chủ Intel Xeon 8280 xuống 14 máy AMD EPYC 9965**, hiệu năng tương đương. Kết quả: −86% số máy chủ, −69% điện năng, **−41% tổng chi phí sở hữu 3 năm**.
- **Tốc độ xử lý lệnh:** 3,9 ms.
- **Kế hoạch:** trung tâm dữ liệu thứ hai tại TP.HCM để giảm độ trễ; tích hợp VNeID (mục tiêu 4/2026); sẵn sàng cho giao dịch T+0.

## 1.5 Kết quả kinh doanh gần đây (tỷ VND)

| Chỉ tiêu | FY2025 | Q4/2025 | Q1/2026 | Q2/2026 | H1/2026 |
|---|---|---|---|---|---|
| Doanh thu hoạt động | 1.467 (+77%) | 434 (+85,8%) | 395 (+62%) | 453,1 (+56%) | 848,2 (+58,9%) |
| LNTT | 340,2 (+50%) | **11,7** | **14,2** | 98,9 (+8,7%) | 113,1 |
| Biên LNTT | 23,2% | **2,7%** | **3,6%** | 21,8% | 13,3% |
| Doanh thu môi giới | 404 | ~125 | 119,5 | 102,5 (+38,8% YoY) | 222,1 (+80,8% YoY) |
| Chi phí môi giới | — | **~150 (+198%)** | **137,8 (+125%)** | — | — |
| Dư nợ margin + ứng trước | 5.832 | 5.832 | 5.910 | 6.303 (+25% YoY) | 6.303 |
| Thị phần phái sinh | 21,47% (cả năm) | 24,26% | 25,50% | 25,38% | — |

*Chú thích: "—" là không có số liệu công bố. Doanh thu môi giới Q4/2025 (~125 tỷ) được tính lại trong phiên làm việc khác, cần đối chiếu với báo cáo tài chính.*

## 1.6 Kế hoạch 2026 và cam kết lúc IPO

**Nghị quyết ĐHCĐ 26/3/2026:**
- Mục tiêu doanh thu 1.736 tỷ (+18,2%), LNTT 550 tỷ (+61,7%).
- Trái phiếu 3.500 tỷ (2.500 tỷ không chuyển đổi + 1.000 tỷ chuyển đổi), dùng cho cho vay margin và công nghệ.
- Lập công ty chứng khoán tại Trung tâm Tài chính Quốc tế (IFC); phạm vi hoạt động gồm cả quản lý quỹ.
- **10 tỷ đồng cho 1% cổ phần VNDA** (công ty tài sản số), với vai trò kết nối, không trực tiếp vận hành.
- Tham gia sàn tín chỉ carbon; ESOP 4,28 triệu cổ phiếu; cổ tức tối đa 7%.
- Chủ tịch nêu **chủ trương tự lập công ty quản lý quỹ mới thay vì mua bán sáp nhập**, vì định giá các công ty quỹ hiện quá cao. Đây là chủ trương, chưa có nghị quyết riêng.

**So với cam kết lúc IPO (7/2024, cho giai đoạn 5 năm):**

| Chỉ tiêu | Cam kết đến ~2029 | Hiện tại |
|---|---|---|
| Khách hàng | 5 triệu | 1,7 triệu |
| Lợi nhuận/năm | 2.400 tỷ (100 triệu USD) | Mục tiêu 2026 là 550 tỷ; H1 đạt 113 tỷ |
| Vốn hóa | 72.000 tỷ (3 tỷ USD) | **~9.400 tỷ** (ước tính của tôi: 428 triệu cổ phiếu × 22.000đ ngày 16/9/2026) |

## 1.7 Các vấn đề của DNSE

### A. Vấn đề rút ra từ phân tích data pack và báo cáo

**P1 — Vấn đề gốc: thu hút được tài khoản, không thu hút được tiền.**
DNSE có 12,27% số tài khoản nhưng chỉ 2,88% giao dịch trên HNX, dưới 2,94% trên HOSE, và 1,39% dư nợ cho vay. Quy về tỷ số so với thị trường: một tài khoản DNSE giao dịch bằng **0,23** và vay bằng **0,11** một tài khoản trung bình.
Tính trên mỗi tài khoản: doanh thu 498.900đ/nửa năm, doanh thu môi giới 130.600đ, tài sản khách hàng 34,7 triệu đồng.

**P2 — Tăng trưởng phi kinh tế.**
Doanh thu tăng 58,9% nhưng biên LNTT giảm từ 23,2% xuống 13,3%. Riêng Q1/2026: chi phí hoạt động +120%, chi phí môi giới +125%, dự phòng tự doanh +405%.

**P3 — Kế hoạch 2026 gần như chắc trượt.**
H1 mới đạt 20,6% mục tiêu lợi nhuận. H2 cần 436,9 tỷ LNTT, tức **3,86 lần H1**, hay ~218 tỷ mỗi quý — gấp 2,2 lần quý tốt nhất công ty từng có.

**P4 — Doanh thu phụ thuộc bảng cân đối.**
Lãi cho vay (39,6%) cộng thu nhập đầu tư (22,8%) chiếm **62,4% doanh thu H1**. Phần này phụ thuộc vào quy mô vốn và diễn biến thị trường, không phụ thuộc vào giao dịch của khách hàng.

**P5 — Tập trung vào phái sinh, và mảng này đang chững lại.**
Thị phần phái sinh 25,38%, trong khi thị phần cổ phiếu HNX chỉ 2,88%. Từ 5/2025 DNSE còn trả thay khách phí ký quỹ phái sinh, tức mảng mạnh nhất lại tốn thêm chi phí.

**P6 — Thua ở mảng mà ngành kiếm tiền.**
Dư nợ cho vay: TCBS 51.500 tỷ, SSI 40.500, VPBankS 38.200, DNSE 6.303. Tăng trưởng LNTT Q2/2026 so với cùng kỳ của DNSE là **+8,7%, thấp nhất nhóm so sánh** (VPBankS gấp ~4 lần, VNDirect +127%, VPS +57%, SSI +32%, TCBS +21%).

**P7 — Lỗi app và lỗi mở tài khoản lặp lại.**
Trong review tiêu cực, 25,8% về crash hoặc lỗi đăng nhập, 19,6% về mở tài khoản (eKYC, OTP, NFC). Các lỗi này xuất hiện theo từng đợt qua nhiều năm, cho thấy chưa được sửa dứt điểm. Với công ty không có chi nhánh, app lỗi nghĩa là không phục vụ được khách hàng.

**P8 — Khách hàng mất lòng tin.**
16,2% review tiêu cực cáo buộc lừa đảo, xoay quanh hai điểm: thưởng 100.000đ nhưng phải nạp tối thiểu 2 triệu, và phí đóng tài khoản 100.000đ. Spam chiếm **27,1% review của DNSE**, so với 7,0% ở VPS và 4,5% ở FPTS. Điểm review có nội dung thực chất giảm từ **4,07 sao (2024) xuống 2,36 sao (2025)**.

**P9 — Thu hút khách từ nhóm có ít tiền nhất.**
Nhóm 15–24 tuổi có khoảng cách lớn nhất giữa thói quen dùng công nghệ và khoản tiền có thể đầu tư (**35,1 điểm**), priority score chỉ 2,25 (nhóm ưu tiên đạt 9,0–9,3). Nhóm này chiếm khoảng 70% khách hàng DNSE.

### B. Vấn đề tìm thêm trên mạng

**N1 — Vi phạm pháp luật lặp lại, lần gần nhất nặng nhất.**
DNSE đã bị phạt ba lần: 9/2023 (125 triệu), 2024 (125 triệu), và **17/8/2026: Quyết định 461/QĐ-XPHC, tổng phạt 802,5 triệu đồng**. Lần thứ ba gồm các vi phạm:
- 275 triệu: cung cấp *"ứng lãi vị thế, ứng rút ký quỹ ngoài giờ và ứng trước ký quỹ cho hoạt động môi giới chứng khoán phái sinh"* **từ 1/1/2024 đến 16/6/2026** mà không báo cáo UBCKNN trước.
- 187,5 triệu: cho vay margin đối với **người nội bộ và người có liên quan của người nội bộ**.
- 137,5 triệu: cho khách đặt lệnh mua khi chưa đủ tiền.
- 137,5 triệu: cho khách giao dịch ký quỹ vượt sức mua.
- 65 triệu: vi phạm khác.
- **Biện pháp khắc phục:** *"buộc dừng cung cấp dịch vụ ứng lãi vị thế, ứng rút ký quỹ ngoài giờ, ứng trước ký quỹ cho hoạt động môi giới chứng khoán phái sinh"*.

Vì sao quan trọng:
1. Ba dịch vụ bị buộc dừng chính là các tiện ích giúp khách phái sinh rút lãi, rút ký quỹ và vào lệnh dễ hơn, tức một phần lợi thế cạnh tranh ở mảng phái sinh.
2. 🔎 Thời gian cung cấp các dịch vụ này (1/2024–6/2026) trùng với giai đoạn thị phần phái sinh tăng từ 4% lên 25%. Đây là trùng thời điểm, **chưa chứng minh được quan hệ nhân quả**.
3. Cho vay margin người nội bộ là dấu hiệu yếu về quản trị công ty.
4. **Mọi sản phẩm tài chính số mới đều phải báo cáo UBCKNN trước khi triển khai.** Đây là ràng buộc trực tiếp cho bất kỳ khuyến nghị sản phẩm nào.

**N2 — Lợi nhuận đã sụt hai quý liên tiếp, không chỉ riêng Q1/2026.**
Q4/2025: LNTT 11,7 tỷ, LNST giảm 72%. Tổng chi phí 425,6 tỷ (+112%), trong đó chi phí môi giới gần 150 tỷ (+198%). Nguyên nhân chính được nêu là trích lập dự phòng tự doanh. Cách giải thích biên thấp ở Q1/2026 là "cú sốc một quý" vì vậy không đứng vững: biên LNTT dưới 4% trong **hai quý liền**.

**N3 — Mảng môi giới lỗ ngay ở cấp chi phí trực tiếp.**
Q4/2025: thu ~125 tỷ, chi ~150 tỷ. Q1/2026: thu 119,5 tỷ, chi 137,8 tỷ. Miễn phí giao dịch đang được bù bằng chính lợi nhuận của công ty.

**N4 — Chi phí vốn tăng nhanh hơn dư nợ.**
Vay ngắn hạn tăng từ 6.494 lên 9.302 tỷ (Q4/2025). Theo tổng hợp báo chí, chi phí lãi vay Q2/2026 tăng 165,6% và chi phí tài chính H1 tăng 210%, trong khi dư nợ margin chỉ tăng 25%. 🔎 Biên lãi ròng từ cho vay đang bị thu hẹp, nên con số "lợi suất cho vay ~11%" trong báo cáo (tính trước chi phí vốn) đang phóng đại mức sinh lời thực. Cần đối chiếu với báo cáo tài chính gốc.

**N5 — Miễn phí giao dịch không còn là khác biệt.**
Từ 2024: MBS miễn phí trọn đời cả cơ sở lẫn phái sinh cho tài khoản mới; TCBS miễn phí không thời hạn mọi sản phẩm; SSI miễn phí 12 tháng; VPS miễn phí 6 tháng; JBSV và Pinetree miễn phí trọn đời. Chủ tịch MB Lưu Trung Thái: phí giao dịch rồi sẽ về 0 như phí chuyển khoản.

**N6 — Phái sinh chững lại, đối thủ lấy lại đà.**
Q2/2026: VPS tăng từ 33,34% lên 33,84%, DNSE giảm nhẹ từ 25,5% xuống 25,38%, SSI tăng từ 7,2% lên 8,21%, HSC đạt 9,23%. Thanh khoản thị trường phái sinh Q2 **giảm 22,1%** so với Q1.
*Điều chỉnh so với nhận định trước:* doanh thu môi giới Q2 của DNSE giảm 14,2% so với Q1, **ít hơn mức giảm 22% của thị trường**. Phần giảm này chủ yếu do thị trường, không phải do DNSE mất khách.

**N7 — Thị trường vốn chưa tin vào câu chuyện tăng trưởng.**
- Phiên chào sàn giảm 4,7% so với giá IPO.
- Giá ~22.000đ (16/9/2026), so với giá IPO 30.000đ; sau điều chỉnh cho đợt quyền mua, giá IPO tương đương ~27.000đ, nên giá hiện tại **thấp hơn ~18%**.
- Vốn hóa ~9.400 tỷ, **thấp hơn định giá IPO 9.900 tỷ, dù đã huy động thêm ~1.275 tỷ**.
- Đợt chào bán quyền mua phải gia hạn, và một cổ đông lớn đăng ký chuyển nhượng quyền mua.

**N8 — Còn rất xa cam kết IPO** (bảng ở mục 1.6).

**N9 — Sản phẩm sinh lời kém cạnh tranh.**
Tài khoản không ngủ tối đa 4,3%, nhưng 1,0 điểm trong đó phụ thuộc vào giá trị giao dịch, nên người chỉ gửi tiền không đạt mức tối đa. TCBS iPower trả tối đa **6%**. Các gói sinh lời tự động của ngân hàng: Techcombank tối đa 4%, VPBank 3,5%, VIB tối đa 4,3%.

**N10 — Bị mạo danh để lừa đảo.**
Có website giả mạo DNSE (dnsevn.com) để đánh cắp thông tin đăng nhập. Vấn đề này cộng thêm vào sự mất lòng tin đã thấy trong review.

### C. Bảng tổng hợp

| # | Vấn đề | Loại | Mức độ | DNSE tự kiểm soát được? | Sản phẩm số giải quyết được? |
|---|---|---|---|---|---|
| P1 | Tài khoản nhiều nhưng ít tiền | Mô hình kinh doanh | Rất cao | Có | **Có — trọng tâm** |
| P2–P3, N2 | Biên lợi nhuận sụp, trượt kế hoạch | Tài chính | Rất cao | Một phần | Gián tiếp |
| N3, N5 | Môi giới lỗ; miễn phí không còn khác biệt | Mô hình kinh doanh | Cao | Có | Có (kiếm tiền theo cách khác) |
| N4 | Chi phí vốn tăng | Tài chính | Cao | Một phần | Có (tiền gửi của khách là nguồn vốn rẻ hơn) 🔎 |
| P5, N6 | Tập trung phái sinh, phái sinh chững | Chiến lược | Cao | Thấp | Một phần (T+0) |
| N1 | Vi phạm pháp luật, dịch vụ bị buộc dừng | Pháp lý, quản trị | Cao | Có | **Là ràng buộc** cho mọi sản phẩm mới |
| P7 | Lỗi app, lỗi mở tài khoản | Vận hành | Cao | Có | Có |
| P8, N10 | Mất lòng tin | Thương hiệu | Cao | Có | Có (minh bạch điều khoản) |
| P9 | Thu hút sai nhóm khách | Chiến lược | Trung bình–Cao | Có | Có |
| N9 | Sản phẩm sinh lời kém cạnh tranh | Sản phẩm | Trung bình | Có | **Có — trọng tâm** |
| N7–N8 | Giá cổ phiếu yếu, xa cam kết IPO | Thị trường vốn | Trung bình | Gián tiếp | Gián tiếp |

---

# SECTION 2 — BÀI TOÁN BA: CHIẾN LƯỢC SẢN PHẨM SỐ

## 2.1 Đề bài Round 2 yêu cầu gì

Theo question booklet:
- **Vai trò:** business analyst của một tổ chức fintech đang đánh giá thị trường mục tiêu. Dataset là nền tảng chính. Phải kết hợp bối cảnh vĩ mô, xu hướng ngân hàng, hành vi khách hàng, và phân tích **vĩ mô + cạnh tranh để tìm khoảng trống thị trường**.
- **Đầu ra:** đề xuất thị trường mục tiêu tiềm năng nhất cho ban lãnh đạo, kèm **một hướng sơ bộ** (sản phẩm, dịch vụ, cải tiến vận hành, chiến dịch…) để phát triển tiếp ở Round 3A. Round 2 chỉ là **ý tưởng chiến lược**, chưa phải giải pháp hoàn chỉnh.
- **Các phần bắt buộc:** bối cảnh, phân tích dữ liệu và insight, ưu tiên một vấn đề, các phương án chiến lược và đánh đổi, khuyến nghị sơ bộ, hướng kiểm chứng (giả định, kết quả kỳ vọng, KPI, việc cần test).
- **Bắt buộc tách bạch** fact, giả định, giả thuyết. Dùng nhiều hình trực quan.
- **Rubric:** hai tiêu chí điểm cao nhất là *Analytical findings & accuracy* (15) và *Problem/opportunity prioritization* (15). Các tiêu chí còn lại 10 điểm mỗi tiêu chí.

**Hệ quả cho việc chọn hướng:** "chiến lược sản phẩm số" khớp trực tiếp với phần *Preliminary recommendation*, và với tiêu chí chọn công ty *Development potential* (đủ cơ sở để biến thành sản phẩm ở Round 3).

## 2.2 Các câu hỏi phụ đã hỏi và kết luận rút gọn

**Q1. Lợi nhuận của DNSE đến từ đâu, xu hướng theo từng nguồn thế nào?**
- Báo cáo tài chính chỉ chia **doanh thu** theo nguồn, không chia **lợi nhuận** theo mảng.
- Lãi cho vay là nguồn lớn nhất và tăng nhanh nhất, nhưng thị phần cho vay đứng yên ~1,39%: tăng vì thị trường margin lớn lên, không phải vì DNSE có thêm khách vay.
- Phí môi giới đi ngang, chủ yếu đến từ phái sinh.
- Thu nhập tự doanh tăng gấp đôi nhưng rủi ro cao.
- Doanh thu tăng thêm 100 đồng thì lợi nhuận chỉ tăng ~5 đồng (so Q2/2026 với cùng kỳ).

**Q2. Vì sao lợi nhuận giảm mà DNSE vẫn giữ miễn phí giao dịch?**
Bốn lý do:
1. Cam kết "trọn đời" không thể rút lại mà không mất uy tín với 1,7 triệu khách.
2. Miễn phí giờ là chuẩn chung của ngành; bỏ nó thì DNSE mất định vị duy nhất.
3. Công ty đang coi đây là giai đoạn chiếm thị phần, sẽ thu tiền sau qua margin; ĐHCĐ 2026 nêu rõ ý định nhân bản mô hình phái sinh sang cơ sở.
4. Cần câu chuyện tăng trưởng để phát hành 3.500 tỷ trái phiếu.

*Cập nhật từ tra cứu mới:* biên lợi nhuận thấp kéo dài **hai quý liền** (Q4/2025 và Q1/2026), và mảng môi giới lỗ ở cấp chi phí trực tiếp. Chiến lược "chịu lỗ để chiếm thị phần" chưa có dấu hiệu thu hồi được tiền.

**Q3. Có phải DNSE đang "nuôi" Gen Z (nghèo bây giờ, giàu sau) cộng với đón đầu thị trường phái sinh?**
- Về lý thuyết, đây là chiến lược hợp lý ("capture young, monetise later"). Nhưng **dữ liệu hiện có đi ngược lại**:
  - Mô hình Findex xếp nhóm 15–24 thấp nhất về ưu tiên (2,25 so với 9,0–9,3).
  - Review cho thấy một phần khách đến vì săn thưởng, không vì ý định đầu tư.
  - Chi phí chuyển đổi thấp: một người có thể mở tài khoản ở nhiều công ty, nên giàu lên rồi họ vẫn có thể chuyển sang nơi khác.
  - Findex là số liệu một thời điểm, không chứng minh được một nhóm người sẽ giàu lên theo thời gian.
- **Điều kiện để giả thuyết này đúng:** phải có một sản phẩm **giữ lại phần tiền tăng thêm** khi thu nhập của Gen Z tăng. DNSE chưa có sản phẩm này ở quy mô đáng kể. Đây là cầu nối trực tiếp sang khuyến nghị ở mục 2.6.

**Q4. DNSE cạnh tranh với VPS ở phái sinh thế nào? Vì sao hút khách ít tiền mà lại tập trung vào phái sinh?**
- **Cần sửa tiền đề:** trong phái sinh, ký quỹ là tiền nhà đầu tư tự nộp vào VSD (~17–18,5% giá trị hợp đồng), không phải khoản vay của công ty chứng khoán. Vì vậy phái sinh là mảng **ít tốn vốn** nhất với DNSE. Mảng tốn vốn là margin cổ phiếu cơ sở.
- *Điều chỉnh sau tra cứu mới:* DNSE đã dùng vốn của mình qua các dịch vụ "ứng trước ký quỹ" và "ứng lãi vị thế", và đây chính là các dịch vụ bị **buộc dừng từ 8/2026**. Từ nay phái sinh sẽ thực sự ít tốn vốn, nhưng cũng kém tiện lợi hơn.
- **Cách DNSE thắng thị phần:**
  - Phí 0 đồng, và trả thay phí VSD đúng lúc chuyển sang KRX (thị phần tăng từ 17,33% lên 23,67% cùng giai đoạn; trùng thời điểm, chưa chứng minh nhân quả).
  - Công nghệ: API cho bot, tự động cắt lỗ, không phải chuyển tiền giữa tài khoản.
  - Cộng đồng: cuộc thi "Cưỡi sóng phái sinh". Chủ tịch nói tỷ lệ khách phái sinh rời bỏ "gần như bằng 0".
- **Vì sao khách ít tiền đi cùng phái sinh:** chỉ cần vài chục triệu đồng là có đòn bẩy mà không phải trả lãi vay. Thị phần phái sinh lại dễ nhìn thấy, tốt cho thương hiệu sau IPO.
- **Chỗ không khớp:** kênh thu hút khách (trẻ, ít tiền, phái sinh) không trùng với nguồn lợi nhuận (margin cơ sở, cần khách có tài sản).

**Q5. Có nên dùng NLP để thu thập tin tức về DNSE?**
Không cần NLP nặng. Nên chọn lọc tin tức rồi trích sự kiện thủ công, hoặc gắn thẻ theo từ khóa như cách làm với review. Lý do: giám khảo chấm việc truy vết được nguồn, và kết luận từ mô hình NLP khó giải trình từng câu.

## 2.3 Chẩn đoán: hành trình khách hàng gãy ở đâu

| Tầng | Sản phẩm / chiêu thức | Bằng chứng | Đánh giá |
|---|---|---|---|
| 1. Thu hút | Miễn phí giao dịch, thưởng đăng ký, KOL/YouTube, bảng giá Gen Z | 12,27% số tài khoản; 20% tài khoản mở mới năm 2025 | ✅ Mạnh, nhưng đắt và kéo theo khách săn thưởng |
| 2. Mở tài khoản | eKYC 3–5 phút, NFC, OTP | 19,6% review tiêu cực | ⚠️ Nhiều trục trặc |
| 3. **Nạp tiền lần đầu** | Thưởng 100.000đ kèm điều kiện nạp 2 triệu | Tài sản bình quân 34,7 triệu/tài khoản; đây là trigger chính của các cáo buộc lừa đảo | ❌ **Điểm gãy chính** |
| 4. **Giữ tiền trên nền tảng** | Tài khoản không ngủ, Trứng Vàng | Chỉ 4 review nhắc tới; lãi 4,3% thấp hơn TCBS 6% | ❌ Có sản phẩm nhưng ít người dùng, kém cạnh tranh |
| 5. Giao dịch, đòn bẩy | Future X, Margin Deal, Ensa, API | Phái sinh 25,38%; cho vay 1,39% | ⚠️ Mạnh ở phái sinh (ít tốn vốn nhưng ít tiền); yếu ở margin cơ sở (nguồn lãi chính) |
| 6. Niềm tin, gắn bó | — | Cáo buộc lừa đảo 16,2%, phí đóng tài khoản, 3 lần bị phạt, bị mạo danh | ❌ |

**Insight chính:** DNSE đầu tư mạnh vào tầng 1 (thu hút) và tầng 5 (phái sinh), nhưng bỏ trống tầng 3–4. Tầng 3–4 lại chính là nơi tạo ra **tài sản đảm bảo cho nguồn lợi nhuận chính** (lãi margin). Lỗ hổng không nằm ở công nghệ — DNSE đã có hạ tầng tốt (3,9 ms, API) và đã có sẵn sản phẩm cho tầng 4. Lỗ hổng nằm ở **thiết kế hành trình và cách định giá**.

## 2.4 Phát biểu bài toán BA

**Câu hỏi kinh doanh** (bản tiếng Anh dùng cho báo cáo):
> *How can DNSE convert its 1.7 million low-balance accounts into funded, asset-holding accounts through its digital product layer — without breaking the zero-fee promise and within regulatory limits?*

**Các bên liên quan:**
- Ban điều hành: P&L, kế hoạch 2026.
- Khách hàng: Gen Z và người đi làm.
- Cổ đông và trái chủ: chương trình trái phiếu 3.500 tỷ.
- UBCKNN: cơ quan phải duyệt sản phẩm mới.

**Vì sao phải làm ngay:**
- H2/2026 cần lợi nhuận gấp 3,9 lần H1.
- T+0 sắp áp dụng: CEO dự báo khách phái sinh sẽ chuyển một phần sang thị trường cơ sở.
- FTSE nâng hạng từ 21/9/2026: dòng vốn hướng vào cổ phiếu vốn hóa lớn và vừa.
- Làn sóng tiết kiệm hộ gia đình: tỷ lệ tiết kiệm tại tổ chức tài chính tăng từ 19,9% lên 43,1%.
- Sau quyết định phạt 8/2026, DNSE phải thiết kế lại các dịch vụ tài chính.

**Chỉ số trọng tâm (north star):** tỷ lệ tài khoản có tài sản (funded-account rate) và tài sản bình quân trên mỗi tài khoản (AUA/account).

**Phân khúc mục tiêu — hai hướng song song:**

| Hướng | Phân khúc | Mục tiêu | Căn cứ |
|---|---|---|---|
| **Hướng 1 — kiếm tiền** | Người đi làm, học vấn THCS trở lên, thuộc 60% thu nhập cao (gồm cả ~30% khách hiện hữu không thuộc Gen Z) | Tăng tài sản bình quân và dư nợ margin | Findex: priority score 9,0–9,3; activation gap 28,5–31,7 điểm; 15–17,5 triệu người chưa chuyển đổi |
| **Hướng 2 — tạo thói quen** | ~800.000 khách Gen Z đã có trên nền tảng | Tạo thói quen để lại tiền trên nền tảng, **chưa nhắm doanh thu ngay** | Activation gap lớn nhất (33,6 điểm); chi phí thu hút đã trả; đây là điều kiện để giả thuyết ở Q3 trở thành đúng |

## 2.5 Các phương án chiến lược sản phẩm số

**Tiêu chí so sánh:** (1) tác động tới doanh thu trên mỗi tài khoản có tài sản; (2) nhu cầu vốn; (3) khả thi pháp lý; (4) thời gian ra kết quả; (5) mức độ khớp với bằng chứng; (6) rủi ro chính.

| Phương án | Cơ chế | (1) | (2) | (3) | (4) | (5) | Đánh đổi / rủi ro |
|---|---|---|---|---|---|---|---|
| **A. Tiếp tục thu hút khách** | Tăng khuyến mãi, KOL, referral | Thấp | Thấp | Cao | Nhanh | Thấp | Thêm tài khoản từ nhóm ít tiền; chi phí môi giới đã +125–198% |
| **B. Bậc thang kích hoạt (activation ladder)** | Bật sẵn Tài khoản không ngủ khi mở tài khoản; tự động chuyển tiền nhàn rỗi → Trứng Vàng / quỹ → cổ phiếu / Margin Deal; sửa luồng nạp tiền lần đầu | **Cao** | TB (trả lãi cho khách; nhưng tiền khách gửi cũng là nguồn vốn) | TB (phải báo cáo UBCKNN trước) | TB | **Cao** | Phải định giá cạnh tranh với TCBS 6%; cần giấy phép quỹ hoặc đối tác; rủi ro niềm tin khi giữ tiền của khách |
| **C. Cầu nối phái sinh → cơ sở (dựa trên T+0)** | Một chạm chuyển từ phái sinh sang cổ phiếu hoặc Margin Deal; gói ưu đãi margin cho khách phái sinh | TB–Cao | Cao (cần vốn cho vay) | Cao | Phụ thuộc lộ trình T+0 | TB (dựa vào phát biểu của CEO) | Chưa biết thời điểm T+0; khách phái sinh ít tiền |
| **D. Freemium → Premium** | Giữ miễn phí giao dịch; thu phí dịch vụ nâng cao: Ensa Pro, gói API/bot, dữ liệu | TB | Thấp | Cao | Nhanh | Thấp–TB (chưa có dữ liệu về nhu cầu trả phí) | Đi ngược hình ảnh "miễn phí" nếu làm không khéo |
| **E. Thu phí trở lại / gói phí** | Áp lại phí giao dịch hoặc bán gói phí | Cao ngắn hạn | Thấp | Cao | Nhanh | Thấp | **Loại** — phá cam kết "trọn đời", cộng hưởng với vấn đề niềm tin |

**Mỗi phương án phải hy sinh gì:**
- **A** bảo vệ thị phần tài khoản mở mới nhưng làm nặng thêm P1–P3.
- **C** tận dụng thế mạnh phái sinh nhưng phụ thuộc vào thời điểm T+0 và vốn cho vay.
- **D** không cần vốn nhưng chỉ kiếm tiền từ nhóm nhỏ khách chuyên nghiệp, không chạm vào ~1,7 triệu tài khoản ít tiền.
- **B** là phương án duy nhất **tác động vào đúng tầng 3–4 đang gãy**, và dựa trên sản phẩm đã có sẵn.

## 2.6 Khuyến nghị sơ bộ (ý tưởng chiến lược cho Round 3A)

**Chiến lược "Kích hoạt trước tiên":** phương án B là lõi, C là đòn bẩy giai đoạn 2, D chỉ thử nghiệm nhỏ.

**Chuỗi tạo giá trị:**
> Tiền nhàn rỗi tự động vào Tài khoản không ngủ → một phần chuyển sang Trứng Vàng hoặc chứng chỉ quỹ → tài sản trên nền tảng tăng → tài sản đảm bảo cho Margin Deal tăng → dư nợ và thu nhập lãi tăng mà **không cần khách giao dịch nhiều hơn** → cộng thêm phí phân phối quỹ, khoản thu định kỳ không phụ thuộc hướng thị trường.

**Phạm vi đề xuất cho Round 3A:**
1. **Sửa tầng 3:** bỏ phí đóng tài khoản 100.000đ; viết lại điều khoản thưởng 100.000đ / nạp 2 triệu cho minh bạch; thêm luồng "nạp tiền lần đầu" với mức tối thiểu thấp (Trứng Vàng đã cho phép bắt đầu từ 1 triệu).
2. **Nâng tầng 4:** bật sẵn Tài khoản không ngủ khi mở tài khoản; tách phần lãi thưởng theo giao dịch ra khỏi lãi tiết kiệm để người chỉ gửi tiền hiểu rõ mình nhận bao nhiêu. 🔎 Mức lãi cạnh tranh với TCBS iPower là giả thuyết, cần test giá.
3. **Nguồn tiền vào tự động cho Hướng 1:** chuyển lương tự động hoặc nạp tiền định kỳ qua ngân hàng đối tác hoặc ZaloPay (đã có Open API). 🔎 Mức độ chấp nhận là giả thuyết.
4. **Bậc thang tài sản:** tiền nhàn rỗi → trái phiếu / quỹ → cổ phiếu → Margin Deal. Mỗi bậc là một lần kích hoạt đo được.
5. **Giai đoạn 2 — cầu nối T+0:** đưa khách phái sinh sang cổ phiếu và Margin Deal khi T+0 được áp dụng.

**Điều kiện khả thi:**

| Điều kiện | Hiện trạng |
|---|---|
| Sản phẩm | ✅ Đã có Tài khoản không ngủ, Trứng Vàng, Margin Deal |
| Vốn | ✅ Trái phiếu 3.500 tỷ và ~1.275 tỷ từ quyền mua, dành cho margin |
| Quản lý quỹ | ⚠️ Mới là chủ trương lập công ty mới; cần đối tác trong thời gian chờ |
| Công nghệ | ✅ 3,9 ms, Open API, microservices |
| **Pháp lý** | ⚠️ **Phải báo cáo UBCKNN trước khi ra mắt** — bài học từ quyết định 461/QĐ-XPHC. Đây là điều kiện tiên quyết, không phải chi tiết phụ |

**Ước lượng giá trị:** tăng dư nợ thêm 1.000 tỷ (+16%) mang lại ~110 tỷ thu nhập lãi gộp/năm, tương đương ~20% mục tiêu LNTT 2026. 🔎 Đây là số **trước chi phí vốn**; chi phí vốn đang tăng (N4) nên lợi nhuận ròng sẽ thấp hơn.

## 2.7 Hướng kiểm chứng (giả định, test, KPI)

| # | Giả định cần kiểm chứng | Cách test ở Round 3 | KPI |
|---|---|---|---|
| A1 | Phần lớn tài khoản DNSE gần như không có tiền | Lấy phân phối số dư tài khoản từ dữ liệu nội bộ | % tài khoản có tài sản; tài sản bình quân trên mỗi tài khoản |
| A2 | Bật sẵn Tài khoản không ngủ làm tăng lượng tiền giữ lại | A/B test luồng mở tài khoản | Tỷ lệ bật tính năng; tỷ lệ tài khoản có tài sản sau 30 và 90 ngày |
| A3 | Khách nhạy với lãi suất khi so với TCBS và ngân hàng | Price ladder hoặc conjoint trên phân khúc Hướng 1 | Tiền nạp vào tăng thêm khi lãi tăng 0,5 điểm |
| A4 | Tài sản trên nền tảng kéo theo dư nợ margin | Hồi quy dư nợ margin theo tài sản khách hàng (chuỗi số liệu đã công bố) | Dư nợ trên mỗi tài khoản có tài sản |
| A5 | Số dư của Gen Z tăng dần và họ ở lại DNSE | Theo dõi các nhóm khách theo năm mở tài khoản 2021–2026 | Tăng trưởng số dư theo nhóm; tỷ lệ còn hoạt động sau 12 tháng |
| A6 | Sản phẩm được UBCKNN chấp thuận | Tham vấn trước với UBCKNN | Có chấp thuận trước ngày ra mắt |
| A7 | Minh bạch điều khoản giúp lấy lại lòng tin | So sánh review trước và sau khi thay đổi | % review tiêu cực thuộc nhóm "lừa đảo" và "khuyến mãi" |
| A8 | T+0 kéo khách phái sinh sang thị trường cơ sở | Theo dõi hành vi sau khi T+0 được áp dụng | % khách phái sinh giao dịch cả cổ phiếu |

## 2.8 Việc cần làm với báo cáo hiện tại (còn 3 ngày)

Sắp theo thứ tự ưu tiên:
1. **Đổi khuyến nghị từ "xây mới" sang "mở rộng và định giá lại"** Tài khoản không ngủ và Trứng Vàng. Nếu không nhắc hai sản phẩm này, giám khảo biết về DNSE sẽ thấy ngay chỗ hổng.
2. **Sửa mốc so sánh lãi suất:** sản phẩm rút được bất cứ lúc nào thì so với các gói sinh lời tự động (ngân hàng 3,5–4,3%, TCBS 6%); sản phẩm có kỳ hạn mới so với tiền gửi có kỳ hạn (6–9%).
3. **Thêm quyết định phạt 17/8/2026** vào phần rủi ro, phần khả thi và phần kiểm chứng.
4. **Viết lại câu về quản lý quỹ:** chưa có nghị quyết riêng, nhưng lãnh đạo đã công bố chủ trương tự lập công ty.
5. **Bổ sung cơ chế ký quỹ phái sinh vào §4.1** (tiền của nhà đầu tư, không phải khoản vay), kèm ghi chú về các dịch vụ "ứng trước" vừa bị buộc dừng.
6. **Thêm số Q4/2025** để cho thấy biên lợi nhuận thấp kéo dài hai quý liền, và thêm việc mảng môi giới lỗ ở cấp chi phí trực tiếp.
7. **Điền chỗ trống trong chuỗi thị phần phái sinh (Figure 2):** Q4/2024 là 9,98%; Q1/2025 là 16,72%.
8. **Ghi chú** rằng doanh thu môi giới Q2 giảm chủ yếu do thanh khoản thị trường giảm 22%.
9. Giữ tổng độ dài dưới 3.500 từ; mục 1–8 có thể viết thành câu ngắn hoặc đưa vào appendix.

---

## Nguồn

**Tài liệu nội bộ:** `doc/[FBA 6] QUESTION BOOKLET ROUND 2 (1).pdf`; `FBA_Round2_DNSE_data_pack.xlsx`; `doc/FBAR2_2026_DNSE_Analysis.docx`; `doc/dnse.md`.

**Công ty, IPO, vốn:**
- [Tạp chí KT-TC — DNSE 18 tuổi](https://tapchikinhtetaichinh.vn/dnse-18-tuoi-dau-an-tien-phong-tren-ban-do-cong-nghe-tai-chinh-viet-nam.html)
- [Về DNSE — HDSD Entrade X](https://hdsd.dnse.com.vn/su-kien-dnse/su-kien-ipo-dnse/ipo-cau-hoi-thuong-gap/ve-dnse)
- [Báo Đầu tư — Chào sàn 1/7/2024](https://baodautu.vn/chung-khoan-dnse-se-chao-san-hose-ngay-17-voi-dinh-gia-9900-ty-dong-d218267.html)
- [Báo Đầu tư — Nhà đầu tư IPO tạm lỗ 4,7%](https://baodautu.vn/chung-khoan-dnse-nha-dau-tu-tam-lo-47-khi-tham-gia-mua-30-trieu-co-phieu-ipo-d219007.html)
- [Vietstock — Định giá gần 10.000 tỷ](https://vietstock.vn/2024/06/chung-khoan-dnse-sap-niem-yet-tren-hose-dinh-gia-gan-10000-ty-dong-741-1200877.htm)
- [VnExpress — Phát hành 85,65 triệu cổ phiếu](https://vnexpress.net/dnse-du-kien-phat-hanh-85-65-trieu-co-phieu-4863642.html)
- [Thương hiệu & Công luận — Gia hạn chào bán](https://thuonghieucongluan.com.vn/dnse-bat-ngo-gia-han-thoi-gian-chao-ban-85-65-trieu-co-phieu-a306299.html)
- [Thương hiệu & Công luận — Cổ đông lớn chuyển nhượng quyền mua](https://thuonghieucongluan.com.vn/co-dong-lon-dang-ky-chuyen-nhuong-quyen-mua-dse-a304998.html)
- [CafeF — Hoàn tất tăng vốn](https://cafef.vn/dnse-hoan-tat-tang-von-ngay-truoc-them-dhdcd-thuong-nien-188260325144346909.chn)
- [Simplize — Giá DSE](https://simplize.vn/co-phieu/DSE)

**Xử phạt, pháp lý:**
- [Market Times — Phạt 802,5 triệu](https://markettimes.vn/chung-khoan-dnse-dse-cua-chu-tich-nguyen-hoang-giang-bi-phat-128642.html)
- [Phụ nữ Việt Nam — Buộc dừng dịch vụ tài chính](https://phunuvietnam.vn/cong-ty-chung-khoan-dnse-bi-buoc-dung-cung-cap-dich-vu-tai-chinh-238260818165854342.htm)
- [Thương trường — Chi tiết vi phạm](https://thuongtruong.com.vn/news/chung-khoan-dnse-bi-phat-8025-trieu-dong-vi-loat-vi-pham-trong-hoat-dong-chung-khoan-168363.html)
- [Thương hiệu & Công luận — Phạt 125 triệu (mã L18)](https://thuonghieucongluan.com.vn/cong-ty-co-phan-chung-khoan-dnse-bi-xu-phat-125-trieu-dong-a243582.html)
- [DNSE — Cảnh báo lừa đảo](https://www.dnse.com.vn/tin-tuc/canh-bao-lua-dao-va-khuyen-cao-giao-dich-an-toan)

**Kết quả kinh doanh:**
- [Báo Đầu tư — LN Q4/2025 giảm mạnh](https://baodautu.vn/chi-phi-moi-gioi-tang-cao-loi-nhuan-chung-khoan-dnse-quy-iv2025-giam-manh-d493637.html)
- [Báo Pháp luật — Q1/2026](https://doanhnhan.baophapluat.vn/chung-khoan-dnse-dse-bao-doanh-thu-quy-i-tang-62-du-no-margin-ap-sat-moc-6-000-ty-dong.html)
- [Vietstock — Q1/2026](https://vietstock.vn/2026/04/dnse-noi-tiep-da-tang-truong-doanh-thu-va-du-no-margin-737-1429717.htm)
- [Người Đưa Tin — H1/2026](https://www.nguoiduatin.vn/doanh-thu-moi-gioi-dnse-tang-hon-80-sau-nua-dau-nam-2026-204260721150941466.htm)
- [Mekong Asean — H1/2026](https://mekongasean.vn/doanh-thu-hoat-dong-dnse-tang-gan-60-trong-6-thang-dau-nam-57583.html)
- [Báo Pháp luật — Q2/2026](https://doanhnhan.baophapluat.vn/du-no-margin-lap-dinh-6-300-ty-dong-loi-nhuan-quy-ii-cua-chung-khoan-dnse-dse-tang-13.html)

**ĐHCĐ 2026:**
- [Báo Đầu tư](https://baodautu.vn/dhdcd-dnse-san-sang-cho-giao-dich-t0-dat-muc-tieu-tham-vong-nam-2026-d553634.html)
- [Báo Pháp luật — Carbon, quỹ, trung tâm dữ liệu](https://doanhnhan.baophapluat.vn/dhdcd-dnse-len-ke-hoach-tham-gia-san-tin-chi-carbon-phat-hanh-3-500-ty-dong-trai-phieu-nam-2026.html)
- [Dân trí — IFC](https://dantri.com.vn/kinh-doanh/dnse-thong-qua-chu-truong-thanh-lap-cong-ty-chung-khoan-tai-ifc-20260327114025078.htm)
- [Nhà Quản lý](https://nhaquanly.vn/dhdcd-dnse-2026-chot-muc-tieu-tang-truong-loi-nhuan-tren-60-huy-dong-3500-ty-qua-trai-phieu-a18342.html)

**Phái sinh, cạnh tranh, Gen Z:**
- [Người Quan Sát — Thanh khoản Q2/2026 giảm 22%](https://nguoiquansat.vn/thi-truong-phai-sinh-ha-nhiet-thanh-khoan-quy-ii-boc-hoi-22-cuoc-choi-moi-gioi-van-thuoc-ve-vps-va-dnse-302475.html)
- [VnExpress — Chiến lược bứt tốc phái sinh](https://vnexpress.net/chien-luoc-giup-dnse-but-toc-tren-duong-dua-phai-sinh-4888928.html)
- [Fili — Phái sinh 2025](https://fili.vn/2026/01/thi-truong-phai-sinh-2025-vps-danh-roi-thi-phan-dnse-tao-buoc-nhay-vot-830-1389313.htm)
- [Vietstock — Top 2 Q2/2026](https://vietstock.vn/2026/07/dnse-giu-vung-top-2-thi-phan-chung-khoan-phai-sinh-tiep-tuc-mo-rong-dau-an-tren-thi-truong-737-1463117.htm)
- [Nhà Đầu Tư — Trả hộ phí ký quỹ](https://nhadautu.vn/chung-khoan-dnse-choi-lon-khi-tra-ho-phi-ky-quy-phai-sinh-cho-khach-hang-d96127.html)
- [Tin nhanh CK — Cuộc đua miễn phí giao dịch](https://www.tinnhanhchungkhoan.vn/khi-ong-lon-tham-gia-cuoc-dua-mien-phi-giao-dich-post342834.html)
- [VnExpress — Cách DNSE thu hút Gen Z](https://vnexpress.net/cach-dnse-thu-hut-khach-hang-gen-z-4916725.html)
- [Vietstock — Bảng giá Gen Z](https://vietstock.vn/2025/05/dnse-ra-mat-phien-ban-bang-gia-dau-tien-tren-thi-truong-danh-rieng-cho-gen-z-737-1313381.htm)

**Sản phẩm và công nghệ:**
- [Tài khoản không ngủ](https://www.dnse.com.vn/san-pham/tai-khoan-khong-ngu)
- [So sánh các gói sinh lời tự động 2025](https://www.dnse.com.vn/hoc/chuong-trinh-sinh-loi-tu-dong)
- [Trứng Vàng](https://kinhtechungkhoan.vn/dnse-gioi-thieu-san-pham-trung-vang-voi-loi-suat-dau-tu-hap-dan-1043755.html)
- [Margin Deal](https://dantri.com.vn/kinh-doanh/chung-khoan-dnse-tien-phong-ra-mat-he-thong-quan-tri-theo-tung-giao-dich-20221213172235616.htm)
- [Future X](https://dantri.com.vn/kinh-doanh/dnse-ra-mat-san-pham-chung-khoan-phai-sinh-co-ty-le-coc-chi-1848-20230629160034799.htm)
- [Ensa](https://vneconomy.vn/tro-ly-chung-khoan-ao-ensa-cua-dnse-nhan-giai-thuong-giai-phap-ai-dot-pha-linh-vuc-tai-chinh.htm)
- [Lightspeed API](https://www.dnse.com.vn/lightspeed-api)
- [ZaloPay Open API](https://cafef.vn/don-dau-xu-huong-open-api-trong-chung-khoan-dnse-khang-dinh-vi-the-voi-cu-bat-tay-zalopay-188240105204213522.chn)
- [AMD case study](https://www.amd.com/en/resources/case-studies/dnse-securities.html)
- [ITviec](https://itviec.com/companies/dnse)
- [Future Tech Summit](https://tapchikinhtetaichinh.vn/dnse-future-tech-summit-giai-bai-toan-ha-tang-va-open-api-cho-ky-nguyen-giao-dich-t0-103263.html)

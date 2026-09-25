# DNSE — Các vấn đề & Bài toán BA về chiến lược sản phẩm số

*Ghi chú làm việc nội bộ cho team FBA Season 6, Round 2. Lập ngày 24/09/2026; cập nhật cùng ngày theo BCTC và tài liệu gốc; cập nhật 25/09/2026 theo thông báo gốc của HOSE, HNX, VSDC và BCTC toàn ngành.*
*Hạn nộp: **21:00 ngày 27/09/2026**. Báo cáo tối đa 3.500 từ, viết bằng tiếng Anh, nộp PDF.*

**Nguồn tổng hợp:**
- **Nguồn gốc (sơ cấp):**
  - BCTC của DNSE, mọi dòng, Q1/2018–Q2/2026, kéo từ Vietcap bằng `01b_dnse_financials_fetch.py` và đối chiếu với BCTC bán niên 2026 do KPMG soát xét.
  - BCTC của mọi công ty chứng khoán có trên Vietcap (44 mã, gồm **VPS, niêm yết HOSE mã VCK**), Q1/2018–Q2/2026, kéo bằng `01c_peer_financials_fetch.py`.
  - Thông báo thị phần môi giới gốc của HNX (139 thông báo, từ Q4/2017) và HOSE (2023–Q2/2026), kéo bằng `01d_market_macro_fetch.py`.
  - Báo cáo thường niên VSDC 2018–2025 (số tài khoản cuối năm), giá ngày chỉ số và phái sinh (Vietcap), World Bank WDI, thông cáo NSO 2026.
  - Báo cáo thường niên 2025 của DNSE.
  - Nghị quyết 01/2026/NQ-DNSE-ĐHĐCĐ cùng các tờ trình ĐHCĐ 2026.
  - Bộ đếm tài khoản trên trang chủ VSDC.
- **Nguồn khác:** data pack Excel, báo cáo docx, tra cứu báo chí ngày 23–24/09/2026, question booklet Round 2.
- Phân tích chi tiết và biểu đồ dài hạn ở `bctc_analysis.md`.

**Quy ước:** 🔎 đánh dấu giả thuyết hoặc suy luận cần kiểm chứng; **(báo chí)** đánh dấu số liệu chưa có văn bản gốc. Đề bài chấm điểm việc tách bạch fact và giả thuyết.

### Những gì đã thay đổi so với bản trước

| Nội dung | Bản trước | Bản này | Nguồn |
|---|---|---|---|
| LNTT Q2/2026 và H1/2026 | 98,9 / 113,1 | **97,4 / 111,6** | BCTC bán niên soát xét (bản tự lập 20/7 ghi 113,1) |
| Doanh thu 2025 | 1.467 (+77%), gọi là "doanh thu hoạt động" | Doanh thu hoạt động **1.457,9 (+80,6%)**; 1.467 là *tổng doanh thu* (thêm thu nhập tài chính và thu nhập khác) | BCTC; báo cáo thường niên trang 13 |
| Tiến độ kế hoạch doanh thu | 48,9% | **49,1%**, vì kế hoạch đặt trên tổng doanh thu | Tờ trình 05/2026 |
| "Dự phòng tự doanh +405%" | Dùng làm bằng chứng | **Bỏ**: không dòng nào tái lập được; dòng 24 chỉ +70% và chủ yếu là chi phí vốn | BCTC |
| "Thu nhập đầu tư" 22,8%, phụ thuộc bảng cân đối 62,4% | Định nghĩa lẫn lộn giữa các kỳ | **71,5%** (cho vay 39,6 + tiền gửi HTM 22,8 + tự doanh 9,1) | BCTC |
| Môi giới lỗ | Chỉ Q4/2025 và Q1/2026 | **16 quý liên tiếp**, lũy kế −190 tỷ; 10/10 đối thủ lớn có lãi (xem dòng "Môi giới lỗ so với ngành") | BCTC DNSE và đối thủ |
| Tài sản khách hàng | 52.000 tỷ, 34,7 triệu/tài khoản | **53.471 tỷ, 35,3 triệu/tài khoản**; chỉ **1,8%** tài khoản có tài sản ròng từ 10 triệu | Báo cáo thường niên trang 29–30 |
| Quản lý quỹ | "Chưa có nghị quyết riêng; chủ trương tự lập" | **ĐHCĐ 2025 và 2026 đều thông qua** chủ trương sở hữu một công ty quản lý quỹ làm công ty con; chưa thực hiện | NQ 01/2026 Điều 15, Tờ trình 11 |
| VNDA 10 tỷ, sàn carbon | Ghi là nghị quyết ĐHCĐ | **Không có** trong nghị quyết lẫn tờ trình | NQ 01/2026, tập tờ trình |
| Dư nợ, LNTT đối thủ | Bảng tổng hợp của báo | BCTC từng công ty. SSI Q2/2026: **1.529** (báo ghi 1.511) | Vietcap |
| Giá trị khuyến nghị (+1.000 tỷ dư nợ) | 110 tỷ, bằng 20% kế hoạch | 112 tỷ trước chi phí vốn, **khoảng 49 tỷ sau chi phí vốn 6,3%**, bằng 9% kế hoạch | BCTC |
| P3: H2 cần bao nhiêu | "Gấp 2,2 lần quý tốt nhất" | **~219 tỷ/quý, gấp 1,28 lần quý tốt nhất** (Q3/2025: 171,1) | BCTC |
| Tỷ trọng tài khoản của DNSE | 12,27% (1,7 triệu tại 30/6 chia cho 13,85 triệu tại 31/8) | Báo cáo dùng **12,24%**: mẫu số là bộ đếm VSDC 13.887.603 ngày 24/9/2026 (nguồn gốc, nhưng lệch ngày nên hơi thấp). Nếu dùng số VSDC cùng ngày 30/6/2026 (13.430.517, qua Tạp chí KT-TC) thì là **≥12,66%**. Tỷ số 0,24 và 0,11 gần như không đổi | VSDC; Tạp chí KT-TC, 8/7/2026 |
| Tỷ lệ active so với ngành | Chưa có đối chiếu | DNSE 5,7% so với TCBS ~30% và VNDirect 30,8% (2021). Chi tiết ở mục 1.8 | BCTN 2025; báo cáo HSC; VietnamBiz |
| Thị phần HOSE, HNX, phái sinh | Bảng tổng hợp của báo | **Thông báo gốc của hai sở**, chuỗi 2018–Q2/2026. Phái sinh Q2/2025 là **17,62%** (báo ghi 17,33%); có thêm Q2–Q3/2024 (5,11%, 5,30%) | HNX, HOSE (`01d`) |
| VPS | "Chưa niêm yết", dư nợ 31.300 và LNTT theo báo | **Niêm yết HOSE, mã VCK.** Dư nợ **31.312**, LNTT Q2/2026 **1.378,4** (+56,8%) từ BCTC | Vietcap (`01c`) |
| Tỷ trọng tài khoản và cho vay theo thời gian | Chỉ có một thời điểm | Tài khoản 2,75% → **12,74%** (2022–2025), dư nợ 2,74% → **1,85%**: hai đường tách nhau từ 2023. Chi tiết ở `bctc_analysis.md` mục 10 | VSDC, BCTN 2025, BCTC toàn ngành |
| Môi giới lỗ so với ngành | "9/9 đối thủ niêm yết có lãi" | Trong 11 công ty lớn chỉ DNSE lỗ; trên 42 công ty có BCTC có 19 công ty lỗ, nhưng DNSE lỗ **nặng nhất** (−44,5 tỷ H1/2026, gấp 2,6 lần công ty thứ hai). Cả ngành vẫn lãi môi giới mọi năm | BCTC toàn ngành |
| "Ngoài DNSE không công ty nào công bố số tài khoản" | Ghi trong giới hạn B3 của báo cáo | **Sai**: VPS (1.547.000, 9/2025) và TCBS (>1,2 triệu, cuối 2025) đều công bố. Chi tiết ở mục 1.9 | Tài liệu IPO VPS; Vietstock |

---

# SECTION 1 — THÔNG TIN DNSE VÀ CÁC VẤN ĐỀ

## 1.1 Hồ sơ công ty

| Hạng mục | Thông tin |
|---|---|
| Tên | CTCP Chứng khoán DNSE (tên cũ: Chứng khoán Đại Nam), mã **DSE** trên HOSE |
| Thành lập | 2007, vốn ban đầu 38 tỷ đồng. Chuyển đổi thành công ty chứng khoán công nghệ trong giai đoạn 2021–2022: vốn điều lệ tăng từ 160 lên 1.000 rồi 3.000 tỷ (BCTC) |
| Vốn điều lệ | **4.282,5 tỷ đồng**, 428.249.806 cổ phiếu, tại 30/6/2026 sau đợt phát hành quyền mua (BCTC). Lúc IPO là 3.300 tỷ |
| Tổng tài sản | 15.139 tỷ (cuối 2025); 15.208 tỷ (30/6/2026) |
| Sở hữu | Encapital Financial Technology và Encapital Holdings giữ **67,1%**. PYN Elite Fund mua khoảng 12% vốn chủ vào tháng 1/2024 **(báo chí)** |
| Lãnh đạo | Chủ tịch HĐQT **Nguyễn Hoàng Giang** (ký NQ 01/2026), Tổng giám đốc **Nguyễn Ngọc Linh** (ký BCTC), Giám đốc Công nghệ **Nguyễn Đức Bình** |
| Nhân sự | 151–300 người (ITviec) |
| Kênh phân phối | 100% qua app/web Entrade X, **không có chi nhánh** |
| Khách hàng | **1.512.920 tài khoản** cuối 2025, bằng 13% toàn thị trường (báo cáo thường niên) → **hơn 1,7 triệu** H1/2026 **(thông cáo công ty qua báo chí)**, tức **≥12,66%** của 13.430.517 tài khoản toàn thị trường cùng ngày 30/6/2026 (báo cáo dùng 12,24%, chia cho bộ đếm VSDC ngày 24/9, xem mục 1.9) |
| Mức độ hoạt động | Chỉ **85.739 khách active** trong tháng 12/2025 (**5,7%**), tăng từ 41.900 (4,2%) tháng 12/2024; **27.100 khách** có tài sản ròng từ 10 triệu đồng trở lên (**1,8%**); hơn 2.000 khách từ 1 tỷ trở lên (báo cáo thường niên, PDF trang 30 = trang in 58). So với đối thủ: mục 1.8 |
| Tài sản khách hàng | 53.471 tỷ (AUM, cuối 2025), khoảng 35,3 triệu/tài khoản, lệch về số ít khách lớn. Tiền mặt của khách: 1.961 tỷ (30/6/2026), khoảng **1,15 triệu/tài khoản** (BCTC, ngoại bảng) |
| Cơ cấu khách hàng | Khoảng 800.000 khách Gen Z, chiếm khoảng 70% (tính đến Q1/2025) **(báo chí)**. 🔎 Báo cáo thường niên không nêu cơ cấu tuổi; con số này khớp quy mô tài khoản Q1/2025 (khoảng 1,13 triệu) |

## 1.2 Các mốc chính

| Thời điểm | Sự kiện |
|---|---|
| 2007 | Thành lập với tên Chứng khoán Đại Nam, vốn 38 tỷ |
| 2018–2020 | Công ty nhỏ: vốn điều lệ 160 tỷ, doanh thu 18–28 tỷ/năm, lợi nhuận gần 0 (BCTC). 5.548 tài khoản cuối 2020 (báo cáo thường niên) |
| 2021–2022 | Encapital tái định vị thành công ty chứng khoán công nghệ, ra mắt Entrade X. Vốn điều lệ tăng lên 1.000 tỷ (2021) và 3.000 tỷ (2022); tài khoản tăng lên 44.727 (2021) và 189.845 (2022). 🔎 Môi giới còn lãi ở mức chi phí trực tiếp đến Q2/2022, lỗ từ Q3/2022. Thời điểm áp dụng miễn phí giao dịch trọn đời cần kiểm chứng |
| 12/2022 | Ra mắt **Margin Deal**, hệ thống đầu tiên ở Việt Nam quản lý khoản vay margin theo từng giao dịch |
| 6/2023 | Ra mắt **Future X** (phái sinh), tỷ lệ ký quỹ 18,48% |
| 9/2023 | Bị UBCKNN phạt lần 1: 125 triệu đồng (vi phạm quy định nhận lệnh) **(báo chí)** |
| 11/2023 | Lãi margin 11,5%; mức 5,99% cho 10 mã. LNST 9 tháng 2023 tăng 334% (LNTT tăng 349%) (BCTC) |
| 1/2024 | Tích hợp Open API với ZaloPay; PYN Elite đầu tư |
| 2024 | Bị phạt lần 2: 125 triệu đồng (cho vay margin mã L18 sau khi HNX đã loại mã này khỏi danh sách) **(báo chí)** |
| 1/7/2024 | Niêm yết HOSE, giá IPO 30.000đ, định giá khoảng 9.900 tỷ. **Phiên đầu giảm 4,7%** so với giá IPO **(báo chí)** |
| 2024 | Trợ lý AI **Ensa** đạt giải "Giải pháp AI đột phá lĩnh vực tài chính" (AI Awards 2024) |
| Q4/2024 | Lần đầu vào top 2 thị phần phái sinh (9,98%) (báo cáo thường niên) |
| 5/2025 | Ra mắt bảng giá dành riêng cho Gen Z. Trả thay khách phí VSD và phí quản lý ký quỹ phái sinh trong giai đoạn chuyển sang hệ thống KRX (5–9/2025) |
| 6/2025 | Ra mắt **Tài khoản không ngủ** (báo cáo thường niên trang 35) |
| 2025 | 518.514 tài khoản mở mới, chiếm 20% toàn thị trường (Q1/2025 chiếm 34%). Thị phần phái sinh cả năm 21,47%. Tạm ứng cổ tức 7% vốn điều lệ, tức 239,8 tỷ đồng (Tờ trình 04/2026) |
| 21/11/2025 | Sự kiện DNSE Future Tech Summit, công bố tốc độ xử lý lệnh **3,9 ms** |
| Q4/2025 | LNTT 11,7 tỷ, **LNST giảm 72%** so với cùng kỳ (BCTC) |
| Q4/2025–3/2026 | Phát hành 85,65 triệu cổ phiếu quyền mua giá 15.000đ (tỷ lệ 4:1), thu khoảng 1.275 tỷ. Phải **gia hạn** thời gian chào bán **(báo chí)**. Vốn chủ tăng từ 4.302 lên 5.358 tỷ trong Q1/2026 (BCTC) |
| 26/3/2026 | ĐHCĐ thông qua 22 điều: kế hoạch tổng doanh thu 1.736 tỷ, LNTT 550 tỷ; trái phiếu 2.500 + 1.000 tỷ; sở hữu công ty quản lý quỹ; công ty chứng khoán tại IFC; chứng quyền; ESOP (chi tiết ở mục 1.6) |
| 14/8/2026 | BCTC bán niên KPMG soát xét: LNTT H1 111,6 tỷ, thấp hơn bản tự lập (113,1) vì chi phí quản lý tăng 1,5 tỷ |
| **17/8/2026** | **Bị phạt lần 3: 802,5 triệu đồng, buộc dừng 3 dịch vụ phái sinh** **(báo chí)**, chi tiết ở mục 1.7B |
| 21/9/2026 | FTSE Russell nâng hạng Việt Nam lên thị trường mới nổi thứ cấp |

## 1.3 Hệ sinh thái sản phẩm số trên Entrade X

| Sản phẩm | Cơ chế | Vai trò trong hành trình khách hàng |
|---|---|---|
| **Entrade X** | App giao dịch cơ sở. Mở tài khoản online trong 3–5 phút (eKYC, NFC), miễn phí giao dịch trọn đời | Thu hút khách |
| **Future X** | Phái sinh. Ký quỹ 18,48% (đòn bẩy khoảng 5–7 lần), giao dịch trên cùng tài khoản cơ sở, không phải chuyển tiền giữa hai tài khoản, miễn phí giao dịch | Tạo tương tác, tạo thị phần |
| **Margin Deal** | Vay theo từng giao dịch: mỗi deal có tỷ lệ vay, lãi suất, mức call riêng, lãi/lỗ theo thời gian thực | Kiếm tiền (lãi vay) |
| **Tài khoản không ngủ** (từ 6/2025) | Sinh lời trên tiền nhàn rỗi: **1,8% cố định + tối đa 1,5% theo số dư + tối đa 1,0% theo giá trị giao dịch = tối đa 4,3%/năm**. Không yêu cầu số dư tối thiểu, trần 30 tỷ, trả lãi hàng tháng | Giữ tiền trên nền tảng |
| **Trứng Vàng (Egg X)** | Đầu tư trái phiếu niêm yết theo kỳ hạn, từ 1 triệu đồng, tự động tái tục. Mã đầu tiên là trái phiếu Agribank. **Kế hoạch 2026: hợp tác Vietcombank, VietinBank và BIDV để mở rộng sang trái phiếu và chứng chỉ quỹ** (Tờ trình 05/2026) | Giữ tiền trên nền tảng |
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

## 1.5 Kết quả kinh doanh (tỷ VND, theo BCTC)

| Chỉ tiêu | FY2024 | FY2025 | Q4/2025 | Q1/2026 | Q2/2026 | H1/2026 |
|---|---:|---:|---:|---:|---:|---:|
| Doanh thu hoạt động | 807,4 | 1.457,9 (+80,6%) | 434,8 (+85,9%) | 395,1 (+62,3%) | 453,1 (+56,1%) | 848,2 (+59,0%) |
| Tổng doanh thu (gồm thu nhập tài chính) | 813,0 | 1.465,4* | 437,1 | 397,4 | 455,1 | 852,5 |
| LNTT | 227,5 | 340,2 (+49,5%) | **11,7** | **14,2** | 97,4 (+7,0%) | 111,6 |
| LNST | 181,8 | 272,5 | 9,3 (−72%) | 11,3 | 81,8 | 93,1 |
| Biên LNTT | 28,2% | 23,3% | **2,7%** | **3,6%** | 21,5% | 13,2% |
| Doanh thu môi giới | 144,8 | 404,0 | 125,0 | 119,5 | 102,5 (+38,8%) | 222,1 (+80,8%) |
| Chi phí môi giới trực tiếp | 174,8 | 464,9 | 149,9 (+198%) | 137,8 (+125%) | 128,7 | 266,5 |
| **Kết quả môi giới** | −30,0 | −60,8 | −24,9 | −18,3 | −26,2 | −44,5 |
| Lãi/lỗ tự doanh thuần (FVTPL) | 6,8 | 146,2 | −1,1 | −9,6 | 43,5 | 33,9 |
| Chi phí lãi vay + dòng 24 (chi phí vốn và dự phòng) | 210,6 | 429,8 | 151,0 | 160,5 | 163,6 | 324,1 |
| Dư nợ margin + ứng trước, cuối kỳ | 3.882 | 5.832 | 5.832 | 5.910 | 6.303 (+24,7%) | 6.303 |
| Vốn chủ sở hữu, cuối kỳ | 4.030 | 4.302 | 4.302 | 5.358 | 5.440 | 5.440 |
| Dư nợ / vốn chủ (trần 200%) | 96% | 136% | 136% | 110% | 116% | 116% |
| Tiền của khách (ngoại bảng) | 1.340 | 2.903 | 2.903 | 2.869 | 1.961 | 1.961 |
| Thị phần phái sinh | 6,14% | 21,47% | 24,26% | 25,50% | 25,38% | — |

*Nguồn: BCTC qua `01b`; Q2/2026 bằng H1 soát xét trừ Q1. \*Cộng thu nhập khác khoảng 1,6 thì ra 1.467 tỷ như báo cáo thường niên. Tổng doanh thu Q4/2025 tính bằng doanh thu hoạt động cộng thu nhập tài chính. Dòng 24 của mẫu BCTC gộp dự phòng với chi phí đi vay của khoản cho vay. Thị phần phái sinh lấy từ thông báo của HNX qua báo chí; con số 21,47% (2025) được báo cáo thường niên xác nhận.*

**Xu hướng dài hạn** (chi tiết ở `bctc_analysis.md`):
- Doanh thu tăng từ 21,6 tỷ (2020) lên 180,7 (2021), 452,1 (2022), 714,5 (2023), 807,4 (2024) và 1.457,9 tỷ (2025). Bình quân +68,5%/năm giai đoạn 2021–2025.
- **Lợi nhuận lõi đi ngang.** LNTT không tính lãi/lỗ tự doanh là 156 (2022), 128 (2023), 221 (2024), 194 (2025) và 78 tỷ (H1/2026). Lợi nhuận đỉnh năm 2023 (285,6) và 2025 (340,2) chủ yếu nhờ lãi tự doanh, lần lượt 158 và 146 tỷ.
- **ROE** 8,9% (2021), 3,7% (2022), 7,1% (2023), 5,0% (2024), 6,5% (2025), khoảng 3,8% quy năm (H1/2026). Luôn thấp hơn hoặc xấp xỉ lãi tiết kiệm 12 tháng (khoảng 7%).
- **Cơ cấu tài sản:** tiền gửi có kỳ hạn và trái phiếu HTM chiếm 41–48% tổng tài sản giai đoạn 2022–2025, lớn hơn dư nợ cho vay (33–39%).

## 1.6 Kế hoạch 2026 và cam kết lúc IPO

**Nghị quyết 01/2026/NQ-DNSE-ĐHĐCĐ ngày 26/3/2026** (22 điều) và các tờ trình kèm theo:
- **Kế hoạch kinh doanh** (Điều 9, Tờ trình 05): tổng doanh thu 1.736 tỷ (+18,2%, trên nền tổng doanh thu 2025 là 1.467), chi phí 1.186 tỷ (+5,2%), LNTT 550 tỷ (+61,7%).
- **Trái phiếu:** không chuyển đổi, không kèm chứng quyền, tối đa 2.500 tỷ (Điều 12, Tờ trình 08); chuyển đổi riêng lẻ tối đa 1.000 tỷ (Điều 13, Tờ trình 09). Mục đích sử dụng vốn giao HĐQT quyết định. Tiền từ đợt trái phiếu ra công chúng năm 2025 được dùng cho ứng trước và cho vay ký quỹ (Tờ trình 10).
- **Công ty quản lý quỹ** (Điều 15, Tờ trình 11): thông qua chủ trương *"đầu tư/góp vốn/mua lại cổ phần, phần vốn góp để sở hữu 01 công ty quản lý quỹ làm công ty con"*, gồm quản lý và **phân phối chứng chỉ quỹ** và quản lý danh mục.
  - Đây là **lần thứ hai**: ĐHCĐ 2025 đã thông qua (NQ 01/2025), nhưng HĐQT chưa thực hiện do biến động thị trường.
  - Điều kiện: tỷ lệ vốn khả dụng sau giao dịch tối thiểu 180%.
  - Báo chí dẫn lời Chủ tịch muốn "tự lập thay vì M&A". Nghị quyết cho phép cả hai cách (góp vốn thành lập hoặc mua lại).
- **Công ty chứng khoán tại IFC TP.HCM** (Điều 17, Tờ trình 13).
- **Chứng quyền có bảo đảm:** xin cấp phép và triển khai (Điều 16, Tờ trình 12).
- **ESOP:** tối đa 4.282.500 cổ phiếu, tức 1% (Điều 10, Tờ trình 06).
- **Cổ tức:** năm 2025 tạm ứng 7% vốn điều lệ, tức 239,8 tỷ đồng (bằng 88% LNST 2025). Năm 2026 tối đa 7%, bằng tiền mặt và/hoặc cổ phiếu (Điều 8, Tờ trình 04).
- **Chiến lược 2026** (Tờ trình 05): đơn giản hóa trải nghiệm đầu tư; lệnh AI, Ensa, SENSES, TradingView; hợp tác ZaloPay và các fintech; **hợp tác Vietcombank, VietinBank, BIDV phát triển Trứng Vàng gồm trái phiếu và chứng chỉ quỹ**.
- ~~10 tỷ đồng cho 1% cổ phần VNDA~~; ~~tham gia sàn tín chỉ carbon~~: **không có trong nghị quyết lẫn tờ trình**. Nếu có, các nội dung này chỉ xuất hiện trong phần thảo luận mà báo chí đưa tin. Không dùng trong phân tích.

**So với cam kết lúc IPO** (7/2024, cho giai đoạn 5 năm; nguồn cam kết: báo chí):

| Chỉ tiêu | Cam kết đến khoảng 2029 | Hiện tại |
|---|---|---|
| Khách hàng | 5 triệu | 1,51 triệu (cuối 2025); hơn 1,7 triệu (H1/2026) |
| Lợi nhuận/năm | 2.400 tỷ (100 triệu USD) | Kế hoạch 2026 là 550 tỷ; H1 đạt 111,6 tỷ |
| Vốn hóa | 72.000 tỷ (3 tỷ USD) | **Khoảng 9.420 tỷ** (428,25 triệu cổ phiếu theo BCTC × 22.000đ ngày 16/9/2026 theo Simplize) |

## 1.7 Các vấn đề của DNSE

### A. Vấn đề rút ra từ phân tích data pack và báo cáo

**P1 — Vấn đề gốc: thu hút được tài khoản, không thu hút được tiền.**
- **So với thị trường:** DNSE có khoảng 12,2–12,7% số tài khoản (báo cáo dùng 12,24% theo bộ đếm VSDC; ≥12,66% nếu cùng ngày 30/6/2026) nhưng chỉ 2,88% giao dịch trên HNX, dưới 2,94% trên HOSE, và 1,39% dư nợ cho vay. Quy về tỷ số, một tài khoản DNSE giao dịch bằng **0,23** và vay bằng **0,11** một tài khoản trung bình.
- **So với đối thủ có tên:** tỷ lệ active 5,7% so với khoảng 30% ở TCBS và VNDirect; cường độ giao dịch mỗi tài khoản khoảng 0,23 so với khoảng 0,9 (TCBS) và 0,8–1,2 (VPS). Chi tiết và giới hạn ở mục 1.8.
- **Bằng chứng trực tiếp** (báo cáo thường niên 2025): chỉ **5,7%** tài khoản có hoạt động trong tháng 12/2025, và **1,8%** có tài sản ròng từ 10 triệu đồng. Tiền mặt của khách chỉ khoảng 1,15 triệu/tài khoản (30/6/2026).
- **Tính trên mỗi tài khoản:** doanh thu 499.000đ/nửa năm, doanh thu môi giới 130.600đ, tài sản khách hàng bình quân 35,3 triệu đồng (bị kéo lên bởi hơn 2.000 khách từ 1 tỷ trở lên).
- **Không thiếu vốn cho vay:** dư nợ bằng 116% vốn chủ (trần 200%), còn khoảng 4.600 tỷ dư địa. Điểm nghẽn là tài sản của khách.

**P2 — Tăng trưởng phi kinh tế.**
- Doanh thu H1/2026 tăng 59,0% nhưng biên LNTT giảm từ 23,3% (2025) xuống 13,2%. Riêng Q1/2026: chi phí hoạt động +120%, chi phí môi giới +125%, chi phí vốn và dự phòng (dòng 24) +70%, lỗ tự doanh thuần 9,6 tỷ.
- Nhìn dài hạn: **lợi nhuận lõi (không tính tự doanh) đi ngang ở 128–221 tỷ/năm từ 2022**, trong khi doanh thu tăng 3,2 lần. Năm 2025, nếu bỏ tự doanh thì lợi nhuận giảm 12%, trong khi LNTT báo cáo tăng 50%.

**P3 — Kế hoạch 2026 gần như chắc trượt.**
H1 mới đạt 20,3% mục tiêu lợi nhuận và 49,1% mục tiêu tổng doanh thu. H2 cần 438,4 tỷ LNTT, tức **3,9 lần H1**, hay khoảng 219 tỷ mỗi quý. Mức này **cao hơn 28% so với quý tốt nhất từng có** (Q3/2025: 171,1 tỷ, trong đó có lãi tự doanh lớn).

**P4 — Doanh thu phụ thuộc bảng cân đối.**
- Trong H1/2026: lãi cho vay 39,6%, lãi tiền gửi và trái phiếu HTM 22,8%, lãi tự doanh 9,1%. Cộng lại là **71,5% doanh thu**, phụ thuộc quy mô vốn và diễn biến thị trường chứ không phụ thuộc giao dịch của khách.
- Tỷ trọng này từng là 78% (2022), 89% (2023), 81% (2024). Nó giảm là nhờ phí phái sinh, nhưng mảng phí này lại lỗ (N3).

**P5 — Tập trung vào phái sinh, và mảng này đang chững lại.**
Thị phần phái sinh 25,38%, trong khi thị phần cổ phiếu HNX chỉ 2,88%. Từ 5/2025 DNSE còn trả thay khách phí ký quỹ phái sinh, tức mảng mạnh nhất lại tốn thêm chi phí.

**P6 — Thua ở mảng mà ngành kiếm tiền.**
- **Dư nợ cho vay tại 30/6/2026** (BCTC từng công ty): TCBS 51.522 tỷ, SSI 40.473, VPBankS 38.177, VPS 31.312 (mã VCK), HSC 29.024, Vietcap 17.146, MBS 16.828, VIX 13.958, VNDirect 12.859, SHS 11.722, **DNSE 6.303**.
- **Tăng trưởng LNTT Q2/2026 so với cùng kỳ:** DNSE +7,0%; VPBankS +293%, VNDirect +127%, VPS +56,8%, HSC +42%, MBS +38%, Vietcap +28%, SSI +28%, TCBS +21%, SHS −81%, VIX −95%. DNSE thấp hơn mọi công ty lớn, chỉ cao hơn SHS và VIX.
- **LNTT Q2/2026:** DNSE đứng thứ 9/11 công ty.

**P7 — Lỗi app và lỗi mở tài khoản lặp lại.**
Trong review tiêu cực, 25,8% về crash hoặc lỗi đăng nhập, 19,6% về mở tài khoản (eKYC, OTP, NFC). Các lỗi này xuất hiện theo từng đợt qua nhiều năm, cho thấy chưa được sửa dứt điểm. Với công ty không có chi nhánh, app lỗi nghĩa là không phục vụ được khách hàng.

**P8 — Khách hàng mất lòng tin.**
16,2% review tiêu cực cáo buộc lừa đảo, xoay quanh hai điểm: thưởng 100.000đ nhưng phải nạp tối thiểu 2 triệu, và phí đóng tài khoản 100.000đ. Spam chiếm **27,1% review của DNSE**, so với 7,0% ở VPS và 4,5% ở FPTS. Điểm review có nội dung thực chất giảm từ **4,07 sao (2024) xuống 2,36 sao (2025)**.

**P9 — Thu hút khách từ nhóm có ít tiền nhất.**
Nhóm 15–24 tuổi có khoảng cách lớn nhất giữa thói quen dùng công nghệ và khoản tiền có thể đầu tư (**35,1 điểm**), priority score chỉ 2,25 (nhóm ưu tiên đạt 9,0–9,3). Nhóm này chiếm khoảng 70% khách hàng DNSE **(báo chí)**. Chỉ 1,8% tài khoản có tài sản ròng từ 10 triệu đồng, khớp với bức tranh này.

### B. Vấn đề tìm thêm trên mạng

**N1 — Vi phạm pháp luật lặp lại, lần gần nhất nặng nhất** **(báo chí; quyết định gốc trên ssc.gov.vn chưa được đối chiếu).**
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

**N2 — Lợi nhuận đã sụt hai quý liên tiếp, không chỉ riêng Q1/2026** (BCTC).
- Q4/2025: LNTT 11,7 tỷ, LNST giảm 72%. Tổng chi phí khoảng 425 tỷ (+114%), trong đó chi phí môi giới 149,9 tỷ (+198%), chi phí vốn và dự phòng 151 tỷ, lỗ đánh giá lại tài sản tự doanh chưa thực hiện 53,2 tỷ.
- Báo chí quy nguyên nhân cho "trích lập dự phòng tự doanh". BCTC cho thấy nguyên nhân chủ yếu là **chi phí môi giới, chi phí vốn và lỗ đánh giá lại**.
- Biên LNTT dưới 4% trong **hai quý liền** (2,7% và 3,6%), nên không thể coi Q1/2026 là "cú sốc một quý".

**N3 — Mảng môi giới lỗ ngay ở cấp chi phí trực tiếp, và đây là vấn đề riêng của DNSE** (BCTC DNSE và đối thủ).
- Lỗ **16 quý liên tiếp** từ Q3/2022, lũy kế **−190 tỷ**, chưa tính chi phí quản lý phân bổ. Năm 2021 doanh thu môi giới còn bằng 175% chi phí trực tiếp; năm 2025 chỉ còn 87%.
- Trong H1/2026, **cả 9 đối thủ niêm yết đều có lãi môi giới**: SSI +362, TCBS +283, Vietcap +216, HSC +119, VNDirect +114, MBS +56, VIX +48, SHS +17, VPBankS +3 tỷ. Riêng DNSE là −44,5 tỷ.

**N4 — Chi phí vốn tăng nhanh hơn dư nợ** (BCTC).
- Vay ngắn hạn tăng từ 6.494 (cuối 2024) lên 9.302 tỷ (cuối 2025); cuối 2025 phát hành thêm 1.298 tỷ trái phiếu dài hạn. Chi phí lãi vay Q2/2026 tăng 165,6% và chi phí tài chính H1 tăng 209%, trong khi dư nợ chỉ tăng 24,7%.
- Chi phí vốn ước tính (lãi vay cộng dòng 24, trừ phần tăng dự phòng) tăng từ 3,6% (Q2–Q3/2024) lên **6,5%** (Q2/2026). Lợi suất cho vay khoảng 11,2% (H1/2026), nên chênh lệch còn khoảng 4,9 điểm; Q1/2026 chỉ 3,9 điểm.
- Con số "lợi suất cho vay khoảng 11%" là trước chi phí vốn. Sau chi phí vốn, tăng 1.000 tỷ dư nợ chỉ mang lại khoảng 49 tỷ/năm.

**N5 — Miễn phí giao dịch không còn là khác biệt** **(báo chí, thông tin từ 2024, cần cập nhật)**.
Từ 2024: MBS miễn phí trọn đời cả cơ sở lẫn phái sinh cho tài khoản mới; TCBS miễn phí không thời hạn mọi sản phẩm; SSI miễn phí 12 tháng; VPS miễn phí 6 tháng; JBSV và Pinetree miễn phí trọn đời. Chủ tịch MB Lưu Trung Thái: phí giao dịch rồi sẽ về 0 như phí chuyển khoản.

**N6 — Phái sinh chững lại, đối thủ lấy lại đà** (thông báo gốc HNX).
Q2/2026: VPS tăng từ 33,34% lên 33,84%, DNSE giảm nhẹ từ 25,5% xuống 25,38%, SSI tăng từ 7,2% lên 8,21%, TCBS từ 4,32% lên 4,83%; HSC giảm từ 9,66% xuống 9,23%. Giá trị giao dịch bình quân ngày của hợp đồng VN30 tháng gần nhất Q2 **giảm 23,6%** so với Q1 (53.508 xuống 40.855 tỷ; báo chí ghi toàn thị trường giảm 22,1%). Nhìn dài hơn: DNSE ở quanh 24–25,5% suốt 4 quý, sau khi tăng từ 4,01% (Q1/2024); trong cùng hai năm VPS mất 25 điểm.
*Điều chỉnh so với nhận định trước:* doanh thu môi giới Q2 của DNSE giảm 14,2% so với Q1 (BCTC), **ít hơn mức giảm 22% của thị trường**. Phần giảm này chủ yếu do thị trường, không phải do DNSE mất khách.

**N7 — Thị trường vốn chưa tin vào câu chuyện tăng trưởng.**
- Phiên chào sàn giảm 4,7% so với giá IPO (báo chí).
- Giá khoảng 22.000đ (16/9/2026), so với giá IPO 30.000đ. Sau điều chỉnh cho đợt quyền mua, giá IPO tương đương khoảng 27.000đ, nên giá hiện tại **thấp hơn khoảng 18%**.
- Vốn hóa khoảng 9.420 tỷ, **thấp hơn định giá IPO 9.900 tỷ, dù đã huy động thêm khoảng 1.275 tỷ**.
- Đợt chào bán quyền mua phải gia hạn, và một cổ đông lớn đăng ký chuyển nhượng quyền mua (báo chí).
- **Giải thích cơ bản từ BCTC:** ROE chỉ 3,7–8,9% từ 2021 (khoảng 3,8% quy năm trong H1/2026), thấp hơn lãi tiết kiệm. Năm 2025 công ty vẫn chia 239,8 tỷ cổ tức (88% LNST), rồi phát hành thêm cổ phiếu để huy động 1.275 tỷ.

**N8 — Còn rất xa cam kết IPO** (bảng ở mục 1.6).

**N9 — Sản phẩm sinh lời kém cạnh tranh** (trang sản phẩm của các công ty, cần chốt lại ngày).
Tài khoản không ngủ tối đa 4,3%, nhưng 1,0 điểm trong đó phụ thuộc vào giá trị giao dịch, nên người chỉ gửi tiền không đạt mức tối đa. TCBS iPower trả tối đa **6%**. Các gói sinh lời tự động của ngân hàng: Techcombank tối đa 4%, VPBank 3,5%, VIB tối đa 4,3%.

**N10 — Bị mạo danh để lừa đảo.**
Có website giả mạo DNSE (dnsevn.com) để đánh cắp thông tin đăng nhập. Vấn đề này cộng thêm vào sự mất lòng tin đã thấy trong review.

### C. Vấn đề mới từ chuỗi BCTC 2018–2026

**F1 — Lợi nhuận phụ thuộc tự doanh.**
Lãi/lỗ tự doanh thuần dao động từ −61 tỷ (2022) đến +158 tỷ (2023) và +146 tỷ (2025), quyết định năm nào lợi nhuận "đẹp". Biên LNTT theo quý dao động 15–57%, có ba quý dưới 5%. Mục tiêu 550 tỷ năm 2026 gần như phải dựa vào tự doanh.

**F2 — Tài sản lớn nhất là tiền gửi ngân hàng đang cầm cố, gần như không tạo chênh lệch.**
- Tiền gửi có kỳ hạn, chứng chỉ tiền gửi và trái phiếu HTM chiếm 41–48% tổng tài sản giai đoạn 2022–2025 (6.266 tỷ cuối 2025; 5.714 tỷ tại 30/6/2026).
- Tại 30/6/2026 có 4.257 tỷ tiền gửi và 1.050 tỷ trái phiếu **đang cầm cố cho các khoản vay ngân hàng**, tức 93% (thuyết minh 8b, BCTC bán niên).
- Lợi suất khoảng 5–6%/năm, xấp xỉ hoặc thấp hơn chi phí vốn. Khoản này làm phình doanh thu (21–30%) và bảng cân đối nhưng gần như không tạo lợi nhuận.
- 🔎 Nhiều khả năng đây là điều kiện ngân hàng đặt ra để cấp hạn mức vay. Nếu đúng, chi phí vốn thực của mảng cho vay cao hơn con số ước tính.

**F3 — ROE thấp kéo dài** (xem N7).

### D. Bảng tổng hợp

| # | Vấn đề | Loại | Mức độ | DNSE tự kiểm soát được? | Sản phẩm số giải quyết được? |
|---|---|---|---|---|---|
| P1 | Tài khoản nhiều nhưng ít tiền (1,8% có tài sản ròng ≥10 triệu) | Mô hình kinh doanh | Rất cao | Có | **Có — trọng tâm** |
| P2–P3, N2, F1 | Lợi nhuận lõi đi ngang, biên sụp, phụ thuộc tự doanh, trượt kế hoạch | Tài chính | Rất cao | Một phần | Gián tiếp |
| N3, N5 | Môi giới lỗ 16 quý (riêng DNSE); miễn phí không còn khác biệt | Mô hình kinh doanh | Cao | Có | Có (kiếm tiền theo cách khác) |
| N4, F2 | Chi phí vốn tăng; tiền gửi cầm cố không tạo chênh lệch | Tài chính | Cao | Một phần | Có (tiền gửi của khách là nguồn vốn rẻ hơn) 🔎 |
| P5, N6 | Tập trung phái sinh, phái sinh chững | Chiến lược | Cao | Thấp | Một phần (T+0) |
| N1 | Vi phạm pháp luật, dịch vụ bị buộc dừng | Pháp lý, quản trị | Cao | Có | **Là ràng buộc** cho mọi sản phẩm mới |
| P7 | Lỗi app, lỗi mở tài khoản | Vận hành | Cao | Có | Có |
| P8, N10 | Mất lòng tin | Thương hiệu | Cao | Có | Có (minh bạch điều khoản) |
| P9 | Thu hút sai nhóm khách | Chiến lược | Trung bình–Cao | Có | Có |
| N9 | Sản phẩm sinh lời kém cạnh tranh | Sản phẩm | Trung bình | Có | **Có — trọng tâm** |
| N7–N8, F3 | Giá cổ phiếu yếu, ROE thấp, xa cam kết IPO | Thị trường vốn | Trung bình | Gián tiếp | Gián tiếp |

## 1.8 Tỷ lệ tài khoản active: DNSE so với đối thủ và ngành

*Tra cứu ngày 24/09/2026. Câu hỏi: 5,7% là vấn đề riêng của DNSE hay hiện tượng chung của ngành? Mọi số dưới đây đã đối chiếu lại với nguồn, không lấy từ báo cáo của nhóm.*

### A. Số liệu của DNSE (báo cáo thường niên 2025, PDF trang 29–30 = trang in 56–58)

| Chỉ tiêu | 12/2024 | 12/2025 |
|---|---:|---:|
| Tổng tài khoản, cuối kỳ | 994.811 | 1.512.920 |
| Khách active trong tháng | 41.900 | 85.739 |
| Tỷ lệ active | **4,2%** | **5,7%** |

- **Định nghĩa:** chú thích Hình 23 ghi *"sử dụng tối thiểu 1 sản phẩm trong tháng"*; phần chữ ghi *"khách hàng active giao dịch… khách hàng có giao dịch"*. Hai cách viết hơi khác nhau, nhưng cả hai đều đo trong **một tháng** (monthly active).
- **Chuỗi active theo tháng năm 2025 (Hình 23):** 51.815 (T1), 65.369, 68.845, 68.267, 68.272, 69.145, 71.785, 77.349, 83.741, 86.181, **87.285 (T11, cao nhất)**, 85.739 (T12).
- **Tài khoản mở mới theo quý 2025 (Hình 21):** Q1 131.122 (34% thị trường), Q2 104.785 (18%), Q3 127.344 (16%), Q4 155.263 (19%); cả năm 518.514 trên 2.573.945 (20%).
- **Tổng tài khoản theo năm (Hình 22):** 5.548 (2020), 44.727 (2021), 189.845 (2022), 561.279 (2023), 994.811 (2024), 1.512.920 (2025).
- 🔎 **Tài khoản mở mới so với khách active tăng thêm:** năm 2025 mở mới 518.514 tài khoản, nhưng số khách active chỉ tăng khoảng 43.800 (từ 41.900 lên 85.739). Tức cứ 100 tài khoản mở mới chỉ tương ứng khoảng **8 khách active tăng thêm**. Đây là phép chia hai mức tăng ròng, không theo dõi từng nhóm khách, nên chỉ là ước lượng.
- Tỷ lệ active **có cải thiện** (4,2% lên 5,7%). Báo cáo nên nói điều này để không bị coi là chọn số bất lợi.

### B. Đối thủ và ngành

| Công ty | Tổng tài khoản | Active | Tỷ lệ | Định nghĩa, kỳ đo | Nguồn | Mức tin cậy |
|---|---:|---:|---:|---|---|---|
| **DNSE** | 1.512.920 (31/12/2025) | 85.739 | **5,7%** | Dùng ≥1 sản phẩm trong tháng 12/2025 | BCTN 2025 | Sơ cấp |
| **TCBS** | >1,1 triệu (Q1/2025) | — | **~30%** | "Hoạt động thường xuyên", không nêu kỳ đo | Báo cáo HSC 19/8/2025 đăng trên tcbs.com.vn, trang 8 | Phân tích của HSC dựa trên số của TCBS; đã đọc bản gốc |
| **VNDirect** | 674.546 (cuối 2021) | 208.089 | **30,8%** | "Active (có giao dịch)", không nêu kỳ đo. Các năm trước đó dưới 25% | VietnamBiz 09/06/2022 | **(báo chí)**; chưa đối chiếu với BCTN 2021 của VNDirect |
| **VPS** | 1.547.000 (9/2025), khoảng 15% tài khoản toàn thị trường | Không công bố | — | Chỉ công bố cơ cấu tuổi của khách cá nhân hoạt động: dưới 30 tuổi 32%, 30–50 tuổi 61%, trên 50 tuổi 7% | Tài liệu giới thiệu IPO VPS, 10/2025, trang 9 | Sơ cấp (tài liệu công ty) |
| SSI, HSC, Vietcap, MBS, VPBankS | — | — | — | Không tìm thấy số công bố | — | — |

**Tham chiếu quốc tế** (báo cáo HSC, trang 23). Đây là tỷ lệ *tài khoản có nạp tiền*, không phải tỷ lệ active:
- Futu/Moomoo: khoảng 25,1 triệu người dùng, 2,4 triệu tài khoản có nạp tiền (khoảng 9,6%).
- eToro: khoảng 38 triệu đăng ký, 3,5 triệu tài khoản có nạp tiền (khoảng 9,2%).
- DNSE: 27.100 khách có NAV từ 10 triệu đồng, tức 1,8%. 🔎 Không so thẳng được, vì ngưỡng 10 triệu đồng cao hơn mức "có nạp tiền". BCTN có nhắc nhóm NAV từ 1 triệu đồng nhưng không công bố số.

**Tài khoản "chết" là hiện tượng chung của ngành:**
- Tháng 10/2023 toàn thị trường đóng 545.386 tài khoản, trong đó MBS đóng 543.753 (99,7%). MBS giải thích đây là các tài khoản *"đã mở trước đó nhưng không có phát sinh giao dịch"*. Cùng tháng chỉ mở mới 167.659, nên tổng tài khoản cá nhân trong nước giảm ròng khoảng 377.700, còn 7.384.707 (CafeBiz 07/11/2023, dẫn VSDC). Tính cả hai tháng, MBS đóng hơn 880.000 tài khoản (Saigon Times).
- Nguyên nhân mang tính cơ chế: mở tài khoản miễn phí qua eKYC, khuyến mãi khi mở tài khoản, một người mở ở nhiều công ty. VSDC đếm tài khoản chứ không đếm người.

### C. So sánh chắc hơn: cường độ giao dịch trên mỗi tài khoản

Cách này không phụ thuộc vào định nghĩa "active" của từng công ty. Tỷ số = thị phần môi giới ÷ tỷ trọng tài khoản; bằng 1 nghĩa là một tài khoản của công ty đó giao dịch ngang một tài khoản trung bình của thị trường. 🔎 Kết quả là xấp xỉ, vì số tài khoản của TCBS và VPS không cùng ngày với thị phần.

| Công ty | Tỷ trọng tài khoản | Thị phần HOSE Q2/2026 | Thị phần HNX Q2/2026 | Tỷ số |
|---|---:|---:|---:|---:|
| **DNSE** | ≥12,66% (1,7 triệu / 13.430.517, cùng ngày 30/6/2026) | <2,94% | 2,88% | **~0,23** |
| **TCBS** | ~9,9% (>1,2 triệu cuối 2025 / khoảng 12,12 triệu 🔎) | 9,36% | 9,00% | **~0,9** |
| **VPS** | ~15% (công ty tự công bố, 9/2025) | 12,61% | 17,71% | **~0,8–1,2** |

- 🔎 Tổng tài khoản cuối 2025 (khoảng 12,12 triệu) được ước tính bằng số cuối tháng 6/2026 (13.430.517) trừ phần tăng trong nửa đầu năm (1.312.232 trong nước và 1.638 nước ngoài).
- Thị trường tăng tài khoản nhanh hơn TCBS và VPS, nên tỷ trọng tài khoản thực tế của hai công ty này vào giữa năm 2026 có lẽ thấp hơn số trong bảng, và tỷ số của họ còn cao hơn nữa. Kết luận không đổi: **một tài khoản DNSE giao dịch bằng khoảng 1/4 một tài khoản TCBS hoặc VPS**.
- Giới hạn: thị phần sàn gồm cả giao dịch của khách tổ chức và nước ngoài. Công ty có nhiều khách tổ chức (SSI, HSC, Vietcap) sẽ có tỷ số cao hơn vì lý do đó, nên chỉ so với công ty bán lẻ tương tự như TCBS và VPS (VPS công bố 94% giá trị giao dịch đến từ khách cá nhân; TCBS chưa có số).

### D. Kết luận

1. Có khoảng cách lớn giữa tổng tài khoản và tài khoản active là **chuyện bình thường của ngành**.
2. Nhưng **mức của DNSE thấp hơn rõ rệt**: 5,7% chỉ bằng khoảng 1/5 mức ~30% mà TCBS và VNDirect công bố. Ngay cả những năm tệ nhất của VNDirect (dưới 25%) vẫn cao gấp khoảng 4 lần.
3. 🔎 Một phần chênh lệch đến từ định nghĩa: DNSE đo trong 1 tháng, còn TCBS và VNDirect không nêu kỳ đo, nhiều khả năng rộng hơn 1 tháng nên tỷ lệ tự nhiên cao hơn. Chênh 4–5 lần thì khó giải thích hết bằng định nghĩa, và cách so sánh ở mục C (không phụ thuộc định nghĩa) cho cùng kết quả.
4. TCBS là đối chiếu công bằng nhất: cùng mô hình app và eKYC, cùng quy mô khoảng 1,1–1,2 triệu tài khoản.
5. **Giới hạn phải ghi trong báo cáo:** chỉ 2 đối thủ công bố tỷ lệ active, định nghĩa không đồng nhất, số của VNDirect đã cũ (2021). Đây **không phải trung bình ngành**; nên viết "so với hai đối thủ có công bố".

## 1.9 Kiểm chứng số liệu tài khoản trong báo cáo (24/09/2026)

*Kiểm tra mọi con số về tài khoản, tỷ lệ active và thị phần trong `06_build_report.js` và `brokers.py`, đối chiếu với nguồn gốc. ✅ khớp nguồn gốc; ⚠️ khớp nhưng nguồn chỉ là thông cáo công ty hoặc báo chí; ❌ cần sửa.*

| # | Nội dung trong báo cáo (vị trí trong `06`) | Nguồn đang dùng | Kết quả kiểm chứng |
|---|---|---|---|
| 1 | 1.512.920 tài khoản cuối 2025 (§3.2, Bảng A1) | BCTN 2025 | ✅ BCTN, Hình 22 |
| 2 | 85.739 khách active tháng 12/2025, "used any product in December" (§3.2, §7) | BCTN 2025 | ✅ BCTN, Hình 23; mô tả trong báo cáo đúng định nghĩa |
| 3 | 27.100 khách có NAV từ 10 triệu (§3.2, §7) | BCTN 2025 | ✅ BCTN, trang 30 |
| 4 | 2025: 20% thị phần mở mới (§3.1, Bảng A1) | BCTN 2025 | ✅ 518.514 / 2.573.945. Ghi chú: mẫu số "toàn thị trường" là mức tăng ròng tài khoản của VSDC (Vietstock: Q1/2025 "tăng thêm gần 388.000"), nên nếu có đóng tài khoản thì thị phần hơi cao hơn thực tế. Ảnh hưởng nhỏ |
| 5 | Q1/2025: 34% thị phần mở mới (chỉ có trong ghi chú này) | BCTN 2025 | ✅ 131.122 / 388.089. Thông cáo tháng 4/2025 ghi 128.000 và 33% là số sơ bộ; dùng số BCTN |
| 6 | Q1/2024: hơn 120.000 tài khoản, 30% thị phần mở mới (§3.1) | Báo chí | ⚠️ Khớp VnEconomy, nhưng đó là thông cáo công ty. Có thể thay bằng số trong BCTN 2024 |
| 7 | Q1/2026: 142.000 tài khoản, 18% thị phần; 1,65 triệu tài khoản (§3.1, Bảng A1) | Thông cáo | ⚠️ Khớp Vietstock 04/2026; chưa có văn bản gốc |
| 8 | "Hơn 1,7 triệu" khách hàng giữa năm 2026 (tóm tắt, §1.2, §3.1) | Thông cáo | ⚠️ Khớp Mekong Asean 21/7/2026. "Hơn 1,7 triệu" là cận dưới |
| 9 | **Tỷ trọng tài khoản 12,27%**, "13,85 triệu tài khoản" (tóm tắt "one eighth", §3.2, §4.4, B1, Hình 3) | `brokers.py`: 1,7 triệu / 13.852.633 | ❌ **Lệch ngày**: tử số tại 30/6/2026, mẫu số tại 31/8/2026. VSDC tại 30/6/2026 là **13.430.517** nên tỷ trọng là **≥12,66%**. Ngoài ra mẫu số ngày 31/8 thực tế là 13.814.693 + 52.633 = 13.867.326 (báo cáo làm tròn xuống 13,80 triệu và bỏ tài khoản tổ chức trong nước). Kết luận không đổi (0,23 và 0,11), nhưng phải sửa số. Ở §4.4, mốc "55.000 tỷ" đổi thành khoảng **57.000 tỷ** |
| 10 | HNX Q2/2026: DNSE 2,88%, hạng 8 (tóm tắt, §3.2) | Thông báo gốc HNX | ✅ Khớp |
| 11 | HOSE Q2/2026: top 10, tổng 65,19% (Q1: 69,05%), hạng 10 là 2,94% (§1.1, §3.2) | Thông báo gốc HOSE (api.hsx.vn) | ✅ Khớp cả 10 dòng |
| 12 | Phái sinh Q2/2026: DNSE 25,38%, VPS 33,84% (tóm tắt, §3.1) | Thông báo gốc HNX | ✅ Khớp. Cả nửa năm 2026: 25,47% (thông cáo DNSE) |
| 13 | Dư nợ toàn ngành 453.800 tỷ, DNSE 1,39% (tóm tắt, §3.2, §4.4) | Vietstock | ⚠️ Vẫn là báo chí. Tổng BCTC của 42 công ty là 345.309 tỷ (76%), tăng 7,3% trong quý, khớp mức 7% báo đưa; DNSE chiếm 1,82% tổng này. Mục B1 của báo cáo đã giải thích |
| 14 | "DNSE has grown its customer base faster than any competitor" (§3.1, dòng 367) | Không có nguồn | ❌ Không kiểm chứng được "any competitor", vì VSDC không công bố số theo công ty. Nên thay bằng so sánh với hai đối thủ có công bố: năm 2025 DNSE mở mới 518.514; TCBS hơn 138.000; VPS khoảng 124.000 (tăng từ 1.423.000 lên 1.547.000 trong 12/2024–9/2025) |
| 15 | Giới hạn B3: "Per-broker account counts are not published by any firm other than DNSE" (dòng 630) | — | ❌ **Sai**: VPS (1.547.000, 9/2025) và TCBS (>1,1 triệu Q1/2025 với ~30% hoạt động thường xuyên; >1,2 triệu cuối 2025) đều công bố. Phải sửa, và nên đưa so sánh đối thủ ở mục 1.8C vào §3.2 |
| 16 | Tiền của khách 1,15 triệu/tài khoản (chỉ có trong ghi chú này, P1) | BCTC, ngoại bảng | ⚠️ BCTN ghi "tổng giá trị tiền gửi của khách hàng" 3.157 tỷ tại 31/12/2025 (CASA), trong khi BCTC ngoại bảng ghi 2.903 tỷ. Hai định nghĩa khác nhau; khi trích dẫn phải nói rõ dùng số nào |

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
- BCTC công ty chứng khoán tách **doanh thu và chi phí trực tiếp** theo từng mảng. Nhờ vậy tính được kết quả của môi giới và tự doanh, nhưng không tính được lợi nhuận của mảng cho vay, vì chi phí vốn không được phân bổ.
- **H1/2026, từ doanh thu đến lợi nhuận:** lãi cho vay 336 tỷ cộng lãi tiền gửi/trái phiếu 193 tỷ chưa đủ bù chi phí vốn 324 tỷ và chi phí môi giới 267 tỷ. LNTT còn 112 tỷ nhờ phí môi giới 222 tỷ và tự doanh thuần 34 tỷ.
- **Lãi cho vay** là nguồn thu lớn nhất từ 2022, với lợi suất ổn định 10–12%. 🔎 Câu "thị phần cho vay đứng yên khoảng 1,39%" chưa có chuỗi số liệu toàn ngành để kiểm chứng.
- **Phí môi giới** tăng mạnh từ 2025 nhờ phái sinh, nhưng lỗ sau chi phí trực tiếp 16 quý liền.
- **Tự doanh** dao động mạnh: lãi thuần 6,8 tỷ (2024) lên 146 tỷ (2025). Đây là nguồn quyết định lợi nhuận năm.
- Doanh thu tăng thêm 100 đồng thì lợi nhuận chỉ tăng khoảng 4 đồng (Q2/2026 so với cùng kỳ, theo số soát xét).

**Q2. Vì sao lợi nhuận giảm mà DNSE vẫn giữ miễn phí giao dịch?**
Bốn lý do:
1. Cam kết "trọn đời" không thể rút lại mà không mất uy tín với hơn 1,7 triệu khách.
2. Miễn phí giờ là chuẩn chung của ngành; bỏ nó thì DNSE mất định vị duy nhất.
3. Công ty đang coi đây là giai đoạn chiếm thị phần, sẽ thu tiền sau qua margin; ĐHCĐ 2026 nêu ý định nhân bản mô hình phái sinh sang cơ sở (báo chí).
4. Cần câu chuyện tăng trưởng để phát hành 3.500 tỷ trái phiếu.

*Cập nhật từ BCTC:* môi giới lỗ ở cấp chi phí trực tiếp **16 quý liền**, trong khi mọi đối thủ niêm yết đều có lãi ở mảng này. Chiến lược "chịu lỗ để chiếm thị phần" chưa có dấu hiệu thu hồi được tiền. Chỉ 5,7% tài khoản có hoạt động trong tháng 12/2025.

**Q3. Có phải DNSE đang "nuôi" Gen Z (nghèo bây giờ, giàu sau) cộng với đón đầu thị trường phái sinh?**
- Về lý thuyết, đây là chiến lược hợp lý ("capture young, monetise later"). Nhưng **dữ liệu hiện có đi ngược lại**:
  - Mô hình Findex xếp nhóm 15–24 thấp nhất về ưu tiên (2,25 so với 9,0–9,3).
  - Review cho thấy một phần khách đến vì săn thưởng, không vì ý định đầu tư.
  - Chỉ 1,8% tài khoản có tài sản ròng từ 10 triệu đồng; tiền mặt của khách khoảng 1,15 triệu/tài khoản.
  - Chi phí chuyển đổi thấp: một người có thể mở tài khoản ở nhiều công ty, nên giàu lên rồi họ vẫn có thể chuyển sang nơi khác.
  - Findex là số liệu một thời điểm, không chứng minh được một nhóm người sẽ giàu lên theo thời gian.
- **Điều kiện để giả thuyết này đúng:** phải có một sản phẩm **giữ lại phần tiền tăng thêm** khi thu nhập của Gen Z tăng. Tài khoản không ngủ (từ 6/2025) và Trứng Vàng là bước đầu nhưng chưa ở quy mô đáng kể. Đây là cầu nối trực tiếp sang khuyến nghị ở mục 2.6.

**Q4. DNSE cạnh tranh với VPS ở phái sinh thế nào? Vì sao hút khách ít tiền mà lại tập trung vào phái sinh?**
- **Cần sửa tiền đề:** trong phái sinh, ký quỹ là tiền nhà đầu tư tự nộp vào VSD (khoảng 17–18,5% giá trị hợp đồng), không phải khoản vay của công ty chứng khoán. Vì vậy phái sinh là mảng **ít tốn vốn** nhất với DNSE. Mảng tốn vốn là margin cổ phiếu cơ sở.
- *Điều chỉnh sau tra cứu mới:* DNSE đã dùng vốn của mình qua các dịch vụ "ứng trước ký quỹ" và "ứng lãi vị thế", và đây chính là các dịch vụ bị **buộc dừng từ 8/2026**. Từ nay phái sinh sẽ thực sự ít tốn vốn, nhưng cũng kém tiện lợi hơn.
- **Cách DNSE thắng thị phần:**
  - Phí 0 đồng, và trả thay phí VSD đúng lúc chuyển sang KRX (thị phần tăng từ 17,62% lên 23,67% cùng giai đoạn theo thông báo HNX; trùng thời điểm, chưa chứng minh nhân quả).
  - Công nghệ: API cho bot, tự động cắt lỗ, không phải chuyển tiền giữa tài khoản.
  - Cộng đồng: cuộc thi "Cưỡi sóng phái sinh". Chủ tịch nói tỷ lệ khách phái sinh rời bỏ "gần như bằng 0".
- **Cái giá:** chi phí môi giới tăng cùng nhịp doanh thu, nên phí phái sinh thu thêm không tạo lãi (N3).
- **Vì sao khách ít tiền đi cùng phái sinh:** chỉ cần vài chục triệu đồng là có đòn bẩy mà không phải trả lãi vay. Thị phần phái sinh lại dễ nhìn thấy, tốt cho thương hiệu sau IPO.
- **Chỗ không khớp:** kênh thu hút khách (trẻ, ít tiền, phái sinh) không trùng với nguồn lợi nhuận (margin cơ sở, cần khách có tài sản).

**Q5. Có nên dùng NLP để thu thập tin tức về DNSE?**
Không cần NLP nặng. Nên chọn lọc tin tức rồi trích sự kiện thủ công, hoặc gắn thẻ theo từ khóa như cách làm với review. Lý do: giám khảo chấm việc truy vết được nguồn, và kết luận từ mô hình NLP khó giải trình từng câu. *Cập nhật:* số liệu tài chính giờ lấy thẳng từ BCTC qua API (`01b`, `01c`), không cần qua tin tức.

**Q6. Vì sao báo cáo trước đây chỉ phân tích năm 2026?**
Data pack ban đầu dựng từ tin báo chí, mà báo chí chỉ đưa tin các kỳ gần nhất; BCTC gốc lại là bản scan. Giờ đã có chuỗi 2018–2026 (xem `bctc_analysis.md`).

## 2.3 Chẩn đoán: hành trình khách hàng gãy ở đâu

| Tầng | Sản phẩm / chiêu thức | Bằng chứng | Đánh giá |
|---|---|---|---|
| 1. Thu hút | Miễn phí giao dịch, thưởng đăng ký, KOL/YouTube, bảng giá Gen Z | 12,24% số tài khoản (12,74% cuối 2025); 518.514 tài khoản mở mới năm 2025, chiếm 20% toàn thị trường (34% trong Q1/2025) | ✅ Mạnh, nhưng đắt (môi giới lỗ 16 quý) và kéo theo khách săn thưởng |
| 2. Mở tài khoản | eKYC 3–5 phút, NFC, OTP | 19,6% review tiêu cực | ⚠️ Nhiều trục trặc |
| 3. **Nạp tiền lần đầu** | Thưởng 100.000đ kèm điều kiện nạp 2 triệu | **Chỉ 1,8% tài khoản có tài sản ròng từ 10 triệu; 5,7% active trong tháng 12/2025; tiền mặt khoảng 1,15 triệu/tài khoản.** Đây là trigger chính của các cáo buộc lừa đảo | ❌ **Điểm gãy chính** (giờ có bằng chứng sơ cấp) |
| 4. **Giữ tiền trên nền tảng** | Tài khoản không ngủ (từ 6/2025), Trứng Vàng | Chỉ 4 review nhắc tới; lãi 4,3% thấp hơn TCBS 6%; tiền khách giảm 32% trong Q2/2026 | ❌ Có sản phẩm nhưng ít người dùng, kém cạnh tranh |
| 5. Giao dịch, đòn bẩy | Future X, Margin Deal, Ensa, API | Phái sinh 25,38%; cho vay 1,39%; dư nợ/vốn chủ mới 116% | ⚠️ Mạnh ở phái sinh (nhưng lỗ phí); yếu ở margin cơ sở (nguồn lãi chính, không thiếu vốn mà thiếu khách có tài sản) |
| 6. Niềm tin, gắn bó | — | Cáo buộc lừa đảo 16,2%, phí đóng tài khoản, 3 lần bị phạt, bị mạo danh | ❌ |

**Insight chính:**
- DNSE đầu tư mạnh vào tầng 1 (thu hút) và tầng 5 (phái sinh), nhưng bỏ trống tầng 3–4.
- Tầng 3–4 lại chính là nơi tạo ra **tài sản đảm bảo cho nguồn lợi nhuận chính** (lãi margin). Dư địa vốn cho vay còn khoảng 4.600 tỷ, nhưng không có khách có tài sản để vay.
- Lỗ hổng không nằm ở công nghệ (3,9 ms, API) hay ở sản phẩm (đã có Tài khoản không ngủ, Trứng Vàng). Lỗ hổng nằm ở **thiết kế hành trình và cách định giá**.

## 2.4 Phát biểu bài toán BA

**Câu hỏi kinh doanh** (bản tiếng Anh dùng cho báo cáo):
> *How can DNSE convert its 1.7 million low-balance accounts into funded, asset-holding accounts through its digital product layer — without breaking the zero-fee promise and within regulatory limits?*

**Các bên liên quan:**
- Ban điều hành: P&L, kế hoạch 2026.
- Khách hàng: Gen Z và người đi làm.
- Cổ đông và trái chủ: chương trình trái phiếu 3.500 tỷ.
- UBCKNN: cơ quan phải duyệt sản phẩm mới.

**Vì sao phải làm ngay:**
- H2/2026 cần lợi nhuận gấp 3,9 lần H1, tức khoảng 219 tỷ mỗi quý.
- T+0 sắp áp dụng: CEO dự báo khách phái sinh sẽ chuyển một phần sang thị trường cơ sở (báo chí).
- FTSE nâng hạng từ 21/9/2026: dòng vốn hướng vào cổ phiếu vốn hóa lớn và vừa.
- Làn sóng tiết kiệm hộ gia đình: tỷ lệ tiết kiệm tại tổ chức tài chính tăng từ 19,9% lên 43,1% (Findex).
- Sau quyết định phạt 8/2026, DNSE phải thiết kế lại các dịch vụ tài chính.
- Chi phí vốn đã lên 6,5%, nên nguồn tiền của khách càng có giá trị.

**Chỉ số trọng tâm (north star):** tỷ lệ tài khoản có tài sản (funded-account rate) và tài sản bình quân trên mỗi tài khoản (AUA/account).
**Mốc hiện tại** (báo cáo thường niên 2025): 1,8% tài khoản có tài sản ròng từ 10 triệu; 5,7% active mỗi tháng; tiền mặt khoảng 1,15 triệu/tài khoản.

**Phân khúc mục tiêu — hai hướng song song:**

| Hướng | Phân khúc | Mục tiêu | Căn cứ |
|---|---|---|---|
| **Hướng 1 — kiếm tiền** | Người đi làm, học vấn THCS trở lên, thuộc 60% thu nhập cao (gồm cả khoảng 30% khách hiện hữu không thuộc Gen Z) | Tăng tài sản bình quân và dư nợ margin | Findex: priority score 9,0–9,3; activation gap 28,5–31,7 điểm; 15–17,5 triệu người chưa chuyển đổi |
| **Hướng 2 — tạo thói quen** | Khoảng 800.000 khách Gen Z đã có trên nền tảng **(báo chí)** | Tạo thói quen để lại tiền trên nền tảng, **chưa nhắm doanh thu ngay** | Activation gap lớn nhất (33,6 điểm); chi phí thu hút đã trả; đây là điều kiện để giả thuyết ở Q3 trở thành đúng |

## 2.5 Các phương án chiến lược sản phẩm số

**Tiêu chí so sánh:** (1) tác động tới doanh thu trên mỗi tài khoản có tài sản; (2) nhu cầu vốn; (3) khả thi pháp lý; (4) thời gian ra kết quả; (5) mức độ khớp với bằng chứng; (6) rủi ro chính.

| Phương án | Cơ chế | (1) | (2) | (3) | (4) | (5) | Đánh đổi / rủi ro |
|---|---|---|---|---|---|---|---|
| **A. Tiếp tục thu hút khách** | Tăng khuyến mãi, KOL, referral | Thấp | Thấp | Cao | Nhanh | Thấp | Thêm tài khoản từ nhóm ít tiền; chi phí môi giới đã +125–198% và mảng này lỗ 16 quý |
| **B. Bậc thang kích hoạt (activation ladder)** | Bật sẵn Tài khoản không ngủ khi mở tài khoản; tự động chuyển tiền nhàn rỗi → Trứng Vàng / quỹ → cổ phiếu / Margin Deal; sửa luồng nạp tiền lần đầu | **Cao** | TB (trả lãi cho khách; nhưng tiền khách gửi cũng là nguồn vốn) | TB (phải báo cáo UBCKNN trước) | TB | **Cao** | Phải định giá cạnh tranh với TCBS 6%; cần **hoàn tất thương vụ công ty quản lý quỹ đã được ĐHCĐ thông qua**, hoặc đối tác trong thời gian chờ; rủi ro niềm tin khi giữ tiền của khách |
| **C. Cầu nối phái sinh → cơ sở (dựa trên T+0)** | Một chạm chuyển từ phái sinh sang cổ phiếu hoặc Margin Deal; gói ưu đãi margin cho khách phái sinh | TB–Cao | Cao (cần vốn cho vay; còn khoảng 4.600 tỷ dư địa) | Cao | Phụ thuộc lộ trình T+0 | TB (dựa vào phát biểu của CEO) | Chưa biết thời điểm T+0; khách phái sinh ít tiền |
| **D. Freemium → Premium** | Giữ miễn phí giao dịch; thu phí dịch vụ nâng cao: Ensa Pro, gói API/bot, dữ liệu | TB | Thấp | Cao | Nhanh | Thấp–TB (chưa có dữ liệu về nhu cầu trả phí) | Đi ngược hình ảnh "miễn phí" nếu làm không khéo |
| **E. Thu phí trở lại / gói phí** | Áp lại phí giao dịch hoặc bán gói phí | Cao ngắn hạn | Thấp | Cao | Nhanh | Thấp | **Loại**: phá cam kết "trọn đời", cộng hưởng với vấn đề niềm tin. 🔎 Tuy vậy, môi giới là mảng duy nhất DNSE lỗ trong khi đối thủ lãi; cần làm rõ chi phí môi giới gồm những gì trước khi loại hẳn hướng "tái cấu trúc chi phí môi giới" |

**Mỗi phương án phải hy sinh gì:**
- **A** bảo vệ thị phần tài khoản mở mới nhưng làm nặng thêm P1–P3 và N3.
- **C** tận dụng thế mạnh phái sinh nhưng phụ thuộc vào thời điểm T+0.
- **D** không cần vốn nhưng chỉ kiếm tiền từ nhóm nhỏ khách chuyên nghiệp, không chạm vào khoảng 1,7 triệu tài khoản ít tiền.
- **B** là phương án duy nhất **tác động vào đúng tầng 3–4 đang gãy**, dựa trên sản phẩm đã có sẵn, và **khớp với định hướng chính công ty đã thông qua** (công ty quản lý quỹ; Trứng Vàng với ba ngân hàng).

## 2.6 Khuyến nghị sơ bộ (ý tưởng chiến lược cho Round 3A)

**Chiến lược "Kích hoạt trước tiên":** phương án B là lõi, C là đòn bẩy giai đoạn 2, D chỉ thử nghiệm nhỏ.

**Chuỗi tạo giá trị:**
> Tiền nhàn rỗi tự động vào Tài khoản không ngủ → một phần chuyển sang Trứng Vàng hoặc chứng chỉ quỹ → tài sản trên nền tảng tăng → tài sản đảm bảo cho Margin Deal tăng → dư nợ và thu nhập lãi tăng mà **không cần khách giao dịch nhiều hơn** → cộng thêm phí phân phối quỹ, khoản thu định kỳ không phụ thuộc hướng thị trường (giảm phụ thuộc tự doanh, F1).

**Phạm vi đề xuất cho Round 3A:**
1. **Sửa tầng 3:** bỏ phí đóng tài khoản 100.000đ; viết lại điều khoản thưởng 100.000đ / nạp 2 triệu cho minh bạch; thêm luồng "nạp tiền lần đầu" với mức tối thiểu thấp (Trứng Vàng đã cho phép bắt đầu từ 1 triệu). Mục tiêu: nâng tỷ lệ tài khoản có tài sản ròng từ 10 triệu lên trên mốc 1,8%.
2. **Nâng tầng 4:** bật sẵn Tài khoản không ngủ khi mở tài khoản; tách phần lãi thưởng theo giao dịch ra khỏi lãi tiết kiệm để người chỉ gửi tiền hiểu rõ mình nhận bao nhiêu. 🔎 Mức lãi cạnh tranh với TCBS iPower là giả thuyết, cần test giá. Chi phí vốn hiện 6,5% là trần tham chiếu cho lãi trả khách.
3. **Nguồn tiền vào tự động cho Hướng 1:** chuyển lương tự động hoặc nạp tiền định kỳ qua ngân hàng đối tác (Vietcombank, VietinBank, BIDV đã nằm trong kế hoạch 2026) hoặc ZaloPay (đã có Open API). 🔎 Mức độ chấp nhận là giả thuyết.
4. **Bậc thang tài sản:** tiền nhàn rỗi → trái phiếu / quỹ → cổ phiếu → Margin Deal. Mỗi bậc là một lần kích hoạt đo được.
5. **Giai đoạn 2 — cầu nối T+0:** đưa khách phái sinh sang cổ phiếu và Margin Deal khi T+0 được áp dụng.

**Điều kiện khả thi:**

| Điều kiện | Hiện trạng |
|---|---|
| Sản phẩm | ✅ Đã có Tài khoản không ngủ (6/2025), Trứng Vàng, Margin Deal |
| Vốn | ✅ Trái phiếu 2.500 + 1.000 tỷ (NQ 01/2026) và khoảng 1.275 tỷ từ quyền mua. Dư nợ/vốn chủ mới 116%, còn khoảng 4.600 tỷ dư địa trước trần 200% |
| Quản lý quỹ | ✅ Chủ trương sở hữu một công ty quản lý quỹ làm công ty con đã được thông qua hai năm liền (NQ 01/2025, NQ 01/2026 Điều 15). ⚠️ Chưa thực hiện; cần đối tác phân phối trong thời gian chờ |
| Đối tác ngân hàng | ✅ Kế hoạch 2026 dự kiến hợp tác Vietcombank, VietinBank, BIDV cho Trứng Vàng gồm trái phiếu và chứng chỉ quỹ (Tờ trình 05) |
| Công nghệ | ✅ 3,9 ms, Open API, microservices |
| **Pháp lý** | ⚠️ **Phải báo cáo UBCKNN trước khi ra mắt**: bài học từ quyết định 461/QĐ-XPHC. Đây là điều kiện tiên quyết, không phải chi tiết phụ |

**Ước lượng giá trị:** tăng dư nợ thêm 1.000 tỷ (+16%) mang lại khoảng 112 tỷ thu nhập lãi gộp/năm (lợi suất 11,2%). **Sau chi phí vốn khoảng 6,3%, còn khoảng 49 tỷ/năm, bằng 9% mục tiêu LNTT 2026.** Chi phí vốn là ước tính vì dòng 24 gộp dự phòng với chi phí vay; nếu tiền gửi cầm cố (F2) là điều kiện vay thì chi phí thực còn cao hơn.

## 2.7 Hướng kiểm chứng (giả định, test, KPI)

| # | Giả định cần kiểm chứng | Cách test ở Round 3 | KPI |
|---|---|---|---|
| A1 | Phần lớn tài khoản DNSE gần như không có tiền | **Đã có mốc công bố:** 5,7% active, 1,8% có tài sản ròng từ 10 triệu. Cần phân phối số dư dưới ngưỡng này từ dữ liệu nội bộ | % tài khoản có tài sản; tài sản bình quân trên mỗi tài khoản |
| A2 | Bật sẵn Tài khoản không ngủ làm tăng lượng tiền giữ lại | A/B test luồng mở tài khoản | Tỷ lệ bật tính năng; tỷ lệ tài khoản có tài sản sau 30 và 90 ngày |
| A3 | Khách nhạy với lãi suất khi so với TCBS và ngân hàng | Price ladder hoặc conjoint trên phân khúc Hướng 1 | Tiền nạp vào tăng thêm khi lãi tăng 0,5 điểm |
| A4 | Tài sản trên nền tảng kéo theo dư nợ margin | Hồi quy dư nợ theo tiền khách (chuỗi quý từ BCTC) và AUM (theo quý trong báo cáo thường niên); đối chiếu chéo với 9 đối thủ (`peer_financials.json`) | Dư nợ trên mỗi tài khoản có tài sản |
| A5 | Số dư của Gen Z tăng dần và họ ở lại DNSE | Theo dõi các nhóm khách theo năm mở tài khoản 2021–2026 | Tăng trưởng số dư theo nhóm; tỷ lệ còn hoạt động sau 12 tháng |
| A6 | Sản phẩm được UBCKNN chấp thuận | Tham vấn trước với UBCKNN | Có chấp thuận trước ngày ra mắt |
| A7 | Minh bạch điều khoản giúp lấy lại lòng tin | So sánh review trước và sau khi thay đổi | % review tiêu cực thuộc nhóm "lừa đảo" và "khuyến mãi" |
| A8 | T+0 kéo khách phái sinh sang thị trường cơ sở | Theo dõi hành vi sau khi T+0 được áp dụng | % khách phái sinh giao dịch cả cổ phiếu |
| A9 | Chi phí môi giới có thể giảm mà không mất khách | Tách cấu phần chi phí môi giới (phí sở, hoa hồng đối tác, marketing) từ dữ liệu nội bộ; so với đối thủ | Kết quả môi giới sau chi phí trực tiếp |

## 2.8 Việc cần làm với báo cáo hiện tại (còn 3 ngày)

**Đã làm** (báo cáo build ngày 24/9):
- ✅ Số liệu tài chính lấy từ BCTC; LNTT soát xét 111,6; tỷ trọng doanh thu 71,5%; bỏ con số 405%.
- ✅ Thêm Q4/2025 (hai quý biên dưới 4%) và môi giới lỗ 16 quý.
- ✅ Viết lại câu về quản lý quỹ theo NQ 01/2026 Điều 15; bỏ VNDA và carbon.
- ✅ Thêm bằng chứng 5,7% active và 1,8% có tài sản ròng từ 10 triệu vào mục 3.2.
- ✅ Số liệu đối thủ theo BCTC; DNSE đứng thứ 9/11 về LNTT Q2/2026.
- ✅ Giá trị khuyến nghị tính sau chi phí vốn; tiến độ kế hoạch tính theo tổng doanh thu.
- ✅ (25/9) Thị phần HOSE, HNX, phái sinh đọc từ thông báo gốc; Bảng A2 đủ top 10 cả ba thị trường; Figure 2 đủ 10 quý từ Q1/2024, không còn khoảng trống.
- ✅ (25/9) VPS lấy từ BCTC (mã VCK); bỏ nguồn Mekong Asean và hai bài Vietstock về thị phần. Chỉ còn tổng dư nợ ngành 453.800 là số báo chí.
- ✅ (25/9) Mẫu số tài khoản là bộ đếm VSDC 13.887.603 (24/9/2026): tỷ trọng 12,24%. Thanh khoản so sánh cùng kỳ Q2/2026: hợp đồng VN30 tháng gần nhất 40.855 tỷ/ngày so với HOSE 22.163 tỷ/ngày (thay 43.925 và 17.336 của báo).

**Còn phải làm**, theo thứ tự ưu tiên:
1. **Rút báo cáo từ 3.797 xuống dưới 3.500 từ.**
2. **Đổi khuyến nghị từ "xây mới" sang "mở rộng và định giá lại"** Tài khoản không ngủ và Trứng Vàng, gắn với kế hoạch hợp tác ba ngân hàng mà công ty đã công bố.
3. **Sửa mốc so sánh lãi suất:** sản phẩm rút được bất cứ lúc nào thì so với các gói sinh lời tự động (ngân hàng 3,5–4,3%, TCBS 6%); sản phẩm có kỳ hạn mới so với tiền gửi có kỳ hạn (6–9%).
4. **Thêm quyết định phạt 17/8/2026** vào phần rủi ro, phần khả thi và phần kiểm chứng (đối chiếu quyết định gốc trên ssc.gov.vn trước).
5. **Cân nhắc thay Figure 7 bằng biểu đồ lợi nhuận lõi và tự doanh** (`fig/bctc/bctc_10_core_profit.png`), và thêm một câu về tiền gửi cầm cố (F2) ở mục 4.4.
6. **Bổ sung cơ chế ký quỹ phái sinh vào §4.1** (tiền của nhà đầu tư, không phải khoản vay), kèm ghi chú về các dịch vụ "ứng trước" vừa bị buộc dừng.
7. ~~Chuỗi thị phần phái sinh (Figure 2)~~ ✅ Đã đủ từ thông báo gốc HNX, gồm Q2–Q3/2024 (5,11%, 5,30%); Q1/2025 là 16,72%, Q2/2025 là 17,62%.
8. **Ghi chú** rằng doanh thu môi giới Q2 giảm chủ yếu do thanh khoản phái sinh giảm khoảng 23% (hợp đồng tháng gần nhất, Vietcap).
9. **Tỷ trọng tài khoản:** code đã đọc mẫu số từ `market_macro.json` (12,24%, bộ đếm VSDC ngày 24/9). Nếu team muốn dùng số cùng ngày 30/6 (≥12,66%, VSDC qua Tạp chí KT-TC), chỉ cần đổi `vsdc_latest` trong `01d` rồi build lại; toàn bộ câu chữ và Hình 3 tự cập nhật.
10. **Sửa giới hạn B3** (`06` dòng 630), vì VPS và TCBS có công bố số tài khoản. Nên đưa bảng cường độ giao dịch ở mục 1.8C vào §3.2: nó biến điểm yếu "không có đối thủ để so" thành bằng chứng mạnh nhất cho P1.
11. **Thay câu "faster than any competitor"** (`06` dòng 367) bằng so sánh với TCBS và VPS (mục 1.9 dòng 14).
12. **Thêm xu hướng active 4,2% lên 5,7%** vào §3.2, kèm so sánh với TCBS ~30%, ghi rõ giới hạn định nghĩa.
13. **Cân nhắc thay một câu ở §3.2 bằng chuỗi thời gian** (`fig/bctc/bctc_12_dnse_shares.png`): tỷ trọng tài khoản tăng từ 2,75% lên 12,74% trong 2022–2025, còn tỷ trọng dư nợ giảm từ 2,74% xuống 1,85%. Đây là bằng chứng theo thời gian mạnh hơn cho P1 so với một thời điểm duy nhất.
*Mục 9–13: thay chữ chứ không thêm chữ, vì báo cáo vẫn phải xuống dưới 3.500 từ.*

---

## Nguồn

**Nguồn gốc (sơ cấp):**
- BCTC DNSE Q1/2018–Q2/2026, mọi dòng: Vietcap IQ, `iq.vietcap.com.vn/api/iq-insight-service/v1/company/DSE/financial-statement` (kéo bằng `01b_dnse_financials_fetch.py`, ngày 24/9/2026).
- [BCTC Q2/2026 (20/7/2026) và BCTC bán niên 2026 soát xét (14/8/2026) — IR DNSE](https://ir.dnse.com.vn/vi/ctype-finance_report)
- BCTC 9 công ty chứng khoán niêm yết (TCX, SSI, VPX, HCM, VND, VCI, MBS, SHS, VIX): Vietcap IQ, kéo bằng `01c_peer_financials_fetch.py`.
- [Báo cáo thường niên 2025 — IR DNSE](https://ir.dnse.com.vn/vi/ctype-yearly_report): số tài khoản, khách active, tài sản ròng, AUM (trang 29–30); Tài khoản không ngủ (trang 35).
- [Nghị quyết 01/2026/NQ-DNSE-ĐHĐCĐ, biên bản và tờ trình ĐHCĐ 2026 — IR DNSE](https://ir.dnse.com.vn/vi/ntag-dai-hoi-dong-co-dong-19)
- [VSDC](https://www.vsd.vn/vi/): bộ đếm số tài khoản giao dịch (13.887.603, ngày 24/9/2026).
- [Báo cáo thường niên 2025, bản PDF trực tiếp](https://cdn.dnse.com.vn/dnse-assets/CBTT/DSE%20-%20BCTN%202025.pdf): Hình 21 (mở mới theo quý), Hình 22 (tài khoản theo năm), Hình 23 (active theo tháng), trang 29–30.
- [Tài liệu giới thiệu IPO VPS, 10/2025](https://s3-storage.shs.com.vn/shs-website/Sites/QuoteVN/SiteRoot/reportattach/20251023_145047_IPO%20VPS..pdf): số tài khoản 12/2019–9/2025, cơ cấu tuổi khách hoạt động (trang 9).
- [Báo cáo HSC về TCBS, 19/8/2025](https://www.tcbs.com.vn/documents/10181/757092/TCBS-Report-19-Aug-25-VN_byHSC.pdf): 1,1 triệu tài khoản, ~30% hoạt động thường xuyên (trang 8); Futu, eToro (trang 23).

*Đối chiếu tỷ lệ active và tổng tài khoản thị trường (mục 1.8, 1.9):*
- [VietnamBiz — Tỷ lệ tài khoản nằm chết cao (VNDirect 2021)](https://vietnambiz.vn/mot-nguoi-co-hang-chuc-tai-khoan-ty-le-nam-chet-cao-con-so-ky-luc-tai-khoan-mo-moi-con-nghia-ly-gi-202269161920589.htm)
- [Vietstock — TCBS lợi nhuận 2025 (hơn 1,2 triệu khách cá nhân)](https://vietstock.vn/2026/01/tcbs-loi-nhuan-nam-2025-dat-ky-luc-hon-7100-ty-dong-737-1390730.htm)
- [CafeBiz — 99,7% tài khoản bị đóng tháng 10/2023 đến từ MBS](https://cafebiz.vn/997-trong-so-gan-550000-tai-khoan-chung-khoan-bi-dong-trong-thang-10-deu-den-tu-mbs-176231107204845206.chn)
- [Saigon Times — Hơn 880.000 tài khoản tại MBS đóng trong hai tháng](https://thesaigontimes.vn/hon-880-000-tai-khoan-chung-khoan-tai-mbs-dong-trong-hai-thang/)
- [Tạp chí KT-TC — Tài khoản vượt 13,4 triệu sau nửa đầu năm (VSDC 30/6/2026)](https://tapchikinhtetaichinh.vn/tai-khoan-chung-khoan-vuot-moc-13-4-trieu-sau-nua-dau-nam-161247.html)
- [Nhân Dân — Tháng 8/2026 mở mới gần 230.000 tài khoản (VSDC 31/8/2026)](https://nhandan.vn/tam-thang-dau-nam-viet-nam-co-them-hon-2-trieu-tai-khoan-chung-khoan-post988680.html)
- [Fili — DNSE thị phần mở mới 20%, active users 2025](https://fili.vn/2026/01/dnse-duy-tri-thi-phan-tai-khoan-mo-moi-20-so-luong-active-users-nam-2025-gap-doi-nam-truoc-737-1396577.htm)
- [Vietstock — DNSE 33% thị phần mở mới Q1/2025 (số sơ bộ)](https://vietstock.vn/2025/04/dnse-nam-33-thi-phan-tai-khoan-chung-khoan-mo-moi-trong-quy-1-830-1297161.htm)
- [Mekong Asean — DNSE H1/2026: hơn 1,7 triệu khách hàng](https://mekongasean.vn/doanh-thu-hoat-dong-dnse-tang-gan-60-trong-6-thang-dau-nam-57583.html)
- [Mekong Asean — Thị phần môi giới HOSE quý 2/2026](https://mekongasean.vn/thi-phan-moi-gioi-hose-quy-22026-vps-tiep-tuc-dan-dau-vpbanks-len-cao-ky-luc-57063.html)
- [VnEconomy — DNSE 30% thị phần mở mới Q1/2024](https://vneconomy.vn/dnse-chiem-30-thi-phan-tai-khoan-chung-khoan-mo-moi-trong-quy-1.htm)
- Phân tích và biểu đồ: `bctc_analysis.md`, `fig/bctc/`.

**Tài liệu nội bộ:** `doc/[FBA 6] QUESTION BOOKLET ROUND 2 (1).pdf`; `FBA_Round2_DNSE_data_pack.xlsx`; `FBAR2_2026_DNSE_Analysis.docx`; `doc/dnse.md`.

**Báo chí (thứ cấp):**

*Công ty, IPO, vốn:*
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

*Xử phạt, pháp lý:*
- [Market Times — Phạt 802,5 triệu](https://markettimes.vn/chung-khoan-dnse-dse-cua-chu-tich-nguyen-hoang-giang-bi-phat-128642.html)
- [Phụ nữ Việt Nam — Buộc dừng dịch vụ tài chính](https://phunuvietnam.vn/cong-ty-chung-khoan-dnse-bi-buoc-dung-cung-cap-dich-vu-tai-chinh-238260818165854342.htm)
- [Thương trường — Chi tiết vi phạm](https://thuongtruong.com.vn/news/chung-khoan-dnse-bi-phat-8025-trieu-dong-vi-loat-vi-pham-trong-hoat-dong-chung-khoan-168363.html)
- [Thương hiệu & Công luận — Phạt 125 triệu (mã L18)](https://thuonghieucongluan.com.vn/cong-ty-co-phan-chung-khoan-dnse-bi-xu-phat-125-trieu-dong-a243582.html)
- [DNSE — Cảnh báo lừa đảo](https://www.dnse.com.vn/tin-tuc/canh-bao-lua-dao-va-khuyen-cao-giao-dich-an-toan)

*Kết quả kinh doanh* (đã được BCTC thay thế; giữ để tham chiếu):
- [Báo Đầu tư — LN Q4/2025 giảm mạnh](https://baodautu.vn/chi-phi-moi-gioi-tang-cao-loi-nhuan-chung-khoan-dnse-quy-iv2025-giam-manh-d493637.html)
- [Báo Pháp luật — Q1/2026](https://doanhnhan.baophapluat.vn/chung-khoan-dnse-dse-bao-doanh-thu-quy-i-tang-62-du-no-margin-ap-sat-moc-6-000-ty-dong.html)
- [Vietstock — Q1/2026](https://vietstock.vn/2026/04/dnse-noi-tiep-da-tang-truong-doanh-thu-va-du-no-margin-737-1429717.htm)
- [Người Đưa Tin — H1/2026](https://www.nguoiduatin.vn/doanh-thu-moi-gioi-dnse-tang-hon-80-sau-nua-dau-nam-2026-204260721150941466.htm)
- [Mekong Asean — H1/2026](https://mekongasean.vn/doanh-thu-hoat-dong-dnse-tang-gan-60-trong-6-thang-dau-nam-57583.html)
- [Báo Pháp luật — Q2/2026](https://doanhnhan.baophapluat.vn/du-no-margin-lap-dinh-6-300-ty-dong-loi-nhuan-quy-ii-cua-chung-khoan-dnse-dse-tang-13.html)

*ĐHCĐ 2026* (đã được nghị quyết và tờ trình thay thế; các nội dung VNDA và carbon trong bài Báo Pháp luật không có trong văn bản):
- [Báo Đầu tư](https://baodautu.vn/dhdcd-dnse-san-sang-cho-giao-dich-t0-dat-muc-tieu-tham-vong-nam-2026-d553634.html)
- [Báo Pháp luật — Carbon, quỹ, trung tâm dữ liệu](https://doanhnhan.baophapluat.vn/dhdcd-dnse-len-ke-hoach-tham-gia-san-tin-chi-carbon-phat-hanh-3-500-ty-dong-trai-phieu-nam-2026.html)
- [Dân trí — IFC](https://dantri.com.vn/kinh-doanh/dnse-thong-qua-chu-truong-thanh-lap-cong-ty-chung-khoan-tai-ifc-20260327114025078.htm)
- [Nhà Quản lý](https://nhaquanly.vn/dhdcd-dnse-2026-chot-muc-tieu-tang-truong-loi-nhuan-tren-60-huy-dong-3500-ty-qua-trai-phieu-a18342.html)

*Phái sinh, cạnh tranh, Gen Z:*
- [Người Quan Sát — Thanh khoản Q2/2026 giảm 22%](https://nguoiquansat.vn/thi-truong-phai-sinh-ha-nhiet-thanh-khoan-quy-ii-boc-hoi-22-cuoc-choi-moi-gioi-van-thuoc-ve-vps-va-dnse-302475.html)
- [VnExpress — Chiến lược bứt tốc phái sinh](https://vnexpress.net/chien-luoc-giup-dnse-but-toc-tren-duong-dua-phai-sinh-4888928.html)
- [Fili — Phái sinh 2025](https://fili.vn/2026/01/thi-truong-phai-sinh-2025-vps-danh-roi-thi-phan-dnse-tao-buoc-nhay-vot-830-1389313.htm)
- [Vietstock — Top 2 Q2/2026](https://vietstock.vn/2026/07/dnse-giu-vung-top-2-thi-phan-chung-khoan-phai-sinh-tiep-tuc-mo-rong-dau-an-tren-thi-truong-737-1463117.htm)
- [Nhà Đầu Tư — Trả hộ phí ký quỹ](https://nhadautu.vn/chung-khoan-dnse-choi-lon-khi-tra-ho-phi-ky-quy-phai-sinh-cho-khach-hang-d96127.html)
- [Tin nhanh CK — Cuộc đua miễn phí giao dịch](https://www.tinnhanhchungkhoan.vn/khi-ong-lon-tham-gia-cuoc-dua-mien-phi-giao-dich-post342834.html)
- [VnExpress — Cách DNSE thu hút Gen Z](https://vnexpress.net/cach-dnse-thu-hut-khach-hang-gen-z-4916725.html)
- [Vietstock — Bảng giá Gen Z](https://vietstock.vn/2025/05/dnse-ra-mat-phien-ban-bang-gia-dau-tien-tren-thi-truong-danh-rieng-cho-gen-z-737-1313381.htm)

*Sản phẩm và công nghệ:*
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

# -*- coding: utf-8 -*-
"""Google Play review dataset for DNSE Entrade X and two peer broker apps.

Collection method
-----------------
Source: Google Play public review listing, retrieved 20-21 September 2026 through the
store's own batchexecute endpoint (rpcid UsvDTd), paginated with the continuation token
returned by each response. No authentication, no private data. Fields captured per
review: review id, author display name, star rating, free text, timestamp, thumbs-up count.

Apps pulled
  vn.com.encapital.arrow  DNSE Entrade X        868 reviews (full available history, 2020-2026)
  vn.com.vpbs.smartone    VPS SmartOne        1,200 reviews (pagination cap)
  com.fpts.eztrade        FPTS EzTrade          177 reviews (full available history)

Cleaning rule (identical for all three apps, applied to a normalised copy of the text:
NFKC, then NFD with combining marks stripped, then lower-cased. The NFKC step matters
because a large share of the loan spam disguises itself with mathematical-alphanumeric
Unicode letters such as VayTotNhat)

  loan_spam      /(vay\\s*9|vaytotnhat|vay\\s*t?o?t\\s*nhat|ktien|vayhangdau|vay333|
                   vayfe|fbvay|c0m|\\.com\\b|vay\\s*0\\s*%|vay\\s*von\\s*0)/i
  referral_spam  /(ma\\s*(gioi\\s*thieu|gt|moi|dai\\s*ly)|nhap\\s*ma|ref(erral)?\\s*id|
                   \\bma\\s*\\d{5,}|\\d{6}\\s*(nhan|ma))/i
  duplicate      identical alphanumeric-only normalised text, second and later copies
                 dropped, texts under 4 characters exempt
  generic        a kept review of four words or fewer carrying no theme match, for
                 example "tot", "hay", "ok". Counted separately, not removed.

Theme tags are non-exclusive keyword matches on the normalised Vietnamese text.
"""

# ---------------------------------------------------------------- headline counts
DNSE_TOTALS = {
    "raw_n": 868, "loan_spam": 127, "referral_spam": 72, "duplicates": 36,
    "clean_n": 633, "raw_mean": 3.287, "clean_mean": 3.161, "removed_mean": 3.626,
    "negative_1_2": 271, "neutral_3": 31, "positive_4_5": 331, "generic_in_clean": 110,
}

# rating, raw count, clean count
RATING_HIST = [
    (1, 331, 252), (2, 19, 19), (3, 31, 31), (4, 44, 37), (5, 443, 294),
]

# ---------------------------------------------------------------- by year
YEAR_HEADER = ["year", "raw_n", "raw_mean", "removed_n", "removed_pct", "clean_n",
               "clean_mean", "generic_n", "generic_pct", "substantive_n", "substantive_mean"]
YEAR_TAB = [
    ["2020",   3, 3.667,   0,  0.0,   3, 3.667,  0,  0.0,   3, 3.667],
    ["2021",  72, 2.306,  13, 18.1,  59, 1.983,  2,  3.4,  57, 1.877],
    ["2022", 207, 3.343, 101, 48.8, 106, 3.142, 19, 17.9,  87, 2.851],
    ["2023", 154, 3.019,  86, 55.8,  68, 2.574,  6,  8.8,  62, 2.403],
    ["2024", 202, 4.361,  27, 13.4, 175, 4.291, 54, 30.9, 121, 4.066],
    ["2025", 159, 2.660,   7,  4.4, 152, 2.632, 20, 13.2, 132, 2.364],
    ["2026",  71, 3.028,   1,  1.4,  70, 3.057,  9, 12.9,  61, 2.852],
]

# ---------------------------------------------------------------- themes
THEMES = ["onboarding", "stability", "money", "promo", "fees", "fraud",
          "closure", "yield", "influencer", "zalopay", "ui"]

THEME_LABEL = {
    "onboarding": "Account opening, eKYC, OTP, NFC identity capture",
    "stability":  "App crashes, freezes, login failures, slow order routing",
    "money":      "Deposits not credited, withdrawal delays, T+ settlement",
    "promo":      "Sign-up bonus terms, advertised rewards not received",
    "fees":       "Commission and charges differing from the advertised rate",
    "fraud":      "Explicit accusation of deception or fake reviews",
    "closure":    "Cannot close the account, closure fee",
    "yield":      "Idle-cash auto-earning feature (tai khoan khong ngu)",
    "influencer": "Reached the app through a YouTube or social referral",
    "zalopay":    "ZaloPay linkage and its transaction charge",
    "ui":         "Interface, charts, layout, usability",
}

# theme, negative(1-2), neutral(3), positive(4-5), all clean, share of negatives %
THEME_HEADER = ["theme", "neg_1_2", "neutral_3", "pos_4_5", "all_clean", "pct_of_negatives"]
THEME_TAB = [
    ["onboarding", 53, 4,  5,  62, 19.6],
    ["stability",  70, 5, 28, 103, 25.8],
    ["money",      14, 2,  7,  23,  5.2],
    ["promo",      26, 3,  6,  35,  9.6],
    ["fees",        4, 2,  5,  11,  1.5],
    ["fraud",      44, 2,  1,  47, 16.2],
    ["closure",     8, 0,  0,   8,  3.0],
    ["yield",       0, 0,  4,   4,  0.0],
    ["influencer",  5, 0, 10,  15,  1.8],
    ["zalopay",     2, 1,  2,   5,  0.7],
    ["ui",          3, 5, 25,  33,  1.1],
]

# negative reviews only, by year and theme
NEG_YEAR_HEADER = ["year", "negative_n"] + THEMES
NEG_YEAR = [
    ["2020",  1,  0,  0, 0,  0, 0,  0, 0, 0, 0, 0, 0],
    ["2021", 43, 17,  4, 1,  2, 0,  2, 0, 0, 1, 0, 0],
    ["2022", 42, 13,  8, 2,  4, 1,  5, 2, 0, 0, 0, 0],
    ["2023", 38,  2, 24, 0,  0, 0,  1, 0, 0, 0, 0, 0],
    ["2024", 25,  3,  6, 1,  2, 0,  6, 1, 0, 1, 0, 1],
    ["2025", 88, 14, 12, 7, 16, 3, 28, 4, 0, 3, 1, 1],
    ["2026", 34,  4, 16, 3,  2, 0,  2, 1, 0, 0, 1, 1],
]

# ---------------------------------------------------------------- peer comparison
PEER_HEADER = ["app", "package", "raw_n", "clean_n", "removed_pct", "raw_mean",
               "clean_mean", "n_2024", "mean_2024", "n_2025", "mean_2025",
               "n_2026", "mean_2026", "pct_1_star", "pct_5_star"]
PEERS = [
    ["DNSE Entrade X", "vn.com.encapital.arrow", 868,  633, 27.1, 3.287, 3.161,
     175, 4.291, 152, 2.632,  70, 3.057, 39.8, 46.4],
    ["VPS SmartOne",   "vn.com.vpbs.smartone",  1200, 1116,  7.0, 2.597, 2.515,
     320, 2.191, 247, 2.081, 113, 2.071, 53.3, 30.4],
    ["FPTS EzTrade",   "com.fpts.eztrade",       177,  169,  4.5, 2.181, 2.154,
       0,  None, 146, 1.979,  23, 3.261, 59.2, 20.1],
]

# ---------------------------------------------------------------- selected reviews
QUOTE_HEADER = ["review_id", "rating", "date", "thumbs_up", "themes", "text"]
QUOTES = [
 ["cf18775a",1,"2025-05-24",54,"onboarding|closure","Bị gài rồi, bạn nào muốn đăng kí thì phải biết 1 điều là k thể hủy đăng ký kể cả khi tài khoản chưa được duyệt cũng không hủy được, và cái đoạn chụp h"],
 ["e8fe4927",1,"2021-09-23",28,"onboarding","23.09.2021 đk lúc 10h sáng chờ tới gần 13h chưa vào đc mà cứ thông báo phải đợi 1h xác thực. app này có vấn đề chắc lun, đụng tới tiền bạc mà cứ lề mề"],
 ["5efad1d8",1,"2025-07-12",25,"onboarding","không quét dc nfc là sao. đăng kí mà khó thế."],
 ["e752ae28",1,"2025-05-31",22,"onboarding","có cái mã otp mà mãi dell gửi dc"],
 ["ec7cd283",1,"2025-04-17",20,"onboarding","đăng ký xác thực 5 lần ko đc cứ bảo vì hình chụp bị mờ"],
 ["91029c97",2,"2025-06-02",18,"stability|money","Khi nạp tiền không vào giờ giao dịch, dù tiền đã trừ ở tài khoản ngân hàng, nhưng tài khoản chứng khoán không nhận được. Liên hệ cả bộ phận CSKH thì p"],
 ["f95e155b",1,"2024-08-07",18,"stability","Từ ngày 6 đến nay chart, thông tin đều bị đơ mà không có bất kỳ thông báo nào. Cái duy nhất còn hiển thị là phần tin tức. Liên quan đến tiền mà Ad chơi"],
 ["d7b0e147",1,"2025-04-08",17,"onboarding|stability","mã otp bị lỗi"],
 ["4b62d195",1,"2021-08-22",16,"onboarding|stability","Điện thoại CMT nét như gì cứ bảo chùi camera, ko xác thực nổi đã thế còn lỗi liên tục, ko nên tải app này"],
 ["975c8060",1,"2025-07-25",15,"stability","lỗi đăng nhập ko vào được thì mất tiền 100%"],
 ["564355fd",1,"2025-06-28",50,"money|promo|fraud","lừa đảo thông tin sai sự thật không có vụ được 100k liền đâu phải nạp tiền vào tối thiểu 2tr mới được"],
 ["940c13ed",1,"2025-01-27",20,"money","Giam tiền nạp thì lẹ bán cổ phiếu ra tiền thì k cho rút muốn rút phải ứng tiền phí cực chát."],
 ["0a2388c6",1,"2025-08-20",9,"stability|money","cty khá ok chỉ có điều làm lâu lâu chuyển khoản vào mà hệ thống ngân hàng bị lỗi (chờ xử lý) khi ngân hàng xử lý xong tiền thì đã chuyển nhưng xử lý"],
 ["e74d3efa",1,"2024-08-25",7,"stability|money","Chán thật đi uống nước muốn rút tiền mà cứ lỗi"],
 ["811c5661",1,"2025-06-09",58,"promo|fraud","MN CHÚ Ý SCAM NHA KHÔNG NHẬN ĐƯỢC 100K MUỐN XOÁ TK PHẢI TRẢ NÓ 100K ĐỂ XOÁ NÓ LẤY CẮP THÔNG TIN AE CHÚ Ý"],
 ["0db61d25",1,"2025-06-07",43,"promo","mọi người đừng để bị dụ nhận 100k nha, kh dc đâu"],
 ["0318e923",1,"2025-08-06",32,"promo","quảng cáo sai sự thật. phải nạp vào trong app 2 triệu mới được 100k. không như quảng cáo là tải app được nhận 100k."],
 ["276fb209",1,"2025-06-07",26,"promo|fraud","scam không như quảng cáo"],
 ["f07f6887",1,"2025-06-24",24,"promo|fees","Phí giao dịch cao, không như quảng cáo. Đánh giá 1* vì sự mập mờ này"],
 ["e6b00c91",2,"2025-05-19",22,"fees","Thấy bảo miễn phí giao dịch mà vẫn mất phí đều đều hây"],
 ["92b7466a",1,"2022-09-05",1,"stability|fees","phí rẻ nhưng hay lỗi hệ thống cần nâng cấp lên cho bằng các cty khác."],
 ["ee1f33ca",1,"2025-03-24",0,"fees|fraud","Công ty lừa đảo. Ghi phí 0.045%, nhưng nó tính 0.5%"],
 ["d63fde57",1,"2025-04-18",50,"fraud","như lừa đảo z"],
 ["023d90b3",1,"2025-06-08",46,"fraud","app này MN nên cẩn thận nó lừa đó vì chọn đăng nhập thì kh thể hủy đc với lại lượt đánh giá toàn là đánh giá ảo nên đừng tin"],
 ["ba551fd3",1,"2025-06-25",42,"fraud","Lưu ý nha anh em LỪA ĐẢO ĂN THÔNG TIN KHÁCH HÀNG. ĐÁNH GIÁ 5 SAO ĐỀU LÀ GIẢ"],
 ["9d0f25ad",1,"2024-04-28",46,"closure","Tao muốn xóa hợp đồng vĩnh viễn"],
 ["2513906a",1,"2025-01-23",17,"promo|closure","Này thì đóng tài khoản mất phí 100k. Lần đầu tiên t nghe có 1 ctck đóng tài khoản mất 100k. Mà giữ tk để cập nhật thông tin thì không được. Chốt 1 sao"],
 ["bf576f62",1,"2025-10-14",10,"closure","ko bt dùng cũng ko cho xóa tài khoản tôi muốn xóa tài khoản"],
 ["0fa0a9f4",1,"2022-06-26",8,"closure","Làm sao để xóa tài khoản ạ"],
 ["6e881a12",1,"2025-05-18",17,"influencer","vì thấy qc app này qua green tuber nên tải và cho 1 sao nè"],
 ["b2970aa5",1,"2021-08-24",4,"influencer","Không nhận được tiền đâu, và mấy thằng youtube cũng luôn thổi phồng lên."],
 ["3217d538",1,"2025-04-04",3,"influencer","coi ytb quảng cáo hoài"],
 ["523d5f8f",1,"2025-04-30",0,"influencer","mấy app của Học Viện Bò và Gấu"],
 ["658a04b9",1,"2024-12-25",0,"promo|influencer","lừa đảo tải đường link của học viện bò và gấu rồi mà ko được tặng 200k"],
 ["db32d5d4",1,"2025-08-24",15,"zalopay","app có liên kết với zalopay để giao dịch, nhưng khi liên kết sẽ bị zalopay trừ 0,12% mỗi giao dịch mà liên kết này không thể gỡ được. điểm trừ quá lớn"],
 ["31147446",1,"2026-07-05",5,"stability|promo|fraud|zalopay","Nền tảng thiếu minh bạch, hoạt động chậm, trung gian, phát sinh nhiều loại chi phí."],
 ["d2094e6d",1,"2025-06-22",1,"onboarding|stability|fraud|ui","phần yêu cầu xác minh quá rắc rối. Xác minh 3 lần không lỗi chân dung thì lỗi cccd"],
 ["042dbd9d",1,"2026-07-29",0,"ui","app tệ. từ giao diện cho đến chức năng."],
 ["248db681",5,"2026-05-15",13,"stability|yield|influencer|ui","Ngoại trừ lâu lâu hay lỗi, thì thực ra tcx, vpx, ssi cũng lỗi bấy bá, thì thực sự app dnse là app ck tốt nhất ttck vn rồi. - phí thấp - tk không ngủ"],
 ["209c03a4",4,"2026-01-22",0,"yield","tôi đang dùng về tiền không ngủ và sinh lời tự động quá linh hoạt tuyệt vời"],
 ["fa30782f",5,"2025-11-27",0,"yield","App đặt lệnh dễ dàng nhanh chóng không phải dùng nhiều thao tác. Xem thông tin, tin tức rõ ràng, dễ nhìn"],
 ["4094bad4",5,"2025-05-04",31,"stability|ui","Giao diện đơn giản, thuận tiện, phí thấp"],
 ["06c66fa6",4,"2025-05-04",24,"","mong muốn che số dư, khối lượng như vps"],
 ["a018878c",5,"2024-11-13",24,"money|promo|influencer","mình đã quá chán nản khuyến nghị của các broker ít kinh nghiệm thì tìm thấy dnse, khuyến nghị của app khá ok với nhà đầu tư nhỏ lẻ, ít kinh nghiệm"],
 ["3098e894",5,"2025-05-08",20,"stability","ko bị lag như bên ssi iboard"],
 ["5529fbb6",5,"2025-07-09",19,"","Sao mãi chưa thấy tính năng gửi thông báo thế DNSE ơi? Có setting thông báo các kiểu nhưng không nhận được thông báo nào cả."],
 ["10f974fe",5,"2024-10-12",19,"","có rút được tiền ko mọi người"],
 ["d3a9f078",4,"2024-12-21",18,"stability","tiền bán cổ phiếu về chậm quá."],
 ["2683adda",5,"2023-09-01",18,"influencer","Anh chị bò và gấu là người giúp em nơi em có thể học hỏi về app cảm ơn nhiều"],
 ["1e200051",4,"2025-07-04",17,"stability|money|influencer|ui","ủng hộ kênh youtube Bò và Gấu nên cài đặt app và đầu tư. app khá tốt, mình mua bán cp chưa gặp trục trặc gì. có AI hỗ trợ (chỉ ở mức trung bình)"],
]

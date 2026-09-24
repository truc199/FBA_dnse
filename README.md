# FBA Season 6 Round 2 — DNSE Securities: data extraction and build code

Everything used to produce `FBAR2_2026_DNSE_Analysis.docx` and
`FBA_Round2_DNSE_data_pack.xlsx`. Run in numbered order; each step writes files the
next one reads.

## Environment

```bash
pip install -r requirements.txt      # or: uv sync
npm install docx
```

Python 3.9+ (the project's own uv environment pins 3.14) and Node 16+. LibreOffice
is needed only for the final recalculation step; `recalc.py` finds `soffice` on the
PATH or in the default install folder.

## Run order

| Step | File | What it does | Writes |
|---|---|---|---|
| 1 | `01_findex_fetch.py` | Pulls the whole Global Findex record for Vietnam from the World Bank API and checks every value in `findex_data.py` against it | `findex_raw.json` |
| 1b | `01b_dnse_financials_fetch.py` | Pulls DNSE's full financial statements (income statement, balance sheet, cash flow, notes; every quarter since 2018) from Vietcap's data service and checks the figures typed into `07` against them | `dnse_financials_raw.json`, `dnse_financials_quarterly.csv`, `dnse_financials_annual.csv`, `dnse_financials.json` |
| 2a | `02a_playstore_scrape_browser.js` | Google Play review collector, pasted into the browser console | CSV via clipboard |
| 2b | `02b_playstore_scrape_python.py` | The same collector as a standalone script | `reviews_raw_<package>.csv` |
| 2c | `02c_appstore_scrape.py` | Written reviews of the same apps from the Vietnamese App Store, plus Apple's star-rating counts; merges with earlier runs | `reviews_raw_ios_<package>.csv`, `appstore_meta.json` |
| 3 | `03_reviews_clean.py` | Normalises, flags spam, drops copy-paste duplicates, tags themes, aggregates one app | `reviews_flagged_*.csv`, `reviews_summary_*.json` |
| 3b | `03b_reviews_tables.py` | Runs the step 3 rules over the three pulls (VPS cut to its 1,200 most recent) and writes the review data module | `reviews.py`, `reviews_tables.json`, `reviews_flagged_*.csv` for exactly the rows used |
| 4 | `04_segment_model.py` | Builds the two Findex indices and ranks the segments | `segment_model.json` |
| 5a | `05a_charts_financial.py` | Figures 2, 7, 8, 9, 11 | `fig/*.png` |
| 5b | `05b_charts_evidence.py` | Figures 1, 3, 4, 5, 6, 10 | `fig/*.png` |
| 5c | `05c_charts_bctc.py` | Ten long-run charts of the filed statements, 2018 to Q2 2026, and a check of press figures against them; findings in `bctc_analysis.md` | `fig/bctc/*.png` |
| 6 | `06_build_report.js` | Builds the Word report and prints the main-body word count | `FBAR2_2026_DNSE_Analysis.docx` |
| 7 | `07_build_workbook.py` | Builds the 14-tab workbook | `FBA_Round2_DNSE_data_pack.xlsx` |

```bash
python3 01_findex_fetch.py                 # optional, findex_data.py is already here
python3 01b_dnse_financials_fetch.py
python3 02b_playstore_scrape_python.py
python3 02c_appstore_scrape.py             # about 4 minutes; run twice to fill gaps
python3 03_reviews_clean.py --selftest
python3 03_reviews_clean.py reviews_raw_vn.com.encapital.arrow.csv   # per-app audit files
python3 03b_reviews_tables.py
python3 04_segment_model.py
python3 05a_charts_financial.py && python3 05b_charts_evidence.py
node 06_build_report.js
python3 07_build_workbook.py
python3 recalc.py FBA_Round2_DNSE_data_pack.xlsx     # caches formula values
```

`06` reads `reviews_tables.json`, `segment_model.json` and `dnse_financials.json`, so
every review, segment and DNSE financial number in the report comes from the pipeline
rather than being typed into the prose; `brokers.py`, `05a` and `07` read the same
financials file. If the top three segments ever change, `06` stops with an error, because
Sections 4.2 and 6 name that group in words.

## Network note

Both pulls run from an ordinary home connection (checked 23 September 2026). They
fail from some cloud containers: `api.worldbank.org` can be refused by an egress
proxy, and Google Play returns an empty result set to datacentre IP ranges. In that
case use `02a` in a browser, and keep the `findex_data.py` already in this folder.

## The App Store cross-check

Google Play covers Android users only. `02c` pulls written reviews of the same three
apps from the Vietnamese App Store through Apple's public feed, and `03b` cleans them
with the same rule. The feed serves at most 500 recent and 500 most helpful reviews
per app and drops pages at random, so `02c` retries every page, fetches both orders,
and merges each run into the CSV already on disk. It has no full history, so the App
Store is used as a cross-check over 2025 and 2026, the years all six series cover,
not as a second time series. Results sit in Appendix A6 of the report and at the
bottom of the workbook's `Review analysis` tab. App Store referral spam writes its
codes in capitals and digits (MFBCFA, G25PRK), which is why the referral rule in `03`
recognises those as well as six-digit codes.

## What is exact and what is a reconstruction

Be able to answer this if a judge asks.

**The published cleaning log is reproducible.** Re-pulling on 23 September 2026 and
running the pre-revision rules (kept in `_backup_original_2026-09-23/`) gives 127 loan
spam, 36 duplicates, 633 retained and a clean mean of 3.161 for DNSE; 1,116 and 2.515
for VPS's 1,200 most recent reviews; 169 and 2.154 for FPTS. Referral spam is 71
rather than 72 because one 2026 referral post has since been deleted from Google Play.

**The rules were then revised** after a code audit (`doc/code_audit.md`, items A1 to
A6). The referral rule caught genuine complaints about one-time passwords ("nhập mã
OTP") and ordinary phrases such as "mà mọi người"; the duplicate rule removed identical
short reviews written by different people; several theme keywords matched unrelated
words once tone marks were stripped (lỗi/lời/lợi, lừa/lựa, sập/sắp, thưởng/thường).
Every figure now in `reviews.py` comes from the revised rules, which `03 --selftest`
checks against each of those cases. The generic flag is one word, which is the rule
the published figures used; the old code and text said four words.

**Theme keywords remain a reconstruction.** The lists used for the first draft were
built interactively and not saved. The current lists put the complaint themes in the
same rank order.

**DNSE's statements are pulled, not typed.** `01b` takes every line of the filings as
Vietcap maps them onto the securities-company template, so brokerage, lending and
proprietary revenue each come with their own direct cost. The half-year figures match
the KPMG-reviewed statements of 14 August 2026 (on `ir.dnse.com.vn`) to the dong:
pre-tax profit 111.6 billion, against the 113.1 of the quarterly statement of 20 July,
so Q2 2026 is 97.4 rather than the 98.9 the press reported. The same pull corrected
2025 revenue (1,457.9, not 1,467) and investment income, which the earlier pack took
from trading gains for 2025 and from held-to-maturity interest for 2026.

Three cautions. Template line 24 (`iss168`) reports loan-loss provisions and the
borrowing cost of the loan book as one figure; the allowance on the balance sheet
moves by a few billion a quarter while the line runs at 70 to 130 billion, so most of
it is funding cost, and funding cost in the pack is estimated by removing the change
in the allowance. Investors' securities off the balance sheet (`nos379`) are at par
value, as note 26 of the statements says, so they understate market value and cannot
be set against the annual report's 52,000 billion. And the press figure of 405 per
cent growth in proprietary provisions for Q1 2026 is not reproduced by any line of
the filings, so it was dropped.

**Hand-entered, with sources.** `brokers.py` holds the exchange market-share tables,
industry lending balances and quarterly profits; its DNSE rows are read from
`dnse_financials.json`. These come from HOSE and HNX
announcements and from published financial statements; each block names its source.
They are typed in rather than scraped, so check them against the source before citing.
The FTSE constituent count is marked unverified there.

## Data files

| File | Contents |
|---|---|
| `findex_data.py` | `SEGMENTS`, `SEG2024` (51 indicators × 13 segments), `NATIONAL2024`, `TRENDS`; labels and themes hand-written, values checked by step 1 |
| `reviews.py` | Generated by step 3b: cleaning log, ratings by year, generic-flag sensitivity, theme table, three-app comparison, 50 selected quotes |
| `brokers.py` | HOSE, HNX and derivatives market share; lending balances; Q2 2026 profits; market totals |
| `dnse_financials.json` | Step 1b output: DNSE key lines by quarter, half year and year, with derived ratios and their definitions |
| `dnse_financials_quarterly.csv`, `dnse_financials_annual.csv` | Step 1b output: every line of the filed statements |
| `segment_model.json` | Step 4 output read by the report |
| `reviews_tables.json` | Step 3b output read by the report |
| `reviews_raw_ios_*.csv`, `appstore_meta.json` | Step 2c output: App Store written reviews and star-rating counts |

## Method, in one paragraph each

**Review cleaning.** Fold the text with NFKC, then NFD with combining marks stripped,
then map the stroked d, then lower case. Flag loan advertising by lending-site brands
and their obfuscations. Flag referral farming only where a referral phrase sits next to
a six-digit or letter code or a reward amount. Drop copy-paste duplicates: the same text
of 20 or more characters, keeping the earliest copy. Flag, but keep, any retained review
of a single word carrying no theme, so a year of one-word praise cannot be read as
satisfaction. That flag exposes the 2024 rating peak: a third of that year's retained
reviews were generic against about one in eight in 2025, and the substantive mean fell
by about 1.8 stars. The fall holds under a four-word rule too.

**Segment model.** Index A averages six Findex indicators covering investable surplus
held formally. Index B averages six covering digital transacting habit. Both are
unweighted, because any weighting chosen after seeing the data would be fitted to the
conclusion. They average different indicators, so compare segments within an index,
not A against B. The activation gap is account ownership minus saving at a financial
institution. Segment population shares are recovered from the survey itself: each
pair of segments splits all adults, so the national figure is a weighted average of
the two halves. Priority rank is the composite index times the unconverted pool,
computed before rounding. On the workbook's `Segment model` tab every index is a live
formula reading from `Segments 2024`, so the model can be audited cell by cell.

**Market share.** Each exchange defines share as a proportion of traded value on
that exchange alone. Shares from different exchanges are never compared with one
another anywhere in the report. An earlier draft did make that comparison and it
overstated the central finding, which is why every figure now carries the name of
its market.

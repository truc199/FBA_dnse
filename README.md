# DNSE Securities: from accounts to assets

Replication package for the Round 2 business analytics report of **Future Business Analyst Season 6** (RMIT BFC Hanoi), written by **Team KTQT FTUers** on DNSE Securities Joint Stock Company (HOSE: DSE).

The report finds that DNSE opens accounts at scale but few of them are funded: in December 2025, 1.8 per cent of its 1.51 million accounts held VND 10 million or more. It recommends *Payday Portfolio*, a goal-based plan that moves part of each salary into a diversified portfolio on payday, and organises DNSE's wider technology around customer balances.

This repository holds the final report, the data behind it and the code that produces every chart, every data-driven table and the Word document itself.

## Repository structure

```
dnse-fba-round2/
├── README.md
├── requirements.txt
├── run_all.py                    runs the whole pipeline with one command
├── report/                       the final report, as submitted
│   ├── FBAR2_2026_KTQT_FTUers.pdf
│   └── FBAR2_2026_KTQT_FTUers.docx
├── data/                         every input, as used for the report
│   ├── manual/                   hand-collected figures, one CSV per source table (9 files)
│   ├── findex_raw.json           World Bank Global Findex, Vietnam, complete API response
│   ├── dnse_financials*.{json,csv}    DNSE financial statements, every quarter and year
│   ├── peer_financials.json      the same lines for every listed securities company
│   ├── market_macro.json         index prices, exchange market shares, VSDC accounts, macro series
│   ├── reviews_raw_*.csv         Google Play and App Store reviews of DNSE, VPS and FPTS (6 files)
│   ├── appstore_meta.json        App Store star-rating counts
│   ├── reviews_flagged_*.csv     the same reviews with spam flags and complaint themes (6 files)
│   ├── reviews_summary_*.json    summary of each Google Play pull (3 files)
│   ├── reviews_tables.json       review tables used in the report (also as reviews.py)
│   └── segment_model.json        Findex segment indices
├── src/
│   ├── config.py                 paths and the DNSE colour palette
│   ├── analysis.py               calculations shared by the figures and tables
│   ├── pipeline/                 data collection and preparation, steps 01 to 04
│   ├── figures/                  charts (charts.py), diagrams (diagrams.py), style and printed sizes
│   ├── tables/                   table export, recomputation and check
│   └── report/                   report text, Word template, title page and build script
└── outputs/
    ├── figures/                  the 24 figures of the report (PNG)
    ├── tables/                   the 24 tables of the report (CSV), index.csv, check_tables.md
    │   └── computed/             13 tables recomputed from data/
    └── report/                   the report rebuilt by the code (created by run_all.py, not tracked)
```

## Quick start

Python 3.10 or later is needed (tested with 3.11).

```bash
git clone <repository URL>
cd dnse-fba-round2
python -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python run_all.py
```

The run takes about 20 seconds and writes the figures, the tables and a rebuilt copy of the report into `outputs/`. The Word file is always rebuilt. A PDF is also produced when [LibreOffice](https://www.libreoffice.org/) is installed; otherwise open the Word file and save it as PDF.

Figures use Calibri or, where Calibri is missing, the metrically identical Carlito font. On a machine with neither, matplotlib falls back to another font and label positions can shift slightly.

## What `run_all.py` does

| Stage | Script | Reads | Writes |
|---|---|---|---|
| 1. Reviews | `src/pipeline/03_reviews_clean.py` (self-test, then each Google Play pull) | `reviews_raw_*.csv` | `reviews_flagged_*.csv`, `reviews_summary_*.json` |
| | `src/pipeline/03b_reviews_tables.py` | raw reviews, `appstore_meta.json` | `reviews_tables.json`, `reviews.py`, `reviews_flagged_*.csv` |
| 2. Segments | `src/pipeline/04_segment_model.py` | `findex_data.py` | `segment_model.json` |
| 3. Figures | `src/figures/make_figures.py` | `data/` | `outputs/figures/*.png` |
| 4. Tables | `src/tables/export_tables.py` | `report/FBAR2_2026_KTQT_FTUers.docx` | `outputs/tables/*.csv`, `index.csv` |
| | `src/tables/make_tables.py` | `data/` | `outputs/tables/computed/*.csv` |
| | `src/tables/check_tables.py` | both sets of tables | `outputs/tables/check_tables.md` |
| 5. Report | `src/report/build_report.py` | template, `content.py`, figures | `outputs/report/FBAR2_2026_KTQT_FTUers_rebuilt.docx` (and `.pdf`) |

Options: `--no-report` stops after the tables, `--paginate` recomputes the page numbers in the contents lists with LibreOffice, and `--fetch` downloads the data again first (see [Refreshing the data](#refreshing-the-data)).

Every script can also be run on its own from the repository root, for example `python src/figures/make_figures.py` or `python src/pipeline/03_reviews_clean.py --selftest`. Re-running the pipeline on the data in this repository reproduces every file in `data/` and `outputs/tables/` byte for byte. On the same platform, fonts and package versions (see [Requirements](#requirements)) the figures are reproduced byte for byte too; other versions or fonts render text slightly differently but draw the same numbers.

## Data

### Downloaded data

| File | Content | Source | Retrieved |
|---|---|---|---|
| `findex_raw.json` | All Global Findex series for Vietnam, every wave and demographic segment (19,878 observations) | World Bank API, source 28 | database updated 6 October 2025 |
| `dnse_financials_raw.json`, `dnse_financials_quarterly.csv`, `dnse_financials_annual.csv`, `dnse_financials.json` | DNSE income statement, balance sheet, cash flow and notes, 2018 to Q2 2026, and the key lines used in the report | Vietcap IQ financial-statement service | 24 September 2026 |
| `peer_financials.json` | The same key lines for every securities company covered by Vietcap, with industry totals | Vietcap IQ | 25 September 2026 |
| `market_macro.json` | Index and futures prices, HOSE and HNX brokerage market shares, VSDC account counts, World Bank WDI series and 2026 releases of the National Statistics Office | Vietcap price service, HOSE, HNX, VSDC, World Bank, National Statistics Office | 25 September 2026 |
| `reviews_raw_<app>.csv` | Google Play reviews of DNSE Entrade X, VPS SmartOne and FPTS EzTrade | Google Play | 23 September 2026 |
| `reviews_raw_ios_<app>.csv`, `appstore_meta.json` | App Store reviews of the same apps (Vietnam storefront) and star-rating counts | Apple customer-review feed and lookup API | 24 September 2026 |

`src/pipeline/findex_data.py` holds the 51 Findex indicators used in the report, and `01_findex_fetch.py` checks each of them against a fresh API pull. `src/pipeline/brokers.py` assembles the second-quarter 2026 industry cross-section (exchange market shares, lending and profit) from `market_macro.json` and the filings.

### Hand-collected inputs (`data/manual/`)

Figures that come from company announcements, press reports or the authors' assumptions are kept in small CSV files, each with a `source` column where it applies.

| File | Content | Used in |
|---|---|---|
| `dnse_accounts.csv` | DNSE account counts, active customers, balances and product users | Figures 3, 7 and 11; Table B3 |
| `idle_cash_rates.csv` | Returns on idle cash at DNSE, TCBS and banks, and inflation | Figure 1 |
| `industry_investor_cash.csv` | Industry investor cash by quarter | Figure 2 |
| `market_position.csv` | DNSE's share of eight markets, with the labels of Table C1 | Figure 4; Table C1 |
| `peer_accounts.csv` | Customer accounts and parent bank of each peer | Figure C1; Table C2 |
| `press_figures.csv` | Press figures reconciled with the filings | Table A2 |
| `scenario_assumptions.csv`, `scenario_baseline.csv` | Assumptions of the three Payday Portfolio scenarios | Table F5; Figure F1 |
| `validation_roadmap.csv` | Tasks and months of the Round 3 validation plan | Figure F2 |

### Privacy

The reviews are public app-store content. Reviewer display names have been replaced by pseudonymous identifiers (`u_` followed by twelve characters of a SHA-256 hash), which keeps different reviews by the same person linkable for the duplicate check, and one telephone number written in a review has been masked. Review texts are kept so that the spam rules and theme coding can be audited.

### Refreshing the data

`python run_all.py --fetch` downloads everything again before the analysis. The sources change over time (new quarters, restated figures, new reviews), so the figures and tables will then no longer match the report, and `check_tables.py` will list the differences. Two collectors need care:

* Google Play returns nothing to some data-centre IP ranges. Run `02b_playstore_scrape_python.py` from an ordinary internet connection, or use the browser-console version `02a_playstore_scrape_browser.js`, which is the method used for the report.
* Apple's review feed serves a different subset on each request. `02c_appstore_scrape.py` merges repeated runs by review id; `--fresh` starts again from nothing.

## Figures

Each figure is drawn by one function and saved at the size it has in the report.

| Figure | File | Function |
|---|---|---|
| 1 | `fig01_idle_cash_returns.png` | `charts.fig01_idle_cash_returns` |
| 2 | `fig02_investor_cash_index.png` | `charts.fig02_investor_cash_index` |
| 3 | `fig03_funding_funnel.png` | `charts.fig03_funding_funnel` |
| 4 | `fig04_market_position.png` | `charts.fig04_market_position` |
| 5 | `fig05_brokerage_vs_cost.png` | `charts.fig05_brokerage_vs_cost` |
| 6 | `fig06_funding_structure.png` | `charts.fig06_funding_structure` |
| 7 | `fig07_platform_cost.png` | `charts.fig07_platform_cost` |
| 8 | `fig08_complaint_themes.png` | `charts.fig08_complaint_themes` |
| 9 | `fig09_findex_segments.png` | `charts.fig09_findex_segments` |
| 10 | `fig10_root_cause.png` | `diagrams.fig10_root_cause` |
| 11 | `fig11_growth_index.png` | `charts.fig11_growth_index` |
| 12 | `fig12_payday_flow.png` | `diagrams.fig12_payday_flow` |
| 13 | `fig13_contribution_threshold.png` | `charts.fig13_contribution_threshold` |
| 14 | `fig14_ecosystem.png` | `diagrams.fig14_ecosystem` |
| B1 to B4 | `figB1_revenue_profit.png`, `figB2_revenue_allocation.png`, `figB3_yields_funding.png`, `figB4_asset_composition.png` | `charts.figB1_*` to `charts.figB4_*` |
| C1 | `figC1_peer_per_account.png` | `charts.figC1_peer_per_account` |
| D1, D2 | `figD1_rating_by_year.png`, `figD2_store_ratings.png` | `charts.figD1_*`, `charts.figD2_*` |
| E1 | `figE1_findex_behaviour.png` | `charts.figE1_findex_behaviour` |
| F1, F2 | `figF1_scenarios.png`, `figF2_roadmap.png` | `charts.figF1_*`, `charts.figF2_*` |

The DNSE red palette is defined once in `src/config.py`, and the printed size of every figure in `src/figures/style.py`.

## Tables

`outputs/tables/` holds all 24 tables of the final report as CSV files, exported from the Word document, and `index.csv` lists each table with its caption and source note. Thirteen of them are computed from data, and `make_tables.py` rebuilds these from `data/` with the same layout, labels and number format under the same file names in `outputs/tables/computed/`:

* A2 (filings column), A3 and A4: data preparation and review cleaning
* B1, B2 and B3: DNSE financial statements, ratios and the platform cost proxy
* C1 and C2: market position and peers
* D1 and D2: complaint themes and the three-broker comparison
* E1 and E2: Findex segments and their ranks
* F5: Payday Portfolio scenarios

The remaining eleven tables (1, A1, C3, D3, E3, F1 to F4, F6 and G1) are written by the authors: evidence lists, design tables, translated quotations and the assessment of proposals.

`check_tables.py` compares the two sets cell by cell and writes `outputs/tables/check_tables.md`. Of 614 cells, 611 are identical; the three known differences are listed below.

## Differences from the submitted report

The rebuilt report (`outputs/report/`) has the same text, tables and page layout as the submitted one. Its figures are drawn by this code from the same data and at the same size, so they look almost identical but are not pixel copies. Five figure labels and three table cells differ from the submitted PDF by rounding or labelling. In each case the code output agrees with the filings and with the other tables of the report.

| Where | Submitted report | Code output | Reason |
|---|---|---|---|
| Figure 4, new accounts, 2025 | 20.0 | 20.1 | 518,514 of 2,573,945 new accounts is 20.14 per cent, as in Table C1 |
| Figure 5, legend | Direct brokerage and custody cost | Direct brokerage cost | The series is the brokerage cost line of Table B1. Adding custody costs would raise the 16-quarter shortfall from VND 190 billion to VND 224 billion |
| Figure B1, 2023 operating revenue | 714 | 715 | VND 714.51 billion (714.5 in Table B1) |
| Figure B2, 2025 funding cost and provisions | 30 | 29 | 429.8 / 1,457.9 = 29.5 per cent (Table B1) |
| Figure B4, 2022 margin loans | 36 | 35 | Loans net of the loss allowance are 35.0 per cent of total assets |
| Table B1, interest expense plus line 24, 2021 | 23.9 | 24.0 | VND 23.958 billion in the filings |
| Table B1, interest expense plus line 24, 2022 | 172.2 | 172.3 | VND 172.252 billion in the filings |
| Table B2, deposits and bonds held to maturity, 2022 | 2,824 | 2,823 | VND 2,823.49 billion in the filings |

None of these numbers is quoted in the text of the report.

## How the report is built

`src/report/build_report.py` assembles the Word document from three inputs:

* `src/report/template/base_report.docx`, the team's earlier draft, which supplies the styles, the appendices and the reference list;
* `src/report/content.py`, the executive summary and Sections 1 to 5 of the final report (3,476 words);
* the figures in `outputs/figures/`.

It replaces the main body, rebuilds the contents lists, applies the appendix changes of the final version, inserts the figures at their printed size, drops references that are no longer cited and builds the title page (`title_page.py`, background image in `src/report/assets/`). Page numbers for the contents lists are read from `src/report/pages.json`; `--paginate` recomputes them with LibreOffice.

## Methods in brief

Definitions follow Appendix A of the report.

* **Funding cost** is interest expense plus template line 24, less the rise in the allowance for loan losses. The cost of funds annualises it over average borrowings and bonds, and the net interest margin deducts it from interest on loans, deposits and bonds held to maturity.
* **Core pre-tax profit** excludes the net result on financial assets at fair value through profit or loss.
* **Platform cost proxy** is staff costs and outsourced services from the note on administrative expenses, plus depreciation and amortisation from the cash flow statement.
* **Review cleaning** normalises the text (Unicode compatibility form, no diacritics, lower case), removes loan advertising, referral farming and copy-paste duplicates, flags one-word reviews as generic and tags complaint themes with whole-word keyword rules. `03_reviews_clean.py --selftest` runs 37 test cases.
* **Segment ranking** min-max normalises six Findex criteria across twelve segments and ranks them under four weighting schemes (`analysis.segment_ranks`).
* **Scenarios** multiply savers, monthly contribution, the share of contributions kept and 18 months. Fees apply a fee yield to the assets, and tier interest is an upper bound (`analysis.scenarios`).

## Requirements

* Python 3.10 or later with the packages in `requirements.txt` (matplotlib, numpy, pillow, python-docx, lxml, pypdf; google-play-scraper only for `--fetch`)
* LibreOffice, optional, for the PDF and for `--paginate`
* Calibri or Carlito, optional, for figures identical to the report

The committed outputs were produced on Linux with Python 3.11.15, matplotlib 3.10.9, numpy 2.4.4, pillow 12.2.0, python-docx 1.2.0, lxml 6.1.0, pypdf 3.17.4 and LibreOffice for the PDF. A clean install of `requirements.txt` in a new virtual environment (matplotlib 3.11.2) gives identical data and tables.

## Credits

Team KTQT FTUers, Future Business Analyst Season 6, Round 2, 27 September 2026.

The data remain subject to the terms of their sources: the World Bank (Global Findex and World Development Indicators), Vietcap Securities, the Ho Chi Minh City and Hanoi stock exchanges, VSDC, the National Statistics Office, Google Play and the Apple App Store. The title-page background image in `src/report/assets/` was supplied by the team for the report.

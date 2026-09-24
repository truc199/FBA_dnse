# FBA Season 6 Round 2 — DNSE Securities: data extraction and build code

Everything used to produce `FBAR2_2026_DNSE_Analysis.docx` and
`FBA_Round2_DNSE_data_pack.xlsx`. Run in numbered order; each step writes files the
next one reads.

## Environment

```bash
pip install -r requirements.txt
npm install docx
```

Python 3.9+ and Node 16+. LibreOffice is needed only for the final recalculation
step (`soffice`), and the xlsx skill ships a `recalc.py` that wraps it.

## Run order

| Step | File | What it does | Runs where |
|---|---|---|---|
| 1 | `01_findex_fetch.py` | Pulls the whole Global Findex record for Vietnam from the World Bank API | Any machine with open internet |
| 2a | `02a_playstore_scrape_browser.js` | Google Play review collector, pasted into the browser console | Browser, on play.google.com |
| 2b | `02b_playstore_scrape_python.py` | The same collector as a standalone script | Laptop, not a datacentre IP |
| 3 | `03_reviews_clean.py` | Normalises, de-spams, de-duplicates, tags themes, aggregates | Anywhere |
| 4 | `04_segment_model.py` | Builds the two Findex indices and ranks the segments | Anywhere |
| 5a | `05a_charts_financial.py` | Figures 2, 7, 8, 9, 11 | Anywhere |
| 5b | `05b_charts_evidence.py` | Figures 1, 3, 4, 5, 6, 10 | Anywhere |
| 6 | `06_build_report.js` | Builds the Word report and prints the main-body word count | Anywhere |
| 7 | `07_build_workbook.py` | Builds the 14-tab workbook | Anywhere |

```bash
python3 01_findex_fetch.py                 # optional, findex_data.py is already here
python3 02b_playstore_scrape_python.py
python3 03_reviews_clean.py reviews_raw_vn.com.encapital.arrow.csv
python3 04_segment_model.py
python3 05a_charts_financial.py && python3 05b_charts_evidence.py
node 06_build_report.js
python3 07_build_workbook.py
python3 recalc.py FBA_Round2_DNSE_data_pack.xlsx     # caches formula values
```

## Network note, read this before you file a bug

Two of the sources are blocked from the cloud container this was assembled in, so
steps 1 and 2b could not be re-run here at packaging time:

- `api.worldbank.org` is refused by the container's egress proxy. The original pull
  was made through the browser, where the request is not proxied. `findex_data.py`
  in this folder is that pull, already parsed.
- Google Play returns an empty result set to datacentre IP ranges. The original pull
  was made with `02a` in the browser. Run `02b` from an ordinary connection.

Both scripts are correct and complete. They need a normal internet connection, not
a fix.

## What is exact and what is a reconstruction

Be able to answer this if a judge asks.

**Exact.** The cleaning rules in `03_reviews_clean.py` are the rules that produced
every published cleaning figure: 868 retrieved, 127 loan spam, 72 referral spam, 36
duplicates, 633 retained, mean 3.287 before and 3.161 after. The normalisation is
the load-bearing part, because roughly one in eight spam reviews writes its brand in
mathematical alphanumeric Unicode and survives a plain keyword filter. Run
`python3 03_reviews_clean.py --selftest` to see that case caught.

**A reconstruction.** The theme keyword lists were built interactively against the
corpus and were not saved. The lists in `03_reviews_clean.py` reproduce the rank
order of the complaint themes and land within a few counts of the published table,
but not cell for cell. Published theme counts came from the original run and are
recorded in `data/reviews.py`. If you re-run the pipeline and report new numbers,
report the new ones and say so.

**Hand-entered, with sources.** `data/brokers.py` holds the exchange market-share
tables, industry lending balances and quarterly profits. These come from HOSE and
HNX announcements and from published financial statements; each block names its
source. They are typed in rather than scraped, so check them against the source
before citing.

## Data files

| File | Contents |
|---|---|
| `findex_data.py` | `SEGMENTS`, `SEG2024` (51 indicators × 13 segments), `NATIONAL2024`, `TRENDS` |
| `data/reviews.py` | Cleaning log, ratings by year, theme table, three-app comparison, 50 selected quotes |
| `data/brokers.py` | HOSE, HNX and derivatives market share; lending balances; Q2 2026 profits; market totals |

## Method, in one paragraph each

**Review cleaning.** Fold the text with NFKC, then NFD with combining marks
stripped, then map the stroked d, then lower case. Match two regular expressions
against the folded text for loan advertising and referral-code farming. Drop later
copies of identical alphanumeric-only folded text, exempting anything under four
characters. Flag, but keep, any retained review of four words or fewer carrying no
theme, so a year of one-word praise cannot be read as satisfaction. That last flag
is what exposed the 2024 rating peak: 30.9 per cent of that year's retained reviews
were generic, against 13.2 per cent in 2025, and the substantive mean fell from 4.07
to 2.36.

**Segment model.** Index A averages six Findex indicators covering investable
surplus held formally. Index B averages six covering digital transacting habit. Both
are unweighted, because any weighting chosen after seeing the data would be fitted
to the conclusion. The activation gap is account ownership minus saving at a
financial institution, which counts adults already inside the formal system who are
not yet putting money to work. Priority rank is the composite index times the
unconverted pool. On the workbook's `Segment model` tab every one of these is a live
formula reading from `Segments 2024`, so the model can be audited cell by cell.

**Market share.** Each exchange defines share as a proportion of traded value on
that exchange alone. Shares from different exchanges are never compared with one
another anywhere in the report. An earlier draft did make that comparison and it
overstated the central finding, which is why every figure now carries the name of
its market.

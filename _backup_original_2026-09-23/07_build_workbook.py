import os, sys
_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path[:0] = [_HERE, os.path.join(_HERE, 'data')]
from findex_data import SEGMENTS, SEG2024, NATIONAL2024, TRENDS

from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

NAVY = "1F3864"
ACCENT = "2E74B5"
LIGHT = "EDF2F8"
WARM = "FBF0E4"

F = "Arial"
H = Font(name=F, size=10, bold=True, color="FFFFFF")
B = Font(name=F, size=10, bold=True)
N = Font(name=F, size=10)
SM = Font(name=F, size=9, color="595959")
TITLE = Font(name=F, size=14, bold=True, color=NAVY)
SUB = Font(name=F, size=10, color="595959")

hdr_fill = PatternFill("solid", fgColor=NAVY)
alt_fill = PatternFill("solid", fgColor=LIGHT)
warm_fill = PatternFill("solid", fgColor=WARM)
thin = Side(style="thin", color="CFDAE8")
box = Border(left=thin, right=thin, top=thin, bottom=thin)

wb = Workbook()

# ---------------------------------------------------------------- README
ws = wb.active
ws.title = "Read me"
ws.sheet_view.showGridLines = False
ws.column_dimensions['A'].width = 3
ws.column_dimensions['B'].width = 30
ws.column_dimensions['C'].width = 95

r = 2
ws.cell(r, 2, "FBA Season 6 Round 2 consolidated data pack: DNSE Securities").font = TITLE
r += 1
ws.cell(r, 2, "Every dataset behind the DNSE report, in one file. Compiled 20 to 21 September 2026.").font = SUB
r += 2

rows = [
 ("What this is",
  "Five datasets in one workbook. DNSE company financials and market position, the Vietnamese securities industry cross-section, 868 cleaned Google Play reviews of DNSE and two competitors, the complete Global Findex record for Vietnam, and a macro reference sheet. Every computed cell is a formula, so editing an input updates everything downstream."),
 ("Where the data came from",
  "Company data from DNSE quarterly financial statements and investor relations releases. Market share from the HOSE and HNX quarterly announcements of 7 July 2026. Industry lending and profit from Q2 2026 financial statements as compiled by Vietstock and Mekong Asean. Findex from the World Bank Open Data API, source 28, country VNM, endpoint api.worldbank.org/v2/sources/28/country/VNM/series/all/data?format=json, which returned 19,878 observations of which 3,022 are non-null. Reviews from the public Google Play listings for vn.com.encapital.arrow, vn.com.vpbs.smartone and com.fpts.eztrade."),
 ("How to read the colours",
  "Blue figures are inputs taken directly from a source. Green figures are links to another sheet. Black figures are formulas computed in this workbook. Yellow fill marks an assumption you may want to change. Editing a blue or yellow cell updates every black cell that depends on it."),
 ("The review data",
  "868 DNSE reviews, 1,200 VPS and 177 FPTS, collected 20 to 21 September 2026. The cleaning rule is written out in full on the 'Review analysis' sheet and was applied identically to all three applications, so the comparison is like for like. 235 DNSE reviews were removed as loan advertising, referral farming or duplicates."),
 ("Survey waves covered",
  "2011, 2014, 2017, 2022 and 2024. Note the labelling: the round usually called Global Findex 2021 is filed under 2022 for Vietnam in the World Bank API, and Vietnam's 2021 slot is empty. This workbook uses the API's own year labels. The 2024 wave was published in the Global Findex 2025 release; fieldwork ran May to December 2024."),
 ("Sample",
  "1,000 Vietnamese adults aged 15 and over, 199 variables in the underlying microdata file. All figures here are weighted population estimates, expressed as a percentage of adults aged 15+ unless the label says otherwise."),
 ("The microdata",
  "This workbook holds published aggregates. The respondent-level file (1,000 rows, 199 columns) is a separate free download at microdata.worldbank.org/index.php/catalog/7998, reference VNM_2024_FINDEX_v02_M. Download that too if you want to do your own cross-tabulations."),
 ("Why the segments matter",
  "Findex publishes every indicator broken down twelve ways: by sex, age band, education, income quintile group, urban or rural, and labour force status. That is a ready-made market segmentation. The 'Segments 2024' sheet is the core table."),
 ("A caution on precision",
  "1,000 respondents split twelve ways leaves small cells. Treat differences of a few percentage points as noise and say so in your report. The large gaps, 30 points and more, are real."),
 ("A caution on definitions",
  "Findex says 70.6% of Vietnamese adults aged 15+ had an account in 2024. The State Bank puts payment account penetration above 89% of people aged 15+ for H1 2026. The two are directly comparable in denominator and roughly 18 points apart. Both are defensible: one counts people who report having an account when surveyed, the other counts accounts on bank systems, which includes duplicates one person holds across banks. Findex separately finds only 2.1% of adults holding an inactive account, which does not close the gap. Do not mix them in one chart without saying which is which. Naming the discrepancy is worth marks under evidence transparency."),
 ("Verification",
  "Every figure on the 'Vietnam reference' sheet was re-checked against primary or Vietnamese-language sources on 20 September 2026. Twelve claims changed on review, including the small-firm credit access ladder, the biometric verification count, bank asset sizes and the brokerage market share tables. Appendix C of the accompanying report lists each one."),
 ("Licence",
  "World Bank Open Data, CC BY 4.0. Cite as: World Bank, Global Findex Database 2025. Reproducing it in a student report is fine; say where it came from."),
]
for lab, txt in rows:
    c1 = ws.cell(r, 2, lab); c1.font = B; c1.alignment = Alignment(vertical="top")
    c2 = ws.cell(r, 3, txt); c2.font = N; c2.alignment = Alignment(wrap_text=True, vertical="top")
    ws.row_dimensions[r].height = 14 * (1 + len(txt)//105)
    r += 1

r += 1
ws.cell(r, 2, "Sheets in this workbook").font = Font(name=F, size=11, bold=True, color=ACCENT)
r += 1
for lab, txt in [
 ("DNSE financials", "Quarterly and half-year revenue, profit and balance-sheet lines with computed margins and revenue mix."),
 ("Market share", "HOSE, HNX and derivatives brokerage share for every firm in the top ten, second quarter of 2026."),
 ("Industry cross-section", "Lending balances and pre-tax profit for the largest securities firms, with shares of the industry total."),
 ("DNSE position", "The five share measures that define the monetisation gap, each against its own denominator."),
 ("Review analysis", "Cleaning log, ratings by year, complaint themes and the three-app comparison."),
 ("Review quotes", "Fifty selected reviews with rating, date, helpfulness votes and theme tags."),
 ("Segment model", "The derived priority segment. Every index cell is a formula reading from Segments 2024."),
 ("Segments 2024", "51 Findex indicators by all twelve Findex segments, latest wave."),
 ("Segment gaps", "Computed gaps between rich and poor, urban and rural, and by education."),
 ("National 2024", "Indicators the World Bank publishes only at national level for 2024."),
 ("Trends", "Headline indicators across all five survey waves, 2011 to 2024."),
 ("Vietnam reference", "Macro, banking, payments and capital-markets figures with sources and periods."),
 ("Sources", "Where to get everything else, with links."),
]:
    ws.cell(r, 2, lab).font = B
    ws.cell(r, 3, txt).font = N
    r += 1

r += 1
ws.cell(r, 2, "Findex segment codes").font = Font(name=F, size=11, bold=True, color=ACCENT)
r += 1
ws.cell(r, 3, "Indicator ids ending .1 to .12 are segment cuts of the base indicator: .1 women, .2 men, .3 age 15-24, .4 age 25+, .5 primary education or less, .6 secondary or more, .7 poorest 40%, .8 richest 60%, .9 rural, .10 urban, .11 out of the labour force, .12 in the labour force. A suffix of .s means the figure is a share of a sub-population rather than of all adults.").font = N
ws.cell(r, 3).alignment = Alignment(wrap_text=True, vertical="top")
ws.row_dimensions[r].height = 42

# ---------------------------------------------------------------- SEGMENTS 2024
ws = wb.create_sheet("Segments 2024")
ws.sheet_view.showGridLines = False
headers = ["Indicator id", "Indicator", "Theme"] + SEGMENTS
widths = [22, 52, 16] + [13]*len(SEGMENTS)
for i, w in enumerate(widths, start=1):
    ws.column_dimensions[get_column_letter(i)].width = w

ws.cell(1, 1, "Vietnam Findex 2024: indicators by segment").font = TITLE
ws.cell(2, 1, "Percentage of adults aged 15+ in each segment. Source: World Bank Global Findex Database 2025, retrieved via the World Bank API, 20 September 2026.").font = SM

hr = 4
for i, h in enumerate(headers, start=1):
    c = ws.cell(hr, i, h); c.font = H; c.fill = hdr_fill; c.border = box
    c.alignment = Alignment(wrap_text=True, vertical="center", horizontal="center" if i > 3 else "left")
ws.row_dimensions[hr].height = 34
ws.freeze_panes = "D5"

r = hr + 1
seg_row_index = {}
for ind_id, label, theme, vals in SEG2024:
    seg_row_index[ind_id] = r
    fill = alt_fill if (r - hr) % 2 == 0 else None
    for i, v in enumerate([ind_id, label, theme], start=1):
        c = ws.cell(r, i, v); c.font = N; c.border = box
        if fill: c.fill = fill
    for si in range(len(SEGMENTS)):
        c = ws.cell(r, 4 + si, round(vals[si], 2) if si in vals else None)
        c.font = N; c.border = box; c.number_format = '0.0'
        if fill: c.fill = fill
    r += 1

last_seg_row = r - 1
ws.auto_filter.ref = f"A{hr}:{get_column_letter(len(headers))}{last_seg_row}"

# ---------------------------------------------------------------- SEGMENT GAPS
ws = wb.create_sheet("Segment gaps")
ws.sheet_view.showGridLines = False
ws.cell(1, 1, "Where the segment gaps are widest").font = TITLE
ws.cell(2, 1, "Every figure is a formula referencing 'Segments 2024', so edits there flow through. Gaps are in percentage points.").font = SM

gap_headers = ["Indicator", "Theme", "All adults", "Income gap (richest 60% less poorest 40%)",
               "Education gap (secondary+ less primary or less)", "Urban less rural",
               "Men less women", "Young less older", "In work less out of work"]
for i, w in enumerate([50, 16, 12, 17, 17, 13, 13, 13, 14], start=1):
    ws.column_dimensions[get_column_letter(i)].width = w

hr = 4
for i, h in enumerate(gap_headers, start=1):
    c = ws.cell(hr, i, h); c.font = H; c.fill = hdr_fill; c.border = box
    c.alignment = Alignment(wrap_text=True, vertical="center", horizontal="center" if i > 2 else "left")
ws.row_dimensions[hr].height = 46
ws.freeze_panes = "C5"

# segment column letters on 'Segments 2024': D=All,E=Women,F=Men,G=Young,H=Older,
# I=Primary,J=Secondary,K=Poorest,L=Richest,M=Rural,N=Urban,O=OutLF,P=InLF
r = hr + 1
for ind_id, label, theme, vals in SEG2024:
    sr = seg_row_index[ind_id]
    fill = alt_fill if (r - hr) % 2 == 0 else None
    c = ws.cell(r, 1, label); c.font = N; c.border = box
    c2 = ws.cell(r, 2, theme); c2.font = N; c2.border = box
    ws.cell(r, 3, f"='Segments 2024'!D{sr}")
    ws.cell(r, 4, f"='Segments 2024'!L{sr}-'Segments 2024'!K{sr}")
    ws.cell(r, 5, f"='Segments 2024'!J{sr}-'Segments 2024'!I{sr}")
    ws.cell(r, 6, f"='Segments 2024'!N{sr}-'Segments 2024'!M{sr}")
    ws.cell(r, 7, f"='Segments 2024'!F{sr}-'Segments 2024'!E{sr}")
    ws.cell(r, 8, f"='Segments 2024'!G{sr}-'Segments 2024'!H{sr}")
    ws.cell(r, 9, f"='Segments 2024'!P{sr}-'Segments 2024'!O{sr}")
    for col in range(1, 10):
        cc = ws.cell(r, col); cc.border = box
        if col >= 3:
            cc.font = N; cc.number_format = '0.0;(0.0);-'
        if fill: cc.fill = fill
    r += 1
ws.auto_filter.ref = f"A{hr}:I{r-1}"

# ---------------------------------------------------------------- NATIONAL 2024
ws = wb.create_sheet("National 2024")
ws.sheet_view.showGridLines = False
ws.cell(1, 1, "Vietnam Findex 2024: national figures without a published segment breakdown").font = TITLE
ws.cell(2, 1, "Percentage of adults aged 15+. These are the indicators the World Bank published for 2024 at national level only.").font = SM
for i, w in enumerate([22, 62, 18, 14], start=1):
    ws.column_dimensions[get_column_letter(i)].width = w
hr = 4
for i, h in enumerate(["Indicator id", "Indicator", "Theme", "2024 (%)"], start=1):
    c = ws.cell(hr, i, h); c.font = H; c.fill = hdr_fill; c.border = box
ws.freeze_panes = "A5"
r = hr + 1
for ind_id, label, theme, val in sorted(NATIONAL2024, key=lambda x: (x[2], -x[3])):
    fill = alt_fill if (r - hr) % 2 == 0 else None
    for i, v in enumerate([ind_id, label, theme], start=1):
        c = ws.cell(r, i, v); c.font = N; c.border = box
        if fill: c.fill = fill
    c = ws.cell(r, 4, round(val, 2)); c.font = N; c.border = box; c.number_format = '0.0'
    if fill: c.fill = fill
    r += 1
ws.auto_filter.ref = f"A{hr}:D{r-1}"

# ---------------------------------------------------------------- TRENDS
ws = wb.create_sheet("Trends")
ws.sheet_view.showGridLines = False
ws.cell(1, 1, "Vietnam Findex headline indicators, 2011 to 2024").font = TITLE
ws.cell(2, 1, "Percentage of adults aged 15+. Blank means the question was not asked in that wave. Change columns show percentage points.").font = SM
years = [2011, 2014, 2017, 2022, 2024]
hdrs = ["Indicator id", "Indicator"] + [str(y) for y in years] + ["Change 2017 to 2024", "Change 2022 to 2024"]
for i, w in enumerate([22, 52, 11, 11, 11, 11, 11, 17, 17], start=1):
    ws.column_dimensions[get_column_letter(i)].width = w
hr = 4
for i, h in enumerate(hdrs, start=1):
    c = ws.cell(hr, i, h); c.font = H; c.fill = hdr_fill; c.border = box
    c.alignment = Alignment(wrap_text=True, vertical="center", horizontal="center" if i > 2 else "left")
ws.row_dimensions[hr].height = 30
ws.freeze_panes = "C5"
r = hr + 1
for ind_id, label, series in TRENDS:
    fill = alt_fill if (r - hr) % 2 == 0 else None
    for i, v in enumerate([ind_id, label], start=1):
        c = ws.cell(r, i, v); c.font = N; c.border = box
        if fill: c.fill = fill
    for yi, y in enumerate(years):
        c = ws.cell(r, 3 + yi, round(series[y], 2) if y in series else None)
        c.font = N; c.border = box; c.number_format = '0.0'
        if fill: c.fill = fill
    # change columns as formulas, guarded for blanks
    c = ws.cell(r, 8, f'=IF(OR(E{r}="",G{r}=""),"",G{r}-E{r})')
    c.font = N; c.border = box; c.number_format = '0.0;(0.0);-'
    if fill: c.fill = fill
    c = ws.cell(r, 9, f'=IF(OR(F{r}="",G{r}=""),"",G{r}-F{r})')
    c.font = N; c.border = box; c.number_format = '0.0;(0.0);-'
    if fill: c.fill = fill
    r += 1
ws.auto_filter.ref = f"A{hr}:I{r-1}"

# ---------------------------------------------------------------- VIETNAM REFERENCE
ws = wb.create_sheet("Vietnam reference")
ws.sheet_view.showGridLines = False
ws.cell(1, 1, "Vietnam macro, banking and market reference figures").font = TITLE
ws.cell(2, 1, "Compiled 20 September 2026. Every row names its period and source. Re-check each figure against the source before citing it in a submission.").font = SM
for i, w in enumerate([18, 46, 30, 18, 34], start=1):
    ws.column_dimensions[get_column_letter(i)].width = w
hr = 4
for i, h in enumerate(["Category", "Indicator", "Value", "Period", "Source"], start=1):
    c = ws.cell(hr, i, h); c.font = H; c.fill = hdr_fill; c.border = box
ws.freeze_panes = "A5"

REF = [
("Macro","GDP growth","8.18%","H1 2026","National Statistics Office"),
("Macro","GDP growth","8.39%","Q2 2026","National Statistics Office"),
("Macro","GDP growth","7.83%","Q1 2026","National Statistics Office"),
("Macro","GDP growth forecast","7.3%","FY2026","Bloomberg survey, July 2026"),
("Macro","GDP growth forecast","6.8%","FY2026","World Bank, May 2026"),
("Macro","GDP growth forecast","7.2%","FY2026","AMRO"),
("Macro","CPI inflation","4.69% y/y","June 2026","National Statistics Office"),
("Macro","CPI inflation, average","4.38%","H1 2026","National Statistics Office"),
("Macro","Core inflation","4.50%","June 2026","National Statistics Office"),
("Macro","Retail sales","VND 3,889.5tn, +12.9% nominal, +7.3% real","H1 2026","National Statistics Office"),
("Macro","FDI registered","USD 34.65bn, +61.0%","H1 2026","National Statistics Office"),
("Macro","FDI disbursed","USD 13.03bn, +11.2%","H1 2026","National Statistics Office"),
("Macro","Exports","USD 266.52bn, +21.0%","H1 2026","National Statistics Office"),
("Macro","Imports","USD 283.17bn, +33.4%","H1 2026","National Statistics Office"),
("Macro","Trade deficit","USD 16.65bn","H1 2026","National Statistics Office"),
("Macro","Unemployment rate","2.22%","H1 2026","National Statistics Office"),
("Macro","Employed persons","52.6 million","H1 2026","National Statistics Office"),
("Macro","Average monthly income","About VND 9.0 million","Q2 2026","National Statistics Office"),
("Macro","New enterprises registered","111.7 thousand, +22.5%","H1 2026","National Statistics Office"),
("Macro","Enterprises dissolved","About 24.0 thousand, +94.7%","H1 2026","National Statistics Office"),
("Macro","Exchange rate","About VND 26,000 to 26,300 per USD","2026","UOB projections, market data"),

("Banking","Listed bank total assets","Over VND 21 quadrillion, +23%","End-2025","Listed bank filings"),
("Banking","Sector total assets including Agribank","Roughly VND 24 quadrillion","End-2025","Derived from bank filings"),
("Banking","Credit growth","About 19%","FY2025","SBV, FiinRatings"),
("Banking","Deposit growth","11.4%","FY2025","FiinRatings"),
("Banking","Credit to GDP","Above 140%","2025","FiinRatings"),
("Banking","Net interest margin, sector","2.9%","FY2025","FiinRatings"),
("Banking","Net interest margin, forecast","Below 3.0%","FY2026","FiinRatings"),
("Banking","NIM, state-owned banks","2.6%","FY2025","FiinRatings"),
("Banking","NIM, top four private banks","3.9%","FY2025","FiinRatings"),
("Banking","NIM, other private banks","2.7%","FY2025","FiinRatings"),
("Banking","Non-performing loan ratio","About 1.9%","FY2025","FiinRatings"),
("Banking","Special mention loans","1.2%","FY2025","FiinRatings"),
("Banking","Net write-offs","1.3% of average gross loans","FY2025","FiinRatings"),
("Banking","Return on assets","About 1.4%","FY2025","FiinRatings"),
("Banking","Sector return on equity","17 to 18%","FY2025","Market data"),
("Banking","Cost to income, median","51.0%","FY2025","FiinRatings"),
("Banking","Capital adequacy, median","11.9%","H1 2025","FiinRatings"),
("Banking","Loan to deposit, state-owned","78.3%","FY2025","FiinRatings"),
("Banking","Loan to deposit, top four private","82.8%","FY2025","FiinRatings"),
("Banking","Loan to deposit, other private","71.1%","FY2025","FiinRatings"),
("Banking","Non-interest income share","23.8% of total operating income","FY2025","FiinRatings"),
("Banking","Lending mix","Corporate 54%, retail 46%","FY2025","FiinRatings"),
("Banking","Real estate and construction loans","24.6% of total","FY2025","FiinRatings"),
("Banking","Twelve-month deposit rates","About 7%, some banks above 8%","March 2026","VinaCapital"),
("Banking","Listed banks with assets above VND 1 quadrillion","Six: BIDV, VietinBank, Vietcombank, MB, VPBank, Techcombank","End-2025","Bank filings"),
("Banking","BIDV total assets","About VND 3.3 quadrillion, +21%","End-2025","Bank filings"),
("Banking","VietinBank total assets","About VND 2.7 quadrillion, +16%","End-2025","Bank filings"),
("Banking","Vietcombank total assets","About VND 2.4 quadrillion, +17%","End-2025","Bank filings"),
("Banking","VPBank total assets","About VND 1.3 quadrillion, +36%","End-2025","Bank filings"),
("Banking","Techcombank total assets","About VND 1.2 quadrillion, +22%","End-2025","Bank filings"),
("Banking","MB total assets","Above VND 1,600 trillion, +43% y/y","End-2025","MB 2026 plan"),
("Banking","MB pre-tax profit","VND 34,268 billion, +18.9%","FY2025","MB 2026 plan"),
("Banking","MB outstanding loans","Above VND 1,000 trillion, +37%","FY2025","MB 2026 plan"),
("Banking","MB customers","35 million, target 40 million","2025 to 2026","MB 2026 plan"),
("Banking","MBBank app users","35 million, largest in Vietnam","2025","MB 2026 plan"),
("Banking","BIZ MBBank business users","More than 358,000","2025","MB 2026 plan"),
("Banking","MB 2026 targets","Credit and deposit growth 30-35%, profit +15%, ROE above 20%, NPL below 1%, CASA about 36%","FY2026","MB 2026 plan"),
("Banking","MB loan to deposit ratio","About 79%","2026","FiinRatings, press"),
("Banking","SMBC stake in VPBank","15%, acquired for USD 1.5 billion","Completed 2023","VPBank, SMBC"),
("Banking","Techcombank retail credit","VND 372.0 trillion, +30.8%","FY2025","Techcombank FY25 press release"),
("Banking","Techcombank corporate credit","VND 452.1 trillion, +13.4%","FY2025","Techcombank FY25 press release"),
("Banking","Techcombank customer deposits","VND 665.6 trillion, CASA balance VND 268.7 trillion, CASA ratio 40.4%","FY2025","Techcombank FY25 press release"),
("Banking","Techcombank profitability","ROE 16.0% LTM, ROA 2.4%, CIR 30.8%, NIM 3.8% LTM, NPL 1.13%, CAR 14.6%","FY2025","Techcombank FY25 press release"),
("Banking","Listed commercial banks","27","H1 2026","Vietnamese financial press"),
("Banking","SMBC Consumer Finance stake in FE Credit","49%","2021","VPBank, SMBC"),
("Banking","Cake by VPBank customers","About 6.2 million in 2025; company claims over 7 million by 2026","2025 to 2026","Company statements"),
("Banking","Cake profitability","EBITDA-positive from Q3 2024. Company-reported, no audited standalone accounts","2024","Company statements"),
("Banking","Cake average revenue per user","USD 25 in 2025, projected USD 44 in 2026. Company-reported, unaudited","2025 to 2026","Company statements"),

("Payments","Non-cash transactions","Over 15 billion transactions, over VND 190 quadrillion, volume +34.28%, value +12.24%","H1 2026","State Bank of Vietnam"),
("Payments","Non-cash payment value per day","About VND 1.05 quadrillion, roughly USD 40 billion","H1 2026","State Bank of Vietnam"),
("Payments","Non-cash transactions","Volume +43.3%, value +24.2%","9M 2025","State Bank of Vietnam"),
("Payments","QR code payments","Volume +61.6%, value +150.7%","9M 2025","State Bank of Vietnam"),
("Payments","Internet banking","Volume +51.2%, value +37.2%","9M 2025","State Bank of Vietnam"),
("Payments","Mobile banking","Volume +37.4%, value +21.8%","9M 2025","State Bank of Vietnam"),
("Payments","ATM transactions","Volume -16.77%, value -5.74%","9M 2025","State Bank of Vietnam"),
("Payments","Mobile Money accounts","10.89 million, 70% rural","September 2025","State Bank of Vietnam"),
("Payments","Individual payment accounts","About 232 million, +14%","2025","State Bank of Vietnam"),
("Payments","Cards in circulation","Over 164 million","2025","State Bank of Vietnam"),
("Payments","Payment account penetration, official","Over 89% of people aged 15+","H1 2026","State Bank of Vietnam"),
("Payments","Account ownership, survey measure","70.6% of adults aged 15+","Findex 2024 fieldwork","World Bank Global Findex"),
("Payments","Biometric verification","167.8 million individual customer records, 2.78 million institutional records. Counts records, not people","31 July 2026","State Bank of Vietnam"),
("Payments","SIMO fraud alerts","4.6 million customers alerted, 1.5 million transactions abandoned, about VND 5.2 trillion prevented","July 2026","State Bank of Vietnam"),
("Payments","Fraud prevention","440,000+ transactions flagged, VND 1.6tn prevented","2025","State Bank of Vietnam"),
("Payments","Licensed providers","53 payment providers, 49 e-wallet operators","2025","State Bank of Vietnam"),

("Business","Active economic establishments","Nearly 6.3 million, employing over 30.37 million people","2026 census","National Statistics Office"),
("Business","Enterprises","859,048","2026 census","National Statistics Office"),
("Business","Cooperatives","17,145","2026 census","National Statistics Office"),
("Business","Individual business households","5,254,952","2026 census","National Statistics Office"),
("Business","Enterprise growth versus 2020","+25.5%","2026 census","National Statistics Office"),
("Business","FDI enterprises","About 30,000, +34% versus 2020","2026 census","National Statistics Office"),
("Business","Workers in economic establishments","Over 30.37 million","2026 census","National Statistics Office"),
("Business","Enterprise employment","17.6 million, about 57.6% of workers in economic establishments, not of the 52.6 million national employed","2026 census","National Statistics Office"),
("Business","Micro enterprise credit access","8.8%","To July 2026","FiinGroup"),
("Business","Small and medium enterprise credit access","30.9%","To July 2026","FiinGroup"),
("Business","All SMEs credit access","20.5%","To July 2026","FiinGroup"),
("Business","Large enterprise credit access","61.4%","To July 2026","FiinGroup"),
("Business","Preferential credit programme","VND 408 trillion across 12 banks, for SMEs and other growth drivers, not SME-only","24 August 2026","Thoi bao Ngan hang, SBV directive 7 August 2026"),
("Business","Big four share of SME commitment","VND 220 trillion","August 2026","Press reporting"),
("Business","Tax exemption threshold","VND 500 million revenue","From 2026","Revised Personal Income Tax Law"),
("Business","E-invoice threshold","VND 1 billion revenue","From 2026","Decree 68/2026/ND-CP"),
("Business","Net income method threshold","VND 3 billion revenue","From 2026","Decree 68/2026/ND-CP"),

("Markets","Domestic individual securities accounts","13.8 million, about 14% of the population","End-August 2026","VSDC"),
("Markets","Foreign securities accounts","52,633","End-August 2026","VSDC"),
("Markets","New accounts in 2026","Over 2 million, about 230,000 in August","To end-August 2026","VSDC"),

("Markets","Retail share of account growth","Over 99%","2026","VSDC"),
("Markets","Margin lending outstanding","Over VND 420 trillion","Q1 2026","Securities company filings"),
("Markets","Industry margin to equity","About 83%, ceiling 200%","Q1 2026","Securities company filings"),
("Markets","Brokerage share, VPS","12.61%","Q2 2026 HOSE","HOSE"),
("Markets","Brokerage share, SSI","11.17%","Q2 2026 HOSE","HOSE"),
("Markets","Brokerage share, TCBS","9.36%","Q2 2026 HOSE","HOSE"),
("Markets","Brokerage share, VPS on HNX","17.71%","Q2 2026 HNX","HNX"),
("Markets","Brokerage share, TCBS on HNX","9.00%","Q2 2026 HNX","HNX"),
("Markets","Derivatives share, VPS","33.84%, first place","Q2 2026","HNX"),
("Markets","DNSE derivatives share","25.38%, second behind VPS","Q2 2026","DNSE investor relations"),
("Markets","DNSE derivatives share","25.47%, second place","H1 2026","DNSE investor relations"),
("Markets","DNSE listed stock share on HNX","2.88%, eighth","Q2 2026","DNSE investor relations"),
("Markets","DNSE revenue","VND 455.2 billion, +55.9% y/y","Q2 2026","DNSE investor relations"),
("Markets","DNSE revenue","VND 852.6 billion, +58.4% y/y","H1 2026","DNSE investor relations"),
("Markets","DNSE pre-tax profit","VND 98.9 billion, +8.7% y/y","Q2 2026","DNSE investor relations"),
("Markets","TCBS assets under management","VND 645 trillion","FY2025","Techcombank investor presentation"),
("Markets","FTSE Russell reclassification","Frontier to Secondary Emerging, effective at the open on 21 September 2026","2026","LSEG, FTSE Russell"),
("Markets","Vietnamese stocks in the FTSE review","28","2026","LSEG, FTSE Russell"),
("Markets","FTSE-benchmarked assets","About USD 18.1 trillion","2026","FTSE Russell"),

("Insurance","Life new business premiums","VND 23 trillion","2017","Milliman"),
("Insurance","Life new business premiums","VND 50 trillion","2022","Milliman"),
("Insurance","Life new business premiums","VND 34 trillion","2023","Milliman"),
("Insurance","Life new business premiums","VND 25 trillion","2024","Milliman"),
("Insurance","Life new business premiums","VND 24 trillion","2025","Milliman"),
("Insurance","Bancassurance growth before the crisis","53% CAGR","To 2022","Milliman"),
("Insurance","Top seven market share","75%, Bao Viet Life 21%","2025","Milliman"),
("Insurance","First-year lapse rates","Above 70% at some insurers","Post-crisis","Milliman"),

("Regulation","Decree 94/2025/ND-CP","Banking sandbox: P2P lending, open API, credit scoring","From 1 July 2025","Government of Vietnam"),
("Regulation","Circular 64/2024/TT-NHNN","Open API standards, compliance by 1 March 2027","2024","State Bank of Vietnam"),
("Regulation","Resolution 202/2025/QH15","Provinces reduced from 63 to 34, being 28 provinces and 6 centrally-run cities; districts abolished","Passed 12 June 2025, effective 1 July 2025","National Assembly"),
("Regulation","Decree 68/2026/ND-CP","Household business tax administration","5 March 2026","Government of Vietnam"),
("Regulation","Lump-sum tax abolished","Household businesses must self-declare","From 1 January 2026","Revised Personal Income Tax Law"),
("Regulation","Resolution 05/2025/NQ-CP","Five-year crypto pilot, charter capital VND 10,000bn","9 September 2025","Government of Vietnam"),
("Regulation","Circular 14/2025","Basel III capital requirements","Phasing in","State Bank of Vietnam"),
]

r = hr + 1
cat = None
for row in REF:
    fill = warm_fill if row[0] != cat else (alt_fill if (r - hr) % 2 == 0 else None)
    if row[0] != cat:
        cat = row[0]
    for i, v in enumerate(row, start=1):
        c = ws.cell(r, i, v); c.font = N; c.border = box
        c.alignment = Alignment(wrap_text=True, vertical="top")
        if fill: c.fill = fill
    r += 1
ws.auto_filter.ref = f"A{hr}:E{r-1}"

# ---------------------------------------------------------------- SOURCES
ws = wb.create_sheet("Sources")
ws.sheet_view.showGridLines = False
ws.cell(1, 1, "Where to get the rest of the data").font = TITLE
ws.cell(2, 1, "Checked in a browser on 20 September 2026. Notes record what was actually found, including where a site turned out to be thinner than expected.").font = SM
for i, w in enumerate([26, 30, 56, 48], start=1):
    ws.column_dimensions[get_column_letter(i)].width = w
hr = 4
for i, h in enumerate(["Source", "Covers", "Link", "Notes"], start=1):
    c = ws.cell(hr, i, h); c.font = H; c.fill = hdr_fill; c.border = box
ws.freeze_panes = "A5"

SRC = [
("World Bank Microdata Library","Findex respondent-level file","microdata.worldbank.org/index.php/catalog/7998","Verified: 1,000 cases, 199 variables, reference VNM_2024_FINDEX_v02_M. Free after accepting terms, no registration"),
("World Bank Open Data API","Findex aggregates","api.worldbank.org/v2/sources/28/country/VNM/series/all/data?format=json","Verified: the source of this workbook. No key needed"),
("National Statistics Office","GDP, CPI, FDI, trade, provincial data, 2026 census","nso.gov.vn","English releases available. Provincial series break at 1 July 2025 because of the merger"),
("State Bank of Vietnam","Payment statistics, credit data, circulars","sbv.gov.vn","Aggregate only. Good for payments and regulation"),
("Vietstock","Listed company financials","finance.vietstock.vn/TICKER/tai-chinh.htm","Verified: swap the ticker to change company. History to 2011. Pre-computes NIM, cost of funds and yield on earning assets. Has a data export menu"),
("CafeF","Listed company financials","s.cafef.vn","Alternative structure, useful as a cross-check against Vietstock"),
("VPBank investor relations","VPB filings and investor decks","vpbank.com.vn/en/quan-he-nha-dau-tu","Verified: statements 2011 to 2026, VAS and IFRS, consolidated and separate, searchable PDFs. Quarterly Performance Packs carry segment detail"),
("DNSE investor relations","DSE filings and market share","ir.dnse.com.vn/en","Verified: English site, Q2 2026 published, annual reports 2024 and 2025, earnings releases with market share"),
("Techcombank investor relations","TCB investor presentation","techcombank.com","The most detailed investor deck in Vietnamese banking"),
("MB","MBB filings","mbbank.com.vn","English investor pages were partly unavailable when checked. Use Vietstock and HOSE instead"),
("HOSE","Listings, filings, brokerage share","hsx.vn","Quarterly brokerage market share tables"),
("HNX","Listings, derivatives market share","hnx.vn","Source of the DNSE derivatives share figures"),
("VSDC","Securities account statistics","vsdc.vn","Monthly account openings split by investor type"),
("NAPAS","Interbank switching, VietQR","napas.com.vn","Aggregate payment statistics"),
("FiinRatings and FiinGroup","Banking and consumer finance research","fiinratings.vn, fiingroup.vn","Some reports free. Source of most banking metrics in this workbook"),
("VinaCapital","Monthly macro commentary","vof.vinacapital.com","Free, current, well sourced"),
("Milliman","Life insurance analysis","milliman.com","Source of the insurance premium series"),
("Google Play scraping","App reviews","google-play-scraper on npm or PyPI","Thousands of dated, rated, versioned reviews per app. Genuinely messy, which suits the data-cleaning criterion"),
("App Store scraping","App reviews","app-store-scraper","Same approach for iOS"),
]
r = hr + 1
for row in SRC:
    fill = alt_fill if (r - hr) % 2 == 0 else None
    for i, v in enumerate(row, start=1):
        c = ws.cell(r, i, v); c.font = N; c.border = box
        c.alignment = Alignment(wrap_text=True, vertical="top")
        if fill: c.fill = fill
    r += 1


# ================================================================
# CONSOLIDATED SHEETS ADDED FOR THE DNSE REPORT
# ================================================================
import reviews as RV
import brokers as BR

BLUE_IN = Font(name=F, size=10, color="0000FF")          # hardcoded input
GREEN_LK = Font(name=F, size=10, color="008000")         # link to another sheet
YELLOW = PatternFill("solid", fgColor="FFFF00")

def sheet(name, title, subtitle, widths):
    w = wb.create_sheet(name)
    w.sheet_view.showGridLines = False
    w.cell(1, 1, title).font = TITLE
    w.cell(2, 1, subtitle).font = SM
    for i, ww in enumerate(widths, start=1):
        w.column_dimensions[get_column_letter(i)].width = ww
    return w

def head(w, row, labels, center_from=1):
    for i, h in enumerate(labels, start=1):
        c = w.cell(row, i, h); c.font = H; c.fill = hdr_fill; c.border = box
        c.alignment = Alignment(wrap_text=True, vertical="center",
                                horizontal="center" if i > center_from else "left")
    w.row_dimensions[row].height = 30

def put(w, row, col, val, font=None, fmt=None, fill=None, wrap=False):
    c = w.cell(row, col, val)
    c.font = font or N
    c.border = box
    if fmt: c.number_format = fmt
    if fill: c.fill = fill
    if wrap: c.alignment = Alignment(wrap_text=True, vertical="top")
    return c

MONEY = '#,##0.0;(#,##0.0);-'
INT = '#,##0;(#,##0);-'
PCT1 = '0.0;(0.0);-'
PCT2 = '0.00;(0.00);-'

# ---------------------------------------------------------------- DNSE FINANCIALS
ws = sheet("DNSE financials",
           "DNSE Securities: reported financials",
           "VND billion unless stated. Blue cells are figures taken directly from DNSE disclosures. "
           "Black cells are formulas. Source: DNSE quarterly financial statements and investor relations releases.",
           [42, 15, 15, 15, 15, 15, 46])
hr = 4
head(ws, hr, ["Line", "FY2025", "Q1 2026", "Q2 2026", "H1 2026", "H1 as % of FY2025", "Note"], 1)
ws.freeze_panes = "B5"

FIN = [
    # label, FY2025, Q1, Q2, H1 (None means compute as Q1+Q2), fmt, note
    ("Operating revenue",                  1467.0, 395.0, 453.1, 848.2, MONEY,
     "Half-year revenue of 848.2 reconciles with the two quarterly figures to within rounding."),
    ("Interest on lending and receivables", 555.8, 147.5, 188.6, None, MONEY, ""),
    ("Brokerage commissions",               404.0, 119.5, 102.5, None, MONEY, "Majority derivatives"),
    ("Investment income",                   171.4,  98.4,  95.0, None, MONEY, "FVTPL and held to maturity"),
    ("Other revenue",                       335.8,  29.6,  67.0, None, MONEY,
     "Residual of each column."),
    ("Pre-tax profit",                      340.2,  14.2,  98.9, 113.1, MONEY, ""),
    ("Profit after tax",                    272.5,  11.3,  83.0,  94.3, MONEY, ""),
    ("Margin loans and advances, period end",5832.0,5910.0,6303.0,6303.0, INT,
     "Balance, not a flow. H1 equals the Q2 closing balance. Q2 2026 is a record for the firm."),
]
r = hr + 1
rowmap = {}
for lab, fy, q1, q2, h1, fmt, note in FIN:
    fill = alt_fill if (r - hr) % 2 == 0 else None
    put(ws, r, 1, lab, B, fill=fill)
    put(ws, r, 2, fy, BLUE_IN, fmt, fill)
    put(ws, r, 3, q1, BLUE_IN, fmt, fill)
    put(ws, r, 4, q2, BLUE_IN, fmt, fill)
    if h1 is None:
        put(ws, r, 5, f"=C{r}+D{r}", N, fmt, fill)
    else:
        put(ws, r, 5, h1, BLUE_IN, fmt, fill)
    put(ws, r, 6, f'=IF(B{r}=0,"",E{r}/B{r}*100)', N, PCT1, fill)
    put(ws, r, 7, note, SM, fill=fill, wrap=True)
    rowmap[lab] = r
    r += 1

rev = rowmap["Operating revenue"]; pbt = rowmap["Pre-tax profit"]
r += 1
ws.cell(r, 1, "Computed ratios").font = Font(name=F, size=11, bold=True, color=ACCENT)
r += 1
head(ws, r, ["Ratio", "FY2025", "Q1 2026", "Q2 2026", "H1 2026", "", "Note"], 1)
hr2 = r
r += 1
put(ws, r, 1, "Pre-tax profit margin, per cent", B)
for col in "BCDE":
    put(ws, r, "BCDE".index(col) + 2, f"={col}{pbt}/{col}{rev}*100", N, PCT1)
put(ws, r, 7, "Falls from 23.2 in 2025 to 13.3 at the 2026 half year", SM, wrap=True)
r += 1
for lab in ["Interest on lending and receivables", "Brokerage commissions", "Investment income"]:
    put(ws, r, 1, f"{lab}, share of revenue", N)
    for col in "BCDE":
        put(ws, r, "BCDE".index(col) + 2, f"={col}{rowmap[lab]}/{col}{rev}*100", N, PCT1)
    r += 1

r += 1
ws.cell(r, 1, "Customers, plan and yield").font = Font(name=F, size=11, bold=True, color=ACCENT)
r += 1
head(ws, r, ["Item", "Value", "Unit", "", "", "", "Source or formula"], 1)
r += 1
ACC = [
    ("Customer accounts, end 2025", 1500000, "accounts", "DNSE annual report 2025"),
    ("Customer accounts, Q1 2026", 1650000, "accounts", "Q1 2026 release"),
    ("Customer accounts, H1 2026", 1700000, "accounts", "H1 2026 release, stated as over 1.7 million"),
    ("Share of new accounts opened, 2025", 20.0, "per cent", "DNSE annual report 2025"),
    ("Share of new accounts opened, Q1 2026", 18.0, "per cent", "Q1 2026 release, 142,000 accounts"),
    ("2026 revenue target", 1736.0, "VND bn", "2026 annual general meeting"),
    ("2026 pre-tax profit target", 550.0, "VND bn", "2026 annual general meeting"),
    ("Charter capital", 4286.0, "VND bn", "428.6 million shares"),
    ("Customer assets, end 2025", 52000.0, "VND bn", "DNSE annual report 2025, approximate"),
]
first_acc = r
for lab, val, unit, src in ACC:
    fill = alt_fill if (r - first_acc) % 2 == 0 else None
    put(ws, r, 1, lab, N, fill=fill)
    put(ws, r, 2, val, BLUE_IN, INT if unit == "accounts" else MONEY, fill)
    put(ws, r, 3, unit, N, fill=fill)
    for cc in (4, 5, 6):
        put(ws, r, cc, None, N, fill=fill)
    put(ws, r, 7, src, SM, fill=fill, wrap=True)
    rowmap[lab] = r
    r += 1

r += 1
DERIVED = [
    ("Revenue per account, H1 2026, VND thousand",
     f"=E{rev}*1000000/B{rowmap['Customer accounts, H1 2026']}", '#,##0',
     "Half-year operating revenue divided by accounts"),
    ("Brokerage revenue per account, H1 2026, VND thousand",
     f"=E{rowmap['Brokerage commissions']}*1000000/B{rowmap['Customer accounts, H1 2026']}", '#,##0',
     "Half-year brokerage commissions divided by accounts"),
    ("Customer assets per account, end 2025, VND million",
     f"=B{rowmap['Customer assets, end 2025']}*1000/B{rowmap['Customer accounts, end 2025']}", '#,##0.0',
     "Approximate customer assets divided by accounts"),
    ("Implied annual yield on lending, per cent",
     f"=E{rowmap['Interest on lending and receivables']}/((C{rowmap['Margin loans and advances, period end']}"
     f"+D{rowmap['Margin loans and advances, period end']})/2)*2*100", PCT1,
     "Half-year interest divided by the average of the Q1 and Q2 closing balances, annualised"),
    ("H1 revenue as a share of the 2026 target, per cent",
     f"=E{rev}/B{rowmap['2026 revenue target']}*100", PCT1, "Half-year pace would be 50"),
    ("H1 profit as a share of the 2026 target, per cent",
     f"=E{pbt}/B{rowmap['2026 pre-tax profit target']}*100", PCT1, "Half-year pace would be 50"),
    ("Pre-tax profit still required in H2 2026, VND bn",
     f"=B{rowmap['2026 pre-tax profit target']}-E{pbt}", MONEY, "Target less the half-year result"),
    ("H2 requirement as a multiple of H1",
     f"=(B{rowmap['2026 pre-tax profit target']}-E{pbt})/E{pbt}", '0.00"x"', ""),
]
ws.cell(r, 1, "Derived measures").font = Font(name=F, size=11, bold=True, color=ACCENT)
r += 1
head(ws, r, ["Measure", "Value", "", "", "", "", "Definition"], 1)
r += 1
first_d = r
for lab, formula, fmt, note in DERIVED:
    fill = alt_fill if (r - first_d) % 2 == 0 else None
    put(ws, r, 1, lab, B, fill=fill)
    put(ws, r, 2, formula, N, fmt, fill)
    for cc in (3, 4, 5, 6):
        put(ws, r, cc, None, N, fill=fill)
    put(ws, r, 7, note, SM, fill=fill, wrap=True)
    r += 1

# ---------------------------------------------------------------- MARKET SHARE
ws = sheet("Market share",
           "Brokerage market share, second quarter of 2026",
           "Each percentage is a share of traded value on the named market. Shares from different markets are not comparable "
           "with one another. Sources: HOSE and HNX quarterly announcements of 7 July 2026.",
           [30, 16, 16, 16, 16, 16, 40])
hr = 4
head(ws, hr, ["Firm", "HOSE Q2 2026", "HOSE Q1 2026", "HOSE change, points",
              "HNX Q2 2026", "Derivatives Q2 2026", "Note"], 1)
ws.freeze_panes = "B5"

hnx_map = {n: v for _, n, v in BR.HNX_Q2_2026}
der_map = {n: v for _, n, v in BR.DERIV_Q2_2026}
notes = {"VPS": "Leads every market but lost 2.71 points of HOSE share in one quarter",
         "VPBankS": "Largest gainer of the quarter on both exchanges",
         "DNSE": "Second in derivatives, eighth on HNX, outside the top ten on HOSE",
         "TCBS": "Largest lending book in the industry"}
r = hr + 1
firms = []
for _, name, q2, q1 in BR.HOSE_Q2_2026:
    firms.append(name)
    fill = alt_fill if (r - hr) % 2 == 0 else None
    put(ws, r, 1, name, B, fill=fill)
    put(ws, r, 2, q2, BLUE_IN, PCT2, fill)
    put(ws, r, 3, q1, BLUE_IN, PCT2, fill)
    put(ws, r, 4, f'=IF(OR(B{r}="",C{r}=""),"",B{r}-C{r})', N, PCT2, fill)
    put(ws, r, 5, hnx_map.get(name), BLUE_IN, PCT2, fill)
    put(ws, r, 6, der_map.get(name), BLUE_IN, PCT2, fill)
    put(ws, r, 7, notes.get(name, ""), SM, fill=fill, wrap=True)
    r += 1
for _, name, v in BR.HNX_Q2_2026:
    if name in firms or v is None:
        continue
    fill = alt_fill if (r - hr) % 2 == 0 else None
    put(ws, r, 1, name, B, fill=fill)
    put(ws, r, 2, "outside top ten", N, fill=fill)
    put(ws, r, 3, None, N, fill=fill)
    put(ws, r, 4, None, N, fill=fill)
    put(ws, r, 5, v, BLUE_IN, PCT2, fill)
    put(ws, r, 6, der_map.get(name), BLUE_IN, PCT2, fill)
    put(ws, r, 7, notes.get(name, ""), SM, fill=fill, wrap=True)
    r += 1
last_ms = r - 1
put(ws, r, 1, "Sum of the firms listed above", B)
put(ws, r, 2, f"=SUM(B{hr+1}:B{last_ms})", N, PCT2)
put(ws, r, 3, f"=SUM(C{hr+1}:C{last_ms})", N, PCT2)
put(ws, r, 4, None, N)
put(ws, r, 5, f"=SUM(E{hr+1}:E{last_ms})", N, PCT2)
put(ws, r, 6, f"=SUM(F{hr+1}:F{last_ms})", N, PCT2)
put(ws, r, 7, "HOSE column should reconcile to the top-ten total of 65.19", SM, wrap=True)
r += 1
put(ws, r, 1, "Published top ten total", B)
put(ws, r, 2, 65.19, BLUE_IN, PCT2)
put(ws, r, 3, BR.HOSE_TOP10_Q1, BLUE_IN, PCT2)
put(ws, r, 4, None, N)
put(ws, r, 5, BR.HNX_TOP10_Q2, BLUE_IN, PCT2)
put(ws, r, 6, BR.DERIV_TOP10_Q2, BLUE_IN, PCT2)
put(ws, r, 7, "HNX and derivatives columns include only the firms whose figures were published", SM, wrap=True)
r += 3

ws.cell(r, 1, "DNSE derivatives brokerage share by quarter").font = Font(name=F, size=11, bold=True, color=ACCENT)
r += 1
head(ws, r, ["Quarter", "Share, per cent", "Change on previous, points", "", "", "", "Source"], 1)
r += 1
first_q = r
for i, (q, v) in enumerate(BR.DNSE_DERIV_SERIES):
    fill = alt_fill if (r - first_q) % 2 == 0 else None
    put(ws, r, 1, q, N, fill=fill)
    put(ws, r, 2, v, BLUE_IN, PCT2, fill)
    put(ws, r, 3, "" if i == 0 else f"=B{r}-B{r-1}", N, PCT2, fill)
    for cc in (4, 5, 6):
        put(ws, r, cc, None, N, fill=fill)
    put(ws, r, 7, "HNX quarterly announcement", SM, fill=fill)
    r += 1

# ---------------------------------------------------------------- INDUSTRY CROSS-SECTION
ws = sheet("Industry cross-section",
           "Vietnamese securities industry, second quarter of 2026",
           "Lending balances and pre-tax profit from quarterly financial statements. Shares are formulas against the "
           "industry total in the assumption cell below.",
           [30, 20, 20, 20, 20, 44])
hr = 4
head(ws, hr, ["Firm", "Lending balance, VND bn", "Share of industry, per cent",
              "Q2 2026 pre-tax profit, VND bn", "HOSE brokerage share, per cent", "Note"], 1)
ws.freeze_panes = "B5"
pbt_map = {n: v for n, v, _ in BR.PBT_Q2_2026}
yoy_map = {n: c for n, _, c in BR.PBT_Q2_2026}
hose_map = {n: v for _, n, v, _ in BR.HOSE_Q2_2026}
allfirms = sorted(set(list(dict(BR.MARGIN_Q2_2026).keys()) + list(pbt_map.keys())),
                  key=lambda n: -(dict(BR.MARGIN_Q2_2026).get(n) or 0))
mg = dict(BR.MARGIN_Q2_2026)
r = hr + 1
first_f = r
for name in allfirms:
    fill = alt_fill if (r - first_f) % 2 == 0 else None
    put(ws, r, 1, name, B, fill=fill)
    put(ws, r, 2, mg.get(name), BLUE_IN, INT, fill)
    put(ws, r, 3, f'=IF(B{r}="","",B{r}/$B${first_f + len(allfirms) + 1}*100)', N, PCT2, fill)
    put(ws, r, 4, pbt_map.get(name), BLUE_IN, MONEY, fill)
    put(ws, r, 5, hose_map.get(name), BLUE_IN, PCT2, fill)
    put(ws, r, 6, ("Year on year " + yoy_map[name]) if name in yoy_map else "", SM, fill=fill, wrap=True)
    r += 1
put(ws, r, 1, "Firms listed above", B)
put(ws, r, 2, f"=SUM(B{first_f}:B{r-1})", N, INT)
put(ws, r, 3, f"=B{r}/$B${r+1}*100", N, PCT2)
put(ws, r, 4, f"=SUM(D{first_f}:D{r-1})", N, MONEY)
put(ws, r, 5, None, N)
put(ws, r, 6, "", SM)
r += 1
put(ws, r, 1, "Industry total lending", B, fill=warm_fill)
put(ws, r, 2, BR.MARGIN_TOTAL_Q2, BLUE_IN, INT, warm_fill)
put(ws, r, 3, None, N, fill=warm_fill)
put(ws, r, 4, None, N, fill=warm_fill)
put(ws, r, 5, None, N, fill=warm_fill)
put(ws, r, 6, BR.MARGIN_NOTE, SM, fill=warm_fill, wrap=True)
ws.row_dimensions[r].height = 40
ind_total_row = r
r += 2
put(ws, r, 1, "Previous quarter industry total", N)
put(ws, r, 2, BR.MARGIN_TOTAL_Q1, BLUE_IN, INT)
put(ws, r, 3, f"=(B{ind_total_row}-B{r})/B{r}*100", N, PCT1)
put(ws, r, 4, None, N)
put(ws, r, 5, None, N)
put(ws, r, 6, "Quarterly growth in industry lending, per cent, reported as 7", SM, wrap=True)

# ---------------------------------------------------------------- DNSE POSITION
ws = sheet("DNSE position",
           "Where DNSE is large and where it is small",
           "Each row compares DNSE against its own denominator. The five denominators differ, so the rows measure "
           "position in five separate markets rather than five slices of one market.",
           [42, 20, 20, 22, 18, 44])
hr = 4
head(ws, hr, ["Measure", "DNSE", "Market total", "Unit", "DNSE share, per cent", "Source"], 1)
POS = [
    ("Customer accounts", 1700000, 13852633, "accounts",
     "13.80 million domestic individual accounts plus 52,633 foreign accounts, end August 2026, VSDC"),
    ("Derivatives brokerage", 25.38, 100.0, "per cent of traded value", "HNX Q2 2026 announcement"),
    ("HNX listed-share brokerage", 2.88, 100.0, "per cent of traded value", "HNX Q2 2026 announcement, rank 8 of 10"),
    ("HOSE listed-share brokerage", None, 100.0, "per cent of traded value",
     "Not in the top ten. Tenth place held 2.94 per cent, so DNSE is below that"),
    ("Lending balance", 6303.0, 453800.0, "VND bn", "Q2 2026 financial statements, industry total from Vietstock"),
    ("Q2 2026 pre-tax profit", 98.9, 9977.0, "VND bn", "Sum of the firms on the Industry cross-section sheet"),
]
r = hr + 1
first_p = r
for lab, dv, tot, unit, src in POS:
    fill = alt_fill if (r - first_p) % 2 == 0 else None
    put(ws, r, 1, lab, B, fill=fill)
    put(ws, r, 2, dv, BLUE_IN, INT if unit == "accounts" else MONEY, fill)
    put(ws, r, 3, tot, BLUE_IN, INT if unit == "accounts" else MONEY, fill)
    put(ws, r, 4, unit, N, fill=fill)
    put(ws, r, 5, f'=IF(B{r}="","",B{r}/C{r}*100)', N, PCT2, fill)
    put(ws, r, 6, src, SM, fill=fill, wrap=True)
    r += 1
acc_row, hnx_row = first_p, first_p + 2
r += 1
ws.cell(r, 1, "The monetisation gap").font = Font(name=F, size=11, bold=True, color=ACCENT)
r += 1
head(ws, r, ["Ratio", "Value", "", "", "", "Reading"], 1)
r += 1
put(ws, r, 1, "HNX trading share divided by account share", B)
put(ws, r, 2, f"=E{hnx_row}/E{acc_row}", N, '0.000')
for cc in (3, 4, 5):
    put(ws, r, cc, None, N)
put(ws, r, 6, "An average DNSE account trades at this fraction of the value of an average market account", SM, wrap=True)
r += 1
put(ws, r, 1, "Lending share divided by account share", B)
put(ws, r, 2, f"=E{first_p+4}/E{acc_row}", N, '0.000')
for cc in (3, 4, 5):
    put(ws, r, cc, None, N)
put(ws, r, 6, "An average DNSE account carries this fraction of the borrowing of an average market account", SM, wrap=True)
r += 1
put(ws, r, 1, "Derivatives share divided by account share", B)
put(ws, r, 2, f"=E{first_p+1}/E{acc_row}", N, '0.000')
for cc in (3, 4, 5):
    put(ws, r, cc, None, N)
put(ws, r, 6, "Above one, so the derivatives franchise runs ahead of the account base", SM, wrap=True)

# ---------------------------------------------------------------- REVIEW ANALYSIS
ws = sheet("Review analysis",
           "Google Play reviews: DNSE Entrade X and two competitors",
           "Collected 20 to 21 September 2026 from the public Google Play listings. The cleaning rule described below "
           "was applied identically to all three applications.",
           [40, 15, 15, 15, 15, 15, 46])
r = 4
ws.cell(r, 1, "Method").font = Font(name=F, size=11, bold=True, color=ACCENT)
r += 1
METHOD = [
    ("Retrieval", "Google Play public review listing, paginated through the store's own continuation token. "
                  "Fields captured: review id, author, star rating, text, timestamp, helpfulness votes. No authentication."),
    ("Normalisation", "Every review text was converted to a comparable form before filtering: Unicode compatibility "
                      "composition, then decomposition with combining marks removed, then lower case. The first step "
                      "matters because much of the loan spam disguises itself with mathematical alphanumeric characters "
                      "such as VayTotNhat, which plain keyword filters miss."),
    ("Loan spam rule", "vay 9 | vaytotnhat | vay t?o?t nhat | ktien | vayhangdau | vay333 | vayfe | fbvay | c0m | "
                       ".com | vay 0 % | vay von 0"),
    ("Referral spam rule", "ma (gioi thieu | gt | moi | dai ly) | nhap ma | ref(erral)? id | ma + five or more digits | "
                           "six digits followed by nhan or ma"),
    ("Duplicate rule", "Identical alphanumeric-only normalised text. Second and later copies removed. "
                       "Texts under four characters are exempt."),
    ("Generic flag", "A retained review of four words or fewer carrying no theme, for example tot, hay, ok. "
                     "Counted separately rather than removed, so that a year full of one-word praise cannot be read as satisfaction."),
    ("Theme tags", "Non-exclusive keyword matches on the normalised text. A review may carry several themes or none."),
    ("Known limitation", "App store reviews are self-selected and over-represent dissatisfied users. The peer comparison "
                         "mitigates this partially, because the same bias applies to all three applications. "
                         "The VPS sample is capped at 1,200 by pagination and is truncated toward recent reviews."),
]
for lab, txt in METHOD:
    ws.cell(r, 1, lab).font = B
    ws.cell(r, 1).alignment = Alignment(vertical="top")
    c = ws.cell(r, 2, txt); c.font = N; c.alignment = Alignment(wrap_text=True, vertical="top")
    ws.merge_cells(start_row=r, start_column=2, end_row=r, end_column=7)
    ws.row_dimensions[r].height = 13 * (1 + len(txt) // 108)
    r += 1

r += 1
ws.cell(r, 1, "Cleaning log").font = Font(name=F, size=11, bold=True, color=ACCENT)
r += 1
head(ws, r, ["Stage", "DNSE", "VPS SmartOne", "FPTS EzTrade", "", "", "Note"], 1)
r += 1
first_c = r
CLEAN = [
    ("Reviews retrieved", 868, 1200, 177, "Full available history except VPS, capped by pagination"),
    ("Loan advertising removed", 127, None, None, ""),
    ("Referral farming removed", 72, None, None, ""),
    ("Duplicates removed", 36, None, None, ""),
    ("Reviews retained", 633, 1116, 169, "DNSE loses 27.1 per cent, VPS 7.0, FPTS 4.5"),
]
for lab, a, b, cc_, note in CLEAN:
    fill = alt_fill if (r - first_c) % 2 == 0 else None
    put(ws, r, 1, lab, B, fill=fill)
    put(ws, r, 2, a, BLUE_IN, INT, fill)
    put(ws, r, 3, b, BLUE_IN, INT, fill)
    put(ws, r, 4, cc_, BLUE_IN, INT, fill)
    put(ws, r, 5, None, N, fill=fill)
    put(ws, r, 6, None, N, fill=fill)
    put(ws, r, 7, note, SM, fill=fill, wrap=True)
    r += 1
put(ws, r, 1, "Removed as a share of the pull, per cent", N)
for col, ci in (("B", 2), ("C", 3), ("D", 4)):
    put(ws, r, ci, f"=({col}{first_c}-{col}{first_c+4})/{col}{first_c}*100", N, PCT1)
put(ws, r, 5, None, N); put(ws, r, 6, None, N)
put(ws, r, 7, "", SM)
r += 1
MEANS = [("Mean rating before cleaning", 3.287, 2.597, 2.181),
         ("Mean rating after cleaning", 3.161, 2.515, 2.154),
         ("Mean rating of removed material", 3.626, None, None)]
for lab, a, b, cc_ in MEANS:
    put(ws, r, 1, lab, N)
    put(ws, r, 2, a, BLUE_IN, '0.000')
    put(ws, r, 3, b, BLUE_IN, '0.000')
    put(ws, r, 4, cc_, BLUE_IN, '0.000')
    put(ws, r, 5, None, N); put(ws, r, 6, None, N)
    put(ws, r, 7, "Cleaning lowers the DNSE mean because the spam removed is rated more favourably than the genuine reviews left behind" if "removed" in lab else "", SM, wrap=True)
    r += 1

r += 1
ws.cell(r, 1, "DNSE ratings by year").font = Font(name=F, size=11, bold=True, color=ACCENT)
r += 1
head(ws, r, ["Year", "Retrieved", "Removed", "Removed, per cent", "Retained", "Mean, retained", "Generic, of retained"], 1)
hdr_y = r
r += 1
first_y = r
for row in RV.YEAR_TAB:
    y, raw_n, raw_mean, rem_n, rem_pct, cl_n, cl_mean, gen_n, gen_pct, sub_n, sub_mean = row
    fill = alt_fill if (r - first_y) % 2 == 0 else None
    put(ws, r, 1, y, B, fill=fill)
    put(ws, r, 2, raw_n, BLUE_IN, INT, fill)
    put(ws, r, 3, rem_n, BLUE_IN, INT, fill)
    put(ws, r, 4, f"=C{r}/B{r}*100", N, PCT1, fill)
    put(ws, r, 5, f"=B{r}-C{r}", N, INT, fill)
    put(ws, r, 6, cl_mean, BLUE_IN, '0.000', fill)
    put(ws, r, 7, gen_n, BLUE_IN, INT, fill)
    r += 1
last_y = r - 1
put(ws, r, 1, "Total", B)
for ci, col in ((2, "B"), (3, "C"), (5, "E"), (7, "G")):
    put(ws, r, ci, f"=SUM({col}{first_y}:{col}{last_y})", B, INT)
put(ws, r, 4, f"=C{r}/B{r}*100", B, PCT1)
put(ws, r, 6, 3.161, BLUE_IN, '0.000')
r += 2

ws.cell(r, 1, "DNSE substantive ratings by year").font = Font(name=F, size=11, bold=True, color=ACCENT)
r += 1
head(ws, r, ["Year", "Substantive reviews", "Mean rating", "Generic share of retained, per cent", "", "", "Reading"], 1)
r += 1
first_s = r
for row in RV.YEAR_TAB:
    y = row[0]
    fill = alt_fill if (r - first_s) % 2 == 0 else None
    put(ws, r, 1, y, B, fill=fill)
    put(ws, r, 2, row[9], BLUE_IN, INT, fill)
    put(ws, r, 3, row[10], BLUE_IN, '0.000', fill)
    put(ws, r, 4, row[8], BLUE_IN, PCT1, fill)
    put(ws, r, 5, None, N, fill=fill); put(ws, r, 6, None, N, fill=fill)
    note = ""
    if y == "2024": note = "Highest mean of any year, and also the highest share of one-word reviews"
    if y == "2025": note = "Substantive rating falls by 1.70 stars on a larger sample"
    put(ws, r, 7, note, SM, fill=fill, wrap=True)
    r += 1
r += 1

ws.cell(r, 1, "Complaint themes").font = Font(name=F, size=11, bold=True, color=ACCENT)
r += 1
head(ws, r, ["Theme", "One and two star", "Three star", "Four and five star", "All retained",
             "Share of negatives, per cent", "Definition"], 1)
r += 1
first_t = r
neg_total = 271
for th, negn, midn, posn, alln, pct in RV.THEME_TAB:
    fill = alt_fill if (r - first_t) % 2 == 0 else None
    put(ws, r, 1, th, B, fill=fill)
    put(ws, r, 2, negn, BLUE_IN, INT, fill)
    put(ws, r, 3, midn, BLUE_IN, INT, fill)
    put(ws, r, 4, posn, BLUE_IN, INT, fill)
    put(ws, r, 5, f"=B{r}+C{r}+D{r}", N, INT, fill)
    put(ws, r, 6, f"=B{r}/{neg_total}*100", N, PCT1, fill)
    put(ws, r, 7, RV.THEME_LABEL[th], SM, fill=fill, wrap=True)
    r += 1
put(ws, r, 1, "Reviews in each rating band", B)
put(ws, r, 2, 271, BLUE_IN, INT)
put(ws, r, 3, 31, BLUE_IN, INT)
put(ws, r, 4, 331, BLUE_IN, INT)
put(ws, r, 5, f"=B{r}+C{r}+D{r}", B, INT)
put(ws, r, 6, None, N)
put(ws, r, 7, "Themes are not exclusive, so the theme rows above sum to more than the band totals", SM, wrap=True)
r += 2

ws.cell(r, 1, "Three-application comparison").font = Font(name=F, size=11, bold=True, color=ACCENT)
r += 1
head(ws, r, ["Application", "Retrieved", "Retained", "Mean, retained", "Mean 2025", "Mean 2026", "One star share, per cent"], 1)
r += 1
first_pp = r
for row in RV.PEERS:
    app, pkg, raw_n, cl_n, rem, raw_m, cl_m, n24, m24, n25, m25, n26, m26, p1, p5 = row
    fill = alt_fill if (r - first_pp) % 2 == 0 else None
    put(ws, r, 1, app, B, fill=fill)
    put(ws, r, 2, raw_n, BLUE_IN, INT, fill)
    put(ws, r, 3, cl_n, BLUE_IN, INT, fill)
    put(ws, r, 4, cl_m, BLUE_IN, '0.000', fill)
    put(ws, r, 5, m25, BLUE_IN, '0.000', fill)
    put(ws, r, 6, m26, BLUE_IN, '0.000', fill)
    put(ws, r, 7, p1, BLUE_IN, PCT1, fill)
    r += 1

# ---------------------------------------------------------------- REVIEW QUOTES
ws = sheet("Review quotes",
           "Selected DNSE reviews",
           "Fifty reviews chosen as the most upvoted within each complaint theme, plus the most upvoted substantive "
           "positive reviews. Text is Vietnamese as written, truncated to 150 characters.",
           [12, 9, 13, 11, 26, 96])
hr = 4
head(ws, hr, ["Review id", "Stars", "Date", "Helpful votes", "Themes", "Text"], 1)
ws.freeze_panes = "A5"
r = hr + 1
for row in RV.QUOTES:
    fill = alt_fill if (r - hr) % 2 == 0 else None
    put(ws, r, 1, row[0], N, fill=fill)
    put(ws, r, 2, row[1], N, '0', fill)
    put(ws, r, 3, row[2], N, fill=fill)
    put(ws, r, 4, row[3], N, INT, fill)
    put(ws, r, 5, row[4], N, fill=fill, wrap=True)
    put(ws, r, 6, row[5], N, fill=fill, wrap=True)
    r += 1
ws.auto_filter.ref = f"A{hr}:F{r-1}"

# ---------------------------------------------------------------- SEGMENT MODEL
from importlib import import_module
_sm = import_module("04_segment_model")
INVESTABLE, DIGITAL, POP_SHARE, SEG_IDX = _sm.INVESTABLE, _sm.DIGITAL, _sm.POP_SHARE, _sm.IDX

ws = sheet("Segment model",
           "Deriving the priority customer segment",
           "Every index cell is a formula reading from the 'Segments 2024' sheet, so editing that sheet updates this one. "
           "Both indices are unweighted means, because any weighting chosen after seeing the data would be fitted to the result.",
           [28, 13, 13, 13, 13, 13, 13, 13, 14, 13, 44])

r = 4
ws.cell(r, 1, "Assumption").font = Font(name=F, size=11, bold=True, color=ACCENT)
r += 1
put(ws, r, 1, "Vietnamese adults aged 15 and over, millions", B, fill=YELLOW)
adults_cell = f"$B${r}"
put(ws, r, 2, 80.6, BLUE_IN, '0.0', YELLOW)
put(ws, r, 3, "General Statistics Office 2024 population structure applied to a population of 102 million", SM, wrap=True)
ws.merge_cells(start_row=r, start_column=3, end_row=r, end_column=11)
r += 2

ws.cell(r, 1, "Index definitions").font = Font(name=F, size=11, bold=True, color=ACCENT)
r += 1
head(ws, r, ["Index", "Indicator id", "Indicator", "", "", "", "", "", "", "", "Row on Segments 2024"], 2)
r += 1
first_def = r
for code in INVESTABLE + DIGITAL:
    label, theme, vals = SEG_IDX[code]
    fill = alt_fill if (r - first_def) % 2 == 0 else None
    put(ws, r, 1, "A investable surplus" if code in INVESTABLE else "B digital habit", N, fill=fill)
    put(ws, r, 2, code, N, fill=fill)
    put(ws, r, 3, label, N, fill=fill, wrap=True)
    ws.merge_cells(start_row=r, start_column=3, end_row=r, end_column=10)
    for cc in range(4, 11):
        ws.cell(r, cc).border = box
        if fill: ws.cell(r, cc).fill = fill
    put(ws, r, 11, seg_row_index[code], N, '0', fill)
    r += 1
r += 1

ws.cell(r, 1, "Segment scores").font = Font(name=F, size=11, bold=True, color=ACCENT)
r += 1
head(ws, r, ["Segment", "Index A investable", "Index B digital", "Composite",
             "Account, per cent", "Saved at an institution, per cent", "Activation gap, points",
             "Population share, per cent", "Unconverted adults, millions", "Priority score", "Reading"], 1)
ws.row_dimensions[r].height = 46
r += 1
first_seg = r

acc_row_src = seg_row_index["account.t.d"]
fi_row_src = seg_row_index["fin17a"]
READ = {
    "In labour force": "Highest priority score. Largest unconverted pool at a high propensity.",
    "Richest 60%": "Highest propensity on both indices. Second on priority score.",
    "Secondary educ or more": "Effectively tied with the richest 60 per cent.",
    "Young (15-24)": "Widest separation between digital habit and investable surplus, and the largest activation gap of any segment. Cheap to acquire and hard to fund.",
    "Poorest 40%": "Lowest propensity on both indices.",
    "All adults": "National benchmark, not a segment.",
}
for j, name in enumerate(SEGMENTS):
    col = get_column_letter(4 + j)
    fill = alt_fill if (r - first_seg) % 2 == 0 else None
    put(ws, r, 1, name, B, fill=fill)
    fa = ",".join([f"'Segments 2024'!{col}{seg_row_index[k]}" for k in INVESTABLE])
    fb = ",".join([f"'Segments 2024'!{col}{seg_row_index[k]}" for k in DIGITAL])
    put(ws, r, 2, f"=AVERAGE({fa})", GREEN_LK, PCT1, fill)
    put(ws, r, 3, f"=AVERAGE({fb})", GREEN_LK, PCT1, fill)
    put(ws, r, 4, f"=AVERAGE(B{r},C{r})", N, PCT1, fill)
    put(ws, r, 5, f"='Segments 2024'!{col}{acc_row_src}", GREEN_LK, PCT1, fill)
    put(ws, r, 6, f"='Segments 2024'!{col}{fi_row_src}", GREEN_LK, PCT1, fill)
    put(ws, r, 7, f"=E{r}-F{r}", N, PCT1, fill)
    put(ws, r, 8, POP_SHARE[name], BLUE_IN, PCT1, fill)
    put(ws, r, 9, f"={adults_cell}*H{r}/100*G{r}/100", N, '0.00', fill)
    put(ws, r, 10, f"=D{r}*I{r}/100", N, '0.00', fill)
    put(ws, r, 11, READ.get(name, ""), SM, fill=fill, wrap=True)
    r += 1
last_seg_model = r - 1
r += 1
put(ws, r, 1, "Spread, Index B less Index A", B)
put(ws, r, 2, f"=SUMPRODUCT(MAX(C{first_seg+1}:C{last_seg_model}-B{first_seg+1}:B{last_seg_model}))", N, PCT1)
put(ws, r, 3, "Array formula. The widest spread belongs to adults aged 15 to 24.", SM, wrap=True)
ws.merge_cells(start_row=r, start_column=3, end_row=r, end_column=11)

# ---------------------------------------------------------------- REORDER AND SAVE
order = ["Read me", "DNSE financials", "Market share", "Industry cross-section", "DNSE position",
         "Review analysis", "Review quotes", "Segment model", "Segments 2024", "Segment gaps",
         "National 2024", "Trends", "Vietnam reference", "Sources"]
wb._sheets = [wb[n] for n in order if n in wb.sheetnames] + \
             [s for s in wb._sheets if s.title not in order]
for s in wb._sheets:
    s.sheet_properties.tabColor = None

OUT = os.path.join(_HERE, 'FBA_Round2_DNSE_data_pack.xlsx')
wb.save(OUT)
print("saved", OUT, "sheets:", len(wb._sheets))

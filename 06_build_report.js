const fs = require('fs');
const path = require('path');
const {
  Document, Packer, Paragraph, TextRun, HeadingLevel, AlignmentType,
  Table, TableRow, TableCell, WidthType, ShadingType, BorderStyle,
  PageBreak, Footer, PageNumber, LevelFormat, ImageRun
} = require('docx');

const FONT = "Times New Roman";
const GREY = "3F3F3F";

// ---------------- data written by the pipeline ----------------
// Numbers produced by 03b (reviews) and 04 (segment model) are read here instead of
// being typed into the prose and tables, so a re-run cannot leave the text behind.
const SEG = require('./segment_model.json');
const RV = require('./reviews_tables.json');
const D = RV.DNSE_TOTALS;
const f1 = x => x.toFixed(1), f2 = x => x.toFixed(2);
const int = x => x.toLocaleString('en-US');
const pct = (a, b) => (a / b * 100).toFixed(1);
const MONTHS = ["January", "February", "March", "April", "May", "June", "July", "August",
                "September", "October", "November", "December"];
const DATE = iso => { const [y, m, d] = iso.split('-'); return `${+d} ${MONTHS[+m - 1]} ${y}`; };
const yr = y => RV.YEAR_TAB.find(r => r[0] === y);
const gen = y => RV.GENERIC_SENSITIVITY.find(r => r[0] === y);
const theme = t => RV.THEME_TAB.find(r => r[0] === t);
const peer = name => RV.PEERS.find(r => r[0].startsWith(name));
const clog = name => RV.CLEANING_LOG.find(r => r[0].startsWith(name));
const seg = name => SEG.rows.find(r => r.segment === name);
const rank = k => SEG.rows.find(r => r.priority_rank === k);
const SEGNAME = {
  "Richest 60%": "Richest 60 per cent", "Poorest 40%": "Poorest 40 per cent",
  "Secondary educ or more": "Secondary education or more",
  "Primary educ or less": "Primary education or less",
  "Older (25+)": "Aged 25 and over", "Young (15-24)": "Aged 15 to 24"
};
const segName = s => SEGNAME[s] || s;
const bMinusA = r => r.index_b_digital - r.index_a_investable;
const VPS = peer("VPS"), FPTS = peer("FPTS"), DN = peer("DNSE");
// App Store cross-check (02c, 03b)
const iosLog = name => RV.IOS_CLEANING_LOG.find(r => r[0].startsWith(name));
const store = name => RV.STORE_COMPARE.find(r => r[0].startsWith(name));
const SG = RV.STORE_GROUPS;
const IOS_N = RV.IOS_CLEANING_LOG.reduce((t, r) => t + r[1], 0);

// DNSE's filed statements, pulled by 01b. Costs are negative, as filed.
const FS = require('./dnse_financials.json');
const FQ = FS.quarterly, FH = FS.half_year, FYR = FS.annual, FD = FS.derived;
const Q1 = FQ["2026Q1"], Q2 = FQ["2026Q2"], Q4 = FQ["2025Q4"], HY = FH["2026H1"], FY25 = FYR["FY2025"];
const TOTAL_REV = HY.revenue + HY.financial_income;
// 2026 plan, Proposal 05/2026 approved by AGM Resolution 01/2026. Its revenue is total revenue, including financial income.
const TARGET_REV = 1736, TARGET_PBT = 550;
// DNSE annual report 2025, pages 29 and 30.
const AR25 = { accounts: 1512920, active_dec: 85739, nav10m: 27100 };
const f0 = x => Math.round(x).toString();
const money = x => x.toLocaleString('en-US', { minimumFractionDigits: 1, maximumFractionDigits: 1 });
const whole = x => Math.round(x).toLocaleString('en-US');
const growth = (a, b) => (a / b - 1) * 100;
const margin = d => d.pbt / d.revenue * 100;
const share = k => HY[k] / HY.revenue * 100;
const fvtplNet = d => d.rev_fvtpl + d.cost_fvtpl;
const debt = d => d.short_term_borrowing + (d.bonds_short || 0) + (d.bonds_long || 0);
const QLIST = Object.keys(FQ);
const BROKE_RUN = QLIST.length - QLIST.findIndex((p, i) => QLIST.slice(i).every(q => (FD[q].brokerage_net ?? 0) < 0));
const OPEX_Q1 = growth(Q1.operating_cost, FQ["2025Q1"].operating_cost);
// Same basis as the workbook's derived measures: average of the end-2025, Q1 and Q2 balances, annualised.
const YIELD = HY.rev_lending / ((FY25.loans + Q1.loans + Q2.loans) / 3) * 2 * 100;
const FUND = (-(HY.interest_expense + HY.cost_provision_and_loan_funding) - (FY25.loan_allowance - Q2.loan_allowance))
  / ((debt(FY25) + debt(Q1) + debt(Q2)) / 3) * 2 * 100;
const GROSS_GAIN = 1000 * YIELD / 100, NET_GAIN = 1000 * (YIELD - FUND) / 100;
const L2E = Q2.loans / Q2.equity * 100;
const BS_SHARE = share("rev_lending") + share("rev_htm") + share("rev_fvtpl");
// Peer brokers' filings, pulled by 01c: the firms named in the report, VPS (HOSE: VCK) included.
const PANEL = require('./peer_financials.json');
const PEER = Object.fromEntries(Object.entries(PANEL.firms).filter(([, d]) => d.focus));
const peerQ2 = n => PEER[n].quarterly["2026Q2"];
const PEERS = Object.keys(PEER);
// Exchange announcements, VSDC and daily market value, read by 01d.
const MM = require('./market_macro.json');
const HOSE_T = MM.hose_market_share.tables, HNX_T = MM.hnx_market_share.tables;
const topTen = rows => rows.filter(r => r[0] <= 10).reduce((t, r) => t + r[2], 0);
const HOSE_TOP_Q2 = topTen(HOSE_T["2026Q2"]), HOSE_TOP_Q1 = topTen(HOSE_T["2026Q1"]);
const HOSE_TENTH = HOSE_T["2026Q2"][9][2];
const dnseIn = rows => (rows.find(r => /DNSE/.test(r[1])) || [])[2];
const DNSE_HNX = dnseIn(HNX_T.listed["2026Q2"]), DNSE_DER = dnseIn(HNX_T.derivatives["2026Q2"]);
const INDUSTRY_LENDING = 453800;   // VND bn, Vietstock compilation; the one industry figure not in any filing
const LEND_SHARE = Q2.loans / INDUSTRY_LENDING * 100;
const ACCOUNTS = MM.vsdc_latest.investor_trading_accounts, ACC_DATE = MM.vsdc_latest.date;
const ACC_SHARE = 1.7e6 / ACCOUNTS * 100;
const avgValue = (sym, from, to) => {
  const v = MM.prices[sym].daily.filter(r => r[0] >= from && r[0] <= to && r[3]).map(r => r[3]);
  return v.reduce((a, b) => a + b, 0) / v.length;
};
const FUT_Q2 = avgValue("VN30F1M", "2026-04-01", "2026-06-30"), HOSE_Q2 = avgValue("VNINDEX", "2026-04-01", "2026-06-30");
const shortName = s => [["Kỹ Thương", "TCBS"], ["VPBank", "VPBankS"], ["VNDIRECT", "VNDirect"], ["Thành phố Hồ Chí Minh", "HSC"],
  ["Mirae", "Mirae Asset Vietnam"], ["KIS", "KIS Vietnam"], ["BIDV", "BSC"], ["Phú Hưng", "PHS"], ["FPT", "FPTS"],
  ["Ngoại thương", "VCBS"], ["DNSE", "DNSE"], ["Vietcap", "Vietcap"], ["VIX", "VIX"], ["SSI", "SSI"], ["VPS", "VPS"],
  ["khoán MB", "MBS"]].find(([k]) => s.toLowerCase().includes(k.toLowerCase()))?.[1] ?? s;
const TOP = PEERS.reduce((a, n) => peerQ2(n).pbt > peerQ2(a).pbt ? n : a);
const BOTTOM = PEERS.reduce((a, n) => peerQ2(n).pbt < peerQ2(a).pbt ? n : a);
const NUMWORD = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve"];
const ORDWORD = ["", "first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth", "ninth", "tenth", "eleventh", "twelfth"];
const PBT_RANK = 1 + PEERS.filter(n => peerQ2(n).pbt > Q2.pbt).length;
const PBT_FIRMS = PEERS.length + 1;
if (!(fvtplNet(Q4) < 0 && fvtplNet(Q1) < 0)) {
  throw new Error("Trading assets no longer lost money in Q4 2025 and Q1 2026. Rewrite Section 4.4 and Table 4.");
}

// ---------------- word counter ----------------
let BODY = false;
let WORDS = 0;
function count(t) { if (BODY && typeof t === 'string') WORDS += t.trim().split(/\s+/).filter(Boolean).length; }

// ---------------- helpers ----------------
function H1(t) {
  count(t);
  return new Paragraph({
    heading: HeadingLevel.HEADING_1, spacing: { before: 340, after: 160 },
    children: [new TextRun({ text: t, bold: true, size: 30, font: FONT, color: "000000" })]
  });
}
function H2(t) {
  count(t);
  return new Paragraph({
    heading: HeadingLevel.HEADING_2, spacing: { before: 260, after: 120 },
    children: [new TextRun({ text: t, bold: true, size: 25, font: FONT, color: "000000" })]
  });
}
function P(t, o = {}) {
  count(t);
  return new Paragraph({
    spacing: { after: o.after === undefined ? 160 : o.after, line: 300 },
    alignment: o.align || AlignmentType.JUSTIFIED,
    indent: o.indent,
    children: [new TextRun({
      text: t, size: o.size || 23, font: FONT,
      italics: o.italics, bold: o.bold, color: "000000"
    })]
  });
}
function Bullet(t) {
  count(t);
  return new Paragraph({
    numbering: { reference: "b", level: 0 },
    spacing: { after: 90, line: 300 },
    children: [new TextRun({ text: t, size: 23, font: FONT, color: "000000" })]
  });
}
function Num(t) {
  count(t);
  return new Paragraph({
    numbering: { reference: "n", level: 0 },
    spacing: { after: 90, line: 300 },
    children: [new TextRun({ text: t, size: 23, font: FONT, color: "000000" })]
  });
}
function Spacer(h = 120) {
  return new Paragraph({ spacing: { after: h }, children: [new TextRun({ text: "", size: 10 })] });
}
function cell(text, w, o = {}) {
  const lines = Array.isArray(text) ? text : [text];
  return new TableCell({
    width: { size: w, type: WidthType.DXA },
    shading: o.fill ? { type: ShadingType.CLEAR, fill: o.fill, color: "auto" } : undefined,
    margins: { top: 70, bottom: 70, left: 100, right: 100 },
    verticalAlign: "center",
    children: lines.map(l => new Paragraph({
      spacing: { after: 0, line: 260 },
      alignment: o.align || AlignmentType.LEFT,
      children: [new TextRun({ text: String(l), size: o.size || 20, font: FONT, bold: o.bold, color: "000000" })]
    }))
  });
}
function T(widths, header, rows, o = {}) {
  const trs = [];
  if (header) trs.push(new TableRow({
    tableHeader: true,
    children: header.map((h, i) => cell(h, widths[i], {
      bold: true, fill: "E8E8E8", size: o.hs || 20,
      align: (o.numCols && o.numCols.includes(i)) ? AlignmentType.RIGHT : AlignmentType.LEFT
    }))
  }));
  rows.forEach(r => trs.push(new TableRow({
    children: r.map((cv, i) => cell(cv, widths[i], {
      size: o.bs || 20,
      bold: o.boldFirst && i === 0,
      align: (o.numCols && o.numCols.includes(i)) ? AlignmentType.RIGHT : AlignmentType.LEFT
    }))
  })));
  return new Table({
    columnWidths: widths,
    width: { size: widths.reduce((a, b) => a + b, 0), type: WidthType.DXA },
    borders: {
      top: { style: BorderStyle.SINGLE, size: 6, color: "000000" },
      bottom: { style: BorderStyle.SINGLE, size: 6, color: "000000" },
      left: { style: BorderStyle.NONE }, right: { style: BorderStyle.NONE },
      insideHorizontal: { style: BorderStyle.SINGLE, size: 2, color: "B0B0B0" },
      insideVertical: { style: BorderStyle.NONE }
    },
    rows: trs
  });
}
function Fig(file, widthPx) {
  // Height follows the PNG's own aspect ratio. A PNG stores its width and height as
  // big-endian integers at bytes 16 to 23. bbox_inches="tight" changes both, so a
  // typed-in height stretched some figures by up to a fifth.
  const data = fs.readFileSync(path.join(__dirname, 'fig', file + '.png'));
  const w = data.readUInt32BE(16), h = data.readUInt32BE(20);
  return new Paragraph({
    alignment: AlignmentType.CENTER,
    spacing: { before: 120, after: 60 },
    children: [new ImageRun({
      type: "png", data,
      transformation: { width: widthPx, height: Math.round(widthPx * h / w) }
    })]
  });
}
function Cap(t) {
  return new Paragraph({
    alignment: AlignmentType.LEFT, spacing: { after: 200 },
    children: [new TextRun({ text: t, size: 19, font: FONT, italics: true, color: GREY })]
  });
}
function TabCap(t) {
  return new Paragraph({
    alignment: AlignmentType.LEFT, spacing: { before: 90, after: 200 },
    children: [new TextRun({ text: t, size: 19, font: FONT, italics: true, color: GREY })]
  });
}
function Ctr(t, size, bold, after) {
  return new Paragraph({
    alignment: AlignmentType.CENTER, spacing: { after: after === undefined ? 120 : after },
    children: [new TextRun({ text: t, size: size || 22, font: FONT, bold: bold, color: "000000" })]
  });
}

// Output of 04_segment_model.py (segment_model.json): the national row, then every
// segment in priority order, composite index times unconverted pool.
const SEGRANKED = SEG.rows.filter(r => r.priority_rank).sort((a, b) => a.priority_rank - b.priority_rank);
const SEGROWS = [seg("All adults")].concat(SEGRANKED).map(r => [
  segName(r.segment), f1(r.index_a_investable), f1(r.index_b_digital), f1(r.composite),
  f1(r.account_pct), f1(r.saved_at_fi_pct), f1(r.activation_gap_pp), f2(r.unactivated_adults_m)
]);
const TOP3 = [1, 2, 3].map(rank);
// The prose in Sections 4.2 and 6 names the priority group as the overlap of these three
// segments. Stop rather than print a paragraph the model no longer supports.
const PROSE = {
  "Secondary educ or more": "adults with secondary education or more",
  "In labour force": "adults in the labour force",
  "Richest 60%": "the upper 60 per cent of the income distribution"
};
if (TOP3.map(r => r.segment).join("|") !== Object.keys(PROSE).join("|")) {
  throw new Error("Top three segments changed: " + TOP3.map(r => r.segment).join(", ") +
                  ". Rewrite Section 4.2 and the executive summary before rebuilding.");
}
const YOUNG = seg("Young (15-24)");
const NEXT_SPREAD = SEGRANKED.filter(r => r !== YOUNG).map(bMinusA).sort((a, b) => b - a)[0];
// Spearman rank correlation of the two indices across segments other than the young
const RHO = (() => {
  const rows = SEGRANKED.filter(r => r !== YOUNG);
  const rk = k => { const v = rows.map(r => r[k]); const s = [...v].sort((a, b) => b - a);
                    return v.map(x => s.indexOf(x) + 1); };
  const a = rk("index_a_investable"), b = rk("index_b_digital"), n = rows.length;
  return 1 - 6 * a.reduce((t, x, i) => t + (x - b[i]) ** 2, 0) / (n * (n * n - 1));
})();

const c = [];

// ======================================================= TITLE PAGE
c.push(Spacer(1500));
c.push(Ctr("FUTURE BUSINESS ANALYST SEASON 6", 22, false, 110));
c.push(Ctr("ROUND 2 BUSINESS ANALYTICS REPORT", 22, false, 340));
c.push(Ctr("Acquisition without activation", 44, true, 170));
c.push(Ctr("Why DNSE Securities holds a quarter of Vietnam's derivatives market, "
  + "one eighth of its securities accounts and under three per cent of its cash equity trading", 24, false, 420));
c.push(new Paragraph({
  alignment: AlignmentType.CENTER, spacing: { after: 100 },
  border: { top: { style: BorderStyle.SINGLE, size: 8, color: "000000" } },
  children: [new TextRun({ text: "", size: 6 })]
}));
c.push(Ctr("Selected organisation: DNSE Securities Joint Stock Company (HOSE: DSE)", 22, false, 80));
c.push(Ctr("Category: wealthtech and technology-enabled financial institutions", 22, false, 80));
c.push(Ctr("21 September 2026", 22, false, 0));
c.push(new Paragraph({ children: [new PageBreak()] }));

// ======================================================= EXECUTIVE SUMMARY
c.push(H1("Executive summary"));
c.push(P("DNSE Securities removed the price of trading. It was the first Vietnamese securities company to offer commission-free trading for life, and acquisition followed. By the middle of 2026 it served more than 1.7 million customers, roughly one eighth of all securities accounts in Vietnam, and it held 25.38 per cent of derivatives brokerage on the Hanoi Stock Exchange, second only to VPS."));
c.push(P(`Activity has not followed acquisition. In the same quarter DNSE intermediated ${f2(DNSE_HNX)} per cent of listed share trading on the Hanoi exchange and did not appear in the top ten on the larger Ho Chi Minh exchange, where tenth place required ${f2(HOSE_TENTH)} per cent. Its lending book of VND ${whole(Q2.loans)} billion was ${f2(LEND_SHARE)} per cent of the industry total.` + " Setting account share against trading share, an average DNSE account generates about a quarter of the cash equity trading value of an average market account."));
c.push(P(`The income statement shows what that costs. Operating revenue rose ${f1(growth(HY.revenue, FH["2025H1"].revenue))} per cent year on year in the first half of 2026 while the pre-tax profit margin fell from ${f1(margin(FY25))} per cent across 2025 to ${f1(margin(HY))} per cent in the half year. Direct brokerage costs have exceeded brokerage commissions in each of the last ${BROKE_RUN} quarters, and operating expenses rose ${f0(OPEX_Q1)} per cent in the first quarter of 2026. At the half-year the firm had delivered ${f1(TOTAL_REV / TARGET_REV * 100)} per cent of its total revenue target and ${f1(HY.pbt / TARGET_PBT * 100)} per cent of its profit target.`));
c.push(P(`This report draws on company disclosures, exchange market share reports, World Bank Global Findex 2024 segment data for Vietnam and ${int(D.raw_n)} Google Play reviews of DNSE, with ${int(VPS[2] + FPTS[2])} reviews of two competitor applications, collected and cleaned for this study. The review evidence locates the friction. Among ${D.negative_1_2} cleaned negative reviews, ${f1(theme("stability")[5])} per cent concern crashes and login failures and ${f1(theme("onboarding")[5])} per cent concern account opening. A further ${f1(theme("fraud")[5])} per cent accuse the firm of deception.` + " Around a third of those name a cause, most often a sign-up bonus that requires a VND 2 million deposit or an account closure fee of VND 100,000; the rest are one-line accusations."));
c.push(P(`Scoring the Findex segment matrix produces the priority customer group rather than assuming it. Adults with secondary education or more, adults in the labour force and the upper 60 per cent of the income distribution rank first, second and third, and the priority group is where they overlap: employed, secondary-educated adults in the upper income group. These segments combine a high propensity to hold investable balances with the largest unconverted pools, between ${f1(Math.min(...TOP3.map(r => r.unactivated_adults_m)))} and ${f1(Math.max(...TOP3.map(r => r.unactivated_adults_m)))} million adults each who hold an account and do not save through a financial institution.` + " The segment with the widest gap between digital habit and accumulated surplus is adults aged 15 to 24, which is the group a free application acquires most cheaply and monetises least."));
c.push(P("The priority problem is revenue per account. The recommendation is a cash management and fund distribution layer that converts idle balances into funded, yield-bearing accounts, priced against bank deposit rates near 7 per cent. Higher assets per account expand the collateral base for margin lending, which is already the firm's largest revenue line. The 2026 annual general meeting approved a VND 3,500 billion bond programme that funds it and, for the second year running, the acquisition of a fund management company that the board has not yet completed; closing it, or a distribution partner in the meantime, is the first step. Round 3 should test willingness to pay, the activation sequence and the effect on lending balances."));
c.push(new Paragraph({ children: [new PageBreak()] }));

// ======================================================= CONTENTS
c.push(H1("Contents"));
const toc = [
  ["1.", "Introduction and business context", ["1.1 The organisation", "1.2 The business area under investigation", "1.3 The question this report answers"]],
  ["2.", "Data and analytical method", ["2.1 Data collected", "2.2 Preparation and quality control", "2.3 Analytical method"]],
  ["3.", "Findings from the data", ["3.1 Acquisition is working", "3.2 Conversion is not", "3.3 What customers say about the product", "3.4 What the gap costs"]],
  ["4.", "Discussion and main analysis", ["4.1 Why the gap exists", "4.2 Where the money actually sits", "4.3 Market and macroeconomic conditions", "4.4 Prioritising the problem"]],
  ["5.", "Strategic alternatives", []],
  ["6.", "Preliminary recommendation", []],
  ["7.", "Validation direction", []],
  ["8.", "Conclusion", []],
  ["", "Appendix A. Data tables", []],
  ["", "Appendix B. Method, assumptions and limitations", []],
  ["", "References", []]
];
toc.forEach(([n, t, subs]) => {
  c.push(new Paragraph({
    spacing: { before: 130, after: 30 },
    children: [new TextRun({ text: (n ? n + "  " : "") + t, bold: true, size: 23, font: FONT, color: "000000" })]
  }));
  subs.forEach(s => c.push(new Paragraph({
    spacing: { after: 20 }, indent: { left: 420 },
    children: [new TextRun({ text: s, size: 21, font: FONT, color: "000000" })]
  })));
});
c.push(new Paragraph({ children: [new PageBreak()] }));

// ======================================================= BODY STARTS
BODY = true;

// ---------------------------------------- 1. INTRODUCTION
c.push(H1("1. Introduction and business context"));

c.push(H2("1.1 The organisation"));
c.push(P("DNSE Securities Joint Stock Company is a Vietnamese securities firm listed on the Ho Chi Minh Stock Exchange under the code DSE. Its 2024 listing was the only initial public offering on the Vietnamese market that year." + ` Charter capital stands at VND ${money(Q2.charter_capital)} billion and total assets reached VND ${whole(FY25.total_assets)} billion at the end of 2025.`));
c.push(P("The firm distributes entirely through its Entrade X platform and operates without a branch network. It became the first Vietnamese securities company to offer lifetime commission-free trading, so order execution is free and revenue comes from margin lending, advances against sale proceeds, custody and proprietary investment. In December 2022 it launched Vietnam's first per-position margin system, which manages leverage on an individual position rather than across the whole account. From May 2025 it has absorbed derivatives margin management fees on behalf of customers."));

c.push(P(`The market DNSE competes in is crowded and fragmenting. The ten largest firms accounted for ${f2(HOSE_TOP_Q2)} per cent of trading on the Ho Chi Minh exchange in the second quarter of 2026, down from ${f2(HOSE_TOP_Q1)} per cent three months earlier.` + " Almost four percentage points of share moved to smaller firms in one quarter. Industry profit comes mainly from lending rather than from commissions, with VND 453,800 billion outstanding at the end of June 2026 against a regulatory cap of 200 per cent of equity. " + `Pre-tax profit in that quarter ranged from VND ${whole(peerQ2(TOP).pbt)} billion at ${TOP} to VND ${money(peerQ2(BOTTOM).pbt)} billion at ${BOTTOM}, and DNSE's VND ${money(Q2.pbt)} billion ranked ${ORDWORD[PBT_RANK]} of ${NUMWORD[PBT_FIRMS]}, which shows the scale difference between DNSE and the firms whose accounts it is winning.`));
c.push(Fig("fig11_peer_profit", 530));
c.push(Cap(`Figure 1. Pre-tax profit of Vietnamese securities firms, second quarter of 2026, from each firm's filed statements. DNSE ranks second in derivatives brokerage and ${ORDWORD[PBT_RANK]} of these ${NUMWORD[PBT_FIRMS]} firms by earnings.`));

c.push(H2("1.2 The business area under investigation"));
c.push(P("This report examines how DNSE converts customer acquisition into revenue. Because execution is free, account numbers measure reach rather than income. Revenue arises only when a customer funds the account, holds assets and borrows against them, so the commercial question is how many of the 1.7 million accounts reach that state."));

c.push(H2("1.3 The question this report answers"));
c.push(P("Three readings of DNSE's position were tested against the evidence. The first treats the firm as undersized and argues for more acquisition. The second treats derivatives concentration as the core risk. The third treats low revenue per account as the binding constraint. Sections 3 and 4 show that the third fits the data, and Section 4.4 sets out the ranking criteria."));

// ---------------------------------------- 2. DATA AND METHOD
c.push(H1("2. Data and analytical method"));

c.push(H2("2.1 Data collected"));
c.push(P("Five datasets were assembled. Four are secondary and published. One is primary and was collected for this study."));
c.push(T([2500, 3300, 3220],
  ["Dataset", "Content", "Source and period"],
  [
    ["Company financials", "Every line of the income statement, balance sheet, cash flow and notes; accounts and plan targets", `DNSE filed statements, Q1 2018 to Q2 2026, retrieved from Vietcap's data service ${DATE(FS.pulled)}; annual report 2025; 2026 AGM resolution and proposals`],
    ["Exchange market share", "Brokerage share on HOSE, HNX, UPCoM and derivatives for every firm in the top ten", "HOSE and HNX quarterly announcements read from the exchanges' sites, 2018 to Q2 2026"],
    ["Industry cross-section", "Lending balances, pre-tax profit and brokerage results for the largest securities firms", `Filed statements of all ${PANEL.totals["2026Q2"].firms_reporting_loans} brokers with filings on Vietcap's data service, VPS included, 2018 to Q2 2026; only the industry lending total is a press compilation`],
    ["Financial inclusion", "51 Findex indicators for Vietnam across 13 demographic segments, plus five survey waves from 2011 to 2024", "World Bank Global Findex, open data interface source 28, retrieved 20 September 2026"],
    ["Customer reviews", `${int(D.raw_n)} DNSE reviews and ${int(VPS[2] + FPTS[2])} competitor reviews on Google Play, and ${int(IOS_N)} App Store reviews of the same three applications, with rating, date, text and helpfulness votes`, `Google Play and Vietnamese App Store public listings, pulled ${DATE(D.pulled)} and ${DATE(RV.APPSTORE_PULLED)}, reviews to ${DATE(RV.CUTOFF)}`]
  ],
  { bs: 18, hs: 18 }));
c.push(TabCap("Table 1. Evidence base. Full source addresses are listed in Appendix A."));

c.push(H2("2.2 Preparation and quality control"));
c.push(P("Financial figures were taken from primary disclosures rather than press summaries wherever both existed. Where the two disagreed, the disclosure was used and the discrepancy recorded. Industry lending illustrates the point. Press coverage of the second quarter of 2026 reports three different industry totals, namely VND 435,000 billion, VND 445,000 billion and VND 453,800 billion. The three measure different things, since the largest includes advances against sale proceeds alongside margin loans. This report uses VND 453,800 billion throughout and states the basis wherever a share is calculated from it."));
c.push(P("Market share figures are defined by each exchange as a share of traded value on that exchange alone. Shares from different exchanges are therefore never compared with one another in this report, and each figure carries the name of the market it belongs to."));
c.push(P("The review dataset required the most work. Vietnamese application stores carry heavy comment spam from unlicensed lending sites, and much of it disguises itself using mathematical alphanumeric Unicode characters that defeat plain keyword filters. Every review text was normalised to a comparable form before filtering, using Unicode compatibility composition followed by removal of diacritics and conversion to lower case. Two regular expression rules then flagged loan advertising and referral code farming, the second only where a referral phrase sits next to a code or a reward amount, so that genuine complaints about one-time passwords are not caught. Copy-paste duplicates of longer texts were removed, while identical short reviews written by different people were kept. The identical rule was applied to all three applications so that the comparison in Figure 6 is like for like. The same rule was applied to written reviews from the Vietnamese App Store, whose public feed serves recent reviews only, as a cross-check for 2025 and 2026."));
const CL = ["DNSE", "VPS", "FPTS"].map(clog);
const cleanNum = (i, d) => CL.map(r => d ? (r[i] === null ? "" : r[i].toFixed(d)) : int(r[i]));
c.push(T([2900, 1450, 1450, 1450, 1770],
  ["Stage", "DNSE", "VPS", "FPTS", "Note"],
  [
    ["Reviews retrieved"].concat(cleanNum(1), [`Full available history except VPS, its ${int(VPS[2])} most recent`]),
    ["Loan advertising removed"].concat(cleanNum(2), [`${pct(D.loan_spam, D.raw_n)} per cent of the DNSE pull`]),
    ["Referral farming removed"].concat(cleanNum(3), [`${pct(D.referral_spam, D.raw_n)} per cent of the DNSE pull`]),
    ["Duplicates removed"].concat(cleanNum(4), ["Copy-paste text of 20 or more characters"]),
    ["Reviews retained"].concat(cleanNum(5), [CL.map(r => pct(r[1] - r[5], r[1])).join(", ") + " per cent removed"]),
    ["Mean rating before cleaning"].concat(cleanNum(6, 3), [""]),
    ["Mean rating after cleaning"].concat(cleanNum(7, 3), [`Removed DNSE material rated ${D.removed_mean.toFixed(3)} on average`])
  ],
  { bs: 18, hs: 18, numCols: [1, 2, 3] }));
c.push(TabCap("Table 2. Review cleaning log. Cleaning lowers the DNSE mean because the spam it removes is rated more favourably than the genuine reviews it leaves behind."));
c.push(P(`Cleaning changed the conclusion. In 2022 and 2023, ${f1(yr("2022")[4])} and ${f1(yr("2023")[4])} per cent of all DNSE reviews were spam,` + " so an uncleaned reading of those years would have measured the spam rather than the customers. The cleaned series in Figure 4 is a different shape from the raw one."));

c.push(H2("2.3 Analytical method"));
c.push(P("Three methods were used. Share comparison places the same firm against several denominators, which isolates the point in the customer journey where performance changes. Thematic coding assigns each cleaned review one or more non-exclusive labels through keyword matching on the normalised text, and one-word reviews carrying no label are counted separately as generic so that they do not inflate a favourable reading. Index construction converts the Findex segment matrix into two scores, each comparable across segments, described in Section 4.2, using unweighted means so that no weighting choice is fitted to the result."));

// ---------------------------------------- 3. FINDINGS
c.push(H1("3. Findings from the data"));

c.push(H2("3.1 Acquisition is working"));
c.push(P("DNSE has grown its customer base faster than any competitor. It opened more than 120,000 accounts in the first quarter of 2024, equal to 30 per cent of all new accounts in the market. In 2025 it took 20 per cent of new openings and closed the year with 1.5 million accounts. It opened 142,000 accounts in the first quarter of 2026, an 18 per cent share, and passed 1.7 million customers by mid-year."));
c.push(P("Derivatives followed the same path. DNSE reached 4.01 per cent of derivatives brokerage in the first quarter of 2024 and 25.38 per cent by the second quarter of 2026, ranking second for seven consecutive quarters while the leader VPS fell to 33.84 per cent."));
c.push(Fig("fig1_derivatives_share", 555));
c.push(Cap("Figure 2. DNSE derivatives brokerage market share by quarter since it entered the top ten, from the Hanoi Stock Exchange's quarterly announcements."));

c.push(H2("3.2 Conversion is not"));
c.push(P(`The same firm looks very different once activity replaces registration as the measure. In the second quarter of 2026 DNSE intermediated ${f2(DNSE_HNX)} per cent of listed share trading on the Hanoi exchange, ranking eighth of ten. It did not enter the top ten on the Ho Chi Minh exchange, where tenth place required ${f2(HOSE_TENTH)} per cent. Its margin loan and advance balance of VND ${whole(Q2.loans)} billion, a record for the firm, was ${f2(LEND_SHARE)} per cent of the VND 453,800 billion lent across the industry.`));
c.push(Fig("fig2_monetisation_gap", 555));
c.push(Cap("Figure 3. DNSE share of the Vietnamese market on five measures, second quarter of 2026. Each percentage is a share of its own market, and the five denominators differ."));
c.push(P(`Dividing trading share by account share gives the relative intensity of an average account. DNSE holds ${f2(ACC_SHARE)} per cent of the ${f2(ACCOUNTS / 1e6)} million securities accounts in the market and produces ${f2(DNSE_HNX)} per cent of Hanoi listed share trading. An average DNSE account therefore trades at about ${f1(DNSE_HNX / ACC_SHARE * 100)} per cent of the value of an average market account. Both sides of that ratio count accounts rather than people, and one investor may hold accounts at several firms. The Ho Chi Minh exchange gives only an upper bound, because DNSE is outside its top ten: ${f1(HOSE_TENTH / ACC_SHARE * 100)} per cent at most. Lending shows the same pattern more sharply, at ${f2(LEND_SHARE)} per cent of industry balances against ${f2(ACC_SHARE)} per cent of accounts.` + ` The company's own figures confirm the reading: of ${int(AR25.accounts)} accounts at the end of 2025, ${int(AR25.active_dec)} customers used any product in December and ${int(AR25.nav10m)} held net assets of VND 10 million or more, ${f1(AR25.active_dec / AR25.accounts * 100)} and ${f1(AR25.nav10m / AR25.accounts * 100)} per cent.`));

c.push(H2("3.3 What customers say about the product"));
c.push(P(`Rating data explains part of the gap. After cleaning, DNSE averages ${f2(D.clean_mean)} stars across ${int(D.clean_n)} reviews, ahead of VPS at ${f2(VPS[6])} and FPTS at ${f2(FPTS[6])}, so the product compares well against its closest competitors. The direction of travel is the concern. Substantive reviews, meaning cleaned reviews that carry a content theme rather than a single word of praise, averaged ${f2(yr("2024")[10])} stars in 2024 and ${f2(yr("2025")[10])} in 2025.`));
c.push(Fig("fig7_review_rating_by_year", 545));
c.push(Cap(`Figure 4. Mean rating of substantive DNSE reviews by year, after spam removal; 2020, with three reviews, is omitted. The 2024 figure also rests on the year with the highest share of one-word reviews, at ${f1(yr("2024")[8])} per cent of cleaned reviews against ${f1(yr("2025")[8])} per cent in 2025. The fall does not depend on that cut-off: treating reviews of up to four words as generic, the substantive mean still falls from ${f2(gen("2024")[7])} to ${f2(gen("2025")[7])}.`));
c.push(P(`The themes show where the friction sits. Among ${D.negative_1_2} cleaned one and two star reviews, crashes and login failures account for ${f1(theme("stability")[5])} per cent and account opening for ${f1(theme("onboarding")[5])} per cent. Accusations of deception account for ${f1(theme("fraud")[5])} per cent,` + " and reading those reviews identifies two specific triggers. A sign-up promotion advertised as VND 100,000 requires a deposit of VND 2 million, and closing an account costs VND 100,000. Both appear repeatedly among the most upvoted reviews of 2025."));
c.push(Fig("fig8_negative_themes", 560));
c.push(Cap(`Figure 5. Themes in the ${D.negative_1_2} cleaned one and two star DNSE reviews.` + " Themes are not exclusive, so a review may appear in more than one row."));
c.push(P("Two further readings matter. Complaints about account opening concentrate in 2021, 2022 and 2025, and complaints about stability concentrate in 2023 and 2026, which indicates recurring rather than resolved problems. Separately, the feature customers praise without prompting is the automatic earning of idle cash, described in Vietnamese as the account that does not sleep. That feature already does at a small scale what Section 6 recommends doing deliberately."));
c.push(Fig("fig9_peer_ratings", 520));
c.push(Cap(`Figure 6. Mean ratings of three Vietnamese broker applications under the identical cleaning rule. DNSE leads across all reviews pulled. For 2026 alone the means are ${f2(DN[12])} for DNSE, ${f2(VPS[12])} for VPS and ${f2(FPTS[12])} for FPTS, the last on ${FPTS[11]} reviews.`));
{
  const d = store("DNSE"), f = store("FPTS");
  const vsFpts = d[5] < f[5] ? "slightly below FPTS" : "above FPTS";
  c.push(P(`The App Store, whose iPhone users sit closer to the upper-income segment prioritised in Section 4.2, gives a cross-check for 2025 and 2026 (Appendix A6). Its reviewers rate DNSE lower, at ${f2(d[5])} stars against ${f2(d[2])} on Google Play, and ${vsFpts}. They complain about the product rather than the promotion: crashes, login and account opening appear in ${Math.round(SG.product[3])} per cent of negative reviews against ${Math.round(SG.product[1])} per cent on Google Play, deception and bonus terms in ${Math.round(SG.promotion[3])} against ${Math.round(SG.promotion[1])} per cent.`));
}

c.push(H2("3.4 What the gap costs"));
c.push(P(`Revenue growth has continued while profitability has not. Operating revenue reached VND ${money(FY25.revenue)} billion in 2025, up ${f1(growth(FY25.revenue, FYR["FY2024"].revenue))} per cent, and VND ${money(HY.revenue)} billion in the first half of 2026, up ${f1(growth(HY.revenue, FH["2025H1"].revenue))} per cent. Pre-tax profit moved differently, from VND ${money(FY25.pbt)} billion in 2025 to VND ${money(HY.pbt)} billion in the first half of 2026. The pre-tax margin fell from ${f1(margin(FY25))} per cent to ${f1(margin(HY))} per cent, and was ${f1(margin(Q4))} and ${f1(margin(Q1))} per cent in the two quarters to March 2026.`));
c.push(Fig("fig3_revenue_margin", 545));
c.push(Cap(`Figure 7. Pre-tax profit margin by reporting period. In the first quarter of 2026 operating expenses rose ${f0(OPEX_Q1)} per cent and brokerage costs ${f0(growth(Q1.cost_brokerage, FQ["2025Q1"].cost_brokerage))} per cent on a year earlier, and trading assets lost VND ${money(-fvtplNet(Q1))} billion net.`));
c.push(P(`The composition of revenue explains the exposure. Interest on lending and receivables contributed ${f1(share("rev_lending"))} per cent of first half revenue, interest on held-to-maturity investments ${f1(share("rev_htm"))} per cent and gross trading gains ${f1(share("rev_fvtpl"))} per cent, so ${f1(BS_SHARE)} per cent of revenue depends on balance sheet size and market direction rather than on customer transactions. Brokerage commissions, at ${f1(share("rev_brokerage"))} per cent, come mostly from derivatives, and direct brokerage costs exceeded them by VND ${money(-(HY.rev_brokerage + HY.cost_brokerage))} billion in the half year.`));
c.push(Fig("fig4_revenue_mix", 545));
c.push(Cap("Figure 8. Composition of DNSE operating revenue, first half of 2026."));
c.push(P("Against plan the position is clear. DNSE targets VND 1,736 billion of total revenue, which includes financial income, and VND 550 billion of pre-tax profit for 2026. " + `The half-year delivered ${f1(TOTAL_REV / TARGET_REV * 100)} per cent of the revenue target and ${f1(HY.pbt / TARGET_PBT * 100)} per cent of the profit target, so the second half must produce VND ${money(TARGET_PBT - HY.pbt)} billion of pre-tax profit, which is ${f1((TARGET_PBT - HY.pbt) / HY.pbt)} times the first half.`));
c.push(Fig("fig5_plan_progress", 545));
c.push(Cap("Figure 9. Progress against the 2026 plan at the half year."));

// ---------------------------------------- 4. DISCUSSION
c.push(H1("4. Discussion and main analysis"));

c.push(H2("4.1 Why the gap exists"));
c.push(P("Free execution attracts the customers for whom price is the deciding factor. Those customers are, by construction, the ones with the smallest balances, since a commission saving only matters when it is large relative to the amount invested. The review data supports this reading directly, because a visible share of DNSE customers arrived through YouTube promotion and sign-up bonuses rather than through an investment decision. Reviews mentioning a social media referral appear at 1.8 per cent of negatives and 2.7 per cent of positives, and the most common complaint among them is that the promised bonus did not arrive."));
c.push(P("Derivatives compounds the effect. A derivatives account needs a margin deposit and turns over quickly, so it produces visible market share from a small pool of capital. In the second quarter of 2026 the front-month VN30 futures contract alone averaged VND " + whole(FUT_Q2) + " billion of daily notional value, against VND " + whole(HOSE_Q2) + " billion of daily value on the Ho Chi Minh cash market. Futures notional is not directly comparable with cash turnover, because a contract controls a notional amount many times the margin posted against it, and that is the point. High share in derivatives is compatible with a small asset base, which is exactly what DNSE reports."));
c.push(P(`The firm has also absorbed cost to sustain both effects. Free execution, absorbed derivatives fees and acquisition spending all appear in the operating expense line that rose ${f0(OPEX_Q1)} per cent in the first quarter of 2026. Growth in accounts is being bought, and the revenue per account has not risen to match.`));

c.push(H2("4.2 Where the money actually sits"));
c.push(P("Choosing a target segment by assertion would not survive scrutiny, so the Findex segment matrix was scored instead. Two indices were built from indicators the survey reports for every demographic cut. Index A measures investable surplus held formally, averaging six indicators covering saving at an institution, monthly saving into an account, storing money in an account, receiving interest, saving for old age and the ability to cover more than two months without income. Index B measures digital transacting habit, averaging six indicators covering digitally enabled accounts, daily internet use, smartphone ownership, weekly card or mobile payment in store, mobile balance checking and wage receipt into an account. Both use unweighted means of percentages. Because they average different indicators, each index compares segments with one another, and the level of one says nothing about the level of the other."));
c.push(P("A third quantity, the activation gap, is the distance in percentage points between account ownership and saving at a financial institution within a segment. It counts adults already inside the formal system who are not yet putting money to work, which is the population a broker is trying to reach."));
c.push(Fig("fig10_segment_model", 520));
c.push(Cap("Figure 10. Vietnamese adults by digital habit and investable surplus, Global Findex 2024. The two indices average different indicators, so segments are compared with each other rather than one index with the other. Blue marks the three segments with the highest priority score."));
c.push(P(`Three findings follow. The two indices rank the segments almost identically, with a rank correlation of ${f2(RHO)} across every segment except one, so the adults who already transact digitally are the ones who hold formal savings. Ranking segments by propensity multiplied by the size of the unconverted pool places ${PROSE[TOP3[0].segment]} first, at ${f1(TOP3[0].unactivated_adults_m)} million unconverted, followed by ${PROSE[TOP3[1].segment]} at ${f1(TOP3[1].unactivated_adults_m)} million and ${PROSE[TOP3[2].segment]} at ${f1(TOP3[2].unactivated_adults_m)} million. The priority segment is the intersection of those three, which is employed, secondary-educated adults in the upper income group.`));
c.push(P(`The third finding is the sharpest, and it is the exception to the first. Adults aged 15 to 24 show the widest separation between digital habit and investable surplus, at ${f1(bMinusA(YOUNG))} points against ${f1(NEXT_SPREAD)} for the next segment, and they carry the largest activation gap of any group at ${f1(YOUNG.activation_gap_pp)} percentage points.` + " That is the cohort a free trading application acquires most cheaply, and it is the cohort least able to fund an account. DNSE's acquisition engine is tuned to the segment with the least money."));
c.push(T([2400, 1350, 1350, 1450, 1450, 1020],
  ["Segment", "Index A investable", "Index B digital", "Activation gap, points", "Unconverted, millions", "Priority rank"],
  [
    ...SEGRANKED.filter(r => r.priority_rank <= 4 ||
                         ["Urban", "Young (15-24)", "Poorest 40%"].includes(r.segment))
      .map(r => [segName(r.segment), f1(r.index_a_investable), f1(r.index_b_digital),
                 f1(r.activation_gap_pp), f1(r.unactivated_adults_m), String(r.priority_rank)])
  ],
  { bs: 18, hs: 17, numCols: [1, 2, 3, 4, 5] }));
c.push(TabCap("Table 3. Selected rows of the segment model. Priority rank is the composite index multiplied by the unconverted pool, computed before rounding. The full 13-segment table and all 12 underlying indicators are in Appendix A."));

c.push(H2("4.3 Market and macroeconomic conditions"));
c.push(P("Three conditions make the opportunity current. Household financial assets are accumulating quickly. The share of Vietnamese adults saving at a financial institution rose from 19.9 per cent in 2022 to 43.1 per cent in 2024. Borrowing from formal institutions fell from 21.7 per cent in 2017 to 7.7 per cent in 2024. Vietnamese households are accumulating rather than leveraging."));
c.push(Fig("fig6_findex_save_borrow", 545));
c.push(Cap("Figure 11. Vietnamese adults saving at and borrowing from a financial institution, Global Findex waves 2011 to 2024."));
c.push(P("Second, the competitive benchmark is visible and high. Term deposit rates run from about 6 per cent at the largest banks to about 9 per cent on certificates of deposit at smaller institutions, against headline inflation of 4.69 per cent in June 2026. Any cash management product must clear a rate customers can see on a bank counter. Gross domestic product grew 8.18 per cent in the first half of 2026, so household income is rising alongside those rates."));
c.push(P("Third, the reclassification of Vietnam to FTSE Russell secondary emerging market status took effect on 21 September 2026, with 32 Vietnamese stocks on FTSE Russell's April 2026 indicative list. Published estimates of passive inflow start at about 2.2 billion United States dollars, and wider estimates that include active money run higher. The flow is directed at large and mid capitalisation cash equities, which is the market where DNSE is weakest. Several Vietnamese securities firms are on that list and DSE is not one of them."));

c.push(H2("4.4 Prioritising the problem"));
c.push(P("The three candidate problems from Section 1.3 were scored on three criteria. Size of effect asks how much of the revenue base the problem governs. Control asks whether DNSE can change the outcome with decisions it already has authority to make. Evidence strength asks how many independent sources support the diagnosis."));
c.push(P("Low revenue per funded account ranks first on all three. It governs lending, brokerage and fee revenue at the same time, because each depends on the customer holding assets on the platform. It sits within product and pricing decisions the firm already controls. Three independent measures point to it, namely the ratio of trading share to account share, the ratio of lending share to account share, and the review evidence that acquisition runs through promotional bonuses rather than investment intent."));
c.push(P(`The scale of the prize can be stated from the filed statements. Interest income of VND ${money(HY.rev_lending)} billion in the first half of 2026 on an average lending balance of about VND ${whole((FY25.loans + Q1.loans + Q2.loans) / 3)} billion, the mean of the balances at the end of 2025 and of each quarter, implies a yield near ${f0(YIELD)} per cent a year, against an estimated funding cost of ${f1(FUND)} per cent. Raising the lending book by VND 1,000 billion, an increase of ${f0(1000 / Q2.loans * 100)} per cent, would add roughly VND ${f0(GROSS_GAIN)} billion of annual interest income, or about VND ${f0(NET_GAIN)} billion after funding costs, which is ${f0(NET_GAIN / TARGET_PBT * 100)} per cent of the 2026 pre-tax profit target.` + ` Closing the full distance between DNSE's ${f2(LEND_SHARE)} per cent lending share and its ${f2(ACC_SHARE)} per cent account share would imply a book near VND ${whole(Math.round(Q2.loans * ACC_SHARE / LEND_SHARE / 1000) * 1000)} billion, which exceeds the firm's capital and is not a realistic target. The point is that even a small movement toward the account share is material.`));
c.push(P("Derivatives concentration ranks second. The effect is large, since a quarter of brokerage revenue would be exposed to a regulatory or volatility shock, and the evidence is strong because the share series is published. It ranks below revenue per account because DNSE cannot control the structure of the derivatives market. Proprietary trading volatility ranks third. Net trading losses in the two quarters to March 2026 are a real signal, and risk limits are adjustable, but two quarters is a thin evidentiary base and the exposure is smaller than the other two."));
c.push(T([2600, 1600, 1600, 1600, 1620],
  ["Candidate problem", "Size of effect", "Within firm control", "Evidence strength", "Rank"],
  [
    ["Low revenue per funded account", "High. Governs lending, brokerage and fee revenue together", "High. Product and pricing decisions", "Strong. Three independent share measures plus review themes", "1"],
    ["Concentration in derivatives", "Medium. Regulatory or volatility shock would remove a quarter of brokerage revenue", "Low. Depends on market structure", "Strong. Published share series", "2"],
    ["Proprietary trading volatility", "Medium. Trading assets lost money net in two consecutive quarters", "Medium. Risk limits are adjustable", "Moderate. Two quarters of evidence", "3"]
  ],
  { bs: 18, hs: 18 }));
c.push(TabCap("Table 4. Problem prioritisation. Resolving revenue per account raises funded balances, which expands the collateral base for lending and reduces the need to earn through proprietary positions."));

// ---------------------------------------- 5. ALTERNATIVES
c.push(H1("5. Strategic alternatives"));
c.push(P("Four options were considered against the priority problem. Each is assessed on the revenue it can reach, the capital and time it needs, and the risk it carries."));
c.push(T([1900, 2900, 2200, 2020],
  ["Option", "Mechanism", "Strengths", "Weaknesses"],
  [
    ["A. Continue acquiring", "Spend further on promotion and referral to add accounts at the current conversion rate",
     "Protects the new-account share that supports the brand", `Adds accounts from the segment with the least investable surplus and raises the expense line already growing at ${f0(OPEX_Q1)} per cent`],
    ["B. Cash management and fund distribution", "Pay a competitive return on idle balances and distribute investment certificates, converting deposits into on-platform assets",
     "Raises assets per account, expands the collateral base for lending and answers the rate benchmark directly. Funding is already authorised",
     "Needs a funding rate credible against deposits paying 6 to 9 per cent, completion of the approved fund management acquisition or a distribution partner, and scale before the margin works"],
    ["C. Deepen the derivatives franchise", "Invest further in the product where share is already 25.38 per cent",
     "Builds on a demonstrated strength and needs little new capability", "Increases dependence on one product and on a market where regulatory tightening is possible"],
    ["D. Move upmarket to advised clients", "Add advisory and relationship coverage for higher balance customers",
     "Directly raises revenue per account", "Requires a branch or adviser cost base the firm has deliberately avoided, and competes with entrenched full-service firms"]
  ],
  { bs: 17, hs: 18 }));
c.push(TabCap("Table 5. Strategic alternatives assessed against the priority problem."));
c.push(P("Option A raises the cost base without addressing conversion. Option C concentrates risk in the business the firm already depends on. Option D contradicts the distribution model that gives DNSE its cost advantage. Option B is the only option that raises revenue per account while reinforcing the firm's largest revenue line."));

// ---------------------------------------- 6. RECOMMENDATION
c.push(H1("6. Preliminary recommendation"));
c.push(P("DNSE should build a cash management and fund distribution layer that converts idle account balances into funded, yield-bearing positions, and should target it at employed, secondary-educated adults in the upper 60 per cent of the income distribution who already hold bank savings."));
c.push(P("The mechanism runs through the balance sheet in a specific order. Customer cash held on the platform earns a return. Higher on-platform assets raise the collateral available for margin lending, which was the largest revenue line in the first half of 2026 at " + f1(share("rev_lending")) + " per cent. Higher lending balances raise interest income without requiring an increase in the trading activity of individual customers. Fund distribution adds a recurring fee that does not depend on market direction, which addresses the proprietary volatility identified in Table 4."));
c.push(P("Two conditions make this feasible now. The 2026 annual general meeting approved a bond programme of VND 2,500 billion non-convertible and VND 1,000 billion convertible, which provides the funding a cash management product needs. Customers already recognise the feature, since the idle cash earning function is the capability they praise most often without being asked about it. The same meeting approved, for the second year running, owning one fund management company as a subsidiary to manage and distribute investment fund certificates, alongside a securities company at the Ho Chi Minh City International Financial Centre. The board has not yet completed that acquisition, and the 2026 plan already names Vietcombank, VietinBank and BIDV as intended partners for bonds and fund certificates on the Trung Vang (Golden Egg) product. Closing the acquisition, or distributing through a partner fund manager until it closes, is the first decision Round 3 should resolve."));
c.push(P("The first constraint is price. A product competing with deposits paying 6 to 9 per cent, and offering less protection than a bank deposit, must justify the difference through liquidity, integration with trading or tax treatment. The second constraint is trust. The " + f1(theme("fraud")[5]) + " per cent of negative reviews accusing the firm of deception concern promotional terms and closure fees, and a savings product launched from that starting position needs its terms stated plainly. Removing the VND 100,000 account closure fee and restating the sign-up promotion are low cost actions that address the most frequent complaints directly."));

// ---------------------------------------- 7. VALIDATION
c.push(H1("7. Validation direction"));
c.push(P("Four tests would confirm or reject the recommendation before commitment."));
c.push(Num(`Measure the full distribution of account balances at DNSE. The annual report gives two thresholds, ${f1(AR25.active_dec / AR25.accounts * 100)} per cent active and ${f1(AR25.nav10m / AR25.accounts * 100)} per cent above VND 10 million; the company holds the distribution below them, which would show where funded balances begin and how they move after onboarding.`));
c.push(Num("Test willingness to pay against deposits. A conjoint or price ladder survey of the priority segment would establish the return at which customers move cash from a bank to a broker, and whether liquidity or integration substitutes for rate."));
c.push(Num("Estimate the lending response. The link from on-platform assets to margin balances is the core of the recommendation. Regressing historical margin balances on customer assets, using the disclosed series, would size the effect; with lending at " + f0(L2E) + " per cent of equity, the 200 per cent regulatory cap is not yet the constraint."));
c.push(Num("Verify the review evidence against internal data. App store reviews are self-selected and skew negative. Comparing the theme frequencies in Figure 5 with the firm's support ticket categories would show whether crashes, onboarding and promotional disputes hold the same rank internally."));

// ---------------------------------------- 8. CONCLUSION
c.push(H1("8. Conclusion"));
c.push(P("DNSE built an acquisition engine that works and a monetisation engine that has not kept pace. It holds one eighth of Vietnam's securities accounts, a quarter of the derivatives market, under three per cent of cash equity trading and 1.39 per cent of industry lending. The gap between those numbers is the business problem, and it is visible in a pre-tax margin that fell from " + `${f1(margin(FY25))} per cent to ${f1(margin(HY))} per cent while revenue grew ${f0(growth(HY.revenue, FH["2025H1"].revenue))} per cent.` + " The Findex evidence shows that the adults who hold investable savings are the ones already transacting digitally, and that their savings are now accumulating quickly. Converting existing accounts into funded accounts addresses the constraint using a mandate the firm already holds."));

BODY = false;
c.push(new Paragraph({ children: [new PageBreak()] }));

// ======================================================= APPENDIX A
c.push(H1("Appendix A. Data tables"));

c.push(H2("A1. DNSE financial series"));
c.push(T([2500, 1620, 1620, 1620, 1660],
  ["VND billion unless stated", "FY2025", "Q1 2026", "Q2 2026", "H1 2026"],
  [
    ["Operating revenue", d => money(d.revenue)],
    ["Interest on lending and receivables", d => money(d.rev_lending)],
    ["Brokerage commissions", d => money(d.rev_brokerage)],
    ["Brokerage direct costs", d => money(d.cost_brokerage)],
    ["Interest on held-to-maturity investments", d => money(d.rev_htm)],
    ["Gross trading gains", d => money(d.rev_fvtpl)],
    ["Pre-tax profit", d => money(d.pbt)],
    ["Profit after tax", d => money(d.pat)],
    ["Pre-tax margin, per cent", d => f1(margin(d))],
    ["Margin loans and advances", d => whole(d.loans)],
    ["Shareholders' equity", d => whole(d.equity)]
  ].map(([lab, fmt]) => [lab, ...[FY25, Q1, Q2, HY].map(fmt)]).concat([
    ["Customer accounts, millions", (AR25.accounts / 1e6).toFixed(2), "1.65", "1.70", "1.70"],
    ["Share of new accounts, per cent", "20", "18", "", ""]
  ]), { bs: 18, hs: 18, numCols: [1, 2, 3, 4] }));
c.push(TabCap("Table A1. DNSE filed statements, retrieved from Vietcap's data service by step 01b; costs are negative. The second quarter of 2026 is the KPMG-reviewed half year less the first quarter. Accounts and new-account shares are from investor relations releases."));

c.push(H2("A2. Market share, second quarter of 2026"));
c.push(T([2600, 1900, 1900, 1900, 1120],
  ["Firm", "HOSE shares", "HNX shares", "Derivatives", "Lending, VND bn"],
  (() => {
    const byName = rows => Object.fromEntries(rows.map(r => [shortName(r[1]), r[2]]));
    const [ho, hn, de] = [HOSE_T["2026Q2"], HNX_T.listed["2026Q2"], HNX_T.derivatives["2026Q2"]].map(byName);
    const TICKER = { BSC: "BSI", FPTS: "FTS", PHS: "PHS" };   // filing brokers outside the report's peer set
    const lend = n => n === "DNSE" ? Q2.loans : (PANEL.firms[n] || PANEL.firms[TICKER[n]] || {}).quarterly?.["2026Q2"]?.loans;
    const cell = (m, n) => m[n] === undefined ? "" : f2(m[n]);
    return [...new Set([...Object.keys(ho), ...Object.keys(hn), ...Object.keys(de)])]
      .map(n => [n, cell(ho, n), cell(hn, n), cell(de, n), lend(n) ? whole(lend(n)) : ""])
      .concat([["Top ten combined", f2(HOSE_TOP_Q2), f2(topTen(HNX_T.listed["2026Q2"])),
                f2(topTen(HNX_T.derivatives["2026Q2"])), `${whole(INDUSTRY_LENDING)} industry`]]);
  })(), { bs: 17, hs: 17, numCols: [1, 2, 3, 4] }));
c.push(TabCap("Table A2. Percentages are share of traded value on the named market; an empty cell means the firm was outside that market's top ten. Market shares are from the HOSE and HNX quarterly announcements of July 2026. Lending balances are from each firm's filed statements at 30 June 2026; the industry total is a Vietstock compilation."));

c.push(H2("A3. Findex segment model, all thirteen segments"));
c.push(T([2260, 1020, 1020, 1020, 1020, 1120, 1120, 1440],
  ["Segment", "Index A", "Index B", "Composite", "Account", "Saved at FI", "Gap, points", "Unconverted, m"],
  SEGROWS, { bs: 17, hs: 16, numCols: [1, 2, 3, 4, 5, 6, 7] }));
c.push(TabCap("Table A3. Index A averages saving at an institution, monthly saving into an account, storing money in an account, receiving interest, saving for old age and the ability to cover two months without income. Index B averages digitally enabled account, daily internet use, smartphone ownership, weekly in-store card or mobile payment, mobile balance checking and wage receipt into an account. All values are percentages of adults aged 15 and over in that segment, from the Global Findex 2024 Vietnam file. The unconverted column applies segment population shares, recovered from the Findex estimates themselves, to 80.6 million adults."));

c.push(H2("A4. Review dataset"));
c.push(T([1120, 1120, 1300, 1300, 1300, 1300, 1580],
  ["Year", "Retrieved", "Removed", "Retained", "Mean, clean", "Generic", "Mean, substantive"],
  RV.YEAR_TAB.map(r => [r[0], int(r[1]), int(r[3]), int(r[5]), f2(r[6]), int(r[7]), f2(r[10])])
    .concat([["Total", int(D.raw_n), int(D.raw_n - D.clean_n), int(D.clean_n), f2(D.clean_mean),
              int(D.generic_in_clean), f2(D.substantive_mean)]]),
  { bs: 18, hs: 17, numCols: [1, 2, 3, 4, 5, 6] }));
c.push(TabCap(`Table A4. DNSE Entrade X reviews on Google Play, pulled ${DATE(D.pulled)}. Generic means a retained review of a single word carrying no theme.`));

const THEMENAME = {
  stability: "Crashes, freezes, login failures", onboarding: "Account opening and identity checks",
  fraud: "Accusation of deception", promo: "Sign-up bonus terms", money: "Deposits and withdrawals",
  closure: "Cannot close the account", influencer: "Arrived through a social referral",
  ui: "Interface and charts", fees: "Charges differing from advertised",
  zalopay: "ZaloPay linkage", yield: "Idle cash earning feature"
};
c.push(T([2700, 1300, 1300, 1300, 1300, 1720],
  ["Theme", "One and two star", "Three star", "Four and five star", "All retained", "Share of negatives"],
  [...RV.THEME_TAB].sort((a, b) => b[1] - a[1])
    .map(r => [THEMENAME[r[0]], String(r[1]), String(r[2]), String(r[3]), String(r[4]), `${f1(r[5])} per cent`]),
  { bs: 18, hs: 17, numCols: [1, 2, 3, 4, 5] }));
c.push(TabCap(`Table A5. Themes are non-exclusive, so the columns sum to more than the ${int(D.clean_n)} retained reviews. Negatives number ${D.negative_1_2}, neutrals ${D.neutral_3} and positives ${D.positive_4_5}.`));

c.push(H2("A5. Primary data sources"));
c.push(T([2700, 6320],
  ["Dataset", "Address"],
  [
    ["DNSE investor relations", "https://www.dnse.com.vn/quan-he-nha-dau-tu"],
    ["DNSE financial statements", "https://ir.dnse.com.vn/vi/ctype-finance_report"],
    ["DNSE annual report 2025", "https://ir.dnse.com.vn/vi/ctype-yearly_report"],
    ["DNSE 2026 AGM resolution and proposals", "https://ir.dnse.com.vn/vi/ntag-dai-hoi-dong-co-dong-19"],
    ["DNSE statements, every line", "https://iq.vietcap.com.vn/api/iq-insight-service/v1/company/DSE/financial-statement"],
    ["HOSE market share announcements", "https://www.hsx.vn"],
    ["HNX market share announcements", "https://www.hnx.vn"],
    ["Vietnam Securities Depository account statistics", "https://vsdc.vn"],
    ["Global Findex Vietnam indicators", "https://api.worldbank.org/v2/sources/28/country/VNM/series/all/data?format=json"],
    ["Global Findex 2024 microdata", "https://microdata.worldbank.org/index.php/catalog/7998"],
    ["DNSE Entrade X reviews", "https://play.google.com/store/apps/details?id=vn.com.encapital.arrow"],
    ["VPS SmartOne reviews", "https://play.google.com/store/apps/details?id=vn.com.vpbs.smartone"],
    ["FPTS EzTrade reviews", "https://play.google.com/store/apps/details?id=com.fpts.eztrade"],
    ["App Store listings, Vietnam", "https://apps.apple.com/vn/app/id1529981425 (DNSE), id1431656423 (VPS), id6737305302 (FPTS)"],
    ["App Store review feed", "https://itunes.apple.com/vn/rss/customerreviews/page=1/id=1529981425/sortby=mostrecent/json"],
    ["National Statistics Office releases", "https://www.nso.gov.vn"]
  ], { bs: 18, hs: 18 }));
c.push(TabCap("Table A6. Addresses for every dataset used. The accompanying workbook contains the full extracted tables."));

c.push(H2("A6. App Store cross-check"));
c.push(T([2300, 1150, 1150, 1150, 1400, 1870],
  ["Application", "Retrieved", "Referral spam removed", "Retained", "Mean, raw and clean", "Store rating, all ratings"],
  RV.IOS_CLEANING_LOG.map(r => [`${r[0]} (${r[9].slice(0, 4)} to ${r[10].slice(0, 4)})`, int(r[1]), int(r[3]),
    int(r[5]), `${f2(r[6])} / ${f2(r[7])}`, r[11] ? `${f2(r[12])} from ${int(r[11])}` : ""]),
  { bs: 17, hs: 17, numCols: [1, 2, 3, 4, 5] }));
c.push(TabCap(`Table A7. Written reviews from the Vietnamese App Store, pulled ${DATE(RV.APPSTORE_PULLED)} through Apple's public feed, which serves at most 500 recent and 500 most helpful reviews per application, and cleaned with the same rule as Google Play. The store rating counts every star rating, most of them given without text, as reported by Apple's lookup service.` + RV.IOS_CLEANING_LOG.filter(r => r[11] && r[11] < r[1]).map(r => ` For ${r[0].split(" ")[0]} Apple reports fewer ratings than the feed holds written reviews, so that count likely covers the current version only.`).join("")));
c.push(T([2300, 1100, 1100, 1250, 1100, 1100, 1250],
  ["Application", "Google Play, n", "Google Play, mean", "Google Play, one star", "App Store, n", "App Store, mean", "App Store, one star"],
  RV.STORE_COMPARE.map(r => [r[0], int(r[1]), f2(r[2]), `${f1(r[3])}%`, int(r[4]), f2(r[5]), `${f1(r[6])}%`]),
  { bs: 17, hs: 16, numCols: [1, 2, 3, 4, 5, 6] }));
c.push(TabCap(`Table A8. Cleaned reviews dated ${DATE(RV.STORE_WINDOW[0])} to ${DATE(RV.STORE_WINDOW[1])}, the period all six series cover.`));
c.push(Fig("figA1_store_comparison", 545));
c.push(Cap(`Figure A1. Google Play against the App Store, 2025 and 2026. Left, mean rating of cleaned reviews. Right, themes in DNSE's one and two star reviews; themes are not exclusive.`));
c.push(T([2700, 1250, 1250, 1250, 1250, 1320],
  ["Theme", "Google Play, n", "Google Play, share", "App Store, n", "App Store, share", "Both stores, n"],
  RV.STORE_THEMES.filter(r => r[5] > 0).map(r => [THEMENAME[r[0]], String(r[1]), `${f1(r[2])}%`,
    String(r[3]), `${f1(r[4])}%`, String(r[5])]),
  { bs: 17, hs: 16, numCols: [1, 2, 3, 4, 5] }));
c.push(TabCap(`Table A9. Themes in DNSE's one and two star reviews, ${RV.STORE_WINDOW[0].slice(0, 4)} to ${RV.STORE_WINDOW[1].slice(0, 4)}: ${RV.STORE_NEGATIVES[0]} on Google Play and ${RV.STORE_NEGATIVES[1]} on the App Store. Counted once per review, crashes, login or account opening appear in ${f1(SG.product[1])} and ${f1(SG.product[3])} per cent, and deception or bonus terms in ${f1(SG.promotion[1])} and ${f1(SG.promotion[3])} per cent.`));

// ======================================================= APPENDIX B
c.push(new Paragraph({ children: [new PageBreak()] }));
c.push(H1("Appendix B. Method, assumptions and limitations"));

c.push(H2("B1. Definitions and units"));
c.push(P("All currency figures are Vietnamese dong unless stated. Market share on HOSE, HNX and the derivatives market is defined by each exchange as a share of traded value on that market alone, so a figure from one exchange is never compared with a figure from another. Lending balances are margin loans plus advances against sale proceeds, which is the basis on which Vietstock compiles the industry total of VND 453,800 billion. Press estimates of margin lending alone for the same date cluster near VND 445,000 billion, and DNSE's share is " + f2(LEND_SHARE) + " per cent on the first basis and " + f2(Q2.loans / 445000 * 100) + " per cent on the second." + ` The ${PANEL.totals["2026Q2"].firms_reporting_loans} brokers with filings account for VND ${whole(PANEL.totals["2026Q2"].loans)} billion of it, ${f0(PANEL.totals["2026Q2"].loans / INDUSTRY_LENDING * 100)} per cent; the rest sits with brokers that do not file on the service.`));
c.push(P(`Account share divides DNSE's 1.7 million accounts at 30 June 2026 by the ${int(ACCOUNTS)} investor trading accounts on the VSDC counter on ${DATE(ACC_DATE)}. The later market date understates DNSE's share slightly. One investor may hold accounts at several firms, so both counts are accounts rather than people.`));

c.push(H2("B2. Assumptions stated"));
c.push(Bullet(`Half-year figures add the two quarters for income and take the 30 June balance for stocks. The second quarter is the KPMG-reviewed half year less the first quarter, so its pre-tax profit of VND ${money(Q2.pbt)} billion is below the VND 98.9 billion first reported on 20 July 2026.`));
c.push(Bullet("Funding cost is estimated as interest expense plus template line 24 less the rise in the loan-loss allowance, because the securities-company template reports loan-loss provisions and the borrowing cost of the loan book as one line."));
c.push(Bullet(`DNSE's HOSE share is treated as below ${f2(HOSE_TENTH)} per cent because the firm does not appear in the top ten and tenth place held ${f2(HOSE_TENTH)} per cent. No point estimate is used.`));
c.push(Bullet("Segment population shares applied in Table A3 are recovered from the Findex estimates themselves. Each pair of segments splits all adults in two, so the national figure for any indicator is a weighted average of the two halves, which fixes the weights; the income pair comes back as its defined 40 and 60 per cent. They are applied to 80.6 million adults aged 15 and over."));
c.push(Bullet(`Market share is read from the exchanges' own announcements: ${MM.hnx_market_share.notices_used.length} HNX notices from 2018 and every HOSE notice its news service holds. Quarters before DNSE entered a top ten carry only the tenth-place share, which bounds DNSE's share from above.`));
c.push(Bullet("Segment indices use unweighted means. Any weighting chosen after inspecting the data would be fitted to the conclusion, so none was applied."));

c.push(H2("B3. Limitations"));
c.push(P("Four limitations affect the strength of the conclusions. Per-broker account counts are not published by any firm other than DNSE, so the account-to-activity comparison in Section 3.2 cannot be repeated for competitors and the finding rests on DNSE against the market average rather than against a named peer."));
c.push(P("The funding cost in Section 4.4 is an estimate. Template line 24 holds loan-loss provisions and the borrowing cost of the loan book together, and the estimate removes the change in the balance-sheet allowance; write-offs would make it overstate funding cost and understate the net gain from extra lending."));
c.push(P("App store reviews are self-selected and over-represent dissatisfied users, so the theme frequencies in Figure 5 describe the composition of complaints rather than the incidence of problems across the customer base. The peer comparison in Figure 6 mitigates this partially, because the same selection bias applies to all three applications under the same cleaning rule." + ` The VPS sample is its ${int(VPS[2])} most recent reviews, back to ${DATE(RV.VPS_SPAN[0])}, so it is weighted toward recent years; the listing itself goes back further.` + (iosLog("DNSE") && iosLog("DNSE")[11] ? ` Written reviews are also harsher than ratings as a whole: on the App Store DNSE averages ${f2(iosLog("DNSE")[12])} stars from ${int(iosLog("DNSE")[11])} ratings, most given without text, against ${f2(iosLog("DNSE")[7])} in its cleaned written reviews. Apple's feed serves recent reviews only, so the App Store evidence is a cross-check rather than a second time series.` : "")));
c.push(P("Findex segments are reported one dimension at a time, so the intersection identified in Section 4.2 is inferred from three separate rankings rather than measured directly. The microdata file would allow the intersection to be measured, and that is the first extension proposed for Round 3."));

c.push(H2("B4. Accuracy checks performed"));
c.push(P("Every figure was traced to a primary disclosure or an exchange announcement. A verification pass against the first draft of this analysis corrected twelve figures. Three were material. An 8.8 per cent digital adoption rate belongs to micro enterprises and not to all small and medium enterprises. A count of 132.4 million biometric verifications measures customer records and not individuals. A share comparison set DNSE's Hanoi exchange position against competitor positions on the Ho Chi Minh exchange. That last error would have overstated the gap described in Section 3.2, and correcting it is why every market share figure in this report carries the name of its exchange."));
c.push(P(`DNSE's financial figures were replaced on ${DATE(FS.pulled)} by a line-by-line pull of its filed statements, checked against the reviewed half-year statements. The pull separated operating revenue, VND ${money(FY25.revenue)} billion for 2025, from the VND 1,467 billion total revenue in the annual report, which adds financial and other income; the 2026 plan is set on total revenue and is compared on that basis. It replaced first-half pre-tax profit of VND 113.1 billion with the reviewed VND ${money(HY.pbt)} billion, and corrected investment income, which the earlier draft had taken from trading gains for 2025 and from held-to-maturity interest for 2026. It also dropped a press figure of 405 per cent growth in proprietary provisions that no line of the filings reproduces; the line it appears to describe mostly holds the borrowing cost of the loan book. Peer lending and profit were replaced by each listed firm's own filings, which moved SSI's second-quarter pre-tax profit from the press figure of VND 1,511 billion to VND ${whole(peerQ2("SSI").pbt)} billion.`));
c.push(P("Company facts were checked against the 2025 annual report and the resolution and proposals of the 2026 annual general meeting. The annual report gave the account count, active customers and customer assets used here, which replace rounded press figures. The resolution showed that the meeting approved the acquisition of a fund management company, which an earlier draft reported as not approved, and it contains no approval of a digital asset stake or of carbon credit participation, which press coverage had attributed to the meeting; both were removed."));
c.push(P("The review cleaning rules were revised on 23 September 2026 after an audit of the code. The referral rule had caught genuine complaints about one-time passwords, the duplicate rule had removed identical short reviews written by different people, and several theme keywords matched unrelated words once Vietnamese tone marks were removed. Every review figure in this report uses the revised rules, and re-running the previous rules on the same pull reproduces the earlier cleaning log exactly. Segment population shares were also recovered from the Findex estimates themselves in place of typed-in values, which moved adults with secondary education or more to first place in the priority ranking."));

// ======================================================= REFERENCES
c.push(new Paragraph({ children: [new PageBreak()] }));
c.push(H1("References"));
const refs = [
  `Apple Inc. (2026) App Store customer reviews, Vietnam storefront, for Entrade X by DNSE, VPS SmartOne and FPTS EzTrade. Public review feed, retrieved ${DATE(RV.APPSTORE_PULLED)}.`,
  "DNSE Securities Joint Stock Company (2026) Financial statements for the second quarter of 2026, 20 July 2026, and interim financial statements for the six months to 30 June 2026, reviewed by KPMG, 14 August 2026. Hanoi.",
  "DNSE Securities Joint Stock Company (2026) Resolution 01/2026/NQ-DNSE-DHDCD of the 2026 annual general meeting of shareholders, 26 March 2026, and the proposals submitted to it, 23 March 2026. Hanoi.",
  "DNSE Securities Joint Stock Company (2026) Annual report 2025. Hanoi.",
  "FiinRatings (2026) Vietnam banking sector outlook 2026. Hanoi.",
  `Google LLC (2026) Google Play reviews, Vietnam, for Entrade X, VPS SmartOne and FPTS EzTrade. Retrieved ${DATE(D.pulled)}.`,
  "Hanoi Stock Exchange (2018 to 2026) Brokerage market share of the ten largest securities companies, listed shares, UPCoM and derivatives, quarterly announcements from the fourth quarter of 2017 to the second quarter of 2026.",
  "Ho Chi Minh Stock Exchange (2019 to 2026) Brokerage market share of the ten largest securities companies, quarterly announcements, 2023 to the second quarter of 2026 and the fourth quarter of 2018 to the first quarter of 2019.",
  "KPMG (2025) Vietnam 2026 outlook. October 2025.",
  "London Stock Exchange Group (2026) FTSE Russell interim country classification review and Vietnam reclassification, effective 21 September 2026.",
  "National Statistics Office of Vietnam (2026) Socio-economic performance in the second quarter and first half of 2026. Hanoi.",
  "State Bank of Vietnam (2026) Payment system statistics and biometric verification data, first half of 2026.",
  "UOB, PwC Singapore and the Singapore FinTech Association (2025) FinTech in ASEAN 2025.",
  `Vietcap Securities (2026) IQ Insight financial statement data for DSE and every securities company it covers, first quarter of 2018 to second quarter of 2026, and daily index and futures prices. Retrieved ${DATE(FS.pulled)} and ${DATE(MM.pulled)}.`,
  `Vietnam Securities Depository and Clearing Corporation (2019 to 2026) Annual reports 2018 to 2025, and the investor account counter at vsd.vn, retrieved ${DATE(ACC_DATE)}.`,
  "Vietstock (2026) Margin lending reaches a record VND 454 trillion, with divergence across the field. July 2026.",
  "The Investor (2026) FTSE Russell names 32 Vietnamese stocks eligible for emerging-market index inclusion. 8 April 2026.",
  "World Bank (2025) The Global Findex Database 2025: connectivity and financial inclusion in the digital economy. Washington DC. Vietnam indicators retrieved from the World Bank open data interface, source 28, on 20 September 2026.",
  "World Bank (2025) Viet Nam: Global Findex 2025 microdata, reference VNM_2024_FINDEX_v02_M. Microdata Library, catalogue entry 7998."
];
refs.forEach(r => c.push(new Paragraph({
  spacing: { after: 130, line: 280 },
  indent: { left: 420, hanging: 420 },
  children: [new TextRun({ text: r, size: 21, font: FONT, color: "000000" })]
})));

// ======================================================= DOC
const doc = new Document({
  creator: "FBA Season 6 Round 2",
  title: "Acquisition without activation: DNSE Securities",
  numbering: {
    config: [
      { reference: "b", levels: [{ level: 0, format: LevelFormat.BULLET, text: "•", alignment: AlignmentType.LEFT,
        style: { paragraph: { indent: { left: 460, hanging: 240 } } } }] },
      { reference: "n", levels: [{ level: 0, format: LevelFormat.DECIMAL, text: "%1.", alignment: AlignmentType.LEFT,
        style: { paragraph: { indent: { left: 460, hanging: 240 } } } }] }
    ]
  },
  styles: { default: { document: { run: { font: FONT, size: 23, color: "000000" } } } },
  sections: [{
    properties: { page: { margin: { top: 1440, right: 1440, bottom: 1440, left: 1440 } } },
    footers: {
      default: new Footer({
        children: [new Paragraph({
          alignment: AlignmentType.CENTER,
          children: [new TextRun({ children: [PageNumber.CURRENT], size: 18, font: FONT, color: "000000" })]
        })]
      })
    },
    children: c
  }]
});

Packer.toBuffer(doc).then(b => {
  fs.writeFileSync(require('path').join(__dirname, 'FBAR2_2026_DNSE_Analysis.docx'), b);
  console.log('written bytes', b.length);
  console.log('MAIN BODY WORDS', WORDS);
});

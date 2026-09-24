const fs = require('fs');
const {
  Document, Packer, Paragraph, TextRun, HeadingLevel, AlignmentType,
  Table, TableRow, TableCell, WidthType, ShadingType, BorderStyle,
  PageBreak, Footer, PageNumber, LevelFormat, ImageRun
} = require('docx');

const FONT = "Times New Roman";
const GREY = "3F3F3F";

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
function Fig(file, widthPx, heightPx) {
  return new Paragraph({
    alignment: AlignmentType.CENTER,
    spacing: { before: 120, after: 60 },
    children: [new ImageRun({
      type: "png",
      data: fs.readFileSync(require('path').join(__dirname, 'fig', file + '.png')),
      transformation: { width: widthPx, height: heightPx }
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

// Output of /home/claude/segment_model.py, ordered by composite index times unconverted pool
const SEGROWS = [
  ["All adults", "36.8", "59.4", "48.1", "70.5", "43.1", "27.5", "22.13"],
  ["In labour force", "41.5", "65.1", "53.3", "77.9", "48.4", "29.5", "17.47"],
  ["Richest 60 per cent", "46.0", "72.0", "59.0", "85.5", "53.8", "31.7", "15.34"],
  ["Secondary education or more", "39.5", "63.5", "51.5", "75.2", "46.7", "28.5", "17.55"],
  ["Aged 25 and over", "38.1", "57.9", "48.0", "70.2", "44.1", "26.1", "17.44"],
  ["Rural", "33.8", "56.1", "45.0", "67.4", "40.5", "26.9", "13.44"],
  ["Men", "35.0", "59.8", "47.4", "71.2", "41.0", "30.2", "11.97"],
  ["Women", "38.6", "59.0", "48.8", "69.9", "45.1", "24.8", "10.18"],
  ["Urban", "43.0", "66.0", "54.5", "77.0", "48.4", "28.6", "8.76"],
  ["Aged 15 to 24", "31.1", "66.2", "48.6", "72.2", "38.6", "33.6", "4.63"],
  ["Poorest 40 per cent", "23.1", "40.5", "31.8", "48.1", "27.1", "21.1", "6.79"],
  ["Out of labour force", "18.4", "36.6", "27.5", "41.3", "21.9", "19.4", "4.13"],
  ["Primary education or less", "15.6", "26.5", "21.1", "33.5", "14.0", "19.5", "3.71"]
];

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
c.push(P("Activity has not followed acquisition. In the same quarter DNSE intermediated 2.88 per cent of listed share trading on the Hanoi exchange and did not appear in the top ten on the larger Ho Chi Minh exchange, where tenth place required 2.94 per cent. Its lending book of VND 6,303 billion was 1.39 per cent of the industry total. Setting account share against trading share, an average DNSE account generates about a quarter of the cash equity trading value of an average market account."));
c.push(P("The income statement shows what that costs. Operating revenue rose 58.9 per cent year on year in the first half of 2026 while the pre-tax profit margin fell from 23.2 per cent across 2025 to 13.3 per cent in the half year. Operating expenses rose 120 per cent in the first quarter of 2026 and provisions against the proprietary portfolio rose 405 per cent. At the half-year the firm had delivered 48.9 per cent of its revenue target and 20.6 per cent of its profit target."));
c.push(P("This report draws on company disclosures, exchange market share reports, World Bank Global Findex 2024 microdata for Vietnam and 868 Google Play reviews of DNSE and two competitor applications collected and cleaned for this study. The review evidence locates the friction. Among 271 cleaned negative reviews, 25.8 per cent concern crashes and login failures and 19.6 per cent concern account opening. A further 16.2 per cent accuse the firm of deception. Most of those cite a sign-up bonus that requires a VND 2 million deposit, or an account closure fee of VND 100,000."));
c.push(P("Scoring the Findex segment matrix produces the priority customer group rather than assuming it. Employed adults with secondary education in the upper 60 per cent of the income distribution rank first. They combine a high propensity to hold investable balances with the largest unconverted pool, between 15 and 17.5 million adults who hold an account and do not save through a financial institution. The segment with the widest gap between digital habit and accumulated surplus is adults aged 15 to 24, which is the group a free application acquires most cheaply and monetises least."));
c.push(P("The priority problem is revenue per account. The recommendation is a cash management and fund distribution layer that converts idle balances into funded, yield-bearing accounts, priced against bank deposit rates near 7 per cent. Higher assets per account expand the collateral base for margin lending, which is already the firm's largest revenue line. The 2026 annual general meeting approved a VND 3,500 billion bond programme that funds it, although it did not approve a fund management vehicle, so a licence or a distribution partner is the first step. Round 3 should test willingness to pay, the activation sequence and the effect on lending balances."));
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
c.push(P("DNSE Securities Joint Stock Company is a Vietnamese securities firm listed on the Ho Chi Minh Stock Exchange under the code DSE. Its 2024 listing was the only initial public offering on the Vietnamese market that year. Charter capital stands at approximately VND 4,286 billion and total assets passed VND 15,000 billion at the end of 2025."));
c.push(P("The firm distributes entirely through its Entrade X platform and operates without a branch network. It became the first Vietnamese securities company to offer lifetime commission-free trading, so order execution is free and revenue comes from margin lending, advances against sale proceeds, custody and proprietary investment. In December 2022 it launched Vietnam's first per-position margin system, which manages leverage on an individual position rather than across the whole account. From May 2025 it has absorbed derivatives margin management fees on behalf of customers."));

c.push(P("The market DNSE competes in is crowded and fragmenting. The ten largest firms accounted for 65.19 per cent of trading on the Ho Chi Minh exchange in the second quarter of 2026, down from 69.05 per cent three months earlier. Almost four percentage points of share moved to smaller firms in one quarter. Industry profit comes mainly from lending rather than from commissions, with VND 453,800 billion outstanding at the end of June 2026 against a regulatory cap of 200 per cent of equity. Pre-tax profit in that quarter ranged from VND 2,159 billion at VPBankS down to VND 98.9 billion at DNSE, which shows the scale difference between DNSE and the firms whose accounts it is winning."));
c.push(Fig("fig11_peer_profit", 530, 233));
c.push(Cap("Figure 1. Pre-tax profit of selected Vietnamese securities firms, second quarter of 2026. DNSE ranks second in derivatives brokerage and well outside the top ten by earnings."));

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
    ["Company financials", "Quarterly and half-year revenue, profit, revenue lines, lending balance, accounts, plan targets", "DNSE investor relations disclosures and financial statements, FY2024 to Q2 2026"],
    ["Exchange market share", "Brokerage share on HOSE, HNX, UPCoM and derivatives for every firm in the top ten", "HOSE and HNX quarterly announcements, Q1 2024 to Q2 2026"],
    ["Industry cross-section", "Lending balances, pre-tax profit and revenue for the largest securities firms", "Q2 2026 financial statements compiled by Vietstock and Mekong Asean"],
    ["Financial inclusion", "51 Findex indicators for Vietnam across 13 demographic segments, plus five survey waves from 2011 to 2024", "World Bank Global Findex, open data interface source 28, retrieved 20 September 2026"],
    ["Customer reviews", "868 DNSE reviews and 1,377 competitor reviews with rating, date, text and helpfulness votes", "Google Play public listings, collected 20 to 21 September 2026"]
  ],
  { bs: 18, hs: 18 }));
c.push(TabCap("Table 1. Evidence base. Full source addresses are listed in Appendix A."));

c.push(H2("2.2 Preparation and quality control"));
c.push(P("Financial figures were taken from primary disclosures rather than press summaries wherever both existed. Where the two disagreed, the disclosure was used and the discrepancy recorded. Industry lending illustrates the point. Press coverage of the second quarter of 2026 reports three different industry totals, namely VND 435,000 billion, VND 445,000 billion and VND 453,800 billion. The three measure different things, since the largest includes advances against sale proceeds alongside margin loans. This report uses VND 453,800 billion throughout and states the basis wherever a share is calculated from it."));
c.push(P("Market share figures are defined by each exchange as a share of traded value on that exchange alone. Shares from different exchanges are therefore never compared with one another in this report, and each figure carries the name of the market it belongs to."));
c.push(P("The review dataset required the most work. Vietnamese application stores carry heavy comment spam from unlicensed lending sites, and much of it disguises itself using mathematical alphanumeric Unicode characters that defeat plain keyword filters. Every review text was normalised to a comparable form before filtering, using Unicode compatibility composition followed by removal of diacritics and conversion to lower case. Two regular expression rules then flagged loan advertising and referral code farming, and exact duplicates of already-seen text were removed. The identical rule was applied to all three applications so that the comparison in Figure 6 is like for like."));
c.push(T([2900, 1450, 1450, 1450, 1770],
  ["Stage", "DNSE", "VPS", "FPTS", "Note"],
  [
    ["Reviews retrieved", "868", "1,200", "177", "Full available history except VPS, capped by pagination"],
    ["Loan advertising removed", "127", "", "", "14.6 per cent of the DNSE pull"],
    ["Referral farming removed", "72", "", "", "8.3 per cent of the DNSE pull"],
    ["Duplicates removed", "36", "", "", "Identical normalised text"],
    ["Reviews retained", "633", "1,116", "169", "27.1, 7.0 and 4.5 per cent removed"],
    ["Mean rating before cleaning", "3.287", "2.597", "2.181", ""],
    ["Mean rating after cleaning", "3.161", "2.515", "2.154", "Removed material rated 3.626 on average"]
  ],
  { bs: 18, hs: 18, numCols: [1, 2, 3] }));
c.push(TabCap("Table 2. Review cleaning log. Cleaning lowers the DNSE mean because the spam it removes is rated more favourably than the genuine reviews it leaves behind."));
c.push(P("Cleaning changed the conclusion. In 2022 and 2023, 48.8 and 55.8 per cent of all DNSE reviews were spam, so an uncleaned reading of those years would have measured the spam rather than the customers. The cleaned series in Figure 4 is a different shape from the raw one."));

c.push(H2("2.3 Analytical method"));
c.push(P("Three methods were used. Share comparison places the same firm against several denominators, which isolates the point in the customer journey where performance changes. Thematic coding assigns each cleaned review one or more non-exclusive labels through keyword matching on the normalised text, and short reviews carrying no label are counted separately as generic so that they do not inflate a favourable reading. Index construction converts the Findex segment matrix into two comparable scores, described in Section 4.2, using unweighted means so that no weighting choice is fitted to the result."));

// ---------------------------------------- 3. FINDINGS
c.push(H1("3. Findings from the data"));

c.push(H2("3.1 Acquisition is working"));
c.push(P("DNSE has grown its customer base faster than any competitor. It opened more than 120,000 accounts in the first quarter of 2024, equal to 30 per cent of all new accounts in the market. In 2025 it took 20 per cent of new openings and closed the year with 1.5 million accounts. It opened 142,000 accounts in the first quarter of 2026, an 18 per cent share, and passed 1.7 million customers by mid-year."));
c.push(P("Derivatives followed the same path. DNSE reached 4.01 per cent of derivatives brokerage in the first quarter of 2024 and 25.38 per cent by the second quarter of 2026, ranking second for seven consecutive quarters while the leader VPS fell to 33.84 per cent."));
c.push(Fig("fig1_derivatives_share", 555, 246));
c.push(Cap("Figure 2. DNSE derivatives brokerage market share, Hanoi Stock Exchange. Quarterly observations between the first quarter of 2024 and the first quarter of 2025 were not published and the line is interpolated across that interval."));

c.push(H2("3.2 Conversion is not"));
c.push(P("The same firm looks very different once activity replaces registration as the measure. In the second quarter of 2026 DNSE intermediated 2.88 per cent of listed share trading on the Hanoi exchange, ranking eighth of ten. It did not enter the top ten on the Ho Chi Minh exchange, where tenth place required 2.94 per cent. Its margin loan and advance balance of VND 6,303 billion, a record for the firm, was 1.39 per cent of the VND 453,800 billion lent across the industry."));
c.push(Fig("fig2_monetisation_gap", 555, 270));
c.push(Cap("Figure 3. DNSE share of the Vietnamese market on five measures, second quarter of 2026. Each percentage is a share of its own market, and the five denominators differ."));
c.push(P("Dividing trading share by account share gives the relative intensity of an average account. DNSE holds 12.27 per cent of the 13.85 million securities accounts in the market and produces 2.88 per cent of Hanoi listed share trading. An average DNSE account therefore trades at about 23 per cent of the value of an average market account. Both sides of that ratio count accounts rather than people, and one investor may hold accounts at several firms. The equivalent figure on the Ho Chi Minh exchange is lower still. Lending shows the same pattern more sharply, at 1.39 per cent of industry balances against 12.27 per cent of accounts."));

c.push(H2("3.3 What customers say about the product"));
c.push(P("Rating data explains part of the gap. After cleaning, DNSE averages 3.161 stars across 633 reviews, ahead of VPS at 2.515 and FPTS at 2.154, so the product compares well against its closest competitors. The direction of travel is the concern. Substantive reviews, meaning cleaned reviews that carry a content theme rather than a single word of praise, averaged 4.07 stars in 2024 and 2.36 in 2025."));
c.push(Fig("fig7_review_rating_by_year", 545, 250));
c.push(Cap("Figure 4. Mean rating of substantive DNSE reviews by year, after spam and duplicate removal. The 2024 figure also rests on the year with the highest share of one-word reviews, at 30.9 per cent of cleaned reviews against 13.2 per cent in 2025."));
c.push(P("The themes show where the friction sits. Among 271 cleaned one and two star reviews, crashes and login failures account for 25.8 per cent and account opening for 19.6 per cent. Accusations of deception account for 16.2 per cent, and reading those reviews identifies two specific triggers. A sign-up promotion advertised as VND 100,000 requires a deposit of VND 2 million, and closing an account costs VND 100,000. Both appear repeatedly among the most upvoted reviews of 2025."));
c.push(Fig("fig8_negative_themes", 560, 213));
c.push(Cap("Figure 5. Themes in the 271 cleaned one and two star DNSE reviews. Themes are not exclusive, so a review may appear in more than one row."));
c.push(P("Two further readings matter. Complaints about account opening concentrate in 2021, 2022 and 2025, and complaints about stability concentrate in 2023 and 2026, which indicates recurring rather than resolved problems. Separately, the feature customers praise without prompting is the automatic earning of idle cash, described in Vietnamese as the account that does not sleep. That feature already does at a small scale what Section 6 recommends doing deliberately."));
c.push(Fig("fig9_peer_ratings", 520, 249));
c.push(Cap("Figure 6. Mean ratings of three Vietnamese broker applications under the identical cleaning rule. DNSE leads on the full history and in 2026."));

c.push(H2("3.4 What the gap costs"));
c.push(P("Revenue growth has continued while profitability has not. Operating revenue reached VND 1,467 billion in 2025, up 77 per cent, and VND 848.2 billion in the first half of 2026, up 58.9 per cent. Pre-tax profit moved differently, from VND 340.2 billion in 2025 to VND 113.1 billion in the first half of 2026. The pre-tax margin fell from 23.2 per cent to 13.3 per cent, and touched 3.6 per cent in the first quarter."));
c.push(Fig("fig3_revenue_margin", 545, 234));
c.push(Cap("Figure 7. Pre-tax profit margin by reporting period. The first quarter of 2026 carried a 120 per cent increase in operating expenses, a 125 per cent increase in brokerage costs and a 405 per cent increase in provisions against the proprietary portfolio."));
c.push(P("The composition of revenue explains the exposure. Interest on lending and receivables contributed 39.6 per cent of first half revenue and investment income 22.8 per cent, so a majority of revenue depends on balance sheet size and market direction rather than on customer transactions. Brokerage commissions, at 26.2 per cent, come mostly from derivatives."));
c.push(Fig("fig4_revenue_mix", 545, 121));
c.push(Cap("Figure 8. Composition of DNSE operating revenue, first half of 2026."));
c.push(P("Against plan the position is clear. DNSE targets VND 1,736 billion of revenue and VND 550 billion of pre-tax profit for 2026. The half-year delivered 48.9 per cent of the revenue target and 20.6 per cent of the profit target, so the second half must produce VND 436.9 billion of pre-tax profit, which is 3.9 times the first half."));
c.push(Fig("fig5_plan_progress", 545, 179));
c.push(Cap("Figure 9. Progress against the 2026 plan at the half year."));

// ---------------------------------------- 4. DISCUSSION
c.push(H1("4. Discussion and main analysis"));

c.push(H2("4.1 Why the gap exists"));
c.push(P("Free execution attracts the customers for whom price is the deciding factor. Those customers are, by construction, the ones with the smallest balances, since a commission saving only matters when it is large relative to the amount invested. The review data supports this reading directly, because a visible share of DNSE customers arrived through YouTube promotion and sign-up bonuses rather than through an investment decision. Reviews mentioning a social media referral appear at 1.8 per cent of negatives and 2.7 per cent of positives, and the most common complaint among them is that the promised bonus did not arrive."));
c.push(P("Derivatives compounds the effect. A derivatives account needs a margin deposit and turns over quickly, so it produces visible market share from a small pool of capital. In the second quarter of 2026 the VN30 futures market averaged VND 43,925 billion of daily notional value, against VND 17,336 billion of daily value on the Ho Chi Minh cash market in August. Futures notional is not directly comparable with cash turnover, because a contract controls a notional amount many times the margin posted against it, and that is the point. High share in derivatives is compatible with a small asset base, which is exactly what DNSE reports."));
c.push(P("The firm has also absorbed cost to sustain both effects. Free execution, absorbed derivatives fees and acquisition spending all appear in the operating expense line that rose 120 per cent in the first quarter of 2026. Growth in accounts is being bought, and the revenue per account has not risen to match."));

c.push(H2("4.2 Where the money actually sits"));
c.push(P("Choosing a target segment by assertion would not survive scrutiny, so the Findex segment matrix was scored instead. Two indices were built from indicators the survey reports for every demographic cut. Index A measures investable surplus held formally, averaging six indicators covering saving at an institution, monthly saving into an account, storing money in an account, receiving interest, saving for old age and the ability to cover more than two months without income. Index B measures digital transacting habit, averaging six indicators covering digitally enabled accounts, daily internet use, smartphone ownership, weekly card or mobile payment in store, mobile balance checking and wage receipt into an account. Both use unweighted means of percentages already expressed on the same scale."));
c.push(P("A third quantity, the activation gap, is the distance in percentage points between account ownership and saving at a financial institution within a segment. It counts adults already inside the formal system who are not yet putting money to work, which is the population a broker is trying to reach."));
c.push(Fig("fig10_segment_model", 520, 320));
c.push(Cap("Figure 10. Vietnamese adults by digital habit and investable surplus, Global Findex 2024. Every segment lies below the diagonal, so digital readiness exceeds investable surplus everywhere in Vietnam."));
c.push(P("Three findings follow. Every segment sits below the diagonal, which means digital capability is ahead of accumulated savings across the whole population, so distribution is not the binding constraint anywhere. Ranking segments by propensity multiplied by the size of the unconverted pool places adults in the labour force first, at 17.5 million unconverted. The upper 60 per cent of the income distribution and adults with secondary education or more follow, and their scores are within 0.2 per cent of each other, so they should be treated as equal. The priority segment is the intersection of those three, which is employed, secondary-educated adults in the upper income group."));
c.push(P("The third finding is the sharpest. Adults aged 15 to 24 show the widest separation between digital habit and investable surplus, at 35.1 points against 26.0 for the next segment, and they carry the largest activation gap of any group at 33.6 percentage points. That is the cohort a free trading application acquires most cheaply, and it is the cohort least able to fund an account. DNSE's acquisition engine is tuned to the segment with the least money."));
c.push(T([2400, 1350, 1350, 1450, 1450, 1020],
  ["Segment", "Index A investable", "Index B digital", "Activation gap, points", "Unconverted, millions", "Priority rank"],
  [
    ["In labour force", "41.5", "65.1", "29.5", "17.5", "1"],
    ["Richest 60 per cent", "46.0", "72.0", "31.7", "15.3", "2"],
    ["Secondary education or more", "39.5", "63.5", "28.5", "17.6", "3"],
    ["Aged 25 and over", "38.1", "57.9", "26.1", "17.4", "4"],
    ["Urban", "43.0", "66.0", "28.6", "8.8", "8"],
    ["Aged 15 to 24", "31.1", "66.2", "33.6", "4.6", "9"],
    ["Poorest 40 per cent", "23.1", "40.5", "21.1", "6.8", "10"]
  ],
  { bs: 18, hs: 17, numCols: [1, 2, 3, 4, 5] }));
c.push(TabCap("Table 3. Selected rows of the segment model. Priority rank is the composite index multiplied by the unconverted pool. The full 13-segment table and all 12 underlying indicators are in Appendix A."));

c.push(H2("4.3 Market and macroeconomic conditions"));
c.push(P("Three conditions make the opportunity current. Household financial assets are accumulating quickly. The share of Vietnamese adults saving at a financial institution rose from 19.9 per cent in 2022 to 43.1 per cent in 2024. Borrowing from formal institutions fell from 21.7 per cent in 2017 to 7.7 per cent over the same period. Vietnamese households are accumulating rather than leveraging."));
c.push(Fig("fig6_findex_save_borrow", 545, 241));
c.push(Cap("Figure 11. Vietnamese adults saving at and borrowing from a financial institution, Global Findex waves 2011 to 2024."));
c.push(P("Second, the competitive benchmark is visible and high. Term deposit rates run from about 6 per cent at the largest banks to about 9 per cent on certificates of deposit at smaller institutions, against headline inflation of 4.69 per cent in June 2026. Any cash management product must clear a rate customers can see on a bank counter. Gross domestic product grew 8.18 per cent in the first half of 2026, so household income is rising alongside those rates."));
c.push(P("Third, the reclassification of Vietnam to FTSE Russell secondary emerging market status took effect on 21 September 2026, covering 27 constituents. Published estimates of passive inflow start at about 2.2 billion United States dollars, and wider estimates that include active money run higher. The flow is directed at large and mid capitalisation cash equities, which is the market where DNSE is weakest. Several Vietnamese securities firms are among the constituents and DSE is not one of them."));

c.push(H2("4.4 Prioritising the problem"));
c.push(P("The three candidate problems from Section 1.3 were scored on three criteria. Size of effect asks how much of the revenue base the problem governs. Control asks whether DNSE can change the outcome with decisions it already has authority to make. Evidence strength asks how many independent sources support the diagnosis."));
c.push(P("Low revenue per funded account ranks first on all three. It governs lending, brokerage and fee revenue at the same time, because each depends on the customer holding assets on the platform. It sits within product and pricing decisions the firm already controls. Three independent measures point to it, namely the ratio of trading share to account share, the ratio of lending share to account share, and the review evidence that acquisition runs through promotional bonuses rather than investment intent."));
c.push(P("The scale of the prize can be stated from disclosed figures. Interest income of VND 336.1 billion in the first half of 2026 on an average lending balance of about VND 6,106 billion implies a yield near 11 per cent a year. Raising the lending book by VND 1,000 billion, an increase of 16 per cent on the current balance, would add roughly VND 110 billion of annual interest income before funding costs. That is 20 per cent of the 2026 pre-tax profit target. Closing the full distance between DNSE's 1.39 per cent lending share and its 12.27 per cent account share would imply a book near VND 55,000 billion, which exceeds the firm's capital and is not a realistic target. The point is that even a small movement toward the account share is material."));
c.push(P("Derivatives concentration ranks second. The effect is large, since a quarter of brokerage revenue would be exposed to a regulatory or volatility shock, and the evidence is strong because the share series is published. It ranks below revenue per account because DNSE cannot control the structure of the derivatives market. Proprietary trading volatility ranks third. Provisions rising 405 per cent in one quarter is a real signal, and risk limits are adjustable, but one quarter is a thin evidentiary base and the exposure is smaller than the other two."));
c.push(T([2600, 1600, 1600, 1600, 1620],
  ["Candidate problem", "Size of effect", "Within firm control", "Evidence strength", "Rank"],
  [
    ["Low revenue per funded account", "High. Governs lending, brokerage and fee revenue together", "High. Product and pricing decisions", "Strong. Three independent share measures plus review themes", "1"],
    ["Concentration in derivatives", "Medium. Regulatory or volatility shock would remove a quarter of brokerage revenue", "Low. Depends on market structure", "Strong. Published share series", "2"],
    ["Proprietary trading volatility", "Medium. Provisions rose 405 per cent in one quarter", "Medium. Risk limits are adjustable", "Moderate. One quarter of evidence", "3"]
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
     "Protects the new-account share that supports the brand", "Adds accounts from the segment with the least investable surplus and raises the expense line already growing at 120 per cent"],
    ["B. Cash management and fund distribution", "Pay a competitive return on idle balances and distribute investment certificates, converting deposits into on-platform assets",
     "Raises assets per account, expands the collateral base for lending and answers the rate benchmark directly. Funding is already authorised",
     "Needs a funding rate credible against deposits paying 6 to 9 per cent, a fund management licence or a distribution partner, and scale before the margin works"],
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
c.push(P("The mechanism runs through the balance sheet in a specific order. Customer cash held on the platform earns a return. Higher on-platform assets raise the collateral available for margin lending, which was the largest revenue line in the first half of 2026 at 39.6 per cent. Higher lending balances raise interest income without requiring an increase in the trading activity of individual customers. Fund distribution adds a recurring fee that does not depend on market direction, which addresses the proprietary volatility identified in Table 4."));
c.push(P("Two conditions make this feasible now. The 2026 annual general meeting approved a bond programme of VND 2,500 billion non-convertible and VND 1,000 billion convertible, which provides the funding a cash management product needs. Customers already recognise the feature, since the idle cash earning function is the capability they praise most often without being asked about it. One condition is missing. The same meeting approved a securities company at the Ho Chi Minh City International Financial Centre, a VND 10 billion stake in a digital asset company and participation in the carbon credit exchange, and it did not approve a fund management vehicle. Distributing investment certificates therefore requires either a licence application or a partnership with an existing fund manager, and that is the first decision Round 3 should resolve."));
c.push(P("The first constraint is price. A product competing with deposits paying 6 to 9 per cent, and offering less protection than a bank deposit, must justify the difference through liquidity, integration with trading or tax treatment. The second constraint is trust. The 16.2 per cent of negative reviews accusing the firm of deception concern promotional terms and closure fees, and a savings product launched from that starting position needs its terms stated plainly. Removing the VND 100,000 account closure fee and restating the sign-up promotion are low cost actions that address the most frequent complaints directly."));

// ---------------------------------------- 7. VALIDATION
c.push(H1("7. Validation direction"));
c.push(P("Four tests would confirm or reject the recommendation before commitment."));
c.push(Num("Measure the distribution of account balances at DNSE. This report infers low balances per account from the ratio of trading share to account share. The company holds the distribution directly, and it would confirm whether inactivity concentrates in a small tail or runs across the base."));
c.push(Num("Test willingness to pay against deposits. A conjoint or price ladder survey of the priority segment would establish the return at which customers move cash from a bank to a broker, and whether liquidity or integration substitutes for rate."));
c.push(Num("Estimate the lending response. The link from on-platform assets to margin balances is the core of the recommendation. Regressing historical margin balances on customer assets, using the disclosed series, would size the effect and test whether the 200 per cent regulatory cap binds before the commercial opportunity is exhausted."));
c.push(Num("Verify the review evidence against internal data. App store reviews are self-selected and skew negative. Comparing the theme frequencies in Figure 5 with the firm's support ticket categories would show whether crashes, onboarding and promotional disputes hold the same rank internally."));

// ---------------------------------------- 8. CONCLUSION
c.push(H1("8. Conclusion"));
c.push(P("DNSE built an acquisition engine that works and a monetisation engine that has not kept pace. It holds one eighth of Vietnam's securities accounts, a quarter of the derivatives market, under three per cent of cash equity trading and 1.39 per cent of industry lending. The gap between those numbers is the business problem, and it is visible in a pre-tax margin that fell from 23.2 per cent to 13.3 per cent while revenue grew 59 per cent. The Findex evidence shows a population whose digital readiness is ahead of its investable savings in every segment, and whose savings are now accumulating quickly. Converting existing accounts into funded accounts addresses the constraint using a mandate the firm already holds."));

BODY = false;
c.push(new Paragraph({ children: [new PageBreak()] }));

// ======================================================= APPENDIX A
c.push(H1("Appendix A. Data tables"));

c.push(H2("A1. DNSE financial series"));
c.push(T([2500, 1620, 1620, 1620, 1660],
  ["VND billion unless stated", "FY2025", "Q1 2026", "Q2 2026", "H1 2026"],
  [
    ["Operating revenue", "1,467.0", "395.0", "453.1", "848.2"],
    ["Interest on lending and receivables", "555.8", "147.5", "188.6", "336.1"],
    ["Brokerage commissions", "404.0", "119.5", "102.5", "222.1"],
    ["Investment income", "171.4", "98.4", "95.0", "193.4"],
    ["Pre-tax profit", "340.2", "14.2", "98.9", "113.1"],
    ["Profit after tax", "272.5", "11.3", "83.0", "94.3"],
    ["Pre-tax margin, per cent", "23.2", "3.6", "21.7", "13.3"],
    ["Margin loans and advances", "5,832", "5,910", "6,303", "6,303"],
    ["Customer accounts, millions", "1.50", "1.65", "1.70", "1.70"],
    ["Share of new accounts, per cent", "20", "18", "", ""]
  ], { bs: 18, hs: 18, numCols: [1, 2, 3, 4] }));
c.push(TabCap("Table A1. Sources are DNSE quarterly financial statements and investor relations releases."));

c.push(H2("A2. Market share, second quarter of 2026"));
c.push(T([2600, 1900, 1900, 1900, 1120],
  ["Firm", "HOSE shares", "HNX shares", "Derivatives", "Lending, VND bn"],
  [
    ["VPS", "12.61", "17.71", "33.84", "31,300"],
    ["SSI", "11.17", "not published", "8.21", "40,500"],
    ["TCBS", "9.36", "9.00", "", "51,500"],
    ["Vietcap", "7.00", "2.86", "", ""],
    ["HSC", "6.80", "outside top ten", "", "29,000"],
    ["MBS", "4.79", "not published", "about 4", ""],
    ["VNDirect", "3.96", "not published", "about 4", ""],
    ["VPBankS", "3.57", "6.71", "", "38,200"],
    ["KIS Vietnam", "2.99", "outside top ten", "", ""],
    ["Mirae Asset Vietnam", "2.94", "outside top ten", "below 2", ""],
    ["BSC", "outside top ten", "3.58", "", ""],
    ["DNSE", "outside top ten", "2.88", "25.38", "6,303"],
    ["VIX", "outside top ten", "2.66", "", ""],
    ["Top ten combined", "65.19", "63.20", "94.52", "453,800 industry"]
  ], { bs: 17, hs: 17, numCols: [1, 2, 3, 4] }));
c.push(TabCap("Table A2. Percentages are share of traded value on the named market. Empty cells were not published in the sources consulted. Sources are the HOSE and HNX quarterly announcements of 7 July 2026 and the Q2 2026 financial statements compiled by Vietstock."));

c.push(H2("A3. Findex segment model, all thirteen segments"));
c.push(T([2260, 1020, 1020, 1020, 1020, 1120, 1120, 1440],
  ["Segment", "Index A", "Index B", "Composite", "Account", "Saved at FI", "Gap, points", "Unconverted, m"],
  SEGROWS, { bs: 17, hs: 16, numCols: [1, 2, 3, 4, 5, 6, 7] }));
c.push(TabCap("Table A3. Index A averages saving at an institution, monthly saving into an account, storing money in an account, receiving interest, saving for old age and the ability to cover two months without income. Index B averages digitally enabled account, daily internet use, smartphone ownership, weekly in-store card or mobile payment, mobile balance checking and wage receipt into an account. All values are percentages of adults aged 15 and over in that segment, from the Global Findex 2024 Vietnam file. The unconverted column applies segment population shares to 80.6 million adults."));

c.push(H2("A4. Review dataset"));
c.push(T([1120, 1120, 1300, 1300, 1300, 1300, 1580],
  ["Year", "Retrieved", "Removed", "Retained", "Mean, clean", "Generic", "Mean, substantive"],
  [
    ["2020", "3", "0", "3", "3.67", "0", "3.67"],
    ["2021", "72", "13", "59", "1.98", "2", "1.88"],
    ["2022", "207", "101", "106", "3.14", "19", "2.85"],
    ["2023", "154", "86", "68", "2.57", "6", "2.40"],
    ["2024", "202", "27", "175", "4.29", "54", "4.07"],
    ["2025", "159", "7", "152", "2.63", "20", "2.36"],
    ["2026", "71", "1", "70", "3.06", "9", "2.85"],
    ["Total", "868", "235", "633", "3.16", "110", "3.05"]
  ], { bs: 18, hs: 17, numCols: [1, 2, 3, 4, 5, 6] }));
c.push(TabCap("Table A4. DNSE Entrade X reviews on Google Play, retrieved 20 to 21 September 2026. Generic means a retained review of four words or fewer carrying no theme."));

c.push(T([2700, 1300, 1300, 1300, 1300, 1720],
  ["Theme", "One and two star", "Three star", "Four and five star", "All retained", "Share of negatives"],
  [
    ["Crashes, freezes, login failures", "70", "5", "28", "103", "25.8 per cent"],
    ["Account opening and identity checks", "53", "4", "5", "62", "19.6 per cent"],
    ["Accusation of deception", "44", "2", "1", "47", "16.2 per cent"],
    ["Sign-up bonus terms", "26", "3", "6", "35", "9.6 per cent"],
    ["Deposits and withdrawals", "14", "2", "7", "23", "5.2 per cent"],
    ["Cannot close the account", "8", "0", "0", "8", "3.0 per cent"],
    ["Arrived through a social referral", "5", "0", "10", "15", "1.8 per cent"],
    ["Interface and charts", "3", "5", "25", "33", "1.1 per cent"],
    ["Charges differing from advertised", "4", "2", "5", "11", "1.5 per cent"],
    ["ZaloPay linkage", "2", "1", "2", "5", "0.7 per cent"],
    ["Idle cash earning feature", "0", "0", "4", "4", "0.0 per cent"]
  ], { bs: 18, hs: 17, numCols: [1, 2, 3, 4, 5] }));
c.push(TabCap("Table A5. Themes are non-exclusive, so the columns sum to more than the 633 retained reviews. Negatives number 271, neutrals 31 and positives 331."));

c.push(H2("A5. Primary data sources"));
c.push(T([2700, 6320],
  ["Dataset", "Address"],
  [
    ["DNSE investor relations", "https://www.dnse.com.vn/quan-he-nha-dau-tu"],
    ["HOSE market share announcements", "https://www.hsx.vn"],
    ["HNX market share announcements", "https://www.hnx.vn"],
    ["Vietnam Securities Depository account statistics", "https://vsdc.vn"],
    ["Global Findex Vietnam indicators", "https://api.worldbank.org/v2/sources/28/country/VNM/series/all/data?format=json"],
    ["Global Findex 2024 microdata", "https://microdata.worldbank.org/index.php/catalog/7998"],
    ["DNSE Entrade X reviews", "https://play.google.com/store/apps/details?id=vn.com.encapital.arrow"],
    ["VPS SmartOne reviews", "https://play.google.com/store/apps/details?id=vn.com.vpbs.smartone"],
    ["FPTS EzTrade reviews", "https://play.google.com/store/apps/details?id=com.fpts.eztrade"],
    ["National Statistics Office releases", "https://www.nso.gov.vn"]
  ], { bs: 18, hs: 18 }));
c.push(TabCap("Table A6. Addresses for every dataset used. The accompanying workbook contains the full extracted tables."));

// ======================================================= APPENDIX B
c.push(new Paragraph({ children: [new PageBreak()] }));
c.push(H1("Appendix B. Method, assumptions and limitations"));

c.push(H2("B1. Definitions and units"));
c.push(P("All currency figures are Vietnamese dong unless stated. Market share on HOSE, HNX and the derivatives market is defined by each exchange as a share of traded value on that market alone, so a figure from one exchange is never compared with a figure from another. Lending balances are margin loans plus advances against sale proceeds, which is the basis on which Vietstock compiles the industry total of VND 453,800 billion. Press estimates of margin lending alone for the same date cluster near VND 445,000 billion, and DNSE's share is 1.39 per cent on the first basis and 1.42 per cent on the second."));
c.push(P("Account share uses 13.80 million domestic individual accounts plus 52,633 foreign accounts at the end of August 2026 as the denominator. One investor may hold accounts at several firms, so the denominator counts accounts rather than people."));

c.push(H2("B2. Assumptions stated"));
c.push(Bullet("Half-year operating revenue is VND 848.2 billion, which reconciles with the two quarterly figures of VND 395.0 billion and VND 453.1 billion to within rounding."));
c.push(Bullet("DNSE's HOSE share is treated as below 2.94 per cent because the firm does not appear in the top ten and tenth place held 2.94 per cent. No point estimate is used."));
c.push(Bullet("Segment population shares applied in Table A3 come from the Findex country tables and the General Statistics Office 2024 population structure, applied to 80.6 million adults aged 15 and over."));
c.push(Bullet("Derivatives share between the first quarter of 2024 and the first quarter of 2025 was not published quarterly, and Figure 2 interpolates across that interval."));
c.push(Bullet("Segment indices use unweighted means. Any weighting chosen after inspecting the data would be fitted to the conclusion, so none was applied."));

c.push(H2("B3. Limitations"));
c.push(P("Four limitations affect the strength of the conclusions. Per-broker account counts are not published by any firm other than DNSE, so the account-to-activity comparison in Section 3.2 cannot be repeated for competitors and the finding rests on DNSE against the market average rather than against a named peer."));
c.push(P("Shareholders' equity for the relevant quarters appears only in scanned statements without a text layer, so lending headroom against the 200 per cent regulatory cap was not calculated and no ratio depending on it appears in this report."));
c.push(P("App store reviews are self-selected and over-represent dissatisfied users, so the theme frequencies in Figure 5 describe the composition of complaints rather than the incidence of problems across the customer base. The peer comparison in Figure 6 mitigates this partially, because the same selection bias applies to all three applications under the same cleaning rule. The VPS sample is capped at 1,200 by pagination and is therefore truncated toward recent reviews."));
c.push(P("Findex segments are reported one dimension at a time, so the intersection identified in Section 4.2 is inferred from three separate rankings rather than measured directly. The microdata file would allow the intersection to be measured, and that is the first extension proposed for Round 3."));

c.push(H2("B4. Accuracy checks performed"));
c.push(P("Every figure was traced to a primary disclosure or an exchange announcement. A verification pass against the first draft of this analysis corrected twelve figures. Three were material. An 8.8 per cent digital adoption rate belongs to micro enterprises and not to all small and medium enterprises. A count of 132.4 million biometric verifications measures customer records and not individuals. A share comparison set DNSE's Hanoi exchange position against competitor positions on the Ho Chi Minh exchange. That last error would have overstated the gap described in Section 3.2, and correcting it is why every market share figure in this report carries the name of its exchange."));

// ======================================================= REFERENCES
c.push(new Paragraph({ children: [new PageBreak()] }));
c.push(H1("References"));
const refs = [
  "DNSE Securities Joint Stock Company (2026) Consolidated financial statements for the second quarter of 2026 and investor relations releases for the first half of 2026. Hanoi.",
  "DNSE Securities Joint Stock Company (2026) Resolutions of the 2026 annual general meeting of shareholders. Hanoi.",
  "DNSE Securities Joint Stock Company (2026) Annual report 2025. Hanoi.",
  "FiinRatings (2026) Vietnam banking sector outlook 2026. Hanoi.",
  "Hanoi Stock Exchange (2026) Brokerage market share of the ten largest securities companies, listed shares, UPCoM and derivatives, second quarter and first half of 2026. Announcement of 7 July 2026.",
  "Ho Chi Minh Stock Exchange (2026) Brokerage market share of the ten largest securities companies, second quarter of 2026. Announcement of 7 July 2026.",
  "KPMG (2025) Vietnam 2026 outlook. October 2025.",
  "London Stock Exchange Group (2026) FTSE Russell interim country classification review and Vietnam reclassification, effective 21 September 2026.",
  "Mekong Asean (2026) Comparison of profit across the leading securities companies, second quarter 2026. July 2026.",
  "National Statistics Office of Vietnam (2026) Socio-economic performance in the second quarter and first half of 2026. Hanoi.",
  "State Bank of Vietnam (2026) Payment system statistics and biometric verification data, first half of 2026.",
  "UOB, PwC Singapore and the Singapore FinTech Association (2025) FinTech in ASEAN 2025.",
  "Vietnam Securities Depository and Clearing Corporation (2026) Monthly securities account statistics, August 2026.",
  "Vietstock (2026) Margin lending reaches a record VND 454 trillion, with divergence across the field. July 2026.",
  "Vietstock (2026) Brokerage market share on HNX and UPCoM shifts in the first half. 7 July 2026.",
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

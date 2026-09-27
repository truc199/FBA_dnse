#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""01d -- Market, macro and exchange data from primary sources, 2018 onwards, written to market_macro.json."""
import datetime
import io
import json
import os
import re
import ssl
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
import zipfile
import html as H

from pypdf import PdfReader

import sys as _sys, os as _os
_sys.path.insert(0, _os.path.dirname(_os.path.abspath(__file__)))
from paths import DATA  # all data files live in <repo>/data
HERE = DATA
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126 Safari/537.36"
START = "2018-01-01"

PRICE_URL = "https://trading.vietcap.com.vn/api/chart/OHLCChart/gap-chart"
VCI_HEADERS = {"Content-Type": "application/json", "Referer": "https://trading.vietcap.com.vn/",
               "Origin": "https://trading.vietcap.com.vn"}
SYMBOLS = {"VNINDEX": "VN-Index (HOSE)", "HNXIndex": "HNX-Index", "HNXUpcomIndex": "UPCoM-Index",
           "VN30F1M": "VN30 index futures, front month", "DSE": "DNSE Securities (HOSE: DSE)"}
FUTURES, FUTURES_MULTIPLIER = "VN30F1M", 100_000   # VND per index point per contract

WDI = {
    "NY.GDP.MKTP.KD.ZG": "GDP growth, per cent",
    "FP.CPI.TOTL.ZG": "Consumer price inflation, per cent",
    "NY.GDP.PCAP.CD": "GDP per capita, current USD",
    "NY.GNS.ICTR.ZS": "Gross savings, per cent of GDP",
    "NE.CON.PRVT.ZS": "Household consumption, per cent of GDP",
    "FR.INR.DPST": "Deposit interest rate, per cent",
    "FR.INR.LEND": "Lending interest rate, per cent",
    "FS.AST.PRVT.GD.ZS": "Domestic credit to the private sector, per cent of GDP",
    "FM.LBL.BMNY.GD.ZS": "Broad money, per cent of GDP",
    "CM.MKT.LCAP.GD.ZS": "Market capitalisation of listed companies, per cent of GDP",
    "CM.MKT.TRAD.GD.ZS": "Value of stocks traded, per cent of GDP",
    "SL.UEM.TOTL.ZS": "Unemployment, per cent of labour force",
    "PA.NUS.FCRF": "Official exchange rate, VND per USD",
    "SP.POP.TOTL": "Population",
    "IT.NET.USER.ZS": "Internet users, per cent of population",
}

HNX = "https://www.hnx.vn"
HNX_SEARCH_KEY = "thị phần môi giới"

# Year-end investor accounts managed by VSDC, from its annual reports (text PDFs, read 25 September 2026).
VSDC_AR = "https://vsdc.vn:9994/VSD_PORTAL//ckeditor/"
VSDC_ACCOUNTS = {
    # year: (total, domestic, foreign, opened in the year, report)
    "2018": (2182327, 2154033, 28294, 276547, "7TPTS2ePd95efBi89Fj0OQ/9RaEQ_BC 2018.pdf"),
    "2019": (2374894, 2342679, 32215, 213596, "7TPTS2ePd95efBi89Fj0OQ/kfWW2_BC 2019.pdf"),
    "2020": (2771409, 2736338, 35071, 401783, "145/57rJK_20210715_VSD_AR2020 - ban chuan up web.pdf"),
    "2021": (4310211, 4270701, 39510, None, "145/oY7bA_VSD_AR2021 - web.pdf"),
    "2022": (6897071, 6854360, 42711, 2608645, "145/C8oYp_20230906 VSD_AR2022 - web.pdf"),
    "2023": (7292361, 7246977, 45384, 1539304, "461/oEZuL_20240729_VSD_AR2023.pdf"),
    "2024": (9297988, 9250208, 47780, 2134838, "461/P5JeL_Final BCTN_20250711_VSDC_AR2024.pdf"),
    "2025": (11871933, 11821745, 50188, 2681838, "461/yvooS_Final_20260507 VSD AR2025.pdf"),
}
VSDC_LATEST = {"date": "2026-09-24", "investor_trading_accounts": 13887603, "source": "https://www.vsd.vn/vi/ (homepage counter)"}

# NSO 2026 releases, figures as stated in the text.
NSO = "https://www.nso.gov.vn/tin-tuc-thong-ke/2026/"
NSO_2026 = [
    ("GDP growth, Q1 2026", 7.94, "per cent y/y", NSO + "07/mot-so-net-chinh-tinh-hinh-kinh-te-xa-hoi-quy-ii-va-6-thang-dau-nam-2026/"),
    ("GDP growth, Q2 2026", 8.39, "per cent y/y", NSO + "07/mot-so-net-chinh-tinh-hinh-kinh-te-xa-hoi-quy-ii-va-6-thang-dau-nam-2026/"),
    ("GDP growth, H1 2026", 8.18, "per cent y/y", NSO + "07/mot-so-net-chinh-tinh-hinh-kinh-te-xa-hoi-quy-ii-va-6-thang-dau-nam-2026/"),
    ("Average monthly income of workers, Q2 2026", 9.0, "VND million, about", NSO + "07/mot-so-net-chinh-tinh-hinh-kinh-te-xa-hoi-quy-ii-va-6-thang-dau-nam-2026/"),
    ("Exports, H1 2026", 21.0, "per cent y/y", NSO + "07/mot-so-net-chinh-tinh-hinh-kinh-te-xa-hoi-quy-ii-va-6-thang-dau-nam-2026/"),
    ("Imports, H1 2026", 33.4, "per cent y/y", NSO + "07/mot-so-net-chinh-tinh-hinh-kinh-te-xa-hoi-quy-ii-va-6-thang-dau-nam-2026/"),
    ("CPI, June 2026", 4.69, "per cent y/y", NSO + "07/chi-so-gia-tieu-dung-chi-so-gia-vang-va-chi-so-gia-do-la-my-thang-sau-quy-ii-va-6-thang-dau-nam-2026/"),
    ("Core inflation, June 2026", 4.50, "per cent y/y", NSO + "07/chi-so-gia-tieu-dung-chi-so-gia-vang-va-chi-so-gia-do-la-my-thang-sau-quy-ii-va-6-thang-dau-nam-2026/"),
    ("CPI, August 2026", 4.89, "per cent y/y", NSO + "09/mot-so-net-chinh-tinh-hinh-kinh-te-xa-hoi-thang-tam-va-8-thang-nam-2026/"),
    ("CPI, average of eight months 2026", 4.45, "per cent y/y", NSO + "09/mot-so-net-chinh-tinh-hinh-kinh-te-xa-hoi-thang-tam-va-8-thang-nam-2026/"),
    ("Retail sales, August 2026", 14.9, "per cent y/y", NSO + "09/mot-so-net-chinh-tinh-hinh-kinh-te-xa-hoi-thang-tam-va-8-thang-nam-2026/"),
]


# hnx.vn serves its certificate without the intermediate, so verification fails; the pages are public and read-only.
_HNX_CTX = ssl.create_default_context()
_HNX_CTX.check_hostname = False
_HNX_CTX.verify_mode = ssl.CERT_NONE


def http(url, data=None, headers=None, tries=4):
    ctx = _HNX_CTX if "hnx.vn" in url else None
    for attempt in range(tries):
        try:
            req = urllib.request.Request(url, data=data, headers={"User-Agent": UA, **(headers or {})})
            with urllib.request.urlopen(req, timeout=90, context=ctx) as r:
                return r.read()
        except (urllib.error.URLError, TimeoutError):
            if attempt == tries - 1:
                raise
            time.sleep(3 * (attempt + 1))


# ---------------------------------------------------------------- prices
def prices(symbol):
    body = json.dumps({"timeFrame": "ONE_DAY", "symbols": [symbol], "to": int(time.time()), "countBack": 2600}).encode()
    d = json.loads(http(PRICE_URL, body, VCI_HEADERS))[0]
    rows = []
    for t, c, v, val in zip(d["t"], d["c"], d["v"], d["accumulatedValue"]):
        day = datetime.datetime.fromtimestamp(int(t), datetime.timezone.utc).date().isoformat()
        if day < START or not v:
            continue
        if symbol == FUTURES:
            # The service's futures value is unusable before 22 July 2024, so use contracts x close x multiplier.
            bn = round(v * c * FUTURES_MULTIPLIER / 1e9, 3)
        else:
            # Value arrives in dong until 11 August 2025 and in VND million after; no day's value reaches 1e9 million.
            bn = None if val is None else round(val / 1e9 if val >= 1e9 else val / 1e3, 3)
        rows.append([day, c, v, bn])
    return rows


def annual(rows):
    out = {}
    for y in sorted({r[0][:4] for r in rows}):
        yr = [r for r in rows if r[0][:4] == y]
        vals = [r[3] for r in yr if r[3] is not None]
        out[y] = {"close": yr[-1][1], "last_date": yr[-1][0], "trading_days": len(yr),
                  "avg_daily_value_bn": round(sum(vals) / len(vals), 1) if vals else None}
    years = list(out)
    for prev, y in zip(years, years[1:]):
        out[y]["change_pct"] = round((out[y]["close"] / out[prev]["close"] - 1) * 100, 2)
    return out


# ---------------------------------------------------------------- World Bank
def wdi():
    url = (f"https://api.worldbank.org/v2/country/VNM/indicator/{';'.join(WDI)}"
           f"?format=json&date=2018:{datetime.date.today().year}&per_page=2000&source=2")
    meta, rows = json.loads(http(url))
    out = {k: {"label": v, "values": {}} for k, v in WDI.items()}
    for r in rows or []:
        if r["value"] is not None:
            out[r["indicator"]["id"]]["values"][r["date"]] = r["value"]
    return meta.get("lastupdated"), out


# ---------------------------------------------------------------- HNX brokerage market share
def hnx_notices():
    """Every notice the HNX site search returns for the key, oldest first."""
    items, page = [], 1
    while True:
        data = urllib.parse.urlencode({"key": HNX_SEARCH_KEY, "pCurrentPage": page}).encode()
        h = http(HNX + "/ModuleSearchALL/SearchDataHNX/SearchArticleByKey", data,
                 {"X-Requested-With": "XMLHttpRequest",
                  "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"}).decode("utf-8", "ignore")
        found = re.findall(r'href="([^"]+)" title="([^"]+)">[^<]*</a>\s*<span class="divArticlesPublicTime">\[([^\]]+)\]', h)
        if not found or page > 40:
            return items
        items += [(d, H.unescape(t), href) for href, t, d in found]
        page += 1


def quarter_of(title):
    if re.search(r"6 tháng|năm \d{4}\s*$|dẫn đầu", title, re.I):
        return None
    m = re.search(r"[Qq]u[ýy]\s*(IV|III|II|I|\d)\s*(?:/|năm)\s*(\d{4})", title)
    if not m:
        return None
    q = {"I": 1, "II": 2, "III": 3, "IV": 4}.get(m.group(1), m.group(1))
    return f"{m.group(2)}Q{q}"


def market_of(text):
    t = text.lower()
    if "phái sinh" in t or "tương lai" in t:
        return "derivatives"
    if "upcom" in t:
        return "upcom"
    if "trái phiếu" in t or "công cụ nợ" in t:
        return None
    if "niêm yết" in t or "cổ phiếu" in t or "chứng khoán lớn nhất" in t:
        return "listed"
    return None


def notice_text(path):
    h = http(HNX + "/vi-vn" + path).decode("utf-8", "ignore")
    body = re.sub(r"<script.*?</script>|<style.*?</style>", " ", h, flags=re.S)
    parts = [H.unescape(re.sub(r"<[^>]+>", " ", body))]
    for a in re.findall(r'href="(https?://owa\.hnx\.vn[^"]+\.(?:pdf|docx?|PDF|DOCX?))"', h):
        b = http(urllib.parse.quote(a, safe=":/%"))
        low = a.lower()
        if low.endswith(".pdf"):
            parts.append("\n".join(p.extract_text() or "" for p in PdfReader(io.BytesIO(b)).pages))
        elif low.endswith(".docx"):
            parts.append(re.sub(r"<[^>]+>", " ", zipfile.ZipFile(io.BytesIO(b)).read("word/document.xml").decode("utf-8")))
        else:   # Word 97 keeps its text as UTF-16, with control characters between table cells
            parts.append(re.sub(r"[\x00-\x1f]", " ", b.decode("utf-16-le", "ignore")))
    return re.sub(r"\s+", " ", " ".join(parts).replace("|", " "))


ROW = re.compile(r"(?<![\d,.])(\d{1,2}) ((?:Công ty|CTCP|CTCK|Chứng khoán|Công Ty)[^%]{3,140}?) (\d{1,2}[,.]\d{1,2}) ?%")
HEADING = re.compile(r"(?i)(?:top\s+)?(?:mười\s*\(10\)|10\s*\(mười\))[^:]{0,220}:")


def tables_in(text, title_market):
    heads = [(m.start(), market_of(m.group(0))) for m in HEADING.finditer(text)]
    if not heads:
        heads = [(0, title_market)]
    out = {}
    for i, (pos, market) in enumerate(heads):
        end = heads[i + 1][0] if i + 1 < len(heads) else len(text)
        rows = [[int(r), re.sub(r"\s+", " ", n).strip(), float(s.replace(",", "."))] for r, n, s in ROW.findall(text[pos:end])]
        seen, clean = set(), []
        for r in rows:
            if r[0] not in seen and 1 <= r[0] <= 50:
                seen.add(r[0])
                clean.append(r)
        if market and clean and market not in out:
            out[market] = sorted(clean)
    return out


def hnx_market_share():
    notices = [n for n in hnx_notices() if int(n[0][-4:]) >= 2018]
    tables, used = {}, []
    for date, title, path in notices:
        period = quarter_of(title)
        if not period:
            continue
        try:
            found = tables_in(notice_text(path), market_of(title))
        except Exception as e:                                  # one unreadable notice should not stop the pull
            print(f"  skipped {path}: {e}")
            continue
        for market, rows in found.items():
            tables.setdefault(market, {})[period] = rows            # later notices, including corrections, win
            used.append({"date": date, "title": title, "url": HNX + "/vi-vn" + path, "market": market, "period": period})
    dnse = {}
    for market, by_period in tables.items():
        for period, rows in sorted(by_period.items()):
            hit = next((r for r in rows if re.search(r"DNSE|Đại Nam", r[1])), None)
            tenth = next((r[2] for r in rows if r[0] == 10), None)
            dnse.setdefault(market, {})[period] = {"share": hit[2] if hit else None, "rank": hit[0] if hit else None,
                                                   "tenth_place_share": tenth}
    return {"notices_used": used, "tables": tables, "dnse": dnse}


# ---------------------------------------------------------------- HOSE brokerage market share
HOSE_NEWS = "https://api.hsx.vn/n/api/v1/1/news"
HOSE_HEADERS = {"Accept": "application/json", "Origin": "https://www.hsx.vn", "Referer": "https://www.hsx.vn/"}


def hose_quarter_table(summary):
    """The top-ten table whose heading names a quarter rather than the half year or the year."""
    for heading, table in re.findall(r"(.{0,600}?)(<table.*?</table>)", summary, flags=re.S):
        head = H.unescape(re.sub(r"<[^>]+>", " ", heading)).upper()
        if "QUÝ" not in head:
            continue
        rows = []
        for tr in re.findall(r"<tr>(.*?)</tr>", table, flags=re.S):
            cells = [re.sub(r"\s+", " ", H.unescape(re.sub(r"<[^>]+>", " ", c))).strip()
                     for c in re.findall(r"<td[^>]*>(.*?)</td>", tr, flags=re.S)]
            share = next((c for c in reversed(cells) if c.endswith("%")), None)
            if cells and cells[0].isdigit() and share:
                rows.append([int(cells[0]), cells[1], float(share.rstrip("%").replace(",", "."))])
        if rows:
            return rows
    return None


def hose_market_share(first_year=2018):
    tables, used = {}, []
    today = datetime.date.today()
    for year in range(first_year, today.year + 1):
        for q in range(1, 5):
            start = datetime.date(year, 3 * q, 1) + datetime.timedelta(days=31)
            start = start.replace(day=1)
            if start > today:
                break
            end = start + datetime.timedelta(days=20)
            qs = urllib.parse.urlencode({"pageIndex": 1, "pageSize": 500, "startDate": start.isoformat(),
                                         "endDate": end.isoformat()})
            news = json.loads(http(f"{HOSE_NEWS}/newstype/-1/1?{qs}", headers=HOSE_HEADERS))["data"]["list"]
            for item in news:
                if not re.search(r"thị phần.*môi giới|môi giới.*thị phần", item["title"], re.I):
                    continue
                summary = json.loads(http(f"{HOSE_NEWS}/{item['id']}", headers=HOSE_HEADERS))["data"].get("summary") or ""
                rows = hose_quarter_table(summary)
                if rows:
                    tables[f"{year}Q{q}"] = rows
                    used.append({"period": f"{year}Q{q}", "title": item["title"], "id": item["id"]})
                    break
    dnse = {p: {"share": next((r[2] for r in rows if "DNSE" in r[1]), None),
                "tenth_place_share": next((r[2] for r in rows if r[0] == 10), None),
                "top_ten_combined": round(sum(r[2] for r in rows if r[0] <= 10), 2)} for p, rows in tables.items()}
    return {"source": HOSE_NEWS, "notices_used": used, "tables": tables, "dnse": dnse}


if __name__ == "__main__":
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    out = {"pulled": datetime.date.today().isoformat(), "prices": {}}
    for sym, label in SYMBOLS.items():
        rows = prices(sym)
        out["prices"][sym] = {"label": label, "source": PRICE_URL, "columns": ["date", "close", "volume", "value_bn"],
                              "daily": rows, "annual": annual(rows)}
        print(f"{sym:14} {rows[0][0]} to {rows[-1][0]}, {len(rows)} days, last close {rows[-1][1]}")
    out["wdi_updated"], out["wdi"] = wdi()
    print(f"World Bank WDI, last updated {out['wdi_updated']}: {sum(len(v['values']) for v in out['wdi'].values())} values")
    out["hnx_market_share"] = hnx_market_share()
    print(f"HNX notices used: {len(out['hnx_market_share']['notices_used'])}")
    out["hose_market_share"] = hose_market_share()
    print(f"HOSE quarters found: {sorted(out['hose_market_share']['tables'])}")
    out["vsdc_accounts"] = {y: {"total": t, "domestic": d, "foreign": f, "opened": o, "source": VSDC_AR + src}
                            for y, (t, d, f, o, src) in VSDC_ACCOUNTS.items()}
    out["vsdc_latest"] = VSDC_LATEST
    out["nso_2026"] = [{"indicator": i, "value": v, "unit": u, "source": s} for i, v, u, s in NSO_2026]
    with open(os.path.join(HERE, "market_macro.json"), "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, separators=(",", ":"))
    print("Wrote market_macro.json.\n")

    print("DNSE on HNX, share % (rank; tenth place)")
    for market, by_period in out["hnx_market_share"]["dnse"].items():
        print(f"  {market}: " + ", ".join(f"{p} {d['share'] if d['share'] is not None else '-'}"
                                          f"({d['rank'] or '>10'}; {d['tenth_place_share']})" for p, d in by_period.items()))
    print("\nVN-Index and HOSE value by year")
    for y, a in out["prices"]["VNINDEX"]["annual"].items():
        print(f"  {y}: close {a['close']:.2f}, change {a.get('change_pct', '-')}, average daily value {a['avg_daily_value_bn']:,.0f} bn")

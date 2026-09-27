"""Re-run the whole analysis, from the data in data/ to the figures, tables and rebuilt report.

    python run_all.py                  clean the reviews, rebuild the segment model, draw the figures,
                                       recompute and check the tables, rebuild the report (Word; PDF too
                                       when LibreOffice is installed)
    python run_all.py --fetch          first download the data again from the original sources
    python run_all.py --no-report      stop after the tables
    python run_all.py --paginate       recompute the page numbers of the contents lists (needs LibreOffice)

The data in data/ is the snapshot used for the report. --fetch replaces it with whatever the sources
publish today, so figures and tables will then differ from the report.
"""
import argparse
import os
import shutil
import subprocess
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent
PIPE = ROOT / "src" / "pipeline"
PLAY_APPS = ["vn.com.encapital.arrow", "vn.com.vpbs.smartone", "com.fpts.eztrade"]


def run(script, *args, optional=False):
    cmd = [sys.executable, str(script), *map(str, args)]
    print(f"\n$ python {Path(script).relative_to(ROOT)} {' '.join(map(str, args))}".rstrip(), flush=True)
    env = dict(os.environ, PYTHONIOENCODING="utf-8", PYTHONUTF8="1")
    result = subprocess.run(cmd, cwd=ROOT, env=env)
    if result.returncode != 0:
        if optional:
            print(f"  (skipped: {Path(script).name} exited with status {result.returncode})")
            return False
        sys.exit(f"stopped: {Path(script).name} exited with status {result.returncode}")
    return True


def stage(title):
    print(f"\n{'=' * 78}\n{title}\n{'=' * 78}", flush=True)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--fetch", action="store_true", help="download the data again before the analysis")
    ap.add_argument("--no-report", action="store_true", help="skip the report rebuild")
    ap.add_argument("--paginate", action="store_true", help="recompute page numbers with LibreOffice")
    a = ap.parse_args()
    t0 = time.time()

    if a.fetch:
        stage("0. Fetch data from the sources (overwrites data/)")
        run(PIPE / "01_findex_fetch.py")
        run(PIPE / "01b_dnse_financials_fetch.py")
        run(PIPE / "01c_peer_financials_fetch.py")
        run(PIPE / "01d_market_macro_fetch.py")
        run(PIPE / "02b_playstore_scrape_python.py", optional=True)   # needs google-play-scraper
        run(PIPE / "02c_appstore_scrape.py", optional=True)

    stage("1. Clean and tag the app reviews")
    run(PIPE / "03_reviews_clean.py", "--selftest")
    for app in PLAY_APPS:
        run(PIPE / "03_reviews_clean.py", ROOT / "data" / f"reviews_raw_{app}.csv")
    run(PIPE / "03b_reviews_tables.py")

    stage("2. Findex segment model")
    run(PIPE / "04_segment_model.py")

    stage("3. Figures (outputs/figures)")
    run(ROOT / "src" / "figures" / "make_figures.py")

    stage("4. Tables (outputs/tables)")
    run(ROOT / "src" / "tables" / "export_tables.py")
    run(ROOT / "src" / "tables" / "make_tables.py")
    run(ROOT / "src" / "tables" / "check_tables.py", optional=True)

    if not a.no_report:
        stage("5. Rebuild the report (outputs/report)")
        has_office = any(shutil.which(n) for n in ("soffice", "libreoffice")) or any(
            Path(p).exists() for p in (r"C:\Program Files\LibreOffice\program\soffice.exe",
                                       "/Applications/LibreOffice.app/Contents/MacOS/soffice"))
        flags = (["--paginate"] if a.paginate else []) + (["--pdf"] if has_office else [])
        run(ROOT / "src" / "report" / "build_report.py", *flags)

    print(f"\nDone in {time.time() - t0:.0f} s.")


if __name__ == "__main__":
    main()

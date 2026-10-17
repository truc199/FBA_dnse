"""Runs the Round 3 pipeline: model test, cohort model, plan tables, review coding, deck tables, charts,
diagrams, the check of the deck content and reports, the Word file for team review, and the English and
Vietnamese companion reports (Word and PDF).

Round 2 files are only read, never written; run_all.py is unchanged.

Run from the repository root: python src/round3/run_round3.py
"""
import subprocess
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
STEPS = ["test_payday_model.py", "payday_model.py", "plan_tables.py", "reviews_2026.py", "deck_tables.py",
         "figures_round3.py", "diagrams_round3.py", "check_deck_content.py", "build_content_docx.py",
         "build_report_docx.py"]


def main():
    t0 = time.time()
    for step in STEPS:
        print(f"\n$ python src/round3/{step}")
        if subprocess.run([sys.executable, str(HERE / step)], cwd=HERE.parents[1]).returncode != 0:
            print(f"\nFAILED at {step}")
            return 1
    print(f"\nDone in {time.time() - t0:.0f} s.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

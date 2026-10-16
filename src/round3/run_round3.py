"""Runs the Round 3 pipeline: model test, cohort model, review coding, figures.

Round 2 files are only read, never written; run_all.py is unchanged.

Run from the repository root: python src/round3/run_round3.py
"""
import subprocess
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
STEPS = ["test_payday_model.py", "payday_model.py", "reviews_2026.py", "figures_round3.py"]


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

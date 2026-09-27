"""Draw every figure in the report into outputs/figures/."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from figures import charts, diagrams  # noqa: E402


def main():
    for fn in charts.ALL + diagrams.ALL:
        fn()


if __name__ == "__main__":
    main()

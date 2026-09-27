"""Shared locations for the pipeline scripts: every data file lives in <repo>/data."""
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(SCRIPT_DIR))
DATA = os.path.join(ROOT, "data")

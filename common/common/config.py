"""Project configuration"""
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent.parent

ASSETS_PATH = ROOT_DIR / "assets"
FIGS_PATH =  ASSETS_PATH / "figs"
OUTPUT_PATH = FIGS_PATH / "output"

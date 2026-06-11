from pathlib import Path

REPO_ROOT = Path("/content/Y3_EPA_NHS-Staff-Survey_NLP-Hybrid-Workflow")

DATA_DIR = REPO_ROOT / "data"
RAW_DIR = DATA_DIR / "raw"
PROCESSED_DIR = DATA_DIR / "processed"

STAFF_SURVEY_FILES = {
    2020: RAW_DIR / "20 NSS Free Text.xlsx",
    2021: RAW_DIR / "21 NSS Free Text.xlsx",
    2022: RAW_DIR / "22 NSS Free Text.xlsx",
    2023: RAW_DIR / "23 NSS Free Text.xlsx",
    2024: RAW_DIR / "24 NSS Free Text.xlsx",
    2025: RAW_DIR / "25 NSS Free Text.xlsx",
}

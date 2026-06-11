from pathlib import Path

REPO_ROOT = Path("/content/Y3_EPA_NHS-Staff-Survey_NLP-Hybrid-Workflow")

DATA_DIR = REPO_ROOT / "data"
RAW_DIR = DATA_DIR / "raw"
PROCESSED_DIR = DATA_DIR / "processed"


# Add this dictionary so pipeline/load.py can import it
STAFF_SURVEY_FILES = {
    2020: RAW_DIR / "2020 NSS Free Text.csv",
    2021: RAW_DIR / "2021 NSS Free Text.csv",
    2022: RAW_DIR / "2022 NSS Free Text.csv",
    2023: RAW_DIR / "2023 NSS Free Text.csv",
    2024: RAW_DIR / "2024 NSS Free Text.csv",
    2025: RAW_DIR / "2025 NSS Free Text.csv",
}

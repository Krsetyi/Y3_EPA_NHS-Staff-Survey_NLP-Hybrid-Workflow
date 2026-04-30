from pathlib import Path

# Placeholder paths – real ones set in Colab
DATA_DIR = Path("/content/data")
RAW_DIR = DATA_DIR / "raw"
PROCESSED_DIR = DATA_DIR / "processed"

# Add this dictionary so pipeline/load.py can import it
STAFF_SURVEY_FILES = {
    2020: RAW_DIR / "2020.csv",
    2021: RAW_DIR / "2021.csv",
    2022: RAW_DIR / "2022.csv",
    2023: RAW_DIR / "2023.csv",
  2024: RAW_DIR / "2024/csv",
  2025: RAW_DIR / "2025.csv"
}

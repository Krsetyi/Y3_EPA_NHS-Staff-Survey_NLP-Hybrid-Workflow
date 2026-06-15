import pandas as pd
from config.paths import STAFF_SURVEY_FILES

# Unified schema for NLP years
REQUIRED_COLUMNS = [
    "comment_id",
    "free_text",
    "year",
    "org_code",
    "prompt_type",
    "care_group",
]

def _generate_ids(year: int, n: int) -> list[str]:
    """Generate zero-padded IDs like 2024_000001."""
    return [f"{year}_{i:06d}" for i in range(1, n + 1)]


def load_year(year: int) -> pd.DataFrame:
    """
    Load a single year of NSS free-text data.
    2023–2025 → fully normalised for NLP pipeline.
    2020–2022 → loaded raw (not NLP-ready).
    """
    path = STAFF_SURVEY_FILES[year]

    # Read Excel or CSV
    if path.suffix.lower() in [".xlsx", ".xls"]:
        df = pd.read_excel(path, sheet_name="Sheet1" if year == 2025 else 0)
    else:
        df = pd.read_csv(path)

    # -----------------------------
    # YEARS NOT USED FOR NLP (2020–2022)
    # -----------------------------
    if year in [2020, 2021, 2022]:
        df["year"] = year
        return df  # raw, unstructured, for context only

    # -----------------------------
    # NLP YEARS (2023–2025)
    # -----------------------------
    if year == 2023:
        df = df.rename(columns={
            "ID": "comment_id",
            "Comment": "free_text",
        })
        df["care_group"] = None

    elif year == 2024:
        df = df.rename(columns={
            "Comment": "free_text",
        })
        df["comment_id"] = _generate_ids(2024, len(df))
        df["care_group"] = None

    elif year == 2025:
        df = df.rename(columns={
            "Comment": "free_text",
            "NB1": "care_group",
        })
        df["comment_id"] = _generate_ids(2025, len(df))

    # Add shared metadata
    df["year"] = year
    df["org_code"] = None
    df["prompt_type"] = "Any other comments"

    # Keep only required columns
    df = df[REQUIRED_COLUMNS]

    return df


def load_all_years(years: list[int]) -> pd.DataFrame:
    """Load and combine multiple years."""
    frames = [load_year(y) for y in years if y >= 2023]
    return pd.concat(frames, ignore_index=True)


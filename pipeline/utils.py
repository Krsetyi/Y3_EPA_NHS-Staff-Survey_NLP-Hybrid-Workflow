utils_path = "/content/Y3_EPA_NHS-Staff-Survey_NLP-Hybrid-Workflow/pipeline/utils.py"

clean_utils = """import logging

# ---------------------------------------------------------
# Logger
# ---------------------------------------------------------
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

if not logger.handlers:
    handler = logging.StreamHandler()
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    handler.setFormatter(formatter)
    logger.addHandler(handler)


# ---------------------------------------------------------
# Preprocessing entry point
# ---------------------------------------------------------
def run_preprocessing(years: list[int]):
    \"""
    Full preprocessing pipeline:
    - Load all years
    - Rename free_text_response to comment_text
    - Clean text
    - Return processed dataframe
    \"""
    from .utils import logger
    from .load import load_all_years
    from .clean import clean_dataframe

    logger.info("Loading data for years: %s", years)

    df = load_all_years(years)

    # Normalise column name
    if "free_text_response" in df.columns:
        df = df.rename(columns={"free_text_response": "comment_text"})

    df = clean_dataframe(df, text_column="comment_text")

    logger.info("Preprocessing complete. Rows: %d", len(df))
    return df
"""

with open(utils_path, "w") as f:
    f.write(clean_utils)

print("utils.py overwritten CLEANLY.")

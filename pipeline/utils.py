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
    from .utils import logger
    from .load import load_all_years
    from .clean import clean_dataframe

    logger.info("Loading data for years: %s", years)

    df = load_all_years(years)

    # --- Normalise column names ---
    df.columns = [c.strip().lower() for c in df.columns]

    # --- Map any known text column to comment_text ---
    TEXT_COLS = [
        "free_text_response",
        "comment",
        "comments",
        "comment_text",
        "response",
        "response_text",
        "nb1",
        "question text",
        "question_text",
        "column 1",
        "column 2",
    ]

    text_col = None
    for col in df.columns:
        if col in TEXT_COLS:
            text_col = col
            break

    if text_col is None:
        raise KeyError("No text column found in dataframe.")

    df = df.rename(columns={text_col: "comment_text"})

    # --- Clean text ---
    df = clean_dataframe(df, text_column="comment_text")

    logger.info("Preprocessing complete. Rows: %d", len(df))
    return df

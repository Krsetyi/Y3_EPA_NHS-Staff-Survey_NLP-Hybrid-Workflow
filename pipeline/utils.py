import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

if not logger.handlers:
    handler = logging.StreamHandler()
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    handler.setFormatter(formatter)
    logger.addHandler(handler)

def run_preprocessing(years: list[int]):
    """
    Full preprocessing pipeline:
    - Load all years
    - Normalise text column names
    - Rename to comment_text for pipeline compatibility
    - Clean text
    - Return processed dataframe
    """
    from .utils import logger
    from .load import load_all_years
    from .clean import clean_dataframe

    logger.info("Loading data for years: %s", years)

    # Load and normalise
    df = load_all_years(years)

    # Rename unified column to what the pipeline expects
    if "free_text_response" in df.columns:
        df = df.rename(columns={"free_text_response": "comment_text"})

    # Clean text
    df = clean_dataframe(df, text_column="comment_text")

    logger.info("Preprocessing complete. Rows: %d", len(df))
    return df

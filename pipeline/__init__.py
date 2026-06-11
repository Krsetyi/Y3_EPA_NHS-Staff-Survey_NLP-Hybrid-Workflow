from pathlib import Path

run_preprocessing_block = """
def run_preprocessing(years: list[int]):
    from .utils import logger
    from .load import load_all_years
    from .clean import clean_dataframe

    logger.info("Loading data for years: %s", years)

    df = load_all_years(years)

    # Your files all use free_text_response
    if "free_text_response" in df.columns:
        df = df.rename(columns={"free_text_response": "comment_text"})

    df = clean_dataframe(df, text_column="comment_text")

    logger.info("Preprocessing complete. Rows: %d", len(df))
    return df
"""

for rel in ["pipeline/__init__.py", "pipeline/utils.py"]:
    fpath = REPO_ROOT / rel
    with open(fpath, "w") as f:
        f.write(run_preprocessing_block)

print("run_preprocessing overwritten in both files.")


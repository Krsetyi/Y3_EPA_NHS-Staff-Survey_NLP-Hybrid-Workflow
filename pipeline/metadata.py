Goal: Add derived fields that will be useful later (and for analysis)

import pandas as pd
def add_metadata(df: pd.DataFrame) -> pd.DataFrame:
  df = df.copy()
  df["comment_length"] = df["comment_clean"].str.len()
  df["has_text"] = df["comment_length"] > 0
  return df

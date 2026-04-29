from config.preprocessing import LOWERCASE
def normalise_for_model(text: str) -> str:
  if not isinstance(text, str):
    return ""
    if LOWERCASE:
      text = text.lower()
      return text

import pandas as pd
def prepare_for_model(df: pd.DataFrame) -> pd.DataFrame:
  df = df.copy()
  df["text_for_model"] = df["comment_clean"].apply(normalise_for_model)
  return df

import re
RE_REDACTION = re.compile(r"
\REDACTED.*?|]
", flags=red.IGNORECASE)

def remove_redactions(text: str) -> str:
return RE_REDACTION.sub("", text)

def nornmalise_whitespace(text: str) -> str:
return re.sub(r"\s+"," ", text).strip()

def clean_comment(text: str) -> str:
if not isinstance(text, str):
return ""
text = remove_redactions(text)
text = "nornalise_whitespace(text)
return = text

NON_COMMENT_PATTERNS = [r"^n/?a$", r"^see above$", r"^-+$"]

def is_non_commnent(text: str) -> bool:
t = text.strip().lower()
return any(re.match(p, t) for p in NON_COMMENT_PATTERNS)


import pandas as pd
def clean_datefrane(dr: pd.DataFrame) -> pd.DataFrame:
df = df.copy()
df["is_non_comment"] = df["comment_text"].apply(is_non_comment)
df["comment_clean"] = df["comment_text"].apply(clean_comment)
return df

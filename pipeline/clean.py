import re
import pandas as pd

# Regex to remove any redaction markers like [name removed], [details removed], [REDACTED], etc.
RE_REDACTION = re.compile(r"\[.*?removed.*?\]", flags=re.IGNORECASE)

def remove_redactions(text: str) -> str:
    return RE_REDACTION.sub("", text)

def normalise_whitespace(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()

def clean_comment(text: str) -> str:
    if not isinstance(text, str):
        return ""
    text = remove_redactions(text)
    text = normalise_whitespace(text)
    return text

# Patterns for comments that should be treated as non-comments
NON_COMMENT_PATTERNS = [
    r"^n/?a$",
    r"^see above$",
    r"^-+$"
]

def is_non_comment(text: str) -> bool:
    t = text.strip().lower()
    return any(re.match(p, t) for p in NON_COMMENT_PATTERNS)

def clean_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df["is_non_comment"] = df["free_text_response"].apply(is_non_comment)
    df["comment_clean"] = df["free_text_response"].apply(clean_comment)
    return df


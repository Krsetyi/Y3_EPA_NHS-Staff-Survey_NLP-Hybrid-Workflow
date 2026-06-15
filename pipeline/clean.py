import re
import pandas as pd

# Build the pattern safely without raw strings
pattern_removed = re.escape("[removed]")
pattern_name_removed = re.escape("[name removed]")
pattern_details_removed = re.escape("[details removed]")

# Combine into one regex
RE_REDACTION = re.compile(
    f"{pattern_removed}|{pattern_name_removed}|{pattern_details_removed}",
    flags=re.IGNORECASE
)

def remove_redactions(text: str) -> str:
    if not isinstance(text, str):
        return ""
    return RE_REDACTION.sub("", text)

def normalise_whitespace(text: str) -> str:
    return " ".join(text.split())

def clean_comment(text: str) -> str:
    if not isinstance(text, str):
        return ""
    text = remove_redactions(text)
    text = normalise_whitespace(text)
    return text

NON_COMMENT_PATTERNS = [
    r"^n/?a$",
    r"^see above$",
    r"^-+$"
]

def is_non_comment(text: str) -> bool:
    if not isinstance(text, str):
        return True
    t = text.strip().lower()
    return any(re.match(p, t) for p in NON_COMMENT_PATTERNS)

def clean_dataframe(df: pd.DataFrame, text_column: str = "comment_text") -> pd.DataFrame:
    df = df.copy()
    df["is_non_comment"] = df[text_column].apply(is_non_comment)
    df["comment_clean"] = df[text_column].apply(clean_comment)
    return df

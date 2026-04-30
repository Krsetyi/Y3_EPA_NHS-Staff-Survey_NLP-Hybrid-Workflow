REQUIRED_COLUMNS = [
  "comment_id",
  "comment_text",
  "year",
  "org_code",
  "prompt_type",
]

# load_year function
def load_year(year: int) -> pd.DataFrame:
    path = STAFF_SURVEY_FILES[year]

    # Choose reader based on file extension
    if path.suffix.lower() in [".xlsx", ".xls"]:
        df = pd.read_excel(path)
    else:
        df = pd.read_csv(path)

    # basic validation
    missing = [c for c in REQUIRED_COLUMNS if c not in df.columns]
    if missing:
        raise ValueError(f"Missing columns for {year}: {missing}")

    return df

# load_all_years function
def load_all_years(years: list[int]) -> pd.DataFrame:
  frames = [load_year(y) for y in years]
  df = pd.concat(frames, ignore_index=True)
  return df

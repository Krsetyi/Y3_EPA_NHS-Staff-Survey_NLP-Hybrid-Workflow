from .load import load_all_years
from .clean import clean_dataframe
from .metadata import add_metadata
from .prepare import prepare_for_model

def run_preprocessing(years):
    """
    Run the full preprocessing pipeline:
    - Load raw data for given years
    - Clean text (redactions, whitespace, non-comments)
    - Add metadata (length, flags)
    - Prepare text for modelling
    """
    df = load_all_years(years)
    df = clean_dataframe(df)
    df = add_metadata(df)
    df = prepare_for_model(df)
    return df

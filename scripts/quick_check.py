from pipeline import run_preprocessing
df = run_preprocessing([2022])
df.head()
df["comment_clean"].sample(10)

# check for no obvious broken text, redactions removed, non-comments flagged, text_for_model looks sensible

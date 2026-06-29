import pandas as pd
import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

def run_multilabel_classification(df, taxonomy_path):
    taxonomy = pd.read_csv(taxonomy_path, encoding="ISO-8859-1")

    # Load cue phrases
    taxonomy["cue_list"] = taxonomy["SFTT_Cues"].fillna("").apply(
        lambda x: [c.strip() for c in x.split(";") if c.strip()]
    )

    # Load embedding model
    model = SentenceTransformer("sentence-transformers/all-mpnet-base-v2")

    # Encode cue phrases
    cue_embeddings = model.encode(
        taxonomy["cue_list"].apply(lambda cues: " ".join(cues)).tolist(),
        normalize_embeddings=True
    )

    # Encode comments
    comment_embeddings = model.encode(
        df["comment_clean"].fillna("").tolist(),
        normalize_embeddings=True
    )

    # Compute cosine similarity
    sims = cosine_similarity(comment_embeddings, cue_embeddings)

    # Threshold for assignment
    THRESHOLD = 0.35

    multilabels = []
    for i in range(len(df)):
        row_sims = sims[i]
        assigned = taxonomy.loc[row_sims >= THRESHOLD, "Primary_SubScore_Axis"].tolist()
        multilabels.append(assigned)

    df["multilabel_themes"] = multilabels
    return df

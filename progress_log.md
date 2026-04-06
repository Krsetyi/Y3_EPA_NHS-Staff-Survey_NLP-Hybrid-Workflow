**Date:** 6th April 2026

**Time spent:** 2 hours

**Task:** Assess the suitability of annual NSS free-text datasets (2020-2025) for model fine-tuning. Ran automated scoring across coverage, quality, and relevance, and reviewed outputs in the context of known shifts in staff survey behaviour

**Decisions made:** 
- Identified that 2021-2025 datasets have low relevance scores due to short comment length and reduced engagement following COVID. Volumes stabilised around 450 - 600 rows per year, which is insufficient for fine-tuning
- Confirmed that this pattern reflects a behavioural change, not a data quality issue. The generalised post-COVID prompt produces shorter, less experessive comments
- Noted that 2020 scored highly on relevance and volume, but represents a COVID-specific anomaly with unusually long, emotionally charged comments, and elevated IG-risk
- Implementedc a contextual override to exclude 2020 from fine-tuning to avoid biasing the model toward crisis-era sentiment
- Decided to use 2021-2025 for evaluation only, and to fine-tune on the combined multi-year dataset that reflects the post-COVID "new-normal"

**Questions / risks:**
- Risk - Fine-tuning on 2020 alone would bias the model toward COVID-era themes (PPE, safety, burnout) and distort expectations of comment length
- Risk - Annual datasets (2021-2025) are individually too small to train a model; need to ensure the combined dataset has sufficient volume and thematic diversity
- Question - Should the relevance scoring thresholds be adjusted to better reflect modern NHS free-text behaviour, where shorter comments are now the norm?
- Question - Do we need additional augmentation or synthetic examples to compensate for reduced expressiveness in post-COVID data?

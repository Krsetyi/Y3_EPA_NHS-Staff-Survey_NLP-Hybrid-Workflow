# `src/` README

`pipeline/` 
Modular workflow

- load.py - read raw files
- clean.py - text and numeric cleaning
- metadata.py - add derived fields
- prepare.py - final formatting
- run_preprocessing.py - orchestration function
<br/>
<br/>

`utils/`
Reusable helpers

- Logging
- Validation
- File checks
<br/>
<br/>

`explainability/`
For attention heatmaps and feature contribution

- Attention extraction
- Feature importance calculation

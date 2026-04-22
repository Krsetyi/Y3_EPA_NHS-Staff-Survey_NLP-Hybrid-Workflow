# Question-to-Theme Mapping

## Overview
This folder contains the question-to-theme mapping tables used to align NHS Staff Survey questions with the hierarchical People Promise taxonomy. These mappings were developed through four years of manual free text analysis and provide the conceptual foundation for consistent, transparent classiication of staff comments.

The mapping shows how each survey question relates to:
- a People Promise category
- a theme
- a sub-theme
- and, where applicable, a further sub-theme
This structure supports reproducibility, auditability, and alignment with national frameworks.

## Purpose of This Mapping

The question-to-theme mapping serves several key functions:
1. Validates the taxonomy
- It demonstrates that the People Promise hierarchy used in the annotation schema is grounded in the actual constructs measured by the NHS Staff Survey.
2. Supports consistent manual and hybrid annotation.
- By linking questions to themes, analysts can more reliably interpret the intent behind comments and reduce subjective variation
3. Enables training data creation.
- If supervised or hybrid models are developed, this mapping helps identify representative examples for each theme.
4. Strengthens governance and transparency
- It provides a clear audit trail showing how thematic decisions were made and how the taxonomy sligns with national survey design.
5. Helps future analysts understand the logic
- Anyone reviewing or extending the taxonomy can see the rationale behind each category

## Files in This Folder
### question_theme_mapping.csv
A long-format table where each row represents a single survey question mapped to:
- People Promise
- Theme
- Sub-theme
- Further sub-theme (if applicable)
This structure makes it easy to filter, pivot, or join with other datasets

### README.md
This document

### CHANGELOG.md
If included, this file tracks updates to the mapping over time.

## How the Mapping is Structured
Each row in the CSV includes:
| Column | Description|
| Question | The NHS Staff Survey question text |
| PeoplePromise | The top level People Promise category |
| Theme | The theme within the People Promise |
| SubTheme | The sub theme (if applicable) |
| FurtherSubTheme | Additional granularity where relevant |
| Notes | Optional analyst notes |
This mirrors the structure of the annotation schema but focuses on survey questions, not free text comments.

## How This Mapping Is Used int he Workflow

### During manual analysis
Analysts use the mapping to ensure consistent interpretation of comments that reference specific survey constrcuts.

### During model development
The mapping can be used to:
- Generate labelled examples
- Validate model predictions
- Support rule-basxed overrides
- Interpret topic modelling outputs

### During reporting
It helps explkain how free text insights relate back to the quantiative survey structure.

## Maintenance Guidelines
- Add new mappins as new rows - do not overwrite existing ones
- Use version control (pull requests) for transparency
- Document any changes in CHANGELOG.md
- Keep question wording consistent with the official NHS Staff Survey
- Use the Notes column to explain ambiguous or multi-theme mappings

## Relationship to the Annotation Schema
This mapping is not part of the schema itself, instead it is a supporting artefact that:
- Informs the Peole Promise taxonomy
- Strengthens methodological transparency
- Provides evidence for EPA assessment
- Supports reproducibility and governance
The annotation schema lives in /schema/. This folder provides the conceptual link between the survey instrument and the taxonomy

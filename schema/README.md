# Annotation Schema

## Overview
This folder contains the three-layer annotation schema used to classify the NHS Staff Survery free-text comments within the hybrid NLP workflow. The schema provides a structured, auditable way to map comments to
- NHS People Promise themes and sub themes
- Emergent themes identified through topic modelling
- Action-owner routing categories for organisational response

The schema is designed to be machine-readable, version-controlled, and aligned to NHS workforce, OD, and governance structures.


## File Structure

annotation_schema.csv

A long-format table where each row represents a single atomic category (e.g. a sub-theme or emergent theme)
This structure supports filtering, joining, and future model training

#### Columns include:
| Column | Description |
|----------|----------|
| Layer | 1 = People Promise taxonomy, 2 = Emergent themes, 3 = Action-owner routing |
| PeoplePromise | Top-level Peole Promise category (Layer 1 only) |
| Theme | Themes within the People Promise or emergent theme name |
| SubTheme | Sub-theme (Layer 1 only)
| FurtherSubTheme | Additional granularity where applicable |
|RoutingOwner| Senior leadership group responsible for action (Layer 3) |
| Notes | Optional notes for analysts or maintainers |


## Layer Descriptions

### Layer 1 - People Promise Theme Classification

This layer contains the full hierarchical taxonomy developed through four years of manual analysis.
It includes:
- People Promise categories
- Themes
- Sub-themes
- Further sub-themes (where applicable)

This layer ensures consistency with national frameworks and supports interpretability for leadership audiences

### Layer 2 - Emergent Theme Detection

This layer captures new or unexpected themes identified through unsupervised topic modelling.
Examples include:
- Operational friction points
- Localised cultural issues
- New organisational risks
- Policy / change related themes
- Unexpected positive signals

These themes evolve over time and may be promoted into Layer 1 if they stabilise.

### Layer 3 - Action-Owner Routing

This layer maps actionable themes to the senior leadership group responsible for responding.
Examples include (awaiting actual list):
- People & OD Leadership Team
- EDI Steering Group
- Workforce Planning
- Wellbeing & Engagement
- Quality Governance
- HR Business Partners
- Operational Leadership Team
- Analyst Review Required

This layer ensures that insights lead to clear accountability and organisational action.


## How to Use This Schema

### For Analysts
- Filter by Layer to work with specific parts of the taxonomy
- Join model outputs to the schema using theme/sub-theme names
- Use RoutingOwner to generate action-focused reports

### For Developers
- Use the schema as a label map for supervised or hybrid models
- Validate model outputs against the schema to ensure consistency
- Extend the schema by adding new rows rather than modifying existing ones

### For Goverance and Leadership
- Provides transparency on how comments are classified
- Shows how actionable issues are routed
- Supports auditability and repeatability


## Maintenance Guidelines
- Do not delete rows - use version control to track changes
- Add new themes as new rows
- Promote emergent themes to Layer 1 only after analyst review
- Update routing owners when governance structures change
- Use the Notes column to document rationale for changes


## Versioning
All changes to the schema should be made via pull request to ensure:
- Traceability
- Peer review
- Clear change history

This support reproducibility and strengthens the governance model

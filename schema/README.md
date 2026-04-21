# Annotation Schema - README

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

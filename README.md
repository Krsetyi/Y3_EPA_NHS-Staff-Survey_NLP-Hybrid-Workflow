# Y3_EPA_NHS-Staff-Survey_NLP-Hybrid-Workflow

## Overview
Project explores how NLP can be used for free-text comments in the NHS Staff Survey.
Aims is to identify themes, emotions, and patterns in staff experience.
Maintiaining transparency, ethics, and usefulness for organisational decision making
Combines several modern techniques include topic modelling, sentiment analysis, multi-label classification, and transformer based language models.
Designed to be clear, reproducible and suitable for use within NHS IG requirements

## What this project does
Helps organisations to:
- Understand what staff are talking about in their free comments
- Identify common themes such as: workload, leadership, teamwork, wellbeing
- Detect emotional tone: frustration, pride, anxiety, optimism
- Recognise when comments relate to more than one issue at the same time
- Produce insights that support workforce planning, culture improvement, and staff wellbeing initiatives
No real NHS data is included in this repository. Only example structures and placeholder files are provided

## Why this  matters
Free text contains rich insights that quant often miss. However, manually reading is time-concuming, inconsistent, and emotionally taxxing
NLP offers a way to ana,yse at scale while still respecting:
- Staff confidentiality
- NHS IG
- Ethical and fair use of AI
- Transparency and accountability
Project demonstrates how these principles can be combined - practical, responsible workflow

## How it works
4 main stages
#### Preparation
- Text is cleaned and prepared
- No personal identifiers used
- Data handled with NHS IG standards
#### Understanding the Content
- Topic modelling for main themes
- Multi-label classification for comments that relate to several issues at once
#### Understanding the Emotion
- Sentiment and emotion analysis for tone
- Helps identify areas of concern or positive experience
#### Bringing it Together
- Hybrid pipeline combines methods
- Results summarised in a clear, accessible way
- Human review included to ensure accuracy and fairness

## What's Inside
Repo organised into simple folder
- docs/
-   Plain English explanations of workflow, ethics, and evaluation
- notebooks/
-   Step by step example analysis notebooks
- src/
-   Code used to run the workflow
- reports/
-   Example outputs and diagrams
- data/
-   empty folders showing where data WOULD go

## IG and ethics summary
Project follows key principles
- No identifiable data stored in repo
- All analysis steps are transparent and documented
- Human oversight included to avoid misinterpretation
- Methods chosen to minimuse bias and support fairness
- Workflow aligns with GDPR and NHS IG expectations
Full explaination available in docs/ethics_ig.md

## Who it's for
- NHS workforce teams
- Organisational development and culture teams
- Analysts and data scientists
- Leaders seeking evidence-based insight
- Apprentices and students completing applied project
Wrriten to be accessible for both tech and non tech audiences

## How to use
- documentation to understand workflow
- notebooks to see example analyses
- code to understand how each method works
- reports to view example outputs
You do NOT need tech skills to understand the high-level concepts

## Contact details
For questions, improvements, or collaboration, please contact the project owner

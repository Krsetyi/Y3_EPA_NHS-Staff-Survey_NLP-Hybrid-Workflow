```mermaid
flowchart LR
    %% Style settings for a more visual, infographic feel
    classDef stage fill:#e8f1fb,stroke:#2a4b8d,stroke-width:1px,color:#1a1a1a;
    classDef process fill:#fdf6e3,stroke:#b58900,stroke-width:1px,color:#1a1a1a;
    classDef analysis fill:#e8fbe8,stroke:#3a7a3a,stroke-width:1px,color:#1a1a1a;
    classDef output fill:#fff2f2,stroke:#b30000,stroke-width:1px,color:#1a1a1a;

    %% Pipeline
    A[📥 Secure NHS Data Ingestion<br><small>Free‑text collected safely inside NHS systems</small>]:::stage --> 
    B[🧹 Data Preparation<br><small>Cleaning, de‑identification, standardisation</small>]:::process

    B --> C[🧭 Topic Modelling<br><small>Unsupervised discovery of themes</small>]:::analysis
    B --> D[💬 Sentiment & Emotion Analysis<br><small>Detect tone and emotional signals</small>]:::analysis
    B --> E[🏷 Multi‑Label Classification<br><small>Identify multiple issues per comment</small>]:::analysis

    C --> F[🔗 Hybrid Integration Layer<br><small>Combine themes, emotions, and labels</small>]:::process
    D --> F
    E --> F

    F --> G[👀 Human Review & Quality Checks<br><small>Fairness, accuracy, context</small>]:::stage

    G --> H[📊 Final Insights & Reporting<br><small>Dashboards, summaries, organisational learning</small>]:::output

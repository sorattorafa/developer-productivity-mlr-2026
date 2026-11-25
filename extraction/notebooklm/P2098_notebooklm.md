# P2098 — Multimodal Workload Analysis for Developer Burnout Prediction: Integrating Jira and GitHub Activity Data

**Decisao: INCLUIDO | Qualidade: 4/5**

---

## Dados Bibliograficos

| Campo | Valor |
|-------|-------|
| **ID** | P2098 |
| **Autores** | AI Mohamed Sabeeb, JD Tenushi Erandi, WV Chandima Maduwanthi [1] |
| **Ano** | Not specified in header (references include 2025) [2, 3] |
| **Venue** | Not specified in paper header [1] |
| **DOI** | Not specified in paper text [1] |
| **Tipo** | Conference paper / Pre-print [1] |
| **Metodo** | Repository mining / Machine learning / Quantitative [4-6] |
| **Amostra** | 20-MAD dataset containing 20 years of Jira issue-tracking and GitHub version-control data from Apache projects (Hadoop, HDFS, Zookeeper) [4, 7] |
| **Contexto** | Open-Source Software (OSS) — Apache projects [7, 8] |
| **Modo de trabalho** | Not specified [8] |
| **Metodologia** | Agile (Scrum / Kanban context discussed) [9, 10] |

---

## Objetivo

The main objective of this study is to propose and evaluate a proactive, data-driven multimodal framework that integrates task management and issue-tracking data from Jira with code contribution activity from GitHub to predict developer burnout risk [4]. By combining task assignment workload and actual development activity patterns extracted from the open-source Mozilla–Apache (20-MAD) dataset, the authors aim to address the limitations of survey-based or single-source approaches, train and evaluate multiple machine learning classification algorithms, and deploy a dashboard prototype featuring an LLM-based natural language interface for monitoring developer well-being [4, 5, 11, 12].

---

## Questoes de Pesquisa

- **RQ1**: To what extent can the integration of Jira task-management data and GitHub code-activity data improve the prediction of developer burnout risk? [13]
- **RQ2**: Which multimodal workload indicators extracted from Jira and GitHub data best predict developer burnout risk? [13]
- **RQ3**: How accurately can different machine learning models predict developer burnout risk using integrated Jira and GitHub activity data? [13]
- **RQ4**: Which machine learning model performs best for burnout-risk classification in the proposed multimodal framework? [13]
- **RQ5**: How can a real-time dashboard with an integrated natural language interface make developer burnout-risk analytics more accessible and interpretable for technical and non-technical stakeholders? [13]

---

## Metricas e Instrumentos de Avaliacao

| Metrica | Categoria | Nivel | Como Coletada | Validada |
|---------|-----------|-------|---------------|----------|
| `commits_count` | Activity | Individual | Extracted from GitHub commit logs over rolling time windows | Partial (\\(\rho = 0.519\\)) [5, 14, 15] |
| `total_lines_changed` | Activity / Quality | Individual | Calculated from code churn in GitHub commits | Partial (\\(\rho = 0.486\\)) [5, 14, 15] |
| `issues_count` / `issues_handled` | Activity / Delivery | Individual | Extracted from Jira issue-tracking backlog/metadata | Partial (\\(\rho = 0.454\\)) [5, 14, 15] |
| `early_morning_commits` | Activity / Work Patterns | Individual | Commit timestamps (\\(\le\\)06:00) from GitHub logs | Partial (\\(\rho = 0.361\\)) [15, 16] |
| `unique_components` | Process / Collaboration | Individual | Count of distinct Jira/GitHub components worked on | Partial (\\(\rho = 0.324\\)) [5, 15, 17] |
| `late_night_commits` | Activity / Work Patterns | Individual | Commit timestamps (\\(\ge\\)22:00) from GitHub logs | Partial (\\(\rho = 0.295\\)) [15, 16] |
| `average_lines_changed` | Activity | Individual | Mean lines changed per commit from GitHub | Partial (\\(\rho = 0.293\\)) [15] |
| `unresolved_issue_ratio` | Productivity / Quality | Individual / Team | Ratio of unresolved issues to total issues in Jira | Partial (\\(\rho = 0.196\\)) [10, 15] |
| `weekend_work_ratio` | Activity / Work Patterns | Individual | Proportion of commits made on weekends via GitHub | Partial (\\(\rho = 0.138\\)) [15, 16] |
| `high_priority_ratio` | Task Complexity | Individual | Ratio of high-priority issues assigned in Jira | Partial (\\(\rho = 0.088\\)) [15] |
| `average_issue_age` | Delivery / Process | Individual / Team | Time elapsed between issue creation and resolution in Jira | Partial (\\(\rho = 0.030\\)) [15] |
| `average_commit_time` | Activity / Work Patterns | Individual | Average hour of day of GitHub commits | Partial (\\(\rho = -0.102\\)) [15] |
| `work_in_progress` (WIP) / Workload Intensity (\\(W_d\\)) | Activity / Workload | Individual | Jira issue metadata & GitHub rolling windows | Partial (\\(B_d\\) composite proxy score) [10, 18, 19] |
| `issue_reopen_rate` | Quality / Process | Individual / Team | Jira issue status transition logs | Partial [10] |
| `cycle_lead_time` | Delivery | Individual / Team | Jira issue creation, start, and resolution timestamps | Partial [10] |

---

## Frameworks e Metricas

### Frameworks Referenciados
- **Maslach Burnout Inventory (MBI)**: REFERENCED (Discussed as theoretical grounding defining burnout across emotional exhaustion, depersonalization, and reduced accomplishment) [20, 21].
- **Burnout Assessment Tool (BAT)**: REFERENCED (Discussed for its four core dimensions—exhaustion, mental distance, cognitive impairment, emotional impairment—used to conceptually align the composite proxy score) [18, 22, 23].
- **Valence–Arousal–Dominance (VAD) Framework**: REFERENCED (Cited/discussed for emotion analysis in Jira issue comments) [24, 25].
- **Job Demands-Resources (JD-R) Approach**: REFERENCED (Cited via Demerouti & Sanz Vergel to justify operational weighting of workload intensity) [19, 26].
- *Note*: Standard software engineering measurement frameworks such as DORA, SPACE, DevEx, GQM, HEART, or OKR are **NOT** mentioned in this paper.

### Frameworks Propostos
- **Multimodal Developer Burnout Prediction Framework**: The paper proposes an end-to-end data-driven framework integrating Jira task-management data and GitHub code-activity data [4]. The framework encompasses rolling time-window feature extraction, a theory-informed composite proxy score (\\(B_d = 0.35W_d + 0.25I_d + 0.25C_d + 0.15X_d\\)), supervised ML classification (with ANN as top performer), and a React-Vite dashboard prototype with an LLM-powered natural language interface for real-time risk assessment and mitigation recommendations [4, 5, 11, 12, 18, 19, 27].

---

## Fatores que Influenciam Produtividade

### Fatores Positivos
| Fator | Categoria |
|-------|-----------|
| Balanced work style (balancing coding and team collaboration) [28, 29] | Process |
| Automated issue prioritization (minimizes cognitive overload) [30, 31] | Technical |
| Real-time burnout risk monitoring and transparent analytics dashboard [11, 27, 32] | Organizational |
| Proactive workload reallocation and sprint buffer time planning [12, 33] | Process |

### Fatores Negativos
| Fator | Categoria |
|-------|-----------|
| High commit frequency and excessive lines changed (`commits_count`, `total_lines_changed`) [5, 14, 15] | Technical |
| Excessive issue volume / high assigned backlog load (`issues_count`) [5, 14, 15] | Process |
| Irregular and off-hours work patterns (early morning, late night, weekend commits) [5, 15, 16] | Human |
| Context switching across multiple unique components and repositories [17, 22, 29] | Technical |
| Agile iteration pressure and tight delivery deadlines [9] | Organizational |
| High pull request failure rates and excessive code churn [34, 35] | Technical |

---

## Papel da IA e Automacao

| Campo | Valor |
|-------|-------|
| **Usa IA/ML?** | Yes — Machine learning models (ANN/MLP, XGBoost, Stacking Ensemble, Voting Ensemble, AdaBoost, etc.) were evaluated for burnout prediction (ANN reached 98.48% accuracy) [5, 15, 36]. An LLM architecture is integrated for the natural language dashboard interface [11, 12]. |
| **Automacao de coleta?** | Yes — Repository mining automatically extracts and maps Jira issue tracking and GitHub commit activity data (with live API integration planned for future work) [4, 7, 12, 37]. |
| **Impacto de IA na produtividade?** | Reduces cognitive fatigue (e.g., via automated issue prioritization) and generates actionable workload mitigation recommendations to maintain productivity and developer well-being [11, 12, 30, 38]. |

---

## Resultados Principais

- **Best Model Performance**: Artificial Neural Network (ANN / MLP) achieved the highest predictive performance with an **accuracy of 98.48%**, **precision of 97.92%**, **recall of 96.90%**, and **F1-score of 97.41%** [5, 15].
- **Machine Learning Comparison**: Other top-performing models evaluated include XGBoost (F1: 96.27%, Accuracy: 97.82%), Stacking Ensemble (F1: 95.46%, Accuracy: 97.34%), Voting Ensemble (F1: 95.33%, Accuracy: 97.31%), AdaBoost (F1: 94.19%, Accuracy: 96.68%), Gradient Boosting (F1: 92.78%), Logistic Regression (F1: 91.68%), SVM (F1: 90.50%), Random Forest (F1: 89.86%), and Decision Tree (F1: 83.32%) [15, 36, 39].
- **Key Burnout Predictors (Spearman Correlation \\(\rho\\))**:
  - `commits_count` (\\(\rho = 0.519\\)): Strongest positive association with developer burnout risk [5, 14, 15].
  - `total_lines_changed` (\\(\rho = 0.486\\)): High coding volume strongly correlates with burnout [14, 15].
  - `issues_count` / `issues_handled` (\\(\rho = 0.454\\)): High task assignment volume is significantly linked to burnout [14, 15].
  - `early_morning_commits` (\\(\rho = 0.361\\)): Irregular early work patterns correlate with stress [15, 16].
  - `unique_components` (\\(\rho = 0.324\\)): Frequent context switching increases cognitive load [15, 17].
  - `late_night_commits` (\\(\rho = 0.295\\)) & `average_lines_changed` (\\(\rho = 0.293\\)): Night work and high average change sizes reflect elevated risk [15, 16].
  - `unresolved_issue_ratio` (\\(\rho = 0.196\\)) & `weekend_work_ratio` (\\(\rho = 0.138\\)) [15, 16].
  - `average_commit_time` (\\(\rho = -0.102\\)): Negatively associated with burnout risk [15].
- **Multimodal Integration Superiority**: Combining task-management signals from Jira with code activity from GitHub provides superior predictive power over analyzing either platform in isolation [4, 40, 41].
- **Interactive Dashboard & NLP Interface**: Developed a React-Vite dashboard integrated with the ANN model and an LLM-powered natural language query interface to deliver real-time risk scores and tailored mitigation recommendations [11, 12, 27, 38].

---

## Desafios do Uso das Metricas

- **Single-Source Isolation Anti-Pattern**: Analyzing Jira or GitHub data independently fails to account for the interplay between assigned task workload and actual development output [4, 40, 42].
- **Survey Dependency & Retrospective Lag**: Traditional survey tools (MBI, BAT) are subjective, periodic, and reactive, lacking real-time continuous monitoring capabilities [4, 20, 21, 43].
- **Lack of Ground-Truth Repository Labels**: Mining historical repository data requires theory-informed proxy formulations (\\(B_d = 0.35W_d + 0.25I_d + 0.25C_d + 0.15X_d\\)) with heuristic weightings due to the absence of direct clinical/survey annotations [18, 19].
- **Context Switching Overlook**: Tracking raw commit counts without factoring in component context switching ignores cognitive fatigue caused by domain switching [17, 22, 29].
- **Misinterpretation of Off-Hours Activity**: High commit activity during off-work hours (late night, early morning, weekends) may be misconstrued as high productivity rather than a sign of burnout risk [5, 16, 41].

---

## Avaliacao de Qualidade Metodologica

| Criterio | Pontuacao (0-2) |
|----------|----------------|
| Objetivo claramente definido | 2 |
| Metodologia adequada ao objetivo | 2 |
| Amostra/contexto descrito adequadamente | 1 |
| Ameacas a validade discutidas | 1 |
| Resultados com evidencia suficiente | 2 |
| Contribuicao clara para pratica ou teoria | 2 |
| **TOTAL** | **10/12** |

---

## Limitacoes

- **Open-Source Dataset Context**: The study uses historical data from the Mozilla–Apache (20-MAD) open-source dataset, which may limit generalizability to industrial software development teams and commercial agile workflows [8, 31, 44].
- **Proxy Burnout Formulation**: Ground-truth burnout labels were generated using an operational proxy score (\\(B_d\\)) based on heuristic dimensional weights rather than direct survey-validated clinical diagnostics [18, 19].
- **Absence of Live API Connections**: The prototype dashboard relies on manually entered metric inputs rather than live, continuous API integrations with Jira and GitHub repositories [27, 44].
- **Heuristic Classification Threshold**: Supervised classification utilizes a default operational midpoint threshold (\\(\theta = 0.5\\)) to binarize continuous burnout risk scores [45].

---

## Contribuicao Principal

The primary contribution of this paper is the proposal, implementation, and evaluation of a multimodal, data-driven framework that unifies Jira task management data and GitHub code activity data for developer burnout prediction [4, 41, 46]. By developing a theory-informed proxy score that incorporates workload intensity, work pattern irregularity, task complexity, and context switching, the authors demonstrate that machine learning models—specifically an Artificial Neural Network achieving 98.48% accuracy—outperform single-source alternatives and establish key behavioral predictors such as commit count, lines changed, and issues handled [5, 14, 18, 36]. Furthermore, they operationalize their model into a functional React-Vite dashboard prototype paired with an LLM-based natural language interface, enabling stakeholders to interactively assess burnout risk and receive automated workload mitigation guidance [11, 12, 27, 32, 38].

---

*Extraido via NotebookLM em October 2026 para MLR: Software Developer Metrics in Practice*
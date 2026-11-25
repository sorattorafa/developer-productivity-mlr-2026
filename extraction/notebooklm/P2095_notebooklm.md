# P2095 — AI-Assisted Software Testing Improvements

**Decisao: INCLUIDO | Qualidade: 5/5**

---

## Dados Bibliograficos

| Campo | Valor |
|-------|-------|
| **ID** | P2095 |
| **Autores** | Haldun Halil Olcay, Dilara Albayrak [1] |
| **Ano** | 2024 (Data de acesso das referencias: Dezembro de 2024) [2, 3] |
| **Venue** | Nao especificado no texto (Formato de artigo de conferencia / Relatorio tecnico IEEE) [1, 4] |
| **DOI** | Nao especificado [1] |
| **Tipo** | Technical report / Conference paper [1, 4] |
| **Metodo** | Case study / Quantitative and qualitative empirical analysis [1, 5, 6] |
| **Amostra** | 9 equipes de desenvolvimento cross-functional, 17 projetos principais e ~50 projetos secundarios no setor de turismo, dados de 12 meses (~4.200 PRs limpos, 2.700 issues Jira, 400 relatos de sintomas) [5, 7, 8] |
| **Contexto** | Industry (SeturTech — B2C travel platforms e ferramentas operacionais internas) [1, 5, 7] |
| **Modo de trabalho** | Not specified [5, 7] |
| **Metodologia** | Agile / DevOps (Scrum, CI/CD, Pull Requests, DORA Metrics) [8-11] |

---

## Objetivo

This paper presents an empirical analysis of software development metrics and qualitative symptoms collected via the Oobeya platform across 9 software teams at SeturTech over a 12-month period [1, 5, 7]. The primary objective is to evaluate the relationships, alignment, and discrepancies between quantitative engineering performance indicators (such as DORA metrics, technical debt, and PR review times) and qualitative process symptoms (e.g., oversized PRs, high cognitive load) [1, 8, 12, 13]. Additionally, the paper aims to outline a conceptual framework and pilot implementation for leveraging Artificial Intelligence (predictive analytics, anomaly detection, root cause analysis, self-healing tests, and automated recommendations) to resolve data inconsistencies, address process bottlenecks, and enhance software Quality Assurance (QA) performance [1, 14-17].

---

## Questoes de Pesquisa

- **RQ1**: Do recurring qualitative symptoms (process anti-patterns and bottlenecks detected by Oobeya) noticeably impact quantitative software delivery speed and quality metrics? [12]
- **RQ2**: How reliable and consistent are the objective engineering metrics collected by Oobeya, and do discrepancies exist between metrics and qualitative symptoms or industry standards? [13]

---

## Metricas e Instrumentos de Avaliacao

| Metrica | Categoria | Nivel | Como Coletada | Validada |
|---------|-----------|-------|---------------|----------|
| **Deployment Frequency (DF)** | Delivery | Team | Automated via Oobeya integrating Azure DevOps / CI/CD pipelines [8, 9, 18] | Yes [8, 18] |
| **Lead Time for Changes (LTC)** | Delivery | Team | Automated via Oobeya integrating Git, Azure DevOps, and Jira [7-9, 19] | Yes [8, 19] |
| **Change Failure Rate (CFR)** | Quality | Team / Organization | Automated via Oobeya tracking production release failures and incident logs [8, 20] | Yes [8, 20] |
| **Mean Time to Restore Service / Time to Restore Service (MTTR / TTRS)** | Delivery / Quality | Team / Organization | Automated via Oobeya incident tracking integrations [8, 21] | Yes [8, 21] |
| **PR Size (Lines of Code)** | Activity / Quality | Individual / Team | Automated line count extraction from Git pull requests via Azure DevOps / Jira [7, 8, 19] | Yes [8, 19] |
| **Technical Debt (Warnings / Issues)** | Quality | Team / Project | Automated static code analysis from SonarQube integrated with Oobeya [7, 8, 20, 22] | Yes [8, 20] |
| **Lightning Pull Requests (LPRs) Frequency** | Activity / Process | Team | Automated count of rapidly merged and deployed pull requests via Oobeya [21] | Partial [21, 23] |
| **Code Review Duration / Review Time** | Activity / Process | Team | Automated tracking of duration between PR creation and merge in Git / Azure DevOps [8, 24] | Yes [8, 24] |
| **Rework Rate** | Quality / Activity | Team | Automated tracking of code modifications and reverts within sprint PRs via Oobeya [25-27] | Partial [25, 26] |
| **PR Revert Rate** | Quality | Team | Automated count of reverted pull requests via Oobeya [28] | Partial [28] |
| **Coding Time** | Activity | Individual / Team | Automated tracking of active development duration prior to PR submission via Oobeya [16] | Partial [16] |
| **Cycle Time** | Delivery | Team | Automated tracking of total SDLC duration from work start to release via Oobeya [29, 30] | Yes [29, 30] |
| **Planning Accuracy** | Process / Delivery | Team | Automated comparison of planned vs completed story points/tasks in Jira via Oobeya [30] | Partial [30] |
| **Sprint Delivery Rate** | Delivery | Team | Automated calculation of completed work items per sprint via Jira / Oobeya [30] | Partial [30] |

---

## Frameworks e Metricas

### Frameworks Referenciados
- **DORA Metrics (DevOps Research and Assessment)**: APPLIED — Used as the primary quantitative baseline for software delivery performance (Deployment Frequency, Lead Time for Changes, Change Failure Rate, MTTR) [8, 9, 18].
- **Agile / SDLC Frameworks**: APPLIED — Used for sprint tracking, issue management (Jira), and process execution [7, 9, 11].
- **CI/CD & Engineering Intelligence Frameworks**: APPLIED — Implemented via Oobeya integrated with Azure DevOps and SonarQube [4, 7, 9].
- *Note*: Other frameworks such as **SPACE**, **DevEx**, **GQM**, **HEART**, or **OKR** are **NOT** explicitly mentioned or cited in the paper.

### Frameworks Propostos
- **Conceptual AI-Driven QA Enhancement Framework**: Proposed by the authors to elevate Oobeya from a passive visualization tool into an active intelligence system [1, 14, 17]. It comprises four key components:
  1. *Predictive Analytics for QA*: Machine learning models (e.g., decision tree classifiers) trained on historical SDLC data to forecast late deliveries, bug spikes, and symptom risks [15, 27, 31].
  2. *Intelligent Test Automation and Maintenance*: Self-healing test scripts that automatically adapt to UI changes, combined with generative AI for automated test case generation from requirements [32-34].
  3. *Symptom Analysis & Recommendation System*: Clustering and classification algorithms to detect combined symptom patterns and provide context-aware actionable recommendations [28, 34, 35].
  4. *Root Cause Analysis & Anomaly Detection*: Advanced correlation models to uncover complex metric interactions and detect reporting/data inconsistencies [16, 17, 36].

---

## Fatores que Influenciam Produtividade

### Fatores Positivos
| Fator | Categoria |
|-------|-----------|
| Small Pull Request size (LOC < 200) [19, 37] | Technical / Process |
| High Deployment Frequency [18, 19] | Process / Delivery |
| Optimized and well-structured code review workflows (e.g., Team 4, Team 8, Team 2) [37-39] | Process / Human |
| Automated QA, static code analysis (SonarQube), and CI/CD integrations [7-9] | Technical / Process |
| AI-driven predictive insights and proactive recommendations (proposed) [15, 17, 35] | Technical / Process |

### Fatores Negativos
| Fator | Categoria |
|-------|-----------|
| Oversized Pull Requests (Large LOC changes) [19, 22, 25] | Technical / Process |
| High Cognitive Load and context-switching [22] | Human / Organizational |
| High Technical Debt (static analysis warnings, SonarQube issues) [20, 22, 40] | Technical |
| Excessive Lightning Pull Requests (rushed merges reducing QA and review rigor under pressure) [21, 23] | Process / Technical |
| Long Code Review Durations / Review bottlenecks (reviewer unavailability, non-technical delays) [37, 38, 41] | Process / Organizational |
| High Rework Rate and PR Revert Rate [25, 26, 28] | Quality / Process |
| Discrepancies between quantitative metrics and qualitative symptoms [1, 13, 42] | Organizational / Process |

---

## Papel da IA e Automacao

| Campo | Valor |
|-------|-------|
| Usa IA/ML? | Yes — Proposed implementation uses ML (Decision Tree Classifier, Clustering) and Generative AI for QA [15, 27, 28, 33]. (Note: LLM tools ChatGPT and Gemini were also used by authors for text summarization/editing) [43]. |
| Automacao de coleta? | Yes — Oobeya automatically aggregates metric data and detects process symptoms from Azure DevOps, Jira, and SonarQube [9, 10, 25]. |
| Impacto de IA na produtividade? | Proposed / Empirically projected — AI transforms passive metric reporting into active decision support, reducing test maintenance effort, accelerating root cause analysis, predicting defects before release, and recommending context-aware process fixes [15, 17, 32, 35]. |

---

## Resultados Principais

- **PR Size vs. Deployment Frequency**: Strong negative correlation (Pearson \\(r = -0.82\\)) [44]. Teams submitting larger code changes consistently experienced lower deployment frequencies (e.g., Team 7 with ~1,078 LOC deployed 0.42 times/week vs. Team 9 with ~135 LOC deploying 1.38 times/week) [19, 21].
- **PR Size vs. Technical Debt**: Strong positive correlation (Pearson \\(r = 0.78\\)) [44]. Larger PR sizes accumulated substantially more static analysis technical debt warnings [40].
- **Lightning Pull Requests (LPR) vs. Time to Restore Service (TTRS)**: Moderate positive correlation (Pearson \\(r = 0.66\\)) [44]. Rapidly merged/deployed PRs under pressure correlated with longer incident recovery times (e.g., Team 4 with 364 LPRs had a TTRS of 194 hours), showing that rushed changes bypass review rigor and introduce subtle system defects [21, 23].
- **Technical Debt vs. Change Failure Rate**: Moderate positive correlation (Pearson \\(r = 0.61\\)) [44]. High technical debt directly increased release failure rates in production [20].
- **PR Size vs. Review Duration Inconsistencies**: PR size alone does not dictate review speed [37, 38]. For example, Team 1 (219 LOC) averaged 780 hours of review time, while Team 3 (1,167 LOC) managed 360 hours, and Team 5 (1,114 LOC) achieved 180 hours [38, 41, 44, 45]. Factors like reviewer availability, change complexity, and process bottlenecks drive review duration [37].
- **Dataset Scale**: Analyzed data from 9 cross-functional teams across 17 major and ~50 minor projects over 12 months, filtering >5,000 PRs and 2,700 Jira issues to a clean set of ~4,200 PRs, 400 qualitative symptom reports, and >20 metrics [5, 7, 8].

---

## Desafios do Uso das Metricas

- **Discrepancies Between Metrics and Symptoms**: Significant gaps exist between objective quantitative data and qualitative symptoms reported or perceived by teams [1, 42].
- **Opacity of Symptom Detection Algorithms**: Oobeya's internal mechanisms for flagging symptoms (e.g., "high cognitive load") are undisclosed, risking misinterpretation or over-reliance on automated alerts without verification [39, 46].
- **Dependency on Integration Integrity**: Metric accuracy strictly depends on complete and consistent data across Jira, Azure DevOps, and SonarQube; missing tags or unlinked PRs forced exclusion of >800 PRs [7, 46, 47].
- **Risk of Inferring Causality from Correlation**: Statistical correlations do not confirm causation, as organizational context, project complexity, and team dynamics remain unmeasured [47].
- **Perverse Incentives / Goodhart's Law (Lightning PRs)**: Rushing merges to meet velocity demands introduces defects, bypasses thorough QA, and ultimately prolongs system recovery times [21, 23].
- **Rigidity to Custom Domain Workflows**: Standard metrics do not automatically adapt to unique domain-specific needs (e.g., tourism industry workflows) [48].

---

## Avaliacao de Qualidade Metodologica

| Criterio | Pontuacao (0-2) |
|----------|----------------|
| Objetivo claramente definido | 2 |
| Metodologia adequada ao objetivo | 2 |
| Amostra/contexto descrito adequadamente | 2 |
| Ameacas a validade discutidas | 2 |
| Resultados com evidencia suficiente | 2 |
| Contribuicao clara para pratica ou teoria | 2 |
| **TOTAL** | **12/12** |

---

## Limitacoes

- **Black-Box Symptom Detection Logic**: Oobeya's internal logic and threshold rules for identifying qualitative symptoms are undocumented and proprietary [39, 46].
- **Sensitivity to Toolchain Data Quality**: Incomplete configurations or unlinked records across Azure DevOps, Jira, and SonarQube distort metric calculations and required excluding ~800 PRs [7, 46, 47].
- **Correlational Nature of Findings**: The study establishes correlations but cannot prove causality due to uncaptured confounding variables like team experience or domain complexity [47].
- **Lack of Domain-Specific Customization**: Standard engineering metrics do not account for specialized tourism domain workflows or company-specific goals [48].
- **Pilot Scope**: The proposed decision tree ML model and AI recommendation framework are designed for a short 2-sprint pilot on historical data, requiring further practical validation [27, 29].

---

## Contribuicao Principal

The main contribution of this paper is an empirical evaluation of the alignment and discrepancies between quantitative software engineering metrics (e.g., DORA indicators, technical debt) and qualitative process symptoms across 9 industrial teams over a 12-month period, demonstrating key relationships such as how oversized pull requests and rushed 'Lightning PRs' degrade delivery velocity and prolong incident recovery times [1, 5, 8, 19, 21, 44]. Grounded in these empirical insights, the paper contributes a conceptual framework and pilot implementation design for augmenting software intelligence platforms (such as Oobeya) with AI-driven predictive analytics, anomaly detection, root cause analysis, and context-aware recommendations to foster data-driven continuous improvement in software quality assurance [1, 14, 17, 27].

---

*Extraido via NotebookLM em October 2026 para MLR: Software Developer Metrics in Practice*

---

📊 Would you like me to generate a visual scatter plot comparing PR Size against Deployment Frequency or Technical Debt from this study?
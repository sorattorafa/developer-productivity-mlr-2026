# P2014 — BayesInsights: Modelling Software Delivery and Developer Experience with Bayesian Networks at Bloomberg

**Decisao: INCLUIDO | Qualidade: 4.5/5**

---

## Dados Bibliograficos

| Campo | Valor |
|-------|-------|
| **ID** | P2014 |
| **Autores** | Serkan Kirbas, Federica Sarro, David Williams [1, 2] |
| **Ano** | 2026 [2] |
| **Venue** | 34th ACM Joint European Software Engineering Conference and Symposium on the Foundations of Software Engineering (FSE Companion ’26) [2] |
| **DOI** | 10.1145/3803437.3805242 [2] |
| **Tipo** | Conference paper (Industry Experience / Short Paper Track) [2] |
| **Metodo** | Mixed methods (Literature review, expert survey, structure learning algorithms, performance benchmarking, focus groups) [3-5] |
| **Amostra** | Internal engineer survey (>2,000 responses across 20 questions) [4]; Expert insight survey (\\(n=8\\) DevX experts) [6]; Evaluation study (28 senior Bloomberg practitioners attended focus groups, 24 completed questionnaire) [5, 7] |
| **Contexto** | Industry — Bloomberg [1, 3] |
| **Modo de trabalho** | Not specified [1] |
| **Metodologia** | DevOps / Agile [8, 9] |

---

## Objetivo

The primary objective of this paper is to present and evaluate *BayesInsights*, an interactive software engineering tool developed at Bloomberg that uses Bayesian Networks (BNs) to model causal and probabilistic dependencies between software delivery performance and Developer Experience (DevEx) metrics [3, 4]. By addressing the limitations of static metric dashboards, BayesInsights enables engineering leaders and practitioners to conduct root-cause analysis, evaluate trade-offs, and perform "what-if" impact scenarios to understand how changes in engineering practices propagate through complex socio-technical systems [8, 10, 11].

---

## Questoes de Pesquisa

The paper does not state explicit formal research questions prefixed with RQ1/RQ2, but addresses three core empirical and technical evaluation goals [5, 7, 12, 13]:

- **RQ1 (Technical Performance & Scalability)**: Can Bayesian Networks be queried with sufficiently low latency to enable real-time interactive scenario exploration in a large-scale industrial setting? [12]
- **RQ2 (Perceived Usefulness & Practical Impact)**: How useful do senior software engineering practitioners find BayesInsights for identifying software delivery challenges and root causes at team and organizational levels? [5, 14]
- **RQ3 (Interpretability & Model Trust)**: To what extent do practitioners understand the visual inter-metric dependencies and trust the model's probabilistic outputs for decision-making? [15]

---

## Metricas e Instrumentos de Avaliacao

| Metrica | Categoria | Nivel | Como Coletada | Validada |
|---------|-----------|-------|---------------|----------|
| Change Lead Time | Delivery / Throughput | Team/Organization | Automated CI/CD pipeline & repository data [9] | Yes [9] |
| Deployment Frequency | Delivery / Throughput | Team/Organization | Automated CI/CD pipeline data [9] | Yes [9] |
| Failed Deployment Recovery Time | Delivery / Stability | Team/Organization | Incident tracking & deployment systems [9] | Yes [9] |
| Change Failure Rate | Delivery / Quality / Stability | Team/Organization | CI/CD & incident reporting systems [9] | Yes [9] |
| Time Lost to Obstacles | DevEx / Productivity | Individual/Team | Internal quarterly engineer survey (Likert scale) [8, 10] | Yes [8, 10] |
| Developer Happiness | DevEx / Satisfaction | Individual/Team | Internal quarterly engineer survey (Likert scale) [8, 10] | Yes [8, 10] |
| Focus without Distraction | DevEx / Activity | Individual/Team | Internal quarterly engineer survey (Likert scale) [8, 10] | Yes [8, 10] |
| Environment Performance | DevEx / Infrastructure | Individual/Team | Internal quarterly engineer survey (Likert scale) [8, 10] | Yes [8, 10] |
| Code Understanding | DevEx / Quality | Individual/Team | Internal quarterly engineer survey (Likert scale) [8, 10] | Yes [8, 10] |
| Meaningful Work | DevEx / Satisfaction | Individual/Team | Internal quarterly engineer survey (Likert scale) [8, 10] | Yes [8, 10] |
| Tech Debt Impact | DevEx / Quality | Individual/Team | Internal quarterly engineer survey (Likert scale) [16] | Yes [16] |

---

## Frameworks e Metricas

### Frameworks Referenciados
- **DORA (DevOps Research and Assessment)**: APPLIED — core metrics (Change Lead Time, Deployment Frequency, Failed Deployment Recovery Time, Change Failure Rate) form the foundation of the software delivery performance Bayesian Network [8, 9].
- **SPACE Framework**: REFERENCED — serves as a conceptual foundation for capturing developer productivity and perceptions across satisfaction, performance, activity, communication, and efficiency [8, 17].
- **DevEx Framework**: APPLIED — provides the conceptual framework for measuring developer perceptions, satisfaction, engagement, and work environment obstacles [8, 9].

### Frameworks Propostos
- **BayesInsights Causal BN Framework**: A novel hybrid modeling framework that combines theoretical literature (DORA/SPACE), expert insight surveys with weighted scoring (threshold \\(\ge 0.70\\)), and structure learning algorithms (Hill-Climbing and Peter-Clark with bootstrap resampling and BIC scoring) to construct Directed Acyclic Graphs (DAGs) and Conditional Probability Tables (CPTs) with Dirichlet smoothing [4, 18-21].

---

## Fatores que Influenciam Produtividade

### Fatores Positivos
| Fator | Categoria |
|-------|-----------|
| Focus without Distraction | Human / Process [10] |
| Environment Performance | Technical [10] |
| Code Understanding | Technical / Human [10] |
| Meaningful Work | Human / Organizational [10] |
| CI/CD and Automated Testing Capabilities | Technical / Process [8] |

### Fatores Negativos
| Fator | Categoria |
|-------|-----------|
| Time Lost to Obstacles | Process / Organizational [10] |
| Technical Debt Impact | Technical [16] |
| Work Environment Distractions / Interruptions | Organizational / Human [10] |
| Hidden Confounders (Spurious dependencies, toolchain/culture noise) | Organizational [22] |

---

## Papel da IA e Automacao

| Campo | Valor |
|-------|-------|
| **Usa IA/ML?** | Yes — Applies Bayesian Networks (via `pgmpy`), Hill-Climbing (HC), and Peter-Clark (PC) structure learning algorithms with bootstrap resampling and Bayesian Information Criterion (BIC) model selection [4, 20, 23]. |
| **Automacao de coleta?** | Partial — Ingests automated pipeline delivery metrics combined with quarterly structured survey data (>2,000 responses); CPT parameter estimation and BDeu smoothing are automated via Django backend [4, 21, 23, 24]. |
| **Impacto de IA na produtividade?** | The BN model automates probabilistic impact analysis and what-if scenario reasoning, enabling software engineering leaders to pinpoint root causes, evaluate trade-offs, and prioritize interventions [3, 10, 11, 14]. |

---

## Resultados Principais

- **High Perceived Usefulness**: 95.8% of focus group participants (23/24) reported that BayesInsights is useful for identifying software delivery challenges at team and organizational levels [5, 14, 25].
- **Ease of Interpretation**: 75% stated that model outputs were easy to interpret, and 83.3% clearly understood how the tool visualizes inter-metric impacts during what-if scenario analyses [15, 26].
- **High Adoption Intent**: 79.2% indicated they would use or recommend BayesInsights within their own teams [14, 26].
- **Confidence in Outputs**: 70.9% expressed confidence in the tool's outputs when reasoning about software delivery and DevEx [15].
- **Immediate Value**: 25% of participants generated concrete performance improvement ideas during a brief 15-minute hands-on demonstration [14].
- **Low Latency Performance**: Benchmark testing yielded an average response time of 24 ms for single inference requests and median response times under 40 ms under a load of 50 concurrent users [12].
- **Expert Model Superiority**: Expert-refined BN models achieved better Bayesian Information Criterion (BIC) fit scores than pure unconstrained algorithmic structure learning (Hill-Climbing and PC) [20].
- **Deployment Status**: BayesInsights is currently deployed in early access across 7 engineering teams at Bloomberg [25-27].

---

## Desafios do Uso das Metricas

- **Goodhart's Law & Dashboard Ambiguity**: Traditional metric dashboards show *what* changed (e.g., lower deployment frequency) without explaining *why*, creating interpretation ambiguity and risks of unintended incentives [8, 28].
- **Hidden Confounders**: Confounders like organizational culture, toolchain maturity, and team composition create spurious statistical associations between metrics [22].
- **Survey Biases & Noise**: DevEx survey data is susceptible to recall bias, subjective interpretation bias, and temporal noise [22, 29].
- **Unreliability of Pure Algorithmic Learning**: Unconstrained structure learning algorithms (PC/HC) degrade on noisy software engineering data and risk overfitting or including non-causal edges if not guided by domain expertise [20, 22, 29].
- **Temporal & Organizational Variance**: Causal relationships between software metrics evolve over time and vary across project phases and teams [22].
- **CPT Data Sparsity**: Rare or unobserved parent-child state combinations require Dirichlet smoothing (BDeu) to avoid zero probabilities [21].

---

## Avaliacao de Qualidade Metodologica

| Criterio | Pontuacao (0-2) |
|----------|----------------|
| Objetivo claramente definido | 2 [3, 4] |
| Metodologia adequada ao objetivo | 2 [4, 18, 20] |
| Amostra/contexto descrito adequadamente | 2 [4, 6, 7] |
| Ameacas a validade discutidas | 1 [6, 22, 29] |
| Resultados com evidencia suficiente | 2 [5, 12, 14, 15] |
| Contribuicao clara para pratica ou teoria | 2 [3, 26, 27] |
| **TOTAL** | **11/12** |

---

## Limitacoes

- **Context Specificity**: Models and network parameters were developed specifically for Bloomberg's internal survey structure and engineering environment; results may not directly generalize to other companies without adaptation [16, 19, 30].
- **Dependence on Subjective Survey Data**: Key DevEx variables rely on quarterly self-reported Likert-scale engineer survey data, inheriting subjective biases [8, 22, 24].
- **Small Expert Survey Sample Size**: The expert refinement survey relied on \\(n=8\\) DevX team experts, prioritizing domain depth over broad statistical generalization [6].
- **Proprietary Data & Code Access**: Internal survey responses, learned conditional probability tables, and production codebase cannot be shared publicly [19, 30].
- **Early-Stage Deployment**: User study evaluations reflect early-access testing (7 teams, 28 focus group participants); longitudinal studies are needed to evaluate long-term organizational impact [25-27].
- **Lack of Natural Language Explanations**: Participants noted that the interface currently lacks automated textual summaries explaining probability shifts and suggesting best-practice actions [31].

---

## Contribuicao Principal

The principal contribution of this paper is the design, implementation, and empirical evaluation of *BayesInsights*, an industrial tool and hybrid modeling methodology developed at Bloomberg that applies Bayesian Networks to connect software delivery metrics (DORA) with Developer Experience (DevEx) survey data [3, 4, 9]. By combining foundational literature, expert surveys, and structure learning algorithms, the authors demonstrate that causal graphical models can resolve the ambiguity of traditional metric dashboards, empowering software engineering practitioners and leaders to conduct interactive, real-time "what-if" scenario analyses and root-cause identifications [3, 10, 14, 18].

---

*Extraido via NotebookLM em October 2026 para MLR: Software Developer Metrics in Practice*

---

💡 *Would you like me to create a detailed synthesis report or a comparative summary comparing BayesInsights with other software productivity frameworks in your notebook?*
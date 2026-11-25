# P2111 — Productivity Factors in Agile Software Development Projects

**Decisao: INCLUIDO | Qualidade: 3/5**

---

## Dados Bibliograficos

| Campo | Valor |
|-------|-------|
| **ID** | P2111 |
| **Autores** | Mili Turić, Stipe Čelar & Srđana Dragičević [1] |
| **Ano** | 2023 [1] |
| **Venue** | Proceedings of the 34th DAAAM International Symposium on Intelligent Manufacturing and Automation [1] |
| **DOI** | 10.2507/34th.daaam.proceedings.001 [1] |
| **Tipo** | Conference paper (Proceedings article) [1] |
| **Metodo** | Literature review & Experience-based framework proposal [2-4] |
| **Amostra** | Literature overview of secondary/primary studies (mapping studies and surveys with 53 to 616 primary papers and up to 622 developers) [5, 6] combined with 18 personal factors derived from 13 years of practical experience monitoring small agile teams [3, 7] |
| **Contexto** | Industry (Small Agile Software Development projects, Micro/Small software companies) [8, 9] |
| **Modo de trabalho** | Not specified [2, 8, 10] |
| **Metodologia** | Agile Software Development (ASD) / Lean Software Development [2, 11] |

---

## Objetivo

The paper provides a literature overview of productivity factors in Agile Software Development (ASD) and addresses the research gap where existing literature focuses predominantly on team productivity rather than individual developer productivity [2, 10, 12]. Specifically, the paper aims to identify and propose a structured set of 18 personal productivity factors tailored for software developers in small agile software development projects, evaluated on a three-level weighting scale (\\(f=10, 8, 5\\)) based on 13 years of practical industry experience to assist project managers in evaluating developer capability and stabilizing task effort estimation models [2, 4, 7, 8, 10].

---

## Questoes de Pesquisa

Not explicitly defined in the paper (the authors present a narrative literature overview and propose 18 personal productivity factors without defining formally numbered research questions) [2, 13, 14].

---

## Metricas e Instrumentos de Avaliacao

| Metrica | Categoria | Nivel | Como Coletada | Validada |
|---------|-----------|-------|---------------|----------|
| Personal Capability Score (\\(f\\) weighting scale: 10, 8, 5) | Productivity / DevEx | Individual | Expert/Manager assessment assigning weight values across 18 personal factors | Partial (derived from 13 years of monitoring small agile teams) [3, 7] |
| Bug Production Rate (\\(F14\\)) | Quality | Individual | Defect tracking system logs and developer time spent on bug removal | Partial (proposed metric parameter) [15, 16] |
| Self-Rated Productivity | Productivity | Individual | Survey questionnaires administered to developers | Yes (statistically validated by Murphy-Hill et al. across 622 developers) [6] |
| Developer Skills / Task Effort Estimation Score | Productivity / Delivery | Individual / Team | Bayesian Network model calculations using personal capability parameters | Yes (validated in Bayesian Network models by Dragicevic et al. and Turic et al.) [8, 17, 18] |

---

## Frameworks e Metricas

### Frameworks Referenciados
- **Big-Five Personality Traits Framework**: REFERENCED — Cites Iqbal et al. mapping Big-Five personality traits (Openness, Conscientiousness, Extraversion, Agreeableness, Neuroticism) to Software Life Cycle (SLC) phases and developer soft skills [6, 19].
- **Lean Software Development / Lean Management**: REFERENCED — Cites Lean principles as the foundation for Agile Software Development methodologies aimed at eliminating process waste [11].
- **Bayesian Network Effort Estimation Model**: REFERENCED / APPLIED — Discusses Bayesian Network models (Dragicevic et al. and Turic et al.) that utilize a 'Developer skills' node fed by personal productivity parameters [8, 17, 18].
- **Traditional Effort Estimation Techniques**: REFERENCED — Mentions Functional Analysis and Planning Poker as traditional estimation frameworks [11].
- *Note*: DORA, SPACE, DevEx, GQM, HEART, and OKR frameworks are NOT mentioned or referenced in this paper [2, 10, 14, 20].

### Frameworks Propostos
- **18 Personal Productivity Factors & Three-Level Weighting Framework**: Proposes a capability assessment framework consisting of 18 personal productivity factors (F1 to F18) categorized for individual developers in small agile projects [4, 16, 21]. Each factor is assigned a numerical weighting value on a three-level scale (\\(f=10\\) for very important, \\(f=8\\) for medium importance, \\(f=5\\) for non-crucial/good-to-have) based on 13 years of practical experience to quantify developer capability for ASD effort estimation models [3, 7].

---

## Fatores que Influenciam Produtividade

### Fatores Positivos
| Fator | Categoria |
|-------|-----------|
| Work experience in similar jobs (F1) | Human / Technical [21] |
| Knowledge of technology (F2) | Technical [22] |
| Level of learning and work habits (F3) | Human / Process [22] |
| Ability to work autonomously (F4) | Human [22] |
| Work complexity handling capacity (F5) | Technical / Process [23] |
| Identification with project and positive attitude towards work (F6) | Human [23] |
| High concentration and focus (F7) | Human [23] |
| Skill in performing specific work types (F8) | Technical / Human [24] |
| Knowledge of the project plan and objectives (F9) | Organizational / Process [24] |
| Knowledge of the overall product and architecture (F10) | Technical / Organizational [24] |
| Responsibility and influence on decision making (F11) | Organizational / Human [24] |
| Effective team communication (F12) | Human [24] |
| Agility (dexterity and diligence in task performance) (F13) | Human / Process [15] |
| Knowledge of the business area/domain (F15) | Technical / Organizational [16] |
| Testing effort during development to reduce defects (F16) | Process / Technical [16] |
| Experience in performing similar tasks (F17) | Technical / Human [16] |
| Job enthusiasm, peer support for new ideas, and performance feedback | Human / Organizational [6] |
| Team effectiveness, team management, motivation, and customer satisfaction | Organizational / Process [25] |
| Staff skills, user cooperation, available tools, and appropriate programming language choice | Technical / Human / Process [12] |

### Fatores Negativos
| Fator | Categoria |
|-------|-----------|
| High rate of bug production and time spent removing bugs (F14) | Technical / Quality [15] |
| High need for daily supervision and mentoring (F18) | Human / Process [16] |
| Schedule and resource constraints | Organizational / Process [12] |
| High problem complexity, code complexity, and data complexity | Technical [12] |
| Instability and unreliability in effort estimation caused by unpredictable human factors | Human / Process [8] |
| Subjectivity and lack of measurable criteria for productivity impact | Process / Organizational [13] |

---

## Papel da IA e Automacao

| Campo | Valor |
|-------|-------|
| Usa IA/ML? | Yes — The paper cites studies that introduce Artificial Intelligence (AI) and Machine Learning (ML) techniques (e.g., Decision Trees, Ensemble methods, Bayesian Networks) to improve effort and cost estimation accuracy in Agile Software Development [11, 17, 18, 26-28]. |
| Automacao de coleta? | No — Quantification of the 18 productivity factors relies on manual, expert evaluation and subjective weighting by project managers rather than automated tool collection [7, 13]. |
| Impacto de IA na produtividade? | The paper highlights that AI/ML models enhance effort estimation accuracy, but does not empirically measure AI's direct impact on developer productivity itself [3, 11, 26]. |

---

## Resultados Principais

- Existing literature on productivity in Agile Software Development is predominantly team-oriented, with individual developer productivity factors rarely isolated or highlighted [4, 12, 25].
- Comprehensive literature studies identify extensive factor lists: Jones identified >200 productivity and quality factors [12, 14]; Matos et al. cataloged 90 effort factors [26]; Dutra et al. identified 101 human factors [25]; Guerrero-Calvache & Hernández mapped 63 team productivity factors across 616 studies [5]; and Iqbal et al. classified 77 teamwork factors across 53 studies into 6 groups (technical, non-technical, organizational, environmental, project management, user requirements) [5, 29].
- In a survey of 622 developers across 3 US companies, 48 factors were identified, with job enthusiasm, peer support for new ideas, and useful feedback about job performance emerging as the 3 most statistically significant predictors of developer productivity [6].
- Individual developer productivity has a significantly higher relative impact in small teams and micro/small software companies than in large organizations [8].
- The authors synthesize and define 18 personal productivity factors (F1–F18) tailored specifically for developers in small ASD projects [4, 16, 21].
- A three-level weighting scale (\\(f=10\\) for very important, \\(f=8\\) for medium importance, \\(f=5\\) for non-crucial/good-to-have) derived from 13 years of practical experience in small agile teams provides a practical mechanism to quantify developer capability for effort estimation models [3, 7].

---

## Desafios do Uso das Metricas

- **Measurement Subjectivity**: Establishing measurable criteria for productivity factors is difficult because productivity assessment remains largely subjective and context-dependent [13].
- **Human Factor Instability**: Developer capability ('Developer skills' node in estimation models like Bayesian Networks) represents a human factor that introduces model instability and unreliability [8].
- **Unequal Factor Weighting**: Productivity factors do not contribute equally to productivity, requiring customized weighting scales rather than uniform metrics [7].
- **Neglect of Individual Variance**: Literature and agile frameworks focus almost exclusively on team-level metrics, ignoring the fact that individual developers can be multiple times more productive than peers with similar backgrounds [4, 12, 29].

---

## Avaliacao de Qualidade Metodologica

| Criterio | Pontuacao (0-2) |
|----------|----------------|
| Objetivo claramente definido | 2 |
| Metodologia adequada ao objetivo | 1 |
| Amostra/contexto descrito adequadamente | 1 |
| Ameacas a validade discutidas | 0 |
| Resultados com evidencia suficiente | 1 |
| Contribuicao clara para pratica ou teoria | 2 |
| **TOTAL** | **7/12** |

*Justification*: The objective is clearly formulated (2/2) [2, 10]. The narrative literature overview and expert proposal are adequate for a symposium summary, though lacking systematic review protocols (1/2) [2, 14]. Context (small agile teams) is specified, but sample details for the proposed weighting scale rely on informal reference to 13 years of experience (1/2) [3, 8]. Threats to validity are not explicitly discussed (0/2) [4, 13]. Literature evidence supports factor selection, but empirical statistical validation of the proposed weights is left for future work (1/2) [4, 9]. The contribution provides a practical, directly applicable 18-factor catalog for software project managers (2/2) [4, 7, 21]. Total score: 7/12 (approx. 3/5 quality rating) [1, 4].

---

## Limitacoes

- The 18 personal productivity factors and three-level weighting scale are proposed based on narrative literature synthesis and 13 years of author practical experience, without formal statistical validation in this publication [3, 4, 7].
- The formal integration and empirical validation of these 18 factors within Bayesian Network task estimation models are deferred to future research [4, 9].
- The literature overview provided is narrative rather than a formal Systematic Literature Review (SLR) or Systematic Mapping Study [2, 5, 14].
- The proposed weighting values (5, 8, 10) are subjective and require manual calibration by each company to match its specific operating environment [3].

---

## Contribuicao Principal

The principal contribution of this paper is the proposal of a practical catalog of 18 personal productivity factors (F1–F18) tailored specifically for software developers in small agile projects, paired with a three-level weighting scale (\\(f=10, 8, 5\\)) derived from 13 years of industry experience [2, 4, 7, 21]. This work addresses a critical gap in agile software engineering literature—which overwhelmingly focuses on team-level productivity—by providing project managers in micro and small software companies with a manageable framework to evaluate individual developer capability and stabilize agile task effort estimation models [3, 4, 8, 10].

---

*Extraido via NotebookLM em October 2026 para MLR: Software Developer Metrics in Practice*

💡 **Next Step**: Would you like me to generate a tailored report or comparison slide deck summarizing these 18 productivity factors for your software engineering management review?
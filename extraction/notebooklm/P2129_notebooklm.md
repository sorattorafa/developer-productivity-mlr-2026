# P2129 — Copilot's island of joy: balancing individual satisfaction with team interaction in agile development

**Decisao: INCLUIDO | Qualidade: 4.5/5**

---

## Dados Bibliograficos

| Campo | Valor |
|-------|-------|
| **ID** | P2129 [1] |
| **Autores** | Viggo Tellefsen Wivestad, Astri Barbala, Viktoria Stray [1] |
| **Ano** | 2025 [2] |
| **Venue** | XP 2024 Workshops, LNBIP 524 [2] |
| **DOI** | 10.1007/978-3-031-72781-8_13 [2] |
| **Tipo** | Conference paper (Workshop paper) [2] |
| **Metodo** | Quantitative (Exploratory, cross-sectional, natural quasi-experiment) [3, 4] |
| **Amostra** | 115 participants (67 Copilot users and 48 non-users; 81% inhouse employees, 15% women, 79% men, 1% other, 5% undisclosed) [4, 5] |
| **Contexto** | Industry / Public sector (National Welfare Administration - NAV, Norway; IT department with ~1000 employees) [3] |
| **Modo de trabalho** | Not specified [4, 6] |
| **Metodologia** | Agile (Scrum, continuous software engineering, data-driven practices) [2, 3] |

---

## Objetivo

The main objective of this study is to evaluate the adoption and impact of GitHub Copilot in agile software development within a large public sector organization (NAV in Norway) by conducting a comparative quasi-experimental analysis between users and non-users to assess differences in perceived productivity, job satisfaction, task focus, collaboration, and team dependency [1, 3, 4].

---

## Questoes de Pesquisa

- **RQ1**: What benefits of using GitHub Copilot can be identified when comparing users to a control group? [7]

---

## Metricas e Instrumentos de Avaliacao

| Metrica | Categoria | Nivel | Como Coletada | Validada |
|---------|-----------|-------|---------------|----------|
| **Copilot is valuable** ("I view Copilot as a valuable tool for developers") [8, 9] | Satisfaction / DevEx | Individual | Survey (5-point Likert scale, T2B analysis) [8, 10, 11] | Yes (p = 0.000 < 0.0056) [8, 11] |
| **Can focus on satisfying work** ("I am able to focus on satisfying work most of my work time") [5, 8, 9] | DevEx / Efficiency and flow | Individual | Survey (5-point Likert scale, T2B analysis) [8, 10, 11] | Yes (p = 0.002 < 0.0056) [5, 8, 11] |
| **Satisfied with job** ("I feel satisfied with my job") [8, 9, 12] | Satisfaction | Individual | Survey (5-point Likert scale, T2B analysis) [8, 10, 11] | Partial (p = 0.031; not significant under Bonferroni corrected threshold) [5, 8, 11] |
| **Is in flow when coding** ("I often find myself 'in the flow' while coding") [8, 9] | Efficiency and flow | Individual | Survey (5-point Likert scale, T2B analysis) [8, 10, 11] | No (p = 0.273) [8] |
| **Productive when coding** ("I feel productive when I code") [8, 9] | Productivity / Performance | Individual | Survey (5-point Likert scale, T2B analysis) [8, 10, 11] | No (p = 0.490) [8] |
| **Critical of AI in public sector** ("I am critical of the use of AI-tools in the public sector") [8, 9, 13] | Satisfaction / Governance | Individual / Organization | Survey (5-point Likert scale, T2B analysis) [8, 10, 11] | Yes (p = 0.000 < 0.0056) [8, 11, 13] |
| **Dependent on colleagues** ("I am dependent on colleagues for help and guidance") [8, 9, 13] | Collaboration | Team / Individual | Survey (5-point Likert scale, T2B analysis) [8, 10, 11] | Yes (p = 0.003 < 0.0056) [8, 11, 13] |
| **Frustrated when coding** ("I often feel frustrated during coding sessions") [8, 9, 14] | Satisfaction / DevEx | Individual | Survey (5-point Likert scale, T2B analysis) [8, 10, 11] | No (p = 0.075) [8] |
| **Searches for information online** ("Searching for information and resources online is a central part of my job") [8, 9] | Activity / DevEx | Individual | Survey (5-point Likert scale, T2B analysis) [8, 10, 11] | No (p = 0.360) [8] |

---

## Frameworks e Metricas

### Frameworks Referenciados
- **SPACE Framework**: REFERENCED and APPLIED — The study adapted survey items based on GitHub Research's survey, which utilizes the five SPACE dimensions: Satisfaction and well-being, Performance, Activity, Communication and collaboration, and Efficiency and flow [7, 15].

### Frameworks Propostos
- None proposed [4, 15].

---

## Fatores que Influenciam Produtividade

### Fatores Positivos
| Fator | Categoria |
|-------|-----------|
| Utilization of GitHub Copilot (AI coding assistants) to move past frustrating tasks and focus on engaging, satisfying work [1, 5] | Technical / Process |
| Reduced individual dependency on colleagues for basic help and troubleshooting [1, 13] | Human / Process |
| Higher overall job satisfaction among developers [5, 12] | Human |
| Continuous software engineering and data-driven organizational practices [3] | Process / Organizational |

### Fatores Negativos
| Fator | Categoria |
|-------|-----------|
| Potential reduction in team interaction, knowledge sharing, and agile collaboration ("island of joy" isolation) [1, 6, 9] | Human / Organizational / Process |
| Coding session frustration and tedious/demotivating tasks [5, 14] | Human / Process |
| Skepticism regarding data privacy and unannounced data collection in the public sector [13] | Organizational / Human |
| Higher interaction barriers for remote team members [6] | Organizational / Process |

---

## Papel da IA e Automacao

| Campo | Valor |
|-------|-------|
| **Usa IA/ML?** | Yes — GitHub Copilot (Generative AI coding assistant) evaluated across agile software product teams [1, 3, 16]. |
| **Automacao de coleta?** | No — Data was collected using an online survey instrument (57 items) and analyzed quantitatively using Python (Mann-Whitney U test, RBC, CLES) [10, 11]. |
| **Impacto de IA na produtividade?** | Copilot users demonstrated a statistically significant increase in focus on satisfying work (72% vs 50%, p = 0.002) and a statistically significant drop in reliance on colleagues (45% vs 21% disagreement, p = 0.003) [5, 13]. However, differences in perceived coding productivity (86% vs 80%) and flow state (68% vs 62%) were not statistically significant compared to the control group [8, 9, 14]. Increased autonomy also carries a risk of team isolation ("islands of joy") [1, 6, 9]. |

---

## Resultados Principais

- **Enhanced Focus on Satisfying Tasks**: Copilot users reported a statistically significant higher ability to focus on satisfying work compared to non-users (72% vs 50%, p = 0.002, CLES = 0.657) [5, 8].
- **Decreased Dependence on Colleagues**: Copilot users were significantly less dependent on colleagues for help and guidance, with 45% of users disagreeing that they rely on colleagues versus only 21% of non-users (p = 0.003, CLES = 0.658) [8, 13].
- **Lower Skepticism Toward AI in Public Sector**: Users were significantly less critical of AI tool usage in the public sector than non-users (64% disagreed with being critical vs 34% of non-users, p = 0.000, CLES = 0.705) [8, 13].
- **Perceived Tool Value**: 82% of users viewed Copilot as a valuable tool compared to 51% of non-users (p = 0.000) [8, 9, 17].
- **Non-Significant Differences**:
  - **Job Satisfaction**: Users reported higher job satisfaction (87% vs 73%), but the difference was not statistically significant under the Bonferroni-corrected threshold (p = 0.031 > 0.0056) [5, 8, 14].
  - **Flow and Productivity**: Perceived flow state (68% vs 62%, p = 0.273), coding productivity (86% vs 80%, p = 0.490), coding frustration (59% vs 48% disagreement, p = 0.075), and online searching (3% vs 5% disagreement, p = 0.360) showed no statistically significant differences between groups [8, 9, 14].
- **Emergence of "Islands of Joy"**: While AI coding assistants improve individual developer satisfaction and self-reliance, they may inadvertently decrease team collaboration and knowledge sharing, posing new challenges for Scrum Masters and agile team dynamics [1, 6, 9].

---

## Desafios do Uso das Metricas

- **Selection and Motivation Bias**: Non-randomized group allocation (volunteers vs. non-users) makes it difficult to separate true tool efficacy from baseline user motivation or self-selection bias [4, 12, 17].
- **Expectancy Effects**: Perceived gains reported in un-controlled surveys (e.g. flow and productivity) were not confirmed statistically when comparing against a control group, indicating possible user expectancy effects [12].
- **Agile Anti-Patterns (Developer Isolation)**: Over-reliance on AI assistants can reduce spontaneous peer interactions, resulting in knowledge silos and individual "islands of joy" that conflict with agile principles of team interaction [1, 6, 9].
- **Governance and Privacy Concerns**: Skepticism among non-users regarding data usage, privacy, and unannounced data processing in public sector contexts [13].

---

## Avaliacao de Qualidade Metodologica

| Criterio | Pontuacao (0-2) |
|----------|----------------|
| Objetivo claramente definido | 2 |
| Metodologia adequada ao objetivo | 2 |
| Amostra/contexto descrito adequadamente | 2 |
| Ameacas a validade discutidas | 1 |
| Resultados com evidencia suficiente | 2 |
| Contribuicao clara para pratica ou teoria | 2 |
| **TOTAL** | **11/12** |

---

## Limitacoes

- **Non-Randomized Control Group**: The experiment and control groups were not randomly assigned, introduce potential self-selection bias and pre-existing motivational differences [4, 12, 17].
- **Cross-Sectional Nature**: The study captures developer sentiment at a single point in time rather than tracking longitudinal performance over time [4].
- **Single Public Sector Context**: Conducted exclusively within one public sector organization in Norway (NAV), which may constrain generalizability to private sector or non-agile environments [3, 18].
- **Subjective Survey Measures**: Relies on self-reported perception items rather than direct telemetry or repository metrics (such as cycle time, commit frequency, or code quality metrics) [10, 15].
- **Rephrased Survey Items**: Generalizing original Copilot-specific questions to enable group comparison may have introduced vagueness, potentially masking subtle tool-specific impacts [12, 15].

---

## Contribuicao Principal

This paper presents an empirical comparative evaluation of GitHub Copilot within an agile public sector software organization (NAV), comparing active users with a non-user control group using adapted SPACE framework metrics [3, 7, 15]. The authors demonstrate that while Copilot significantly increases developers' focus on satisfying tasks and reduces individual reliance on colleagues, it does NOT deliver statistically significant improvements in overall perceived coding productivity or flow state [1, 5, 8, 14]. Crucially, the paper introduces the concept of "islands of joy," warning that gains in individual developer satisfaction must be carefully managed by Scrum Masters to prevent developer isolation and maintain agile team collaboration, knowledge sharing, and cohesion [1, 6, 9].

---

*Extraido via NotebookLM em October 2026 para MLR: Software Developer Metrics in Practice*

---

💡 Would you like me to generate a structured comparison table or draft a presentation slide deck summarizing these findings for your literature review?
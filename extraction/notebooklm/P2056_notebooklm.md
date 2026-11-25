# P2056 — Understanding developer well-being: measuring mental health and productivity in software teams

**Decisao: INCLUIDO | Qualidade: 5/5** [1-4]

---

## Dados Bibliograficos

| Campo | Valor |
|-------|-------|
| **ID** | P2056 [5] |
| **Autores** | Johny Arriel, Theo Canuto, Júlia Azevedo, Maria Vitoria Lima, Paulo Mann, Alessandro Garcia, Juliana Alves Pereira [5, 6] |
| **Ano** | 2026 [5] |
| **Venue** | Empirical Software Engineering [5] |
| **DOI** | 10.1007/s10664-026-10830-6 [5] |
| **Tipo** | Journal article [5] |
| **Metodo** | Mixed methods (Systematic literature mapping, survey, and structured interviews) [7-9] |
| **Amostra** | 47 software developers in the survey, 22 of whom participated in structured interviews; 178 initial papers mapped resulting in 65 relevant studies [7, 10, 11] |
| **Contexto** | Industry (36 Private sector, 5 Non-profit, 3 Startups, 2 Public sector; company sizes ranging from <9 to 500+ employees) [12, 13] |
| **Modo de trabalho** | Hybrid (26), In-person (22), Fully remote (16) [13] |
| **Metodologia** | Workflow-agnostic (Agile/Scrum used as primary operational setting, with non-Agile/hybrid mappings provided) [14, 15] |

---

## Objetivo

The primary objective of this paper is to propose and evaluate a catalog of 12 metrics designed to measure developer mental health and productivity in software engineering teams [7, 16]. Grounded in organizational psychology theories, the study maps key factors influencing well-being and performance, establishes structured measurement strategies combining self-reports, peer feedback, and automated tool data, and empirically evaluates software developers' perceptions regarding the clarity, applicability, and acceptance of these metrics in industrial contexts [7, 16-18].

---

## Questoes de Pesquisa

- **RQ1:** How do software developers define mental health and productivity? [19]
- **RQ2:** How do software developers perceive the catalog of measurements and metrics as indicators of mental health and productivity? [20]
- **RQ3:** How can the catalog support project managers in promoting productivity while ensuring developers’ mental health? [21]

---

## Metricas e Instrumentos de Avaliacao

| Metrica | Categoria | Nivel | Como Coletada | Validada |
|---------|-----------|-------|---------------|----------|
| **Self Vision (SVI)** | Individual Productivity / DevEx [14, 22] | Individual [22] | Daily self-rating score (IPP) on a 1–10 scale via custom App with visual anchors [23, 24] | Partial [7, 17] |
| **Team Vision (TVI)** | Individual Productivity / Collaboration [22, 25] | Team / Individual [22, 26] | Daily 360° peer-rating score (TPP = S/N) assessing peer productivity/collaboration via App [23, 26] | Partial [7, 17] |
| **Work Vision (WVI)** | Individual Mental Health / DevEx [22, 27] | Individual / Team [22, 28] | Weekly percentage calculation comparing self-assessment against team perception: WVI = (IPP - TPP) * 10 [23, 28] | Partial [7, 17] |
| **Work Capacity (WCA)** | Productivity / Delivery [22, 29] | Individual / Team [22, 29] | Percentage of completed vs. assigned story points (PCSP = CSP/ASP * 100) via Jira or task completion rate [23, 30] | Partial [7, 31] |
| **Work Environmental Conditions (WEC)** | Individual Mental Health / Team Mental Health [32, 33] | Team / Organization [32, 34] | Percentage of checked items on a workplace condition checklist (PCI = IC/TIC * 100) via App during retrospectives/milestones [23, 34] | Partial [7, 17] |
| **Turnover (TOV)** | Team Mental Health / Satisfaction [35-37] | Team / Project [35, 36] | Project-level turnover rate: TR = (NLD/OTS) * 100 tracking team departures via App/HR logs [23, 38] | Partial [7, 31] |
| **Quality of Social Interactions (QSI)** | Individual Mental Health / Team Mental Health [35, 38] | Individual / Team [35, 39] | Percentage of negative interactions (PNI = TTN/TT * 100) classified automatically using AI/NLP sentiment analysis on communication platforms (GitHub, Slack, Jira) [23, 39, 40] | Partial [7, 41] |
| **Absenteeism (ABS)** | Individual Mental Health / Activity [35, 42] | Individual / Team [35, 43] | Absenteeism rate tracking last-minute rescheduling or unjustified absences: AR = (TRE/TS) * 100 via App [23, 43] | Partial [7, 31] |
| **Missed Tasks (MTA)** | Productivity / Activity [35, 43] | Individual / Team [35, 44] | Percentage of tasks in progress not updated for more than 24 hours: PMT = (ToM/ToT) * 100 via Jira [23, 44] | Partial [7, 31] |
| **Motivation (MOT)** | Individual Mental Health / DevEx [35, 45] | Individual [35, 46] | Composite metric formula: MOT = 100 - ((QSI + AR + PMT) / 3) combining normalized subcomponents via Jira/App [23, 46, 47] | Partial [7, 17] |
| **Number of Commits (NOC)** | Productivity / Activity [18, 48] | Individual / Team [18, 49] | Total count of code commits extracted directly from version control systems (Git, GitHub, GitLab) [23, 48, 49] | Yes [31, 48] |
| **Number of Resolved Issues (NRI)** | Productivity / Delivery [18, 49] | Individual / Team [18, 50] | Total count of resolved or closed issues extracted from issue trackers (Jira, GitHub Issues) [23, 49, 50] | Yes [31, 51] |

---

## Frameworks e Metricas

### Frameworks Referenciados
- **Job Demands–Resources (JD-R) Model**: REFERENCED — Used as the theoretical foundation for TVI, WCA, ABS, MTA, and MOT to capture job resources and burnout strain [25, 29, 42, 43, 45, 52].
- **Self-Determination Theory (SDT)**: REFERENCED — Used to ground SVI, QSI, and MOT regarding psychological needs for autonomy, competence, and relatedness [14, 38, 45, 52, 53].
- **Conservation of Resources (COR) Theory**: REFERENCED — Used to explain resource loss spirals and resource conservation mechanisms in WCA, WEC, TOV, ABS, and MTA [29, 33, 34, 42, 52, 53].
- **Cognitive Evaluation Theory (CET)**: REFERENCED — Applied as an SDT sub-theory for self-evaluation and intrinsic motivation in SVI [14, 54].
- **Person-Environment Fit Theory**: REFERENCED — Applied to justify alignment between environmental attributes and developer needs in WEC [33].
- **Social Exchange Theory (SET) & Social Capital Theory**: REFERENCED — Cited for reciprocity and relational dynamics in TOV and QSI [37, 38].
- **Socio-Technical Congruence (STC)**: REFERENCED — Discussed in the evaluation of team collaboration and communication alignment [55].

### Frameworks Propostos
- **Developer Mental Health and Productivity Metrics Catalog & Conceptual Causal Model**: A proposed 12-metric framework organized across three theoretical layers: (1) *Individual Psychological Mechanisms* (SVI, MOT, ABS, MTA), (2) *Social and Environmental Dynamics* (WEC, TVI, QSI, WVI), and (3) *Productivity Outcomes and Resource Dynamics* (WCA, NOC, NRI, TOV) [17, 56]. It includes a conceptual causal diagram outlining positive and negative feedback loops among mental health and productivity indicators [54, 57].

---

## Fatores que Influenciam Produtividade

### Fatores Positivos
| Fator | Categoria |
|-------|-----------|
| Motivation boost & Job enthusiasm [58, 59] | Human [58, 59] |
| Team cohesion, collaboration, and mutual support [58, 60] | Human / Process [58, 60] |
| Clear communication & Positive work culture [58-60] | Organizational / Human [58-60] |
| Proper tooling & Supportive environmental conditions [33, 53, 61] | Technical / Organizational [33, 53, 61] |
| Autonomy & Perceived competence [14, 53] | Human / Organizational [14, 53] |
| Meaningful feedback & Recognition [58] | Organizational / Human [58] |

### Fatores Negativos
| Fator | Categoria |
|-------|-----------|
| Work overload & Unrealistic deadlines [62, 63] | Process / Organizational [62, 63] |
| Unhealthy competition & Pressure from reward systems [59, 64] | Organizational / Human [59, 64] |
| Inadequate tools & Context switching [53] | Technical / Process [53] |
| Role ambiguity & Unclear expectations [62] | Organizational / Process [62] |
| Perceived privacy invasion & Digital surveillance [65-67] | Organizational / Human [65-67] |
| High project turnover & Frequent member rotation [36, 37] | Organizational / Process [36, 37] |

---

## Papel da IA e Automacao

| Campo | Valor |
|-------|-------|
| **Usa IA/ML?** | Yes — NLP and sentiment analysis models (e.g., SE-specific or general classifiers) are used to detect negative communication for QSI, and ML is proposed for future burnout prediction [39, 68, 69]. |
| **Automacao de coleta?** | Yes — Automated data collection integrated with software development infrastructure (GitHub, Git, Jira, Slack, Teams) [18, 23, 70, 71]. |
| **Impacto de IA na produtividade?** | Developers expressed skepticism regarding AI reliability in correctly capturing sarcasm, tone, and context in technical text, warning that inaccurate AI classification creates surveillance anxiety and damages trust [41, 66, 72]. |

---

## Resultados Principais

- **Gap between metric acceptance and evaluative application**: Over 80% of developers approved the proposed measurement mechanisms (formulas and data inputs), but approval dropped by more than 60% for metrics like NOC when used as evaluative workplace performance tools due to privacy and autonomy concerns [7, 67, 73].
- **Dissatisfaction with isolated output metrics**: NOC (Number of Commits) was heavily rejected as a productivity indicator (74%+ negative citations) for measuring quantity over quality and ignoring collaboration [74, 75].
- **High approval for delivery and progress metrics**: Work Capacity (WCA) and Missed Tasks (MTA) received widespread approval (>80% acceptance) for focusing on completed complexity and identifying stagnant progress rather than counting raw activities [67, 74, 75].
- **Strong resistance to AI surveillance**: Quality of Social Interactions (QSI) faced the strongest resistance due to privacy concerns (77%+ concerns raised), behavioral distortion under monitoring, and doubts over AI sentiment accuracy [41, 66, 72, 76].
- **Praise for self-other alignment**: Work Vision (WVI) received the highest positive rating (10 positive citations, 0 negative) for helping developers identify personal self-assessment bias against team peer perceptions [75, 77].
- **Expanded view of mental health and productivity**: 100% of interviewed developers associated mental health with overall mental well-being (extending WHO definitions to include coping and physical health), and 82% identified organizational/managerial "expectations" as the primary driver of productivity [78-80].
- **Unanimous managerial utility**: 100% of developers agreed that the catalog is an extremely useful resource for project managers when applied non-punitively, recommending metric customization (36%) and avoiding metric overload (45%) [81, 82].

---

## Desafios do Uso das Metricas

- **Evaluative Misuse & Surveillance Stress**: Framing well-being or productivity metrics as punitive or evaluative tools creates anxiety, reduces autonomy, and fosters counterproductive work behaviors [65, 67, 73].
- **Privacy Concerns**: Automated monitoring of chat logs or code review comments (e.g., QSI via AI) is perceived as an invasive surveillance practice that undermines psychological safety [41, 66].
- **Metric Overload**: Attempting to track all 12 metrics simultaneously causes participant fatigue and dilutes managerial focus [82].
- **Superficiality of Raw Activity Metrics**: Metrics like commit counts fail to account for task complexity, code quality, architectural design, or context switching [16, 48, 74].
- **AI Sentiment Inaccuracy**: Generic AI models struggle with developer jargon, sarcasm, and emotional nuances, leading to false classifications in social interaction metrics [68, 72].

---

## Avaliacao de Qualidade Metodologica

| Criterio | Pontuacao (0-2) |
|----------|----------------|
| Objetivo claramente definido | 2 [7, 16, 83] |
| Metodologia adequada ao objetivo | 2 [7-9] |
| Amostra/contexto descrito adequadamente | 2 [12, 13, 84] |
| Ameacas a validade discutidas | 2 [1-4] |
| Resultados com evidencia suficiente | 2 [85-87] |
| Contribuicao clara para pratica ou teoria | 2 [17, 88, 89] |
| **TOTAL** | **12/12** |

---

## Limitacoes

- Sample size constrained to 47 survey respondents and 22 interviewees, predominantly sourced from specific professional networks in Brazil [3, 84].
- Initial validation focused on perceived usefulness, clarity, and applicability prior to long-term real-world longitudinal deployment [90-92].
- Sequential survey-interview design introduced potential anchoring effects toward the predefined 12-metric catalog [91].
- Certain metrics rely heavily on Agile artifacts (e.g., story points for WCA), requiring manual adaptation for non-Agile development environments [3, 15].
- Dataset size limited the feasibility of exploratory factor analysis (EFA) or principal component analysis (PCA) for structural redundancy verification [93, 94].

---

## Contribuicao Principal

The primary contribution of this paper is the proposal and empirical evaluation of a 12-metric catalog for software developer mental health and productivity, grounded in organizational psychology theories (SDT, JD-R, COR) [7, 17, 52]. Combining qualitative and quantitative feedback from software developers, the paper demonstrates how developers conceptualize well-being and productivity, reveals the significant gap between measurement mechanism acceptance and evaluative resistance, and outlines actionable guidelines and an implementation roadmap for project managers to sustainably foster developer health and performance [7, 17, 89, 92, 95].

---

*Extraido via NotebookLM em October 2026 para MLR: Software Developer Metrics in Practice*
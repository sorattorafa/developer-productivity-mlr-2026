# P2073 — Beyond Productivity Gains: Analyzing the Effects of AI-assisted Coding Tools on Developer Experience within a Brazilian Fintech Organization

**Decisao: INCLUIDO | Qualidade: 5/5** [1, 2]

---

## Dados Bibliograficos

| Campo | Valor |
|-------|-------|
| **ID** | P2073 [1] |
| **Autores** | Sabrina C. Winckler, Josiane Kroll, Leticia S. Machado [3] |
| **Ano** | 2026 [2] |
| **Venue** | SBES 2026 (Brazilian Symposium on Software Engineering) [2] |
| **DOI** | 10.5281/zenodo.21938780 [4] |
| **Tipo** | Conference paper [2] |
| **Metodo** | Mixed methods (Longitudinal case study, Repository mining, CI/CD & AI telemetry, Retrospectives, Semi-structured interviews) [1, 5-7] |
| **Amostra** | 78 repositories and 27 developers active across both Q3-2024 and Q3-2025 observation periods; 33 total workforce in Q3-2025; 9 practitioners for qualitative feedback [1, 2, 8] |
| **Contexto** | Industry (Brazilian financial technology company / fintech) [1, 9] |
| **Modo de trabalho** | Not specified [1, 10] |
| **Metodologia** | Agile / DevOps (characterized by sprint quarters, CI/CD pipelines, PR/MR code review workflows, Jira ticketing, and retrospectives) [5-7, 11] |

---

## Objetivo

The paper investigates how the adoption of AI-assisted coding tools (GitHub Copilot and Windsurf) affects developer experience (DevEx), cognitive load, feedback loops, and team workflows within a Brazilian fintech organization [1, 10]. By comparing pre-adoption (Q3-2024) and post-adoption (Q3-2025) periods using telemetry, repository mining, and qualitative evidence, the study evaluates whether task-level productivity gains translate into system-level organizational delivery performance [1, 2, 12].

---

## Questoes de Pesquisa

- **RQ1**: How do AI-assisted coding tools affect feedback loops (e.g., CI/CD pipelines, code review cycles, and access to technical information)? [10]
- **RQ2**: How do AI-assisted coding tools affect cognitive load (e.g., code comprehension, AI-generated code validation, prompt formulation, and incident resolution)? [10]
- **RQ3**: How do AI-assisted coding tools affect flow state (e.g., developer-reported experience, task focus, and learning)? [10]

---

## Metricas e Instrumentos de Avaliacao

| Metrica | Categoria | Nivel | Como Coletada | Validada |
|---------|-----------|-------|---------------|----------|
| **Pipeline Frequency** | Activity / Delivery | Team/Organization | CI/CD Telemetry (GitLab & Bitbucket) [6, 11] | Yes [6] |
| **Pipeline Duration** | Activity / Delivery | Team/Organization | CI/CD Telemetry (GitLab & Bitbucket) [6, 11] | Yes [6] |
| **Pipeline Success Rate** | Quality / Delivery | Team/Organization | CI/CD Telemetry (GitLab & Bitbucket) [6, 11] | Yes [6] |
| **Pull Request (PR) Creation Volume** | Activity / Delivery | Individual/Team | Repository mining (GitLab & Bitbucket) [6, 11] | Yes [6] |
| **Median PR Review Time** | Delivery / Collaboration | Team | Repository mining (GitLab & Bitbucket) [6, 11] | Yes [6] |
| **Median PR Merge Time** | Delivery / Flow | Team | Repository mining (GitLab & Bitbucket) [6, 11] | Yes [6] |
| **Commit Frequency** | Activity | Individual/Team | Repository mining across 78 repositories [6, 13, 14] | Yes [6] |
| **Commit Type Distribution** | Process / Activity | Individual/Team | Repository message mining (Feature, Fix/Bug, Docs, Test, Refactor, Update, Chore, Other) [6, 13, 14] | Yes [6] |
| **Normalized Code Churn per Commit** | Quality / Activity | Individual/Team | Repository mining (lines added/deleted per contribution) [6, 13, 14] | Yes [6] |
| **Issue / Incident Volume** | Quality / Delivery | Organization | Jira ticket records [6, 15] | Yes [6] |
| **Median Incident Resolution Time** | Quality / Delivery | Team/Organization | Jira ticket records [6, 15] | Yes [6] |
| **Copilot Suggestion Acceptance Rate** | DevEx / Activity | Individual/Team | GitHub Copilot Telemetry via Copilot Metrics Viewer v2.0.2 (by count and lines of code) [6, 14, 16] | Partial [6, 14] |
| **AI Engagement (Completions & Chat Turns)** | DevEx / Activity | Individual/Team | GitHub Copilot Telemetry via Copilot Metrics Viewer v2.0.2 [6, 16, 17] | Partial [6] |
| **Developer Perceptions of Flow, Feedback, and Cognitive Load** | DevEx / Satisfaction | Individual | Participant observation, DevEx-inspired retrospective board, and semi-structured interviews [5, 7, 18] | Yes [7] |

---

## Frameworks e Metricas

### Frameworks Referenciados
- **DevEx Framework (Forsgren et al., Greiler et al.)**: **APPLIED** — Serves as the primary analytical lens throughout the study, evaluating feedback loops, cognitive load, and flow state [1, 5, 19].
- **SPACE Model (Forsgren et al.)**: **APPLIED** — Used to structure the qualitative interview protocol across its six core themes (Satisfaction, Performance, Activity, Communication, Efficiency/flow) [7].
- **DevEx in Action**: **APPLIED** — Used as a structured retrospective board instrument for team data collection [7].

*(Note: Frameworks such as DORA, GQM, HEART, or OKR were not explicitly cited or applied in this paper.)*

### Frameworks Propostos
The paper does not propose a new formal metric framework [1, 20]. Instead, it extends the practical application of the DevEx framework to AI-assisted coding adoption, conceptualizing AI adoption as a socio-technical transformation [5, 19, 20].

---

## Fatores que Influenciam Produtividade

### Fatores Positivos
| Fator | Categoria |
|-------|-----------|
| **AI-assisted code completion and suggestion generation (GitHub Copilot / Windsurf)** | Technical [1, 16] |
| **Acceleration of routine implementation, documentation, and syntax work** | Technical / Process [8, 13, 21] |
| **Faster access to technical information and accelerated developer learning curve** | Human / Technical [13, 18, 22] |
| **Improved task focus, organization, and sustaining flow state during planned work** | Human / Process [18, 22] |
| **Faster code review and merge cycle times in structured feature development (Bitbucket)** | Organizational / Process [11, 23] |
| **Shift toward smaller, incremental commits and reduced code churn per contribution** | Process / Technical [13, 14] |

### Fatores Negativos
| Fator | Categoria |
|-------|-----------|
| **Increased cognitive effort required to validate AI outputs, refine prompts, and steer AI agents** | Human / Technical [8, 18, 21] |
| **Ineffectiveness of AI tools in complex, reactive, and incident-driven operational scenarios** | Technical / Operational [13, 15, 23] |
| **Severe friction and delay during incidents (median incident resolution time increased by 377%)** | Organizational / Process [15, 23] |
| **Reduction in CI/CD pipeline success rates (-7.9 pp on GitLab, -16.9 pp on Bitbucket) and longer execution times** | Process / Technical [11, 23] |
| **Tool ecosystem instability and tool sunsetting (e.g., Windsurf discontinued in July 2025)** | Organizational / Technical [12, 24] |

---

## Papel da IA e Automacao

| Campo | Valor |
|-------|-------|
| **Usa IA/ML?** | Yes — Evaluates GitHub Copilot and Windsurf (LLM-based AI coding assistants) [1, 12, 25]. |
| **Automacao de coleta?** | Yes — Uses automated telemetry extraction via Copilot Metrics Viewer v2.0.2, repository mining, CI/CD telemetry, and Jira logs [6, 16]. |
| **Impacto de IA na produtividade?** | Context-dependent ("Productivity Paradox"): AI accelerated individual fine-grained code completion and structured feature workflows (Bitbucket), but shifted cognitive load toward supervision/validation and significantly increased resolution times (+377%) and review friction in reactive/incident workflows (GitLab) [1, 11, 15, 21, 23, 26]. |

---

## Resultados Principais

- **High AI Tool Adoption**: 96.6% adoption rate among licensed developers (28 of 29 licensed developers used GitHub Copilot at least once; 33 total active developers in Q3-2025) [16].
- **Substantial Activity Volume**: Generated 37,692 code completions and 17,729 chat interactions during Q3-2025, maintaining 17–20 weekly active users [16, 17].
- **Targeted AI Acceptance**: Suggestion acceptance reached 30.2% by count but only 21.9% by lines of code, indicating a preference for fine-grained, targeted code completions rather than broad code generation [14].
- **Divergent Workflow Dynamics (Bitbucket vs. GitLab)**:
  - **Bitbucket (Structured Feature Work)**: Pipeline frequency increased (+185.8%), PR creation grew (+16.0%), median review time decreased (-53.1%), and median merge time decreased (-40.3%) [11, 23].
  - **GitLab (Reactive Maintenance & Incidents)**: Pipeline frequency dropped (-33.7%), pipeline duration grew (+79.0%), median review time increased (+123%), and median merge time increased (+133.3%) [11, 23].
- **Declining Delivery Stability**: Pipeline success rates dropped on both platforms (-7.9 percentage points on GitLab and -16.9 percentage points on Bitbucket) [11, 23].
- **Smaller, Focused Commit Profiles**: Commit frequency increased while code churn per commit decreased, alongside a higher proportion of Feature commits relative to Update commits [13, 14].
- **The Incident Resolution Paradox**: Overall incident ticket volume fell by -35.2%, but median incident resolution time increased by +377%, revealing that remaining operational issues required substantially more time and contextual reasoning [15].
- **Cognitive Load Redistribution**: Mental effort shifted away from writing routine boilerplate code toward reviewing, prompt engineering, validating generated solutions, and "steering the agent" [8, 18, 21].

---

## Desafios do Uso das Metricas

- **Telemetry and Usage Metric Bias**: Usage frequency and acceptance rates fail to reflect delivery quality, system stability, or pipeline performance [1, 20, 27].
- **The Productivity Paradox**: Task-level coding speed does not automatically translate into improved organizational delivery performance [1, 20, 26].
- **Workflow Amplification Anti-Pattern**: AI assistants amplify existing workflow properties—streamlining structured, low-friction tasks while aggravating bottlenecks in reactive or complex scenarios [20, 26].
- **Supervision Overhead**: AI code generation introduces a non-trivial cognitive burden for developers who must continuously validate output accuracy to prevent subtle errors [8, 18, 21].
- **Ecosystem Volatility**: Managing and measuring AI productivity is hampered by rapid technological shifts, such as tool deprecations (e.g., Windsurf phased out within months) [12, 24].

---

## Avaliacao de Qualidade Metodologica

| Criterio | Pontuacao (0-2) |
|----------|----------------|
| **Objetivo claramente definido** | 2 |
| **Metodologia adequada ao objetivo** | 2 |
| **Amostra/contexto descrito adequadamente** | 2 |
| **Ameacas a validade discutidas** | 2 |
| **Resultados com evidencia suficiente** | 2 |
| **Contribuicao clara para pratica ou teoria** | 2 |
| **TOTAL** | **12/12** |

*(Methodological quality score: 12/12, corresponding to 5/5).* [1, 2, 8, 20, 24]

---

## Limitacoes

- **Single Case Study Context**: Findings from one Brazilian fintech organization subject to specific regulatory and operational pressures may not directly generalize across all software sectors [1, 9, 24].
- **Confounding Organizational Variables**: Comparing Q3-2024 against Q3-2025 introduces potential confounding factors, including shifts in team composition, repository maturity, and project priorities [2, 8, 12].
- **Ongoing Study Phase**: Qualitative retrospectives and interview protocols represent an ongoing research effort [1, 4, 10].
- **Ecosystem Instability**: Changing AI availability (such as Windsurf's discontinuation mid-study) complicates multi-tool longitudinal isolation [12, 24].

---

## Contribuicao Principal

The paper presents longitudinal empirical evidence regarding the organizational and workflow impact of AI-assisted coding tools in a real-world fintech setting [1, 10, 12]. Its primary contribution lies in demonstrating the "productivity paradox" and the "amplification hypothesis"—proving that AI coding assistants accelerate structured, planned development tasks, but increase friction, review times, and cognitive load in reactive, incident-driven workflows, thereby showing that usage telemetry alone cannot evaluate the true impact of AI on software delivery [1, 15, 20, 23, 26, 27].

---

*Extraido via NotebookLM em October 2026 para MLR: Software Developer Metrics in Practice*
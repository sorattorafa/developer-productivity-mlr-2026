# P2122 — Productivity, turnover, and team stability of agile teams in open-source software projects

**Decisao: INCLUIDO | Qualidade: 4.5/5**

---

## Dados Bibliograficos

| Campo | Valor |
|-------|-------|
| **ID** | P2122 [1] |
| **Autores** | Ezequiel Scott, Khaled Nimr Charkie, Dietmar Pfahl [1] |
| **Ano** | 2020 [2] |
| **Venue** | 46th Euromicro Conference on Software Engineering and Advanced Applications (SEAA 2020) [2] |
| **DOI** | 10.1109/SEAA51224.2020.00029 [2] |
| **Tipo** | Conference paper [2] |
| **Metodo** | Repository mining & Quantitative empirical study (Statistical Process Control & Non-parametric hypothesis testing) [1, 3-5] |
| **Amostra** | 7 open-source projects (after filtering), 6,887 issue reports, 387 iterations, 198 unique developers [6, 7] |
| **Contexto** | Open-Source Software (OSS) using JIRA issue tracking and agile development practices (Appcelerator Studio, Apache Mesos, MuleSoft, NEXUS, Titanium SDK/CLI, Accelerator Studio, Spring XD) [8-10] |
| **Modo de trabalho** | Not specified [1, 8] |
| **Metodologia** | Agile (Scrum / Iterative development using Epics, User Stories, Story Points, and Iterations) [1, 10, 11] |

---

## Objetivo

The main objective of this paper is to analyze the productivity achieved by agile teams in open-source software (OSS) projects and identify contextual factors that explain unusual variations (out-of-control values) in productivity [1, 12]. By extracting historical data from JIRA server instances across seven open-source projects, the study examines how team velocity (normalized per developer) and focus factor per iteration relate to four key project dynamic factors: iteration length, turnover of leavers, turnover of newcomers, and the team stability index [1, 3, 9, 12].

---

## Questoes de Pesquisa

- **RQ1**: What contextual factors are related to iterations whose velocity is out of control in open source projects? [13]
- **RQ2**: What contextual factors are related to iterations whose focus factor is out of control in open-source projects? [14]

---

## Metricas e Instrumentos de Avaliacao

| Metrica | Categoria | Nivel | Como Coletada | Validada |
|---------|-----------|-------|---------------|----------|
| **Velocity (\\(V_i\\))** | Productivity / Delivery | Team | Sum of story points of all completed issues ("Done", "Resolved", "Closed") whose last status update was made within iteration \\(i\\), extracted from JIRA [15, 16]. | Yes [15] |
| **Individual Velocity** | Productivity / Activity | Individual | Velocity of iteration \\(i\\) normalized by the number of active developers assigned to at least one issue in iteration \\(i\\) (story points per person) [12, 17]. | Yes [12, 17] |
| **Work Capacity (\\(W_i\\))** | Productivity / Activity | Team | Sum of story points of all issues having their last status update within iteration \\(i\\), regardless of completion status, extracted from JIRA [16, 18]. | Yes [16, 18] |
| **Focus Factor (\\(F_i\\))** | Productivity / Delivery | Team | Calculated as the ratio between velocity and work capacity (\\(F_i = V_i / W_i\\)) per iteration [18, 19]. | Yes [18, 19] |
| **Iteration Length** | Process | Team | Duration in days calculated as the elapsed time between the start and end dates of iteration \\(i\\) in JIRA [19, 20]. | Yes [19, 20] |
| **Turnover Rate (Leavers)** | Collaboration / Human | Team | Number of developers active in iteration \\(i-1\\) but inactive in iteration \\(i\\), divided by the average number of active developers across iterations \\(i-1\\) and \\(i\\) [20, 21]. | Yes [20, 21] |
| **Turnover Rate (Newcomers)** | Collaboration / Human | Team | Number of new developers active in iteration \\(i\\) but inactive in iteration \\(i-1\\), divided by the average number of active developers across iterations \\(i-1\\) and \\(i\\) [22]. | Yes [22] |
| **Team Stability Index (\\(TSI^{-1}\\))** | Collaboration / Human | Team | Inverse function of TSI (\\(TSI_i = (|D_0| + |D_i - D_{i-1}| + |D_{i-1} - D_i|) / |D_0|\\)), measuring team composition stability relative to initial developers (\\(D_0\\)) [23, 24]. | Yes [23, 24] |

---

## Frameworks e Metricas

### Frameworks Referenciados
- **Statistical Process Control (SPC) / Individuals and Moving Range (I-MR) Charts**: APPLIED — Used as the primary statistical framework to set upper and lower control limits (UCL, LCL, CL) and classify iterations into control zones (\\(D+\\), \\(D-\\), \\(N\\)) [4, 24-26].
- **Agile / Scrum Framework**: REFERENCED & APPLIED — Serves as the underlying development paradigm, utilizing Sprints/Iterations, Story Points, Epics, User Stories, Velocity, and Focus Factor [1, 10, 11, 16, 27].
- *Note on DORA, SPACE, DevEx, GQM, HEART, OKR*: None of these specific frameworks are mentioned or applied in the paper [1-80].

### Frameworks Propostos
- The paper does not propose a new conceptual framework [1-80]. It presents an empirical analytical approach combining Statistical Process Control (I-MR charts with zone classification) and non-parametric statistical tests (Kruskal-Wallis H test) to evaluate agile team dynamics [5, 17, 24].

---

## Fatores que Influenciam Produtividade

### Fatores Positivos
| Fator | Categoria |
|-------|-----------|
| **High Team Stability (\\(TSI^{-1}\\))** | Human / Organizational [1, 48, 56] |
| **Low Developer Turnover (Leavers & Newcomers)** | Human / Organizational [1, 44, 45, 56] |
| **Longer Iteration Length** (associated with high individual velocity in aggregated analysis) | Process [47] |

### Fatores Negativos
| Fator | Categoria |
|-------|-----------|
| **High Turnover Rate of Leavers** | Human / Organizational [1, 44, 56] |
| **High Turnover Rate of Newcomers** | Human / Organizational [1, 45, 56] |
| **Low Team Stability (\\(TSI^{-1}\\))** | Human / Organizational [1, 48, 56] |

---

## Papel da IA e Automacao

| Campo | Valor |
|-------|-------|
| **Usa IA/ML?** | No — The study relies on Statistical Process Control (SPC), logarithmic data transformations, and non-parametric hypothesis tests rather than AI or machine learning models [5, 24, 42]. |
| **Automacao de coleta?** | Yes — Data extraction from public JIRA server instances (issues, change logs, iteration dates) was performed automatically and processed via Python and Jupyter notebooks [9, 67]. |
| **Impacto de IA na produtividade?** | Not evaluated / Not applicable — AI and automation tools were not analyzed in the study [1-80]. |

---

## Resultados Principais

- **Turnover of Leavers and Velocity**: Iterations with exceptionally low individual velocity (zone \\(D-\\)) exhibited significantly higher turnover of leavers than controlled iterations (zone \\(N\\)) or high-velocity iterations (zone \\(D+\\)) (\\(p = .002\\) vs \\(D-\\), \\(p = .007\\) vs \\(N\\)) [43, 44].
- **Turnover of Newcomers and Velocity**: Iterations with low individual velocity (zone \\(D-\\)) showed a higher turnover rate of newcomers compared to \\(D+\\) iterations (\\(p = .042\\)) [44, 45].
- **Team Stability and Velocity**: Iterations with high individual velocity (zone \\(D+\\)) demonstrated significantly higher team stability (\\(TSI^{-1}\\)) than controlled iterations (\\(p = .017\\)) and low-velocity iterations (\\(p = .013\\)), maintaining values close to 0.8 [47, 48].
- **Iteration Length and Velocity**: Aggregated analysis showed that high-velocity iterations (zone \\(D+\\)) were significantly longer (\\(p = .008\\)) than low-velocity iterations [46, 47].
- **Focus Factor Dynamics**: Focus factor showed fewer statistically significant relationships with context factors; turnover of leavers (\\(p = 0.52\\)), turnover of newcomers (\\(p = 0.19\\)), and team stability (\\(p = 0.50\\)) did not vary significantly across control zones [51, 52, 54, 55].
- **Iteration Length and Focus Factor**: Iterations with low focus factor (zone \\(D-\\)) were significantly longer than high focus factor iterations (\\(p = 0.10\\), Kruskal-Wallis \\(H = 4.57\\)) [53, 60].

---

## Desafios do Uso das Metricas

- **Incomplete Work Masking**: Velocity measures only completed or closed issues ("Done", "Resolved", "Closed") and fails to account for partially completed work [14, 16].
- **Retrospective Work Capacity Assumption**: Calculating work capacity retrospectively may be inaccurate in open-source settings where iterations are less strictly time-boxed or planned than in proprietary corporate projects [61].
- **Violation of Normality in SPC**: Statistical Process Control requires normal distributions; 5 out of 7 projects violated normality for individual velocity, requiring logarithmic transformations before applying control limits [42, 66].
- **Filtering Zero-Activity Iterations**: Removing iterations with null velocity or work capacity avoids noise but risks excluding genuine low-performance periods [38, 64].
- **Resolution of Turnover Metrics**: Turnover formulas based on iteration endpoints do not capture intra-iteration team fluctuations [64].

---

## Avaliacao de Qualidade Metodologica

| Criterio | Pontuacao (0-2) |
|----------|----------------|
| Objetivo claramente definido | 2 [12-14] |
| Metodologia adequada ao objetivo | 2 [5, 17, 24] |
| Amostra/contexto descrito adequadamente | 2 [6, 7, 9] |
| Ameacas a validade discutidas | 2 [62, 63, 65, 66] |
| Resultados com evidencia suficiente | 2 [5, 44, 45, 48] |
| Contribuicao clara para pratica ou teoria | 1 [34, 56, 68] |
| **TOTAL** | **11/12** |

---

## Limitacoes

- **Lack of Causal Inference**: The data-driven empirical design identifies statistical associations but cannot establish causality [62].
- **Construct Validity of Productivity Proxies**: Velocity and focus factor are indirect proxies, and there is no universal consensus on measuring software productivity [63].
- **Inferred Agility**: The study inferred agile practices from JIRA artifacts (user stories, epics, story points) rather than direct observation of team workflows [65].
- **Generalizability**: Findings are based on 7 open-source projects, limiting direct generalizability to all open-source or commercial agile settings [68].
- **Intra-iteration Granularity**: Turnover calculations assume static team composition within iterations and ignore mid-iteration developer join/leave events [64].

---

## Contribuicao Principal

The main contribution of this paper is providing quantitative empirical evidence on how team stability, developer turnover, and iteration length relate to productivity proxies (velocity and focus factor) in agile open-source projects [1, 3, 69, 70]. By applying Statistical Process Control (I-MR charts) to JIRA repository data across seven open-source projects, the study demonstrates that maintaining high team stability and minimizing developer turnover (both leavers and newcomers) are strongly associated with iterations achieving high individual velocity, offering practical guidelines for managing team churn in open-source development [1, 48, 56, 70].

---

*Extraido via NotebookLM em October 2026 para MLR: Software Developer Metrics in Practice*

---

📊 Would you like me to create an infographic or visual chart summarizing the productivity and turnover comparisons across these open-source projects?
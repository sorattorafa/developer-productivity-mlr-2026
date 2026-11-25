# P2103 — No silver bullets: Why understanding software cycle time is messy, not magic

**Decisao: INCLUIDO | Qualidade: 5/5**

---

## Dados Bibliograficos

| Campo | Valor |
|-------|-------|
| **ID** | P2103 [1] |
| **Autores** | John C. Flournoy, Carol S. Lee, Maggie Wu, Catherine M. Hicks [1, 2] |
| **Ano** | 2025 [1] |
| **Venue** | Technical Report / Pre-print (Developer Success Lab at Pluralsight / OSF / GitHub) [3-5] |
| **DOI** | Not specified [1] |
| **Tipo** | Technical report / Working paper [1, 3] |
| **Metodo** | Quantitative / Repository mining / Longitudinal statistical analysis (Bayesian hierarchical linear modeling) [1, 6-8] |
| **Amostra** | 55,619 monthly observations across 12 months (2022) from 11,398 contributors in 216 organizations [1, 6, 9] |
| **Contexto** | Industry — 216 commercial organizations across Technology, Finance, Government, Insurance, Retail, and other sectors [9, 10] |
| **Modo de trabalho** | Not specified [9, 10] |
| **Metodologia** | Not specified [9, 10] |

---

## Objetivo

The main objective of the paper is to empirically analyze software cycle time—defined as the duration between ticket opening and ticket closing—and evaluate how software development process factors (coding time, task scoping, and collaboration) influence delivery speed across engineering organizations [1, 6, 11]. Using a dataset of over 55,000 monthly aggregated observations from 216 organizations, the study applies Bayesian hierarchical linear modeling with Weibull distributions to disaggregate within-person and between-person effects as well as individual- and organizational-level variations, demonstrating the inherent noise and limitations of using cycle time for evaluating individual developer performance [1, 6, 8, 12].

---

## Questoes de Pesquisa

- **RQ1**: How do common workplace and software development process factors impact cycle time? [13]
- **RQ2**: How much between- and within-person variation is there in cycle time? [13]

---

## Metricas e Instrumentos de Avaliacao

| Metrica | Categoria | Nivel | Como Coletada | Validada |
|---------|-----------|-------|---------------|----------|
| **Cycle Time** | Delivery / Speed | Individual / Team | Aggregated median duration (in seconds) from ticket start to ticket end for all tickets opened in a month [14, 15] | Partial [16-19] |
| **Proportion of Unclosed Tickets** | Control / Activity | Individual | Logistic quantile transformed proportion of tickets opened in a month that remained unclosed at data cutoff [15, 20] | Yes [8, 20] |
| **Coding Days per Week** | Activity / Coding Time | Individual | Average number of days per week in a month where a developer made at least one Git commit [15, 21] | Partial [21] |
| **Total Merged PRs** | Activity / Task Scoping | Individual | Monthly count of merged pull requests per developer in Git repositories [15, 22] | Partial [22] |
| **Percent Defect Tickets** | Quality / Task Scoping | Individual | Monthly percentage of opened tickets categorized as defects/bugs [15, 23] | Partial [23, 24] |
| **Degree Centrality** | Collaboration | Individual | Normalized network centrality (multiplied by 100) based on shared PR contributions and reviews [7, 25] | Partial [25, 26] |
| **Comments per PR** | Collaboration | Individual | Monthly average number of comments per merged PR authored by the developer [7, 27] | Partial [27, 28] |
| **Team Size** | Context / Organizational | Individual / Team | Average size across all co-located activity teams an individual belongs to [15, 29] | Partial [29, 30] |

---

## Frameworks e Metricas

### Frameworks Referenciados
- **DORA (DevOps Research and Assessment)**: REFERENCED — Cited and discussed regarding the four key software delivery metrics (lead time, deployment frequency, change failure rate, and mean time to recovery) and how cycle time aligns conceptually with lead time [17].
- **SPACE**: REFERENCED — Discussed in the context of developer productivity frameworks and multi-dimensional measurement [31-33].
- **DevEx (Developer Experience)**: REFERENCED — Discussed regarding developer experience, friction reduction, release fluidness, and sociocognitive thriving [34-36].

### Frameworks Propostos
The paper does not propose a new named practitioner metrics framework (such as DORA or SPACE) [6, 37]. Instead, it proposes a **Bayesian Hierarchical Modeling Framework** (utilizing Weibull outcome distributions and disaggregating within-person deviations from year-level averages) to analyze complex, heavy-tailed software operational metrics at scale while accounting for nested individual and organizational variance [1, 6, 8, 12].

---

## Fatores que Influenciam Produtividade

### Fatores Positivos
| Fator | Categoria |
|-------|-----------|
| Increased Coding Days per Week (within-person deviation: \\(\beta = -0.0794\\); year average: \\(\beta = -0.0839\\)) [38] | Technical / Process |
| Higher Total Merged PRs / Smaller PR Scoping (within-person deviation: \\(\beta = -0.0127\\); year average: \\(\beta = -0.0083\\)) [38, 39] | Process / Technical |
| Higher Degree Centrality / Shared PR Collaboration (within-person deviation: \\(\beta = -0.0023\\); year average: \\(\beta = -0.0040\\)) [39] | Human / Collaboration |
| Month-to-month increase in Percent Defect Tickets (within-person deviation: \\(\beta = -0.0019\\), reflecting quick bug-fixing shifts) [39, 40] | Process / Technical |
| End-of-Quarter Cadence (within-quarter month slope: \\(\beta = -0.0085\\)) [38, 41] | Organizational / Process |

### Fatores Negativos
| Fator | Categoria |
|-------|-----------|
| Higher Yearly Average Percent Defect Tickets (year average: \\(\beta = 0.0060\\), reflecting defect-heavy workloads or role constraints) [24, 39] | Quality / Process |
| Higher Comments per PR (within-person deviation: \\(\beta = 0.0046\\); year average: \\(\beta = 0.0098\\), reflecting coordination overhead or complex fixes) [28, 39] | Technical / Collaboration |
| High Unexplained Variation / Noise across and within individuals (\\(SD_{\text{org:user}} = 0.645\\)) [42, 43] | Organizational / Process |
| Sociocognitive Friction, Workplace Surveillance, and Individual Ability Myths ("10x engineer") [44-46] | Organizational / Human |

---

## Papel da IA e Automacao

| Campo | Valor |
|-------|-------|
| **Usa IA/ML?** | No — The study's analytical methodology relies on Bayesian hierarchical linear modeling (Stan/brms) rather than machine learning or AI models [7, 8]. |
| **Automacao de coleta?** | Yes — Data collection was fully automated via background integration of Git repositories and ticketing software (Flow at Appfire / Pluralsight Flow) without direct human reporting [3, 9]. |
| **Impacto de IA na produtividade?** | Not evaluated — The study discusses AI skill threat and transitions in related literature [36], but does not measure AI tool usage or AI impact in its dataset [9, 15]. |

---

## Resultados Principais

- **Modest Effect Sizes**: All measured process factors demonstrate statistically precise directional associations with cycle time (100% sign probability), but individual effect sizes are modest relative to overall background noise [1, 26, 38, 41].
- **Coding Days**: Coding days per week has a strong positive association with delivery speed (reducing cycle time). The posterior median for within-person deviation is \\(-0.0794\\) (100% sign probability) and for year-average is \\(-0.0839\\) (100% sign probability) [38]. An increase of 1 coding day per week reduces organizational cycle time by approximately 2 days [47, 48].
- **Task Scoping via PRs**: A higher number of merged PRs is associated with shorter cycle time (within-person slope = \\(-0.0127\\), 100% sign probability; year-average slope = \\(-0.0083\\), 100% sign probability), supporting the practice of breaking work into smaller pull requests [22, 38, 39].
- **Defect Ticket Divergence**: Percent defect tickets shows opposing levels of effect: developers with a higher yearly defect percentage experience longer cycle times (\\(\beta = +0.0060\\), 100% sign probability), whereas a monthly spike in defect percentage for a given developer correlates with shorter cycle time (\\(\beta = -0.0019\\), 100% sign probability) due to shifts toward quick bug fixes [24, 39, 40, 49].
- **Collaboration Dynamics**: Higher degree centrality (shared PR contributions) decreases cycle time (within-person slope = \\(-0.0023\\); year-average slope = \\(-0.0040\\)), indicating collaboration speeds up delivery [28, 39, 50]. Conversely, more comments per PR increases cycle time (within-person slope = \\(+0.0046\\); year-average slope = \\(+0.0098\\)), capturing discussion of complex problems or coordination friction [28, 39, 51].
- **Substantial Heterogeneity and Noise**: Individual-level scale variance (\\(SD = 0.645\\) [0.631, 0.661]) exceeds organizational-level scale variance (\\(SD = 0.474\\) [0.424, 0.529]) [42, 43]. Within-person month-to-month variation is huge, making single monthly measurements an extremely noisy indicator of individual performance [1, 52-54].
- **Quarterly Acceleration**: Cycle time decreases slightly toward the end of business quarters (within-quarter month slope = \\(-0.0085\\), 95% sign probability) [38, 41].

---

## Desafios do Uso das Metricas

- **High Noise and Unreliable Snapshots**: Any single observation or monthly average of cycle time provides a very noisy signal of typical performance due to massive unexplained within-person and between-person variability [1, 52, 54].
- **Anti-Pattern of Individual Evaluation**: Using cycle time to evaluate, rank, or reward individual developers is an explicit anti-pattern because cycle time is heavily driven by systems-level organizational factors outside individual contributor control [1, 54, 55].
- **Distance from Value and Quality**: Cycle time measures delivery velocity rather than output quality, business outcomes, technical debt reduction, or user value [16, 56-58].
- **Surveillance and Dehumanization**: Tracking activity metrics without procedural justice or developer context can trigger worker discontent, anxiety, perception of workplace surveillance, and organizational dehumanization [44, 59, 60].
- **Distributional Misrepresentation**: Modeling cycle time with standard Gaussian (normal) distributions distorts results; cycle time is highly skewed and heavy-tailed, requiring survival distributions like Weibull [8, 61].
- **Invisible Collaboration**: Quantitative activity metrics miss unrecorded collaborative work such as informal mentorship, pair/mob programming, architecture planning, and unlogged discussions [62].

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

- **Construct Validity**: Relies on the assumption that engineering teams log and close tickets accurately and promptly; the dataset lacked qualitative validation of ticketing practices across organizations [18].
- **External Validity**: The sample is non-random, consisting of commercial organizations that opted into a specific software metrics tool (Pluralsight Flow/Appfire Flow), limiting generalizability [9, 10, 63].
- **Internal Validity**:
  - Team size is operationalized as a static, yearly average based on co-located activity, failing to capture dynamic team shifts or cross-team collaboration [29, 30].
  - Invisible collaborative activities (mentorship, pair programming, planning) and contributor role ambiguity (e.g., job titles) are unmeasured in Git/ticket data [62].
  - Ticket assignment patterns (e.g., systematic assignment of complex bugs to specific developers) were unobserved [63, 64].
- **Statistical Conclusion Validity**: Parameter estimates remain conditional on specific model assumptions (additivity, Weibull distribution, smooth thin-plate splines), and unmodeled confounders or feedback loops in ticket lifecycles could introduce bias [65].

---

## Contribuicao Principal

The paper's primary contribution is twofold: first, it establishes a Bayesian hierarchical modeling methodology (using Weibull distributions to separate individual, organizational, and within-person variations) for evaluating software operational data across a massive longitudinal dataset (over 55,000 observations across 216 organizations), empirically demonstrating that cycle time is dominated by high context-specific variability and unexplained noise [1, 6, 8, 42]; second, it provides evidence-based guidance for software practitioners, cautioning against using velocity metrics for individual developer evaluation and demonstrating that improving software delivery velocity requires systems-level organizational changes rather than individual-focused interventions [1, 54, 55].

---

*Extraido via NotebookLM em October 2026 para MLR: Software Developer Metrics in Practice*
# P2101 — What's DAT? Three Case Studies of Measuring Software Development Productivity at Meta With Diff Authoring Time

**Decisao: INCLUIDO | Qualidade: 5/5**

---

## Dados Bibliograficos

| Campo | Valor |
|-------|-------|
| **ID** | P2101 |
| **Autores** | Moritz Beller, Amanda Park, Karim Nakad, Akshay Patel, Sarita Mohanty, Ford Garberson, Henri Verroken, Andrew Kennedy, Ian G. Malone, Vaishali Garg, Pavel Avgustinov [1-3] |
| **Ano** | 2026 [3, 4] |
| **Venue** | IEEE/ACM 48th International Conference on Software Engineering (ICSE-SEIP '26) [3, 4] |
| **DOI** | 10.1145/3786583.3786901 [3, 4] |
| **Tipo** | Conference paper (ICSE Software Engineering in Practice) [3, 4] |
| **Metodo** | Mixed methods (Controlled experiment, Case studies, Survey, Observational UX screen recording study, Descriptive statistics) [2, 5-10] |
| **Amostra** | n = ~20 diffs (UX study), 968 diffs (Survey), ~10,000 diffs (Typed mocking experiment), n >> 10,000 diffs (React case study), n = ~50,000 diffs monthly (Code sharing case study) [11-15] |
| **Contexto** | Industry (Meta Platforms, Inc., DevInfra organization) [1, 16] |
| **Modo de trabalho** | Not specified [1, 16] |
| **Metodologia** | Continuous Experimentation (CE) / DevOps / Internal product development [4, 17-19] |

---

## Objetivo

The paper proposes Diff Authoring Time (DAT), a time-based developer velocity metric that measures the active work time engineers spend developing self-contained code changes (diffs) at Meta [2, 5]. The primary objective is to replace inaccurate and gameable traditional productivity metrics with an objective, telemetry-driven measurement framework that enables continuous, statistically rigorous experimentation on internal tools, programming languages, and frameworks at industry scale [2, 5, 16]. By establishing DAT, the authors aim to shift internal developer infrastructure development toward a scientifically grounded, data-driven methodology similar to external product continuous experimentation [16, 17, 20].

---

## Questoes de Pesquisa

- **RQ1**: Does the introduction of language-level static types (specifically typed mocking in the Hack language) significantly reduce developer authoring time (DAT) in a large-scale industrial setting [2, 8, 13, 21]?
- **RQ2**: What is the impact of automatic memoization via the React compiler (React Forget) on software development velocity (DAT) compared to manual component memoization [2, 9, 21, 22]?
- **RQ3**: How can efficiency gains from cross-platform code sharing frameworks be quantified in terms of authoring time saved (\\(DAT_{saved}\\)) relative to platform-specific counterfactual development [10, 15, 21, 23]?

---

## Metricas e Instrumentos de Avaliacao

| Metrica | Categoria | Nivel | Como Coletada | Validada |
|---------|-----------|-------|---------------|----------|
| **Diff Authoring Time (DAT)** | Productivity / Delivery | Individual / Team | OS foreground telemetry, IDE session tracking (VS Code, Android Studio), version control events (Sapling), and review tool events (Phabricator) [2, 5, 24, 25]. | Yes [2, 5, 11, 12, 26] |
| **Anchor-DAT** | Productivity / Delivery | Individual / Team | Heuristic mapping preceding active work in vetted auxiliary tools (e.g., terminal, SQL interfaces) to the subsequent precise match diff session [27-29]. | Yes [29-31] |
| **Time Spent by Diff (TSD)** | Productivity | Individual / Team | Averaged active coding time in a period divided by the number of published diffs [32]. | Partial [30, 32, 33] |
| **Code Gestation Time (CGT)** | Productivity / Delivery | Individual / Team | Composite metric measuring duration from initial code start to final diff landing [32]. | No [32] |
| **Lines of Code (LOC)** | Activity | Individual / Team | Version control diff file statistics [9, 34, 35]. | No [34, 35] |
| **Change Count** | Activity | Individual / Team | Repository commit or published diff counts [34, 35]. | No [34, 35] |
| **Function Points** | Productivity | Organization | Manual complexity judgment and third-party estimation guidelines [34]. | Partial [34] |

---

## Frameworks e Metricas

### Frameworks Referenciados
- **SPACE**: REFERENCED — Cited as an umbrella framework for developer productivity that defers specific metric choices to users [35].
- **DevEx / DX Core 4**: REFERENCED — Cited regarding developer experience and core productivity dimensions [14, 22, 34, 35].
- **CE Maturity Model (Melegati et al.)**: REFERENCED & APPLIED — Cited to contextualize Meta Infrastructure's progression through 5 stages of Continuous Experimentation adoption [18, 19].

### Frameworks Propostos
- **Diff Authoring Time (DAT) Metric Framework**: A telemetry and algorithm framework combining 1-left-shift commit-to-session matching, active OS foreground focus, and anchor heuristics integrated with Meta's internal experimentation platform (Deltoid) [5, 24, 27, 36, 37].
- **Counterfactual Model for Code Sharing Efficiency**: An estimation framework calculating saved DAT (\\(DAT_{saved}\\)) by comparing actual code-shared diff DAT against counterfactual baselines derived from app/platform-specific unshared diffs normalized by diff size terciles [10, 38, 39].

---

## Fatores que Influenciam Produtividade

### Fatores Positivos
| Fator | Categoria |
|-------|-----------|
| Typed Mocking (Static type checking in testing frameworks) [2, 40, 41] | Technical |
| Automatic Memoization (React Forget compiler auto-memoization) [2, 22, 23] | Technical |
| Cross-Platform Code Sharing (Shared libraries across mobile/web platforms) [15, 21, 23] | Technical / Organizational |
| Early feedback loops / IDE static analysis type error detection [40, 42] | Technical / Process |
| Continuous Experimentation (CE) culture for internal tooling [17, 19, 43] | Organizational / Process |

### Fatores Negativos
| Fator | Categoria |
|-------|-----------|
| Untyped Mocking APIs causing runtime `TypehintViolation` exceptions in CI [40, 44, 45] | Technical |
| Manual Memoization boilerplate code, manual state tracking, and resulting bugs [22, 46] | Technical |
| Sub-second task switching and multi-tasking across tools [11, 47] | Human / Process |
| Delayed CI test execution feedback loops [40, 45] | Technical / Process |
| Redundant development of identical changes across separate platforms [23, 39] | Organizational / Process |

---

## Papel da IA e Automacao

| Campo | Valor |
|-------|-------|
| Usa IA/ML? | Yes — Discusses LLM base models (e.g., LLaMA-33B vs LLaMA-65B), AI-assisted code authoring, and AI coding agents [48-51]. |
| Automacao de coleta? | Yes — Fully automated OS, IDE, and version control telemetry tracking active foreground developer focus without manual logging [2, 5, 25]. |
| Impacto de IA na produtividade? | Notes that AI coding agents may initially increase DAT due to execution speed constraints, but DAT provides the objective metric to track long-term agent optimization and guide loss functions [50, 51]. |

---

## Resultados Principais

- **Validation & Accuracy**: DAT achieved over 90% accuracy (within ±5% of ground truth) in screen-recording UX studies across ~20 diffs, outperforming human annotators during rapid context switches [11].
- **Diff Coverage**: DAT covers >95% of all eligible diffs at Meta and demonstrates long-term stability using 99th percentile winsorized averages [26, 30].
- **Typed Mocking Experiment**: Introducing a typed mocking API in Hack yielded a statistically significant 14% overall DAT reduction (\\(p < 0.001, n \approx 10,000\\)), with 19%–24% DAT savings for diffs modifying up to 4 files, prompting a 100% rollout across Meta [21, 41, 42].
- **React Auto-Memoization**: A mixed-effects regression model showed a 33% DAT reduction for diffs using compiler auto-memoization compared to manual memoization (\\(n \gg 10,000\\)) [9, 21, 23].
- **Code Sharing Frameworks**: A counterfactual model covering ~50,000 monthly diffs showed a >50% relative DAT efficiency gain over non-shared development, saving thousands of engineering hours annually [15, 21].

---

## Desafios do Uso das Metricas

- Off-screen human activities (whiteboarding, paper sketching, offline meetings) cannot be captured by telemetry [36, 52].
- Trade-off between precision and recall (heuristics like Anchor-DAT increase tool coverage but risk including non-diff activity) [27, 53].
- Noise introduced when developers use unsupported editors and copy-paste code into the environment [54].
- Statistical noise when detecting small effect sizes with limited developer samples, requiring long experiment durations [55].
- Risk of "metric-blindness" if organizations reject promising innovations (such as early-stage AI coding agents) solely due to initial metric lag [50].
- Governance and privacy risks if productivity metrics are misused for individual evaluation rather than tooling experimentation [33].

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

- Automated telemetry cannot capture offline cognitive effort (whiteboarding, paper sketching, team meetings, PTO/sick leave) [36, 52].
- Non-randomized observational case study designs (e.g., React compiler) required post-hoc regression and Wasserstein distance adjustments rather than pure A/B testing [9].
- Counterfactual code-sharing model relies on estimated baselines from unshared diffs rather than directly observable parallel developments [10, 38].
- Findings reflect a single large-scale company (Meta Infrastructure) with highly integrated internal toolchains (Sapling, VS Code, Phabricator, Deltoid), which may require adaptation in heterogeneous corporate environments [16, 25, 37, 56].
- Fine-grained UI micro-optimizations may not produce statistically detectable DAT changes due to baseline cognitive variance [54, 57].

---

## Contribuicao Principal

The primary contribution of this paper is the conceptualization, implementation, and large-scale validation of Diff Authoring Time (DAT), an objective, time-based developer velocity metric grounded in automated IDE, version control, and OS telemetry [2, 5, 20]. By applying DAT across Meta's infrastructure organization, the authors demonstrate how diff-grain velocity tracking enables continuous, statistically rigorous software engineering experimentation—providing empirical proof that static typing reduces authoring time by 14%, compiler auto-memoization cuts development time by 33%, and code sharing yields over 50% efficiency gains [2, 20, 21, 58].

---

*Extraido via NotebookLM em October 2026 para MLR: Software Developer Metrics in Practice*
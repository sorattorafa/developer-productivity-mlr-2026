# P2099 — Measuring productivity: All models are wrong, but some are useful

**Decisao: INCLUIDO | Qualidade: 4.5/5**

---

## Dados Bibliograficos

| Campo | Valor |
|-------|-------|
| **ID** | P2099 [1] |
| **Autores** | Ciera Jaspan, Collin Green [1-3] |
| **Ano** | 2025 [1] |
| **Venue** | IEEE Software [1, 4, 5] |
| **DOI** | 10.1109/MS.2024.3511735 [1] |
| **Tipo** | Journal article / Invited column [1, 6] |
| **Metodo** | Experience report / Mixed methods (Logs-based metrics, Diary studies, Longitudinal surveys) [7-9] |
| **Amostra** | Software engineers at Google (logs-based measurement covering approximately every engineer, plus quarterly survey respondents) [7-9] |
| **Contexto** | Industry — Google (large tech enterprise) [7, 10, 11] |
| **Modo de trabalho** | Not specified (mentions remote work during COVID-19 pandemic as an event analyzed via logs) [8, 12] |
| **Metodologia** | Not specified [7] |

---

## Objetivo

The main objective of the paper is to frame software developer productivity measurement as an exercise in model building, grounded in George Box's principle that "all models are wrong, but some are useful" [1, 6, 10]. The authors describe Google's approach to designing holistic, multi-method productivity models that balance trade-offs among Speed, Ease, and Quality while avoiding "worrying selectivity" (such as single-metric traps) and unintended behavioral incentives [10, 13-15]. Additionally, the paper provides pragmatic guidelines for engineering organizations of different sizes on how to measure productivity effectively according to their scale and resources [11, 16, 17].

---

## Questoes de Pesquisa

Not explicitly stated (the paper is an industry experience report/invited column based on a summit keynote address rather than an empirical study structured around formal research questions) [1, 6].

---

## Metricas e Instrumentos de Avaliacao

| Metrica | Categoria | Nivel | Como Coletada | Validada |
|---------|-----------|-------|---------------|----------|
| Build latency | DevEx / Delivery | Individual / Team | Logs-based metric (tool instrumentation) | Yes (validated via developer diary studies) [7, 18] |
| Active coding time | Activity / DevEx | Individual | Logs-based metric (tool instrumentation) | Yes (validated via developer diary studies) [7, 18] |
| Test flakiness | Quality | Team / Organization | Logs-based metric (tool instrumentation) | Yes [7, 16, 18] |
| Lines of code (LOC) | Productivity / Activity | Individual | Version control logs | No (cited as an example of a worryingly selective metric that incentivizes verbose code) [14, 19] |
| Changes submitted / Code delivered | Delivery / Activity | Individual / Team | Repository / Deployment logs | Partial [19, 20] |
| Self-reported engineering velocity | Productivity / DevEx | Individual / Team | Longitudinal quarterly survey | Yes (used for triangulation with logs-based metrics) [9, 20] |
| Overall role satisfaction | Satisfaction / DevEx | Individual | Longitudinal quarterly survey | Yes [9, 12] |
| Flow, focus, and friction | DevEx / Productivity | Individual | Subjective survey items | Partial [2, 12, 21] |
| Technical debt | Quality / DevEx | Team / Organization | Subjective survey items (objective metrics in development) | Partial [2, 12] |

---

## Frameworks e Metricas

### Frameworks Referenciados
- **SPACE**: REFERENCED (cited as a framework that provides a holistic view across multiple productivity dimensions, similar to Google's Speed, Ease, Quality approach) [5, 15, 21].
- **Goodhart's Law / Box's Model Principles**: REFERENCED (discussed regarding measurement targets, unintended behavioral incentives, and trade-offs between parsimony and selectivity) [6, 14, 22].
- Other frameworks such as DORA, GQM, HEART, and OKR are not explicitly mentioned in the text.

### Frameworks Propostos
- **Speed, Ease, and Quality Triangulation Framework**: A holistic productivity model proposed by Google that balances three core outcomes (Speed, Ease, Quality) by combining objective quantitative tool logs with subjective qualitative data (quarterly surveys and diary studies) to capture context and prevent blind spots [7-9, 12, 15].

---

## Fatores que Influenciam Produtividade

### Fatores Positivos
| Fator | Categoria |
|-------|-----------|
| Standardized, always-on internal tool instrumentation across the organization | Technical / Organizational [7, 8] |
| Triangulating objective logs with subjective developer surveys and diary studies | Organizational / Process [7, 9] |
| Improving developer experience aspects like code review velocity, flow, and low build latency | Technical / Process [12, 23] |
| Open discussion of productivity friction and obstacles in small teams | Organizational / Human [11] |

### Fatores Negativos
| Fator | Categoria |
|-------|-----------|
| Relying on single-metric productivity models (worrying selectivity) | Process / Organizational [13, 23] |
| Perverse incentives created by metric targets (Goodhart's Law, e.g., lines of code encouraging verbose code) | Organizational / Human [14] |
| Arbitrarily removing critical quality processes (e.g., removing code reviews to artificially boost speed) | Process / Technical [23] |
| Human and operational bottlenecks (fatigue, injuries, tool breakage, or burnout) | Human / Technical [24] |
| Technical friction such as flaky tests, frequent rollbacks, and poor internal documentation | Technical / Process [16] |

---

## Papel da IA e Automacao

| Campo | Valor |
|-------|-------|
| Usa IA/ML? | Yes — The authors state that they are actively adjusting Google's longitudinal engineering survey to measure how AI is changing developer experience and productivity [12]. |
| Automacao de coleta? | Yes — Automated, unobtrusive, always-on log collection across standardized in-house developer tools for approximately every engineer at Google [7, 8]. |
| Impacto de IA na produtividade? | The paper notes that AI is transforming developer experience and productivity, prompting Google to pivot survey benchmarks to capture its impact, though specific quantitative productivity numbers for AI are not reported in this paper [12]. |

---

## Resultados Principais

- **Productivity as Model Building**: Measuring developer productivity is an exercise in model building where all models are inherently wrong; the key is ensuring models are not wrong in problematic ways by avoiding "worrying selectivity" [1, 6, 10, 13].
- **Three Core Outcomes**: Developer productivity requires balancing three core outcomes: **Speed, Ease, and Quality** [15].
- **Flaws of Single Metrics**: Single-metric models omit critical trade-offs and trigger Goodhart's Law, creating unintended negative behaviors (e.g., using lines of code as a sole speed metric incentivizes verbose code) [14, 19, 23].
- **Triangulation via Logs and Surveys**: Combining automated tool logs (always-on, unobtrusive, high statistical power) with quarterly subjective surveys and diary studies validates metrics, reveals discrepancies, and measures non-loggable concepts like role satisfaction or flow [7-9, 12].
- **Recommendations by Organization Size**:
  - *Small teams (fits in a conference room)*: Do not measure metrics; use direct discussions to identify and resolve productivity friction [11].
  - *Medium organizations*: Use developer surveys as a low-cost starting point to target specific friction areas (e.g., flaky tests, documentation) [16].
  - *Large enterprises*: Invest in dedicated research teams, multi-method triangulation, log instrumentation, and longitudinal surveys [11, 17].

---

## Desafios do Uso das Metricas

- **Worrying Selectivity**: Omitting essential software engineering facets (such as code quality, system design, or production management) when creating productivity models [13, 19, 22].
- **Goodhart's Law and Unintended Incentives**: When metrics become explicit targets, developers adapt to meet the target, leading to poor trade-offs or unwanted behaviors [14].
- **Inability of Logs to Capture Full Context**: Objective logs cannot measure subjective sentiment, job satisfaction, mental flow, or technical debt without survey triangulation [9, 12].
- **Excessive Overhead for Small Teams**: Building complex metric instrumentation in small teams creates overhead that outweighs its practical utility [11].
- **Misapplying Narrow Metrics Globally**: Using narrow metrics designed for specific problem-solving as global measures of overall developer productivity [16, 17].

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

*Note on evaluation: The paper clearly defines its objective [1, 10], applies a solid industrial experience methodology combining logs, diary studies, and longitudinal surveys at Google [7-9], describes its context thoroughly [7, 10], presents concrete evidence and rationale [7-9, 12, 14, 23], and offers strong practical contributions [11, 16, 17]. Threats to validity and model limitations are discussed conceptually (selectivity, biases, recall issues) [12-14], though not in a formal academic subsection given the invited column format [1, 6].*

---

## Limitacoes

- **Context Specificity**: Findings and infrastructure reflect Google's environment, which features highly standardized in-house tools and dedicated research teams that smaller organizations may lack [7, 11].
- **Format Constraints**: As an invited expert column based on a summit keynote, the paper does not present raw empirical tables or statistical hypothesis testing [1, 6].
- **Log Limitations**: Logs-based quantitative metrics cannot measure subjective feelings, job satisfaction, flow, or technical debt directly without survey triangulation [9, 12].
- **Survey Biases**: Subjective survey responses are subject to noise, recall bias, and complex cognitive interpretations by respondents [12].

---

## Contribuicao Principal

The paper's primary contribution is a conceptual and practical framework for software developer productivity measurement based on statistical model building principles [1, 6, 10]. Grounded in George Box's concept that "all models are wrong, but some are useful," the authors demonstrate why single-metric models fail due to Goodhart's Law and "worrying selectivity" [6, 13, 14]. They introduce Google's holistic triangulation approach, which balances Speed, Ease, and Quality by combining automated tool logs with subjective developer surveys and diary studies [7-9, 15]. Furthermore, the paper provides pragmatic guidance tailored to organizational scale, advising small teams to avoid metric overhead in favor of direct communication, medium teams to leverage developer surveys, and large organizations to invest in multi-method measurement [11, 16, 17].

---

*Extraido via NotebookLM em October 2026 para MLR: Software Developer Metrics in Practice*

---

💡 **Sugestão para o próximo passo:** Se desejar, posso ajudar a comparar as diretrizes e a abordagem de triangulação deste artigo com outros modelos populares do seu repositório (como SPACE ou DORA) ou detalhar alguma seção específica!
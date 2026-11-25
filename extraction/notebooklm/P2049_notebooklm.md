# P2049 — Creating benchmarkable components to measure the quality of AI-enhanced developer tools

**Decisao: INCLUIDO | Qualidade: 4.5/5**

---

## Dados Bibliograficos

| Campo | Valor |
|-------|-------|
| **ID** | P2049 |
| **Autores** | Elise Paradis, Ambar Murillo, Maulishree Pandey, Sarah D’Angelo, Andrew Macvean, Ben Ferrari-Church, Matthew Hughes [1, 2] |
| **Ano** | 2025 [3] |
| **Venue** | Extended Abstracts of the CHI Conference on Human Factors in Computing Systems (CHI EA ’25) [3, 4] |
| **DOI** | 10.1145/3706599.3706674 [3] |
| **Tipo** | Conference paper (Extended Abstract / Case Study) [3, 5] |
| **Metodo** | Mixed methods (Case study, Literature review, Cognitive testing, Pilot study, Randomized Controlled Trial, Surveys) [5-9] |
| **Amostra** | 17 Google software engineers in cognitive testing (9 in round 1, 8 in round 2); 8 C++ developers in pilot testing; >100 participants required for RCT statistical power [7, 10-12] |
| **Contexto** | Industry (Google, backend software development, C++ environment, internal IDE tools) [5, 7, 13, 14] |
| **Modo de trabalho** | Not specified (Asynchronous, self-administered study tasks) [15] |
| **Metodologia** | Not specified |

---

## Objetivo

The main objective of this paper is to describe a process for creating robust, enterprise-grade, and modular components to benchmark the developer experience (DX) dimensions and productivity impact of generative AI features for code in an enterprise environment (specifically Google's AI for code tools) [5, 16, 17].

---

## Questoes de Pesquisa

- **RQ1**: How might we support the creation of robust, enterprise-grade, and modular evaluation components to better understand the impact of AI on developer workflows, while systematically comparing the quality of features across products and over time? [16]
  - *(In other words)*: How might we create benchmarkable components that accelerate other researchers at Google and beyond in assessing the quality and impact of their AI features for code? [16]

---

## Metricas e Instrumentos de Avaliacao

| Metrica | Categoria | Nivel | Como Coletada | Validada |
|---------|-----------|-------|---------------|----------|
| **Satisfaction** | Satisfaction | Individual | Post-task / Feature survey (Likert scale) [18, 19] | Yes [7, 11] |
| **Trust in accuracy** | DevEx / Satisfaction | Individual | Post-task / Feature survey (Likert scale) [18-20] | Yes [7, 10] |
| **Goal importance** | Activity / Context | Individual | Post-task survey [18, 21] | Yes [7] |
| **Helpfulness** | DevEx / Productivity | Individual | Feature survey [18, 22] | Yes [7] |
| **Feature completeness** | DevEx / Quality | Individual | Feature survey [18, 23] | Yes [7] |
| **Perceived code quality** | Quality | Individual | Post-task / Feature survey [18, 24-26] | Yes [7, 10] |
| **Long-term impact on the code base** | Quality | Individual / Team | Feature survey [24] | Yes [7] |
| **Ease of use** | DevEx | Individual | Feature survey [24, 26] | Yes [7] |
| **Perceived productivity** | Productivity | Individual | Post-task / Feature survey [24, 27-29] | Yes [7, 10] |
| **Developer velocity / Time on task** | Productivity / Delivery | Individual | Automated tracking via precise logging infrastructure [15, 30, 31] | Yes [8, 11] |

---

## Frameworks e Metricas

### Frameworks Referenciados
- **SPACE framework**: REFERENCED (cited as the basis for Google's internal DX metrics framework, modified with additional system efficiency concepts) [32]
- **Google internal DX metrics framework**: APPLIED (used to select benchmarkable sentiment and productivity metrics) [32]
- **General Attitudes Towards AI / Technology scales**: REFERENCED (reviewed during literature review to inform survey design) [6, 33, 34]

### Frameworks Propostos
The paper proposes a 3-activity modular benchmarking program framework for evaluating generative AI developer tools:
1. **Activity 1**: Pre-task questionnaires covering demographics, AI usage, and attitudes towards AI, plus a feature onboarding review [9, 35].
2. **Activity 2**: Completion of a standardized, enterprise-grade coding task (with or without AI) [9, 36].
3. **Activity 3**: Post-task survey and feature-specific evaluation surveys [9, 37].

---

## Fatores que Influenciam Produtividade

### Fatores Positivos
| Fator | Categoria |
|-------|-----------|
| Programming experience / Seniority [13, 38] | Human |
| Hours spent programming per day [13, 38] | Process / Human |
| Language and tool familiarity (C++) [8, 13] | Technical / Human |
| Availability of AI-enhanced code completion/suggestions [38, 39] | Technical |
| Positive attitude and trust in AI outputs [13, 18] | Human |

### Fatores Negativos
| Fator | Categoria |
|-------|-----------|
| Inexperience / Accepting low-quality AI generated code [38] | Human |
| Difficulties in code understanding, editing, and debugging AI output [40] | Technical |
| Integration friction outside primary IDEs [40] | Technical / Process |
| Lack of developer control over AI features [22, 25] | Technical |
| Task unfamiliarity [21] | Human / Process |

---

## Papel da IA e Automacao

| Campo | Valor |
|-------|-------|
| **Usa IA/ML?** | Yes — evaluates IDE-based generative AI coding features (code completion, generation, and assistance) [30, 38, 39]. |
| **Automacao de coleta?** | Yes — precise automated logging infrastructure tracks time on task, and questionnaires are self-administered asynchronously [15, 31]. |
| **Impacto de IA na produtividade?** | Developers using Google's AI coding tools completed the enterprise task 21% faster compared to the control group, with higher benefits observed for senior engineers and frequent coders [38]. |

---

## Resultados Principais

- Developers with access to Google's IDE-based AI features completed a complex, enterprise-grade C++ task **21% faster** than those in the control group [38].
- Seniority and daily hours spent programming positively moderated the velocity gains achieved with AI tools [38].
- Cognitive testing (2 rounds with 17 Google engineers) revealed that several published external survey questions suffered from double-barreled structures or vague phrasing, requiring extensive adaptation [7, 10].
- Pilot testing across 8 iterations established a reliable enterprise coding task (building a C++ data logging server) executable in under 1.5 hours without researcher intervention [8, 11, 14].
- Established that product quality benchmarking requires a balanced focus between underlying LLM model performance and the overall developer experience (DX) [2, 41, 42].

---

## Desafios do Uso das Metricas

- Industry over-steering toward computational model benchmarks (e.g., Pass@1, PyBench) rather than developer experience metrics [2, 41, 43].
- Rapid iteration of generative AI features making static benchmarks quickly obsolete [4].
- Difficulty in creating high-fidelity, enterprise-grade benchmarking tasks that remain feasible within realistic time windows (<2.5 hours) without turning into toy problems [4, 44].
- High resource and time investments required (developing and pre-testing the components spanned nearly a full calendar year) [12].
- Dependency on precise automated logging infrastructure, as self-reported completion times lack rigor [31].
- Large sample size requirements (>100 participants) to achieve sufficient statistical power in randomized controlled trials [12, 31].

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

- Conducted within a single enterprise environment (Google) using proprietary internal C++ infrastructure, which may limit direct generalizability to small-scale or non-enterprise setups [5, 14, 45].
- Significant creation and validation timeline required (~1 full calendar year) [12].
- Requires robust, mature logging infrastructure to record exact time on task [31].
- High statistical power requirements (>100 participants) needed for controlled trial implementations [12, 31].
- Requires substantial participant time commitment (up to 4 hours across 3 activities) [9, 15].

---

## Contribuicao Principal

The primary contribution of this paper is the step-by-step methodology, pre-tested survey instruments, standardized C++ task stimulus, and experimental protocol shared to enable researchers and practitioners to rigorously benchmark the user experience, productivity gains, and quality of generative AI developer tools across products and over time [5, 17, 46].

---

*Extraido via NotebookLM em October 2026 para MLR: Software Developer Metrics in Practice*

---

💡 **Nudge**: Would you like me to create a tailored summary report or flashcard study deck from this analysis for quick review?
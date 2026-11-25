# P2027 — Experimental Analysis of Productive Interaction Strategy with ChatGPT: User Study on Function and Project-level Code Generation Tasks

**Decisao: INCLUIDO | Qualidade: 5/5** [1-5]

---

## Dados Bibliograficos

| Campo | Valor |
|-------|-------|
| **ID** | P2027 [1] |
| **Autores** | Sangwon Hyun, Hyunjun Kim, Jinhyuk Jang, Hyojin Choi, Muhammad Ali Babar [1] |
| **Ano** | 2026 [6] |
| **Venue** | ACM Transactions on Software Engineering and Methodology (TOSEM) [7] |
| **DOI** | https://doi.org/10.1145/3844949 [6] |
| **Tipo** | Journal article [6, 7] |
| **Metodo** | Empirical study / Controlled experiment (Mixed quantitative feature screening and qualitative trace analysis) [1, 5, 8] |
| **Amostra** | 36 participants (18 undergraduate students, 8 graduate students, and 10 industry/research practitioners) [1, 8, 9] |
| **Contexto** | Mixed (Academic and Industry backgrounds; global sample across East Asia, Southeast Asia, Europe, and Oceania) [9-11] |
| **Modo de trabalho** | Hybrid (Conducted online and offline) [12] |
| **Metodologia** | Not specified [12, 13] |

---

## Objetivo

The main objective of this paper is to conduct a controlled empirical analysis of Human-LLM Interaction (HLI) features and prompting strategies associated with software engineering code generation productivity across both function-level and dependency-rich project-level tasks [1, 4, 8]. The authors aim to identify which user, model, and interaction features consistently correlate with code generation performance, formulate evidence-backed interaction guidelines, and establish a comprehensive taxonomy of runtime and logic errors encountered during LLM-assisted code generation along with mitigation plans [1-4].

---

## Questoes de Pesquisa

- **RQ1**: Which HLI features show the strongest and the most consistent associations with code generation productivity under the study condition? [4]
- **RQ2**: What best practice guidelines can be established for strategic interactions with GPTs to enhance productivity? [4]
  - **RQ2-1**: Which prompting patterns yield the highest productivity for both function-level and project-level software engineering tasks? [4]
  - **RQ2-2**: What features distinguish the Best quartile group from the other groups? [4]
- **RQ3**: What errors occur during HLI processes for code generation? [4]

---

## Metricas e Instrumentos de Avaliacao

| Metrica | Categoria | Nivel | Como Coletada | Validada |
|---------|-----------|-------|---------------|----------|
| **Test Passed Rate (TPR)** | Productivity / Quality | Individual | Automated execution of predefined unit test cases over a 70-minute session [2, 14-16] | Yes [2, 15, 16] |
| **Time-to-Completion** | Productivity / Delivery | Individual | Logged time taken when all test cases are satisfied within 70 minutes [16] | Yes [16] |
| **Subjective Productivity** | Satisfaction / DevEx | Individual | Post-task survey with 30 multiple-choice and text questions (0–100 scale) [12, 17, 18] | Yes [17, 18] |
| **Subjective Accuracy** | Quality / Satisfaction | Individual | Post-task survey evaluation of generated code accuracy (0–100 scale) [18-20] | Yes [18] |
| **Subjective Efficiency** | DevEx / Productivity | Individual | Post-task survey evaluation of prompting strategy efficiency (0–100 scale) [18-20] | Yes [18] |
| **Future Usage Preference** | Satisfaction / DevEx | Individual | Post-task survey rating participant preference to adopt prompting patterns in practice (0–100 scale) [17-20] | Yes [17, 18] |
| **Fixing Time by Generation Time Ratio** | Process / Activity | Individual | Manual time tracking from screen recordings and GPT chat logs comparing code fixing vs. initial code generation [21, 22] | Yes [21, 22] |
| **Pass@K** | Productivity / Quality | Individual | Referenced benchmark metric for LLM code generation accuracy [16] | Yes [16, 23] |

---

## Frameworks e Metricas

### Frameworks Referenciados
- **SPACE Framework** (Forsgren et al., 2021): REFERENCED — Cited to emphasize that developer productivity is multidimensional rather than reducible to a single output metric [24, 25].
- **DevEx Framework** (Noda et al., 2023): REFERENCED — Cited to highlight the impact of developer experience, friction points, and perceived productivity [25, 26].
- **5W1H HLI Catalogue** (Gao et al., 2024): REFERENCED — Extended to construct the catalogue of User, Model, and Interaction attributes for code generation tasks [27, 28].
- **ClassEval Benchmark Framework** (Du et al., 2023/2024): REFERENCED — Used as a structural baseline for class-level skeleton code design and multi-class dependency evaluation [3, 23, 29].
- **Test-Driven Development (TDD)**: REFERENCED — Cited and discussed as an interaction process model for LLM-assisted workflows [13, 30-32].

### Frameworks Propostos
- **Multi-Class Code Generation Benchmark & HLI Productivity Framework**: Proposed two multi-class project-level benchmark tasks (E-Commerce App and Smart Home Gym) with 228 test cases, an exploratory HLI feature-screening framework utilizing ElasticNet, Debiased Lasso, and Bootstrap stability selection, and a taxonomy of 29 runtime and logic error categories [1-3, 5, 33, 34].

---

## Fatores que Influenciam Produtividade

### Fatores Positivos
| Fator | Categoria |
|-------|-----------|
| **Few-Shot Prompting Pattern** (demonstrates the strongest and most consistent association with high Test Passed Rate across tasks) [2, 35, 36] | Technical / Process |
| **Reflection Prompting Pattern** (yields the highest maximum Test Passed Rate and superior subjective satisfaction in project-level tasks) [36, 37] | Process / Human |
| **Debugging-Oriented Time Allocation** (shifting effort to refine code iteratively after quick initial implementation, ~3:1 fixing-to-generation ratio) [2, 22, 35] | Process / Technical |
| **Context Curation combining Copy-Paste with Manual Formulation** (adding specific requirements, rules, or expected model roles) [2, 38, 39] | Process / Technical |
| **Utilizing Executable Test Logs and Test Case Code as Debugging Context** [40] | Technical / Process |
| **Paid GPT Model Tier (GPT-4o)** (associated with top-quartile performance, though secondary to prompting strategy) [35, 41, 42] | Technical |

### Fatores Negativos
| Fator | Categoria |
|-------|-----------|
| **Excessive Prompting Interactions in Cognitive Verifier & Alternative Approach Patterns** (~50% more prompt exchanges required per class, creating overhead in time-bounded tasks) [43] | Process / Technical |
| **Relying Solely on Manual Context Formulation Without Copy-Pasting Specifications** (increases LLM hallucinations due to missing contextual constraints) [44, 45] | Process / Technical |
| **Allocating Too Much Time to Initial Code Generation vs. Iterative Debugging** [22] | Process |
| **Relying Solely on High-Level Design Documents for Debugging** (less effective than exact test case code and tracebacks) [40] | Process / Technical |
| **High Reliance on User Algorithmic Experience Without Copying Specifications** (leads participants to bypass canonical specifications, causing context omissions) [35, 44] | Human / Process |
| **Context Window Overload / Excessive Redundant Details in Prompts** (triggers multi-class dependency hallucinations, e.g., ad-hoc list/dict implementations instead of dependent objects) [46] | Technical |

---

## Papel da IA e Automacao

| Campo | Valor |
|-------|-------|
| **Usa IA/ML?** | **Yes** — Participants used ChatGPT models (Free tier: GPT-3.5 / GPT-4o-mini; Paid tier: GPT-4o / o1) for function-level and project-level code generation and debugging tasks [1, 47, 48]. |
| **Automacao de coleta?** | **Yes** — Automated execution of unit test suites to measure Test Passed Rates (TPR), branch/line coverage evaluation, and online survey response collection [12, 15, 17]. |
| **Impacto de IA na produtividade?** | **High for function-level tasks** (10/12 participants passed 100% of tests within 70 min) [49]; **Moderate/Challenging for multi-class project-level tasks** (max TPR of 53%, average 32–48% depending on prompt pattern) [20, 50]. Interaction strategies (prompting pattern, context curation, time allocation) impacted productivity significantly more than model tier alone [42, 51, 52]. |

---

## Resultados Principais

- **Consistent Productivity Drivers (RQ1)**: Statistical screening (ElasticNet, Debiased Lasso, Bootstrap selection across 15 HLI features) revealed that prompt pattern (specifically Few-Shot), debugging-oriented time allocation, and context curation behavior are the features most strongly and consistently associated with Test Passed Rate (TPR) [2, 5, 35, 53].
- **Prompt Pattern Performance (RQ2-1)**:
  - *Function-level tasks*: High success across all patterns (10 of 12 participants achieved 100% TPR) [49]. Few-Shot and Cognitive Verifier achieved the highest productivity (avg TPR = 1.0) and future preference ratings (93.33%) [19, 54].
  - *Project-level tasks*: Maximum TPR achieved was 0.53 (121/228 test cases passed in 70 minutes) [50]. Few-Shot achieved the highest average TPR (0.48) with statistically significant superiority over Alternative Approach (p = 0.02) and Cognitive Verifier (p = 0.0005) [20, 36]. Reflection achieved the highest maximum TPR (0.53) and top subjective productivity (66.17), accuracy (62.17), and efficiency (74.17) scores [20, 37].
- **Interaction Overhead**: Cognitive Verifier and Alternative Approach patterns required an average of 5.4 to 7.3 prompt requests per class compared to 3.5 to 5.0 for Few-Shot and Reflection, creating significant interaction friction in time-bounded project tasks [43].
- **Top Quartile Practices (RQ2-2)**:
  - Participants in the top TPR quartile allocated approximately 3x more time to code fixing/debugging (avg 50 min) than initial generation (avg 17 min), whereas lower quartiles spent ~50% of session time generating initial code and ran out of time during debugging [22].
  - Combining Copy-Paste of design specifications with Manual Formulation (clarifying expected model roles or edge rules) increased test pass performance by ~24% compared to pure Copy-Paste [39, 55].
  - 10 out of the top 12 participants used executable test case code and failure tracebacks directly as debugging context rather than high-level design documents [40].
- **Error Taxonomy (RQ3)**: Out of 791 total errors recorded across 6,336 test executions, 675 runtime and logic errors were analyzed and categorized into a taxonomy of 29 categories: 19 runtime error categories (420 instances; e.g., V-1 regex condition issues, A-3 immutable attribute settings) and 10 logic error categories (255 instances; e.g., L-8 multi-class dependency issues, L-7 missing conditions) [34, 56-58].
- **Model Tier vs. Prompting Strategy**: While Paid GPT-4o models yielded a 12.2% higher average TPR than Free models in project-level tasks, the difference was not statistically significant (p > 0.05) [42]. In contrast, prompting patterns and time allocation produced statistically significant productivity differences within the same model tier [42, 52].

---

## Desafios do Uso das Metricas

- **Limitations of Single-Dimension Metrics**: Relying solely on code correctness metrics like TPR or Pass@K fails to capture maintenance, code security, reusability, or developer satisfaction [16, 59].
- **Multi-Class Complexity Degradation**: Pass rates drop dramatically when moving from isolated function-level requirements to multi-class project tasks with cross-class dependencies and state propagation [1, 23, 33, 50].
- **Context Window Overload**: Providing excessive or redundant design documentation in prompts degrades model performance on multi-class dependencies, causing models to invent ad-hoc data structures instead of instantiating dependent classes (Error L-8) [46].
- **Hallucinated Solutions in Multi-Option Patterns**: In the Alternative Approach pattern, models tend to apply detailed context only to the first option, producing hallucinated logic in subsequent options while persuasively recommending them to users [60].
- **Side-Effect Errors During Iterative Patching**: Automated code fixes frequently introduce regression side-effects in non-target code areas, such as removing existing attributes, altering function parameter orders, or changing method names (Errors A-4, A-5, L-4, L-5, L-9) [61, 62].

---

## Avaliacao de Qualidade Metodologica

| Criterio | Pontuacao (0-2) |
|----------|----------------|
| Objetivo claramente definido | 2 [4] |
| Metodologia adequada ao objetivo | 2 [5, 8] |
| Amostra/contexto descrito adequadamente | 2 [9-11] |
| Ameacas a validade discutidas | 2 [59, 63-65] |
| Resultados com evidencia suficiente | 2 [5, 20, 22, 36] |
| Contribuicao clara para pratica ou teoria | 2 [1-3, 66] |
| **TOTAL** | **12/12** [1-5] |

---

## Limitacoes

- **Exploratory Sample Size**: With 36 participants and 15 candidate features, the quantitative statistical analysis is exploratory (feature screening) rather than confirmatory causal testing [5, 8, 65].
- **WebUI Interface Constraint**: Participants used a standardized web chat interface rather than IDE-integrated assistants (e.g., GitHub Copilot) or API tools, which may limit direct transferability to IDE environments [47, 64, 67].
- **Controlled Task Scope**: Project-level tasks (E-Commerce App and Smart Home Gym) were controlled proxies focused on multi-class dependencies, excluding UI, external APIs, deployment infrastructure, or legacy codebases [33, 64].
- **Task 2 Progression Threshold**: Access to Task 2 required passing 121/128 tests in Task 1; because most participants did not pass Task 1 within 70 minutes, complete combinatorial data across both tasks was limited [65, 68].
- **Bounded Manual Coding Intervention**: Manual coding was permitted after three unsuccessful GPT attempts on an issue, meaning final TPR reflects a combination of LLM output, human prompting, and minor manual fixes [59, 69].
- **Unarchived Initial Agreement Matrix**: The pre-adjudication inter-rater label matrix for error taxonomy was not retained in numerical format, though consensus was reached through 3-author adjudication [51].

---

## Contribuicao Principal

The principal contribution of this paper is an empirical, evidence-backed characterization of Human-LLM Interaction (HLI) strategies for code generation across function-level and multi-class project-level software engineering tasks [1, 8, 70]. The authors introduce two open-source multi-class benchmark tasks, demonstrate through quantitative screening and qualitative trace analysis that interaction behavior (specifically Few-Shot prompting, a 3:1 debugging-to-generation time allocation, and combining Copy-Paste with manual context formulation) drives code generation productivity more significantly than model tier alone, and establish a comprehensive taxonomy of 29 runtime and logic error categories with actionable mitigation guidelines for developers, researchers, and tool builders [1-3, 66, 70].

---

*Extraido via NotebookLM em October 2026 para MLR: Software Developer Metrics in Practice*

---

💡 Would you like me to generate a tailored report artifact summarizing these findings or compare P2027 against other empirical studies in your collection?
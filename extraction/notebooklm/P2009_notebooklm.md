# P2009 — Beyond Correctness: Measuring Hallucination Impact in AI-Assisted Development Workflows

**Decisao: INCLUIDO | Qualidade: 3.5/5**

---

## Dados Bibliograficos

| Campo | Valor |
|-------|-------|
| **ID** | P2009 [1] |
| **Autores** | Shubham Gupta, Kusumakumari Vanteru, Prathyusha Kanmanth Reddy, Shashidhar Sunkireddy [1] |
| **Ano** | 2026 [1] |
| **Venue** | International Conference on Innovations in Emerging Technologies for Sustainable Development (ICIETSD) / IEEE [1] |
| **DOI** | 10.1109/ICIETSD68684.2026.11584879 [1] |
| **Tipo** | Conference paper [1] |
| **Metodo** | Experiment (Within-subjects experimental design using a calibrated synthetic dataset) [2, 3] |
| **Amostra** | Synthetic dataset modeling hundreds of vibe-coding sessions across web spanning, data processing, and scripting tasks [3] |
| **Contexto** | AI-assisted development / Vibe coding in AI-native IDEs (calibrated using empirical findings from Industry & OSS) [1, 3, 4] |
| **Modo de trabalho** | Not specified [1, 4] |
| **Metodologia** | Not specified [1, 4] |

---

## Objetivo

This paper aims to move beyond binary code correctness evaluations by proposing a multi-dimensional measurement framework to assess the downstream impact of LLM hallucinations on developer productivity, code quality, and technical debt accumulation within vibe coding workflows in AI-native IDEs [5-8].

---

## Questoes de Pesquisa

- **RQ1**: How do particular types of hallucinations in AI-assisted code generation influence the productivity of developers, code quality, and technical debt in vibe coding workflows? [8]

---

## Metricas e Instrumentos de Avaliacao

| Metrica | Categoria | Nivel | Como Coletada | Validada |
|---------|-----------|-------|---------------|----------|
| **Task completion time** | Productivity | Individual | Wall-clock time from task start to passing tests logged via IDE timestamps [9, 10] | Yes [9] |
| **Iteration count** | Productivity | Individual | Number of prompt–execute cycles per task logged automatically in the IDE [10, 11] | Yes [9] |
| **Context switches** | Productivity / DevEx | Individual | IDE event logs tracking switches to external tooling or manual documentation lookups [10, 11] | Yes [11] |
| **Automated test pass rate** | Quality | Individual / Team | Test suite execution pass percentage per completed task [10, 11] | Yes [12] |
| **Defect density** | Quality | Individual / Team | Number of defects per thousand lines of code (defects/KLOC) [11, 13] | Yes [12] |
| **API-misuse rate** | Quality | Individual / Team | Rule-based classification matching API calls against schemas (hallucination, intent, missing item, redundancy) [10, 12] | Yes [12] |
| **Static-analysis warnings** | Quality | Individual / Team | Automated static analyzer output for type errors, unsafe operations, or performance anti-patterns [10, 12] | Yes [12] |
| **Rework ratio** | Technical Debt | Individual / Team | Fraction of code lines modified or rewritten shortly after generation due to hallucination defects [14] | Partial [14] |
| **Architectural erosion indicators** | Technical Debt | Team / Organization | Analysis of dependency graph complexity (e.g., new dependencies added per 10 tasks) and duplicated logic [14, 15] | Partial [14] |
| **Latent defect risk** | Technical Debt | Team / Organization | Static checks and follow-up task tracking for unresolved hallucination artifacts that passed initial tests [14] | Partial [14] |

---

## Frameworks e Metricas

### Frameworks Referenciados
- **API Misuse Taxonomy (Kang et al., 2024)**: REFERENCED and APPLIED (used to classify API errors into hallucination, intent, missing item, and redundancy misuses) [10, 16, 17].
- **Multi-Dimensional Developer Productivity Models (Narasimhan et al., 2025; Ziegler et al., 2022)**: REFERENCED (synthesized to inform task completion time, iteration count, and cognitive load metrics) [2, 9, 17, 18].

### Frameworks Propostos
- **Hallucination Impact Propagation Framework in Vibe Coding**: Proposes a multi-dimensional conceptual model linking three developer-facing hallucination types (Fabricated APIs, Incorrect Parameters, Non-existent Libraries) through prompt-execution loops (LLM Suggestion → Developer Acceptance → Execution & Feedback) to measure outcomes across Developer Productivity (task time, iterations, context switches), Code Quality (test pass rate, defect density, API misuses), and Technical Debt (rework ratio, dependency sprawl, latent defect risk) [7-9, 11, 12, 14, 19, 20].

---

## Fatores que Influenciam Produtividade

### Fatores Positivos
| Fator | Categoria |
|-------|-----------|
| Automated setups, settings, and boilerplate generation in AI-native IDEs (3-5x acceleration in initial prototyping) | Technical [21] |
| Natural language intent specification reducing initial task initiation overhead and manual code writing | Process [22, 23] |
| Broad speculative AI suggestions accelerating initial exploration and design ideas | Technical [24, 25] |
| Cognitive offloading of repetitive tasks to LLM coding assistants | Human [21] |

### Fatores Negativos
| Fator | Categoria |
|-------|-----------|
| Hallucinations (fabricated APIs, wrong parameters, nonexistent packages) requiring repetitive debugging and trial-and-error cycles | Technical [24, 26, 27] |
| High context switching frequency to inspect external documentation or resolve execution failures | Process / Human [11, 27] |
| Over-reliance and decreased critical code examination leading to subtle runtime and semantic bugs | Human [18, 21, 28] |
| Overhead of validating, correcting, and refactoring unreliable AI suggestions | Process [18, 29] |
| Dependency sprawl and package confusion risks resulting in technical debt and supply-chain vulnerabilities | Organizational / Technical [15, 30, 31] |

---

## Papel da IA e Automacao

| Campo | Valor |
|-------|-------|
| **Usa IA/ML?** | Yes — Evaluates LLM coding assistants and AI-native IDEs operating in vibe coding workflows [4, 5, 22]. |
| **Automacao de coleta?** | Yes — Automated logging of prompts, AI responses, compilation/test execution, IDE event timestamps, static analysis, and rule-based API misuse detection [10]. |
| **Impacto de IA na produtividade?** | Mixed / Nuanced — Hallucination-rich AI assistance slightly decreases median task time (26 min vs 30 min baseline) but increases iteration count (6 vs 4), context switches (5 vs 3), rework ratio (31% vs 18%), defect density (1.4 vs 0.8 defects/KLOC), and dependency sprawl (2.6 vs 1.2 new dependencies/10 tasks) [13, 15, 27]. |

---

## Resultados Principais

- **Hallucination Breakdown**: In hallucination-rich vibe coding sessions, API misuses comprised 40% Incorrect Parameters, 35% Fabricated APIs, and 25% Non-existent Libraries [32].
- **Short-Term Speed vs. Debugging Overhead**: Exposure to high hallucination rates slightly reduced median task completion time from 30 to 26 minutes, but increased iterations per task from 4 to 6 and context switches from 3 to 5 due to trial-and-error debugging [27].
- **Degradation of Code Quality**: High hallucination incidence caused test pass rates to drop from 92% to 84%, defect density to increase from 0.8 to 1.4 defects/KLOC, and API hallucination misuses per task to jump from 0.5 to 2.1 [13, 33].
- **Accumulation of Technical Debt**: Hallucinations elevated the rework ratio from 18% to 31%, increased new dependency acquisition from 1.2 to 2.6 per 10 tasks, and raised relative latent defect risk from 1.0 to 1.8 [15].
- **Vulnerability of Vibe Coding**: Vibe coding workflows, which prioritize rapid execution feedback over manual code review, are particularly susceptible to accepting confident hallucinations that introduce subtle semantic bugs and long-term architectural debt [4, 21, 28, 34].

---

## Desafios do Uso das Metricas

- Evaluating LLM tools strictly via dichotomous accuracy/correctness metrics obscures long-term workflow disruptions and structural debt [6, 8, 23].
- Direct measurement of technical debt is inherently difficult, necessitating proxy metrics (rework ratio, dependency graph complexity, latent defect risk) [12, 14].
- **Anti-pattern**: Relying exclusively on immediate execution feedback without manual inspection in vibe coding, which allows latent hallucination defects to bypass shallow tests [4, 14, 21, 28].
- **Anti-pattern**: Blindly accepting suggested external dependencies, leading to package confusion vulnerabilities and dependency sprawl [30, 31, 34].

---

## Avaliacao de Qualidade Metodologica

| Criterio | Pontuacao (0-2) |
|----------|----------------|
| Objetivo claramente definido | 2 |
| Metodologia adequada ao objetivo | 1 |
| Amostra/contexto descrito adequadamente | 1 |
| Ameacas a validade discutidas | 1 |
| Resultados com evidencia suficiente | 1 |
| Contribuicao clara para pratica ou teoria | 2 |
| **TOTAL** | **8/12** |

---

## Limitacoes

- Relies on a synthetic dataset calibrated from prior empirical literature rather than a large-scale empirical study with real human developers [3, 35, 36].
- Task domain is focused on web spanning, data processing, and scripting tasks, which may not represent complex enterprise software systems [3, 36].
- Technical debt metrics are proxy indicators rather than direct observations from multi-year software maintenance [14, 37].
- Findings require further validation across different IDE designs, organizational policies, guardrail architectures, and programming languages [36].

---

## Contribuicao Principal

The main contribution of this paper is the introduction of a multi-dimensional framework and evaluation model that measures the impact of LLM hallucinations beyond simple code correctness by quantifying their downstream effects on developer productivity, code quality, and technical debt within vibe coding workflows [5-8, 19]. By establishing a taxonomy of developer-facing hallucinations (fabricated APIs, incorrect parameters, non-existent libraries) and tracing their propagation through prompt-execution feedback loops, the study provides calibrated empirical insights into the trade-offs between short-term coding speed and long-term codebase health, alongside practical mitigation strategies for AI-native IDEs [7, 19, 38-40].

---

*Extraido via NotebookLM em October 2026 para MLR: Software Developer Metrics in Practice*

🔍 Would you like me to synthesize these findings into a comparative report alongside other papers in your systematic mapping study?
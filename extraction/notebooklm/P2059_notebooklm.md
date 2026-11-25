# P2059 — Echoes of AI: Investigating the downstream effects of AI assistants on software maintainability

**Decisao: INCLUIDO | Qualidade: 5/5** [1-3]

---

## Dados Bibliograficos

| Campo | Valor |
|-------|-------|
| **ID** | P2059 [1] |
| **Autores** | Markus Borg, Dave Hewett, Nadim Hagatulah, Noric Couderc, Emma Söderberg, Donald Graham, Uttam Kini, Dave Farley [1, 4] |
| **Ano** | 2026 [1] |
| **Venue** | Empirical Software Engineering (EMSE) [1] |
| **DOI** | 10.1007/s10664-026-10889-1 [1] |
| **Tipo** | Journal article [1] |
| **Metodo** | Controlled experiment (Preregistered two-phase study with Phase 2 Randomized Controlled Trial) [1, 5] |
| **Amostra** | 151 participants with valid completed tasks (76 in Phase 1, 75 in Phase 2; 95.4% professional developers; out of 449 total pre-screening signups) [1, 2, 6, 7] |
| **Contexto** | Industry / Mixed (Professional software developers across various international IT organizations and Equal Experts community) [1, 8-10] |
| **Modo de trabalho** | Remote [6, 11] |
| **Metodologia** | Not specified [6, 12] |

---

## Objetivo

This study investigates whether co-developing source code with AI assistants (such as GitHub Copilot, ChatGPT, and Cursor) affects downstream software maintainability, specifically assessing how easily and efficiently other developers can subsequently evolve and modify that code without AI assistance [1, 5, 13].

---

## Questoes de Pesquisa

- **RQ1**: Do developers manually evolve code that has been co-developed with AI assistants more efficiently? [13]
- **RQ2**: Does code co-developed with AI assistants result in higher quality upon manual evolution? [13]

---

## Metricas e Instrumentos de Avaliacao

| Metrica | Categoria | Nivel | Como Coletada | Validada |
|---------|-----------|-------|---------------|----------|
| Completion Time | Productivity / Efficiency and flow | Individual | Continuous integration timestamps via snapcode.review/GitHub Actions pipeline and self-reported estimates for interrupted sessions | Yes [13-16] |
| CodeHealth (CH) | Quality / Maintainability | Project (File-weighted average) | Static code analysis using CodeScene CLI with customized sensitivity configuration in GitHub Actions pipeline | Yes [13, 17-19] |
| Test Coverage (TC) | Quality / Activity | Project | Line coverage measured using JaCoCo integrated into GitHub Actions CI pipeline | Yes [13, 20] |
| Perceived Productivity (PP) | DevEx / Productivity / Satisfaction | Individual | 10-item 5-point Likert scale in exit survey mapped to the SPACE framework | Yes (Cronbach's \\(\alpha = 0.82\\)) [13, 14, 21] |
| Lines of Code (LoC) / Git Activity | Activity | Project / Individual | Git diff analysis and `cloc` tool executed in continuous integration pipeline | Yes [18, 22, 23] |
| Code Smells & Static Violations | Quality | File / Project | Static analysis tools CodeScene (25+ smell rules) and PMD linter (v7.13.0) | Yes [17, 24-26] |

---

## Frameworks e Metricas

### Frameworks Referenciados
- **SPACE**: REFERENCED & APPLIED — Used to conceptualize multi-dimensional developer productivity (Satisfaction, Performance, Activity, Communication/Collaboration, Efficiency/Flow) and structure the 10-item perceived productivity Likert instrument [5, 14, 27].
- **ISO/IEC 25010**: REFERENCED — Cited to frame the top-level definition of software maintainability and its five sub-characteristics (modularity, reusability, analyzability, modifiability, testability) [28, 29].
- **GQM (Goal Question Metric)**: REFERENCED — Applied to structure the study's overall research goal, research questions, and quantitative metrics [6, 13].
- **DORA**: REFERENCED — Discussed in background context regarding software engineering measurement frameworks [13].
- **ACM SIGSOFT Empirical Standards**: REFERENCED — Used as a design guide and reporting checklist for human-subject software engineering experiments and ethics [3, 13, 30].

### Frameworks Propostos
The paper does not propose a new software metric framework; rather, it proposes a preregistered, two-phase empirical experimental methodology (combining Phase 1 feature implementation and Phase 2 RCT code hand-off evolution) to quantify downstream maintainability [1, 5, 31].

---

## Fatores que Influenciam Produtividade

### Fatores Positivos
| Fator | Categoria |
|-------|-----------|
| Direct use of AI assistants during initial feature implementation (median 30.7% speedup) | Technical [1, 32] |
| Habitual use and familiarity with AI assistants (55.9% posterior mean speedup) | Human [1, 33] |
| High Java programming proficiency and developer seniority | Human [33, 34] |
| AI assistance during technology stack onboarding and code comprehension | Technical / Human [35, 36] |
| AI assistance in reducing setup friction and boilerplate code generation | Process / Technical [37] |

### Fatores Negativos
| Fator | Categoria |
|-------|-----------|
| Task interruptions and breaks during development sessions (173.7% completion time increase) | Process / Human [38] |
| Unfamiliarity with technology stack (Java, Spring Boot, JPA) and local environment setup issues | Human / Process [37, 39] |
| Ambiguity in quality expectations and subjective "definition of done" | Process [40, 41] |
| Misleading AI assistant suggestions during bug fixing and initial debugging | Technical [42, 43] |
| Onboarding and understanding larger or bloated codebases handed off by prior developers | Technical / Process [44] |

---

## Papel da IA e Automacao

| Campo | Valor |
|-------|-------|
| Usa IA/ML? | Yes — Phase 1 evaluates participants using generative AI tools (GitHub Copilot, ChatGPT, Cursor, JetBrains AI, Claude, etc.) vs. manual development [1, 10, 45] |
| Automacao de coleta? | Yes — Fully automated CI/CD pipeline via GitHub Actions, snapcode.review, JaCoCo, CodeScene, and PMD for metric collection [18, 20, 25, 46] |
| Impacto de IA na produtividade? | Direct impact in Phase 1: 30.7% median task completion time reduction (55.9% speedup for habitual users). Downstream impact in Phase 2 RCT: No statistically significant difference in completion time (-12.6% posterior mean change, \\(p = 0.56\\)) or perceived productivity (-0.10 mean diff, \\(p = 0.37\\)) when evolving AI-co-developed code [1, 47-50] |

---

## Resultados Principais

- **Direct Speedup in Phase 1**: Direct use of AI assistants resulted in a 30.7% median reduction in task completion time (Cliff's \\(\delta = -0.42, p = 0.0029\\)), with habitual AI users achieving a 55.9% posterior mean speedup (95% CrI: [-77.1%, -30.6%]) [1, 32, 33, 51].
- **Phase 2 Downstream Completion Time (RQ1)**: No statistically significant difference in completion time was observed when new developers evolved AI-assisted code vs. manually written code (median 136 min vs. 173 min, Cliff's \\(\delta = -0.079, p = 0.56\\); Bayesian posterior mean change: -12.6%, 95% CrI: [-45.8%, +32.7%]) [1, 47, 48].
- **Phase 2 Perceived Productivity (RQ1)**: No significant difference in perceived productivity occurred between treatment (mean 3.95) and control (mean 4.06, \\(p = 0.37\\), Cohen's \\(d = -0.21\\); Bayesian latent productivity change: -1.26 SD, 95% CrI: [-2.46, +2.31]) [49, 50].
- **Phase 2 Code Quality / CodeHealth (RQ2)**: Frequentist analysis showed no significant difference in CodeHealth between treatment (mean 8.49) and control (mean 8.44, \\(p = 0.24\\), Cohen's \\(d = 0.28\\)). However, Bayesian analysis indicated a small, reliable CodeHealth advantage (+0.10 points, \\(P(\Delta > 0) = 98\%\\), 95% CrI: [+0.02, +0.19]) when the original code was co-developed by a habitual AI user [52, 53].
- **Phase 2 Test Coverage (RQ2)**: Test coverage showed no difference between groups, with both achieving a median line coverage of 70% (Cliff's \\(\delta = 0.09, p = 0.49\\); Bayesian predicted mean change: +1 percentage point) [54-56].
- **Impact of Session Interruptions**: Taking breaks during task execution was the single largest factor slowing completion time (+173.7% increase, 95% CrI: [+37.7%, +416.9%]) [38].
- **Developer Skill vs. AI Impact**: A developer's individual Java proficiency had a stronger positive impact on code quality and downstream evolution than whether AI assistance was used [34, 57].
- **Code Smells & Refactoring Patterns**: AI-assisted developers resolved the "Bumpy Road" code smell more frequently in Phase 1 (72% vs. 46%), but introduced higher volumes of surface-level comments, formatting verbosity, and complex conditional statements [58-61].

---

## Desafios do Uso das Metricas

- **Uninterrupted Session Protocol Violations**: 48.3% of participants completed tasks with interruptions, rendering raw git timestamps unreliable and necessitating post-hoc self-reported time estimates [16, 62].
- **Vague Quality Expectations & Subjective "Definition of Done"**: Unconstrained instructions caused wide participant variation in effort allocation (ranging from 5-minute minimal implementations to 13-hour comprehensive refactorings), adding noise to completion time and code quality metrics [40, 41, 63, 64].
- **Setup Friction & Tech Stack Noise**: Varying local environment setup issues and differences in Spring Boot/Java familiarity created task duration variance unrelated to source code maintainability [37, 63].
- **Statistical Power Constraints in RCT**: The Phase 2 sample size (\\(N=75\\)) achieved 80% power only for large effect sizes (\\(d \approx 0.66\\)), rendering frequentist statistical tests underpowered for detecting subtle maintainability differences [7, 65, 66].
- **Aggregating Ordinal Likert Data**: Converting discrete ordinal survey items into continuous perceived productivity mean scores required validation via Cronbach's alpha and Bayesian ordinal logistic regression modeling [21, 67, 68].

---

## Avaliacao de Qualidade Metodologica

| Criterio | Pontuacao (0-2) |
|----------|----------------|
| Objetivo claramente definido | 2 [1, 13] |
| Metodologia adequada ao objetivo | 2 [1, 5, 30, 69] |
| Amostra/contexto descrito adequadamente | 2 [6, 7, 9] |
| Ameacas a validade discutidas | 2 [66, 70-72] |
| Resultados com evidencia suficiente | 2 [47, 52, 73, 74] |
| Contribuicao clara para pratica ou teoria | 2 [2, 75-77] |
| **TOTAL** | **12/12** [1, 3, 70] |

---

## Limitacoes

- **Short-Term Evaluation Horizon**: Focuses strictly on immediate single hand-off evolution tasks rather than long-term maintainability over extended software lifecycles [70].
- **Individual Developer Focus**: Evaluates individual code hand-offs and does not address social team dynamics, code review processes, or collaborative maintenance [70].
- **Small Codebase Scale**: The target system (RecipeFinder, 2 KLoC) was kept small for feasibility, limiting conclusions regarding large-scale enterprise architectures or LLM context window limits [70, 78].
- **Manual Phase 2 Evolution**: Phase 2 maintainers evolved code without AI assistance; scenarios where downstream maintainers also use AI were not evaluated [70, 79].
- **Omitted Quality Dimensions**: Security vulnerabilities, runtime performance, and architectural trade-offs were outside the study's scope [70].
- **Demographic & Tooling Constraints**: Heavy male gender skew (95%), lack of representation from major Asian developer markets (China, Japan, South Korea), and pre-dates third-generation autonomous coding agents [80-82].

---

## Contribuicao Principal

The main contribution of this paper is providing the first preregistered, randomized controlled trial examining the downstream effects of AI-assisted development on software maintainability when source code is subsequently evolved by another developer [1, 2, 5]. The study demonstrates that while direct use of AI assistants provides significant short-term speedups (~30–56%), it introduces no systematic maintainability penalties or major speed/quality advantages for future developers evolving the codebase [1, 51, 83]. It highlights that human developer proficiency remains paramount, while cautioning against emerging risks of codebase bloat and cognitive debt from unrestrained AI code generation [34, 76, 77, 84, 85].

---

*Extraido via NotebookLM em October 2026 para MLR: Software Developer Metrics in Practice*

💡 **Próximo passo**: Gostaria que eu transformasse este resumo estruturado em um relatório executivo em PDF, ou prefere criar um slide deck para apresentar estas descobertas?
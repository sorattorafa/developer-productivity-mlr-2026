# P2036 — AI IDEs or Autonomous Agents? Measuring the Impact of Coding Agents on Software Development

**Decisao: INCLUIDO | Qualidade: 5/5**

---

## Dados Bibliograficos

| Campo | Valor |
|-------|-------|
| **ID** | P2036 |
| **Autores** | Shyam Agarwal, Hao He, Bogdan Vasilescu [1] |
| **Ano** | 2026 [2, 3] |
| **Venue** | 23rd International Conference on Mining Software Repositories (MSR ’26) [3] |
| **DOI** | 10.1145/3793302.3793589 [2, 3] |
| **Tipo** | Conference paper [3] |
| **Metodo** | Quantitative / Repository mining / Quasi-experimental (Staggered Difference-in-Differences with Propensity Score Matching) [4-6] |
| **Amostra** | AIDev dataset (v3), GitHub open-source repositories (≥10 stars, ≥10 agentic PRs). Heterogeneous samples: 401 Agent-First (AF) repositories matched to 606 controls (15,664 obs); 117 IDE-First (IF) repositories matched to 73 controls (3,572 obs) [7-10]. |
| **Contexto** | Open-Source Software (OSS) repositories on GitHub [8, 9, 11, 12] |
| **Modo de trabalho** | Not specified (Distributed open-source software development) [11, 12] |
| **Metodologia** | Not specified (PR-based collaborative software development workflow) [7, 11, 13] |

---

## Objetivo

The main objective of the paper is to evaluate the causal impact of adopting LLM-based autonomous coding agents on project-level software development velocity and code quality in open-source GitHub repositories [4, 11]. Using a longitudinal quasi-experimental staggered difference-in-differences design with propensity score matching, the authors examine whether coding agents accelerate development, how their effects differ from inline IDE-based AI assistants, and whether prior exposure to AI IDEs moderates these velocity and quality outcomes [4-6].

---

## Questoes de Pesquisa

- **RQ1: Development Velocity Impact** — How does the adoption of coding agents affect development velocity? [14]
- **RQ2: Software Quality Impact** — How does the adoption of coding agents affect software quality? [14]
- **RQ3: Prior AI Exposure and Transition Effects** — How do the effects of adopting coding agents differ between repositories with and without prior IDE-based AI assistance? [14]

---

## Metricas e Instrumentos de Avaliacao

| Metrica | Categoria | Nivel | Como Coletada | Validada |
|---------|-----------|-------|---------------|----------|
| **Commits** | Productivity / Delivery | Organization (Repository) | Version history / GHArchive / SonarQube [15] | Yes [6, 9] |
| **Lines Added** | Productivity / Activity | Organization (Repository) | SonarQube / Version history [15] | Yes [6, 9] |
| **Static Analysis Warnings** | Quality | Organization (Repository) | SonarQube static analysis [15] | Yes [6, 9] |
| **Cognitive / Code Complexity** | Quality / DevEx | Organization (Repository) | SonarQube cognitive complexity engine [15] | Yes [6, 9] |
| **Duplicated Line Density** | Quality | Organization (Repository) | SonarQube duplicated code analysis [15] | Yes [6, 9] |
| **Comment Line Density** | Quality / Maintainability | Organization (Repository) | SonarQube comment density analyzer [15] | Yes [6, 9] |

---

## Frameworks e Metricas

### Frameworks Referenciados
- No standard software measurement frameworks (such as DORA, SPACE, DevEx, GQM, HEART, or OKR) are explicitly named or formally cited in the text [16]; however, velocity and code quality measurement dimensions aligned with empirical software engineering research (throughput, complexity, static analysis warnings) are REFERENCED in prior literature and APPLIED via SonarQube and GHArchive telemetry [15, 16].

### Frameworks Propostos
- No new theoretical framework is proposed; the paper applies a quantitative quasi-experimental framework combining Propensity Score Matching (PSM) with Borusyak et al.'s imputation-based staggered Difference-in-Differences estimator to isolate causal treatment effects of agentic AI adoption [4-6].

---

## Fatores que Influenciam Produtividade

### Fatores Positivos
| Fator | Categoria |
|-------|-----------|
| Initial adoption of autonomous coding agents in new-to-AI workflows (Agent-First repos: +36.3% commits, +76.6% lines added) [17, 18] | Technical |
| Asynchronous, repository-level autonomous contributions (multi-file edits, feature implementation, automated PR generation) [7, 11, 13] | Process |
| Automated test generation, documentation generation, and autonomous refactoring [7, 19] | Technical / Process |
| Increased documentation and comment line density in IDE-first repositories (+22.3% comment density) [18, 19] | Technical / Process |

### Fatores Negativos
| Fator | Categoria |
|-------|-----------|
| Prior exposure to AI IDEs / AI saturation (diminishing velocity returns: +3.1% commits, -6.3% lines added in IF repos) [17, 18, 20] | Technical / Organizational |
| Increased code/cognitive complexity (+34.9% AF, +42.9% IF) leading to agent-induced technical debt [18, 19, 21] | Technical |
| Increased static analysis warnings (+17.7% AF, +19.0% IF) requiring additional inspection [18, 21] | Technical |
| Coordination, triage, and PR review overhead in larger/more mature repositories [20] | Process / Organizational |
| Lack of quality safeguards, complexity-aware review, and provenance tracking for agentic PRs [22] | Process / Organizational |

---

## Papel da IA e Automacao

| Campo | Valor |
|-------|-------|
| **Usa IA/ML?** | **Yes** — Evaluates LLM-based autonomous coding agents (Claude Code, OpenAI Codex, Devin, Cursor Agent, OpenHands, Jules, Codegen, Cosine, Tembo) and AI IDE assistants (GitHub Copilot, Cursor, WindSurf) [8, 13, 23]. |
| **Automacao de coleta?** | **Yes** — Automated repository data mining via GHArchive, AIDev dataset (v3), GitHub REST/GraphQL parsing (branch prefixes, bot logins, commit authors, PR comments), and SonarQube static analysis [7, 15, 23]. |
| **Impacto de IA na produtividade?** | **Heterogeneous and front-loaded**: Large velocity gains materialize only when agents are the first observable AI tool in a project (AF: +36.3% commits, +76.6% lines added) [17, 18]. In repositories with prior AI IDE usage (IF), throughput gains are minimal (+3.1% commits, -6.3% lines added) and short-lived [17, 18], while quality risks (increased complexity ~35–43% and static analysis warnings ~18–19%) are persistent across all settings [18, 21]. |

---

## Resultados Principais

- **Velocity Acceleration in Agent-First Repositories**: Repositories adopting AI agents as their first AI tool (AF) experienced substantial post-adoption velocity increases: **+36.3% commits** and **+76.6% lines added** on average [18], with an initial spike at \\(t=0\\) reaching **+111% commits** and **+216% lines added** [18].
- **Diminishing Returns in IDE-First Repositories**: Repositories with prior AI IDE usage (IF) saw virtually no long-term throughput gain (**+3.1% commits** and **-6.3% lines added**) [18], with velocity returning near zero or turning negative by \\(t=6\\) (lines added \\(\sim -61\%\\), commits \\(\sim -35\%\\)) [18, 20].
- **Persistent Maintainability and Quality Debt**: Software quality risks increased consistently across both settings regardless of prior AI experience [11, 21]:
  - **Static analysis warnings** increased by **+17.7%** in AF and **+19.0%** in IF repositories [18, 21].
  - **Cognitive/code complexity** increased by **+34.9%** in AF and **+42.9%** in IF repositories (reaching up to +49% at \\(t=5\\) in AF) [18, 21].
- **Divergent Comment Line Density**: Comment density surged in IF repositories (**+22.3%** overall, \\(>+30\%\\) by \\(t=6\\)) [18, 19], whereas changes in AF repositories were muted (**+4.3%**) [18, 19], suggesting teams with prior AI experience utilize agents heavily for documentation [19].
- **Minimal Code Duplication**: Duplicated line density showed small and non-significant changes (**+7.9%** in AF, **-0.9%** in IF) [18, 19], indicating quality degradation stems from structural/cognitive complexity rather than copy-paste replication [19].

---

## Desafios do Uso das Metricas

- **Agent-Induced Technical Debt Illusion**: Relying solely on throughput/velocity metrics creates a misleading picture of productivity while masking persistent maintenance degradation (cognitive complexity and static analysis warnings) [11, 19].
- **Left-Censoring and Attribution Telemetry Noise**: Detecting and attributing AI agent PRs from git logs requires complex multi-signal cascading heuristics (branch prefixes, bot logins, commit author names, PR description patterns) [7, 8, 23].
- **Inability to Capture Developer-Level Interaction Intensity**: Repository-level aggregate metrics cannot observe individual developer interactions, prompt engineering effort, or manual code review time [6].
- **Short-Term Throughput vs. Long-Term Quality Anti-Pattern**: High-volume AI code churn creates review overhead and integration bottlenecks that offset localized coding speedups [19, 20, 22].
- **Parallel Trend Baseline Differences**: Isolated pre-treatment differences in quality metrics reflect systematic baseline differences between treated and control repositories [19].

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

- **Attribution and Recall Errors**: Agent identification relies on observable signals (PR titles, logins, branch names, descriptions) which may miss unlabelled agent contributions or introduce timing noise [8, 23].
- **Lack of Developer-Level Telemetry**: The study cannot observe individual developer interactions, prompt engineering effort, developer satisfaction, or exact time spent reviewing agent pull requests [6].
- **Quasi-Experimental Baseline Differences**: Isolated significant pre-treatment differences in static analysis warnings and code complexity suggest parallel trend assumptions may not fully hold for all quality outcomes [19].
- **Open-Source Specific Context**: Findings are derived from public GitHub repositories (≥10 stars) and may not directly generalize to closed-source enterprise software environments with mandatory human review workflows [8, 22].
- **Observation Window**: The 6-month post-adoption panel tracks medium-term trajectories but cannot capture multi-year architectural debt or maintenance costs [7, 24].

---

## Contribuicao Principal

The paper provides the first large-scale, longitudinal causal evaluation comparing the repository-level impacts of adopting autonomous AI coding agents versus inline AI IDE assistants [11, 14]. It demonstrates that autonomous agents deliver substantial front-loaded velocity gains only when introduced into new-to-AI workflows, whereas in AI-saturated environments, velocity benefits fade while cognitive complexity and static analysis warnings rise across all settings [11, 17, 18, 21]. These findings establish empirical evidence of an amplified speed–maintainability trade-off, highlighting the critical need for quality safeguards, complexity-aware code reviews, and selective deployment strategies [11, 22].

---

*Extraido via NotebookLM em October 2026 para MLR: Software Developer Metrics in Practice*
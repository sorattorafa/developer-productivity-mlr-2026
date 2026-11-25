# P2041 — Divergence or Convergence? A Deep Insight into the Crowd Collaboration and its Productivity in Open Source Software based on Entropy

**Decisao: INCLUIDO | Qualidade: 5/5**

---

## Dados Bibliograficos

| Campo | Valor |
|-------|-------|
| **ID** | P2041 |
| **Autores** | Yang Shen, Tao Wang, Xunhui Zhang, Yang Zhang, Cheng Yang, Bo Ding, Huaimin Wang [1-3] |
| **Ano** | 2026 [4, 5] |
| **Venue** | Proceedings of the 2026 CHI Conference on Human Factors in Computing Systems (CHI ’26) [5] |
| **DOI** | https://doi.org/10.1145/3772318.3791405 [4, 5] |
| **Tipo** | Conference paper [5] |
| **Metodo** | Quantitative / Repository mining / Longitudinal panel regression analysis [6-9] |
| **Amostra** | 8 open-source GitHub repositories (4 enterprise-driven: facebook/docusaurus, microsoft/playwright, alibaba/nacos, google/googletest; 4 community-driven: fastapi/fastapi, vuejs/vue, rustdesk/rustdesk, ohmyzsh/ohmyzsh), comprising 12,720 forks and 39,300,748 commits [8, 10] |
| **Contexto** | Open Source Software (OSS) GitHub repositories — 4 corporate-driven projects and 4 community-driven projects [6, 10] |
| **Modo de trabalho** | Not specified (Distributed open source software development) [3, 11, 12] |
| **Metodologia** | Not specified (Fork and Pull-Request collaborative model) [3, 12] |

---

## Objetivo

This paper aims to systematically quantify integration effectiveness in open-source software (OSS) repositories by proposing a novel information-theoretic metric called **Convergence Entropy** (\\(H_{conv}\\)), which measures the distributional similarity between original commits across forks and merged commits into the main repository, adjusted by the overall commit merge ratio [3, 13-15]. Furthermore, the paper examines the longitudinal relationship between convergence entropy and three core dimensions of project productivity (Performance, Activity, and Efficiency & Flow) based on the SPACE framework, evaluating how contextual factors such as governance structure, project age, fork volume, issue backlog, codebase size, and developer team composition moderate these dynamics [6, 7, 16, 17].

---

## Questoes de Pesquisa

- **RQ1**: What is the correlation between convergence entropy and the number of new bugs in OSS projects, and what factors could alter this dynamic? [18, 19]
- **RQ2**: How is convergence entropy correlated with the number of new commits in OSS projects, and what factors may affect this connection? [20, 21]
- **RQ3**: To what extent does convergence entropy correlate with issue resolution time in OSS projects, and what factors could strengthen or weaken this association? [22, 23]

---

## Metricas e Instrumentos de Avaliacao

| Metrica | Categoria | Nivel | Como Coletada | Validada |
|---------|-----------|-------|---------------|----------|
| **Convergence Entropy (\\(H_{conv}\\))** | Collaboration / Integration Effectiveness | Team/Organization | Calculated monthly using Jensen-Shannon Divergence (JSD) between original commit distribution across forks (\\(P_o\\)) and merged commit distribution (\\(P_m\\)), scaled by merge ratio (\\(C_m / C_o\\)), via GitHub REST & GraphQL APIs [13, 15, 24, 25] | Yes [9, 13, 15] |
| **New Bugs** | Quality / Performance | Team/Organization | Monthly count of newly opened issues identified as bugs via keyword search in issue titles and tags (defect, error, bug, issue, mistake, incorrect, fault, flaw) via GitHub API [17, 18, 26] | Yes [26, 27] |
| **New Commits** | Productivity / Activity | Team/Organization | Monthly total count of new commits added across all core and external developers via GitHub API [17, 20, 28] | Yes [28, 29] |
| **Issue Resolution Time** | Delivery / Efficiency & Flow | Team/Organization | Monthly average duration (from creation to closure) for all issues closed within the time window via GitHub API [17, 22, 30] | Yes [30, 31] |
| **Ratio of Contributing Forks** | Collaboration / Inefficiency | Team/Organization | Ratio of forks contributing back to the total active forks (cited from Zhou et al.) [32, 33] | Yes [32, 34] |
| **Ratio of Merged PRs** | Collaboration / Inefficiency | Team/Organization | Ratio of merged PRs to total closed PRs (cited from Zhou et al.) [32, 33] | Yes [32, 34] |
| **Ratio of Duplicate PRs** | Quality / Inefficiency | Team/Organization | Ratio of duplicate PRs to total closed PRs (cited from Zhou et al.) [32, 33] | Yes [32, 34] |
| **Presence of Hard Forks** | Collaboration / Inefficiency | Team/Organization | Binary indicator variable denoting presence of hard forks (cited from Zhou et al.) [32, 35] | Yes [32, 34] |
| **Fork Entropy** | Collaboration / Activity | Team/Organization | Average pairwise distance between file modification vectors of forks within a time window (cited from Wang et al.) [35, 36] | Yes [36, 37] |
| **Control Variables (Project Age, NumForks, NumIssues, NumPrs, NumFiles, NumCore, NumExt)** | Activity / Context / Collaboration | Team/Organization / Individual | Aggregated monthly repository metadata and active developer counts via GitHub API [31, 38] | Yes [27, 37, 39] |

---

## Frameworks e Metricas

### Frameworks Referenciados
- **SPACE Framework**: APPLIED — Cited (Forsgren et al., 2021) and directly used to select project productivity dimensions: Performance (New Bugs), Activity (New Commits), and Efficiency & Flow (Issue Resolution Time) [6, 7, 17]. (Satisfaction & Well-being and Communication & Collaboration were excluded with explicit domain rationale) [31].
- **Developer Experience (DevEx)**: REFERENCED — Cited in background literature on developer experience concepts [20, 40].

### Frameworks Propostos
- **Convergence Entropy Model**: PROPOSED & APPLIED — An information-theoretic measurement framework based on Jensen-Shannon Divergence (JSD) that quantifies continuous integration effectiveness in distributed fork practices by measuring how closely original commit distributions match merged commit distributions across forks, scaled by the commit merge ratio [13-15, 24].

---

## Fatores que Influenciam Produtividade

### Fatores Positivos
| Fator | Categoria |
|-------|-----------|
| **Alta Convergence Entropy (\\(H_{conv}\\))** | Technical/Process — Significantly reduces new bugs across all projects [18, 41, 42], increases new commits in community projects [20, 43], and accelerates issue resolution in enterprise projects [22, 44]. |
| **Maturidade do Projeto (Project Age) com alta \\(H_{conv}\\) em projetos comunitarios** | Process/Organizational — Accelerates bug reduction over time [42, 45] and boosts overall commit volume [43, 46]. |
| **Supervisao Corporativa / Processos Estruturados em projetos de empresa com muitos forks** | Process/Organizational — Mitigates complexity and significantly shortens issue resolution duration in high-fork corporate environments [44, 47]. |
| **Volume de Pull Requests (\\(NumPrs\\)) combinado com \\(H_{conv}\\)** | Process/Technical — Enhances bug-reducing efficacy [29, 48] and accelerates commit velocity [46, 49]. |
| **Participacao de Colaboradores Externos (\\(NumExt\\)) em projetos corporativos** | Human/Organizational — Strengthens bug reduction [42, 48] and accelerates issue resolution efficiency [44, 50]. |

### Fatores Negativos
| Fator | Categoria |
|-------|-----------|
| **Baixa Convergence Entropy (\\(H_{conv}\\))** | Technical/Process — Leads to fragmented development, duplicate effort, unmerged/rejected contributions, and community drift [51, 52]. |
| **Acumulo de Issues e Arquivos (\\(NumIssues\\), \\(NumFiles\\))** | Process/Technical — Weakens the bug-reducing impact of convergence entropy [42, 48] and increases issue resolution times due to coordination overhead [44, 53]. |
| **Burocracia e Roadmaps Rigidos em Projetos Corporativos** | Organizational/Process — High convergence entropy in enterprise projects correlates with suppressed commit volume (\\(New Commits\\)), as corporate maintainers selectively reject divergent external code [43, 54, 55]. |
| **Gargalos de Mantenedores em Projetos Comunitarios** | Human/Organizational — High convergence combined with expanding codebases/issues overloads volunteer core teams, prolonging issue resolution times [53, 55, 56]. |
| **Escalabilidade Descontrolada de Forks sem Integracao em Empresas** | Process/Technical — High fork counts combined with low convergence entropy increase bug risk and fix delays [27, 47]. |

---

## Papel da IA e Automacao

| Campo | Valor |
|-------|-------|
| **Usa IA/ML?** | **No** — The study employs econometric panel regression models (Random Effects Model) and information theory (Jensen-Shannon Divergence), not machine learning or AI algorithms [9, 13, 57]. |
| **Automacao de coleta?** | **Yes** — Automated data collection pipelines using GitHub REST API and GraphQL API to extract commit logs, fork activity, issue records, and event histories [8, 25]. |
| **Impacto de IA na produtividade?** | **Not specified** — The paper does not evaluate AI tools or AI-driven code generation impact [17, 25]. |

---

## Resultados Principais

- **RQ1 — Software Quality (New Bugs)**: Convergence entropy (\\(H_{conv}\\)) is significantly negatively correlated with new bugs (\\(\beta = -13.220, p < 0.001\\)) across all projects [41, 48]. In non-company projects, this bug-reducing association strengthens as projects mature (\\(\beta = -9.900, p < 0.001\\)) and with core developer involvement, but weakens under high issue and file backlogs [42, 45, 48]. In company projects, bug reduction strengthens with external contributors (\\(\beta = -5.685, p < 0.05\\)) but weakens when fork volume scales up (\\(\beta = 44.705, p < 0.001\\)) [42, 48].
- **RQ2 — Output Activity (New Commits)**: The correlation between \\(H_{conv}\\) and new commits diverges sharply based on project governance: positive and significant in non-company projects (\\(\beta = 198.257, p < 0.001\\)) but negative in company projects (\\(\beta = -39.967, p < 0.001\\)) [43, 46]. In non-company projects, positive correlation strengthens with project age (\\(\beta = 50.727, p < 0.05\\)), pull requests (\\(\beta = 52.763, p < 0.001\\)), and external contributors (\\(\beta = 23.331, p < 0.05\\)) [43, 46]. In company projects, negative correlation strengthens with project age (\\(\beta = -42.432, p < 0.001\\)) as strict alignment with corporate roadmaps suppresses divergent contributions [43, 46, 54].
- **RQ3 — Process Efficiency (Issue Resolution Time)**: \\(H_{conv}\\) exhibits contrasting associations with issue resolution time: positive in non-company projects (\\(\beta = 86.725, p < 0.001\\)), indicating coordination bottlenecks in volunteer communities, but negative in company projects (\\(\beta = -30.049, p < 0.01\\)), reflecting efficiency gains from centralized resources [44, 50, 53]. In high-fork company projects, high convergence entropy significantly reduces fix times (\\(\beta = -43.547, p < 0.05\\)) [47, 50].
- **Governance Context Matters**: Corporate projects prioritize internal roadmaps and selective quality control (causing commit suppression but faster fixes), whereas community-driven projects rely on inclusive integration to sustain volunteer participation and commit output [54-56].

---

## Desafios do Uso das Metricas

- **Contextual Misinterpretation**: Static metrics (such as raw fork counts or commit totals) are misleading; high fork activity without integration does not indicate health, and low commit volume in enterprise projects may reflect strict quality control rather than low output [51, 55, 58].
- **Coordination Bottlenecks**: High integration effort in community-driven projects with expanding codebases introduces severe coordination overhead, prolonging issue resolution times [53, 56].
- **Maintainer Overload in Corporate Review**: Rapid scaling of forks combined with strong convergence can overwhelm centralized corporate review pipelines, requiring selective rejection [27, 55].
- **Identification of Developer Roles**: GitHub does not publicly expose repository management privilege lists, requiring event-level permission tracking across 53 issue event types to differentiate core members from external contributors accurately [59, 60].

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

- **Tamanho da Amostra**: Restricted to 8 large-scale, highly active GitHub projects, which limits direct extrapolation to small, niche, or inactive OSS repositories [10, 61].
- **Foco Exclusivo em External Contributors**: Isolates fork activities from external developers, excluding direct branch commit workflows used by core team members with repository write access [62].
- **Complexidade Nao Observada de Issues**: Issue resolution duration may be influenced by unobserved issue complexity, though partially smoothed by monthly aggregation and controlling for project age [63].
- **Natureza Correlacional**: Panel regression models identify longitudinal correlations rather than definitive causal links [64, 65].
- **Dependencia de Dados Ativos do GitHub**: Relies on active GitHub REST/GraphQL API data, excluding deleted repositories, removed commits, and automated bot accounts [25].

---

## Contribuicao Principal

The paper introduces **Convergence Entropy** (\\(H_{conv}\\)), a novel information-theoretic metric grounded in Jensen-Shannon Divergence that quantifies continuous integration effectiveness in distributed fork-and-pull software development [13-15]. Through longitudinal panel regression across 8 major GitHub projects, the study demonstrates that higher convergence entropy consistently improves software quality by reducing bugs [41, 42], while its effects on development output (commits) and process efficiency (issue resolution time) diverge fundamentally between community-driven and corporate-backed ecosystems [43, 44, 55]. This work provides critical theoretical insights into crowd collaboration dynamics and actionable governance recommendations for managing open-source sustainability [66-68].

---

*Extraido via NotebookLM em October 2026 para MLR: Software Developer Metrics in Practice*


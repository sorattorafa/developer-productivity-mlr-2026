# P2104 — Human-AI experience in integrated development environments: a systematic literature review

**Decisao: INCLUIDO | Qualidade: 5/5**

---

## Dados Bibliograficos

| Campo | Valor |
|-------|-------|
| **ID** | P2104 [1] |
| **Autores** | Agnia Sergeyuk, Ilya Zakharov, Ekaterina Koshchenko, Maliheh Izadi [1, 2] |
| **Ano** | 2025 [3, 4] |
| **Venue** | Springer / Manuscript (JetBrains Research & Delft University of Technology) [2, 5] |
| **DOI** | 10.5281/zenodo.16877797 (Supplementary Dataset) [4] |
| **Tipo** | Journal article / Manuscript (Systematic Literature Review) [1, 6, 7] |
| **Metodo** | Systematic Literature Review (SLR) following PRISMA guidelines [6, 8] |
| **Amostra** | 90 included studies (selected from 257 identified / 223 screened) [6, 9, 10] |
| **Contexto** | Mixed (71 professional, 19 educational) [11] |
| **Modo de trabalho** | Not specified (encompasses remote, hybrid, and lab/on-site study environments across reviewed literature) [12-14] |
| **Metodologia** | Waterfall model used for SDLC stage categorization; Agile/DevOps in individual primary studies [8, 15] |

---

## Objetivo

The primary objective of this systematic literature review is to synthesize existing research on Human-AI Experience in Integrated Development Environments (in-IDE HAX), categorizing 90 empirical studies across Impact, Design, and Quality dimensions, identifying key trends and gaps in current software development practices, and defining a structured research agenda to guide future academic and industrial efforts [1, 9, 16].

---

## Questoes de Pesquisa

- **RQ1**: What aspects of software development related to HAX within IDEs have been extensively studied, and which areas remain underexplored? [8]
- **RQ2**: What are the key findings in the field of HAX in IDEs? [17]
- **RQ3**: What are the potential directions for future research and development in the field of HAX in IDEs? [17]

---

## Metricas e Instrumentos de Avaliacao

| Metrica | Categoria | Nivel | Como Coletada | Validada |
|---------|-----------|-------|---------------|----------|
| Task Completion Time / Speed | Productivity | Individual | Timed experiments, IDE telemetry, and user study task logs [13, 18, 19] | Yes [18, 20] |
| Suggestion Acceptance Rate | Activity / Productivity | Individual | Telemetry logs and IDE action tracking [19, 21, 22] | Yes [20, 21] |
| Code Verification & Repair Effort | Productivity / Activity | Individual | User study logs, eye tracking, and IDE interaction logs [19, 21, 22] | Yes [20, 21] |
| Code Correctness / Functional Accuracy | Quality | Individual | Automated test suites, benchmarks, unit tests, and static analysis [23-25] | Yes [20, 23] |
| Security Vulnerability Rate | Quality | Individual | Static security analysis tools and vulnerability scanners [23, 24] | Yes [20, 24] |
| Code Readability & Maintainability | Quality | Individual | Eye-tracking visual inspection, subjective developer ratings, and code metrics [25, 26] | Partial [20, 26] |
| Perceived Mental Workload | DevEx / Satisfaction | Individual | Standardized subjective workload surveys (e.g., NASA-TLX) [27, 28] | Yes [20, 27] |
| Trust & Reliance (Over/Under-reliance) | DevEx / Satisfaction | Individual | Behavioral logs, post-task questionnaires, and interviews [29-31] | Yes [20, 29] |
| Developer Self-Efficacy | DevEx | Individual | Pre- and post-task self-efficacy survey instruments [27, 28] | Yes [20, 27] |

---

## Frameworks e Metricas

### Frameworks Referenciados
- **PRISMA (Preferred Reporting Items for Systematic Reviews and Meta-Analyses)**: APPLIED — Used as the formal methodology to conduct and report the systematic literature review [6, 8].
- **Waterfall Model**: APPLIED — Used as an operational framework to delineate and categorize stages of the Software Development Lifecycle (SDLC) [8].
- **in-IDE HAX Taxonomy (Sergeyuk et al., 2024)**: APPLIED — Used as the primary classification taxonomy spanning Impact, Design, and Quality dimensions [6, 32].
- **DevEx Framework**: REFERENCED — Discussed across primary studies in relation to developer experience, cognitive workload, and satisfaction [19, 27, 33].

### Frameworks Propostos
The paper refines and proposes a comprehensive 3-dimensional taxonomy for in-IDE HAX research comprising **Impact** (effects on workflows, productivity, and trust), **Design** (autocompletion vs. conversational modes, prompt engineering, context awareness, explainability, and user control), and **Quality** (correctness, maintainability, readability, and security) [32-34]. Additionally, it introduces a structured research agenda mapping 17 topics to 10 methodology types [35, 36].

---

## Fatores que Influenciam Produtividade

### Fatores Positivos
| Fator | Categoria |
|-------|-----------|
| Reduced context switching by remaining within the IDE workspace [19, 37] | Technical |
| Offloading boilerplate and repetitive code generation to AI [19, 37] | Process |
| High developer expertise and domain familiarity (higher productivity ceiling) [18, 33] | Human |
| Rich project context integration into LLM prompts [38, 39] | Technical |
| Structured prompting strategies and explicit prompt engineering training [27, 39, 40] | Human / Process |
| In-IDE explainability, uncertainty highlighting, and live runtime feedback [21, 38, 39] | Technical |

### Fatores Negativos
| Fator | Categoria |
|-------|-----------|
| High verification and code repair overhead (taking up to 50% of developer time) [19, 21] | Process |
| Subtle logical bugs and insecure code patterns in AI suggestions [21, 23, 24] | Technical |
| Automation bias and over-reliance leading to uncritical acceptance in novices [21, 27, 30] | Human |
| Under-reliance and rejection of valid code by professionals due to lack of rationale [19, 30] | Human / Technical |
| Complex, open-ended, or proprietary codebases lacking contextual AI support [19, 37] | Organizational / Technical |
| Misleading AI suggestions causing cognitive drift away from correct solutions [19, 27] | Human / Technical |

---

## Papel da IA e Automacao

| Campo | Valor |
|-------|-------|
| Usa IA/ML? | Yes — Synthesizes 90 studies on AI/ML coding assistants integrated into IDEs (e.g., GitHub Copilot, Cursor, IntelliCode, PairBuddy, Prompt Sapper) [1, 28, 41]. |
| Automacao de coleta? | Yes — Data extraction was performed manually supported by the AI tool Elicit to formulate study summaries, with 100% human review and verification [42]. |
| Impacto de IA na produtividade? | Positive for routine/boilerplate tasks (e.g., up to 55.8% faster implementation of HTTP servers, 26–35% gain in complex tasks), but offset by verification costs (up to 50% time spent inspecting/repairing) and risks of over-reliance or security defects [18, 21, 24, 37]. |

---

## Resultados Principais

- **Heavy Concentration on Professional Contexts & Implementation**: 71 of 90 reviewed studies target professional settings, while 19 focus on educational contexts [11]. Research heavily emphasizes the code implementation stage, leaving requirements, testing, and deployment understudied [33, 43].
- **Over-reliance on GitHub Copilot**: 36 out of 90 studies specifically examine GitHub Copilot, posing a risk of overgeneralizing findings to other AI architectures or tools [28, 43].
- **Productivity vs. Verification Trade-off**: While AI speeds up routine authoring (up to 55.8% faster in well-defined tasks) [18], developers spend up to 50% of their time inspecting suggestions, refining prompts, and repairing generated code [19, 21].
- **Divergent Impact by Expertise**: Novices complete tasks faster and report lower workload but suffer from automation bias and over-trust [27, 30]. Experienced developers gain higher productivity ceilings but may under-rely on AI when output rationale is missing [18, 19, 30].
- **Core Design Principles**: Studies converge on three design imperatives: rich Context Awareness, Explainability & Transparency (e.g., highlighting uncertain tokens), and User Control & Adaptability (blending inline autocompletion with chat) [38, 39, 44].
- **Security & Quality Risks**: Up to 36% of security vulnerabilities in AI-assisted code stem from model suggestions replicating unsafe training patterns [24, 25]. Generated code also exhibits readability and maintainability issues [25, 26].
- **Underpowered User Sample Sizes**: The median sample size across experimental user studies in the literature is 17 participants, demonstrating a need for higher-powered, longitudinal evaluations [14, 45, 46].

---

## Desafios do Uso das Metricas

- **Flaw of Acceptance Rate as a Quality Metric**: High suggestion acceptance rate does not guarantee high productivity or code quality, as accepted code often contains subtle flaws or requires downstream editing [19, 21, 22].
- **Inadequacy of Duration-Only Metrics**: Measuring task completion time alone fails to capture verification overhead, code maintainability trade-offs, and mental workload [19, 21, 22].
- **Automation Bias**: Novices accepting incorrect AI suggestions without visual inspection or testing [21, 30].
- **Trust Calibration Anti-patterns**: Over-reliance among beginners leading to skill atrophy, alongside under-reliance among experts who reject valid suggestions lacking transparent rationale [19, 30].
- **Unspecified Context & SDLC Reporting**: 46 of 71 professional studies and 13 of 16 educational studies omit the target SDLC stage, hindering cross-study metric comparison [15, 47, 48].

---

## Avaliacao de Qualidade Metodologica

| Criterio | Pontuacao (0-2) |
|----------|----------------|
| Objetivo claramente definido | 2 [20] |
| Metodologia adequada ao objetivo | 2 [20] |
| Amostra/contexto descrito adequadamente | 2 [20] |
| Ameacas a validade discutidas | 2 [20, 49-51] |
| Resultados com evidencia suficiente | 2 [20] |
| Contribuicao clara para pratica ou teoria | 2 [20] |
| **TOTAL** | **12/12** [20, 52] |

---

## Limitacoes

- **Sampling & Terminology Bias**: Risk of omitting relevant studies due to inconsistent terminology across digital library indices, mitigated through backward snowballing and expert additions [49, 53].
- **Tool Homogeneity**: Over-representation of GitHub Copilot (36/90 studies), limiting generalizability to alternative interaction paradigms or open-source assistants [28, 43].
- **Temporal Window Constraints**: Inclusion restricted to studies published or preprinted between January 2022 and November 2024 [3, 50, 54].
- **Exclusion of Non-Adopters**: Lack of empirical coverage on developers who choose not to use AI tools or have abandoned them [33, 43, 55].
- **Inclusion of Non-Peer-Reviewed ArXiv Preprints**: Included to capture rapid domain advancements and null/negative findings, though lacking formal archival peer review [50, 56].

---

## Contribuicao Principal

This paper presents the first systematic literature review focused specifically on Human-AI Experience in Integrated Development Environments (in-IDE HAX) [57]. By analyzing 90 empirical studies using the PRISMA framework, it establishes a unified taxonomy spanning Impact, Design, and Quality dimensions, synthesizes empirical findings regarding developer productivity, verification costs, and code security, and defines a structured future research agenda mapping 17 topics to 10 methodology types to guide subsequent research and tool development [1, 6, 35, 43].

---

*Extraido via NotebookLM em October 2026 para MLR: Software Developer Metrics in Practice*

💡 Would you like me to generate a comparative analysis, slide outline, or summary report based on this review?
# P2085 — The transformative influence of llms on software development & developer productivity

**Decisao: INCLUIDO | Qualidade: 4/5**

---

## Dados Bibliograficos

| Campo | Valor |
|-------|-------|
| **ID** | P2085 |
| **Autores** | Sajed Jalil [1] |
| **Ano** | 2025 [1] |
| **Venue** | International Conference on Artificial Intelligence, Computer, Data Sciences and Applications (ACDSA 2025) [1] |
| **DOI** | Not specified in the paper |
| **Tipo** | Conference paper [1] |
| **Metodo** | Literature review / Systematic survey (Thematic analysis with open coding) [2, 3] |
| **Amostra** | 23 selected publications (20 scholarly articles and 3 developer surveys/blogs/articles reviewing tools like GitHub Copilot, ChatGPT, Tabnine, Cursor) [4-6] |
| **Contexto** | Software Engineering (SE) and Human-Computer Interaction (HCI) — spanning Industry, Academic, and Open-Source Software (OSS) contexts [4, 5, 7, 8] |
| **Modo de trabalho** | Not specified (covers individual, small, large, and multinational co-located and distributed developer team settings) [9-11] |
| **Metodologia** | Not specified (surveys software engineering activities broadly across SDLC stages) [12] |

---

## Objetivo

The main objective of this paper is to present a systematic literature review on the transformative impact of Large Language Models (LLMs) and AI Pair Programming assistants on software development practices and developer productivity [1, 2, 7]. The author aims to analyze evolutionary trajectories in software engineering driven by AI tool adoption, introduce a novel taxonomy classifying influencing factors across 11 major categories and 53 subcategories, evaluate the practical benefits and usability drawbacks experienced by developers, and outline 12 key open problems to guide future research in SE and HCI [2, 6, 7, 13].

---

## Questoes de Pesquisa

- **RQ1**: How have software engineering practices evolved in response to the adoption of AI pair programming tools? [7]
- **RQ2**: What factors steer and influence these evolutionary trends across Software Engineering, Machine Learning, and HCI? [7, 14]
- **RQ3**: What aspects of AI pair programming are working effectively, and what usability or technical challenges remain? [7]
- **RQ4**: What are the existing open problems that require future investigation in the domain of AI-assisted software development? [7, 13]

---

## Metricas e Instrumentos de Avaliacao

| Metrica | Categoria | Nivel | Como Coletada | Validada |
|---------|-----------|-------|---------------|----------|
| Volume of code added and omitted | Productivity | Individual | Mineração de repositório / estática de código [15, 16] | Yes [15] |
| Time to completion & time to success | DevEx | Individual | Medição de tempo de execução de tarefas em estudos de usuário [17, 18] | Yes [17] |
| Code quality, precision & complexity | Quality | Individual | Análise estática, benchmarks (ex: HumanEval) e execuções de testes [12, 19-21] | Yes [12, 19] |
| Compilation error rate | Quality | Individual | Execução de compilador em IDE e logs de build [19, 22, 23] | Yes [19] |
| Usability perception & developer sentiment | Satisfaction | Individual | Questionários de pesquisa, entrevistas e codificação aberta [3, 17, 24, 25] | Partial [25, 26] |

---

## Frameworks e Metricas

### Frameworks Referenciados
- **SPACE / DORA / DevEx / GQM / HEART / OKR**: None of these standard software engineering productivity frameworks are explicitly referenced or applied in the paper.
- **Software Development Life Cycle (SDLC)**: REFERENCED — used as a structural framework to evaluate AI assistance across requirement analysis, architectural design, code generation, testing, code review, and maintenance [12, 27].
- **Thematic Analysis & Open Coding**: APPLIED — used as the qualitative methodology to analyze literature and derive the classification taxonomy [3, 28].

### Frameworks Propostos
- **11-Category & 53-Subcategory Taxonomy**: The paper proposes a novel taxonomy to classify factors influencing software development when using AI tools, spanning Source of Assistance, SDLC Assistance, Scope, Domain, Knowledge Level, Collaboration, Mental Models, Learning, Benefits, Concerns, and Cognitive Factors [6, 24, 27].

---

## Fatores que Influenciam Produtividade

### Fatores Positivos
| Fator | Categoria |
|-------|-----------|
| Rapid synthesis of source code, unit tests, and boilerplate templates [23, 29, 30] | Technical |
| Accelerated learning of new programming languages and onboarding [31, 32] | Human |
| Enhanced discoverability of bugs, edge cases, and code problem locations [16, 33] | Technical |
| Reduced time to task completion and boosted developer efficiency [16, 18] | Process |
| Assistance in requirement analysis and user story refinement [9, 12] | Process |
| Preservation and management of legacy codebases [9, 19] | Organizational |

### Fatores Negativos
| Fator | Categoria |
|-------|-----------|
| Increased cognitive load and context-switching distractions [21, 34, 35] | Human |
| Non-deterministic outputs generating varying code for identical prompts [36-38] | Technical |
| High compilation error rates at class, module, and project levels [22, 23] | Technical |
| Limited context window leading to local-only method focus [17, 22, 36] | Technical |
| Security risks, data privacy leaks, and secret key exposures [15, 36, 39] | Organizational |
| Potential open-source software license violations [37, 40] | Process |
| Mistrust, hallucinations, and unverified generated content [20, 36, 41] | Human |

---

## Papel da IA e Automacao

| Campo | Valor |
|-------|-------|
| Usa IA/ML? | Yes — The central focus of the paper is the evaluation of Generative AI and Large Language Models (LLMs) used as AI Pair Programming Assistants (e.g., GitHub Copilot, ChatGPT, Tabnine, Cursor, Devin) [1, 28, 42, 43]. |
| Automacao de coleta? | Yes — Surveys studies that collect data through automated IDE telemetry, static code analysis, and standardized benchmark datasets like HumanEval [4, 6, 44]. |
| Impacto de IA na produtividade? | Significant positive impact on developer coding speed and task efficiency, though offset by usability challenges such as non-determinism, context limitations, and cognitive load [2, 16, 18, 21]. |

---

## Resultados Principais

- **Taxonomy Creation**: Developed a novel classification scheme containing **11 major categories and 53 subcategories** to organize factors steering AI-assisted software engineering [6, 24, 27].
- **Literature Corpus**: Systematically reviewed **23 selected publications** (20 conference/journal papers and 3 developer surveys/blogs/articles) published between 2015 and 2025 [4-6].
- **User Study Scale**: Empirical studies in the surveyed literature featured participant sample sizes ranging from **15 to 2,047 developers** (e.g., 2,047 in CACM 2022 [40]; 410 in ICSE 2024 [17]; 61 in ICSE 2023 [44]).
- **Model Evolution Scale**: Highlights the growth from early ML models like Code2vec (trained on **12 million methods** from GitHub) to massive LLMs with estimated **trillions of parameters** (e.g., ChatGPT, Claude, Perplexity) [45].
- **Scope Limitations**: Code generation tools perform best at inline and **method levels**, but exhibit the highest frequency of compilation errors at **class, module, and project levels** due to context window limits [22, 23, 44].
- **Usability Gap**: Observational user studies are overwhelmingly small-scale (**15 to 30 participants**), frequently relying on graduate students, which limits generalizability to professional industry settings [26].
- **12 Open Problems**: Identified **12 open research challenges**, including non-determinism, accessibility for non-expert developers, bias mitigation, AI system testing, content verification, and training data quality [13, 26, 38, 41, 46-48].

---

## Desafios do Uso das Metricas

- **Lack of Universal Quality Standards**: No standardized framework exists to measure the quality of software artifacts generated by AI pair programmers [20].
- **Oversight of Cognitive Metrics**: Performance and productivity measurements frequently ignore cognitive burden and context-switching overhead [21].
- **Metric Distortion**: Using raw volume of code added or omitted as a proxy for productivity can disguise code quality degradation and increased maintenance overhead [15, 16, 20].
- **Self-Reporting Bias**: Reliance on developer survey responses introduces subjective bias and self-reporting inaccuracies [26].
- **Benchmark Inadequacy**: Standard benchmark datasets (e.g., HumanEval) only evaluate isolated, small-scale coding tasks and fail to capture complex, multi-turn project-level developer workflows [4, 41].

---

## Avaliacao de Qualidade Metodologica

| Criterio | Pontuacao (0-2) |
|----------|----------------|
| Objetivo claramente definido | 2 |
| Metodologia adequada ao objetivo | 2 |
| Amostra/contexto descrito adequadamente | 1 |
| Ameacas a validade discutidas | 1 |
| Resultados com evidencia suficiente | 2 |
| Contribuicao clara para pratica ou teoria | 2 |
| **TOTAL** | **10/12** |

---

## Limitacoes

- **Single-Author Review**: The literature review was conducted by a single author, restricting the total volume of papers that could be comprehensively synthesized [3].
- **Rapid Technological Obsolescence**: The rapid evolution of commercial LLMs means specific tool findings may become quickly outdated [1, 42, 45].
- **Participant Pool Bias**: Many surveyed empirical studies rely on small observational groups (**15 to 30 participants**), predominantly composed of graduate students rather than experienced industry professionals [26].
- **Task Scale Constraints**: Existing empirical evaluations and benchmarks focus primarily on small, isolated tasks rather than large-scale, repository-wide software development [23, 41].

---

## Contribuicao Principal

The primary contribution of this paper is the proposal of a novel 11-category, 53-subcategory taxonomy that systematically organizes the influencing factors, SDLC applications, and usability challenges of Large Language Models (LLMs) and AI Pair Programmers in software development [6, 7, 24, 27]. By synthesizing findings from 23 key publications and industry surveys, the paper highlights the trade-offs between productivity gains and critical issues like non-determinism, cognitive load, and data privacy, while outlining 12 distinct open problems to structure future empirical research in software engineering and HCI [2, 7, 13, 20, 21, 39].

---

*Extraido via NotebookLM em October 2026 para MLR: Software Developer Metrics in Practice*
# P2094 — A dive into the state of parallel application development in high-performance computing

**Decisao: INCLUIDO | Qualidade: 5/5**

---

## Dados Bibliograficos

| Campo | Valor |
|-------|-------|
| **ID** | P2094 [1, 2] |
| **Autores** | Gabriella Andrade, Dalvan Griebler, Rodrigo Santos, Luiz Gustavo Fernandes [1, 3] |
| **Ano** | 2026 / 2027 [1] |
| **Venue** | Information and Software Technology (ScienceDirect) [1] |
| **DOI** | https://doi.org/10.1016/j.infsof.2026.108327 [1] |
| **Tipo** | Journal article [1] |
| **Metodo** | Mixed methods (Online Survey with 131 participants, quantitative statistical Chi-Square testing, and qualitative Grounded Theory open and axial coding) [1, 4, 5] |
| **Amostra** | 131 parallel application developers from 26 countries (89 PhD, 35 Master's degree; 84 self-rated Experts, 41 Intermediate; 77 with >10 years of experience) [1, 6, 7] |
| **Contexto** | Mixed (103 participants in Universities, 21 in Research Centers such as BSC, Argonne, LNCC, LBNL, and 7 in Industry companies including Google, HPE, Intel, Nvidia, Pagonxt, SERPRO) [6] |
| **Modo de trabalho** | Not specified [1, 6] |
| **Metodologia** | Not specified (Focuses on parallel programming interfaces and models rather than general agile or waterfall software processes) [8, 9] |

---

## Objetivo

This study aims to identify the key factors that limit developer productivity in parallel application development, evaluate how different parallel programming interfaces (PPIs) support novice versus experienced programmers, and explore potential strategies, tools, and educational practices to enhance parallel software development productivity in High-Performance Computing (HPC) [1, 2].

---

## Questoes de Pesquisa

- **RQ1**: What factors affect productivity when coding parallel applications? [2]
- **RQ2**: What can be done to increase the productivity of parallel application developers? [2]

---

## Metricas e Instrumentos de Avaliacao

| Metrica | Categoria | Nivel | Como Coletada | Validada |
|---------|-----------|-------|---------------|----------|
| **Lines of Code (LOC / SLOC)** | Productivity / Activity | Individual / Team | Static code measurement / source code analysis [8, 10] | Partial (Established SE metric, but cited as lacking parallelism sensitivity) [8, 11] |
| **Halstead Complexity Metrics** | Productivity / Quality | Individual | Static source code operator and operand analysis [8] | Partial (Traditional SE metric with noted limitations for parallel code) [8] |
| **COCOMO / COCOMO II** | Productivity / Delivery | Organization / Team | Algorithmic effort estimation based on project cost drivers [8, 12] | Partial (Conceptual extension proposed for HPC, but not practical) [8, 12] |
| **Usability / Efficiency (ISO 9241-11)** | DevEx / Productivity | Individual | Evaluates human effort, project expenditures, and resource utilization relative to outcomes [8] | Yes (Standardized ISO metric framework) [8] |
| **Development Effort / Time** | Productivity | Individual / Team | Controlled programming experiments (time to complete tasks) and developer self-reported estimates [8, 13, 14] | Yes [8, 13] |
| **Danis et al. Workflow Complexity** | DevEx / Productivity | Individual | Spreadsheet tracking step counts, context changes, and working memory load per task [12, 13] | Partial [12, 13] |

---

## Frameworks e Metricas

### Frameworks Referenciados
- **ISO 9241-11**: REFERENCED (cited to define usability, efficiency, and productivity indicators based on human effort and resource utilization) [8].
- **COCOMO II**: REFERENCED (discussed as a software effort estimation model conceptually adapted for HPC) [8, 12].
- **DORA, SPACE, DevEx, HEART, OKR**: Not mentioned in the paper [8, 12, 13].

### Frameworks Propostos
- **Conceptual Diagram of Productivity Factors in Parallel Programming Applications (Fig. 14)**: The authors proposed a conceptual model synthesized via Grounded Theory coding [3, 10, 12]. It organizes productivity determinants into Developer Factors (experience, knowledge), PPI Factors (abstraction, usability, syntax), Enabling Factors (tools, documentation, education, patterns), Barriers (debugging, complexity, sequential refactoring, architectural mapping), and Productivity Outcomes [3, 10].

---

## Fatores que Influenciam Produtividade

### Fatores Positivos
| Fator | Categoria |
|-------|-----------|
| **High-level PPI abstractions (pragmas, directives, pattern skeletons, and templates)** | Technical [8, 15, 16] |
| **Incremental parallelism via OpenMP pragmas for novice developers** | Technical [16] |
| **Comprehensive PPI documentation and online usage examples** | Process / Technical [15, 17, 18] |
| **Profiling tools with actionable output explanations and bottleneck identification** | Technical [17-19] |
| **Development support tools (automated data partitioning, workload balancing, dependency visualization)** | Technical [19] |
| **Early education in parallel programming (introducing concepts at the start of undergraduate programs)** | Human / Organizational [17, 18] |
| **Hands-on training, hackathons, and industry/academic internships** | Human / Organizational [17, 18] |
| **Standardized and cross-platform / portable programming interfaces** | Technical [15, 16] |

### Fatores Negativos
| Fator | Categoria |
|-------|-----------|
| **Debugging and testing are harder and time-consuming (39.7%)** | Technical / Process [20, 21] |
| **High complexity of parallel models and low-level details (35.1%)** | Technical [20, 21] |
| **PPIs are not user-friendly (16.8%)** | Technical [15, 21] |
| **Requires extensive development effort (13.7%)** | Human / Process [15, 21] |
| **Requires correct mapping to target parallel architecture (13.7%)** | Technical [15, 21] |
| **Difficulty converting sequential code to parallel code / refactoring (10.7%)** | Technical / Process [20, 21] |
| **Difficulty improving performance due to lack of PPI/hardware knowledge (10.7%)** | Technical / Human [15, 21] |
| **Degree of asynchronism (7.6%)** | Technical [21] |
| **Difficulty ensuring code portability across architectures (6.9%)** | Technical [20, 21] |
| **Challenging code maintenance (6.1%)** | Process / Technical [20, 21] |
| **Difficulty choosing appropriate parallel programming model (6.1%)** | Process / Technical [15, 21] |
| **Lack of scalability (5.3%)** | Technical [20, 21] |
| **Installation issues (4.6%)** | Process / Technical [15, 21] |
| **Increases number of lines of code (3.1%)** | Technical [20, 21] |
| **Lack of flexibility (3.1%)** | Technical [20, 21] |
| **Need to test each routine individually on accelerator/GPU (1.5%)** | Process / Technical [15, 21] |
| **Lack of documentation for PPIs, especially open-source libraries** | Process / Technical [15] |
| **Late introduction of parallel programming in university curricula (end of degree)** | Organizational / Human [18, 22] |

---

## Papel da IA e Automacao

| Campo | Valor |
|-------|-------|
| **Usa IA/ML?** | No (The study itself uses standard statistical tests and qualitative Grounded Theory coding; Artificial Intelligence is noted as an application domain by 1% of participants, and ML effort estimation models are proposed for future research) [3, 4, 23]. |
| **Automacao de coleta?** | Partial (Survey responses were collected automatically via Google Forms, but qualitative analysis required manual Grounded Theory open and axial coding in ATLAS.ti) [4, 14, 24]. |
| **Impacto de IA na produtividade?** | Not evaluated directly (The paper notes CUDA and GPU parallelization are essential for training deep learning and AI models, but does not measure AI coding assistants on parallel developer productivity) [23, 25]. |

---

## Resultados Principais

- **Participant Demographics**: 131 developers across 26 countries completed the survey (18.37% response rate from 713 invited) [6, 26]. 89 participants hold a PhD, 35 hold a Master's degree, 84 self-rate as experts, and 77 have >10 years of parallel computing experience [6, 7].
- **Parallelization Strategy**: 73% (96 participants) develop parallel applications by converting existing sequential code, while 62% implement parallelism from scratch [5]. Experienced developers (>10 years experience) significantly favor starting from scratch (71%, \\(p=0.010\\)) compared to beginners/intermediates (41%) [5, 27].
- **Dominant PPIs and Architectures**: OpenMP is the most widely used interface (100 participants / 76%), followed by MPI (92 / 70%) and CUDA (86 / 66%) [28]. Multi-core CPUs (122), GPUs (99), and Clusters (91) are the primary target architectures [28]. Chi-square tests confirm CUDA is significantly associated with GPUs (\\(p<0.001\\)) and MPI with Clusters (\\(p<0.001\\)), while OpenMP is used across all platforms [29].
- **Programming Languages**: C and C++ dominate parallel application development (71% / 93 participants each), followed by Python (32% / 42 participants) and Fortran (17% / 22 participants) [30]. C/C++ developers show statistically significant usage associations with OpenMP, MPI, CUDA, and OpenACC [30].
- **Top Productivity Obstacles**: Difficulties in debugging/testing (39.7%) and high programming complexity (35.1%) are the primary bottlenecks, driven by race conditions, profiler output interpretation, and hardware memory management [20, 21].
- **Recommended PPI for Beginners**: OpenMP is recommended by ~64% of respondents due to its simple pragma syntax, incremental parallelization capability, gentle learning curve, and multi-core CPU accessibility [16, 17].
- **Recommended PPI for Experts**: CUDA (34%) and MPI (34%) are the top recommendations for expert developers to maximize GPU and cluster hardware performance, despite steep learning curves and low-level memory/concurrency overhead [25, 31].

---

## Desafios do Uso das Metricas

- **Inadequacy of Traditional SE Metrics**: Standard software engineering coding metrics (LOC, Halstead, COCOMO II) fail to capture parallelism-specific factors such as thread synchronization, data decomposition, communication overhead, and target architecture hierarchies (e.g., GPU warp/grid management vs CPU multi-threading) [2, 8].
- **Unusable Conceptual Models**: Extensions of traditional models like COCOMO II for HPC remain purely conceptual and cannot be operationalized in real-world practice [12].
- **High Cost of Empirical Experiments**: Evaluating productivity through controlled student experiments is time-consuming, expensive, and difficult to scale with statistically representative samples of experienced parallel computing developers [8, 14].
- **Lack of Parallelism-Sensitive Metrics**: There is an absence of validated offline metrics tailored specifically to measure parallel programming effort and model abstractions [2, 8].

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

*Justificativa da Pontuacao*:
1. **Objetivo (2/2)**: The study explicitly specifies research goals (G1, G2, G3) via GQM and states research questions RQ1 and RQ2 clearly [2, 12].
2. **Metodologia (2/2)**: Combines descriptive statistics, Chi-Square independence tests (\\(p\\)-values provided), and Grounded Theory qualitative coding (open and axial coding via ATLAS.ti) [4, 5, 29].
3. **Amostra/contexto (2/2)**: Thorough demographic characterization covering 131 participants, 26 countries, education levels, affiliations, years of experience, self-rated expertise, application domains, languages, and architectures [6, 7, 23, 28].
4. **Ameacas a validade (2/2)**: Section 6 explicitly details internal, construct, external, and conclusion validity threats along with mitigation steps [22].
5. **Resultados (2/2)**: Provides frequency tables, statistical significance tests, qualitative ATLAS.ti diagrams, and participant direct quotes [5, 19-21, 29].
6. **Contribuicao (2/2)**: Synthesizes findings into a novel conceptual diagram of productivity factors, offers concrete guidelines for beginner vs expert PPI selection, and lays out an open benchmark dataset agenda for effort estimation models [3, 10].

---

## Limitacoes

- **Geographic Representation**: Most participants are located in the Americas (Brazil 41%, USA 9%) and Europe (Italy 10%, Spain 8%, Germany 5%), with no participants from Africa and minimal representation from Asia, limiting global generalization [6, 22].
- **Sample Coverage of Modern Architectures**: The sampled population shows a relative lack of hybrid and heterogeneous server architectures [22].
- **Unweighted Productivity Factors**: The study identifies factors qualitatively and ranks them by mention frequency, but does not measure the quantitative relative weight or impact of each factor on overall development effort [3, 21].
- **Subjectivity in Qualitative Coding**: Grounded Theory qualitative procedures involve human interpretation, though mitigated by multi-researcher cross-validation [4, 22].

---

## Contribuicao Principal

The primary contribution of this paper is a comprehensive empirical study based on a survey of 131 parallel application developers from 26 countries, combining quantitative statistical tests and Grounded Theory qualitative coding to map the state of parallel application development in HPC [1, 4, 5]. The paper classifies PPI adoption across experience levels and hardware targets, identifies debugging complexity and lack of developer knowledge as primary productivity barriers, evaluates OpenMP (for beginners) versus CUDA/MPI (for experts), and synthesizes these findings into a conceptual model of productivity factors to inform future programming tools, effort prediction models, and HPC educational curricula [3, 10, 17, 25].

---

*Extraido via NotebookLM em October 2026 para MLR: Software Developer Metrics in Practice*

---

💡 **Sugestao:** Gostaria que eu transformasse esta analise em um relatorio formatado em PDF ou em um conjunto de slides para apresentacao?
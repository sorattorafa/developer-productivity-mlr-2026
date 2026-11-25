# G083 — Implementation and Comparison of Code Complexity Metrics to Assess Developer Productivity

**Decisao: INCLUIDO | Qualidade GL: 5.5/6**

---

## Dados Bibliograficos

| Campo | Valor |
|-------|-------|
| **ID** | G083 |
| **Autor/Organizacao** | Christian Ispas (Technical University of Munich — TUM, School of Computation, Information and Technology) [1] |
| **Data** | November 17, 2025 [2] |
| **Tipo** | Academic Thesis (Bachelor's Thesis in Informatics) [1] |
| **URL** | https://github.com/Chrisman2003/code-complexity-metrics [3] |

---

## Resumo

This study presents a Bachelor's thesis conducted at the Technical University of Munich (TUM) focused on quantifying code complexity in modern GPU-based parallel programming frameworks using C++ codebases [1, 2]. While traditional code complexity metrics have existed since the 1970s, their specialized application to modern GPU parallel models remains sparse in scientific literature [4]. The core objective of the work is to evaluate inter-framework and inter-algorithmic code complexity by controlling for algorithm or framework implementations, mitigating confounding factors across diverse GPU models [5-7].

The author implements a CLI tool in Python that extracts five code complexity metrics: Source Lines of Code (SLOC), Cyclomatic Complexity, Nesting Depth Complexity, Cognitive Complexity, and Halstead Complexity [2, 8]. The tool utilizes regular expressions and Clang/LLVM front-end Control Flow Graphs (CFGs) for parsing C++ and GPU kernel source code, enriched with framework-specific keyword vocabularies [9-12]. The software architecture includes automated testing via Pytest and continuous integration (CI) via GitHub Actions, as well as a statistical analysis pipeline for generating comparative visual reports [2, 13-15].

Experimental evaluation across benchmark algorithms (Polyhedral Gravity Model, N-Body Simulation, Matrix Multiplication, and Vector Addition) reveals that CUDA consistently exhibits the highest Halstead difficulty and volume, reflecting a low abstraction level and rich GPU-specific constructs [2, 16, 17]. Graphics API frameworks like Vulkan exhibit extreme complexity for complex domain models like Polyhedral Gravity due to verbose namespace invocations (`vk::`), but revert to moderate/low complexity for simpler linear algebra operations [16-18]. High-level abstractions such as Kokkos maintain stable, low-volatility complexity in the middle range across all tested algorithms [16, 17].

---

## Frameworks Mencionados

* **DORA, SPACE, DevEx**: Not mentioned or discussed in the source material.
* **CUDA**: Discussed extensively [19]. Consistently exhibits the highest Halstead difficulty and volume across N-Body Simulation, Matrix Multiplication, and Vector Addition [16, 17]. Critiqued for high implementation difficulty and shifting low-level management onto developers, despite its historical dominance and performance [17, 20].
* **Kokkos**: Discussed and recommended for performance portability and maintainability due to its low volatility, consistently occupying a moderate middle-range complexity ranking across all benchmark algorithms [16, 17, 21].
* **Vulkan / OpenGL Vulkan**: Discussed [22]. Demonstrates extreme Halstead complexity (difficulty 643.53, volume 38,149.62) for the Polyhedral Gravity Model due to explicit memory management and `vk::` namespace prefixes, but shows low-to-middle complexity for simpler linear algebra tasks [16-18].
* **OpenCL**: Discussed [23]. Exhibits lower complexity in Polyhedral Gravity but higher relative complexity in N-Body Simulation, Matrix Multiplication, and Vector Addition [16, 24].
* **AdaptiveCPP (formerly hipSYCL)**: Discussed [25]. Consistently ranks in the middle pack of complexity across tested benchmark algorithms [16, 24].
* **OpenMP**: Discussed [26]. Shows low-to-moderate complexity across algorithms through declarative pragma directives (`#pragma omp`) [16, 24].
* **OpenACC**: Discussed [27]. Shows low complexity in Vector Addition and Polyhedral Gravity due to high-level directive abstractions (`#pragma acc`) [16, 24].
* **WebGPU**: Discussed [28]. Demonstrates relatively low Halstead complexity in the Polyhedral Gravity Model [16, 18].
* **Boost Compute**: Discussed [29]. Exhibits lower-to-middle complexity for N-Body Simulation, Matrix Multiplication, and Vector Addition [16, 24].
* **Metal**: Discussed [30]. Evaluated for Vector Addition, displaying moderate-to-high Halstead volume and difficulty [16, 24].
* **Thrust**: Discussed as a high-level C++ template library built on CUDA that abstracts parallel algorithms into high-level host functions [31].

---

## Metricas Mencionadas

* **Source Lines of Code (SLOC)**: Counts non-empty, non-comment, non-header source lines [32]. Intuitive but naive metric that ignores control flow and language verbosity, though strongly correlated with general developer effort and Halstead metrics [33, 34].
* **Cyclomatic Complexity (McCabe)**: Quantifies linearly independent control flow paths, computed either via Clang front-end Control Flow Graphs (\\(M = E - N + 2P\\)) or regex decision point counts (\\(M = D + 1\\)) [35-38]. Non-CFG regex parsing achieves identical results for deterministic code while running ~300x faster than Clang CFG traversal [39].
* **Nesting Depth Complexity**: Measures the maximum nesting level of control structures (`{ ... }`), serving as a structural bridge between Cyclomatic and Cognitive Complexity [40, 41].
* **Cognitive Complexity (SonarQube / Campbell)**: Measures developer mental effort by weighting control flow structures by their current nesting level [42, 43]. Alleviates Cyclomatic Complexity pitfalls by treating switch-case chains as a single increment (+1), ignoring default function paths, and counting consecutive boolean operator sequences as single increments [43-45].
* **Halstead Complexity Metrics**: Evaluates Program Vocabulary (\\(n = n_1 + n_2\\)), Program Length (\\(N = N_1 + N_2\\)), Program Volume (\\(V\\)), Program Difficulty (\\(D\\)), Program Effort (\\(E = D \times V\\)), and Estimated Time (\\(T\\)) based on unique and total operators (\\(n_1, N_1\\)) and operands (\\(n_2, N_2\\)) [46, 47]. Enriched with framework-specific keyword sets (e.g., `cudaMalloc`, `Kokkos::`, `vk::`) to isolate GPU-native complexity [11, 12, 48].
* **Halstead Density (Effort / SLOC)**: Meta-metric combining Halstead Effort per line of code to evaluate the concentration of operators and operands per line [49-51].
* **DORA, SPACE, DevEx, Churn, Commit Frequency, Maintainability Index**: Not mentioned or defined in this source.

---

## Insights para Praticantes

* **Evaluate Framework Trade-offs Beyond Performance**: Low-level frameworks like CUDA provide high execution performance but impose substantial code complexity (highest Halstead difficulty and volume), shifting memory allocation and synchronization overhead onto developers [17, 20].
* **Prefer Abstractions for Long-Term Maintainability**: Portability frameworks like Kokkos offer stable, low-volatility complexity across diverse algorithms, making them optimal choices when developer productivity and code maintainability are priorities [16, 17].
* **Contextualize Framework Complexity by Domain**: Framework complexity is highly sensitive to algorithmic structure; verbose graphics APIs (Vulkan) exhibit extreme complexity for intricate domain models (Polyhedral Gravity) but remain manageable for simple vector/matrix operations [17, 18].
* **Combine Control Flow and Halstead Perspectives**: Relying solely on SLOC or Cyclomatic Complexity fails to capture code density and cognitive load [50, 52]. Pairing Cognitive Complexity (nesting-weighted control flow) with Halstead Density (operators/operands per line) provides a holistic assessment of maintainability [50, 53].
* **Adopt Scalable CI/CD Static Analysis**: Regex-based static analysis produces identical Cyclomatic Complexity values to Clang Control Flow Graph (CFG) extraction for standard control flows while running over 300x faster, making non-CFG regex approaches far more viable for continuous integration pipelines [39].

---

## Avaliacao de Qualidade GL (Garousi et al.)

| Criterio | Pontuacao (0-1) | Justificativa |
|----------|----------------|---------------|
| Autoridade do autor/organizacao | 0.5 | Tese de Bacharelado por aluno da Technische Universität München (TUM), sob supervisao de professor e mestrando [1, 2]. |
| Descricao de metodologia | 1.0 | Metodologia detalhada de implementacao das metricas, analise estatica via regex/Clang, suite de testes e pipeline estatistico [8, 9, 14, 15]. |
| Data de publicacao | 1.0 | Data explicita de conclusao e apresentacao: 17 de novembro de 2025 [2]. |
| Objetividade (vies comercial) | 1.0 | Trabalho academico independente sem fins comerciais ou vies patrocinado [2]. |
| Referencias citadas | 1.0 | Ampla fundamentacao teorica citando 66 referencias academicas e documentacoes tecnicas oficiais [54]. |
| Contribuicao nova | 1.0 | Aplicacao inedita e comparativa de metricas de complexidade de codigo a frameworks de programacao paralela GPU [2, 4, 55]. |
| **TOTAL** | **5.5/6** | **Avaliacao Global de Qualidade de Literatura Cinzenta** |

---

*Extraido via NotebookLM em October 2026 para MLR: Software Developer Metrics in Practice*

💡 Would you like me to generate a comparative table summarizing the complexity metrics across all four benchmark algorithms (Polyhedral Gravity, N-Body, Matrix Multiplication, Vector Addition)?
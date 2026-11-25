# G094 — Advancing scientific productivity through better scientific software: Developer productivity and software sustainability report

**Decisao: INCLUIDO | Qualidade GL: 5.6/6**

---

## Dados Bibliograficos

| Campo | Valor |
|-------|-------|
| **ID** | G094 |
| **Autor/Organizacao** | IDEAS-ECP Team and Collaborators (U.S. Department of Energy / Exascale Computing Project) [1, 2] |
| **Data** | January 28, 2020 [1] |
| **Tipo** | Industry report / Technical report (Government white paper) [1] |
| **URL** | http://www.osti.gov/scitech/ [1] |

---

## Resumo

The report *Advancing Scientific Productivity through Better Scientific Software* addresses the critical challenges surrounding software developer productivity and software sustainability within extreme-scale Computational Science and Engineering (CSE) under the U.S. Department of Energy (DOE) Exascale Computing Project (ECP) [1, 3, 4]. As computer architectures undergo disruptive shifts toward heterogeneous multicore CPU/GPU nodes, scientific applications face severe bottlenecks in scaling, refactoring, and maintainability [3, 5]. Concurrently, scientific frontiers demand complex multiphysics and multiscale simulations requiring cross-team code integration [6, 7]. Consequently, developer productivity and software sustainability are identified as vital prerequisites for preserving the quality, trustworthiness, and development velocity of extreme-scale research [3, 8, 9].

To overcome these bottlenecks, the IDEAS-ECP project establishes four core synergistic strategies: (1) curating software engineering best practices tailored specifically to scientific software development [4, 10, 11], (2) incrementally upgrading team practices via the Productivity and Sustainability Improvement Planning (PSIP) workflow [10, 12, 13], (3) establishing software communities and Software Development Kits (SDKs) like xSDK to ensure library interoperability and shared community policies [12, 14-16], and (4) leading broad community outreach through the Better Scientific Software (BSSw.io) portal, BSSw Fellowships, webinars, and tutorials [12, 17-20]. Real-world case studies across ECP projects (such as EXAALT, ExaStar, and Exascale MPI) demonstrate how PSIP facilitates continuous integration, automated testing, code refactoring, and developer onboarding [21-23].

Finally, the report advocates for fundamental cultural change across the scientific computing ecosystem [4, 24, 25]. It emphasizes elevating computational transparency and reproducibility (e.g., through artifact badging and open research software) [26, 27], establishing recognized career paths for Research Software Engineers (RSEs) [28, 29], and securing explicit funding for *Research Software Science* to systematically study and improve scientific software practices [30-32].

---

## Frameworks Mencionados

*   **DORA / SPACE / DevEx**: Not explicitly mentioned in this report (commercial/industry DevOps frameworks are not addressed in this scientific computing source) [8, 33].
*   **PSIP (Productivity and Sustainability Improvement Planning)**: Discussed extensively and recommended as a lightweight, iterative process improvement framework specifically created for scientific software teams [10, 12, 13].
*   **Agile Methodologies (Scrum, Kanban)**: Discussed as lightweight structured management processes requiring domain-specific adaptation for scientific computing environments [33].
*   **Software Development Kits (SDKs) / xSDK Framework**: Discussed and recommended for organizing complementary software products, defining community software policies, and ensuring horizontal library interoperability [14-16].
*   **Community Infrastructure Frameworks (URSSI, SSI, Software Carpentry, ReSA, US-RSE)**: Mentioned as complementary external communities and institutional frameworks fostering research software sustainability [28, 34-36].

---

## Metricas Mencionadas

*   **Developer Productivity & Sustainability Metrics**: The report explicitly notes that general, actionable quantitative metrics for scientific software developer productivity have historically proven difficult to define [8, 37].
*   **PSIP Progress Scores (0–5 Scale)**: Qualitative and process-tracking metrics used in PSIP progress cards to measure maturity in continuous integration, testing coverage, refactoring, and developer onboarding [23, 38].
*   **Verification & Test Coverage Metrics**: Evaluating the extent of test coverage for internal code functionality (e.g., AMR functionality coverage in FLASH/ExaStar and Boost/CTest integration in EXAALT) [23, 38].
*   **Build & CI Regression Metrics**: Automated tracking of build stability and test pass/fail rates in continuous integration pipelines (e.g., Jenkins nightly builds) [23, 38].
*   **Community Engagement Metrics**: Outreach tracking metrics including webinar registrations (averaging 148 registrations and 46 ECP attendees per session) and website contribution counts [39, 40].
*   **Hardware/Performance Metrics**: Mentions historical hardware efficiency metrics such as FLOPS/Watt in background discussions [41].

---

## Insights para Praticantes

*   **Adopt Incremental Process Improvement**: Avoid imposing rigid industrial software engineering models; instead, adopt lightweight, iterative frameworks like PSIP that integrate directly into primary feature development without disrupting scientific output [13, 42, 43].
*   **Target Critical Technical Bottlenecks First**: Prioritize foundational practices that yield rapid, tangible payoff, such as continuous integration (CI) build pipelines, automated unit testing, standardized Git workflows, and structured onboarding documentation [23, 44, 45].
*   **Adopt Community Software Policies**: Align software development with standardized community policies (e.g., xSDK policies) for build tools (CMake/Autoconf), test suites, and MPI communicators to facilitate interoperability and cross-team integration [16, 46].
*   **Manage Technical Debt via Tech Refreshment**: Treat scientific software as a long-term research asset by systematically scheduling code refactoring and continuous technology refreshment [47, 48].
*   **Foster Culture and Career Pathways**: Encourage formal recognition of software contributions, participate in community hubs like BSSw.io, and support dedicated Research Software Engineer (RSE) roles [17, 28, 29].

---

## Avaliacao de Qualidade GL (Garousi et al.)

| Criterio | Pontuacao (0-1) |
|----------|----------------|
| Autoridade do autor/organizacao | 1.0 |
| Descricao de metodologia | 0.8 |
| Data de publicacao | 1.0 |
| Objetividade (vies comercial) | 1.0 |
| Referencias citadas | 1.0 |
| Contribuicao nova | 0.8 |
| **TOTAL** | **5.6/6** |

---

*Extraido via NotebookLM em October 2026 para MLR: Software Developer Metrics in Practice*

---

💡 Would you like to generate a comparative report or mind map comparing this ECP report's PSIP framework with other developer productivity sources in your collection?
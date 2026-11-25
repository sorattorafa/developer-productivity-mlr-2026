# G084 — How Effective are AI-powered Code Assistants in Enhancing Developer Productivity?

**Decisao: INCLUIDO | Qualidade GL: 5.5/6** [1-4]

---

## Dados Bibliograficos

| Campo | Valor |
|-------|-------|
| **ID** | G084 [1] |
| **Autor/Organizacao** | Thin Thu Thu Thaw / Jamk University of Applied Sciences [1] |
| **Data** | May 2025 [1] |
| **Tipo** | Academic thesis (Bachelor's thesis) [1] |
| **URL** | Not stated in source [1, 3] |

---

## Resumo

This empirical study evaluates the effectiveness of AI-powered code assistants—specifically GitHub Copilot, Tabnine, and Codeium—in enhancing software developer productivity across different experience levels and task complexities [2, 5]. Conducted as a Bachelor's thesis at Jamk University of Applied Sciences, the research addresses the empirical gap in understanding how AI coding tools impact developer workflows beyond anecdotal accounts or small-scale controlled experiments [1, 6]. Productivity is conceptualized as a multidimensional construct encompassing coding speed, accuracy, bug reduction, tool usability, cognitive offloading, situated learning, and developer satisfaction [2, 7, 8].

Using a mixed-methods research design, the author collected quantitative data from a structured survey of 100 software developers and qualitative insights from 10 semi-structured interviews [2, 4]. Statistical analysis in SPSS—including Cronbach's alpha reliability tests, Pearson correlation matrices, and multiple linear regression—revealed that code suggestion quality was the single strongest predictor and primary driver of developer productivity (\\(\beta = 1.162, p < .001, r = .798\\)) [2, 9, 10]. While tool usability, user expertise, and task complexity demonstrated strong positive bivariate correlations with productivity (\\(r = .694\\) to \\(.753\\)) [11], tool usability exhibited a negative regression coefficient (\\(\beta = -.690, p = .001\\)) when controlling for other variables, suggesting that over-reliance on simple interfaces can cause disengagement or critical thinking degradation [12, 13].

Thematic analysis of developer interviews highlighted substantial time savings on routine and syntax-heavy operations (e.g., CRUD functions, boilerplate generation, API integrations) and reduced context switching [14-16]. However, developers voiced strong concerns regarding deskilling (particularly among junior developers accepting flawed code without logic validation), security vulnerabilities, licensing/GPL code attribution risks, and declining AI model performance on complex, multi-step domain logic [17-22]. The study concludes that AI code assistants function most effectively as cognitive collaborators rather than human replacements, requiring active human verification and formal organizational governance [23-26].

---

## Frameworks Mencionados

- **DORA, SPACE, DevEx**: Not explicitly mentioned in this source [1, 3].
- **Cognitive Load Theory (Sweller, 1988)**: Discussed as a theoretical model explaining how AI code assistants reduce extraneous mental load by automating command-level syntax, enabling developers to reserve cognitive capacity for high-level problem-solving [27-30].
- **Technology Acceptance Model (TAM)**: Discussed to evaluate how user trust, perceived usefulness, and ease of use influence developer adoption and integration of AI tools into daily workflows [27-29, 31].
- **Situated Learning Theory**: Discussed as a framework illustrating how tools like GitHub Copilot act as digital tutors by delivering contextual, just-in-time feedback during live coding sessions [27-30].
- **Activity Theory**: Discussed to analyze the structural interactions between the human developer, the AI assistant, and the task environment to evaluate workflow friction and goal attainment [32].
- **Flow Theory (Csikszentmihalyi, 1990)**: Discussed regarding how AI assistants minimize context switching (e.g., reducing documentation lookup and web browsing), thereby sustaining developer focus and flow state [7, 14, 33].
- **Braun and Clarke's (2006) Six-Step Thematic Analysis Framework**: Utilized for qualitative coding and thematic synthesis of interview transcripts and notes [34, 35].

---

## Metricas Mencionadas

- **Time to Complete Task / Task Completion Speed**: Quantitative and qualitative metric evaluating development acceleration and execution time across coding tasks [8, 15, 36-38].
- **Code Suggestion Quality / Context Accuracy**: Measured via syntax correctness, context accuracy, function completeness, repetition rate, and logical fit [36, 37, 39, 40].
- **Error Rates / Code Correctness / Debugging Workload**: Measured as an indicator of code accuracy, bug reduction, and compilation error frequency [8, 36, 37, 41, 42].
- **Task Throughput / Output Volume**: Evaluated through tasks completed per session and feature delivery velocity [36, 37, 43, 44].
- **Sprint Velocity and Backlog Reduction**: Mentioned in the context of scaled agile teams leveraging AI tools to control delivery velocity [45].
- **Developer Satisfaction and Morale**: Measured on a 5-point Likert scale as a qualitative dimension of perceived productivity [8, 36, 37, 44, 46].
- **Tool Usability / Ease of Use**: Measured via IDE integration, responsiveness/latency, ease of error correction, and interface navigation [36, 39, 47-49].
- **Task Complexity**: Developer-rated difficulty based on logic depth, external library usage, domain unfamiliarity, and conditional branching [36, 47, 50].
- **User Expertise / Experience Level**: Evaluated by years of programming experience, language proficiency, prior AI tool usage, and self-assessed task confidence [36, 47, 51, 52].
- **Number of Iterations / Manual Corrections**: Measured during observational task execution to evaluate AI code suggestion accuracy [36-38].
- **Lines of Code / Commits**: Explicitly critiqued as overly simplistic traditional output metrics that fail to reflect cognitive efficiency, flow state, or long-term software quality [7, 53].

---

## Insights para Praticantes

- **Mandatory Human Code Verification**: Developers must critically inspect and test all AI-generated code snippets before deployment, as high confidence scores do not guarantee optimal logic, security, or best practices [17, 21, 25, 54].
- **Prioritize Suggestion Quality Over Interface Features**: Organizations selecting AI tools should evaluate contextual code accuracy over superficial UI features, as suggestion precision is the sole statistically significant driver of real productivity gains (\\(\beta = 1.162\\)) [10, 40, 55].
- **Mitigate Over-reliance and Deskilling in Junior Developers**: Team leads and educators must establish mentorship structures and learning scaffolds to prevent entry-level developers from blindly accepting code without understanding core logical principles [17, 20, 56, 57].
- **Integrate AI into the Secure Development Lifecycle (SDLC)**: Enterprises must implement static application security testing (SAST), vulnerability checks, and automated open-source license filters to guard against copyright violations and insecure code patterns inherited from public training sets [18, 19, 21, 57, 58].
- **Context-Specific Tool Selection**: Match specific tools to operational requirements—deploy GitHub Copilot for real-time task automation or privacy-oriented assistants like Codeium for on-premise, sensitive enterprise environments [59-61].
- **Treat AI as a Cognitive Partner, Not a Substitute**: Leverage AI code assistants for boilerplate generation, syntax lookup, and routine CRUD functions, while retaining human developer authority over architectural design, intricate multi-step logic, and ethical decisions [22-24, 26, 62].

---

## Avaliacao de Qualidade GL (Garousi et al.)

| Criterio | Pontuacao (0-1) |
|----------|----------------|
| Autoridade do autor/organizacao | 0.5 [1] |
| Descricao de metodologia | 1.0 [2, 4, 63] |
| Data de publicacao | 1.0 [1] |
| Objetividade (vies comercial) | 1.0 [2, 3] |
| Referencias citadas | 1.0 [64-77] |
| Contribuicao nova | 1.0 [2, 5, 78] |
| **TOTAL** | **5.5/6** [1-4, 65] |

---

*Extraido via NotebookLM em October 2026 para MLR: Software Developer Metrics in Practice*

💡 Would you like me to compare these findings with other grey literature sources or academic papers in your notebook?
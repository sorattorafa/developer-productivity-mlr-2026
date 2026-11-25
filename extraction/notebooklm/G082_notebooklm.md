# G082 — Generative AI and Software Developer Productivity-A Pilot Case Study at a Finnish Technology Consultancy

**Decisao: INCLUIDO | Qualidade GL: 5.5/6**

---

## Dados Bibliograficos

| Campo | Valor |
|-------|-------|
| **ID** | G082 |
| **Autor/Organizacao** | Petteri Häkkinen (Aalto University / Siili Solutions Oyj) [1, 2] |
| **Data** | July 31, 2025 [2] |
| **Tipo** | Master's thesis (Academic Grey Literature) [1] |
| **URL** | Not specified in source [1] |

---

## Resumo

This study examines the causal impact of Generative AI (GenAI) tools on software developer productivity and analyzes how implementation intensity—specifically structured training—moderates these productivity effects [2]. Conducted between July and September 2024 at Siili Solutions Oyj, a Finnish technology consultancy, the study implemented a three-arm randomized controlled trial (RCT) involving 25 professional software developers who completed 130 task observations across seven standardized development activities [2-4]. Participants were randomized across three arms: a control group with no GenAI access (Group B), a basic treatment group receiving tool access (GitHub Copilot and ChatGPT) alongside basic workflow guidance (Group A), and an enhanced treatment group receiving tool access (GitHub Copilot, ChatGPT, and Claude) plus two structured training sessions led by a principal consultant (Group C) [5, 6].

Intention-To-Treat (ITT) analysis indicates that developers granted GenAI access complete tasks 40.2% faster (0.402 log-point reduction) and produce 26.2% higher quality code (0.262 log-point increase), as evaluated on a 0–20 point scale by a senior expert developer [7-9]. Evaluating implementation intensity reveals a key operational insight: basic tool access alone yields a 25.7% speedup with a non-significant 15.5% quality improvement, whereas enhanced implementation with structured training delivers a 52% time reduction and a 66.9% quality increase relative to control [10, 11]. Direct comparisons between the treatment arms demonstrate that training primarily amplifies code quality (+29.2%), while time savings emerge from tool access alone [12, 13].

Task-level analysis shows substantial heterogeneity in treatment effects: documentation tasks yield the largest time savings (-82%), refactoring achieves a 75% speedup, and test writing demonstrates a 101% quality improvement [14, 15]. Conversely, complex tasks such as bug fixing and full-stack feature development exhibit minimal or no impact [16]. Major methodological limitations include a 35.9% overall attrition rate (15.4% in control vs. 46.2% in treatment) and low post-hoc statistical power (25% for time, 19% for quality) [17]. Nevertheless, Lee bounds analysis confirms that positive effects on time efficiency (-28.9% to -58.1%) and code quality (+8.9% to +58.5%) persist even under worst-case differential attrition assumptions [18, 19].

---

## Frameworks Mencionados

- **SPACE Framework** (Forsgren et al., 2021): Discussed and operationalized [20, 21]. The author maps "activity" to development speed and "performance" to code quality, adopting SPACE's recommendation to evaluate multiple complementary metrics in tandem to reveal speed-quality trade-offs [21].
- **Task-Based Production Framework** (Autor et al., 2003; Acemoglu & Restrepo, 2018): Discussed to explain task-level heterogeneity [22, 23]. Routine cognitive tasks (documentation, boilerplate code) sit above the AI automation threshold, whereas non-routine analytic tasks (debugging, architecture) remain below it [23-25].
- **Organizational Complementarities Theory** (Milgrom & Roberts, 1990; Brynjolfsson & Hitt, 2003): Discussed and supported [26-28]. Highlights that tool adoption requires complementary investments in training and workflow modifications to achieve super-additive productivity gains [27, 29].
- **Jagged Technological Frontier** (Dell'Acqua et al., 2023): Discussed [25, 28, 30]. Demonstrates that AI capabilities create an irregular boundary across tasks, yielding high performance on tasks within the frontier and potential errors outside it [30].
- **Unified Theory of Acceptance and Use of Technology (UTAUT)** (Venkatesh et al., 2003): Discussed regarding determinants of AI adoption, including performance expectancy, effort expectancy, social influence, and facilitating conditions [31, 32].
- **Four-Scenario Framework** (Sauvola et al., 2024): Discussed regarding how routine coding tasks transition to AI automation under human oversight versus complex system design [33].

---

## Metricas Mencionadas

- **Task Completion Time (Minutes)**: Primary efficiency metric, self-reported immediately post-task and log-transformed for statistical modeling [34].
- **Code Quality Score (0–20 Scale)**: Primary quality metric, evaluated by a senior developer with over 20 years of experience across technical accuracy, code organization, best practice adherence, and solution appropriateness [35].
- **Pull Request Velocity & Commit Frequency**: Cited from field literature (Cui et al., 2025) as speed metrics (PRs +26.08%, commits +13.55%, builds +38.38%) [36].
- **Build Success Rate & PR Approval Rate**: Cited from Cui et al. (2025) as quality proxies in organizational field settings [36].
- **Lines of Code (Log-transformed LOC)**: Cited from Gambacorta et al. (2024) as an output metric (+55% overall, +67% for junior developers), but critiqued for failing to capture code maintainability or debugging effort [37, 38].
- **Correctness, Consistency, Comprehensiveness, Conciseness**: Cited from Kabir et al. (2024) for manual evaluation of AI-generated responses [39].
- **Perceived Task Difficulty (1–5 Scale)**: Collected as a secondary process metric [40].
- **Tool Usage Indicator (Binary)**: Task-level binary indicator for GitHub Copilot, ChatGPT, and Claude usage used in Instrumental Variables (2SLS) modeling [41, 42].

---

## Insights para Praticantes

- **Tool Access Alone Is Insufficient for Quality Gains**: Providing developers with access to GenAI tools yields time savings (~29%), but structured training is required to achieve statistically significant code quality improvements (+66.9% vs. control, +29.2% vs. basic access) [13, 43, 44].
- **Target Rollouts to High-Yield Tasks**: Organizations should prioritize GenAI integration for structured, pattern-heavy tasks such as documentation (-82% time reduction), refactoring (-75% time reduction), and test writing (+101% quality increase) [14, 15, 45, 46].
- **Maintain Traditional Workflows for Complex Reasoning**: Tasks requiring deep diagnostic reasoning or multi-layer integration (e.g., bug fixing and full-stack development) show minimal benefits from GenAI tools, requiring continued reliance on human expertise [16, 46].
- **Leverage Language-Specific Expertise**: Core programming language proficiency (e.g., TypeScript) strongly complements GenAI tools, predicting higher code quality across all experimental groups [47, 48].
- **Adapt Quality Assurance Protocols**: Organizations must update code review standards to detect AI-specific errors and verification overhead, ensuring that faster code generation does not accumulate technical debt [49, 50].

---

## Avaliacao de Qualidade GL (Garousi et al.)

| Criterio | Pontuacao (0-1) |
|----------|----------------|
| Autoridade do autor/organizacao | 0.5 |
| Descricao de metodologia | 1.0 |
| Data de publicacao | 1.0 |
| Objetividade (vies comercial) | 1.0 |
| Referencias citadas | 1.0 |
| Contribuicao nova | 1.0 |
| **TOTAL** | **5.5/6** |

---

*Extraido via NotebookLM em October 2026 para MLR: Software Developer Metrics in Practice*
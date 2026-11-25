# G109 — AI isn't making developers more productive, it's making them busier

**Decisao: INCLUIDO | Qualidade GL: 4.5/6**

---

## Dados Bibliograficos

| Campo | Valor |
|-------|-------|
| **ID** | G109 |
| **Autor/Organizacao** | Chris Stokel-Walker / LeadDev |
| **Data** | June 11, 2026 |
| **Tipo** | Blog post / Industry article |
| **URL** | https://leaddev.com/ai/ai-isnt-making-developers-more-productive-its-making-them-busier |

---

## Resumo

AI-coding tools have rapidly become an essential part of developer toolboxes, with recent releases like Anthropic's Fable and Claude Code advancing tool capabilities. However, a study analyzing over 100,000 GitHub developers conducted by researchers from the Massachusetts Institute of Technology (MIT) and the Wharton School of Business provides a reality check for engineering management: task-level coding gains do not translate directly into software delivery. While early autocomplete tools like GitHub Copilot increased coding activity (commits) by 40%, interactive synchronous agents boosted gains to 140%, and autonomous asynchronous agents increased commits by 180% and lines of code written by 741%, these task-level gains attenuate sharply as work moves up the organizational hierarchy.

The researchers attribute this disparity to the "weak-link hypothesis." While AI tools effectively accelerate raw code generation, downstream stages of the software development lifecycle—including pull request (PR) reviews, code integration, and release management—continue to rely heavily on human effort and judgment. Because human capacity for code review remains fixed, a 741% increase in generated lines of code yields only a 65% increase in PRs and a 20% increase in actual software releases. As Alfonso Graziano (AI technical lead at Nearform) notes, speeding up non-bottleneck stages merely accumulates work-in-progress (WIP) in front of the primary constraint, creating organizational traffic jams.

This pipeline bottleneck extends all the way to end-users: despite a moderate spike in app releases across the Apple App Store and Google Play Store since mid-2025, total app usage has remained entirely flat, demonstrating that flooding the market with AI-assisted software does not automatically create value or discovery for users. To adapt, engineering leaders must initiate a mentality shift regarding developer roles. As Josh King (CTO of &above) highlights, developers are transitioning from code writers to code evaluators, with code review expanding to consume roughly half of a developer's workload (e.g., growing from 3–4 open PRs per project to 20+). Delivery speed now depends on how quickly organizations adapt their review, testing, and maintenance processes to match the volume of AI-generated code.

---

## Frameworks Mencionados

* **DORA, SPACE, DevEx**: Not explicitly mentioned in the source text.
* **Weak-Link Hypothesis**: Discussed by researchers from MIT and the Wharton School of Business to explain why task-level AI coding gains attenuate across the software development lifecycle due to downstream human code review and integration constraints.
* **Theory of Constraints / System Throughput Principles**: Discussed implicitly by Alfonso Graziano (Nearform), highlighting that system throughput is set by its slowest stage, and accelerating earlier stages increases work-in-progress (WIP) without increasing overall release output.

---

## Metricas Mencionadas

* **Commits / Coding Activity Increase by AI Tool Generation**:
  * **Autocomplete tools (e.g., GitHub Copilot)**: +40% increase in commits.
  * **Interactive synchronous agents (e.g., Claude Code)**: +140% cumulative increase in commits.
  * **Autonomous asynchronous agents**: +180% increase in commits.
* **Lines of Code (LoC) Increase**: +741% increase in lines of code written enabled by autonomous asynchronous agents.
* **Pull Requests (PRs) Increase**: +65% bump in PRs (attenuated from the 741% increase in written code).
* **Open Pull Requests per Project**: Increased from 3–4 open PRs at one time to 20+ open PRs (at &above).
* **Software Releases Increase**: +20% increase in actual software releases (attenuated from 741% LoC increase and 65% PR increase).
* **Code Review Workload Share**: Code review now constitutes ~50% (half) of a developer's job (at &above).
* **App Store & Google Play Store Releases**: Moderate spike in new application releases observed since mid-2025.
* **Total App Usage / User Engagement**: Flat (0% growth) despite the increase in app store releases.
* **Developer Study Sample Size**: Over 100,000 GitHub developers analyzed across MIT and Wharton School of Business research.

---

## Insights para Praticantes

* **Differentiate Code Generation from Software Delivery**: Recognize that writing code is not equivalent to shipping software. Task-level productivity gains attenuate sharply due to downstream human constraints in the software development lifecycle.
* **Identify and Unblock Pipeline Constraints**: Overall system throughput is dictated by its slowest stage (code review, testing, integration, release management). Accelerating code generation without expanding review capacity inflates work-in-progress (WIP) and congests the delivery pipeline.
* **Transition Developer Roles from Code Writers to Code Evaluators**: Shift developer mindsets and team processes toward code evaluation and review, which now represents up to 50% of developer workload.
* **Modernize Review and Testing Workflows**: Overhaul review, testing, and maintenance frameworks to accommodate higher volumes of concurrent PRs (e.g., managing 20+ open PRs per project instead of 3–4).
* **Prioritize User Value Over Software Volume**: Understand that increasing the volume of AI-assisted releases does not guarantee user adoption or market impact, as total app usage remains flat.

---

## Avaliacao de Qualidade GL (Garousi et al.)

| Criterio | Pontuacao (0-1) |
|----------|----------------|
| Autoridade do autor/organizacao | 0.5 |
| Descricao de metodologia | 0.5 |
| Data de publicacao | 1.0 |
| Objetividade (vies comercial) | 1.0 |
| Referencias citadas | 0.5 |
| Contribuicao nova | 1.0 |
| **TOTAL** | **4.5/6** |

---

*Extraido via NotebookLM em October 2026 para MLR: Software Developer Metrics in Practice*
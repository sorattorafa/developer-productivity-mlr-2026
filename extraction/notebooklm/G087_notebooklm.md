# G087 — How generative artificial intelligence (AI) tools can enhance software development?

**Decisao: INCLUIDO | Qualidade GL: 5.5/6**

---

## Dados Bibliograficos

| Campo | Valor |
|-------|-------|
| **ID** | G087 |
| **Autor/Organizacao** | Tran Huy Nguyen Nguyen / Lappeenranta–Lahti University of Technology LUT |
| **Data** | 2026 |
| **Tipo** | Bachelor's thesis |
| **URL** | N/A (Not specified in source) |

---

## Resumo

This Bachelor's thesis investigates how software engineers integrate generative AI (GenAI) tools into their daily workflows and how they perceive the impact of these tools on developer productivity [1-3]. The study addresses an empirical paradox in existing literature, where controlled experiments report task speedups exceeding 50% while real-world randomized controlled trials with experienced developers observe a 19% slowdown [2, 4, 5]. To explain these conflicting findings, a qualitative research methodology was conducted involving semi-structured interviews with six software developers across varying seniority levels and domains in Northern Europe, analyzed using thematic analysis guided by the SPACE framework [6-8].

The study identifies three core themes [9]. First, GenAI is embedded in daily development work, assisting both with implementation tasks (such as boilerplate generation and refactoring) and problem comprehension (such as requirements analysis, terminology clarification, and codebase navigation) [6, 9-11]. Second, while perceived productivity gains are consistent across all participants, their magnitude varies widely—from a modest 5% overall workflow time savings to a 40–50% net task acceleration [9, 12, 13]. These gains depend strictly on four conditions: task type (routine vs. novel), developer experience, codebase familiarity, and organizational data governance policies [9, 13-15]. Third, the developer's role is shifting from manual code writing to supervision, context engineering, and output verification [9, 16, 17].

The thesis concludes that apparent disagreements in previous quantitative literature stem from evaluating isolated implementation tasks rather than complete software development lifecycles [18, 19]. Because manual coding constitutes only a minority fraction (20–30%) of a developer's total workload, time saved during code generation is frequently absorbed by providing project context, debugging hallucinations, and conducting line-by-line verification [20-23]. Evaluating GenAI solely through output volume metrics exaggerates its real productivity contribution, highlighting the necessity of multi-dimensional evaluation models like SPACE [18, 24, 25].

---

## Frameworks Mencionados

* **SPACE Framework (Forsgren et al., 2021)**: Extensively discussed and used as the primary theoretical framework to structure the interview guide, analyze developer perceptions, and map findings across all five productivity dimensions (Satisfaction & Well-being, Performance, Activity, Communication & Collaboration, Efficiency & Flow) [6, 8, 24, 26, 27].
* **Brooks' Accidental vs. Essential Complexity Framework (Brooks, 1987)**: Discussed to contextualize GenAI as a new layer of software abstraction that reduces accidental complexity while introducing a novel supervision and verification burden [28-30].
* **Gioia Data Structure Methodology (Gioia et al., 2013)**: Applied as a qualitative analysis framework to structure first-order codes, sub-themes, and main themes [31, 32].
* **DORA Framework**: Not mentioned in the source [26, 33].
* **DevEx Framework**: Not explicitly mentioned as a named framework in the source [26, 33].

---

## Metricas Mencionadas

* **Task Completion Speed / Duration Reduction**: 55.8% speed increase in controlled experiments (Peng et al., 2023) [4, 34]; 19% completion time slowdown in real-world RCT with experienced developers (Becker et al., 2025) [4, 5]; participant estimates ranging from 5% overall workflow time saved (P4) to 40–50% net time savings after debugging (P5) or reducing 8-hour tasks to 2–4 hours (P1) [12, 13, 35].
* **Completed Tasks Volume**: Pooled 26.08% increase in completed tasks across 4,867 developers in field experiments (Cui et al., 2025) [36, 37].
* **Lines of Code (LOC) & Commit Counts**: Discussed and critiqued as traditional activity metrics that mislead evaluation by capturing raw output generation while ignoring context preparation, review, debugging, and refactoring effort [38-40].
* **Tool Adoption & Trust Percentages**: 84% adoption or plan-to-use rate in Stack Overflow 2025 survey (up from 76% in 2024), accompanied by favorable sentiment falling to 60% and rising distrust in AI accuracy [36, 41, 42].
* **Security Vulnerability Rate**: 40% average vulnerability rate in AI-generated code evaluated across security-relevant scenarios (Pearce et al., 2022) [43, 44].
* **Workload Allocation Percentage**: Manual coding accounts for only 20–30% of working time for senior/lead roles (P3), with 70–80% consumed by stakeholder alignment and requirement analysis [20, 45].

---

## Insights para Praticantes

* **Role Shift to AI Supervision**: Software engineers must transition their skill set from manual code writing to preparing context, guiding prompts, and systematically reviewing AI-generated output [9, 16, 17].
* **Mandatory Verification & Criticality-Based Review**: Developers should treat AI as an untrusted assistant and adjust code verification depth based on codebase familiarity and system safety criticality [22, 46-48].
* **Context-Dependent Productivity Expectations**: Managers should not expect uniform productivity leaps, as gains depend heavily on task routine, developer seniority, codebase familiarity, and domain constraints [9, 13, 14, 49, 50].
* **Secure Infrastructure Adoption**: Organizations should implement internal AI gateways and hosted models to enable secure tool usage without exposing confidential intellectual property or logs [51-53].
* **Holistic Productivity Assessment**: Teams should avoid evaluating AI impact via simplistic output counters (such as LOC or PR counts) and instead adopt multi-dimensional metrics like SPACE [18, 24, 25, 50].

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

*Justificativa dos criterios:*
* **Autoridade do autor/organizacao (0.5)**: Bachelor's thesis student (Tran Huy Nguyen Nguyen) at Lappeenranta–Lahti University of Technology LUT under examiner Sreman Chandio [1]. Academic university publication context, but authored by a degree candidate [1].
* **Descricao de metodologia (1.0)**: Rigorous qualitative methodology describing semi-structured interviews with 6 developers, thematic analysis following Braun & Clarke (2006) across 6 phases, coding spreadsheets, Miro affinity mapping, and ethical protocols [6-8, 54].
* **Data de publicacao (1.0)**: Explicitly stated as 2026, with interviews conducted between December 2025 and July 2026 [1, 6].
* **Objetividade (vies comercial) (1.0)**: Academic research with no commercial conflict of interest, explicit AI usage disclosures (Claude Pro, Gemini Pro), and full author responsibility [26, 55].
* **Referencias citadas (1.0)**: Extensively cited with over 50 academic papers and industry surveys (Forsgren et al., Brooks, Peng et al., Becker et al., Cui et al., Braun & Clarke, Hou et al., etc.) [56-72].
* **Contribuicao nova (1.0)**: Provides original qualitative evidence resolving the empirical paradox in GenAI productivity literature across Northern European software professionals [9, 18, 30, 73].

---

*Extraido via NotebookLM em October 2026 para MLR: Software Developer Metrics in Practice*

---

💡 Would you like me to generate a slide deck or summary report comparing these findings with other grey literature sources in your collection?
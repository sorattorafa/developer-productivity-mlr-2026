# G090 — Developer productivity with and without github copilot: A longitudinal mixed-methods case study

**Decisao: INCLUIDO | Qualidade GL: 6.0/6**

---

## Dados Bibliograficos

| Campo | Valor |
|-------|-------|
| **ID** | G090 |
| **Autor/Organizacao** | Viktoria Stray (University of Oslo, SINTEF), Elias Goldmann Brandtzæg (University of Oslo), Viggo Tellefsen Wivestad (SINTEF), Astri Barbala (SINTEF), Nils Brede Moe (SINTEF) [1] |
| **Data** | 2025 [1, 2] |
| **Tipo** | Academic case study / Empirical research paper [1, 3] |
| **URL** | https://figshare.com/s/736af5662435675e7914 [4] |

---

## Resumo

This study investigates the real-world impact of GitHub Copilot on developer activity and perceived productivity within NAV IT, the IT division of a large Norwegian public sector organization [1, 3]. The authors conducted a longitudinal mixed-methods case study analyzing 26,317 unique non-merge commits across 703 GitHub repositories over a two-year period (105 weeks), comparing 25 GitHub Copilot users with 14 non-users [1, 5]. Quantitative commit data was collected via custom Python scripts using PyDriller and combined with survey responses and 13 semi-structured interviews [1, 6, 7].

The analysis revealed that developers who adopted Copilot were consistently more active than non-users both before and after Copilot was introduced, committing more than twice as frequently on average [1, 8]. Following adoption, Copilot users experienced a minor, non-statistically significant increase in net lines of code (+16 net lines/week average), while structural code quality metrics such as function complexity and average module size remained unchanged [9-11]. These results demonstrate a clear self-selection effect, showing that early adopters were already more active developers prior to tool availability [12, 13].

There was no statistically significant correlation between changes in commit-based activity metrics and developers' self-reported productivity improvements (Spearman \\(\rho = 0.17, p = 0.406\\)) [14]. While most Copilot users reported feeling slightly or moderately more productive, this subjective boost stemmed from reduced cognitive load, faster syntax lookup, elimination of repetitive boilerplate code, and an improved feeling of daily flow, rather than an increase in raw output volume [14-17].

---

## Frameworks Mencionados

- **SPACE Framework** (Forsgren et al., 2021): Discussed and highlighted as particularly relevant due to its emphasis on satisfaction, flow, and collaboration, supporting the finding that developer productivity is multidimensional and subjective [17-19].
- **DORA & DevEx Frameworks**: Not explicitly mentioned in this study (the source focuses on commit activity metrics, survey perceptions, and SPACE dimensions).

---

## Metricas Mencionadas

- **Commit Count / Commit Frequency**: Measured weekly number of commits per developer to track activity over time [1, 5, 20].
- **Lines of Code (LOC) / Net Lines Changed**: Evaluated as weekly insertions (lines added), deletions (lines removed), and net diff [9, 15, 20].
- **Code Quality / Structural Metrics**: Function complexity and average module size evaluated to test for code degradation; no significant changes were detected [10].
- **Perceived Productivity**: Measured using a 5-point Likert scale (ranging from "Major decrease" (-2) to "Major increase" (+2)) in developer surveys [6, 14, 21].
- **Task Completion Speed**: Discussed in background and literature comparison (e.g., Peng et al., Cui et al., Rajbhoj et al.) regarding short-term task completion time [11, 22, 23].
- **Traditional Metrics (critiqued)**: Lines of Code (LOC), Function Points (FP), task counts, and bugs fixed are discussed and critiqued for lacking context and failing to reflect multidimensional knowledge work [24-26].

---

## Insights para Praticantes

- **Beware of Self-Selection Bias**: Naively comparing Copilot users against non-users after rollout can lead to the false conclusion that AI tools caused higher activity, whereas longitudinal data shows adopters were already more active baseline contributors [13, 27].
- **AI Tooling as Strategic Investment**: Granting AI tool licenses serves as an investment in developer experience, satisfaction, and retention for highly engaged staff rather than expecting a simple linear boost in raw code output [28].
- **Evaluate via Qualitative Experience and Flow**: Managers should assess AI tools using developer surveys and qualitative feedback on mental effort, flow, and frustration reduction, rather than relying exclusively on commit volume or line counts [27, 28].
- **Focus on Eliminating Boilerplate**: Copilot provides the greatest subjective value by handling repetitive boilerplate, documentation, and routine tasks, allowing developers to maintain cognitive flow and spend more mental energy on complex problem solving [15-17].

---

## Avaliacao de Qualidade GL (Garousi et al.)

| Criterio | Pontuacao (0-1) |
|----------|----------------|
| Autoridade do autor/organizacao | 1.0 |
| Descricao de metodologia | 1.0 |
| Data de publicacao | 1.0 |
| Objetividade (vies comercial) | 1.0 |
| Referencias citadas | 1.0 |
| Contribuicao nova | 1.0 |
| **TOTAL** | **6.0/6** |

---

*Extraido via NotebookLM em October 2026 para MLR: Software Developer Metrics in Practice*

---

💡 Would you like me to create a comparison report or slide deck synthesizing how these real-world findings compare with lab-based Copilot studies cited in your literature?
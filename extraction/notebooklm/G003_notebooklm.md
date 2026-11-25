# G003 — Choosing Measurement Frameworks to Fit Your Organizational Goals

**Decisao: INCLUIDO | Qualidade GL: 5/6**

---

## Dados Bibliograficos

| Campo | Valor |
|-------|-------|
| **ID** | G003 |
| **Autor/Organizacao** | DORA (DevOps Research and Assessment) [1] |
| **Data** | 2025 [1] |
| **Tipo** | Industry report [1] |
| **URL** | https://dora.dev/research/2025/measurement-frameworks/ [1] |

---

## Resumo

The source outlines how organizations can use measurement frameworks to drive impactful change in software development. It posits that measurement is complex and requires frameworks to translate broad concepts, such as **developer experience**, into distinct, measurable concepts like **speed** or **satisfaction** [1]. The report suggests a two-step process: first, defining the "why" by identifying the goals and decisions measurement will inform, and second, deciding on the "what" and "how" regarding specific metrics and data collection methods [2, 3].

Data collection is categorized into **self-reported data** (surveys, interviews, diary studies) and **logs-based measures** (quantity, time-based, frequency) [4, 5]. While self-reported data captures subjective experiences like **well-being**, logs-based metrics provide standardized data at scale [4, 5]. The source emphasizes that frameworks like **DORA**, **SPACE**, and **H.E.A.R.T.** often have overlapping underlying metrics, such as **productivity**, which can be used to serve different organizational lenses [5].

Finally, the report addresses measurement in the age of **AI**, recommending that organizations adapt existing frameworks rather than overhauling them [6, 7]. It suggests using current measures as baselines to understand how AI affects the balance between **velocity** and **code quality** [7]. To implement these strategies, it recommends the **PDCA (Plan, Do, Check, Adjust)** framework to ensure measurement remains a continuous and intentional process [8].

---

## Frameworks Mencionados

*   **DORA software delivery metrics**: Recommended to understand software delivery impact [2, 8].
*   **SPACE**: Referenced as a common framework for measuring software development [2].
*   **DevEx**: Referenced as a framework focused on developer experience [2].
*   **H.E.A.R.T.**: Referenced/Recommended; specifically suggested to be combined with DORA metrics to understand tool experience [2, 8].
*   **PDCA (Plan, Do, Check, Adjust)**: Recommended as a framework for acting on measurement findings and strategy [8].

---

## Metricas Mencionadas

*   **Speed and Satisfaction**: Key concepts used as examples of measurable topics [1].
*   **Developer Experience, Product Excellence, and Organizational Effectiveness**: Described as the overarching goals or "lenses" for measurement [2, 5].
*   **Well-being and Perceived Effectiveness**: Subjective concepts captured via self-reported data [4, 6].
*   **Quantity (number of commits or users)**: A logs-based measure to count specific artifacts [5].
*   **Time-based measures and Frequency**: Logs-based measures for activity duration and rate [5].
*   **Productivity (code commits or pull requests)**: Mentioned as overlapping metrics used across different frameworks [5].
*   **Developer Workload**: Mentioned in the context of developer experience [5].
*   **Developer Velocity and Code Quality**: Discussed specifically in the context of the impact of AI [7].

---

## Insights para Praticantes

*   **Start with the "Why"**: Always define the goals and intended decisions before selecting metrics, as frameworks are the lens through which data is viewed [2, 3].
*   **Balance Data Sources**: Combine self-reported data to capture subjective sentiment with logs-based data for objective, scalable measurement [4, 5].
*   **Leverage Overlap**: Recognise that a single metric (like **pull requests**) can inform different goals, from organizational effectiveness to developer workload [5].
*   **Iterate with PDCA**: Use the **Plan, Do, Check, Adjust** cycle to set baselines, implement changes, and refine the measurement strategy over time [8].
*   **Baseline for AI**: When introducing AI tools, use existing metrics as a baseline to monitor if increases in **velocity** are negatively impacting long-term **code quality** [7].

---

## Avaliacao de Qualidade GL (Garousi et al.)

| Criterio | Pontuacao (0-1) | Justificativa |
|----------|----------------|---------------|
| Autoridade do autor/organizacao | 1 | DORA is a leading authority in DevOps research [1]. |
| Descricao de metodologia | 0.5 | Mentions academic/industry references but does not detail the specific research methodology for this specific report [2]. |
| Data de publicacao | 1 | Published in 2025, making it very current [1]. |
| Objetividade (vies comercial) | 1 | Explicitly states it is not recommending one framework over others and focuses on guidance [9]. |
| Referencias citadas | 0.5 | Mentions established frameworks (SPACE, HEART) but lacks a formal reference list in the excerpt [2]. |
| Contribuicao nova | 1 | Provides specific, actionable guidance on combining frameworks and adapting to AI [7, 8]. |
| **TOTAL** | **5/6** | |

---

*Extraido via NotebookLM em March 2026 para MLR: Software Developer Metrics in Practice*
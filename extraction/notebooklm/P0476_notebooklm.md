# P0476 — Metrics to quantify software developer experience: a systematic mapping

**Decisao: INCLUIDO | Qualidade: 5/5**

---

## Dados Bibliograficos

| Campo | Valor |
|-------|-------|
| **ID** | P0476 [1] |
| **Autores** | Renata Brasil-Silva, Fábio Levy Siqueira [1, 2] |
| **Ano** | 2022 [1, 3] |
| **Venue** | SAC '22: The 37th ACM/SIGAPP Symposium on Applied Computing [2, 3] |
| **DOI** | 10.1145/3477314.3507304 [3, 4] |
| **Tipo** | Conference paper [3, 5] |
| **Metodo** | Systematic mapping [6-8] |
| **Amostra** | 34 primary studies selected from an initial pool of 1085 papers [5, 6, 9] |
| **Contexto** | Academic/Research context reviewing studies from Industry and Open Source Software (OSS) [8, 10] |
| **Modo de trabalho** | Not specified |
| **Metodologia** | Follows systematic mapping guidelines by Kitchenham and Petersen [8, 11] |

---

## Objetivo

The main objective of the paper is to identify how developer experience is currently quantified in Software Engineering research and to categorize the purposes for which these metrics are used [7, 8]. It aims to provide a catalog of experience metrics that can assist researchers and practitioners in choosing appropriate metrics based on their available data and research goals [7, 12].

---

## Questoes de Pesquisa

*   **RQ1:** What metrics are used to measure developer experience in Software Engineering? [8]
*   **RQ2:** What data is used to measure developer experience? [8]
*   **RQ3:** What subjects are addressed with developer experience? [8]
*   **RQ4:** What experience category is measured? [8]
*   **RQ5:** What is the goal of the studies that measure developer experience? [8]

---

## Metricas e Instrumentos de Avaliacao

| Metrica | Categoria | Nivel | Como Coletada | Validada |
|---------|-----------|-------|---------------|----------|
| Number of commits | Activity | Individual | Version Control Systems (mining) | Partial [13-15] |
| Number of lines of code (code churn) | Activity | Individual | Version Control Systems (mining) | Partial [14, 16] |
| Seniority (time in months/years) | Activity | Individual | Self-assessment or repository data | Partial [14, 17] |
| Social coding platform info (e.g., Stack Overflow reputation) | Activity | Individual | Social coding platforms (APIs/Mining) | Partial [14, 17] |
| Bug reports/fixing | Activity | Individual | Issue tracking systems | Partial [14] |
| Comments in code review | Collaboration | Individual | Code review systems | Partial [14, 18] |
| Number of files modified | Activity | Individual | Version Control Systems (mining) | Partial [14] |
| Graph-based metrics (influence/interactions) | Collaboration | Individual/Team | Interaction analysis (bugs/reviews) | Partial [18, 19] |
| Self-assessed values | Activity | Individual | Surveys/Interviews | Partial [19] |

---

## Frameworks e Metricas

### Frameworks Referenciados
*   **GQM (Goal Question Metric):** REFERENCED (implicitly in the context of measurement guidelines) [8, 11].
*   **Code Ownership:** REFERENCED (discussed as a related concept for measuring experience/expertise) [20, 21].
*   **Truck Factor (Bus Factor):** REFERENCED (discussed as a subject related to knowledge concentration) [22, 23].

### Frameworks Propostos
The paper does not propose a new measurement framework but provides a structured **catalog of metrics** extracted from the mapping study [7, 12, 19].

---

## Fatores que Influenciam Produtividade

### Fatores Positivos
| Fator | Categoria |
|-------|-----------|
| Accumulated knowledge from activities | Human [3] |
| Experience in specific programming languages | Technical [24] |
| High contribution to specific code parts (Ownership) | Technical/Human [20] |

### Fatores Negativos
| Fator | Categoria |
|-------|-----------|
| Knowledge loss due to turnover | Organizational [25] |
| "Forgetting effect" (knowledge decay over time) | Human [15] |
| Developer style bias (e.g., frequent small commits) | Process [15] |

---

## Papel da IA e Automacao

| Campo | Valor |
|-------|-------|
| Usa IA/ML? | No — The mapping itself is manual; however, it mentions primary studies using algorithms for "truck factor" and "expert identification" [18, 22, 23]. |
| Automacao de coleta? | Yes — Highlights that most data is collected via automated repository mining (25 out of 34 studies) [13, 17, 26]. |
| Impacto de IA na produtividade? | Not explicitly analyzed in this mapping. |

---

## Resultados Principais

*   The mapping identified **34 primary studies** out of 1085 initial results [5, 9].
*   **Counting activities** (commits and lines of code) is the most frequent approach, used in 26% and 22% of papers respectively [6, 14, 17].
*   **85% of studies** are evaluation research conducted in real-world industrial or open-source contexts [10].
*   **61% of metrics** focus on "Code" experience (specific components, files, or projects) [24, 27].
*   There is an increasing interest in topics like **bug triaging and expert identification** since 2019 [5].

---

## Desafios do Uso das Metricas

*   **Counting bias:** Metrics based solely on counting (commits/lines) do not reflect technical quality or individual developer style [15, 16].
*   **Lack of context:** Many metrics capture local experience but disregard general knowledge or interactions with other developers [18, 28].
*   **Temporal decay:** Metrics often fail to account for the "forgetting effect" where past experience does not equal current proficiency [15].
*   **Data availability vs. Accuracy:** The popularity of counting-based metrics may be due to data ease of access rather than their effectiveness in capturing true experience [17].

---

## Avaliacao de Qualidade Metodologica

| Criterio | Pontuacao (0-2) |
|----------|----------------|
| Objetivo claramente definido | 2 [8] |
| Metodologia adequada ao objetivo | 2 [8, 11] |
| Amostra/contexto descrito adequadamente | 2 [5, 9, 29] |
| Ameacas a validade discutidas | 2 [11, 30] |
| Resultados com evidencia suficiente | 2 [5, 31] |
| Contribuicao clara para pratica ou teoria | 2 [7, 12] |
| **TOTAL** | **12/12** |

---

## Limitacoes

*   The **search string** and choice of terms may have missed relevant papers [30].
*   The search was restricted to **six digital databases** and might not have covered all relevant literature [30].
*   Potential for **selection bias**, as the process was primarily executed by one author [11].
*   The study only included papers in **English** [32].

---

## Contribuicao Principal

The paper contributes a comprehensive **catalog of metrics** used to quantify software developer experience, organized by the type of data used, the category of experience measured, and the research goal [7, 12, 19]. It highlights the dominance of repository mining and activity counting in current research while identifying gaps in capturing developer interactions and the temporal aspects of knowledge [17, 18, 21].

---

*Extraido via NotebookLM em March 2026 para MLR: Software Developer Metrics in Practice*
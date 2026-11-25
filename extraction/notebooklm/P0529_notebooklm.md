# P0529 — Unhappy developers: bad for themselves, bad for process, and bad for software product

**Decisao: INCLUIDO | Qualidade: 4/5**

---

## Dados Bibliograficos

| Campo | Valor |
|-------|-------|
| **ID** | P0529 |
| **Autores** | Daniel Graziotin, Fabian Fagerholm, Xiaofeng Wang, Pekka Abrahamsson [1] |
| **Ano** | 2017 [2] |
| **Venue** | 2017 IEEE/ACM 39th IEEE International Conference on Software Engineering Companion [2] |
| **DOI** | https://doi.org/10.6084/m9.figshare.c.3355707 (Online Appendix) [3] |
| **Tipo** | Conference paper [2] |
| **Metodo** | Mixed methods (Qualitative data analysis of survey responses for this paper) [4] |
| **Amostra** | 181 valid and complete responses from GitHub contributors [4, 5] |
| **Contexto** | Mixed: 78% professional developers, 13% other roles (CEO, CTO, academic), and students/unemployed [5] |
| **Modo de trabalho** | Not specified |
| **Metodologia** | Not specified (References Agile and Lean in related work context) [6] |

---

## Objetivo

The main objective of the paper is to explore and identify the experienced **consequences of unhappiness** among software developers while they are developing software [7, 8]. It aims to understand the negative impact of developer affect on the individual, the development process, and the resulting software artifacts [7, 9].

---

## Questoes de Pesquisa

*   **RQ1:** What are the experienced consequences of unhappiness among software developers while developing software? [8]

---

## Metricas e Instrumentos de Avaliacao

| Metrica | Categoria | Nivel | Como Coletada | Validada |
|---------|-----------|-------|---------------|----------|
| **Scale of Positive and Negative Experience (SPANE)** | Satisfaction / Affect | Individual | Survey (12 scale items) | Yes [10, 11] |
| **Qualitative Codes (49 consequences)** | Affect / DevEx | Individual | Open-ended survey questions analyzed via Open/Axial/Selective Coding | Partial (Qualitative approach) [5, 10] |

---

## Frameworks e Metricas

### Frameworks Referenciados
*   **Happy-productive worker thesis:** REFERENCED (Used as the theoretical basis for the study) [7, 12].
*   **Scale of Positive and Negative Experience (SPANE):** APPLIED (Used to assess the happiness of individuals in the survey) [10].

### Frameworks Propostos
*   **Classification Schema of Unhappiness Consequences:** The paper proposes a schema identifying 49 types of consequences of developer unhappiness, grouped into 16 categories and sub-categories such as "Internal Consequences," "Process Consequences," and "Artifact-oriented Consequences" [2, 13].

---

## Fatores que Influenciam Produtividade

### Fatores Positivos
| Fator | Categoria |
|-------|-----------|
| Happiness / Positive Affect | Human |

### Fatores Negativos
| Fator | Categoria |
|-------|-----------|
| Unhappiness | Human [7] |
| Mental Fatigue / Low focus | Human [2] |
| Stress and Burnout | Human [14] |
| Anxiety | Human [14] |
| Low self-esteem | Human [14] |
| Sadness / Depression | Human [14] |
| Low motivation | Human [15] |
| Process shortcuts / Deviating from practices | Process [16] |

---

## Papel da IA e Automacao

| Campo | Valor |
|-------|-------|
| Usa IA/ML? | No |
| Automacao de coleta? | No (Manual retrieval of contact info from GitHub Archive) [4, 10] |
| Impacto de IA na produtividade? | Not discussed |

---

## Resultados Principais

*   The study identified **49 potential consequences of unhappiness** while developing software [7].
*   Consequences are categorized into **Internal (Developer's Own Being)**, **Process**, and **Artifact-oriented** [2, 15, 17].
*   The highest impact of unhappiness is on **productivity and performance**, accounting for approximately **40% of the in-text references** (combining low cognitive performance and process-related productivity) [18].
*   Unhappiness is a stated cause of mental health issues, including **stress, burnout, anxiety, and depression** [14, 18].
*   Unhappy developers report **low motivation**, which can lead to work withdrawal and even quitting jobs [15, 18].
*   Developers tend to take **shortcuts** and produce **"ugly" solutions** when unhappy, directly leading to **low code quality** and higher bug frequency [13, 16, 17].
*   In extreme cases, unhappiness leads to the **deletion of codebases** or entire projects [19].

---

## Desafios do Uso das Metricas

*   The paper does not explicitly list challenges for *using* metrics, but it highlights the **limitations of current SE research** in addressing mental health and affective consequences, which are more commonly explored in psychology [18].
*   **Space limitations** in publication prevent the reporting of all 49 identified codes in detail within the conference paper [2].

---

## Avaliacao de Qualidade Metodologica

| Criterio | Pontuacao (0-2) |
|----------|----------------|
| Objetivo claramente definido | 2 |
| Metodologia adequada ao objetivo | 2 |
| Amostra/contexto descrito adequadamente | 2 |
| Ameacas a validade discutidas | 0 |
| Resultados com evidencia suficiente | 2 |
| Contribuicao clara para pratica ou teoria | 2 |
| **TOTAL** | **10/12** |

*Note: The score for "Ameacas a validade" is 0 because threats were not mentioned in the provided excerpts.*

---

## Limitacoes

*   The study reports only the **most frequent codes** due to conference space limitations [2].
*   The results are based on **self-reported** qualitative data from a survey [4].
*   The focus is limited to the **consequences of unhappiness**, though it is part of a larger study [4, 19].

---

## Contribuicao Principal

The paper provides the **first systematic classification of the consequences of unhappiness** among software developers, offering an openly available schema of 49 impacts [4, 7]. It demonstrates that unhappiness is not just a personal issue but has tangible negative effects on **development performance (productivity), the software process (shortcuts/delays), and the software product (low code quality)** [9, 13, 18].

---

*Extraido via NotebookLM em March 2026 para MLR: Software Developer Metrics in Practice*
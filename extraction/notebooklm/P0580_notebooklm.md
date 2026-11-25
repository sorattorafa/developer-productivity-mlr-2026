# P0580 — Context-aware code recommendation in Intellij IDEA

**Decisao: INCLUIDO | Qualidade: 5/5**

---

## Dados Bibliograficos

| Campo | Valor |
|-------|-------|
| **ID** | P0580 |
| **Autores** | Shamsa Abid, Hamid Abdul Basit, Shafay Shamail [1, 2] |
| **Ano** | 2022 [2, 3] |
| **Venue** | ESEC/FSE '22: 30th ACM Joint European Software Engineering Conference and Symposium on the Foundations of Software Engineering [2, 3] |
| **DOI** | https://doi.org/10.1145/3540250.3558937 [1, 4] |
| **Tipo** | Conference paper [2, 3] |
| **Metodo** | Experiment (Automated offline evaluation) [5-7] |
| **Amostra** | 120 Android Java projects from GitHub (30 each for Music Player, Bluetooth chat, Weather, and File Management) [5, 8] |
| **Contexto** | OSS — Open Source projects from GitHub [6, 8, 9] |
| **Modo de trabalho** | Not specified |
| **Metodologia** | Not specified |

---

## Objetivo

The main objective of the paper is to present and evaluate **CA-FACER** (Context-aware Feature-driven API usage-based Code Recommender), an **Intellij IDEA plugin** designed to support **opportunistic code reuse** [5, 6]. The tool leverages a developer's active development context (methods in the project being edited) to recommend related code snippets representing features the developer might want to implement next [5, 10].

---

## Questoes de Pesquisa

*   **RQ1:** Does introducing context-awareness improve the performance of code recommendations compared to a baseline system (FACER)? [8, 11]
*   **RQ2:** What is the effect of context size (initial vs. evolved development stages) on the precision of recommendations? [8, 12]

---

## Metricas e Instrumentos de Avaliacao

| Metrica | Categoria | Nivel | Como Coletada | Validada |
|---------|-----------|-------|---------------|----------|
| **Precision (P@5)** | Quality | Individual | Calculated as the fraction of recommended methods that belong to the set of ground truth methods [6, 11] | Yes [11] |
| **Success Rate** | Quality | Individual | Ratio of successful recommendations where at least one relevant method is found in the top N [5, 6] | Yes [11] |
| **Mean Reciprocal Rank (MRR)** | Quality | Individual | Automated calculation based on the position of the first relevant recommendation [11] | Yes [11] |

---

## Frameworks e Metricas

### Frameworks Referenciados
*   **Collaborative Filtering:** APPLIED — Used to calculate prediction scores for the likelihood of a feature being relevant to the user project [6, 13, 14].
*   **Method Clone Classes:** APPLIED — Used to cluster similar functionalities based on API usages to identify features [5, 6, 15].
*   **Cosine Similarity:** APPLIED — Used to compute the similarity between the user's project and projects in the repository [13, 16].

### Frameworks Propostos
The paper proposes the **CA-FACER** framework, which uses a hybrid contextual modeling approach combining **pre-filtering** (finding contextually similar projects), **feature popularity-based recommendation** (collaborative filtering), and **post-filtering** (removing features already in the user's context) [6, 17].

---

## Fatores que Influenciam Produtividade

### Fatores Positivos
| Fator | Categoria |
|-------|-----------|
| Context-aware code recommendations | Technical [5, 18] |
| Opportunistic code reuse | Process [5, 18] |
| Reduced need for multiple manual searches | Process [18] |

### Fatores Negativos
| Fator | Categoria |
|-------|-----------|
| Time spent searching for code online | Process [5] |
| Lack of support for context-aware "on-the-go" recommendations | Technical [5] |

---

## Papel da IA e Automacao

| Campo | Valor |
|-------|-------|
| Usa IA/ML? | Yes — Uses **Collaborative Filtering** and **clustering algorithms** to identify API usage-based Method Clone Classes [6, 13]. |
| Automacao de coleta? | Yes — Automatically parses the user's active code file to identify development context and features [6, 19, 20]. |
| Impacto de IA na produtividade? | Improves recommendation precision by up to 46% compared to non-context-aware baselines, facilitating faster development [5, 6, 11]. |

---

## Resultados Principais

*   **46% improvement in precision** was observed using the context-aware approach over the baseline FACER system [5, 6, 11].
*   Achieved an **average precision (P@5) of 94%** for initial development stages and **83%** for evolved stages [5, 6].
*   Achieved a **success rate of 90% and 95%** for initial and evolved contexts, respectively [5, 6].
*   Statistical tests (Wilcoxon) confirmed that CA-FACER performance is **significantly better** than the baseline (p < 0.05) [11].
*   Internal experiments on 1,114 projects indicate the technique **scales well** [9].

---

## Desafios do Uso das Metricas

*   **Context Mapping:** A developer's method may not map to any existing Method Clone Class in the repository, resulting in that method being excluded from the context [21].
*   **Context Size:** The precision of recommendations can vary significantly depending on whether the project is in an initial or evolved stage of development [6, 11].

---

## Avaliacao de Qualidade Metodologica

| Criterio | Pontuacao (0-2) |
|----------|----------------|
| Objetivo claramente definido | 2 |
| Metodologia adequada ao objetivo | 2 |
| Amostra/contexto descrito adequadamente | 2 |
| Ameacas a validade discutidas | 2 |
| Resultados com evidencia suficiente | 2 |
| Contribuicao clara para pratica ou teoria | 2 |
| **TOTAL** | **12/12** |

---

## Limitacoes

*   **Simulated Context:** The evaluation used simulated development contexts (splitting project methods into context and ground truth), which may not perfectly replicate real-world developer behavior [9, 12].
*   **Dataset Scope:** The evaluation was limited to **120 Android Java projects** from GitHub rather than large-scale industrial or organizational source code [8, 9].
*   **Language Specificity:** The current implementation and evaluation focus specifically on **Java for Android** [5, 8].

---

## Contribuicao Principal

The primary contribution is the development and evaluation of **CA-FACER**, a novel context-aware tool that provides **feature-driven code recommendations** [5, 6]. Unlike previous systems that focus on single-method completion or query-based search, CA-FACER uses the entire active code context to proactively recommend multiple related features for **opportunistic reuse**, significantly improving recommendation precision and supporting rapid application development [5, 14, 18].

---

*Extraido via NotebookLM em March 2026 para MLR: Software Developer Metrics in Practice*
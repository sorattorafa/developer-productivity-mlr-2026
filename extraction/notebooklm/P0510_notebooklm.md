# P0510 — Developers' Visuo-Spatial Mental Model and Program Comprehension

**Decisao: INCLUIDO | Qualidade: 5/5**

---

## Dados Bibliograficos

| Campo | Valor |
|-------|-------|
| **ID** | P0510 |
| **Autores** | Abir Bouraffa, Gian-Luca Fuhrmann, Walid Maalej [1] |
| **Ano** | Not explicitly stated (Citations include 2022) [2, 3] |
| **Venue** | Not specified (Authors from Universität Hamburg) [1] |
| **DOI** | Not specified |
| **Tipo** | Conference paper [1, 4] |
| **Metodo** | Experiment (Between-subject design) [5, 6] |
| **Amostra** | 20 developers (Initial 26, 6 eliminated) [7, 8] |
| **Contexto** | Mixed (Academic and Industry — Students and Professionals) [8-10] |
| **Modo de trabalho** | Online (Remote) [5, 6, 11] |
| **Metodologia** | Not specified |

---

## Objetivo

The main objective of the paper is to investigate the association between developers' **visuo-spatial mental models** (influenced by **spatial code representation** and **visuo-spatial working memory**) and their **code comprehension** performance and behavior [1, 12, 13].

---

## Questoes de Pesquisa

* **RQ1:** Does the spatial representation of code influence code comprehension performance? [13]
* **RQ2:** How does the use of a code canvas influence the time allocated to specific comprehension activities such as navigation and understanding? [14]
* **RQ3:** How is developer’s visuo-spatial working memory associated with code comprehension performance? [14]

---

## Metricas e Instrumentos de Avaliacao

| Metrica | Categoria | Nivel | Como Coletada | Validada |
|---------|-----------|-------|---------------|----------|
| **Net time** | Productivity | Individual | Server logs (Task duration) [15, 16] | Yes [17] |
| **File accuracy** | Quality | Individual | Sørensen–Dice F1-score (Relevant files) [18] | Yes [17] |
| **Annotation Accuracy** | Quality | Individual | Sørensen–Dice F1-score (Relevant lines) [18] | Yes [17] |
| **Understanding Time** | Activity | Individual | Aggregated trigger events (Idle time analysis) [19, 20] | Yes [21] |
| **Navigation Time** | Activity | Individual | Logged interaction events [19, 22] | Yes [21] |
| **Corsi Block test score** | Human Factor | Individual | Digital Corsi Block-Tapping test [23-25] | Yes [26] |

---

## Frameworks e Metricas

### Frameworks Referenciados
* **Code Bubbles**: REFERENCED (discussed as early paradigm) [27].
* **Code Canvas**: REFERENCED/APPLIED (Alternative IDE design used as experimental treatment) [27, 28].
* **Synectic**: REFERENCED (Canvas-based IDE for newcomers) [29].
* **Language Server Protocol (LSP)**: APPLIED (Used for syntax highlighting and lookups) [30].
* **Tatool**: APPLIED (Open-source framework for the Corsi test) [31].

### Frameworks Propostos
The paper does not propose a new framework but presents a **web-based code visualization tool** designed to support both tab-based and canvas-based representations for experimental purposes [28, 32].

---

## Fatores que Influenciam Produtividade

### Fatores Positivos
| Fator | Categoria |
|-------|-----------|
| **Professional Development Experience** | Human (Negative correlation with task time) [33] |
| **High Visuo-spatial Memory** | Human (More efficient navigation and fewer UI interactions) [34, 35] |
| **Logical Arrangement (Code Canvas)** | Process (Side-by-side file comparison supports dependency study) [36] |

### Fatores Negativos
| Fator | Categoria |
|-------|-----------|
| **Visual Clutter/Overlaps** | Process (Affects users with low spatial memory on canvas) [37, 38] |
| **Bento-box IDE Design limitations** | Process (Requires constant tab-switching/scrolling) [39] |
| **Fatigue** | Human (Potential extraneous variable) [40] |

---

## Papel da IA e Automacao

| Campo | Valor |
|-------|-------|
| Usa IA/ML? | **No** — Uses semantic tokenization via LSP but not artificial intelligence [30]. |
| Automacao de coleta? | **Yes** — Interaction logs (clicks, file opens, moves) were automatically captured by the web tool [15, 41]. |
| Impacto de IA na produtividade? | **N/A** |

---

## Resultados Principais

* **No significant impact** of code representation (canvas vs. tab) or visuo-spatial working memory on overall comprehension performance (accuracy or time) [5, 14, 42].
* **Canvas group** spent approximately **10 minutes less** on tasks on average, though this was not statistically significant [43].
* **Significant negative correlation** between visuo-spatial working memory and time spent on **annotations and UI interactions** [34, 44].
* **Significant positive correlation** between visuo-spatial memory and **navigation time**, suggesting higher-memory users navigate more frequently but more efficiently [34, 45].
* Developers with **higher spatial memory** tended to keep more files open simultaneously (visual clutter), while those with **lower memory** tended to "clean up" the canvas and arrange files logically [37, 44].

---

## Desafios do Uso das Metricas

* **Overloaded environments**: Developers often work in chaotic IDE sessions with high window overlap (>100% screen size), making layout metrics complex [38, 46].
* **Idle time estimation**: Differentiating between cognitive "understanding time" and simple idleness is difficult without fine-grained mouse/keyboard tracking [47, 48].

---

## Avaliacao de Qualidade Metodologica

| Criterio | Pontuacao (0-2) |
|----------|----------------|
| Objetivo claramente definido | 2 |
| Metodologia adequada ao objetivo | 2 |
| Amostra/contexto descrito adequadamente | 1 |
| Ameacas a validade discutidas | 2 |
| Resultados com evidencia suficiente | 2 |
| Contribuicao clara para pratica ou teoria | 2 |
| **TOTAL** | **11/12** |

---

## Limitacoes

* **Small sample size**: Only 20 participants, which limits statistical power and generalizability [49].
* **Coarse logging**: Lack of fine-grained data (mouse drifts/keyboard) may have underestimated "understanding time" [48].
* **Fatigue detection**: The Corsi test was performed at the end, potentially affected by task exhaustion [40].
* **Task representativeness**: Tasks may not fully reflect the breadth of real-world development [40].

---

## Contribuicao Principal

The paper demonstrates that while **alternative code visualizations** (like canvases) do not immediately improve comprehension scores, **cognitive traits** such as visuo-spatial working memory are significant confounders that dictate how developers navigate code and interact with their environment [50, 51]. This suggests that future IDEs should offer **personalized navigation support** based on individual cognitive profiles [49, 51].

---

*Extraido via NotebookLM em March 2026 para MLR: Software Developer Metrics in Practice*
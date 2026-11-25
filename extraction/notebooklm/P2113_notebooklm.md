# P2113 — Developer productivity for humans, part 8: Creativity in software engineering

**Decisao: INCLUIDO | Qualidade: 4/5**

---

## Dados Bibliograficos

| Campo | Valor |
|-------|-------|
| **ID** | P2113 |
| **Autores** | Sarah Inman, Sarah D’Angelo, Bogdan Vasilescu [1, 2] |
| **Ano** | 2024 [3] |
| **Venue** | IEEE Software [1, 3] |
| **DOI** | 10.1109/MS.2023.3340831 [3] |
| **Tipo** | Journal article / IEEE Software Column [1, 3] |
| **Metodo** | Qualitative (Diary study with feedback and photo elicitation, structured interviews, Grounded Theory analysis) [4-6] |
| **Amostra** | Software developers at Google (exact sample size N not explicitly stated in the text) [4] |
| **Contexto** | Industry (Google) [4, 7, 8] |
| **Modo de trabalho** | Hybrid / Distributed (mentions hybrid models, remote chat collaboration across oceans, and office discussions) [9, 10] |
| **Metodologia** | Not specified (covers general software development workflows, refactoring, and collaboration) [6, 11] |

---

## Objetivo

This paper aims to investigate how software developers at Google define and experience creativity in their daily work, establishing a grounded definition of creativity in software engineering that reflects human experiences rather than traditional definitions focused strictly on novelty [1, 4].

---

## Questoes de Pesquisa

The paper does not state formal research questions labeled RQ1 or RQ2, but it implicitly addresses the following core research questions:
- **RQ1**: How do software developers define and experience creativity within their daily software engineering workflows? [4, 5]
- **RQ2**: How do development tools, collaboration practices, and problem-solving activities foster or hinder creativity in software engineering? [9, 12, 13]

---

## Metricas e Instrumentos de Avaliacao

| Metrica | Categoria | Nivel | Como Coletada | Validada |
|---------|-----------|-------|---------------|----------|
| Number of new features compared to bugs [3] | Quality / Activity | Product / Individual | Repository mining (cited prior literature) [3] | Yes [3] |
| Novel reuse of existing libraries [3] | Activity / Delivery | Product / Individual | Repository mining (cited prior literature) [3] | Yes [3] |
| Novel combinations of existing concepts / citations [14] | Innovation | Product / Organization | Citation / literature network analysis (cited prior literature) [14] | Yes [14] |
| Qualitative creative moments / screenshots [5, 15] | DevEx / Satisfaction | Individual | Feedback and photo elicitation in diary study [5, 15] | Yes [5, 15] |

---

## Frameworks e Metricas

### Frameworks Referenciados
- **Grounded Theory**: APPLIED as the qualitative methodology for line-by-line coding of diary entries and interview transcripts [6].
- **Boden's Concept of Combinational Creativity**: REFERENCED to ground software creativity as the combination of familiar ideas in unfamiliar ways [7, 16].
- **Amabile et al. Creativity Model**: REFERENCED to contextualize classic definitions of creativity based on novelty and usefulness [1, 17].
- **Note on standard SE frameworks (DORA, SPACE, DevEx, GQM, HEART, OKR)**: Standard quantitative measurement frameworks like DORA, SPACE, GQM, HEART, or OKR are not explicitly cited or measured in this paper, although developer experience (DevEx) is discussed conceptually [9, 18].

### Frameworks Propostos
The paper proposes a conceptual framework for creativity in software engineering centered on three pillars: (1) Collaboration and brainstorming, (2) Exploration and learning during problem-solving, and (3) Clever reuse and recombination of existing code [12].

---

## Fatores que Influenciam Produtividade

### Fatores Positivos
| Fator | Categoria |
|-------|-----------|
| Team communication and chat cross-pollination during ideation [10, 12] | Organizational / Process |
| Culture of knowledge sharing and accessible documentation [13, 19] | Organizational / Process |
| Refactoring and code cleanup to make classes/structures easier to use [11, 20] | Technical / Process |
| Deep focus and flow states during problem-solving [10] | Human |
| Learning new tools, concepts, and system architectures [13, 19] | Human / Technical |
| Clever reuse and recombination of existing code constructs [12, 21] | Technical / Process |

### Fatores Negativos
| Fator | Categoria |
|-------|-----------|
| Poor documentation and burdensome knowledge access requirements [13] | Process / Organizational |
| Overemphasizing novelty or unique code designs ("snowflake code") [21] | Technical / Human |
| Overoptimizing for short-term speed and efficiency at the expense of creative exploration [22] | Organizational / Process |
| Coordination challenges in remote or distributed collaboration [10, 22] | Organizational / Human |

---

## Papel da IA e Automacao

| Campo | Valor |
|-------|-------|
| Usa IA/ML? | No — the empirical study itself does not employ AI/ML, but discusses future research questions on LLMs and AI developer tools [9, 23]. |
| Automacao de coleta? | No — data collection relied on self-reported diary entries, screenshots, and structured interviews [5, 15]. |
| Impacto de IA na produtividade? | The authors note that while current AI/LLM tools focus on writing code faster, over-optimizing for speed risks offloading or harming the core creative process [22, 23]. |

---

## Resultados Principais

- Software developers define creativity primarily as **clever reuse** and recombination of existing code constructs in useful ways, rather than pure novelty or originality [7, 12].
- Overemphasizing novelty or unique code design is viewed negatively by developers, who refer to it as **"snowflake code"** [21].
- Refactoring code to make it cleaner, more reusable, or easier for future developers to use is identified as a primary source of creative satisfaction [11, 20].
- High-quality documentation and knowledge sharing mitigate learning hindrances, enabling developers to engage in creative problem-solving [13, 19].
- Short-term productivity hindrances (such as learning new tools or refactoring) can serve as critical enablers of long-term creativity and software engineering quality [22].

---

## Desafios do Uso das Metricas

- Standard productivity metrics that focus strictly on speed and volume risk penalizing creative activities like refactoring, documentation, and learning [22, 24].
- Classic definitions of creativity that emphasize novelty fail to capture software development reality, where reusability and utility are paramount [7, 21].
- Quantitative measurement of software creativity is difficult to implement without creating perverse incentives that discourage code reuse [14, 21].

---

## Avaliacao de Qualidade Metodologica

| Criterio | Pontuacao (0-2) |
|----------|----------------|
| Objetivo claramente definido | 2 [4] |
| Metodologia adequada ao objetivo | 2 [5, 6] |
| Amostra/contexto descrito adequadamente | 1 [4] |
| Ameacas a validade discutidas | 1 [8, 25] |
| Resultados com evidencia suficiente | 2 [11, 12] |
| Contribuicao clara para pratica ou teoria | 2 [7, 25] |
| **TOTAL** | **10/12** |

---

## Limitacoes

- The study is restricted to software developers at a single large organization (Google), which may limit generalizability to other industry contexts or open-source projects [4, 8].
- The exact sample size (\\(N\\)) of participants in the diary study and interviews is not explicitly stated in the paper text [4].
- Data collection relies on participant self-reports, diary reflections, and screenshot selections [5, 15].
- The paper does not propose or quantitatively validate a formal metric suite for operationalizing creativity [14, 25].

---

## Contribuicao Principal

The primary contribution of this paper is redefining creativity in software engineering through the lens of developers' lived experiences, establishing that SE creativity centers on clever reuse, reusability, and utility rather than pure novelty [7, 12]. This framing provides a foundation for evaluating future developer tooling, balancing productivity metrics with long-term code quality, and designing AI-assisted workflows that support human creativity [22, 23, 25].

---

*Extraido via NotebookLM em October 2026 para MLR: Software Developer Metrics in Practice*

---

💡 Would you like me to synthesize these findings with other papers in your review, or generate a comparative table on developer metrics?
# P1299 — Examining the Use and Impact of an AI Code Assistant on Developer Productivity and Experience in the Enterprise

**Decisao: INCLUIDO | Qualidade: 5/5**

---

## Dados Bibliograficos

| Campo | Valor |
|-------|-------|
| **ID** | P1299 |
| **Autores** | Justin D. Weisz, Shraddha Vijay Kumar, Michael Muller, Karen-Ellen Browne, Arielle Goldberg, Katrin Ellice Heintze, Shagun Bajpai |
| **Ano** | 2025 |
| **Venue** | CHI EA '25: Extended Abstracts of the CHI Conference on Human Factors in Computing Systems |
| **DOI** | https://doi.org/10.1145/3706599.3706670 |
| **Tipo** | Conference paper (Extended Abstract) |
| **Metodo** | Mixed methods (Large-scale Survey and Unmoderated Usability Testing) |
| **Amostra** | 669 survey respondents and 15 usability testing participants |
| **Contexto** | Industry — Internal deployment within IBM |
| **Modo de trabalho** | Not specified (Enterprise environment) |
| **Metodologia** | Not specified (Mentions Agile-related concepts like "sprints" in results) |

---

## Objetivo

The paper aims to examine the internal use of the watsonx Code Assistant (WCA) at IBM to understand its impact on **developer productivity and experience** [1]. It focuses on subjective perceptions of productivity, motivations for use or non-use, and emerging issues regarding **authorship and responsibility** for AI-generated code [1, 2].

---

## Questoes de Pesquisa

*   **RQ1:** How does an LLM-powered assistant impact developers’ perceptions of their own productivity? [2]
*   **RQ2:** What are the primary motivations and use cases for developers using an AI code assistant in an enterprise setting? [1, 3]
*   **RQ3:** How do developers perceive authorship and responsibility when co-creating code with an AI? [1, 4]

---

## Metricas e Instrumentos de Avaliacao

| Metrica | Categoria | Nivel | Como Coletada | Validada |
|---------|-----------|-------|---------------|----------|
| Effort (Ease of work) | Productivity | Individual | 7-point semantic differential scale (Survey) | Yes (Ref [5]) |
| Quality of Work | Quality | Individual | 7-point semantic differential scale (Survey) | Yes (Ref [5]) |
| Speed (Perceived) | Productivity | Individual | 7-point semantic differential scale (Survey) | Yes (Ref [5]) |
| Self-efficacy | DevEx | Individual | 4-item Likert scale (Survey) | Yes (Ref [6]) |
| Output Quality | Quality | Individual | 5-point scale (Survey) for code, docs, tests, etc. | Yes (Alpha = 0.83) |
| Chat Response Speed | Activity | Individual | 5-point scale (Survey) | No |

---

## Frameworks e Metricas

### Frameworks Referenciados
*   **SPACE**: REFERENCED — Cited to contextualize the multi-faceted nature of productivity [7].
*   **Technology Acceptance Model (TAM)**: REFERENCED — Cited regarding the learning curve of new technologies [6].

### Frameworks Propostos
The paper does not propose a new framework but applies a **mixed-methods case study** approach to evaluate attitudinal measures of productivity [8, 9].

---

## Fatores que Influenciam Produtividade

### Fatores Positivos
| Fator | Categoria |
|-------|-----------|
| Discovering starting points/solutions | Human/Cognitive |
| Automating boilerplate and repetitive tasks | Process |
| Code understanding and explanation | Technical |
| Management recommendation and support | Organizational |

### Fatores Negativos
| Fator | Categoria |
|-------|-----------|
| AI Hallucinations/Incorrectness | Technical |
| Latency/Slow response speeds | Technical |
| Need for intensive manual verification/review | Process |
| Concerns about deskilling or "laziness" | Human |
| Perceived social stigma/embarrassment | Organizational |

---

## Papel da IA e Automacao

| Campo | Valor |
|-------|-------|
| Usa IA/ML? | Yes — Uses the watsonx Code Assistant (WCA) powered by Large Language Models (LLMs) [1, 10]. |
| Automacao de coleta? | No — Data collection was manual via surveys and usability tests [9, 11]. |
| Impacto de IA na produtividade? | Results show a small net productivity increase, though gains are not evenly distributed (57.4% felt more effective vs. 42.6% who did not) [12, 13]. |

---

## Resultados Principais

*   **Code understanding** (71.9%) and **answering general programming questions** (68.5%) were the most popular use cases, outperforming direct code generation (55.6%) [14].
*   WCA provided a small but statistically significant improvement in perceived **ease of work, quality, and speed** [12].
*   **83.4% of users** were concerned about the AI reproducing copyrighted material [15].
*   **Joint responsibility** for risk mitigation was high, with 89.2% of users feeling responsible and 96.2% believing the AI is responsible [15].
*   **Shared authorship** is a prevalent feeling: 64.4% of respondents felt both they and the AI were authors when they modified generated code [16].

---

## Desafios do Uso das Metricas

*   **Reliance on attitudinal data**: The study lacked access to behavioral telemetry (e.g., actual number of queries or acceptance rates) due to privacy concerns [9].
*   **Variability in Quality**: Imperfect outputs require additional verification effort, which can become counter-productive if multiple retries are needed [17].
*   **Increased Expectations**: Developers noted that management might expect higher output volumes because the tool is available [18].

---

## Avaliacao de Qualidade Metodologica

| Criterio | Pontuacao (0-2) |
|----------|----------------|
| Objetivo claramente definido | 2 |
| Metodologia adequada ao objetivo | 2 |
| Amostra/contexto descrito adequadamente | 2 |
| Ameacas a validade discutidas | 1 |
| Resultados com evidencia suficiente | 2 |
| Contribuicao clara para pratica ou teoria | 2 |
| **TOTAL** | **11/12** |

---

## Limitacoes

*   The study is based solely on **attitudinal (subjective) data** [9].
*   The findings are specific to the **internal IBM enterprise context** and a specific timeframe (mid-2024) [10, 19].
*   Potential **sampling bias** as some respondents were part of a training program [20].

---

## Contribuicao Principal

The paper provides a detailed **enterprise-scale characterization** of how AI code assistants are actually used, revealing that they are valued as much for **sensemaking and code understanding** as they are for code generation [21, 22]. It highlights the "mixed and disparate" impact of AI on productivity and identifies the emerging need for **socio-technical approaches** to handle shared responsibility and authorship in the age of generative AI [22, 23].

---

*Extraido via NotebookLM em March 2026 para MLR: Software Developer Metrics in Practice*
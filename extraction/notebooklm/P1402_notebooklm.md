# P1402 — Identifying the Factors That Influence Trust in AI Code Completion

**Decisao: INCLUIDO | Qualidade: 5/5**

---

## Dados Bibliograficos

| Campo | Valor |
|-------|-------|
| **ID** | P1402 |
| **Autores** | Adam Brown, Sarah D’Angelo, Ambar Murillo, Ciera Jaspan, Collin Green |
| **Ano** | 2024 |
| **Venue** | AIware '24: 1st ACM International Conference on AI-Powered Software |
| **DOI** | https://doi.org/10.1145/3664646.3664757 |
| **Tipo** | Conference paper |
| **Metodo** | Mixed methods (Qualitative interviews and Quantitative logs-based analysis) |
| **Amostra** | 12 software developers (preliminary study) and 1M multi-line code completion suggestions seen by 59k developers (main study) |
| **Contexto** | Industry (Google LLC) |
| **Modo de trabalho** | Remote (interviews) / Not specified (logs) |
| **Metodologia** | Not specified |

---

## Objetivo

O principal objetivo deste trabalho é identificar e quantificar os fatores que influenciam a confiança dos desenvolvedores em ferramentas de **AI-powered code completion** [1, 2]. Os autores buscam entender como medir a confiabilidade dessas ferramentas de forma passiva e em escala, utilizando dados de logs para determinar quais características da sugestão, do desenvolvedor e do contexto de trabalho afetam a aceitação das sugestões da IA [2, 3].

---

## Questoes de Pesquisa

*   **RQ1:** How do we measure the trustworthiness of AI-powered software development tools? [3]

---

## Metricas e Instrumentos de Avaliacao

| Metrica | Categoria | Nivel | Como Coletada | Validada |
|---------|-----------|-------|---------------|----------|
| **Acceptance Rate** | Quality / Productivity | Individual | Logs (Accepted suggestions as proxy for trust) | Yes (supported by prior literature) [2, 4, 5] |
| **Model Quality Score** | Quality | Individual | Logs (Log-probability of the suggestion being accepted) | Yes (internal model metric) [6, 7] |
| **Language Expertise** | Human | Individual | Logs (% LOC submitted in the language in last 90 days) | Partial (internal operationalization) [6, 8] |
| **Readability** | Human | Individual | Logs (Internal certification of language style guide mastery) | Yes (internal company standard) [9, 10] |
| **Character Length** | Technical | Individual | Logs (Length of the code suggestion) | Yes [6, 7] |
| **Familiarity with Code Completion** | Human | Individual | Logs (Number of suggestions seen overall/daily) | Partial [6, 11] |

---

## Frameworks e Metricas

### Frameworks Referenciados
*   **PICSE (Personal, Interaction, Control, System, and Expectations):** REFERENCED (citado como uma estrutura para construir ferramentas de software confiáveis) [12].

### Frameworks Propostos
O artigo não propõe um novo framework formal, mas valida um conjunto de três dimensões (Characteristics of the Suggestion, Characteristics of the Developer, Development Context) como direcionadores de confiança [13, 14].

---

## Fatores que Influenciam Produtividade

### Fatores Positivos
| Fator | Categoria |
|-------|-----------|
| **Model Quality Score** (Higher quality leads to higher acceptance) | Technical |
| **Language Expertise** (High expertise in the language) | Human |
| **Readability** (Certification in the language) | Human |
| **Low Tenure** (Newer employees with < 6 months are more likely to accept) | Human |
| **Suggestion Length** (Intermediate length preferred over very short or very long) | Technical |

### Fatores Negativos
| Fator | Categoria |
|-------|-----------|
| **Test Files** (Suggestions in tests are significantly less likely to be accepted) | Technical / Context |
| **Bug Fix / Internal Cleanup** (Tasks with constrained scope) | Process |
| **High Daily Exposure** (Seeing too many suggestions across files in one day) | Human |
| **Position in Line** (Suggestions later in a line of code are less likely to be accepted) | Technical |

---

## Papel da IA e Automacao

| Campo | Valor |
|-------|-------|
| Usa IA/ML? | Yes — O estudo analisa ferramentas de preenchimento de código baseadas em modelos de IA generativa [1, 15]. |
| Automacao de coleta? | Yes — Os dados foram extraídos automaticamente via logs do serviço interno de code completion do Google [2, 16]. |
| Impacto de IA na produtividade? | O estudo cita que a aceitação de sugestões (proxy para confiança) é um preditor das percepções de produtividade dos desenvolvedores [4]. |

---

## Resultados Principais

*   O **Model Quality Score** é um dos preditores positivos mais fortes para a aceitação de sugestões (OR = 1.231) [7].
*   Ter **Readability** na linguagem da sugestão aumenta as chances de aceitação em 30,5% (OR = 1.305) [10].
*   Sugestões em **arquivos de teste** são significativamente menos aceitas do que em arquivos de código funcional (OR = 0.792) [17].
*   Desenvolvedores com **menos de 6 meses de empresa** têm maior probabilidade de aceitar sugestões (OR = 1.073) do que aqueles com 1 a 3 anos [18].
*   A familiaridade com a ferramenta (número de exposições) tem um impacto positivo global, mas o excesso de sugestões em um único dia pode reduzir a confiança [11, 19].

---

## Desafios do Uso das Metricas

*   **Over-trusting:** Confiança excessiva em IA sem revisão adequada pode levar à criação de código menos seguro [3].
*   **Review Costs:** Desenvolvedores podem gastar mais tempo revisando sugestões do que economizariam escrevendo o código manualmente [20].
*   **Proxy Limitations:** O uso da taxa de aceitação como proxy para confiança pode não capturar casos em que o desenvolvedor aceita a sugestão, mas a apaga logo em seguida [21].

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

*   **Contexto Único:** O estudo foi realizado exclusivamente no Google, o que pode limitar a generalização para outros ambientes ou populações (ex: estudantes) [21].
*   **Foco Restrito:** A análise focou apenas em sugestões de múltiplas linhas (**multi-line code completions**) [22].
*   **Natureza Correlacional:** Os resultados são estritamente correlacionais, não estabelecendo causalidade direta [23].
*   **Persistência do Código:** O estudo mediu a aceitação, mas não se o código gerado pela IA persistiu no codebase após a submissão [21, 24].

---

## Contribuicao Principal

A principal contribuição deste trabalho é a validação de um modelo de medição de confiança em IA baseado em logs, demonstrando que a confiança não depende apenas da qualidade do modelo, mas é fortemente influenciada pela **expertise do desenvolvedor** (especialmente o domínio da linguagem) e pelo **contexto da tarefa** (como o tipo de arquivo ou escopo do trabalho) [25]. O estudo oferece diretrizes práticas para o design de ferramentas de IA, sugerindo que a personalização e o maior controle do usuário sobre quando e como as sugestões aparecem podem otimizar a experiência e a produtividade [25].

---

*Extraido via NotebookLM em March 2026 para MLR: Software Developer Metrics in Practice*
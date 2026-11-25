# P1476 — Evaluating the Development Experience in Open Science Tools: A Case Study of the dataWASHES API

**Decisao: INCLUIDO | Qualidade: 5/5**

---

## Dados Bibliograficos

| Campo | Valor |
|-------|-------|
| **ID** | P1476 |
| **Autores** | Antônio Souza, Davi Viana, Rodrigo Santos, Allysson Allex Araújo [1] |
| **Ano** | 2024 [2] |
| **Venue** | Not explicitly stated [1] |
| **DOI** | Not available [1] |
| **Tipo** | Conference paper (implied by structure and references to workshop proceedings) [1], [3] |
| **Metodo** | Exploratory Case Study [4], Mixed-methods (Quantitative and Qualitative) [5] |
| **Amostra** | 13 participants (average age 28); 9 from the software industry and 4 currently unemployed [6], [7] |
| **Contexto** | Academic/Open Science — evaluation of the dataWASHES API, a tool for accessing workshop proceedings data [8], [9] |
| **Modo de trabalho** | Remote (Evidence collection conducted online) [10] |
| **Metodologia** | Not specified (Followed Case Study guidelines by Runeson and Höst) [4] |

---

## Objetivo

O principal objetivo deste estudo é investigar e compreender as percepções dos desenvolvedores sobre a **Developer Experience (DX)** ao utilizar a API dataWASHES, uma ferramenta de infraestrutura aberta voltada para a disseminação de dados científicos [8], [11]. O trabalho busca preencher uma lacuna na literatura sobre como a DX se manifesta especificamente em ferramentas de **Open Science** [12], [4].

---

## Questoes de Pesquisa

*   **RQ1:** What are developers’ perceptions of the developer experience with the dataWASHES API? [11], [6]

---

## Metricas e Instrumentos de Avaliacao

| Metrica | Categoria | Nivel | Como Coletada | Validada |
|---------|-----------|-------|---------------|----------|
| Satisfaction (Q1, Q2) | Satisfaction | Individual | Likert Scale (1-5) [13] | Yes (SPACE-inspired) [13], [14] |
| Perceived Simplicity (Q3) | Performance | Individual | Likert Scale (1-5) [13] | Yes (SPACE-inspired) [13], [14] |
| Documentation Adequacy (Q4) | Collaboration | Individual | Likert Scale (1-5) [13] | Yes (SPACE-inspired) [13], [14] |
| Perceived Efficiency (Q5) | Efficiency | Individual | Likert Scale (1-5) [13] | Yes (SPACE-inspired) [13], [14] |
| Workflow Flow (Q6) | Efficiency | Individual | Likert Scale (1-5) [13] | Yes (SPACE-inspired) [13], [14] |
| Initial Perceptions | DevEx | Individual | Think-Aloud method during documentation review [10] | Partial (Qualitative protocol) [5], [14] |

---

## Frameworks e Metricas

### Frameworks Referenciados
*   **SPACE**: APPLIED (Used as the basis for the evaluation dimensions and questionnaire) [11], [15], [13].
*   **DX Framework (Greiler et al.)**: REFERENCED (Cited to discuss factors influencing developer experience) [16], [17].
*   **UX (User Experience)**: REFERENCED (Cited as the origin of DX) [16].

### Frameworks Propostos
O artigo não propõe um novo framework, mas apresenta uma abordagem metodológica reproduzível que combina tarefas baseadas em cenários, protocolos **think-aloud** e o framework SPACE para avaliar ferramentas de ciência aberta [18].

---

## Fatores que Influenciam Produtividade

### Fatores Positivos
| Fator | Categoria |
|-------|-----------|
| Documentation clarity and organization | Technical [10], [19] |
| Tool intuitiveness | Technical [19] |
| Ease of use | Human/Technical [19], [17] |
| Availability of documentation in English | Process [19] |

### Fatores Negativos
| Fator | Categoria |
|-------|-----------|
| Ambiguous filters | Technical [20], [21] |
| Workflow friction (need to rerun tool for file types) | Process [20] |
| Lack of multilingual documentation (Portuguese) | Process [20], [21] |
| Need for more detailed endpoint descriptions (PDF format) | Technical/Process [20] |

---

## Papel da IA e Automacao

| Campo | Valor |
|-------|-------|
| Usa IA/ML? | No — The study references GenAI and GitHub Copilot in related work, but the dataWASHES API itself does not use them [15], [9]. |
| Automacao de coleta? | Yes — The API automates the retrieval of scientific paper data to improve efficiency over manual retrieval [22], [9]. |
| Impacto de IA na produtividade? | Not applicable — findings focus on API interaction rather than AI impact [23], [17]. |

---

## Resultados Principais

*   **84.6%** dos participantes classificaram sua experiência geral no nível mais alto da escala [8], [19].
*   A percepção de **bem-estar e felicidade (Q2)** atingiu a pontuação máxima (5.0) em todas as tarefas [23], [24].
*   A **satisfação (Q1)** e a **eficiência percebida (Q5)** receberam médias elevadas (acima de 4.85) em todos os cenários testados [23], [25], [26].
*   A **simplicidade de execução (Q3)** teve médias ligeiramente inferiores (4.69 a 4.77), indicando oportunidades de melhoria na interface [25], [26].
*   A documentação foi considerada adequada pela grande maioria, embora sugestões de expansão de rotas padrão tenham sido feitas [23], [20].

---

## Desafios do Uso das Metricas

*   **Response Bias**: Riscos associados a interpretações subjetivas dos participantes sobre sua própria experiência [14].
*   **Context Sensitivity**: A DX é moderada por características contextuais, o que significa que diferentes desenvolvedores podem ter percepções variadas sobre a mesma ferramenta com base em seus papéis [17].
*   **Metric Gaps**: O estudo cita lacunas em métricas de colaboração identificadas em trabalhos relacionados que utilizam o framework SPACE [15].

---

## Avaliacao de Qualidade Metodologica

| Criterio | Pontuacao (0-2) |
|----------|----------------|
| Objetivo claramente definido | 2 [11] |
| Metodologia adequada ao objetivo | 2 [4], [5] |
| Amostra/contexto descrito adequadamente | 2 [9], [7] |
| Ameacas a validade discutidas | 2 [14] |
| Resultados com evidencia suficiente | 2 [23], [26] |
| Contribuicao clara para pratica ou teoria | 2 [18] |
| **TOTAL** | **12/12** |

---

## Limitacoes

*   **Sample Size**: O uso de uma amostra pequena e não probabilística (13 participantes) limita a generalização dos resultados [14].
*   **Subjectivity**: Os dados dependem estritamente das percepções e relatos individuais dos participantes [14].
*   **Scope**: O estudo focou em uma única ferramenta (dataWASHES API) em um cenário específico de revisão de literatura [6], [10].

---

## Contribuicao Principal

A principal contribuição deste estudo é a aplicação do **SPACE framework** em um contexto inovador de ferramentas de **Open Science**, demonstrando que a experiência do desenvolvedor é um fator crítico para a eficácia da infraestrutura aberta [18], [27]. O trabalho oferece um modelo metodológico reproduzível para avaliar ferramentas similares e fornece evidências iniciais de que a atenção à DX pode aumentar a adoção de tecnologias voltadas para a disseminação de conhecimento científico [18], [28].

---

*Extraido via NotebookLM em March 2026 para MLR: Software Developer Metrics in Practice*
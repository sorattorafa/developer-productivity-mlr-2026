# P0156 — Software Development Productivity Model: Validation through Expert Review

**Decisao: INCLUIDO | Qualidade: 3/5**

---

## Dados Bibliograficos

| Campo | Valor |
|-------|-------|
| **ID** | P0156 |
| **Autores** | Azryna Azlen Mohd Nordin, Rodziah Latih, Noorazean Mohd Ali [1, 2] |
| **Ano** | 2021 [1] |
| **Venue** | 8th International Conference on Electrical Engineering and Informatics (ICEEI) [1] |
| **DOI** | Not specified in the source [1] |
| **Tipo** | Conference paper [1] |
| **Metodo** | Qualitative (Expert review for validation of factors identified in literature) [3, 4] |
| **Amostra** | 3 specialists (2 academics and 1 public sector executive) [5] |
| **Contexto** | Industry and Academic — focusing on SaaS (Software as a Service) development [3, 5] |
| **Modo de trabalho** | Not specified (mentions "remotely programmable tools" generally) [6] |
| **Metodologia** | Agile (mentioned as relevant for SaaS context) [7] |

---

## Objetivo

O principal objetivo do artigo é relatar os resultados do processo de **validação de fatores de produtividade identificados para o uso de SaaS**, utilizando uma abordagem de **expert review** para fundamentar um Modelo de Produtividade de Desenvolvimento de Software [3, 4].

---

## Questoes de Pesquisa

O estudo não apresenta questões de pesquisa numeradas explicitamente, mas foca em:
- **RQ1:** Quais fatores e subfatores identificados na literatura influenciam a produtividade no desenvolvimento de software em um contexto SaaS? [4]
- **RQ2:** Quais desses fatores são considerados compatíveis e válidos de acordo com a perspectiva de especialistas? [4, 8]

---

## Metricas e Instrumentos de Avaliacao

O artigo discute a medição da produtividade e utiliza um instrumento específico para a validação dos especialistas:

| Metrica | Categoria | Nivel | Como Coletada | Validada |
|---------|-----------|-------|---------------|----------|
| Lines of code written per hour | Activity | Individual | Objective measurement | Yes (Cited as example) [9] |
| Developer's self-assessments | Satisfaction | Individual | Subjective measurement | Yes (Cited as example) [9] |
| 5-level Likert scale questionnaire | Satisfaction/Agreement | Individual (Expert) | Expert Review (Survey) | Yes (For this study) [10] |

---

## Frameworks e Metricas

### Frameworks Referenciados
- **Industry 4.0:** Referenciado como o contexto de novas tecnologias que demandam evolução no desenvolvimento [6].
- **SaaS (Software as a Service):** Referenciado como o modelo de entrega de software central para o estudo [11, 12].

### Frameworks Propostos
- **Software Development Productivity Model:** O artigo propõe e valida um modelo conceitual focado em SaaS, composto por três fatores principais: **Process**, **Development Environment** e **Product or Service**, desdobrados em 17 subfatores [3, 13, 14].

---

## Fatores que Influenciam Produtividade

### Fatores Positivos
| Fator | Categoria |
|-------|-----------|
| Efficient and effective | Process [15, 16] |
| Project management | Process [15, 16] |
| Time (Optimum period) | Process [15, 16] |
| Commitment | Process [15, 16] |
| Cost (Saving costs) | Process [15, 16] |
| Methodology (e.g., Agile) | Process [7, 16] |
| Process maturity | Process [16, 17] |
| Software/Development tools | Technical (Environment) [16, 17] |
| Programming language | Technical (Environment) [16, 17] |
| Documentation | Technical (Environment) [16, 17] |
| Modernity | Technical (Environment) [16, 18] |
| Quality | Technical (Product) [16, 18] |
| Reliability | Technical (Product) [16, 18] |
| Flexible (Customization) | Technical (Product) [16, 19] |
| User interface | Technical (Product) [16, 19] |
| Reuse code | Technical (Product) [16, 19, 20] |

### Fatores Negativos
| Fator | Categoria |
|-------|-----------|
| Hardware concurrent development | Technical (Environment) — Rejected by experts as not applicable to SaaS [16, 21] |
| Software/Database size | Technical (Product) — Rejected as experts believe productivity remains same regardless of size [16, 21] |
| Risk resolution | Process — Only "moderately compatible"; experts felt it might not affect SaaS productivity directly [8, 15] |

---

## Papel da IA e Automacao

| Campo | Valor |
|-------|-------|
| Usa IA/ML? | No [22] |
| Automacao de coleta? | No — Contudo, o texto menciona que "maiores esforços de pesquisa são necessários para atingir mais automação" em atividades de avaliação [22]. |
| Impacto de IA na produtividade? | Not applicable |

---

## Resultados Principais

*   Identificação inicial de **19 fatores** de produtividade através de revisão de literatura [4, 23].
*   Validação por especialistas que resultou na exclusão de 2 fatores ("hardware concurrent development" e "software/database size") por não serem compatíveis com o contexto SaaS [13, 21].
*   O modelo final validado consiste em **3 fatores principais e 17 subfatores** [13, 14].
*   Especialistas forneceram definições refinadas para cada fator, adaptando conceitos tradicionais de engenharia de software para a realidade de SaaS [7, 17-20, 24-27].
*   O fator **"Quality"** foi destacado como o componente mais crítico, pois afeta diretamente a satisfação do cliente e o sucesso do projeto [28].

---

## Desafios do Uso das Metricas

*   **Dificuldade de Definição:** As definições padrão de vocabulários de engenharia de software carecem de detalhes para descrever a situação real do uso de SaaS [24].
*   **Complexidade do Código:** A complexidade e a replicação de código-fonte são citadas como restrições para o aumento da produtividade [23].
*   **Comunicação Ineficaz:** Identificada como uma barreira que SaaS pode ajudar a mitigar através de colaboração [12, 23].

---

## Avaliacao de Qualidade Metodologica

| Criterio | Pontuacao (0-2) |
|----------|----------------|
| Objetivo claramente definido | 2 [3, 4] |
| Metodologia adequada ao objetivo | 1 (Expert review é adequado, mas a amostra é muito pequena) [5] |
| Amostra/contexto descrito adequadamente | 1 (Perfis detalhados, mas apenas 3 especialistas) [5] |
| Ameacas a validade discutidas | 0 (Não explicitamente discutidas no texto fornecido) |
| Resultados com evidencia suficiente | 1 (Baseado em consenso qualitativo de poucos especialistas) [8, 25] |
| Contribuicao clara para pratica ou teoria | 1 (Propõe um modelo inicial para SaaS) [14] |
| **TOTAL** | **6/12** |

---

## Limitacoes

*   **Tamanho da Amostra:** O processo de validação contou com apenas **três especialistas** [5].
*   **Natureza Qualitativa:** O estudo foca em percepções de especialistas e carece de validação empírica quantitativa (como surveys com desenvolvedores) para confirmar o impacto real dos fatores na produtividade [29].
*   **Falta de Impacto Direcional:** O estudo atual não detalha se cada fator tem impacto positivo ou negativo, o que é sugerido para pesquisas futuras [29].

---

## Contribuicao Principal

A principal contribuição deste trabalho é a **proposição e validação qualitativa de um Modelo de Produtividade para o Desenvolvimento de Software em SaaS**, categorizando 17 fatores essenciais em Processos, Ambiente de Desenvolvimento e Produto, fornecendo definições adaptadas para o contexto de nuvem [3, 13, 14].

---

*Extraido via NotebookLM em March 2026 para MLR: Software Developer Metrics in Practice*
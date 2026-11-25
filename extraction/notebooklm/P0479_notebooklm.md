# P0479 — Seamless Data Migration between Database Schemas with DAMI-Framework: An Empirical Study on Developer Experience

**Decisao: INCLUIDO | Qualidade: 5/5**

---

## Dados Bibliograficos

| Campo | Valor |
|-------|-------|
| **ID** | P0479 |
| **Autores** | Delfina Ramos-Vidal, Alejandro Cortiñas, Miguel R. Luaces, Oscar Pedreira, Ángeles Saavedra Places, Wesley K. G. Assunção |
| **Ano** | 2025 |
| **Venue** | EASE '25: Proceedings of the 29th International Conference on Evaluation and Assessment in Software Engineering |
| **DOI** | 10.1145/3756681.3756947 |
| **Tipo** | Conference paper |
| **Metodo** | Mixed methods (Proof-of-concept, controlled experiment, and survey) |
| **Amostra** | 21 participants (11 computer science students and 10 professional developers) |
| **Contexto** | Mixed — Evaluation based on a real-world scientific repository modernization scenario with academic and industry-affiliated participants |
| **Modo de trabalho** | Not specified |
| **Metodologia** | Not specified |

---

## Objetivo

O objetivo principal do artigo é reduzir a carga de trabalho dos desenvolvedores durante a evolução de esquemas de banco de dados através do **DAMI-Framework** [1]. Este framework utiliza uma **Domain-Specific Language (DSL)** e um **parser** para simplificar o mapeamento de esquemas e automatizar a geração de **SQL scripts** necessários para a migração de dados em sistemas legado [1, 2].

---

## Questoes de Pesquisa

O estudo define seus objetivos de avaliação baseados em métricas de usabilidade e experiência do usuário, que podem ser estruturadas como as seguintes questões de pesquisa implícitas:
- **RQ1**: Qual a usabilidade e as limitações do DAMI-DSL sob a perspectiva de suas propriedades (eficiência, expressividade, flexibilidade e concisão)? [3, 4]
- **RQ2**: Qual o nível de satisfação do desenvolvedor, facilidade de aprendizado, legibilidade e confiança ao utilizar o DAMI-DSL em comparação ao SQL? [3-5]
- **RQ3**: Qual o impacto do uso do DAMI-Framework no esforço de migração (linhas de código e erros cometidos) em comparação a scripts manuais? [1, 6, 7]

---

## Metricas e Instrumentos de Avaliacao

| Metrica | Categoria | Nivel | Como Coletada | Validada |
|---------|-----------|-------|---------------|----------|
| Lines of Code (LOC) | Productivity | Individual | Automated count comparing DSL and SQL scripts | Yes [8, 9] |
| Character Count | Productivity | Individual | Automated count of script characters | Yes [6, 9] |
| Usage Efficiency | DevEx | Individual | 5-point Likert scale questionnaire (Q1) | Yes [10, 11] |
| Expressiveness | DevEx | Individual | 5-point Likert scale questionnaire (Q2, Q5) | Yes [10, 11] |
| Flexibility | DevEx | Individual | 5-point Likert scale questionnaire (Q3) | Yes [10, 11] |
| Conciseness | DevEx | Individual | 5-point Likert scale questionnaire (Q4, Q5) | Yes [10, 11] |
| Satisfaction | Satisfaction | Individual | 5-point Likert scale questionnaire (Q6, Q12) | Yes [5, 10, 12] |
| Ease of Learning/Use | DevEx | Individual | 5-point Likert scale questionnaire (Q7, Q8, Q10) | Yes [5, 10, 12] |
| Readability | DevEx | Individual | 5-point Likert scale questionnaire (Q9) | Yes [5, 10] |
| Confidence | DevEx | Individual | 5-point Likert scale questionnaire (Q11) | Yes [10, 12] |
| Error Rate | Quality | Individual | Manual analysis of completed migration tasks | Yes [7] |
| Completion Time | Productivity | Individual | Recorded time for task completion | Yes [13, 14] |

---

## Frameworks e Metricas

### Frameworks Referenciados
- **Goal Question Metric (GQM)**: APPLIED para o design do questionário de usabilidade [3].
- **Usa-DSL**: APPLIED como taxonomia de métricas de usabilidade para DSLs [10].

### Frameworks Propostos
O artigo propõe o **DAMI-Framework**, composto por uma **Domain-Specific Language (DAMI-DSL)** declarativa para definir mapeamentos e transformações, e um **DSL Parser** (baseado em **ANTLR**) que valida os scripts e gera código **SQL** executável [2, 15, 16].

---

## Fatores que Influenciam Produtividade

### Fatores Positivos
| Fator | Categoria |
|-------|-----------|
| Readability (similaridade com linguagem natural) | Technical |
| Automation of SQL generation | Process |
| Code Conciseness (menos LOC e caracteres) | Technical |
| Modular rules and transformation reuse | Process |
| Abstraction of low-level data manipulation | Technical |

### Fatores Negativos
| Fator | Categoria |
|-------|-----------|
| Domain Complexity (dificuldade em entender o esquema legado) | Human |
| High Cognitive Load (mapeamento de primary keys legadas) | Human |
| Lack of documentation in legacy systems | Process |
| Learning curve for unfamiliar DSL syntax | Human |

---

## Papel da IA e Automacao

| Campo | Valor |
|-------|-------|
| Usa IA/ML? | No — O framework utiliza técnicas de Model-Driven Engineering e parsers gramaticais tradicionais (ANTLR) [15, 16]. |
| Automacao de coleta? | No — A coleta de dados foi realizada via questionários estruturados e medição manual de tempo [13, 17]. |
| Impacto de IA na produtividade? | Not applicable |

---

## Resultados Principais

- **Redução de esforço**: O uso do DAMI-DSL reduziu as **Lines of Code (LOC)** em **18.3%** e a contagem de caracteres em **35.6%** em comparação ao SQL [1, 6].
- **Redução de erros**: A taxa de erro caiu de 1.57 (SQL) para **0.38 (DSL)**, representando uma redução de aproximadamente **75.8%** [7].
- **Percepção positiva**: **99%** dos participantes concordaram que a DSL é eficiente e concisa; **91%** expressaram satisfação geral [4].
- **Curva de aprendizado**: Participantes com menos experiência técnica completaram as tarefas mais rapidamente com a DSL após a familiarização inicial com o domínio [14].

---

## Desafios do Uso das Metricas

- **Complexidade de Domínio**: O maior desafio identificado não foi a linguagem em si, mas a compreensão das regras de negócio e do esquema do banco de dados legado [13].
- **Operações Mentais Difíceis (Hard Mental Operations)**: Mapear chaves primárias legadas para novas chaves geradas foi identificado como a parte mais confusa da sintaxe, exigindo alta carga cognitiva [18].
- **Confiança do Usuário**: A métrica de confiança recebeu as avaliações mais baixas, indicando incerteza ao usar uma linguagem nova sem suporte visual ou documentação extensiva [19].

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

- **Generalização**: O estudo baseou-se em um único cenário prático (repositório científico), o que pode não capturar todas as complexidades de migrações industriais massivas [20].
- **Viés de Amostragem**: Utilização de **convenience sampling** com estudantes e desenvolvedores próximos aos autores [21].
- **Efeito de Aprendizado**: Embora mitigado por **counterbalancing**, a ordem das tarefas pode ter influenciado os resultados de tempo [22].

---

## Contribuicao Principal

A contribuição principal é o desenvolvimento e a validação empírica do **DAMI-Framework**, uma solução que simplifica a migração de dados entre esquemas heterogêneos ao abstrair a complexidade do **SQL** através de uma **DSL** intuitiva [1, 23]. O estudo demonstra que o framework não apenas reduz o código necessário, mas também diminui significativamente a incidência de erros cometidos por desenvolvedores, melhorando a experiência geral durante processos de modernização de software [7, 23].

---

*Extraido via NotebookLM em March 2026 para MLR: Software Developer Metrics in Practice*
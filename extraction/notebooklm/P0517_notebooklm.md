# P0517 — Studying and Improving Code Understandability through Atoms of Confusion

**Decisao: INCLUIDO | Qualidade: 5/5**

---

## Dados Bibliograficos

| Campo | Valor |
|-------|-------|
| **ID** | P0517 |
| **Autores** | Guoshuai Shi |
| **Ano** | 2024 (Baseado na referência de reavaliação de sistemas Java) |
| **Venue** | Not specified (Academic Thesis/Research Proposal context) |
| **DOI** | Not available |
| **Tipo** | Research Paper / Doctoral Symposium Proposal |
| **Metodo** | Mixed methods (Mining Software Repository, Developer Survey, Experiment/LLM Refactoring) |
| **Amostra** | 76,610 Pull Requests (PRs) de seis projetos Java de código aberto |
| **Contexto** | OSS (Open-Source Software) — Projetos: openHAB add-ons, Elasticsearch, Jenkins, ksqlDB, Kafka, e Sharding-sphere |
| **Modo de trabalho** | Not specified |
| **Metodologia** | Not specified |

---

## Objetivo

O principal objetivo deste trabalho é investigar como os **Atoms of Confusion (AoCs)** — pequenos padrões de código que, embora sintaticamente corretos, podem causar confusão — afetam a compreensão do programa e a qualidade do código em projetos Java [1, 2]. A pesquisa busca entender o impacto real dos AoCs na propensão a defeitos, a percepção dos desenvolvedores sobre esses padrões e como **Large Language Models (LLMs)** podem ser utilizados para refatorar códigos confusos de forma contextualizada [1, 3].

---

## Questoes de Pesquisa

*   **RQ1:** Qual é o impacto dos AoCs na comunidade de desenvolvimento Open-Source Software (OSS) em termos de propensão a defeitos? [1]
*   **RQ2:** Como os desenvolvedores percebem o impacto dos AoCs na compreensão do código? [1, 4]
*   **RQ3:** Como os Large Language Models (LLMs) podem ser utilizados para auxiliar na refatoração de AoCs quando apropriado? [1, 3]

---

## Metricas e Instrumentos de Avaliacao

| Metrica | Categoria | Nivel | Como Coletada | Validada |
|---------|-----------|-------|---------------|----------|
| AoC addition/removal ratio | Quality | Team/Project | Mining Software Repository (MSR) de Pull Requests [5, 6] | Partial (Replicates and extends previous studies [6, 7]) |
| Likert scale ratings | Satisfaction/DevEx | Individual | Developer survey (Percepção de confusão) [8, 9] | Not specified |
| Time spent on solving coding problems | Productivity | Individual | Developer survey / Coding tasks [8, 9] | Not specified |
| Automatic readability metrics | Quality | Individual/Team | Ferramentas de análise estática (e.g., métrica de Buse e Weimer) [10, 11] | Yes [11] |
| Developer preferences | Satisfaction/DevEx | Individual | User study (Comparação entre código original e refatorado por LLM) [10, 12] | Not specified |

---

## Frameworks e Metricas

### Frameworks Referenciados
- **Atoms of Confusion (AoC):** REFERENCED e APPLIED como o objeto central de estudo para medir confusão no código [1, 7].
- **Mining Software Repository (MSR):** APPLIED como técnica para extração de dados de Pull Requests e Issues [1, 5].
- **Readability Metrics (Buse and Weimer):** REFERENCED para avaliação automática da legibilidade do código refatorado [10, 11].

### Frameworks Propostos
A pesquisa propõe um framework para **LLM-aided AoC Refactoring**, que utiliza dados empíricos de percepção dos desenvolvedores e contexto do projeto para treinar ou ajustar LLMs a sugerirem refatorações apenas quando apropriado, evitando refatorações indiscriminadas [3, 10].

---

## Fatores que Influenciam Produtividade

### Fatores Positivos
| Fator | Categoria |
|-------|-----------|
| Code understandability and clarity | Technical [2, 13] |
| Developer experience and project conventions | Human / Process [14, 15] |
| AI-powered refactoring tools | Technical [5] |

### Fatores Negativos
| Fator | Categoria |
|-------|-----------|
| Atoms of Confusion (AoCs) | Technical [2, 16] |
| Maintenance costs (due to less understandable code) | Process [1] |
| Cognitive load during program comprehension | Human [5] |

---

## Papel da IA e Automacao

| Campo | Valor |
|-------|-------|
| Usa IA/ML? | Yes — Utiliza Large Language Models (LLMs) para sugerir alternativas de refatoração para AoCs [3, 10]. |
| Automacao de coleta? | Yes — Utiliza técnicas de MSR para detectar automaticamente AoCs em Pull Requests e correlacionar com Issues [5, 17]. |
| Impacto de IA na produtividade? | Espera-se que reduza a carga cognitiva dos desenvolvedores e melhore a manutenibilidade do código através de refatorações contextualizadas [3, 5]. |

---

## Resultados Principais

*   Os **Atoms of Confusion (AoCs)** não afetam significativamente a propensão a defeitos em projetos Java de código aberto estudados [1].
*   Pull Requests de correção de bugs (**Bug-Fixing PRs**) tendem a aumentar o número de AoCs com mais frequência do que diminuí-los [15].
*   Não há evidências conclusivas de que os AoCs sejam os culpados por defeitos, pois são adicionados e removidos em frequências similares em BFPRs e NBFPRs [15].
*   Desenvolvedores experientes (seniores) podem introduzir AoCs propositalmente para seguir convenções de codificação específicas do projeto [15].
*   A análise foi baseada em uma amostra robusta de **76.610 Pull Requests** [7].

---

## Desafios do Uso das Metricas

*   **Subjetividade da confusão:** O conceito de "confusão" é subjetivo, tornando necessário incorporar as visões dos desenvolvedores na análise de dados [18].
*   **Contexto vs. Indiscriminação:** O desafio de refatorar AoCs apenas quando apropriado (contexto do projeto e experiência do dev) em vez de removê-los cegamente [3].
*   **Falta de datasets:** Ausência de conjuntos de dados concretos sobre as estratégias de enfrentamento de desenvolvedores em relação a códigos confusos [4].

---

## Avaliacao de Qualidade Metodologica

| Criterio | Pontuacao (0-2) |
|----------|----------------|
| Objetivo claramente definido | 2 |
| Metodologia adequada ao objetivo | 2 |
| Amostra/contexto descrito adequadamente | 2 |
| Ameacas a validade discutidas | 2 |
| Resultados com evidencia suficiente | 1 |
| Contribuicao clara para pratica ou teoria | 2 |
| **TOTAL** | **11/12** |

---

## Limitacoes

*   O estudo preliminar focou apenas na linguagem **Java**, necessitando de expansão para outras linguagens [1, 6].
*   A pesquisa ainda está em progresso quanto à coleta de percepções subjetivas de desenvolvedores através de surveys e entrevistas [18, 19].
*   Dependência da qualidade das ferramentas de detecção automática de AoCs e métricas de legibilidade existentes [5, 10].

---

## Contribuicao Principal

A principal contribuição deste trabalho é o fornecimento de evidências empíricas sobre o impacto dos **Atoms of Confusion** na manutenibilidade e qualidade de software em Java, desafiando a premissa de que eles são inerentemente indutores de defeitos [13, 18]. Além disso, o trabalho estabelece as bases para o desenvolvimento de ferramentas assistidas por IA (LLMs) que auxiliam desenvolvedores a melhorar a compreensibilidade do código de maneira personalizada e sensível ao contexto [5, 20].

---

*Extraido via NotebookLM em March 2026 para MLR: Software Developer Metrics in Practice*
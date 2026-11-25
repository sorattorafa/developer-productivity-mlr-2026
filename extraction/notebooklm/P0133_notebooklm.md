# P0133 — Framework to analyze the relationship between agile software engineers’ emotions and their productivity

**Decisao: INCLUIDO | Qualidade: 6/12**

---

## Dados Bibliograficos

| Campo | Valor |
|-------|-------|
| **ID** | P0133 |
| **Autores** | Martín Gildardo Salido Ortega, Gilberto Borrego Soto, Ramón Rene Palacios Cinco, Luis-Felipe Rodríguez [1] |
| **Ano** | 2021 [1] |
| **Venue** | IEEE (unspecified conference) [1, 2] |
| **DOI** | Not specified [1] |
| **Tipo** | Conference paper [1, 3] |
| **Metodo** | Proposed Framework / Doctoral Work Proposal [3, 4] |
| **Amostra** | N/A (Preliminary framework proposal) [4, 5] |
| **Contexto** | Agile Software Development [4, 6, 7] |
| **Modo de trabalho** | Not specified [3, 8] |
| **Metodologia** | Agile (Scrum and Kanban mentioned) [9, 10] |

---

## Objetivo

O objetivo principal deste artigo é apresentar um **framework preliminar** para determinar a relação entre as **emoções** de um engenheiro de software que trabalha sob metodologias ágeis e a sua **produtividade**, identificando também as possíveis causas dessas emoções [4, 6, 7]. O framework visa sugerir ações para regular ou melhorar o estado emocional dos desenvolvedores para aumentar ou manter níveis desejados de produtividade [6-8].

---

## Questoes de Pesquisa

Embora não listadas formalmente como "RQ", o trabalho aborda:
- Como as emoções influenciam a produtividade em ambientes ágeis? [4, 7, 11]
- Quais são as causas das variações emocionais dos desenvolvedores no contexto de trabalho? [5, 6, 12]
- Como coletar dados sobre emoções e produtividade de forma não intrusiva? [12-14]

---

## Metricas e Instrumentos de Avaliacao

| Metrica | Categoria | Nivel | Como Coletada | Validada |
|---------|-----------|-------|---------------|----------|
| **Emotional State** (e.g., happiness, stress) | Satisfaction/Affect | Individual | Biometric sensors (Empatica E4) measuring skin electricity [8, 15] | Partial (Ref. [15]) |
| **Lines of Code** | Activity | Individual | Analysis of commits [8] | Yes (Ref. [16]) |
| **Team Velocity** (Story points) | Delivery | Team | Counting completed story points over time [8] | Yes (Ref. [16]) |

---

## Frameworks e Metricas

### Frameworks Referenciados
- **Agile Manifesto**: REFERENCED (base for work values) [9].
- **Scrum / Kanban**: REFERENCED (context of team performance) [10, 17].
- **Affective Computing Models**: REFERENCED (context-aware emotional identification) [3, 5].
- **Productivity Models** (Banker et al. / Krishnan et al.): REFERENCED [8, 18, 19].

### Frameworks Propostos
- **Framework Preliminar para Relação Emoção-Produtividade**: Um framework composto por camadas de usuários, dados e processos (interpretação, intervenção e associação) que utiliza **meios não intrusivos** (sensores e mineração de repositórios) para correlacionar o contexto e as emoções do desenvolvedor com seu desempenho produtivo [2, 5, 20].

---

## Fatores que Influenciam Produtividade

### Fatores Positivos
| Fator | Categoria |
|-------|-----------|
| **Happiness** (Happiness/Well-being) | Human [11, 21] |
| **Motivation** | Human [9, 10, 13] |
| **Emotional Intelligence** | Human [10, 20] |
| **Agile Principles Application** | Process [9, 10] |

### Fatores Negativos
| Fator | Categoria |
|-------|-----------|
| **Stress / Anxiety** | Human [2, 10, 11] |
| **Frustration** | Human [2, 11, 13] |
| **Project Complexity** | Technical/Process [11] |
| **Fear of failure** (not finishing on time) | Human [14] |

---

## Papel da IA e Automacao

| Campo | Valor |
|-------|-------|
| Usa IA/ML? | **Yes** — Proposed for emotion identification using Neural Networks or Decision Trees based on biometric data [8]. |
| Automacao de coleta? | **Yes** — Use of non-intrusive smart devices (Smartwatches, bands) and automated repository analysis [3, 8, 20]. |
| Impacto de IA na produtividade? | Indirect — AI helps identify emotional causes to suggest interventions that restore productivity levels [4, 8]. |

---

## Resultados Principais

- Definição de um framework preliminar que integra **contexto, emoções e produtividade** [5, 20].
- Identificação de que desenvolvedores "mais felizes" são **melhores solucionadores de problemas analíticos** [10, 11].
- Proposição de que a coleta de dados **não deve ser intrusiva** (evitando entrevistas/questionários) para não prejudicar a agilidade do processo de desenvolvimento [12, 14, 22].

---

## Desafios do Uso das Metricas

- **Intrusividade**: O uso de entrevistas ou questionários pode distrair o desenvolvedor e reduzir sua agilidade [12, 14].
- **Falta de foco nas causas**: Muitas pesquisas focam no estado emocional, mas ignoram as causas contextuais que levam a esse estado [14, 22].
- **Má aplicação de métodos ágeis**: Pode gerar estresse e frustração se os engenheiros não estiverem alinhados aos princípios [2].

---

## Avaliacao de Qualidade Metodologica

| Criterio | Pontuacao (0-2) |
|----------|----------------|
| Objetivo claramente definido | 2 [4, 6] |
| Metodologia adequada ao objetivo | 1 [3, 5] |
| Amostra/contexto descrito adequadamente | 0 [4] |
| Ameacas a validade discutidas | 0 |
| Resultados com evidencia suficiente | 1 [5, 20] |
| Contribuicao clara para pratica ou teoria | 2 [20] |
| **TOTAL** | **6/12** |

---

## Limitacoes

- O trabalho é uma **proposta preliminar** (trabalho em progresso de doutorado) [4, 6].
- As métricas de produtividade e os métodos de coleta ainda precisam de **definição final e testes** [20].
- A **validação empírica** via caso de estudo ainda é considerada trabalho futuro [5, 20].

---

## Contribuicao Principal

A principal contribuição é a proposição de um **framework de monitoramento não intrusivo** que utiliza computação afetiva (sensores biométricos e dados contextuais) para analisar como o bem-estar emocional impacta a produtividade em ambientes ágeis, permitindo intervenções proativas sem interromper o fluxo de trabalho do desenvolvedor [7, 8, 14, 20].

---

*Extraido via NotebookLM em March 2026 para MLR: Software Developer Metrics in Practice*
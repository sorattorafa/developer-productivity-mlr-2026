# P1306 — Factors Affecting Software Development Productivity: An empirical study

**Decisao: INCLUIDO | Qualidade: 5/5**

---

## Dados Bibliograficos

| Campo | Valor |
|-------|-------|
| **ID** | P1306 |
| **Autores** | Edna Dias Canedo, Giovanni Almeida Santos [1, 2] |
| **Ano** | 2019 [1, 3] |
| **Venue** | XXXIII Brazilian Symposium on Software Engineering (SBES 2019) [2, 3] |
| **DOI** | https://doi.org/10.1145/3350768.3352491 [3, 4] |
| **Tipo** | Conference paper [3] |
| **Metodo** | Mixed methods (Systematic Literature Review and Survey) [2, 5] |
| **Amostra** | SLR: 57 primary studies; Survey: 49 software developers [6-8] |
| **Contexto** | Industry (practitioners in Brasília, Brazil) and Open-source projects [2, 8] |
| **Modo de trabalho** | Not specified [8] |
| **Metodologia** | Mixed (includes Agile, DevOps, and Traditional references) [9-12] |

---

## Objetivo

O objetivo principal deste trabalho é investigar quais fatores afetam a produtividade em projetos de desenvolvimento de software e em projetos open-source [2]. Para alcançar isso, os autores realizaram uma Revisão Sistemática da Literatura (RSL) para identificar fatores de impacto e um levantamento (survey) com profissionais para identificar suas percepções sobre a implementação e o impacto desses fatores em suas atividades diárias [2, 5].

---

## Questoes de Pesquisa

*   **RQ1:** What factors influence the productivity of software development teams? [13]
*   **RQ2:** What is the perception of practitioners regarding factors that influence the productivity of software development teams? [8]

---

## Metricas e Instrumentos de Avaliacao

| Metrica | Categoria | Nivel | Como Coletada | Validada |
|---------|-----------|-------|---------------|----------|
| KLOC / SLOC | Productivity | Team / Individual | Internal viewpoint (counting lines of code) [14, 15] | Yes [14] |
| Function Point Analysis (FPA) | Productivity | Organization / Team | External viewpoint based on functional requirements [16] | Yes [16] |
| Use Case Points (UCP) | Productivity | Organization / Team | Measurement based on use cases [16] | Yes [16] |
| COSMIC Function Points (CFP) | Productivity | Organization / Team | Functional size measurement method [16] | Yes [15, 16] |
| Effort (Work hours) | Productivity | Team / Individual | Recording hours spent on technical and non-technical tasks [17] | Yes [17] |
| Perception of Factors | DevEx / Satisfaction | Individual | Online survey using Likert scale [8] | No (Subjective) [8] |

---

## Frameworks e Metricas

### Frameworks Referenciados
*   **CMMI:** REFERENCED (discussed in relation to software process maturity and rework) [11, 18, 19].
*   **Scrum:** REFERENCED (discussed as an agile practice that can reduce rework when used with CMMI) [11, 18].
*   **COCOMO II:** REFERENCED (cited as a classical source for cost estimation) [20, 21].
*   **PMBOK:** REFERENCED (cited regarding effort and project management) [22].
*   **Function Point Analysis:** REFERENCED (discussed as a size metric) [16].

### Frameworks Propostos
O artigo não propõe um novo framework, mas apresenta uma taxonomia de 37 fatores classificados em quatro categorias: People, Product, Organization e Open-source projects [23, 24].

---

## Fatores que Influenciam Produtividade

### Fatores Positivos
| Fator | Categoria |
|-------|-----------|
| Experience | Human [25, 26] |
| Motivation | Human [26, 27] |
| Team cohesion | Human [26, 28] |
| Collaboration | Human [26, 28] |
| Ease of communication | Human [26, 29] |
| Knowledge management | Organizational [26, 30] |
| Training | Organizational [26, 31] |
| Reuse | Organizational [26, 32] |
| Software processes | Process [11, 26] |
| IT Investments | Organizational [26, 33] |
| Team Engagement | Human [26, 34] |
| Gender Diversity | Human [24, 26] |

### Fatores Negativos
| Fator | Categoria |
|-------|-----------|
| Turnover | Human [26, 35] |
| Application Complexity | Technical [36, 37] |
| Duration of the project | Process [37, 38] |
| Software size | Technical [37, 38] |
| Rework | Process [18, 26] |
| Team size | Organizational [26, 39] |
| Entry Barriers | Organizational / Human [24, 26] |
| Time Disengagement | Human [26, 34] |

---

## Papel da IA e Automacao

| Campo | Valor |
|-------|-------|
| Usa IA/ML? | No [8, 40] |
| Automacao de coleta? | No — data collection was manual through SLR and survey [8, 40] |
| Impacto de IA na produtividade? | Not discussed in the paper |

---

## Resultados Principais

*   Identificação de **37 fatores** que influenciam a produtividade, divididos em quatro categorias principais: Pessoas, Produto, Organização e Projetos Open-source [24].
*   **82%** dos profissionais afirmaram que não existe uma gestão de conhecimento (Knowledge management) eficiente em suas organizações [41].
*   **71%** dos respondentes indicaram que suas organizações não possuem uma base de dados histórica (Historical database) de medições [42].
*   **67%** relataram que não trabalham com um processo de desenvolvimento de software padronizado [19].
*   **53%** dos participantes afirmaram que participam na definição de metas e na alocação de tarefas [19].
*   **74%** dos profissionais consideram a diversidade de gênero (Gender diversity) como um fator importante para a equipe [43].

---

## Desafios do Uso das Metricas

*   A produtividade de software é influenciada por muitos fatores, tornando economicamente inviável considerar todos em uma única análise [44].
*   Dificuldade em comparar produtividade entre diferentes linguagens de programação usando métricas como KLOC e SLOC [15].
*   Muitos fatores identificados na literatura não são implementados na prática pelas organizações de desenvolvimento de software [43].
*   A natureza humana intensiva do desenvolvimento de software torna a produtividade difícil de quantificar e controlar [45].

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

*   A RSL pode não ter selecionado todos os estudos primários relevantes, apesar das buscas manuais e automáticas [46].
*   O processo de extração e classificação de dados foi baseado no julgamento dos autores (ameaça subjetiva) [46].
*   O levantamento (survey) foi limitado a desenvolvedores na cidade de Brasília, o que impede a generalização estatística dos resultados qualitativos [47].
*   As percepções dos entrevistados podem ser enviesadas por suas próprias crenças e experiências pessoais [47].

---

## Contribuicao Principal

A contribuição principal deste estudo é a consolidação e categorização de 37 fatores que impactam a produtividade no desenvolvimento de software, fornecendo uma base teórica e prática para que organizações identifiquem quais elementos devem priorizar para melhorar seu desempenho [24, 48]. O trabalho destaca uma lacuna significativa entre o que a literatura científica sugere e o que as empresas realmente praticam, especialmente em relação à gestão de conhecimento e ao uso de bases de dados históricas para medição [41-43].

---

*Extraido via NotebookLM em March 2026 para MLR: Software Developer Metrics in Practice*
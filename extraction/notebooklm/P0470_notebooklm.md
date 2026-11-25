# P0470 — Fully Automated DORA Metrics Measurement for Continuous Improvement

**Decisao: INCLUIDO | Qualidade: 5/5**

---

## Dados Bibliograficos

| Campo | Valor |
|-------|-------|
| **ID** | P0470 |
| **Autores** | Janick Rüegger, Martin Kropp, Sebastian Graf, Craig Anslow [1] |
| **Ano** | 2024 [2, 3] |
| **Venue** | ICSSP '24: International Conference on Software and Systems Processes [2, 3] |
| **DOI** | https://doi.org/10.1145/3666015.3666020 [3] |
| **Tipo** | Conference paper [2, 3] |
| **Metodo** | Case study [4-6] |
| **Amostra** | 37 microservices [4, 7-9] |
| **Contexto** | Industry (Zurich-based mass-IoT software company) [10] |
| **Modo de trabalho** | Not specified [1-91] |
| **Metodologia** | DevOps and Agile (Scrum) [10] |

---

## Objetivo

O objetivo principal do artigo é apresentar e avaliar uma solução para a medição e o cálculo completamente automatizados das métricas **DORA** a partir de ferramentas de **DevOps**, operando no nível individual de microserviços e em tempo real [4, 14]. O estudo busca fornecer evidências empíricas sobre a praticidade da computação automatizada para apoiar a melhoria contínua na entrega de software [14].

---

## Questoes de Pesquisa

*   **RQ1:** How do the DORA metrics on individual systems differ from the teams performance? [7]
*   **RQ2:** How do the DORA metrics differ between individual systems? [7]
*   **RQ3:** Which technical events are needed to calculate each DORA metric? [7]
*   **RQ4:** Which technical data sources can be used for capturing these events? [7]

---

## Metricas e Instrumentos de Avaliacao

| Metrica | Categoria | Nivel | Como Coletada | Validada |
|---------|-----------|-------|---------------|----------|
| **Deployment Frequency (DF)** | Velocity / Delivery [21, 28] | Individual/Team [4] | Automated via GitLab Pipeline API (successful runs to production) [29, 38] | Yes [10, 19] |
| **Lead Time for Changes (LTFC)** | Velocity / Delivery [21, 30] | Individual/Team [4] | Automated via GitLab API (time between deployment and first commit) [30, 31, 38] | Yes [10, 19] |
| **Mean Time to Restore (MTTR)** | Stability / Delivery [21, 32] | Individual/Team [4] | Automated via Prometheus alerts (duration of defective state) [33, 38] | Yes [10, 19] |
| **Change Failure Rate (CFR)** | Stability / Delivery [21, 34] | Individual/Team [4] | Calculated ratio of incidents (Prometheus) to deployments (GitLab) [35, 38] | Yes [10, 19] |

---

## Frameworks e Metricas

### Frameworks Referenciados
*   **DORA:** APPLIED (used as the primary measurement instrument) [4, 12, 14].
*   **SPACE:** REFERENCED (discussed in the context of developer productivity) [82].
*   **Agile/Scrum:** APPLIED (context of the case study team) [10].

### Frameworks Propostos
O artigo propõe um sistema de medição **open-source** para arquiteturas de microserviços que ingere dados brutos de sistemas de **Source-Code Management (SCM)**, **CI/CD** e **Telemetry** para calcular as métricas DORA automaticamente [14, 37, 39].

---

## Fatores que Influenciam Produtividade

### Fatores Positivos
| Fator | Categoria |
|-------|-----------|
| Automated measurement and real-time insights [14, 26] | Process |
| DevOps tooling and practices (CI/CD, Monitoring) [10, 12, 15] | Technical |
| Shortened feedback cycles [16, 27] | Process |
| Data-driven decision-making [4, 14] | Organizational |

### Fatores Negativos
| Fator | Categoria |
|-------|-----------|
| Subjectivity and bias in qualitative surveys [13, 23] | Human |
| Survey fatigue [13, 24] | Human |
| Lack of granularity in team-level aggregates [4, 13, 25] | Process |
| Outdated or over-generalized assessments [13] | Process |

---

## Papel da IA e Automacao

| Campo | Valor |
|-------|-------|
| Usa IA/ML? | No — o estudo foca em automação baseada em eventos e APIs, não mencionando IA [1-91]. |
| Automacao de coleta? | Yes — coleta totalmente automatizada de commits, pipelines e alertas via GitLab e Prometheus [4, 37]. |
| Impacto de IA na produtividade? | Not applicable [1-91]. |

---

## Resultados Principais

*   O desempenho agregado da equipe não representa adequadamente o desempenho de sistemas individuais; apenas **26.8%** dos sistemas tiveram uma correlação forte com o agregado [58, 60, 61].
*   Diferenças significativas foram encontradas entre microserviços: um único projeto foi responsável por **71.9%** de todas as falhas (**outages**) [47, 62].
*   **27%** dos sistemas foram responsáveis por **62.8%** de todos os **deployments** [45, 62].
*   Sistemas classificados como **críticos** tiveram uma frequência de deployment **2.6 vezes maior** e um **CFR 31.1% menor** que os não críticos [53].
*   O tempo médio de restauração (**MTTR**) foi de **93 segundos** [48].
*   A automação permitiu identificar **outliers** que seriam mascarados em pesquisas qualitativas ou médias de equipe [51, 61].

---

## Desafios do Uso das Metricas

*   Identificar e definir incidentes de forma precisa é complexo e pode simplificar excessivamente os erros de produção [69, 74].
*   Mapear incidentes para **deployments** específicos é notoriamente difícil para calcular o **CFR** [35].
*   Dados de sistema podem omitir fenômenos detectados apenas por humanos fora dos limites das ferramentas [69].
*   Metadados de **commits** podem não ser significativos se práticas de Git inadequadas forem usadas [74].

---

## Avaliacao de Qualidade Metodologica

| Criterio | Pontuacao (0-2) |
|----------|----------------|
| Objetivo claramente definido | 2 [4] |
| Metodologia adequada ao objetivo | 2 [6] |
| Amostra/contexto descrito adequadamente | 2 [8, 10] |
| Ameacas a validade discutidas | 2 [72, 74] |
| Resultados com evidencia suficiente | 2 [43-58] |
| Contribuicao clara para pratica ou teoria | 2 [14, 76] |
| **TOTAL** | **12/12** |

---

## Limitacoes

*   O estudo de caso foi limitado a uma única equipe em uma **start-up** em fase de escala [72].
*   O uso do agregado de microserviços como **proxy** para o desempenho da equipe pode não ser aplicável onde várias equipes compartilham sistemas [73].
*   A medição foca apenas na entrega, excluindo fases de **design** ou provisionamento de infraestrutura [74].
*   O design atual permite apenas uma definição de incidente por sistema [74].
*   Dependência da qualidade dos metadados de ferramentas de terceiros (GitLab/Prometheus) [74].

---

## Contribuicao Principal

A principal contribuição é o desenvolvimento e a validação de uma solução **open-source** que prova a viabilidade técnica da medição automatizada das métricas **DORA** em nível de microserviço [4, 7, 76]. O trabalho demonstra empiricamente que as métricas de nível de equipe (comumente usadas em pesquisas) falham em capturar as variações críticas de desempenho entre os componentes individuais de um sistema distribuído, oferecendo assim uma transparência muito maior para a melhoria contínua baseada em dados [4, 61, 71].

---

*Extraido via NotebookLM em March 2026 para MLR: Software Developer Metrics in Practice*
# P0011 — QEX: Automated Testing Observability and QA Developer Experience Framework

**Decisao: INCLUIDO | Qualidade: 5/5**

---

## Dados Bibliograficos

| Campo | Valor |
|-------|-------|
| **ID** | P0011 |
| **Autores** | Huang Luohua Locke, Yap Kai Ting Keshia, Joseph Chu Ken Yu, Hock Yao Chua [1] |
| **Ano** | 2023 [2] |
| **Venue** | IEEE International Conference on Software Testing, Verification and Validation (ICST) [2, 3] |
| **DOI** | 10.1109/ICST57152.2023.00049 [2] |
| **Tipo** | Conference paper [1, 2] |
| **Metodo** | Case study / Technical implementation [1, 4] |
| **Amostra** | 100+ Quality Assurance (QA) engineers and 10 product lines [5] |
| **Contexto** | Industry — Shopee Pte Ltd (large-scale enterprise) [1] |
| **Modo de trabalho** | Not specified |
| **Metodologia** | DevOps / CI/CD [1, 6, 7] |

---

## Objetivo

O objetivo principal é apresentar o **QEX**, um framework de monitoramento que integra fontes de dados de testes comuns para obter alta **observability** no desenvolvimento de testes [1, 8]. O framework visa fornecer feedback abrangente, confiável e oportuno sobre as atividades de testes, melhorando a **Developer Experience** dos engenheiros de QA e fornecendo insights acionáveis para os stakeholders [4, 8].

---

## Questoes de Pesquisa

O artigo não lista questões de pesquisa explicitamente no formato RQ1, RQ2, mas foca em:
- Como quantificar o uso, estabilidade e desenvolvimento de frameworks de testes automatizados [2].
- Como integrar dados de diferentes fontes (Git, Jenkins, Jira) para fornecer transparência no progresso da maturidade de **Automated Testing (AT)** [9, 10].

---

## Metricas e Instrumentos de Avaliacao

| Metrica | Categoria | Nivel | Como Coletada | Validada |
|---------|-----------|-------|---------------|----------|
| **Pass rate** | Quality | Team/Organization | Automated via testing library RESTful API [11-13] | Yes [14] |
| **Active Score** | Usage/Activity | Team/Organization | Ratio of executed cases to total cases in master branch (Git + Execution data) [14, 15] | Yes [14] |
| **Stability Score** | Quality | Team/Organization | Compound metric (Active Score x Pass Rate) [14, 16] | Yes [14] |
| **AT Sign-off** | Value/Delivery | Team/Organization | Count of Jira tickets signed off based on AT results [11, 17] | Yes [14] |
| **Bugs Found by AT** | Quality/Value | Team/Organization | Number of bug tickets created due to AT failures [9, 17] | Yes [14] |
| **Flakiness** | Quality | Team/Organization | Derived from execution trends [11, 18] | Partial [19] |
| **Test Case Duration** | Quality/Activity | Individual/Team | Measured during test execution [11, 12] | Yes [12] |
| **Maintainer Workload** | Activity | Individual | Extracted from Git log (last contributor) [11, 20, 21] | Partial [21] |

---

## Frameworks e Metricas

### Frameworks Referenciados
- **Developer Experience (DevEx):** APPLIED — Usado como base conceitual para o design do framework (aspectos de cognição, conação e afeto) [18, 22, 23].
- **Test Automation Improvement Model (TAIM):** REFERENCED [24].
- **OKRs:** REFERENCED/APPLIED — Visualizados no dashboard para acompanhar tendências de bugs e sign-offs [25-27].

### Frameworks Propostos
O artigo propõe o **QEX (Automated Testing Observability and QA Developer Experience Framework)**. É um modelo de arquitetura orientada a eventos que centraliza dados de repositórios Git, servidores de CI (Jenkins) e ferramentas de gestão de tarefas (Jira) em um banco de dados de séries temporais (InfluxDB), visualizado através de dashboards no Grafana [8, 28, 29].

---

## Fatores que Influenciam Produtividade

### Fatores Positivos
| Fator | Categoria |
|-------|-----------|
| Event-driven architecture | Technical [30] |
| Real-time feedback/observability | Process [8, 31] |
| Automated ticket updates (CI/CD integration) | Process [7] |
| Centralized/unified dashboard | Organizational [10] |

### Fatores Negativos
| Fator | Categoria |
|-------|-----------|
| Technical complexity of deployment | Technical [32] |
| High maintenance of customized testing libraries | Technical/Process [33] |
| Large scale/complexity of product and test code | Technical [22, 34] |

---

## Papel da IA e Automacao

| Campo | Valor |
|-------|-------|
| Usa IA/ML? | No — Foca em monitoramento e estatística descritiva [1, 14]. |
| Automacao de coleta? | Yes — Coleta automatizada via webhooks, APIs e queriers periódicos de Git, Jenkins e Jira [20, 30, 35]. |
| Impacto de IA na produtividade? | Not applicable. |

---

## Resultados Principais

- O framework suporta mais de **100 engenheiros de QA** em **10 linhas de produtos** diferentes [5].
- Gerencia a execução de **dezenas de milhares de testes diariamente** [5].
- Possui um tempo de reação médio de **alguns milissegundos** devido à arquitetura orientada a eventos [31].
- Proporciona **unified observability**, permitindo que as equipes escolham as melhores ferramentas de teste mantendo métricas padronizadas [10].

---

## Desafios do Uso das Metricas

- **Viés na seleção:** Toda métrica possui um viés intrínseco; o framework tenta mitigar isso oferecendo variedade [31].
- **Abuso de métricas:** Risco de usar métricas isoladas para medir desempenho individual de forma contraproducente [26].
- **Imprecisão contextual:** A definição de "maintainer" via Git log pode se tornar imprecisa após refatorações de código [21].

---

## Avaliacao de Qualidade Metodologica

| Criterio | Pontuacao (0-2) |
|----------|----------------|
| Objetivo claramente definido | 2 [1, 8] |
| Metodologia adequada ao objetivo | 2 [7, 10, 28, 30, 35] |
| Amostra/contexto descrito adequadamente | 2 [5] |
| Ameacas a validade discutidas | 1 [21, 26, 31, 36] |
| Resultados com evidencia suficiente | 2 [5] |
| Contribuicao clara para pratica ou teoria | 2 [37] |
| **TOTAL** | **11/12** |

---

## Limitacoes

- **Sensibilidade ao contexto:** Requer sinalização manual em casos de exceção e pode ser impreciso em atribuições de carga de trabalho após refatoração [21, 36].
- **Manutenção técnica:** O uso de bibliotecas de teste customizadas exige esforço extra de manutenção durante atualizações de versão [33].
- **Complexidade de setup:** Requer um nível considerável de habilidade técnica para implantação inicial [33].

---

## Contribuicao Principal

A principal contribuição é o **framework QEX**, que serve como um blueprint para projetar infraestruturas de teste integradas com alta **observability**. Ele preenche a lacuna de ferramentas específicas para a experiência de desenvolvedores de QA em larga escala, oferecendo uma implementação de código aberto e métricas inovadoras (como Active e Stability Scores) para medir a maturidade e o impacto dos testes automatizados no ciclo de vida de software [1, 37, 38].

---

*Extraido via NotebookLM em March 2026 para MLR: Software Developer Metrics in Practice*
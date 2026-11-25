# P1272 — A Multi-Faceted Approach to Measuring Engineering Productivity

**Decisao: INCLUIDO | Qualidade: 4/5**

---

## Dados Bibliograficos

| Campo | Valor |
|-------|-------|
| **ID** | P1272 |
| **Autores** | Manish Sanwal, Ishan Deva |
| **Ano** | 2024 |
| **Venue** | International Journal of Trend in Scientific Research and Development (IJTSRD) |
| **DOI** | Não fornecido (e-ISSN: 2456-6470) |
| **Tipo** | Journal article |
| **Metodo** | Mixed methods (Proposição de framework e estudo de caso experimental) |
| **Amostra** | 7 equipes diferentes acompanhadas ao longo de 7 sprints |
| **Contexto** | Industry — Engineering Department, News Corporation, New York, USA |
| **Modo de trabalho** | Not specified |
| **Metodologia** | Agile |

---

## Objetivo

O objetivo principal do artigo é introduzir uma abordagem holística para medir a produtividade de engenharia através de um **Productivity Calculator** [1, 2]. O framework visa fornecer uma pontuação baseada em métricas diversificadas para servir como uma ferramenta de **self-assessment** para equipes, auxiliando na identificação de áreas de melhoria e promovendo uma cultura de aprimoramento contínuo, sem o intuito de comparar indivíduos ou equipes de forma injusta [1, 3, 4].

---

## Questoes de Pesquisa

O artigo não lista formalmente questões de pesquisa prefixadas com RQ, mas foca em resolver o problema de como capturar a natureza multifacetada da produtividade além de métricas tradicionais como linhas de código [2, 5].

---

## Metricas e Instrumentos de Avaliacao

| Metrica | Categoria | Nivel | Como Coletada | Validada |
|---------|-----------|-------|---------------|----------|
| **Story Points Completed** | Productivity/Activity | Team | JIRA Plugin | Yes [6] |
| **Number of Blocked Tickets** | Productivity/Activity | Team | JIRA Plugin | Yes [6] |
| **Number of Spikes Executed** | Activity/Innovation | Team | JIRA Plugin | Yes [7] |
| **Priority Tickets/Bugs Undertaken Mid-Sprint** | Delivery/Adaptability | Team | JIRA Plugin | Yes [7] |
| **Cycle Time** | Delivery/Process | Team | JIRA Plugin | Yes [8] |
| **Number of Commits** | Activity | Team | GitHub Integration | Yes [8] |
| **Number of Pull Requests Opened** | Activity/Collaboration | Team | GitHub Integration | Yes [9] |
| **Build Success Rate** | Quality/Delivery | Team | CI/CD Integration | Yes [9] |
| **Code Coverage** | Quality | Team | CI/CD Integration | Yes [9] |
| **Unit Test Quality** | Quality | Team | Mutation Testing (Future) | Partial [10] |
| **New Security Vulnerabilities Introduced** | Quality | Team | CI/CD Integration | Yes [11] |
| **Number of PR Reviews** | Collaboration/Quality | Team | GitHub Integration | Yes [12] |
| **Number of Comments Left** | Collaboration | Team | GitHub Integration | Yes [12] |
| **Number of PRs Merged** | Activity/Delivery | Team | GitHub Integration | Yes [12] |
| **PR Time in Review** | Delivery/Process | Team | GitHub Integration | Yes [13] |
| **Number of Issues Logged** | Quality | Team | QA Systems | Yes [13] |
| **Number of Features Tested** | Quality/Activity | Team | QA Systems | Yes [14] |
| **Deployment Frequency** | Delivery (DORA) | Team | Production Systems | Yes [15] |
| **Lead Time for Changes** | Delivery (DORA) | Team | CI/CD Pipeline | Yes [15] |
| **Change Failure Rate** | Quality (DORA) | Team | Production Systems | Yes [15] |
| **Mean Time to Recovery (MTTR)** | Delivery (DORA) | Team | Production Systems | Yes [16] |

---

## Frameworks e Metricas

### Frameworks Referenciados
- **Agile Methodology**: APPLIED — Utilizado como base para a estrutura de sprints e métricas como Story Points e Velocity [1, 17].
- **DORA Metrics**: APPLIED — Deployment Frequency, Lead Time for Changes, Change Failure Rate e MTTR são integrados ao calculador [14-16, 18].
- **GitHub Copilot Study**: REFERENCED — Citado para demonstrar o impacto da IA na produtividade e satisfação [5].

### Frameworks Propostos
O artigo propõe o **Engineering Productivity Calculator**, que consolida métricas de seis categorias (Agile practices, code contributions, code quality, review activities, QA efforts, e deployment metrics) em um índice único normalizado pelo tamanho da equipe [1, 19, 20]. O framework permite a customização de pesos para cada métrica conforme as prioridades da equipe (ex: foco em inovação vs. foco em entrega) [21, 22].

---

## Fatores que Influenciam Produtividade

### Fatores Positivos
| Fator | Categoria |
|-------|-----------|
| **AI-assisted coding** (GitHub Copilot) | Technical [5] |
| **Smaller, frequent commits/PRs** | Process [8, 9] |
| **Collaborative code review** | Human/Process [11, 12] |
| **Customization of metric weights** | Organizational [20, 21] |

### Fatores Negativos
| Fator | Categoria |
|-------|-----------|
| **Invisible Bottlenecks** (Long PR reviews, bulky commits) | Process [23] |
| **Context Switching** (Mid-sprint high priority tasks) | Human/Process [7] |
| **Security Vulnerabilities** | Technical [11] |
| **High PR Time in Review** | Process [13, 24] |
| **Team availability variations** (Holidays/vacations) | Human/Organizational [24, 25] |

---

## Papel da IA e Automacao

| Campo | Valor |
|-------|-------|
| Usa IA/ML? | Yes — O artigo discute o impacto positivo do GitHub Copilot na velocidade e satisfação [5]. |
| Automacao de coleta? | Yes — Coleta automatizada via plugin JIRA, integrações com GitHub e pipelines de CI/CD [26]. |
| Impacto de IA na produtividade? | Desenvolvedores completam tarefas mais rápido e reportam maior satisfação com assistência de IA [5]. |

---

## Resultados Principais

- **Correlação Inversa**: Identificou-se que o tempo de revisão de PR (*PR Review Time*) é inversamente correlacionado ao número de commits e PRs; ou seja, PRs menores reduzem significativamente o tempo de revisão [24, 27].
- **Sensibilidade do Modelo**: O calculador detectou quedas de produtividade relacionadas a feriados e férias, revelando a necessidade de um fator de normalização baseado em dias úteis trabalhados e não apenas no tamanho da equipe [24, 25].
- **Eficácia do Tooling**: A implementação via JIRA plugin permitiu rastrear tendências de produtividade ao longo de 7 sprints, confirmando sua utilidade para monitorar o desempenho da equipe [27].

---

## Desafios do Uso das Metricas

- **Measurement Challenges**: Algumas métricas são difíceis de automatizar ou quantificar com precisão (ex: qualidade de testes unitários) [14, 28].
- **Overemphasis on Numbers**: Risco de focar excessivamente nos números em detrimento do trabalho significativo [28].
- **Context Ignored**: O risco de as métricas não considerarem fatores externos que afetam a produtividade [28].
- **Misuse for Comparison**: O perigo de usar as pontuações para comparar equipes diferentes, ignorando contextos e desafios únicos [3, 4].

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

- **Dificuldade de Automação**: Algumas métricas críticas de deployment e qualidade ainda são desafiadoras de coletar automaticamente [15, 28].
- **Normalização Inicial**: O fator de normalização inicial por tamanho de equipe não considerou variações de disponibilidade individual (férias/feriados) [24, 25].
- **Foco Quantitativo**: O modelo pode ignorar aspectos qualitativos e criativos intangíveis do desenvolvimento [2, 28].

---

## Contribuicao Principal

A principal contribuição é o desenvolvimento e validação prática de um **Productivity Calculator** multi-facetado que integra métricas técnicas e de processo (JIRA, GitHub, CI/CD) em um único score [1, 26]. Diferente de métricas isoladas, ele oferece uma visão equilibrada e customizável, permitindo que equipes de diferentes perfis (ex: inovação vs. entrega) ajustem os pesos das métricas para alinhar o sistema de medição aos seus objetivos estratégicos específicos [17, 21, 29].

---

*Extraido via NotebookLM em March 2026 para MLR: Software Developer Metrics in Practice*
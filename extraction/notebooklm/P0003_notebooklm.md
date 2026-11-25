# P0003 — A Framework for Automating the Measurement of DevOps Research and Assessment (DORA) Metrics

**Decisao: INCLUIDO | Qualidade: 5/5**

---

## Dados Bibliograficos

| Campo | Valor |
|-------|-------|
| **ID** | P0003 |
| **Autores** | Brennan Wilkes, Alessandra Maciel Paz Milani, Margaret-Anne Storey [1] |
| **Ano** | 2023 [2] |
| **Venue** | IEEE International Conference on Software Maintenance and Evolution (ICSME) [2] |
| **DOI** | 10.1109/ICSME58846.2023.00018 [2] |
| **Tipo** | Conference paper [2] |
| **Metodo** | Repository mining and framework development [1, 3, 4] |
| **Amostra** | 304 popular open source projects hosted on GitHub [3, 4] |
| **Contexto** | OSS (Open Source Software), including libraries, frameworks, and programming languages [1, 3, 5] |
| **Modo de trabalho** | Not specified |
| **Metodologia** | DevOps [6-8] |

---

## Objetivo

O objetivo principal do artigo é apresentar um framework agnóstico a projetos para operacionalizar e automatizar a medição das métricas **DORA** utilizando dados de telemetria do **git** e **GitHub**, superando as limitações de soluções proprietárias que exigem infraestruturas de nuvem específicas [1, 3, 7, 9].

---

## Questoes de Pesquisa

O artigo não lista questões de pesquisa explicitamente numeradas como RQ1 ou RQ2, mas foca na operacionalização das métricas, na criação de um dataset de 304 projetos e na análise da aplicabilidade e limitações da medição automática [3, 10-12].

---

## Metricas e Instrumentos de Avaliacao

| Metrica | Categoria | Nivel | Como Coletada | Validada |
|---------|-----------|-------|---------------|----------|
| **Deployment frequency** | Delivery (Throughput) | Team/Organization | Mined from git tags (semantic versioning) [13-15] | Yes [8, 13] |
| **Lead time for changes** | Delivery (Throughput) | Team/Organization | Mined from git commit and deployment timestamps [16-18] | Yes [8, 13] |
| **Mean time to recover** | Stability | Team/Organization | Mined from GitHub issue reports and deployment times [17, 19, 20] | Yes [8, 13] |
| **Change failure rate** | Stability | Team/Organization | Mined using SZZ algorithm to link bug-fixes to inducing commits [4, 17, 21, 22] | Yes [8, 13] |

---

## Frameworks e Metricas

### Frameworks Referenciados
- **DORA**: APPLIED (Base central para o framework de medição e benchmarking) [1, 8, 23, 24].
- **SPACE**: REFERENCED (Citado em relação à satisfação do desenvolvedor e produtividade) [25].
- **SZZ Algorithm**: APPLIED (Usado para identificar commits que induzem falhas) [22, 26, 27].

### Frameworks Propostos
O artigo propõe um framework que utiliza conceitos de **containment** (alcance de commits no grafo do git) e metadados do GitHub para calcular as quatro métricas DORA de forma automática e retroativa, sem depender de ferramentas de monitoramento de infraestrutura [7, 9, 28-30].

---

## Fatores que Influenciam Produtividade

### Fatores Positivos
| Fator | Categoria |
|-------|-----------|
| **Automation** (CI/CD, repository bots, templates) | Technical/Process [6, 31, 32] |
| **Continuous Delivery** | Process [9, 31, 33] |
| **Financial Support** (Funding) | Organizational [34, 35] |

### Fatores Negativos
| Fator | Categoria |
|-------|-----------|
| **Loss of key contributors** (Main contributor departure) | Human [24, 36] |
| **Bottlenecks in code review** | Process [37] |
| **Lack of standardized calculation** | Process [38, 39] |
| **Survey respondent bias** | Process [40, 41] |

---

## Papel da IA e Automacao

| Campo | Valor |
|-------|-------|
| Usa IA/ML? | Yes — utiliza o algoritmo **SZZ** para identificação de bugs e cita técnicas de Machine Learning em referências de suporte [22, 27, 42]. |
| Automacao de coleta? | Yes — o framework automatiza totalmente a extração de dados do git e GitHub [1, 7, 9, 28]. |
| Impacto de IA na produtividade? | Não avalia o impacto direto da IA na produtividade, mas demonstra como a automação da coleta de dados provê insights sobre a saúde do projeto [24, 35, 43]. |

---

## Resultados Principais

- A mediana da **Deployment Frequency** na amostra de 2021 foi de 24.5 deploys por ano [44].
- O **Lead Time for Changes** mediano foi de 24.9 dias [44].
- O **Mean Time to Recover** mediano foi de 95.2 dias [44].
- A **Change Failure Rate** mediana foi de 60.4% [44].
- 75.6% dos projetos foram classificados como "high performers" em frequência de deployment, mas 76.3% tiveram performance "low" em taxa de falha de mudança comparados aos benchmarks da DORA [45, 46].
- A frequência de deployment mostrou um aumento consistente entre 2013 e 2022 na amostra estudada [47, 48].

---

## Desafios do Uso das Metricas

- Falta de padronização no cálculo das métricas, dificultando benchmarks precisos [38, 39].
- Soluções proprietárias escondem detalhes de implementação (black box) [49, 50].
- Dificuldade em automatizar a definição de "falha" sem infraestrutura de monitoramento em nuvem [5, 51, 52].
- O algoritmo **SZZ** pode apresentar viés e produzir resultados imprecisos (falsos positivos/negativos) [26, 53].
- Dependência de documentação adequada no GitHub (ex: uso de "closes #issue") para vincular commits a falhas [11, 54].

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

- A definição de falha é muito inclusiva (qualquer bug fixado), o que pode inflar a **Change Failure Rate** [37, 51, 55].
- O framework foca apenas em falhas que foram efetivamente corrigidas [56, 57].
- A amostra de 304 projetos não é representativa de todos os projetos open source [58].
- Potencial imprecisão do algoritmo SZZ na identificação de commits indutores de erro [26, 53].

---

## Contribuicao Principal

A principal contribuição é um **framework reproduzível e agnóstico** para a medição automática das métricas DORA baseado em telemetria. Ele permite que projetos que não operam em ambientes de nuvem tradicionais (como bibliotecas e frameworks OSS) possam realizar benchmarking de sua performance de entrega de software e estabilidade de forma objetiva e histórica [1, 3, 9, 59].

---

*Extraido via NotebookLM em March 2026 para MLR: Software Developer Metrics in Practice*
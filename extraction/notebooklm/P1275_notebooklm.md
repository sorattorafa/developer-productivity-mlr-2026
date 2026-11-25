# P1275 — Framework of Software Developers Engagement Antecedents and Productivity - A Review

**Decisao: INCLUIDO | Qualidade: 3/5**

---

## Dados Bibliograficos

| Campo | Valor |
|-------|-------|
| **ID** | P1275 |
| **Autores** | Anwar Ali Milad Alsunki, Musab A. M. Ali, Adam Amril Jaharadak, Nooritawati Md Tahir |
| **Ano** | Not explicitly stated in source (references up to 2019) |
| **Venue** | Not specified in the source |
| **DOI** | Not specified |
| **Tipo** | Review article / Conference paper |
| **Metodo** | Literature review |
| **Amostra** | N/A (The paper reviews existing literature to propose a framework; mentions a planned future sample of 384 developers) |
| **Contexto** | Software development industry, with a focus on preparing for a study in Libya |
| **Modo de trabalho** | Not specified |
| **Metodologia** | Mentions Agile and Lean metrics in the literature review |

---

## Objetivo

O principal objetivo desta pesquisa é realizar uma revisão bibliográfica para identificar os fatores mais críticos para o engajamento de desenvolvedores e o aumento da produtividade em projetos de software [1]. O estudo busca investigar o comportamento humano em tarefas relacionadas ao local de trabalho e propor um framework abrangente que conecte os antecedentes do engajamento com a produtividade final [1, 2].

---

## Questoes de Pesquisa

*   **RQ1**: Quais são os fatores críticos para engajar desenvolvedores e aumentar a produtividade em projetos de software? [1]
*   **RQ2**: Como os fatores organizacionais, do ambiente de desenvolvimento, pessoais/grupais e de processo/projeto se associam ao engajamento e à produtividade? [3-7]
*   **RQ3**: Qual o impacto do engajamento/participação do desenvolvedor na produtividade de software? [7, 8]

---

## Metricas e Instrumentos de Avaliacao

| Metrica | Categoria | Nivel | Como Coletada | Validada |
|---------|-----------|-------|---------------|----------|
| Size-related metrics (ex: source code) | Productivity | Individual/Team | Tracking written code | No |
| Function-related metrics | Productivity | Individual/Team | Measuring useful functionality shipped | No |
| Job throughput | Delivery | Team | Amount of software finished in a sprint | No |
| Cycle time | Delivery | Team | Time taken to complete a cycle | No |
| Lead time | Maintainability/Delivery | Team | Time from request to delivery | No |
| Code protection (Coverage) | Maintainability | Team | Analysis during CI/CD | No |
| Bug prices (Rates) | Quality | Team | Bug tracking and cost of rectification | No |
| Velocity | Effectiveness | Team | Number of tasks completed vs. estimates | No |
| Uptime / Solution schedule | Activity | Team | System performance and adherence to deadlines | No |

---

## Frameworks e Metricas

### Frameworks Referenciados
- **Social Exchange Theory**: REFERENCED (Used to explain the balance between costs/efforts and rewards/benefits) [9, 10].
- **Theory of Work Adjustment (TWA)**: REFERENCED (Used to explain the connection between the individual and the work environment) [9, 11, 12].
- **CI/CD (Continuous Integration/Continuous Distribution)**: REFERENCED (In the context of maintainability metrics) [13].
- **Agile/Lean metrics**: REFERENCED (Used to evaluate efficiency and delivery) [14, 15].

### Frameworks Propostos
O artigo propõe um framework conceitual composto por **16 variáveis independentes** organizadas em quatro grupos: Fatores Organizacionais, Ambiente de Desenvolvimento, Características Pessoais e de Grupo, e Fatores de Processo e Projeto [1, 8]. O modelo teoriza que essas variáveis influenciam o engajamento do desenvolvedor, que por sua vez impacta positivamente a produtividade [8, 16].

---

## Fatores que Influenciam Produtividade

### Fatores Positivos
| Fator | Categoria |
|-------|-----------|
| Top Management Support | Organizational [4, 8] |
| Organizational Culture | Organizational [4, 8] |
| Extrinsic Motives (Rewards/Support) | Organizational [4, 10] |
| Use of Software Tools | Technical [5, 8] |
| Modern Development Practices | Process [5, 8] |
| Technical Ability | Human [6, 8] |
| Intrinsic Motives (Motivation/Attitude) | Human [6, 17] |
| Stakeholders Communication | Process [7, 8] |

### Fatores Negativos
| Fator | Categoria |
|-------|-----------|
| Inefficient Interface (UI/IDE) | Technical [18] |
| Changing Requirements | Process [13] |
| Project Complexity | Process [7] |
| Time spent on program understanding (70%) | Process [18] |
| Technical Debt | Technical [19] |

---

## Papel da IA e Automacao

| Campo | Valor |
|-------|-------|
| Usa IA/ML? | No |
| Automacao de coleta? | Yes — Mentions the use of software tools and CI/CD frameworks for metrics collection |
| Impacto de IA na produtividade? | Not applicable |

---

## Resultados Principais

*   Desenvolvedores gastam aproximadamente **70% do tempo na compreensão do programa** e apenas 5% editando código-fonte [18].
*   O engajamento é definido como um estado psicológico (envolvimento) e um conjunto de atividades (participação) [20].
*   Fatores de "status e oportunidade" têm o maior efeito no desempenho em projetos de código aberto (OSS), enquanto motivos intrínsecos podem não ter efeito direto [17].
*   A produtividade depende significativamente das **capacidades dos desenvolvedores** e das ferramentas/métodos utilizados [21].
*   O framework proposto identifica 16 variáveis distribuídas em 4 categorias principais que influenciam a produtividade via engajamento [8, 16].

---

## Desafios do Uso das Metricas

*   **Ausência de expertise**: Falta de conhecimento sobre como os desenvolvedores realmente gastam seu tempo e como o ambiente os afeta [22].
*   **Foco excessivo em tecnologia**: A literatura frequentemente foca apenas em aspectos técnicos (tamanho/complexidade) e negligencia o fator humano [22].
*   **Falha de métricas tradicionais**: Números associados a orçamento e cronograma falham em determinar a performance e produtividade real de equipes de design [14].
*   **Custo de erro**: Quanto mais tempo se leva para determinar um erro no código, maior o custo para retificá-lo [14].

---

## Avaliacao de Qualidade Metodologica

| Criterio | Pontuacao (0-2) |
|----------|----------------|
| Objetivo claramente definido | 2 |
| Metodologia adequada ao objetivo | 1 |
| Amostra/contexto descrito adequadamente | 1 |
| Ameacas a validade discutidas | 0 |
| Resultados com evidencia suficiente | 1 |
| Contribuicao clara para pratica ou teoria | 2 |
| **TOTAL** | **7/12** |

---

## Limitacoes

*   O estudo é predominantemente uma revisão de literatura e proposta teórica, carecendo de validação empírica imediata nos excertos fornecidos [2, 16].
*   O foco geográfico futuro é restrito a uma região específica (Líbia), o que pode limitar a generalização inicial dos resultados práticos [16, 23].
*   Baseia-se em auto-relatos e levantamentos qualitativos não aprofundados citados na literatura [22].

---

## Contribuicao Principal

A principal contribuição do artigo é a **proposição de um framework teórico integrador** que categoriza 16 antecedentes do engajamento do desenvolvedor (organizacionais, ambientais, pessoais e de processo) e estabelece sua relação hipotética com a produtividade de software, fundamentando-se na Social Exchange Theory e na Theory of Work Adjustment [1, 8, 9].

---

*Extraido via NotebookLM em March 2026 para MLR: Software Developer Metrics in Practice*
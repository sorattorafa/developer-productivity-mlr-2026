# P0093 — API Design and Development for Developer Payroll in Startups Based on Agile Productivity Factors

**Decisao: INCLUIDO | Qualidade: 4.5/5**

---

## Dados Bibliograficos

| Campo | Valor |
|-------|-------|
| **ID** | P0093 |
| **Autores** | Yang Agita Rindri, Rudy Hartanto, Ridi Ferdiana |
| **Ano** | 2018 (estimado com base nas referências e contexto acadêmico) |
| **Venue** | Não explicitado nos excertos (vinculado à Universitas Gadjah Mada) |
| **DOI** | Não disponível nos excertos |
| **Tipo** | Conference paper |
| **Metodo** | Mixed methods (Survey preliminar, Literature review, Case study, API Design and Implementation) |
| **Amostra** | Survey com 5 startups; 3 projetos de 3 startups diferentes para estudo de caso |
| **Contexto** | Industry (Software startups em ambiente Agile) |
| **Modo de trabalho** | Not specified |
| **Metodologia** | Agile |

---

## Objetivo

O objetivo principal deste trabalho é projetar e implementar uma Application Programming Interface (API) para o cálculo de folha de pagamento (payroll) de desenvolvedores em startups, utilizando parâmetros de produtividade ágil [1]. O estudo busca facilitar o desenvolvimento de sistemas de informação de folha de pagamento que considerem fatores além do tempo gasto, como experiência, papéis desempenhados, bugs e pontualidade [1, 2].

---

## Questoes de Pesquisa

O artigo não lista questões de pesquisa prefixadas com "RQ", mas foca em:
- Como formular e calcular o payroll de desenvolvedores de forma apropriada em startups [1]?
- Como os diferentes métodos de payroll afetam o salário final do desenvolvedor [3]?
- Como integrar fatores de produtividade ágil em uma ferramenta de software (API) [4]?

---

## Metricas e Instrumentos de Avaliacao

| Metrica | Categoria | Nivel | Como Coletada | Validada |
|---------|-----------|-------|---------------|----------|
| **Years of experience** | Productivity | Individual | Historical data / Survey | Partial (Cited) [5-7] |
| **Type of roles** | Human / Organizational | Individual | Expert judgement / Role Index | No [4, 8, 9] |
| **Number of bugs** | Quality | Individual | Historical data / Project logs | No [1, 4, 7] |
| **Timeliness (Days late)** | Delivery | Individual | Historical data / project tracking | No [1, 4, 7] |
| **Velocity** | Delivery | Team | Referenced from Scrum literature | Yes (Literature) [10, 11] |
| **Lines of Code (LoC)** | Activity | Individual | Referenced as irrelevant | Yes (Literature) [10, 12] |
| **Function Point** | Delivery | Individual | Referenced from literature | Yes (Literature) [10, 13] |
| **Cumulative time spent** | Activity | Individual | Referenced as conventional method | Yes (Literature) [5, 10] |

---

## Frameworks e Metricas

### Frameworks Referenciados
- **Agile Principle**: APPLIED — Base para os fatores de produtividade selecionados [5, 14].
- **GQM (Goal Question Metrics)**: REFERENCED — Citado como método para determinar métricas apropriadas [13, 15].
- **Scrum**: REFERENCED — Citado no contexto de medição de performance via velocity [10, 15].
- **XP (Extreme Programming)**: REFERENCED — Citado em relação a payroll em pair programming [16].

### Frameworks Propostos
O estudo propõe um **método de cálculo de payroll baseado em índices**, onde o salário líquido (Nett Payroll) é calculado subtraindo-se punições por bugs e atrasos de uma taxa horária que é ajustada por anos de experiência e urgência do papel desempenhado [7, 17]. Este método é implementado via **7 REST API resources** utilizando ASP.NET Web API [1, 18, 19].

---

## Fatores que Influenciam Produtividade

### Fatores Positivos
| Fator | Categoria |
|-------|-----------|
| Developer's years of experience | Human |
| Urgency of project team roles | Organizational |
| Qualifications and behavior (focus/activity) | Human |
| Ability to manage changing priority (Agile) | Process |

### Fatores Negativos
| Fator | Categoria |
|-------|-----------|
| Number of bugs generated | Technical / Quality |
| Task delay / Timeliness issues | Process |
| Developer turnover | Organizational |
| Salary inequality | Organizational / Human |

---

## Papel da IA e Automacao

| Campo | Valor |
|-------|-------|
| Usa IA/ML? | No — O sistema utiliza fórmulas estatísticas e lógicas de negócio fixas [17, 20]. |
| Automacao de coleta? | Yes — Utiliza Excel REST API para expor dados de execução de projeto armazenados no Office 365 [20]. |
| Impacto de IA na produtividade? | Not applicable |

---

## Resultados Principais

- Desenvolvimento bem-sucedido de **7 Payroll REST API resources** (Type of role, Team members, Project profile, User Stories, Project length estimation, Developer Payroll) [1, 18, 19].
- **100% de sucesso nos testes** das APIs realizados com a ferramenta POSTMAN [1, 21].
- O método proposto permite que desenvolvedores com a mesma função recebam salários diferentes com base na experiência [22, 23].
- O papel do Project Manager é identificado como o de maior índice de urgência (1.2), influenciando diretamente o cálculo da taxa horária [9, 23].
- Demonstração de que a desigualdade salarial em startups pode levar à rotatividade e queda de produtividade [12, 24, 25].

---

## Desafios do Uso das Metricas

- **Irrelevância de métricas tradicionais**: O uso de Lines of Code é considerado inadequado para o contexto atual, pois incentiva quantidade sem qualidade [11, 12].
- **Injustiça do tempo acumulado**: Usar apenas horas gastas é visto como um fator de produtividade "injusto" se não acompanhado de outros parâmetros [11].
- **Subjetividade no Expert Judgement**: A definição dos índices de papéis (index b) depende do julgamento de especialistas ou da organização, o que pode variar [8, 23].
- **Falta de transparência**: Métodos existentes em agências governamentais (SBU) não possuem transparência sobre os parâmetros utilizados [26].

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

- O foco do estudo é restrito a pequenas organizações (**startups**) [27].
- A gestão de projetos é limitada ao modelo **agile-based** com Work Breakdown Structure [27].
- Foram considerados apenas **quatro parâmetros** de performance do desenvolvedor [27].
- O estudo sobre a validade do método e a aceitação por parte das startups ainda estava em andamento no momento da publicação [21].

---

## Contribuicao Principal

A principal contribuição é o **desenvolvimento de uma API RESTful** que automatiza o cálculo de payroll integrando fatores de competência (experiência e papéis) e performance (pontualidade e qualidade do código) [1, 21]. O trabalho fornece uma ponte prática entre a teoria de métricas ágeis e a gestão financeira de startups, oferecendo uma ferramenta que pode reduzir o esforço administrativo enquanto promove uma remuneração baseada em mérito e produtividade [1, 2, 21].

---

*Extraido via NotebookLM em March 2026 para MLR: Software Developer Metrics in Practice*
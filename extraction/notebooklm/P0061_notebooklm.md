# P0061 — How Developers and Managers Define and Trade Productivity for Quality

**Decisao: INCLUIDO | Qualidade: 4.5/5**

---

## Dados Bibliograficos

| Campo | Valor |
|-------|-------|
| **ID** | P0061 [1] |
| **Autores** | Margaret-Anne Storey, Brian Houck, Thomas Zimmermann [1] |
| **Ano** | 2022 [2] |
| **Venue** | 15th International Conference on Cooperative and Human Aspects of Software Engineering (CHASE’22) [3, 4] |
| **DOI** | https://doi.org/10.1145/3528579.3529177 [4] |
| **Tipo** | Conference paper [3] |
| **Metodo** | Mixed methods (Exploratory survey study com análise qualitativa indutiva e testes estatísticos quantitativos) [5-9] |
| **Amostra** | 165 participantes (131 developers e 34 managers) [6, 10] |
| **Contexto** | Industry (Microsoft) [5, 6, 11] |
| **Modo de trabalho** | Not specified (estudo realizado em Jan/2020) [10] |
| **Metodologia** | Mixed (menciona Sprints, Integration cycles e MVPs) [12-15] |

---

## Objetivo

O objetivo principal do artigo é investigar como desenvolvedores e gestores definem os conceitos de **productivity** e **quality**, verificar o nível de alinhamento entre as visões desses dois grupos, entender se eles possuem consciência das perspectivas alheias e explorar se (e por que) realizam **trade-offs** entre qualidade e produtividade [5, 6, 11, 16].

---

## Questoes de Pesquisa

*   **RQ1:** How do developers and managers define **productivity?** How **aligned** are developers and managers in their definitions of productivity? [11].
*   **RQ2:** Do developers and managers **understand how the other cohort defines** productivity? [11, 17].
*   **RQ3:** How do developers and managers define **quality?** How **aligned** are developers and managers in their definitions? [17].
*   **RQ4:** Do developers and managers **trade** quality for productivity? What **reasons** do they give for trading or not trading quality for productivity? [17].

---

## Metricas e Instrumentos de Avaliacao

O artigo foca nas percepções sobre métricas, mas cita diversos indicadores utilizados ou mencionados pelos participantes:

| Metrica | Categoria | Nivel | Como Coletada | Validada |
|---------|-----------|-------|---------------|----------|
| Lines of code | Productivity | Individual | Telemetry/Engineering metrics | No (criticada por ser limitada) [18-20] |
| Pull Requests / Check-ins | Activity | Individual | Telemetry | No [21] |
| Number of tasks completed / iteration | Activity | Team | Survey/Telemetry | No [22] |
| Bug counts / Defects | Quality | Individual/Team | Telemetry | No [23, 24] |
| Time to market / Timeliness | Delivery | Organization | Process tracking | No [25, 26] |
| Test coverage | Quality | Team | Telemetry | No [26] |
| Flow state (uninterrupted work) | DevEx | Individual | Self-reported (Survey) | No [12, 27] |
| Customer satisfaction | Satisfaction | Organization | Survey/Feedback | No [23] |

---

## Frameworks e Metricas

### Frameworks Referenciados
*   **SPACE**: APPLIED. Utilizado como base para codificar as respostas sobre produtividade (Satisfaction, Performance, Activity, Collaboration, Efficiency) [28-31].
*   **GQM (Goal-Question-Metric)**: REFERENCED. Citado como abordagem clássica para definir métricas de qualidade [32].
*   **ISO Standards**: REFERENCED. Mencionado em relação à dificuldade de definir qualidade de forma absoluta [32].

### Frameworks Propostos
O artigo propõe o framework **TRUCE** para pensar em qualidade de software, baseado nas categorias que emergiram dos dados: **T**imely delivery, **R**obust features, **U**ser needs, **C**ollaboration enhancement, e **E**volution support [33, 34].

---

## Fatores que Influenciam Produtividade

### Fatores Positivos
| Fator | Categoria |
|-------|-----------|
| Ability to work without interruptions / Flow state | Human/Process [12, 35, 36] |
| Learning new skills | Human [22] |
| Peer support and useful feedback | Human/Social [37] |
| High job enthusiasm/satisfaction | Human [37] |

### Fatores Negativos
| Fator | Categoria |
|-------|-----------|
| Meetings and "meta-work" | Process [27, 36, 38] |
| Context switching / Randomization | Process [27, 39] |
| Legacy code | Technical [40, 41] |
| Tight deadlines / Pressure | Organizational [39, 42] |

---

## Papel da IA e Automacao

| Campo | Valor |
|-------|-------|
| Usa IA/ML? | No — O estudo utiliza métodos manuais de pesquisa e análise qualitativa [7, 10]. |
| Automacao de coleta? | No — Embora mencione o uso de telemetria nas empresas, os dados deste estudo foram coletados via survey manual [10, 43]. |
| Impacto de IA na produtividade? | Not applicable — Não foi foco desta pesquisa. |

---

## Resultados Principais

*   **Desalinhamento na Produtividade**: Desenvolvedores definem produtividade principalmente através de **Activity** (50%), enquanto gestores focam em **Performance** (67%) [36, 44].
*   **Percepção Falha**: Desenvolvedores não são precisos ao prever como seus gestores definem produtividade, frequentemente subestimando a importância da **Efficiency** para os managers [16, 45, 46].
*   **Alinhamento na Qualidade**: Ambos os grupos definem qualidade predominantemente como **Robustness** (>70%), seguida por **Evolvability** e **User Needs** [47-49].
*   **Trade-offs Frequentes**: 52% dos desenvolvedores e 59% dos gestores admitem trocar qualidade por produtividade, geralmente para cumprir prazos agressivos (**deadlines**) [50-52].
*   **Qualidade como Parte da Produtividade**: Cerca de um terço dos participantes recusa a ideia de trade-off, afirmando que entregar com baixa qualidade não é ser produtivo [41, 53, 54].

---

## Desafios do Uso das Metricas

*   **Atividades Invisíveis**: Atividades como ajudar colegas, planejar ou aprender não são capturadas por telemetria, gerando ansiedade nos desenvolvedores [43].
*   **Proxies Inadequadas**: O uso de métricas isoladas de engenharia (como linhas de código) é visto como mecânico e potencialmente prejudicial aos objetivos de longo prazo [18, 19].
*   **Falta de Discussão**: A ausência de conversas explícitas sobre o que os termos significam leva a suposições falsas e conflitos sobre como melhorar o processo [43, 55].

---

## Avaliacao de Qualidade Metodologica

| Criterio | Pontuacao (0-2) |
|----------|----------------|
| Objetivo claramente definido | 2 [5, 6] |
| Metodologia adequada ao objetivo | 2 [7, 11] |
| Amostra/contexto descrito adequadamente | 1 [10, 56] |
| Ameacas a validade discutidas | 2 [9, 56, 57] |
| Resultados com evidencia suficiente | 2 [12-15, 21, 22, 25-27, 36, 38-42, 44-46, 48, 49, 51, 52, 54, 58-82] |
| Contribuicao clara para pratica ou teoria | 2 [31, 34] |
| **TOTAL** | **11/12** |

---

## Limitacoes

*   **Generalização**: Realizado em apenas uma empresa (Microsoft), podendo não representar outras culturas organizacionais [9].
*   **Tamanho da Amostra**: O grupo de gestores foi relativamente pequeno, com baixa taxa de resposta (5%) [10, 56].
*   **Vieses de Survey**: Possibilidade de ambiguidade nas perguntas abertas e viés de resposta dos participantes [56].
*   **Subjetividade**: A codificação qualitativa é indutiva e pode variar entre diferentes pesquisadores [57].

---

## Contribuicao Principal

A principal contribuição do trabalho é a demonstração empírica de que **produtividade** e **qualidade** são lentes multidimensionais que frequentemente estão em tensão. O estudo introduz o framework **TRUCE** para qualidade e reforça o **SPACE** para produtividade, concluindo que o alinhamento explícito entre desenvolvedores e gestores sobre essas definições é um pré-requisito essencial antes da implementação de qualquer métrica de software na prática industrial [2, 34, 53, 83].

---

*Extraido via NotebookLM em March 2026 para MLR: Software Developer Metrics in Practice*
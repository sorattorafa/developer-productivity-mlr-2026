# P0181 — Code Today, Deadline Tomorrow: Procrastination Among Software Developers

**Decisao: INCLUIDO | Qualidade: 5/5**

---

## Dados Bibliograficos

| Campo | Valor |
|-------|-------|
| **ID** | P0181 |
| **Autores** | Zeinabsadat Saghi, Thomas Zimmermann, Souti Chattopadhyay |
| **Ano** | 2025 |
| **Venue** | International Conference on Software Engineering (ICSE) |
| **DOI** | 10.1109/ICSE55347.2025.00198 |
| **Tipo** | Conference paper |
| **Metodo** | Qualitative (Interview study, Qualitative coding, Inductive thematic analysis) |
| **Amostra** | 15 professional developers (11 men, 4 women) |
| **Contexto** | Industry: Software, Marketing, Insurance, Personal Finance, E-commerce, Automotive & Energy |
| **Modo de trabalho** | Mixed (Remote, Hybrid, In-person) |
| **Metodologia** | Not specified (References to Agile practices in context) |

---

## Objetivo

O objetivo principal deste artigo é realizar a primeira investigação detalhada sobre a **procrastinação entre desenvolvedores de software** [1]. O estudo busca identificar os fatores que desencadeiam esse comportamento, compreender seus efeitos (positivos e negativos) no trabalho do desenvolvedor e reunir estratégias práticas para mitigar seus impactos negativos [1, 2].

---

## Questoes de Pesquisa

*   **RQ1:** How does procrastination affect developer’s work? [3]
*   **RQ2:** What factors trigger developer’s procrastination at work? [3]
*   **RQ3:** How can developers manage procrastination? [3]

---

## Metricas e Instrumentos de Avaliacao

Embora o estudo seja qualitativo, ele utiliza dimensões do framework SPACE para categorizar os efeitos percebidos e menciona indicadores de desempenho citados pelos participantes [4, 5]:

| Metrica | Categoria | Nivel | Como Coletada | Validada |
|---------|-----------|-------|---------------|----------|
| **Performance Evaluation Ratings** | Performance | Individual | Perceived (Interview) | No |
| **Lines of Code** | Activity | Individual | Perceived (Interview) | No |
| **Story Points** | Activity | Individual | Perceived (Interview) | No |
| **Code Quality** | Quality | Individual | Perceived (Interview) | No |
| **Technical Debt** | Quality | Team | Perceived (Interview) | No |

---

## Frameworks e Metricas

### Frameworks Referenciados
*   **SPACE:** APPLIED (utilizado como base para agrupar os efeitos da procrastinação em cinco dimensões: satisfação, atividade, comunicação, performance e eficiência) [4].
*   **DevEx (Developer Experience):** REFERENCED (citado como contexto de importância do estudo) [6].
*   **Eisenhower Matrix:** REFERENCED (citado como técnica de gerenciamento) [7].
*   **SMART goals:** REFERENCED (citado como ferramenta para definição de metas) [7].

### Frameworks Propostos
O artigo não propõe um novo framework formal, mas apresenta uma **taxonomia de fatores de procrastinação** (Task-related, Personal, External) e um **conjunto de técnicas de mitigação** categorizadas [1, 8, 9].

---

## Fatores que Influenciam Produtividade

### Fatores Positivos (Percebidos como benefícios da procrastinação)
| Fator | Categoria |
|-------|-----------|
| **Taking Breaks** (Recuperação mental e física) | Human [10] |
| **Short Term Stress Relief** | Human [11] |
| **Better Creativity** (Tempo para reflexão e novas ideias) | Human/Process [12, 13] |
| **Avoiding Unnecessary Work** (Problemas que se resolvem sozinhos) | Process [12, 14] |
| **Near-deadline Efficiency** (Pico de produtividade sob pressão) | Human/Process [15, 16] |

### Fatores Negativos (Gatilhos e efeitos da procrastinação)
| Fator | Categoria |
|-------|-----------|
| **Emotional Distress** (Culpa, vergonha) | Human [17, 18] |
| **Task Vagueness** (Objetivos indefinidos) | Process [19, 20] |
| **More Technical Debt** | Technical [21] |
| **Strained Team Culture** (Reputação negativa) | Organizational [22] |
| **Cascading Delays** (Efeito dominó em sprints) | Process [23, 24] |
| **Dependency on Others** | Organizational [19, 25] |

---

## Papel da IA e Automacao

| Campo | Valor |
|-------|-------|
| Usa IA/ML? | **No** — O estudo é baseado em entrevistas humanas [26]. |
| Automacao de coleta? | **No** — Coleta manual via entrevistas semiestruturadas [26]. |
| Impacto de IA na produtividade? | O artigo discute o potencial de **AI-powered calendars** e **AI-based music recommenders** para ajudar desenvolvedores a manter o foco e gerenciar tarefas no futuro [7, 27]. |

---

## Resultados Principais

*   Foram identificados **15 efeitos negativos** e **8 efeitos positivos** da procrastinação no trabalho de desenvolvimento [1, 8, 28].
*   **Performance** foi a dimensão mais afetada negativamente, com 13 de 15 participantes relatando queda na qualidade do código ou atrasos na entrega [29].
*   Identificaram-se três categorias de gatilhos: **Task-related** (ex: falta de interesse, vagueza), **Personal** (ex: estado mental, medo de falhar) e **External** (ex: distrações, problemas de comunicação) [8, 19, 30].
*   O estudo categorizou três novos tipos de procrastinação para desenvolvedores: **Task Aversion**, **Task Avoidance** e **Strategic Procrastination** [31].
*   Foram compiladas **19 técnicas de mitigação**, focadas em Awareness, Task Focus, Task Planning e Team Support [1, 9].

---

## Desafios do Uso das Metricas

*   **Anti-padrão de "Last minute"**: A dependência da eficiência próxima ao prazo pode levar a código de baixa qualidade [29, 32].
*   **Recall Bias**: Dificuldade dos participantes em lembrar com precisão de experiências passadas de procrastinação durante as entrevistas [33].
*   **Recall vs. Reality**: O estudo baseia-se em efeitos *percebidos*, que podem não corresponder a métricas objetivas de telemetria [26, 33].

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

*   **Tamanho da amostra**: Apenas 15 participantes, o que limita a generalização para todos os desenvolvedores [33].
*   **Self-reported data**: Dependência de relatos pessoais, que podem ser influenciados por vieses de memória ou desejabilidade social [33].
*   **Complexidade Cognitiva**: Mecanismos cognitivos subjacentes à procrastinação não podem ser medidos apenas por entrevistas [33].
*   **Desbalanceamento da amostra**: Potenciais desequilíbrios em dados demográficos podem afetar a ressonância dos achados [33].

---

## Contribuicao Principal

A contribuição principal deste trabalho é o fornecimento da **primeira taxonomia estruturada dos fatores e efeitos da procrastinação na engenharia de software** [1, 34]. Ao identificar que a procrastinação não é meramente uma falha pessoal, mas frequentemente um sintoma de problemas organizacionais ou de definição de tarefas, o estudo oferece insights acionáveis para gestores e desenvolvedores, além de sugerir direções para futuras ferramentas de produtividade baseadas em autoconsciência e suporte de equipe [27, 34, 35].

---

*Extraido via NotebookLM em March 2026 para MLR: Software Developer Metrics in Practice*
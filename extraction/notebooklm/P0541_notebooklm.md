# P0541 — Understanding the Experience of Code Review: Misalignments, Attention, and Units of Analysis

**Decisao: INCLUIDO | Qualidade: 4/5**

---

## Dados Bibliograficos

| Campo | Valor |
|-------|-------|
| **ID** | P0541 |
| **Autores** | Emma Söderberg, Luke Church, Jürgen Börstler, Diederick Niehorster, Christofer Rydenfält [1] |
| **Ano** | 2022 [1, 2] |
| **Venue** | EASE 2022: The International Conference on Evaluation and Assessment in Software Engineering [2] |
| **DOI** | https://doi.org/10.1145/3530019.3530037 [3] |
| **Tipo** | Conference paper [2, 4] |
| **Metodo** | Mixed methods (Qualitative thematic analysis of semi-structured interviews and a Quantitative follow-up survey) [5-7] |
| **Amostra** | 12 interviewees and a survey with 78 started and 44 completed responses [7, 8] |
| **Contexto** | Industry (Two multi-national companies referred to as A and B) [7] |
| **Modo de trabalho** | Not specified (Interviews were conducted via video calls) [7] |
| **Metodologia** | Not specified (Teams mentioned working in an "agile way") [9] |

---

## Objetivo

O objetivo principal do artigo é investigar a experiência dos desenvolvedores no processo de code review, focando em como as ferramentas e processos apoiam ou dificultam as tarefas de revisão [5, 10]. Os autores buscam identificar desalinhamentos (misalignments) que prejudicam o ambiente de trabalho digital e propõem direções para futuras intervenções no design de ferramentas para melhorar a Developer Experience (DevEx) [5, 10].

---

## Questoes de Pesquisa

O artigo não lista formalmente as questões de pesquisa com prefixos RQ, mas define seus objetivos de exploração:
- Investigar a prática dos desenvolvedores e sua experiência no uso de ferramentas no processo de code review [10].
- Entender em que medida essas ferramentas auxiliam nas tarefas de revisão de código [10].
- Identificar e caracterizar desalinhamentos entre as tarefas de revisão e as ferramentas ou processos [6, 11].

---

## Metricas e Instrumentos de Avaliacao

| Metrica | Categoria | Nivel | Como Coletada | Validada |
|---------|-----------|-------|---------------|----------|
| Time spent on code reviews | Activity | Individual | Self-reported survey (hours per week/day) [12, 13] | No |
| Frequency of tool-task misalignments | DevEx | Individual | Self-reported survey (percentage of reviews) [14] | No |
| Disturbance level of misalignments | Satisfaction | Individual | Likert scale (1-7) in survey [15] | No |
| Years of practical experience | Activity | Individual | Self-reported survey [12, 13] | No |

---

## Frameworks e Metricas

### Frameworks Referenciados
- **Developer Experience (DevEx):** REFERENCED - O conceito central é usado para analisar a experiência do desenvolvedor no processo [5, 16, 17].
- **Cognitive Dimensions of Notations:** REFERENCED - Citado na discussão sobre coordenação e notações secundárias [18].
- **Thematic Analysis:** APPLIED - Usado para analisar os dados das entrevistas qualitativas [6, 19].

### Frameworks Propostos
O artigo não propõe um framework formal de métricas, mas apresenta uma **caracterização preliminar de desalinhamentos (misalignments)** dividida em categorias: Tool-Task Misalignment (Conversation, Information, Size) e Process-Task Misalignment (Responsibility, Completion) [11, 20, 21].

---

## Fatores que Influenciam Produtividade

### Fatores Positivos
| Fator | Categoria |
|-------|-----------|
| Small change size | Process |
| Automated style comments (linters/formatters) | Technical |
| Code navigation and syntax highlighting in IDEs | Technical |
| Knowledge sharing during reviews | Human |

### Fatores Negativos
| Fator | Categoria |
|-------|-----------|
| Tool-task misalignment (Information/Conversation/Size) | Technical/Process |
| Process-completion delays (time pressure) | Process |
| Large and complex code changes | Technical/Process |
| Lack of familiarity with the code base | Human |
| Boring and monotone nature of reviews | Human |
| Toxic or public negative feedback (causing insecurity) | Human/Process |

---

## Papel da IA e Automacao

| Campo | Valor |
|-------|-------|
| Usa IA/ML? | No — O estudo não utiliza ou avalia IA/ML diretamente [5, 7]. |
| Automacao de coleta? | No — Os dados foram coletados via entrevistas e survey manual [7, 22]. |
| Impacto de IA na produtividade? | Not applicable — O foco é em automação de estilo (linters) que reduz discussões triviais, mas pode conflitar com estilos individuais [23, 24]. |

---

## Resultados Principais

- **Desalinhamentos frequentes:** Os desenvolvedores enfrentam tool-task misalignments em média em cada quarta revisão de código (24.5%) [6, 14].
- **Desalinhamento de informação:** É o tipo mais comum, onde a ferramenta de revisão não provê o contexto necessário, forçando o desenvolvedor a migrar para a IDE [25-27].
- **Impacto no fluxo:** 22.6% dos respondentes consideram esses desalinhamentos perturbadores (disturbing) em seu trabalho [15, 26].
- **Obstáculos de processo:** O atraso na conclusão das revisões (process-completion) foi identificado como o principal obstáculo para a eficácia [28-30].
- **Percepção emocional:** Alguns desenvolvedores percebem o code review como uma tarefa "chata e monótona", o que afeta o engajamento [31, 32].

---

## Desafios do Uso das Metricas

- O estudo identifica que o uso de métricas de tamanho de mudança (lines of code) como "unidade de análise" muitas vezes não coincide com a "unidade de atenção" do revisor [33].
- **Anti-padrões identificados (referenciando literatura):** Confused reviewers, divergent reviews, low review participation, shallow reviews e toxic reviews [16, 34].
- A dificuldade em manipular conjuntos de mudanças (change sets) faz com que a unidade de análise seja determinada pelo "acaso" do percurso do desenvolvedor, em vez de ser otimizada para a revisão [35].

---

## Avaliacao de Qualidade Metodologica

| Criterio | Pontuacao (0-2) |
|----------|----------------|
| Objetivo claramente definido | 2 |
| Metodologia adequada ao objetivo | 2 |
| Amostra/contexto descrito adequadamente | 1 |
| Ameacas a validade discutidas | 2 |
| Resultados com evidencia suficiente | 1 |
| Contribuicao clara para pratica ou teoria | 2 |
| **TOTAL** | **10/12** |

---

## Limitacoes

- **Tamanho da amostra:** O número de entrevistas (12) e a taxa de resposta do survey (baixa em relação aos convites enviados) limitam a generalização [7, 36].
- **Viés de seleção:** Possível viés na seleção de participantes por contatos internos e auto-seleção no survey [36].
- **Foco em ferramentas específicas:** O estudo tem um viés para o uso do Gerrit, embora mencione GitHub e GitLab [37].
- **Experiência dos sujeitos:** Os participantes eram predominantemente experientes, o que pode não refletir os desafios de desenvolvedores novatos [37].

---

## Contribuicao Principal

A principal contribuição é a **caracterização dos desalinhamentos** entre tarefas, ferramentas e processos no code review, evidenciando que a rigidez das ferramentas atuais frequentemente falha em apoiar a "unidade de atenção" do desenvolvedor [20, 33, 38]. O estudo propõe que futuras ferramentas devem permitir maior controle sobre a unidade de análise e oferecer suporte visual para a coordenação de tarefas e diferentes níveis de atenção (detalhado vs. visão geral) [18, 33, 39].

---

*Extraido via NotebookLM em March 2026 para MLR: Software Developer Metrics in Practice*
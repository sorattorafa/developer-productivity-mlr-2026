# P0249 — The Work Life of Developers: Activities, Switches and Perceived Productivity

**Decisao: INCLUIDO | Qualidade: 5/5**

---

## Dados Bibliograficos

| Campo | Valor |
|-------|-------|
| **ID** | P0249 |
| **Autores** | André N. Meyer, Laura E. Barton, Gail C. Murphy, Thomas Zimmermann, Thomas Fritz [1] |
| **Ano** | 2017 [2] |
| **Venue** | IEEE Transactions on Software Engineering [2] |
| **DOI** | 10.1109/TSE.2017.2656886 [2] |
| **Tipo** | Journal article [2] |
| **Metodo** | Mixed methods (In situ background monitoring and Experience sampling/Diary study) [1, 3] |
| **Amostra** | 20 professional software developers (from an initial 24) [1, 4] |
| **Contexto** | Industry — 4 international companies in the USA, Canada, and Switzerland of varying sizes (from <10 to thousands of developers) [3, 5] |
| **Modo de trabalho** | Not specified (In situ study at the participants' computers) [1, 6] |
| **Metodologia** | Not specified [7] |

---

## Objetivo

O objetivo principal do artigo é investigar como desenvolvedores de software profissionais passam seu tempo de trabalho e como suas atividades e hábitos de trabalho se correlacionam com sua própria percepção de produtividade [1, 6]. Os autores buscam fornecer uma visão mais holística do trabalho do desenvolvedor, indo além de métricas de artefatos únicos para entender a fragmentação do trabalho e as diferenças individuais na produtividade [8, 9].

---

## Questoes de Pesquisa

*   **RQ1:** What does a developer’s work day look like? [2]
*   **RQ2:** How fragmented is a developer’s work? [7]
*   **RQ3:** Are there observable trends in how developers perceive their productivity? [7]
*   **RQ4:** What is the relationship between developers’ activity and perceived productivity at work? [7]

---

## Metricas e Instrumentos de Avaliacao

| Metrica | Categoria | Nivel | Como Coletada | Validada |
|---------|-----------|-------|---------------|----------|
| Perceived Productivity | Productivity/Satisfaction | Individual | Experience sampling (pop-up survey using a 7-point Likert scale) [10, 11] | Yes (based on established study methods) [10, 11] |
| User Input (Keystrokes/Mouse clicks) | Activity | Individual | Background monitoring application (logging event timestamps) [12, 13] | Yes (factual logging) [12, 13] |
| Hours Active | Activity | Individual | Calculated from computer usage logs (excluding inactive periods > 2 min) [14, 15] | Yes [15] |
| Activity Duration (e.g., Coding, Email) | Activity | Individual | Semi-automated mapping of active window titles and process names every 10 seconds [16-18] | Yes (manual check of samples) [17, 19] |
| Activity Switches | Activity | Individual | Frequency of transitions between different activity categories [18, 20] | Yes [20] |
| Number of Self-Reported Tasks | Delivery | Individual | Experience sampling (participants listed tasks performed in the last session) [10, 11, 21] | Partial (subjective reporting) [22] |
| Inactive Periods (Breaks) | Activity | Individual | Identification of lapses in input (short < 15 min, long > 15 min) [23, 24] | Yes [23] |

---

## Frameworks e Metricas

### Frameworks Referenciados
- **Personal Software Process (PSP):** REFERENCED (cited as a method for individual improvement through metrics) [25, 26].
- **Pomodoro Technique:** REFERENCED (discussed as a potential design approach for productivity tools) [27].

### Frameworks Propostos
O artigo não propõe um framework formal de métricas, mas desenvolve **explanatory models** baseados em **stepwise linear regression** para descrever fatores individuais que contribuem para a percepção de produtividade [28, 29].

---

## Fatores que Influenciam Produtividade

### Fatores Positivos
| Fator | Categoria |
|-------|-----------|
| User input rate (Keystrokes and Mouse Clicks) | Human/Technical [9, 30] |
| Number of self-reported tasks (for some individuals) | Human/Process [29, 31] |
| Getting into "the flow" state | Human [32] |
| Completing short context switches during waiting times | Process [33] |

### Fatores Negativos
| Fator | Categoria |
|-------|-----------|
| Email (reading and writing) | Organizational/Process [9, 30] |
| Planned meetings | Organizational/Process [9, 30] |
| Work unrelated web browsing | Human/Process [9, 30] |
| Idle time (unaccounted computer inactivity) | Human/Process [30] |
| High work fragmentation/Frequent activity switches | Process [9, 20, 34] |
| Longer session durations (for some individuals) | Human [21] |

---

## Papel da IA e Automacao

| Campo | Valor |
|-------|-------|
| Usa IA/ML? | No — The study uses linear and logistic regression for data analysis and predictive modeling, but not as part of the software development process itself [28, 35]. |
| Automacao de coleta? | Yes — Activity data (window titles, inputs) was automatically collected by a background monitoring application every 10 seconds [1, 12]. |
| Impacto de IA na produtividade? | Not explicitly findings on IA impact, but the authors suggest using predictive models to automate availability status and reduce interruptions [27]. |

---

## Resultados Principais

*   O trabalho do desenvolvedor é altamente fragmentado: com exceção de reuniões, eles permanecem em uma atividade por apenas **0.3 a 2 minutos** antes de trocar [9, 20].
*   Desenvolvedores passam em média apenas **metade do tempo** de seu dia de trabalho ativos no computador (média de 4.3 horas ativas em um span de 8.4 horas) [15, 36].
*   A percepção de produtividade é um assunto **altamente pessoal**; nenhum modelo único de fatores explicou a produtividade de todos os participantes [9, 31].
*   Participantes podem ser agrupados em ritmos de produtividade: **morning people** (20%), **afternoon people** (40%) e **low-at-lunch people** (35%) [6, 37].
*   Um alto volume de **user input** (teclado e mouse) correlacionou-se positivamente com a produtividade para a maioria, enquanto **e-mails e reuniões** tiveram impacto negativo [9, 30].
*   Foi possível prever sessões de alta/baixa produtividade com uma precisão média de **0.57 e 0.56** respectivamente usando apenas dados de uso do computador [38].

---

## Desafios do Uso das Metricas

*   **Subjetividade das tarefas:** Há grande variação no que desenvolvedores definem como "tarefa" e sua granularidade, dificultando a comparação entre indivíduos [22, 39].
*   **Limitação de artefatos únicos:** Métricas tradicionais (como SLOC ou function points) capturam apenas uma pequena parte do trabalho e falham em fornecer uma visão holística [25, 40, 41].
*   **Privacidade e ética:** A coleta de dados detalhados de atividade gera preocupações de privacidade; o uso obrigatório por gestores pode levar ao "gaming" das métricas por medo de pressão ou demissão [42, 43].
*   **Atividades fora do computador:** Ferramentas automáticas podem falhar em capturar colaborações offline e reuniões não registradas [19, 44].

---

## Avaliacao de Qualidade Metodologica

| Criterio | Pontuacao (0-2) |
|----------|----------------|
| Objetivo claramente definido | 2 [2, 7] |
| Metodologia adequada ao objetivo | 2 [3] |
| Amostra/contexto descrito adequadamente | 2 [5, 45] |
| Ameacas a validade discutidas | 2 [46] |
| Resultados com evidencia suficiente | 2 [13] |
| Contribuicao clara para pratica ou teoria | 2 [41, 47] |
| **TOTAL** | **12/12** |

---

## Limitacoes

*   **Restrição de Plataforma:** O estudo foi limitado a usuários do sistema operacional Windows [48, 49].
*   **Duração do Estudo:** O período de monitoramento de duas semanas pode não capturar todas as fases ou iterações de um projeto [50].
*   **Viés de Autorelato:** A percepção de produtividade é subjetiva e depende da memória e honestidade do participante durante o experience sampling [46].
*   **Atividades Offline:** Embora mitigado por relatos manuais, o sistema de monitoramento não captura automaticamente ações fora do computador [44].

---

## Contribuicao Principal

A contribuição principal deste trabalho é a demonstração empírica de que a produtividade de desenvolvedores de software é um fenômeno **altamente individual e rítmico** [9, 47, 51]. Ao correlacionar logs de atividade detalhados com autorelato de percepção, o estudo revela padrões de fragmentação extrema no trabalho contemporâneo e propõe que futuras ferramentas de suporte devem ser **personalizadas** aos hábitos e ciclos de produtividade únicos de cada desenvolvedor para facilitar o estado de "flow" [27, 41, 47].

---

*Extraido via NotebookLM em March 2026 para MLR: Software Developer Metrics in Practice*
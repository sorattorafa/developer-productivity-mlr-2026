# P2130 — How human and organizational factors influence software teams productivity in covid-19 pandemic: A brazilian survey

**Decisao: INCLUIDO | Qualidade: 4.5/5**

---

## Dados Bibliograficos

| Campo | Valor |
|-------|-------|
| **ID** | P2130 |
| **Autores** | Carla I. M. Bezerra, José Cezar de Souza Filho, Emanuel F. Coutinho, Alice Gama, Ana Lívia Ferreira, Gabriel Leitão de Andrade, Carlos Eduardo Feitosa [1, 2] |
| **Ano** | 2020 [2, 3] |
| **Venue** | 34th Brazilian Symposium on Software Engineering (SBES ’20) [2] |
| **DOI** | 10.1145/3422392.3422417 [2, 3] |
| **Tipo** | Conference paper [2] |
| **Metodo** | Survey (Mixed methods: quantitative descriptive statistics and qualitative Grounded Theory coding) [4-6] |
| **Amostra** | 58 valid software development team members in Brazil [7-9] |
| **Contexto** | Industry — Brazilian software development companies across all Brazilian regions (Northeast: 31, Southeast: 11, North: 8, Midwest: 4, South: 4; 91.4% in small teams of 0–20 people) [7, 9, 10] |
| **Modo de trabalho** | Remote (Work from home during COVID-19 pandemic; prior to pandemic: 41 full-time on-site, 14 hybrid, 3 remote) [7, 11, 12] |
| **Metodologia** | Not specified (investigates roles, experience, team size, and tools, but does not state specific Agile/DevOps/Waterfall distributions) [12-14] |

---

## Objetivo

The main objective of this study is to analyze how human and organizational factors (such as work environment, individual experience, team collaboration, remote communication, motivation, emotional health, and company assistance) influence the productivity of software development teams in Brazilian companies operating in a remote environment during the COVID-19 pandemic [4, 7, 8, 15].

---

## Questoes de Pesquisa

- **RQ1**: How has the remote work environment affected the productivity of software teams during the COVID-19 pandemic? [16]
- **RQ2**: How has experience and individual skills of software teams influence productivity in a remote environment during the COVID-19 pandemic? [17]
- **RQ3**: How has organization and collaboration among software team members been occurring in a remote environment during the COVID-19 pandemic? [17]
- **RQ4**: How was remote communication performed by software teams during the COVID-19 pandemic and what influence did it have on productivity? [18]
- **RQ5**: What is the influence of remote work on the motivation and emotional of software teams during the COVID-19 pandemic? [18]
- **RQ6**: How have software companies assisted their employees in remote work to ensure good productivity during the COVID-19 pandemic? [19]
- **RQ7**: What influence does remote work have on the overall productivity of software teams during the COVID-19 pandemic? [19]

---

## Metricas e Instrumentos de Avaliacao

| Metrica | Categoria | Nivel | Como Coletada | Validada |
|---------|-----------|-------|---------------|----------|
| Perceived Individual Productivity | Productivity | Individual / Team | Self-reported survey questionnaire (4-point scale: unsatisfactory, regular, good, excellent; Q28, Q29) [20-22] | Partial (survey instrument validated via pilot study & expert review) [10, 23] |
| Team Collaboration | Collaboration | Team | Self-reported survey questionnaire (8-point Likert scale: 1 = not very collaborative to 8 = very collaborative; Q14) [24, 25] | Partial (survey instrument validated via pilot study & expert review) [10, 23] |
| Ease of Remote Communication | Collaboration / Communication | Team | Self-reported survey questionnaire (8-point Likert scale: 1 = difficult communication to 8 = easy communication; Q17) [26, 27] | Partial (survey instrument validated via pilot study & expert review) [10, 23] |
| Developer Motivation | Satisfaction / Human | Individual | Self-reported survey questionnaire (8-point Likert scale: 1 = not very motivated to 8 = very motivated; Q21) [28, 29] | Partial (survey instrument validated via pilot study & expert review) [10, 23] |
| Team Turnover Rate | Activity / Organizational | Team | Self-reported survey questionnaire (8-point Likert scale: 1 = low turnover to 8 = high turnover; Q15) [26, 30] | Partial (survey instrument validated via pilot study & expert review) [10, 23] |
| Task Time Distribution | Delivery / Process | Team | Self-reported survey questionnaire (4-point scale: unsatisfactory, regular, good, excellent; Q12) [24, 31] | Partial (survey instrument validated via pilot study & expert review) [10, 23] |

---

## Frameworks e Metricas

### Frameworks Referenciados
- **Grounded Theory (GT) (Corbin & Strauss)**: REFERENCED & APPLIED — used to systematically code qualitative survey responses into open and axial categories [5, 6].
- **Survey Guidelines (Mólleri et al.)**: REFERENCED & APPLIED — used to guide survey design, pilot testing, and reporting [4, 10].
- **Empirical Threats to Validity Guidelines (Wohlin et al.)**: REFERENCED & APPLIED — used to assess conclusion, construct, internal, and external validity [23, 32, 33].
- **Literature Reviews on Productivity Factors (Canedo & Santos; Machuca-Villegas & Gasca-Hurtado; Oliveira et al.)**: REFERENCED — used to select and classify human and organizational factors [15, 34-36].
- *Note*: Frameworks such as DORA, SPACE, DevEx, GQM, HEART, or OKR are not referenced or applied in this paper.

### Frameworks Propostos
The paper does not propose a formal metric framework, but develops a qualitative conceptual model via Grounded Theory linking categories of human/organizational factors (External Interruption, Adaptation, Emotional, Discipline, Task, Communication, Time, Displacement, and Assistance) to team productivity [37-42].

---

## Fatores que Influenciam Produtividade

### Fatores Positivos
| Fator | Categoria |
|-------|-----------|
| Practitioner experience and individual skills (maturity, commitment, readiness to help, self-management) [38, 43, 44] | Human |
| High developer motivation (84.5% feel motivated) [7, 29, 45] | Human |
| High team collaboration and cohesion (93.1% rate team as collaborative) [25, 45] | Human |
| Easy remote communication (84.5% report easy communication) [7, 27, 45] | Process / Human |
| Elimination of daily commute/displacement (saves travel time and reduces daily traffic stress) [42, 46, 47] | Organizational / Human |
| Working hour flexibility and task execution autonomy [47, 48] | Organizational / Process |
| Dedicated/reserved home work environment [41, 47, 49] | Technical / Organizational |
| Adoption of effective communication & collaboration tools (video conferencing, chat, file sharing) [27, 39, 50] | Technical / Process |
| Provision of company support (laptops, monitors, courses, and financial assistance) [40, 51, 52] | Organizational |

### Fatores Negativos
| Fator | Categoria |
|-------|-----------|
| External interruptions in the home environment (family, children, noise pollution, domestic tasks) [7, 11, 37, 53] | Human / Organizational |
| Workspace adaptation difficulties (lack of quiet, private, or ergonomic work space) [41, 49, 53] | Technical / Organizational |
| Adverse emotional and psychological impacts (anxiety, tiredness/exhaustion, apprehension, fear, isolation) [7, 29, 54, 55] | Human |
| Excessive remote meetings causing fatigue and lack of focus/concentration [52, 56] | Process / Human |
| Lack of company assistance/equipment (46.6% received no financial or material support) [21, 51] | Organizational |
| High team turnover (reported by 13.7% of participants, leading to project knowledge loss) [30, 57] | Organizational |
| Team health issues and COVID-19 infection impacting project monitoring and sprint deliveries [48, 54] | Human |
| Asynchronous communication delays and time management difficulties [50, 56] | Process |

---

## Papel da IA e Automacao

| Campo | Valor |
|-------|-------|
| Usa IA/ML? | No — the paper does not use or evaluate AI or Machine Learning techniques [4, 5, 7]. |
| Automacao de coleta? | No — survey data was collected manually via online questionnaires and coded manually using Grounded Theory [4-6, 13]. |
| Impacto de IA na produtividade? | Not evaluated — AI tools and AI impact on productivity were not addressed [4, 7]. |

---

## Resultados Principais

- **Overall Perceived Productivity**: 74.1% of participants reported good (58.6%) or excellent (15.5%) productivity during remote pandemic work, 20.7% reported regular productivity, and 5.2% unsatisfactory productivity [7, 22, 45].
- **Prior Remote Work Experience**: 60.5% of participants who worked full-time on-site prior to the pandemic had no previous remote work experience [49].
- **Work Environment**: 67.2% possessed a reserved workspace at home, whereas 32.8% did not; 43.1% reported that living with family members affected their routine [49].
- **Main Productivity Disruptors**: External interruptions, workspace adaptation, and emotional issues were identified as the primary negative factors affecting productivity [7, 37, 45].
- **Team Collaboration & Cohesion**: 93.1% of respondents rated their software team as collaborative [25, 45].
- **Communication & Tooling**: 84.5% reported easy communication [7, 27, 45]. Video conferencing was used by 96.55% (top tools: Google Meet [20] and MS Teams [10]), email by 87.93%, chat apps by 77.59% (WhatsApp [14], Telegram [7]), and file sharing/collaboration tools by 67.24% (Slack [58], Discord [2], Jira [7], GitLab [7]) [27].
- **Motivation & Mental Health**: 84.5% felt motivated [7, 29, 45], but negative emotions were widespread: anxiety (36), tiredness/exhaustion (35), apprehension (30), fear (27), and irritation (17) [29].
- **Healthcare Maintenance**: 56.9% practiced healthy eating, 37.93% exercised at home, 27.59% sunbathed, 18.97% practiced meditation, and 12.07% used remote psychological therapy; 15.5% engaged in no healthcare activities [54].
- **Company Support**: 53.4% received company assistance (laptops [14], professional courses [34], monitors [45], financial aid [2]), while 46.6% received no material or financial assistance [51].
- **Commute Elimination**: Eliminating travel time significantly reduced stress and wasted time, resulting in direct positive impacts on developer well-being and productivity [46, 47].

---

## Desafios do Uso das Metricas

- **Reliance on Subjective Perceptions**: Productivity was measured solely via self-reported subjective ratings rather than objective metrics (e.g., repository commits, velocity, code churn) [4, 20, 22].
- **Meeting Fatigue & Over-monitoring**: An excessive volume of remote meetings was reported, leading developers to multi-task across concurrent meetings and lose focus on primary tasks [52, 56].
- **Task Estimation Challenges**: 29.3% rated task time distribution as regular or unsatisfactory, highlighting difficulties in adjusting project delivery estimation in remote settings [31].
- **Asynchronous Communication Overhead**: Asynchronous interaction led to higher energy expenditure, slower task resolution, and increased effort for time management [50, 56].
- **Turnover & Knowledge Drain**: High turnover in 13.7% of teams created friction in maintaining project knowledge and ongoing productivity [30].

---

## Avaliacao de Qualidade Metodologica

| Criterio | Pontuacao (0-2) |
|----------|----------------|
| Objetivo claramente definido | 2 |
| Metodologia adequada ao objetivo | 2 |
| Amostra/contexto descrito adequadamente | 2 |
| Ameacas a validade discutidas | 2 |
| Resultados com evidencia suficiente | 2 |
| Contribuicao clara para pratica ou teoria | 1 |
| **TOTAL** | **11/12** |

---

## Limitacoes

- **Sample Size & Regional Distribution**: The sample size of 58 participants is relatively small and concentrated mainly in the Northeast (31) and Southeast (11) regions, limiting statistical power and cross-region comparisons [9, 10, 33].
- **Lack of Generalizability**: Results cannot be generalized across all software project domains, larger enterprises, or differing organizational contexts [33].
- **Subjective Data**: The study relies on personal opinions and self-reported perceptions, which are subject to individual bias [4, 32].
- **Specific Pandemic Context**: Data collection occurred during a short window (May 12–31, 2020) under strict crisis isolation, reflecting emergency remote work rather than standard remote work arrangements [9, 11, 32].

---

## Contribuicao Principal

The main contribution of this paper is an empirical analysis of how human and organizational factors impacted Brazilian software development teams during their emergency transition to remote work in the COVID-19 pandemic [7, 8, 57]. By combining quantitative survey data with qualitative Grounded Theory coding, the study demonstrates that while software developers generally maintained high perceived productivity, motivation, and collaboration, key productivity bottlenecks stemmed from home environment distractions, emotional strain, excessive meetings, and lack of company equipment or financial support [7, 37, 45, 52, 56, 57]. The authors synthesize actionable recommendations for companies, emphasizing investment in ergonomic work kits, healthcare support, turnover reduction, and structured remote communication protocols [45, 52, 57].

---

*Extraido via NotebookLM em October 2026 para MLR: Software Developer Metrics in Practice*

---
💡 **Nudge**: Would you like me to create a tailored summary report or slide deck synthesizing these findings across your literature review sources?
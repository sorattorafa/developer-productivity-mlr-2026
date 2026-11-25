# P2033 — Adoption of AI Assisted Coding – Cognitive Barriers, Motivational Factors and Productivity Gains

**Decisao: INCLUIDO | Qualidade: 4.6/5**

---

## Dados Bibliograficos

| Campo | Valor |
|-------|-------|
| **ID** | P2033 [1] |
| **Autores** | Dhiraj SM Varanasi, Y. Raghu Reddy, Sandip Potdar, Himanshu S Warudkar [1] |
| **Ano** | 2026 [2] |
| **Venue** | Innovations in Software Engineering Conference (ISEC 2026) [2] |
| **DOI** | 10.1145/3796563.3796601 [2] |
| **Tipo** | Conference paper [2] |
| **Metodo** | Mixed methods (Quantitative Survey and Qualitative Semi-structured Interviews) [1, 3] |
| **Amostra** | Survey: 1,029 total participants (999 consented, 699 completed responses; 505 licensed, 194 non-licensed) [4, 5]; Interviews: 19 qualitative interviews across 7 role categories [1, 6] |
| **Contexto** | Industry — Global capability center / technology development arm of a large multinational financial and investment organization (HSBC Software Development India) [1, 5] |
| **Modo de trabalho** | Not specified |
| **Metodologia** | Not specified |

---

## Objetivo

This paper investigates the enterprise adoption of Microsoft GitHub Copilot (GHCP) within the technology development arm of a major multinational financial organization [1, 7]. The primary objective is to evaluate developer adoption patterns, motivational factors, cognitive barriers, and productivity impacts across various stages of the Software Development Life Cycle (SDLC), providing evidence-based recommendations for integrating AI coding assistants into enterprise workflows [1, 8, 9].

---

## Questoes de Pesquisa

- **RQ1**: What are the challenges in adopting code-assisting tools in various stages of SDLC and at what stages software engineers make most use of GHCP? [9]
- **RQ2**: Can GHCP replace/supplement specific parts of SDLC and when is GHCP least preferred? [9]
- **RQ3**: How to enable adopters to use GHCP? [9]
- **RQ4**: Why do stakeholders stop using GHCP? [9]
- **RQ5**: What processes should be included in practice, according to the participants, to ensure an easy/smooth adoption of GHCP? [9]

---

## Metricas e Instrumentos de Avaliacao

| Metrica | Categoria | Nivel | Como Coletada | Validada |
|---------|-----------|-------|---------------|----------|
| **Perceived Productivity Gain** | Productivity | Individual / Team | Heuristic estimation via survey and qualitative interviews (15–40% gain, up to 60% time saved on specific tasks) [10] | No |
| **JIRA Story Points & Task Velocity** | Delivery | Team | Internal sprint tracking compared against pre-adoption baselines [10] | Partial |
| **Pull Request (PR) Completion Rate** | Activity / Delivery | Individual / Team | Cited from baseline industry literature (7.5% to >20% increase) and internal observation [11] | Yes |
| **Code Suggestion Accuracy Rate** | Quality | Individual | Self-reported developer estimation during interviews (60–100% depending on complexity; 70–80% for JUnit tests) [12, 13] | No |
| **Documentation Time Savings** | DevEx / Productivity | Individual / Team | Developer estimates during semi-structured interviews (20–30% time reduction) [14] | No |
| **UTAUT2 Adoption Constructs (\\(R^2 = 0.184\\))** | DevEx / Adoption | Individual | Structured Likert-scale survey analyzed using Partial Least Squares Structural Equation Modeling (PLS-SEM) [15-18] | Yes |

---

## Frameworks e Metricas

### Frameworks Referenciados
- **UTAUT2 (Unified Theory of Acceptance and Use of Technology 2)**: **APPLIED** — Used as the foundational measurement model to structure survey questions and evaluate key constructs via PLS-SEM (Performance Expectancy, Effort Expectancy, Social Influence, Facilitating Conditions, Age, Experience) [15, 17, 19].
- **TAM (Technology Acceptance Model)**: **REFERENCED** — Evaluated during initial survey ideation [3].
- **TAM2, TAM3, UTAUT, DOI, TPB, TTF, MPCU, SCT, TRA, Expectancy Theory, TOE, CBAM, IS Success Model**: **REFERENCED** — Evaluated and compared in a comparative matrix to justify selecting UTAUT2 for technology acceptance [4, 15, 16].

### Frameworks Propostos
- **Enterprise Human-in-the-Loop Adoption Model**: A 6-pillar framework for AI assistant adoption: (1) Position as a Complementary Tool, (2) Streamline Training and Onboarding, (3) Establish Clear Guidelines for Data Sensitivity, (4) Leverage Peer Influence and Community Sharing, (5) Implement a Phased Integration Approach, and (6) Continuously Measure Impact and Refine Practices [20, 21].

---

## Fatores que Influenciam Produtividade

### Fatores Positivos
| Fator | Categoria |
|-------|-----------|
| Real-time code completion and syntax autocompletion [8, 12, 22] | Technical |
| IDE Chat plugin replacing multi-iteration web searches (Google/StackOverflow) [14, 23, 24] | Process |
| Automated unit test case generation (e.g., JUnit 70–80% accuracy) [13, 25] | Technical |
| Automated legacy code & SQL migration (Java 7 to 8, Teradata to BigQuery, DataStage to Spark/Airflow, Mulesoft to Spring Boot) [13] | Technical |
| Automatic code documentation and inline comment generation [14, 26] | Technical / Process |
| Integration with internal tools (e.g., JIRA user story rephrasing, script generation for StarUML) [26] | Process |
| Peer endorsements and manager recommendations (Social Influence, \\(\beta = 0.226\\)) [17, 20, 27] | Human / Organizational |
| Structured organizational learning resources (9-hour Degreed pathway, cheat sheets, internal video sessions) [20, 28, 29] | Organizational |

### Fatores Negativos
| Fator | Categoria |
|-------|-----------|
| Over-reliance risking erosion of fundamental problem-solving and critical thinking skills [25, 30, 31] | Human |
| Inaccurate or context-blind code suggestions requiring manual verification overhead [12, 32, 33] | Technical |
| Data privacy and security concerns regarding sensitive code exposure in editor contexts [25, 34] | Organizational / Technical |
| Lack of prompt engineering skills and difficulty translating vague management requirements [12, 25, 35] | Human |
| High developer self-efficacy / confidence reducing perceived need for AI tools (negative PE path, \\(\beta = -0.111\\)) [17, 36, 37] | Human |
| Unrealistic management expectations assuming AI can replace human expertise without consequences [32, 37] | Organizational / Human |
| Excessive volume and fragmentation of training materials causing information overload [23, 29] | Organizational |

---

## Papel da IA e Automacao

| Campo | Valor |
|-------|-------|
| **Usa IA/ML?** | Yes — Evaluates Microsoft GitHub Copilot (LLM-driven real-time code completion and conversational chat assistant) [1, 7]. |
| **Automacao de coleta?** | No — Data was collected via manual electronic survey distribution and semi-structured interview sessions; objective telemetry logging was excluded due to strict enterprise PII policies [5, 6, 16]. |
| **Impacto de IA na produtividade?** | Heuristic perceived productivity increase of 15% to 40% (saving up to 60% of task time), 20–30% reduction in documentation effort, and a 30–40% boost in overall team productivity fostered by early adopter knowledge sharing [10, 14, 38]. |

---

## Resultados Principais

- **Developer Activities**: Out of 699 survey completers, Copilot was most heavily utilized for Code Completion (534), Coding/Implementation (505), Code Reviews (460), Code Refactoring (429), and Testing (379) [5, 39].
- **PLS-SEM Adoption Drivers**: Among unlicensed developers, the UTAUT2 model accounted for 18.4% of variance (\\(R^2 = 0.184\\)) in adoption behavior [18]. Social Influence (\\(\beta = 0.226\\)) and Effort Expectancy (\\(\beta = 0.141\\)) positively drove usage intention [17, 40]. Performance Expectancy displayed a negative relationship (\\(\beta = -0.111\\)), showing that highly self-confident coders perceive less need for AI assistance [17, 36].
- **Suggestion Accuracy**: Code completion accuracy ranged from 60% to 100% depending on task complexity (100% for simple tasks, 70–80% for high complexity, and 70–80% for JUnit test cases) [12, 13].
- **Feature Utilization**: Code Completion and Chat were widely used, while advanced features (PR Summaries, CLI, Workspace, Extensions, Custom Models) saw minimal or restricted usage due to security governance [22].
- **Role of Expertise**: Subject Matter Experts (SMEs) extracted higher value from Copilot than beginners because SMEs could properly prompt, direct, and validate outputs, whereas beginners risked over-relying on incorrect suggestions [41].

---

## Desafios do Uso das Metricas

- **Inability to Collect Granular Telemetry**: Organizational data privacy and PII compliance mandates forced the removal of individual user identifiers, preventing direct tracking of objective code commit or telemetry metrics [6, 16].
- **Disconnect from Corporate Metrics**: Team-level heuristic indicators (e.g., JIRA story point velocity) did not map directly to standardized enterprise-wide productivity frameworks [10].
- **Perception & Subjectivity Bias**: Productivity findings relied heavily on self-reported survey responses and interview heuristics rather than automated metric pipelines [10, 42].
- **Management Misalignment Anti-Pattern**: Non-technical management developing unrealistic expectations that AI assistants can accelerate delivery without human code validation [32, 37].

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

- **Privacy & Anonymization Constraints**: Discarding PII to meet compliance standards prevented the collection of granular, objective, individual-level metric logs [6, 16].
- **Subjective / Heuristic Measurement**: Primary reliance on developer self-reports and semi-structured interview estimations rather than automated telemetry [10, 42].
- **Exploratory Model Fit (\\(R^2 = 0.184\\))**: The PLS-SEM model explained 18.4% of variance, leaving unmeasured psychological or contextual factors for future studies [18, 36].
- **Single Enterprise Context**: Conducted within a single financial services firm (HSBC Technology India), which may affect generalizability to startups or open-source domains [1, 5, 42].
- **Security-Driven Feature Restrictions**: Restricted access to custom AI models and workspace context limited the scope of features evaluated [22].

---

## Contribuicao Principal

The paper presents an empirical, multi-phase mixed-methods study evaluating GitHub Copilot adoption across nearly 1,000 developers and 19 qualitative interviews within a highly regulated global financial institution [1, 4, 6]. By applying the UTAUT2 framework via PLS-SEM, it demonstrates that peer influence and ease of use are primary adoption drivers, whereas high developer self-efficacy can paradoxically reduce perceived AI utility [17, 36, 40]. Furthermore, it provides a 6-pillar practical enterprise roadmap that positions GenAI coding assistants as human-in-the-loop "pair programmers" supported by structured training, data security protocols, and phased feature integration [1, 20, 21, 43].

---

*Extraido via NotebookLM em October 2026 para MLR: Software Developer Metrics in Practice*
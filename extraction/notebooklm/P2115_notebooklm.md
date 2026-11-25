# P2115 — Software development teams: factors influencing their productivity

**Decisao: INCLUIDO | Qualidade: 4.5/5**

---

## Dados Bibliograficos

| Campo | Valor |
|-------|-------|
| **ID** | P2115 |
| **Autores** | Verónica A. Bollati, Germán Gaona, Paula B. Lima, Liliana Cuenca Pletsch [1, 2] |
| **Ano** | 2023 [1] |
| **Venue** | 21st LACCEI International Multi-Conference for Engineering, Education, and Technology [1] |
| **DOI** | Not specified in paper text (LACCEI proceedings placeholder) [3] |
| **Tipo** | Conference paper [1, 3] |
| **Metodo** | Systematic Literature Review (SLR) [4, 5] |
| **Amostra** | 35 primary studies analyzed (out of 1,223 raw results, 434 unique papers screened, and 85 candidate primary studies) [6-8] |
| **Contexto** | Academic SLR on Agile Software Development Teams [4, 9] |
| **Modo de trabalho** | Not specified (analyzes studies covering On-site/Collocated, Remote, Distributed, and Global Virtual Teams) [10-12] |
| **Metodologia** | Agile (Scrum, XP, Management 3.0, Kanban, Lean, Crystal Clear) [13-16] |

---

## Objetivo

This paper presents a systematic literature review (SLR) aimed at identifying and analyzing the socio-cultural factors that influence the productivity and performance of agile software development teams [4, 9, 17]. It categorizes these factors into dimensions, evaluates their specific impacts on productivity, and investigates whether existing literature proposes adaptations or strategies for agile practices in the presence of these factors [4, 17, 18].

---

## Questoes de Pesquisa

- **RQ1**: What are the socio-cultural factors and their influence on the productivity of agile development teams? [17]
- **RQ2**: How do agile practices adapt to the existence of these factors? [19]

---

## Metricas e Instrumentos de Avaliacao

| Metrica | Categoria | Nivel | Como Coletada | Validada |
|---------|-----------|-------|---------------|----------|
| Customer Satisfaction & Value Delivery | Productivity | Team / Organization | Stakeholder requirements feedback & Agile principles evaluation | Yes [20] |
| Team Velocity | Productivity | Team | Agile project tracking & sprint reporting | Yes [21] |
| Tasks Delivered on Time & Stakeholder Alignment | Activity / Delivery | Individual / Team | Project manager perception surveys & deliverable reviews | Partial [22] |
| Workload per Developer Ratio | Activity / Productivity | Individual | Task assignment tracking & capacity modeling | Partial [23] |
| Code Quality & Architecture (Rework Avoidance) | Quality | Team / Artifact | Code reviews, static analysis, rework tracking | Yes [24, 25] |
| Technical Debt Impact | Quality / DevEx | Team | Codebase maintenance effort analysis & developer morale surveys | Yes [26] |
| Teamwork Quality (TWQ) | Collaboration | Team | Empirical survey questionnaires & replication case studies | Yes [10, 27, 28] |
| Communication Patterns (Centralized vs. Small-World) | Collaboration | Team | Interaction network logging & Kanban process analysis | Yes [29] |
| Developer Tenure & Project Turnover | Activity / Human | Team | Mining open-source repositories (e.g., GitHub) & HR tracking | Yes [29, 30] |

---

## Frameworks e Metricas

### Frameworks Referenciados
- **Scrum**: REFERENCED (discussed as providing daily stand-ups, retrospectives, sprint planning, and proposal boards to improve communication, trust, work environment, and psychological safety) [12, 15, 28, 31].
- **Extreme Programming (XP)**: REFERENCED (discussed for open communication, customer co-location, TDD, continuous integration, simple design, and refactoring) [12, 16, 25, 32].
- **Management 3.0**: REFERENCED (discussed as a leadership model for empowering teams, enhancing soft skills, motivation, shared goals, and self-organization) [13, 33-35].
- **Kanban**: REFERENCED (discussed in studies examining team communication patterns such as centralized vs. small-world networks) [29, 36].
- **Crystal Clear**: REFERENCED (discussed for reflective improvement sessions, psychological safety, and automated test environments) [15, 22, 37].
- **Heart of Agile**: REFERENCED (discussed for practices focused on direct and honest communication) [16, 38].
- **Lean**: REFERENCED (discussed in studies analyzing how developers experience continuous adaptation of team performance) [27, 39, 40].

### Frameworks Propostos
The paper does not propose a new metric framework; instead, it presents an adapted **4-dimensional classification framework** (Organizational, Team, Individual, Process)—adapted from Chow & Cao (2008)—to categorize socio-cultural factors extracted from the literature [14, 41, 42].

---

## Fatores que Influenciam Produtividade

### Fatores Positivos
| Fator | Categoria |
|-------|-----------|
| Open, direct, and frequent face-to-face communication | Human / Process [12, 16, 43] |
| Psychological safety, vulnerability tolerance, and mutual trust | Human [15, 30, 31] |
| Team co-location and close physical proximity | Technical / Process [12, 44] |
| Shared mental models, shared team vision, and common goals | Human / Organizational [33, 45] |
| High teamwork quality, team cohesion, and mutual prestige | Human [40, 46] |
| Team empowerment, self-organization, and decision-making authority | Organizational / Process [33, 47, 48] |
| Diversity in skills, expertise, tenure, and gender | Human / Organizational [29, 48] |
| Customer involvement and fast feedback loops (e.g., in agile testing) | Process / Organizational [43, 49, 50] |
| Strong executive support and agile organizational culture | Organizational [51, 52] |
| Support for individual training, career paths, rewards, and knowledge sharing | Human / Organizational [53, 54] |
| High technical capabilities, domain expertise, and self-efficacy | Human / Technical [34, 55, 56] |
| Feature prioritization (delivering core value first) and high code quality | Technical / Process [24, 49] |
| Small-world communication patterns (in Kanban) | Process / Human [29] |

### Fatores Negativos
| Fator | Categoria |
|-------|-----------|
| Geographic and temporal dispersion among team members | Organizational / Process [12, 44, 57] |
| High technical debt (negatively affects code maintenance and developer morale) | Technical [26] |
| Poor physical work conditions, lack of social interaction, and unfair competition | Organizational / Human [28] |
| Absence of psychological safety and fear of expressing discordant views | Human / Organizational [30] |
| High personnel turnover / rotation (both internal and external) | Organizational / Human [35, 46] |
| Subgroup formation, friction, and lack of intercultural understanding | Human [45, 47] |
| Unbalanced geographic distribution across sites (smaller sites feeling ignored) | Organizational / Human [57] |
| Inadequate remote work infrastructure and communication tools | Technical / Organizational [38, 58] |
| Excessive time pressure, task boredom, and lack of individual recognition | Human [34, 56] |
| Centralized communication patterns | Process / Human [29] |

---

## Papel da IA e Automacao

| Campo | Valor |
|-------|-------|
| **Usa IA/ML?** | No — the paper does not use or evaluate AI/ML models [4, 5]. |
| **Automacao de coleta?** | No — data selection and extraction were executed manually across 5 digital databases using search strings [5, 18, 59]. |
| **Impacto de IA na produtividade?** | Not evaluated — the paper does not address AI tools or their impact on development productivity [4, 17]. |

---

## Resultados Principais

- **Dominance of Interaction Factors**: Factors related to member interactions—specifically communication, physical/perceptual distance, and team organization—exert the strongest impact on team productivity [4, 60, 61].
- **Impact of Individual & Soft Skills**: Soft skills, individual motivation, self-efficacy, technical expertise, and psychological safety significantly dictate overall team performance [34, 56, 60-63].
- **Organizational Alignment & Support**: Strong executive support, agile cultural alignment, personnel management (e.g., minimizing turnover), and project characteristics are vital determinants [35, 51, 52, 64-66].
- **Scarcity of Adaptation Strategies**: Out of 35 analyzed primary studies, almost none propose formal strategies to adapt agile practices to socio-cultural factors (only 2 studies noted minor practice adjustments, such as involving clients in testing [50] and adding a JIRA plugin for early feedback [67]) [62, 68-70].
- **Literature Quality Gap**: Out of 85 candidate primary studies meeting inclusion criteria, only 35 (41.18%) passed the quality threshold (>75%), indicating that much of the published literature lists productivity factors without sufficiently analyzing their concrete impact [7, 8].

---

## Desafios do Uso das Metricas

- **Overemphasis on Deliverables over Value**: Managers frequently focus on output artifacts and task completion rather than continuous customer value creation [22, 24, 25].
- **Superficial Factor Identification**: Much of the literature identifies productivity factors in isolation without evaluating their actual operational impact or providing mitigation strategies [8, 69, 71].
- **Centralized Communication Anti-Pattern**: Relying on centralized communication structures in agile team settings negatively affects iteration performance and code quality [29].
- **Neglect of Human & Emotional Dimensions**: Traditional metric systems capture technical activity while failing to account for team morale, psychological safety, and technical debt [26, 30].
- **Process Fidelity vs. Teamwork**: Strictly following methodology guidelines without building team trust, good teamwork, and open communication fails to yield expected productivity gains [25, 61].

---

## Avaliacao de Qualidade Metodologica

| Criterio | Pontuacao (0-2) |
|----------|----------------|
| Objetivo claramente definido | 2 [17] |
| Metodologia adequada ao objetivo | 2 [5, 59, 72] |
| Amostra/contexto descrito adequadamente | 2 [6-8, 10] |
| Ameacas a validade discutidas | 1 [70] |
| Resultados com evidencia suficiente | 2 [8, 14, 41, 42, 73, 74] |
| Contribuicao clara para pratica ou teoria | 2 [61, 66, 70, 75, 76] |
| **TOTAL** | **11/12** |

---

## Limitacoes

- **Exclusion of Grey Literature**: The review excluded informal sources (such as tech blogs and industry forums) where real-world agile practice adaptations are predominantly published [67, 70].
- **Title and Abstract Search Scope**: Search string queries were restricted to titles and abstracts, which may have omitted studies discussing factors only within the full text [77].
- **Exclusion of Google Scholar**: Google Scholar was excluded to prevent duplicate results, which may have led to missing non-indexed or emerging conference publications [59].
- **Database & Language Limits**: Search was limited to English-language papers indexed in IEEE Xplore, SpringerLink, ScienceDirect, ACM Digital Library, and Scopus [59, 78].

---

## Contribuicao Principal

This paper contributes a systematic synthesis of socio-cultural productivity factors in agile software development, categorizing them across four structural dimensions (Team, Individual, Organizational, and Process) [4, 14, 42, 79]. Its key insight is that team interaction, communication, and psychological safety exert the primary influence on productivity, while uncovering a major academic gap: the lack of validated strategies and concrete adaptations for agile frameworks to address these socio-cultural dynamics in practice [61, 62, 68, 70].

---

*Extraido via NotebookLM em October 2026 para MLR: Software Developer Metrics in Practice*

---

💡 **Next Steps**: Would you like me to create a formatted PDF report or slide deck based on this extracted summary, or conduct further web research on agile adaptation strategies?
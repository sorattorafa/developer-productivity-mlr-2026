# P2119 — Factors influencing productivity of agile software development teamwork: A qualitative system dynamics approach

**Decisao: INCLUIDO | Qualidade: 4.5/5**

---

## Dados Bibliograficos

| Campo | Valor |
|-------|-------|
| **ID** | P2119 |
| **Autores** | Israt Fatema, Kazi Sakib [1] |
| **Ano** | 2017 [2] |
| **Venue** | 2017 24th Asia-Pacific Software Engineering Conference (APSEC) [2] |
| **DOI** | 10.1109/APSEC.2017.95 [3] |
| **Tipo** | Conference paper [2, 3] |
| **Metodo** | Mixed methods (Literature review, semi-structured interviews, questionnaire survey, and qualitative System Dynamics / Causal Loop Diagram) [1, 4, 5] |
| **Amostra** | 12 key project members interviewed (from 4 companies); survey with 17 respondents (1 per software company) out of 25 invited companies in Bangladesh [5-7] |
| **Contexto** | Industry (Software development companies in Bangladesh, including offshore and local software markets) [2, 6, 8] |
| **Modo de trabalho** | Not specified (mentions offshore client interaction, time differences, and collocation used by 9/17 companies, but exact remote/hybrid setup is not specified) [9, 10] |
| **Metodologia** | Agile (100% Scrum) [10, 11] |

---

## Objetivo

The objective of this paper is to identify and analyze the factors influencing agile teamwork productivity using a qualitative System Dynamics (SD) approach [1]. The study aims to understand the complex interdependencies and underlying causal structures at the team's perception level that affect software development productivity over time in agile environments [8, 12, 13].

---

## Questoes de Pesquisa

The paper does not explicitly state formal research questions with RQ1/RQ2 labels; however, it addresses three core investigative goals:
- **Goal 1**: What are the major factors perceived by team members to influence agile teamwork productivity [1, 8]?
- **Goal 2**: What are the primary reasons for agile project failures in software companies [1, 9]?
- **Goal 3**: How do team dynamics, soft factors, and management practices interact feedback-wise to impact actual team productivity over time [8, 12, 13]?

---

## Metricas e Instrumentos de Avaliacao

| Metrica | Categoria | Nivel | Como Coletada | Validada |
|---------|-----------|-------|---------------|----------|
| Timeliness (Pontualidade/Prazos) | Delivery | Team | Management assessment & perception survey [9, 13] | Partial |
| Work Quality (Qualidade do Trabalho) | Quality | Team | Management assessment & perception survey [9, 13, 14] | Partial |
| Quantity (Quantidade de Saida / SLOC / Function Points) | Activity | Individual/Team | Traditional quantitative count / Management assessment [9, 13, 15] | No |
| Customer Satisfaction (Satisfacao do Cliente) | Satisfaction | Organization/Team | Client feedback & management criteria [1, 9, 13] | Partial |
| Staff Turnover Rate (Taxa de Rotatividade) | DevEx / Organizational | Team/Organization | Survey frequency analysis [16] | No |
| Software Reuse Level (Nivel de Reuso de Software) | Process / Activity | Team | Survey frequency analysis [16] | No |

---

## Frameworks e Metricas

### Frameworks Referenciados
- **Input-Process-Output (IPO) Model**: REFERENCED (cited from Melo et al. to analyze team productivity factors) [3, 12].
- **Sociotechnical System Framework**: REFERENCED (cited from Dingsøyr et al. regarding human and technical entity interaction) [12].
- **Abdel-Hamid System Dynamics Model**: REFERENCED (adapted as the base theoretical model where Actual Productivity = Potential Productivity - Losses due to faulty processes) [12, 17].

### Frameworks Propostos
- **Qualitative System Dynamics / Causal Loop Diagram (CLD) Model for Agile Teamwork Productivity**: The paper proposes an empirical Causal Loop Diagram that models the interrelated soft factors (motivation, team management efficiency, team effectiveness, skillfulness, customer satisfaction) and feedback loops (exhaustion from schedule pressure, communication overhead) influencing actual team productivity [1, 13, 17, 18].

---

## Fatores que Influenciam Produtividade

### Fatores Positivos
| Fator | Categoria |
|-------|-----------|
| Communication (Comunicacao eficaz) [9, 19, 20] | Human / Process |
| Coordination (Coordenacao de equipe) [9, 19, 20] | Process / Human |
| Mutual Trust & Team Orientation (Confianca mutua e orientacao de equipe) [19, 20] | Human |
| Feedback & Backup Behaviour (Feedback continuo e comportamento de suporte) [19, 20] | Process / Human |
| Project Management Efficiency & Team Leadership (Eficiencia de gestao e lideranca) [1, 13, 19, 20] | Organizational / Process |
| Motivation (Motivacao da equipe) [1, 7, 13, 19, 20] | Human |
| Staffing & Skillfulness (Alocacao de pessoas qualificadas e capacidade tecnica) [13, 16, 17, 19] | Organizational / Technical |
| Working Environment & Rewards (Ambiente de trabalho e recompensas) [17, 19, 20] | Organizational / Human |
| Team Learning & Adaptability (Aprendizado de equipe e adaptabilidade) [17, 19, 20] | Process / Human |
| Customer Satisfaction (Satisfacao do cliente) [1, 9, 13] | Organizational |

### Fatores Negativos
| Fator | Categoria |
|-------|-----------|
| Lack of Management Support (Falta de suporte da gestao) [1, 9, 11] | Organizational |
| Schedule Pressure & Exhaustion (Pressao de prazo e exaustao/burnout) [14, 17, 20] | Process / Human |
| Communication & Coordination Overhead (Sobrecarga de comunicacao e coordenacao) [14, 17] | Process / Human |
| Resource Constraints (Restricoes de recursos) [17, 20] | Technical / Organizational |
| External Dependencies (Dependencias externas) [17, 20] | Process / Technical |
| Cultural & Language Barriers (Barreiras culturais e de idioma em projetos offshore) [9, 17, 21] | Human / Organizational |
| Unwillingness & Lack of Agile Experience (Resistencia a mudanca e falta de experiencia ágil) [9, 11] | Human / Process |

---

## Papel da IA e Automacao

| Campo | Valor |
|-------|-------|
| Usa IA/ML? | No — The paper does not evaluate or incorporate Artificial Intelligence or Machine Learning [1, 5, 6]. |
| Automacao de coleta? | No — Data collection was conducted manually via semi-structured interviews and survey forms [5-7]. (Continuous Integration and Automated Builds are noted as software practices, not data collection tools) [10, 11]. |
| Impacto de IA na produtividade? | Not applicable — Not evaluated in this study [1, 5]. |

---

## Resultados Principais

- **Top productivity factors**: Agile team members perceive **Communication** (mean 2.82/3), **Staffing** (2.76), **Mutual Trust** (2.76), **Feedback** (2.70), **Coordination** (2.70), **Project Management** (2.58), and **Motivation** (2.58) as the most influential factors driving teamwork productivity [9, 19, 20].
- **Primary cause of failure**: **10 out of 17 software companies** identified **lack of management support** as the main reason for failed agile projects, followed by team unwillingness (5/17), insufficient training (4/17), lack of cultural transition (3/17), and lack of agile experience (3/17) [9, 11].
- **Productivity assessment criteria**: Management primarily evaluates productivity using **Customer Satisfaction** (11/17 companies), **Timeliness** (10/17), **Quality** (10/17), and **Quantity** (5/17) [9, 13].
- **Agile practices adoption**: **Daily Standup** is used by all 17 companies (100%), followed by Continuous Integration (12/17), Retrospectives (11/17), User Stories (11/17), Collocation (9/17), Continuous Deployment (9/17), Refactoring (9/17), and Release Planning (9/17) [9-11].
- **Demographics**: 100% of companies run **Scrum**; 47.8% have 1–2 years of agile experience, 41.2% have 2–5 years, and 11.8% have over 5 years [10, 11].
- **Causal dynamics**: The qualitative CLD illustrates that schedule pressure leads to exhaustion, diminishing developer motivation and productivity, while increased workforce size introduces communication overhead that offsets potential productivity unless team effectiveness and training are supported [14, 17, 18].

---

## Desafios do Uso das Metricas

- **Inadequacy of traditional quantitative metrics**: Knowledge-intensive agile tasks produce intangible outputs where counting Source Lines of Code (SLOC) or Function Points per unit time/cost fails to reflect actual developer productivity [15].
- **Misalignment between team perceptions and management metrics**: Agile developers view productivity through "soft factors" (dynamics, motivation, coordination), whereas management continues to assess performance based on timeliness and deliverable volume [1, 9, 13].
- **Flaws of individual productivity measurement**: Evaluating developers individually ignores team interdependencies and cooperative feedback loops [3, 12].
- **Offshore coordination challenges**: Managing cultural differences, time zone gaps, and language barriers creates friction in offshore agile teamwork [9, 21].
- **Transition hurdles**: Transitioning to self-managing agile teams requires mindset shifts that are frequently hindered by lack of management support and inadequate training [9, 11, 21].

---

## Avaliacao de Qualidade Metodologica

| Criterio | Pontuacao (0-2) |
|----------|----------------|
| Objetivo claramente definido | 2 [1, 8] |
| Metodologia adequada ao objetivo | 2 [4, 5, 13] |
| Amostra/contexto descrito adequadamente | 2 [5, 6, 10, 11] |
| Ameacas a validade discutidas | 1 [7, 14] |
| Resultados com evidencia suficiente | 2 [9, 11, 19, 22] |
| Contribuicao clara para pratica ou teoria | 2 [12, 13, 18, 23] |
| **TOTAL** | **11/12** [1, 7, 14] |

---

## Limitacoes

- **Sample size constraints**: The survey sample was limited to 17 responses (1 per company) and 12 interviewees across 17 software companies due to time constraints [7].
- **Subjective perception bias**: Findings rely on self-reported survey and interview perceptions rather than objective automated metric collection [7].
- **Qualitative CLD scope**: The proposed model is strictly qualitative and does not include quantitative stock-and-flow differential equations, exact delay parameters, or full simulation validation [14, 24].
- **Geographic generalizability**: Data collection was limited to Bangladeshi software companies with heavy offshore outsourcing focus, which may affect generalizability to other regional industry settings [2, 7-9].

---

## Contribuicao Principal

The main contribution of this study is the development of an empirical, qualitative System Dynamics model (Causal Loop Diagram) that captures the complex feedback relationships among "soft factors"—such as team management efficiency, motivation, customer satisfaction, team effectiveness, and developer skillfulness—in agile software teams [1, 13, 17, 18]. By moving beyond static input-process-output models, the research highlights how operational pressures create negative feedback loops (e.g., schedule pressure leading to exhaustion and diminished motivation) [14, 17, 18]. Furthermore, it provides industrial evidence demonstrating that lack of team management support is perceived as the primary driver of agile project failures [9, 11].

---

*Extraido via NotebookLM em October 2026 para MLR: Software Developer Metrics in Practice*

---
💡 **Nudge**: Would you like me to generate a slide deck or visual summary synthesizing these agile productivity factors and causal loops?
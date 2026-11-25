# P2077 — Bridging the Gap: A Data-Driven Analysis of How Traditional Software Engineering Productivity Metrics Overlook Women's Performance [1]

**Decisao: INCLUIDO | Qualidade: 4.5/5** [1, 2]

---

## Dados Bibliograficos

| Campo | Valor |
|-------|-------|
| **ID** | P2077 [1] |
| **Autores** | Lorena M. V. Seabra, Pamela T. L. Bezerra [1] |
| **Ano** | 2025 [3] |
| **Venue** | Not specified (CESAR School / SBC Event Format) [1] |
| **DOI** | Not specified [1] |
| **Tipo** | Conference paper / Technical report [1] |
| **Metodo** | Mixed methods (Survey — Quantitative and Qualitative) [4, 5] |
| **Amostra** | 85 female software engineers across Brazil [1, 3, 4] |
| **Contexto** | Industry / Professional software engineering in Brazil [3, 4] |
| **Modo de trabalho** | Not specified [3] |
| **Metodologia** | Agile (Sprint velocity context) / Not specified [6, 7] |

---

## Objetivo

The main objective of the paper is to examine how traditional software engineering productivity metrics neglect female developers' contributions and gender-specific experiences through a quantitative and qualitative analysis [1, 4]. Based on a survey of 85 female software engineers across Brazil, the study aims to reveal how conventional evaluation models overlook collaborative, cognitive, and supportive work, and to support the design of more equitable and inclusive evaluation frameworks [1, 4].

---

## Questoes de Pesquisa

- **RQ1**: "What are the limitations of existing productivity metrics in software engineering concerning female developers?" [8]
- **RQ2**: "What additional factors, based on female developers' experiences, should be included in productivity measures?" [8]

---

## Metricas e Instrumentos de Avaliacao

| Metrica | Categoria | Nivel | Como Coletada | Validada |
|---------|-----------|-------|---------------|----------|
| Lines of Code (LOC) [6, 9] | Activity / Productivity | Individual | Automated repository mining / IDE counting [6] | No [7] |
| Commit Frequency [6, 9] | Activity / Productivity | Individual | Version control system (Git) logging [6] | No [7] |
| Sprint Velocity [6, 9] | Delivery / Productivity | Team / Individual | Agile project management tools (e.g., Jira) [6, 7] | Partial [7] |
| Defect Resolution Rate [6] | Quality / Productivity | Individual / Team | Issue tracking systems [6] | Partial [7] |
| Peer Feedback (Limited Scope) [9] | Satisfaction / DevEx | Individual | Qualitative surveys / Performance reviews [9, 10] | Partial [9, 10] |
| Mentorship / Onboarding [9] | Collaboration / Human | Individual / Team | Self-reported survey / Untracked formally [9, 11] | No [11, 12] |
| Documentation / Process Improvement [9] | Activity / Quality | Individual / Team | Self-reported survey / Untracked formally [9, 11] | No [11, 12] |

---

## Frameworks e Metricas

### Frameworks Referenciados
- No specific standard framework (e.g., DORA, SPACE, DevEx, GQM) is explicitly named; the paper cites classic software engineering metrics literature (e.g., McConnell 2004, Fenton & Pfleeger 1998, Storey et al. 2017) [6, 7, 10, 13].

### Frameworks Propostos
- The paper does not propose a formal quantitative framework, but presents six preliminary guidelines for inclusive evaluation: incorporating qualitative metrics, enabling peer/team feedback, diversifying performance criteria, acknowledging non-promotable tasks, considering work-life dynamics, and fostering transparency and co-creation [14-16].

---

## Fatores que Influenciam Produtividade

### Fatores Positivos
| Fator | Categoria |
|-------|-----------|
| Mentorship and knowledge sharing [17, 18] | Human / Process |
| Code review and debugging [17] | Technical / Quality |
| Architectural decisions and creative problem-solving [17] | Technical / Process |
| Collaboration, communication, and team alignment [17, 19] | Human / Process |
| Emotional labor and team support [16, 18] | Human |
| Comprehensive documentation and maintainable code [18, 20] | Technical / Process |
| Structured peer and team feedback loops [10, 15] | Organizational / Process |

### Fatores Negativos
| Fator | Categoria |
|-------|-----------|
| Over-reliance on quantitative metrics (LOC, commits, sprint velocity) [6, 7, 21] | Process / Organizational |
| Workplace gender bias and undervaluation of performance [22-24] | Organizational / Human |
| Workplace microaggressions (frequent interruptions in meetings and reviews) [23, 25, 26] | Human / Organizational |
| Assignment to non-promotable or low-visibility tasks [22, 25, 27] | Organizational / Process |
| Exclusion from major technical decisions and high-visibility projects [21, 26] | Organizational / Human |
| Double workload and domestic responsibilities [23, 25, 28] | Human / Organizational |
| Physiological impacts (hormonal variations, menstrual cycle, migraines) [28, 29] | Human |

---

## Papel da IA e Automacao

| Campo | Valor |
|-------|-------|
| **Usa IA/ML?** | No — the study uses descriptive statistical analysis and thematic qualitative analysis of survey data [23, 30]. |
| **Automacao de coleta?** | No — survey responses were collected manually via online questionnaires distributed across social media and professional networks [3]. |
| **Impacto de IA na produtividade?** | Not mentioned — the paper does not evaluate AI tools or AI-driven productivity [3, 5]. |

---

## Resultados Principais

- **Recognition Disparity**: 68% of respondents feel their contributions are less recognized compared to male colleagues [23], with 38.5% explicitly reporting gender bias in evaluations [24, 31].
- **Workplace Microaggressions**: 74% experience frequent interruptions during meetings and code reviews [23]; 41.2% were interrupted or dismissed during technical discussions [26].
- **Exclusion & Task Allocation**: 32.9% were excluded from major technical decisions [26]; 29.4% were assigned less challenging or lower-visibility tasks [26]; 52.9% are frequently assigned to documentation or mentorship [24].
- **Evaluation Criteria vs. Tasks Performed Mismatch**: Companies measure productivity using LOC / Commit Frequency (58.8%), Sprint Velocity (47.1%), and Peer Feedback (35.3%) [9]. However, female developers frequently perform Mentorship / Onboarding (52.9%) and Documentation / Process Improvement (48.2%) [9].
- **Double Workload**: 82% affirm domestic responsibilities affect professional productivity [23]; 54.1% state that household duties limit availability for extra professional development activities [28, 29].
- **Physiological Factors**: 42.3% reported that hormonal variations (e.g., menstrual cycle, migraines) affect focus and productivity [28, 29].
- **Metrics Inadequacy Perception**: 64.7% of participants feel current workplace productivity metrics do not accurately reflect their contributions [24, 30].
- **Underrepresentation in Leadership**: Only 12% of female respondents held leadership positions [32].

---

## Desafios do Uso das Metricas

- **Distorted View of Developer Performance**: Traditional metrics measure output volume rather than efficiency, solution maintainability, or problem complexity [7, 33].
- **Invisibility of Qualitative Contributions**: Critical activities such as mentorship, onboarding, documentation, code review, and emotional support remain invisible in quantitative evaluations [10, 17, 27].
- **Reinforcement of Structural Inequalities**: Female engineers assigned to low-visibility or "supportive" non-promotable tasks face lower performance evaluations and slower career growth [24, 25, 27].
- **Neglect of Work-Life Context and Biological Factors**: Standard metrics treat developer output as linear and ignore external domestic workloads and physiological variations [18, 25, 28].
- **Unconscious Bias in Evaluation**: Achievements of female developers are often credited to collective team effort while male achievements are individualised [22, 25].

---

## Avaliacao de Qualidade Metodologica

| Criterio | Pontuacao (0-2) |
|----------|----------------|
| Objetivo claramente definido | 2 [4, 8] |
| Metodologia adequada ao objetivo | 2 [3-5] |
| Amostra/contexto descrito adequadamente | 2 [3, 31, 32] |
| Ameacas a validade discutidas | 1 [2, 32] |
| Resultados com evidencia suficiente | 2 [9, 23, 24] |
| Contribuicao clara para pratica ou teoria | 2 [14, 16, 34] |
| **TOTAL** | **11/12** [2] |

---

## Limitacoes

- **Sample Size and Non-Probabilistic Sampling**: Based on a non-probabilistic sample of 85 survey respondents across Brazil [2, 3].
- **Underrepresentation of Senior Professionals and Leaders**: High concentration of younger/junior professionals (59.7% aged 20–29; 42.4% junior <3 years) and only 12% in leadership positions, limiting insights into long-term career barriers [2, 32].
- **Self-Reported Data**: Dependence on subjective self-reported survey responses regarding performance, workplace bias, and productivity [2].
- **Geographic Context**: Focused exclusively on female software engineers in Brazil, requiring caution when generalizing findings to other regions [2, 8].

---

## Contribuicao Principal

The main contribution of this paper is providing empirical evidence from 85 female software engineers in Brazil demonstrating that traditional, output-focused software productivity metrics (such as LOC, commit frequency, and sprint velocity) systematically undervalue women's contributions by neglecting qualitative and collaborative responsibilities like mentorship, documentation, and coordination [1, 4, 9, 24]. Furthermore, the study identifies two under-researched factors influencing developer productivity—domestic double workload and physiological hormonal variations—and proposes six practical guidelines to help organizations construct more holistic and inclusive evaluation frameworks [14, 28, 29].

---

*Extraido via NotebookLM em October 2026 para MLR: Software Developer Metrics in Practice*
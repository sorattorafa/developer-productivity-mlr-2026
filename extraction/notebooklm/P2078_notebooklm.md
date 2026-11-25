# P2078 — Are We Measuring the Wrong Things? How Software Project Leaders View Gen-AI-Assisted Developer Productivity

**Decisao: INCLUIDO | Qualidade: 5/5**

---

## Dados Bibliograficos

| Campo | Valor |
|-------|-------|
| **ID** | P2078 [1] |
| **Autores** | Ana Carolina Chagas, Rayfran Rocha Lima, Ana Carolina Oran [1] |
| **Ano** | 2026 [2] |
| **Venue** | Simpósio Brasileiro de Engenharia de Software (SBES 2026) [2] |
| **DOI** | Not specified in paper [1, 3] |
| **Tipo** | Conference paper [2] |
| **Metodo** | Survey (Quantitative statistical analysis and Qualitative thematic analysis) [1, 4, 5] |
| **Amostra** | 20 valid survey responses from software development project leaders (from 22 collected; 1 pilot and 1 corrupted excluded) [6] |
| **Contexto** | Industry and Public Institutions in Brazil (Large enterprises 35%, Medium-sized companies 30%, Startups 20%, Public institutions 15%) [7, 8] |
| **Modo de trabalho** | Hybrid (45%), Fully Remote (40%), Fully On-site (15%) [7] |
| **Metodologia** | Not specified (covers multiple domains: product-related 45%, software development 40%, quality engineering 15%, software architecture 15%, DevOps/SRE/infrastructure 15%, machine learning 10%, governance/PMO 10%, information security 5%) [9, 10] |

---

## Objetivo

This study investigates how software project leaders perceive and evaluate developer productivity in software engineering contexts where Generative Artificial Intelligence (Gen-AI) tools are integrated into everyday development workflows [1, 11]. It seeks to examine how Gen-AI adoption reshapes traditional, artifact-centered productivity notions (such as code volume and delivery speed) toward an interpretation-oriented perspective centered on validation effort, technical judgment, problem understanding, and critical assessment of generated outputs [1, 12-14].

---

## Questoes de Pesquisa

- **RQ1**: How is the adoption of Gen-AI tools modifying the notion of productivity according to software project leaders' perceptions? [4, 11]

---

## Metricas e Instrumentos de Avaliacao

| Metrica | Categoria | Nivel | Como Coletada | Validada |
|---------|-----------|-------|---------------|----------|
| Technical Quality / Qualidade Técnica | Quality | Individual / Team | Managerial assessment / Code reviews [13, 15] | Partial [15] |
| Client-perceived Quality / Qualidade Percebida pelo Cliente | Quality | Team / Organization | Client feedback / Surveys [15] | Partial [15] |
| Delivery Speed / Velocidade de Entrega | Delivery | Individual / Team | Sprint tracking / Issue boards (e.g., Jira) [15, 16] | Yes [15] |
| Quantity of Delivered Tasks / Quantidade de Tarefas Entregues | Activity | Individual / Team | Task management systems [15] | Yes [15] |
| Collaborative Behavior / Comportamento Colaborativo | Collaboration | Individual / Team | Peer evaluation / Managerial observation [13, 15] | Partial [15] |
| Lines of Code (LOC) | Activity | Individual | Repository mining / Automated scripts [1, 16] | Yes (Traditional, but criticized) [1, 12, 16] |
| Commits | Activity | Individual | Version control system (Git) logs [1, 16] | Yes (Traditional, but criticized) [1, 12, 16] |
| Pull Requests | Delivery / Activity | Individual / Team | Repository management platforms [16, 17] | Yes (Traditional, but criticized) [16, 17] |
| Code Quality | Quality | Individual / Team | Code inspection / Static analysis tools [18] | Partial [18] |
| Test Quality | Quality | Individual / Team | Automated test coverage / Peer reviews [18] | Partial [18] |
| Documentation Quality & Volume | Quality / Activity | Individual / Team | Documentation reviews / Audits [18] | Partial [18] |
| Need for Rework | Delivery / Quality | Individual / Team | Bug tracking / Defect density analysis [17, 18] | Partial [18] |
| Delivery Consistency | Delivery | Team / Organization | Project tracking metrics [18] | Partial [18] |
| Code Reuse | Quality / Activity | Team / Organization | Static analysis / Component tracking [18] | Partial [18] |

---

## Frameworks e Metricas

### Frameworks Referenciados
- **SPACE Framework**: **REFERENCED** (Cited via Forsgren et al. [11] in Section 2.2 as a foundational human-centered model combining quantitative and qualitative dimensions of developer productivity) [13, 19].
- **DORA / GQM / HEART / OKR**: Not mentioned in the text.

### Frameworks Propostos
- The paper does not propose a formal, named quantitative framework (e.g., DORA or SPACE). Instead, it introduces a **conceptual reinterpretation framework of productivity** in Gen-AI-assisted software engineering [1, 14]. This conceptual framework posits that productivity in AI-augmented workflows shifts from direct artifact production (lines of code, commits) toward **human mediation activities**: prompt refinement, technical validation effort, solution interpretation, and critical judgment of generated outputs [1, 14, 20, 21].

---

## Fatores que Influenciam Produtividade

### Fatores Positivos
| Fator | Categoria |
|-------|-----------|
| Faster information retrieval and reduced project research time | Technical / Process [22] |
| Selective knowledge acquisition and targeted learning via prompt filtering | Human / Technical [22] |
| Increased delivery speed and improved delivery consistency | Process / Organizational [18] |
| Higher autonomy in problem solving | Human [23, 24] |
| Increased confidence in deliverables and work organization | Human / Process [23] |
| Enhanced clarity of technical reasoning | Human / Technical [23] |
| Boosted developer motivation and proactivity | Human [23] |
| Improved documentation volume and documentation quality | Technical / Process [18] |
| Enhanced collaboration centered on evaluating and debating AI solutions | Organizational / Process [25, 26] |

### Fatores Negativos
| Fator | Categoria |
|-------|-----------|
| Increased validation effort and continuous verification overhead | Process / Technical [17, 18, 20] |
| "Ctrl+C / Ctrl+V" code submission anti-pattern with missing self-review and developer testing | Human / Process [17] |
| Cognitive dependency on Gen-AI tools leading to reduced deep engagement with technical problems | Human [27] |
| AI tool hallucinations, inaccurate outputs, and incomplete contextual understanding | Technical [20, 28] |
| Uneven productivity impact and pipeline blockages caused by inexperienced junior/trainee developers | Organizational / Human [29] |
| Greater variability or potential decline in focus, technical learning depth, and emotional stability | Human [23, 27] |

---

## Papel da IA e Automacao

| Campo | Valor |
|-------|-------|
| Usa IA/ML? | **Yes** — Investigates the use of Generative AI tools (code generation, debugging, documentation support, requirements analysis, test creation) across development workflows [1, 30]. |
| Automacao de coleta? | **No** — Data collection was conducted manually via an online Google Forms questionnaire distributed to software project leaders [6, 31]. |
| Impacto de IA na produtividade? | **Positive operational acceleration**, but shifts human effort toward validation, interpretation, technical judgment, and critical oversight rather than raw artifact volume [1, 15, 21, 32, 33]. |

---

## Resultados Principais

- **Overall Productivity Perception**: All project leaders reported positive or neutral impacts on productivity post-adoption; **0%** reported a productivity decrease [32].
- **Influence on Deliveries**: **61.9%** of participants reported a "high" influence of Gen-AI on team deliveries, **14.3%** reported "very high", **4.8%** reported "low", and **0%** "very low" [34].
- **Most Adopted Evaluation Metrics**:
  - Technical Quality: **95.2%** [15]
  - Client-perceived Quality: **76.2%** [15]
  - Delivery Speed: **71.4%** [15]
  - Quantity of Delivered Tasks: **66.7%** [15]
  - Collaborative Behavior: **66.7%** [15]
- **Perceived Impact on Evaluation Metrics**: **52.4%** reported that Gen-AI impacted evaluation metrics "positively" and **14.3%** "very positively" [15].
- **Demographics & Sample Breakdown**:
  - Sample of **20 valid survey responses** in Brazil (out of 22 collected; 1 pilot and 1 corrupted response excluded) [6, 8].
  - Leadership roles: Project Leaders (**40%**), Technical Leaders (**25%**), QA Leaders (**10%**), Technical Coordinators (**10%**), Project Managers (**10%**), Engineering Managers (**5%**) [9].
  - Professional experience: >15 years (**50%**), 2–5 years (**30%**), <2 years (**10%**), 6–10 years (**5%**), 11–15 years (**5%**) [10].
  - Organization sizes: Large enterprises (**35%**), Medium-sized companies (**30%**), Startups (**20%**), Public institutions (**15%**) [7].
  - Work arrangements: Hybrid (**45%**), Fully Remote (**40%**), Fully On-site (**15%**) [7].
- **Shift in Developer Attributes**: Traditional skills (technical knowledge, domain knowledge) remain critical, while **autonomy, critical thinking, and problem-solving** showed the highest increase in importance post-adoption [24].
- **Redistribution of Developer Effort**: Gen-AI speeds up initial solution drafting, but redistributes developer effort toward prompt engineering, output verification, bug fixing, and context adaptation [17, 18, 20, 35].

---

## Desafios do Uso das Metricas

- **Obsolescence of Artifact-Based Metrics**: Conventional metrics like lines of code, commits, and pull requests fail to capture actual developer effort or understanding in Gen-AI workflows [1, 12, 16].
- **"Ctrl+C / Ctrl+V" Anti-pattern**: Developers copying AI outputs directly without self-testing or code optimization, increasing pull request rework and pipeline blockages [17, 29].
- **Over-reliance and Shallow Learning**: Less experienced developers relying blindly on Gen-AI, leading to superficial technical understanding and reduced critical thinking [27, 29].
- **Fairness in Performance Evaluation**: Difficulty in isolating genuine human technical contribution and merit from AI-assisted code generation during individual evaluations [1, 29, 36].
- **Inflation of Managerial Expectations**: Leaders becoming accustomed to higher output speed, creating pressure on developers while increasing the burden of validation rigor [17, 29].

---

## Avaliacao de Qualidade Metodologica

| Criterio | Pontuacao (0-2) |
|----------|----------------|
| Objetivo claramente definido | 2 [1, 11, 37] |
| Metodologia adequada ao objetivo | 2 [4, 5, 20] |
| Amostra/contexto descrito adequadamente | 2 [6, 7, 9, 10] |
| Ameacas a validade discutidas | 2 [8, 38-40] |
| Resultados com evidencia suficiente | 2 [5, 15, 18, 22, 32] |
| Contribuicao clara para pratica ou teoria | 2 [1, 14, 41] |
| **TOTAL** | **12/12** |

---

## Limitacoes

- **Sample Size and Scope**: Exploratory sample of 20 project leaders in Brazil, limiting broad statistical generalizability across global regions [6, 8].
- **Self-Reported Perceptions**: Data relies on self-reported survey responses rather than direct observational or repository performance telemetry [39].
- **Retrospective Bias**: Retrospective evaluation rather than a longitudinal study measuring team performance before and after Gen-AI adoption over time [39].
- **Selection / Volunteer Bias**: Recruitment via LinkedIn and direct contacts may overrepresent leaders with stronger interest or favorable views toward Gen-AI [6, 8].
- **Qualitative Interpretative Risk**: Thematic coding across open-ended questions carries potential researcher interpretation bias (mitigated by a second researcher review) [5, 40].

---

## Contribuicao Principal

The principal contribution of this study is providing exploratory empirical evidence on how software project leaders reinterpret developer productivity in Gen-AI-assisted software engineering environments [1, 11, 14]. It shifts the productivity assessment discourse from traditional output-centric signals (such as code volume, commits, and delivery speed) toward a managerial perspective centered on human mediation—demonstrating that developer contribution in AI-augmented workflows is increasingly defined by validation effort, technical judgment, critical assessment of AI outputs, and problem framing ability [1, 14, 20, 21, 42].

---

*Extraido via NotebookLM em October 2026 para MLR: Software Developer Metrics in Practice*
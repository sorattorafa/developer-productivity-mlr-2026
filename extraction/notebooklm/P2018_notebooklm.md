# P2018 — Examining Productivity in Educational Environments: Perspectives of Professors and Students on a Capstone Project

**Decisao: INCLUIDO | Qualidade: 5/5**

---

## Dados Bibliograficos

| Campo | Valor |
|-------|-------|
| **ID** | P2018 [1] |
| **Autores** | Vinicius F. Gonçalves, João Pedro T. E. Santo, Guilherme F. Silva, Caio F. A. Tome, Jucele F. A. Vasconcellos, Patrícia G. F. Matsubara [1, 2] |
| **Ano** | 2026 [1] |
| **Venue** | IEEE/ACM 48th International Conference on Software Engineering (ICSE-SEET ’26) [1] |
| **DOI** | 10.1145/3786580.3786993 [1] |
| **Tipo** | Conference paper [1] |
| **Metodo** | Descriptive case study (semi-structured interviews, questionnaires, thematic analysis) [3-8] |
| **Amostra** | 6 supervising professors (P1–P6) and 32 undergraduate students (S1–S32; 6 in round 1, 26 in round 2) [6, 9, 10] |
| **Contexto** | Academic (The Center for Applied Software Engineering — SEN, capstone project program with real external clients at UFMS, Brazil) [2-5, 11, 12] |
| **Modo de trabalho** | On-site (in-person physical attendance tracked in labs/classrooms) [13-15] |
| **Metodologia** | Agile / Scrum (sprints, dailies, sprint reviews, user stories, story points, GitHub, Jira, Discord) [16-19] |

---

## Objetivo

This study investigates how productivity is perceived and evaluated by professors (supervisors) and final-year undergraduate students within a software engineering capstone program (SEN) working on real-client software projects [3-5]. The paper contrasts these educational perspectives with established software industry productivity frameworks, specifically the SPACE framework, to understand shared dimensions and identify aspects unique to educational environments [3, 8, 20-22].

---

## Questoes de Pesquisa

- **RQ1**: What aspects of productivity do professors perceive in software development capstone projects in SEN? [5]
- **RQ2**: What aspects of productivity do students perceive in software development capstone projects in SEN? [5]

---

## Metricas e Instrumentos de Avaliacao

| Metrica | Categoria | Nivel | Como Coletada | Validada |
|---------|-----------|-------|---------------|----------|
| **Volume and Distribution of Commits** | Activity | Individual / Team | Git / GitHub repository tracking (checking commit counts and work distribution across weekdays) [13, 19] | Partial [13, 23] |
| **Artifact / Task Deliveries** | Activity | Individual / Team | Task board inspection (completed cards, resolved bugs, story points delivered on Jira/GitHub/Drive) [18, 19] | Partial [18] |
| **Work Hours & Time Spent** | Activity | Individual | Self-reported time logging / proposed time bank cross-referenced with tasks [13, 24, 25] | No [24] |
| **Physical Absences / Room Attendance** | Activity | Individual | In-person attendance tracking during scheduled project lab days [13-15] | No [13] |
| **Engagement with Client** | Activity / Collaboration | Team | Frequency and quality of client meetings, requirements discovery, and technical discussions [15, 24, 26] | Partial [15, 27] |
| **Estimation Adherence & Delays** | Activity / Efficiency | Individual / Team | Comparing task start/end times against sprint estimates during daily meetings and reviews [19, 25, 28, 29] | No [28] |
| **Deliverable Quality & Defect Rate** | Performance | Individual / Team | Supervisor evaluation, code review, testing, and tracking required bug fixes after delivery [30-33] | Partial [31, 33] |
| **Application of Previous Knowledge** | Learning | Individual | Qualitative supervisor observation of proper architectural and software engineering concept implementation [34, 35] | No [34] |
| **Role-Based Deliveries** | Learning | Individual | Evaluation of role-specific contributions (e.g., UX prototypes, UX writing, architectural documentation) [36, 37] | No [37] |
| **Work Attitude & Problem-Solving Engagement** | Behavioral / Attitude | Individual | Supervisor observation during Agile ceremonies, proactivity in unblocking tasks, and exploring alternative solutions [38, 39] | No [39] |
| **Team Dynamics & Peer Feedback** | Collaboration / Satisfaction | Team / Individual | Peer feedback, monitoring team self-organization, and observing quietness or disengagement during reports [40-43] | Partial [43] |

---

## Frameworks e Metricas

### Frameworks Referenciados
- **SPACE Framework** (Forsgren et al., 2021): **APPLIED** — Used as the primary theoretical baseline to analyze, compare, and categorize professor and student productivity perceptions across Satisfaction, Performance, Activity, Communication/Collaboration, and Efficiency/Flow [2, 9, 24, 66–72].
- **Human-Centered Developer Productivity / DevEx** (Jaspan & Green, 2023; D'Angelo et al., 2024): **REFERENCED** — Discussed as industry precedents combining subjective surveys with log-based metrics [27, 44].
- **Scrum / Agile**: **APPLIED** — Adopted by capstone teams as the operational framework for sprint planning, daily meetings, and reviews [16, 17, 19].
- **Reflexive Weekly Monitoring Method**: **REFERENCED** — Cited from literature (Marques et al., 2018) regarding weekly monitor-guided reflection sessions [45, 46].
*(Note: Frameworks such as DORA, GQM, HEART, or OKR are not mentioned in this paper.)*

### Frameworks Propostos
- The paper does not formalize a fully automated framework tool, but **proposes an extended multidimensional productivity construct for capstone education** [47-49]. This construct enriches the industry SPACE model by adding two major dimensions:
  1. **Learning Signs**: Encompassing role-based learning, application of prior knowledge, needs-driven learning, knowledge sharing, reflective learning, and student ramp-up [42–46, 70].
  2. **Behavioral Cues and Work Attitudes**: Capturing commitment to task completion, problem-solving drive, vigor, dedication, and active project involvement [38, 39, 50].

---

## Fatores que Influenciam Produtividade

### Fatores Positivos
| Fator | Categoria |
|-------|-----------|
| Proper application of previous coursework knowledge and role-based specialization [34, 37] | Process / Human |
| Active engagement with real clients and technical IT team discussions [15, 26] | Process / Organizational |
| Peer collaboration, proactivity in helping teammates, and strong team self-organization [41, 51] | Human / Process |
| High commitment to task completion and exploratory problem-solving drive [38, 39] | Human |
| Clear communication and active participation during daily meetings and ceremonies [17, 52] | Process / Human |
| Adapting provided software artifact templates to project needs [35] | Process |

### Fatores Negativos
| Fator | Categoria |
|-------|-----------|
| High project technical complexity and difficult external client / IT team requirements [26, 53] | Technical / Organizational |
| Imbalance in prior team experience levels causing frustration or intimidation [54] | Human / Organizational |
| Mismatch between student career goals/purpose and assigned project or role [55, 56] | Human / Organizational |
| Heavy external workload (demanding coursework, electives, outside jobs, internships, family issues) [56-58] | Human / Organizational |
| Frequent physical/functional absences, disengagement, and lack of project decision awareness [14, 59] | Human |
| Inaccurate task estimation leading to sprint delays and under-delivery [28, 29] | Process |
| Gaming metrics or inflating code delivery when metrics are tied directly to grading [23, 60] | Process / Organizational |

---

## Papel da IA e Automacao

| Campo | Valor |
|-------|-------|
| **Usa IA/ML?** | **Yes** — The authors used AI-powered audio tools (Riverside and TurboScribe) to transcribe semi-structured professor interviews [61, 62]. In addition, generative AI tools (e.g., GitHub Copilot) are cited in the literature review regarding productivity studies [27]. |
| **Automacao de coleta?** | **No** — SEN currently lacks an automated productivity measurement system; primary research data were collected manually via semi-structured interviews and online questionnaires [6, 7, 63]. |
| **Impacto de IA na produtividade?** | The study references literature (Ziegler et al., 2024 [51]) examining AI assistants within SPACE [27], but does not empirically measure AI tool usage among its own capstone sample. |

---

## Resultados Principais

- **Professors' Holistic Perspective**: Professors evaluate productivity using a broad set of **Signs and Cues** covering SPACE dimensions (Performance, Activity, Communication & Collaboration, Satisfaction) as well as academic-specific dimensions [3, 22, 62].
- **Identification of Learning as a Productivity Dimension**: Professors explicitly view **Learning Signs** (role-based immersion, knowledge application, knowledge sharing, ramp-up) as an essential facet of productivity in capstone settings, accepting that learning gains may temporarily reduce output velocity [42–46, 70].
- **Emphasis on Work Attitude**: Supervisors rely heavily on **Behavioral Cues and Work Attitudes** (proactivity, dedication, vigor, commitment to unblocking tasks) as vital signals of student engagement [38, 39, 50].
- **Students' Activity-Centric Mental Model**: Students hold a narrower mental model predominantly focused on **Activity signs**—evaluating productivity primarily through "how much gets done" (completed tasks, resolved bugs, story points, cards, time/effort spent) [54–56].
- **Detection of Deliberate Low Productivity**: Students spot potential underperformance through missing commitments, disengagement in project decisions, frequent room absences, and downstream workload shifting onto teammates [14, 64-66].
- **Absence of Efficiency & Flow**: Neither professors nor students spontaneously raised the SPACE dimension of **Efficiency and Flow** (uninterrupted focus), likely because social, behavioral, and output signals are more readily observable in collaborative academic environments [67].
- **Impact of Contextual Factors**: 100% of interviewed professors emphasize that contextual factors—both internal (project complexity, experience imbalance) and external (demanding courses, internships, career goals, family issues)—must be considered when judging productivity [49–54, 73].
- **Sample Metrics**: The study interviewed 6 professors supervising up to 12 teams each (P1=8, P2=8, P3=8, P4=12, P5=2, P6=2 teams supervised) [6, 9] and surveyed 32 students across two semesters (78.1% of students agreed they were highly productive, n=25/32; median external SE experience: 1 year; 29/32 male) [10].

---

## Desafios do Uso das Metricas

- **Metric Gaming and System Distortion**: Directly linking quantitative productivity metrics to individual student grades risks encouraging students to "game the system" (e.g., inflating metric counts or line counts), undermining the educational goal of reflective discussion [23, 60].
- **The "No Silver Bullet" Pitfall**: Relying on single metrics (such as LOC or commit counts) fails to reflect quality, learning, or collaboration, often misrepresenting project health [12, 68, 69].
- **Difficulty of Quantifying Quality**: Code and deliverable quality is recognized as vital to true performance but remains subjective and technically difficult to measure [30, 31, 33].
- **Tension Between Learning and Delivery Velocity**: Pushing for maximum output velocity can discourage students from exploring unfamiliar tools or proper design, whereas prioritizing learning can temporarily lower short-term delivery [35, 36, 70].
- **Free-Riding and Score Inflation**: Peer evaluations suffer from tendencies where students penalize obvious free-riders but inflate scores for minimally acceptable peers [43].
- **Invisibility of Flow and Friction**: Individual focus states and flow interruptions are difficult for supervisors to detect without specialized, non-intrusive logging tools [67].

---

## Avaliacao de Qualidade Metodologica

| Criterio | Pontuacao (0-2) |
|----------|----------------|
| **Objetivo claramente definido** | 2 — Research objectives and explicit research questions (RQ1 and RQ2) are clearly articulated [5]. |
| **Metodologia adequada ao objetivo** | 2 — Descriptive case study design using semi-structured interviews, questionnaires, and thematic analysis is well suited for investigating perceptions [5, 8]. |
| **Amostra/contexto descrito adequadamente** | 2 — Extensive detail provided regarding SEN, comparison with global SLR benchmarks, professor demographics, and student cohort numbers [17–23]. |
| **Ameacas a validade discutidas** | 2 — Dedicated limitations section thoroughly discusses construct validity, researcher reflexivity, and transferability [48, 63]. |
| **Resultados com evidencia suficiente** | 2 — Rich qualitative evidence, thematic structures, and direct quotes from P1–P6 and S1–S32 support all findings [26–66]. |
| **Contribuicao clara para pratica ou teoria** | 2 — Provides actionable insights for capstone project management and extends the industry SPACE model to educational settings [22, 48, 49]. |
| **TOTAL** | **12/12** |

---

## Limitacoes

- **Absence of Automated Measurement System**: SEN lacks an automated metric tracking platform, preventing the triangulation of subjective participant reports with objective tool-log data [63].
- **Researcher Reflexivity / Potential Bias**: Two co-authors had past affiliation with SEN (one as supervisor, one as student), presenting potential bias (mitigated by assigning non-SEN authors to analysis and keeping student surveys anonymous) [63].
- **Single-Institution Setting**: Data were collected exclusively within capstone projects at one Brazilian university (UFMS), which may constrain direct statistical generalizability (though SEN alignment with global SLR benchmarks supports typicality) [12, 48].
- **Round 1 Survey Response Rate**: The initial survey round yielded 6 out of 46 responses due to graduating student departure, though the second round achieved 26/46 for a combined total of 32 respondents [10].

---

## Contribuicao Principal

The principal contribution of this paper is demonstrating that industry developer productivity frameworks (such as SPACE) can be meaningfully adapted and expanded for educational capstone environments [3, 21, 22]. By contrasting supervisor and student perspectives, the study reveals that educational productivity extends beyond code delivery and collaboration to incorporate **Learning Signs** (role immersion, knowledge application) and **Behavioral Cues/Work Attitudes** (engagement, problem-solving vigor) [42–48, 70, 71]. These findings provide a theoretical and empirical foundation for designing formative, multidimensional productivity measurement systems that prepare software engineering students for industry realities without incentivizing metric gaming [22, 47, 49, 60].

---

*Extraido via NotebookLM em October 2026 para MLR: Software Developer Metrics in Practice*
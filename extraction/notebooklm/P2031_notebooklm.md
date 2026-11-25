# P2031 — Understanding Task Enjoyment in Software Development: A Mixed-Methods Study on Practitioners From Poland and Brazil

**Decisao: INCLUIDO | Qualidade: 5/5**

---

## Dados Bibliograficos

| Campo | Valor |
|-------|-------|
| **ID** | P2031 [1] |
| **Autores** | Klara Borowa, Bartłomiej Rasztabiga, Hubert Soroka, Maciej Tymoftyjewicz, Rodrigo Rebouças de Almeida [1, 2] |
| **Ano** | 2026 [3, 4] |
| **Venue** | IEEE/ACM 48th International Conference on Software Engineering (ICSE-SEIP '26) [3, 4] |
| **DOI** | 10.1145/3786583.3786884 [3, 4] |
| **Tipo** | Conference paper (ICSE-SEIP '26) [3, 4] |
| **Metodo** | Mixed methods (4-phase study: 2 questionnaires, semi-structured interviews, focus groups) [2, 5, 6] |
| **Amostra** | 173 practitioners total (158 questionnaire respondents [82 in Phase 1, 75 in Phase 3], 11 interviewees in Phase 2, 15 focus group participants across 2 groups in Phase 4) [2, 5, 7-13] |
| **Contexto** | Industry (Software practitioners primarily based in Poland and Brazil across small to large enterprise companies, including a Brazilian finance company for focus groups) [2, 5, 9, 10, 13, 14] |
| **Modo de trabalho** | Not specified (Data was collected online via surveys, interviews, and focus groups, but work arrangements like remote, hybrid, or on-site were not explicitly reported) [8, 14-16] |
| **Metodologia** | Not specified (Agile/Scrum practices like sprint planning and daily meetings are referenced, but specific methodology across all participants is not specified) [17-20] |

---

## Objetivo

The main objective of this study is to investigate software development task preferences among practitioners across diverse roles in Poland and Brazil [2, 5, 21]. Specifically, the paper aims to identify which software development activities are most enjoyed or disliked, uncover the underlying factors influencing these attitudes, evaluate how task enjoyment correlates with time spent on tasks (and potential task avoidance), and propose practical improvements to optimize developer experience and team workflows [2, 5, 21, 22].

---

## Questoes de Pesquisa

- **RQ1**: Which activities related to software development are liked and disliked by practitioners? [5]
- **RQ2**: What are the factors that influence the positive or negative attitude towards these activities? [5]
- **RQ3**: How does personal dislike/enjoyment of certain activities correlate with time spent on them? [5]

---

## Metricas e Instrumentos de Avaliacao

| Metrica | Categoria | Nivel | Como Coletada | Validada |
|---------|-----------|-------|---------------|----------|
| **Task Enjoyment Rating** | Satisfaction / DevEx | Individual | 5-point ordinal scale questionnaire (1 = "Strongly dislike" to 5 = "Strongly enjoy") [23-25] | Yes [23, 24] |
| **Time Spent on Task** | Activity | Individual | 6-point ordinal scale questionnaire (1 = "under 1h" to 6 = "Over 20 hours") [26-28] | Partial [16] |
| **Finding Agreement Rating** | Satisfaction / DevEx | Individual | 5-point Likert scale questionnaire (1 = "Strongly disagree" to 5 = "Strongly agree") [9, 29] | Yes [29, 30] |
| **Task Enjoyment vs. Time Spent Correlation** | Activity / DevEx | Individual / Aggregate | Spearman correlation (\\(r_s\\)) with permutation testing between enjoyment and time spent [27, 28, 31] | Yes [27, 31] |
| **Developer Productivity** | Productivity | Individual / Team | Cited from literature (Murphy-Hill et al., SPACE framework, Nichols) based on job enthusiasm and task output [18, 32-35] | Yes [32, 35] |
| **Developer Happiness / Morale** | Satisfaction / DevEx | Individual | Cited from literature (Graziotin et al., Besker et al.) evaluating consequences of unhappy developers [4, 32, 36-38] | Yes [36, 37] |

---

## Frameworks e Metricas

### Frameworks Referenciados
- **DevEx (Developer Experience)**: REFERENCED — Cited (Fagerholm & Munch, Razzaq et al.) as a overarching domain encompassing factors affecting how developers feel and think about work [20, 36, 39].
- **SPACE Framework**: REFERENCED — Cited (Forsgren et al.) in discussion regarding dimensions of software developer productivity [32, 38].
- **SWEBOK (v4.0)**: APPLIED — SWEBOK engineering knowledge areas were used to extract non-coding tasks (e.g., architecture design, software design, planning, infrastructure) to build the study's task taxonomy [17, 40].
- **Task Taxonomy (Meyer et al.)**: APPLIED — Pre-existing developer task taxonomy by Meyer et al. was extended and applied as the measurement instrument across all 4 study phases [17, 41, 42].

### Frameworks Propostos
- **Expanded Software Development Task Taxonomy**: A 18-activity taxonomy designed to cover all software practitioner roles, non-coding engineering tasks, version control, and waiting time ("Idling") [17, 18, 26, 35, 43].
- **Task Enjoyment & Dislike Factors Taxonomy**: A qualitative framework categorizing 21 positive factors (e.g., Quality/Value impact, Challenge, Growth) and 17 negative factors (e.g., Redundancy & time waste, Monotony, Technical debt) driving task attitudes and avoidance [44-46].

---

## Fatores que Influenciam Produtividade

### Fatores Positivos
| Fator | Categoria |
|-------|-----------|
| **Quality/Value Impact** (Improving software quality or adding system value) [44, 45] | Technical / Process |
| **Challenge & Problem Solving** (Engaging in technical puzzles with clear success criteria) [44, 45] | Technical / Human |
| **Personal Growth & Skill Learning** (Developing competencies and advancing career) [44, 45] | Human |
| **Social Aspects & Team Morale** (Positive team dynamics, unblocking peers, mentoring) [44, 45, 47] | Human / Organizational |
| **Job Enthusiasm & Personal Preference** (Alignment of tasks with intrinsic personal motivators) [34, 35, 44, 45] | Human |
| **Completion Satisfaction** (Sense of pleasure from completing a task) [44, 45] | Human |
| **Autonomy & Self-Organization** (Freedom to organize work) [44, 45] | Organizational / Human |
| **Variety in Work** (Blending routine work with novel tech or activities) [44, 45, 48] | Process / Human |

### Fatores Negativos
| Fator | Categoria |
|-------|-----------|
| **Redundancy & Time Wasting** (Tasks perceived as pointless or delaying core goals) [46, 49] | Process / Organizational |
| **Monotony & Tedium** (Boring, repetitive work like manual testing and documentation) [46, 49, 50] | Process / Human |
| **Unplanned Interruptions** (Disrupting focus and delaying current task execution) [46, 47, 49, 51] | Process / Organizational |
| **Technical Debt** (Poor code structure making maintenance difficult, slow, and frustrating) [32, 46, 52, 53] | Technical |
| **Overly Large Meetings / Too Many Participants** (Involving non-essential people, leading to off-topic talk) [19, 46, 54] | Organizational / Process |
| **Lack of Perceived Value** (Producing artifacts that sit unused or quickly become obsolete) [46, 55, 56] | Process / Technical |
| **High Cognitive Load / Task Difficulty** (Managing implicit knowledge, debugging hard issues without guidance) [33, 46, 49] | Technical / Human |

---

## Papel da IA e Automacao

| Campo | Valor |
|-------|-------|
| **Usa IA/ML?** | Yes — The paper discusses practitioners utilizing Large Language Models (LLMs/AI) to refactor, structure, and generate drafts for documentation (e.g., HotGPT experience cited), converting tedious documentation work into an engaging process [50, 57]. |
| **Automacao de coleta?** | No — Data was collected manually via online survey platforms, semi-structured online interview recordings/transcriptions, and online focus group discussions [7, 8, 14, 15, 23]. Automated telemetry is cited in related work (Obi et al.) but not used for primary data collection [39, 43, 58]. |
| **Impacto de IA na produtividade?** | Positive impact on developer experience and productivity by automating repetitive documentation and testing tasks [50, 57]. Practitioners reported high enthusiasm when using LLMs to structure documentation and handle automated queries [50, 57]. |

---

## Resultados Principais

- **Most Enjoyed Tasks**: **Coding** and **Learning** were universally the most enjoyed activities across all practitioner roles (median rating = **5.0** out of 5 ["Strongly enjoy"], IQR = **1.0**) [24, 25].
- **Most Disliked Task**: **Interruptions** was the most disliked activity overall (median rating = **2.0** ["Dislike"], IQR = **2.0**), with non-developers and managers disliking it more than QAs and Data Engineers [25, 59].
- **Divisive Tasks**: **Manual testing**, **Documentation**, and **Maintenance** had neutral median ratings (**3.0**) but high dispersion (IQR = **2.0**), aligning with role specialization (QAs enjoy manual testing, Architects enjoy documentation, Admins enjoy maintenance) [25, 59].
- **Primary Factors**: The top positive factor driving task enjoyment is **Quality/Value impact** (**68 mentions**), followed by **Challenge** (**51 mentions**) and **Growth** (**46 mentions**) [44, 45]. The top negative factors are **Redundancy & time waste** (**86 mentions**) and **Monotony** (**81 mentions**) [46, 49].
- **Correlation between Enjoyment and Time Spent**: Across all tasks combined, a statistically significant weak correlation exists between enjoyment and time spent (\\(r_s = 0.269\\), \\(p = 3.09 \times 10^{-44}\\)) [27, 28, 47].
- **Maintenance Avoidance**: **Maintenance** is the only task with a statistically significant moderate correlation between enjoyment and time spent (\\(r_s = 0.416\\), \\(p = 0.0002\\), IQR = **2.0**), demonstrating that practitioners who dislike maintenance tend to avoid performing it [28, 52, 53].
- **Tasks Unaffected by Enjoyment**: Time spent on **Bugfixing** (\\(r_s = 0.039\\), \\(p = 0.6369\\)), **Code review** (\\(r_s = 0.151\\), \\(p = 0.0714\\)), **Meetings** (\\(r_s = -0.040\\), \\(p = 0.6103\\)), **Interruptions** (\\(r_s = -0.040\\), \\(p = 0.6155\\)), and **Planning** (\\(r_s = 0.140\\), \\(p = 0.0874\\)) showed no significant correlation with enjoyment because practitioners cannot control the time spent on them [28, 52, 60].
- **Validated Dilemmas**:
  1. *Individual Work vs. Teamwork Dilemma*: Practitioners enjoy helping others (median = 4) but dislike being interrupted (median = 2) [47, 51].
  2. *Experience vs. Exploration Dilemma*: Practitioners prefer tasks they have already mastered but also strongly desire learning new skills [48, 61].

---

## Desafios do Uso das Metricas

- **Evaluating Productivity without Task Context**: Scoring developer productivity without considering specific task types creates inaccurate evaluations due to high task-level variance [18, 33].
- **Relying on Time Spent as a Productivity Metric**: Using time spent on tasks as a direct proxy for productivity or output is unreliable [27, 60].
- **Ignoring Non-Coding Activities**: Focusing metrics exclusively on coding output ignores essential non-coding tasks (documentation, requirements, maintenance) required for overall software quality [21, 62].
- **Unconscious Task Avoidance & Technical Debt Accumulation**: Output metrics fail to detect task avoidance driven by task dislike (e.g., avoiding maintenance due to high technical debt), causing hidden technical debt accumulation [52, 53, 63].
- **Misaligned Task Assignment**: Assigning tasks without considering personal motivators or role fit degrades morale and productivity [4, 34, 59].

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

- **Self-Reported Time Estimates**: Reliance on self-reported retrospective survey estimates regarding time spent on tasks, which are susceptible to memory recall bias and schedule variability [16].
- **Recall Bias**: Negative experiences tend to be recalled more vividly than positive ones during interviews and open-ended survey questions [16].
- **Sampling & Convenience Bias**: Impossibility of defining the exact global target population of software practitioners, leading to potential convenience sampling bias towards Polish and Brazilian participants [9, 13, 64].
- **Qualitative Coding Subjectivity**: Potential qualitative researcher bias during open and hypothesis coding, mitigated by dual-coder review and consensus discussions [64-66].
- **Potential Confirmation Bias**: Risk that participants in interviews and focus groups refrained from providing disconfirmatory feedback when presented with preliminary findings [67].

---

## Contribuicao Principal

The main contribution of this study is an empirical, multi-role investigation of task enjoyment in software development based on an expanded 18-activity taxonomy [2, 5, 17]. By conducting a 4-phase mixed-methods study with 173 practitioners across Poland and Brazil, the authors establish a prioritized ranking of task preferences, categorize key enjoyment and dislike factors, prove that task dislike correlates with task avoidance (most acutely in maintenance), and offer validated, practical recommendations (such as dedicated help timeslots, task blending, and AI-assisted documentation) to improve developer experience and prevent task neglect in industry practice [2, 5, 22, 47, 48, 50, 52, 68].

---

*Extraido via NotebookLM em October 2026 para MLR: Software Developer Metrics in Practice*
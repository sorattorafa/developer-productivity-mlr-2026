# P2038 — Understanding and Enhancing CS Students’ Interaction Experience with AI Coding Assistant Tools

**Decisao: INCLUIDO | Qualidade: 5/5**

---

## Dados Bibliograficos

| Campo | Valor |
|-------|-------|
| **ID** | P2038 [1] |
| **Autores** | Xiao Long, Xin Tan, Yinghao Zhu, Jing Jiang, Li Zhang [1, 2] |
| **Ano** | 2026 [1, 3] |
| **Venue** | ACM Transactions on Software Engineering and Methodology (TOSEM) [1, 3] |
| **DOI** | 10.1145/3785479 [1, 3] |
| **Tipo** | Journal article [1, 3] |
| **Metodo** | Controlled experiment / Mixed methods (quantitative interaction logs and survey, qualitative thematic coding) [4-6] |
| **Amostra** | 27 CS students (6 female, 21 male; 10 senior undergraduates, 17 graduate students) [4, 7, 8] |
| **Contexto** | Academic (Beihang University, Computer Science education) [2, 7-9] |
| **Modo de trabalho** | Remote (controlled online experimental platform) [10] |
| **Metodologia** | Not specified (individual Python programming tasks in algorithm design, CRUD systems, and data processing) [5, 11-14] |

---

## Objetivo

This research aims to investigate Computer Science students' interaction experience, behavioral patterns, decision-making determinants, and usability challenges when engaging with AI Coding Assistant Tools (ACATs) during programming tasks [7, 15]. Through a controlled study involving 27 CS students across three distinct Python programming task categories (Algorithms and Data Structures, Management System Development, and Research Tool Development) using three representative tools (GitHub Copilot, Tabnine, and CodeGeeX), the paper evaluates interaction frequency, code suggestion acceptance rates, self-perceived productivity operationalized via the SPACE framework, and student expectations to establish design implications for future AI tools and pedagogical interaction strategies [4, 5, 7, 16].

---

## Questoes de Pesquisa

- **RQ1**: What are the characteristics of student–ACAT interactions regarding usage frequency and acceptance rates across different scenarios? [15]
- **RQ2**: How does interacting with ACATs affect students’ self-perceived productivity? [17]
- **RQ3**: What are the interaction patterns of students when using ACATs? [18]
- **RQ4**: What factors influence students’ evaluations and decisions when interacting with ACATs? [18]
- **RQ5**: What are the challenges and expectations when students interact with ACATs? [4]

---

## Metricas e Instrumentos de Avaliacao

| Metrica | Categoria | Nivel | Como Coletada | Validada |
|---------|-----------|-------|---------------|----------|
| **Code Suggestion Acceptance Rate** | Productivity / Activity | Individual | Automated VSCode extension logs (`ccdc-plugin`) tracking accepted vs. total recommendations | Yes [4, 19-21] |
| **Interaction Frequency** | Activity | Individual | VSCode log timestamps counting total triggered recommendations | Yes [4, 19, 22] |
| **Perceived Task Difficulty** | Efficiency and flow | Individual | Post-task Likert-scale questionnaire comparing task with/without ACAT | Yes [16, 17, 23, 24] |
| **Frequency of Seeking External Help** | Efficiency and flow | Individual | Self-reported post-task questionnaire | Yes [16, 17, 23, 24] |
| **Self-Assessed Individual Performance** | Performance | Individual | Post-task Likert-scale self-rating | Yes [16, 17, 23, 24] |
| **Perceived Strenuousness of Coding Without ACAT** | Satisfaction and well-being | Individual | Post-task agreement scale measuring cognitive reliance | Yes [16, 23-25] |
| **State Transition Probabilities** | Activity / Behavior | Individual | Systematic open coding and screen recording annotation across interaction stages | Yes [26-30] |
| **Correct Syntax Importance** | Quality | Individual | Post-experiment survey Likert rating | Yes [31, 32] |
| **Similarity to Correct Code** | Quality | Individual | Post-experiment survey Likert rating | Yes [31, 32] |
| **Code Readability** | Quality | Individual | Post-experiment survey Likert rating | Yes [31, 32] |
| **Consistent Code Style** | Quality | Individual | Post-experiment survey Likert rating | Yes [31, 33] |
| **Inclusion of Code Comments** | Quality | Individual | Post-experiment survey Likert rating | Yes [31, 33] |

---

## Frameworks e Metricas

### Frameworks Referenciados
- **SPACE Framework**: **APPLIED** — Used to operationalize self-perceived productivity across three specific dimensions: *Efficiency and flow* (task difficulty, help-seeking frequency), *Performance* (self-assessed output quality), and *Satisfaction and well-being* (perceived strenuousness without ACAT) [16, 23, 24].
- **Comprehensive Understanding of Programmer Status Taxonomy (Mozannar et al.)**: **REFERENCED** — Discussed regarding developer time allocation, verification debt, and cognitive state modeling [34-36].
- **Acceleration and Exploration Modes (Barke et al.)**: **REFERENCED** — Discussed when contrasting professional developer exploration behavior (multi-candidate panel usage) with student behavior [35, 37, 38].

### Frameworks Propostos
- **Five-Layer Hierarchical Interaction Behavior Model**: A novel model structuring student–ACAT interactions into five sequential layers: **Prompt** (P1: comment, P2: code, P3: context, P4: tool prompts), **Understanding**, **Decision** (D1–D9: accept, reject, slow accept, compare recommendations), **Adaption** (A1–A4: modify previous code, modify recommendation, modify both, modify comment prompt), and **Backtrack** (B: delete accepted recommendation) [7, 26, 29, 35, 39-41]. The framework also identifies an independent **Verification** dimension categorized into white-box *verifying internal code logic* and black-box *verifying code output* [42-44].

---

## Fatores que Influenciam Produtividade

### Fatores Positivos
| Fator | Categoria |
|-------|-----------|
| Fulfilling functional requirements (correct logic, API completion, I/O formatting) | Technical [45, 46] |
| Reducing required keystrokes | Technical / Process [45, 46] |
| Providing a code framework, structural outline, or algorithmic idea | Technical / Process [45, 46] |
| Generating simple and repetitive code constructs efficiently | Process [46] |
| Aligning with intuitive student coding habits | Human [46] |
| Single-line code generation providing higher contextual accuracy and focus | Technical / Process [47] |
| "Slow accept" (selective manual typing) boosting confidence and epistemological trust | Human / Process [48-50] |

### Fatores Negativos
| Fator | Categoria |
|-------|-----------|
| Generating irrelevant code, logic flaws, or output format mismatches | Technical [46, 51] |
| Timing synchronization delays causing missed completions during rapid typing | Technical [51, 52] |
| Modifying previously written code to fit accepted suggestions (invariably causing backtracking) | Process / Technical [53-55] |
| Active natural language comment prompts generating unwanted comment chains instead of code | Technical / Process [56, 57] |
| Inconspicuous UI for displaying and cycling candidate recommendations | Technical / Process [58] |
| Contextual error propagation from pre-existing code flaws into AI recommendations | Technical [59] |

---

## Papel da IA e Automacao

| Campo | Valor |
|-------|-------|
| **Usa IA/ML?** | Yes — Evaluates three LLM-powered AI coding assistant tools (GitHub Copilot, Tabnine, CodeGeeX) providing inline ghost-text code completion and sidebar chat [4, 7, 60, 61] |
| **Automacao de coleta?** | Yes — Custom experimental platform with a published VSCode extension (`ccdc-plugin`) automatically logged interaction timestamps, accepted snippets, screen recordings, and dynamically synthesized personalized interview/survey questions [4, 7, 19, 62, 63] |
| **Impacto de IA na produtividade?** | Positive overall impact on self-perceived productivity: reduces perceived task difficulty, improves self-rated performance, decreases external help seeking, and reduces cognitive strain (>55% reported coding without ACAT was strenuous) [16, 17, 24, 25] |

---

## Resultados Principais

- **Acceptance Rates Across Tools**: CodeGeeX achieved the highest average acceptance rate (49%), followed by GitHub Copilot (39%) and Tabnine (24%) [21, 64]. CodeGeeX's higher rate was driven by its single-line prediction approach (53.53% acceptance), which broke complex blocks into sequential steps [47, 64].
- **Recommendation Methods & Content**: Editing line completion (W2) was the most frequently generated recommendation type but suffered low acceptance [65-67]. In terms of content, comments completion and string completion exhibited the lowest acceptance rates across all tools [67, 68].
- **Passive vs. Active Prompting**: Passive prompts (context prompt: 50.1%, code prompt: 48.2%) achieved higher acceptance rates than active natural language comment prompts (43.2%) [56, 69]. Comment prompts frequently failed due to model tendency to generate trailing comment strings rather than code (49.8% rejection rate) [56, 57].
- **The Rework and Backtrack Anti-Pattern**: When students modified their *previous code* to fit a newly accepted AI suggestion (A1 adaptation), it resulted in a **100% backtracking rate** (7 out of 7 observed cases ended in complete code deletion) [53, 55].
- **Efficacy of "Slow Accept"**: Students who manually typed out displayed AI suggestions ("slow accept") experienced zero backtracking, using the inline text to validate their own reasoning and build self-confidence [48-50, 69].
- **Verification Preferences**: Students strongly favored black-box output verification (145 instances, 87%) over white-box internal logic examination (21 instances, 13%) [43, 44].
- **Feature Discoverability**: Only 12 of 27 students utilized auxiliary features (9 NL2Code, 3 debugging, 1 API inquiry, 1 unit test generation); non-users cited lack of feature awareness (7 students) or perceived lack of utility (3 students) [70, 71].
- **Decision Factors & Expectations**: Taxonomy established 22 decision reasons, 11 interaction challenges (e.g., handling complex logic, poor candidate display), and 23 future expectations (e.g., adaptive style learning, direct framework generation) [7, 45, 72-75].

---

## Desafios do Uso das Metricas

- **Outcome Metric Flaws**: Relying solely on overall completion time or success rates hides fine-grained interaction friction and cognitive friction differences caused by varying student baseline skills [22, 76].
- **Acceptance Rate Distortion**: Raw code acceptance rate can be misleading; high acceptance in single-line tools (CodeGeeX) was partly an artifact of splitting multi-line functions into multiple consecutive accept triggers [47].
- **Verification Debt**: Students accepting AI code without prior understanding and relying almost exclusively on output test execution (87%) creates verification debt, risking unspotted logical bugs [36, 42-44].
- **Retrofitting Anti-Pattern**: Attempting to refactor existing code to fit AI suggestions represents an inefficient workflow loop that consistently leads to wasted effort and full deletion [53-55].
- **Candidate Switching Blindness**: Inconspicuous candidate suggestion UI leads 70% of non-candidate users to miss alternative suggestions completely, biasing evaluations toward top-ranked recommendations [33, 58].

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

- **Sample Size and Institution**: Controlled study examined 27 participants from a single university, which may restrict generalizability despite extensive qualitative video annotation (1,909 minutes) [9, 27, 77].
- **Tool Familiarity Discrepancy**: Two participants (Stu18 and Stu22) reported lower familiarity (<3) with their assigned tool, although transferrable Copilot experience and standardized training minimized operational impacts [78-80].
- **Interaction Paradigm Scope**: Findings specifically reflect inline completion and sidebar chat ACATs, and may not generalize to autonomous AI software engineering agents [81].
- **Sampling Strategy**: The qualitative behavior model was derived from the most interactive participant per condition, potentially underrepresenting low-interaction student behaviors [82].
- **Temporal Horizon**: Experiment conducted in early 2024 reflects tool models available at that time [82].
- **Observer Effect**: Awareness of screen and audio recording may induce mild cautious behavior, though remote execution and guaranteed compensation mitigated performance anxiety [83].

---

## Contribuicao Principal

The primary contribution of this paper is a granular, empirical characterization of CS students' interaction dynamics and decision-making processes when working with AI coding assistants [4, 7]. By developing a dedicated experimental platform that captured multimodal process logs and screen recordings from 27 students across 3 task types and 3 ACATs, the authors introduce a novel Five-Layer Hierarchical Interaction Behavior Model (*Prompt*, *Understanding*, *Decision*, *Adaption*, *Backtrack*), classify 22 decision-making factors, 11 challenges, and 23 expectations, and operationalize self-perceived productivity using the SPACE framework [4, 7, 16, 26, 29, 72]. The study provides actionable design recommendations for tool creators (such as improving feature visibility and context-aware suggestion ranking), practical usage guidelines for student developers (e.g., avoiding retrofitting existing code to fit AI suggestions and leveraging "slow accept" for active learning), and rich empirical benchmarks for software engineering education researchers [7, 50, 53, 72, 84, 85].

---

*Extraido via NotebookLM em October 2026 para MLR: Software Developer Metrics in Practice*

---

💡 **Gostaria de explorar mais a fundo este artigo?** Posso criar um relatório detalhado comparando os achados do P2038 com outros estudos da sua revisão sobre o impacto do GitHub Copilot e ferramentas de IA na produtividade e aprendizado de desenvolvedores.
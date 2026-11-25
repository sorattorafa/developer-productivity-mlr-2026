# P2025 — Code with Me or for Me? How Increasing AI Automation Transforms Developer Workflows

**Decisao: INCLUIDO | Qualidade: 5/5**

---

## Dados Bibliograficos

| Campo | Valor |
|-------|-------|
| **ID** | P2025 |
| **Autores** | Valerie Chen, Ameet Talwalkar, Robert Brennan, Graham Neubig [1] |
| **Ano** | 2026 [2, 3] |
| **Venue** | ACM Conference on Human Factors in Computing Systems (CHI '26) [3] |
| **DOI** | 10.1145/3772318.3790850 [2, 3] |
| **Tipo** | Conference paper [3] |
| **Metodo** | Mixed methods (Controlled within-subjects user study, quantitative task correctness and user effort measurements, 5-point Likert surveys, and qualitative trajectory and prompt analysis) [4-7] |
| **Amostra** | 20 participants (students recruited via university mailing lists; 60% with 3–5 years professional experience, 25% with 0–2 years, 15% with 6–10 years; 95% intermediate to advanced Python proficiency; all regular GitHub Copilot users, novice agent users) [8] |
| **Contexto** | Academic / University context (evaluating realistic Python tasks in open-source repositories like Matplotlib and Scikit-learn, alongside GAIA data analysis problems) [8, 9] |
| **Modo de trabalho** | Remote (asynchronous study conducted in participants' own time) [10] |
| **Metodologia** | Not specified [8, 9] |

---

## Objetivo

This paper presents the first controlled user study comparing developer interactions with coding copilots (specifically GitHub Copilot) versus autonomous coding agents (specifically OpenHands) [4, 11]. The main objective is to characterize how increasingly autonomous AI tools affect developer productivity, user experience, and interaction patterns when solving realistic multi-file software engineering tasks [11-13].

---

## Questoes de Pesquisa

- **RQ1**: How do agents and copilots compare in terms of effect on user productivity? [14]
- **RQ2**: How do agents and copilots compare in terms of effect on user experience? [8]
- **RQ3**: How do developers interact with different coding assistants? [8]

---

## Metricas e Instrumentos de Avaliacao

| Metrica | Categoria | Nivel | Como Coletada | Validada |
|---------|-----------|-------|---------------|----------|
| Task Correctness Rate | Quality | Individual | Automated test cases executed on final code snapshots pushed to GitHub [6, 7] | Yes |
| User Time Spent (User Effort) | Productivity | Individual | Sum of active time spent by the user inspecting outputs and writing instructions (measured via screen recordings for Copilot and event stream logs for OpenHands) [5, 7] | Yes |
| Cognitive Load | DevEx | Individual | Post-task survey with 5-point Likert scale (C1 comparison statement) [6, 15] | Partial |
| Perceived Ability (Accomplishing New Tasks) | DevEx | Individual | Post-task survey with 5-point Likert scale (C2 comparison statement) [15, 16] | Partial |
| Task Completion Speed | Productivity | Individual | Post-task survey with 5-point Likert scale (C3 comparison statement) [17, 18] | Partial |
| Flow State | DevEx | Individual | Post-task survey with 5-point Likert scale (C4 comparison statement) [17, 18] | Partial |
| User Satisfaction | Satisfaction | Individual | Post-task survey with 5-point Likert scale (C5 comparison statement) [17, 18] | Partial |
| Output Understanding | DevEx | Individual | Post-task survey with 5-point Likert scale (C6 comparison statement) [18, 19] | Partial |
| Perceived AI Competence | Quality | Individual | Post-task survey with 5-point Likert scale (F1 statement) [20, 21] | Partial |
| Tool Preference / Future Adoption Intent | Satisfaction | Individual | Post-task survey with 5-point Likert scale (F2 statement) [20, 21] | Partial |

---

## Frameworks e Metricas

### Frameworks Referenciados
- **SPACE**: REFERENCED (cited in related work regarding developer productivity and user experience assessment) [12, 22].
- **CUPS (Developer Activities Taxonomy)**: REFERENCED (Mozannar et al., 2024 taxonomy of programmer activities when interacting with code completions) [5, 23].
- **Acceleration vs. Exploration Framework**: REFERENCED (Barke et al., 2023 framework classifying developer usage of code-generating models) [24, 25].

### Frameworks Propostos
The paper does not propose a new formal quantitative metric framework, but formulates **Three Design Desiderata for Collaborative Coding Agents**:
1. **Transparent Agent Behaviors**: Agents should provide clear explanations of what changes were made across multiple files and why [26].
2. **Balanced Level of Proactivity**: Agents must calibrate confidence and resource bounds to prevent making excessive or unrequested code/file edits [21, 27].
3. **Effective Leverage of Human Effort**: Agents should optimize interactive latency and support mixed-initiative multi-tasking workflows [28].

---

## Fatores que Influenciam Produtividade

### Fatores Positivos
| Fator | Categoria |
|-------|-----------|
| Autonomous multi-step execution, file navigation, and code editing capabilities of agents [29, 30] | Technical |
| Automated environment setup and dependency installation by coding agents [31] | Process |
| Automated execution, testing, and debugging of generated code by agents [32, 33] | Process |
| Direct repository inspection and web browsing capabilities to fetch context [34, 35] | Technical |

### Fatores Negativos
| Fator | Categoria |
|-------|-----------|
| High time spent manually configuring Python environments and dependencies in copilot workflows [31] | Process |
| Effort required to manually craft detailed prompts and supply context in copilot workflows [35, 36] | Human |
| Slow agent code generation speed leading to developer waiting time [28] | Technical |
| Overly proactive agent actions (creating excessive files or edits without user bounds) [21, 27] | Technical |
| Low visibility and difficulty understanding complex multi-file changes made by agents [19, 26] | Human |

---

## Papel da IA e Automacao

| Campo | Valor |
|-------|-------|
| **Usa IA/ML?** | Yes — evaluates LLM-based coding tools: GitHub Copilot (using GPT-4o, Claude Sonnet 3.7, Gemini 2.5 Pro, or o3-mini) and OpenHands agent (powered by Claude Sonnet 3.7) [34, 37]. |
| **Automacao de coleta?** | Yes — user telemetry, event stream logs, and timestamped interaction events were automatically logged via the OpenHands web app [5, 38]. |
| **Impacto de IA na produtividade?** | Access to agents resulted in a statistically significant 35% increase in task correctness rate (60% for OpenHands vs. 25% for GitHub Copilot, \\(p=0.02\\)) and reduced active user effort by half (12.5 minutes for agents vs. 25.1 minutes for copilots, \\(p=0.01\\)). Total elapsed execution time was comparable (27.9 minutes) [39, 40]. |

---

## Resultados Principais

- **Task Correctness**: Participants using the coding agent achieved a 60% task correctness rate compared to 25% with the copilot, representing a statistically significant 35% improvement (\\(p = 0.02\\)) [39]. Data analysis tasks were solved exclusively when participants had access to the agent [39].
- **User Effort**: Active user effort was significantly reduced when using agents (12.5 minutes) compared to copilots (25.1 minutes, \\(p = 0.01\\)) [40].
- **Cognitive Load & Perceived Ability**: 75% of participants experienced less cognitive load with OpenHands (\\(p = 0.0006\\)), and 70% reported being able to accomplish new tasks they could not complete previously (\\(p = 0.0013\\)) [15, 16].
- **Output Understanding**: A majority of participants (55%) understood copilot outputs better than agent outputs (\\(p = 0.07\\)), noting that agent edits often felt hidden or hard to control [19].
- **Perceived Competence vs. Preference**: While 70% agreed OpenHands was more competent than a human programmer (\\(p = 0.002\\)), 60% still preferred to continue using GitHub Copilot over OpenHands moving forward (\\(p = 0.04\\)) [20, 21].
- **Workflow Role Shift**: Mechanical tasks (environment setup, running tests, debugging) shifted from human-driven in copilot workflows to AI-driven in agent workflows, moving developers into a supervisory/managerial role [25, 31, 41].

---

## Desafios do Uso das Metricas

- Total elapsed time in agentic workflows does not reflect active developer effort due to autonomous agent background execution [7, 40].
- Static benchmarks (e.g., HumanEval, SWE-Bench) evaluate AI outputs in isolation and fail to capture interactive human-in-the-loop nuances, downstream user utility, or cognitive burden [42-44].
- Evaluating task completion speed is confounded by model response latency versus multi-step iteration efficiency [17, 28].
- Lack of fine-grained telemetry metrics to separate time spent visually inspecting multi-file diffs from time spent crafting natural language prompts [26, 36].

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

- **Single Copilot and Agent Pair**: Evaluated only GitHub Copilot and OpenHands, with OpenHands fixed to Claude Sonnet 3.7 [34, 37, 45].
- **Novice Agent Users**: Participants were experienced copilot users but had no prior experience with coding agents [8, 45].
- **Sample Demographic & Task Scope**: Participant pool consisted of 20 university students working on pre-defined Python tasks in 40-minute blocks [8, 10, 45, 46].
- **Asynchronous Study Environment**: Tasks were executed in isolated experimental sessions, which does not reflect multi-day development cycles or multi-tasking while waiting for agent output [10, 46].
- **Pre-defined Task Lifecycle**: Pre-defined tasks focused on popular Python libraries and did not cover low-resource languages or early software engineering phases like project planning and specification [46].

---

## Contribuicao Principal

The paper provides the first controlled empirical study comparing human developer workflows across AI copilots and autonomous AI coding agents on realistic software development tasks [4, 11]. It demonstrates that while agents significantly improve task correctness (+35%) and cut active developer effort in half, critical user experience limitations—such as lack of transparency, difficulty understanding multi-file edits, and over-proactivity—currently lead developers to prefer copilots for daily work, establishing three key design desiderata for future collaborative AI agents [21, 26-29, 47].

---

*Extraido via NotebookLM em October 2026 para MLR: Software Developer Metrics in Practice*

---

💡 Would you like me to generate a slide deck outline or summary report based on these findings?
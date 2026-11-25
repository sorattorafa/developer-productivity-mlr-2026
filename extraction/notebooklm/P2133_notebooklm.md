# P2133 — Reading between the lines: Modeling user behavior and costs in AI-assisted programming

**Decisao: INCLUIDO | Qualidade: 5/5**

---

## Dados Bibliograficos

| Campo | Valor |
|-------|-------|
| **ID** | P2133 |
| **Autores** | Hussein Mozannar, Gagan Bansal, Adam Fourney, Eric Horvitz [1] |
| **Ano** | 2024 [2, 3] |
| **Venue** | Proceedings of the CHI Conference on Human Factors in Computing Systems (CHI '24) [2, 3] |
| **DOI** | 10.1145/3613904.3641936 [2, 3] |
| **Tipo** | Conference paper [2, 3] |
| **Metodo** | Mixed methods (Pilot study, User study with retrospective video labeling, State machine/Markov chain modeling, Post-study survey) [4-7] |
| **Amostra** | 21 programmers (software engineers, researchers, graduate student interns; 19 Python, 1 C++, 1 JavaScript) [5, 8, 9] |
| **Contexto** | Industry / Corporate Research Lab (Microsoft Research / large organization setting; Visual Studio Code with GitHub Copilot) [1, 7, 8] |
| **Modo de trabalho** | Not specified (User study conducted via video call accessing a remote virtual machine) [7] |
| **Metodologia** | Not specified [7] |

---

## Objetivo

The main objective of this paper is to investigate human-AI interaction in AI-assisted programming (specifically GitHub Copilot) at a granular level in order to identify developer behaviors, interaction costs, and workflow inefficiencies [2, 4]. To achieve this, the authors introduce CUPS (CodeRec User Programming States), a novel taxonomy of programmer activities between telemetry events, and use it to profile developer coding sessions, evaluate cognitive time spent across different interaction states, and propose improved evaluation metrics and interface designs [4, 5, 10].

---

## Questoes de Pesquisa

- **RQ1**: What activities do users undertake in anticipation for, or to trigger a suggestion? [4]
- **RQ2**: What mental processes occur while the suggestions are onscreen, and do people double-check suggestions before or after acceptance? [4]
- **RQ3**: How costly for users are these various new tasks, and which take the most time? [4]

---

## Metricas e Instrumentos de Avaliacao

| Metrica | Categoria | Nivel | Como Coletada | Validada |
|---------|-----------|-------|---------------|----------|
| Task Completion Time [11-13] | Productivity | Individual | Measured in seconds from first line of code written until task completion or 20-minute limit | Yes |
| Suggestion Acceptance Rate [13-16] | Activity / Productivity | Individual | Calculated automatically via IDE telemetry (accepted suggestions / total shown suggestions) | Yes |
| CUPS State Dwell Time (% Session Time) [5, 13, 17] | Activity / DevEx | Individual | Collected via retrospective self-labeling of video-recorded telemetry segments by participants | Yes |
| Time to Accept / Onscreen Display Duration [14, 18-20] | Productivity / Activity | Individual | Telemetry timestamp difference between suggestion display ('shown') and user action ('accept') | Partial |
| Adjusted Suggestion Verification Time [19-21] | Quality / Productivity | Individual | Calculated by adding post-acceptance verification time (dwell time in 'Thinking/Verifying' or 'Editing Last Suggestion' after accepting) to pre-action verification time | Yes |
| Survival Rate of Accepted Code (10-min survival) [20] | Quality / Productivity | Individual / Team | Proposed metric measuring the fraction of accepted suggestions that remain in the codebase after a set period (e.g., 10 minutes) | Yes |
| Prompt Crafting Success Rate [22] | Productivity / Activity | Individual | Measured as the ratio of prompt crafting attempts that successfully lead to an accepted suggestion | Yes |
| SPACE Framework Survey Metrics [8, 23-25] | Satisfaction / DevEx | Individual | Post-study Likert-scale questionnaire measuring perceived productivity, flow, information search, and code quality concerns | Yes |
| State Transition Probability & Entropy Rate [5, 26, 27] | Activity / Process | Individual / Aggregated | Derived from Markov chain state transition matrix across CUPS states during coding sessions | Yes |

---

## Frameworks e Metricas

### Frameworks Referenciados
- **SPACE Framework**: REFERENCED & APPLIED — Cited as the foundation for evaluating developer productivity and experience [23, 28, 29], and applied in the post-study questionnaire [8, 24, 25].
- **Keystroke-Level Model (KLM / GOMS)**: REFERENCED — Cited to contextualize assigning time costs to both cognitive/mental processes and physical typing actions [30].

### Frameworks Propostos
- **CodeRec User Programming States (CUPS)**: A 12-state finite-state machine taxonomy proposed to model programmer intents, activities, and cognitive states during interaction with code recommendation tools [4, 5, 30]. CUPS organizes activities hierarchically into two root segment types ('User Before Action' and 'User Typing or Paused') leading to 12 distinct leaf states: *Thinking/Verifying Suggestion*, *Not Thinking*, *Deferring Thought For Later*, *Thinking About New Code To Write*, *Waiting For Suggestion*, *Writing New Functionality*, *Editing Last Suggestion*, *Editing Written Code*, *Prompt Crafting*, *Writing Documentation*, *Debugging/Testing Code*, and *Looking Up Documentation* [30-33].

---

## Fatores que Influenciam Produtividade

### Fatores Positivos
| Fator | Categoria |
|-------|-----------|
| Rapid automated code generation for boilerplate code and repetitive tasks [3, 25, 34] | Technical |
| Reduced context switching and reliance on external documentation or search engines (e.g., Stack Overflow) [25] | Process |
| Enhanced developer flow and reduced mental friction when implementing familiar logic [25] | Human |
| High prompt crafting attempt success rate (81.3% of prompt crafting sequences yield accepted code) [22] | Technical |
| Thorough pre-acceptance verification of suggestions, reducing post-hoc editing likelihood (down to 18%) [15] | Process |

### Fatores Negativos
| Fator | Categoria |
|-------|-----------|
| High time overhead required for verifying AI recommendations (22.4% of total session time) [17] | Human |
| IDE latency and explicit waiting for AI suggestions to appear (4.2% of session time) [17, 19, 27] | Technical |
| Unwanted interruptions and popups during prompt crafting (89.3% of suggestions displayed while crafting prompts are rejected/ignored) [35] | Process / Technical |
| Deferring thought (accepting unverified code to gain syntax highlighting or see complete implementations), which incurs high post-acceptance editing probability (53%) [15, 36, 37] | Human / Process |
| Developer anxiety regarding code quality, subtle bug introduction, or learning outdated/deprecated practices [25] | Technical / Human |

---

## Papel da IA e Automacao

| Campo | Valor |
|-------|-------|
| Usa IA/ML? | Yes — GitHub Copilot, an LLM-based code recommendation engine built on Transformer architectures (Codex), generates inline code completions inside Visual Studio Code [3, 7, 14]. |
| Automacao de coleta? | Yes — IDE telemetry automatically recorded user actions (shown, accepted, rejected, browse) and timestamps [14], which were coupled with screen video recordings for retrospective segment annotation [6, 7, 38]. |
| Impacto de IA na produtividade? | Significant transformation of developer workflows [3, 39]. While 17/21 participants reported completing tasks faster and 16/21 felt more productive [25], Copilot introduces major cognitive overheads, with 51.5% of total session time spent on Copilot-centric activities (22.4% verifying suggestions, 11.9% editing last suggestion, 11.6% prompt crafting, 4.2% waiting for suggestions, 1.4% deferring thought) [17, 40]. Raw acceptance rates overstate productivity by ignoring post-acceptance verification time [19, 20]. |

---

## Resultados Principais

- **High Dwell Time in Copilot-Centric States**: Participants spent an average of **51.5%** (\\(\pm 19.3\%\\)) of their session duration in Copilot-specific activities (verifying suggestions, deferring thought, waiting for suggestions, prompt crafting, and editing suggestions) [40].
- **Suggestion Verification Overhead**: Verifying suggestions was the single largest consumer of developer time, accounting for **22.4%** (\\(\pm 12.97\%\\)) of session time on average, and exceeding 10% of session time for 20 out of 21 participants [17].
- **Underestimation of Verification Time**: Accounting for post-acceptance verification increases the measured mean verification time from **3.25s** to **15.21s** (nearly 5-fold) for deferred suggestions, and from **3.96s** to **7.03s** for pre-verified suggestions (\\(p < 0.001\\)) [19].
- **Deferred Thought & Verification Debt**: Deferring thought (accepting suggestions without pre-verification, observed 61 times) resulted in a **53%** probability of subsequently editing the accepted code (compared to 18% when verified prior to acceptance, \\(p < 0.001\\)) and a **53.2%** probability of verifying it immediately post-acceptance [15, 19, 37].
- **Prompt Crafting Dynamics**: Suggestions displayed *during* active prompt crafting were overwhelmingly ignored or rejected (**89.3%** rejected/ignored, only 10.7% accepted) [35]. However, overall prompt crafting sequences were effective, with **81.3%** of 59 prompt crafting attempts resulting in an accepted suggestion [22].
- **Telemetry Acceptance Rate**: Participants accepted **34.0%** of 1,024 total shown suggestions, with an average participant acceptance rate of **36.5%** (median 33.8%, range 14.3%–60.7%) [13].
- **Perceived Developer Benefits vs. Concerns**: On post-study surveys, **17/21** developers agreed Copilot helped them code faster, **16/21** felt more productive, and **14/21** reported staying in flow [25]. Conversely, **6/21** expressed concerns regarding code quality, subtle bugs, or outdated code patterns [25].

---

## Desafios do Uso das Metricas

- **Incompleteness of Onscreen Display Time**: Measuring "time to accept" solely as the duration between suggestion display and acceptance misses substantial verification time spent *after* acceptance [18-20].
- **Inflation of Acceptance Rates**: Acceptance rates are inflated by "deferred thought" behaviors, where developers accept suggestions prematurely to get syntax highlighting or view multi-line completions rather than confirming correctness [18, 20, 36].
- **Telemetry Blindness to Cognitive States**: Standard IDE telemetry captures instantaneous actions (accept, reject) but cannot distinguish between active verification, deferred thought, documentation lookup, or prompt crafting during pause segments [31, 41].
- **Distractive Inline Popup Timing**: Displaying suggestions automatically whenever a user pauses can interrupt active prompt engineering or creative problem-solving, leading to low acceptance rates (10.7% during prompt crafting) and cognitive distraction [35, 42].

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

- **Time-Limited Synthetic Tasks**: Coding tasks were pre-selected, constrained to 20 minutes, and performed on a remote virtual machine rather than observing real-world software engineering over longer projects [7, 43, 44].
- **Language Bias**: 19 of the 21 participants used Python (with only 1 C++ and 1 JavaScript user), which may limit generalizability to other programming languages and paradigms [9, 44].
- **Single-State Segment Granularity**: Telemetry segments were limited to a single predominant CUPS label, whereas developers might execute multiple rapid activities within a single segment in practice [33, 44].
- **Absence of Long-Term Horizon Costs**: The study did not evaluate long-term maintenance costs, security vulnerability rates, or cognitive over-reliance resulting from AI code acceptance [44].
- **Organizational Sample Homogeneity**: Participants were recruited from developer lists within a single corporate organization (Microsoft), which could introduce organizational or tool-familiarity biases [8, 44].

---

## Contribuicao Principal

The paper's main contribution is the proposal and empirical validation of CUPS (CodeRec User Programming States), a 12-state taxonomy and Markov state-machine framework for modeling programmer intents, cognitive processes, and interaction costs in AI-assisted programming [4, 5, 21, 26]. Through a user study with 21 programmers annotating 3,137 telemetry segments, the authors demonstrate that AI assistance alters developer behavior significantly — with developers spending 51.5% of session time on Copilot-related tasks and 22.4% on suggestion verification alone [17, 40]. Crucially, the paper proves that conventional IDE telemetry metrics severely underestimate verification time (by up to 5-fold) due to post-acceptance verification [19, 20], providing actionable guidelines for adjusted evaluation metrics and context-aware AI interface designs [20, 42, 45].

---

*Extraido via NotebookLM em October 2026 para MLR: Software Developer Metrics in Practice*

---

💡 *Se desejar, posso gerar um relatório detalhado em PDF ou criar um conjunto de flashcards/quiz sobre a taxonomia CUPS e os impactos de produtividade para facilitar a sua revisão.*
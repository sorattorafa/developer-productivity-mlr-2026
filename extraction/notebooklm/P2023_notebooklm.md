# P2023 — Evolving with AI: A Longitudinal Analysis of Developer Logs

**Decisao: INCLUIDO | Qualidade: 5/5**

---

## Dados Bibliograficos

| Campo | Valor |
|-------|-------|
| **ID** | P2023 |
| **Autores** | Agnia Sergeyuk, Eric Huang, Dariia Karaeva, Anastasiia Serova, Yaroslav Golubev, Iftekhar Ahmed [1] |
| **Ano** | 2026 [2] |
| **Venue** | IEEE/ACM 48th International Conference on Software Engineering (ICSE ’26) [2] |
| **DOI** | 10.1145/3744916.3787811 [2] |
| **Tipo** | Conference paper [2] |
| **Metodo** | Mixed methods (Longitudinal IDE telemetry analysis, Survey, Semi-structured interviews) [3-5] |
| **Amostra** | 800 developers for IDE telemetry (400 AI users, 400 AI non-users over 2 years, 151,904,543 logged events); 62 survey respondents; 5 post-survey interview participants [3, 4, 6, 7] |
| **Contexto** | Industry / Professional software development (JetBrains ecosystem, users of IntelliJ IDEA, PyCharm, PhpStorm, WebStorm across various programming languages and ecosystems) [4, 6, 8, 9] |
| **Modo de trabalho** | Not specified [6] |
| **Metodologia** | Not specified [6] |

---

## Objetivo

The main objective of this paper is to investigate the sustained, long-term influence of AI-powered coding assistants on professional software developers' daily workflows [3, 4]. By combining a two-year longitudinal analysis of fine-grained IDE telemetry logs from 800 developers with a survey of 62 professionals and follow-up interviews, the study analyzes five key dimensions of workflow change—productivity, code quality, code editing, code reuse, and context switching—comparing objective behavioral events with subjective developer perceptions [3, 4, 10].

---

## Questoes de Pesquisa

- **RQ1**: How did the introduction of AI tools influence the productivity of developers? [10]
- **RQ2**: How did the introduction of AI tools influence code quality? [10]
- **RQ3**: How did the introduction of AI tools influence practices of code editing? [10]
- **RQ4**: How did the introduction of AI tools influence practices of code reuse? [10]
- **RQ5**: How did the introduction of AI tools influence practices of context switching? [10]

---

## Metricas e Instrumentos de Avaliacao

| Metrica | Categoria | Nivel | Como Coletada | Validada |
|---------|-----------|-------|---------------|----------|
| Typed characters | Productivity | Individual | IDE Telemetry (Monthly aggregate count of typed characters in the editor) [11, 12] | Yes [11] |
| Perceived productivity | Productivity | Individual | Survey (5-point Likert scale) [13, 14] | Yes [8] |
| Time spent coding | Productivity | Individual | Survey (5-point Likert scale) [13, 14] | Yes [8] |
| Debugging instances | Quality | Individual | IDE Telemetry (Monthly aggregate count of hotkey/contextual debugging activations) [11, 12] | Yes [11] |
| Perceived code quality | Quality | Individual | Survey (5-point Likert scale) [14] | Yes [8] |
| Perceived code readability | Quality | Individual | Survey (5-point Likert scale) [14] | Yes [8] |
| Deletions | Activity / DevEx | Individual | IDE Telemetry (Monthly aggregate count of delete keystrokes, backspaces, and undos) [11, 12] | Yes [11] |
| Perceived code editing frequency | Activity / DevEx | Individual | Survey (5-point Likert scale) [14] | Yes [8] |
| External pastes | Collaboration / Reuse | Individual | IDE Telemetry (Monthly aggregate count of external code pastes not preceded by in-IDE copy) [11, 12] | Yes [11] |
| Perceived code reuse frequency | Collaboration / Reuse | Individual | Survey (5-point Likert scale) [14] | Yes [8] |
| IDE window activations | Activity / DevEx | Individual | IDE Telemetry (Monthly aggregate count of switches back to the IDE from an inactive state) [11, 12] | Yes [11] |
| Perceived context switching frequency | Activity / DevEx | Individual | Survey (5-point Likert scale) [14] | Yes [8] |

---

## Frameworks e Metricas

### Frameworks Referenciados
- **SPACE**: REFERENCED (Cited in related work regarding multidimensional developer productivity dimensions [15, 16]).

### Frameworks Propostos
The paper does not propose a new formal named framework, but establishes an empirical 5-dimension evaluation model (Productivity, Code Quality, Code Editing, Code Reuse, Context Switching) linking behavioral telemetry metrics with developer perception metrics [3, 10, 17].

---

## Fatores que Influenciam Produtividade

### Fatores Positivos
| Fator | Categoria |
|-------|-----------|
| In-IDE AI assistance (code completion, AI chat, code generation, documentation) [18, 19] | Technical |
| Immediate AI help with naming and documentation when developers get stuck [20] | Process |
| Reduced social pressure during code review ("AI as a second pair of eyes") [21] | Human |
| Reduced external context switching when finding quick code answers in-IDE [22] | Process |

### Fatores Negativos
| Fator | Categoria |
|-------|-----------|
| Cognitive overhead, task fragmentation, and frequent context shifts when managing AI suggestions [22-24] | Human |
| Time wasted crafting and refining prompts to obtain desired solutions [20] | Process |
| Effort required to verify, refine, heavy rewrite, or discard suboptimal/imperfect AI code [25, 26] | Technical |
| Skepticism and paranoid triple-checking of AI-generated output [27] | Human |

---

## Papel da IA e Automacao

| Campo | Valor |
|-------|-------|
| Usa IA/ML? | Yes — Investigates general in-IDE AI coding assistants (JetBrains AI Assistant, GitHub Copilot, ChatGPT) providing code completion, AI chat, code generation, and documentation [7, 18, 19]. |
| Automacao de coleta? | Yes — Uses automated, anonymized, fine-grained IDE telemetry logging continuously over two years [4, 28, 29]. |
| Impacto de IA na produtividade? | Positive perceived impact (82.3% report increased productivity; 56.5% report decreased coding time) [30, 31]. Telemetry shows AI users write code significantly faster (+587 typed characters/month vs +75 for non-users), but also delete substantially more (+102 deletions/month vs +7.6 for non-users) [31-34]. |

---

## Resultados Principais

- **Productivity (RQ1)**: 82.3% of survey respondents reported increased productivity and 56.5% indicated decreased time spent coding [30, 31]. Telemetry revealed typed characters increased significantly faster for AI users (+587 characters/month) than AI non-users (+75 characters/month) [31, 32].
- **Code Quality (RQ2)**: 48.4% of respondents reported improved code quality and 43.5% reported improved readability, though nearly 50% perceived no change [31, 35]. Telemetry showed debugging activity remained stable for AI users (no significant trend) while declining slightly for non-users (−0.46 sessions/month) [27, 34].
- **Code Editing (RQ3)**: 43.5% of respondents perceived increased code editing frequency, while 50% reported no change [21, 34]. Telemetry showed code deletions increased substantially faster for AI users (+102 deletions/month) compared to non-users (+7.6 deletions/month) [33, 34].
- **Code Reuse (RQ4)**: Survey respondents were split on external code reuse (37.1% increased, 19.4% decreased, 43.5% no change) [34, 36]. Telemetry showed external pastes increased slightly faster for AI users (+1 paste/month) than non-users (+0.4 pastes/month) [37, 38].
- **Context Switching (RQ5)**: Respondents were divided on context switching frequency (25.8% increased, 21.0% decreased, 53.2% no change) [38, 39]. Telemetry showed IDE window activations increased slightly for AI users (+6.4 activations/month) while decreasing for non-users (−7.6 activations/month) [22, 38].
- **Perception vs. Telemetry Gap**: AI adoption redistributes effort across more fragmented, reactive tasks (curation, editing, verification), creating a disconnect where developers feel clear productivity gains while fine-grained telemetry reveals higher deletion rates and context switching [38, 40, 41].

---

## Desafios do Uso das Metricas

- Disconnect between self-reported developer perceptions and objective behavioral telemetry logs across workflow dimensions [38, 41, 42].
- Over-reliance vs. under-utilization anti-patterns: some developers place undue trust in AI output without critical evaluation, while others express high skepticism and paranoid verification overhead [7, 27, 43, 44].
- Telemetry proxy limitations: low-level IDE action counts (typing, deletions, window switches) capture event volume but lack developer intent, task context, or direct attribution to specific AI suggestions [42, 45].
- Increased curation burden: AI accelerates code generation but shifts developer effort toward code review, filtering, editing, and deleting inefficient generated snippets [25, 26, 38].

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

- **Single IDE Vendor Scope**: Behavioral telemetry is gathered exclusively from JetBrains IDEs, and AI user classification relies on JetBrains AI Assistant interaction [46].
- **Potential Misclassification**: Developers using external AI tools (e.g., web browser ChatGPT) without in-IDE assistant integration might be misclassified as non-users [46].
- **Lack of Task Intent**: Telemetry logs capture event frequencies but do not record developer intent, problem complexity, or collaboration context [42].
- **Sample Selection**: Analyzed AI users were early adopters who maintained active usage over 6+ months, which may not fully represent all developers or casual AI users [41, 47].
- **Pre-Agentic Focus**: Telemetry reflects AI interaction primarily through inline completions and chat suggestions, prior to fully autonomous agentic workflows [48].

---

## Contribuicao Principal

The paper provides a comprehensive two-year longitudinal mixed-methods empirical analysis of professional developers using AI coding assistants, combining 151+ million IDE telemetry events from 800 developers with survey data from 62 professionals [3, 4, 49]. It reveals that while AI accelerates code authoring and is perceived as highly boosting productivity, it quietly restructures software workflows by increasing code editing/deletions, external code integration, and context switching—demonstrating a persistent disconnect between developers' subjective perceptions and their actual daily behavioral telemetry [3, 40, 41, 49].

---

*Extraido via NotebookLM em October 2026 para MLR: Software Developer Metrics in Practice*

---

📊 Would you like me to generate a chart comparing the telemetry trend rates (e.g., typed characters, deletions, pastes, context switches) between AI users and AI non-users, or compile this structured summary into a formatted PDF or report artifact?
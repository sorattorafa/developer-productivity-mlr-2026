# P2131 — Significant productivity gains through programming with large language models

**Decisao: INCLUIDO | Qualidade: 5/5**

---

## Dados Bibliograficos

| Campo | Valor |
|-------|-------|
| **ID** | P2131 |
| **Autores** | Thomas Weber, Maximilian Brandmaier, Albrecht Schmidt, Sven Mayer [1] |
| **Ano** | 2024 [2] |
| **Venue** | Proceedings of the ACM on Human-Computer Interaction (Proc. ACM Hum.-Comput. Interact., Vol. 8, No. EICS, Article 256) [2] |
| **DOI** | 10.1145/3661145 [2] |
| **Tipo** | Journal article [2] |
| **Metodo** | Controlled experiment / User study (Within-subjects, N=24) [1, 3] |
| **Amostra** | 24 participants (out of 29 recruited, 5 excluded; 4 female, 20 male, mean age 26.8, SD 3.6; 5 Master's, 16 Bachelor's, 3 pursuing degree; 9 professional developers, 15 with academic/personal coding experience) [4] |
| **Contexto** | Mixed (Academic and Industry participants recruited across LMU Munich channels and professional networks; tasks executed in Python in a standardized remote desktop virtual environment) [4-6] |
| **Modo de trabalho** | Remote (study conducted via remote desktop virtual machine setup) [6] |
| **Metodologia** | Not specified (individual task execution under experimental conditions) [3, 7] |

---

## Objetivo

This paper aims to investigate how AI assistance for code generation impacts developer productivity and interaction behavior across different interaction paradigms [1, 3]. Specifically, it evaluates and compares an AI auto-complete interface (using GitHub Copilot) and a conversational system (using a GPT-3 chatbot panel in Visual Studio Code) against a traditional web-browser-only baseline in a within-subjects user study (N=24) structured around the five dimensions of the SPACE productivity framework [1, 3, 8].

---

## Questoes de Pesquisa

*Note: The paper does not explicitly label questions as "RQ1/RQ2" in the text, but addresses the following core research questions:*

- **RQ1**: How do different AI coding support mechanisms (inline auto-complete vs. conversational chat) impact software developer productivity across the SPACE framework dimensions compared to a browser-only baseline? [3, 8]
- **RQ2**: How do interaction paradigms influence developer usage strategies, information retrieval behaviors, and code snippet acceptance patterns? [1, 3, 9]
- **RQ3**: How does the use of AI coding assistants affect objective code quality metrics (functional correctness, maintainability) and developer code authoring composition? [10, 11]

---

## Metricas e Instrumentos de Avaliacao

| Metrica | Categoria | Nivel | Como Coletada | Validada |
|---------|-----------|-------|---------------|----------|
| **AttrakDiff (Pragmatic Quality, Hedonic Quality, Attractiveness)** | Satisfaction | Individual | Post-task survey questionnaire (10 questions on Likert scale) [8, 12] | Yes [8, 13] |
| **Perceived Productivity & Satisfaction** | Satisfaction | Individual | End-of-study survey using agree-disagree Likert scales [8, 14] | Yes [14, 15] |
| **Requirement Implementation Correctness (% of correct features)** | Quality (Performance) | Individual | Automated unit testing against pre-defined test criteria [10, 16] | Yes [10] |
| **Maintainability Index** | Quality (Performance) | Individual | Static code analysis combining Cyclomatic Complexity and Halstead Volume [10, 17] | Yes [4, 10] |
| **Percentage of Comments** | Quality (Performance) | Individual | Static code analysis of submitted code files [10, 18] | Yes [10] |
| **Character Output per Minute (Human Authoring Rate)** | Activity | Individual | Automated activity logging normalized by total completion time [11, 19, 20] | Yes [19] |
| **Percentage of Code Created by Human vs. AI** | Activity | Individual | Telemetry logging comparing human keypresses against AI insertions [11, 20] | Yes [11] |
| **Number of Accepted Snippets (Browser / AI / Total)** | Communication | Individual | Interaction logging and screen recording analysis [9, 20] | Yes [9] |
| **Volume of Accepted Characters (Browser / AI / Total)** | Communication | Individual | Telemetry logging of executable code accepted from external sources [9, 20] | Yes [9] |
| **Average Snippet Size (Browser / AI / Total)** | Communication | Individual | Derived by dividing total accepted characters by number of accepted snippets [9, 20] | Yes [9] |
| **Requirements Implemented per Minute (Task Speed)** | Efficiency | Individual | Count of implemented sub-task requirements normalized by task duration [17, 21] | Yes [21] |
| **Task Completion Time** | Efficiency | Individual | Screen recording and background process timer logs [21, 22] | Yes [21] |

---

## Frameworks e Metricas

### Frameworks Referenciados
- **SPACE Framework** (Forsgren et al., 2021) [8, 15]: **APPLIED** — Used as the overarching holistic framework to measure productivity across Satisfaction, Performance, Activity, Communication, and Efficiency [8].
- **AttrakDiff** (Hassenzahl et al., 2003) [8, 13]: **APPLIED** — Used as a validated measurement instrument for subjective user experience and satisfaction (pragmatic quality, hedonic quality, attractiveness) [8, 12].
- **Lines of Code (LoC) / Function Points / Halstead Effort** (Petersen 2011; Hernández-López et al. 2013; Oliveira et al. 2020) [23-26]: **REFERENCED** — Discussed in literature review regarding traditional code-centric productivity measurement [23-25, 27].

### Frameworks Propostos
The paper does not propose a new measurement framework; rather, it operationalizes the SPACE framework specifically for evaluating multi-modal AI programming assistants (auto-complete vs. conversational chat) [3, 8, 28].

---

## Fatores que Influenciam Produtividade

### Fatores Positivos
| Fator | Categoria |
|-------|-----------|
| Rapid code generation from natural language prompts and comments [1, 29] | Technical |
| Inline code auto-completion (GitHub Copilot) reducing context switching [30-32] | Process / Technical |
| Conversational chat assistance (GPT-3) generating complete functions and explanatory code blocks [33-35] | Technical |
| Lowering entry barriers and initial effort when working with unfamiliar modules or APIs [36] | Human / Process |
| Replacement of traditional web browser search (e.g., Stack Overflow) with direct AI prompts [32, 37, 38] | Process |
| High snippet acceptance frequency for short, in-context completion suggestions [34, 39] | Technical / Human |

### Fatores Negativos
| Fator | Categoria |
|-------|-----------|
| Context switching between code editor and chat panel in conversational systems [40, 41] | Process / Technical |
| Information overload and overly verbose chatbot responses distracting focus from code [40, 41] | Human / Technical |
| Overreliance / blind trust in AI suggestions leading to unreviewed code or debugging rabbit holes [25, 35, 42, 43] | Human |
| Reduced developer effort dedicated to reading and understanding generated code [36, 40] | Human |
| Incorrect or misaligned auto-complete suggestions requiring manual corrections [40] | Technical |
| Time and effort required to craft effective natural language prompts [40, 41, 44] | Human / Process |

---

## Papel da IA e Automacao

| Campo | Valor |
|-------|-------|
| **Usa IA/ML?** | Yes — Evaluates GitHub Copilot (Codex-based inline auto-complete) and GPT-3 (conversational chatbot panel within Visual Studio Code) for Python code generation, debugging, and explanation [1, 45]. |
| **Automacao de coleta?** | Yes — Interaction telemetry, keypress tracking, screen recordings, background timer logging, and automated unit test execution for feature validation [9, 10, 19, 26]. |
| **Impacto de IA na produtividade?** | Significant positive impact: Participants implemented ~65% more requirements per minute using either AI assistant compared to the web-only baseline (p = 0.037) [46, 47]. Character output per minute increased significantly (p <= 0.002), while the percentage of human-authored code decreased significantly (p < 0.001) [48]. User satisfaction (AttrakDiff Hedonic Quality p < 0.001, Attractiveness p <= 0.003) improved significantly [12]. Objective code quality (Maintainability Index, correctness) remained comparable to human-authored code [16, 17]. |

---

## Resultados Principais

- **Speed and Efficiency Gains**: Both AI tools enabled developers to implement significantly more requirements per minute (~65% increase) compared to the baseline browser environment (p = 0.037) [46, 47]. Power users with AI experience completed tasks up to 3–4 times faster than peers [42, 49].
- **Task Completion Time**: AI support significantly reduced overall task completion time compared to the baseline (auto-complete: p = 0.028, conversational: p = 0.025) [22].
- **Human Authoring vs. AI Generation**: Character output per minute increased significantly with AI support (p < 0.001 for auto-complete, p = 0.002 for conversational) [48]. Simultaneously, the proportion of code manually typed by the developer decreased significantly (p < 0.001) as AI contributed the majority of code volume [48, 50].
- **Divergent Usage Patterns between Interaction Modalities**:
  - **Auto-complete (Copilot)**: High frequency of accepted code snippets (mean: 12.6, median: 11.5) with small average snippet size (mean: 42.9 chars, median: 41.8 chars) [34].
  - **Conversational (GPT-3)**: Low frequency of accepted code snippets (mean: 5.0, median: 4.5) but significantly larger average snippet size (mean: 205.4 chars, median: 110.9 chars; p < 0.001) [34].
- **Browser Replacement**: Browser usage dropped sharply when AI tools were available (only 4 participants used the browser with auto-complete, and 2 with conversational chat) [37].
- **Code Quality & Maintainability**:
  - **Maintainability Index**: No significant difference across conditions (medians 73 ± 1, range 61–86, p = 0.967) [17].
  - **Functional Correctness**: Unit test pass rates were comparable across conditions (14 baseline, 12 auto-complete, 13 conversational fulfilled 100% of testing criteria, p = 0.728) [16, 17].
  - **Comments**: Auto-complete submitted code contained significantly higher comment percentages (p = 0.014), primarily driven by prompt comments written to trigger completions [22, 51].
- **User Satisfaction**: Both AI tools scored significantly higher on AttrakDiff for Hedonic Quality (p < 0.001) and Attractiveness (p <= 0.003) relative to the baseline [12]. Auto-complete also yielded significantly higher Pragmatic Quality (p = 0.027) [12].

---

## Desafios do Uso das Metricas

- **Overreliance and Blind Trust Anti-Pattern**: Developers frequently accept AI code with minimal review, risking undetected bugs or extended "debugging rabbit holes" (e.g., participant P19 completing tasks in <4 mins without verification) [25, 35, 42, 43].
- **Subjective vs. Objective Metric Discrepancy**: Developers subjectively rate AI performance and code quality higher than baseline, even though objective static code quality metrics (Maintainability Index, test pass rates) show no statistically significant difference [16, 17, 43, 52].
- **Context-Switching Overhead**: Conversational side-panels force developers to shift focus away from the editor, creating interaction friction compared to inline completions [40, 41].
- **Information Overload**: Detailed conversational chatbot responses can present excess text, slowing down developers who must scan through long replies for specific code snippets [40, 41].
- **Prompt Engineering Overhead**: Writing precise inline comments or chat prompts requires time and mental effort that can offset auto-completion speed advantages if suggestions fail [40, 41, 44].
- **Superficial Comment Density**: Higher comment percentages in AI auto-completed code reflect prompting mechanisms rather than explanatory documentation or architectural rationale [51].

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

- **Sample Age and Experience Bias**: Participants leaned towards younger developers (mean age 26.8), who may integrate AI assistants more readily than senior developers with long-established habits [4, 53].
- **Task Scope and Duration Constraints**: Tasks were restricted to short Python exercises (15 minutes limit) to fit the controlled study setup, deferring large-scale software engineering tasks [7, 54].
- **Pre-Structured Problem Decomposition**: Tasks provided structured sub-tasks and starter code, reducing the need for high-level problem decomposition and computational thinking [54, 55].
- **Temporal Model Snapshot**: Experiments represent a specific snapshot of model capabilities (early 2024 versions of GPT-3 and Copilot); rapidly evolving LLM architectures and non-deterministic model outputs could alter interaction patterns [56].
- **Short-Term Controlled Environment**: Observed short-term individual coding rather than long-term team collaboration, multi-developer code maintenance, or repository-scale projects [54, 57].

---

## Contribuicao Principal

The primary contribution of this paper is a rigorous empirical evaluation comparing inline auto-complete and conversational chat AI interfaces across all five dimensions of the SPACE productivity framework [1, 3, 8]. Through a controlled within-subjects user study (N=24), the authors demonstrate that while both AI interaction modalities deliver equivalent ~65% productivity boosts over traditional browser search without degrading objective code maintainability, they induce fundamentally distinct developer usage strategies — auto-complete favoring high-frequency micro-snippets and conversational chat serving as a direct replacement for browser-based documentation search through larger, explanatory code blocks [3, 34, 39, 46, 58].

---

*Extraido via NotebookLM em October 2026 para MLR: Software Developer Metrics in Practice*
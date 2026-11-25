# P2109 — Visualizing interaction data inside & outside the ide to characterize developer productivity

**Decisao: INCLUIDO | Qualidade: 4/5**

---

## Dados Bibliograficos

| Campo | Valor |
|-------|-------|
| **ID** | P2109 |
| **Autores** | Gabriele Di Rosa, Andrea Mocci, Marco D’Ambros [1] |
| **Ano** | 2020 [2] |
| **Venue** | IEEE Working Conference on Software Visualization (VISSOFT 2020) [2] |
| **DOI** | 10.1109/VISSOFT51673.2020.00009 [2] |
| **Tipo** | Conference paper [2] |
| **Metodo** | Mixed methods / Design science (tool development and preliminary case study evaluation) [3-5] |
| **Amostra** | 6 participants (4 master students and 2 professional developers), 20 total sessions collected, 12 analyzed, and 3 detailed sessions presented [5-7] |
| **Contexto** | Mixed (Academic — USI master students in Software and Data Engineering; Industry/R&D — USI CodeLounge professional developers) [5, 7] |
| **Modo de trabalho** | Not specified [5] |
| **Metodologia** | Not specified [5] |

---

## Objetivo

The paper proposes **Ferax**, a data analytics platform designed to measure and analyze work fragmentation and software developer productivity by capturing interaction data both inside the IDE (Visual Studio Code via the **Tako** profiler) and outside the IDE (application usage on macOS and website visits via a Google Chrome extension) [3, 8, 9]. Its main goal is to provide interactive visualizations—such as global digests, single session digests, timelines, and chord diagrams—that allow developers to reflect on their daily habits, quantify the impact of interruptions, and properly classify sessions that might otherwise appear unproductive [2, 3, 10, 11].

---

## Questoes de Pesquisa

The paper does not explicitly define formal research questions (e.g., RQ1, RQ2) [1, 11].

---

## Metricas e Instrumentos de Avaliacao

| Metrica | Categoria | Nivel | Como Coletada | Validada |
|---------|-----------|-------|---------------|----------|
| **Application Focus / Chunk Duration** | Activity | Individual | Observed via macOS `NSRunningApplication` API watching application focus switches [8, 12, 13] | Partial [5, 14] |
| **Website Visits (Productive vs. Distracting)** | Activity / DevEx | Individual | Google Chrome extension tracking URLs and tab focus via Chrome Tabs and Windows APIs [9, 15, 16] | Partial [5] |
| **Edit Ratio** | Productivity / Activity | Individual | Calculated as the ratio of edit events over total IDE events in Visual Studio Code via Tako / LSP messages [17-19] | Yes [14] |
| **Switch Count / Switch Frequency** | Activity / DevEx | Individual | Tracked on application focus changes or browser tab updates [20-22] | Partial [5] |
| **IDE Save Events Count** | Activity | Individual | Recorded by Tako via Language Server Protocol (LSP) text synchronization save messages [21, 23] | No [21] |
| **Edited Documents Count** | Activity | Individual | Extracted by Tako from document edit file paths [21, 24, 25] | No [21] |
| **Visited Websites Count** | Activity | Individual | Counted by the Chrome extension per development session [16, 21, 25] | No [21] |
| **Degree-of-Interest (DOI) / Working Set** | Activity / Productivity | Individual | Recorded in prior literature (MYLYN / DFLOW) [26, 27] | Yes [26, 27] |

---

## Frameworks e Metricas

### Frameworks Referenciados
- **Degree-of-Interest (DOI) / MYLYN Model**: **REFERENCED** (cited for computing developer interest in program entities) [26].
- **DFLOW / TAKO Interaction Model**: **REFERENCED / APPLIED** (the DFLOW interaction model for Pharo was ported to TAKO for Visual Studio Code to capture fine-grained IDE events) [28, 29].
- **Work Fragmentation Model (Sanchez et al.)**: **REFERENCED / APPLIED** (used to classify IDE actions into edits vs. non-edits, aggregate massive edit events under 1 second, and evaluate interruption impact) [14, 17, 18, 30].
- **Language Server Protocol (LSP)**: **REFERENCED / APPLIED** (leveraged as the standardized protocol by TAKO to collect language-specific IDE interactions) [31, 32].

### Frameworks Propostos
- **Ferax Platform & Interaction Taxonomy**: Ferax proposes a holistic interaction tracking model that extends IDE event profilers with external application focus monitoring and browser tab categorization [3, 33]. It establishes a explicit taxonomy categorizing applications (Productive, Non-productive, Uncertain / Purpose: Programming, Collaboration, Social Network, Utility, Browser, Other) and websites (Productive, Distracting), defines core analytical constructs like **chunks** and **switches** (Productive switch, Uncertain switch, Possible interruption switch), and introduces four visual analytics views for retrospective analysis [11, 20, 34-36].

---

## Fatores que Influenciam Produtividade

### Fatores Positivos
| Fator | Categoria |
|-------|-----------|
| Extended activity tracking outside the IDE (enables accurate recognition of documentation reading and collaboration tasks) [1, 33, 37] | Technical / Process |
| Visual reflection tools (Digests, Timeline, Chord diagram) for developer self-retrospection [2, 3, 10, 11] | Process / Human |
| High focus periods (single application chunks lasting longer than 15 minutes) [38, 39] | Human / Process |
| Dedicated collaboration platforms (e.g., Slack, Teams, Gitlab) for task-related communication [35, 40-42] | Technical / Organizational |

### Fatores Negativos
| Fator | Categoria |
|-------|-----------|
| Work fragmentation (frequent switches between applications, averaging ~1 switch per minute) [1, 21, 30] | Process / Human |
| Distractive websites (e.g., social networks like Facebook, Twitter) [36, 40, 43] | Technical / Human |
| Non-productive applications (personal messaging apps like WhatsApp, Telegram during work) [34, 36, 40] | Technical / Human |
| Long interruptions (≥ 15 minutes), causing severe loss of edit ratio for up to 45 minutes after resuming work [30, 44, 45] | Process / Human |

---

## Papel da IA e Automacao

| Campo | Valor |
|-------|-------|
| Usa IA/ML? | No — Ferax relies on deterministic event observation via OS and browser APIs [12, 16] and rule-based custom domain lists [15, 46]. |
| Automacao de coleta? | Yes — Fully automated passive event tracking via Tako (VS Code LSP), Application Focus Recorder (macOS API), and Website Visits Recorder (Chrome extension) communicating over WebSockets [8, 9, 12]. |
| Impacto de IA na produtividade? | Not applicable — AI/ML impact on developer productivity is not evaluated or discussed in the paper [1, 11]. |

---

## Resultados Principais

- **Outside-IDE Activity Classification**: Tracking activities outside the IDE prevents misclassifying non-IDE development tasks [3, 37]. A documentation session with a near-zero IDE edit ratio was shown to be highly productive when tracking revealed extensive active work on Gitlab [37, 42, 47].
- **Interruption Recovery Cost**: Long interruptions (≥ 15 minutes) severely impair productivity; in an evaluated case study, the developer's edit ratio remained minimal for 45 minutes after resuming work following a long WhatsApp interruption [30, 44, 45].
- **High Switch Frequency**: Baseline metrics showed developers tend to change application focus frequently (almost 1 switch per minute in global digests), though short chunks (< 1s) typically correspond to accidental Alt-Tab switches rather than true interruptions [21, 48].
- **Inside-IDE Time Distribution**: Within the IDE, non-edit activities (program understanding and navigation) constitute a major portion of development time [17, 27, 49].
- **Feasibility**: The tool successfully collected 20 development sessions across 6 participants (4 master students, 2 professional developers), demonstrating the feasibility of non-intrusive WebSocket-based telemetry integration across the IDE, OS, and browser [5, 6, 12].

---

## Desafios do Uso das Metricas

- **Misclassification of Non-IDE Time**: Assuming all time spent outside the IDE is an unproductive workflow interruption leads to false conclusions regarding developer performance [1, 33, 50].
- **Static & Context-Blind Categorization**: Categorizing websites/apps as productive or non-productive using fixed domain lists fails to account for dynamic context (e.g., messaging apps used for professional ad-hoc collaboration vs. personal chat) [51, 52].
- **Inability to Detect Idle Time**: Focus tracking alone cannot distinguish between active developer contemplation/thought and actual idle time when away from the keyboard [49, 53].
- **Unmonitored Devices**: Telemetry limited to personal computers misses distractions and interruptions occurring on secondary devices like smartphones [53, 54].
- **Platform Restrictions**: Telemetry solutions restricted to specific operating systems (macOS) or browsers (Chrome) limit metric coverage across diverse multi-platform environments [53, 54].

---

## Avaliacao de Qualidade Metodologica

| Criterio | Pontuacao (0-2) |
|----------|----------------|
| Objetivo claramente definido | 2 [1, 3] |
| Metodologia adequada ao objetivo | 2 [5, 8, 9] |
| Amostra/contexto descrito adequadamente | 1 [5, 7] |
| Ameacas a validade discutidas | 1 [51-53] |
| Resultados com evidencia suficiente | 1 [5, 6, 55] |
| Contribuicao clara para pratica ou teoria | 2 [3, 33, 37] |
| **TOTAL** | **9/12** |

---

## Limitacoes

- **Static Domain & App Classification**: Relies on customizable lists for productive domains/apps that cannot dynamically adapt to context or unlisted new framework documentation sites [51, 52].
- **Lack of Idle Detection**: Tracks active application focus but cannot determine if a developer is idle or thinking [53].
- **Single-OS & Single-Browser Platform Scope**: Telemetry outside the IDE is restricted to macOS and Google Chrome [53, 54].
- **No Secondary Device Telemetry**: Does not capture interactions or distractions happening on mobile phones or external devices [53, 54].
- **Preliminary Evaluation Sample Size**: The evaluation relies on anecdotal evidence from a small sample of 6 participants (20 sessions collected, 12 analyzed, 3 presented in detail) [5, 6, 37, 55].

---

## Contribuicao Principal

The primary contribution of this paper is **Ferax**, an open data analytics platform and architecture that addresses the limitations of IDE-only interaction tracking [3, 8, 9]. By combining Visual Studio Code IDE telemetry (via Tako and the Language Server Protocol) with macOS application focus monitoring and Google Chrome browser tab tracking, Ferax provides a holistic visual environment (digests, timelines, and chord diagrams) that allows software developers to accurately reflect on work fragmentation, recognize valid non-IDE development tasks (such as reading documentation), and identify real productivity bottlenecks [2, 3, 10, 11, 37].

---

*Extraido via NotebookLM em October 2026 para MLR: Software Developer Metrics in Practice*

---

💡 Would you like me to create a visual comparison table or a detailed report comparing this paper with other developer productivity papers in your notebook?
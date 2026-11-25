# P2019 — Developers’ Experience with Generative AI Beyond Productivity Assessment – Insights from an Empirical Mixed-Methods Field Study [1]

**Decisao: INCLUIDO | Qualidade: 5/5** [2-4]

---

## Dados Bibliograficos

| Campo | Valor |
|-------|-------|
| **ID** | P2019 [1] |
| **Autores** | Charlotte Brandebusemeyer, Kerim Zunic, Thomas Zimmermann, Tobias Schimmer, Bert Arnrich [1] |
| **Ano** | 2026 [5] |
| **Venue** | ACM Transactions on Software Engineering and Methodology (TOSEM) [1] |
| **DOI** | https://doi.org/10.1145/3847122 [5] |
| **Tipo** | Journal article [1] |
| **Metodo** | Mixed methods (Empirical field study combining controlled data collection sessions with uncontrolled natural work periods) [2, 6] |
| **Amostra** | 22 professional software developers at SAP (California, USA; fluent in Java) [6, 7] |
| **Contexto** | Industry (SAP Labs, California, USA) [6, 7] |
| **Modo de trabalho** | Not specified [7] |
| **Metodologia** | Not specified [7] |

---

## Objetivo

The main objective of the paper is to investigate how professional software developers engage with Generative AI (GenAI) tools—specifically GitHub Copilot—in their natural work environment beyond traditional output quality and productivity gains [2, 8]. By conducting a 4-day developer-centered empirical mixed-methods field study combining controlled experimental sessions with uncontrolled everyday work periods, the study evaluates the impact of different GenAI interaction modes (in-code suggestions vs. chat prompts) on task efficiency, accuracy, perceived workload, cognitive load, developer experience (DevEx), and team dynamics [2, 6, 9].

---

## Questoes de Pesquisa

- **RQ1:** How do software developers at SAP experience their interaction with AI/GenAI during their workday prior to the study? [10]
- **RQ2:** Which GenAI interaction type is most frequently used and preferred by the participants during the controlled sessions of this study? [10]
- **RQ3:** How does the interaction with GenAI during the controlled sessions of this study impact developers’ efficiency, accuracy and perceived workload? [10]
- **RQ4:** How is the interaction with AI evaluated during everyday working tasks concerning cognitive load and productivity? [10, 11]
- **RQ5:** What concerns and opportunities do developers foresee in the future with GenAI? [11]
- **RQ6:** What was the impact of this study on developers' subsequent use of GenAI? [11]

---

## Metricas e Instrumentos de Avaliacao

| Metrica | Categoria | Nivel | Como Coletada | Validada |
|---------|-----------|-------|---------------|----------|
| NASA-TLX (Perceived Workload) | DevEx / Workload | Individual | 21-point Likert-scaled questionnaire filled after each task [12] | Yes [12] |
| Task Duration (Efficiency) | Productivity / Delivery | Individual | Screen recording timestamp annotations (measured in seconds) [13, 14] | Yes [13] |
| Task Completion Rate (Accuracy) | Quality / Delivery | Individual | Screen recording task outcome verification (success/fail) [13, 15] | Yes [13] |
| Subjective Cognitive Load Rating | DevEx / Cognitive Load | Individual | Self-reported Likert scale (1-7) in workday documentation [16, 17] | Yes [16] |
| Subjective Productivity Rating | Productivity | Individual | Self-reported Likert scale (1-6) in workday documentation [16, 17] | Yes [16] |
| Copilot Evaluation Score | DevEx / Satisfaction | Individual | 5-point Likert questionnaire adapted from the SPACE framework [12, 18] | Yes [12] |
| Interaction Frequency (In-Code vs Chat) | Activity | Individual | Screen recording manual interaction counting [13, 19] | Yes [13] |
| IPIP Big Five Personality Traits | Human | Individual | 50-item International Personality Item Pool pre-questionnaire [20, 21] | Yes [20] |
| Physiological Signals (EDA, BVP, HR) | DevEx / Cognitive Load | Individual | Wearable wristband data collection during controlled sessions [22, 23] | Yes [22] |

---

## Frameworks e Metricas

### Frameworks Referenciados
- **DevEx (Developer Experience) Framework** (Noda et al. / Greiler et al.): **REFERENCED** (analyzed via cognitive load and feedback loop dimensions) [9, 24, 25].
- **SPACE Framework** (Forsgren et al.): **REFERENCED** and **APPLIED** (adapted to construct the Copilot evaluation questionnaire) [12, 24].
- **DORA Metrics**: **REFERENCED** (discussed in developer productivity background) [9, 26].
- **Core 4 Velocity Framework** (Tacho): **REFERENCED** [27].
- **Flow Theory** (Csikszentmihalyi): **REFERENCED** (used to interpret cognitive load and productivity coupling) [24, 28].
- **HumanEval-X Benchmark**: **APPLIED** (used to select standardized baseline and controlled coding tasks) [29, 30].

### Frameworks Propostos
- **Rule-of-Thumb Decision Framework for Interaction Mode Selection:** Proposes a practical decision guide based on task characteristics (coding vs. non-coding, codebase context scope required, need for output explanations) to select upfront between in-code suggestions and chat prompts, avoiding context-switching overhead [2, 31, 32].
- **Multimodal Mixed-Methods Field Study Framework:** Proposes a feasible empirical study design combining controlled experimental sessions (subjective, behavioral, and physiological data) with uncontrolled natural work periods in enterprise settings [2, 6, 11].

---

## Fatores que Influenciam Produtividade

### Fatores Positivos
| Fator | Categoria |
|-------|-----------|
| Using a single interaction type (only in-code suggestions or only chat prompts) per task [14, 33] | Process |
| Automating monotonous, repetitive, and structured tasks (unit testing, boilerplate coding, documentation) [2, 34, 35] | Technical |
| Chat-based prompting for higher-level reasoning, debugging, and codebase explanations [15, 36, 37] | Technical |
| Moderate interaction intensity with AI tools [14] | Process |
| High perceived GenAI output quality and relevance [34, 38] | Technical |
| Lowering activation barriers for seeking initial feedback or starting unfamiliar tasks [39, 40] | Human / Process |

### Fatores Negativos
| Fator | Categoria |
|-------|-----------|
| Combining multiple interaction types (in-code suggestions + chat) within a single task (creates cognitive overhead) [14, 41, 42] | Process |
| Excessive interaction frequency or frequent interaction mode switching [14, 43] | Process |
| Output inaccuracies, hallucinations, and outdated internal models lacking domain context [35, 39, 44] | Technical |
| Prompt sensitivity requiring repeated prompt adjustments [44-46] | Technical |
| High verification overhead required to validate verbose or complex AI code outputs [43-45] | Process / Technical |
| Slow model response times during simple tasks [45, 47] | Technical |

---

## Papel da IA e Automacao

| Campo | Valor |
|-------|-------|
| **Usa IA/ML?** | Yes — GitHub Copilot (GPT-4o default) during controlled sessions; free choice of GenAI tools (e.g., ChatGPT, Gemini) during uncontrolled work periods [6, 7, 13, 48] |
| **Automacao de coleta?** | Yes — Automated screen recording (OBS), global keyboard/mouse tracking (JNativeHook), and wristband physiological sensors combined with self-reported questionnaires [13, 22] |
| **Impacto de IA na produtividade?** | Overall agreement that GenAI increases productivity (M=4.32), especially for monotonous tasks [34]. In controlled settings, using a single interaction mode significantly reduced task duration, whereas combined interaction modes offset gains [14]. In natural work, AI use in development-heavy tasks increased perceived cognitive load without significantly altering perceived productivity unless the AI output was rated as helpful (which substantially boosted perceived productivity, d=0.83) [38, 49]. |

---

## Resultados Principais

- **High Developer Satisfaction:** 72.7% of participants reported being satisfied or very satisfied with GenAI tools (0% dissatisfied), primarily driven by efficiency gains in monotonous and repetitive tasks [34, 50].
- **Dominance of In-Code Suggestions:** In-code suggestions were the primary interaction mode, used >50% of the time by 70% (14/20) of developers during controlled tasks [19]. In-code suggestions were preferred for quick, low-complexity code edits, while chat prompts were favored for complex debugging, explanations, and non-coding tasks [36, 37, 51].
- **Interaction Mode Trade-Offs:** Using either in-code suggestions or chat prompts individually significantly reduced task completion time and perceived workload (NASA-TLX) [14, 41]. However, combining both interaction types within a single task eliminated efficiency benefits and increased cognitive load to levels comparable to working without AI [14, 41, 42].
- **Task Completion & Accuracy:** Chat-based interaction was the only mode that significantly increased the likelihood of successful task completion across tasks [15, 33].
- **Everyday Work & Cognitive Load:** During 445 documented everyday tasks, AI was used in 27.4% of total tasks (and 54.6% of development-heavy tasks) [52]. Using AI in development-heavy tasks significantly increased perceived cognitive load (p=0.008), while perceived productivity only increased significantly when AI output was experienced as helpful (p=0.043, d=0.83) [38, 49].
- **Team Dynamics:** Developers turn more quickly to GenAI for feedback than to colleagues to avoid disturbing peers (Md=4), though peer feedback is still considered more helpful for complex domain problems [40, 53].
- **Increased Behavioral Intentionality:** 73% of participants reported they will adjust their GenAI interaction strategies after participating in the study, demonstrating that structured reflection fosters more intentional AI usage [54, 55].

---

## Desafios do Uso das Metricas

- **Lack of standardized GenAI productivity metrics:** Studies rely on disparate measures such as suggestion acceptance rates, completion times, or self-reports, none of which capture full interaction complexity [56].
- **Invisibility of verification overhead:** Traditional velocity or code acceptance metrics fail to account for time and cognitive load spent reviewing, prompt-tuning, and validating AI outputs [23, 44, 45].
- **Suboptimal interaction anti-patterns:** Unplanned switching between interaction modes (in-code vs. chat) introduces cognitive friction and negates expected time savings [41, 42].
- **Misalignment between efficiency gains and job fulfillment:** Metrics measuring raw output speed do not reflect developer well-being or intrinsic work fulfillment, which scored lower (M=2.91) due to shifting developer roles toward review and validation [34, 57].

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

*Justificativa da Pontuacao:*
- **Objetivo (2/2):** Main objective and 6 research questions are explicitly defined [2, 10, 11].
- **Metodologia (2/2):** Rigorous mixed-methods field study combining controlled experimental tasks with natural work documentation and multimodal data sources [2, 6, 22].
- **Amostra/Contexto (2/2):** Detailed description of the sample (22 SAP developers in California, Java proficiency, experience levels) and organizational context [6, 7].
- **Ameacas a Validade (2/2):** Comprehensive Section 7 explicitly addressing construct, internal, and external validity threats [3, 4, 58-61].
- **Resultados (2/2):** Robust statistical models (linear mixed-effects, Cohen's d, Kendall's tau, post-hoc tests) and qualitative content analysis backed by 66 hours of annotated screen recordings and 445 logged tasks [13, 52, 62, 63].
- **Contribuicao (2/2):** Clear theoretical contributions to developer experience literature and practical contributions including the interaction rule-of-thumb [2, 11, 31, 32].

---

## Limitacoes

- **Single-company setting:** All participants were employees at SAP in California, USA, which may limit generalizability to other corporate cultures or team structures [6, 7, 59].
- **Language restriction:** Controlled coding tasks were performed exclusively in Java; interaction patterns and AI accuracy may vary across other programming languages [6, 60].
- **Tool specificity in controlled sessions:** GitHub Copilot was the sole AI tool used during controlled sessions, although other tools were allowed in uncontrolled periods [6, 7, 59].
- **Small sample size:** Sample of 22 developers limits statistical power for exploratory subgroup analyses (e.g., personality trait correlations) [7, 21, 64].
- **Confounding variables in field settings:** Uncontrolled work periods naturally introduced unobserved workplace environmental variables [58].
- **Unevaluated sensor streams:** Physiological wristband data and fine-grained keystroke/mouse telemetry were reserved for future work and not fully integrated into this paper's core models [22, 61, 65].

---

## Contribuicao Principal

The paper's primary contribution is an empirical, developer-centered evaluation of Generative AI interaction in a professional enterprise setting, combining controlled experimental sessions with natural field observations [2, 6]. It reveals that productivity gains and workload reductions depend heavily on the specific GenAI interaction mode chosen (in-code suggestions vs. chat prompts), demonstrating that switching modes within a task creates cognitive overhead that negates time savings [14, 41, 42]. To address this, the authors introduce a practical rule-of-thumb decision framework to guide interaction choices upfront based on task characteristics, while offering actionable insights into how GenAI impacts developer experience, cognitive load, and team dynamics beyond simple code generation speed [2, 11, 31, 32].

---

*Extraido via NotebookLM em October 2026 para MLR: Software Developer Metrics in Practice*

💡 **Próximo passo:** Se desejar, posso transformar esta análise estruturada em um relatório formatado em PDF ou em uma apresentação de slides para compartilhar com a sua equipe.
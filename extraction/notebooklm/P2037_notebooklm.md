# P2037 — "Game Changer" or "Overenthusiastic Drunk Acquaintance"? Generative AI Use by Blind and Low Vision Software Professionals in the Workplace

**Decisao: INCLUIDO | Qualidade: 5/5** [1-4]

---

## Dados Bibliograficos

| Campo | Valor |
|-------|-------|
| **ID** | P2037 [1] |
| **Autores** | Yoonha Cha, Victoria Jackson, Lauren Shu, Stacy M. Branham, André van der Hoek [5] |
| **Ano** | 2026 [1] |
| **Venue** | 2026 IEEE/ACM 48th International Conference on Software Engineering (ICSE ’26) [1] |
| **DOI** | 10.1145/3744916.3773172 [1] |
| **Tipo** | Conference paper [1] |
| **Metodo** | Qualitative (Semi-structured interviews, reflexive thematic analysis) [3, 6-8] |
| **Amostra** | 39 blind and low vision software professionals (BLVSPs) (51% totally/completely blind, 15% light/color perception, 33% residual vision; 67% North America, 15% Europe, 10% Asia, 8% South America; 34 men, 4 women, 1 non-binary; work tenure: 1 to 31+ years) [7, 9] |
| **Contexto** | Industry and Freelance (Startups to Multinational Corporations; positions: Software Engineers n=21, Accessibility Specialists n=5, UX Specialists, Technical Executives) [7, 9] |
| **Modo de trabalho** | Not specified (Includes corporate settings, freelancing, remote and hybrid collaboration) [7, 9, 10] |
| **Metodologia** | Not specified (Includes general SDLC activities: coding, code review, design review, front-end development, pair programming, debugging) [7, 9, 11] |

---

## Objetivo

To investigate how blind and low vision software professionals (BLVSPs) perceive and utilize Generative AI (GenAI) in the workplace, examine its impact on their daily tasks, workplace accessibility, and career prospects, and analyze the trade-offs (higher risks vs. higher returns) they weigh when deciding whether and when to adopt GenAI tools [6, 7, 12, 13].

---

## Questoes de Pesquisa

- **RQ1**: How do BLVSPs perceive and utilize generative AI in the workplace? [7]
- **RQ2**: How do generative AI tools impact BLVSPs’ work and career prospects? [7]

---

## Metricas e Instrumentos de Avaliacao

| Metrica | Categoria | Nivel | Como Coletada | Validada |
|---------|-----------|-------|---------------|----------|
| GenAI Usage Frequency | Activity | Individual | Self-reported via semi-structured interviews (62.5% daily, 37.5% occasional) [14] | No [8] |
| Perceived Productivity Improvement | Productivity | Individual | Qualitative participant self-reports during interviews [15] | No [8] |
| Visual Description Confidence | DevEx / Quality | Individual | Self-reported percentage confidence (e.g., 80–90% for simple tables/charts) [16] | No [8] |
| Access Labor / Time on Sighted Help & DIY | Activity / DevEx | Individual | Qualitative participant reports of time and effort spent [17-19] | No [8] |
| Mental Toll / Stress Reduction | Satisfaction / DevEx | Individual | Qualitative participant self-reports [15] | No [8] |

---

## Frameworks e Metricas

### Frameworks Referenciados
- No software productivity frameworks (such as DORA, SPACE, DevEx, GQM, HEART, OKR) are explicitly referenced or applied in this paper [7, 8, 20].

### Frameworks Propostos
- None proposed [13]. The paper introduces a conceptual decision model detailing the "Higher-Risk, Higher-Return Calculus" and the "Verification Catch-22" experienced by BLVSPs [13, 21, 22].

---

## Fatores que Influenciam Produtividade

### Fatores Positivos
| Fator | Categoria |
|-------|-----------|
| Automated generation of boilerplate code and code completions across familiar and unfamiliar programming languages [23, 24] | Technical |
| Non-visual interpretation of visual materials (screenshots, UI designs, UML diagrams, tables, flowcharts) via LLMs/GenAI [16, 25-27] | Technical |
| Accelerated debugging and error line identification without manual line-by-line screen reader traversal [11, 28] | Technical |
| Creation and usage of custom/DIY tools based on GenAI APIs tailored for non-visual accessibility [14, 24, 29] | Technical |
| Reduced reliance on asking sighted colleagues for help, preserving professional image and personal autonomy [17, 30, 31] | Human / Organizational |
| Reduction of unpaid "access labor" (decreased need to spend personal time building complex DIY accessibility tools) [18, 19] | Process |
| Reduced mental toll, stress, and fatigue associated with inaccessible software development tools [15] | Human |
| Enhanced ability to communicate using visual terminology with sighted colleagues, improving collaboration [31, 32] | Human |
| Protection against unwanted disability disclosure in client interactions and professional settings [33] | Human / Organizational |

### Fatores Negativos
| Fator | Categoria |
|-------|-----------|
| Suboptimal UX and accessibility of GenAI tool interfaces (unlabeled buttons, missing HTML headings, poor screen reader navigation) [34, 35] | Technical |
| Auditory overload and speech interruptions caused by AI coding assistants (e.g., GitHub Copilot) when used with screen readers [36, 37] | Technical |
| High vulnerability to GenAI hallucinations and the "verification catch-22" (detecting hallucinations with screen readers is taxing or impossible) [21, 38-40] | Technical / Process |
| Inconsistent tool updates that break existing accessibility features, forcing continuous re-learning [41] | Technical / Process |
| Inaccessible IDE extensions (e.g., Cursor code editor lacking accessibility support) [29] | Technical |
| Organizational bans or restrictive policies on GenAI use, forcing clandestine usage on personal devices or workarounds [42, 43] | Organizational / Process |
| Lack of technical support or accessible issue reporting channels from GenAI tool vendors [41] | Technical / Organizational |

---

## Papel da IA e Automacao

| Campo | Valor |
|-------|-------|
| Usa IA/ML? | Yes — Investigates usage of ChatGPT (GPT-4, GPT-4o), Claude (3.5 Sonnet/Haiku), GitHub Copilot, Gemini, DeepSeek, Midjourney, Be My AI, Picture Smart, and custom API-based GenAI tools [14]. |
| Automacao de coleta? | No — Qualitative study using audio-recorded Zoom interviews, transcripts, and thematic analysis [3, 44]. |
| Impacto de IA na produtividade? | Positive overall impact on productivity by automating boilerplate code, interpreting inaccessible visual materials, and streamlining debugging; however, productivity gains are partially eroded by time required to verify hallucinations and navigate inaccessible tool UIs [6, 13, 15, 19, 39]. |

---

## Resultados Principais

- **Sample Demographics**: Qualitative study involving 39 BLVSPs across 4 continents (67% North America, 15% Europe, 10% Asia, 8% South America) with vision levels comprising 51% totally blind, 15% light/color perception, and 33% residual vision; work experience ranged from 1 to 31+ years across startups and multinational corporations [9].
- **Frequency of Adoption**: 62.5% (n = 25) of participants utilized GenAI tools daily in their software development work, while 37.5% (n = 15) used them occasionally [14].
- **Tools Utilized**: Commonly used tools included ChatGPT (GPT-4, GPT-4o), Google Gemini, GitHub Copilot, Claude (3.5 Sonnet, 3.5 Haiku), DeepSeek, Midjourney, as well as accessibility-focused tools (Be My AI, Picture Smart); 5 participants developed custom DIY tools using GenAI APIs [14].
- **Reduction of Access Labor**: GenAI enabled BLVSPs to perform visual and complex tasks independently (e.g., interpreting terminal output tables, analyzing code screenshots, participating in Figma UI design reviews), reducing reliance on sighted colleagues and personal time spent crafting DIY tools [19, 26-28].
- **Verification Catch-22**: Detecting AI hallucinations is uniquely taxing for screen reader users due to linear audio feeds. BLVSPs use GenAI to avoid asking sighted colleagues for help, yet verifying visual or complex AI outputs often forces them to consult sighted colleagues or risk submitting incorrect work [21, 39, 40].
- **UX & Accessibility Deficits**: GitHub Copilot extensions caused aural overload via frequent beeps and speech interruptions [36, 37]. Web interfaces (e.g., ChatGPT) suffered from missing button labels, lack of HTML heading navigation, and accessibility regressions following software updates [34, 35, 41].
- **Organizational Policy Compliance**: Company policies ranged from active encouragement to strict bans; 5 out of 8 participants subject to total bans disclosed clandestine, "under-the-radar" GenAI use on personal devices to maintain productivity and stay competitive with sighted peers [42, 43].
- **Career Advancement Impact**: GenAI lowered barriers to learning programming languages, made non-accessibility tech roles (e.g., software engineering, UI/UX design) more accessible, and allowed BLVSPs to produce deliverables faster, improving their visibility for promotions [45-47].

---

## Desafios do Uso das Metricas

- **Qualitative Nature**: The study relies exclusively on self-reported qualitative interview data and does not measure formal quantitative software developer metrics or productivity telemetry [8].
- **Lack of Objective Validation**: Self-reported productivity gains were not cross-validated with objective IDE telemetry, repository commit metrics, or controlled task-completion timing [8, 48].
- **Verification Overhead**: Measuring net productivity gains is challenging because hidden "verification labor" (checking AI outputs for hallucinations using screen readers) can offset initial time savings [21, 39].
- **Omission of Coding Reliability Metrics**: Authors deliberately omitted statistical Inter-Rater Reliability (IRR), adhering to reflexive thematic analysis methodology [8].

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

- **Geographic Bias**: 67% of participants resided in North America (USA), limiting transferability to other global software development cultures and legal framework contexts [49].
- **Gender Imbalance**: The sample was skewed toward men (34 men, 4 women, 1 non-binary), though reflective of broader industry demographic imbalances [9, 49].
- **Lack of Data Triangulation**: Findings relied solely on semi-structured interview self-reports without triangulation against direct observational studies or quantitative repository mining [48].
- **Rapidly Evolving Technology**: Rapid releases and updates to GenAI models and IDE plugins mean specific accessibility issues documented may be patched or altered over time [50].
- **Unspecified Tool Models**: For certain tasks, the specific LLM model version used by participants was not consistently probed or documented [49].
- **Non-Probabilistic Sampling**: Recruitment relied on professional networks, mailing lists, and snowball sampling due to the small, specialized population size of BLVSPs [51, 52].

---

## Contribuicao Principal

This paper presents the first empirical study investigating how blind and low vision software professionals (BLVSPs) utilize Generative AI in the workplace [13]. It reveals a "higher-risk, higher-return" dynamic: while GenAI serves as a "game changer" by boosting productivity, providing access to visual artifacts, and reducing unpaid access labor, it also exposes BLVSPs to greater risks due to severe UX/accessibility barriers, high vulnerability to hallucinations, and complex verification challenges [6, 7, 13, 19, 21, 39]. The study provides concrete recommendations for tool developers (adhering to WCAG digital accessibility standards), researchers (building non-visual verification mechanisms), and employers (implementing flexible accommodation policies) [53-55].

---

*Extraido via NotebookLM em October 2026 para MLR: Software Developer Metrics in Practice*
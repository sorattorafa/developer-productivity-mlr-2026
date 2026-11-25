# P2007 — A Systematic Literature Review on Intelligent Tools and the Developer Experience

**Decisao: INCLUIDO | Qualidade: 5/5**

---

## Dados Bibliograficos

| Campo | Valor |
|-------|-------|
| **ID** | P2007 [1] |
| **Autores** | Dora Angélica Ávila-Galván, Edgard Benı́tez-Guerrero, Carmen Mezura-Godoy [1] |
| **Ano** | 2025 [2] |
| **Venue** | IEEE International Conference on Software Engineering Research and Innovation (CONISOFT 2025) [2] |
| **DOI** | 10.1109/CONISOFT66928.2025.00046 [2] |
| **Tipo** | Conference paper (Proceeding) [2, 3] |
| **Metodo** | Systematic Literature Review (SLR) [1, 4] |
| **Amostra** | **77 primary studies** selected from an initial set of 4,524 papers [1, 5, 6] |
| **Contexto** | Mixed (Academic and Industry literature reviewing AI-based software development tools and developer experience) [1, 7, 8] |
| **Modo de trabalho** | Not specified [1, 4] |
| **Metodologia** | Not specified (Reviews primary studies covering diverse development practices and frameworks) [2, 4, 9] |

---

## Objetivo

The main objective of this systematic literature review is to analyze, synthesize, and expand the state of the art regarding **developers' experience (DX)** when interacting with **intelligent AI-based software development tools** to (semi)automate tasks across the development lifecycle [1, 10]. Specifically, the study aims to identify existing intelligent tools, determine the software development phases in which they predominate, examine the user experience (UX), developer experience (DX), and human-AI experience (HAX) variables evaluated in recent literature (2020–2025), and analyze current technical and psychological limitations to propose future research directions [1, 10-12].

---

## Questoes de Pesquisa

- **RQ1:** What are the characteristics of AI tools for software development that have evaluated the user experience? [13, 14]
- **RQ2:** What experience variables or metrics have been addressed in the studies? [13, 15]
- **RQ3:** What are the most important findings? [13, 16]
- **RQ4:** What are the limitations of these research works? [13, 17]

---

## Metricas e Instrumentos de Avaliacao

The paper identifies a wide array of UX, DX, and HAX metrics and variables evaluated across the 77 primary studies, categorized into four main dimensions [15, 18]:

| Metrica | Categoria | Nivel | Como Coletada | Validada |
|---------|-----------|-------|---------------|----------|
| **Efficiency (Eficiência)** | Productivity / DevEx [15] | Individual / Team [15] | Task completion time, empirical experiments [15] | Yes [15] |
| **Effectiveness (Eficácia)** | Quality / DevEx [15] | Individual / Team [15] | Task success rate, code accuracy evaluation [15] | Yes [15] |
| **User satisfaction (Satisfação)** | Satisfaction / DevEx [15] | Individual [15] | Standardized questionnaires (e.g., SUS), surveys [15] | Yes [15] |
| **Usefulness (Utilidade)** | DevEx / Productivity [18] | Individual [18] | User surveys, qualitative interviews [18] | Yes [18] |
| **Quantity of recommendations** | Activity / DevEx [18] | Individual [18] | IDE telemetry and tool execution logs [18] | Yes [18] |
| **Quality of recommendations** | Quality / DevEx [18] | Individual [18] | Expert code review, acceptance rate of suggestions [18] | Yes [18] |
| **Appeal, Design & Aesthetics** | DevEx / Satisfaction [18] | Individual [18] | Likert-scale UX questionnaires [18] | Yes [18] |
| **Enjoyment & Hedonic motivation** | Satisfaction / DevEx [18] | Individual [18] | Self-reported motivation surveys [18] | Yes [18] |
| **Feedback quality** | DevEx [18] | Individual [18] | Qualitative user evaluations [18] | Yes [18] |
| **Cognitive load (Carga cognitiva)** | DevEx / Productivity [18] | Individual [18] | Subjective mental workload scales (e.g., NASA-TLX), interviews [18] | Yes [18] |
| **Intention to use (Intenção de uso)** | DevEx / Satisfaction [18] | Individual [18] | TAM (Technology Acceptance Model) surveys [18] | Yes [18] |
| **Flexibility & Clarity** | DevEx [18] | Individual [18] | User perception questionnaires [18] | Yes [18] |
| **Novelty (Novidade)** | DevEx [18] | Individual [18] | Psychometric survey items [18] | Yes [18] |
| **Trust & Transparency** | DevEx / Collaboration [18, 19] | Individual [18, 19] | Qualitative interviews, trust perception scales [18, 19] | Yes [18, 19] |
| **Well-being & Stress reduction** | Satisfaction / DevEx [18] | Individual [18] | Self-reported stress and well-being assessments [18] | Yes [18] |
| **Accessibility (Acessibilidade)** | Quality / DevEx [20, 21] | Individual [20, 21] | Automated accessibility evaluation tools, code auditing [20, 21] | Yes [20, 21] |

---

## Frameworks e Metricas

### Frameworks Referenciados
- **ISO 9241-210 (Human-centred design standard):** **REFERENCED** (cited to define the foundational principles of User Experience) [22, 23].
- **Morville's UX Honeycomb:** **REFERENCED** (discussed regarding core UX facets: useful, usable, desirable, findable, accessible, credible, valuable) [24].
- **Fagerholm & Munch DX Framework:** **REFERENCED** (cited to define Developer Experience across Cognitive, Affective, and Conative dimensions) [24-26].
- **Greiler et al. DX Framework:** **REFERENCED** (discussed as an actionable framework for understanding and improving developer experience) [4, 24].
- **Human-AI Experience (HAX) Framework:** **REFERENCED** (discussed for understanding and designing human interaction with AI-infused tools) [11].
- **PICSE Framework (Johnson et al.):** **REFERENCED** (cited regarding trust establishment in software engineering tools) [3, 27].
- **SPADE Method (Elshan et al.):** **REFERENCED** (cited for low-code development of smart personal assistants) [28, 29].
- **ChatDev Framework (Qian et al.):** **REFERENCED** (cited as a multi-agent communicative framework following waterfall methodology) [9, 30].

### Frameworks Propostos
The paper does **not propose a new operational metric framework**; rather, it synthesizes current literature into a **4-domain taxonomy of Developer Experience metrics** (Usability, Functionality, Subjective/Emotional Aspects, Cognitive/Behavioral Factors) [15, 18] and presents a conceptual diagram mapping **divergent developer perceptions** across trust, usefulness, productivity, tool adaptability, and future employment concerns [17, 31, 32].

---

## Fatores que Influenciam Produtividade

### Fatores Positivos
| Fator | Categoria |
|-------|-----------|
| **Idea generation and problem-solving assistance** (Auxílio na geração de ideias e resolução de problemas) [31, 33] | Technical [31, 33] |
| **Time savings and routine task automation** (Economia de tempo e automação de tarefas repetitivas) [1, 33] | Process [1, 33] |
| **Ability to focus on higher-level key development tasks** [32, 33] | Process [32, 33] |
| **Basic tool adaptability and real-time suggestion completion** [16, 20] | Technical [16, 20] |
| **Productivity boost for novice programmers** with lower initial knowledge [33] | Human [33] |
| **Reduction of work duration and associated stress, enhancing well-being** [18] | Human [18] |

### Fatores Negativos
| Fator | Categoria |
|-------|-----------|
| **AI hallucinations, generic responses, and incorrect code recommendations** [19, 32] | Technical [19, 32] |
| **Time wasted reviewing, debugging, and fixing buggy AI code** [32, 33] | Process / Technical [32, 33] |
| **Over-trust (excessive confidence)** leading to uncritical acceptance of false outputs [31, 32] | Human [31, 32] |
| **Excessive distrust** causing reluctance or total rejection of useful AI tools [19, 31] | Human [19, 31] |
| **Lack of deep personalization** regarding context, individual developer skill level, and coding style [16, 32] | Technical / Organizational [16, 32] |
| **Distraction, annoyance, and workflow interruption** caused by unhelpful pop-up suggestions [34] | Process / Human [34] |
| **Anxiety and fear regarding potential future job replacement by AI automation** [17, 19] | Human / Organizational [17, 19] |

---

## Papel da IA e Automacao

| Campo | Valor |
|-------|-------|
| **Usa IA/ML?** | **Yes** — The review systematically investigates intelligent development tools powered by AI/ML, including LLMs (ChatGPT, GPT-3.5, GPT-4, Claude 3.5), code completion assistants (GitHub Copilot, Tabnine, Amazon CodeWhisperer), multi-agent systems (ChatDev), low-code platforms, and custom research prototypes [1, 9, 20, 21, 35, 36]. |
| **Automacao de coleta?** | **No** — Primary database searches were automated using defined strings, but data extraction and quality screening were conducted manually following Kitchenham's protocol [4, 7, 8, 37]. |
| **Impacto de IA na produtividade?** | **Positive for most developers, particularly novices**, who report significant time savings, faster problem solving, and reduced mental effort [1, 33]. However, **experienced/senior developers often perceive minimal or negative productivity gains** due to time spent fixing low-quality AI code and handling hallucinations [32, 33]. |

---

## Resultados Principais

- **Literature Growth (2020–2025):** The review screened 4,524 articles down to **77 primary studies** published between 2020 and 2025 (3 in 2020, 8 in 2022, 13 in 2023, 32 in 2024, and 21 in 2025), showing a sharp rise in DX research regarding AI tools [3, 5, 6].
- **Publication Venues & Sources:** 42 studies were conference proceedings and 35 were journal papers [3, 14]. **ACM Digital Library** was the leading database (51 papers), followed by ScienceDirect (11), SpringerLink (7), IEEE Xplore (5), and Taylor & Francis (3) [3, 7, 14].
- **Dominance of Coding Phase:** The overwhelming majority of intelligent tools focus on the **coding and implementation** phase (e.g., GitHub Copilot, ChatGPT), as it requires the most developer time and effort, leaving other lifecycle phases (requirements, architecture, testing) less explored [10, 20, 35, 38].
- **Novice vs. Senior Perception Divide:** While novice developers report enhanced productivity and lower stress, experienced developers frequently criticize AI-generated code quality and feel debugging AI suggestions negates time savings [32, 33].
- **The Trust Paradox:** Adoption is heavily constrained by trust dynamics; **over-trust** leads to undetected errors and security flaws, while **under-trust** prevents developers from reaping productivity benefits [19, 31, 32].
- **Text-Centric Interaction Monoculture:** Almost all evaluated tools rely exclusively on text prompts or standard GUI pop-ups; alternative interaction modalities like **voice, touch, and canvas sketching** remain sparsely researched [36, 39-41].
- **Lack of Deep Personalization:** Current AI tools fail to adapt deeply to a developer's specific background knowledge, work habits, project context, or individual coding conventions [16, 32].
- **Job Security Anxiety:** Developers do not currently consider AI tools a threat to their jobs due to current technical flaws, but express growing worry about long-term job replacement as automation matures [17, 19, 32].

---

## Desafios do Uso das Metricas

- **Metric Definition Heterogeneity:** Lack of standardized operational definitions for DX, UX, and HAX metrics across primary studies, hindering direct quantitative cross-study comparisons [42, 43].
- **Over-emphasis on Usability at the Expense of Broader DX:** Heavy reliance on basic usability metrics (efficiency, effectiveness, satisfaction) while neglecting affective factors, long-term cognitive load, autonomy, and psychological well-being [15, 40, 44].
- **Subjectivity and Self-Reporting Bias:** Developer experience evaluations rely heavily on subjective surveys and questionnaires, which are susceptible to perceptual biases and hard to quantify objectively [42].
- **Rapid Obsolescence of Benchmarks:** Due to the fast pace of LLM updates, metric evaluations conducted on older model iterations quickly become outdated [17, 41].
- **Superficial Telemetry:** AI coding assistants typically measure usage through shallow acceptance/rejection logging rather than tracking deep developer flow, cognitive friction, or intent [18, 42].

---

## Avaliacao de Qualidade Metodologica

| Criterio | Pontuacao (0-2) | Justificativa |
|----------|----------------|---------------|
| **Objetivo claramente definido** | 2 | Clear articulation of review objectives, scope, and research questions in Section I & III [1, 4, 10, 13]. |
| **Metodologia adequada ao objetivo** | 2 | Rigorous implementation of Kitchenham's SLR guidelines with explicit search strings and multi-database execution [4, 7, 37]. |
| **Amostra/contexto descrito adequadamente** | 2 | Detailed reporting of candidate paper filtering (4,524 to 77), database breakdowns, and year distributions [3, 5-7, 14]. |
| **Ameacas a validade discutidas** | 2 | Explicit identification of SLR limitations, including gray literature exclusion, language restrictions, and heterogeneity [43]. |
| **Resultados com evidencia suficiente** | 2 | Thorough presentation of both quantitative metrics and qualitative findings across all four research questions [5, 14-17]. |
| **Contribuicao clara para pratica ou teoria** | 2 | Delivers a clear taxonomy of DX metrics and outlines an actionable roadmap for human-centered AI tools [15, 32, 44, 45]. |
| **TOTAL** | **12/12** | **Converted Quality Score: 5/5** |

---

## Limitacoes

- **Exclusion of Gray Literature and Non-English Works:** Excluding unpublished reports, white papers, blog posts, and non-English studies may omit valuable industrial tools and emerging practices [12, 43].
- **High Study Heterogeneity:** Structural differences among primary studies prevented meta-analysis or formal quantitative synthesis [43].
- **Fast Obsolescence:** Rapid advancements in LLM capabilities mean empirical evaluations of specific AI tools can become quickly outdated [17, 41].
- **Narrow Interaction Focus:** Scarcity of primary studies evaluating multimodal interfaces (voice, gesture, touch) limits conclusions to traditional text/GUI tools [36, 40, 41].

---

## Contribuicao Principal

The main contribution of this paper is providing a comprehensive, up-to-date (2020–2025) systematic literature review of **77 primary studies** investigating intelligent AI-based tools and their impact on the **Developer Experience (DX)** [1, 5, 6]. The study maps the current ecosystem of intelligent software tools, categorizes evaluated UX/DX/HAX metrics into a structured 4-domain taxonomy, uncovers critical adoption bottlenecks—such as trust imbalances, lack of deep personalization, and interaction limitations—and outlines an actionable research agenda focused on multimodal developer interfaces, adaptive AI personalization, and human-centered software engineering tools [15, 31, 32, 35, 44, 45].

---

*Extraido via NotebookLM em October 2026 para MLR: Software Developer Metrics in Practice*

---

💡 **Sugestão:** Se desejar, posso transformar esta análise estruturada em um **relatório detalhado (Tailored Report)** ou criar um **mind map** visual das métricas e fatores de produtividade encontrados no artigo. Como prefere prosseguir?
# P2039 — What Needs Attention? Prioritizing Drivers of Developers’ Trust and Adoption of Generative AI

**Decisao: INCLUIDO | Qualidade: 5/5**

---

## Dados Bibliograficos

| Campo | Valor |
|-------|-------|
| **ID** | P2039 [1] |
| **Autores** | Rudrajit Choudhuri, Bianca Trinkenreich, Rahul Pandita, Eirini Kalliamvakou, Igor Steinmacher, Marco Gerosa, Christopher A. Sanchez, Anita Sarma [1] |
| **Ano** | 2026 [2] |
| **Venue** | ACM Transactions on Software Engineering and Methodology (TOSEM) [3] |
| **DOI** | 10.1145/3842739 [2] |
| **Tipo** | Journal article [3] |
| **Metodo** | Mixed methods (Concurrent embedded mixed-methods: Quantitative survey analyzed with PLS-SEM & IPMA, EFA/CFA psychometric evaluation, and qualitative reflexive thematic analysis) [4, 5] |
| **Amostra** | \\(N = 238\\) valid responses from professional software developers at GitHub Inc. (\\(n = 84\\)) and Microsoft (\\(n = 154\\)) [6-8] |
| **Contexto** | Industry (Professional software engineering at global technology corporations: GitHub Inc. and Microsoft) [4, 6, 9] |
| **Modo de trabalho** | Not specified [8, 10] |
| **Metodologia** | Not specified (participants covered diverse software engineering responsibilities, including Coding, Code Review, System Design, DevOps, Testing, and Documentation) [10] |

---

## Objetivo

The paper aims to develop and empirically validate a theoretical model explaining the factors associated with software developers' trust in generative AI (genAI) tools and how trust, alongside developers' cognitive styles (e.g., risk tolerance, technophilic motivations, computer self-efficacy), influences their adoption intentions and usage [4, 6]. Furthermore, using Importance-Performance Matrix Analysis (IPMA) paired with qualitative thematic analysis of developer-reported challenges and risks, the study prioritizes high-impact yet underperforming genAI attributes to provide actionable design guidance for trustworthy and inclusive developer–AI interactions [4, 5, 11].

---

## Questoes de Pesquisa

- **RQ1**: What factors are associated with developers’ trust in genAI tools, and how are developers’ trust and cognitive styles associated with their adoption of these tools? [12]
- **RQ2**: Which genAI factors should be prioritized to foster developers’ trust and adoption? [12]

---

## Metricas e Instrumentos de Avaliacao

| Metrica | Categoria | Nivel | Como Coletada | Validada |
|---------|-----------|-------|---------------|----------|
| **Trust in AI** | DevEx / Satisfaction | Individual | 4-item Likert scale (Trust in eXplainable AI - TXAI scale) [13-15] | Yes [13, 16] |
| **System/Output Quality** | DevEx / Quality | Individual | Likert items (presentation, safety/security, performance, style matching) [17-19] | Yes (validated via EFA/CFA) [18, 20] |
| **Functional Value** | Productivity / DevEx | Individual | Likert items (educational value, practical work advantages) [17, 18, 21] | Yes (validated via EFA/CFA) [18, 20] |
| **Ease of Use** | DevEx | Individual | Likert items (ease of usage, workflow integration ease) [17, 18, 22] | Yes (validated via EFA/CFA) [18, 20] |
| **Goal Maintenance** | DevEx / Activity | Individual | Likert item (sustained alignment with task goals) [17, 18, 22] | Partial (single item retained post-EFA) [23, 24] |
| **Technophilic Motivations** | DevEx / Human | Individual | GenderMag facet survey Likert scale items [14, 25, 26] | Yes [25, 27] |
| **Computer Self-Efficacy** | DevEx / Human | Individual | GenderMag facet survey Likert scale items [14, 25, 26] | Yes [25, 27] |
| **Risk Tolerance** | DevEx / Human | Individual | GenderMag facet survey Likert scale items [14, 25, 28] | Yes [25, 27] |
| **Selective Information Processing** | DevEx / Human | Individual | GenderMag facet survey Likert scale items [14, 25, 29] | Yes [25, 27] |
| **Learning by Tinkering** | DevEx / Human | Individual | GenderMag facet survey Likert scale items [14, 25, 29] | Yes [25, 27] |
| **Behavioral Intention (BI)** | DevEx / Adoption | Individual | UTAUT model Likert scale items [14, 30, 31] | Yes [30, 32, 33] |
| **GenAI Usage** | Activity / Adoption | Individual | UTAUT self-reported frequency item [14, 30, 34] | Yes [30, 32, 33] |

---

## Frameworks e Metricas

### Frameworks Referenciados
- **PICSE Framework** (Personal, Interaction, Control, System, Expectations): REFERENCED & APPLIED — used as the theoretical foundation for trust-related factors, which the authors psychometrically evaluated and refined into a 4-factor structure via EFA/CFA [18, 35-37].
- **GenderMag Method** (Cognitive Styles: Risk Tolerance, Computer Self-Efficacy, Motivations, Information Processing, Learning Style): REFERENCED & APPLIED — used to operationalize and measure individual cognitive-style differences [25, 38, 39].
- **UTAUT** (Unified Theory of Acceptance and Use of Technology): REFERENCED & APPLIED — used to capture behavioral adoption intentions and usage [15, 30, 40].
- **TXAI Instrument** (Trust in eXplainable AI): REFERENCED & APPLIED — used to measure developers' latent trust [13-15].
- **TAM** (Technology Acceptance Model): REFERENCED — cited and discussed regarding technology adoption [40, 41].
- **HACAF** (Human-AI Co-Audit Framework): REFERENCED — discussed in background literature [41].
- **Self-Determination Theory (SDT)**: REFERENCED — applied to explain how interaction friction erodes competence and autonomy [42].
- **Distributed Cognition Theory**: REFERENCED — applied to explain goal-maintenance breakdowns and context disjunction [43].

### Frameworks Propostos
- The paper proposes a psychometrically validated theoretical model that links 4 core trust factors (**System/Output Quality**, **Functional Value**, **Ease of Use**, **Goal Maintenance**) to developers' trust, and combines trust with 5 GenderMag cognitive-style facets to predict genAI behavioral adoption intentions and reported usage [4, 5, 18, 44].
- The paper also introduces an **IPMA-based diagnostic framework** paired with qualitative thematic analysis to identify high-importance, underperforming tool attributes (Quadrant 4) and map them to concrete human-AI interaction design guidelines [11, 45-47].

---

## Fatores que Influenciam Produtividade

### Fatores Positivos
| Fator | Categoria |
|-------|-----------|
| **System/Output Quality** (high performance, output correctness, polished presentation, safety/security practices) [19, 44] | Technical / Process |
| **Functional Value** (educational value, practical advantages for task speed, gaining new perspectives) [21, 48] | Technical / Human |
| **Goal Maintenance** (sustained alignment between genAI actions and evolving task objectives) [22, 48] | Process / Technical |
| **Technophilic Motivations** (intrinsic interest and enjoyment in exploring emerging technology) [26, 49] | Human |
| **Computer Self-Efficacy** (confidence in effectively using and integrating emerging tools) [26, 49] | Human |
| **Risk Tolerance** (willingness to embrace uncertainty and experiment with AI tools) [28, 49] | Human |

### Fatores Negativos
| Fator | Categoria |
|-------|-----------|
| **Goal Maintenance Breakdowns** (task misalignment, lack of contextual awareness, heavy prompt engineering effort) [50-52] | Process / Human |
| **Verification Burden** (cognitive load from double-checking, dissecting, and debugging subtly incorrect code) [52, 53] | Process / Human |
| **Inconsistent Accuracy & Unpredictability** (capricious outputs, oversimplified "cookie-cutter" responses to complex business logic) [54-56] | Technical |
| **Style Mismatch** (failure to follow project architectural/coding conventions, "corp-speak" text style drift) [16, 57] | Technical / Organizational |
| **Presentation & Interface Friction** (constrained chat-only modes, lack of feedback affordances, excessive output verbosity) [58-60] | Technical / Process |
| **Safety, Privacy & Legal Risks** (data leakage concerns with proprietary code, open-source license/IP compliance, hallucinations) [61-63] | Organizational / Technical |
| **GenAI-Induced Technical Debt** (hidden bugs, security vulnerabilities, code quality degradation requiring future rework) [64-67] | Technical / Process |
| **Inefficiency in Complex/Niche Tasks** (shallow, low-effort solutions and unrecoverable error loops) [68, 69] | Technical / Process |

---

## Papel da IA e Automacao

| Campo | Valor |
|-------|-------|
| Usa IA/ML? | **Yes** — evaluates developer-facing generative AI tools powered by large language models (e.g., GitHub Copilot, ChatGPT, Claude) across software development tasks [3, 70]. |
| Automacao de coleta? | **No** — survey responses were collected directly from developers via GitHub's internal survey platform using self-report Likert scales and open-ended text fields [7, 14, 15]. |
| Impacto de IA na produtividade? | Perceived functional value (practical work advantages and learning benefits) is significantly associated with trust (\\(\beta = 0.142, p = 0.029\\)) [71, 72]. However, high verification burden, prompt engineering effort, and output modification overhead introduce extraneous cognitive load that often offsets speed gains in complex production tasks [52, 53, 73]. |

---

## Resultados Principais

- **Drivers of Developers' Trust (\\(R^2 = 0.68\\), Adj. \\(R^2 = 0.672\\))** [74, 75]:
  - **System/Output Quality** is the strongest positive predictor of trust (\\(\beta = 0.60, p < 0.001, f^2 = 0.46\\)) [48, 72].
  - **Goal Maintenance** significantly predicts trust (\\(\beta = 0.24, p = 0.002, f^2 = 0.19\\)) [48, 72].
  - **Functional Value** significantly predicts trust (\\(\beta = 0.14, p = 0.029, f^2 = 0.17\\)) [48, 72].
  - **Ease of Use** showed no statistically significant direct relationship with trust (\\(\beta = 0.02, p = 0.588\\)) [72, 76].
- **Predictors of Adoption Intentions (\\(R^2 = 0.66\\), Adj. \\(R^2 = 0.647\\))** [74, 75]:
  - **Trust** is the primary determinant of behavioral intention (\\(\beta = 0.49, p < 0.001, f^2 = 0.54\\)) [48, 72].
  - **Cognitive Styles** significantly predict adoption intentions: Technophilic Motivations (\\(\beta = 0.23, p = 0.005, f^2 = 0.26\\)), Risk Tolerance (\\(\beta = 0.20, p = 0.001, f^2 = 0.18\\)), and Computer Self-Efficacy (\\(\beta = 0.14, p = 0.012, f^2 = 0.14\\)) [48, 72].
  - Selective Information Processing (\\(\beta = 0.09, p = 0.065\\)) and Learning by Tinkering (\\(\beta = 0.06, p = 0.331\\)) were not statistically significant [72, 76].
- **Tool Usage Prediction (\\(R^2 = 0.33\\), Adj. \\(R^2 = 0.326\\))**: Behavioral intention strongly predicts reported genAI usage at work (\\(\beta = 0.57, p < 0.001, f^2 = 0.45\\)) [71, 72, 75].
- **Control Variable**: Software Engineering (SE) experience showed no significant association with trust (\\(p = 0.125\\)), adoption intention (\\(p = 0.332\\)), or usage (\\(p = 0.275\\)) [72, 77].
- **IPMA Priority Targets (Quadrant 4 — High Importance, Low Performance)** [46, 78, 79]:
  - **For Trust**: Goal Maintenance (\\(E4\\)) and System/Output Quality (including consistent accuracy \\(S4\\), style matching \\(E3\\), presentation \\(S2\\), safety practices \\(S3\\), and task performance \\(S5\\)) require critical design focus [78, 80].
  - **For Adoption**: Trust, Risk Tolerance, and Technophilic Motivations fell into Quadrant 4 [64, 79].
- **Qualitative Root Causes**: 386 open-ended responses revealed that developer friction stems from verification overhead, prompt refinement cycles, "corp-speak" tone drift, privacy uncertainties, and genAI-induced technical debt (hidden bugs, security vulnerabilities, code quality erosion) [50, 57, 61, 65].

---

## Desafios do Uso das Metricas

- **Trust Miscalibration (Over-trust vs. Under-trust)**: Developers risk either over-trusting genAI and shipping unverified vulnerabilities to production, or under-trusting and discarding beneficial support entirely [3, 81].
- **Latent Psychological Measurement**: Trust and cognitive styles are unobservable psychological constructs; relying on unvalidated single-item metrics or unverified frameworks leads to poor model fit and inaccurate conclusions [37, 82, 83].
- **Self-Reported Usage Gap**: Self-reported behavioral intentions and frequency metrics do not automatically reflect real-time, high-stakes code reliance or production code placement [40, 49].
- **Hidden Verification Overhead**: Standard speed/activity metrics mask the extra cognitive load developers expend inspecting, testing, and rewriting "subtly wrong" AI code [52, 53].
- **Domain-Specific Metric Validation**: General ease-of-use or acceptance metrics fail to account for software engineering context nuances, such as repo-level architectural style matching, security linting, or policy-as-code requirements [32, 84, 85].

---

## Avaliacao de Qualidade Metodologica

| Criterio | Pontuacao (0-2) |
|----------|----------------|
| Objetivo claramente definido | 2 [12] |
| Metodologia adequada ao objetivo | 2 [5, 86] |
| Amostra/contexto descrito adequadamente | 2 [7, 8, 10] |
| Ameacas a validade discutidas | 2 [9, 24, 87] |
| Resultados com evidencia suficiente | 2 [72, 74, 75, 88] |
| Contribuicao clara para pratica ou teoria | 2 [5, 47, 89] |
| **TOTAL** | **12/12** |

---

## Limitacoes

- **Cross-Sectional Design**: The study captures early-stage adoption dynamics and measures statistical associations rather than establishing strict causal relationships over time [87, 90].
- **Sample Scope**: Data was gathered exclusively from developers at two major global technology corporations (GitHub Inc. and Microsoft), limiting direct generalizability to small startups, open-source projects, or non-corporate settings [9].
- **Self-Reported Data**: Observations rely on survey responses rather than direct IDE telemetry or behavioral observation logs [91].
- **Single-Indicator Construct**: Psychometric refinement of PICSE reduced Goal Maintenance to a single item (\\(E4\\)), which fixed its loading to unity and precluded internal consistency evaluation (though validated qualitatively) [24].
- **No Participant Re-contact**: Company privacy policies required a single anonymous survey round without the possibility of follow-up validation interviews [91].

---

## Contribuicao Principal

The paper delivers an empirically validated theoretical model and psychometrically sound measurement instrument for developers' trust in and adoption of generative AI in software engineering [5, 36, 89]. By combining Partial Least Squares Structural Equation Modeling (PLS-SEM) with Importance-Performance Matrix Analysis (IPMA) and qualitative thematic analysis, the study identifies critical tool deficiencies—specifically goal maintenance, contextual accuracy, style matching, and safety/security—and translates them into actionable design guidelines (such as user-defined guardrails, steerability mechanisms, prompt-output attribution, grounded utterance transformation, and adaptive interaction design) to foster trustworthy and inclusive human-AI developer tools [4, 11, 89, 92-94].

---

*Extraido via NotebookLM em October 2026 para MLR: Software Developer Metrics in Practice*

---

💡 **Sugestão de próximo passo:** Gostaria que eu transformasse esta análise estruturada em um relatório formatado em PDF ou em uma apresentação de slides para discutir com sua equipe?
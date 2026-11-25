# P2010 — From AI Drag to AI Boost: A Preceptorship Framework for Developing Software Engineering Expertise in the Agentic Era

**Decisao: INCLUIDO | Qualidade: 5/5**

---

## Dados Bibliograficos

| Campo | Valor |
|-------|-------|
| **ID** | P2010 |
| **Autores** | Satyanarayana Gudimetla, Chandrakanth Challa, Suresh Gangula, Sudhakar Vunnam, R Adinarayana, Sudhamadhuri Buhyavarapu [1, 2] |
| **Ano** | 2026 [2, 3] |
| **Venue** | Technical Report / Preprint [1, 2] |
| **DOI** | Not specified [1, 2] |
| **Tipo** | Technical report [1, 2] |
| **Metodo** | Mixed methods (Quasi-experimental evaluation, statistical regression analysis, semi-structured interviews, surveys) [2, 4-6] |
| **Amostra** | 147 software engineers observed over 14 months across 3 cohorts (Pre-AI Baseline \\(n=35\\), AI-Unstructured \\(n=22\\), Preceptorship \\(n=45\\), plus active preceptors \\(n=12\\) and non-preceptor seniors \\(n=38\\)) within a 200-engineer enterprise organization; plus 32 senior engineers interviewed for competency framework creation [2, 4, 5, 7, 8] |
| **Contexto** | Industry (Enterprise software engineering organization of 200 developers responsible for mobile, web, and microservice applications) [2, 9] |
| **Modo de trabalho** | Not specified [9] |
| **Metodologia** | Not specified (Agile/DevOps practices implied via two-week sprints, story points, PR code reviews, and CI/CD pipelines) [8, 10, 11] |

---

## Objetivo

The paper's main objective is to characterize and mitigate the "AI Boost / AI Drag" asymmetry—where agentic AI tools multiply the output of senior engineers who possess systems judgment (\\(B(e) > 1.0\\)), while imposing an epistemic burden on early-in-career (EiC) developers who lack verification capabilities (\\(B(e) < 1.0\\)) [2, 10, 12]. To prevent organizational talent pipeline collapse (the "Narrowing Pyramid") [13, 14], the paper introduces and evaluates a Preceptorship Framework centered on the Preceptor-Learner-Agent (PLA) triad [2, 15, 16]. This framework integrates structured senior mentorship, dual-mode AI interaction (including Socratic Mode for pedagogical inquiry), and six-dimensional competency tracking directly into production engineering workflows to accelerate junior developer competency without degrading senior throughput [2, 15, 17, 18].

---

## Questoes de Pesquisa

The paper does not explicitly label formal research questions as RQ1, RQ2, etc., but it systematically addresses four implicit research objectives [15, 19]:

- **RQ1 (Implicit):** How does the adoption of agentic AI coding assistants impact developer productivity and skill formation across different engineer experience levels (AI Boost vs. AI Drag) [2, 10, 12, 15]?
- **RQ2 (Implicit):** To what extent does a structured Preceptorship Framework (PLA triad with Socratic AI) reduce junior developer time-to-competency (TTC) and prevent skill fragility compared to pre-AI and unstructured AI baselines [2, 5, 15, 20]?
- **RQ3 (Implicit):** How does allocating protected capacity for mentorship affect senior engineer productivity and defect escape rates [8, 17, 21]?
- **RQ4 (Implicit):** How can engineering organizations diagnose and systematically evolve their capability to foster junior developer expertise in AI-augmented environments [2, 15, 22]?

---

## Metricas e Instrumentos de Avaliacao

| Metrica | Categoria | Nivel | Como Coletada | Validada |
|---------|-----------|-------|---------------|----------|
| **Time-to-Competency (TTC)** | Productivity / DevEx / Competency | Individual | Months required for an EiC developer to achieve a mean score of 3.0/5.0 across six competency dimensions via quarterly preceptor evaluations using calibrated 5-point rubrics [5, 20] | Yes (Cohen's \\(\kappa = 0.74\\); sensitivity analysis at 2.8, 3.0, and 3.2 thresholds; covariate OLS regression) [6, 11, 23] |
| **AI Boost Multiplier B(e)** | Productivity | Individual / Experience Level | Ratio \\(P_{\text{AI}}(e) / P_{\text{baseline}}(e)\\) measuring composite throughput (story points per sprint), quality (inverse defect escape rate), and scope (lines of code per PR) across 147 developers over 14 months [7, 10] | Yes (Bootstrap resampling with 10,000 iterations for 95% CIs) [7] |
| **Time to First Independent Feature** | Activity / Delivery | Individual | Months required to independently deliver a feature-scale pull request without preceptor intervention, collected via repository/PR metadata [20, 24] | Yes (Comparative cohort evaluation) [20, 24] |
| **Time to Positive AI Multiplier (>1.0x)** | Productivity | Individual | Months required for an EiC developer to transition from AI Drag (\\(B(e) < 1.0\\)) to net-positive AI productivity (\\(B(e) > 1.0\\)), tracked via sprint telemetry [20, 24] | Yes (Cohort comparative analysis) [20, 24] |
| **12-Month Retention Rate** | Retention / DevEx | Organization / Cohort | Percentage of EiC developers retained 12 months post-onboarding, collected from HR records [20, 23, 24] | Yes (Fisher's exact test, \\(p = 0.009\\), odds ratio = 5.48) [23] |
| **AI-Blackout Task Completion Rate** | Quality / Competency | Individual | Proportion of developers passing \\(\ge 3\\) of 4 proctored 90-minute standardized maintenance exercises completed with all AI tools disabled [24, 25] | Yes (Two-reviewer scoring \\(\kappa = 0.81\\); Cronbach's \\(\alpha = 0.76\\) for the 4-task battery) [25] |
| **Competency Dimension Scores (D1–D6)** | Competency / DevEx | Individual | Scores (1.0–5.0) in Systems Reasoning (D1), Verification Judgment (D2), Debugging Proficiency (D3), Architectural Intuition (D4), Agent Directing (D5), and Operational Awareness (D6) collected quarterly via preceptor rubric assessments + NLP telemetry gap reporting [4, 11, 26, 27] | Yes (Overall Cohen's \\(\kappa = 0.74\\); per-dimension kappas ranging from 0.68 to 0.79) [5, 11] |
| **Code Review Acceptance Rate** | Quality | Individual / Experience Level | Percentage of submitted pull requests accepted upon review, extracted from GitHub/code review logs [7] | Yes (Observed across experience levels) [7] |
| **Defect Escape Rate** | Quality | Individual / Team | Defects reaching production per 100 merged PRs, tracked via CI/CD pipelines, issue trackers, and incident logs [7, 8, 11] | Yes (Tracked across experience tiers and preceptor vs non-preceptor seniors) [7, 8] |
| **Agent Directing Effectiveness** | Activity / Competency | Individual | Rating (1.0–5.0) evaluating problem decomposition, prompt crafting, and agent behavior steering [4, 7, 27] | Yes (Calibrated rubric rating) [7, 28] |
| **Sprint Velocity** | Delivery / Productivity | Individual / Team | Mean story points completed per sprint, extracted from project management tools [8] | Yes (Comparative analysis between preceptor and non-preceptor seniors) [8] |
| **Team Knowledge Redundancy Score** | Collaboration / DevEx | Team | Score (1.0–5.0) measuring the average number of team members capable of maintaining each critical subsystem [8, 21] | Partial (Organizational team metric) [8, 21] |
| **Misconception Detection Classifier Performance** | Quality / Tracking | System / Individual | Classifier precision and recall for identifying learner misconceptions from interaction logs using Claude 3.5 Sonnet [11] | Yes (78% precision and 72% recall on a held-out set of \\(n=300\\)) [11] |

---

## Frameworks e Metricas

### Frameworks Referenciados
- **SPACE Framework** [29]: **REFERENCED** (Cited to emphasize that developer productivity is multidimensional and to warn against unidimensional velocity metrics) [30].
- **DORA Metrics** [13]: **REFERENCED** (Cited as established delivery predictors for DevOps and software pipeline performance) [4, 30].
- **DevEx Framework**: **REFERENCED** (Discussed regarding developer friction, disengagement, psychological safety, and impostor syndrome) [23, 30].
- **Cognitive Apprenticeship Framework (Collins, Brown, & Newman)** [31]: **REFERENCED & APPLIED** (Used as the foundational pedagogical model providing six methods: modeling, coaching, scaffolding, articulation, reflection, and exploration) [4, 15, 32, 33].
- **Zone of Proximal Development (ZPD) (Vygotsky)** [7]: **REFERENCED & APPLIED** (Used as the core calibration principle for adjusting scaffolding across progressive exposure phases) [32-34].
- **Seniority-Biased Technological Change (SenBTC) (Hosseini Maasoum & Lichtinger)** [15, 35]: **REFERENCED** (Used to explain how generative AI amplifies experienced engineers while displacing entry-level roles) [15, 31].
- **People Capability Maturity Model (P-CMM) & CMMI** [36, 37]: **REFERENCED** (Used as structural inspiration for the proposed Preceptorship Maturity Model) [22].

*Note: Frameworks such as GQM, HEART, or OKR are not mentioned in the paper.*

### Frameworks Propostos
- **Preceptor-Learner-Agent (PLA) Triad**: An organizational design pattern establishing bidirectional relationships between Senior Preceptors, Junior Learners, and AI Agents [2, 15, 16]. It incorporates dual-mode AI (Production Mode for senior velocity vs. Socratic Mode for pedagogical engagement), six core competency dimensions (D1–D6), and a 5-phase Progressive Exposure Model (Observe, Assist, Contribute, Lead, Graduate) [4, 18, 34, 38].
- **AI Boost / AI Drag & Narrowing Pyramid Framework**: A theoretical framework describing the empirical threshold (~3 years experience) where AI augmentation transforms from a drag (\\(B(e) < 1.0\\)) into a boost (\\(B(e) \ge 1.8x\\)), modeling the structural risks of narrowing junior developer hiring pipelines [10, 12-14, 39].
- **Preceptorship Maturity Model (PMM)**: A 5-level maturity model (Level 1: Ad Hoc, Level 2: Defined, Level 3: Managed, Level 4: Optimized, Level 5: Innovating) providing diagnostic and prescriptive roadmaps for AI-augmented developer development [2, 15, 22, 40-42].

---

## Fatores que Influenciam Produtividade

### Fatores Positivos
| Fator | Categoria |
|-------|-----------|
| **Agentic AI Augmentation for Experienced Engineers (\\(\ge 3\\) years experience)** | Technical [7, 10, 39] |
| **Structured Preceptorship & Mentorship (20% protected capacity for seniors)** | Organizational [2, 15, 17] |
| **Socratic AI Mode (Inquiry-First protocols & Concept Verification / Teach-Back)** | Human / Process [18, 28, 43] |
| **Dual-Mode AI Configuration (Production Mode vs. Socratic Mode)** | Technical / Process [15, 16, 18] |
| **Competency Tracking & Automated Misconception Signals (24–48h feedback loops)** | Process / Technical [11, 18, 43, 44] |
| **Progressive Exposure Model (Competency-gated phase transitions)** | Process [34, 36, 38] |
| **Preceptor Certification Program (16-hour pedagogical training)** | Human / Organizational [17, 45] |

### Fatores Negativos
| Fator | Categoria |
|-------|-----------|
| **AI Drag (Verification deficit in developers with \\(< 3\\) years experience)** | Human / Technical [2, 12, 39] |
| **Unstructured / Unassisted Generative AI Adoption** | Process / Organizational [2, 5, 46] |
| **Accumulation of Epistemic Debt & Fragile Expert Syndrome** | Human [2, 24, 46-48] |
| **Premature Abstraction & Cargo-Cult Code Generation by AI Agents** | Technical / Process [49] |
| **Learning Displacement (Bypassing effortful cognitive processing / productive struggle)** | Human [49] |
| **Narrowing Engineering Pyramid (Reductions in junior hiring ratios)** | Organizational [2, 13, 14, 50] |
| **Verification Overhead, Integration Effort, & Prompt Iteration Costs** | Technical / Process [30] |

---

## Papel da IA e Automacao

| Campo | Valor |
|-------|-------|
| **Usa IA/ML?** | **Yes** — The paper evaluates agentic coding tools (Cursor, GitHub Copilot, Claude 3.5 Sonnet, GPT-4, Model Context Protocol - MCP) operating in dual modes (Production and Socratic) [9, 15, 18, 35, 44]. It also uses fine-tuned ML (Claude 3.5 Sonnet classifier trained on 1,200 labeled responses) to detect learner misconceptions from interaction logs with 78% precision and 72% recall [11]. |
| **Automacao de coleta?** | **Yes** — Automated telemetry collection from CI/CD pipelines, repository PR metadata, SonarQube static code analysis, AI interaction logs, and an automated competency tracking service that surfaces gap reports to preceptors within 24–48 hours [11, 44]. |
| **Impacto de IA na produtividade?** | **Highly asymmetric** — Experienced engineers (\\(\ge 3\\) years) realize a **2.7x–3.4x throughput boost** [2, 7, 39]. Conversely, juniors (\\(< 3\\) years) using unstructured AI suffer **AI Drag** (\\(0.6x–0.9x\\) baseline multiplier, 22.3% defect escape rate, 25% longer time-to-competency, and a 76.9% failure rate on unassisted tasks) [2, 7, 12, 24, 46]. When paired with the Preceptorship Framework, junior time-to-competency is reduced by **41% vs. pre-AI baseline** and **53% vs. unstructured AI** [2, 20, 51]. |

---

## Resultados Principais

- **AI Boost vs. AI Drag Multipliers:**
  - **Staff/Principal Engineers (\\(10+\\) yrs):** **3.4x** multiplier (95% CI: [3.0, 3.8]), 94.2% code review acceptance, 1.8% defect escape rate [7].
  - **Senior Engineers (\\(5–10\\) yrs):** **2.7x** multiplier (95% CI: [2.4, 3.0]), 89.7% acceptance, 3.2% defect escape rate [7].
  - **Mid-Level Engineers (\\(3–5\\) yrs):** **1.8x** multiplier (95% CI: [1.4, 2.2]), 78.3% acceptance, 7.1% defect escape rate [7].
  - **Junior Engineers (\\(1–3\\) yrs):** **0.9x** multiplier (95% CI: [0.7, 1.1]), 61.4% acceptance, 14.6% defect escape rate (AI Drag) [7, 12].
  - **New Graduates (\\(< 1\\) yr):** **0.6x** multiplier (95% CI: [0.4, 0.8]), 48.2% acceptance, 22.3% defect escape rate (AI Drag) [7, 12].
- **Time-to-Competency (TTC):**
  - Preceptorship cohort achieved competency (3.0/5.0) in **8.4 months** (\\(\sigma = 2.3\\)), compared to **14.2 months** (\\(\sigma = 3.1\\)) for the Pre-AI Baseline (**41% reduction**, Welch's \\(t(62) = 8.74, p < 0.001\\), Cohen's \\(d = 2.13\\)) and **17.8 months** (\\(\sigma = 4.6\\)) for the AI-Unstructured cohort (**53% reduction**) [20, 24, 51].
  - Covariate-adjusted OLS regression (controlling for team fixed effects, project complexity, and prior experience) showed Preceptorship reduced TTC by **5.4 months** (\\(p < 0.001\\), model \\(R^2 = 0.61\\)) [6, 52].
- **Delivery and Autonomy Milestones:**
  - Time to first independent feature was reduced to **5.1 months** in the Preceptorship cohort vs. **8.5 months** in Baseline (-40.0%) and **11.2 months** in Unstructured (-54.5%) [20, 24].
  - Time to achieve a positive AI productivity multiplier (\\(>1.0x\\)) was **6.8 months** for Preceptorship vs. **12.4 months** for Unstructured (-45.2%) [20, 24].
- **Retention & AI-Blackout Performance:**
  - 12-month retention rate reached **91.1%** for the Preceptorship cohort vs. **65.2%** for AI-Unstructured (\\(+25.9\\) percentage points, \\(p = 0.009\\), odds ratio = 5.48) [20, 23, 24].
  - Unassisted "AI-blackout" task completion rate was **61.4%** for Preceptorship vs. **23.1%** for AI-Unstructured (\\(+165.8\%\\) relative improvement, \\(p = 0.002\\)), verifying mitigation of Fragile Expert skill atrophy [2, 24, 46].
- **Senior Preceptor Productivity Impact:**
  - Active senior preceptors maintained a **2.7x** throughput multiplier with only a **4.1%** velocity reduction (32.8 vs. 34.2 story points) despite allocating 20% capacity to mentorship [8, 21].
  - Preceptors achieved **27.6% lower defect escape rates** (2.1% vs. 2.9%) and **88.9% higher team knowledge redundancy** (3.4 vs. 1.8 out of 5.0) compared to non-preceptor seniors [8, 21].

---

## Desafios do Uso das Metricas

- **Unidimensional Productivity Measurement:** Relying solely on lines of code or story points creates false productivity signals, masking epistemic debt and verification deficits in AI-generated code [30, 48, 49].
- **Fragile Expert Anti-Pattern:** High apparent throughput during AI-assisted workflows masks severe failure rates (up to 76.9% in unstructured cohorts) when developers are required to complete maintenance or debugging tasks without AI assistance [2, 24, 46, 47].
- **Verification Deficit:** Junior developers lack the cognitive schemata needed to identify subtle flaws (e.g., race conditions, security vulnerabilities, performance anti-patterns) in AI output, resulting in high production defect escape rates (22.3%) [12].
- **Subjectivity in High-Level Assessment:** Metrics evaluating design judgment and architectural intuition (D4) exhibit lower inter-rater reliability (\\(\kappa = 0.68\\)), requiring qualitative written justification requirements for high scores [5, 11].
- **Retrospective Baseline Measurement Error:** Reconstructing historical pre-AI baseline competency scores from archived records introduces measurement error relative to prospective tracking [9].
- **Pedagogy vs. Surveillance Tension:** Collecting interaction telemetry and NLP logs creates risks of developer perception of surveillance rather than educational feedback, requiring strict access limits and non-employment governance boundaries [53, 54].
- **Short-Term Capacity Optimization Anti-Pattern:** Firms optimizing purely for immediate team output narrow junior hiring, risking catastrophic organizational pipeline collapse and knowledge concentration within 2–5 years [13, 14, 50].

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

- **Non-Randomized Quasi-Experimental Design:** Cohort assignment was determined by onboarding dates rather than random assignment, introducing potential macroeconomic, candidate pool, and historical confounding factors [2, 5, 55, 56].
- **Single-Organization Scope:** Conducted entirely within a single enterprise software company (200 engineers), requiring further replication before generalizing to startups, open-source projects, or safety-critical domains [9, 57].
- **Hawthorne and Organizational Maturation Effects:** Later cohorts benefited from overall organizational AI maturation and increased resources/attention, which cannot be completely isolated from the specific treatment effect [56, 58].
- **Lack of Long-Term Post-Program Follow-Up Data:** The 14-month study window tracks developers during active preceptorship but lacks multi-year post-graduation tracking to verify if competency gains persist after scaffolding is removed [19, 59].
- **Incomplete Unassisted Competency Coverage:** 38.6% of preceptorship graduates still failed the unassisted AI-blackout assessment, indicating developers become significantly more capable but are not fully independent without AI assistance [6].
- **Subgroup Power Constraints:** Small sample sizes in specific subgroups (e.g., \\(n=22\\) in AI-Unstructured, \\(n=12\\) active preceptors) limit statistical power for detecting small effect sizes [8, 60].
- **Construct Reliability Limits in Architecture:** Assessment of architectural intuition (D4) carries inherent subjectivity, reflected in lower inter-rater agreement (\\(\kappa = 0.68\\)) [11, 60].

---

## Contribuicao Principal

The primary contribution of this paper is the conceptualization and empirical evaluation of the **Preceptorship Framework**, operationalized through the **Preceptor-Learner-Agent (PLA) triad**, which addresses seniority-biased technological change ("AI Boost" vs. "AI Drag") in software engineering [2, 15, 16, 33]. By embedding structured senior mentorship (with 20% protected capacity), dual-mode Socratic AI interactions (Inquiry-First and Concept Verification), and six-dimensional competency tracking directly into production workflows, the paper demonstrates that engineering organizations can reduce junior developer time-to-competency by 41% and mitigate skill fragility without degrading senior engineer throughput or collapsing the long-term talent pipeline [2, 8, 15, 17, 18, 20].

---

*Extraido via NotebookLM em October 2026 para MLR: Software Developer Metrics in Practice*

---

💡 **Sugestão de Próximo Passo:** Se desejar, posso elaborar um resumo executivo em formato de relatório ou uma apresentação em tópicos destacando os principais insights práticos do modelo de preceptoria para a gestão de equipes de engenharia de software.
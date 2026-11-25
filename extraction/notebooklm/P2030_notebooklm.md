# P2030 — From Gains to Strains: Modeling Developer Burnout with GenAI Adoption

**Decisao: INCLUIDO | Qualidade: 5/5**

---

## Dados Bibliograficos

| Campo | Valor |
|-------|-------|
| **ID** | P2030 |
| **Autores** | Zixuan Feng, Sadia Afroz, Anita Sarma [1] |
| **Ano** | 2026 [2] |
| **Venue** | IEEE/ACM 48th International Conference on Software Engineering (ICSE-SEIS '26) [2] |
| **DOI** | https://doi.org/10.1145/3786581.3786934 [2] |
| **Tipo** | Conference paper [2] |
| **Metodo** | Mixed methods (Concurrent embedded design: Survey N=442, Partial Least Squares–Structural Equation Modeling [PLS-SEM], Ordinary Least Squares [OLS] Regression, and Qualitative analysis) [1, 3, 4] |
| **Amostra** | N=442 professional developers across 56 Open Source Software (OSS) communities and industry organizations (398 men [90.05%], 44 gender minorities [9.95%]) [3, 5, 6] |
| **Contexto** | Mixed (Industry & Open Source Software communities, including organizational repositories like Microsoft, Google, Netflix, Red Hat, IBM, and open-source infrastructure/AI projects like Kubernetes, Hugging Face, TensorFlow) [5, 7] |
| **Modo de trabalho** | Not specified [7, 8] |
| **Metodologia** | Not specified [7, 8] |

---

## Objetivo

This paper investigates the relationship between the adoption of Generative AI (GenAI) coding tools and software developer burnout [1]. Grounded in the Job Demands–Resources (JD–R) model, the authors construct an empirical, explanatory framework to evaluate how GenAI adoption acts either as a job demand amplifier (by elevating organizational pressure and workload) or as a job resource enabler (through developer autonomy and learning resources), while analyzing how developer characteristics (role, organization size, and industry seniority) affect these dynamics [1, 3, 9, 10].

---

## Questoes de Pesquisa

- **RQ1**: How is GenAI adoption associated with developer burnout? [11]
- **RQ2**: How do developers’ characteristics influence their perceptions of burnout? [11]

---

## Metricas e Instrumentos de Avaliacao

| Metrica | Categoria | Nivel | Como Coletada | Validada |
|---------|-----------|-------|---------------|----------|
| **Burnout** | Satisfaction / DevEx / Well-being | Individual | Survey (4 reflective 5-point Likert items covering exhaustion, cynicism, and job insecurity adapted from Trinkenreich et al.) [12, 13] | Yes (CR = 0.825, AVE = 0.542, Cronbach's \\(\alpha\\) = 0.718) [14] |
| **Organizational Pressure** | Organizational / Process | Individual / Team | Survey (4 reflective 5-point Likert items capturing management adoption mandates, peer dependencies, and performance evaluations) [15, 16] | Yes (CR = 0.875, AVE = 0.642, Cronbach's \\(\alpha\\) = 0.827) [14] |
| **Workload** | Activity / Delivery / DevEx | Individual | Survey (4 reflective 5-point Likert items measuring task overload and intensified effort adapted from Cao et al.) [15, 16] | Yes (CR = 0.866, AVE = 0.621, Cronbach's \\(\alpha\\) = 0.801) [14] |
| **Autonomy** | DevEx / Process | Individual | Survey (3 reflective Likert items assessing decision discretion, authority, and task execution influence adapted from Clausen et al.) [16, 17] | Yes (CR = 0.911, AVE = 0.775, Cronbach's \\(\alpha\\) = 0.856) [14] |
| **Learning Resources** | Organizational Support / DevEx | Organization / Individual | Survey (Single-item 5-point Likert statement assessing org provision of time, training, and learning tools) [16, 17] | Partial (Single-item construct; reliability and AVE not applicable) [14] |
| **AI Perception** | Satisfaction / Attitude | Individual | Survey (Single-item statement rating overall positive agreement with AI usage) [8, 18] | Partial (Single-item control variable) [18] |
| **Task Speedup / Completion Time** | Productivity / Delivery | Individual | Cited literature metrics (e.g., GitHub Copilot RCTs, Becker et al. observational study) [19, 20] | Yes (Cited external studies) [19, 20] |
| **Software Delivery Performance & Code Quality** | Delivery / Quality | Team / Organization | Cited literature metrics (DORA 2024 State of DevOps report metrics) [21] | Yes (Cited external studies) [21] |

---

## Frameworks e Metricas

### Frameworks Referenciados
- **Job Demands–Resources (JD–R) model**: APPLIED — Used as the primary theoretical lens to formulate hypotheses, structure survey items, build PLS-SEM latent constructs, and analyze qualitative findings [1, 3, 22].
- **SPACE framework**: REFERENCED — Discussed regarding how GenAI enhances productivity in routine development tasks [20].
- **DORA framework**: REFERENCED — Discussed in relation to external enterprise reports on software delivery performance and code quality impacts [21].
- **Transactional Model of Stress / Conservation of Resources (COR) / Social Cognitive Theory**: REFERENCED — Discussed as background theories of workplace stress and burnout [23].

### Frameworks Propostos
- **GenAI-Extended Job Demands–Resources Model**: The paper proposes an empirical JD–R structural model specific to GenAI adoption in software engineering [1, 9]. It models **Job Demands** as a higher-order formative construct (comprising Organizational Pressure and Workload) and **Job Resources** as a higher-order formative construct (comprising Autonomy and Learning Resources), controlling for **AI Perception**, explaining 39.8% (\\(R^2 = 0.398\\)) of the variance in developer burnout [16, 24-26].

---

## Fatores que Influenciam Produtividade

### Fatores Positivos
| Fator | Categoria |
|-------|-----------|
| Developer autonomy in choosing when and how to integrate AI tools [27, 28] | Process / Human |
| Organizational provision of explicit learning resources, training, and time to master AI [27, 29] | Organizational |
| Positive developer perceptions, trust, and enthusiasm toward AI automation [30-32] | Human |
| Offloading tedious, repetitive routine tasks to agentic tools (e.g., Cursor) [20, 32] | Technical |

### Fatores Negativos
| Fator | Categoria |
|-------|-----------|
| Top-down organizational mandates and C-level pressure to enforce AI usage [33, 34] | Organizational |
| Workload intensification and unrealistic management expectations for increased output speed [21, 35, 36] | Organizational / Process |
| Increased time spent verifying, debugging subtle errors, and fixing security vulnerabilities in AI-generated code [19, 21, 36] | Technical / Process |
| Constant context switching and attention fragmentation from frequent AI code injections ("mini peer-reviews") [28] | Technical / Human |
| Collaboration friction caused by peers submitting high volumes of unverified, verbose AI content ("AI spam") [37, 38] | Process / Human |
| Lack of formal training, clear guidelines, or structured onboarding for AI tools [21, 29, 39] | Organizational |
| Perceived job insecurity and fear of deskilling due to entry-level position reductions [30, 40] | Organizational / Human |

---

## Papel da IA e Automacao

| Campo | Valor |
|-------|-------|
| **Usa IA/ML?** | Yes — Investigates the integration and impact of Generative AI coding assistants (e.g., GitHub Copilot, Cursor, LLM agents) across software development workflows [1, 32, 41]. |
| **Automacao de coleta?** | No — Primary empirical data was gathered via developer surveys and analyzed using SmartPLS 4, JASP, and qualitative thematic coding [42-44]. |
| **Impacto de IA na produtividade?** | Paradoxical/Mixed: While GenAI can accelerate initial code creation for routine tasks, it shifts effort toward verification, debugging, and code review [19, 45]. When management translates AI tools into higher output quotas, it acts as a demand amplifier that significantly increases burnout (\\(\beta = 0.398, p < 0.001\\)), whereas developer autonomy (\\(\beta = -0.360\\)) and positive AI perceptions (\\(\beta = -0.246\\)) cushion these negative effects [25, 31]. |

---

## Resultados Principais

- **GenAI Adoption Drives Burnout via Job Demands (H1)**: Job Demands resulting from GenAI adoption (organizational pressure and workload intensification) are positively associated with developer burnout (\\(\beta = 0.398, p < 0.001\\)) [31, 46].
- **Job Resources & Positive Attitudes Mitigate Burnout (H2 & H3)**: Job Resources (autonomy and learning resources) (\\(\beta = -0.360, p < 0.001\\)) and positive AI perceptions (\\(\beta = -0.246, p < 0.001\\)) significantly reduce developer burnout [31, 46].
- **Model Explanatory & Predictive Power**: The proposed JD–R structural model accounts for 39.8% of the variance in developer burnout (\\(R^2 = 0.398\\)) with strong predictive relevance (\\(Q^2 = 0.373\\), SRMR \\(< 0.08\\)) [26, 46].
- **Influence of Developer Role & Organization Size (RQ2)**:
  - Developers in coding-intensive roles experience significantly higher Organizational Pressure (\\(\beta = 0.51, p < 0.05\\)) [47, 48].
  - Larger organizations exert higher Organizational Pressure (\\(\beta = 0.41, p < 0.001\\)) and offer less Autonomy (\\(\beta = -0.13, p < 0.001\\)), but provide significantly more Learning Resources (\\(\beta = 0.28, p < 0.001\\)) [47-50].
  - Higher Industry Seniority is positively associated with Autonomy (\\(\beta = 0.18, p < 0.001\\)) and access to Learning Resources (\\(\beta = 0.14, p < 0.05\\)) [47, 49, 50].
  - Overall Burnout did not vary significantly across role, company size, or experience, showing that burnout is an industry-wide challenge (\\(H4a\\) not supported) [47].
- **Gaps in Learning Support**: 22.4% of developers reported receiving no organizational support for AI learning [39]. Self-study (15.23%) is predominantly relied upon by developers in small companies and senior engineers [51, 52].

---

## Desafios do Uso das Metricas

- **Metric-Driven Mandates ("Forced Adoption")**: Mandating AI adoption simply to report usage metrics to upper management forces developers to use tools even when counterproductive [28, 34].
- **Flawed Productivity Metrics**: Measuring developer performance purely by speed or code output volume without accounting for verification, debugging, and oversight costs leads to unsustainable workload expectations [45, 53].
- **KPI Misalignment & AI Spam**: Rewarding raw volume encourages team members to generate and submit massive amounts of unverified, verbose AI code and documentation ("AI spam"), shifting the review and editing burden onto peers [37, 38].
- **Invisibility of Curation Work**: Traditional metrics fail to track or recognize the high cognitive effort required for reviewing and editing AI-generated code, creating equity issues within development teams [38, 45, 54].

---

## Avaliacao de Qualidade Metodologica

| Criterio | Pontuacao (0-2) |
|----------|----------------|
| Objetivo claramente definido | 2 |
| Metodologia adequada ao objetivo | 2 |
| Amostra/contexto descrito adequadamente | 2 |
| Ameacas a validade discutidas | 1 |
| Resultados com evidencia suficiente | 2 |
| Contribuicao clara para pratica ou teoria | 2 |
| **TOTAL** | **11/12** |

*Justificativa*: The paper defines clear research questions and objectives [11]. The concurrent embedded mixed-methods methodology combines robust statistical modeling (PLS-SEM, OLS regression with Benjamini-Hochberg adjustment, power analysis) with qualitative coding (\\(IRR \ge 90\%\\)) [3, 4, 18, 44, 55, 56]. The sample (\\(N=442\\)) across 56 OSS/industry contexts is well-documented [5-7]. Threats to validity and limitations are discussed (e.g., cross-sectional constraints preventing strict causal claims) [57-59]. Findings are strongly backed by statistical metrics (\\(p < 0.001, R^2 = 0.398\\)) and qualitative quotes [26, 31, 34], providing clear theoretical and practical contributions [9, 45, 53, 54].

---

## Limitacoes

- **Cross-sectional Study Design**: The study captures a cross-sectional snapshot, establishing statistical associations between variables rather than definitive longitudinal causality [58].
- **Potential Unmeasured Confounders**: Confounding factors such as baseline developer burnout prior to AI adoption, specific trust levels, or varying task complexity were not directly measured [58].
- **Theoretical Scope**: Although the JD–R model provides a structured framework, certain technical or social nuances of GenAI adoption may lie outside its scope [57].
- **Self-Reported Survey Data**: Findings rely on self-reported survey responses, which may introduce response bias (e.g., developers under high deadline pressure perceiving AI demands differently) [58].

---

## Contribuicao Principal

This paper provides the first empirical and theoretical model establishing how Generative AI adoption impacts software developer burnout [1, 60]. By extending the Job Demands–Resources (JD–R) framework to AI adoption, the study demonstrates that GenAI functions as a double-edged sword: top-down management mandates and elevated output expectations turn GenAI into a demand amplifier that heightens burnout, whereas developer autonomy, learning resources, and positive AI perceptions serve as crucial buffers [9, 31]. The authors offer actionable recommendations for recalibrating performance KPIs, scaffolding continuous learning, and adapting team workflows to ensure sustainable AI integration [9, 53, 54, 61].

---

*Extraido via NotebookLM em October 2026 para MLR: Software Developer Metrics in Practice*
# P2114 — The effect of knowledge work productivity factors on software development

**Decisao: INCLUIDO | Qualidade: 4.6/5**

---

## Dados Bibliograficos

| Campo | Valor |
|-------|-------|
| **ID** | P2114 [1] |
| **Autores** | MOHD ZAIROL YUSOFF, MASSUDI MAHMUDDIN, MAZIDA AHMAD [1] |
| **Ano** | 2017 [1, 2] |
| **Venue** | Journal of Engineering Science and Technology (JESTEC) — Special Issue on ISSC’2016 [1, 2] |
| **DOI** | Not specified [1] |
| **Tipo** | Journal article (Special Issue) [1, 2] |
| **Metodo** | Quantitative / Survey (Structural Equation Modelling — SEM via SmartPLS 3) [3-5] |
| **Amostra** | 150 valid questionnaire responses (out of 200 distributed via email) from software developers, programmers, and system analysts with over 1 year of experience across 70 SME software companies in Peninsular Malaysia (pilot study conducted with 30 developers) [3-6] |
| **Contexto** | Industry (Small and Medium-sized Enterprises — SMEs in software development in Peninsular Malaysia) [2, 3, 5] |
| **Modo de trabalho** | Not specified [1, 3] |
| **Metodologia** | Not specified [1, 3] |

---

## Objetivo

This study aims to examine and validate the knowledge work productivity (KWP) factors that influence software development quality and overall business performance in Small and Medium-sized Enterprises (SMEs) [3, 7, 8]. By expanding traditional KWP theoretical models (specifically Davis & Naumann, 1999), the research evaluates how effectiveness strategies, efficiency strategies, collaboration, programmer performance, and innovation strategies affect knowledge work quality and productivity in SME software companies [3, 9-11].

---

## Questoes de Pesquisa

The paper does not explicitly state numbered Research Questions (RQ1, RQ2), but formulates and evaluates five central hypotheses regarding KWP factors [4, 11]:
- **RQ1 (H1)**: Is Knowledge Work Productivity positively influenced by effectiveness strategies [4, 12]?
- **RQ2 (H2)**: Is Knowledge Work Productivity positively influenced by efficiency strategies [4, 12]?
- **RQ3 (H3)**: Is Knowledge Work Productivity positively influenced by collaboration [4, 13]?
- **RQ4 (H4)**: Is Knowledge Work Productivity positively influenced by programmer performance [4, 14]?
- **RQ5 (H5)**: Is Knowledge Work Productivity positively influenced by innovation strategies [4, 15]?

---

## Metricas e Instrumentos de Avaliacao

| Metrica | Categoria | Nivel | Como Coletada | Validada |
|---------|-----------|-------|---------------|----------|
| **Knowledge Work Productivity (KWP)** | Productivity / Quality | Individual/Team/Organization | Survey questionnaire (8 items: AD, AD2–AD8) using a 7-point Likert scale | Yes (AVE = 0.530, CR = 0.90) [4, 16] |
| **Effectiveness Strategies** | Productivity / Process | Individual/Team/Organization | Survey questionnaire (6 items: EFFECT 1–6) assessing task scope, depth, completeness, and novel technology introduction | Yes (AVE = 0.655, CR = 0.919) [4, 17, 18] |
| **Efficiency Strategies** | Productivity / Process | Organization/Team | Survey questionnaire (5 items: EFFIC 1–5) assessing process approach, timeliness, resource usage, and IT management | Yes (AVE = 0.626, CR = 0.893) [4, 17, 18] |
| **Collaboration** | Collaboration | Team | Survey questionnaire (5 items: COLLA 1–5) assessing teamwork, trust, respect, voluntary communication, and openness to diverse views | Yes (AVE = 0.689, CR = 0.930) [4, 12, 13, 19] |
| **Programmer Performance** | Activity / Productivity | Individual | Survey questionnaire (5 items: PPERF 1–5) assessing day-to-day work quantity/quality, stakeholder interaction, innovation behavior, and standards compliance | Yes (AVE = 0.690, CR = 0.917) [4, 14, 18-20] |
| **Innovation Strategies** | DevEx / Satisfaction / Process | Team/Organization | Survey questionnaire (6 items: INNOV 1–6) assessing creation of better products, efficient processes, services, or market-accepted ideas | Yes (AVE = 0.668, CR = 0.910) [4, 14, 15, 18] |

---

## Frameworks e Metricas

### Frameworks Referenciados
- **Davis & Naumann KWP Model (1999)**: REFERENCED & APPLIED — Serves as the foundational theoretical model for effectiveness and efficiency strategies, which the authors adapt and expand by integrating individual and team performance factors [9, 17, 21].
- **Quality Management Frameworks (Davenport et al., 1996; Akdere, 2009)**: REFERENCED — Cited to contextualize KWP within continuous quality management and performance excellence [9, 22, 23].
- **DORA / SPACE / DevEx / GQM / HEART / OKR**: Not referenced in this paper [1–45].

### Frameworks Propostos
- **Expanded SME Knowledge Work Productivity (KWP) Conceptual Model**: A structural model designed specifically for SME software engineering, integrating five latent constructs (Effectiveness Strategies, Efficiency Strategies, Collaboration, Programmer Performance, Innovation Strategies) to predict Knowledge Work Productivity and quality using PLS-SEM [3, 10, 11].

---

## Fatores que Influenciam Produtividade

### Fatores Positivos
| Fator | Categoria |
|-------|-----------|
| **Collaboration** (Effective teamwork, mutual trust, respect among team members, voluntary communication, and openness to accepting different views) | Human / Organizational [12, 13] |
| **Innovation Strategies** (Creation of improved products, creative processes/services, and novel solutions accepted by the market) | Technical / Process [14, 15] |
| **Programmer Performance** (High daily work quantity/quality, positive interactions with stakeholders, compliance with professional standards, and expert skill development) | Human / Technical [14, 20] |
| **Effectiveness Strategies** (Expanding task scope, depth, and completeness, as well as adopting novel technologies to handle task complexity) | Process / Technical [17, 21] |

### Fatores Negativos
| Fator | Categoria |
|-------|-----------|
| **Isolated Efficiency Strategies** (Focusing strictly on procedural efficiency, timeliness, and resource controls without supporting developer competencies or collaboration — found to have a non-significant, negative relationship \\(\beta = -0.063\\)) | Process / Organizational [24-26] |
| **SME Resource & Capability Bottlenecks** (Resource constraints in labor cost, working capital, lack of Information Systems strategic planning, and repeatedly applying wrong requirement specifications) | Organizational / Technical [8, 27] |

---

## Papel da IA e Automacao

| Campo | Valor |
|-------|-------|
| Usa IA/ML? | No — the paper does not discuss or apply Artificial Intelligence or Machine Learning [1–45]. |
| Automacao de coleta? | No — survey data was collected manually via emailed questionnaires [4, 11]. |
| Impacto de IA na produtividade? | Not addressed in the paper [1–45]. |

---

## Resultados Principais

- The proposed PLS-SEM model accounts for **69.5% of the variance** (\\(R^2 = 0.695\\)) in Knowledge Work Productivity in software development [26, 28].
- **Collaboration** exhibits the strongest positive effect on KWP (\\(\beta = 0.280, p < 0.05, t = 3.431, p = 0.002\\)) [19, 26, 28].
- **Innovation Strategies** significantly and positively influence KWP (\\(\beta = 0.254, p < 0.05, t = 2.852, p = 0.002\\)) [26, 28, 29].
- **Programmer Performance** significantly and positively impacts KWP (\\(\beta = 0.244, p < 0.05, t = 2.474, p = 0.044\\)) [26, 28, 29].
- **Effectiveness Strategies** significantly and positively influence KWP (\\(\beta = 0.213, p < 0.05, t = 2.376, p = 0.048\\)) [26, 28, 29].
- **Efficiency Strategies** do **not** significantly influence KWP (\\(\beta = -0.063, p > 0.05, t = 0.697, p = 0.888\\), n.s.) [24, 26, 29].
- Hypotheses H1, H3, H4, and H5 received statistical support, whereas H2 was not supported [24, 26].
- The survey instrument demonstrated high internal reliability (overall Cronbach's Alpha = 0.98; Composite Reliability = 0.893–0.930; AVE = 0.530–0.690) [5, 16, 18, 19].

---

## Desafios do Uso das Metricas

- **Limitations of traditional input/output metrics**: Measuring developer productivity purely through input/output ratios fails to capture cognitive complexity and software quality [20].
- **Omission of team and individual factors**: Traditional organizational frameworks neglect parameters like interaction quality, innovation behaviors, and team trust, leading to incomplete evaluations [20, 21].
- **Misaligned efficiency initiatives**: Prioritizing rigid efficiency procedures and speed over effectiveness, developer skill growth, and collaboration fails to improve software productivity in SMEs [25, 30].
- **Repeated requirement failures**: Resource constraints and lack of IS strategic planning lead SMEs to repeat erroneous requirements specifications across projects [8, 27].

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

---

## Limitacoes

- **Geographic constraint**: The sample is limited to 70 SME software companies in Peninsular Malaysia, which may restrict generalizability to other geographic regions [5].
- **Organizational context constraint**: The study focuses strictly on SMEs, whose resource limitations and operational dynamics differ from large enterprise environments [1, 2].
- **Cross-sectional design**: Data were gathered at a single point in time, preventing longitudinal observation of productivity factors over time [4, 11].
- **Perceptual survey data**: Relies on self-reported perception items from developers and system analysts, though statistical checks confirmed low risk of common method bias [4, 24, 31].

---

## Contribuicao Principal

The key contribution of this paper is the proposal and empirical validation of a Knowledge Work Productivity (KWP) framework specifically tailored to SME software development [3, 8, 10]. By expanding traditional efficiency/effectiveness models (Davis & Naumann) to integrate collaboration, programmer performance, and innovation strategies, the authors prove via PLS-SEM (\\(R^2 = 0.695\\)) that teamwork, innovation, individual performance, and effectiveness strategies drive software quality and KWP, whereas efficiency strategies alone do not yield significant productivity gains [3, 24, 26, 28].

---

*Extraido via NotebookLM em October 2026 para MLR: Software Developer Metrics in Practice*

---

📊 *Would you like me to extract structured summaries for any other papers or compile a comparative table across multiple studies in your review?*
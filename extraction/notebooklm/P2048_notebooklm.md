# P2048 — Beyond Traditional Metrics: Toward a Multifactorial Model for Measuring Productivity in Agile Software Teams

**Decisao: INCLUIDO | Qualidade: 5/5**

---

## Dados Bibliograficos

| Campo | Valor |
|-------|-------|
| **ID** | P2048 |
| **Autores** | Marcela Guerrero-Calvache, Giovanni Hernández, and María Clara Gómez-Álvarez [1] |
| **Ano** | 2026 [1] |
| **Venue** | *Computers* (MDPI); extended version of an ICCSA 2025 conference paper [1, 2] |
| **DOI** | Not specified in text |
| **Tipo** | Journal article [1, 2] |
| **Metodo** | Mixed methods (Conceptual modeling using UML based on Fenton & Bieman protocol, Content validation via Expert judgment, Exploratory empirical application via Scrum workshops/surveys, Iterative review) [2-10] |
| **Amostra** | 10 software engineering experts (for content validation) and 110 undergraduate Systems/Software Engineering students across 4 Higher Education Institutions in Colombia (for empirical validation) [10-13] |
| **Contexto** | Academic setting simulating agile software development across 4 Colombian Higher Education Institutions, evaluated by MinCiencias-recognized software engineering experts [12-14] |
| **Modo de trabalho** | Not specified |
| **Metodologia** | Agile (Scrum) [2, 8, 13, 15] |

---

## Objetivo

This paper aims to develop, represent, and validate a multifactorial conceptual model based on UML class diagrams and the measurement protocol of Fenton and Bieman to systematically organize, operationalize, and guide productivity measurement in Agile Software Development (ASD) teams [2-4, 16]. By bridging the gap between high-level frameworks and concrete measurement procedures, the model integrates technical, human, social, and organizational dimensions influencing team performance without altering fundamental agile principles [2, 16, 17].

---

## Questoes de Pesquisa

- **RQ1**: What factors significantly influence the productivity of agile teams, and which ones are relevant to include in a conceptual model? [17, 18]
- **RQ2**: How can we measure the productivity of an ASD team using a multifactorial approach? [5, 19]
- **RQ3**: What are the essential components needed to conceptually support the measurement of team productivity in ASD? [6, 20]
- **RQ4**: What elements make up the measurement of productivity in agile software development teams, and how are they conceptually related? [6, 21]

---

## Metricas e Instrumentos de Avaliacao

| Metrica | Categoria | Nivel | Como Coletada | Validada |
|---------|-----------|-------|---------------|----------|
| **Velocity** | Productivity / Meaning | Team | Sum of completed user stories per iteration / Sprint tracking logs [22, 23] | Partial (Exploratory Scrum pilot) [2, 12] |
| **Work Capacity** | Productivity / Meaning | Team | Planned available working hours vs. effort capacity logs [22] | Partial (Exploratory Scrum pilot) [2, 12] |
| **Customer Satisfaction** | Satisfaction / Meaning | Organization / Team | Customer evaluation forms / Feedback surveys [22] | Partial (Exploratory Scrum pilot) [2, 12] |
| **Understanding job roles** | DevEx / Meaning | Individual / Team | Team self-assessment surveys / Questionnaires [22] | Partial (Exploratory Scrum pilot) [2, 12] |
| **Team Capacity** | Productivity / Meaning | Team | Sprint capacity planning artifacts [22] | Partial (Exploratory Scrum pilot) [2, 12] |
| **Goal setting** | Productivity / Flexibility | Team | Target tracking / Sprint commitment review [24] | Partial (Exploratory Scrum pilot) [2, 12] |
| **Quality** | Quality / Flexibility | Team / Product | Defect logs, post-delivery bug tracking, rework metrics [24, 25] | Partial (Exploratory Scrum pilot) [2, 12] |
| **Requirements handling by the Team** | Activity / Flexibility | Team | Product backlog refinement and user story tracking tools [13, 24] | Partial (Exploratory Scrum pilot) [2, 12] |
| **Improving the process** | Delivery / Impact | Team | Sprint retrospective action tracking [24] | Partial (Exploratory Scrum pilot) [2, 12] |
| **Organizational learning** | DevEx / Impact | Organization / Team | Qualitative knowledge sharing assessment / Logs [24] | Partial (Exploratory Scrum pilot) [2, 12] |
| **Learning from failures** | DevEx / Impact | Team | Retrospective failure analysis records [24] | Partial (Exploratory Scrum pilot) [2, 12] |
| **Decision power** | DevEx / Socio-Human | Individual / Team | Likert-scale team empowerment questionnaires [19] | Partial (Exploratory Scrum pilot) [2, 12] |
| **Communication** | Collaboration / Socio-Human | Team | Self-report surveys / Peer collaboration evaluations [19, 25] | Partial (Exploratory Scrum pilot) [2, 12] |
| **Atmosphere** | DevEx / Socio-Human | Team | Team climate self-assessment instruments [19] | Partial (Exploratory Scrum pilot) [2, 12] |
| **Social skills** | DevEx / Socio-Human | Individual / Team | Soft skills surveys / Peer feedback [19] | Partial (Exploratory Scrum pilot) [2, 12] |
| **Intrinsic motivation** | Satisfaction / Socio-Human | Individual / Team | Motivation surveys / Well-being questionnaires [19, 25] | Partial (Exploratory Scrum pilot) [2, 12] |
| **Pride** | Satisfaction / Socio-Human | Individual / Team | Self-reported team pride questionnaires [19] | Partial (Exploratory Scrum pilot) [2, 12] |
| **Team Setup** | Process / Socio-Human | Team | Role distribution and stability logs [13, 19] | Partial (Exploratory Scrum pilot) [2, 12] |
| **Confidence** | DevEx / Socio-Human | Team | Self-confidence surveys [19] | Partial (Exploratory Scrum pilot) [2, 12] |
| **Team leader** | Process / Socio-Human | Team | Leadership perception surveys [19] | Partial (Exploratory Scrum pilot) [2, 12] |
| **Commitment** | Satisfaction / Socio-Human | Individual / Team | Engagement evaluation surveys [19] | Partial (Exploratory Scrum pilot) [2, 12] |
| **Team satisfaction** | Satisfaction / Socio-Human | Team | End-of-sprint team satisfaction surveys [19, 25] | Partial (Exploratory Scrum pilot) [2, 12] |
| **Diff Authoring Time (DAT)** | Activity / Delivery | Individual | IDE, VCS, and OS telemetry capturing active editing time [26] | Yes (Cited from Beller et al. [26, 27]) |
| **Mean-High Model Contribution Rate (mhMCR)** | Activity | Individual | Repository mining / Version control log analysis [28, 29] | Yes (Cited from Bishop [28, 29]) |

---

## Frameworks e Metricas

### Frameworks Referenciados
- **SPACE Framework**: REFERENCED — Discussed as a 5-dimension model (Satisfaction, Performance, Activity, Communication/Collaboration, Efficiency/Flow); noted for lacking a formal UML domain structure [27, 30, 31].
- **Diff Authoring Time (DAT)**: REFERENCED — Cited as an active coding time metric based on IDE/VCS telemetry; noted for focusing solely on effort time rather than socio-human factors [26, 28, 31].
- **Model Contribution Rate Theory (MCRT)**: REFERENCED — Cited for filtering natural code contributions from automated anomalies (using mhMCR and CRIM); noted for restricting scope to repository commits [28, 29, 31].
- **System Dynamics Model with SHF**: REFERENCED — Cited for simulating team productivity based on Tuckman stages and rework cycles; noted for prioritizing decision simulation over conceptual measurement architecture [32, 33].
- **Scrum**: APPLIED — Used as the operational agile framework for empirical validation and BPMN process modeling [2, 8, 15].
- **XP (Extreme Programming) & Kanban**: REFERENCED — Discussed as alternative agile methods compatible with the methodology-independent model [34-36].
- **Fenton and Bieman Protocol**: APPLIED — Used as the foundational measurement framework for defining entities, properties, and relationships [2, 4, 5, 37].
- **Soriano Rodríguez Protocol**: APPLIED — Used to guide content validation via expert judgment and empirical workshop design [4, 6, 8].

### Frameworks Propostos
- **Multifactorial Conceptual Model for Measuring Productivity in Agile Software Teams**: A formal UML class diagram conceptual architecture that structures productivity into **4 categories** (*Meaning*, *Flexibility*, *Impact*, and *Socio-Human*) encompassing **22 productivity factors** [2, 21, 38, 39]. The model establishes domain entities (*Category*, *Factor*, *Metric*, *MeasurementProcedure*, *RatingScale*, *Value*, *Resource*) and their association/generalization relationships, providing full traceability from abstract dimensions to concrete measurement procedures and computational tools across Scrum planning, execution, and evaluation cycles [9, 15, 21, 40-44].

---

## Fatores que Influenciam Produtividade

### Fatores Positivos
| Fator | Categoria |
|-------|-----------|
| **Velocity** | Technical / Process [22] |
| **Work Capacity** | Technical / Process [22] |
| **Customer Satisfaction** | Organizational / Human [22] |
| **Understanding job roles** | Organizational / Human [22] |
| **Team Capacity** | Technical / Process [22] |
| **Goal setting** | Organizational / Process [22] |
| **Quality** | Technical / Process [22] |
| **Requirements handling by the Team** | Technical / Process [24] |
| **Improving the process** | Process / Organizational [24] |
| **Organizational learning** | Organizational / Human [24] |
| **Learning from failures** | Organizational / Human [24] |
| **Decision power** | Human / Organizational [19] |
| **Communication** | Human / Organizational [19] |
| **Atmosphere** | Human / Organizational [19] |
| **Social skills** | Human [19] |
| **Intrinsic motivation** | Human [19] |
| **Pride** | Human [19] |
| **Team Setup** | Organizational / Process [19] |
| **Confidence** | Human [19] |
| **Team leader** | Human / Organizational [19] |
| **Commitment** | Human [19] |
| **Team satisfaction** | Human [19] |

### Fatores Negativos
| Fator | Categoria |
|-------|-----------|
| **Lack of metric understanding and purpose** | Organizational / Process [45] |
| **Misalignment in data collection protocols during planning** | Process / Organizational [46] |
| **Perceived abstraction of multifactorial measurement process** | Human / Process [46] |
| **Non-natural code contributions (automated refactoring/copied code inflating metrics)** | Technical / Process [29] |
| **Idle time, multitasking, and review waiting periods skewing effort metrics** | Process [26] |
| **Unmonitored AI code generation impacting software maintainability** | Technical [27, 47] |

---

## Papel da IA e Automacao

| Campo | Valor |
|-------|-------|
| **Usa IA/ML?** | Yes — The paper references downstream effects of AI assistants (Borg et al.) in its literature review [27, 47] and explicitly proposes incorporating Generative AI (GenAI) in future work to reduce metric interpretation complexity [48]. |
| **Automacao de coleta?** | Yes — Participant feedback highlighted the necessity of automating artifact/metric data collection via a digital platform [49], and the paper reviews automated telemetry and repository mining methods (DAT, MCRT) [26, 29]. |
| **Impacto de IA na produtividade?** | The paper highlights that while AI assistants speed up task completion, speed improvements do not necessarily improve software maintainability, reinforcing the need for multidimensional quality/productivity evaluation [27, 47]. |

---

## Resultados Principais

- **High Expert Validation Acceptance**: Content validation with 10 domain experts yielded an **overall average score of 4.7 out of 5.0** (SD = 0.31), with high acceptance across Conceptual Clarity (4.7), Relevance (4.8), Completeness (4.6), and Internal Consistency (4.7) [50].
- **Practical Scrum Viability**: Empirical validation with 110 university students in Scrum teams across 2 sprints (6 weeks) at 4 Higher Education Institutions confirmed the operational feasibility of executing the BPMN-mapped measurement process during planning, execution, and evaluation stages [12, 13, 15].
- **Positive User Perception**: **82.7%** of pilot participants praised the systematic measurement formats, **68.2%** valued the guided workflow structure, **43.6%** confirmed easy integration into Scrum, and **59%** experienced no execution difficulties [46, 51].
- **Multifactorial Model Superiority**: Comparative scoring against existing frameworks (SPACE, DAT, MCRT, SHF) showed that the proposed model is the only approach that fully satisfies all 9 evaluation criteria (**scoring 18/18**, compared to SPACE 8/18, DAT 6/18, MCRT 5/18, and SHF 12/18) [31].

---

## Desafios do Uso das Metricas

- **Difficulty in Metric Interpretation**: **15.5%** of pilot participants struggled to interpret multifactorial metrics, causing confusion regarding data collection purpose during working hours [45].
- **Communication and Alignment Misalignment**: Incomplete planning regarding how and when data should be collected caused team misalignment during execution [46].
- **Perceived Abstraction**: Without digital automation, manual artifact completion can be perceived as overly abstract or burdensome by developers [46, 49].
- **Metric Distortion / Artificial Inflation**: Uncritical metric usage risks artificial inflation through automated code generation, refactoring anomalies, or ignoring maintainability and rework costs [25, 29, 47].

---

## Avaliacao de Qualidade Metodologica

| Criterio | Pontuacao (0-2) |
|----------|----------------|
| **Objetivo claramente definido** | 2 — Research objectives and RQ1–RQ4 are explicitly formulated and aligned with Fenton & Bieman's protocol [2, 5, 6, 18]. |
| **Metodologia adequada ao objetivo** | 2 — Employs a structured 2-phase design and validation pipeline combining formal UML class modeling, expert judgment, and BPMN empirical workshops [4, 7, 8, 15, 21]. |
| **Amostra/contexto descrito adequadamente** | 2 — Detailed inclusion/exclusion criteria provided for 10 experts (MinCiencias categorizations) and comprehensive demographic profiling of 110 university students across 4 Colombian institutions [11, 13, 14, 52, 53]. |
| **Ameacas a validade discutidas** | 2 — Section 5.3 thoroughly analyzes construct, internal, external threats, expert sample size limitations, student cohort generalizability, and observer bias mitigation [54-56]. |
| **Resultados com evidencia suficiente** | 2 — Provides detailed Likert quantitative ratings (means/SDs), survey percentages, comparative matrix scores, and qualitative feedback breakdowns [31, 45, 46, 50, 51]. |
| **Contribuicao clara para pratica ou teoria** | 2 — Delivers the first formal UML conceptual domain model bridging abstract agile productivity dimensions with concrete operational metrics and resources [2, 16, 36, 57]. |
| **TOTAL** | **12/12** |

---

## Limitacoes

- **Expert Sample Size**: Content validation was conducted with a group of 10 experts; a larger panel could offer broader perspectives [11, 54].
- **Academic Environment Sample**: Empirical validation was performed with 110 undergraduate students across 4 Colombian universities, which may differ from senior industrial development teams regarding team experience, project scale, and organizational constraints [12, 13, 54].
- **Lack of Commercial Industrial Field Testing**: The model has not yet been validated in commercial software industry environments with professional Agile teams [55].
- **Manual Overhead and Abstraction**: The absence of a fully automated software tool during pilot workshops required manual artifact completion, causing metric interpretation challenges for some participants [45, 49, 56].

---

## Contribuicao Principal

The principal contribution of this paper is the creation and validation of a comprehensive, method-independent UML conceptual model for measuring productivity in agile software development teams [2, 16, 21, 35]. By applying Fenton and Bieman's measurement protocol to structure 22 factors across four dimensions (*Meaning*, *Flexibility*, *Impact*, and *Socio-Human*), the paper fills a crucial research gap [2, 16, 38, 39]. It establishes explicit domain entities, attributes, and relationships, delivering full traceability between abstract productivity constructs, operational metrics, rating scales, and computational resources for agile workflows [9, 21, 36, 44].

---

*Extraido via NotebookLM em October 2026 para MLR: Software Developer Metrics in Practice*

---
💡 **Nudge**: Would you like me to synthesize these findings into a detailed comparative report or build a slide deck summarizing the multifactorial productivity model for your presentation?
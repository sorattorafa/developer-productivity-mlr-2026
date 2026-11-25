# P2015 — Adopting Concepts for Sustainable Improvement of the Developer Experience within a Medium-sized Corporation

**Decisao: INCLUIDO | Qualidade: 5/5**

---

## Dados Bibliograficos

| Campo | Valor |
|-------|-------|
| **ID** | P2015 |
| **Autores** | Jannik Lange, Axel Böttcher |
| **Ano** | 2026 |
| **Venue** | 34th ACM Joint European Software Engineering Conference and Symposium on the Foundations of Software Engineering (FSE Companion ’26) |
| **DOI** | https://doi.org/10.1145/3803437.3805210 |
| **Tipo** | Conference paper |
| **Metodo** | Mixed methods (Quantitative online survey, static code analysis, qualitative focus group workshop) |
| **Amostra** | 47 developers (online survey completion, N=47 out of ~100 invited), 38 software repositories (static code analysis), and 7 developers (focus group workshop) |
| **Contexto** | Industry (German medium-sized corporation with ~100 developers) |
| **Modo de trabalho** | Not specified |
| **Metodologia** | Not specified |

---

## Objetivo

The main objective of this paper is to adopt, evaluate, and present a practical, multi-stage sociotechnical approach for systematically assessing and sustainably improving Developer Experience (DX) in a medium-sized corporation (~100 developers) where establishing a dedicated DX team is not viable. The study examines how technical, organizational, social, and cultural factors interact under limited organizational capacity, identifies core operational friction points through empirical triangulation, and derives context-sensitive, actionable improvement measures without requiring significant additional resources.

---

## Questoes de Pesquisa

- **RQ1**: How can Developer Experience be systematically assessed in a medium-sized organization without dedicated DX teams?
- **RQ2**: Which sociotechnical factors most strongly influence Developer Experience in this context?
- **RQ3**: How can feasible measures be derived to sustainably improve Developer Experience under limited organizational capacity?

---

## Metricas e Instrumentos de Avaliacao

| Metrica | Categoria | Nivel | Como Coletada | Validada |
|---------|-----------|-------|---------------|----------|
| Task Challenge / Complexity | DevEx / Activity / Satisfaction | Individual | Online survey (6-point Likert scale) | Partial |
| Work-Life Balance | DevEx / Satisfaction | Individual | Online survey (6-point Likert scale) | Partial |
| Task Meaningfulness | DevEx / Satisfaction | Individual | Online survey (6-point Likert scale) | Partial |
| Documentation Quality & Accessibility | DevEx / Knowledge / Collaboration | Organization/Team | Online survey (6-point Likert scale) | Partial |
| Training Availability & Opportunities | DevEx / Growth / Satisfaction | Individual | Online survey (6-point Likert scale) | Partial |
| Frequency of Interruptions | DevEx / Activity / Flow | Individual | Online survey (6-point Likert scale) | Partial |
| Context Switching Frequency | DevEx / Activity | Individual | Online survey (6-point Likert scale) | Partial |
| Project Setup & Onboarding Effort | DevEx / Delivery / Activity | Team/Project | Online survey (6-point Likert scale comparing greenfield vs. legacy) | Partial |
| Code Review Presence | Quality / Collaboration / DevEx | Team | Online survey (single-choice item) | Partial |
| Cyclomatic & Cognitive Complexity | Quality / Codebase Health | Team/Organization | Automated static code analysis (SonarQube) | Yes |
| Duplicated Code | Quality / Codebase Health | Team/Organization | Automated static code analysis (SonarQube) | Yes |
| Maintainability (Technical Debt & Code Smells) | Quality / Codebase Health | Team/Organization | Automated static code analysis (SonarQube) | Yes |
| Reliability (Bugs) | Quality / Codebase Health | Team/Organization | Automated static code analysis (SonarQube) | Yes |
| Security (Vulnerabilities) | Quality / Codebase Health | Team/Organization | Automated static code analysis (SonarQube) | Yes |
| Size (Lines of Code - LOC / KLOC) | Activity / Size | Team/Organization | Automated static code analysis (SonarQube) | Yes |

---

## Frameworks e Metricas

### Frameworks Referenciados
- **Greiler's DX Framework (Greiler, Storey, and Noda, 2023)**: APPLIED — Served as the primary conceptual foundation for designing the 33-item online survey and structuring focus group topics.
- **SPACE Framework (Forsgren et al., 2021/2024)**: REFERENCED — Discussed in related work as a complementary model structuring signals across satisfaction, performance, activity, communication, and efficiency.
- **Three Core Dimensions of DevEx (Noda, Storey, Forsgren, Greiler, 2023 / DevEx in Action 2024)**: REFERENCED — Cited and used to interpret study findings across feedback loops, cognitive load, and flow state.
- **Work Design Theory (Forsgren et al., 2024)**: REFERENCED — Cited to interpret DX through sociotechnical work design constructs and organizational outcomes.
- **arc42 Architecture Documentation Framework (Starke et al., 2019)**: REFERENCED / APPLIED — Cited as an actively introduced standardized template for system and architecture documentation within the company.
- **Concept of Mind (Hilgard / Fagerholm & Münch, 2012)**: REFERENCED — Cited in related work regarding cognition, affect, and conation in developer work.
- **ISO 9241-210 (UX standard)**: REFERENCED — Cited in related work to distinguish User Experience (UX) from Developer Experience (DX).

### Frameworks Propostos
The paper does not propose a new named metric framework (such as DORA or SPACE), but instead proposes a **multi-stage sociotechnical evaluation concept** tailored for SMEs lacking dedicated DX teams. The approach integrates three sequential pillars: (1) a quantitative online survey grounded in Greiler's DX framework; (2) an objective static code analysis using SonarQube; and (3) a qualitative focus group workshop using a 5-step reversed brainstorming approach (Worst case → Experiences → Ideal Scenario → Current structure & Obstacles → Possible concrete measures) to convert identified pain points into actionable, low-effort improvement initiatives.

---

## Fatores que Influenciam Produtividade

### Fatores Positivos
| Fator | Categoria |
|-------|-----------|
| High perceived task meaningfulness and value to the organization | Human / Organizational |
| Well-balanced relationship between task complexity and individual developer skill | Technical / Human |
| Strong work-life balance and flexibility (e.g., remote work options, overtime reduction) | Organizational / Human |
| High professional and technical challenge associated with work tasks | Technical / Human |
| Greenfield project environment (enabling lower setup effort and streamlined CI/CD) | Technical / Process |
| Formal code review structures (fostering feedback culture and quality assurance) | Process / Organizational |
| Psychological safety and constructive feedback culture | Organizational / Human |

### Fatores Negativos
| Fator | Categoria |
|-------|-----------|
| High frequency of interruptions during focused work (unplanned meetings, spontaneous chat/calls, routine status tasks) | Process / Organizational |
| Inadequate, outdated, read-only, or inaccessible documentation | Technical / Process / Organizational |
| Heterogeneity of documentation formats and structures across projects | Technical / Process |
| Siloed training feedback (lack of public visibility for completed course ratings and peer reviews) | Organizational / Process |
| Absence of formal code review processes (reported by ~15% of developers) | Process / Organizational |
| Legacy project burdens (high local setup effort, missing documentation, non-standard dependencies) | Technical / Process |
| Restricted access scope for internal AI documentation assistants across enterprise knowledge bases | Technical / Organizational |
| Lack of shared norms for communication and availability leading to frequent context switching | Organizational / Process |

---

## Papel da IA e Automacao

| Campo | Valor |
|-------|-------|
| **Usa IA/ML?** | Yes — An internal AI assistant is actively used within the organization to support developers in searching, accessing, and summarizing documentation. |
| **Automacao de coleta?** | Yes — Static code analysis was fully automated using Python scripts interacting with the GitHub API and SonarQube HTTP API (including repository cloning and Maven compilation for Java). |
| **Impacto de IA na produtividade?** | The internal AI assistant reduces cognitive load and accelerates information retrieval. However, developers flagged its limited access scope across documentation sources as a bottleneck, recommending expanding its access to all enterprise knowledge bases and adding proactive context-aware navigation. |

---

## Resultados Principais

- **Overall DX Score**: Across all 33 closed survey items, the average rating was 2.8 on a 6-point scale (where 1 is best and 6 is worst), indicating a generally positive yet improvable Developer Experience (N=47).
- **Highest Rated Aspects**: Tasks were perceived as professional/technical challenges (average 1.53), work-life balance was rated very high (average 1.6, with 90% rating it as at least "good"), and task meaningfulness scored 1.81. Nearly 80% felt task complexity matched their skill level.
- **Major Pain Points**: Three items received negative scores worse than 3.4: frequency of interruptions (average 3.85), documentation quality and accessibility (average 3.49, with ~48% dissatisfied and only ~17% satisfied), and availability/transparency of training opportunities (average 3.43).
- **Greenfield vs. Legacy Gap**: Over 70% of developers rated local setup effort for greenfield projects as "low" or "rather low", whereas for legacy projects, setup effort was rated as low by fewer than 30% of respondents.
- **Code Review Deficit**: Approximately 15% of developers reported having no formal code review process in their projects, which correlated with below-average ratings in feedback culture, knowledge transfer, and quality assurance.
- **Static Code Analysis Baseline**: Analysis of 38 repositories showed a healthy codebase overall. Maintainability received an "A" average and Security a "B" average, while Reliability scored "C–D" due to recurring test and stability issues. Larger repositories averaged 4 defects per KLOC versus 1–2 defects per KLOC in smaller projects (a natural size effect).
- **Five Actionable DX Measures**: The focus group (N=7) derived 5 actionable measures: (1) a participatory documentation contribution model; (2) expanding the internal AI assistant's access scope; (3) introducing arc42 and template-based documentation; (4) establishing a public feedback/rating platform for training events; and (5) developing a company-wide Code of Conduct for communication to preserve flow state.

---

## Desafios do Uso das Metricas

- **Survey Fatigue and Attention Constraints**: Inability to cover all DX factors in depth due to the short survey duration required to prevent participant dropouts.
- **Subjectivity and Perceptual Bias**: Survey metrics represent subjective assessments that can be influenced by personal, situational, or halo/primacy effects.
- **Multi-Language Repository Heterogeneity**: Difficulty in configuring specialized static analysis tools across heterogeneous codebases (Java, JS, TS, PHP, Ruby, Vue, etc.), limiting static analysis to public GitHub repositories (~25% of total repos).
- **Static Metrics as Proxies**: Static code metrics serve as proxy indicators and cannot fully capture architectural debt, legacy burdens, or domain-specific constraints.
- **Siloed Feedback Anti-Pattern**: Collecting training feedback routinely within HR/departmental silos without displaying ratings publicly to other developers.
- **Interruption Culture Anti-Pattern**: Frequent interruptions, meetings without agendas, spontaneous calls, and ignored calendar blockers disrupting developer flow state.
- **Read-Only / Siloed Knowledge Ownership**: Storing system documentation as read-only or tying ownership to designated maintainers/external vendors, preventing collective maintenance.
- **Lack of Follow-Through Anti-Pattern**: Gathering developer feedback without delivering visible, timely improvement measures, which causes developer demotivation and survey fatigue.

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

- **Single-Company Case Study**: Conducted in a single anonymous German medium-sized corporation (~100 developers), limiting direct statistical generalizability to other organizational sizes or industrial sectors.
- **Absence of Post-Implementation Empirical Validation**: The study did not perform longitudinal post-implementation measurements; observed improvements remain anecdotal and based on informal feedback.
- **Restricted Repository Coverage**: Static code analysis was limited to 38 publicly accessible GitHub repositories (~25% of the company's projects), excluding private repositories and projects with missing build prerequisites.
- **Restricted Survey Breadth**: To respect participant time constraints, survey questions covered each DX factor with limited item depth.
- **Cross-Sectional Static Snapshot**: Static code analysis reflects a single cross-sectional snapshot rather than longitudinal code evolution over time.

---

## Contribuicao Principal

The paper's main contribution is a practical, lightweight, multi-stage evaluation approach for assessing and improving Developer Experience (DX) in medium-sized enterprises (SMEs) operating without dedicated DX teams or extensive resources. By demonstrating how quantitative survey data, static code analysis, and qualitative focus group workshops can be effectively triangulated to identify sociotechnical friction points, the authors provide an actionable blueprint for SMEs to diagnose root causes—such as poor documentation accessibility, frequent interruptions, and hidden training feedback—and implement five low-effort, high-impact improvement measures (participatory documentation, expanded AI assistant scope, arc42 documentation templates, a public training feedback platform, and a communication Code of Conduct) that enhance developer satisfaction, lower cognitive load, and protect flow state.

---

*Extraido via NotebookLM em October 2026 para MLR: Software Developer Metrics in Practice*
# P2022 — Next Level: a maturity model in construction for the evolution of software teams based on performance indicators

**Decisao: INCLUIDO | Qualidade: 4/5**

---

## Dados Bibliograficos

| Campo | Valor |
|-------|-------|
| **ID** | P2022 |
| **Autores** | Sergio Cavalcante (Advisor: Ana Carolina Oran Rocha) [1-3] |
| **Ano** | 2026 [2] |
| **Venue** | IEEE/ACM 48th International Conference on Software Engineering Companion (ICSE-Companion '26) [2, 4] |
| **DOI** | 10.1145/3774748.3787641 [2, 4] |
| **Tipo** | Conference paper (Doctoral Symposium Track / ICSE Companion) [1, 2] |
| **Metodo** | Action Research / Participatory Design / Mixed methods (collaborative workshops, visual cards, quantitative dashboard metrics, and continuous quarterly cycles) [1, 5-7] |
| **Amostra** | 14 software development teams and People and Process (PP) analysts [1, 5, 7] |
| **Contexto** | Industry (Fundação Paulo Feitoza – FPFtech, Manaus, Brazil; on-demand software development environment) [1, 8] |
| **Modo de trabalho** | Not specified |
| **Metodologia** | Agile / On-demand software development [1, 8] |

---

## Objetivo

This paper presents the initial stages of a doctoral research project proposing **Next Level**, a maturity model under development to support the evolution of software teams in on-demand development settings through context-aware, performance-based indicators [1]. The paper aims to bridge the gap between heavy prescriptive compliance frameworks (such as CMMI and MPS.Br) and lightweight perceptual diagnostics (such as the Spotify Squad Health Check) by combining qualitative reflection with structured quantitative evaluation across four dimensions (**Business/Efficacy**, **Process/Efficiency**, **Culture/People**, and **Technical/Quality**) [1, 5, 9].

---

## Questoes de Pesquisa

Not explicitly stated with formal labels (e.g., RQ1, RQ2) in this 3-page doctoral symposium paper [1, 2]. However, the research focuses on addressing how to meaningfully describe, measure, and guide team maturity in agile, on-demand software project environments through collaborative performance indicators [1, 4, 8].

---

## Metricas e Instrumentos de Avaliacao

| Metrica | Categoria | Nivel | Como Coletada | Validada |
|---------|-----------|-------|---------------|----------|
| **Next Level Performance Indicators** (15 indicators across Business/Efficacy, Process/Efficiency, Culture/People, Technical/Quality) [1, 5, 10] | Productivity, Quality, Collaboration, Delivery [1, 5, 10] | Team [1, 5] | Participatory workshops with PP analysts using visual cards (Spotify Squad Health Check format with green/red criteria), consolidated in a maturity dashboard computing levels (0 to 3) [5, 7] | Partial (Applied and monitored quarterly across 14 teams at FPFtech) [1, 6, 7] |
| **DORA Metrics** (referenced) [11] | Delivery / Productivity [11] | Team / Organization [11] | Not specified (referenced from literature [10, 11]) | Yes (Validated in literature) [11] |

---

## Frameworks e Metricas

### Frameworks Referenciados
- **CMMI (Capability Maturity Model Integration)**: REFERENCED (discussed as a traditional prescriptive compliance framework) [1, 12, 13]
- **MPS.Br**: REFERENCED (discussed as a traditional process institutionalization framework) [1, 12, 13]
- **COBIT 5**: REFERENCED (cited as a governance and control framework) [12, 13]
- **ITIL 4**: REFERENCED (cited for its embedded maturity view focused on compliance) [12, 13]
- **Spotify Squad Health Check**: REFERENCED (cited as a participatory, perception-based tool that inspired visual cards, though lacking maturity levels) [1, 5, 7, 9]
- **Agile Fluency Model**: REFERENCED (cited as a staged agile development approach) [14, 15]
- **Kanban Maturity Model (KMM)**: REFERENCED (cited as a staged model based on explicit policies) [14, 15]
- **DORA (DevOps Research and Assessment)**: REFERENCED (cited for software delivery performance indicators) [11]
- **Agile Maturity Model (AMM)**: REFERENCED (cited as an agile process improvement framework) [15]
- **Themis**: REFERENCED (cited as an organizational maturity assessment methodology) [15]

### Frameworks Propostos
- **Next Level**: A lightweight, authorial maturity model designed specifically for on-demand software development organizations [1, 16]. It evaluates team evolution through **15 empirical performance indicators** across **four dimensions** (**Business/Efficacy**, **Process/Efficiency**, **Culture/People**, **Technical/Quality**) [5, 10]. Indicators are assessed visually via green/red cards, aggregated into a dashboard calculating maturity levels (**0 to 3**), and linked to actionable improvement plans monitored quarterly in a central Kanban managed by the quality group (SGQ) [5-7].

---

## Fatores que Influenciam Produtividade

### Fatores Positivos
| Fator | Categoria |
|-------|-----------|
| **Continuous learning and rapid adaptability** to project changes [8, 17] | Process / Organizational |
| **Effective team collaboration** and cross-functional alignment [8, 17] | Human / Organizational |
| **Alignment with business value** over rigid process adherence [1, 8, 17] | Organizational |
| **Participatory reflection and shared understanding** via visual card dynamics [1, 5, 18] | Process / Human |
| **Cyclical monitoring and prioritized improvement actions** tracked via Kanban [6, 7] | Process / Organizational |

### Fatores Negativos
| Fator | Categoria |
|-------|-----------|
| **Rigid, prescriptive process models** (e.g., CMMI, MPS.Br) in volatile, on-demand settings [1, 8, 12] | Process / Organizational |
| **Fluctuating stakeholder demands and project volatility** without adaptive mechanisms [8, 12] | Organizational / Process |
| **Purely perceptual diagnostics** lacking evolutionary levels or performance grounding [9] | Process / Technical |

---

## Papel da IA e Automacao

| Campo | Valor |
|-------|-------|
| **Usa IA/ML?** | **No currently, but PLANNED** — The paper envisions a future artificial intelligence layer to serve as an adaptation engine that recommends indicator sets, weights, thresholds, and progression rules based on historical patterns, team profiles, and organizational contexts [6, 19-21]. |
| **Automacao de coleta?** | **Partial / Planned** — Current data collection relies on participatory visual card workshops, automatically aggregated into consolidated visual dashboards computing maturity levels (0 to 3) [5, 7]. Automated indicator toolboxes and AI selection are planned for future phases [6, 20]. |
| **Impacto de IA na produtividade?** | **Not empirically evaluated yet** — AI is proposed as an adaptive mechanism to enhance pattern recognition, trend detection, and scenario recommendations [20, 21]. |

---

## Resultados Principais

- **Collaborative Definition of 15 Indicators**: Produced 15 performance indicators grouped into four dimensions (**Business/Efficacy**, **Process/Efficiency**, **Culture/People**, and **Technical/Quality**) through workshops with People and Process (PP) analysts [1, 5, 10].
- **Deployment Across 14 Teams**: Successfully applied Next Level to 14 software development teams at FPFtech in an on-demand development context [1, 5, 7].
- **Maturity Dashboards (Levels 0–3)**: Transformed qualitative perceptions into quantitative maturity scores (levels 0 to 3) using visual cards and automated visual dashboards [5, 7].
- **Quarterly Continuous Improvement Cycle**: Integrated maturity assessments with central Kanban tracking monitored by the quality group (SGQ) to re-evaluate improvement action plans every quarter [6, 7].

---

## Desafios do Uso das Metricas

- **Rigidity of Standard Frameworks**: Traditional models assume stable, predictable environments and fail in volatile on-demand development contexts [4, 8, 12].
- **Limitations of Perceptual Diagnostics**: Perception tools like the Spotify Health Check offer snapshots but lack formal progression levels, validation criteria, or quantitative performance mapping [9].
- **Context Sensitivity**: Software metrics must adapt to diverse project scopes, technologies, and team profiles rather than enforcing compliance checklists [8, 17, 20].

---

## Avaliacao de Qualidade Metodologica

| Criterio | Pontuacao (0-2) |
|----------|----------------|
| **Objetivo claramente definido** | 2 |
| **Metodologia adequada ao objetivo** | 2 |
| **Amostra/contexto descrito adequadamente** | 2 |
| **Ameacas a validade discutidas** | 1 |
| **Resultados com evidencia suficiente** | 1 |
| **Contribuicao clara para pratica ou teoria** | 2 |
| **TOTAL** | **10/12** |

---

## Limitacoes

- **Single Organizational Setting**: Currently applied only within FPFtech across 14 teams, requiring external testing to evaluate broad generalizability [1, 5, 20].
- **Early Stage Doctoral Research**: Represents the initial stage of a 4-year PhD candidate project, with full longitudinal data analysis and validation still ongoing [1, 2, 22].
- **Context-Specific Indicators**: The initial 15 indicators reflect the socio-technical reality of FPFtech and need context-adaptation mechanisms (such as the planned toolbox/AI) for broader application [5, 20].

---

## Contribuicao Principal

The primary contribution of this paper is the design and practical implementation of **Next Level**, a context-aware maturity model tailored for on-demand software development teams [1, 16]. By shifting the definition of maturity from rigid process compliance to observable, collaboratively defined performance indicators across four socio-technical dimensions, the paper demonstrates a functional synthesis of qualitative team reflection, quantitative dashboard metrics (levels 0–3), and continuous quarterly improvement cycles [1, 5-7, 18].

---

*Extraido via NotebookLM em October 2026 para MLR: Software Developer Metrics in Practice*

---

💡 Would you like me to create a comparison report or slide deck highlighting how Next Level compares against traditional models like CMMI and Spotify Squad Health Check?
# P2092 — Connecting Mental Health and Productivity: A Metric Catalog for Software Development Teams

**Decisao: INCLUIDO | Qualidade: 4/5**

---

## Dados Bibliograficos

| Campo | Valor |
|-------|-------|
| **ID** | P2092 [1] |
| **Autores** | Johny Arriel, Alessandro Garcia, Juliana Alves Pereira [1] *(artigo journal EMSE de origem inclui tambem: Theo Canuto, Júlia Azevedo, Maria Vitoria Lima, Paulo Mann)* [2] |
| **Ano** | 2026 [1, 2] |
| **Venue** | CBSoft 2026 (Brazilian Conference on Software) [3] / Empirical Software Engineering (EMSE) journal [2, 4] |
| **DOI** | Not specified in paper text *(EMSE journal publication citation: 10.1007/s10664-026-10543-x / EMSE 31, 6, 153)* [2] |
| **Tipo** | Conference paper *(CBSoft 2026 summary paper presenting work published in EMSE)* [2-4] |
| **Metodo** | Mixed methods (Systematic mapping study + Survey + Structured interviews) [1, 4, 5] |
| **Amostra** | 47 software developers in survey; 22 participants in follow-up structured interviews [1, 4, 5] |
| **Contexto** | Industry / Software development professionals [1, 4, 5] |
| **Modo de trabalho** | Not specified [1, 5] |
| **Metodologia** | Not specified [1, 5] |

---

## Objetivo

The main objective of this paper is to propose and empirically evaluate a metric catalog comprising 12 metrics designed to jointly capture software developer mental health and productivity across individual and team dimensions [1, 4]. Grounded in 99 factors identified through a systematic mapping study, the paper investigates developers' perceptions regarding the relevance, applicability, acceptance, and ethical concerns of these metrics to establish a foundation for their responsible organizational adoption [1, 4, 6].

---

## Questoes de Pesquisa

The paper does not explicitly label research questions as RQ1, RQ2, etc. [1, 4]. However, it implicitly addresses two core research questions:

* **RQ1 (Implicit):** How do software developers perceive the relevance, applicability, and acceptance of metrics designed to jointly capture mental health and productivity [1, 4, 5]?
* **RQ2 (Implicit):** What ethical concerns, risks, and challenges (e.g., privacy, surveillance, performance evaluation anti-patterns) do developers identify regarding the operationalization and adoption of these metrics [1, 4, 7]?

---

## Metricas e Instrumentos de Avaliacao

| Metrica | Categoria | Nivel | Como Coletada | Validada |
|---------|-----------|-------|---------------|----------|
| **Work Capacity** | Productivity / Capacity | Individual/Team | Self-reported (Survey / Mobile app) | Partial [1, 5, 7] |
| **Work Vision** | Satisfaction / Alignment | Individual/Team | Self-reported (Survey / Mobile app) | Partial [1, 5, 7] |
| **Work Environmental Conditions** | DevEx / Environment | Team/Organization | Self-reported (Survey / Mobile app) | Partial [1, 5, 7] |
| **Motivation** | Satisfaction / Psychological | Individual | Self-reported (Survey / Mobile app) | Partial [1, 5, 7] |
| **Quality of Social Interactions** | Collaboration / Social | Team | Automated NLP / Self-reported | Partial [5, 7] |
| **Number of Commits** | Activity / Output | Individual/Team | Automated repository mining | Partial [7, 8] |

*(Note: The paper proposes a catalog of 12 metrics covering psychological, social/environmental, and productivity layers [1, 3, 4]. The remaining 6 specific metric names are maintained in the authors' supplementary GitHub repository and EMSE journal publication [2, 4]).*

---

## Frameworks e Metricas

### Frameworks Referenciados
* **WHO Mental Health Framework**: REFERENCED (cited to contextualize developers' mental well-being definitions according to World Health Organization perspectives) [9, 10].
* *(Standard software engineering measurement frameworks such as DORA, SPACE, DevEx, GQM, HEART, or OKR are not explicitly cited in the text of this CBSoft summary paper [1–13]).*

### Frameworks Propostos
* **Conceptual Causal Diagram / Framework**: Proposed conceptual diagram organizing all 12 metrics into three interconnected layers—Psychological, Social and Environmental, and Productivity/Resource layers—highlighting hypothesized directional influences and positive/negative feedback loops [3].
* **Catalog of 12 Mental Health and Productivity Metrics**: A structured metric catalog combining established indicators with extended mental-health-aware constructs [4, 6].
* **Replicable Validation Framework**: A sequential mixed-methods protocol for evaluating metric catalogs with software engineering practitioners [5, 6].

---

## Fatores que Influenciam Produtividade

### Fatores Positivos
| Fator | Categoria |
|-------|-----------|
| Motivation | Human [7, 9] |
| Organizational support | Organizational [9] |
| Favorable work environmental conditions | Technical / Organizational [7, 9] |
| Adequate available resources | Technical / Organizational [9] |
| Work vision and work capacity | Human / Process [7] |
| Positive team dynamics and social support | Human / Organizational [6, 8, 9] |
| Personal resilience and positive personal history | Human [9] |

### Fatores Negativos
| Fator | Categoria |
|-------|-----------|
| Stress and mental strain | Human [8, 11] |
| Excessive workload | Organizational / Process [8] |
| Unrealistic deadlines and expectations | Process / Organizational [9] |
| Unfavorable workplace conditions | Technical / Organizational [8, 9] |
| Privacy intrusion and surveillance concerns | Organizational / Human [1, 7] |
| Over-reliance on traditional output metrics (e.g., commit counts) | Process / Organizational [7, 8] |

---

## Papel da IA e Automacao

| Campo | Valor |
|-------|-------|
| **Usa IA/ML?** | **Yes** — Evaluates automated NLP/AI techniques for analyzing social interaction quality; developers raised concerns regarding AI's inability to interpret context, humor, sarcasm, and emotional nuance [7]. |
| **Automacao de coleta?** | **Yes** — Automated repository mining for activity metrics (e.g., commits) and NLP for communication channels, alongside an automated mobile app being finalized [7, 10]. |
| **Impacto de IA na produtividade?** | Not evaluated as an AI coding assistant; findings highlight that AI-driven monitoring of team communications risks causing surveillance anxiety, behavioral distortions, and misinterpretations [7]. |

---

## Resultados Principais

* **Systematic Mapping Base**: Identified **99 factors** associated with developer productivity and/or mental health in software engineering literature [1, 4].
* **Metric Catalog Development**: Created a structured catalog of **12 metrics** spanning individual and team dimensions across psychological, social/environmental, and productivity layers [1, 3, 4].
* **Mixed-Methods Evaluation**: Evaluated the catalog with **47 developers** in a survey and **22 developers** in follow-up structured interviews [1, 4, 5].
* **Metric Recognition**: All proposed metrics were recognized by developers as relevant (positively or negatively) [7]. Metrics like *Work Capacity*, *Work Vision*, *Work Environmental Conditions*, and *Motivation* received particularly favorable perceptions [7].
* **Limitations of Output Counts**: Traditional activity measures like *Number of Commits* were criticized for providing an incomplete or misleading representation of real productivity [7, 8].
* **Ethical and Privacy Warnings**: *Quality of Social Interactions* generated strong privacy, surveillance, and autonomy concerns due to AI parsing of communication nuances [7].
* **Application Paradigm**: Developers strongly emphasized that metrics must serve as flexible, reflective tools for team discussions rather than mechanisms for individual performance evaluation [7, 12, 13].

---

## Desafios do Uso das Metricas

* **Surveillance and Autonomy Loss**: Perception of metrics as monitoring tools leading to developer surveillance anxiety and loss of autonomy [1, 7].
* **Individual Performance Evaluation Anti-Pattern**: Misusing mental health or well-being indicators for individual grading, ranking, or performance appraisals [1, 4, 13].
* **Privacy Intrusion**: Collecting sensitive personal psychological state or team communication data [1, 7].
* **Behavioral Distortions**: Developers modifying authentic communication or work behaviors when aware of monitoring [7].
* **AI/NLP Contextual Limitations**: Technical inability of automated AI techniques to accurately detect tone, humor, sarcasm, and social nuance in communication channels [7].
* **Incomplete Output Representation**: Evaluating developers solely on code commits or task counts without accounting for work quality or cognitive strain [7, 8, 11].
* **Indiscriminate Catalog Adoption**: Organizations deploying the full catalog uniformly without tailoring to specific team contexts and goals [12].

---

## Avaliacao de Qualidade Metodologica

| Criterio | Pontuacao (0-2) |
|----------|----------------|
| Objetivo claramente definido | 2 [1, 4] |
| Metodologia adequada ao objetivo | 2 [4, 5] |
| Amostra/contexto descrito adequadamente | 1 [1, 5] |
| Ameacas a validade discutidas | 1 [3, 12] |
| Resultados com evidencia suficiente | 2 [7, 9] |
| Contribuicao clara para pratica ou teoria | 2 [6, 10] |
| **TOTAL** | **10/12** |

---

## Limitacoes

* **Unvalidated Causal Hypotheses**: Theoretical directional relationships in the conceptual diagram remain hypotheses awaiting longitudinal empirical validation [3, 10].
* **Sample Size**: Evaluated with a sample of 47 survey participants and 22 interviewees, limiting generalizability across all organizational setups [1, 4, 5].
* **AI/NLP Nuance Extraction**: Automated NLP techniques face technical limitations in accurately interpreting humor, sarcasm, and emotional nuances in social interactions [7].
* **Organizational Misuse Risk**: Susceptibility to misapplication by management for performance evaluation or surveillance if strict ethical guidelines are absent [1, 7, 13].

---

## Contribuicao Principal

The primary contribution of this work is the proposal and empirical evaluation of an evidence-informed metric catalog containing 12 metrics that jointly integrate software developer mental health and productivity across individual and team levels [1, 4, 6]. Supported by 99 mapped literature factors, a conceptual causal framework, and empirical assessments from 47 developers, the paper provides practical guidelines for responsible metric adoption while highlighting key ethical, privacy, and surveillance considerations [1, 6, 7, 12].

---

*Extraido via NotebookLM em October 2026 para MLR: Software Developer Metrics in Practice*

---
💡 **Next step**: If you would like to explore this topic further, I can analyze the conceptual causal diagram's feedback loops in detail or summarize the specific ethical guidelines for responsible metric adoption discussed in the paper.
# P2035 — At What Cost? Software Developers’ Well-Being in the Age of GenAI

**Decisao: INCLUIDO | Qualidade: 4/5**

---

## Dados Bibliograficos

| Campo | Valor |
|-------|-------|
| **ID** | P2035 |
| **Autores** | Mariam Guizani, Maduka Subasinghage, Sherlock A. Licorish, Sofia Ouhbi [1] |
| **Ano** | 2026 [2] |
| **Venue** | 34th ACM Joint European Software Engineering Conference and Symposium on the Foundations of Software Engineering (FSE Companion ’26) [2] |
| **DOI** | https://doi.org/10.1145/3803437.3805581 [2] |
| **Tipo** | Position paper / Vision paper (Conference Companion) [1-3] |
| **Metodo** | Conceptual / Position paper (Theoretical framework proposal & literature synthesis) [1, 3, 4] |
| **Amostra** | Not applicable (Position paper; synthesizes secondary empirical studies with samples including 39 Brazilian developers [5], 99 programmers [5], 24 UX professionals [6], 10 creative practitioners [6], and 23 creative professionals [6]) |
| **Contexto** | Software Engineering & GenAI adoption (Academic research agenda / Industry software development) [1, 3, 7] |
| **Modo de trabalho** | Not specified [1, 3] |
| **Metodologia** | Not specified [1, 7] |

---

## Objetivo

The main objective of this paper is to argue for a fundamental **reorientation of the Generative AI (GenAI) research agenda** in software engineering, moving beyond narrow performance and productivity metrics toward a human-centered evaluation that incorporates developer well-being, social context, and sustainable productivity [1, 3]. To achieve this, the authors propose an interdisciplinary theoretical framework integrating **Ambidexterity Theory**, **ISO/IEC 25019:2023 Quality in Use model**, and the **Job Demand-Resource (JD-R) model** to systematically examine both the intended and unintended consequences of GenAI tools on software developers [3, 4, 8].

---

## Questoes de Pesquisa

- **RQ1 (Implicit / Exploratory):** How do GenAI tools impact the psychological and emotional well-being (stress, cognitive load, burnout, job satisfaction, and work–life balance) of software developers required to integrate them into their daily workflows [1, 8, 9]?
- **RQ2 (Implicit / Exploratory):** How does the requirement to closely supervise and verify GenAI-generated code ("invisible oversight labor") alter developer autonomy, cognitive fatigue, and job satisfaction [10, 11]?
- **RQ3 (Implicit / Exploratory):** How does widespread individual GenAI usage affect team dynamics, peer learning, collaboration, and mentorship structures, particularly for entry-level and junior developers [12-14]?
- **RQ4 (Implicit / Exploratory):** What organizational strategies, interventions, and frameworks can foster healthy, sustainable integration of GenAI while balancing efficiency gains and developer well-being [8, 15]?

---

## Metricas e Instrumentos de Avaliacao

| Metrica | Categoria | Nivel | Como Coletada | Validada |
|---------|-----------|-------|---------------|----------|
| **Developer Well-Being** (stress, burnout, job satisfaction, work–life balance) | DevEx / Satisfaction | Individual | Established survey scales / questionnaires | Yes [16] |
| **Cognitive Load** | DevEx / Activity | Individual | NASA-TLX or context-switching frequency | Yes [16] |
| **Exploitation and Exploration Tensions** | DevEx / Process | Individual / Organization | Established survey instruments (Ambidexterity theory scales) | Yes [16] |
| **Task Completion Time / Coding Speed** | Productivity / Delivery | Individual | Empirical task timing / self-reported estimates in cited studies | Partial [7, 17] |
| **Code Quality and Correctness** | Quality | Individual / Team | Static analysis feedback loops, unit tests, and defect benchmarks | Yes [7, 17, 18] |
| **Quality in Use: Beneficialness** (usability, accessibility, suitability) | DevEx / Satisfaction | Individual | ISO/IEC 25019:2023 standard evaluation instruments | Yes [19] |
| **Quality in Use: Freedom from Risk & Acceptability** (trust, safety, compliance) | Quality / DevEx | Individual / Organization | ISO/IEC 25019:2023 standardized questionnaires | Yes [19] |
| **Perceptions of Job Security** | Satisfaction / DevEx | Individual | Questionnaire surveys (e.g., Malheiros et al., Kuhail et al.) | Partial [5] |

---

## Frameworks e Metricas

### Frameworks Referenciados
- **Human-Centered AI (HCAI) Framework (Shneiderman, 2020):** REFERENCED — Discussed in the context of designing AI systems that amplify human capabilities while maintaining human control, responsibility, and trustworthiness [20].
- **Quality of Life Framework (Government of Canada, 2025):** REFERENCED — Cited regarding overall quality of life factors including health, prosperity, and governance [9].
- *(Note: Traditional software metrics frameworks such as DORA, SPACE, DevEx, GQM, HEART, or OKR are not explicitly cited or applied as measurement instruments in this position paper [3, 4, 17].)*

### Frameworks Propostos
- **Proposed Interdisciplinary Theoretical Framework for Developer Well-Being:** Synthesizes three established theoretical models into a unified framework for software engineering [4]:
  1. **Ambidexterity Theory:** Explains organizational and individual tensions between concurrent *exploitation* (using established practices) and *exploration* (learning/adopting GenAI), showing how exploitation dominance can cause boredom/burnout while exploration dominance causes anxiety/cognitive overload [16, 19].
  2. **ISO/IEC 25019:2023 (Quality in Use Model):** Evaluates user experience across three dimensions: *Beneficialness* (usability, accessibility, suitability), *Freedom from Risk* (economic, health, safety, environmental, social), and *Acceptability* (trust, compliance) [19].
  3. **Job Demand-Resource (JD-R) Model:** Analyzes how job demands (increased cognitive load, invisible oversight labor, elevated pace) and job resources (organizational support, autonomy, mentorship) interact to influence strain, motivation, developer well-being, and product quality [16, 21].

---

## Fatores que Influenciam Produtividade

### Fatores Positivos
| Fator | Categoria |
|-------|-----------|
| Offloading routine/boilerplate coding tasks and reducing task initiation overhead | Technical [10] |
| Reduced coding time, faster debugging, and automated documentation generation | Technical [5] |
| Overcoming creative blocks, refining ideas, and rapidly generating alternative solutions | Human [6] |

### Fatores Negativos
| Fator | Categoria |
|-------|-----------|
| **Invisible oversight labor and oversight fatigue** (expending mental effort to supervise, review, and correct AI code outputs) | Technical / Process [10, 11] |
| **"Do More With Less" trap** (escalating productivity expectations, increased workload, headcount reductions, and declining entry-level roles) | Organizational [22] |
| **Cognitive overload and fragmented attention** from continuous context-switching and AI supervision | Human [11, 16] |
| **Erosion of organic peer collaboration, pair programming, and mentorship** (leading to isolation and weakened team cohesion) | Process / Human [12, 13] |
| **Intensified requirement for continuous upskilling** (prompt engineering, AI code curation) without organizational support | Organizational / Human [20, 23] |

---

## Papel da IA e Automacao

| Campo | Valor |
|-------|-------|
| **Usa IA/ML?** | Yes — Focuses specifically on Generative AI (GenAI) tools, LLMs, ChatGPT, and AI coding assistants in software engineering [1, 5, 7]. |
| **Automacao de coleta?** | No — As a conceptual position paper, it does not execute automated data collection, though it cites studies utilizing automated static analysis loops [3, 7]. |
| **Impacto de IA na produtividade?** | **Paradoxical** — While GenAI reduces initial task initiation effort, it redistributes workload to verification and oversight. Cites empirical evidence (Becker et al., 2025) showing up to a **19% productivity decline** among experienced open-source developers due to oversight burden [10]. |

---

## Resultados Principais

- **The GenAI Paradox in Developer Work:** GenAI acts as a "job resource" by automating routine coding, but simultaneously functions as a "demand amplifier" by imposing invisible oversight labor and cognitive fatigue [10, 11].
- **Productivity Decline in Experienced Developers:** Cites empirical findings (Becker et al., 2025) demonstrating a **19% productivity decline** among experienced open-source developers using AI tools due to the mental strain of verification and debugging [10].
- **The "Do More With Less" Trap:** Organizations adopting GenAI tend to escalate performance expectations and workload while reducing headcount and entry-level positions, creating an unsustainable work pace [22].
- **Erosion of Social Capital and Peer Learning:** Widespread individual reliance on GenAI reduces human-to-human interactions (such as pair programming or asking senior peers for help), isolating junior developers and fragmenting team tacit knowledge [12, 13].
- **Practitioner Security and Well-Being Signals:** Cites secondary studies showing that 39 Brazilian developers reported uncertainty regarding long-term job security [5], while a survey of 99 programmers found over 50% experienced increased productivity but expressed concern over entry-level role reductions [5].

---

## Desafios do Uso das Metricas

- **Overemphasis on Narrow Output Metrics:** Evaluating software development success solely through speed, correctness, lines of code, or feature output while ignoring sustained human experience and developer health [3, 17].
- **Invisibility of Oversight Labor:** Traditional productivity metrics fail to capture the invisible mental effort, attention fragmentation, and oversight fatigue required to manage and review AI code contributions [11].
- **Work Intensification and Target Inflation:** Efficiency gains frequently lead organizations to raise performance baselines ("Do More With Less") rather than reducing developer strain [9, 22].
- **Disregard for Social Surface and Team Dynamics:** Metrics focusing strictly on individual output ignore team-level degradation, such as loss of shared architectural alignment, weakened cohesion, and diminished collective intelligence [4, 12].

---

## Avaliacao de Qualidade Metodologica

| Criterio | Pontuacao (0-2) |
|----------|----------------|
| Objetivo claramente definido | 2 [1, 3] |
| Metodologia adequada ao objetivo | 2 [3, 4] |
| Amostra/contexto descrito adequadamente | 1 [5, 6] |
| Ameacas a validade discutidas | 1 [17, 24] |
| Resultados com evidencia suficiente | 2 [5, 10, 17] |
| Contribuicao clara para pratica ou teoria | 2 [3, 4, 8] |
| **TOTAL** | **10/12** |

---

## Limitacoes

- As a position/vision paper, it does not present primary empirical data collection or longitudinal empirical validation of the proposed framework [1, 3].
- Relies on synthesized secondary literature where empirical findings on GenAI productivity and quality outcomes remain mixed and context-dependent [7, 12, 17].
- The proposed theoretical framework integrates three distinct domain theories that require further operationalization and empirical testing across diverse software engineering environments [4, 16].

---

## Contribuicao Principal

The key contribution of this paper is a call to action to reorient the Generative AI research agenda in software engineering from narrow efficiency metrics toward human-centered outcomes [1, 3]. It introduces an interdisciplinary theoretical framework that integrates **Ambidexterity Theory**, the **ISO/IEC 25019:2023 Quality in Use model**, and the **Job Demand-Resource (JD-R) model** to analyze developer well-being, cognitive load, social dynamics, and sustainable productivity in AI-augmented software development environments [3, 4, 8].

---

*Extraido via NotebookLM em October 2026 para MLR: Software Developer Metrics in Practice*


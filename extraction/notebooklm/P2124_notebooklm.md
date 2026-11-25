# P2124 — Toward Optimal Psychological Functioning in AI-Driven Software Engineering Tasks: The Software Evaluation for Well-Being and Optimal Psychological Functioning in a Context-Aware Environment Assessment Framework

**Decisao: INCLUIDO | Qualidade: 9/12**

---

## Dados Bibliograficos

| Campo | Valor |
|-------|-------|
| **ID** | P2124 |
| **Autores** | Oussama Ben Sghaier, Jean-Sébastien Boudrias, Houari Sahraoui [1] |
| **Ano** | 2024 [1] |
| **Venue** | IEEE Software (vol. 41, issue 4, pp. 82–89) [1] |
| **DOI** | 10.1109/MS.2024.3382364 [1] |
| **Tipo** | Journal article [1] |
| **Metodo** | Conceptual framework proposal with an illustrative case study scenario [2, 3] |
| **Amostra** | Illustrative scenario with 2 software developer profiles (entry-level Vinh and experienced Bakhta) [4, 5] |
| **Contexto** | Industry (financial data analysis platform development) [4] |
| **Modo de trabalho** | Not specified |
| **Metodologia** | Not specified |

---

## Objetivo

The main objective of the paper is to introduce **SEWELL-CARE** (*Software Evaluation for Well-Being and Optimal Psychological Functioning in a Context-Aware Environment*), a conceptual framework designed to assess AI-driven software engineering tasks by combining technical performance metrics with human factors, psychological well-being, and work dynamics within specific operational contexts [2, 6, 7].

---

## Questoes de Pesquisa

Not explicitly stated using "RQ" designations in the paper; the authors present a conceptual framework and evaluate its application using a code review scenario [2, 3].

---

## Metricas e Instrumentos de Avaliacao

| Metrica | Categoria | Nivel | Como Coletada | Validada |
|---------|-----------|-------|---------------|----------|
| **Performance–Objective** | Productivity / Quality | Individual | Objective quantifiable data (e.g., accuracy, task execution time) [8] | Yes [8] |
| **Performance–Subjective** | Satisfaction / Quality | Individual | Self-reported opinions, perceptions, and judgments [9] | Yes [9] |
| **Motivation** | DevEx | Individual | Self-reported rating on individual energization and persistence [9] | Yes [9] |
| **Satisfaction** | Satisfaction | Individual | Self-reported contentment and fulfillment scale [9] | Yes [9] |
| **Stress** | DevEx | Individual | Self-reported rating of mental/emotional strain [9] | Yes [9] |
| **Overload** | DevEx | Individual | Self-reported workload and information processing capacity [9] | Yes [9] |
| **Task Conflict** | Collaboration | Team | Perceived disagreement between tasks [10] | Yes [10] |
| **Role Ambiguity** | Collaboration | Individual | Perceived uncertainty regarding task duties and expectations [10] | Yes [10] |
| **Commitment** | Satisfaction | Individual | Dedicated involvement and task responsibility scale [10] | Yes [10] |
| **Rejection** | Attitude | Individual | Disapproval or task refusal indicator [10] | Yes [10] |
| **Precision & Recall** | Quality | Individual | Automated technical evaluation of tool performance [11] | Yes [11] |
| **BLEU Score** | Quality | Individual | Automated NLG/code generation quality measurement [11] | Yes [11] |
| **Code Reviews Completed** | Activity | Individual | Version control repository tracking [12] | Yes [12] |
| **Coding Time** | Delivery | Individual | Automated developer activity tracking [12] | Yes [12] |
| **Number of Commits** | Activity | Individual | Repository mining [12] | Yes [12] |

---

## Frameworks e Metricas

### Frameworks Referenciados
- **SPACE Framework** (Forsgren et al., 2021): REFERENCED — discussed as a multidimensional productivity framework measuring satisfaction, performance, activity, communication, and efficiency across multiple organizational levels [12-14].
- **Work Design Questionnaire (WDQ) / Work Design Model** (Morgeson & Humphrey, 2006; Humphrey et al., 2007): REFERENCED — discussed as a macroscopic job-level framework evaluating motivational, social, and contextual characteristics [14-17].
- **Extreme Programming / Human Aspects** (Hazzan & Tomayko, 2004): REFERENCED — cited regarding human factors in software engineering [1, 18].

### Frameworks Propostos
- **SEWELL-CARE** (*Software Evaluation for Well-Being and Optimal Psychological Functioning in a Context-Aware Environment*): A conceptual assessment framework specifically tailored for AI-driven software engineering tasks [2, 7]. It establishes a three-dimensional space comprising:
  1. **Characteristics**: Task characteristics (Interdependence, Skill Variety, Significance, Identity, Complexity, Feedback, Specialization, Error Rate, Autonomy, Problem-Solving, Accountability, Automation) and Tool characteristics (Explainability, Quality, Relevance, Timeliness) [4, 7, 19-21].
  2. **Contextual Parameters**: Human parameters (Knowledge, Experience) and Environment parameters (Job Stability, Team Support, Software Infrastructure, Scope, Team Communication) [22-25].
  3. **Outcomes**: Performance (Objective, Subjective), General Well-Being (Motivation, Satisfaction, Stress, Overload), Work Dynamics (Task Conflict, Role Ambiguity), and Attitude (Commitment, Rejection) [8-10, 23, 26].

---

## Fatores que Influenciam Produtividade

### Fatores Positivos
| Fator | Categoria |
|-------|-----------|
| High task automation and tool assistance (for novice developers) | Technical [27] |
| AI issue detection, localization, and review comment generation | Technical [28, 29] |
| High task significance (for experienced developers) | Human [30] |
| High task complexity and problem-solving challenges (for experienced developers) | Human [31, 32] |
| High team support and effective team communication | Organizational [22, 24, 25] |
| Robust software infrastructure | Technical [25] |

### Fatores Negativos
| Fator | Categoria |
|-------|-----------|
| High task complexity without sufficient experience or guidance (for junior developers) | Human [31] |
| High task significance causing undue stress and task rejection (for novice developers) | Human [33] |
| Excessive task automation causing loss of fine-grained control or repetition (for experienced developers) | Human [27, 33] |
| Role ambiguity and task conflict | Process [10] |
| Mental strain, stress, and workload overload | Human [9] |

---

## Papel da IA e Automacao

| Campo | Valor |
|-------|-------|
| **Usa IA/ML?** | Yes — The paper specifically targets AI-driven software engineering tasks and assistants (e.g., AI tools that detect bugs, localize issues, generate code review comments, and propose code fixes) [6, 28, 29, 34]. |
| **Automacao de coleta?** | Yes — AI assistants automate task execution and code evaluation, though psychological outcomes and contextual parameters require structured assessment [7, 21, 35]. |
| **Impacto de IA na produtividade?** | Context-dependent: For novice developers, high AI automation enhances objective performance and motivation while reducing stress [27]. For experienced developers, high AI automation improves objective performance but can reduce motivation by making tasks repetitive and increase stress due to loss of fine-grained control [27, 33]. |

---

## Resultados Principais

- **Context Sensitivity**: The impact of task characteristics on performance and psychological outcomes is strongly moderated by developer experience and knowledge [30, 33, 36].
- **Task Significance Effect**: Elevated task significance boosts objective performance and motivation while reducing stress for experienced developers, but increases stress and task rejection risk for novice developers [30, 33].
- **Divergent Automation Outcomes**: High task automation improves objective performance for all developer levels, but yields opposite psychological impacts: it increases motivation and reduces stress for novices, whereas it decreases motivation and elevates stress for senior engineers [27, 33].
- **Complexity and Problem-Solving**: Tasks requiring complex problem-solving motivate and engage senior developers, whereas they increase stress, lower performance, and induce task rejection in junior developers [31, 32].
- **Tailored Work Assignment**: Optimal psychological functioning and productivity are achieved by customizing task design — routing automated AI-assisted reviews to junior developers and complex, problem-solving PRs to senior developers [29].

---

## Desafios do Uso das Metricas

- **Overreliance on Technical Metrics**: Standard tool evaluations rely heavily on objective technical metrics (precision, recall, BLEU score) while ignoring cognitive and well-being impacts on human developers [1, 11].
- **Level Misalignment**: Existing frameworks evaluate jobs at a macroscopic level or measure productivity in isolation, failing to evaluate granular task-level interactions with AI assistants [13, 16].
- **Automation Trade-Offs**: Over-automating tasks can demotivate experienced developers by turning engaging problem-solving activities into repetitive monitoring tasks [27].
- **Scalability in Team Settings**: Designing tasks for larger teams involves complex trade-offs across competing preferences and constraints rather than single-variable outcome maximization [37].

---

## Avaliacao de Qualidade Metodologica

| Criterio | Pontuacao (0-2) |
|----------|----------------|
| Objetivo claramente definido | 2 |
| Metodologia adequada ao objetivo | 2 |
| Amostra/contexto descrito adequadamente | 1 |
| Ameacas a validade discutidas | 1 |
| Resultados com evidencia suficiente | 1 |
| Contribuicao clara para pratica ou teoria | 2 |
| **TOTAL** | **9/12** |

*(Nota: Pontuação fundamentada: Objetivo [2, 6] e contribuição [7, 38] são explícitos e bem definidos (2/2); metodologia conceitual é adequada à proposta (2/2); contexto utiliza um cenário ilustrativo com 2 perfis de desenvolvedores em vez de amostragem empírica ampla (1/2); ameaças à validade e evidências quantitativas são discutidas de forma descritiva/qualitativa e remetidas a trabalhos futuros (1/2 cada)).*

---

## Limitacoes

- **Descriptive Nature**: The current version of SEWELL-CARE is descriptive rather than predictive, lacking quantitative algorithms to forecast outcomes automatically [39].
- **Illustrative Scenario**: Validation is demonstrated via an illustrative 2-developer code review scenario rather than a large-scale empirical field study across multi-organizational teams [3-5].
- **Combinatorial Complexity**: Analyzing interactions across a 3D space (characteristics x context x outcomes) creates a high number of permutations, complicating optimization for large teams [37, 40].

---

## Contribuicao Principal

The primary contribution of this paper is **SEWELL-CARE**, a task-level conceptual assessment framework that bridges technical task attributes, AI tool characteristics, and developer contextual parameters with well-being and psychological functioning outcomes [2, 7, 38]. It equips practitioners with a structured method to tailor AI-driven task design, balancing technical productivity with developer mental health, motivation, and job satisfaction [2, 29, 38].

---

*Extraido via NotebookLM em October 2026 para MLR: Software Developer Metrics in Practice*

---

💡 **Sugestão de Próximo Passo**: Gostaria que eu comparasse a abordagem do **SEWELL-CARE** com o modelo **SPACE** ou **GQM** em uma tabela comparativa detalhada sobre métricas de bem-estar e produtividade?
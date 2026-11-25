# P2042 — Towards an Appropriate Level of Reliance on AI: A Preliminary Reliance-Control Framework for AI in Software Engineering

**Decisao: INCLUIDO | Qualidade: 4/5**

---

## Dados Bibliograficos

| Campo | Valor |
|-------|-------|
| **ID** | P2042 |
| **Autores** | Samuel Ferino, Rashina Hoda, John Grundy, Christoph Treude [1] |
| **Ano** | 2026 [2] |
| **Venue** | 34th ACM International Conference on the Foundations of Software Engineering (FSE Companion ’26) [2] |
| **DOI** | 10.1145/3803437.3806704 [2] |
| **Tipo** | Conference paper (Companion paper) [2] |
| **Metodo** | Qualitative (Socio-Technical Grounded Theory based on semi-structured interviews) [3] |
| **Amostra** | 22 software developers / practitioners [1, 3] |
| **Contexto** | Industry software development practitioners across Asia, Europe, North America, South America, and Oceania using LLM tools [3] |
| **Modo de trabalho** | Not specified |
| **Metodologia** | Not specified |

---

## Objetivo

The paper addresses the problem of achieving an appropriate level of reliance on AI tools in software engineering [1, 4]. By analyzing data from 22 semi-structured interviews with software practitioners using socio-technical grounded theory [3], the authors propose a preliminary two-dimensional Reliance-Control Framework [1, 4, 5]. This framework conceptualizes how developers' level of reliance co-evolves with their level of control over AI systems, broadening the definition of appropriate reliance beyond task accuracy to guide practitioners, team leaders, educators, and researchers toward responsible and effective AI tool adoption [1, 4, 6-8].

---

## Questoes de Pesquisa

No explicit formal research questions (e.g., RQ1, RQ2) are stated in the paper [1, 3, 4]. The study is driven by the broader objective of conceptualizing developer reliance and control over AI tools in software engineering through qualitative grounded theory analysis [1, 3, 4].

---

## Metricas e Instrumentos de Avaliacao

| Metrica | Categoria | Nivel | Como Coletada | Validada |
|---------|-----------|-------|---------------|----------|
| Cognitive Load / Neural Activity | DevEx / Human | Individual | Electroencephalography (EEG) and Natural Language Processing (cited from Kosmyna et al. [9]) [10] | Yes |
| Developer Productivity Gains | Productivity | Individual / Team | SPACE framework metrics in a within-subject user study (cited from Weber et al. [11]) [12] | Yes |
| User Interaction Click Rate | Activity | Individual | User study tracking interaction logs under AI friction interventions (cited from Collins et al. [2]) [13] | Yes |
| Perceived Code Error Rate | Quality | Individual / Organization | Industry report survey (cited from Qodo AI [5]: 25% of developers believe 1 in 5 LLM suggestions contain errors) [14] | Partial |

*Note:* P2042 itself is a qualitative conceptual study based on interviews [3] and does not define or quantitatively measure software developer metrics directly [3, 4]. The metrics listed above are referenced from prior literature cited within the paper [10, 12-14].

---

## Frameworks e Metricas

### Frameworks Referenciados
- **SPACE**: REFERENCED — Discussed in Section 1 regarding productivity gains measured in developer studies (Weber et al. [11]) [12].
- **DORA**: REFERENCED — Discussed in Section 1 regarding enterprise report interest in AI-assisted development [12].
- **Taxonomy of Human-AI Collaboration in SE (Treude & Gerosa [15])**: REFERENCED and APPLIED — Applied in Section 4.2 (Table 3) to map 12 developer-AI interaction types onto the proposed reliance and control dimensions [16-18].

### Frameworks Propostos
- **Reliance-Control Framework for AI in Software Engineering**: A preliminary two-dimensional framework mapping human control against reliance on AI [1, 4, 19]:
  - **Control over AI (5 levels)** [20, 21]: Self-Control (e.g., abstaining/turning off AI suggestions), Taking Control (e.g., context-switching to web platform/dummy data due to privacy), Balanced Control (e.g., TDD supervision, boilerplate code generation), Handing over Control (e.g., vibe coding, agent mode), Losing Control (e.g., inability to debug, introducing code bugs/vulnerabilities).
  - **Reliance on AI (5 levels)** [22, 23]: Self-Reliance (confidence in own skills), Reliance on Colleagues (prioritizing peer support/collaboration), Appropriate Reliance (vigilant of AI pitfalls, cross-checking), Overreliance on AI (excessive trust, urge to use LLM before trying), Full Automation (full task delegation, e.g., meeting summarization).
  - **Sweet Spot**: Intersection of *Balanced Control* and *Appropriate Reliance* (Point 7: Test-driven development with LLMs, prompting across multiple LLMs) [19, 24, 25].

---

## Fatores que Influenciam Produtividade

### Fatores Positivos
| Fator | Categoria |
|-------|-----------|
| AI automation of repetitive development tasks (e.g., code translation, test generation, boilerplate code generation, debugging support) [12, 25-27] | Technical / Process |
| LLM summarization capabilities for fast information retrieval and meeting documentation [11, 26] | Process / Technical |
| Balanced human-AI collaboration (e.g., supervising TDD test scenario generation with LLM agent mode) [25] | Human / Process |
| Solid fundamental developer skills ensuring effective oversight and critical thinking [15, 16, 27] | Human |

### Fatores Negativos
| Fator | Categoria |
|-------|-----------|
| Overreliance on AI causing cognitive debt, atrophy of critical thinking skills, and lower neural/behavioral performance [1, 10] | Human |
| Relinquishing control to AI agent modes leading to code errors, vulnerabilities, or unauthorized multi-file modifications [6, 12, 14, 21] | Technical / Process |
| Reduced team communication when developers spend excessive time tweaking prompts instead of consulting peers [10] | Organizational / Human |
| LLM hallucinations and context size limitations introducing code defects [8, 28] | Technical |
| UI design frictions causing unintended drops in developer engagement or click rates [13] | Technical / Process |

---

## Papel da IA e Automacao

| Campo | Valor |
|-------|-------|
| Usa IA/ML? | Yes — Investigates developer usage of LLM tools (e.g., ChatGPT, Claude, Cursor, Windsurf, GitHub Copilot) for software engineering tasks [1, 3, 25]. |
| Automacao de coleta? | No — Qualitative research methodology using semi-structured interviews (22 participants across 3 rounds) and pre-interview questionnaires [3]. |
| Impacto de IA na produtividade? | AI tools reduce effort and save development time for repetitive tasks [12, 27], but overreliance or losing control degrades code understanding, introduces vulnerabilities, and reduces peer communication [6, 10, 21, 26]. Optimal outcomes occur at the "sweet spot" of balanced control and appropriate reliance [19, 24, 25]. |

---

## Resultados Principais

- **Qualitative Grounded Theory Study**: Derived from 22 semi-structured interviews with software practitioners across 5 continents (Asia, Europe, North America, South America, Oceania) between October 2024 and September 2025 [3].
- **Two-Dimensional Framework**: Defines 5 levels of Control (Self-Control, Taking Control, Balanced Control, Handing over Control, Losing Control) and 5 levels of Reliance (Self-Reliance, Reliance on Colleagues, Appropriate Reliance, Overreliance on AI, Full Automation) [20-24].
- **Identification of the "Sweet Spot"**: Point 7 in the framework represents the optimal intersection of *Balanced Control* and *Appropriate Reliance* (e.g., TDD iterations using LLM agent mode under active human supervision) [19, 24, 25].
- **Mapping Collaboration Taxonomies**: Categorized Treude & Gerosa's 12 interaction types, demonstrating that conversational assistance and comment-guided prompts promote appropriate reliance, whereas auto-complete and file-aware suggestions lean toward overreliance or full automation [16-18].
- **Consequences of Overreliance**: Excessive trust in LLMs leads to reduced team communication on architecture [10], cognitive skill atrophy [1], and code defects (citing 25% of developers reporting 1 in 5 suggestions contain errors) [14].
- **Role of Developer Expertise**: Recommends that novice developers use interaction modes requiring higher human control (e.g., web chat or terminal mode) to prevent overreliance while learning core programming concepts [8, 27, 29].

---

## Desafios do Uso das Metricas

- **Limitations of Interaction-Level Interventions**: Existing UI and prompt interventions (disclaimers, uncertainty highlighting) fail to reliably calibrate trust or cause unintended friction (drop in click rate) [9, 13].
- **Silent Overreliance**: Developers excessively trusting AI outputs without cross-checking documentation or external reliable sources, impairing long-term debugging capabilities [21, 28].
- **Erosion of Team Collaboration**: Developers substituting direct communication with colleagues on critical architecture and design questions for prolonged prompt engineering [10, 22].
- **Organizational Misalignment**: Relying on generic LLM outputs that fail to align with project-specific or organizational norms [25].
- **Unsupervised Agent Execution**: Allowing autonomous AI agents (e.g., Cursor Agent Mode, GitHub Copilot Agent Mode) to perform multi-file edits or pull request generation without adequate human oversight [6, 14, 26].

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

---

## Limitacoes

- **Qualitative Sample & Bias**: Limited sample size (22 interview participants) and potential qualitative research bias inherent in interview-based grounded theory [3, 30].
- **Preliminary Nature**: The Reliance-Control Framework is a preliminary conceptual model requiring further empirical validation through quantitative experiments and longitudinal case studies [4, 30].
- **Illustrative Mapping**: The practical examples and taxonomy mappings provided are illustrative rather than exhaustive [5, 31].
- **Unintegrated Expertise Factor**: Developer expertise and task complexity are recognized as influencing factors but are not yet fully integrated into the 2D matrix structure [16, 27, 29].
- **Rapidly Evolving AI Tooling**: Emerging LLM interaction modes and agent capabilities may continuously alter control and reliance boundaries [14, 27, 30].

---

## Contribuicao Principal

The primary contribution of this paper is the proposal of a novel, preliminary two-dimensional Reliance-Control Framework for AI in software engineering, derived from a socio-technical grounded theory analysis of 22 practitioner interviews [1, 3, 4]. By linking levels of developer reliance (from self-reliance to full automation) with levels of human control (from self-control to losing control), the study broadens the understanding of appropriate reliance beyond task accuracy [1, 4]. It identifies an optimal "sweet spot" at the intersection of balanced control and appropriate reliance, providing actionable guidance for team management, software engineering education, AI tool design, and future empirical SE research [6-8, 14, 19, 24].

---

*Extraido via NotebookLM em October 2026 para MLR: Software Developer Metrics in Practice*
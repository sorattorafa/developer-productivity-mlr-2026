# P2068 — Software Developers' Perceptions of Productivity: An Industry-focused Study

**Decisao: INCLUIDO | Qualidade: 5/5**

---

## Dados Bibliograficos

| Campo | Valor |
|-------|-------|
| **ID** | P2068 [1] |
| **Autores** | Murilo Coelho, Isabelle Reinbold, Lizie Sancho, Matheus Paixao, Allysson Allex Araújo, Sávio Freire [1, 2] |
| **Ano** | 2025 [3] |
| **Venue** | Brazilian Symposium on Software Quality (SBQS 2025) [3] |
| **DOI** | N/A (Replication Package: Zenodo 10.5281/zenodo.17335369) [3, 4] |
| **Tipo** | Conference paper [3] |
| **Metodo** | Qualitative / Mixed methods (Semi-structured focus groups and confirmatory questionnaire) [2, 5] |
| **Amostra** | 16 software developers divided into 2 focus groups (7 and 9 participants), followed by a confirmatory questionnaire [5, 6] |
| **Contexto** | Industry / Research and Technology Organization (RTO) — Atlântico Institute, Brazil [3, 7, 8] |
| **Modo de trabalho** | Remote (predominantly operating under a remote work model across Brazil) [3, 8] |
| **Metodologia** | Not specified [3, 9] |

---

## Objetivo

This paper aims to examine software developers' perceptions of productivity in their day-to-day work, focusing on how productivity is defined and measured across core software development lifecycle activities (coding, code review, and documentation), while investigating the expected impacts, benefits, and drawbacks of adopting Generative AI (GenAI) tools within the hybrid mission of a Brazilian Research and Technology Organization (RTO) [2, 3, 7, 10].

---

## Questoes de Pesquisa

- **RQ1**: What is the perceived productivity of software developers? (Investigates the main factors that lead developers to feel productive or unproductive when performing their activities) [10].
- **RQ2**: How do software developers measure productivity within the software development lifecycle? (Investigates how developers assess productivity in coding, code review, and documentation activities) [10].
- **RQ3**: How is GenAI expected to affect the productivity of software developers? (Identifies the expected impact, benefits, and potential drawbacks of GenAI tools on developer productivity) [10].

---

## Metricas e Instrumentos de Avaliacao

| Metrica | Categoria | Nivel | Como Coletada | Validada |
|---------|-----------|-------|---------------|----------|
| **Progress / Evolution** | Activity / Productivity | Individual / Team | Perceptual assessment of task progression and meeting goals [5, 9] | Partial [11] |
| **Expectations Fulfillment** | Collaboration / Performance | Individual / Team / Organization | Perceptual feedback regarding personal, team, and client expectations [9, 12] | Partial [11] |
| **Timebox / Deadline Adherence** | Delivery / Performance | Individual / Team | Tracking completed demands within established sprint timeboxes [9] | Partial [11] |
| **Code Quality** | Quality | Individual / Team | Assessing compliance with functional and non-functional quality standards [9] | Partial [11] |
| **Efficiency** | DevEx / Productivity | Individual | Perceptual tracking of process optimization and waste reduction [9] | Partial [11] |
| **Code Reusability** | Quality / Activity | Individual | Self-reported identification of generalized, repurposable components [13] | Partial [11] |
| **Code Readability** | Quality | Individual | Peer/self-inspection of naming clarity and function conciseness [13] | Partial [11] |
| **Code Optimization** | Quality | Individual | Technical evaluation of code efficiency and system architecture impact [14] | Partial [11] |
| **Code Functionality** | Quality / Activity | Individual | Direct verification of working algorithms and working implementation [14] | Partial [11] |
| **Requirements Compliance** | Delivery / Quality | Individual | Verifying code output against specific task requirements and scope [15] | Partial [11] |
| **Learning in Code Review** | DevEx / Collaboration | Individual | Self-reported acquisition of new technical knowledge during review [16] | Partial [11] |
| **PR Code Quality** | Quality | Team / Individual | Inspecting Pull Requests against project-specific quality criteria [16] | Partial [11] |
| **Review Turnaround Speed** | Delivery / Flow | Team | Measuring time taken to provide review feedback or merge code [17] | Partial [11] |
| **Documentation Writing Quality** | Quality | Individual / Team | Assessing structural completeness of test scenarios and acceptance criteria [18] | Partial [11] |
| **Documentation Information Clarity** | Quality / Collaboration | Individual / Team | Assessing clarity and absence of ambiguity for downstream consumers [18, 19] | Partial [11] |

---

## Frameworks e Metricas

### Frameworks Referenciados
- **SPACE Framework**: REFERENCED & APPLIED — The paper extensively uses the SPACE framework to map qualitative productivity factors, developer feelings, and GenAI support strategies across its 5 dimensions: Satisfaction and well-being, Performance, Activity, Communication and collaboration, and Efficiency and flow [3, 20-24].
- **GQM (Goal Question Metric)**: REFERENCED — Cited in the background literature as a traditional productivity measurement approach [20, 25].

### Frameworks Propostos
- **Software Developers' Perception of Productivity Conceptual Map**: The authors propose a conceptual framework (Figure 2) synthesizing productivity factors (positive vs. negative), GenAI expected impacts (benefits vs. drawbacks), and specific productivity indicators for coding, code review, and documentation [26-28].

---

## Fatores que Influenciam Produtividade

### Fatores Positivos
| Fator | Categoria |
|-------|-----------|
| **Progress / Evolution (Progresso e evolução nas tarefas)** | Process / Activity [9] |
| **Expectations (Atendimento às expectativas de clientes e time)** | Organizational / Human [9] |
| **Time / Deadline (Cumprimento de prazos e timeboxes)** | Process / Organizational [9] |
| **Quality (Entrega de código com alta qualidade)** | Technical [9] |
| **Efficiency (Otimização de tempo e recursos)** | Process / Human [9] |

### Fatores Negativos
| Fator | Categoria |
|-------|-----------|
| **Repetitive tasks (Execução de tarefas altamente repetitivas)** | Process / Technical [29] |
| **Context switching (Troca constante de contexto e interrupções)** | Human / Organizational [29] |
| **Unclear requirements (Requisitos indefinidos ou vagos)** | Organizational / Process [30] |
| **Non-coding activities (Atividades administrativas e bloqueios fora da codificação)** | Organizational / Process [30] |

---

## Papel da IA e Automacao

| Campo | Valor |
|-------|-------|
| **Usa IA/ML?** | Yes — Investigates developer expectations and adoption of Generative AI / Large Language Models (LLMs) such as ChatGPT [2, 31-33]. |
| **Automacao de coleta?** | No — Data collection was performed via semi-structured online focus groups and transcribed using OpenAI Whisper, followed by manual content analysis [11, 34, 35]. |
| **Impacto de IA na produtividade?** | **Expected Benefits:** Reduces time on routine technical tasks, supports code writing, provides guidance/learning for junior developers, helps initiate tasks ("initial push"), assists in writing documentation, and provides working tool examples [33, 36, 37].<br>**Expected Drawbacks:** Generates dead or duplicated code, produces AI hallucinations, increases debugging effort (up to 4x longer spent analyzing bugs), and risks reducing critical thinking and independence among novice developers [38, 39]. |

---

## Resultados Principais

- **Definition of Developer Productivity**: Productivity in an RTO environment is defined as experiencing quantitative or qualitative progress in writing code that satisfies quality criteria, task requirements, and stakeholder expectations within stipulated deadlines [40].
- **Prevalence of Productivity Factors**: Progress/evolution emerged as the most frequently cited positive productivity factor (23 mentions), followed by expectations (21), time/deadlines (15), quality (9), and efficiency (6) [9].
- **Primary Detractors**: Repetitive manual coding, context switching between tasks, unclear task requirements, and blocking non-coding workload were identified as the primary causes of unproductivity [29, 30].
- **Code Review Perception Duality**: Code review is frequently perceived as an unproductive bottleneck delaying delivery; however, it enhances perceived productivity when it fosters technical learning, maintains PR quality standards, and operates with rapid turnaround speed [16, 17, 41].
- **Documentation Value**: High-quality, clear documentation prevents rework and serves as a direct indicator of team productivity [18, 19].
- **GenAI Debugging Paradox**: Although GenAI speeds up initial task execution and code writing, developers report that time saved can be offset by spending up to 4x longer debugging and validating generated outputs [33, 39].

---

## Desafios do Uso das Metricas

- **Single-Metric Fallacy**: Relying on single proxy metrics (e.g., velocity or lines of code) obscures essential qualitative work such as mentoring, architectural design, and code quality [42].
- **Review Bottleneck Perception**: Formal Pull Request reviews are often viewed as friction points that reduce individual velocity, creating a tension between speed and quality assurance [41].
- **AI Code Bloat and Over-generation**: GenAI tools frequently measure quality by volume, outputting bloated, redundant, or dead code that increases code review overhead and maintenance debt [38].
- **Ambiguity of Non-Coding Tasks**: Activities like architecture discovery and stakeholder communication are essential for project success but make developers feel unproductive due to lack of tangible code output [12, 30].
- **Quantifying Knowledge Work**: Measuring software productivity remains difficult because outputs are knowledge-based rather than physical units, making traditional throughput metrics inadequate [43, 44].

---

## Avaliacao de Qualidade Metodologica

| Criterio | Pontuacao (0-2) |
|----------|----------------|
| Objetivo claramente definido | 2 [2, 3] |
| Metodologia adequada ao objetivo | 2 [8, 11, 34] |
| Amostra/contexto descrito adequadamente | 2 [8, 32, 45, 46] |
| Ameacas a validade discutidas | 2 [47-50] |
| Resultados com evidencia suficiente | 2 [9, 15, 18, 37, 40, 51] |
| Contribuicao clara para pratica ou teoria | 2 [26, 27, 47, 52] |
| **TOTAL** | **12/12** |

---

## Limitacoes

- **Sample Size and Single Organization**: The study was conducted with 16 software developers from a single Brazilian Research and Technology Organization (Atlântico Institute), limiting statistical generalizability to general commercial software firms [3, 8, 50].
- **Scope of Engineering Activities**: Analysis was strictly restricted to coding, code review, and documentation, omitting other lifecycle phases such as requirements elicitation, testing, architecture, and project management [48, 53].
- **Recall Bias in Validation**: The confirmatory questionnaire was administered 6 months after the focus group sessions, introducing potential recall bias among participants [11, 47].
- **Subjective / Self-Reported Data**: Results rely entirely on qualitative self-reported perceptions rather than objective software repository telemetry or quantitative performance tracking [34, 50].
- **Focus Group Moderator Risk**: Focus groups carry potential risks of researcher bias and vocal participant dominance, though mitigated by multi-moderator protocols and equity strategies [6, 47, 48].

---

## Contribuicao Principal

The primary contribution of this paper is an empirical investigation into software developers' perceptions of productivity within the context of a Research and Technology Organization (RTO) in Brazil [2, 3, 26]. The study maps developer perceptions across coding, code review, and documentation activities onto the multidimensional SPACE framework, and proposes a conceptual map detailing productivity factors, measurement indicators, and GenAI trade-offs to guide software organizations in balancing AI-driven efficiency gains with technical quality [3, 21, 26, 27].

---

*Extraido via NotebookLM em October 2026 para MLR: Software Developer Metrics in Practice*
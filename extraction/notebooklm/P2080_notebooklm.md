# P2080 — AI-assisted Collaboration: Exploring Developer Experience with GitHub Copilot and Windsurf [1]

**Decisao: INCLUIDO | Qualidade: 5/5** [1-6]

---

## Dados Bibliograficos

| Campo | Valor |
|-------|-------|
| **ID** | P2080 [1] |
| **Autores** | Sabrina C. Winckler, Jéssica F. Ribeiro, Letícia Machado, Josiane Kroll [7] |
| **Ano** | 2026 [1] |
| **Venue** | IEEE Software [1, 8] |
| **DOI** | 10.1109/MS.2026.3671677 [1] |
| **Tipo** | Journal article [1, 8] |
| **Metodo** | Mixed methods (Case study combining quantitative enterprise telemetry and qualitative thematic analysis) [1, 3, 9] |
| **Amostra** | 36-person technical unit (26 Copilot subscribers [21 active, 4 sporadic, 1 inactive], 2 Windsurf users, 8 non-AI users; 9 provided qualitative reflections) [1, 9-11] |
| **Contexto** | Industry — Brazilian fintech organization (online digital lender founded in 2015, 90 employees, 77 repositories: C#, Java, Python, TypeScript, JavaScript) [3, 12] |
| **Modo de trabalho** | Not specified [3, 12] |
| **Metodologia** | Agile, Continuous Delivery [12] |

---

## Objetivo

This study investigates the adoption and impact of AI-assisted coding tools (specifically GitHub Copilot and Windsurf) on software developer experience (DevEx) within a corporate software engineering setting [1, 2]. Conducted over a three-month period in a Brazilian fintech organization, the research combines quantitative usage telemetry with qualitative thematic analysis to examine how AI tools integrate into daily workflows, how developers manage trust and output validation, and how AI assistance shapes flow state, feedback loops, and cognitive load [1, 2, 13].

---

## Questoes de Pesquisa

*(Note: The paper addresses three main research directions implicitly in its study design [2])*
- **RQ1**: How are AI-assisted coding tools (GitHub Copilot and Windsurf) integrated into daily workplace workflows in a software organization? [2]
- **RQ2**: How do developers handle responsibility, trust, and output validation when using AI-assisted coding tools? [2]
- **RQ3**: How do AI-assisted coding tools affect Developer Experience (DevEx) across flow state, feedback loops, and cognitive load? [1, 2]

---

## Metricas e Instrumentos de Avaliacao

| Metrica | Categoria | Nivel | Como Coletada | Validada |
|---------|-----------|-------|---------------|----------|
| **Number of Prompts** | Activity / Usage | Organization | Quantitative enterprise telemetry via GitHub Copilot Metrics Viewer (v2.0.2) | Yes [4, 14] |
| **Number of Suggestions** | Activity / Usage | Organization | Quantitative enterprise telemetry via GitHub Copilot Metrics Viewer (v2.0.2) | Yes [4, 14] |
| **Acceptance Rate by Count** | Productivity / Quality | Organization | Quantitative enterprise telemetry (accepted suggestions / total suggestions) | Yes [4, 14] |
| **Line-Level Acceptance Rate** | Productivity / Quality | Organization | Quantitative enterprise telemetry (accepted lines / total suggested lines) | Yes [4, 14] |
| **Flow State Perceptions** | DevEx / Satisfaction | Individual | Qualitative participant observation in technical meetings & deductive thematic coding | Yes [9, 13] |
| **Feedback Loops Perceptions** | DevEx / Collaboration | Individual | Qualitative participant observation in technical meetings & deductive thematic coding | Yes [9, 13] |
| **Cognitive Load Perceptions** | DevEx / Productivity | Individual | Qualitative participant observation in technical meetings & deductive thematic coding | Yes [9, 13] |

---

## Frameworks e Metricas

### Frameworks Referenciados
- **DevEx Framework** (Noda et al., Forsgren et al.): APPLIED — used as the core qualitative evaluation framework focusing on flow state, feedback loops, and cognitive load [1, 13, 15].

### Frameworks Propostos
- None proposed as a new formal framework; the paper applies and extends the 3-dimension DevEx framework to AI-assisted tool adoption [1, 5, 13].

---

## Fatores que Influenciam Produtividade

### Fatores Positivos
| Fator | Categoria |
|-------|-----------|
| Automation of routine coding, boilerplate, documentation, and test generation | Technical [1, 15, 16] |
| Accelerated developer learning curve and onboarding | Human [16, 17] |
| Improved work organization and sustained flow state | Process [16, 17] |
| Enhanced problem-solving and operational troubleshooting | Technical [16, 17] |
| Real-time code completion providing immediate feedback loops | Technical [15, 16] |
| AI functioning as a collaborative partner or senior developer proxy | Human / Organizational [16, 17] |

### Fatores Negativos
| Fator | Categoria |
|-------|-----------|
| High validation burden (prompt engineering, verifying suggestions, bug checking) | Human / Process [1, 5, 18] |
| Increased cognitive load required to guide, steer, and review AI output | Human / Technical [17, 18] |
| Risk of over-reliance on AI output ("crutch for shortcomings") | Human [17, 18] |
| Strict regulatory, architectural, and codebase constraints in fintech | Organizational / Technical [6, 19] |
| Lack of organizational telemetry/analytics for tools like Windsurf | Technical / Organizational [9, 14] |

---

## Papel da IA e Automacao

| Campo | Valor |
|-------|-------|
| **Usa IA/ML?** | Yes — GitHub Copilot (LLM-based code completion/chat) and Windsurf (Cascade agentic platform) [1, 15]. |
| **Automacao de coleta?** | Yes (Partial) — Automated quantitative telemetry collected for GitHub Copilot via enterprise dashboard viewer; qualitative observations collected manually [9, 14]. |
| **Impacto de IA na produtividade?** | Positive for routine task execution and flow state, but creates a "productivity-validation tension" where time saved on writing code is offset by cognitive effort spent validating and reviewing AI output [1, 5, 20]. |

---

## Resultados Principais

- **Tool Adoption Trends**: 58.3% (21/36) of technical unit members actively used GitHub Copilot, 5.6% (2/36) used Windsurf, 11.1% (4/36) used Copilot sporadically, 2.8% (1/36) was inactive, and 22.2% (8/36) maintained no AI tool subscription [11, 21].
- **Copilot Enterprise Telemetry**: Active users generated 47,336 prompts and 98,797 code suggestions, achieving an overall suggestion acceptance rate of 24.23% (by count) and a line-level acceptance rate of 16.36% over the study period [19, 22].
- **DevEx Dimensions & Qualitative Frequency**:
  - *Cognitive Load* was the most frequent qualitative theme (33% of participants), driven by the need to review, guide, and steer AI output [17, 20].
  - *Flow State* benefits were widely reported, with developers describing tools as "game changers" for routine task execution, learning acceleration, and work organization [16, 17, 20].
  - *Feedback Loops* showed positive perceptions, with AI viewed as an effective collaborator similar to a senior developer [16, 17, 20].
- **Productivity-Validation Tension**: AI tools accelerate routine tasks but introduce sustained validation burdens (prompt formulation, output verification, architectural alignment), shifting developer workload rather than eliminating it [1, 5, 18].
- **Seniority & Meta-cognitive Skills**: Senior developers and tech leads exhibited greater meta-cognitive awareness in knowing when to leverage vs. verify AI suggestions compared to junior peers [5, 23].

---

## Desafios do Uso das Metricas

- **Tool Analytics Asymmetry**: Windsurf's individual licensing model lacks enterprise organizational telemetry, preventing direct quantitative comparison with GitHub Copilot [9, 14].
- **Telemetry Retention & Versioning Issues**: Updating the GitHub Copilot Metrics Viewer (v2.0.2 to v2.1.2) blocked access to raw telemetry for early months (May–June 2025), limiting historical granular comparison [11].
- **Lack of User-Level Normalization**: Enterprise telemetry metrics were aggregate counts across active users rather than normalized by active developer hours or individual accounts [4, 22].
- **Organizational Confounders**: Regulatory fintech constraints, complex business logic, strict code review policies, and codebase traits (77 repos) make it difficult to isolate AI productivity gains from general engineering context [6, 19].

---

## Avaliacao de Qualidade Metodologica

| Criterio | Pontuacao (0-2) |
|----------|----------------|
| Objetivo claramente definido | 2 [1, 2] |
| Metodologia adequada ao objetivo | 2 [1, 3, 9] |
| Amostra/contexto descrito adequadamente | 2 [3, 10-12] |
| Ameacas a validade discutidas | 2 [6, 11, 22] |
| Resultados com evidencia suficiente | 2 [4, 19, 20] |
| Contribuicao clara para pratica ou teoria | 2 [1, 5, 24] |
| **TOTAL** | **12/12** [1-6] |

---

## Limitacoes

- Single case study in a Brazilian fintech company, limiting external validity and domain generalization [3, 6].
- Small qualitative sample (n=9 submitted reflections out of a 36-person technical unit) and very small Windsurf user sample (n=2) [6, 9, 11].
- Voluntary tool adoption introducing potential selection bias [6, 25].
- Short telemetry observation window (3 months) affected by platform configuration changes and retention limits [6, 11, 14].
- Lack of quantitative usage telemetry for Windsurf due to licensing constraints [6, 9, 14].

---

## Contribuicao Principal

This paper delivers empirical evidence on how AI-assisted coding tools (GitHub Copilot and Windsurf) impact Developer Experience (DevEx) in a real-world corporate fintech setting [1-3]. By combining enterprise quantitative usage telemetry with qualitative participant observations across flow state, feedback loops, and cognitive load, the study frames AI adoption as a sociotechnical transformation rather than simple tool substitution, identifying a fundamental "productivity-validation tension" where routine task acceleration is counterbalanced by an enduring requirement for human oversight and verification [1, 5, 24].

---

*Extraido via NotebookLM em October 2026 para MLR: Software Developer Metrics in Practice*

💡 *Would you like me to synthesize these findings into a comparative summary or generate a slide deck for your MLR presentation?*
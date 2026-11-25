# G105 — AI Accountability Report

**Decisao: INCLUIDO | Qualidade GL: 4.5/6**

---

## Dados Bibliograficos

| Campo | Valor |
|-------|-------|
| **ID** | G105 |
| **Autor/Organizacao** | GitLab Inc. (conducted by The Harris Poll) |
| **Data** | June 23, 2026 |
| **Tipo** | Industry report / Press release |
| **URL** | https://about.gitlab.com/press/releases/2026-06-23-gitlab-research-reveals-organizations-are-generating-ai-code-faster-than-they-can-control-it/ |

---

## Resumo

GitLab Inc. released its AI Accountability Report based on a survey conducted by The Harris Poll of 1,528 developers and technology buyers across six countries [1]. The report indicates that while AI coding adoption has surged—with 91% of organizations using two or more AI coding tools and 78% reporting faster code output—code generation speed is running ahead of organizational governance [1, 2]. Overall, 80% of organizations adopted AI tools faster than establishing policies to govern them, and 92% report facing governance challenges with AI-generated code [1, 3].

The report identifies the **"AI Paradox"**, where 79% of respondents agree that individual developer productivity has improved, yet the broader software delivery process has not accelerated at the same pace [2]. Instead, bottlenecks have shifted downstream: 85% agree that the main bottleneck has moved from writing code to reviewing and validating it [4]. Critical traceability gaps persist: 43% of organizations cannot reliably distinguish AI-generated code from human-written code, 82% view AI-generated code as a risk for creating new technical debt, and 34% of organizations that experienced a production incident in the past year were unable to determine whether AI-generated code contributed to it [1, 2, 4].

To mitigate these risks, industry priorities are shifting from pure code generation to code governance [5]. 85% of respondents agree that the next phase of AI in software development will focus primarily on governing code [5]. Consequently, 91% of organizations plan to invest in AI code governance tools over the next 12 months, with 98% having already allocated or expecting to allocate budget toward establishing context, traceability, and governance within integrated DevSecOps platforms [3, 5].

---

## Frameworks Mencionados

* **DORA Framework**: Not explicitly mentioned in the source [1-11].
* **SPACE Framework**: Not explicitly mentioned in the source [1-11].
* **DevEx Framework**: Not explicitly mentioned in the source [1-11].
* **DevSecOps Platform Context**: Mentioned and recommended as the underlying intelligent orchestration framework for embedding context, traceability, and governance into the software development lifecycle [1, 5, 7].
* **AI Accountability Framework**: Defined in the report as the organizational and technical capability to answer three core questions about any line of AI-generated code: (1) Where did it come from?, (2) What was it meant to do?, and (3) Who is responsible for it once in production? [1].
* **The "AI Paradox" Concept**: Introduced to explain the divergence where individual developer coding speed increases while the overall end-to-end software delivery process remains constrained by downstream validation bottlenecks [2, 4].

---

## Metricas Mencionadas

* **AI Tool Adoption Depth**: 91% of organizations have 2 or more AI coding tools in active use; 54% have 3 or more [1, 2].
* **Governance Policy Lag**: 80% agree their organization adopted AI tools faster than it developed policies to govern them [1, 3].
* **Governance Challenges**: 92% report governance challenges with AI-generated code [1, 3].
* **Code Output Velocity**: 78% report developers are writing and committing code faster since adopting AI tools [1, 2].
* **ROI Expectation Rate**: 60% report AI coding ROI has exceeded expectations [2].
* **Individual Developer Productivity**: 79% agree individual developer productivity has improved with AI tools [2].
* **Perceived Code Quality**: 73% report overall code quality has improved [2].
* **Technical Debt Risk**: 82% state AI-generated code risks creating a new form of technical debt organizations are not prepared to manage [1, 2].
* **Code Maintainability Concern**: 73% express concern regarding the maintainability of AI-generated code in their codebase [1].
* **Code Origin Indistinguishability**: 43% cannot reliably distinguish AI-generated code from human-written code [1, 4].
* **Review & Validation Bottleneck Shift**: 85% agree AI has shifted the delivery bottleneck from writing code to reviewing and validating it [4].
* **Post-Creation Governance Challenge**: 84% agree the biggest challenge with AI-generated code is governing what happens to it after creation [4].
* **Incident Traceability Gap**: 87% are confident they could determine within 24 hours whether AI-generated code caused an incident, yet 34% of organizations experiencing an incident in the past year failed to make that determination [4].
* **Structural Toolchain Barriers**: 40% cite fragmented toolchains and 39% cite systems that do not track code origin as top barriers to control [4].
* **SDLC Data Integration**: Only 28% report their software development lifecycle tools are fully integrated with shared data and workflows [3].
* **Code Accumulation Risk**: 83% identify AI-generated code accumulation as a current risk (44% label it a top technology risk) [3].
* **Governance Investment Intent**: 91% are likely to invest in AI code governance tools in the next 12 months; 98% have allocated or expect to allocate budget [3].
* **Future Strategic Focus**: 85% agree the next phase of AI in software will focus less on generating code and more on governing it [5].

---

## Insights para Praticantes

* **Resolve the AI Paradox Downstream**: Accelerating code writing alone does not speed up software delivery; software engineering teams must optimize code review, verification, and testing processes where bottlenecks now reside [2, 4].
* **Implement Provenance and Ownership Controls**: Establish organizational capabilities and platform telemetry to answer where AI code came from, what its purpose was, and who owns it in production [1].
* **Consolidate Fragmented Toolchains**: Integrate software development lifecycle (SDLC) tools around shared context and unified data graphs rather than relying on point solutions [3-5].
* **Manage Technical Debt Proactively**: Track AI code accumulation and maintainability risks early to prevent unmanageable technical debt and production incidents [1-3].
* **Shift from Code Generation to Code Governance**: Shift engineering management focus toward context, traceability, and governance built directly into DevSecOps platforms [3, 5].

---

## Avaliacao de Qualidade GL (Garousi et al.)

| Criterio | Pontuacao (0-1) |
|----------|----------------|
| Autoridade do autor/organizacao | 1.0 |
| Descricao de metodologia | 1.0 |
| Data de publicacao | 1.0 |
| Objetividade (vies comercial) | 0.5 |
| Referencias citadas | 0.0 |
| Contribuicao nova | 1.0 |
| **TOTAL** | **4.5/6** |

---

*Extraido via NotebookLM em October 2026 para MLR: Software Developer Metrics in Practice*

---

💡 **Próximo passo:** Se desejar, posso converter esta análise em um relatório executivo em PDF ou criar uma apresentação visual comparando estes dados de governança de IA com outras fontes do seu projeto.
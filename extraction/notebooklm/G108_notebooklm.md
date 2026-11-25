# G108 — The struggle to prove AI productivity gains

**Decisao: INCLUIDO | Qualidade GL: 4.5/6**

---

## Dados Bibliograficos

| Campo | Valor |
|-------|-------|
| **ID** | G108 |
| **Autor/Organizacao** | Michael Hill / LeadDev |
| **Data** | March 25, 2026 |
| **Tipo** | Blog post / Industry article |
| **URL** | https://leaddev.com/ai/the-struggle-to-prove-ai-productivity-gains |

---

## Resumo

Despite near-universal exploration and adoption of AI-coding tools across software organizations (98% according to LeadDev's AI Impact Report 2025), companies struggle to measure and prove tangible productivity gains [1-3]. A study by Multitudes involving over 700 engineering professionals found that 75% of respondents struggle to measure AI's impact on engineering productivity [2]. This comes amid escalating executive expectations: 40% of participants feel board-level pressure to adopt AI tools, and 39% feel pressure to deliver outcome improvements, with 60% citing productivity as the primary required outcome [4]. Meanwhile, traditional productivity metrics—such as lines of code—break down in AI-assisted workflows, leaving productivity cited by 26% of respondents as the most difficult factor to gauge [2, 3, 5].

Measuring productivity in the era of AI is uniquely complex because software development is collaborative knowledge work, and AI changes workflows across the entire path from idea to production [5, 6]. Conventional activity metrics can be misleading because AI may inflate code volume while reducing quality, or decrease code volume by generating more concise, efficient solutions [7]. Furthermore, rapid code generation moves the primary workflow bottleneck upstream to problem definition and task specification—determining what to build next—which legacy code-focused metrics fail to capture [8]. This measurement gap is compounded by a lack of structured goal setting: only 31% of organizations have OKRs in place to measure AI tooling impact, and only 15% track speed and velocity impacts with OKRs despite 86% wanting to use AI to move faster [7].

To address these challenges, experts advocate treating productivity as a system-level outcome rather than relying on a single metric [9]. Lauren Peate (CEO of Multitudes) recommends a three-tiered measurement approach: defining clear goals, adopting feasible "good enough" metrics across four key buckets (AI usage data, customer value delivered, customer pain created, and human impact), and using metrics to drive continuous experimentation [9-11]. Krishnan Sridhar (VP of Engineering at LinkedIn) emphasizes evaluating flow, collaboration, decision-making, and software resilience to confirm whether teams are shipping on roadmaps faster and with confidence [9, 11, 12].

---

## Frameworks Mencionados

- **McKinsey Framework / Historical Benchmarks**: Mentioned as an example of persistent, unsuccessful industry attempts to measure engineering productivity ("Just ask McKinsey") [5].
- **Objectives and Key Results (OKRs)**: Discussed as a goal-tracking framework; 31% of organizations maintain AI-specific OKRs and 15% track speed and velocity impacts via OKRs [7].
- **DevEx / DevX**: Referenced within Krishnan Sridhar's corporate title ("VP of engineering, DevX and platforms at LinkedIn"), though not detailed as a standalone framework in the text [6].
- **System-Level Productivity Framework (Sridhar)**: Recommended framework evaluating productivity across flow, collaboration, judgment, decision-making, velocity, and quality across the end-to-end lifecycle [9, 12].
- **Three-Tiered Measurement Approach (Peate)**: Practical framework comprising (1) goal definition, (2) selection of feasible metrics across four buckets, and (3) continuous experimentation and progress tracking over time [9-11].
- **DORA & SPACE Frameworks**: **Not mentioned** in this source [1-15].

---

## Metricas Mencionadas

- **Lines of Code (LoC) / Code Volume**: Identified as a traditional activity metric that breaks down with AI coding tools, as AI can artificially inflate code output or decrease it via optimization [2, 5, 7].
- **AI Usage Telemetry (Tokens Used, Lines Accepted, Usage Cost, Intervention Dates)**: Recommended usage metrics to track adoption intensity and isolate pre- and post-AI experiment performance [11, 13].
- **Customer Value Delivered (Features Shipped, Pull Requests Shipped, Tickets Completed)**: Outcome-oriented metrics to evaluate functional output delivered to users [13].
- **Customer Pain Created (Incidents, Bug Reports, Leading Quality Indicators)**: Quality and resilience metrics used to monitor negative impacts or regressions caused by AI adoption [13].
- **Human Impact (Out-of-Hours Work)**: Developer wellbeing metric tracked to identify potential burnout or extra workload resulting from AI tool rollouts [12].
- **Speed & Velocity / Delivery Outcomes**: Tracked via speed/velocity OKRs to assess whether teams deliver roadmaps faster with confidence [7, 12].
- **Tech Debt & Output Quality**: Highlighted by survey respondents as critical factors impacted by AI adoption (cited by 13% and 11% of respondents, respectively) [3].

---

## Insights para Praticantes

- **Adopt a "Done is Better Than Perfect" Metric Strategy**: Focus on practical, feasible metrics tracked consistently across usage, value, quality, and human impact rather than seeking an impossibly perfect metric [2, 9].
- **Expand Measurement Upstream Across the Lifecycle**: Recognize that AI accelerates code generation, shifting the key bottleneck upstream to problem definition, user research, and task preparation [6, 8].
- **Run Controlled Pre/Post AI Experiments**: Compare performance before and after AI deployment, and contrast high AI adopters against low adopters to isolate AI's true impact [13].
- **Align Board Expectations via Leadership Education**: Proactively educate leadership and reset board expectations around outcome-focused metrics rather than raw tool usage or vanity adoption counts [4, 12].
- **Incorporate Leading Indicators for Quality and Wellbeing**: Track leading indicators for bugs/incidents and monitor out-of-hours work to prevent quality degradation or engineer burnout [12, 13].

---

## Avaliacao de Qualidade GL (Garousi et al.)

| Criterio | Pontuacao (0-1) |
|----------|----------------|
| Autoridade do autor/organizacao | 1.0 |
| Descricao de metodologia | 0.5 |
| Data de publicacao | 1.0 |
| Objetividade (vies comercial) | 0.5 |
| Referencias citadas | 0.5 |
| Contribuicao nova | 1.0 |
| **TOTAL** | **4.5/6** |

---

*Extraido via NotebookLM em October 2026 para MLR: Software Developer Metrics in Practice*

💡 Would you like me to analyze another grey literature source for your systematic review or export this summary into a report artifact?
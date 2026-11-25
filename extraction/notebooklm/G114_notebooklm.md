# G114 — How tech companies measure the impact of AI on software development

**Decisao: INCLUIDO | Qualidade GL: 5.5/6**

---

## Dados Bibliograficos

| Campo | Valor |
|-------|-------|
| **ID** | G114 |
| **Autor/Organizacao** | Gergely Orosz and Laura Tacho (The Pragmatic Engineer / DX) |
| **Data** | September 16, 2025 |
| **Tipo** | Blog post / Industry newsletter deepdive |
| **URL** | https://newsletter.pragmaticengineer.com/p/how-tech-companies-measure-the-impact-of-ai |

---

## Resumo

This deepdive article, authored by Gergely Orosz and Laura Tacho (CTO at DX), investigates how 18 major tech companies—including Google, GitHub, Microsoft, Dropbox, Monzo, Atlassian, Adyen, Booking.com, Grammarly, Webflow, and Glassdoor—measure the real-world impact of AI coding tools on software development. While 85% of software engineers report using AI tools at work, 60% of engineering leaders cite a lack of clear metrics as their primary AI challenge. The article highlights a significant "measurement gap," criticizing one-dimensional industry headlines that focus almost exclusively on lines of code (LOC) generated or acceptance rates while ignoring long-term code quality, maintainability, innovation, and developer experience.

The authors demonstrate that evaluating AI impact does not require inventing completely new metrics. Instead, organizations should build on established "core" engineering metrics—such as Pull Request (PR) Throughput, PR Cycle Time, and Change Failure Rate—and combine them with targeted AI metrics like Daily/Weekly Active Users, Customer Satisfaction (CSAT) of AI tools, time saved per engineer, and AI spend. By slicing and dicing data across user cohorts (such as role, tenure, programming language, and AI usage level), companies like Webflow and Dropbox identified a ~20% increase in PR throughput among regular AI users, while observing that senior engineers may experience temporary slowdowns due to increased code review demands.

The article introduces the AI Measurement Framework (co-developed by Laura Tacho and Abi Noda) and details three complementary data collection mechanisms: quantitative systems data (VCS, CI/CD, admin APIs), qualitative periodic surveys (measuring change confidence, code maintainability, and DevEx), and experience sampling (in-the-moment feedback). Additionally, a practitioner case study interview with Suhail Patel (Platform Lead at Monzo Bank) reveals practical challenges: AI vendors often hoard usage telemetry, AI tools deliver massive efficiency gains (40–60% effort reduction) specifically on code migrations and boilerplate tasks, and companies must enforce strict guardrails to prevent AI models from indexing or leaking sensitive customer data.

---

## Frameworks Mencionados

- **AI Measurement Framework** (co-authored by Laura Tacho and Abi Noda): **Recommended & Discussed.** Synthesizes field research and data from over 400 companies to recommend a balanced set of AI adoption/usage metrics alongside core engineering metrics, placing Developer Experience (DevEx) at the center across speed, quality, and maintainability.
- **Core 4 Framework**: **Recommended & Discussed.** Utilized by companies such as Dropbox, Adyen, and Booking.com to track foundational software delivery metrics (e.g., PR Throughput and Change Failure Rate) as a baseline before and during AI tool deployment.
- **Developer Experience (DevEx) Framework / Developer Experience Index**: **Recommended & Discussed.** Used to track and reduce friction across the entire software development lifecycle (planning, building, testing, release, and production support) to ensure AI speed gains do not introduce friction downstream.
- **DORA / Speed & Quality Metrics Framework**: **Recommended & Discussed.** Metrics such as Change Failure Rate, Deployment Frequency, and PR Cycle Time are highlighted as necessary counter-balances to track reliability alongside speed.
- **McKinsey Developer Productivity Model**: **Critiqued.** Referenced in contrast as a flawed, single-metric attempt to measure developer productivity that was publicly countered by Kent Beck and Gergely Orosz.

---

## Metricas Mencionadas

- **Lines of Code (LOC) / AI-Generated LOC**: **Critiqued.** Widely cited in headlines (e.g., Google reporting 25% and Microsoft 30% AI-generated code), but criticized as a misleading, superficial metric that risks accumulating technical debt.
- **Acceptance Rate**: **Critiqued / Limited Scope.** Measures the percentage of AI coding suggestions accepted in the IDE. Used by GitHub (for Copilot product decisions), T-Mobile, and Atlassian, but noted as declining in popularity because it ignores long-term code maintainability, reverted code, and actual developer productivity.
- **Pull Request (PR) Throughput**: **Recommended.** Number of merged pull requests per developer/week. Dropbox and Webflow report a ~20% boost in PR throughput for regular AI users compared to non-AI users.
- **Change Failure Rate (CFR)**: **Recommended.** Percentage of deployments causing production failures. Tracked alongside PR throughput by nearly all profiled companies (e.g., Dropbox) to ensure speed increases do not compromise system stability.
- **PR Cycle Time & Deployment Frequency**: **Recommended.** System-level speed metrics measured via source control and CI/CD build tools.
- **Daily Active Users (DAU) & Weekly Active Users (WAU)**: **Recommended.** Tracks organizational adoption levels of AI tools (e.g., Dropbox achieved 90% WAU).
- **Customer Satisfaction (CSAT) / Developer Satisfaction with AI Tools**: **Recommended.** Measured by ~75% of profiled companies to evaluate developer sentiment and sustainable tooling practices.
- **Time Saved per Engineer**: **Recommended.** Self-reported metric quantifying weekly or daily time savings attributed to AI tools.
- **Bad Developer Day (BDD)**: **Discussed (Microsoft).** Measures daily friction and toil (time spent on incident mitigation, compliance, meeting overhead, task management) balanced against PR coding activity.
- **Experimentation Rate (A/B Tests per Month)**: **Discussed (Glassdoor).** Tracks the number of monthly A/B tests to assess how AI tools accelerate prototyping and innovation.
- **Percentage Capacity Worked / Capacity Utilization Rate**: **Discussed (Glassdoor).** Compares total potential vs. actual utilization of an AI tool to detect usage plateaus and guide tool budget reallocations.
- **AI Spend / Token Consumption / Cost Analysis**: **Discussed.** Tracking financial investment, token consumption, and R&D budget shifts (e.g., Shopify using an AI Leaderboard to track individual developer token usage).
- **Change Confidence**: **Recommended (Survey-based).** Developer self-reported confidence that a proposed code change will not break production.
- **Code Maintainability & Perception of Quality**: **Recommended (Survey-based).** Evaluates code readability, ease of modification, and whether AI usage accumulates technical debt.

---

## Insights para Praticantes

- **Pair Speed Metrics with Quality Safeguards**: Always track speed metrics (e.g., PR Throughput) alongside quality and stability safeguards (e.g., Change Failure Rate, Change Confidence) to prevent AI-generated code from creating long-term technical debt.
- **Establish Solid Performance Baselines First**: Companies that already track foundational engineering efficiency (using frameworks like Core 4 or DevEx) can measure AI impact far more effectively. Establish baseline measurements before introducing new AI tools.
- **Segment Data Across Developer Cohorts**: Slicing metrics by tenure, role, programming language, and AI usage level helps pinpoint high-impact use cases (e.g., 3+ year tenure devs gaining maximum speed) and identifies bottlenecks (e.g., senior devs spending extra time reviewing junior AI-generated code).
- **Protect Developer Experience (DevEx)**: Removing friction in code authoring can inadvertently add friction to code reviews, testing, or incident handling. Regularly measure developer satisfaction (CSAT) to ensure sustainable adoption.
- **Use a Multi-Modal Measurement Strategy**: Combine quantitative system data (VCS, CI/CD, vendor APIs) for output metrics with qualitative periodic surveys (for maintainability and change confidence) and experience sampling (for real-time workflow friction).
- **Practical Takeaways from Monzo Bank Case Study**:
  - **High-Value Use Cases**: AI tools provide the greatest tangible return (40–60% effort reduction) on structured, repetitive tasks such as code migrations, dependency updates, and boilerplate generation.
  - **Security & Data Privacy Guardrails**: Establish strict boundaries preventing AI models from indexing customer data, sensitive databases, or internal credentials.
  - **Vendor Telemetry Limitations**: Do not rely solely on vendor-provided metrics (like acceptance rate), as vendors often obscure detailed usage telemetry to maintain platform lock-in.
  - **Hiring & Retention**: Providing best-in-class AI tooling is increasingly crucial for recruiting and retaining senior software engineering talent.
  - **Cost Awareness**: Monitor token costs and optimize tool defaults (e.g., disabling automatic AI code reviews if they generate low-value noise at high token cost).

---

## Avaliacao de Qualidade GL (Garousi et al.)

| Criterio | Pontuacao (0-1) |
|----------|----------------|
| Autoridade do autor/organizacao | 1.0 |
| Descricao de metodologia | 1.0 |
| Data de publicacao | 1.0 |
| Objetividade (vies comercial) | 0.5 |
| Referencias citadas | 1.0 |
| Contribuicao nova | 1.0 |
| **TOTAL** | **5.5/6** |

---

*Extraido via NotebookLM em October 2026 para MLR: Software Developer Metrics in Practice*
# G102 — 2026 Software Engineering Benchmarks Report

**Decisao: INCLUIDO | Qualidade GL: 4/6**

---

## Dados Bibliograficos

| Campo | Valor |
|-------|-------|
| **ID** | G102 |
| **Autor/Organizacao** | LinearB |
| **Data** | 2026 |
| **Tipo** | Industry report |
| **URL** | https://linearb.io/resources/software-engineering-benchmarks-report |

---

## Resumo

The **2026 Software Engineering Benchmarks Report** by LinearB analyzes dataset findings from over 8.1 million pull requests across 4,800+ organizations worldwide, combined with data from the 2026 AI in Engineering Leadership survey. The report establishes industry standards across 20 metrics spanning the entire SDLC, structured around delivery, predictability, and project management.

A central focus of this year's edition is the measurement of AI tools and their impact on delivery velocity, code quality, and team health. The findings highlight significant operational differences between AI-generated and manual pull requests: AI PRs experience a 4.6x longer wait time before review starts, but are reviewed 2x faster once picked up by reviewers. Furthermore, acceptance rates for AI-generated PRs are substantially lower (32.7%) compared to manual PRs (84.4%).

The report also gathers qualitative perspectives from engineering leaders regarding AI adoption concerns, code quality confidence, and expected AI impact over the next 12 months. Additionally, it highlights tool-specific performance trends (such as Devin and Copilot) and discusses the necessity of a context layer to make agentic software factories measurable and prove AI ROI.

---

## Frameworks Mencionados

- **DORA / Classic SDLC Delivery Frameworks**: Not explicitly named as "DORA" in the text, but classic DORA metrics (Cycle Time, Deploy Frequency, Change Failure Rate) are incorporated as core benchmark categories for Delivery and Predictability.
- **Agentic Software Factory Framework / Context Layer**: Discussed as an operational framework to establish a context layer for measuring cost per effective PR and agentic PR yield.

---

## Metricas Mencionadas

- **Delivery Metrics**:
  - **Cycle Time**: Benchmark spanning full SDLC delivery.
  - **Deploy Frequency**: Benchmark for deployment cadence.
  - **PR Size**: Measurement of pull request volume/scope.
- **Predictability Metrics**:
  - **Change Failure Rate**: Metric tracking deployment failure occurrences.
  - **Rework Rate**: Metric measuring code modification/refactoring after initial write.
  - **Planning Accuracy**: Predictability metric measuring planned vs. delivered work.
- **Project Management Metrics**:
  - **Issues Linked to Parents**: Traceability metric for task hierarchy.
  - **In Progress Issues with Assignees**: Work-in-progress governance metric.
- **AI Productivity & Review Metrics**:
  - **AI PR Wait Time Before Review**: AI PRs wait 4.6x longer prior to initial review compared to baseline.
  - **AI PR Review Speed**: AI PRs are reviewed 2x faster once review begins.
  - **Acceptance Rate (AI-generated PRs vs. Manual PRs)**: AI-generated PR acceptance rate is 32.7% versus 84.4% for manual PRs.
  - **Bot Acceptance Rates by Tool**: Tracks tool-specific acceptance rate trajectories (e.g., Devin rising since April, Copilot slipping since May).
  - **Cost per Effective PR**: AI ROI metric measured within the software factory context layer.
  - **Agentic PR Yield**: Benchmark metric for automated/agentic code generation output.

---

## Insights para Praticantes

- **Address AI Review Bottlenecks**: AI code generation increases pull request volume, causing AI PRs to wait 4.6x longer for initial review. Engineering teams must adapt review workflows to prevent PR queue stagnation.
- **Focus on Code Quality over Generation Speed**: The low acceptance rate of AI-generated PRs (32.7% vs. 84.4% for manual code) indicates that raw code generation does not automatically translate into merged production code.
- **Monitor Tool-Specific Variance**: Bot performance and acceptance rates vary across tools and drift over time (e.g., Devin vs. Copilot trends), requiring ongoing tool evaluation.
- **Implement a Context Layer for AI ROI**: Measuring AI ROI in modern software factories requires going beyond output volume to track metrics like cost per effective PR and agentic PR yield.

---

## Avaliacao de Qualidade GL (Garousi et al.)

| Criterio | Pontuacao (0-1) |
|----------|----------------|
| Autoridade do autor/organizacao | 1.0 |
| Descricao de metodologia | 0.5 |
| Data de publicacao | 1.0 |
| Objetividade (vies comercial) | 0.5 |
| Referencias citadas | 0.0 |
| Contribuicao nova | 1.0 |
| **TOTAL** | **4.0/6** |

---

*Extraido via NotebookLM em October 2026 para MLR: Software Developer Metrics in Practice*
# G018 — Software Development Metrics Guide: Benchmarks & Best Practices

**Decisao: INCLUIDO (Guia abrangente de metricas de desenvolvimento com benchmarks empiricos de 6.1M PRs: DORA, leading indicators, developer experience, investimento e previsibilidade) | Qualidade: 4/5**

> Extracao regenerada a partir do conteudo completo da pagina (fetch da URL oficial). Substitui a versao anterior que continha apenas placeholder.

---

## Dados Bibliograficos

| Campo | Valor |
|-------|-------|
| **ID** | G018 |
| **Autores** | Cecilia Tao (LinearB) |
| **Ano** | 2025 (jul/2025) |
| **Venue** | LinearB Blog |
| **URL** | https://linearb.io/blog/software-development-metrics-guide |
| **Tipo** | Blog / Guia |
| **GL Tier** | 2nd (Vendor blog/guide) |
| **Metodo** | Sintese de benchmarks a partir de dados de produto (6.1M pull requests, 3.000+ times) |
| **Contexto** | Times de engenharia de software (startups a enterprise; 32 paises, 167.437 contribuidores) |

---

## Objetivo
Fornecer um guia pratico de metricas de desenvolvimento de software, com benchmarks empiricos
derivados da analise de 6.1 milhoes de pull requests de 3.000+ times, cobrindo desde metricas
DORA ate leading indicators, developer experience, investimento de engenharia e previsibilidade,
com estrategias de implementacao.

---

## Frameworks e Metricas

### Frameworks Mencionados
- DORA (DevOps Research and Assessment) - 4 metricas + benchmarks Elite/Good/Fair/Needs-Focus
- Developer Experience (DevEx) e Developer Productivity (DevProd) como duas dimensoes-chave
- (SPACE nao e discutido; sem framework DevEx formal de Noda/Storey, mas trata "developer experience" substantivamente)

### Metricas Propostas/Discutidas
- **DORA:** Cycle Time (Elite <26h), Deployment Frequency (Elite >1/service/dia), Change Failure Rate (Elite <1%), MTTR (Elite <6h). Correlacoes: 2.6x crescimento de receita, 2.1x retencao, 1.8x satisfacao do cliente.
- **Leading indicators:** PR size (<194), PR Maturity (>91%), Pickup/Approve/Merge time, Refactor Rate vs Rework Rate, work distribution.
- **Developer Experience:** Focus Time, Task Balance, Developer Toil (<15%), Unplanned work, WIP limits, Meeting Team Goals — ligados a satisfacao, engajamento, burnout, retencao.
- **Engineering investment:** New Value (55%), Feature Enhancements (20%), DevEx Improvements (15%), KTLO (10%).
- **Previsibilidade/planejamento:** Planning Accuracy (75-96%), Capacity Accuracy (>80%), PM hygiene (issues/branches linked, estimation, assignees).

---

## Impacto de IA
O corpo do guia NAO discute IA de forma substantiva (o tema central sao metricas e benchmarks).
Ha mencoes de produto/navegacao a "AI era" e "Measuring AI Impact", mas sem analise.

---

## Principais Contribuicoes
- Benchmarks empiricos por tier (Elite/Good/Fair/Needs-Focus) para DORA e leading indicators,
  derivados de 6.1M PRs - referencia pratica para comparacao.
- Articula DORA (lagging) + leading indicators preditivos + developer experience + investimento
  num programa de metricas coerente.
- Enfatiza o equilibrio entre produtividade de entrega e experiencia/bem-estar do desenvolvedor
  (burnout, toil, focus time) para performance sustentavel.

---

## Contexto de Aplicacao
Blog/guia de fornecedor (LinearB) para lideres de engenharia. Dados de benchmark vem do produto
da LinearB; conteudo prescritivo, mas ancorado em dados reais (nao estudo academico).

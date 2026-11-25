# G013 — Value Stream Analytics - GitLab Docs

**Decisao: INCLUIDO (Mede o fluxo de valor e o desempenho do ciclo de vida do desenvolvimento, incl. metricas DORA e de fluxo) | Qualidade: 4/5**

> Extracao regenerada a partir do conteudo completo da pagina (fetch da URL oficial). Substitui a versao anterior que continha apenas placeholder ("collect via browser").

---

## Dados Bibliograficos

| Campo | Valor |
|-------|-------|
| **ID** | G013 |
| **Autores** | GitLab Inc. |
| **Ano** | 2024 |
| **Venue** | GitLab Documentation |
| **URL** | https://docs.gitlab.com/user/group/value_stream_analytics/ |
| **Tipo** | Documentacao Tecnica |
| **GL Tier** | 2nd (Vendor Documentation) |
| **Metodo** | Documentacao de produto (ferramenta de analytics de fluxo) |
| **Contexto** | Plataforma GitLab (Free/Premium/Ultimate; GitLab.com, Self-Managed, Dedicated) |

---

## Objetivo
Documentar o Value Stream Analytics (VSA) do GitLab: ferramenta que calcula a duracao de cada
estagio do processo de desenvolvimento (da ideia a producao) a partir de eventos de issues e
merge requests, para medir velocidade, identificar gargalos e ineficiencias, e otimizar o fluxo
de entrega de valor no SDLC.

---

## Frameworks e Metricas

### Frameworks Mencionados
- Value Stream Analytics (VSA) / Value Stream Management (VSM)
- DORA (DevOps Research and Assessment) - 4 metricas (nivel Ultimate)
- Modelo de estagios do ciclo de vida (Issue, Plan, Code, Test, Review, Staging)

### Metricas Propostas/Discutidas
- **Duracao por estagio (mediana):** Issue, Plan, Code, Test (pipeline CI/CD), Review (revisao de MR), Staging (merge -> deploy em producao).
- **Metricas de ciclo de vida:** Lead time (issue criada -> fechada); Cycle time (commit que referencia a issue -> issue fechada); New issues; Deploys.
- **DORA (Ultimate):** Deployment frequency, Lead time for changes, Time to restore service, Change failure rate.
- **Tasks by type:** tarefas concluidas (issues fechadas + MRs mergeados) por dia.
- **Total time chart:** media de dias para os ciclos de desenvolvimento completarem.
- **Cumulative label event duration** (estagios baseados em labels).

---

## Impacto de IA
A pagina do Value Stream Analytics NAO discute IA/GitLab Duo (diferente do Value Streams
Dashboard, G012). Foco em metricas de fluxo, ciclo de vida e DORA.

---

## Principais Contribuicoes
- Operacionaliza a medicao de fluxo de valor (idea-to-production) por estagios, com eventos
  configuraveis (timestamp e label-based) e estagios customizados.
- Integra metricas de fluxo/lifecycle com as metricas DORA num unico painel de Overview.
- Expoe API GraphQL para exportacao de metricas (count, median, average por estagio) e relatorios.

---

## Contexto de Aplicacao
Documentacao de fornecedor (GitLab) voltada a equipes que medem e otimizam o fluxo de entrega
(lead time, cycle time, gargalos por estagio). Material prescritivo/de produto, sem estudo
empirico proprio.

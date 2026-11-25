# G012 — Value Streams Dashboard - GitLab Docs

**Decisao: INCLUIDO (Discute medicao de software delivery performance, fluxo de valor e impacto de IA no SDLC) | Qualidade: 4/5**

> Extracao regenerada a partir do conteudo completo da pagina (fetch da URL oficial). Substitui a versao anterior que continha apenas placeholder ("collect via browser").

---

## Dados Bibliograficos

| Campo | Valor |
|-------|-------|
| **ID** | G012 |
| **Autores** | GitLab Inc. |
| **Ano** | 2024 |
| **Venue** | GitLab Documentation |
| **URL** | https://docs.gitlab.com/user/analytics/value_streams_dashboard/ |
| **Tipo** | Documentacao Tecnica |
| **GL Tier** | 2nd (Vendor Documentation) |
| **Metodo** | Documentacao de produto (painel de analytics) |
| **Contexto** | Plataforma GitLab (Premium/Ultimate; GitLab.com, Self-Managed, Dedicated) |

---

## Objetivo
Documentar o Value Streams Dashboard do GitLab: um painel centralizado e customizavel que
funciona como single source of truth (SSOT), reunindo metricas de DORA, fluxo de valor (Value
Stream Analytics), seguranca/vulnerabilidades e uso de IA (GitLab Duo). Permite identificar
tendencias e padroes, comparar desempenho entre grupos/projetos/equipes, e demonstrar o ROI
de investimentos em IA no ciclo de desenvolvimento (SDLC).

---

## Frameworks e Metricas

### Frameworks Mencionados
- DORA (DevOps Research and Assessment) - 4 metricas-chave + DORA Performers score (high/medium/low)
- Value Stream Analytics (VSA) / flow metrics
- Value Stream Management (VSM)
- GitLab Duo (assistente de IA) - Code Suggestions, Chat, Root Cause Analysis

### Metricas Propostas/Discutidas
- **DORA (delivery/estabilidade):** Deployment frequency, Lead time for changes, Time to restore service, Change failure rate (com limiares high/medium/low explicitos).
- **Fluxo (VSA):** Lead time (issue criada -> fechada), Cycle time (commit -> issue fechada).
- **Output/atividade:** Issues criadas, Issues fechadas, Number of deploys, Merge request throughput, Median time to merge, Contributor count.
- **Seguranca:** Vulnerabilidades criticas e altas ao longo do tempo.
- **CI/CD:** Total pipeline runs, Pipeline median duration, Pipeline success rate, Pipeline failure rate.
- **IA (GitLab Duo):** Feature usage, Code Suggestions usage, Code Suggestions acceptance rate, Chat usage, Root Cause Analysis usage.

---

## Impacto de IA
A documentacao posiciona o dashboard como instrumento para "entender o impacto de adicionar IA
ao SDLC e demonstrar o ROI dos investimentos em GitLab Duo". A visualizacao `ai_impact_table`
e as metricas de uso/aceitacao de Code Suggestions permitem acompanhar a adocao e o efeito da
IA junto das metricas DORA e de fluxo. Relevante para a RQ3 (impacto da IA na medicao).

---

## Principais Contribuicoes
- Consolida, em um unico painel (SSOT), metricas de entrega (DORA), fluxo de valor, seguranca e IA.
- Operacionaliza o DORA Performers score com limiares quantitativos por categoria.
- Comparacao mes a mes (DevSecOps metrics comparison) com Change % e tendencias, e drill-down por projeto/metrica.
- Dashboards customizaveis via YAML versionado; relatorios agendaveis via GraphQL API.

---

## Contexto de Aplicacao
Documentacao de fornecedor (GitLab) voltada a organizacoes que usam a plataforma para medir e
melhorar desempenho de DevOps/entrega de software e, mais recentemente, o impacto da IA. Sem
estudo empirico proprio; e material prescritivo/de produto.

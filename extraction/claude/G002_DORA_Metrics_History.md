# G002 — A History of DORA's Software Delivery Metrics

**Decisão: INCLUIDO | Qualidade: 5/5**

---

## Dados Bibliograficos

| Campo | Valor |
|-------|-------|
| **ID** | G002 |
| **Autores** | Nathen Harvey (DORA) |
| **Ano** | 2026 |
| **Venue** | dora.dev |
| **URL** | https://dora.dev/guides/dora-metrics/history/ |
| **Tipo** | Documentation |
| **GL Tier** | 1st tier (Official DORA source) |
| **Metodo** | Histórico de evolução de métricas |
| **Contexto** | Documentação técnica mostrando evolução temporal das métricas DORA desde 2014 |

---

## Objetivo

Documentar a evolução histórica das métricas de desempenho de entrega de software da DORA ao longo de mais de uma década de pesquisa, explicando as mudanças nas definições, nomes e escopo que refletem a mudança das realidades tecnológicas.

---

## Frameworks e Metricas

### Frameworks Mencionados
- DORA Software Delivery Performance Metrics (evolução de 4 para 5 métricas)

### Metricas Propostas/Discutidas
- **2014-2015 (4 métricas iniciais):**
  - Deployment frequency
  - Lead time for changes
  - Mean time to recover (MTTR)
  - Change fail rate
- **2016-2018 (padronização):**
  - Throughput: Deployment frequency, Deployment lead time
  - Stability: MTTR, Change fail rate
  - Availability (adicionada em 2018)
- **2021-2023 (refinamento):**
  - Reliability (substituindo Availability)
  - Failed deployment recovery time (renomeação de MTTR)
- **2024 (5 métricas):**
  - Deployment rework rate (nova métrica)

---

## Principais Contribuicoes

- **Evolução das definições:** Demonstra como as métricas evoluíram de uma perspectiva simplificada (3-4 métricas) para um modelo mais nuançado (5 métricas) refletindo maturidade da indústria
- **Distinção terminológica:** Esclarece mudanças importantes como a renomeação de MTTR para Failed deployment recovery time para excluir falhas não relacionadas a mudanças de software
- **Separação de conceitos:** Diferencia entre medidas de software delivery e medidas de performance operacional (reliability vs availability)
- **Validação de modelos de negócio:** A evolução demonstra o refinamento científico contínuo, com mudanças baseadas em análise estatística e feedback da indústria
- **Inclusão de retrabalho:** A adição da quinta métrica (deployment rework rate) em 2024 reconhece explicitamente o impacto do retrabalho na produtividade

---

## Contribuicao Principal

Este documento fornece contexto histórico crucial para compreender a origem e evolução do framework DORA. Demonstra como as métricas foram refinadas ao longo de uma década através de pesquisa rigorosa e feedback da indústria, validando a robustez do modelo atual. A contribuição principal é evidenciar que o framework DORA não é estático, mas evolui continuamente para refletir melhor compreensão científica do desempenho de entrega de software e mudanças na paisagem tecnológica.

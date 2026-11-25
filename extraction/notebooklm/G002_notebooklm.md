# G002 — A History of DORA's Software Delivery Metrics

**Decisao: INCLUIDO | Qualidade GL: 5/6**

---

## Dados Bibliograficos

| Campo | Valor |
|-------|-------|
| **ID** | G002 |
| **Autor/Organizacao** | Nathen Harvey / DORA [1] |
| **Data** | January 5, 2026 [2] |
| **Tipo** | Documentation / Guide [1] |
| **URL** | https://dora.dev/guides/dora-metrics/history/ [1] |

---

## Resumo

Este documento descreve a evolução histórica das métricas de desempenho de entrega de software estabelecidas pela DORA ao longo de mais de uma década [1]. O texto detalha como as métricas deixaram de ser uma definição estática de "IT performance" para se tornarem um modelo dinâmico que reflete as mudanças no cenário tecnológico, evoluindo de quatro para cinco métricas fundamentais [1, 3].

A narrativa destaca marcos importantes, como a solidificação da dualidade entre **Throughput** e **Stability** em 2015 e a introdução de **Availability** e **Reliability** entre 2018 e 2021 para medir a saúde operacional [4, 5]. Em 2023 e 2024, o framework passou por refinamentos significativos, incluindo a redefinição de métricas de recuperação e a introdução de uma métrica específica para **rework** [3, 6].

---

## Frameworks Mencionados

*   **DORA**: Discutido como o framework de pesquisa principal que investiga capacidades de alta performance [1].
*   **Software Delivery and Operational (SDO) performance**: Mencionado como a expansão terminológica que inclui saúde operacional além da entrega de software [5].

---

## Metricas Mencionadas

*   **Deployment frequency**: Utilizada desde 2014 para medir a frequência de mudanças em produção [3, 7].
*   **Lead time for changes / Change lead time**: Mede o tempo desde o commit do código até a implantação bem-sucedida [3, 7].
*   **Mean time to recover (MTTR) / Time to restore service**: Métrica original de estabilidade, posteriormente renomeada para foco estatístico [4, 6, 7].
*   **Change fail rate**: Percentual de implantações que causam falhas em produção [2, 4, 7].
*   **Availability**: Introduzida em 2018 para medir se as equipes cumprem promessas sobre o software operado [4, 5].
*   **Reliability**: Evolução da métrica de disponibilidade que abrange **latency**, **performance** e **scalability** [5].
*   **Failed deployment recovery time**: Redefinição de 2023 para o tempo de recuperação especificamente após uma mudança falha em produção [3, 6].
*   **Deployment rework rate**: A "quinta métrica" introduzida em 2024 para medir o volume de trabalho não planejado para corrigir bugs [2, 3].

---

## Insights para Praticantes

*   **Velocidade não sacrifica estabilidade**: Organizações de alta performance conseguem excelência tanto em **Throughput** quanto em **Stability** simultaneamente [4].
*   **Evolução da Recuperação**: A medição de tempo de recuperação deve focar em falhas causadas por mudanças de software para manter o alinhamento estatístico com outras métricas de entrega, distinguindo-as de falhas externas como quedas de data center [6].
*   **Rework como indicador**: A métrica de **change failure rate** atua como um proxy para a quantidade de **rework** que uma equipe deve realizar [3].
*   **Performance Operacional vs. Entrega**: Métricas como **Reliability** são consideradas medidas de performance operacional, enquanto as outras cinco métricas focam estritamente na entrega de software [3, 5].

---

## Avaliacao de Qualidade GL (Garousi et al.)

| Criterio | Pontuacao (0-1) |
|----------|----------------|
| Autoridade do autor/organizacao | 1 |
| Descricao de metodologia | 1 |
| Data de publicacao | 1 |
| Objetividade (vies comercial) | 1 |
| Referencias citadas | 0 |
| Contribuicao nova | 1 |
| **TOTAL** | **5/6** |

---

*Extraido via NotebookLM em March 2026 para MLR: Software Developer Metrics in Practice*
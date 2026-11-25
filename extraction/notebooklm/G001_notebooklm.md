# G001 — DORA's Software Delivery Performance Metrics - Guide

**Decisao: INCLUIDO | Qualidade GL: 6/6**

---

## Dados Bibliograficos

| Campo | Valor |
|-------|-------|
| **ID** | G001 |
| **Autor/Organizacao** | Nathen Harvey / DORA |
| **Data** | January 5, 2026 |
| **Tipo** | Documentation / Guide |
| **URL** | https://dora.dev/guides/dora-metrics/ |

---

## Resumo

Este guia detalha as cinco métricas de desempenho de entrega de software identificadas pela pesquisa do **DORA** para medir desfechos do processo de entrega, as quais são preditoras de performance organizacional e bem-estar dos membros da equipe [1]. As métricas evoluíram de um modelo original de quatro chaves para o atual modelo de cinco métricas, funcionando como **leading indicators** para performance organizacional e **lagging indicators** para práticas de desenvolvimento [1, 2].

O framework divide o desempenho em duas categorias principais: **throughput** (capacidade de mover mudanças pelo sistema com velocidade) e **instability** (qualidade e confiança nas implantações) [2, 3]. A fonte enfatiza que velocidade e estabilidade não são alvos de troca (**trade-offs**), mas sim correlacionados, onde equipes de alta performance apresentam excelência em ambos os aspectos simultaneamente [4, 5].

---

## Frameworks Mencionados

*   **DORA**: Framework principal discutido e recomendado para medir a performance de entrega de software [1, 2].

---

## Metricas Mencionadas

*   **Change lead time**: O tempo que uma mudança leva desde o *commit* no controle de versão até a implantação em produção [3].
*   **Deployment frequency**: O número de implantações em um período ou o tempo entre elas [3].
*   **Failed deployment recovery time**: O tempo necessário para recuperar de uma implantação que falhou e exigiu intervenção imediata [3].
*   **Change fail rate**: A proporção de implantações que requerem intervenção imediata (como *rollbacks* ou *hotfixes*) após o lançamento [3, 4].
*   **Deployment rework rate**: A proporção de implantações não planejadas que ocorrem devido a um incidente em produção [4].

---

## Insights para Praticantes

*   **Evite a Lei de Goodhart**: Não defina métricas como objetivos finais, pois isso incentiva as equipes a "jogarem" com os dados [6].
*   **Contexto é fundamental**: As métricas devem ser aplicadas ao nível de aplicação ou serviço individual, e não misturadas ou comparadas entre equipes com contextos diferentes [5-7].
*   **Propriedade Compartilhada**: As métricas devem ser compartilhadas entre desenvolvimento, operações e equipes de lançamento para promover colaboração [7].
*   **Foco na Melhoria, não apenas na Medição**: Reduzir o **batch size** das mudanças é uma estratégia recomendada para melhorar todas as métricas simultaneamente [8].
*   **Processo Iterativo**: O guia sugere estabelecer um *baseline* via **DORA Quick Check**, identificar gargalos e repetir o processo de melhoria continuamente [9].

---

## Avaliacao de Qualidade GL (Garousi et al.)

| Criterio | Pontuacao (0-1) |
|----------|----------------|
| Autoridade do autor/organizacao | 1 |
| Descricao de metodologia | 1 |
| Data de publicacao | 1 |
| Objetividade (vies comercial) | 1 |
| Referencias citadas | 1 |
| Contribuicao nova | 1 |
| **TOTAL** | **6/6** |

---

*Extraido via NotebookLM em March 2026 para MLR: Software Developer Metrics in Practice* [10, 11]
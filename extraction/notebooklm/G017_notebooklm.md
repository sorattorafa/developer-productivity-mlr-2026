# G017 — What are DORA Metrics and How to Unlock Elite Engineering Performance

**Decisão: INCLUIDO | Qualidade GL: 3.5/6**

---

## Dados Bibliográficos

| Campo | Valor |
|-------|-------|
| **ID** | G017 |
| **Autor/Organizacao** | Ben Lloyd Pearson / LinearB |
| **Data** | Não explicitada (Acesso em Março de 2026) |
| **Tipo** | Blog post |
| **URL** | https://linearb.io/blog/dora-metrics |

---

## Resumo

Este guia abrangente da LinearB detalha o programa **DORA**, fundado em 2015 por Gene Kim, Jez Humble e Nicole Forsgren, e posteriormente adquirido pelo Google Cloud em 2018 [1]. O texto explora como as capacidades de **software delivery** impactam o sucesso organizacional, destacando que equipes classificadas como "Elite" possuem 2x mais probabilidade de atingir metas de performance e 1.8x mais chances de reportar alta satisfação do cliente [1].

A fonte descreve as quatro métricas fundamentais (**Deployment Frequency, Change Lead Time, Change Fail Percentage** e **Failed Deployment Recovery Time**), fornecendo benchmarks específicos para performance de nível Elite [1, 2]. Além disso, discute estratégias de melhoria, componentes do **Cycle Time** e compara o framework DORA com outras abordagens emergentes no setor, como **SPACE** e **DevEx** [1, 3].

---

## Frameworks Mencionados

*   **DORA**: Discutido em detalhe e recomendado como base para medir capacidades de entrega baseadas em pesquisa [1].
*   **SPACE**: Mencionado em comparação para uma visão holística da produtividade (Satisfaction, Performance, Activity, Communication, Efficiency) [1].
*   **DevEx**: Mencionado em comparação, focado na experiência do desenvolvedor, incluindo **feedback loops**, **cognitive load** e **flow state** [1].
*   **DX Core 4**: Mencionado como um framework unificado focado em **Speed, Effectiveness, Quality** e **Impact** [1].

---

## Metricas Mencionadas

*   **Deployment Frequency**: Mede a frequência de deploy por serviço (Elite: >1 por dia) [1].
*   **Change Lead Time**: Tempo entre o commit e a produção (Elite: <26 horas); decomposto em **Coding time, Pickup time, Review time** e **Deploy time** [1, 3].
*   **Change Fail Percentage**: Taxa de falhas em mudanças (Elite: <1%) [1].
*   **Failed Deployment Recovery Time**: Tempo para restaurar o serviço após falha (Elite: <6 horas) [1].
*   **Planning Accuracy**: Citada como uma métrica ausente em frameworks tradicionais, mas essencial para previsibilidade [3].
*   **Cycle Time**: Métrica central no estudo de caso da Syngenta [3].
*   **Rework Percentage** e **Review Depth**: Identificadas como métricas importantes que faltam nos frameworks existentes [3].

---

## Insights para Praticantes

*   **Benchmarks de Elite**: Para atingir alta performance, as equipes devem buscar realizar deploys diários e manter o tempo de recuperação de falhas abaixo de 6 horas [1].
*   **Limitações de Frameworks**: Frameworks padrão como DORA podem ignorar aspectos críticos como **technical debt management**, **architecture stability** e **infrastructure reliability** [3].
*   **Escalabilidade e Eficiência**: O caso da Syngenta demonstra que é possível reduzir o **Cycle Time** em 81% e aumentar a **Planning Accuracy** em 33% mesmo durante um crescimento acelerado da equipe de 150 para 400 desenvolvedores [3].
*   **Foco no Review**: A análise do **Change Lead Time** revela que tempos de **Pickup** e **Review** são componentes acionáveis para otimizar o fluxo de entrega [3].

---

## Avaliacao de Qualidade GL (Garousi et al.)

| Criterio | Pontuacao (0-1) |
|----------|----------------|
| Autoridade do autor/organizacao | 1 |
| Descricao de metodologia | 0 |
| Data de publicacao | 0 |
| Objetividade (vies comercial) | 0.5 |
| Referencias citadas | 1 |
| Contribuicao nova | 1 |
| **TOTAL** | **3.5/6** |

---

*Extraído via NotebookLM em March 2026 para MLR: Software Developer Metrics in Practice*
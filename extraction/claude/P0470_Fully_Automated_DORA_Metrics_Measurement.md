# P0470 — Fully Automated DORA Metrics Measurement for Continuous Improvement

> Reextração corrigida a partir do PDF (a versão anterior trazia autor errado "Marques et al." e amostra inventada "múltiplos projetos OSS ao longo de anos"; o estudo real é um case study industrial de um time, 37 microsserviços, 4 semanas).

**Decisao: INCLUIDO | Qualidade: 4/5**

## Dados Bibliograficos

| Campo | Valor |
|-------|-------|
| ID | P0470 |
| Autores | Janick Rüegger, Martin Kropp, Sebastian Graf, Craig Anslow |
| Ano | 2024 |
| Venue | ICSSP '24 (Int. Conference on Software and Systems Processes), München |
| DOI | 10.1145/3666015.3666020 |
| Tipo | Conference paper (research article) |
| Metodo | Design de sistema + estudo de caso industrial |
| Amostra | 1 time responsável por 37 microsserviços, período de 4 semanas |
| Contexto | Indústria (DevOps) |

## Objetivo
Apresentar uma solução **open-source** que mede e calcula as métricas DORA de forma **totalmente automatizada**, em tempo real e no nível de microsserviço individual, a partir de dados de ferramentas DevOps — em contraste com surveys (subjetivos, esporádicos, no nível de time).

## Método e dados
Sistema automatizado avaliado em estudo de caso industrial: análise comparativa do desempenho de um time com 37 microsserviços durante 4 semanas. Demonstra cálculo automatizado das 4 métricas DORA com granularidade por serviço.

## Categorias de métrica (leitura do PDF)
- Delivery Performance: **Yes** (deployment frequency, lead time for changes — núcleo DORA, medidos automaticamente)
- Quality: **Yes** (change failure rate e MTTR — por convenção do codebook caem em Quality)
- Agile/Process: **Yes** (métricas de processo DevOps / melhoria contínua, granularidade por microsserviço)
- Survey/Perceptual: **No** (explicitamente automatizado, contrastado com surveys)
- Activity/Code: No · Productivity/Performance: No · Collaboration: No · Satisfaction/Wellbeing: No · DevEx Dimensions: No
- DORA Applied: **Yes** · SPACE: No · AI Discussed: No

## Avaliação de qualidade (Dybå & Dingsøyr)
Objetivo claro, método sólido, contexto industrial bem descrito, artefato open-source. Limitações: 1 time, janela curta (4 semanas), generalização limitada. Média ~4/5.

# P0532 — Smart Build Targets Batching Service at Google

**Decisao: INCLUIDO | Qualidade: 4/5**

---

## Dados Bibliograficos

| Campo | Valor |
|-------|-------|
| **ID** | P0532 |
| **Autores** | Kaiyuan Wang, Daniel Rall, Greg Tener, Vijay Gullapalli, Xin Huang, Ahmed Gad |
| **Ano** | 2021 |
| **Venue** | ICSE-SEIP 2021 (43rd International Conference on Software Engineering: Software Engineering in Practice) |
| **Tipo** | Estudo de Caso em Indústria (Industry Case Study) |
| **Metodo** | Análise técnica de sistema em produção com coleta de telemetria e métricas de performance |
| **Amostra** | Builds do Google com monolith codebase contendo tens de milhões de targets |
| **Contexto** | Build Optimization - Sistema de Batching de Targets para Bazel em Google |

---

## Objetivo

Descrever e avaliar um serviço de batching inteligente de targets de build (BTBS - Build Target Batching Service) desenvolvido para resolver problema crítico no Google: quando um build inclui muitos targets, o codebase monolítico do Google frequentemente excede deadlines de execução, causando out of memory (OOM) ou deadline exceeded errors. O objetivo é documentar técnica que particiona um grande stream de targets em lotes otimizados que minimizam erros de OOM/DE enquanto mantém build efficiency.

---

## Questoes de Pesquisa

- **RQ1**: Como particionar um grande stream de targets em lotes que minimizem OOM e deadline exceeded errors?
- **RQ2**: Qual é a acurácia de modelos de predição de memória e ocupação de executor para targets de build?
- **RQ3**: Como feature engineering e machine learning podem otimizar estratégias de batching?
- **RQ4**: Qual é o impacto do BTBS em redução de builds falhados e melhoria de produtividade?

---

## Dados da Pesquisa

### Amostra
- Google monolithic codebase com tens de milhões de build targets
- Período: Dados de produção de agosto 2021 (snapshot mensal)
- Volume: 1.47 milhões de EnqueueTargets RPC calls diariamente (média)
- 102 milhões de builds criados por BTBS (2.92 milhões diariamente em média)
- Dados de telemetria de ~17-18 dias de operação no mês de agosto

### Fonte de Dados
- Telemetria de builds de Bazel em Google's build infrastructure
- Logs de execução com informações de memória e ocupação
- Dados de serviço de evento coletados via sistema de event service
- Registro de Bazel com flags, targets e metadados de build

### Metodos de Coleta
- Coleta automática de telemetria durante build execution
- Monitoramento de pico de memória (peak heap memory usage)
- Tracking de occupancy de executor (executor service units - ESU)
- Análise de erros de build (OOM, Type I DE errors)
- Machine learning model training com regressão linear
- Feature engineering com crossing de features

### Periodo de Analise
- Análise principal: agosto 2021 (single month snapshot)
- Treinamento de modelos: 17 dias de dados (weekday data, excluindo períodos anômalos)
- Avaliação contínua: Sistema em operação desde implementação até setembro 2021

---

## Metricas e Instrumentos de Avaliacao

**Métricas de Erros de Build**:
- OOM (Out of Memory): Builds que excedem memória alocada
- DE (Deadline Exceeded): Builds que excedem tempo de deadline
- Type I errors: Predições que resultam em deadline exceedance sem causa real

**Métricas de Predição**:
- Root Mean Square Error (RMSE): Medida de acurácia do modelo de memória
- Memory prediction: Estimativa de peak heap memory para build
- Occupancy prediction: Estimativa de occupancy de executor em ESU (Executor Service Units)

**Métricas de Performance**:
- OPS (Queries per Second): Taxa de requisições para BTBS
- Latency (ms): Latência da API EnqueueTargets
- StreamTC: Total target count por RPC
- StreamBC: Total gerado build count por RPC
- BuildTC: Targets por build individual
- ExecT: Tempo de execução do build
- Memory: Uso de memória do build
- Occupancy: Ocupação de executor do build

**Features de Machine Learning** (Tabela III):
- Build priority, command name, originating user, product area
- Targets, target count, packages, package count
- Cache test results, CPU architecture, discard analysis cache
- Fuseless output, jobs concurrency, keep going, keep state
- Runs per test, test size filters, use action cache

**Análise de Batching**:
- Batch size reasons: ONLY_ONE_TARGET, MAX_TARGETS, ALL_REMAINING_TARGETS, MAX_MEMORY, MAX_OCCUPANCY, MEMORY_ESTIMATE_ERROR, OCCUPANCY_ESTIMATE_ERROR
- Binary search para encontrar batch size ótimo
- Medição de trade-offs entre tamanho de batch e erros

---

## Resultados Principais

**Taxa de Erros Reduzida**:
- OOM rate antes de BTBS: acima de 0.08%
- OOM rate com BTBS: 0.08% (redução significativa)
- DE rate antes: acima de 0.05%
- DE rate com BTBS: 0.05% (redução consistente)

**Acurácia dos Modelos de Predição**:
- Memory model RMSE: Varia de 0.8 GB a 13 GB dependendo do batch size reason
- Occupancy model RMSE: Varia de 0.0 a 2.8 Occupancy units
- MAX_MEMORY batch reason: 46.9k (0.36) builds com MAX_MEMORY batch size reason
- MAX_OCCUPANCY batch reason: 35 (0.06) builds

**Distribução de Batch Size Reasons**:
- ONLY_ONE_TARGET: 21.12% dos builds
- MAX_TARGETS: 22.95% dos builds
- ALL_REMAINING_TARGETS: 33.06% dos builds
- MAX_MEMORY: 12.71% dos builds
- MAX_OCCUPANCY: 0.06% dos builds
- MEMORY_ESTIMATE_ERROR: 0.10% dos builds
- OCCUPANCY_ESTIMATE_ERROR: 0.00% dos builds

**Performance de BTBS**:
- OPS: 6.27 (média), 0.12 (min), 4.24 (mediana), 18.89 (max)
- Latency: 265-414 ms (média), 1-81 ms (min), 150-179 ms (mediana), 698-886 ms (max)
- StreamTC: 674 (média), 1 (min), 2 (mediana), 70m (max)
- BuildTC: 339 (média), 1 (min), 24 (mediana), 900 (max)
- Memory: 394 (média), 0.1 (min), 250 (mediana), 7923 (max) em GB
- Occupancy: 18.3 (média), 0 (min), 2.8 (mediana), 2066.4 (max) em ESU

**Impacto em Produtividade**:
- BTBS reduz número de builds falhados significativamente
- Melhoria de developer productivity ao reduzir build failure retries
- Economia de recursos computacionais através de batching eficiente

---

## Desafios do Uso das Metricas

1. Variabilidade entre tipos de targets: Diferentes tipos de targets (Java, C++, tests) têm padrões de memória/ocupação muito diferentes, afetando acurácia do modelo

2. Modelo específico a Google: Sistema treinado em Google's monolithic codebase, pode não generalizar para outras organizações ou sistemas de build distribuídos

3. Feature engineering complexo: Muitas features de Bazel (flags, arquitetura, configurações) afetam predição, algumas correlacionadas de forma não-linear

4. Snapshot temporal: Dados de agosto 2021 representam snapshot, padrões de build podem variar sazonalmente (por exemplo, períodos de maior desenvolvimento)

5. Mudanças em codebase: Conforme codebase evolui com novos targets/dependências, modelos treinados podem perder acurácia

6. Colateral damage: Conceito de "colateral damage" (atrasos em builds independentes devido a queueing) não é capturado diretamente pelas métricas

---

## Avaliacao de Qualidade

| Criterio | Pontuacao (0-2) |
|----------|-----------------|
| Objetivo claramente definido | 2 |
| Metodologia adequada | 2 |
| Amostra/contexto descrito | 2 |
| Ameacas a validade discutidas | 1 |
| Resultados com evidencia | 2 |
| Contribuicao clara | 1 |
| **TOTAL** | **10/12** |

---

## Limitacoes

1. Contexto específico a Google: Sistema desenvolvido e avaliado exclusivamente em infraestrutura Google, generalização para outras organizações questionável

2. Snapshot temporal: Dados de agosto 2021 podem não ser representativos de padrões ao longo de todo o ano

3. Falta de comparação baseline: Não há comparação quantitativa com abordagens alternativas de batching

4. Modelo específico a Bazel: Algoritmo assume características específicas de Bazel, pode não generalizar para outros build systems

5. Confundidores não controlados: Mudanças em policies de scheduling, configurações de hardware ou práticas de desenvolvimento podem afetar resultados

6. Avaliação limitada de impacto: Impacto em produtividade do desenvolvedor medido indiretamente via redução de builds falhados

---

## Contribuicao Principal

O trabalho descreve primeira técnica prática que efetivamente cria builds a partir de um grande stream de targets (potencialmente milhões) com objetivo de minimizar OOM e deadline exceeded errors através de machine learning-based batching. Contribuição-chave é demonstrar que models de predição de memória e occupancy de executor, combinados com estratégia de binary search para encontrar batch size ótimo, podem reduzir OOM rate de 0.08%+ a 0.08% (baseline) e DE rate de 0.05%+ a 0.05%. O trabalho fornece insights práticos sobre feature engineering para predição de resource usage em builds complexos, incluindo análise de importância de features e técnicas de feature crossing. Demonstra scalability do sistema em contexto de Google's massive codebase com 1.47 milhões de requisições diárias, sugerindo aplicabilidade em outras grandes organizações com monolithic codebases. Contribui direções práticas para otimização de build systems em infraestruturas de desenvolvimento em larga escala, melhorando produtividade de desenvolvedores através de redução de build failures e otimização de resource allocation.

---

*Extraido em Marco 2026 para MLR: Software Developer Metrics in Practice*

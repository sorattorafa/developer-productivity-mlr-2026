# P0532 — Smart build targets batching service at Google

**Decisao: INCLUIDO | Qualidade: 5/5**

---

## Dados Bibliograficos

| Campo | Valor |
|-------|-------|
| **ID** | P0532 |
| **Autores** | Kaiyuan Wang, Daniel Rall, Greg Tener, Vijay Gullapalli, Xin Huang, Ahmed Gad |
| **Ano** | 2021 |
| **Venue** | ICSE-SEIP (International Conference on Software Engineering: Software Engineering in Practice) |
| **DOI** | 10.1109/ICSE-SEIP52600.2021.00025 |
| **Tipo** | Conference paper |
| **Metodo** | Case study / Experiment (Production deployment evaluation) |
| **Amostra** | 51 million EnqueueTargets RPC calls and 102 million builds |
| **Contexto** | Industry — Google Inc. monolithic codebase with tens of millions of build targets |
| **Modo de trabalho** | Not specified |
| **Metodologia** | DevOps (Continuous Integration) |

---

## Objetivo

O objetivo principal do artigo é propor e avaliar o **Build Target Batching Service (BTBS)**, um serviço que utiliza modelos de **machine learning** para prever o uso de memória e a ocupação de executores de um build [1-3]. O sistema visa particionar grandes fluxos de alvos (targets) em lotes (batches) de forma que os builds resultantes não excedam os limites de recursos, minimizando erros de **Out of Memory (OOM)** e **Deadline Exceeded (DE)**, aumentando assim a produtividade dos desenvolvedores ao reduzir a necessidade de repetições (retries) de builds com falha [1, 4].

---

## Questoes de Pesquisa

O artigo não lista explicitamente perguntas de pesquisa no formato "RQ", mas foca em demonstrar a eficácia da técnica proposta em:
- **Objetivo 1:** Criar builds efetivamente a partir de um grande fluxo de alvos para minimizar erros de OOM e DE [4].
- **Objetivo 2:** Prever o uso de memória e ocupação de executores em execuções de build [4].
- **Objetivo 3:** Reduzir as taxas de erro OOM e DE em um ambiente de produção em larga escala [4].

---

## Metricas e Instrumentos de Avaliacao

| Metrica | Categoria | Nivel | Como Coletada | Validada |
|---------|-----------|-------|---------------|----------|
| OOM rate | Quality | Organization | Calculada como a porcentagem de builds que falham por falta de memória | Yes |
| DE rate | Quality | Organization | Calculada como a porcentagem de builds que excedem o tempo limite de execução | Yes |
| Peak post full GC heap memory usage | Activity | Organization | Registrada pelo Bazel no JVM durante a execução do build | Yes |
| Average executor occupancy (ESU) | Activity | Organization | Soma do tempo de serviço do executor dividida pelo tempo de execução do build | Yes |
| QPS (Queries Per Second) | Activity | Organization | Monitoramento do tráfego do RPC EnqueueTargets | Yes |
| Latency | Activity | Organization | Tempo de resposta da chamada de streaming RPC | Yes |
| Build execution time | Activity | Organization | Wall time da execução do comando, excluindo o tempo de inicialização do Bazel | Yes |

---

## Frameworks e Metricas

### Frameworks Referenciados
- **Continuous Integration (CI):** REFERENCED — Discutido como o contexto onde o BTBS opera [5].
- **Bazel:** APPLIED — Utilizado como a ferramenta de build e teste onde as medições e o serviço são aplicados [6, 7].
- **AutoML:** REFERENCED — Ferramenta similar citada para a geração de feature crosses [8].

### Frameworks Propostos
O artigo propõe o **BTBS (Build Target Batching Service)**, que utiliza um algoritmo de batching baseado em busca binária e modelos de regressão linear para otimizar a distribuição de alvos de build com base na previsão de consumo de recursos (memória e CPU/ESU) [2, 9, 10].

---

## Fatores que Influenciam Produtividade

### Fatores Positivos
| Fator | Categoria |
|-------|-----------|
| Smart batching of targets | Technical |
| Prediction of memory and occupancy usage | Technical |
| Lexicographical sorting of targets (dependency sharing) | Process |
| Action caching in executor cluster | Technical |
| Automatic build failure retry | Process |

### Fatores Negativos
| Fator | Categoria |
|-------|-----------|
| Out of Memory (OOM) errors | Technical |
| Deadline Exceeded (DE) errors | Technical |
| Collateral damage (delays due to mixed executor requirements) | Technical/Process |
| Large number of targets in a single build execution | Technical |

---

## Papel da IA e Automacao

| Campo | Valor |
|-------|-------|
| Usa IA/ML? | Yes — Utiliza modelos de regressão linear treinados via stochastic gradient descent com feature crossing para prever uso de memória e ocupação [11-13]. |
| Automacao de coleta? | Yes — Um job Flume gera features e labels diariamente a partir das estatísticas de execução armazenadas em um sistema de arquivos distribuído [14, 15]. |
| Impacto de IA na produtividade? | Reduz a taxa de OOM para 0.08% e DE para 0.05%, economizando recursos computacionais e reduzindo retries manuais e automáticos que bloqueiam os desenvolvedores [3, 4, 7]. |

---

## Resultados Principais

- O BTBS alcançou uma **taxa de OOM de 0.08%** e uma **taxa de DE de 0.05%** em produção [3, 4].
- Durante o experimento de 35 dias, o serviço processou **51 milhões de chamadas RPC** e criou **102 milhões de builds** [16].
- O modelo de memória é utilizado em aproximadamente **78.78% de todos os builds** gerados [17].
- A ordenação lexicográfica dos alvos ajudou a construir grafos de dependência mais compactos, reduzindo o uso de memória [18].
- O uso de modelos de ML permitiu aumentar a densidade dos lotes (batch density) sem sobrecarregar os workers do Bazel [19].

---

## Desafios do Uso das Metricas

- **Monotonicidade:** Os modelos de ML precisam ser monotônicos em relação às features de alvos para que a busca binária de batching funcione corretamente [13, 20].
- **Model Drift:** Padrões de memória podem mudar rapidamente (ex: regressões no Bazel), exigindo o treinamento contínuo de modelos de curto prazo (último dia) para complementar os modelos de longo prazo (17 dias) [21, 22].
- **Type II DE errors:** Builds que excedem o prazo devido a ações sequenciais longas, que não são correlacionadas com a ocupação média e não são evitadas pelo batching [23-25].
- **Collateral Damage:** Atrasos causados por builds que requerem múltiplos tipos de executores (ex: CPU e GPU), resolvidos pelo agrupamento de alvos por tipo de executor antes do batching [9, 26, 27].

---

## Avaliacao de Qualidade Metodologica

| Criterio | Pontuacao (0-2) |
|----------|----------------|
| Objetivo claramente definido | 2 |
| Metodologia adequada ao objetivo | 2 |
| Amostra/contexto descrito adequadamente | 2 |
| Ameacas a validade discutidas | 1 |
| Resultados com evidencia suficiente | 2 |
| Contribuicao clara para pratica ou teoria | 2 |
| **TOTAL** | **11/12** |

---

## Limitacoes

- O serviço **não considera erros de DE do Tipo II**, que ocorrem devido a cadeias de ações sequenciais longas e não estão diretamente ligados à ocupação do executor [24, 25].
- O BTBS **não pode dividir um único alvo**; se um único alvo exceder os limites de memória ou tempo, o sistema não consegue evitar a falha [28, 29].
- A precisão do modelo pode ser afetada por builds que não acionam o Garbage Collection (GC), levando a superestimações de memória [30, 31].

---

## Contribuicao Principal

A principal contribuição é o projeto e a implementação em escala industrial do primeiro serviço de batching inteligente de alvos de build (**BTBS**). O artigo demonstra como modelos de **machine learning** podem ser aplicados com sucesso para prever o consumo de recursos de infraestrutura em sistemas de build complexos, transformando um problema de esgotamento de recursos em uma tarefa de otimização de lotes, resultando em uma infraestrutura de CI mais estável e produtiva para milhares de engenheiros [4, 7, 32].

---

*Extraido via NotebookLM em March 2026 para MLR: Software Developer Metrics in Practice*
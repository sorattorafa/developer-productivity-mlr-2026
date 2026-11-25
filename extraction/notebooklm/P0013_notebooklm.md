# P0013 — Supporting the Developer Experience with Production Metrics

**Decisao: INCLUIDO | Qualidade: 3/5**

---

## Dados Bibliograficos

| Campo | Valor |
|-------|-------|
| **ID** | P0013 |
| **Autores** | Robert Chatley [1] |
| **Ano** | c. 2019 [2] |
| **Venue** | Not specified (Position paper) [1] |
| **DOI** | Not specified |
| **Tipo** | Position paper [1] |
| **Metodo** | Qualitative (Research Roadmap / Position Paper) [1, 3] |
| **Amostra** | N/A (Conceptual roadmap) [3, 4] |
| **Contexto** | Industry (Continuous software engineering, web applications, and services) [1, 5] |
| **Modo de trabalho** | Not specified |
| **Metodologia** | Continuous Delivery / Continuous Software Engineering [1, 6] |

---

## Objetivo

O objetivo principal deste artigo é apresentar um roteiro (roadmap) para o desenvolvimento de ferramentas que capturem dados de sistemas em produção (como traces de execução e exceções) e os apresentem de forma contextualizada e acionável aos desenvolvedores dentro de seus ambientes de desenvolvimento regulares (IDEs) [1, 3]. O intuito é permitir que os desenvolvedores tomem decisões informadas sobre o impacto de mudanças no código durante o trabalho diário [1].

---

## Questoes de Pesquisa

O artigo propõe investigar as seguintes questões como parte de seu roteiro de pesquisa:
- **RQ1:** Os tipos de métricas capturados por ferramentas de Application Performance Management (APM) podem fornecer insights profundos o suficiente para resolver os problemas práticos descritos? [7]
- **RQ2:** Qual abordagem é mais eficaz para rastreio de versões: o pipeline de build enviar dados para o serviço de métricas ou os agentes de monitoramento/log estarem cientes da versão implantada no código? [8]
- **RQ3:** No fornecimento de dados, é melhor relatar valores atuais ou mudanças e deltas (comparações com médias históricas)? [9]
- **RQ4:** Essas informações ajudam a guiar o trabalho dos desenvolvedores e permitem avaliar o impacto de suas mudanças? [10]
- **RQ5:** A apresentação dessas estatísticas prova ser uma fonte útil de informação ou apenas uma distração? [10]

---

## Metricas e Instrumentos de Avaliacao

| Metrica | Categoria | Nivel | Como Coletada | Validada |
|---------|-----------|-------|---------------|----------|
| Execution path frequency | Activity / DevEx | Individual/Team | Fine-grained instrumentation/profiling agents [10, 11] | Partial [10] |
| Exception frequency | Quality / DevEx | Individual/Team | Processing production logs and IDE overlay [12] | No [12] |
| Deployment environment (What is deployed where) | Delivery | Individual | Integration with build/deployment pipeline [13, 14] | No [14] |
| Performance KPIs (timings/bottlenecks) | Productivity / Quality | Organization | APM tools (e.g., NewRelic, Google-wide profiling) [9, 15] | Yes [15] |
| Execution deltas (changes in behavior) | Activity / DevEx | Individual/Team | Analysis of version control and build system data [16] | No [16] |

---

## Frameworks e Metricas

### Frameworks Referenciados
- **Continuous Software Engineering:** REFERENCED (contexto principal do trabalho) [1, 17].
- **Continuous Delivery:** REFERENCED (processo de entrega descrito) [6, 14, 18].
- **Application Performance Management (APM):** REFERENCED (como fonte de dados existente) [1, 5, 7, 9].

### Frameworks Propostos
O artigo propõe uma **arquitetura de sistema (Envisioned Architecture)** para coleta e análise de métricas que integra o IDE do desenvolvedor, sistemas de controle de versão, pipelines de build, ambientes de staging/produção e uma plataforma de métricas centralizada [16, Fig 1].

---

## Fatores que Influenciam Produtividade

### Fatores Positivos
| Fator | Categoria |
|-------|-----------|
| Short feedback cycles | Process [19] |
| Automated build and deployment pipelines | Process [13] |
| Context-sensitive production data in IDE | Technical [1, 11] |

### Fatores Negativos
| Fator | Categoria |
|-------|-----------|
| Disconnect between logs and development flow | Process [20] |
| High rate of release (reducing data per version) | Process [18] |
| Complexity of multiple pre-production environments | Process [6, 13] |

---

## Papel da IA e Automacao

| Campo | Valor |
|-------|-------|
| Usa IA/ML? | No [Baseado na ausência de menção nas fontes] |
| Automacao de coleta? | Yes — Proposta de integração automatizada entre o pipeline de build, agentes de profiling e a IDE [7, 13, 21]. |
| Impacto de IA na produtividade? | N/A |

---

## Resultados Principais

Como este é um "position paper", os resultados focam no roteiro e arquitetura propostos:
*   A necessidade de converter grandes quantidades de dados de APM em informações acionáveis para desenvolvedores [1].
*   A identificação de três áreas problemáticas principais: Traces de execução (identificar caminhos "quentes"), Relato de exceções (visibilidade imediata no código) e Status de implantação (saber o que está rodando em qual ambiente) [12, 13, 19, 22].
*   A proposição de um sistema que sobreponha (overlay) dados de produção diretamente no código fonte no IDE [11, 12, 21].
*   O desafio de realizar profiling contínuo sem introduzir overhead inaceitável na performance da aplicação [9, 21].

---

## Desafios do Uso das Metricas

*   **Engineering Challenge:** Integrar ferramentas diferentes e gerenciar o fluxo de dados entre elas [7].
*   **Version Tracking:** Sincronizar dados de monitoramento com hashes específicos do Git ou números de build em ambientes de entrega rápida [8, 18].
*   **Data Granularity:** Ferramentas de prateleira (off-the-shelf) podem não fornecer a granularidade necessária (ex: qual branch foi tomada) [9].
*   **Information Overload:** Risco de as estatísticas se tornarem uma distração para o desenvolvedor [10].
*   **Analysis Intricacy:** Dificuldade em agregar dados quando múltiplas implantações ocorrem por dia (batch sizes reduzidos) [18].

---

## Avaliacao de Qualidade Metodologica

| Criterio | Pontuacao (0-2) |
|----------|----------------|
| Objetivo claramente definido | 2 [1] |
| Metodologia adequada ao objetivo | 1 [Position paper sem validação empírica] |
| Amostra/contexto descrito adequadamente | 1 [Descreve o cenário industrial, mas sem amostra] [4, 5] |
| Ameacas a validade discutidas | 1 [Desafios técnicos discutidos] [7-9, 15, 18, 23] |
| Resultados com evidencia suficiente | 1 [Baseado em exemplos conceituais e roadmap] [19, 22] |
| Contribuicao clara para pratica ou teoria | 2 [Define nova direção de pesquisa] [3, 21] |
| **TOTAL** | **8/12** |

---

## Limitacoes

*   **Falta de Validação Empírica:** As ferramentas e abordagens propostas ainda não foram testadas com desenvolvedores reais ou dados de produção representativos no momento da escrita [4, 10].
*   **Dependência de Colaboração:** A pesquisa de impacto depende de parcerias entre pesquisadores e profissionais da indústria para obter dados reais [4].
*   **Performance Overhead:** O risco de que o profiling detalhado afete negativamente a performance do sistema em produção [9, 21].

---

## Contribuicao Principal

A principal contribuição é a proposição de um **fechamento do ciclo de feedback (closing the loop)** entre a operação (produção) e o desenvolvimento, fornecendo dados de tempo de execução diretamente no IDE. O trabalho define um roteiro de pesquisa que vai além de métricas de performance genéricas, focando em comportamentos de execução específicos do código para melhorar a experiência do desenvolvedor em ambientes de engenharia de software contínua [1, 17, 21].

---

*Extraido via NotebookLM em March 2026 para MLR: Software Developer Metrics in Practice*
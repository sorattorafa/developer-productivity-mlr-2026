# P0036 — A Multi-Agent AI Framework for Agile Workflow Automation, Issue Resolution, and Developer Performance Evaluation

**Decisao: INCLUIDO | Qualidade: 3/5**

---

## Dados Bibliograficos

| Campo | Valor |
|-------|-------|
| **ID** | P0036 |
| **Autores** | Chathurya Adapa, Anjana A R K, Rafsal Rahim, Ajay Victor |
| **Ano** | 2025 |
| **Venue** | International Conference for Women in Innovation, Technology & Entrepreneurship (ICWITE 2025) |
| **DOI** | Not specified (ISBN: 978-1-6654-5762-0) |
| **Tipo** | Conference paper |
| **Metodo** | Experiment / Benchmarking (Evaluation using synthetic datasets) |
| **Amostra** | Set of synthetic examples and prompts simulating real-world Agile workflows |
| **Contexto** | Industry (IBM India Systems Development Labs) |
| **Modo de trabalho** | Not specified |
| **Metodologia** | Agile (Scrum) |

---

## Objetivo

O objetivo principal do artigo é propor um **framework de IA baseado em agentes (agentic AI)** para automatizar e aprimorar a colaboração e a gestão de tarefas em equipes ágeis [1]. O sistema utiliza uma rede de módulos de IA integrados com transcrição de chamadas em tempo real para gerenciar três áreas principais: rastreamento de tarefas (**task tracking**), resolução de problemas (**issue resolution**) e avaliação de desempenho de desenvolvedores (**developer performance evaluation**) [1, 2].

---

## Questoes de Pesquisa

O artigo não lista formalmente questões de pesquisa prefixadas com RQ, mas foca em avaliar:
- A eficácia da extração autônoma de dados de reuniões de *stand-up* [3, 4].
- O impacto da automação na redução do esforço manual de atualização de tickets e resolução de bloqueadores [2, 5].
- A eficiência do uso de agentes para gerar relatórios de desempenho e reduzir a carga de trabalho gerencial [5, 6].

---

## Metricas e Instrumentos de Avaliacao

| Metrica | Categoria | Nivel | Como Coletada | Validada |
|---------|-----------|-------|---------------|----------|
| **Extraction accuracy** | Quality | Team | Autonomous parsing of meeting transcripts by AI Agent I [3, 7] | Yes (95%) |
| **Manual task updates reduction** | Productivity | Team | Automation of ticket status changes (e.g., Jira) [3, 8] | Yes (60%) |
| **Contextual relevance (Blockers)** | Quality | Team | Analysis of blockers by Agent II based on historical data [3, 9] | Yes (85%) |
| **Blocker resolution time reduction** | Productivity | Team | Comparison of resolution time using AI suggestions vs. manual [3, 5] | Yes (40%) |
| **Developer hours saved** | Productivity | Individual | Annual aggregation of time saved by eliminating manual updates [5, 10] | Yes (22-25h) |
| **Manager evaluation time reduction** | Productivity | Organization | Time spent on performance reviews with agent assistance vs. manual [5, 8] | Yes (75%) |
| **Sprint planning accuracy** | Productivity | Team | Improvement in planning accuracy via agent insights [5, 11] | Yes (20%) |
| **Performance Rating (1-5)** | Performance | Individual | Analysis of Jira activity, story points, and consistency by Agent III [6] | Partial |

---

## Frameworks e Metricas

### Frameworks Referenciados
- **Agile/Scrum**: APPLICADO (Contexto principal do trabalho) [1, 12].
- **I-AM-BEE (Intelligent Agent-Based Engineering Ecosystem)**: APPLICADO (Utilizado para orquestração e modularidade do sistema) [13, 14].
- **RAG (Retrieval-Augmented Generation)**: APPLICADO (Usado para resolução de bloqueadores) [9, 15].

### Frameworks Propostos
O artigo propõe um **Multi-agent AI Framework** modular e conteinerizado, onde agentes especializados (Agent I, II e III) colaboram através de uma camada de orquestração central para automatizar cerimônias ágeis e análise de produtividade [2, 13, 16].

---

## Fatores que Influenciam Produtividade

### Fatores Positivos
| Fator | Categoria |
|-------|-----------|
| Autonomous task synchronization | Process |
| Real-time blocker resolution assistance | Technical |
| Automated performance insights generation | Organizational |
| Reduction in manual operational overhead | Process |

### Fatores Negativos
| Fator | Categoria |
|-------|-----------|
| Manual status updates friction | Process |
| Delays in blocker identification | Process |
| Time-intensive performance reviews | Organizational |

---

## Papel da IA e Automacao

| Campo | Valor |
|-------|-------|
| Usa IA/ML? | **Yes**. Utiliza LLMs como **Granite 3.3** e **LLaMA** para percepção, raciocínio e ação autônoma [17, 18]. |
| Automacao de coleta? | **Yes**. Automação da coleta de métricas via integração com APIs de ferramentas como Jira e transcrição de áudio [7, 9, 19]. |
| Impacto de IA na produtividade? | Redução drástica de esforço manual: 60% dos tickets atualizados automaticamente e redução de 75% no tempo de avaliação gerencial [3, 5, 8]. |

---

## Resultados Principais

- **Acurácia de extração de 95%** em transcrições de reuniões diárias [3].
- **Redução de 75% no tempo de avaliação de gerentes**, caindo de 6 horas para 1.3 horas por desenvolvedor anualmente [5, 8].
- **Economia de 22–25 horas anuais por desenvolvedor** através da eliminação de atualizações manuais de tarefas [5, 10].
- **Redução de 40% no tempo de resolução de bloqueadores** através de sugestões contextuais do agente de RAG [3, 20].
- **Melhoria de 20% na precisão do planejamento de sprint** [5].

---

## Desafios do Uso das Metricas

- **Privacidade**: O artigo ressalta a importância de práticas de coleta de dados sensíveis à privacidade (**privacy-aware**) [6, 19].
- **Fricção e Inconsistência**: Processos manuais tradicionais introduzem atrasos e inconsistências que limitam a utilidade das métricas coletadas manualmente [2, 12].
- **Dependência de Dados Históricos**: A eficácia do agente de bloqueadores depende da qualidade da base de conhecimento e documentação (ex: Confluence) [9].

---

## Avaliacao de Qualidade Metodologica

| Criterio | Pontuacao (0-2) |
|----------|----------------|
| Objetivo claramente definido | 2 |
| Metodologia adequada ao objetivo | 1 |
| Amostra/contexto descrito adequadamente | 1 |
| Ameacas a validade discutidas | 0 |
| Resultados com evidencia suficiente | 1 |
| Contribuicao clara para pratica ou teoria | 2 |
| **TOTAL** | **7/12** |

---

## Limitacoes

- A implementação de uma **Prova de Conceito (PoC)** real em ambiente de produção é citada como trabalho futuro [21].
- A avaliação apresentada baseia-se em **conjuntos de dados sintéticos** e benchmarking preliminar, não em um estudo de caso longitudinal com usuários reais [16, 21, 22].

---

## Contribuicao Principal

A principal contribuição é a criação de uma **arquitetura multi-agente modular (I-AM-BEE)** que preenche a lacuna entre modelos teóricos de colaboração de IA e o fluxo de trabalho prático de engenharia de software [2, 23]. O framework demonstra como agentes inteligentes podem atuar como colaboradores ativos em cerimônias ágeis, reduzindo significativamente a carga administrativa tanto para desenvolvedores quanto para gestores [2, 8, 22].

---

*Extraido via NotebookLM em March 2026 para MLR: Software Developer Metrics in Practice*
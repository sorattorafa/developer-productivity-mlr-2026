# P1818 — Performance Measurement Framework for Agile Scrum Software Engineering Environment

**Decisao: INCLUIDO | Qualidade: 3/5**

---

## Dados Bibliograficos

| Campo | Valor |
|-------|-------|
| **ID** | P1818 |
| **Autores** | Chathurya Adapa, Anjana A R K, Rafsal Rahim, Ajay Victor [1, 2] |
| **Ano** | 2025 [1] |
| **Venue** | International Conference for Women in Innovation, Technology & Entrepreneurship (ICWITE 2025) [1] |
| **DOI** | 978-1-6654-5762-0/25 (ISBN/IEEE) [1] |
| **Tipo** | Conference paper [1] |
| **Metodo** | Proposta de framework e avaliação via simulação com exemplos sintéticos (Benchmarking) [3-5] |
| **Amostra** | Exemplos sintéticos de transcrições de stand-ups, sincronização de ferramentas de gestão e métricas de desenvolvedores [3, 4, 6] |
| **Contexto** | Industrial (IBM India Private Limited) utilizando ferramentas como Jira, Slack e Confluence [1, 7, 8] |
| **Modo de trabalho** | Not specified (embora utilize ferramentas para colaboração remota/assíncrona) [7, 9] |
| **Metodologia** | Agile Scrum [2, 5, 10, 11] |

---

## Objetivo

O objetivo principal do artigo é propor um framework de inteligência artificial agentiva (Agentic AI) multi-agente para automatizar e aprimorar a colaboração em equipes ágeis e a gestão de tarefas [2, 7]. O sistema visa reduzir processos manuais de atualização de status, identificação de impedimentos (blockers) e acompanhamento de desempenho, permitindo que as equipes operem com maior eficiência e menos atrito operacional [5, 7, 10].

---

## Questoes de Pesquisa

O artigo não lista explicitamente perguntas de pesquisa numeradas, mas foca em avaliar:
- A precisão da extração de dados de reuniões diárias (stand-ups) por IAs agentivas [12, 13].
- O nível de automação possível na sincronização de ferramentas de gerenciamento de projetos [12, 14].
- A eficácia da IA na resolução de impedimentos e na economia de tempo para desenvolvedores e gestores [8, 15, 16].

---

## Metricas e Instrumentos de Avaliacao

| Metrica | Categoria | Nivel | Como Coletada | Validada |
|---------|-----------|-------|---------------|----------|
| Extraction accuracy | Quality | Team | Processamento de linguagem natural de transcrições de voz [12, 13] | Partial (Benchmarked 95%) [12, 17] |
| Manual task updates reduction | Productivity | Team/Org | Automação de mudanças de status via Jira REST API [12, 14] | Partial (60% automation) [12, 16] |
| Blocker resolution time reduction | Productivity | Team | Sugestões baseadas em RAG e histórico do Jira/Confluence [8, 12] | Partial (Up to 40% reduction) [15, 17] |
| Developer hours saved | Productivity | Individual | Eliminação de atualizações manuais de tarefas [15, 18] | Partial (22-25h annually) [15, 17] |
| Manager evaluation time | Productivity | Organization | Agregação automática de dados longitudinais de contribuição [15, 19] | Partial (75% reduction) [15, 16] |
| Sprint planning accuracy | Quality | Team | Otimização do fluxo de trabalho via agentes [15, 20] | Partial (~20% improvement) [15, 20] |
| Jira tickets closed | Activity | Individual | Dados de atividade do Jira [11] | No [19] |
| Total story points completed | Delivery | Individual | Dados de atividade do Jira [11] | No [11] |
| Stand-up consistency | Activity | Individual | Frequência de participação em reuniões [11, 19] | No [19] |
| Task estimation accuracy | Productivity | Individual | Comparação entre tempo estimado e tempo real [11, 19] | No [19] |

---

## Frameworks e Metricas

### Frameworks Referenciados
- **I-AM-BEE (Intelligent Agent-Based Engineering Ecosystem)**: APPLIED — Utilizado como a arquitetura base para a coordenação e escalabilidade dos agentes [21, 22].
- **RAG (Retrieval-Augmented Generation)**: APPLIED — Utilizado pelo agente de resolução de impedimentos para consultar bases de conhecimento [8, 10, 23].
- **Chroma / LangChain**: APPLIED — Tecnologias utilizadas para implementar o sistema de recuperação de informações [23].

### Frameworks Propostos
O artigo propõe um framework multi-agente modular consistindo em três agentes principais interconectados: um para extração de tarefas e sincronização com o Jira, um para resolução inteligente de bloqueios (usando RAG) e um terceiro para monitoramento e análise de performance de desenvolvedores [4, 7, 14].

---

## Fatores que Influenciam Produtividade

### Fatores Positivos
| Fator | Categoria |
|-------|-----------|
| Automacao de tarefas rotineiras | Process |
| Sincronizacao em tempo real de cerimônias ágeis | Technical |
| Resolucao inteligente de blockers baseada em historico | Technical |
| Reducao de overhead gerencial em avaliacoes | Organizational |

### Fatores Negativos
| Fator | Categoria |
|-------|-----------|
| Processos manuais de atualizacao de status | Process |
| Dependencia de tagging manual em ferramentas de gestao | Process |
| Atrasos na identificacao de impedimentos | Process |
| Inconsistencias no rastreamento de performance | Human |

---

## Papel da IA e Automacao

| Campo | Valor |
|-------|-------|
| Usa IA/ML? | Yes — Utiliza Agentic AI baseada em modelos Transformer (Granite 3.3 e LLaMA) e RAG [2, 23-25]. |
| Automacao de coleta? | Yes — Transcrições Speech-to-Text automáticas alimentam os agentes que atualizam ferramentas de gestão sem intervenção humana [8, 13, 14]. |
| Impacto de IA na produtividade? | Redução de 30% no esforço de rastreamento manual e economia de até 25 horas anuais por desenvolvedor [15, 20]. |

---

## Resultados Principais

- Automação de aproximadamente **60% das mudanças de status de tickets** com 95% de precisão na extração de dados [12, 16].
- Redução de até **40% no tempo de resolução de impedimentos** [12, 17].
- Economia de **22 a 25 horas anuais por desenvolvedor** ao eliminar atualizações manuais [15, 18].
- Redução de mais de **75% no tempo gasto por gestores** em avaliações (de 6 horas para 1,3 horas por desenvolvedor/ano) [15, 16].
- Melhoria de cerca de **20% na precisão do planejamento de sprints** [15, 20].

---

## Desafios do Uso das Metricas

- Necessidade de garantir **alinhamento de objetivos** e coordenação em sistemas multi-agente [26].
- Desafios éticos e de implantação, como **transparência e explicabilidade** das decisões da IA [26, 27].
- Riscos de privacidade na coleta de dados longitudinais de performance [11, 19].
- Manutenção da **consistência das métricas** como indicadores de suporte em vez de determinantes estritos de performance [19].

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

- A implementação de uma Prova de Conceito (PoC) completa é citada como **trabalho futuro**, baseando os resultados atuais em design preliminar e benchmarking [5].
- Os testes foram realizados primariamente com **dados sintéticos** (synthetic examples) para simular o fluxo de trabalho ágil [3, 4].
- Possível dependência de infraestrutura específica de modelos de linguagem de larga escala (LLMs) corporativos [24].

---

## Contribuicao Principal

A principal contribuição é a introdução de uma **arquitetura modular de orquestração multi-agente** capaz de gerenciar autonomamente três processos centrais do Scrum: extração de atualizações de reuniões diárias, resolução de bloqueios técnicos e análise de produtividade de desenvolvedores [5, 7]. O framework preenche uma lacuna na pesquisa de automação ágil ao passar de simples assistentes de IA para agentes que participam ativamente do fluxo de trabalho de engenharia [3, 7].

---

*Extraido via NotebookLM em March 2026 para MLR: Software Developer Metrics in Practice*
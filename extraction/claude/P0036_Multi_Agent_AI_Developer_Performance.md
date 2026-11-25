# P0036 — A Multi-Agent AI Framework for Agile Workflow Automation, Issue Resolution, and Developer Performance Evaluation

**Decisao: INCLUIDO | Qualidade: 2/5**

---

## Dados Bibliograficos

| Campo | Valor |
|-------|-------|
| **ID** | P0036 |
| **Autores** | Chathurya Adapa, Anjana A R K, Rafsal Rahim, Ajay Victor |
| **Afiliacao** | IBM India Private Limited, Bangalore |
| **Ano** | 2025 |
| **Venue** | ICWITE 2025 (International Conference for Women in Innovation, Technology & Entrepreneurship) |
| **Tipo** | Conference paper |
| **Metodo** | Experience report (dados sinteticos) |
| **Amostra** | IBM India — equipes ageis (dados sinteticos para avaliacao) |
| **Contexto** | Grande empresa (IBM) — agile software development |
| **Metodologia** | Agile/Scrum |

---

## Objetivo

Propor um framework multi-agente baseado em IA (I-AM-BEE) para automatizar colaboracao em equipes ageis, incluindo transcricao de stand-ups, sincronizacao de tarefas, resolucao de blockers e avaliacao de performance de desenvolvedores.

---

## Questoes de Pesquisa

- **RQ1**: Como automatizar e melhorar a colaboracao agil atraves de agentes IA multitarefa que participam ativamente em cerimônias ageis?
- **RQ2**: Podem agentes IA extrair e sincronizar informacoes de reunioes de stand-up com sistemas de gerenciamento de projetos em tempo real?
- **RQ3**: Como mensurar e agregar dados de performance de desenvolvedores de forma justa e privada atraves de agentes IA?

---

## Dados da Pesquisa

### Contexto
- **Organizacao**: IBM India Private Limited, Bangalore
- **Tipo de estudo**: Experience report (dados sinteticos)
- **Framework**: I-AM-BEE (Intelligent Agent-Based Engineering Ecosystem)

### Dados Utilizados
- **Tipo**: Synthetic dataset simulando workflows agiles reais
- **Fontes de dados sinteticas**:
  1. **Stand-up transcripts**: Exemplos sinteticos de daily stand-up meetings (transcritos via speech-to-text)
  2. **Project management data**: Jira tasks, status updates, story points
  3. **Historical blocker database**: Exemplos de blockers e resolucoes passadas
  4. **Confluence documentation**: Team knowledge base
- **Proposito**: Validacao de conceito para arquitetura; não dados reais de producao

---

## Metricas e Instrumentos de Avaliacao

### Instrumental e Processos

**3 Agentes IA (multi-agent architecture)**:

**Agent 1: Transcription & Task Synchronization**
- **Input**: Audio de daily stand-ups
- **Processamento**:
  - Speech-to-text: Google Speech API ou Whisper
  - Accuracy: ~95% transcription accuracy
  - NLP parsing: Extrai task identifiers, status indicators ("In Progress", "Blocked", "Done")
- **Output**: Structured task data enviado para Jira REST API
- **Metric**: Ticket automation rate = ~60% dos updates automatizados

**Agent 2: Blocker Resolution Assistance**
- **Input**: Blocked task descriptions, historical blockers database
- **Processamento**: Retrieval-Augmented Generation (RAG)
  - Vector database: Chroma + LangChain
  - Semantic search: Cosine similarity entre query e historical solutions
  - LLM: Granite 3.3 (IBM) ou Llama 3 (Meta)
- **Accuracy**: ~85% blocker resolution relevance
- **Output**: Suggested solutions to help unblock tasks
- **Metric**: Blocker resolution time reduction ~40%

**Agent 3: Developer Performance Monitoring**
- **Input**: Developer activity data (task completion, blocker resolution, stand-up participation)
- **Processamento**:
  - Metrics aggregation: Time-series database (InfluxDB ou equivalent)
  - Privacy-aware collection: Anonymized contributor IDs
  - Performance scoring: Composite metrics
- **Output**: Performance summaries (individual + team-level)
- **Metrics**:
  - Task completion frequency (tasks/sprint)
  - Contribution to blocker resolution (blockers resolved)
  - Stand-up participation consistency (attendance rate)
  - Task estimation accuracy (planned vs actual)
  - Completion within estimated time (% on-time)

### Metricas de Avaliacao (Projetadas/Sinteticas)

| Metrica | Categoria | Valor | Nota |
|---------|-----------|-------|------|
| **Ticket automation** | Eficiencia do Agent 1 | ~60% | Reducao de updates manuais |
| **Transcript extraction accuracy** | Confiabilidade | ~95% | Speech-to-text accuracy |
| **Blocker resolution time** | Eficiencia do Agent 2 | -40% reducao | vs manual resolution |
| **Developer hours saved** | Impacto | 22-25h/dev/ano | Automatic updates + performance tracking |
| **Manager evaluation time** | Eficiencia de avaliacao | 6h → 1.3h/dev/ano | >75% reducao |
| **Sprint planning accuracy** | Predicao | ~20% melhoria | Melhor dados historicos |
| **Manual tracking effort** | Overhead | ~30% reducao | Menos data entry |

### Dimensoes de Dados Coletados

**Developer Performance Dimensions** (6 dimensoes, cada uma rastreada):
1. **Task completion frequency**: Tasks completos por sprint/ciclo
2. **Contribution to blocker resolution**: Historical count de blockers que developer resolveu
3. **Stand-up participation consistency**: Dias presentes em stand-ups / total dias
4. **Task estimation accuracy**: |Estimated hours - Actual hours| / Estimated hours
5. **Completion within estimated time**: % de tasks completos <= estimated deadline
6. **Code review participation**: Reviews provided (se dados disponiveis)

**Storage**:
- Time-series database: Metrics armazenadas com timestamps
- Temporal resolution: Daily aggregation
- Privacy: Anonymized developer IDs (mapping table secured separadamente)

---

## Frameworks e Metricas

### C1 - Frameworks

- **I-AM-BEE Framework** (proposto): sistema multi-agente com 3 modulos
  - Agente 1: Transcricao de stand-up + sincronizacao com Jira
  - Agente 2: Resolucao de blockers (RAG-based com Chroma + LangChain)
  - Agente 3: Monitoramento de performance de desenvolvedores
- Modelos: Granite 3.3 (IBM), Llama 3 (Meta)
- Nenhum framework padrao (DORA, SPACE, DevEx) referenciado

### C2 - Metricas Especificas

| Metrica | Categoria | Nivel | Como Coletada | Validada |
|---------|-----------|-------|---------------|----------|
| Task completion frequency | Produtividade | Individual | Jira/project tools via AI agent | Nao (sintetico) |
| Contribution to blocker resolution | Colaboracao | Individual | Historical blockers DB + RAG | Nao (sintetico) |
| Stand-up participation consistency | Atividade | Individual | Transcricao automatica | Nao (sintetico) |
| Task estimation accuracy | Produtividade | Individual | Estimativa vs real (Jira) | Nao (sintetico) |
| Completion within estimated time | Velocidade | Individual | Jira timestamps | Nao (sintetico) |
| Ticket automation rate | Eficiencia | Equipe | Agent vs manual tracking | Parcial (~60%) |
| Transcript extraction accuracy | Eficiencia | Sistema | NLP parsing accuracy | Parcial (~95%) |

### C3 - Classificacao

- **Objetivas**: Task completion frequency, estimation accuracy, timeliness (automatizadas via agent)
- **Output**: Tasks concluidas, blocker contributions
- **Processo**: Stand-up participation, blocker resolution time

---

## Fatores que Influenciam Produtividade

### D1 - Fatores Positivos
| Fator | Categoria |
|-------|-----------|
| Automacao de updates de tickets (60%) reduz overhead manual | Ferramental |
| Resolucao de blockers com contexto historico (RAG) | Ferramental |
| Performance summaries automatizadas economizam tempo gerencial | Organizacional |
| Sincronizacao real-time entre stand-ups e project tools | Tecnico |

### D2 - Fatores Negativos
| Fator | Categoria |
|-------|-----------|
| Updates manuais de tickets causam friccao, delays, inconsistencias | Organizacional |
| Avaliacao gerencial consome ~6h/dev/ano em revisoes manuais | Organizacional |
| Blockers sem contexto historico demoram a ser resolvidos | Tecnico |
| Risco de metricas serem usadas punitivamente | Humano/Psicologico |

### D3 - Relacoes Identificadas
- Nao formalmente testadas (dados sinteticos), mas projetadas:
  - Automacao de tickets → +produtividade
  - RAG para blockers → -40% tempo de resolucao
  - AI performance summaries → -75% tempo de avaliacao gerencial

---

## Papel da IA e Automacao

| Campo | Valor |
|-------|-------|
| Usa IA/ML? | Sim — central ao framework |
| Tecnica | LLMs (Granite 3.3, Llama 3), RAG (Chroma + LangChain), NLP/Speech-to-text |
| Fontes de dados | Stand-up transcripts, Jira tasks, Confluence docs, historical blockers |
| Automacao de coleta? | Sim — agentes coletam metricas automaticamente de project tools |
| Compara IA vs manual? | Sim — Agent vs Manual tracking (60% automacao, 75% reducao avaliacao) |

---

## Resultados (Projetados/Estimados)

| Metrica | Resultado |
|---------|-----------|
| Ticket status automation | ~60% dos updates automatizados |
| Transcript extraction accuracy | ~95% |
| Blocker resolution time | Reducao de ~40% |
| Developer hours saved | 22-25h/dev/ano |
| Manager evaluation time | 6h → 1.3h/dev/ano (>75% reducao) |
| Sprint planning accuracy | ~20% melhoria |
| Manual tracking effort | ~30% reducao |

---

## Desafios do Uso das Metricas

1. **Updates manuais causam friccao**: tarefas de tracking manual introduzem delays e inconsistencias
2. **Avaliacao gerencial intensiva**: ~6h por desenvolvedor por ano em revisoes manuais e reunioes
3. **Privacy concerns**: monitoramento AI de performance levanta preocupacoes de privacidade
4. **Metricas como indicadores, nao determinantes**: autores enfatizam que devem ser "supportive indicators rather than strict performance determinants" para evitar uso punitivo
5. **Dependencia de dados sinteticos**: framework nao validado com dados reais

---

## Avaliacao de Qualidade Metodologica

| Criterio | Pontuacao (0-2) |
|----------|----------------|
| Objetivo claramente definido | 2 |
| Metodologia adequada ao objetivo | 1 |
| Amostra/contexto descrito | 0 (sintetico) |
| Ameacas a validade discutidas | 0 |
| Resultados com evidencia suficiente | 0 (projetados) |
| Contribuicao clara | 1 |
| **TOTAL** | **4/12 (Baixa)** |

---

## Limitacoes

1. **Apenas dados sinteticos/simulados** — nenhuma validacao real-world
2. **Metricas projetadas, nao medidas empiricamente** — resultados sao estimativas
3. **Contexto unico (IBM India)** — generalizacao desconhecida
4. **Privacy-aware collection mencionada mas nao detalhada** — implementacao vaga
5. **Sem comparacao com frameworks existentes** (DORA, SPACE, DevEx)
6. **Sem discussao de ameacas a validade**

---

## Contribuicao Principal

Framework multi-agente AI (I-AM-BEE) para automatizar avaliacao de desenvolvedores em ambiente agil, combinando transcricao de stand-ups, sincronizacao de tarefas, resolucao de blockers via RAG e monitoramento de performance com metricas individuais armazenadas em time-series DB.

## Trabalhos Futuros Relevantes

- Validacao empirica com equipes reais
- Integracao com mais plataformas (Trello, Asana alem de Jira)
- Mecanismos formais de privacidade para metricas de performance
- Comparacao com DORA/SPACE metrics

---

*Extraido em Marco 2026 para MLR: Software Developer Metrics in Practice*

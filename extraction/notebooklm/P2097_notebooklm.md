# P2097 — Integrating Generative AI Across the Agile Software Development Lifecycle

**Decisao: INCLUIDO | Qualidade: 4/5**

---

## Dados Bibliograficos

| Campo | Valor |
|-------|-------|
| **ID** | P2097 [1] |
| **Autores** | Bolatov Adlet Maratovich, Kumalakov Bolatzhan Armenovich [1] |
| **Ano** | Not explicitly specified in header (references include studies up to 2025) [1, 2] |
| **Venue** | Not specified [1] |
| **DOI** | Not specified [1] |
| **Tipo** | Research paper / Conference paper [1] |
| **Metodo** | Mixed methods (Framework engineering/Prototyping, A/B testing, Controlled experiment, LLM benchmarking, Ablation study) [1-4] |
| **Amostra** | 2 software architecture domains (Hospital Management System - HMS, E-commerce system), ~30 code generation and refactoring tasks (~15 per domain), benchmarked across 7 LLMs [2, 4] |
| **Contexto** | Academic / Simulated Agile software development environment (Astana IT University, two-week Agile Scrum sprints) [1, 2] |
| **Modo de trabalho** | Not specified [1] |
| **Metodologia** | Agile Scrum / DevOps [1, 3, 5, 6] |

---

## Objetivo

This paper aims to design and evaluate a structured generative AI-assisted software engineering framework integrated directly into the Agile Scrum lifecycle and CI/CD pipelines [1, 7]. By leveraging multi-agent collaborative systems (MetaGPT) and transitioning from a messaging prototype to an interactive web dashboard, the research automates key software development phases from requirements engineering to continuous deployment, evaluating the impact on DORA metrics, coding speed, and defect density across both premium paid LLMs and free local open-source models [1, 3, 4, 8-10].

---

## Questoes de Pesquisa

Nenhuma questão de pesquisa formalmente rotulada como RQ1, RQ2, etc. foi explicitamente enumerada no texto do artigo [3]. No entanto, o estudo é estruturado em torno de uma hipótese central e três áreas de investigação implícitas [3]:

- **RQ1 (Implícita)**: Como a integração direta de IA Generativa no modelo híbrido Agile Scrum/DevOps afeta a automação do ciclo de vida, a velocidade de desenvolvimento e a redução de erros manuais? [1, 3]
- **RQ2 (Implícita)**: Quais são as diferenças de desempenho, precisão arquitetural e métricas DORA entre o uso de LLMs pagos de ponta (ex: GPT-4o, Claude 3.5 Sonnet) e modelos open-source executados localmente (ex: Llama 3 8B, Mistral)? [4, 10-13]
- **RQ3 (Implícita)**: Qual a eficácia de um módulo de análise de defeitos e auditoria de segurança automatizada na detecção e correção de vulnerabilidades em código gerado por IA? [14, 15]

---

## Metricas e Instrumentos de Avaliacao

| Metrica | Categoria | Nivel | Como Coletada | Validada |
|---------|-----------|-------|---------------|----------|
| **Deployment Frequency** | Delivery / Activity | Organization / Team | Automated release tracking via CI/CD pipeline [5, 10] | Yes (Google Cloud DORA Report 2023) [3, 5] |
| **Lead Time for Changes** | Delivery | Team / Organization | Time tracked from commit to production deployment [5, 10] | Yes (Google Cloud DORA Report 2023) [3, 5] |
| **Change Failure Rate** | Quality / Delivery | Team / Organization | Percentage of deployments causing production failures or rollbacks [5, 10] | Yes (Google Cloud DORA Report 2023) [3, 5] |
| **Mean Time to Recovery (MTTR)** | Delivery / Reliability | Team / Organization | Average time required to restore service after a failure [5, 10] | Yes (Google Cloud DORA Report 2023) [3, 5] |
| **Defect / Bug Rate (per KLOC)** | Quality | Team / Codebase | Number of defects per 1,000 lines of code via static application security testing (SAST) and QA agent [2, 5, 10] | Yes (Standard software engineering metric) [3, 5] |
| **Architectural Accuracy Rate (%)** | Quality | Model / Task | Benchmarking accuracy in generating valid PlantUML scripts, PRDs, and cross-file dependencies [11, 12] | Partial (Custom benchmark across ~30 tasks) [2, 12] |
| **Coding Speed Increase (%)** | Productivity | Individual / Team | Comparative timing measurement for task completion against control groups / manual baselines [1, 16] | Yes (Chen et al., 2021 baseline) [16] |
| **Code / Test Coverage (%)** | Quality | Codebase / Pipeline | Automated unit test coverage tracking in CI/CD pipeline [8, 16, 17] | Yes (Fraser & Arcuri, 2013 / EvoSuite baseline) [16] |

---

## Frameworks e Metricas

### Frameworks Referenciados
- **DORA (DevOps Research and Assessment)**: APPLIED (used as the primary benchmark instrument to measure operational impact: Deployment Frequency, Lead Time for Changes, Change Failure Rate, MTTR) [3, 5, 10].
- **Agile Scrum**: APPLIED (used as the core operational methodology for sprint planning, user stories, and ceremonies) [1, 5, 6, 18].
- **DevOps / CI/CD**: APPLIED (used as the pipeline framework for automated testing, deployment, and security auditing) [3, 6, 17, 19].
- **MetaGPT**: APPLIED (multi-agent collaborative software engineering framework simulating software company roles) [1, 9].
- **EvoSuite**: REFERENCED (cited in literature review for genetic algorithm-based test generation) [16].
- **Waterfall / V-Model**: REFERENCED (discussed and evaluated as rigid alternative SDLC models) [5].

### Frameworks Propostos
- **Framework de Engenharia de Software Assistido por IA Generativa em Agile Scrum**: A structured multi-agent framework integrated into an interactive web application dashboard [1, 8]. It maps GenAI capabilities and MetaGPT role-specific agents (Boss, ProductManager, Architect, ProjectManager, Engineer, QA) directly into Agile Scrum ceremonies and artifacts, combining automated PlantUML system architecture generation, multi-agent code generation, static application security testing (SAST), and automated CI/CD pipeline monitoring [2, 6, 8, 9, 17, 18].

---

## Fatores que Influenciam Produtividade

### Fatores Positivos
| Fator | Categoria |
|-------|-----------|
| Automação multi-agente de tarefas repetitivas e geração de código (MetaGPT) [1, 9] | Technical / Process |
| Visualização centralizada e dashboard web interativo para acompanhamento de artefatos [8, 20] | Process / Technical |
| Uso de LLMs com alta precisão arquitetural (>90%: GPT-4o, Claude 3.5 Sonnet) [11, 12] | Technical |
| Sprints curtos e ciclos de feedback rápido do Agile Scrum integrados a pipelines CI/CD [3, 5, 6] | Process |
| Geração automatizada de diagramas PlantUML (Class/Sequence) e casos de teste automatizados [6, 9, 17] | Technical / Process |

### Fatores Negativos
| Fator | Categoria |
|-------|-----------|
| Erros de lógica e alucinações de endpoints em LLMs locais/gratuitos (Llama 3 8B, Mistral) [11, 13] | Technical / Human |
| Vulnerabilidades de segurança em código gerado por IA (SQL injection CWE-89, JWT hardcoded, buffer overflow) [14, 21] | Technical / Process |
| Restrições de interfaces baseadas em mensagens (ex: Telegram bot) para gerenciar artefatos visuais e estado do projeto [20] | Technical / Process |
| Fricção de integração de ferramentas de segurança locais (ex: Semgrep) em ambientes Windows vs Linux [22] | Technical / Organizational |
| Interpretação incorreta de requisitos por humanos sem automação (causa de 40–50% dos defeitos na literatura) [23] | Human / Process |

---

## Papel da IA e Automacao

| Campo | Valor |
|-------|-------|
| **Usa IA/ML?** | Yes — Generative AI models (GPT-4o, Claude 3.5 Sonnet, Gemini 1.5 Pro, GPT-3.5 Turbo, Gemini Flash, Llama 3 8B, Mistral) integrated via the MetaGPT multi-agent framework [1, 4, 9]. |
| **Automacao de coleta?** | Yes — Automated collection of DORA metrics, unit test coverage, static application security testing (SAST), and defect density tracking through the web dashboard and QA agent [2, 6, 8, 17]. |
| **Impacto de IA na produtividade?** | Significant positive impact: 55.8% increase in coding speed [1]; Lead Time for Changes reduced to 1–2 days (paid models) or 3–5 days (local models) [10]; Defect Rate reduced to 0.2–0.5 per KLOC (paid models) or 0.8–1.2 (local models) [10]; Daily / On-Demand deployment frequency achieved with premium models [10]. |

---

## Resultados Principais

- **Aumento da Velocidade de Codificação**: Aceleração de até 55.8% na velocidade de desenvolvimento e escrita de código [1, 16].
- **Acurácia Arquitetural dos Modelos**: Modelos pagos de alto desempenho apresentaram excelente precisão na geração de diagramas PlantUML, PRDs e dependências de arquivos (Claude 3.5 Sonnet: 95%, GPT-4o: 94%, Gemini 1.5 Pro: 91%) [11, 12]. Modelos open-source locais apresentaram desempenho inferior (Llama 3 8B: 68%, Mistral: 65%) [12].
- **Melhoria Significativa nas Métricas DORA (vs Baseline Tradicional)**:
  - *Deployment Frequency*: Evoluiu de quinzenal (baseline) para semanal (modelos locais) e diária/sob demanda (modelos pagos) [10].
  - *Lead Time for Changes*: Reduzido de 7–14 dias para 3–5 dias (modelos locais) e 1–2 dias (modelos pagos) [10].
  - *Change Failure Rate*: Reduzido de 15–20% para 10–15% (modelos locais) e 2–5% (modelos pagos) [10].
  - *Mean Time to Recovery (MTTR)*: Reduzido de 1–2 dias para <1 dia (modelos locais) e <4 horas (modelos pagos) [10].
  - *Defect Rate*: Reduzido de 1.5–2.0 defeitos por KLOC para 0.8–1.2 (locais) e 0.2–0.5 (pagos) [10].
- **Detecção e Correção Automatizada de Defeitos de Segurança**: O agente de QA e auditoria automatizada interceptou até 75% dos defeitos comuns, identificando e corrigindo SQL Injection (CWE-89), segredos JWT hardcoded e funções inseguras de memória (gets/strcpy) em C/C++ [1, 14].
- **Evolução da Interface**: A substituição do protótipo inicial em bot do Telegram por uma aplicação web centralizada eliminou gargalos de formatação e visualização de diagramas UML [8, 20].

---

## Desafios do Uso das Metricas

- **Propagação de Práticas Inseguras de Código**: A IA aprende com repositórios públicos e pode reproduzir padronizações inseguras (ex: SQL injection, segredos hardcoded em arquivos), tornando a análise estática automatizada indispensável [14, 21].
- **Alucinações e Erros Lógicos em LLMs Locais**: A menor capacidade de retenção de contexto em modelos abertos gera endpoints de API inexistentes e erros lógicos, aumentando a necessidade de intervenção humana na etapa de QA [11, 13].
- **Limitações de Interfaces Baseadas em Mensagens**: Bots de chat não oferecem a persistência de estado e a capacidade visual necessárias para gerenciar métricas e artefatos complexos de engenharia de software [20].
- **Fricção de Ferramentas de Segurança em Diferentes SOs**: Dificuldades técnicas ao executar scanners de vulnerabilidade locais (ex: Semgrep) em ambientes Windows evidenciam a necessidade de pipelines baseados em Linux [22].

---

## Avaliacao de Qualidade Metodologica

| Criterio | Pontuacao (0-2) |
|----------|----------------|
| Objetivo claramente definido | 2 [1, 7] |
| Metodologia adequada ao objetivo | 2 [2, 3] |
| Amostra/contexto descrito adequadamente | 1 [2] |
| Ameacas a validade discutidas | 1 [22] |
| Resultados com evidencia suficiente | 2 [10, 12, 14] |
| Contribuicao clara para pratica ou teoria | 2 [1, 9, 24] |
| **TOTAL** | **10/12** |

---

## Limitacoes

- Modelos open-source locais (Llama 3 8B, Mistral) enfrentam limitações na retenção de contextos estendidos necessários para o design de sistemas completos [11].
- Risco contínuo de geração de código contendo vulnerabilidades de segurança herdadas de dados de treinamento públicos [14, 21].
- Incompatibilidades operacionais e fricção na integração de ferramentas como Semgrep em sistemas operacionais Windows [22].
- Inadequação de interfaces de chat/messaging para a gestão abrangente do ciclo de vida de desenvolvimento de software [20].
- Avaliação empírica realizada em ambiente controlado com 2 domínios (Hospital Management System e E-commerce) e ~30 tarefas, requerendo validação futura em larga escala em ambientes corporativos reais [2].

---

## Contribuicao Principal

A principal contribuição do artigo é a proposição e avaliação empírica de um framework integrado de engenharia de software assistido por IA Generativa estruturado na metodologia Agile Scrum e impulsionado pela arquitetura multi-agente MetaGPT [1, 9]. O trabalho demonstra como a transição de protótipos de chat para um painel web centralizado viabiliza a automação ponta a ponta do SDLC — desde a análise de requisitos até a implantação contínua em CI/CD —, quantificando aumentos expressivos na velocidade de codificação (55.8%) e na otimização das métricas DORA, ao mesmo tempo em que comprova a necessidade indispensável de agentes automatizados de auditoria de segurança para interceptar vulnerabilidades em código gerado por IA [1, 8, 10, 14, 24].

---

*Extraido via NotebookLM em October 2026 para MLR: Software Developer Metrics in Practice*

---

💡 **Sugestão de próximo passo**: Gostaria que eu elaborasse um gráfico comparativo em imagem (PNG) ou um relatório detalhado em PDF focando especificamente nos resultados de desempenho dos modelos pagos versus modelos locais abertos?
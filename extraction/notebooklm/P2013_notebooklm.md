# P2013 — Abstracting Deployment Complexity with Platform Engineering Through Centralized Continuous Integration and Continuous Delivery

**Decisao: INCLUIDO | Qualidade: 5/5**

---

## Dados Bibliograficos

| Campo | Valor |
|-------|-------|
| **ID** | P2013 |
| **Autores** | Joseph Christian Yusmita, Jacqueline Audrey Iman, Venessa, Anderies [1, 2] |
| **Ano** | 2026 [3, 4] |
| **Venue** | Not specified (Academic paper, Computer Science Department, Bina Nusantara University) [1, 2] |
| **DOI** | Not specified |
| **Tipo** | Case study report / Conference paper [2, 5] |
| **Metodo** | Retrospective observational case study (Mixed methods) [2, 6, 7] |
| **Amostra** | 30 microservices migrated to production (out of ~300 enterprise services) observed across a 10-month period (April 2025 – February 2026); pipeline execution logs metadata + up to 39 recorded Microsoft Teams incident meetings [6-8] |
| **Contexto** | Industry (Large-scale enterprise with ~300 microservices) [2, 6] |
| **Modo de trabalho** | Not specified (recorded Microsoft Teams meetings used for collaborative incident remediation) [8, 9] |
| **Metodologia** | DevOps / Platform Engineering [2, 5] |

---

## Objetivo

The paper proposes a centralized CI/CD pipeline architecture that acts as an Internal Developer Platform (IDP) using Platform Engineering principles to abstract deployment complexity in enterprise microservice environments [2, 10]. The primary objective is to enable developers with limited DevOps experience to operate pipelines independently via declarative interfaces while enforcing security scanning and quality gates [11-13]. The study evaluates this architecture through a retrospective observational case study comparing a centralized approach against a previous decentralized approach across 30 microservices using standard DORA metrics [2, 6, 14, 15].

---

## Questoes de Pesquisa

- **RQ1**: How can a centralized CI/CD architecture be designed to help the operations team abstract deployment complexity through an IDP? [15]
- **RQ2**: To what extent does a centralized configuration pipeline reduce the operational complexity compared to the decentralized approach? [15]

---

## Metricas e Instrumentos de Avaliacao

| Metrica | Categoria | Nivel | Como Coletada | Validada |
|---------|-----------|-------|---------------|----------|
| Lead Time for Change | Delivery | Team/Organization | Programmatically scraped via Azure DevOps REST API (`Pipeline/Runs` endpoint) by calculating average pipeline execution duration from `createdDate` to `finishedDate` across successful production runs [16-18] | Partial (Standard DORA metric, but constrained by organizational boundaries to measure CI/CD pipeline execution duration rather than full commit-to-production time) [9, 19] |
| Change Failure Rate (CFR) | Quality | Team/Organization | Calculated by dividing failed deployments requiring remediation by total successful production deployments, mapped via timestamp overlap with recorded incident meetings [8, 20, 21] | Yes (Standard DORA metric) [14, 15, 20] |
| Mean Time to Restore (MTTR) | Quality | Team/Organization | Calculated as the average time to resolve affected services across recorded incidents, measured from the start of recorded Microsoft Teams incident meetings to the completion of the resolving pipeline run [8, 21, 22] | Yes (Standard DORA metric, validated via collaborative incident meeting proxy) [9, 14, 15, 21] |

---

## Frameworks e Metricas

### Frameworks Referenciados
- **DORA (DevOps Research and Assessment)**: APPLIED — Used as the core measurement framework to evaluate delivery performance (Lead Time, Change Failure Rate, and MTTR) [14, 15, 23].
- **GitOps**: REFERENCED — Cited as inspiration for the *Constrained Entry Point* principle and declarative configuration management via version-controlled repositories [24-26].
- **DevSecOps**: REFERENCED — Discussed in relation to embedding automated security scanning (GitHub Advanced Security) and quality test gates directly into the pipeline workflow [13, 16].
- **Team Topologies**: REFERENCED — Cited (Skelton & Pais) regarding the establishment of dedicated platform teams managing Internal Developer Platforms (IDPs) [27, 28].
- **Internal Developer Platform (IDP)**: APPLIED — Used as the underlying platform architecture model for self-service pipeline execution [2, 10, 27, 29].

### Frameworks Propostos
- **Centralized CI/CD IDP Architecture (Platform Engineering Framework)**: Proposes an enterprise CI/CD architecture structured around four core design principles [10, 24]:
  1. *Constrained Entry Point*: User interactions are restricted to predefined declarative YAML instances rather than direct infrastructure modifications [24, 30].
  2. *Fail-Fast Validation*: Runtime schema validation (implemented using Zod) detects configuration errors early and aborts before execution [25, 28, 31].
  3. *Standardization*: Mandatory security scanning (GHAS) and automated test gates enforce uniform quality standards [13, 28, 31].
  4. *Dynamic Strategies*: Flexible build and deployment strategies (Docker, Helm, Kubernetes) dynamically adapt to heterogeneous microservice stacks [7, 32, 33].

---

## Fatores que Influenciam Produtividade

### Fatores Positivos
| Fator | Categoria |
|-------|-----------|
| Centralização e padronização dos pipelines em um único repositório gerenciado [11, 34] | Technical |
| Capacidade de auto-serviço (self-service) com interfaces declarativas simples (IDP) [11, 30] | Process |
| Validação rápida de falhas (Fail-Fast Validation) com detecção precoce de erros [25, 28] | Technical |
| Gates de segurança (GHAS) e testes automatizados integrados obrigatoriamente [13, 31] | Process |
| Implementação de otimizações globais pela equipe de plataforma em um único local [34] | Organizational |

### Fatores Negativos
| Fator | Categoria |
|-------|-----------|
| Aumento da complexidade de abstração no repositório centralizado do IDP [35, 36] | Technical |
| Ponto Único de Falha (Single Point of Failure - SPF) no repositório central [35, 36] | Technical |
| Transferência do fardo de manutenção individual para a equipe de plataforma [36] | Organizational |
| Diagnóstico e depuração de falhas complexas mais difíceis, aumentando o MTTR [35, 36] | Process |
| Lacuna de habilidades em DevOps entre desenvolvedores e a equipe de infraestrutura [12] | Human |

---

## Papel da IA e Automacao

| Campo | Valor |
|-------|-------|
| Usa IA/ML? | No — The current system does not utilize AI/ML. However, the authors explicitly propose investigating Large Language Models (LLMs) or AI-driven diagnostic tools in future work to parse and debug complex pipeline failures [37, 38]. |
| Automacao de coleta? | Yes — Automated scraping of pipeline run metadata via Azure DevOps REST API (`Pipeline/Runs` endpoint) [7, 16]. |
| Impacto de IA na produtividade? | Not evaluated in the current study (proposed as future research to reduce MTTR) [37, 38]. |

---

## Resultados Principais

- **Redução de 77.9% no Lead Time**: O tempo médio de execução dos pipelines de implantação caiu de 22.6 minutos na abordagem descentralizada para 5.0 minutos na abordagem centralizada [14, 22].
- **Redução de 88.2% na Taxa de Falhas de Mudança (CFR)**: A porcentagem de implantações que resultaram em falha diminuiu de 16.7% para 2.0% [14, 34].
- **Aumento no Volume de Implantações**: O número de implantações bem-sucedidas em produção subiu de 143 (em 7 meses no modelo descentralizado) para 161 (em 3 meses no modelo centralizado) [34, 39].
- **Aumento de 63.0% no MTTR (Trade-off de Manutenção)**: O tempo médio de restauração de serviços aumentou de 3.0 horas para 5.0 horas, demonstrando que a centralização deslocou a complexidade para a manutenção da plataforma e introduziu um Ponto Único de Falha [14, 35, 36, 39].

---

## Desafios do Uso das Metricas

- **Restrição de Escopo no Lead Time**: Devido à falta de acesso direto dos mantenedores do IDP aos repositórios Git das aplicações, o Lead Time foi restrito à duração da execução do pipeline CI/CD [9, 19].
- **Proxy de Esforço Colaborativo via Reuniões**: A ausência de sistemas uniformes de chamados e monitoramento forçou o uso de reuniões gravadas no Microsoft Teams como proxy, capturando apenas o esforço colaborativo síncrono [9, 18].
- **Dificuldade de Diagnóstico no IDP**: A abstração da lógica de pipeline ocultou detalhes de execução, tornando o diagnóstico e a recuperação de falhas centralizadas mais demorados para a equipe de plataforma [35, 36].
- **Risco de Ponto Único de Falha (SPF)**: Alterações no repositório central de CI/CD têm o potencial de afetar e interromper múltiplos microserviços simultaneamente [35, 36].

---

## Avaliacao de Qualidade Metodologica

| Criterio | Pontuacao (0-2) |
|----------|----------------|
| Objetivo claramente definido | 2 |
| Metodologia adequada ao objetivo | 2 |
| Amostra/contexto descrito adequadamente | 2 |
| Ameacas a validade discutidas | 2 |
| Resultados com evidencia suficiente | 2 |
| Contribuicao clara para pratica ou teoria | 2 |
| **TOTAL** | **12/12** |

---

## Limitacoes

- **Impossibilidade de Medir Lead Time Completo**: A falta de acesso ao Git impediu medir o tempo desde o commit inicial até a entrada em produção [9, 19].
- **Inconsistência em Ferramentas de Incidente e Monitoramento**: A ausência de logs padronizados de incidentes exigiu o uso de reuniões gravadas do Teams como proxy [9].
- **Exclusão de Esforço Individual e Assíncrono**: Resolução individual de problemas, conversas assíncronas, testes manuais e atividades pós-incidente não foram capturadas no conjunto de dados [9, 18].
- **Recorte da Amostra**: Apenas 30 dos aproximadamente 300 microserviços da empresa foram migrados com sucesso para produção durante o período de 10 meses [6, 40].
- **Exclusão de Ferramentas Legadas**: Aplicações utilizando ferramentas como Jenkins foram excluídas por restrições de extração via API do Azure DevOps [16, 17].

---

## Contribuicao Principal

The paper provides empirical evidence on applying Platform Engineering principles to abstract deployment complexity in enterprise microservices through a centralized CI/CD Internal Developer Platform (IDP) [2, 10, 41]. Its primary contribution lies in demonstrating that while centralized CI/CD architectures substantially improve deployment speed (77.9% lower Lead Time) and delivery reliability (88.2% lower CFR), they introduce a key architectural trade-off: shifting complexity into platform maintenance and increasing service recovery time (63.0% higher MTTR) due to a Single Point of Failure [14, 36]. This offers practical architectural guidelines and baseline metrics for DevOps teams and platform engineering leaders [5].

---

*Extraido via NotebookLM em October 2026 para MLR: Software Developer Metrics in Practice*


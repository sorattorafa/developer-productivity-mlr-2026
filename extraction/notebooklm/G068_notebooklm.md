# G068 — MetricSynth: Framework for Aggregating DORA and KPI Metrics Across Multi-Platform Engineering

**Decisao: INCLUIDO | Qualidade GL: 6/6**

---

## Dados Bibliograficos

| Campo | Valor |
|-------|-------|
| **ID** | G068 |
| **Autor/Organizacao** | Pallav Jain, Yuvraj Agrawal, Ashutosh Nigam, Pushpak Patil (Adobe Inc.) |
| **Data** | 2025/2026 (baseado em referências e dados de 2025) |
| **Tipo** | Technical Paper / White paper |
| **URL** | Não disponível nos trechos fornecidos |

---

## Resumo

O documento descreve o **MetricSynth**, um framework centralizado desenvolvido pela Adobe para agregar métricas de engenharia e **Key Performance Indicators (KPIs)** provenientes de ferramentas silenciadas (Jira, Git, Jenkins, Splunk, etc.) [1, 2]. A arquitetura é composta por seis camadas, incluindo ingestão de dados via **cron jobs**, armazenamento em **MongoDB** com **dual-schema strategy** (dados brutos e processados), processamento para pré-computação de métricas e uma camada de apresentação utilizando a ferramenta de **Business Intelligence (BI)** de código aberto **Metabase** [3-6].

A implementação do sistema visou reduzir o esforço manual de geração de relatórios, que anteriormente consumia horas de gerentes de engenharia e programas [7, 8]. O framework foca em cinco áreas principais: **Developer Productivity**, **Quality & Reliability**, **Automation Tooling**, **Engagement** e **Operational Efficiency** [9, 10]. Os resultados indicam uma economia estimada de 40 horas semanais por pessoa na organização e a capacidade de identificar rapidamente gargalos através da correlação de dados entre diferentes plataformas [8, 11].

---

## Frameworks Mencionados

*   **DORA (DevOps Research and Assessment):** Recomendado e utilizado como base para métricas de eficiência operacional e produtividade [9, 12, 13].
*   **DevEx (Developer Experience):** Discutido como o foco central para visibilidade da saúde do ecossistema de software [1, 9].
*   **Goodhart’s Law:** Mencionado no contexto de mitigar o risco de métricas se tornarem alvos de manipulação [12, 14].

---

## Metricas Mencionadas

*   **Lead Time for Changes (DORA):** Tempo mediano entre o code commit e o deployment em produção [15].
*   **PR Cycle Time:** Tempo mediano da criação do Pull Request até o merge [16].
*   **Code Commit Frequency:** Média de commits por desenvolvedor por dia [16].
*   **Build Induced Latency:** Tempo de espera por feedback do CI após submissão de PR [16].
*   **PR Throughput:** Número médio de Pull Requests mesclados por equipe por semana [16].
*   **Co-pilot Assistance Metrics:** Taxas de aceitação/declínio e linhas de código geradas por IA [16].
*   **Stability / User Crash Rate:** Porcentagem de usuários sem crashes ou sessões que terminam em crash [17].
*   **Blocker/Critical Bugs:** Quantidade de bugs de alta prioridade abertos no Jira [17].
*   **Bug Mix Overall:** Distribuição de bugs por níveis de severidade [17].
*   **Deployment Frequency (DORA):** Número de implantações em produção por semana [13].
*   **Main Fail Rate (DORA-aligned):** Porcentagem de falhas de build no branch principal [13].
*   **Average Turnaround Time:** Tempo total do disparo do build até a conclusão [13].
*   **Automation Code Coverage:** Porcentagem de declarações de código cobertas por testes automatizados [18].
*   **Automation Health:** Porcentagem de passagens de suítes de testes em um ciclo [18].
*   **MAU (Monthly Active Users) & RMAU:** Métricas de engajamento de usuários ativos [19].

---

## Insights para Praticantes

*   **Centralização de Dados:** Unificar dados de ferramentas heterogêneas (Jira, Jenkins, Splunk) permite identificar correlações que seriam invisíveis em silos, como o impacto de falhas de CI no **PR Cycle Time** [11, 12].
*   **Dual-Schema Storage:** Utilizar coleções de dados brutos (**Raw Data**) para auditoria e dados processados (**Processed Data**) para visualização otimiza a performance de ferramentas de BI [4].
*   **Pre-computation:** Realizar o cálculo de métricas complexas na camada de processamento (atuando como um **caching layer**) garante carregamento quase instantâneo dos dashboards no Metabase [5, 20].
*   **Ética e Cultura:** Para evitar o uso punitivo de métricas, deve-se agregar dados de saída individual (como **Commit Frequency**) apenas em nível de equipe ou organização, focando em tendências em vez de valores absolutos [21, 22].
*   **Alertas Proativos:** Implementar uma camada de alerta (**Alerting Layer**) que notifica via Slack ou e-mail quando métricas críticas (ex: **Crash Rate**) ultrapassam thresholds definidos [23].

---

## Avaliacao de Qualidade GL (Garousi et al.)

| Criterio | Pontuacao (0-1) |
|----------|----------------|
| Autoridade do autor/organizacao | 1 |
| Descricao de metodologia | 1 |
| Data de publicacao | 1 |
| Objetividade (vies comercial) | 1 |
| Referencias citadas | 1 |
| Contribuicao nova | 1 |
| **TOTAL** | **6/6** |

---

*Extraido via NotebookLM em March 2026 para MLR: Software Developer Metrics in Practice*
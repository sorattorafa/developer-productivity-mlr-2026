# G012 — Value Streams Dashboard - GitLab Docs

**Decisao: INCLUIDO | Qualidade GL: 4.5/6**

---

## Dados Bibliograficos

| Campo | Valor |
|-------|-------|
| **ID** | G012 |
| **Autor/Organizacao** | GitLab |
| **Data** | Não mencionado (Acessado em 04 de junho de 2026) |
| **Tipo** | Documentation |
| **URL** | Não especificado na fonte (Seção: *Analyze GitLab usage > Value streams dashboard*) |

---

## Resumo

A documentação detalha o **Value Streams Dashboard** do GitLab, um painel customizável disponível para os níveis Premium e Ultimate (GitLab.com, Self-Managed e Dedicated). Este dashboard atua como uma única fonte de verdade (SSOT) centralizada para que stakeholders possam identificar tendências, padrões e oportunidades de melhoria em processos de transformação digital. 

O painel fornece visualizações para diversas categorias de métricas, incluindo **DORA**, **Value Stream Analytics (VSA)**, **Vulnerabilidades** e o impacto do **GitLab Duo** (IA). O sistema agrega dados continuamente em background e permite comparar o desempenho entre diferentes projetos e equipes ao longo de um período (como comparações mensais retrospectivas de seis meses), ajudando a identificar precocemente tendências negativas e a exposição a riscos de segurança.

---

## Frameworks Mencionados

*   **DORA (DevOps Research and Assessment)**: Avaliado em painéis dedicados, classificando a performance dos projetos nas categorias Alta, Média e Baixa.
*   **DevSecOps**: Utilizado para agrupar comparações de métricas de ciclo de vida (Lifecycle), métricas DORA e métricas de segurança.
*   **Value Stream Management (VSM)**: Abordagem central que baseia a estruturação do painel para demonstrar o fluxo de entrega de valor.

---

## Metricas Mencionadas

*   **DORA Metrics**: Inclui **Deployment frequency** (média de deploys para produção por dia), **Lead time for changes**, **Time to restore service** e **Change failure rate**.
*   **Lifecycle Metrics (VSA)**: Inclui **Lead time** (mediana do tempo da criação ao fechamento de uma issue) e **Cycle time** (mediana do primeiro commit no merge request até o fechamento da issue).
*   **Productivity & CI/CD**: Medições como **Merge request throughput** (MRs mergeados por mês), **Total pipeline runs**, **Pipeline success/failure rate** e **Median time to merge**.
*   **AI Impact (GitLab Duo)**: Acompanha métricas de adoção de IA, como **Code Suggestions acceptance rate**, **Feature usage** e **Non-Agentic Chat usage**.
*   **Security Metrics**: Monitoramento contínuo de **Critical vulnerabilities** e **High vulnerabilities** ao longo do tempo.

---

## Insights para Praticantes

*   **Governança como Código**: O dashboard não é apenas visual; as equipes podem customizar os painéis através de arquivos de configuração **YAML** armazenados no repositório. Isso permite o controle de versão das métricas, possibilitando rastrear o histórico de mudanças no painel e facilitando a colaboração.
*   **Medição do ROI de Inteligência Artificial**: Uma novidade valiosa para líderes técnicos é a capacidade de medir o impacto direto e o Retorno sobre Investimento (ROI) da adição de IA (GitLab Duo) no ciclo de desenvolvimento de software (SDLC).
*   **Automação de Relatórios**: Para manter as lideranças informadas de forma proativa, os praticantes podem utilizar uma ferramenta de CI/CD integrada à GraphQL API para agendar **Scheduled Reports**, que geram automaticamente issues contendo tabelas comparativas de métricas em formato Markdown.
*   **Classificação de Performance DORA**: O painel **DORA Performers score** traduz automaticamente as métricas brutas em scores categóricos (ex: projetos com *High deployment frequency* realizam 30 ou mais deploys por mês), facilitando o benchmarking interno.
*   **Independência de Ferramentas Externas**: Métricas cruciais de velocidade e throughput (como DORA e tempo de merge) são calculadas nativamente sem a obrigatoriedade de integração com o Jira.

---

## Avaliacao de Qualidade GL (Garousi et al.)

| Criterio | Pontuacao (0-1) |
|----------|----------------|
| Autoridade do autor/organizacao | 1 |
| Descricao de metodologia | 1 |
| Data de publicacao | 1 |
| Objetividade (vies comercial) | 0.5 |
| Referencias citadas | 0 |
| Contribuicao nova | 1 |
| **TOTAL** | **4.5/6** |

---

*Extraido via NotebookLM em June 2026 para MLR: Software Developer Metrics in Practice*
# G011 — DevOps Research and Assessment (DORA) Metrics - GitLab Docs

**Decisao: INCLUIDO | Qualidade GL: 4.5/6**

---

## Dados Bibliograficos

| Campo | Valor |
|-------|-------|
| **ID** | G011 |
| **Autor/Organizacao** | GitLab [1] |
| **Data** | Não mencionado (Acessado em 08 de março de 2026) [1] |
| **Tipo** | Documentation [1] |
| **URL** | https://docs.gitlab.com/user/analytics/dora_metrics/ [1] |

---

## Resumo

A documentação descreve a implementação das métricas de **DevOps Research and Assessment (DORA)** dentro da plataforma GitLab, especificamente para os níveis Ultimate, GitLab.com, Self-Managed e Dedicated [1]. O objetivo dessas métricas é fornecer insights baseados em evidências sobre a performance de DevOps, focando em quatro medições fundamentais que avaliam a velocidade de entrega e a estabilidade das mudanças em produção [1, 2].

O GitLab divide essas métricas em duas categorias principais: **Velocity** e **Stability** [2]. O sistema utiliza métodos específicos de agregação de dados, como médias diárias para frequência e medianas para métricas de tempo, disponibilizando os resultados através de painéis como o **Value Streams Dashboard**, gráficos analíticos de CI/CD, relatórios de insights e APIs (GraphQL e REST) [3].

---

## Frameworks Mencionados

*   **DORA**: Discutido e implementado como o framework central para medição de performance de entrega de software [1, 3].

---

## Metricas Mencionadas

*   **Deployment frequency (Velocity)**: Medida pela média de **successful deployments** por dia em um ambiente específico [2].
*   **Lead time for changes (Velocity)**: Calculado em segundos como o tempo necessário para entregar um **merge request** com sucesso, desde o momento do merge até o código estar rodando em produção [2].
*   **Change failure rate (Stability)**: Medido como o percentual de **deployments** que causam um incidente em produção [3].
*   **Time to restore service (Stability)**: Medido como o tempo mediano em que um incidente permaneceu aberto em um ambiente de produção [3].

---

## Insights para Praticantes

*   As métricas DORA permitem que as equipes demonstrem de forma quantitativa a rapidez com que entregam valor e a resiliência de seus processos de produção [1].
*   A plataforma diferencia o cálculo de **Lead time for changes** focando especificamente no intervalo entre o merge e a execução em produção, utilizando segundos como unidade de precisão [2].
*   Para fins de análise e relatórios customizados, os praticantes podem extrair esses dados diretamente via **GraphQL API** ou **REST API**, além de visualizá-los nos dashboards nativos do GitLab [3].
*   A consistência dos dados é mantida através de agregação padronizada: médias diárias para frequência e medianas para as demais métricas de tempo e falha [3].

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

*Extraido via NotebookLM em March 2026 para MLR: Software Developer Metrics in Practice*
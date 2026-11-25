# G011 — DevOps Research and Assessment (DORA) Metrics - GitLab Docs

**Decisao: INCLUIDO (Discute métricas de desempenho de entrega de software) | Qualidade: 4/5**

---

## Dados Bibliograficos

| Campo | Valor |
|-------|-------|
| **ID** | G011 |
| **Autores** | GitLab Inc. |
| **Ano** | 2024 |
| **Venue** | GitLab Documentation |
| **URL** | https://docs.gitlab.com/user/analytics/dora_metrics/ |
| **Tipo** | Documentação Técnica |
| **GL Tier** | 2nd (Vendor Documentation) |
| **Metodo** | Documentação de implementação e métricas |
| **Contexto** | Plataforma GitLab CI/CD |

---

## Objetivo
Documentar a implementação e utilização das métricas DORA (DevOps Research and Assessment) na plataforma GitLab, fornecendo uma base para medir a performance de entrega de software e a estabilidade em produção.

---

## Frameworks e Metricas

### Frameworks Mencionados
- DORA (DevOps Research and Assessment) - 4 métricas principais

### Metricas Propostas/Discutidas
- **Deployment Frequency**: Número médio de deployments por dia para um ambiente específico
- **Lead Time for Changes**: Tempo em segundos para entregar uma merge request em produção (do merge até código rodando)
- **Time to Restore Service**: Tempo mediano que um incidente permaneceu aberto em produção
- **Change Failure Rate**: Percentual de deployments que causam incidentes em produção

---

## Principais Contribuicoes
- Implementação integrada de métricas DORA na plataforma GitLab com cálculo automático
- Visualização das métricas em múltiplos formatos: Value Streams Dashboard, gráficos CI/CD, relatórios Insights e APIs (GraphQL/REST)
- Metodologia de agregação de dados usando médias diárias para frequência de deployment e medianas para outras métricas
- Distinção clara entre métricas de velocidade (deployment frequency, lead time) e estabilidade (change failure rate, restore time)
- Acesso a dados em camadas Ultimate do GitLab com suporte para GitLab.com, Self-Managed e Dedicated

---

## Contribuicao Principal
GitLab fornece uma implementação integrada e operacional das métricas DORA, permitindo que equipes meçam automaticamente sua performance de entrega de software sem ferramentas externas adicionais. A documentação detalha os cálculos específicos para cada métrica, facilitando a adoção de frameworks de avaliação de performance baseados em pesquisa (Kim et al., 2018). Isso permite que organizações de qualquer tamanho obtenham "evidence-based insights" sobre sua capacidade de entrega de mudanças e a qualidade de suas produções, fundamentais para avaliar a produtividade e maturidade do desenvolvimento de software.

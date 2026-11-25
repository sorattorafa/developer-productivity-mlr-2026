# P0011 — QEX: Automated Testing Observability and QA Developer Experience Framework

**Decisao: INCLUIDO | Qualidade: 4/5**

---

## Dados Bibliograficos

| Campo | Valor |
|-------|-------|
| **ID** | P0011 |
| **Autores** | Huang Luohua Locke, Yap Kai Ting Keshia, Joseph Chu Ken Yu, Hock Yao Chua |
| **Ano** | 2023 |
| **Venue** | 2023 IEEE Conference on Software Testing, Verification and Validation (ICST) |
| **DOI** | 10.1109/ICST57152.2023.00049 |
| **Tipo** | Estudo de caso industrial com implementação de framework |
| **Metodo** | Engenharia de software empírica; design e implementação de arquitetura event-driven |
| **Amostra** | Mais de 100 engenheiros de QA em 10 linhas de produto na empresa Shopee |
| **Contexto** | Ambiente empresarial de escala grande com milhares de testes executados diariamente |
| **Modo de trabalho** | Integração com múltiplas ferramentas (Git, Jenkins, Jira, InfluxDB, Grafana) |

---

## Objetivo
Desenvolver um framework de observabilidade (QEX) que integra fontes de dados de teste comuns para fornecer visibilidade abrangente sobre desenvolvimento de testes e melhorar a experiência do desenvolvedor de QA (QA Developer Experience) em contextos empresariais de escala grande.

---

## Questoes de Pesquisa
- **RQ1**: Como integrar múltiplas fontes de dados de teste para obter observabilidade abrangente?
- **RQ2**: Que métricas são mais relevantes para o QA Developer Experience?

---

## Metricas e Instrumentos de Avaliacao
- **Métricas de Qualidade**: Taxa de aprovação, tempo de execução, flakiness, cobertura por serviço, mantenedores por caso
- **Métricas de Dependência**: Casos com taxas de falha correlacionadas
- **Métricas de Uso**: Taxa de execução, executor principal de testes
- **Métricas de Desenvolvimento**: Novos casos diários, serviços com suporte limitado, frequência de mudanças
- **Métricas de Equipe**: Alocação de trabalho de testes
- **Métricas de Valor**: Tickets assinados por testes, bugs encontrados
- **Active Score**: Razão de testes executados para testes no ramo master
- **Stability Score**: Combinação de Active Score com taxa de aprovação
- **Dashboard Grafana** para visualização em tempo real

---

## Resultados Principais
- QEX está em produção suportando 100+ engenheiros de QA em 10 linhas de produto
- Dezenas de milhares de testes executados diariamente sem impacto significativo no desempenho
- Tempo médio de reação da arquitetura event-driven é de alguns milissegundos
- Integração do Kafka minimiza perda de dados
- Framework permite plugar facilmente novas fontes de dados
- Métricas fornecidas são simples, obtidas facilmente e fornecidas em tempo real

---

## Desafios do Uso das Metricas
- **Seleção de métricas**: Toda métrica apresenta viés; difícil escolher conjunto adequado sem distorcer incentivos
- **Contexto insensível**: Implementação não é context-sensitive e requer flagging manual em casos extremos
- **Definição de mantenedor**: Baseada no último contribuidor do git log, pode estar imprecisa após refactoring
- **Risco de abuso**: Métricas simples podem ser usadas de forma contraproducente se medindo qualidade isoladamente
- **Complexidade técnica**: Implementação requer manutenção de múltiplos componentes
- **Customização de testes**: Modificações de biblioteca de teste requerem esforço adicional de manutenção

---

## Contribuicao Principal
Apresenta QEX, primeiro framework industrial padronizado para observabilidade integrada de testes automatizados com implementação de código aberto. Demonstra como integrar dados de múltiplas fontes (Git, Jenkins, Jira) através de arquitetura event-driven para fornecer feedback compreensivo, confiável e oportuno sobre atividade de testes, elevando QA Developer Experience em ambientes empresariais de larga escala.

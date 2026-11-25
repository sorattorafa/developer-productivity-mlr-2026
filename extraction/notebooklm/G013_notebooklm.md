Aqui está o resumo estruturado com base nas fontes fornecidas, seguindo estritamente o formato solicitado:

# G012 — Value Stream Analytics - GitLab Docs

**Decisao: INCLUIDO | Qualidade GL: 4.5/6**

---

## Dados Bibliograficos

| Campo | Valor |
|-------|-------|
| **ID** | G012 |
| **Autor/Organizacao** | GitLab |
| **Data** | Não mencionado (Acessado em 04 de junho de 2026) |
| **Tipo** | Documentation |
| **URL** | GitLab Docs - Secção "Value stream analytics" |

---

## Resumo

A documentação do GitLab detalha o recurso de **Value stream analytics**, desenhado para calcular a duração de todas as etapas do processo de desenvolvimento de software. A funcionalidade auxilia as empresas a visualizarem seus fluxos de trabalho *DevSecOps* de ponta a ponta, permitindo a identificação de ineficiências, gargalos processuais e fatores que desaceleram o ciclo de vida do desenvolvimento. 

O sistema possui uma estrutura hierárquica baseada em fluxos de valor (*value streams*) e estágios (*stages*), onde cada estágio é definido e medido através de uma combinação de eventos iniciais e finais gerados a partir de *issues* e *merge requests*. A plataforma permite a utilização de fluxos padrão do sistema ou a criação de fluxos customizados, fornecendo métricas de produtividade do ciclo de vida e de performance de engenharia.

---

## Frameworks Mencionados

*   **Value Stream Management (VSM)**: Utilizado como conceito estrutural para organizar o processo de trabalho que entrega valor aos clientes em estágios mensuráveis.
*   **DevSecOps**: Mencionado como a natureza dos fluxos de trabalho que a ferramenta visa visualizar e otimizar ponta a ponta.
*   **DORA (DevOps Research and Assessment)**: Suportado através da extração de métricas de performance nativas pelo *Value Streams Dashboard* (disponível nas tiers Ultimate/Premium).

---

## Metricas Mencionadas

*   **Lead time (Lifecycle metrics)**: O tempo mediano calculado a partir do momento em que uma *issue* foi criada até o momento em que foi fechada.
*   **Cycle time (Lifecycle metrics)**: O tempo mediano entre o momento em que uma *issue* é referenciada pela primeira vez na mensagem de *commit* de um *merge request* e quando a referida *issue* é fechada.
*   **New issues (Lifecycle metrics)**: O número absoluto de novas *issues* criadas no período.
*   **Deploys (Lifecycle metrics)**: O número total de *deployments* realizados em um ambiente de produção.
*   **Stage durations**: O tempo mediano que os itens gastam em etapas de desenvolvimento pré-definidas, como *Issue*, *Plan*, *Code*, *Test*, *Review* e *Staging*.
*   **DORA metrics**: A plataforma também lista as métricas DORA — *Deployment frequency*, *Lead time for changes*, *Time to restore service* e *Change failure rate* — integradas ao fluxo de valor.

---

## Insights para Praticantes

*   A duração de cada estágio baseia-se na fórmula explícita: **Tempo do evento final - Tempo do evento inicial**. No entanto, para itens que transitam várias vezes de ida e volta entre os estágios, a medição contabiliza exclusivamente os *timestamps* dos eventos mais recentes (finais).
*   Para acompanhar *workflows* altamente complexos e repetitivos, as equipes podem utilizar a configuração de **Duração Cumulativa de Eventos de Labels** (*Cumulative label event duration*), que soma os fragmentos de tempo (ex: status "em progresso") sem inflar erroneamente o total em horas/dias em que um item ficou paralisado.
*   É recomendado aos times de engenharia o uso de automação (*webhooks*) para aplicar *labels* automaticamente em etapas chave do fluxo, garantindo dados precisos para o *Value stream analytics* customizado.
*   Para fins de relatórios externos e painéis corporativos complexos, os profissionais podem utilizar a **Value Stream Analytics GraphQL API** para extrair metadados das durações ou criar *scripts* (via *scheduled pipelines*) para comparar distorções temporais e demonstrar mudanças de tendência em métricas de produtividade.

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

*Extraido via NotebookLM em Junho de 2026 para MLR: Software Developer Metrics in Practice*
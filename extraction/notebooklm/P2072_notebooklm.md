# P2072 — Develop, Deploy, Operate: A holistic model for understanding the costs and value of software development [1]

**Decisao: INCLUIDO | Qualidade: 3.5/5** [1-3].

---

## Dados Bibliograficos

| Campo | Valor |
|-------|-------|
| **ID** | P2072 [1] |
| **Autores** | Titus Winters, Leah Rivers, Salim Virji [1] |
| **Ano** | 2025 [4] |
| **Venue** | ACM (ACM Queue) [1, 4] |
| **DOI** | Não especificado no artigo [1] |
| **Tipo** | Journal article / Technical practice article [1, 4] |
| **Metodo** | Conceptual model / Technical position paper [1, 2] |
| **Amostra** | Não aplicável (modelo conceitual baseado na experiência prática dos autores na indústria) [1, 4-6] |
| **Contexto** | Industry (desenvolvimento comercial de software em larga escala na Google, Adobe e AWS) [1, 4-6] |
| **Modo de trabalho** | Not specified [1] |
| **Metodologia** | DevOps, Continuous Deployment (CD), Agile [7-9] |

---

## Objetivo

O objetivo principal do artigo é apresentar um modelo holístico para compreender os custos, o valor comercial e as trocas de recursos (*tradeoffs*) envolvidos no desenvolvimento de software comercial através de três processos interdependentes: desenvolvimento, implantação (*deployment*) e operação [1, 10]. O trabalho busca estabelecer um vocabulário compartilhado entre equipes de produto, engenharia de plataforma e liderança [1], fornecendo uma estrutura para avaliar o impacto mensurável de investimentos em infraestrutura, ferramentas de desenvolvimento e otimização de processos através de quatro dimensões de impacto [3, 11, 12].

---

## Questoes de Pesquisa

O artigo é um estudo conceitual e de análise técnica da indústria, não apresentando questões de pesquisa formais (RQ1, RQ2, etc.) explicitamente formuladas [1, 2].

---

## Metricas e Instrumentos de Avaliacao

| Metrica | Categoria | Nivel | Como Coletada | Validada |
|---------|-----------|-------|---------------|----------|
| **Commit to deploy time** | Delivery / Activity | Team / Organization | Telemetria automatizada do pipeline de CI/CD [7, 13] | Yes (DORA) [7, 13] |
| **Change failure rate** | Quality / Delivery | Team / Organization | Telemetria automatizada de monitoramento e incidentes [13, 14] | Yes (DORA) [14, 15] |
| **Failed deployment recovery time (MTTR)** | Delivery / Quality | Team / Organization | Telemetria de sistemas de release e monitoramento [14, 16] | Yes (DORA) [14, 15] |
| **Release cadence / Frequency** | Delivery / Activity | Team / Organization | Registros automatizados de implantação [8, 13, 17] | Yes [13, 17] |
| **Lines of Code (LOC)** | Activity | Individual | Logs do sistema de controle de versão [18] | No (citada explicitamente como indicador inadequado) [18] |
| **Proposed / submitted changes (PRs / Commits)** | Activity | Individual | Logs de VCS e ferramentas de code review [18] | Partial (indica atividade, mas não resultados ou valor) [18] |
| **Feature count / Feature velocity** | Productivity / Delivery | Team / Organization | Ferramentas de gestão de projetos / issue trackers [18] | Partial (difícil definição precisa de "feature") [18] |
| **Edit-build-test cycle time / Presubmit latency** | DevEx / Productivity | Individual / Team | Telemetria de IDE e sistemas de compilação [19, 20] | Yes [19, 20] |
| **IDE feature usage (autoformatting / autofix)** | DevEx / Activity | Individual / Team | Telemetria do IDE [20-22] | Partial [20, 21] |
| **Developer self-reported productivity / Well-being** | Satisfaction / DevEx | Individual | Pesquisas qualitativas / pesquisas de clima [23] | Yes (DORA / SPACE) [23, 24] |
| **Defect Detection and Resolution (DDR) cost** | Quality / Efficiency | Organization / Team | Função de estimativa consensual baseada em tempo de exposição e engenheiros afetados [2, 21] | Partial (modelo de estimativa proposto) [2, 21] |
| **Defect-generation rate** | Quality | Individual / Team | Logs de testes e rastreadores de bugs [19] | Partial [19] |
| **Defect false negative rate** | Quality | Team / System | Correlação entre pipeline e incidentes em produção [25] | Partial [25] |
| **Defect false positive rate** | Quality / DevEx | Team | Telemetria de sistemas de testes e CI [20, 25] | Partial [20, 25] |
| **Outage counts** | Quality / Reliability | Organization | Gestão de incidentes [15] | Partial (proxy macro, sem significância estatística para ferramentas isoladas) [15] |
| **Customer-facing compute consumption** | Efficiency / Hardware | Organization / System | Telemetria de nuvem e consumo de hardware em produção [26, 27] | Yes [26, 27] |
| **Internal engineer-facing compute consumption** | Efficiency / Hardware | Organization / Team | Telemetria de infraestrutura de CI/CD e testes [26, 27] | Yes [26, 27] |

---

## Frameworks e Metricas

### Frameworks Referenciados
- **DORA (DevOps Research and Assessment)**: REFERENCED e APPLIED (Discutido e aplicado para métricas de entrega como *commit-to-deploy*, taxa de falha em mudanças, tempo de recuperação e bem-estar) [7, 13-15, 23].
- **SPACE Framework**: REFERENCED (Discutido como um lembrete de que métricas e proxies de produtividade devem ser usados em uma constelação de métricas em tensão mútua) [24].

### Frameworks Propostos
- **Modelo Holístico Develop, Deploy, Operate (DDO)**: Modelo de fluxo de trabalho de desenvolvimento de software comercial que divide a entrega de software em três processos interdependentes [1, 10]:
  1. *Development*: Processo criativo centrado no ser humano para projetar e expressar intenção [18, 28, 29].
  2. *Deployment*: Processo de fábrica automatizado voltado para avaliação mecanizada de testes e sinais de qualidade [7, 29].
  3. *Operation*: Processo focado em lidar com o inesperado em produção e maximizar o valor acumulado no tempo [8, 17].
- **Estrutura das Quatro Formas de Impacto Mensurável**:
  1. *Product Success* (Receita, alcance, adoção, confiança do usuário e satisfação do cliente) [11].
  2. *Hardware Resource Efficiency* (Eficiência no consumo de computação voltada ao cliente e interna de engenharia) [11, 26].
  3. *Engineering Capacity* (Redução do trabalho braçal e sofrimento na implantação, e otimização do custo de detecção e resolução de defeitos - DDR) [11, 21, 30, 31].
  4. *Strategic Capabilities* (Capacidades qualitativas inéditas, telemetria e uso de IA para síntese de informações) [11, 31, 32].
- **Modelo de Estimativa de Custo de Detecção e Resolução de Defetos (DDR)**: Função de estimativa consensual na qual o custo de um defeito escala linearmente com o tempo de exposição e a quantidade de engenheiros expostos [2, 21].

---

## Fatores que Influenciam Produtividade

### Fatores Positivos
| Fator | Categoria |
|-------|-----------|
| Automação de processos de implantação (CI/CD) e eliminação de trabalho braçal (*toil*) | Technical / Process [7, 29, 30] |
| Feedback rápido no presubmit e ferramentas integradas ao IDE (autoformatação e autofix) | Technical / DevEx [20-22] |
| Cadência de lançamentos frequente (*Continuous Deployment*) | Process [8, 16, 17] |
| Uso de componentes reutilizáveis, padrões de design e ferramentas de modelagem | Technical / Process [24, 29] |
| Educação e treinamento técnico eficaz para desenvolvedores | Human / Organizational [19, 33] |
| Telemetria aprimorada, diagnósticos e ferramentas de visibilidade (ex: *flame graphs*) | Technical [31, 32, 34] |
| Uso de IA para agregação, síntese de dados e auxílio à tomada de decisão | Technical / Human [32] |
| Padronização de ferramentas e infraestrutura compartilhada entre equipes | Organizational / Process [9, 35] |

### Fatores Negativos
| Fator | Categoria |
|-------|-----------|
| Envolvimento humano em etapas rotineiras de implantação (*deployment pain* e *toil*) | Process / Human [7, 29, 30] |
| Alta latência no ciclo de desenvolvimento e testes (*edit-build-test latency*) | Process / Technical [19, 20, 36] |
| Detecção tardia de defeitos no fluxo de trabalho | Process / Technical [21, 35, 37] |
| Altas taxas de falsos positivos em testes de presubmit e integração | Technical / DevEx [20, 25] |
| Acúmulo de trabalho em progresso (*Work in Progress* - WIP) não implantado | Process [13, 36] |
| Frustração e perda de bem-estar do desenvolvedor decorrentes de gargalos criativos e burocracia | Human / Organizational [23, 30] |
| Falhas de qualidade e defeitos manifestados em produção | Quality / Organizational [37-39] |

---

## Papel da IA e Automacao

| Campo | Valor |
|-------|-------|
| **Usa IA/ML?** | Yes — O artigo discute a IA como uma capacidade estratégica para agregar e sintetizar informações brutas em formatos utilizáveis para suporte à decisão humana [4, 32]. |
| **Automacao de coleta?** | Yes — Recomenda a automação completa da coleta de métricas de deployment (DORA), telemetria de CI/CD e infraestrutura [7, 9, 13, 29]. |
| **Impacto de IA na produtividade?** | O artigo compara o impacto da IA ao surgimento dos motores de busca nos anos 1990, destacando ganhos de produtividade ao transformar dados dispersos em visões consolidadas [32]. |

---

## Resultados Principais

- **Aumento de até 50% no Valor Acumulado com Releases Diários:** Equipes que realizam lançamentos diários em vez de trimestrais podem obter um aumento de até 50% no integral de valor implantado ao longo do tempo, mantendo a mesma produção total de mudanças [8, 17].
- **Natureza Criativa do Desenvolvimento:** O desenvolvimento de software é um processo humano, criativo e de design; métricas individuais de atividade (como LOC ou contagem de commits) não refletem resultados nem produtividade de valor [18, 28].
- **Natureza Mecânica do Deployment:** A etapa de implantação pós-submissão de código é um processo de fábrica executado por máquinas; a intervenção humana rotineira é considerada uma falha de automação (*toil*) [7, 29].
- **Escalabilidade Linear do Custo de Defeitos (DDR):** O custo de resolução de um defeito cresce linearmente com o tempo de existência do bug e o número de desenvolvedores expostos a ele [21]. O uso de autoformatação no IDE reduz a duração do defeito de horas/dias para segundos/minutos [22].
- **Quatro Dimensões de Impacto Organizacional:** Investimentos em plataforma e infraestrutura produzem impactos mensuráveis em *Product Success*, *Hardware Resource Efficiency*, *Engineering Capacity* e *Strategic Capabilities* [3, 11, 12, 40].
- **Diferença entre Custos Fixos e Perdas:** Custos de pessoal e infraestrutura são fixos em curtos prazos, enquanto defeitos em produção geram perdas imprevisíveis de receita e reputação [38, 39, 41].

---

## Desafios do Uso das Metricas

- **Uso de Linhas de Código e PRs como Proxies Individuais:** Tentar medir a produtividade individual através de contagem de linhas de código ou submissões de alterações é uma prática falha que indica apenas atividade e não entregas de valor [18].
- **Impossibilidade de Medir Contrafactuais:** Não é viável medir diretamente o impacto de ferramentas ou intervenções pontuais contra resultados que foram evitados (contrafactuais) no nível individual ou de pequenos grupos [42, 43].
- **Métrica Isolada de Redução de Outages:** Avaliar o impacto de ferramentas ou processos de software com base unicamente na redução do número total de *outages* raramente gera resultados estatisticamente significativos [15].
- **Tensão entre Fidelidade de Testes e Custo de Resolução:** Testes em produção oferecem maior fidelidade de sinal, porém apresentam maior risco de perdas financeiras; mover todos os testes para o início aumenta a latência e o consumo de hardware do desenvolvedor [35, 37].
- **Trocas Ineficientes entre Computação e Tempo do Desenvolvedor:** Gastar capacidade excessiva de engenharia para alcançar reduções insignificantes de custos de hardware diminui a satisfação da equipe sem gerar retorno positivo proporcional [26, 27, 44].

---

## Avaliacao de Qualidade Metodologica

| Criterio | Pontuacao (0-2) |
|----------|----------------|
| Objetivo claramente definido | 2 [1, 10] |
| Metodologia adequada ao objetivo | 1 [1, 2] |
| Amostra/contexto descrito adequadamente | 1 [1, 4-6] |
| Ameacas a validade discutidas | 1 [15, 37, 42] |
| Resultados com evidencia suficiente | 1 [3, 7, 15, 17] |
| Contribuicao clara para pratica ou teoria | 2 [1, 3, 12] |
| **TOTAL** | **8/12** [1, 3] |

---

## Limitacoes

- **Ausência de Validação Empírica Quantitativa Própria:** O artigo é conceitual e baseado na experiência dos autores e literatura existente, não apresentando um estudo empírico com coleta primária de dados quantitativos ou qualitativos formais no próprio texto [1, 2].
- **Foco Predominante no Contexto de Software Comercial em Larga Escala:** As premissas econômicas e operacionais do modelo (como custos fixos de infraestrutura e engenharia) aplicam-se precipuamente a médias e grandes empresas de software comercial e organizações SaaS [1, 41, 45].
- **Dificuldade Prática na Parametrização da Função de DDR:** A aplicação prática da função de estimativa do custo de detecção e resolução de defeitos requer a calibração de parâmetros complexos de latência e taxas de defeitos que podem variar entre equipes [19, 25, 46, 47].

---

## Contribuicao Principal

A principal contribuição do artigo é a proposição do modelo holístico *Develop, Deploy, Operate* (DDO), que estabelece uma ponte conceitual e econômica entre a prática da engenharia de software e a tomada de decisões de investimento corporativo [1, 3, 10]. Ao diferenciar formalmente o desenvolvimento como um processo criativo humano e a implantação como um processo de fábrica automatizado [28, 29], o trabalho fornece às organizações um modelo prático para avaliar o retorno de investimento (*ROI*) em infraestrutura e ferramentas através de quatro dimensões de impacto (*Product Success*, *Hardware Resource Efficiency*, *Engineering Capacity* e *Strategic Capabilities*) [11, 12], evitando armadilhas comuns associadas ao uso de métricas falhas de produtividade individual [18, 42].

---

*Extraido via NotebookLM em October 2026 para MLR: Software Developer Metrics in Practice*

📊 Gostaria de gerar um relatório detalhado em formato PDF ou criar uma apresentação de slides resumindo o modelo Develop, Deploy, Operate para a sua equipe?
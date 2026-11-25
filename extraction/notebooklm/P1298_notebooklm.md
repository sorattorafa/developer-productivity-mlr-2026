# P1298 — Software developer productivity loss due to technical debt—A replication and extension study examining developers’ development work
**Decisão: INCLUIDO | Qualidade: 5/5**
## Dados Bibliográficos
| Campo | Valor |
|-------|-------|
| **ID** | P1298 |
| **Autores** | Terese Besker, Antonio Martini, Jan Bosch |
| **Ano** | 2019 |
| **Venue** | The Journal of Systems and Software |
| **DOI** | https://doi.org/10.1016/j.jss.2019.06.004 |
| **Tipo** | Journal Article |
| **Método** | Estudo longitudinal (medições quantitativas repetidas) com entrevistas qualitativas de acompanhamento e um estudo de replicação |
| **Amostra** | Estudo original: 43 desenvolvedores de 6 empresas e 16 entrevistas (12 desenvolvedores, 4 gerentes). Estudo de replicação: 47 desenvolvedores de 1 empresa. |
| **Contexto** | Indústria de software com profissionais estabelecidos (sistemas embarcados, sistemas de tempo real, sistemas de análise de dados, etc.) |
| **Modo de trabalho** | Não especificado diretamente (focado no trabalho diário de desenvolvimento corporativo) |
| **Metodologia** | Triangulação metodológica mista (quantitativa e qualitativa) e replicação do estudo |

---

## Objetivo
Explorar as consequências da Dívida Técnica (Technical Debt - TD) em termos de desperdício de tempo de desenvolvimento, investigando em quais atividades esse tempo perdido é gasto e se diferentes tipos de TD impactam a quantidade de tempo desperdiçado de maneiras diferentes.

---

## Questões de Pesquisa
*   **RQ1:** De que maneiras a dívida técnica desperdiça o tempo de trabalho dos desenvolvedores? (Subdividida para investigar a quantidade de tempo perdido, diferenças baseadas em características do indivíduo e padrões de distribuição no tempo).
*   **RQ2:** Em quais atividades extras o tempo desperdiçado é gasto?.
*   **RQ3:** De que maneira os diferentes tipos de dívida técnica afetam a quantidade de tempo desperdiçado?.
*   **RQ4:** Com que frequência os desenvolvedores são forçados a introduzir novas dívidas técnicas devido a dívidas técnicas já existentes?.
*   **RQ5:** Existe diferença na conscientização sobre a dívida técnica entre desenvolvedores e seus gerentes?.
*   **RQ6:** Quais são os desafios no rastreamento dos juros da dívida técnica?.

---

## Métricas e Instrumentos de Avaliação

| Métrica | Categoria | Nível | Como Coletada | Validada |
|---------|-----------|-------|---------------|----------|
| **Wasted time (Tempo desperdiçado)** | Process | Individual | Autorrelatada via questionários online preenchidos duas vezes por semana durante sete semanas, indicando a porcentagem de tempo de desenvolvimento desperdiçado lidando com TD. | Sim (Corroborada pelo estudo de replicação). |

---

## Frameworks e Métricas
### Frameworks Referenciados
*   Goal-Question-Metric (GQM).
### Frameworks Propostos
*   Nenhum framework novo foi proposto.

---

## Fatores que Influenciam Produtividade
### Fatores Positivos
| Fator | Categoria |
|-------|-----------|
| Conscientização e rastreamento do tempo perdido (facilita o planejamento de capacidade e a comunicação com gerentes) | Process |
| Refatoração contínua para manter a dívida técnica controlada | Technical |

### Fatores Negativos
| Fator | Categoria |
|-------|-----------|
| Presença de Dívida Técnica (TD) no software | Technical |
| Tempo excessivo gasto em testes adicionais, análise extra de código e refatorações não planejadas causadas por TD | Process |
| "Dívida Contagiosa" (introdução forçada de nova TD devido à restrição de tempo gerada pela TD existente) | Process/Technical |

---

## Papel da IA e Automação

| Campo | Valor |
|-------|-------|
| Usa IA/ML? | Não — Os dados foram puramente baseados nas percepções e métricas relatadas por humanos sobre o processo de software. |
| Automação de coleta? | Não — As coletas foram realizadas através de questionários online preenchidos manualmente pelos participantes (SurveyMonkey) e transcrição de entrevistas. |
| Impacto de IA na produtividade? | Não aplicável aos resultados deste artigo. |

---

## Resultados Principais
*   **Desperdício de tempo:** Os desenvolvedores relataram que perdem, em média, **23,1% do seu tempo geral de desenvolvimento** devido a problemas relacionados à dívida técnica.
*   **Atividades mais impactadas:** As atividades onde o tempo é mais comumente desperdiçado são **testes adicionais**, seguido por **análise adicional de código-fonte** e **refatoração adicional**.
*   **Dívida Contagiosa:** Em 24% das ocorrências em que encontraram TD, os desenvolvedores relataram que foram **forçados a introduzir novas dívidas técnicas** devido à pressão de tempo e gargalos provocados pela TD original.
*   **Tipos de TD mais custosos:** Questões relacionadas a Testes e a Código-Fonte são os tipos de TD com a mais forte associação ao tempo desperdiçado e também são as causas mais comuns que forçam a introdução de nova dívida técnica.
*   **Discrepância de Conscientização:** Desenvolvedores possuem alta consciência de que perdem quase um quarto de seu tempo para a TD, mas a alta gestão possui um nível de conscientização consideravelmente mais baixo sobre o tamanho desse gargalo produtivo.

---

## Desafios do Uso das Métricas
Embora desenvolvedores e gerentes reconheçam os benefícios de se quantificar o impacto da TD na produtividade, há uma forte **relutância na adoção de um rastreamento contínuo**. Os profissionais alegam que reportar o desperdício de tempo exigiria muito esforço extra, enquanto os gerentes evitam introduzir métricas pelo medo de engatilhar uma "espiral negativa" e aumento do estresse na equipe.

---

## Avaliação de Qualidade Metodológica

| Critério | Pontuação (0-2) |
|----------|----------------|
| Objetivo claramente definido | 2 |
| Metodologia adequada ao objetivo | 2 |
| Amostra/contexto descrito adequadamente | 2 |
| Ameaças à validade discutidas | 2 |
| Resultados com evidência suficiente | 2 |
| Contribuição clara para prática ou teoria | 2 |
| **TOTAL** | **12/12** |

---

## Limitações
*   **Viés de seleção:** A escolha dos desenvolvedores participantes concentrou-se apenas nas empresas de uma rede específica de contatos, o que pode restringir a diversidade da amostra original.
*   **Viés de autodeclaração:** Os resultados são baseados em métricas autorrelatadas pelos participantes através dos surveys, o que depende da capacidade de cada desenvolvedor de quantificar corretamente o tempo desperdiçado e o exato tipo de TD, sem o uso de ferramentas automatizadas para verificação.
*   **Restrição de papéis:** Os resultados limitam-se ao ponto de vista de desenvolvedores seniores e gestores diretos, e podem não se generalizar a outras atuações no ciclo de desenvolvimento de software.

---

## Contribuição Principal
Este artigo contribui com quantificações empíricas severas ao provar que **a Dívida Técnica causa a perda direta de quase um quarto (23%) do tempo total de desenvolvedores**. Revela que a maior parte desse tempo é ineficientemente drenada por atividades de testes extras e análise de código obsoleto. Adicionalmente, o estudo apresenta provas empíricas diretas sobre a **natureza contagiosa da Dívida Técnica**, demonstrando como dívidas antigas pressionam a capacidade do desenvolvedor, coagindo-o de forma forçada à geração de mais Dívida Técnica em cerca de 24% dos casos.
# P1524 — An Empirical Analysis of the Effect of Agile Teams on Software Productivity

**Decisao: INCLUIDO | Qualidade: 4.5/5**

---

## Dados Bibliograficos

| Campo | Valor |
|-------|-------|
| **ID** | P1524 |
| **Autores** | Javed Iqbal, Mazni Omar, Azman Yasin [1] |
| **Ano** | 2019 [1] |
| **Venue** | 2nd International Conference on Computing, Mathematics and Engineering Technologies (iCoMET 2019) [1] |
| **DOI** | Not available in sources [1-39] |
| **Tipo** | Conference paper [1] |
| **Metodo** | Mixed methods (Literature review and Quantitative Survey) [1, 9] |
| **Amostra** | 52 agile software development professionals [1, 3, 9] |
| **Contexto** | Industry (52 companies in Pakistan) [1, 3, 9] |
| **Modo de trabalho** | Not specified [1-39] |
| **Metodologia** | Agile (Scrum, Extreme Programming (XP), Kanban) [3, 18] |

---

## Objetivo

O objetivo deste trabalho é identificar fatores críticos que afetam as equipes ágeis e especificar como esses fatores impactam a produtividade do software, buscando fornecer evidências empíricas para preencher a lacuna na literatura sobre a dinâmica do trabalho em equipe ágil [1, 3, 9].

---

## Questoes de Pesquisa

RQ1: How do the agile team factors impact on software productivity and how these relate with each other (either positively or negatively)? [9]

---

## Metricas e Instrumentos de Avaliacao

| Metrica | Categoria | Nivel | Como Coletada | Validada |
|---------|-----------|-------|---------------|----------|
| Software Productivity | Productivity | Team | Self-perceived (Likert Scale 1-5) via online survey [9, 19] | Yes (Cronbach’s alpha = 0.75) [14] |
| Team Velocity | Activity | Team | Measured by the number of user stories included in each iteration [8, 11] | No (Not explicitly stated) |
| Quality Conformance (Defects) | Quality | Team | Number of defects found in testing [8] | No (Referenced from literature) |
| Function Point (FP) | Delivery | Team | Function per person effort [8] | No (Referenced from literature) |
| Team Empowerment | Collaboration | Team | Likert Scale survey questions regarding decision-making [10, 22] | Yes (Correlation analysis) [21] |
| Inter-team coordination | Collaboration | Team | Survey on responsibilities for goal achievement [10, 22] | Yes (Correlation analysis) [21] |
| Quality Conformance (Testing) | Quality | Team | Survey on frequency of test cases and integration testing [12, 23] | Yes (Correlation analysis) [21] |

---

## Frameworks e Metricas

### Frameworks Referenciados
- **Input-Process-Output (IPO)**: APPLIED (Used to study agile team productivity using team perception) [5].
- **Salas model (Team effectiveness)**: REFERENCED (Includes factors like leadership and mutual performance monitoring) [5, 24].
- **Dickinson model (Teamwork measurement)**: REFERENCED (Includes leadership, communication, and coordination) [6, 24].
- **Hoegl model (Teamwork quality)**: REFERENCED (Includes balance of member contributions and mutual support) [6, 24].
- **Agile Manifesto**: REFERENCED (Used to define criteria for software productivity) [3].

### Frameworks Propostos
O artigo não propõe um novo framework, mas categoriza 23 sub-fatores de equipes ágeis em sete categorias principais para análise de correlação [9-13].

---

## Fatores que Influenciam Produtividade

### Fatores Positivos
| Fator | Categoria |
|-------|-----------|
| Team Empowerment | Human/Organizational [7, 21, 25] |
| Inter-team coordination | Process/Organizational [7, 21, 25] |
| Requirements as User Stories | Process [8, 21, 25] |
| Requirements workshop involvement | Process/Human [11, 21, 25] |
| Features clear and ready for development | Technical/Process [16, 21, 25] |
| Test cases written up-front | Technical/Process [17, 21, 25] |
| Integration Testing throughout the lifecycle | Technical/Process [17, 21, 25] |
| Team Effectiveness (cooperation, decision making) | Human/Process [3, 21, 25] |

### Fatores Negativos
| Fator | Categoria |
|-------|-----------|
| Leader chairing meeting (Negative correlation -0.14) | Process/Human [21, 22, 25] |
| Automated unit testing (Negative correlation -0.15) | Technical [21, 23, 25] |
| Automated build and regression testing (Negative correlation -0.12) | Technical [21, 23, 25] |

---

## Papel da IA e Automacao

| Campo | Valor |
|-------|-------|
| Usa IA/ML? | No — The paper identifies factors but does not use or specifically focus on IA/ML technology [1-26]. |
| Automacao de coleta? | No — Data was collected through an online survey (Google Forms) and literature review [9, 38]. |
| Impacto de IA na produtividade? | Not addressed [1-39]. |

---

## Resultados Principais

- A produtividade do software está positivamente correlacionada com a maioria dos fatores identificados de equipes ágeis [1, 21].
- Os fatores com correlação positiva mais significativa (p < 0.05) incluem: **Requirements workshop involvement (r=0.42)**, **Team effectiveness (r=0.39)**, **Requirements as User Stories (r=0.38)** e **Features clarity (r=0.35)** [21, 23].
- **80.77%** dos profissionais (soma de "Agree" e "Strongly Agree") percebem que as equipes ágeis aumentam a produtividade [19].
- A metodologia **Kanban** apresentou a maior média de produtividade percebida (4.15) em comparação com Scrum (4.11) e XP (3.9) [18].
- Contrariamente ao esperado, atividades de **Automated unit testing** e **Automated builds** mostraram correlações negativas fracas com a produtividade na amostra estudada (-0.15 e -0.12, respectivamente) [21, 23].

---

## Desafios do Uso das Metricas

- **Requisitos Incertos**: O gerenciamento de requisitos mal definidos é um desafio crítico, sendo citado que 55% dos projetos falham por esse motivo [8, 21].
- **Falta de evidência empírica**: A literatura carece de dados quantitativos sobre como os fatores de equipe afetam especificamente a produtividade em contextos ágeis [1, 3].
- **Interpretação de correlações baixas**: Valores de correlação baixos podem ser erroneamente interpretados como inexistentes, quando ainda podem ter implicações significativas na prática [21].

---

## Avaliacao de Qualidade Metodologica

| Criterio | Pontuacao (0-2) |
|----------|----------------|
| Objetivo claramente definido | 2 [1, 3] |
| Metodologia adequada ao objetivo | 2 [9] |
| Amostra/contexto descrito adequadamente | 2 [1, 9] |
| Ameacas a validade discutidas | 1 [21, 26] |
| Resultados com evidencia suficiente | 2 [21-23] |
| Contribuicao clara para pratica ou teoria | 2 [1, 25] |
| **TOTAL** | **11/12** |

---

## Limitacoes

- A necessidade de maior precisão estatística em testes futuros para examinar a produtividade com maior profundidade [26].
- O estudo foca apenas no contexto de empresas de software no Paquistão, o que pode limitar a generalização para outras culturas ou regiões [1, 9].
- Dependência de percepções autorrelatadas (survey) em vez de métricas objetivas de repositórios [9, 13].

---

## Contribuicao Principal

A principal contribuição do artigo é a identificação e validação estatística de fatores críticos de equipes ágeis — como empoderamento, coordenação e clareza de requisitos — que correlacionam positivamente com a produtividade do software. O estudo fornece uma base quantitativa para que profissionais de software entendam quais dinâmicas de equipe são mais vitais para o sucesso de projetos ágeis, destacando que fatores humanos e de processo podem ser mais impactantes que a automação técnica isolada [1, 21, 25, 26].

---

*Extraido via NotebookLM em March 2026 para MLR: Software Developer Metrics in Practice*
# P0485 — Technical debt cripples software developer productivity: a longitudinal study on developers' daily software development work

**Decisao: INCLUIDO | Qualidade: 5/5**

---

## Dados Bibliograficos

| Campo | Valor |
|-------|-------|
| **ID** | P0485 |
| **Autores** | Terese Besker, Antonio Martini, Jan Bosch [1] |
| **Ano** | 2018 [1] |
| **Venue** | TechDebt '18: Proceedings of the 2018 International Conference on Technical Debt [2] |
| **DOI** | https://doi.org/10.1145/3194164.3194178 [1] |
| **Tipo** | Conference paper [2] |
| **Metodo** | Mixed methods (Longitudinal study with surveys and semi-structured interviews) [3, 4] |
| **Amostra** | 43 software developers for the longitudinal phase and 16 practitioners (12 developers, 4 managers) for interviews [3, 5] |
| **Contexto** | Industry — seven software companies in Sweden and Norway involved in contextual analysis, with six participating in the full study [5, 6] |
| **Modo de trabalho** | Not specified [6] |
| **Metodologia** | Not specified (participants came from diverse companies with university-level education and varied experience) [6, 7] |

---

## Objetivo

O objetivo principal deste estudo é explorar as consequências negativas da **Technical Debt (TD)** em termos de tempo desperdiçado no desenvolvimento de software [3]. O trabalho investiga em quais atividades adicionais esse tempo é gasto, se diferentes tipos de TD impactam o desperdício de forma distinta, e examina os benefícios de rastrear e comunicar a quantidade de tempo desperdiçado sob a perspectiva de desenvolvedores e gestores [3, 8].

---

## Questoes de Pesquisa

*   **RQ1:** How much of software developers’ overall development time is wasted due to Technical Debt? [8]
*   **RQ1.1:** Is it possible to distinguish any patterns from the distribution of the wasted time over a calendar period? [8]
*   **RQ2:** On which extra activities are the wasted time spent? [8]
*   **RQ3:** In what ways do different Technical Debt types affect the amount of wasted time? [8]
*   **RQ4:** How often are developers forced to introduce new Technical Debt due to already existing Technical Debt? [8]
*   **RQ5:** How aware are the developers and their managers about the wasted time due to Technical Debt? Do developers and managers consider the insight into the wasted time useful? [9]

---

## Metricas e Instrumentos de Avaliacao

| Metrica | Categoria | Nivel | Como Coletada | Validada |
|---------|-----------|-------|---------------|----------|
| **Wasted development time** | Productivity | Individual | Reported as a percentage (0-100%) via longitudinal surveys twice a week for 7 weeks [5, 10] | Yes (Triangulated with interviews) [4] |
| **Extra activities frequency** | Activity | Individual | Multi-selection list of 6 activities (Testing, Code Analysis, Refactoring, etc.) in surveys [10] | Partial (Based on previous research) [10] |
| **Negative impact of TD types** | Quality | Individual | 5-point Likert Scale (Not at All to To a Great Extent) for different TD categories [10] | Yes (Statistical significance tested) [11, 12] |
| **Forced new TD introduction** | Quality | Individual | Likert scale reporting how often existing TD forced new debt [13] | Yes (Qualitative confirmation) [14] |

---

## Frameworks e Metricas

### Frameworks Referenciados
*   **Technical Debt Metaphor (Ward Cunningham):** REFERENCED (Used as the foundational concept for the study) [15].
*   **Contagious Debt:** REFERENCED (Used to discuss the non-linear growth of interest when one TD causes another) [16, 17].

### Frameworks Propostos
O artigo não propõe um framework formal, mas utiliza um modelo estatístico de **Mixed Effects Models** para analisar a variabilidade inter-individual e intra-individual do tempo desperdiçado [11, 18].

---

## Fatores que Influenciam Produtividade

### Fatores Positivos
| Fator | Categoria |
|-------|-----------|
| **Tracking and communicating wasted time** | Organizational |
| **Awareness of TD consequences** | Human |

### Fatores Negativos
| Fator | Categoria |
|-------|-----------|
| **Technical Debt (General)** | Technical |
| **Time Pressure** | Organizational |
| **Contagious Debt (Forced new TD)** | Technical |
| **Lack of aligned strategy for TD** | Process |

---

## Papel da IA e Automacao

| Campo | Valor |
|-------|-------|
| Usa IA/ML? | No — The study uses statistical modeling (linear mixed models) in R and SPSS [11]. |
| Automacao de coleta? | No — Data was collected manually through surveys hosted on Survey Monkey [5, 6]. |
| Impacto de IA na produtividade? | Not addressed in this study. |

---

## Resultados Principais

*   Desenvolvedores desperdiçam, em média, **23,1% de seu tempo de trabalho** devido à Technical Debt [3, 19].
*   As atividades extras mais comuns onde o tempo é desperdiçado são **Additional testing**, seguido por **Additional source code analysis** e **Additional refactoring** [3, 20].
*   Em **24% das ocasiões**, os desenvolvedores são forçados a introduzir novos TD devido a dívidas já existentes (contagious debt) [3, 14].
*   Dívidas relacionadas a **Source Code** têm a associação mais forte com o tempo desperdiçado [21].
*   Gestores possuem uma **consciência significativamente menor** sobre o desperdício de tempo comparado aos desenvolvedores, muitas vezes considerando o nível de desperdício reportado como "inaceitável" enquanto desenvolvedores o veem como natural [22, 23].

---

## Desafios do Uso das Metricas

*   **Subjetividade do Self-reporting:** Desenvolvedores podem ter conhecimento insuficiente para categorizar tipos específicos de TD ou quantificar o desperdício com precisão total [24].
*   **Falta de Medição Formal:** Nenhuma das empresas estudadas rastreava ou media formalmente o tempo desperdiçado por TD antes do estudo [25].
*   **Divergência de Percepção:** Gestores e desenvolvedores discordam sobre o que constitui uma quantidade "razoável" de tempo gasto em manutenção [23].

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

*   **Viés Geográfico:** Os resultados podem ser diferentes em outras áreas geográficas ou culturas de desenvolvimento [24].
*   **Natureza do Self-report:** Dependência da percepção individual dos desenvolvedores para quantificar variáveis técnicas [24].
*   **Generalização Limitada:** Os achados focam especificamente em desenvolvedores e gestores, não podendo ser generalizados para outros papéis sem estudos adicionais [24].

---

## Contribuicao Principal

Este estudo fornece a primeira evidência empírica longitudinal de que a **Technical Debt** consome quase um quarto do tempo produtivo dos desenvolvedores [3, 26]. A pesquisa destaca o fenômeno da **"dívida contagiosa"**, onde o TD existente força a criação de novos atalhos técnicos, e demonstra uma lacuna crítica de comunicação entre desenvolvedores e gestores quanto ao impacto real da dívida técnica na eficiência operacional [14, 23, 26].

---

*Extraido via NotebookLM em March 2026 para MLR: Software Developer Metrics in Practice*
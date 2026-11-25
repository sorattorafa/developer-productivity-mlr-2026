# P1503 — How Was Your Weekend? Software Development Teams Working From Home During COVID-19

**Decisao: INCLUIDO | Qualidade: 5/5**

---

## Dados Bibliograficos

| Campo | Valor |
|-------|-------|
| **ID** | P1503 |
| **Autores** | Courtney Miller, Paige Rodeghero, Margaret-Anne Storey, Denae Ford, Thomas Zimmermann |
| **Ano** | 2021 |
| **Venue** | 2021 IEEE/ACM 43rd International Conference on Software Engineering (ICSE) |
| **DOI** | 10.1109/ICSE43902.2021.00064 |
| **Tipo** | Conference paper |
| **Metodo** | Mixed methods (Qualitative content analysis and Quantitative regression analysis) |
| **Amostra** | Survey 1: 2,265 responses; Survey 2: 608 responses |
| **Contexto** | Industry — Large software company in the United States |
| **Modo de trabalho** | Remote (Working From Home during COVID-19) |
| **Metodologia** | Not specified (Variety of development techniques) |

---

## Objetivo

O objetivo principal do artigo é investigar como a cultura de equipe e a produtividade das equipes de desenvolvimento de software foram afetadas pela mudança em massa para o trabalho remoto durante a pandemia de COVID-19 [1, 2]. O estudo busca identificar fatores culturais (como comunicação, camaradagem e coesão) que influenciam a produtividade da equipe nesse cenário de crise para informar gestores sobre como apoiar o desempenho sustentado [2, 3].

---

## Questoes de Pesquisa

*   **RQ1:** How has the ability for teams to meet milestones changed during WFH? [4]
*   **RQ2:** How has team culture changed during WFH? [4]
*   **RQ3:** How have teams supported their members during WFH? [4]
*   **RQ4:** How has team communication and collaboration changed during WFH? [4]
*   **RQ5:** How have social interactions within teams changed during WFH? [4]
*   **RQ6:** Which factors are associated with a change in team productivity during WFH? [4]

---

## Metricas e Instrumentos de Avaliacao

| Metrica | Categoria | Nivel | Como Coletada | Validada |
|---------|-----------|-------|---------------|----------|
| Perceived change in team productivity | Productivity | Team | 5-point Likert scale (Survey) | No [5, 6] |
| Ability to reach milestones | Productivity | Team | Binary question (Yes/No) + Open-ended explanation | No [7, 8] |
| Communication ease with colleagues | Collaboration | Team | 5-point Likert scale (Survey) | Partial (derived from literature) [9, 10] |
| Social connection with team members | Satisfaction | Team | 5-point Likert scale (Survey) | Partial (derived from literature) [9, 11] |
| Frequency of scheduled social activities | Activity | Team | 5-point frequency scale (Survey) | No [11] |
| Awareness of colleague's work | Collaboration | Team | Likert scale (Survey) | No [10, 12] |

---

## Frameworks e Metricas

### Frameworks Referenciados
*   **Automated Trace Data** (Bao et al.) — REFERENCED (Discussed as an alternative measurement approach) [13, 14].
*   **Qualitative Content Analysis** (Card Sorting) — APPLIED (Used for analyzing open-ended survey responses) [15].
*   **Akaike Information Criterion (AIC)** — APPLIED (Used for variable selection in the regression model) [16, 17].

### Frameworks Propostos
O artigo não propõe um novo framework formal com nome próprio, mas constrói e valida um **Team Productivity Model** baseado em regressão linear para identificar fatores de cultura de equipe associados à produtividade percebida [18, 19].

---

## Fatores que Influenciam Produtividade

### Fatores Positivos
| Fator | Categoria |
|-------|-----------|
| Ability to Brainstorm with Team Members | Technical/Process [20, 21] |
| Impactful Contributions I Make to Team | Human/Psychological [22, 23] |
| Ability to Make Decisions as Team | Process/Organizational [22, 23] |
| External Team Bonding Activities | Organizational/Social [24, 25] |
| Team Members are Supportive of New Ideas | Human/Cultural [24, 25] |

### Fatores Negativos
| Fator | Categoria |
|-------|-----------|
| Less Awareness of What Colleagues are Working On | Process/Technical [20, 24] |
| Difficulty Communicating with Colleagues | Process/Technical [20, 23] |
| Meeting Fatigue/Increased Meeting Volume | Process/Human [26, 27] |
| Loss of Ad-hoc In-person Communication | Human/Social [28, 29] |

---

## Papel da IA e Automacao

| Campo | Valor |
|-------|-------|
| Usa IA/ML? | No — O estudo utiliza métodos estatísticos tradicionais (regressão linear) [18]. |
| Automacao de coleta? | No — Os dados foram coletados manualmente via questionários (Qualtrics e Microsoft Forms Pro) [7, 30]. |
| Impacto de IA na produtividade? | Not applicable — O foco é na colaboração humana e cultura de equipe. |

---

## Resultados Principais

*   **74%** dos desenvolvedores relataram sentir falta das interações sociais com colegas [2].
*   **65%** relataram uma diminuição no sentimento de conexão social com a equipe [31, 32].
*   **51%** sentiram uma queda na facilidade de comunicação com os colegas [2, 32].
*   **57%** perceberam uma diminuição na capacidade de realizar brainstorming com a equipe [32, 33].
*   **58%** relataram estar menos cientes do que os colegas estão trabalhando [12].
*   Apenas **23%** dos participantes relataram uma diminuição real na produtividade da equipe, enquanto a maioria (**56%**) não percebeu mudança significativa [34-36].
*   O modelo de regressão identificou que a **consciência do trabalho alheio**, a **capacidade de brainstorming** e a **facilidade de comunicação** são os preditores mais fortes da produtividade da equipe [20, 37].

---

## Desafios do Uso das Metricas

*   **Subjetividade:** Dependência de métricas de percepção individual em vez de dados objetivos [6, 38].
*   **Dificuldade de triangulação:** Por ser uma pesquisa anônima, não foi possível cruzar dados de membros da mesma equipe [38].
*   **Falta de causalidade:** O estudo identifica correlações estatísticas, mas não pode afirmar relações de causa e efeito entre os fatores culturais e a produtividade [39].

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

*   **Generalização:** O estudo foi realizado em apenas uma grande empresa de software (Microsoft) nos EUA, o que limita a aplicação dos resultados a empresas menores ou de outras regiões [40].
*   **Viés de Voluntariado:** Pessoas que escolhem participar de pesquisas podem ter traços de personalidade diferentes da população total [41].
*   **Período Específico:** Os dados refletem o WFH durante uma pandemia global, o que pode diferir do trabalho remoto em tempos normais [6].
*   **Auto-relato:** A produtividade foi medida exclusivamente através da percepção dos desenvolvedores [6].

---

## Contribuicao Principal

A principal contribuição deste trabalho é a demonstração empírica de que a **conexão social e a facilidade de comunicação** são fundamentais para a produtividade de equipes de software remotas [2, 42]. O estudo eleva a discussão da produtividade para além de métricas técnicas individuais, focando em fatores de cultura de equipe, como a capacidade de brainstorming e o apoio mútuo, fornecendo recomendações práticas para gestores manterem a coesão da equipe em ambientes distribuídos [3, 43, 44].

---

*Extraido via NotebookLM em March 2026 para MLR: Software Developer Metrics in Practice*
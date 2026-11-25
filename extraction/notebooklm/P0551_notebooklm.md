# P0551 — A Survey-Based Qualitative Study to Characterize Expectations of Software Developers from Five Stakeholders

**Decisao: INCLUIDO | Qualidade: 5/5**

---

## Dados Bibliograficos

| Campo | Valor |
|-------|-------|
| **ID** | P0551 |
| **Autores** | Khalid Hasan, Partho Chakraborty, Rifat Shahriyar, Anindya Iqbal, Gias Uddin |
| **Ano** | 2021 |
| **Venue** | ACM / IEEE International Symposium on Empirical Software Engineering and Measurement (ESEM) |
| **DOI** | 10.1145/3475716.3475787 |
| **Tipo** | Conference paper |
| **Metodo** | Qualitative study (Survey, Semi-formal interviews, Open coding, Card sorting) |
| **Amostra** | 181 professional software developers |
| **Contexto** | Industry (primarily small and medium-sized organizations) |
| **Modo de trabalho** | Not specified (conducted during COVID-19 pandemic) |
| **Metodologia** | Not specified |

---

## Objetivo

O objetivo principal do artigo é compreender e caracterizar as expectativas de desenvolvedores de software profissionais em relação a cinco diferentes stakeholders (organizações, gestores, pares, novas contratações, e governo/instituições educacionais) para entender como essas percepções afetam a produtividade e o bem-estar no trabalho [1-3].

---

## Questoes de Pesquisa

*   **RQ1:** What do professional software developers in our survey expect from their organizations? [4]
*   **RQ2:** What do professional software developers in our survey expect from managers? [5]
*   **RQ3:** What professional software developers in our survey expect from peers in the team? [5]
*   **RQ4:** What professional software developers in our survey expect from the new hires? [5]
*   **RQ5:** What do the developers in our survey expect from government and universities? [6]

---

## Metricas e Instrumentos de Avaliacao

O estudo é qualitativo e foca em categorizar respostas abertas. No entanto, cita as seguintes métricas e instrumentos no contexto de trabalhos relacionados:

| Metrica | Categoria | Nivel | Como Coletada | Validada |
|---------|-----------|-------|---------------|----------|
| Project size/Requirements | Productivity | Organization | Document analysis (Albrecht framework) | Yes [7] |
| Velocity, Quality, Satisfaction | Productivity | Team/Individual | Multidimensional framework (Sadowski et al.) | Yes [8] |
| Self-appraisal vs. Manager's appraisal | Productivity | Individual | Comparative survey | Yes [9] |
| Frequency of expectation types | Satisfaction | Group | Survey data analysis (Open coding) | Yes [10, 11] |
| Inter-coder agreement (Kappa, Pi, Alpha) | Quality | Study level | Statistical calculation | Yes [12, 13] |

---

## Frameworks e Metricas

### Frameworks Referenciados
*   **Software development productivity framework (Velocity, Quality, Satisfaction):** REFERENCED (citado para discutir dimensões da produtividade) [8].
*   **WorkAnalytics:** REFERENCED (citado no contexto de auto-monitoramento) [14].
*   **Cognitive support framework based on bots:** REFERENCED (citado como suporte para desenvolvedores) [15].

### Frameworks Propostos
O artigo propõe um **catálogo e hierarquia de 18 tipos de expectativas** organizados em seis temas: Well-being, Leadership, Practice, Productivity, Career growth, e Education [16-18].

---

## Fatores que Influenciam Produtividade

### Fatores Positivos
| Fator | Categoria |
|-------|-----------|
| Thriving and supportive workplace culture | Organizational [19] |
| Supportive attitude and clear communication from peers | Human [20] |
| Tech savvy managers | Organizational/Technical [21] |
| Adoption of standard Software Engineering (SE) practices | Process [20, 22] |
| Industry-oriented teaching in universities | Organizational/Human [23] |
| Pair programming | Process [24] |

### Fatores Negativos
| Fator | Categoria |
|-------|-----------|
| Interruptions and context switches | Process/Human [25, 26] |
| Lack of support to manage expectations and happiness | Human/Organizational [27] |
| Corporate politics | Organizational [10, 28] |
| Stressful moments (e.g., COVID-19 pandemic) | Human [15, 25] |
| Sloppy management due to poor quantification of productivity | Process [29] |

---

## Papel da IA e Automacao

| Campo | Valor |
|-------|-------|
| Usa IA/ML? | No — o estudo menciona sentiment analysis em trabalhos relacionados para analisar artefatos de SE, mas não a utiliza diretamente [30]. |
| Automacao de coleta? | No — os dados foram coletados via surveys manuais e entrevistas semi-formais [1, 31]. |
| Impacto de IA na produtividade? | O artigo referencia o uso de bots para suporte cognitivo como uma forma de reduzir interrupções e melhorar a produtividade [15]. |

---

## Resultados Principais

*   Identificação de **18 tipos de expectativas multi-facetadas** agrupadas em seis temas principais [16, 22].
*   A expectativa mais citada em relação às organizações é uma **cultura de trabalho saudável** (48.8%), superando benefícios financeiros [28, 32].
*   Em relação aos gestores, desenvolvedores priorizam **People skill** (48.6%) e gestão adequada (43.8%) [11].
*   Dos pares (peers), espera-se atitude de suporte (55.3%) e conhecimento em **standard SE practices** (54.1%) [11].
*   Para novas contratações, a principal expectativa é a **motivação para aprender** (52.9%) [11].
*   Universidades são cobradas por um ensino orientado à indústria (77.1%) e o governo por políticas e facilidades para o setor (63.1%) [33].
*   Expectativas relacionadas ao trabalho (486 citações) superam as relacionadas à carreira (239 citações), sugerindo que dinheiro ou promoções não garantem felicidade por si sós [28].

---

## Desafios do Uso das Metricas

*   **Interrupções:** Dificultam a medição precisa da produtividade, pois desenvolvedores realizam tarefas mesmo sob interrupção [26].
*   **Contexto da COVID-19:** Recomendação de não confiar em medidas tradicionais de produtividade durante crises [9].
*   **Incentivos Distorcidos:** A quantificação da produtividade pode distorcer incentivos se não for bem medida, influenciando uma gestão negligente [9].
*   **Subjetividade:** Diferenças significativas entre a auto-avaliação do funcionário e a avaliação do gestor [9].

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

*   **Viés do pesquisador:** A codificação aberta pode introduzir interpretações subjetivas [34].
*   **Viés de seleção:** Uso de conexões pessoais e *snowball sampling* pode limitar a representatividade [35].
*   **Generalização:** Os resultados podem ser mais aplicáveis a empresas de pequeno e médio porte [13].
*   **Taxa de resposta:** Devido ao método de amostragem, não foi possível calcular a taxa de resposta exata [36].

---

## Contribuicao Principal

A principal contribuição é o desenvolvimento de uma **hierarquia abrangente de expectativas de desenvolvedores**, revelando que a produtividade e o bem-estar são problemas socio-técnicos que dependem fortemente de uma gestão de expectativas eficaz entre diversos atores sociais, indo além de métricas técnicas puras [2, 37, 38].

---

*Extraido via NotebookLM em March 2026 para MLR: Software Developer Metrics in Practice*
# P0534 — On the Unhappiness of Software Developers

**Decisao: INCLUIDO | Qualidade: 5/5**

---

## Dados Bibliograficos

| Campo | Valor |
|-------|-------|
| **ID** | P0534 |
| **Autores** | Daniel Graziotin, Fabian Fagerholm, Xiaofeng Wang, Pekka Abrahamsson |
| **Ano** | 2017 |
| **Venue** | Evaluation and Assessment in Software Engineering (EASE '17) |
| **DOI** | http://dx.doi.org/10.1145/3084226.3084242 |
| **Tipo** | Conference paper |
| **Metodo** | Mixed methods (Quantitative and Qualitative Survey) |
| **Amostra** | 2,220 developers (initial), 1,318 complete and valid responses |
| **Contexto** | Mixed: GitHub community members, including professionals (75%), students (15%), and hobbyists from 88 countries |
| **Modo de trabalho** | Not specified (includes freelancers, employees, and startup founders) |
| **Metodologia** | Not specified (diverse sample across various development environments) |

---

## Objetivo

O principal objetivo do artigo é ampliar a compreensão sobre a infelicidade entre desenvolvedores de software, estabelecendo uma estimativa de base (baseline) para a distribuição da (in)felicidade na população e identificando as causas que levam os desenvolvedores a se sentirem infelizes durante o desenvolvimento de software [1, 2].

---

## Questoes de Pesquisa

*   **RQ1:** What is the distribution of (un)happiness among software developers? [2]
*   **RQ2:** What are the experienced causes for unhappiness among software developers while developing software? [3]

---

## Metricas e Instrumentos de Avaliacao

| Metrica | Categoria | Nivel | Como Coletada | Validada |
|---------|-----------|-------|---------------|----------|
| SPANE-P (Positive Experience) | Satisfaction / Affect | Individual | Survey (12-item scale) | Yes [4, 5] |
| SPANE-N (Negative Experience) | Satisfaction / Affect | Individual | Survey (12-item scale) | Yes [4, 5] |
| SPANE-B (Affect Balance) | Satisfaction / Affect | Individual | Subtraction (SPANE-P - SPANE-N) | Yes [5] |

---

## Frameworks e Metricas

### Frameworks Referenciados
*   **Happy-productive worker thesis:** REFERENCED (Discutido como fundamentação teórica) [1, 6].
*   **Behavioral Software Engineering:** REFERENCED (Citado como o campo de pesquisa emergente) [7].
*   **Scale of Positive and Negative Experience (SPANE):** APPLIED (Utilizado como o principal instrumento de medição) [4, 8].
*   **Positive and Negative Affect Schedule (PANAS):** REFERENCED (Discutido em termos de limitações superadas pelo SPANE) [4].

### Frameworks Propostos
O artigo não propõe um novo framework de métricas, mas desenvolve uma **taxonomia de causas de infelicidade** dividida em categorias internas (Developer’s own being) e externas (People, Artifact, Process) [9, 10].

---

## Fatores que Influenciam Produtividade

### Fatores Positivos
| Fator | Categoria |
|-------|-----------|
| Positive affective states | Human |
| Happiness (associated with shorter fixing time) | Human |

### Fatores Negativos
| Fator | Categoria |
|-------|-----------|
| Being stuck in problem solving | Human (Internal) |
| Time pressure (unrealistic deadlines) | Process |
| Bad code quality and coding practice | Technical (Artifact) |
| Under-performing colleague | Human (People) |
| Feel inadequate with work (lack of skills) | Human (Internal) |
| Mundane or repetitive tasks | Process |
| Unexplained broken code | Technical (Artifact) |
| Bad decision making (technical or business) | Process |
| Imposed limitation on development (tools/languages) | Technical (Artifact) |
| Personal issues (non-work related) | Human (Internal) |

---

## Papel da IA e Automacao

| Campo | Valor |
|-------|-------|
| Usa IA/ML? | No — a análise qualitativa foi feita via manual coding (NVIVO) [11]. |
| Automacao de coleta? | Partial — o GitHub Archive foi usado para extrair e-mails, mas a coleta de dados foi via survey manual [12, 13]. |
| Impacto de IA na produtividade? | Not applicable — não abordado no estudo. |

---

## Resultados Principais

*   Desenvolvedores de software são uma população **levemente feliz**, com uma média de Affect Balance (SPANE-B) de **9.05** (em uma escala de -24 a +24) [1, 14].
*   A distribuição da felicidade não é normal, apresentando um desvio (skew) para a esquerda [15].
*   Foram identificados **219 fatores** que causam infelicidade [1, 16].
*   **Causas externas** são muito mais frequentes (1.843 ocorrências) do que causas internas (437 ocorrências) [9].
*   Os problemas técnicos relacionados ao **artefato** (788 menções) e ao **processo** (544 menções) dominam as causas de infelicidade, superando fatores humanos/sociais (416 menções) [17].
*   Variáveis demográficas como idade, gênero, país e renda **não mostraram relação significativa** com os níveis de felicidade [16].

---

## Desafios do Uso das Metricas

*   **Social desirability bias:** Participantes podem tentar parecer mais positivos do que realmente são [18].
*   **Dificuldade de generalização:** A amostra é limitada a usuários ativos do GitHub, que podem ser mais jovens ou ter perfis diferentes da média geral [18, 19].
*   **Atribuição de causalidade:** Dependência da capacidade dos participantes de identificar e articular corretamente as fontes de sua infelicidade [20].

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

*   **Representatividade:** Foco exclusivo na comunidade GitHub, o que pode excluir desenvolvedores que não participam de comunidades abertas ou possuem restrições empresariais [18, 19].
*   **Desequilíbrio de Gênero:** A amostra foi composta por 94% de homens, refletindo vieses existentes na área, mas limitando a análise para outros gêneros [21].
*   **Efeito de Ordem:** A ordem das perguntas na survey poderia influenciar o contexto das respostas (embora mitigado por randomização) [20].
*   **Memória:** O instrumento SPANE baseia-se no relato de experiências das últimas 4 semanas, dependendo da precisão da memória dos participantes [4].

---

## Contribuicao Principal

A principal contribuição do trabalho é o fornecimento da **primeira estimativa de base (baseline) quantitativa da felicidade** de desenvolvedores em larga escala, aliada a uma **taxonomia detalhada de 219 causas de infelicidade**. O estudo demonstra que a infelicidade dos desenvolvedores é predominantemente causada por fatores externos controláveis (processos e ferramentas), e não por traços internos, sugerindo que gestores têm oportunidades reais de melhorar o bem-estar e a produtividade através de intervenções técnicas e organizacionais [1, 3, 22, 23].

---

*Extraido via NotebookLM em March 2026 para MLR: Software Developer Metrics in Practice*
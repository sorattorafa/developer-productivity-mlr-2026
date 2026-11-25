# P0482 — Low-code vs. the developer: An empirical study on the developer experience and efficiency of a no-code platform

**Decisao: INCLUIDO | Qualidade: 4.5/5**

---

## Dados Bibliograficos

| Campo | Valor |
|-------|-------|
| **ID** | P0482 |
| **Autores** | Till Guthardt, Jens Kosiol, Oliver Hohlfeld [1, 2] |
| **Ano** | 2024 [3, 4] |
| **Venue** | MODELS Companion '24 (ACM/IEEE 27th International Conference on Model Driven Engineering Languages and Systems) [3, 4] |
| **DOI** | 10.1145/3652620.3688332 [1, 4] |
| **Tipo** | Conference paper [1, 3] |
| **Metodo** | Mixed methods (Qualitative semi-structured interviews and Quantitative experiment) [2, 5] |
| **Amostra** | 6 experts de SMEs (entrevistas) e 10 estudantes (experimento: 5 com experiência em programação e 5 sem) [6-8] |
| **Contexto** | Industry (SMEs na região de Hesse, Alemanha) e Academic (University of Kassel e TH Köln) [7-9] |
| **Modo de trabalho** | On-site (experimento realizado em sala controlada) [7] |
| **Metodologia** | Not specified [10, 11] |

---

## Objetivo

O objetivo principal do artigo é investigar a aceitação e as barreiras das **Low-Code Development Platforms (LCDPs)** em pequenas e médias empresas (SMEs) e comparar empiricamente o desempenho e a experiência de desenvolvedores experientes versus **citizen developers** (pessoas sem experiência prévia em programação) ao utilizar uma ferramenta de **no-code** [2, 5, 9, 12].

---

## Questoes de Pesquisa

*   **RQ1:** How accepted are LCDPs in SMEs and what barriers prevent SMEs from using them? [5, 13]
*   **RQ2:** What experience is required to use no-code tools efficiently? [14, 15]

---

## Metricas e Instrumentos de Avaliacao

| Metrica | Categoria | Nivel | Como Coletada | Validada |
|---------|-----------|-------|---------------|----------|
| Success (Correctness) | Quality | Individual | Grading scheme baseado na correção das funcionalidades da app [8, 16] | Partial (Custom scheme) [16, 17] |
| Processing Time | Productivity | Individual | Medição do tempo do início à sinalização de término pelo participante [16, 18] | Yes (Standard measure) [16] |
| Question Count | Productivity / DevEx | Individual | Contagem de perguntas feitas durante a tarefa [8, 16] | No [16] |
| Ease of Use (FQ1) | Satisfaction / DevEx | Individual | Likert scale de 5 pontos no questionário final [16, 19] | Partial [20] |
| Learnability (FQ2) | DevEx | Individual | Likert scale de 5 pontos no questionário final [19, 21] | Partial [20] |
| Perceived Challenge (FQ3/FQ5) | DevEx | Individual | Likert scale de 5 pontos no questionário final [19] | Partial [20] |

---

## Frameworks e Metricas

### Frameworks Referenciados
*   **Developer Experience (DevEx):** REFERENCED (utilizado como conceito central para avaliar a facilidade de uso e aprendizado) [1, 12, 21, 22].
*   **Low-Code Development Platforms (LCDPs):** REFERENCED (objeto central do estudo) [2, 23, 24].

### Frameworks Propostos
O artigo não propõe um framework formal, mas desenvolve um **prototype no-code builder** para fins de experimentação controlada [5, 25].

---

## Fatores que Influenciam Produtividade

### Fatores Positivos
| Fator | Categoria |
|-------|-----------|
| Ready-made components (Drag-and-drop) | Technical [2, 23] |
| Automation of deployment | Process [23] |
| Technology affinity (Tech-savvy users) | Human [26, 27] |
| Specialized tools for specific use cases | Technical [13, 28] |

### Fatores Negativos
| Fator | Categoria |
|-------|-----------|
| Fear of excessive training costs/time | Organizational [5, 29, 30] |
| Limited functionality and flexibility | Technical [31-33] |
| Lack of employee capacity | Organizational [31] |
| Vendor lock-in | Organizational [33] |
| Low awareness of platforms | Human / Process [31] |

---

## Papel da IA e Automacao

| Campo | Valor |
|-------|-------|
| Usa IA/ML? | No — O protótipo é focado em UI elements e predefined controllers [25, 34, 35]. |
| Automacao de coleta? | Yes — Screen recordings e logs foram usados para coletar interações e tempo [16, 36]. |
| Impacto de IA na produtividade? | Not applicable — Não foi testado no estudo. |

---

## Resultados Principais

*   Não houve diferença estatisticamente significativa na **correctness** das tarefas entre programadores e **citizen developers** (quase todos atingiram 100%) [2, 8, 18, 37].
*   A diferença no **processing time** entre os grupos também não foi estatisticamente significativa (Median: 23 min para inexperientes vs. 19 min para experientes, p=0.8785) [2, 18, 38, 39].
*   O estudo identificou o **medo de custos excessivos de treinamento** como uma barreira proeminente para a adoção de LCDPs em SMEs, um fator menos citado em estudos anteriores [5, 29, 33].
*   Alta **learnability** (4.3/5) e facilidade de uso (4.1/5) foram relatadas igualmente por ambos os grupos [21, 36].
*   A afinidade tecnológica pessoal teve a maior correlação com o sucesso na tarefa (r=0.68) [26, 27].

---

## Desafios do Uso das Metricas

*   **Small sample size:** O pequeno número de participantes (10 no experimento, 6 nas entrevistas) limita o poder estatístico e a generalização [27, 32].
*   **Task complexity:** As tarefas do estudo foram consideradas relativamente simples, o que pode ter mascarado diferenças que surgiriam em apps complexas [27, 40, 41].
*   **Unreliability of automation:** Menção de que transcrições automáticas de entrevistas nem sempre são confiáveis, exigindo correção manual [11].

---

## Avaliacao de Qualidade Metodologica

| Criterio | Pontuacao (0-2) |
|----------|----------------|
| Objetivo claramente definido | 2 [2, 5] |
| Metodologia adequada ao objetivo | 2 [5, 18] |
| Amostra/contexto descrito adequadamente | 1 [6, 8, 27] |
| Ameacas a validade discutidas | 2 [27, 32] |
| Resultados com evidencia suficiente | 2 [39, 42, 43] |
| Contribuicao clara para pratica ou teoria | 2 [18, 29, 44] |
| **TOTAL** | **11/12** |

---

## Limitacoes

*   **Tamanho da amostra:** Apenas 10 participantes no estudo de usuário e 6 entrevistas, o que limita a generalização dos resultados [27, 32].
*   **Simplicidade da ferramenta:** O protótipo utilizado possui funcionalidades restritas em comparação com plataformas industriais [27].
*   **Complexidade das tarefas:** As tarefas podem não ter sido desafiadoras o suficiente para diferenciar o desempenho de especialistas [27, 41].
*   **Viés de apresentação:** A demonstração inicial da ferramenta pode ter influenciado as respostas dos entrevistados sobre casos de uso [45].

---

## Contribuicao Principal

A principal contribuição do artigo é demonstrar, por meio de um estudo empírico quantitativo (o primeiro a comparar tempo de processamento), que a experiência prévia em programação não é um diferencial crítico para a eficiência e sucesso em tarefas simples de desenvolvimento **no-code**, sugerindo que as preocupações de empresas sobre longos períodos de treinamento para **citizen developers** podem ser infundadas [2, 18, 30, 44].

---

*Extraido via NotebookLM em March 2026 para MLR: Software Developer Metrics in Practice*
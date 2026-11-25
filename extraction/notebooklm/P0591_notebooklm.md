# P0591 — Chatting with AI: Deciphering Developer Conversations with ChatGPT

**Decisao: INCLUIDO | Qualidade: 4.5/5**

---

## Dados Bibliograficos

| Campo | Valor |
|-------|-------|
| **ID** | P0591 |
| **Autores** | Suad Mohamed, Abdullah Parvin, Esteban Parra |
| **Ano** | 2024 |
| **Venue** | 21st International Conference on Mining Software Repositories (MSR ’24) |
| **DOI** | https://doi.org/10.1145/3643991.3645078 |
| **Tipo** | Conference paper |
| **Metodo** | Empirical study (Mixed methods: Open coding and Machine Learning classification) |
| **Amostra** | 321 ChatGPT conversations (filtered from a snapshot of 1,929 links) |
| **Contexto** | Mixed — conversations sourced from GitHub and Hacker News via the DevGPT dataset |
| **Modo de trabalho** | Not specified |
| **Metodologia** | Not specified |

---

## Objetivo

O principal objetivo do artigo é compreender como os desenvolvedores se envolvem e utilizam Large Language Models (LLMs), identificando padrões e propósitos nas conversas que eles mantêm com o ChatGPT [1, 2]. O estudo busca preencher a lacuna de conhecimento que existe além das evidências anedóticas sobre o uso dessas ferramentas no desenvolvimento de software [1, 3].

---

## Questoes de Pesquisa

*   **RQ1:** What are the most common usages or types of questions that developers present to ChatGPT? [2]

---

## Metricas e Instrumentos de Avaliacao

| Metrica | Categoria | Nivel | Como Coletada | Validada |
|---------|-----------|-------|---------------|----------|
| Accuracy | Quality | Individual | Calculada via ML classifier performance [4] | Yes [5] |
| Precision | Quality | Individual | Calculada via ML classifier performance [4] | Yes [6] |
| Recall | Quality | Individual | Calculada via ML classifier performance [4] | Yes [6] |
| F1-score | Quality | Individual | Média harmônica de Precision e Recall [4] | Yes [7] |
| Occurrence/Frequency | Activity | Individual | Contagem manual e percentual de categorias [8, 9] | Partial (via Cohen’s Kappa) [6] |
| Cohen’s Kappa Agreement | Collaboration | Team | Medida de concordância entre anotadores (0.584) [6] | Yes [10] |

---

## Frameworks e Metricas

### Frameworks Referenciados
*   **DevGPT**: REFERENCED — O dataset utilizado como fonte primária das conversas [11, 12].

### Frameworks Propostos
O artigo não propõe um novo framework formal, mas apresenta uma taxonomia de 19 categorias para classificar os propósitos das conversas entre desenvolvedores e LLMs [6, 8].

---

## Fatores que Influenciam Produtividade

### Fatores Positivos
| Fator | Categoria |
|-------|-----------|
| Automation of tedious tasks | Process |
| Information gathering / Knowledge base access | Technical/Human |
| Assistance in writing and suggesting code | Technical |
| Code comprehension and debugging support | Technical |

### Fatores Negativos
| Fator | Categoria |
|-------|-----------|
| Privacy concerns and lack of direct consent | Organizational/Human |
| Apprehension towards LLM competence in abstract tasks | Human |
| Risk of misused usage data for predatory monetization | Organizational |

---

## Papel da IA e Automacao

| Campo | Valor |
|-------|-------|
| Usa IA/ML? | Yes — O estudo analisa o uso de ChatGPT e utiliza classificadores como Random Forest e SVM para categorizar conversas [2, 4]. |
| Automacao de coleta? | No — Os dados foram extraídos de um dataset pré-existente (DevGPT) [11]. |
| Impacto de IA na produtividade? | LLMs melhoram a produtividade ao auxiliar em tarefas como geração de especificações, documentação, tradução de linguagens e depuração [10, 13]. |

---

## Resultados Principais

*   Identificação de **19 categorias distintas** de propósitos em conversas de desenvolvedores com IA [8].
*   **57,02%** das conversas são relacionadas a tarefas de codificação, enquanto **42,98%** referem-se a tarefas não relacionadas a código [2].
*   Os usos mais comuns são **Write Code (18,07%)** e **General Info (13,08%)** [2, 9].
*   **10,59%** das conversas são testes de Turing para avaliar as capacidades intrínsecas dos modelos [14].
*   O classificador **Random Forest** obteve o melhor desempenho na identificação automática das categorias, com um F1-score de 0,582 [7].
*   **91%** das conversas rotuladas como "simple task" foram identificadas corretamente pelo modelo de ML [15].

---

## Desafios do Uso das Metricas

*   **Imbalanced data**: O desequilíbrio nas amostras coletadas causou falsos positivos na classificação automática de certas categorias [15].
*   **Privacy concerns**: A falta de consentimento direto dos usuários cujas conversas compõem o dataset gera desafios éticos e de privacidade [16].
*   **Researcher bias**: O uso de open coding introduz o risco de interpretações enviesadas ou omissão de casos de uso não presentes na amostra [17].

---

## Avaliacao de Qualidade Metodologica

| Criterio | Pontuacao (0-2) |
|----------|----------------|
| Objetivo claramente definido | 2 |
| Metodologia adequada ao objetivo | 2 |
| Amostra/contexto descrito adequadamente | 2 |
| Ameacas a validade discutidas | 2 |
| Resultados com evidencia suficiente | 2 |
| Contribuicao clara para pratica ou teoria | 1 |
| **TOTAL** | **11/12** |

---

## Limitacoes

*   Tamanho reduzido da amostra para o treinamento de modelos de machine learning [15].
*   Preocupações com a privacidade e a falta de consentimento direto dos participantes originais das conversas [16].
*   Possibilidade de viés dos pesquisadores durante o processo de open coding [17].
*   Uso de uma lista fixa de amostras em vez de uma abordagem de saturação teórica [17].
*   Resultados baseados em um único snapshot do dataset DevGPT, o que pode limitar a generalização para todas as interações desenvolvedor-IA [18].

---

## Contribuicao Principal

A principal contribuição deste trabalho é a criação de uma taxonomia empírica que decifra como desenvolvedores interagem com LLMs, revelando que o ChatGPT é utilizado tanto como um assistente técnico especializado (especialmente para geração de código e debugging) quanto como uma ferramenta de busca de informação geral, destacando sua versatilidade no ecossistema de desenvolvimento de software [1, 2, 19, 20].

---

*Extraido via NotebookLM em March 2026 para MLR: Software Developer Metrics in Practice*
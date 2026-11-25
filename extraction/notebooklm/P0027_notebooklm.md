# P0027 — What Predicts Software Developers’ Productivity?

**Decisao: INCLUIDO | Qualidade: 5/5**

---

## Dados Bibliograficos

| Campo | Valor |
|-------|-------|
| **ID** | P0027 |
| **Autores** | Emerson Murphy-Hill, Ciera Jaspan, Caitlin Sadowski, David Shepherd, Michael Phillips, Collin Winter, Andrea Knight, Edward Smith, and Matthew Jorde [1] |
| **Ano** | 2019 [2] |
| **Venue** | IEEE Transactions on Software Engineering [2] |
| **DOI** | 10.1109/TSE.2019.2900308 [2] |
| **Tipo** | Journal article [2] |
| **Metodo** | Quantitative and Qualitative (Survey and multiple regression models) [3, 4] |
| **Amostra** | 622 software developers and 88 analysts [4-7] |
| **Contexto** | Industry: Google, ABB, and National Instruments [5, 8] |
| **Modo de trabalho** | Not explicitly specified for the whole sample, but Google is described as valuing co-location in open-plan offices [8] |
| **Metodologia** | Mixed/Not specified; Google uses flexible per-team processes (e.g., Agile) [8] |

---

## Objetivo

O objetivo principal do artigo é realizar um estudo comparativo abrangente para identificar e classificar os fatores que predizem a produtividade percebida dos desenvolvedores de software em diferentes empresas e compará-los com outros trabalhadores do conhecimento (knowledge workers) [3, 9, 10].

---

## Questoes de Pesquisa

*   **RQ1:** What factors most strongly predict developers’ self-rated productivity? [3]
*   **RQ2:** How do these factors differ across companies? [3]
*   **RQ3:** What predicts developer self-rated productivity, in particular, compared to other knowledge workers? [3]

---

## Metricas e Instrumentos de Avaliacao

| Metrica | Categoria | Nivel | Como Coletada | Validada |
|---------|-----------|-------|---------------|----------|
| Self-rated productivity | Productivity | Individual | Survey (Rating of agreement with "I regularly reach a high level of productivity") [11] | Yes (via interview and field test) [11, 12] |
| Lines of code changed per unit time | Activity | Individual | Repository mining (Google only) [13] | No (considered a fraught measure) [13] |
| Number of changelists merged per unit time | Activity | Individual | Repository mining (Google only) [13] | Partial (used for contextualization) [14] |
| 48 Productivity Factors | Human/Technical/Organizational | Individual/Team | Survey (agreement with 48 statements) [15] | Yes (derived from validated literature) [16-19] |

---

## Frameworks e Metricas

### Frameworks Referenciados
*   **SmartWoW:** APPLIED (The survey instrument was partially based on this tool) [17].
*   **COCOMO II:** APPLIED (Several factors analyzed were derived from the COCOMO II line of research) [20].
*   **Work Design Questionnaire (WDQ):** REFERENCED (Source for several productivity factors) [18].
*   **Job Diagnostic Survey (JDS):** REFERENCED [18].
*   **Knowledge Work Productivity Assessment (KWPA):** REFERENCED [21].

### Frameworks Propostos
O artigo não propõe um novo framework, mas fornece um ranking priorizado de fatores de produtividade que pode servir como guia para intervenções organizacionais [22, 23].

---

## Fatores que Influenciam Produtividade

### Fatores Positivos
| Fator | Categoria |
|-------|-----------|
| Job enthusiasm [5, 24] | Human |
| Peer support for new ideas [5, 24] | Human/Social |
| Receiving useful feedback about job performance [5, 24] | Organizational/Human |
| Task variety [5, 25] | Process |
| Ability to work remotely [5, 26] | Environmental/Organizational |

### Fatores Negativos
| Fator | Categoria |
|-------|-----------|
| Personnel turnover on the team [27] | Organizational |
| High software complexity [20] | Technical |
| Interruptions and distractions [21, 28] | Environmental |

---

## Papel da IA e Automacao

| Campo | Valor |
|-------|-------|
| Usa IA/ML? | No — o estudo utiliza modelos de regressão linear múltipla para análise estatística [4]. |
| Automacao de coleta? | No — a coleta principal foi realizada via survey manual [29]. |
| Impacto de IA na produtividade? | Not applicable — o estudo não foca em ferramentas de IA [1, 5]. |

---

## Resultados Principais

*   Os fatores que mais fortemente predizem a produtividade autorreferida são **não-técnicos**, como entusiasmo pelo trabalho, apoio de colegas a novas ideias e feedback útil sobre o desempenho [5, 24].
*   Fatores técnicos tradicionais (como os do **COCOMO II**, ex: processamento e armazenamento de dados) mostraram-se preditores mais fracos de produtividade individual do que fatores humanos e sociais [20, 30].
*   Métricas objetivas (Lines of Code, Changelists) explicam apenas uma pequena parcela (menos de **3%**) da percepção de produtividade do próprio desenvolvedor [14].
*   Desenvolvedores diferem de outros trabalhadores do conhecimento (analistas) por serem mais sensíveis à **variedade de tarefas** e à capacidade de **trabalhar remotamente** [2, 25].
*   A antiguidade (seniority) tem uma correlação negativa com a produtividade autorreferida; desenvolvedores mais seniores tendem a se avaliar como ligeiramente menos produtivos [14].

---

## Desafios do Uso das Metricas

*   **Objective measures** (como linhas de código) sofrem de falta de flexibilidade e podem ser "manipuladas" (gaming) pelos desenvolvedores [31].
*   **Subjective measures** podem ser afetadas por vieses cognitivos e pelo viés de desejabilidade social (social desirability bias) [31, 32].
*   **Causality:** O estudo mede correlações, mas não pode estabelecer definitivamente que um fator causa produtividade sem experimentos controlados adicionais [33-35].

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

*   O estudo foca em apenas uma dimensão da produtividade (autopercepção) [32].
*   Uso de uma única pergunta para medir a produtividade, o que pode não capturar toda a experiência do desenvolvedor [36].
*   Ausência de uma janela de tempo fixa definida na pergunta da pesquisa (ex: produtividade na última semana vs. último ano) [36].
*   A generalização é limitada, pois os dados vêm de apenas três empresas de grande porte [37].
*   Possível viés de não-resposta, dado que os participantes foram voluntários [37].

---

## Contribuicao Principal

O estudo representa a investigação mais ampla até o momento sobre o que prediz a produtividade individual dos desenvolvedores, demonstrando que **fatores humanos e sociais são preditores significativamente mais fortes do que fatores técnicos**, desafiando o foco tradicional da pesquisa em engenharia de software [9, 24, 38].

---

*Extraido via NotebookLM em March 2026 para MLR: Software Developer Metrics in Practice*
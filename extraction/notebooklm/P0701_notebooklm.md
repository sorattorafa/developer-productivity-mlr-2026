# P0701 — Metrics for Evaluating and Improving Transparency in Software Engineering: An Empirical Study and Improvement Model

**Decisao: INCLUIDO | Qualidade: 5/5**

---

## Dados Bibliograficos

| Campo | Valor |
|-------|-------|
| **ID** | P0701 |
| **Autores** | Paulinus Ofem, Bassey Isong, Francis Lugayizi |
| **Ano** | 2024 |
| **Venue** | SN Computer Science |
| **DOI** | 10.1007/s42979-024-03471-3 |
| **Tipo** | Journal article (Original Research) |
| **Metodo** | Quantitative (Descriptive, Correlational, Causal, and Controlled Experiment) |
| **Amostra** | 252 valid responses (210 professionals/experts/postgraduates and 42 students) |
| **Contexto** | Mixed — ICT professionals and computing students from South Africa and globally via online platforms |
| **Modo de trabalho** | Mixed (Experiment conducted both in-person and online) |
| **Metodologia** | Focused on Requirements Engineering (comparing OO-SRS vs NOO-SRS) |

---

## Objetivo

O principal objetivo deste estudo é validar empiricamente medidas e métricas para avaliar e melhorar a transparência de produtos do ciclo de vida de desenvolvimento de software (SDLC) [1]. A pesquisa investiga as correlações entre fatores de transparência e suas métricas correspondentes, demonstrando sua utilidade através de um experimento controlado que analisa o impacto da transparência na manutenibilidade (Maintainability), comunicação e produtividade dos stakeholders [1, 2].

---

## Questoes de Pesquisa

* **RQ1:** Avaliar o impacto da transparência na manutenibilidade (Maintainability) de Software Requirements Specifications (SRS) [3].
* **RQ2:** Avaliar o impacto da transparência na comunicação eficaz e eficiente de SRSs [3].
* **RQ3:** Avaliar o impacto da transparência na produtividade dos stakeholders utilizando diferentes SRSs [3].
* **RQ4:** Investigar as correlações entre os fatores (constructs) de transparência e suas métricas [3].
* **RQ5:** Investigar as percepções dos stakeholders em relação a diferentes tipos de SRS [3].
* **RQ6:** Propor um modelo de melhoria de transparência (Transparency-Improving Model) [3].

---

## Metricas e Instrumentos de Avaliacao

| Metrica | Categoria | Nivel | Como Coletada | Validada |
|---------|-----------|-------|---------------|----------|
| Modifiability Time (MT) | Quality (Maintainability) | Individual/Team | Experiment Task / Questionnaire | Yes [4, 5] |
| Modifiability Efficiency (MEffic) | Productivity | Individual/Team | Experiment Task / Questionnaire | Yes [4, 5] |
| Modifiability Effectiveness (MEffec) | Productivity | Individual/Team | Experiment Task / Questionnaire | Yes [4, 5] |
| Understandability Time (UnT) | Quality (Maintainability) | Individual/Team | Experiment Task / Questionnaire | Yes [5, 6] |
| Understandability Effectiveness (UnEffec) | Productivity | Individual/Team | Experiment Task / Questionnaire | Yes [5, 6] |
| Understandability Efficiency (UnEffic) | Productivity | Individual/Team | Experiment Task / Questionnaire | Yes [5, 6] |
| Portability of Info Channel (PIC) | Quality (Accessibility) | Organization | Objective assessment / Questionnaire | Yes [5, 7] |
| Completeness of Information (CoI) | Quality (Accessibility) | Organization | Questionnaire | Yes [5, 7] |
| Ease of Finding Info (EFI) | Quality (Accessibility) | Individual | Questionnaire | Yes [5, 7] |
| Usability Time (UsT) | Productivity | Individual | Experiment Task / Questionnaire | Yes [5, 8] |
| Satisfactory Usage (SU) | Satisfaction | Individual | Questionnaire | Yes [5, 8] |
| Ease of Reuse (EoR) | Quality (Reusability) | Individual/Team | Questionnaire | Yes [5, 9] |
| Readability Index (RoI) | Quality (Understandability) | Individual/Team | Objective Index (Gunning Fog/Flesch) | Yes [5, 6] |
| Conciseness Index (ConI) | Quality (Understandability) | Individual/Team | Objective Assessment | Yes [5, 6] |

---

## Frameworks e Metricas

### Frameworks Referenciados
* **Goal Question Metric (GQM):** APPLIED — Utilizado como base para o desenvolvimento do modelo de melhoria e das métricas [10, 11].
* **ISO/IEC 25010:** REFERENCED — Citado como padrão para modelos de qualidade de software [12].
* **Gilb and Finzi’s "define-your-own model":** APPLIED — Adotado em combinação com GQM para definir medidas [10].
* **Personal Construct Theory (PCT):** REFERENCED — Discutido como estratégia para lidar com requisitos antagônicos [13].

### Frameworks Propostos
O estudo propõe o **Transparency Improvement Model**, baseado no paradigma GQM, que integra dez passos: (1) estabelecer requisitos de transparência, (2) estabelecer metas, (3) criar questões, (4) identificar fatores de qualidade, (5) identificar métricas, (6) criar tarefas de avaliação, (7) analisar resultados, (8) gerar feedback, (9) processo de melhoria e (10) reavaliação [14, 15].

---

## Fatores que Influenciam Produtividade

### Fatores Positivos
| Fator | Categoria |
|-------|-----------|
| Object-Oriented Use Case Modeling | Technical/Process [1, 16] |
| High Understandability and Modifiability | Quality [17, 18] |
| Effective Communication (Shared Understanding) | Process [19, 20] |

### Fatores Negativos
| Fator | Categoria |
|-------|-----------|
| Natural Language-based SRS (Text-based) | Technical/Process [16] |
| Document Length (high number of pages) | Technical [21] |
| Ambiguity in Transparency Requirements | Process [22] |

---

## Papel da IA e Automacao

| Campo | Valor |
|-------|-------|
| Usa IA/ML? | No — O estudo foca em métricas empíricas coletadas via humanos [23]. |
| Automacao de coleta? | No — Coleta realizada via questionários estruturados (Google Forms) [24]. |
| Impacto de IA na produtividade? | Not applicable — Não discutido no escopo deste artigo. |

---

## Resultados Principais

* **Superioridade do OO-SRS:** Documentações baseadas em Use Case Modeling (Object-Oriented) são significativamente mais fáceis de manter, oferecem melhor comunicação e maior produtividade (Mean 3.75 de eficácia vs 3.26 no texto natural) [1, 16, 25].
* **Manutenibilidade:** O grupo OO-SRS reportou modifiabilidade muito superior (Mean 18.23) em comparação ao grupo de texto natural (Mean 0.91) [26].
* **Correlações Fortes:** Foram encontradas correlações positivas fortes entre todos os constructos de transparência (Acessibilidade, Usabilidade, Compreensibilidade, Reusabilidade e Modificabilidade) [27, 28].
* **Ajuste do Modelo:** A análise de regressão mostrou que o modelo explica 47% da variância da transparência para documentação OO-SRS e 26% para texto natural [29].
* **Percepção dos Stakeholders:** 80.2% dos participantes do OO-SRS não tiveram problemas com a estrutura do documento, enquanto a vasta maioria do grupo NL-SRS reportou dificuldades [21, 30].

---

## Desafios do Uso das Metricas

* **Natureza Multifacetada:** A complexidade e ambiguidade inerentes ao conceito de transparência dificultam a medição precisa [22, 31].
* **Propriedades Antagônicas:** Conflitos entre transparência e requisitos de privacidade, segurança e confidencialidade [22].
* **Custo de Implementação:** A inclusão de processos de transparência pode elevar o custo total do desenvolvimento de software [32].
* **Resistência Humana:** Engenheiros de requisitos podem perceber ferramentas de verificação de qualidade como uma ameaça à segurança no emprego [33].

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

* **Escopo da Fase:** O estudo limitou-se à fase de Engenharia de Requisitos (RE) e especificamente a documentos SRS [34, 35].
* **Representatividade da Amostra:** Excluiu usuários finais e clientes não técnicos (foco apenas em profissionais de TIC) [34, 36].
* **Complexidade do Material:** Os materiais e tarefas experimentais podem não representar totalmente a complexidade de projetos industriais de grande escala [35, 37].
* **Falta de Rastreabilidade:** A ausência de ferramentas de rastreabilidade (Traceability) nos documentos pode ter afetado o desempenho na análise de impacto [35].

---

## Contribuicao Principal

A principal contribuição deste trabalho é a validação empírica de um conjunto de métricas de transparência e a proposição de um **Modelo de Melhoria da Transparência (Transparency Improvement Model)** estruturado. O estudo prova que a adoção de técnicas orientadas a objetos na documentação de requisitos (implicit transparency) é superior ao uso de linguagem natural pura, resultando em ganhos mensuráveis de manutenibilidade, clareza na comunicação e produtividade dos desenvolvedores [1, 38, 39].

---

*Extraido via NotebookLM em March 2026 para MLR: Software Developer Metrics in Practice*
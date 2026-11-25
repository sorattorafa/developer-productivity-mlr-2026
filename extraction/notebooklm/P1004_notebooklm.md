# P1004 — Developer Experience Considering Work Difficulty in Software Development

**Decisao: INCLUIDO | Qualidade: 5/5**

---

## Dados Bibliograficos

| Campo | Valor |
|-------|-------|
| **ID** | P1004 |
| **Autores** | Taketo Tsunoda, Hironori Washizaki, Yosiaki Fukazawa, Sakae Inoue, Yoshiiku Hanai, Masanobu Kanazawa |
| **Ano** | 2018 |
| **Venue** | International Journal of Networked and Distributed Computing |
| **DOI** | Not specified |
| **Tipo** | Journal article (Extended version of conference paper) |
| **Metodo** | Repository mining / Quantitative analysis |
| **Amostra** | 3 commercial projects, each with ~250,000 LOC and ~200 developers |
| **Contexto** | Industry — three large commercial projects executed by the same organization |
| **Modo de trabalho** | Not specified |
| **Metodologia** | Not specified |

---

## Objetivo

O principal objetivo do artigo é examinar a relação entre a experiência do desenvolvedor e a introdução de defeitos, considerando a dificuldade do trabalho (Work difficulty) [1, 2]. Os autores argumentam que, para avaliar os desenvolvedores de forma justa, é necessário levar em conta a complexidade dos arquivos e sua origem, pois desenvolvedores experientes podem ser erroneamente rotulados como propensos a erros apenas por trabalharem em partes mais complexas do sistema [2, 3].

---

## Questoes de Pesquisa

*   **RQ1:** Do defect tendency and complexity of inherited files vary with file-experienced developer participation? [4]
*   **RQ2:** Do experienced developers introduce fewer defects or work on more complicated files? [4]
*   **RQ3:** Does the same developer introduce many defects in each project? What are the features of these developers? [4]

---

## Metricas e Instrumentos de Avaliacao

| Metrica | Categoria | Nivel | Como Coletada | Validada |
|---------|-----------|-------|---------------|----------|
| Lines of Code (LOC) | Quality/Complexity | Individual | Product metrics via repository analysis | Yes [5, 6] |
| Call Number | Quality/Complexity | Individual | Number of functions/methods defined in other files called by a file | Yes [5, 6] |
| Defect Rate | Quality | Individual/Team | Ratio of files with at least one defect, identified via SZZ algorithm | Yes [7, 8] |
| Number of Organizations | Complexity/Context | Organization | Count of organizations that previously modified a file (File Origin) | Yes [5, 9] |
| Contributing Rate | Activity | Individual | Ratio of modifications by a developer type vs total file changes | Yes [10] |

---

## Frameworks e Metricas

### Frameworks Referenciados
*   **SZZ Algorithm**: APPLIED — Utilizado para identificar automaticamente quais alterações introduziram bugs através de dados do SVN e bug tracking systems [7].
*   **Wilcoxon Rank Sum Test**: APPLIED — Utilizado para análise estatística das diferenças entre grupos de desenvolvedores e complexidade de arquivos [11, 12].

### Frameworks Propostos
O artigo não propõe um novo framework nomeado, mas apresenta uma metodologia para classificação de arquivos baseada em **File Origin** (Número de Organizações envolvidas) para avaliar a dificuldade do trabalho [2, 5].

---

## Fatores que Influenciam Produtividade

### Fatores Positivos
| Fator | Categoria |
|-------|-----------|
| Developer Experience (Specific and General) | Human |
| Domain Experience | Human |

### Fatores Negativos
| Fator | Categoria |
|-------|-----------|
| File Complexity (High LOC/Call Number) | Technical |
| Multiple Organizations Involvement (File Origin) | Organizational |
| High Number of Developers per File | Process |

---

## Papel da IA e Automacao

| Campo | Valor |
|-------|-------|
| Usa IA/ML? | No |
| Automacao de coleta? | Yes — O algoritmo SZZ automatiza a identificação de mudanças que introduzem bugs [7]. |
| Impacto de IA na produtividade? | Not applicable |

---

## Resultados Principais

*   Desenvolvedores não familiarizados com projetos anteriores tendem a introduzir mais defeitos, mesmo em arquivos que não são complexos [13].
*   Desenvolvedores experientes não trabalham necessariamente em arquivos mais complicados [1, 13].
*   Ao considerar uma dificuldade de trabalho similar, desenvolvedores experientes introduzem menos defeitos [1, 13, 14].
*   A maioria dos desenvolvedores não introduz muitos defeitos de forma consistente; o número de defeitos em um projeto não é um preditor confiável para o próximo [15].
*   Os desenvolvedores que introduzem o maior número de defeitos são geralmente aqueles responsáveis pelos arquivos mais complexos (maior LOC e Call Number) [3, 16].
*   A propensão a defeitos de um desenvolvedor altamente "buggy" diminui à medida que ele ganha experiência específica no domínio [14, 16].

---

## Desafios do Uso das Metricas

*   **Fair Evaluation**: Avaliar desenvolvedores apenas por taxas de defeitos sem considerar a complexidade do código (Work difficulty) leva a avaliações injustas [2, 3].
*   **Expert Assignment**: A dificuldade de atribuir tarefas complexas aos desenvolvedores corretos sem métricas que capturem a dificuldade real do trabalho [17].

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

*   O estudo analisou apenas três projetos de uma única organização [14, 18].
*   Não foi considerado se os desenvolvedores permaneceram no mesmo domínio funcional ao mudar de projeto [18].
*   As métricas utilizadas (defesas, LOC, Call Number) capturam apenas uma parcela limitada da qualidade do código e da experiência [18].

---

## Contribuicao Principal

A principal contribuição do trabalho é a demonstração empírica de que a **experiência do desenvolvedor deve ser avaliada em conjunto com a dificuldade da tarefa** (Work difficulty) [1, 14]. O estudo prova que a complexidade dos arquivos é um fator determinante na introdução de erros, e que desenvolvedores experientes mostram sua superioridade técnica principalmente quando enfrentam níveis de dificuldade comparáveis aos de iniciantes, reduzindo significativamente a taxa de bugs à medida que ganham maturidade no domínio específico [13, 14, 16].

---

*Extraido via NotebookLM em March 2026 para MLR: Software Developer Metrics in Practice*
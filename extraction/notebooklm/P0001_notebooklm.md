# P0001 — Understanding Developer Productivity: Input-Output Perspectives Within the SPACE Framework

**Decisao: INCLUIDO | Qualidade: 5/5**

---

## Dados Bibliograficos

| Campo | Valor |
|-------|-------|
| **ID** | P0001 |
| **Autores** | Iman Tunggono, Elfindah Princes |
| **Ano** | 2024 |
| **Venue** | Not specified (BINUS Graduate Program) |
| **DOI** | Not specified |
| **Tipo** | Conference paper |
| **Metodo** | Quantitative (Survey and PLS-SEM) |
| **Amostra** | 161 validated responses from professional developers |
| **Contexto** | Industry — Indonesian professional software development communities (LinkedIn, Facebook, Discord) |
| **Modo de trabalho** | Not specified |
| **Metodologia** | Not specified |

---

## Objetivo

O objetivo principal do estudo é investigar como as dimensões do **SPACE Framework** interagem dentro de um modelo de **input-output** e determinar quais dessas dimensões exercem a influência mais forte na produtividade percebida pelos desenvolvedores [1, 2].

---

## Questoes de Pesquisa

*   **RQ1:** How these [SPACE] dimensions interact within an input-output model? [1]
*   **RQ2:** Which [dimensions] most strongly influence developers' perceived productivity? [1]

---

## Metricas e Instrumentos de Avaliacao

| Metrica | Categoria | Nivel | Como Coletada | Validada |
|---------|-----------|-------|---------------|----------|
| **Satisfaction (SATF)** | Satisfaction | Individual | 5-point Likert Scale (Adaptado de [3, 4]) | Yes [3, 5] |
| **Communication (COMM)** | Collaboration | Individual/Team | 5-point Likert Scale (Adaptado de [3, 4]) | Yes [3, 5] |
| **Efficiency (EFFC)** | Process | Individual | 5-point Likert Scale (Adaptado de [3]) | Yes [3, 5] |
| **Activity (ACTV)** | Activity | Individual | 5-point Likert Scale (Adaptado de [3]) | Yes [3, 5] |
| **Performance (PERF)** | Quality | Individual/Team | 5-point Likert Scale (Adaptado de [3, 6]) | Yes [3, 5] |
| **Perceived Productivity (PROD)** | Productivity | Individual/Team | 5-point Likert Scale (Adaptado de [7, 8]) | Yes [3, 5] |

---

## Frameworks e Metricas

### Frameworks Referenciados
*   **SPACE Framework**: APPLIED (Base principal para o modelo de pesquisa) [2, 9].
*   **DORA metrics**: REFERENCED (Discutido como focado em DevOps e métricas quantitativas) [10].
*   **DevEx framework**: REFERENCED (Discutido por sua perspectiva centrada no desenvolvedor) [9].

### Frameworks Propostos
O estudo propõe um **Input-Output Model** baseado no SPACE, definindo **Activity (ACTV)** como o *input* e **Performance (PERF)** como o *output*, com as dimensões de Satisfaction, Communication e Efficiency atuando como fatores indiretos que potencializam a entrada ou a saída [2].

---

## Fatores que Influenciam Produtividade

### Fatores Positivos
| Fator | Categoria |
|-------|-----------|
| **Performance (Work quality)** | Technical |
| **Communication** | Organizational/Process |
| **Efficiency (Flow state/Lack of disruptions)** | Process |

### Fatores Negativos
| Fator | Categoria |
|-------|-----------|
| **Disruptions/Interruptions** | Process |
| **Context switching** | Process |
| **Poor technical documentation** | Process |

---

## Papel da IA e Automacao

| Campo | Valor |
|-------|-------|
| Usa IA/ML? | **Yes** — Os autores declararam o uso da ferramenta **DeepSeek** para verificação gramatical e paráfrase no manuscrito [8]. |
| Automacao de coleta? | **No** — A coleta foi realizada via survey manual [11]. |
| Impacto de IA na produtividade? | O estudo menciona a adoção de IA como um dos fatores que contribuíram para demissões no setor tecnológico em 2022, mas não mede seu impacto direto na produtividade dos participantes [12]. |

---

## Resultados Principais

*   **Performance (PERF)**, particularmente a qualidade do trabalho, é o principal driver da produtividade percebida (β = 0.602, p < 0.001) [1, 13].
*   Métricas quantitativas de **Activity (ACTV)** não possuem relação estatisticamente significativa com os resultados de produtividade (β = -0.049, p = 0.518) [1, 13, 14].
*   A **Satisfaction (SATF)** não demonstrou influência significativa na produtividade neste modelo (β = 0.06, p = 0.219) [1, 15, 16].
*   **Communication (COMM)** e **Efficiency (EFFC)** influenciam a produtividade principalmente através do aumento da performance [15, 17].
*   A comunicação demonstrou um efeito moderado e significativo tanto na atividade (β = 0.303) quanto na performance (β = 0.356) [13].

---

## Desafios do Uso das Metricas

*   A complexidade de implementação prática do framework SPACE devido à sua abstração [9].
*   Risco de distorção de incentivos ao utilizar métricas compostas [18].
*   Métricas puramente quantitativas são propensas a manipulação ou interpretação errônea [18].
*   Dificuldade de comparação entre estudos devido à falta de medidas padronizadas de produtividade [19].

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

*   A amostra é composta majoritariamente por desenvolvedores jovens, do sexo masculino e residentes na Indonésia, o que pode limitar a generalização para outros grupos [19].
*   O uso exclusivo de surveys introduz o risco de viés de auto-relato (self-report bias) [19].
*   A ausência de métricas comportamentais objetivas para complementar os dados de percepção [6, 19].

---

## Contribuicao Principal

A principal contribuição do trabalho é a validação empírica de que a produtividade no desenvolvimento de software é impulsionada pela **qualidade da entrega (performance)** e pela **comunicação**, desafiando métricas convencionais que focam apenas no volume de atividades [1, 6]. O estudo reforça que intervenções organizacionais devem priorizar a otimização de processos e qualidade em vez de apenas monitorar a quantidade de código ou tarefas concluídas [14, 20].

---

*Extraido via NotebookLM em March 2026 para MLR: Software Developer Metrics in Practice*
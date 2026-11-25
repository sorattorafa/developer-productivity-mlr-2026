# P1297 — Software Project Managers' Perceptions of Productivity Factors: Findings from a Qualitative Study

**Decisao: INCLUIDO | Qualidade: 5/5**

---

## Dados Bibliograficos

| Campo | Valor |
|-------|-------|
| **ID** | P1297 |
| **Autores** | Edson Oliveira, Tayana Conte, Marco Cristo, Emilia Mendes [1] |
| **Ano** | 2016 [2] |
| **Venue** | International Symposium on Empirical Software Engineering and Measurement (ESEM) [2] |
| **DOI** | http://dx.doi.org/10.1145/2961111.2962626 [3] |
| **Tipo** | Conference paper [2] |
| **Metodo** | Qualitative (Exploratory Case Study using semi-structured interviews and Grounded Theory procedures) [4-6] |
| **Amostra** | 12 software managers [7] |
| **Contexto** | Industry (Mixed): Three Brazilian software organizations (two public, one private foundation) in Manaus [5, 8, 9] |
| **Modo de trabalho** | Not specified [9] |
| **Metodologia** | Mixed (Prescriptive and Agile) [10] |

---

## Objetivo

O objetivo principal deste estudo é entender a percepção dos gerentes de projeto em relação à **productivity** dos desenvolvedores [4]. A pesquisa busca investigar como esses profissionais compreendem e julgam intuitivamente a produtividade, especialmente em contextos onde métricas objetivas não estão disponíveis ou não são confiáveis [11, 12].

---

## Questoes de Pesquisa

*   **RQ1:** What is developer’s productivity according to software managers? [13]
*   **RQ2:** How do software managers identify the developer’s productivity? [13]

---

## Metricas e Instrumentos de Avaliacao

O estudo foca em percepções subjetivas, mas menciona métricas tradicionais identificadas na literatura.

| Metrica | Categoria | Nivel | Como Coletada | Validada |
|---------|-----------|-------|---------------|----------|
| Source Lines of Code (SLOC)/time | Activity | Individual | Literature Review (Referenced) [14] | No (Subject of study) |
| Tasks Completed/time | Delivery | Individual | Literature Review (Referenced) [14] | No (Subject of study) |
| Tasks delivered on time | Productivity | Individual | Perceptual (Interviews) [15] | Yes (Qualitatively) [16] |
| Need for rework | Quality | Individual | Perceptual (Interviews) [17] | Yes (Qualitatively) [16] |
| Meeting stakeholder expectations | Satisfaction | Individual | Perceptual (Interviews) [18] | Yes (Qualitatively) [16] |

---

## Frameworks e Metricas

### Frameworks Referenciados
*   **Grounded Theory (GT):** REFERENCED (procedimentos de **open coding** e **axial coding** aplicados na análise qualitativa) [6, 19].
*   **Case Study Guidelines (Runeson et al.):** REFERENCED (usado para condução do estudo de caso e transcrições) [5, 20].

### Frameworks Propostos
O artigo não propõe um framework formal, mas apresenta um modelo conceitual onde a percepção de produtividade é formada por quatro pilares: **timely delivery**, **quality (no rework)**, **stakeholder satisfaction** e **behavioral factors** [21, 22].

---

## Fatores que Influenciam Produtividade

### Fatores Positivos
| Fator | Categoria |
|-------|-----------|
| Technical qualification [23] | Human |
| Focus and commitment [24] | Human |
| Proactivity [25] | Human |
| Ability to handle high complexity tasks [26] | Technical |
| Team feedback/Role modeling [27, 28] | Organizational |

### Fatores Negativos
| Fator | Categoria |
|-------|-----------|
| Need for rework [17] | Process |
| Task delays [29] | Process |
| Stakeholder dissatisfaction [29] | Organizational |
| Lack of focus/commitment [25] | Human |

---

## Papel da IA e Automacao

| Campo | Valor |
|-------|-------|
| Usa IA/ML? | No |
| Automacao de coleta? | No (coleta manual via entrevistas) [10] |
| Impacto de IA na produtividade? | Not mentioned |

---

## Resultados Principais

*   A percepção dos gerentes sobre produtividade é influenciada por quatro fatores principais: (1) tarefas entregues no prazo, (2) ausência de **rework**, (3) produtos que atendem às expectativas dos **stakeholders** e (4) comportamento pessoal (foco e proatividade) [21, 22].
*   A **complexity** da tarefa atua como um moderador: desenvolvedores que concluem tarefas mais complexas são vistos como mais produtivos [26].
*   Gerentes utilizam o histórico de entregas sem **rework** como uma métrica de produtividade subjetiva e intuitiva [30, 31].
*   Fatores humanos e comportamentais (como compromisso) são tão importantes para a percepção do gerente quanto a saída técnica [25, 32].
*   A confiança do gerente no desenvolvedor permite delegar tarefas sem receio dos resultados, baseando-se na percepção de produtividade construída [28].

---

## Desafios do Uso das Metricas

*   **Subjectivity:** A gestão de capital humano é frequentemente baseada na percepção intuitiva dos gerentes em vez de dados quantitativos [4, 11].
*   **Metric Reliability:** Métricas objetivas podem ser inexistentes ou pouco confiáveis nas organizações [11].
*   **Context Bias:** Percepções podem ser enviesadas por crenças pessoais dos gerentes [33].

---

## Avaliacao de Qualidade Metodologica

| Criterio | Pontuacao (0-2) |
|----------|----------------|
| Objetivo claramente definido | 2 [4] |
| Metodologia adequada ao objetivo | 2 [5, 6] |
| Amostra/contexto descrito adequadamente | 2 [9, 34] |
| Ameacas a validade discutidas | 2 [33, 35, 36] |
| Resultados com evidencia suficiente | 2 [15, 16] |
| Contribuicao clara para pratica ou teoria | 2 [12, 37] |
| **TOTAL** | **12/12** |

---

## Limitacoes

*   **Generalização:** Os resultados são limitados a três organizações de uma região específica do Brasil (Manaus) [35].
*   **Bias:** Possível viés dos entrevistados baseado em suas próprias crenças e viés do pesquisador durante a coleta e análise de dados [33].
*   **Natureza Qualitativa:** O estudo não utiliza argumentos estatísticos para generalização [35].

---

## Contribuicao Principal

A principal contribuição deste trabalho é deslocar o foco do estudo da produtividade da auto-percepção do desenvolvedor para a **perspective of software managers** [12, 38]. O estudo revela que, na prática, os gerentes utilizam as "entregas no prazo sem necessidade de retrabalho" como a métrica subjetiva central para avaliar o desempenho, destacando o papel crítico que os **human factors** desempenham na visão organizacional de produtividade [30, 31].

---

*Extraido via NotebookLM em March 2026 para MLR: Software Developer Metrics in Practice*
# Software Project Managers’ Perceptions of Productivity Factors: Findings from a Qualitative Study

**Decisao: INCLUIDO | Qualidade: 5/5**

---

## Dados Bibliograficos

| Campo | Valor |
|-------|-------|
| **ID** | P1475 |
| **Autores** | Edson Oliveira, Tayana Conte, Marco Cristo, Emilia Mendes [1, 2] |
| **Ano** | 2016 [3] |
| **Venue** | ESEM '16: Proceedings of the 10th ACM/IEEE International Symposium on Empirical Software Engineering and Measurement [3] |
| **DOI** | http://dx.doi.org/10.1145/2961111.2962626 [3, 4] |
| **Tipo** | Conference paper [3] |
| **Metodo** | Qualitative (exploratory Case study) using semi-structured interviews and Grounded Theory procedures [5-8] |
| **Amostra** | 12 software managers [5, 9] |
| **Contexto** | Industry (Three organizations in Manaus, Brazil: two public and one non-profit private foundation) [5, 7, 10, 11] |
| **Modo de trabalho** | Not specified [11] |
| **Metodologia** | Mixed (Prescriptive and Agile) [11, 12] |

---

## Objetivo

O objetivo principal deste estudo é entender a percepção de gerentes de projeto em relação à produtividade dos desenvolvedores de software [5]. A pesquisa busca investigar como esses gestores compreendem e julgam intuitivamente a produtividade, especialmente em contextos onde métricas objetivas podem não estar disponíveis ou não ser confiáveis [6, 13, 14].

---

## Questoes de Pesquisa

*   **RQ1:** What is developer’s productivity according to software managers? [14]
*   **RQ2:** How do software managers identify the developer’s productivity? [7, 14]

---

## Metricas e Instrumentos de Avaliacao

O estudo foca em fatores perceptuais que funcionam como métricas subjetivas para os gestores [15, 16].

| Metrica | Categoria | Nivel | Como Coletada | Validada |
|---------|-----------|-------|---------------|----------|
| Tasks delivered on time | Delivery | Individual | Perceptual/Historical [17, 18] | No [15] |
| Artifacts with no need for rework | Quality | Individual | Perceptual/Review [19, 20] | No [15] |
| Meeting stakeholders’ expectations | Satisfaction | Individual | Feedback/Customer satisfaction [21, 22] | No [15] |
| Personal behavior (focus, proactivity) | Human | Individual | Observation/Team feedback [23-25] | No [15] |
| SLOC/time | Activity | Individual | Referenced from literature [26] | N/A |
| Tasks Completed/time | Delivery | Individual | Referenced from literature [26] | N/A |

---

## Frameworks e Metricas

### Frameworks Referenciados
- **ISO/IEEE Software Engineering Standards**: REFERENCED (Discutido no contexto de harmonização de métricas) [27].
- **Grounded Theory (GT)**: APPLIED (Procedimentos de codificação aberta e axial utilizados para análise de dados) [8, 28].

### Frameworks Propostos
O artigo não propõe um framework formal, mas identifica um modelo de quatro fatores (entregas no prazo, ausência de retrabalho, expectativas dos stakeholders e comportamento pessoal) que influenciam a percepção da produtividade [29, 30].

---

## Fatores que Influenciam Produtividade

### Fatores Positivos
| Fator | Categoria |
|-------|-----------|
| Technical qualification | Human [25, 31] |
| Focus and Commitment | Human [23, 25] |
| Proactivity | Human [24, 29] |
| Tasks delivered on time | Process [17, 18] |
| No need for rework | Process/Quality [19, 20] |

### Fatores Negativos
| Fator | Categoria |
|-------|-----------|
| Task delays | Process [22] |
| Need for excessive rework | Process/Quality [16, 19, 20] |
| Lack of focus or commitment | Human [24, 25] |
| Dissatisfied stakeholders | Quality [22] |

---

## Papel da IA e Automacao

| Campo | Valor |
|-------|-------|
| Usa IA/ML? | No — O estudo é focado em percepções humanas qualitativas [5, 6]. |
| Automacao de coleta? | No — Os dados foram coletados via entrevistas semiestruturadas [12]. |
| Impacto de IA na produtividade? | Not mentioned. |

---

## Resultados Principais

*   A percepção dos gerentes sobre produtividade é influenciada por quatro fatores principais: tarefas entregues no prazo, ausência de retrabalho, atendimento às expectativas dos stakeholders e comportamento pessoal (foco e proatividade) [29, 30].
*   A **complexidade da tarefa** é o único fator mencionado capaz de moderar a percepção da produtividade (tarefas mais complexas finalizadas indicam maior produtividade) [21, 32].
*   Gestores constroem sua confiança em desenvolvedores produtivos baseando-se no histórico de entregas sem falhas [15, 33].
*   O feedback da equipe e dos líderes de time é fundamental para formar a imagem mental da produtividade de cada desenvolvedor [34, 35].
*   Fatores humanos e comportamentais desempenham um papel muito mais central na percepção prática da produtividade do que a literatura tradicional de engenharia de software sugere [25, 29, 36].

---

## Desafios do Uso das Metricas

*   **Subjetividade:** Gestores frequentemente usam métricas intuitivas e subjetivas em vez de medidas objetivas [15, 16].
*   **Viés de Comportamento:** A percepção de produtividade pode ser influenciada por atitudes não técnicas, como "ficar calmo" ou "comprometimento", que podem não refletir o output real [23, 24].
*   **Dependência de Feedback:** A avaliação depende fortemente da comunicação entre líderes de equipe e gerentes de nível superior [34, 35].

---

## Avaliacao de Qualidade Metodologica

| Criterio | Pontuacao (0-2) |
|----------|----------------|
| Objetivo claramente definido | 2 [5, 6] |
| Metodologia adequada ao objetivo | 2 [7, 8] |
| Amostra/contexto descrito adequadamente | 2 [9, 11, 37] |
| Ameacas a validade discutidas | 2 [38-40] |
| Resultados com evidencia suficiente | 2 [17, 19-21, 23, 24, 31, 32, 34, 41] |
| Contribuicao clara para pratica ou teoria | 2 [29, 36] |
| **TOTAL** | **12/12** |

---

## Limitacoes

*   **Generalização:** Os resultados baseiam-se em apenas três organizações em uma região específica do Brasil (Manaus), o que pode não representar todos os contextos [38].
*   **Viés dos Entrevistados:** As percepções podem ser baseadas em crenças pessoais que podem causar distorções da realidade [38, 39].
*   **Viés do Pesquisador:** A interpretação dos dados qualitativos pode ter sido influenciada pelos autores (mitigado por revisões por pares) [39, 40].

---

## Contribuicao Principal

O estudo contribui ao demonstrar que, na prática, a produtividade de desenvolvedores de software é percebida pelos gestores como um conceito multidimensional que vai além do rácio entre "output e input" [29, 36]. A principal contribuição é a identificação de que **fatores humanos** (comportamento, compromisso) e **qualidade subjetiva** (ausência de retrabalho e satisfação do cliente) são métricas intuitivas tão ou mais importantes que a velocidade de entrega para o gerenciamento de capital humano em software [15, 25, 29].

---

*Extraido via NotebookLM em March 2026 para MLR: Software Developer Metrics in Practice*
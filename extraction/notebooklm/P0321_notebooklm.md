# P0321 — Characterizing Software Developers by Perceptions of Productivity

**Decisao: INCLUIDO | Qualidade: 5/5**

---

## Dados Bibliograficos

| Campo | Valor |
|-------|-------|
| **ID** | P0321 |
| **Autores** | André N. Meyer, Thomas Zimmermann, Thomas Fritz [1] |
| **Ano** | 2017 [2, 3] |
| **Venue** | ACM/IEEE International Symposium on Empirical Software Engineering and Measurement (ESEM) [2] |
| **DOI** | 10.5281/zenodo.837228 (Supplementary material) [4] |
| **Tipo** | Conference paper [2] |
| **Metodo** | Survey e Cluster analysis [5, 6] |
| **Amostra** | 413 professional software developers [1, 4] |
| **Contexto** | Industry (Microsoft) [1, 2] |
| **Modo de trabalho** | Not specified [7] |
| **Metodologia** | Not specified [7] |

---

## Objetivo

O objetivo principal deste trabalho é explorar as características das percepções de produtividade dos desenvolvedores e identificar grupos (clusters) de desenvolvedores que compartilham percepções semelhantes [5]. Os autores buscam entender a variação e as características comuns nessas percepções para fornecer suporte melhor e mais personalizado aos desenvolvedores por meio de ferramentas e práticas de trabalho [5, 8].

---

## Questoes de Pesquisa

O artigo não lista questões de pesquisa prefixadas com "RQ", mas define o escopo da investigação em torno de:
- Quais são as características das percepções de produtividade dos desenvolvedores? [5]
- Existem grupos de desenvolvedores com percepções de produtividade semelhantes? [5]
- Como esses grupos podem ser caracterizados com base em fatores que influenciam a produtividade e métricas de interesse? [5, 6]

---

## Metricas e Instrumentos de Avaliacao

| Metrica | Categoria | Nivel | Como Coletada | Validada |
|---------|-----------|-------|---------------|----------|
| Time spent coding | Activity | Individual | Survey (Self-report interest) [9, 10] | No [6, 11] |
| Longest period focused on a task without interruption | Activity | Individual | Survey (Self-report interest) [10] | No [6, 11] |
| Number of interruptions | Activity | Individual | Survey (Self-report interest) [3, 12] | No [6, 11] |
| Duration of each interruption | Activity | Individual | Survey (Self-report interest) [3] | No [6, 11] |
| Tasks worked on | Activity | Individual | Survey (Self-report interest) [10] | No [6, 11] |
| Number of emails sent/received | Activity | Individual | Survey (Self-report interest) [9, 13] | No [6, 11] |
| Number of open application windows | Activity | Individual | Survey (Self-report interest) [10] | No [6, 11] |
| Inbox size | Activity | Individual | Survey (Self-report interest) [10] | No [6, 11] |
| Websites visited the most | Activity | Individual | Survey (Self-report interest) [14, 15] | No [6, 11] |
| List of applications used | Activity | Individual | Survey (Self-report interest) [14, 15] | No [6, 11] |

---

## Frameworks e Metricas

### Frameworks Referenciados
- **Big Five personality traits (OCEAN)**: REFERENCED (usado como analogia para o conceito de "productivity traits") [16].

### Frameworks Propostos
O artigo propõe um conjunto inicial de seis **"productivity traits"** ou categorias de desenvolvedores baseadas em suas percepções de produtividade: Social, Lone, Focused, Balanced, Leading, e Goal-oriented developers [6, 16].

---

## Fatores que Influenciam Produtividade

### Fatores Positivos
| Fator | Categoria |
|-------|-----------|
| Writing code | Technical [17] |
| Solving problems / Fixing bugs | Technical [3] |
| Helping coworkers / Collaborating | Human/Social [3] |
| Code reviews | Process [3] |
| Being happy | Human [17] |
| Fewer interruptions | Organizational [17] |
| Clear goals / Making progress | Process [18] |

### Fatores Negativos
| Fator | Categoria |
|-------|-----------|
| Meetings (sem objetivo ou em excesso) | Process [17, 19] |
| Interruptions / Background noise | Organizational [3, 15] |
| Fragmentation of work / Multitasking | Process [18, 19] |
| Email (alto volume) | Technical/Process [3] |
| Unclear or irrelevant tasks | Process [12] |
| Broken builds / Blocking tasks | Technical/Process [18] |

---

## Papel da IA e Automacao

| Campo | Valor |
|-------|-------|
| Usa IA/ML? | No [2, 6] |
| Automacao de coleta? | No (estudo baseado em survey manual) [2] |
| Impacto de IA na produtividade? | Not discussed in this paper. |

---

## Resultados Principais

- Identificação de **seis clusters** distintos de desenvolvedores: Social (15%), Lone (15.5%), Focused (13%), Balanced (12.1%), Leading (23.5%), e Goal-oriented (9.2%) [6, 13, 15, 20-24].
- A maioria dos desenvolvedores se sente produtiva ao **escrever código** (exceto o cluster "Leading") e em dias com **poucas reuniões** e **poucas interrupções** [17].
- O cluster **Social** valoriza ajudar colegas e revisões de código, enquanto o **Lone** prefere trabalhar sozinho em problemas técnicos sem ruído ou interrupções [3].
- Desenvolvedores **Focused** priorizam eficiência e concentração em uma única tarefa, enquanto **Goal-oriented** focam no progresso e conclusão das tarefas [12, 14, 18].
- Os resultados sugerem que intervenções para melhorar a produtividade (como design de escritórios ou ferramentas) devem ser **personalizadas** de acordo com o perfil do desenvolvedor [25, 26].

---

## Desafios do Uso das Metricas

- **Percepções variadas**: A produtividade significa coisas diferentes para desenvolvedores diferentes, tornando métricas "tamanho único" ineficazes [8, 25].
- **Fatores subjetivos**: Muitos elementos que impactam a produtividade (como felicidade ou sensação de progresso) não são capturados por métricas de repositório tradicionais [8, 9, 27].
- **Viés de resposta**: Tendências pessoais de serem mais positivos ou negativos em pesquisas podem distorcer os dados de medição subjetiva [28].

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

- **Generalização**: O estudo foi realizado apenas com desenvolvedores de uma única empresa (Microsoft) [29].
- **Seleção de questões**: As perguntas da pesquisa podem não ter capturado todas as dimensões possíveis da produtividade [11].
- **Escolha do algoritmo**: O uso de algoritmos de clustering específicos e a decisão de usar certas perguntas para descrever os clusters podem ter influenciado os resultados finais [11].

---

## Contribuicao Principal

O trabalho fornece um primeiro passo exploratório na identificação de **categorias comuns de percepções de produtividade** entre desenvolvedores profissionais [30]. Ao agrupar desenvolvedores em seis perfis distintos, o estudo oferece uma base teórica para o desenvolvimento de ferramentas de suporte personalizadas e para a otimização do fluxo de trabalho tanto em nível individual quanto de equipe, reconhecendo que os desenvolvedores não são um grupo homogêneo em seus hábitos e preferências de trabalho [1, 16, 25].

---

*Extraido via NotebookLM em March 2026 para MLR: Software Developer Metrics in Practice*
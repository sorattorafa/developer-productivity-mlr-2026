# P0611 — How does working from home affect developer productivity? — A case study of Baidu during the COVID-19 pandemic

**Decisao: INCLUIDO | Qualidade: 5/5**

---

## Dados Bibliograficos

| Campo | Valor |
|-------|-------|
| **ID** | P0611 |
| **Autores** | Lingfeng Bao, Tao Li, Xin Xia, Kaiyu Zhu, Hui Li, Xiaohu Yang |
| **Ano** | 2022 |
| **Venue** | Science China Information Sciences |
| **DOI** | https://doi.org/10.1007/s11432-020-3278-4 |
| **Tipo** | Journal article |
| **Metodo** | Mixed methods (Quantitative analysis of developer activities and Qualitative survey) |
| **Amostra** | 139 developers, 8 projects, 2428 daily activity records |
| **Contexto** | Industry — Baidu Inc. (China) |
| **Modo de trabalho** | Remote (Working from home) vs. On-site |
| **Metodologia** | Not specified |

---

## Objetivo

O objetivo principal do estudo é realizar uma **análise quantitativa** para investigar a diferença na **produtividade dos desenvolvedores** entre o trabalho remoto (Working from home - WFH) e o trabalho presencial (onsite) [1]. A pesquisa utiliza um conjunto de dados de atividades diárias de desenvolvedores da Baidu Inc. coletados durante a pandemia de COVID-19 para entender os impactos e os motivos por trás das variações de produtividade [1, 2].

---

## Questoes de Pesquisa

*   **RQ1:** Existem diferenças significativas na produtividade do desenvolvedor entre trabalhar em casa e trabalhar no local? [3]
*   **RQ2:** Diferentes linguagens de programação afetam a produtividade do desenvolvedor ao trabalhar em casa? [4]
*   **RQ3:** Diferentes tipos de projeto afetam a produtividade do desenvolvedor ao trabalhar em casa? [5]
*   **RQ4:** Diferentes idades de projeto afetam a produtividade do desenvolvedor ao trabalhar em casa? [6]
*   **RQ5:** Diferentes tamanhos de projeto afetam a produtividade do desenvolvedor ao trabalhar em casa? [7]
*   **RQ6:** Desenvolvedores individuais têm produtividades diferentes ao trabalhar em casa? [8]

---

## Metricas e Instrumentos de Avaliacao

| Metrica | Categoria | Nivel | Como Coletada | Validada |
|---------|-----------|-------|---------------|----------|
| **commit count** | Productivity/Activity | Individual | Daily activity logs (Repository mining) | Partial [9, 10] |
| **line inserted** | Productivity/Activity | Individual | Daily activity logs (Repository mining) | Partial [9, 10] |
| **line deleted** | Productivity/Activity | Individual | Daily activity logs (Repository mining) | Partial [9, 10] |
| **review count** | Collaboration/Activity | Individual | Daily activity logs (Code review system) | Partial [9, 11] |
| **build count** | Activity | Individual | CI system logs | No [9, 12] |
| **release count** | Delivery/Activity | Individual | Release system logs | No [9, 12] |
| **compile count** | Activity | Individual | Development tool logs | No [9, 12] |
| **job status build** | Quality | Individual | Success rate in CI logs | No [13] |
| **job status release** | Quality/Delivery | Individual | Success rate in release logs | No [13] |

---

## Frameworks e Metricas

### Frameworks Referenciados
*   **LOC (Lines of Code):** REFERENCED (discutido como métrica comum, embora controversa) [9, 14].
*   **Function Points:** REFERENCED (citado como métrica de produtividade em trabalhos relacionados) [14].
*   **Socio-technical congruence:** REFERENCED (citado como framework para avaliar impacto de dependências na produtividade) [15].

### Frameworks Propostos
O artigo não propõe um novo framework formal, mas utiliza um conjunto de **métricas agregadas** (mean, median, sum, max, min) para comparar distribuições de produtividade [16, 17].

---

## Fatores que Influenciam Produtividade

### Fatores Positivos
| Fator | Categoria |
|-------|-----------|
| Foco (sem interrupções de colegas) | Human/Process [18] |
| Economia de tempo e custo de transporte | Human/Organizational [18] |
| Melhor equilíbrio entre vida pessoal e profissional (Work-life balance) | Human [19] |
| Flexibilidade de horário (trabalho cedo ou tarde da noite) | Process [18, 19] |
| Relatórios diários (Daily reports) aumentando a disciplina | Process [18] |

### Fatores Negativos
| Fator | Categoria |
|-------|-----------|
| Interrupções domésticas (filhos, pets, cozinhar) | Human/Environment [19] |
| Falta de autodisciplina em ambiente relaxado | Human [19] |
| Redução na eficiência de colaboração e comunicação | Process [19, 20] |
| Necessidade de acesso remoto a máquinas potentes (especialmente em C++) | Technical [4] |
| Complexidade de coordenação em projetos grandes ou novos | Organizational/Process [21, 22] |

---

## Papel da IA e Automacao

| Campo | Valor |
|-------|-------|
| Usa IA/ML? | No — O estudo utiliza testes estatísticos (Wilcoxon) e Cliff's delta [23]. |
| Automacao de coleta? | Yes — Os dados foram extraídos automaticamente dos logs de atividade da empresa [9, 24]. |
| Impacto de IA na produtividade? | N/A — O estudo não avalia o impacto de ferramentas de IA na produtividade. |

---

## Resultados Principais

*   **Impactos Variados:** O trabalho remoto (WFH) tem impactos positivos e negativos dependendo da métrica; por exemplo, houve redução significativa no somatório de compilações e linhas inseridas/deletadas [25].
*   **Sucesso de Releases:** A taxa de sucesso de *releases* caiu significativamente durante o WFH ($p=0.002$), sugerindo que atividades que exigem mais colaboração são mais afetadas [25].
*   **Linguagens de Programação:** Projetos em **Java** sofreram mais impactos negativos que projetos em **C++** [26, 27].
*   **Características do Projeto:** Projetos grandes, projetos mais novos (criados em 2018) e tipos como SDK/SERVER apresentaram quedas de produtividade mais acentuadas que projetos pequenos, antigos ou do tipo APP [21, 22, 28].
*   **Individualidade:** Para a maioria dos desenvolvedores (**84.8%**), a produtividade no WFH foi similar à presencial; apenas uma pequena parcela teve mudanças significativas (positivas ou negativas) [29, 30].

---

## Desafios do Uso das Metricas

*   **Privacidade e Segurança:** Necessidade de **padronizar (standardize)** os valores numéricos (z-score), impedindo a análise de valores absolutos reais [10, 13].
*   **Validade da Métrica:** O uso de métricas como "linhas de código" é reconhecido como limitado por depender de experiência e estilo de programação [9, 10].
*   **Fatores de Confusão:** Dificuldade em isolar outros fatores, como mudanças na carga de trabalho durante o período da pandemia [10].

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

*   **Generalização:** Os dados provêm de apenas uma empresa (Baidu), o que pode não representar toda a indústria [11].
*   **Tamanho da Amostra:** O estudo analisou apenas 8 projetos e 139 desenvolvedores [11].
*   **Métricas Limitadas:** Foco em métricas quantitativas de atividade, sem considerar fatores subjetivos como humor ou ambiente doméstico detalhado na parte quantitativa [10, 31].

---

## Contribuicao Principal

A principal contribuição deste trabalho é ser o primeiro a investigar o impacto do trabalho remoto (WFH) na produtividade de desenvolvedores de software de forma quantitativa, baseando-se em **atividades diárias reais** em vez de apenas percepções [32, 33]. O estudo demonstra que o WFH não é universalmente positivo ou negativo, mas que sua eficácia depende fortemente de características do projeto (tamanho, idade, tecnologia) e do perfil individual do desenvolvedor, oferecendo subsídios para que empresas adotem políticas híbridas ou remotas personalizadas [34, 35].

---

*Extraido via NotebookLM em March 2026 para MLR: Software Developer Metrics in Practice*
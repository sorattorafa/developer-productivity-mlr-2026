# G067 — Measuring the impact of early-2025 AI on experienced open-source developer productivity

**Decisao: INCLUIDO | Qualidade GL: 6/6**

---

## Dados Bibliograficos

| Campo | Valor |
|-------|-------|
| **ID** | G067 |
| **Autor/Organizacao** | Joel Becker, Nate Rush, Beth Barnes, David Rein / Model Evaluation & Threat Research (METR) |
| **Data** | 2025 |
| **Tipo** | Technical Report / White Paper |
| **URL** | Not provided in excerpt |

---

## Resumo

Este estudo detalha um **randomized controlled trial (RCT)** conduzido entre fevereiro e junho de 2025 para medir o impacto de ferramentas de IA de fronteira na produtividade de 16 desenvolvedores experientes de **open-source** [1]. Os participantes, que possuíam em média 5 anos de experiência nos repositórios testados, completaram 246 tarefas reais (como bug reports e feature requests) em projetos maduros [1-3]. As tarefas foram distribuídas aleatoriamente entre condições que permitiam ou proibiam o uso de ferramentas como **Cursor Pro** e **Claude 3.5/3.7 Sonnet** [2, 4].

Os resultados revelaram uma desconexão significativa entre a percepção e a realidade: enquanto especialistas e os próprios desenvolvedores previam ganhos de produtividade de 20% a 39%, o uso de IA na verdade **aumentou o tempo de conclusão das tarefas em 19%** [1, 5, 6]. Esta lentidão foi atribuída a fatores como a baixa confiabilidade das gerações de IA (taxa de aceitação <44%), a complexidade inerente de grandes repositórios legados e a incapacidade da IA em acessar o **implicit repository context** dominado pelos mantenedores experientes [7-10].

---

## Frameworks Mencionados

*   **Agrawal et al. Framework**: Citado para tratar a IA como uma queda no custo de **prediction** e analisar consequências distributivas baseadas em experiência [11].
*   **DORA / SPACE / DevEx**: Não mencionados explicitamente nas fontes fornecidas.

---

## Metricas Mencionadas

*   **Completion time (S)**: Medida primária definida como a mudança percentual no tempo de conclusão de uma tarefa devido ao uso de IA [12, 13].
*   **Forecasted Speedup**: Estimativas ex-ante de desenvolvedores e especialistas sobre a redução de tempo esperada [5, 14, 15].
*   **Acceptance Rate**: Porcentagem de linhas de código sugeridas pela IA que foram aceitas pelos desenvolvedores (registrada em <44%) [8, 16].
*   **Activity Labels (Screen Recording)**: Decomposição do tempo em categorias como **Reviewing AI output** (9% do tempo), **Prompting AI** (8%), **Waiting on AI** (4%), **Active coding**, **Reading/searching**, e **Idle** [17-20].
*   **Prior Task Exposure & External Resource Needs**: Escalas ordinais (1-5 e 1-3) usadas para quantificar a familiaridade do desenvolvedor com a tarefa e a dependência de documentação externa [21, 22].
*   **Lines of Code (LOC)**: Mencionada como uma métrica de saída, mas criticada por não capturar produtividade real (visto que a IA pode gerar código verboso e funcionalmente equivalente) [23-25].

---

## Insights para Praticantes

*   **Over-optimism**: Desenvolvedores experientes tendem a superestimar a ajuda da IA mesmo após o uso, mantendo uma percepção de "ganho" (estimado por eles em 20%) enquanto os dados mostram perda real de tempo (19%) [5, 26].
*   **Expertise Paradox**: A IA é menos eficaz em tarefas onde o desenvolvedor já possui alta senioridade e baixo uso de recursos externos; o benefício parece maior em tarefas de baixa exposição prévia (**unfamiliar issues**) [22, 27, 28].
*   **AI Reliability & Cleaning**: Em repositórios de alta qualidade, os desenvolvedores gastam cerca de 9% do seu tempo revisando ou limpando o código da IA para atingir os padrões do projeto [8, 29].
*   **Complexity Barrier**: O desempenho da IA degrada em ambientes com grandes bases de código (ex: >1.000.000 linhas) e arquivos extensos, onde as ferramentas podem introduzir erros ou fazer alterações irrelevantes [9, 30].
*   **Implicit Context**: Modelos de IA frequentemente falham por não possuírem o conhecimento tácito sobre decisões de design e dados específicos que mantenedores experientes utilizam intuitivamente [10].

---

## Avaliacao de Qualidade GL (Garousi et al.)

| Criterio | Pontuacao (0-1) |
|----------|----------------|
| Autoridade do autor/organizacao | 1 |
| Descricao de metodologia | 1 |
| Data de publicacao | 1 |
| Objetividade (vies comercial) | 1 |
| Referencias citadas | 1 |
| Contribuicao nova | 1 |
| **TOTAL** | **6/6** |

---

*Extraido via NotebookLM em March 2026 para MLR: Software Developer Metrics in Practice*
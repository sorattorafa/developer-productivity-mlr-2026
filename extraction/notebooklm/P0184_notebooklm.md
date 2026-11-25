# P0184 — How developers feel about tools: an investigation on software startup professionals experience with virtual kanban boards

**Decisao: INCLUIDO | Qualidade: 5/5**

---

## Dados Bibliograficos

| Campo | Valor |
|-------|-------|
| **ID** | P0184 |
| **Autores** | Crismerlyn Pereira, Angelica Santos, Leticia Machado, Luciana Zaina [1] |
| **Ano** | 2022 [2] |
| **Venue** | 15th International Conference on Cooperative and Human Aspects of Software Engineering (CHASE’22) [2, 3] |
| **DOI** | https://doi.org/10.1145/3528579.3529172 [2, 3] |
| **Tipo** | Conference paper [2] |
| **Metodo** | Qualitative study (Semi-structured interviews) [4, 5] |
| **Amostra** | 10 software startup professionals from 6 different Brazilian startups [5-7] |
| **Contexto** | Industry (Software startups in Brazil across Digital Tech, Edutech, Proptech, and Fintech segments) [4, 8, 9] |
| **Modo de trabalho** | Remote (due to COVID-19 pandemic) [10, 11] |
| **Metodologia** | Agile (Scrum and/or Kanban) [8, 9, 12] |

---

## Objetivo

O principal objetivo do artigo é entender como os profissionais de **software startups** vivenciam o uso de **virtual kanban boards** em suas atividades diárias, analisando dados qualitativos sob a perspectiva do framework de **Developer Experience (DX)** [4, 13, 14].

---

## Questoes de Pesquisa

*   **RQ1:** How do software startups professionals experience the use of virtual kanban boards in their daily activities? [6, 14, 15].

---

## Metricas e Instrumentos de Avaliacao

O estudo é primariamente qualitativo e utiliza o **Developer Experience (DX) framework** como principal instrumento para avaliar a percepção dos profissionais [6, 16].

| Metrica | Categoria | Nivel | Como Coletada | Validada |
|---------|-----------|-------|---------------|----------|
| **Work performance** (Self-evaluated) | Satisfaction/DevEx | Individual | Semi-structured Interview (Q25) | No [17] |
| **Task visibility** | DevEx/Collaboration | Team | Interview (Q15) | No [18, 19] |
| **Task predictability** | Productivity | Individual/Team | Qualitative Analysis | No [20] |
| **WIP (Work-in-progress) limits** | Activity | Team | Interview (Q16) | No [18, 21] |

---

## Frameworks e Metricas

### Frameworks Referenciados
*   **Developer Experience (DX) Framework (Fagerholm and Münch):** APPLIED — utilizado como lente teórica para análise de dados e mapeamento de perguntas de entrevista [4, 6, 22, 23].
*   **UX (User Experience):** REFERENCED — citado para contextualizar a origem do conceito de DX [24].
*   **Software Startup Themes (Paternoster et al.):** REFERENCED — utilizado para caracterizar as startups participantes e embasar as recomendações [25-27].

### Frameworks Propostos
O artigo não propõe um novo framework de medição, mas apresenta um conjunto de **8 Startup-Related Recommendations (SSR)** para otimizar o uso de quadros Kanban em startups [28-30].

---

## Fatores que Influenciam Produtividade

### Fatores Positivos
| Fator | Categoria |
|-------|-----------|
| **Task visibility** | Technical/Process [19, 31] |
| **Autonomy in task selection** | Human/Organizational [28, 32, 33] |
| **Integration with tools (Slack, GitHub)** | Technical [34, 35] |
| **Team collaboration and alignment** | Human/Process [36-38] |
| **Historical project data access** | Process [39, 40] |

### Fatores Negativos
| Fator | Categoria |
|-------|-----------|
| **Lack of tool training** | Human/Organizational [21, 41, 42] |
| **Information overload (Confusing boards)** | Process/Cognitive [35, 43] |
| **Lack of visual standardization (Labels/Rules)** | Process [11, 42, 44] |
| **Difficulty in bulk task management** | Technical/Process [45, 46] |
| **Pressure from complex/urgent tasks** | Human/Emotional [47] |

---

## Papel da IA e Automacao

| Campo | Valor |
|-------|-------|
| Usa IA/ML? | No [As fontes não mencionam o uso de IA ou ML no estudo ou na ferramenta] |
| Automacao de coleta? | Yes — O artigo menciona integração com GitHub para vincular tarefas automaticamente e atualização automática de datas e status ao mover cards no Jira [34, 35, 48] |
| Impacto de IA na produtividade? | N/A |

---

## Resultados Principais

*   Os participantes concordam que os quadros Kanban virtuais são **essenciais** para rastrear projetos e realizar o trabalho [13, 28, 49, 50].
*   O uso dos quadros estimula a **autonomia** dos profissionais nas atividades rotineiras [28, 51, 52].
*   A falta de conhecimento sobre as funcionalidades das ferramentas (devido à falta de treinamento formal) causa **frustração** [28, 41, 53].
*   A transparência do fluxo de trabalho aumenta a confiança dos desenvolvedores ao selecionar tarefas adequadas às suas habilidades [31, 54].
*   Foram geradas **8 recomendações (SSRs)** específicas para startups, como usar o quadro como repositório de documentação para mitigar a escassez de recursos [29, 55].

---

## Desafios do Uso das Metricas

O artigo identifica desafios práticos e comportamentais no uso da ferramenta que impactam a medição do progresso:
*   **Acordos verbais não registrados:** Decisões tomadas em reuniões que não são refletidas no quadro, prejudicando a consistência da informação [21, 35, 56].
*   **Sobrecarga cognitiva:** Quadros com excesso de informação ou múltiplos projetos simultâneos tornam a gestão caótica [35, 43].
*   **Resistência a tarefas complexas:** Profissionais sentem-se intimidados ao serem atribuídos a tarefas urgentes ou demoradas visíveis no quadro [47, 57].

---

## Avaliacao de Qualidade Metodologica

| Criterio | Pontuacao (0-2) |
|----------|----------------|
| Objetivo claramente definido | 2 [4, 14] |
| Metodologia adequada ao objetivo | 2 [4, 16] |
| Amostra/contexto descrito adequadamente | 2 [8, 9] |
| Ameacas a validade discutidas | 2 [58-60] |
| Resultados com evidencia suficiente | 2 [61, 62] |
| Contribuicao clara para pratica ou teoria | 2 [29, 30] |
| **TOTAL** | **12/12** |

---

## Limitacoes

*   **Tamanho da amostra:** 10 entrevistas é considerado um número moderado dada a diversidade de startups no Brasil [63, 64].
*   **Subjetividade:** A classificação dos dados nas dimensões de DX depende da interpretação dos pesquisadores (embora mitigada por rodadas de consenso) [59, 60].
*   **Contexto Geográfico:** O estudo focou exclusivamente em startups brasileiras [4, 64].
*   **Diversidade de Ferramentas:** Diferentes ferramentas possuem funcionalidades distintas que não foram analisadas de forma cruzada em profundidade [64, 65].

---

## Contribuicao Principal

A principal contribuição é uma investigação profunda da experiência do desenvolvedor em startups com ferramentas de gestão visual, culminando em um conjunto de **recomendações práticas (SSRs)** que conectam as dimensões de DX (cognição, conação e afeto) às características intrínsecas de startups, visando melhorar a produtividade e a satisfação em ambientes de alta incerteza e recursos limitados [28, 30, 52, 66].

---

*Extraido via NotebookLM em March 2026 para MLR: Software Developer Metrics in Practice*
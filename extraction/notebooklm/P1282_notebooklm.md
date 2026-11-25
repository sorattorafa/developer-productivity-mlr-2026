# P1282 — Fostering Software Developer Productivity through Awareness Increase and Goal-Setting

**Decisao: INCLUIDO | Qualidade: 5/5**

---

## Dados Bibliograficos

| Campo | Valor |
|-------|-------|
| **ID** | P1282 |
| **Autores** | André N. Meyer |
| **Ano** | 2019 |
| **Venue** | University of Zurich (Dissertation) |
| **DOI** | https://doi.org/10.5167/uzh-174312 |
| **Tipo** | Dissertation (PhD Thesis) |
| **Metodo** | Mixed methods (Field studies, surveys, observations, automated monitoring, machine learning) |
| **Amostra** | ~7000 participações totais (incluindo 5971 respostas de survey e múltiplos grupos de 20-449 profissionais) |
| **Contexto** | Industry (17 empresas, desde startups a multinacionais, em 12 países) |
| **Modo de trabalho** | On-site (contexto de escritório) e Work from home (como condição atípica) |
| **Metodologia** | Agile (Scrum mencionado em contextos de equipes estudadas) |

---

## Objetivo

O objetivo principal da pesquisa é fomentar a produtividade de desenvolvedores de software através do aumento da conscientização (awareness) sobre seus próprios hábitos de trabalho [1, 2]. A tese busca primeiro entender a produtividade sob uma perspectiva "bottom-up" (percepção individual) para então desenvolver ferramentas e estratégias, como monitoramento pessoal e indicadores externos, que motivem mudanças de comportamento produtivas [3, 4].

---

## Questoes de Pesquisa

* **RQ1:** How does a software developer’s workday look like in terms of a) activities, b) tasks, c) work fragmentation, and d) perceived productivity? [5]
* **RQ2:** Can we foster productivity by increasing developers’ self-awareness about work and productivity through a) self-monitoring and b) reflective goal-setting? [6]
* **RQ3:** Can we foster productivity by increasing developers’ external awareness about work and productivity through modeling and externally indicating interruptibility? [6]

---

## Metricas e Instrumentos de Avaliacao

| Metrica | Categoria | Nivel | Como Coletada | Validada |
|---------|-----------|-------|---------------|----------|
| Perceived Productivity | Satisfaction | Individual | 7-point Likert scale (experience sampling pop-ups) | Yes |
| Computer interaction data | Activity | Individual | Mouse clicks, movements, and keystroke counts | Yes |
| Time spent in applications | Activity | Individual | Background monitoring (automated window title mapping) | Yes |
| Task switches | Activity/Fragmentation | Individual | Inferred via ML models from interaction data | Yes (87% accuracy) |
| Interruptibility | Collaboration | Individual | FlowLight sensing based on computer activity | Yes (71% accuracy) |
| Self-reported interruptions | Collaboration | Individual | Manual logging and survey responses | Yes |
| Task types | Activity | Individual | Manual coding of observations and self-reports | Yes |

---

## Frameworks e Metricas

### Frameworks Referenciados
* **Personal Software Process (PSP):** REFERENCED como base para autorreflexão em desenvolvimento [7].
* **Transtheoretical Model of Behavior Change (TTM):** REFERENCED para modelar estágios de mudança de hábito [8].
* **SMART goals:** APPLIED para estruturar metas específicas e mensuráveis dos desenvolvedores [9, 10].
* **Grounded Theory:** APPLIED na análise qualitativa dos dados de surveys e entrevistas [11, 12].
* **Big Five Personality Traits (OCEAN):** REFERENCED como comparação para "productivity traits" [13].

### Frameworks Propostos
* **PersonalAnalytics:** Um sistema de monitoramento pessoal no local de trabalho que combina rastreamento automático com amostragem de experiência (experience sampling) [14].
* **FlowLight:** Uma abordagem que combina um indicador físico (LED estilo semáforo) com medição automática de interruptibilidade [15].
* **Reflective Goal-Setting Framework:** Um processo estruturado para autorreflexão diária e definição de metas de hábitos de trabalho [16, 17].
* **Productivity Personas:** Seis perfis de desenvolvedores baseados em suas percepções de produtividade (Social, Lone, Focused, Balanced, Leading, Goal-oriented) [18].

---

## Fatores que Influenciam Produtividade

### Fatores Positivos
| Fator | Categoria |
|-------|-----------|
| Ability to work focused | Human/Process |
| Making progress on tasks | Process/Activity |
| Helping others (para o perfil "social") | Human/Collaboration |
| Learning new things | Human |
| Agency (control over workday) | Organizational |

### Fatores Negativos
| Fator | Categoria |
|-------|-----------|
| External interruptions | Collaboration/Human |
| Fragmented work | Process |
| Unplanned/Inefficient meetings | Process/Organizational |
| Infrastructure issues | Technical |
| Context switches | Process/Human |
| Administrative tasks | Process |

---

## Papel da IA e Automacao

| Campo | Valor |
|-------|-------|
| Usa IA/ML? | Yes — Random Forest para detecção automática de trocas de tarefas e tipos de tarefas [19]. |
| Automacao de coleta? | Yes — Coleta contínua de interação com janelas, mouse e teclado via PersonalAnalytics [14]. |
| Impacto de IA na produtividade? | Permite identificar contextos de tarefas e interruptibilidade em tempo real, reduzindo o esforço manual do desenvolvedor para gerenciar ferramentas de suporte [20, 21]. |

---

## Resultados Principais

* O trabalho dos desenvolvedores é altamente fragmentado: média de **6.0 trocas de tarefa por hora** e apenas 13.2 minutos dedicados a uma tarefa antes de trocar [19, 20].
* A produtividade é pessoal, mas segue padrões: desenvolvedores podem ser agrupados em pessoas "da manhã", "baixa no almoço" e "da tarde" [22].
* O uso da ferramenta **PersonalAnalytics gerou insights significativos para 82%** dos participantes [23].
* Autorreflexão proposital apoiou a identificação de metas em 83% e motivou mudanças de comportamento em 80% dos casos [23].
* O sistema **FlowLight reduziu interrupções externas em 46%** [24].
* Modelos de ML detectaram trocas de tarefas com **87% de acurácia** [19].

---

## Desafios do Uso das Metricas

* O uso de métricas top-down (como linhas de código) pode levar desenvolvedores a "game the system" (fraudar o sistema) ou distorcer incentivos [25, 26].
* Dificuldade de generalizar modelos de produtividade devido à natureza altamente individual das percepções dos desenvolvedores [27].
* Preocupações com privacidade ao coletar dados sensíveis de interação no computador (ex: títulos de janelas, conteúdos) [28].

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

* **Escopo da Coleta:** Os dados quantitativos focam quase exclusivamente no trabalho realizado no computador, perdendo atividades offline ou em outros dispositivos [29, 30].
* **Viés de Auto-seleção:** Voluntários para estudos de monitoramento podem ter predisposição maior para quantificação pessoal [31].
* **Recollection Bias:** Dependência de autorrelatos para a "ground truth" das tarefas, que pode ser imprecisa [32].
* **Curto Prazo:** Observou-se apenas mudanças de comportamento de curto prazo durante os períodos de estudo [33].

---

## Contribuicao Principal

A tese contribui com uma investigação profunda e em escala sobre a produtividade sob a ótica do desenvolvedor, entregando modelos validados para detecção de tarefas e ferramentas práticas (PersonalAnalytics e FlowLight) que comprovadamente aumentam a conscientização e reduzem custos de interrupção, promovendo um ambiente de trabalho mais focado e satisfatório [1, 34, 35].

---

*Extraido via NotebookLM em March 2026 para MLR: Software Developer Metrics in Practice*
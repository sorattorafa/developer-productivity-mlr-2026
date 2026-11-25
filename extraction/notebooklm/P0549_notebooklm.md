# P0549 — Productivity assessment of neural code completion

**Decisao: INCLUIDO | Qualidade: 5/5**

---

## Dados Bibliograficos

| Campo | Valor |
|-------|-------|
| **ID** | P0549 |
| **Autores** | Albert Ziegler, Eirini Kalliamvakou, X. Alice Li, Andrew Rice, Devon Rifkin, Shawn Simister, Ganesh Sittampalam, Edward Aftandilian |
| **Ano** | 2022 |
| **Venue** | 6th ACM SIGPLAN International Symposium on Machine Programming (MAPS ’22) |
| **DOI** | 10.1145/3520312.3534864 |
| **Tipo** | Conference paper |
| **Metodo** | Mixed methods (Case study, Survey, Quantitative telemetry analysis) |
| **Amostra** | 2.631 respostas de pesquisa vinculadas a dados de telemetria de uso do IDE |
| **Contexto** | Industry — Usuários do GitHub Copilot, incluindo uma proporção significativa de programadores profissionais |
| **Modo de trabalho** | Not specified |
| **Metodologia** | Not specified |

---

## Objetivo

O objetivo principal do artigo é investigar se as medições de uso das interações dos desenvolvedores com o GitHub Copilot podem prever a produtividade percebida relatada pelos próprios desenvolvedores, estabelecendo uma ligação entre telemetria automatizada e dados de autorrelato [1, 2].

---

## Questoes de Pesquisa

*   **RQ1:** As medições de uso das interações com o GitHub Copilot podem prever a produtividade percebida? [1]
*   **RQ2:** Quais métricas específicas (taxa de aceitação, persistência, volume de código) melhor se correlacionam com a percepção de produtividade? [1, 3]
*   **RQ3:** Como fatores externos, como a linguagem de programação e ciclos circadianos, influenciam a taxa de aceitação? [4, 5]

---

## Metricas e Instrumentos de Avaliacao

| Metrica | Categoria | Nivel | Como Coletada | Validada |
|---------|-----------|-------|---------------|----------|
| Acceptance rate | Productivity | Individual | IDE Telemetry (accepted_per_shown) | Yes |
| Persistence rate | Productivity | Individual | IDE Telemetry (unchanged_X_per_accepted) | Partial |
| Fuzzy persistence rate | Productivity | Individual | IDE Telemetry (mostly_unchanged_X_per_accepted) | Partial |
| Contribution speed | Activity | Individual | IDE Telemetry (accepted_char_per_hour) | Yes |
| Acceptance frequency | Activity | Individual | IDE Telemetry (accepted_per_hour) | Yes |
| Perceived Productivity | Satisfaction/DevEx | Individual | Likert-style Survey (SPACE dimensions) | Yes |
| Aggregate productivity score | Satisfaction/DevEx | Individual | Mean of 12 survey measures | Yes |

---

## Frameworks e Metricas

### Frameworks Referenciados
- **SPACE framework**: APPLIED — Utilizado para desenhar a pesquisa cobrindo as dimensões de Satisfação, Performance, Comunicação/Colaboração e Eficiência/Fluxo [2, 6].

### Frameworks Propostos
O artigo não propõe um novo framework formal, mas introduz um "funil de conclusão de código" (code completion funnel) para categorizar eventos de telemetria desde a oportunidade de conclusão até a persistência do código [7, 8].

---

## Fatores que Influenciam Produtividade

### Fatores Positivos
| Fator | Categoria |
|-------|-----------|
| Neural code completion (AI assistance) | Technical |
| High Acceptance rate | Technical/Human |
| Use of untyped languages (JavaScript/Python) | Technical |

### Fatores Negativos
| Fator | Categoria |
|-------|-----------|
| Reviewing suggestions (potential flow detriment) | Human |
| Erroneous suggestions (requiring deletion) | Technical |
| Working during "usual" office hours (lower acceptance rate) | Process/Human |

---

## Papel da IA e Automacao

| Campo | Valor |
|-------|-------|
| Usa IA/ML? | Yes — Utiliza o GitHub Copilot, baseado no modelo OpenAI Codex (GPT-3) para síntese de código [9, 10]. |
| Automacao de coleta? | Yes — Telemetria coletada automaticamente via IDE para eventos de aceitação e edição [1, 8]. |
| Impacto de IA na produtividade? | Existe uma correlação positiva e estatisticamente significativa entre a taxa de aceitação de sugestões da IA e a produtividade percebida (ρ = 0.24) [3]. |

---

## Resultados Principais

*   A **taxa de aceitação (acceptance rate)** é o melhor preditor da produtividade percebida pelo desenvolvedor (ρ = 0.24, P < 0.0001) [3].
*   Métricas de persistência detalhadas são menos correlacionadas com a produtividade do que a simples aceitação imediata [11].
*   O GitHub Copilot apresentou uma taxa de aceitação média de **27%** e mais de **31 aceitações diárias por usuário (DCPU)** [12].
*   Linguagens não tipadas como **JavaScript (31,4%)** e **Python (30,8%)** possuem taxas de aceitação mais altas que TypeScript (26,3%) [13].
*   A taxa de aceitação é significativamente menor durante o horário comercial típico (21,2%) em comparação com fins de semana (23,5%) [14].
*   A combinação de métricas (taxa de aceitação + frequência + volume) melhora a capacidade preditiva do modelo [15].

---

## Desafios do Uso das Metricas

*   **Variância não explicada:** Fatores humanos e contextuais deixam muita variância fora do alcance da telemetria [3, 16].
*   **Lei de Goodhart:** Otimizar cegamente para a taxa de aceitação pode incentivar mudanças artificiais que não beneficiam o usuário (ex: dividir sugestões em partes menores) [17].
*   **Privacidade:** A coleta de telemetria detalhada exige controles estritos de segurança e privacidade dos dados do usuário [18].
*   **Viés de grupo:** Focar em uma única métrica de topo pode enviesar a ferramenta para linguagens ou grupos majoritários [18].

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

*   O estudo estabelece apenas correlação, não causalidade direta entre as métricas e a produtividade [19].
*   A produtividade percebida pode não refletir a produtividade real em termos de tempo de conclusão de tarefas [16].
*   A investigação foi limitada a uma única ferramenta (GitHub Copilot) com um motor neural fixo [20].
*   Possível viés de seleção, pois os participantes eram usuários voluntários de um "technical preview" [21].

---

## Contribuicao Principal

O artigo demonstra que métricas simples de telemetria, especificamente a taxa de aceitação de sugestões, servem como proxies eficazes para a produtividade percebida em ferramentas de conclusão de código baseadas em IA. Ele fornece a primeira evidência empírica ligando dados de uso automatizados com a experiência subjetiva do desenvolvedor (DevEx), sugerindo que o monitoramento da taxa de aceitação é um indicador confiável para a performance desses sistemas em larga escala [2, 3, 22, 23].

---

*Extraido via NotebookLM em March 2026 para MLR: Software Developer Metrics in Practice*
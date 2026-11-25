# P0178 — Identifying Factors Contributing to “Bad Days” for Software Developers: A Mixed-Methods Study

**Decisao: INCLUIDO | Qualidade: 5/5**

---

## Dados Bibliograficos

| Campo | Valor |
|-------|-------|
| **ID** | P0178 |
| **Autores** | Ike Obi, Jenna Butler, Sankeerti Haniyur, Brian Hassan, Margaret-Anne Storey, Brendan Murphy |
| **Ano** | 2024 |
| **Venue** | Not explicitly stated (appears to be a Software Engineering conference paper) |
| **DOI** | Not available |
| **Tipo** | Conference paper |
| **Metodo** | Mixed methods (Interviews, Surveys, Diary Study, and Telemetry data analysis) |
| **Amostra** | 22 interviewees, 214 survey respondents, 79 diary study participants (775 entries), and 131 developers for telemetry analysis |
| **Contexto** | Industry (Large technology company, implicitly Microsoft) |
| **Modo de trabalho** | Remote (Work-from-home), Hybrid, and On-site |
| **Metodologia** | Not specified (mentions Agile-related processes like PRs and Builds) |

---

## Objetivo

O objetivo principal deste estudo é identificar e validar de forma holística os fatores que contribuem para "dias ruins" (**bad days**) de desenvolvedores de software, examinando seu impacto na produtividade, satisfação e bem-estar, além de utilizar dados de telemetria do sistema para validar as percepções subjetivas dos profissionais [1], [2]. O estudo busca ir além da fricção de ferramentas, investigando como problemas técnicos e não técnicos interagem para afetar a vida profissional e pessoal dos desenvolvedores [3], [4].

---

## Questoes de Pesquisa

*   **RQ1:** What factors cause a “bad day” for developers? [5]
*   **RQ2:** In what ways do developers describe how these “bad day” factors impact them and their work? [5]
*   **RQ3:** Can we observe “bad day” factors using telemetry data? [5]

---

## Metricas e Instrumentos de Avaliacao

| Metrica | Categoria | Nivel | Como Coletada | Validada |
|---------|-----------|-------|---------------|----------|
| **TotalPullRequestTimeHours** | Delivery | Individual | Telemetry | Yes [6] |
| **DwellTimeHours** | Activity | Individual | Telemetry | Yes [6] |
| **CodeReviewTimeHours** | Activity | Individual | Telemetry | No (No sig. diff) [6] |
| **TotalReviewers** | Collaboration | Individual | Telemetry | No (No sig. diff) [6] |
| **TotalBuildTimeMinutes** | Activity | Individual | Telemetry | Yes [7] |
| **CoreBuildTimeMinutes** | Activity | Individual | Telemetry | Yes [7] |
| **BuildSuccessRate** | Quality | Individual | Telemetry | No (No sig. diff) [7] |
| **Bad Day Frequency** | Satisfaction | Individual | Survey (Self-reported) | Yes [8], [9] |

---

## Frameworks e Metricas

### Frameworks Referenciados
*   **DevEx (Developer Experience):** REFERENCED (citado como crucial para produtividade e retenção) [10].
*   **SPACE:** REFERENCED (citado como um modelo abrangente para medir produtividade) [11].

### Frameworks Propostos
O artigo não propõe um novo framework formal, mas oferece uma categorização temática dos fatores de "dias ruins" baseada em **Tooling/Infrastructure**, **Process Inefficiencies** e **Team Dynamics** [12].

---

## Fatores que Influenciam Produtividade

### Fatores Positivos
| Fator | Categoria |
|-------|-----------|
| Flow state | Human [2], [13] |
| Faster build processes | Technical [14] |
| Control over workday/minimizing disruptions | Process [15] |
| Positive emotional states | Human [13] |

### Fatores Negativos
| Fator | Categoria |
|-------|-----------|
| PR delayed (flaky tests, build failure, unresponsive reviews) | Technical/Process [16] |
| Engineering System Friction (broken tools) | Technical [17], [18] |
| High meeting load | Organizational [19], [16] |
| Slow/laggy laptop | Technical [16] |
| Unclear project ownership/Confusion in work tracking | Process [20] |
| Interpersonal conflicts/unresponsive teammates | Human [21] |
| Lack of documentation | Process [20] |

---

## Papel da IA e Automacao

| Campo | Valor |
|-------|-------|
| Usa IA/ML? | No — a pesquisa utiliza métodos estatísticos e qualitativos tradicionais [22]. |
| Automacao de coleta? | Yes — dados de telemetria (PRs, builds, logs) foram coletados automaticamente via sistema [23], [24]. |
| Impacto de IA na produtividade? | Not applicable — o estudo foca em fricções de sistemas de engenharia e processos humanos [12]. |

---

## Resultados Principais

*   **97% dos desenvolvedores** relataram ter tido pelo menos um "dia ruim" no último mês [9].
*   O fator número 1 causador de dias ruins é o **atraso em Pull Requests (PR)** por razões fora do controle do desenvolvedor (Média 4.22) [16].
*   **Validação por Telemetria:** Desenvolvedores que relataram dias ruins tiveram um **TotalPullRequestTimeHours 23.8% maior** e um **DwellTimeHours (tempo de espera) 48.8% maior** do que o grupo de controle [6].
*   O tempo médio de **Build** foi significativamente maior para quem relatou dias ruins (49.74 min vs 36.65 min), uma diferença de **26.3%** [7].
*   Dias ruins geram um **vicious cycle**: causam estresse que afeta o sono, fazendo com que o desenvolvedor retorne ao trabalho exausto e menos produtivo no dia seguinte [4].

---

## Desafios do Uso das Metricas

*   Muitos fatores subjetivos críticos, como "sentir que não fez nada" ou "desafios de equipe", não são facilmente capturáveis apenas por dados de sistema (**telemetry**) [25].
*   A necessidade de anonimização e consentimento ético para vincular percepções subjetivas a logs de sistema é um desafio logístico e de privacidade [26], [24].
*   Fatores como "confiança do desenvolvedor" e "síndrome do impostor" exigem métodos qualitativos, pois métricas quantitativas isoladas podem mascarar o sofrimento emocional [27], [28].

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

*   A amostra é limitada a uma subpopulação de uma única organização, o que pode não representar a realidade de outras empresas ou culturas [29].
*   Viés de participação: desenvolvedores que enfrentam mais dias ruins podem ter tido maior propensão a se voluntariar para o estudo [30].
*   Diferenças culturais no conforto de expressar opiniões negativas podem ter influenciado as respostas dos surveys e entrevistas [30].

---

## Contribuicao Principal

A principal contribuição deste estudo é a demonstração empírica de que os "dias ruins" não são apenas frustrações passageiras, mas eventos com impactos severos na saúde mental (ansiedade, burnout), na vida pessoal (conflitos familiares, falta de exercício) e na retenção de talentos (desilusão e busca por novos empregos) [31], [32]. Ao validar percepções subjetivas com telemetria, o artigo fornece uma base sólida para que organizações parem de olhar para fricções de ferramentas de forma isolada e adotem uma abordagem centrada no desenvolvedor para mitigar o ciclo vicioso de improdutividade e exaustão [4].

---

*Extraido via NotebookLM em March 2026 para MLR: Software Developer Metrics in Practice*
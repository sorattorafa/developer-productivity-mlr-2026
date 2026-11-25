# P0603 — Understanding and effectively mitigating code review anxiety

**Decisao: INCLUIDO | Qualidade: 5/5**

---

## Dados Bibliograficos

| Campo | Valor |
|-------|-------|
| **ID** | P0603 |
| **Autores** | Carol S. Lee, Catherine M. Hicks |
| **Ano** | 2024 |
| **Venue** | Empirical Software Engineering |
| **DOI** | https://doi.org/10.1007/s10664-024-10550-9 |
| **Tipo** | Journal article |
| **Metodo** | Mixed methods (Quantitative: Randomized waitlist control trial, Path analysis, MANCOVA; Qualitative: adapting clinical models) [1-4] |
| **Amostra** | 59 professional developers (30 workshop condition, 29 control condition) [5] |
| **Contexto** | Industry (Participants from various industries including Technology, Education, Financial Services, etc.) [6] |
| **Modo de trabalho** | Not specified [6] |
| **Metodologia** | Not specified [6] |

---

## Objetivo

O objetivo principal do artigo é apresentar um framework empírico para compreender os fatores que mantêm e exacerbam a ansiedade em Code Reviews e testar a eficácia de uma intervenção inovadora (workshop cognitivo-comportamental de sessão única) para mitigar essa ansiedade e seus comportamentos de esquiva associados [1, 7].

---

## Questoes de Pesquisa

*   **RQ1 (H1):** Self-efficacy, cost bias e probability bias mantêm e exacerbam a ansiedade em Code Review, de modo que menor autoeficácia e maiores vieses estão associados a maior ansiedade? [8, 9]
*   **RQ2 (H2):** Esses fatores psicológicos e a própria ansiedade estão associados a uma maior esquiva (avoidance) durante os Code Reviews? [8, 9]
*   **RQ3 (H3):** Participantes do workshop experimentarão menor ansiedade, maior autoeficácia, menores vieses e maior autocompaixão em comparação ao grupo de controle? [10, 11]

---

## Metricas e Instrumentos de Avaliacao

| Metrica | Categoria | Nivel | Como Coletada | Validada |
|---------|-----------|-------|---------------|----------|
| Subjective Units of Distress Scale (SUDS) | Satisfaction / DevEx | Individual | Self-report (Likert 0-10) | Yes [12, 13] |
| Probability Bias Rating (PB) | DevEx | Individual | Self-report (Likert 0-8) | Partial (Adapted) [13] |
| Cost Bias Rating (CB) | DevEx | Individual | Self-report (Likert 0-8) | Partial (Adapted) [14] |
| Anxiety Self Efficacy (ASE) | DevEx | Individual | Self-report (Likert 1-9) | Partial (Adapted) [15] |
| State Self Compassion Scale (S-SCS) | Satisfaction / DevEx | Individual | Self-report (6 items) | Yes [16] |
| Code Review Avoidance (CRA) | Activity / Collaboration | Individual | Self-report (Likert 0-4) | Partial (Adapted) [16] |

---

## Frameworks e Metricas

### Frameworks Referenciados
*   **DevEx (Developer Experience):** REFERENCED (como contexto para a pesquisa) [17].
*   **Cognitive-Behavioral Group Therapy (CBGT):** APPLIED (base para o desenvolvimento do workshop) [18].
*   **Dialectical Behavior Therapy (DBT):** APPLIED (uso de técnicas como TIPP, DEAR MAN e GIVE FAST) [12, 18, 19].
*   **Stereotype Inoculation Model:** REFERENCED (para discutir mecanismos de suporte para minorias) [20].

### Frameworks Propostos
O artigo propõe um **modelo empírico de ansiedade em Code Review** que conecta mecanismos cognitivos (Anxiety Self-Efficacy, Cost Bias, Probability Bias) ao estado de ansiedade e comportamentos de Code Review Avoidance (procrastinação, "rubber stamping", desengajamento cognitivo) [1, 53, Fig. 5].

---

## Fatores que Influenciam Produtividade

### Fatores Positivos
| Fator | Categoria |
|-------|-----------|
| Anxiety Self-Efficacy (Autoeficácia na gestão da ansiedade) | Human [1, 21] |
| Self-Compassion (Autocompaixão) | Human [22] |
| Positive relationships with peers | Human [23] |
| Effective code review tools | Technical [23] |
| Small pull requests | Process [23] |

### Fatores Negativos
| Fator | Categoria |
|-------|-----------|
| Code Review Anxiety (Fear of judgment/criticism) | Human [24, 25] |
| Cost Bias (Superestimar o custo de erros) | Human [9, 21] |
| Probability Bias (Superestimar a chance de erros) | Human [9, 26] |
| Avoidance / Procrastination | Process / Human [26, 27] |
| Rumination (Ruminação pós-evento) | Human [28] |

---

## Papel da IA e Automacao

| Campo | Valor |
|-------|-------|
| Usa IA/ML? | No — O estudo foca em intervenções psicológicas humanas [10, 18]. |
| Automacao de coleta? | No — Coleta via surveys de autorrelato [12]. |
| Impacto de IA na produtividade? | Referenciado na literatura como forma de reduzir cognitive load e time burden através de loops de feedback automatizados [23]. |

---

## Resultados Principais

*   **Redução da Ansiedade:** Participantes do workshop tiveram uma redução significativamente maior na ansiedade (SUDS) com tamanho de efeito médio ($\eta^2 = 0.12$) [11, 29].
*   **Aumento da Autoeficácia:** O workshop aumentou significativamente a Anxiety Self-Efficacy com um tamanho de efeito grande ($\eta^2 = 0.34$) [11, 29].
*   **Aumento da Autocompaixão:** Houve um aumento significativo na autocompaixão (S-SCS) no grupo do workshop ($\eta^2 = 0.10$) [11, 29].
*   **Fatores Preditores:** A autoeficácia foi o preditor mais forte da ansiedade ($\beta = -0.36$), e a ansiedade foi o preditor mais forte da esquiva ($\beta = 0.42$) [9, 30].
*   **Universalidade:** A ansiedade em Code Review **não foi associada ao gênero ou aos anos de experiência** de codificação, refutando mitos de que seria um "problema de desenvolvedores juniores" [31, 32].
*   **Clínica vs Estatística:** 43% dos participantes do workshop alcançaram mudança clinicamente significativa na ansiedade, comparado a 17% no grupo de controle [33].

---

## Desafios do Uso das Metricas

*   **Avoidance Behaviors:** O uso de métricas de atividade pode ser camuflado por comportamentos de esquiva como "rubber stamping" (aprovar sem revisar) ou leitura superficial para reduzir a ansiedade no momento [26, 27].
*   **Safety Behaviors:** Desenvolvedores podem usar comportamentos de segurança para esconder o sofrimento, dificultando a detecção da ansiedade por gestores [28].
*   **Contextual Sensitivity:** Métoras que focam apenas em probabilidade de erro (Probability Bias) podem ser ineficazes se não considerarem o contexto real onde erros acontecem [34].

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

*   **Cross-sectional data:** O modelo de ansiedade baseou-se em dados transversais, o que limita conclusões definitivas sobre causalidade [35].
*   **Construct validity:** Algumas métricas foram adaptadas de instrumentos validados, mas não validadas especificamente para o contexto de software antes do estudo [35].
*   **Selection bias:** A amostragem foi por conveniência (participantes voluntários), o que pode atrair indivíduos mais interessados em saúde mental [36].
*   **Lack of double-blind:** O facilitador sabia qual grupo era o de controle, embora verificações de percepção de ajuda tenham sido feitas [37].
*   **Expert Facilitator:** O workshop foi conduzido por uma psicóloga clínica; os resultados podem variar com facilitadores sem esse treinamento [38].

---

## Contribuicao Principal

A principal contribuição é a criação de um **modelo empírico pioneiro que explica como a ansiedade em Code Review é mantida** por mecanismos psicológicos e como ela gera comportamentos de esquiva que prejudicam a qualidade e a colaboração. Além disso, o estudo prova que um **workshop breve e baseado em evidências clínicas** pode reduzir significativamente essa ansiedade, aumentando a autoeficácia e a autocompaixão dos desenvolvedores, oferecendo uma estratégia prática e de baixo custo para melhorar a experiência do desenvolvedor (DevEx) nas organizações [2, 39].

---

*Extraido via NotebookLM em March 2026 para MLR: Software Developer Metrics in Practice*
# P2096 — Both personality and social identity predict perceived software team productivity: A survey study [1]

**Decisao: INCLUIDO | Qualidade: 5/5** [1-4]

---

## Dados Bibliograficos

| Campo | Valor |
|-------|-------|
| **ID** | P2096 |
| **Autores** | Karim Abdeldayem, Karam Khatib, Lucas Gren [1] |
| **Ano** | 2026 [1] |
| **Venue** | Information and Software Technology (Vol. 197, 108196) [1] |
| **DOI** | https://doi.org/10.1016/j.infsof.2026.108196 [1] |
| **Tipo** | Journal article [1] |
| **Metodo** | Survey (Quantitative — Multiple Linear Regression) [1, 2] |
| **Amostra** | 71 complete responses (50.7% Software Developers, 22.6% Project Managers, 14.0% Team/Tech Leads, 12.7% UX/UI Designers) [2] |
| **Contexto** | Open-Source Software (OSS) — active contributors recruited via 5 developer mailing lists (Apache OpenOffice, Mozilla, Eclipse, Python-dev, VirtualBox) [2] |
| **Modo de trabalho** | Remote (Distributed OSS development) [2] |
| **Metodologia** | Not specified [2] |

---

## Objetivo

This paper investigates which factors from **personality** (Big Five model) and **social identity** (Collective Self-Esteem dimensions) best predict perceived software team productivity, and whether both constructs act as **complementary predictors** within a single predictive regression model [1, 5].

---

## Questoes de Pesquisa

**RQ1:** To what extent do personality traits and social identity factors jointly predict perceived team productivity in software development? [5]

---

## Metricas e Instrumentos de Avaliacao

| Metrica | Categoria | Nivel | Como Coletada | Validada |
|---------|-----------|-------|---------------|----------|
| **Big Five Personality Traits** (Agreeableness, Neuroticism, Intellect/Openness, Extraversion, Conscientiousness) | Human / Personality | Individual | Online survey using the 20-item Mini-IPIP scale (4 items per trait, 5-point Likert) [2] | Yes (Donnellan et al., 2006) [2] |
| **Collective Self-Esteem / CSE** (Public CSE, Membership Esteem, Private CSE, Importance to Identity) | Collaboration / Social Identity | Individual | Online survey using the 16-item Luhtanen and Crocker CSE scale (4 items per dimension, 5-point Likert) [2] | Yes (Luhtanen and Crocker, 1992) [2] |
| **Perceived Team Productivity** (On-time delivery, High quality, Team effectiveness) | Productivity | Team (measured as individual perception) | Online survey using 3 self-assessed items (mean of delivery on time, high quality, and team effectiveness, 5-point Likert) [2] | Yes (Established self-assessed measure in SE, e.g., Forsgren et al., 2021) [2] |

---

## Frameworks e Metricas

### Frameworks Referenciados
- **SPACE Framework** (Forsgren et al., 2021): **REFERENCED** (cited as theoretical background for developer productivity measurement) [2, 4].
- **Big Five Personality Model** (Goldberg, 1992 / Mini-IPIP by Donnellan et al., 2006): **APPLIED** (used as measurement instrument for individual personality traits) [2, 5].
- **Collective Self-Esteem (CSE) Scale** (Luhtanen & Crocker, 1992): **APPLIED** (used as measurement instrument for social identity dimensions) [2, 5].

### Frameworks Propostos
The paper does not propose a new named framework; rather, it establishes an **integrated linear regression predictive model** combining Big Five personality traits and Collective Self-Esteem (CSE) dimensions [1, 2].

---

## Fatores que Influenciam Produtividade

### Fatores Positivos
| Fator | Categoria |
|-------|-----------|
| **Agreeableness** (\\(\beta = 0.319, p = 0.002\\)) [3] | Human |
| **Public Collective Self-Esteem** (\\(\beta = 0.290, p = 0.005\\)) [3] | Organizational / Human |
| **Membership Esteem** (\\(\beta = 0.277, p = 0.009\\)) [3] | Organizational / Human |
| **Intellect / Openness** (\\(\beta = 0.183, p = 0.070\\), tentative) [3] | Human |
| **Team cohesion, shared goals, stable team composition, and team recognition** [3] | Organizational / Process |

### Fatores Negativos
| Fator | Categoria |
|-------|-----------|
| **Neuroticism** (\\(\beta = -0.223, p = 0.033\\)) [3] | Human |
| **Friction and poor team coordination** [3] | Process / Human |

---

## Papel da IA e Automacao

| Campo | Valor |
|-------|-------|
| **Usa IA/ML?** | **Yes** — The authors declared using Claude Code with Opus 4.7 during manuscript preparation for text improvement, proofreading, and writing LaTeX code [4]. |
| **Automacao de coleta?** | **No** — Data was collected via an online survey manually distributed to OSS developer mailing lists [2]. |
| **Impacto de IA na produtividade?** | **Not evaluated** — The study did not examine the impact of AI or automation tools on productivity [1, 2]. |

---

## Resultados Principais

- The retained regression model explained roughly a third of the variance in perceived software team productivity (\\(adjusted\ R^2 = 0.329, F(5, 65) = 7.86, p < 0.001\\)) [2, 3].
- Predictors from **both personality and social identity** survived backward elimination, demonstrating that they are complementary predictors [1, 3].
- **Agreeableness** (personality) was the single strongest positive predictor (\\(\beta = 0.319, B = 0.354, SE = 0.112, t = 3.17, p = 0.002\\)) [3].
- **Public CSE** (social identity) was the second strongest predictor (\\(\beta = 0.290, B = 0.152, SE = 0.052, t = 2.91, p = 0.005\\)) [3].
- **Membership Esteem** (social identity) was the third strongest predictor (\\(\beta = 0.277, B = 0.155, SE = 0.057, t = 2.70, p = 0.009\\)) [3].
- **Neuroticism** (personality) significantly negatively predicted perceived team productivity (\\(\beta = -0.223, B = -0.154, SE = 0.071, t = -2.18, p = 0.033\\)) [3].
- **Intellect/Openness** (personality) sat near the inclusion threshold (\\(\beta = 0.183, B = 0.145, SE = 0.079, t = 1.85, p = 0.070\\)), which should be read as tentative given the lenient \\(\alpha = 0.10\\) [2, 3].
- Four initial predictors were removed during backward elimination (\\(p > 0.10\\)): Extraversion, Conscientiousness, Private CSE, and Importance to Identity [2, 6].
- Statistical diagnostics confirmed model validity: VIF values close to 1 (max VIF = 1.10, no multicollinearity), Durbin-Watson = 2.04 (no autocorrelation), homoscedasticity, and approximate residual normality [2, 3].

---

## Desafios do Uso das Metricas

- **Common Method Bias**: All constructs were collected via self-report on the same survey instrument at a single point in time [3].
- **Perceived vs. Objective Measurement**: Team productivity was operationalized as self-assessed perception rather than objective repository or delivery metrics [2, 3].
- **Individual-Level Perception of Team Property**: Measures each individual's perception of their team rather than an aggregated team-level metric, preventing multi-level modeling since participants were not known to share teams [4].
- **Social Desirability Bias**: Self-evaluations of personality traits and collective self-esteem may be influenced by social desirability [3].
- **Short Psychometric Instruments**: Use of brief scales (Mini-IPIP with 4 items per trait) might capture less variance than longer personality inventories [4].

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

- **Small Convenience Sample**: Sample size of \\(n = 71\\) active OSS contributors, requiring a more lenient alpha threshold (\\(\alpha = 0.10\\)) [2, 4].
- **Sampling & Role Bias**: Recruited exclusively through 5 open-source developer mailing lists, with responses skewed toward software developers (50.7%) [2, 4].
- **Generalizability Context**: Findings apply directly to distributed open-source development and may not transfer cleanly to in-house corporate software teams [2, 4].
- **Lack of Geographic Demographics**: Participants' country of residence was not recorded [2].
- **Subjective Single-Source Data**: Reliance on self-assessed productivity rather than objective performance metrics [3, 4].

---

## Contribuicao Principal

The paper's main contribution is demonstrating for the first time that **personality (Big Five) and social identity (Collective Self-Esteem)** act as complementary, non-overlapping predictors of perceived software team productivity when evaluated in a unified regression model [1, 3, 5]. By showing that top predictors alternate between individual traits (Agreeableness, Neuroticism) and group identification factors (Public CSE, Membership Esteem), the authors establish that single-construct studies are under-specified and that managers must address both individual selection and team cohesion when composing software engineering teams [1, 3, 4].

---

*Extraido via NotebookLM em October 2026 para MLR: Software Developer Metrics in Practice*

---

💡 Would you like me to generate a visual comparison chart of the standardized regression coefficients (\\(\beta\\)) or summarize another paper for your literature review?
# P2050 — Results from a Replicated Experiment on the Affective Reactions of Novice Developers When Applying Test-Driven Development

**Decisao: INCLUIDO | Qualidade: 4.5/5**

---

## Dados Bibliograficos

| Campo | Valor |
|-------|-------|
| **ID** | P2050 [1] |
| **Autores** | Simone Romano, Giuseppe Scanniello, Maria Teresa Baldassarre, Davide Fucci, Danilo Caivano [1] |
| **Ano** | 2020 [2] |
| **Venue** | XP 2020 (Agile Processes in Software Engineering and Extreme Programming), LNBIP 383 [2] |
| **DOI** | 10.1007/978-3-030-49392-9_15 [2] |
| **Tipo** | Conference paper (Book chapter / Conference proceedings) [2] |
| **Metodo** | Replicated experiment (Controlled experiment) [1, 3] |
| **Amostra** | 59 second-year CS undergraduate students (replication); 29 third-year CS undergraduate students (baseline) [1, 3, 4] |
| **Contexto** | Academic (University of Bari and University of Basilicata, Italy) [1, 4-6] |
| **Modo de trabalho** | On-site (University computer laboratories) [7, 8] |
| **Metodologia** | Test-Driven Development (TDD) vs. Non-TDD / Your Way (YW) [1, 4, 9] |

---

## Objetivo

The main objective of this paper is to validate the findings of a baseline experiment by evaluating the affective reactions (pleasure, arousal, dominance, and liking) of novice developers when practicing Test-Driven Development (TDD) compared to a non-TDD approach (Your Way), as well as their specific affective reactions during the implementation and testing phases [1, 3, 10].

---

## Questoes de Pesquisa

- **RQ1**: Is there a difference in the affective reactions of novice developers to a development approach (i.e., TDD vs. a non-TDD approach)? [11]
- **RQ2**: Is there a difference in the affective reactions of novice developers to the implementation phase when comparing TDD to a non-TDD approach? [11]
- **RQ3**: Is there a difference in the affective reactions of novice developers to the testing phase when comparing TDD to a non-TDD approach? [5]

---

## Metricas e Instrumentos de Avaliacao

| Metrica | Categoria | Nivel | Como Coletada | Validada |
|---------|-----------|-------|---------------|----------|
| **APPPLS** (Pleasure - Approach) | DevEx / Satisfaction | Individual | Self-Assessment Manikin (SAM) 9-point rating scale [10, 12, 13] | Yes [10, 12] |
| **APPARS** (Arousal - Approach) | DevEx / Satisfaction | Individual | Self-Assessment Manikin (SAM) 9-point rating scale [10, 12, 13] | Yes [10, 12] |
| **APPDOM** (Dominance - Approach) | DevEx / Satisfaction | Individual | Self-Assessment Manikin (SAM) 9-point rating scale [10, 12, 13] | Yes [10, 12] |
| **APPLIK** (Liking - Approach) | DevEx / Satisfaction | Individual | Liking dimension (9-point thumb rating scale) [10, 13, 14] | Yes [15] |
| **IMPPLS** (Pleasure - Implementation) | DevEx / Satisfaction | Individual | Self-Assessment Manikin (SAM) 9-point rating scale [10, 12, 13] | Yes [10, 12] |
| **IMPARS** (Arousal - Implementation) | DevEx / Satisfaction | Individual | Self-Assessment Manikin (SAM) 9-point rating scale [10, 12, 13] | Yes [10, 12] |
| **IMPDOM** (Dominance - Implementation) | DevEx / Satisfaction | Individual | Self-Assessment Manikin (SAM) 9-point rating scale [10, 12, 13] | Yes [10, 12] |
| **IMPLIK** (Liking - Implementation) | DevEx / Satisfaction | Individual | Liking dimension (9-point thumb rating scale) [10, 13, 14] | Yes [15] |
| **TESPLS** (Pleasure - Testing) | DevEx / Satisfaction | Individual | Self-Assessment Manikin (SAM) 9-point rating scale [10, 12, 13] | Yes [10, 12] |
| **TESARS** (Arousal - Testing) | DevEx / Satisfaction | Individual | Self-Assessment Manikin (SAM) 9-point rating scale [10, 12, 13] | Yes [10, 12] |
| **TESDOM** (Dominance - Testing) | DevEx / Satisfaction | Individual | Self-Assessment Manikin (SAM) 9-point rating scale [10, 12, 13] | Yes [10, 12] |
| **TESLIK** (Liking - Testing) | DevEx / Satisfaction | Individual | Liking dimension (9-point thumb rating scale) [10, 13, 14] | Yes [15] |
| **STR** (Development Performance) | Productivity / Delivery | Individual | Normalized percentage of user stories implemented in a 3-hour fixed window  [16, 17] | Yes [2] |

---

## Frameworks e Metricas

### Frameworks Referenciados
- **PAD (Pleasure-Arousal-Dominance) Model**: REFERENCED — Psychological model describing emotional states across three dimensional axes [12, 18].
- **SAM (Self-Assessment Manikin)**: APPLIED — Pictorial self-assessment instrument measuring pleasure, arousal, dominance, and extended with a liking scale [10, 12, 14].
- **Standard Industry Frameworks (DORA, SPACE, DevEx, GQM, HEART, OKR)**: NOT REFERENCED or APPLIED in this study [1, 12].

### Frameworks Propostos
None — the paper does not propose a new metric framework [1, 3].

---

## Fatores que Influenciam Produtividade

### Fatores Positivos
| Fator | Categoria |
|-------|-----------|
| **Positive affective states** (pleasure and dominance correlated with higher performance) [14] | Human |
| **Structured training in unit testing and JUnit** [7, 8] | Process |

### Fatores Negativos
| Fator | Categoria |
|-------|-----------|
| **Negative affective states** (e.g., frustration from writing failing unit tests before code) [10] | Human |
| **Prior habit/experience with test-last development** creating resistance to TDD [19] | Process / Human |
| **Fixed time constraints** during development tasks [16, 20] | Organizational / Process |

---

## Papel da IA e Automacao

| Campo | Valor |
|-------|-------|
| **Usa IA/ML?** | No — the paper does not evaluate or utilize AI/ML techniques [1, 4]. |
| **Automacao de coleta?** | Partial — customer acceptance testing was automated via JUnit test suites, and statistical evaluation utilized analysis scripts [21, 22]. |
| **Impacto de IA na produtividade?** | Not addressed in this paper [1]. |

---

## Resultados Principais

- **No Significant Difference in Replication**: In the replicated experiment with 59 participants, ANOVA Type Statistic (ATS) showed no statistically significant differences between TDD and non-TDD (YW) across all 12 affective reaction DVs [23-26].
- **Affective Reactions to Development Approach (RQ1)**: P-values showed no significant effect of TDD on pleasure (p=0.6937), arousal (p=0.6421), dominance (p=0.8295), or liking (p=0.9211) [23, 24].
- **Affective Reactions to Implementation Phase (RQ2)**: P-values showed no significant effect of TDD on pleasure (p=0.9040), arousal (p=0.7781), dominance (p=0.9529), or liking (p=0.8048) [24, 25].
- **Affective Reactions to Testing Phase (RQ3)**: P-values showed no significant effect of TDD on pleasure (p=0.5722), arousal (p=0.7446), dominance (p=0.5090), or liking (p=0.4588) [25, 26].
- **Discrepancy with Baseline Findings**: The replication failed to support the baseline experiment's findings (29 participants), which had reported that developers liked TDD less (p=0.0024, Cliff's δ=0.6048, large), liked implementing code less under TDD (p=0.0396, Cliff's δ=0.4286, medium), and felt less happy while testing under TDD (p=0.0178, Cliff's δ=0.5000, large) [15, 27, 28].
- **Influence of Prior Unit Testing Experience**: The authors speculate that the divergence between baseline and replication results is caused by participant background: baseline subjects had prior unit testing experience in a test-last manner (causing negative affective reactions when forced to write tests first), whereas replication subjects had no prior unit testing experience [19].
- **Development Performance (STR)**: Neither TDD nor YW significantly impacted development performance in either the baseline experiment (p=0.4765) or the replication (p=0.4480) [17, 29].

---

## Desafios do Uso das Metricas

- **Subjectivity of Self-Assessment**: Relying on single-point self-assessment instruments (SAM and liking scale) introduces potential subjective response bias [30, 31].
- **Mono-method Bias**: Evaluating developer affective state at a single instance post-task rather than continuously or via multi-method triangulation [30].
- **Evaluation Apprehension & Hypotheses Guessing**: Awareness of being evaluated or attempting to infer research goals might alter participants' self-reported affective scores [30].
- **Resentful Demoralization**: Participants assigned to an unfamiliar development workflow (such as TDD when accustomed to Test-Last) might react negatively or feel demoralized during the task [32].

---

## Avaliacao de Qualidade Metodologica

| Criterio | Pontuacao (0-2) |
|----------|----------------|
| **Objetivo claramente definido** | 2 — Clear research questions, baseline context, and replication objectives provided [4, 11, 33]. |
| **Metodologia adequada ao objetivo** | 2 — Rigorous 2x2 factorial experimental design with non-parametric ATS statistical inference [18, 34, 35]. |
| **Amostra/contexto descrito adequadamente** | 2 — Detailed demographic breakdown, sample sizes (29 vs. 59), and institutional sites reported [4-6]. |
| **Ameacas a validade discutidas** | 2 — Thorough categorization of construct, conclusion, internal, and external validity threats following Wohlin et al. [30-32, 36]. |
| **Resultados com evidencia suficiente** | 2 — Full reporting of p-values, effect sizes, stacked bar distributions, and open replication dataset [15, 22, 24, 37]. |
| **Contribuicao clara para pratica ou teoria** | 1 — Valuable insights for empirical software engineering replication and education, though limited by student subjects [19, 36, 38]. |
| **TOTAL** | **11/12** |

---

## Limitacoes

- **Student Subjects as Proxies**: Involving undergraduate CS students limits direct generalizability to professional software developers in industrial contexts [36].
- **Short Experimental Session**: Development tasks were restricted to a single 3-hour laboratory session on small academic problems (BSK and MRA) [8, 21, 36].
- **Single Post-Task Measurement**: Affective reactions were self-assessed only once after task completion rather than measured continuously during development [30].
- **Fixed Time Pressure**: The fixed time frame (3 hours) may have introduced performance pressure affecting developer sentiment [20].

---

## Contribuicao Principal

The key contribution of this paper is demonstrating through a replicated experiment that Test-Driven Development (TDD) does not inherently cause negative affective reactions (dislike, unhappiness, or lack of control) in novice developers who lack prior test-last habits [1, 19, 25, 28]. By comparing replication results with the baseline study, the authors show that developer resistance or negative feelings toward TDD are strongly conditioned by prior habits (such as writing tests test-last), providing crucial empirical evidence for empirical software engineering and practical recommendations for educators to introduce TDD early in software engineering curricula [19, 38].

---

*Extraido via NotebookLM em October 2026 para MLR: Software Developer Metrics in Practice*

📊 Would you like me to create a comparison report or executive deck summarizing these experimental findings alongside other software engineering metrics studies in your notebook?
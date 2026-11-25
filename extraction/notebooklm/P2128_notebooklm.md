# P2128 — On software productivity analysis with propensity score matching

**Decisao: INCLUIDO | Qualidade: 4/5**

---

## Dados Bibliograficos

| Campo | Valor |
|-------|-------|
| **ID** | P2128 [1] |
| **Autores** | Masateru Tsunoda, Sousuke Amasaki [1] |
| **Ano** | 2017 [2] |
| **Venue** | ACM/IEEE International Symposium on Empirical Software Engineering and Measurement (ESEM) [1, 2] |
| **DOI** | Not explicitly stated in paper text [1, 2] |
| **Tipo** | Conference paper [1, 2] |
| **Metodo** | Repository mining / Secondary observational data analysis (comparing Propensity Score Matching with Linear Regression) [1, 3-5] |
| **Amostra** | 1,010 software projects total across two datasets: 610 filtered projects from ISBSG Release 9 (from 3,026 original projects across 20 countries) and 400 filtered projects from a Finnish software development company dataset (from 407 original projects) [4, 5]. |
| **Contexto** | Industry (cross-company repository data from ISBSG across 20 countries, and single-company industry data from a Finnish enterprise) [4, 5]. |
| **Modo de trabalho** | Not specified [4, 5] |
| **Metodologia** | Not specified [4, 5] |

---

## Objetivo

The main objective of this paper is to investigate what differences the application of Propensity Score Matching (PSM) brings to software productivity analysis in comparison to conventional linear regression methods, specifically addressing the observational nature and confounding bias prevalent in software engineering project repositories [1, 3].

---

## Questoes de Pesquisa

*(Note: The paper does not explicitly label research questions as RQ1, RQ2, etc., but investigates the following core implicit research questions)* [1, 3, 6, 7]:

- **RQ1**: What differences exist in identified critical productivity factors when applying Propensity Score Matching (PSM) compared to conventional Linear Regression analysis on cross-company software project data (ISBSG)? [1, 6-14]
- **RQ2**: What differences exist in identified productivity factors (e.g., required software quality) when applying PSM compared to Linear Regression on single-company software project data (Finnish dataset)? [1, 5, 7, 15-23]

---

## Metricas e Instrumentos de Avaliacao

| Metrica | Categoria | Nivel | Como Coletada | Validada |
|---------|-----------|-------|---------------|----------|
| **Productivity** | Productivity | Project | Defined as software size (Unadjusted Function Points / FP) divided by summary work effort (Person-Hours or Man-Months); log-transformed for analysis [5, 24-26]. | Yes [24, 26] |
| **Software Size (Unadjusted FP)** | Delivery | Project | Function Point analysis count (including EI, EO, EQ, ILF, EIF attributes) [5, 25]. | Yes [25] |
| **Work Effort** | Activity | Project | Summary work effort recorded in person-hours/man-months [5, 25]. | Yes [25] |
| **Duration** | Delivery | Project | Recorded project calendar duration [5, 25]. | Yes [25] |
| **Business Sector** | Organizational | Organization / Project | Categorical classification in repositories (e.g., Insurance, Sector B, Sector M) [8, 18, 25]. | Yes [25] |
| **Development Platform** | Technical | Project | Categorical classification in repositories (e.g., Mainframe, Platform I) [8, 18, 25]. | Yes [25] |
| **Programming Language** | Technical | Project | Categorical classification (e.g., COBOL, Java, C, Perl) [8, 25, 27]. | Yes [25] |
| **Quality Requirements** | Quality | Project | 5-scale ordinal value recorded in the Finnish dataset, dichotomized at level 3 (<3 vs. >=3) for PSM [5, 15, 18]. | Yes [5, 15] |
| **Development Type** | Process | Project | Categorical classification recorded in ISBSG [25]. | Yes [25] |
| **Propensity Score & Average Treatment Effect (ATE)** | Productivity | Project | Calculated via logistic regression model fitted values (probabilities) followed by closest-pair matching and subgroup mean subtraction [27-30]. | Yes [27-30] |

---

## Frameworks e Metricas

### Frameworks Referenciados
- **ANCOVA (Analysis of Covariance)**: REFERENCED — discussed as a statistical framework to eliminate covariance influence [28, 31, 32].
- **SEM (Structural Equation Modeling)**: REFERENCED — mentioned as an alternative method used to mitigate confounding relationships [31].
- **Stratification**: REFERENCED — discussed as a traditional non-parametric method to control confounders, noted as limited when explanatory variables increase [31].
- **Randomized Controlled Trials (RCT)**: REFERENCED — cited from medical/epidemiological literature as non-applicable to observational software datasets [32].
- *(Note: Standard industry frameworks such as DORA, SPACE, DevEx, GQM, HEART, or OKR are NOT mentioned in this paper)* [1-46].

### Frameworks Propostos
- The paper does not propose a new software metric framework; instead, it proposes an analytical procedure adapting **Propensity Score Matching (PSM)** (incorporating logistic regression model construction, c-statistic evaluation, closest propensity matching, and Average Treatment Effect calculation) as a practical triangulation method for software productivity analysis [3, 27-30, 37].

---

## Fatores que Influenciam Produtividade

### Fatores Positivos
| Fator | Categoria |
|-------|-----------|
| **Use of COBOL (under PSM analysis)** | Technical [7, 13] |
| **High Developer Skill (illustrative confounder example)** | Human [33, 34] |
| **Use of Development Tools (illustrative example)** | Technical [33, 34] |
| **Required Quality / Quality Requirements (under Linear Regression)** | Technical / Quality [17, 20] |

### Fatores Negativos
| Fator | Categoria |
|-------|-----------|
| **Insurance Business Sector** | Organizational [11, 13] |
| **Mainframe Development Platform** | Technical [11, 13] |
| **Business Sectors B and M (Finnish dataset)** | Organizational [17, 18] |
| **Platform I (Finnish dataset)** | Technical [17, 18] |
| **Confounding Bias / Observational Repository Bias** | Process / Methodological [31, 33, 34] |

---

## Papel da IA e Automacao

| Campo | Valor |
|-------|-------|
| **Usa IA/ML?** | No — The study employs classical statistical modeling (Logistic Regression for propensity score generation and Linear Regression) [9, 12, 29]. |
| **Automacao de coleta?** | No — Data was retrieved from existing historical project repositories (ISBSG Release 9 and Finnish software effort dataset) [4, 5, 45]. |
| **Impacto de IA na produtividade?** | Not mentioned / Not evaluated in the paper [1-46]. |

---

## Resultados Principais

- **ISBSG Dataset Analysis (610 projects)** [4]:
  - Linear regression (Model 2) estimated that adopting **COBOL** had a negligible positive effect (\\(\text{coef} = 0.02\\)) or slightly negative effect in Model 3 (\\(\text{coef} = -0.05\\)), whereas PSM revealed a clear positive effect size (\\(+0.19\\)) on log-transformed productivity [7, 11, 13].
  - For the **Insurance** business sector, both Linear Regression (\\(\text{coef} = -0.95\\) in Model 2) and PSM (\\(\text{effect size} = -0.92\\)) consistently indicated a substantial negative impact on productivity [11, 13].
  - For **Mainframe** platforms, Linear Regression (\\(\text{coef} = -0.64\\) in Model 2) and PSM (\\(\text{effect size} = -0.32\\)) both confirmed negative effects on productivity [11, 13].
  - Logistic regression models used to compute propensity scores exhibited high discriminative power with \\(c\text{-statistics} > 0.90\\) (Insurance: \\(0.91\\), Mainframe: \\(0.97\\), COBOL: \\(0.97\\)) [13].
- **Finnish Dataset Analysis (400 projects)** [5]:
  - Linear regression suggested that higher **Quality Requirements** significantly increased productivity (\\(\text{coef} = +0.14\\) in Model 2 and \\(+0.19\\) in Model 3) [17, 20].
  - In contrast, PSM demonstrated that Quality Requirements had virtually no effect on productivity (\\(\text{effect size} = 0.02\\)) after controlling for confounding covariates [18, 21, 22].
  - For Business Sectors B and M, and Platform I, both methods showed consistent negative impacts (PSM effect sizes: \\(-0.80\\) for Sector B, \\(-0.47\\) for Sector I, \\(-0.45\\) for Sector M) [17, 18, 21].
  - Propensity score logistic regression models yielded good \\(c\text{-statistics}\\) ranging from \\(0.81\\) to \\(0.87\\) [18, 21].
- **Methodological Evaluation**:
  - Explanatory variables in software project repositories exhibit moderate-to-strong mutual correlations (Cramer's V up to \\(0.67\\) between platform and programming language/quality requirements) [15-17, 36].
  - PSM serves as an accessible triangulation tool alongside linear regression to prevent misidentifying critical productivity factors caused by spurious relationships [23, 37].

---

## Desafios do Uso das Metricas

- **Observational Data Bias & Confounders**: Software project datasets are observational rather than experimental, containing organizational biases and confounders (e.g., developer skill co-varying with tool adoption) that induce sham effects in regression models [31, 33, 34].
- **Naïve Regression Misleading Conclusions**: Standard linear regression fails to account for non-random treatment assignment, leading to potential misattribution of causal productivity drivers [1, 23, 34].
- **Dichotomization of Multi-category Variables**: Applying PSM requires binary treatment conditions, forcing continuous or ordinal variables (such as 5-scale quality requirements or multi-class programming languages) to be converted into dummy variables [9, 18, 27].
- **Data Point Loss in Matching**: PSM discards unmatched control project data points when control group sizes exceed treatment group sizes or overlap is imperfect [30].
- **Limitations of Alternative Confounder Controls**: Stratification rapidly suffers from small cell sample sizes as variables increase, while ANCOVA risks severe bias if covariance model specifications are incorrect [31, 32].
- **Absence of Qualitative Field Surveys**: Statistical techniques alone cannot conclusively verify physical causality without accompanying field interviews or qualitative project surveys [23].

---

## Avaliacao de Qualidade Metodologica

| Criterio | Pontuacao (0-2) |
|----------|----------------|
| Objetivo claramente definido | 2 |
| Metodologia adequada ao objetivo | 2 |
| Amostra/contexto descrito adequadamente | 2 |
| Ameacas a validade discutidas | 1 |
| Resultados com evidencia suficiente | 2 |
| Contribuicao clara para pratica ou teoria | 1 |
| **TOTAL** | **10/12** |

---

## Limitacoes

- **Lack of Qualitative / Field Validation**: The authors performed statistical re-analyses of secondary datasets but did not conduct field surveys or developer interviews to verify whether PSM conclusions reflect actual project realities [23].
- **Binary Treatment Requirement**: PSM requires binary variables, necessitating dummy variable creation and manual thresholding for ordinal scales [18, 27].
- **Unmeasured Confounders**: PSM relies on the "strongly ignorable treatment assignment" assumption; unobserved or unmeasured confounding variables not present in the dataset cannot be controlled [35].
- **Removal of Minor Categories**: Categorical variables representing under 5% of projects were discarded, potentially omitting minor but influential productivity factors [25].
- **List-wise Deletion Reduction**: Projects with missing values were excluded, substantially reducing the available sample size (e.g., filtering ISBSG from 3,026 down to 610 projects) [4].

---

## Contribuicao Principal

This paper demonstrates that Propensity Score Matching (PSM) effectively mitigates confounding bias in observational software project repositories where explanatory variables are heavily correlated [1, 3, 34]. By re-analyzing the ISBSG and Finnish datasets, the authors reveal that conventional linear regression can lead to contradictory conclusions regarding critical productivity factors—such as misjudging the impact of programming languages (COBOL) or overestimating the positive effect of quality requirements [11, 13, 17, 21, 23]. Consequently, the study contributes a practical methodological framework positioning PSM as a lightweight, essential triangulation tool for software engineering managers and researchers to evaluate productivity factors reliably before making process improvement decisions [23, 37, 40].

---

*Extraido via NotebookLM em October 2026 para MLR: Software Developer Metrics in Practice*
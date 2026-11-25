# P2120 — Surveying the developer experience of flaky tests

**Decisao: INCLUIDO | Qualidade: 5/5**

---

## Dados Bibliograficos

| Campo | Valor |
|-------|-------|
| **ID** | P2120 |
| **Autores** | Owain Parry, Gregory M. Kapfhammer, Michael Hilton, Phil McMinn [1] |
| **Ano** | 2022 [2] |
| **Venue** | 44th International Conference on Software Engineering: Software Engineering in Practice (ICSE-SEIP '22) [2] |
| **DOI** | 10.1145/3510457.3513037 [2] |
| **Tipo** | Conference paper [2] |
| **Metodo** | Mixed methods (Literature-guided survey, quantitative Likert analysis, thematic analysis, Q&A thread mining) [3, 4] |
| **Amostra** | 170 developer survey responses and 38 accepted StackOverflow Q&A threads [3, 5] |
| **Contexto** | Mixed (Commercial and Open-Source Software development) [6, 7] |
| **Modo de trabalho** | Not specified |
| **Metodologia** | Not specified (Continuous Integration / DevOps environment context) [2, 8] |

---

## Objetivo

The main objective of this study is to investigate how software developers define, experience, and react to flaky tests, as well as to identify the causes and impacts of test flakiness from a developer-centric perspective [1, 3, 9]. By combining a literature-guided survey of 170 software developers with a thematic analysis of 38 accepted StackOverflow threads, the paper aims to complement prior automated repository mining studies with direct developer insights and provide actionable recommendations for practitioners and researchers [3, 5, 10].

---

## Questoes de Pesquisa

- **RQ1: Definition:** *How do developers define flaky tests?* [10]
- **RQ2: Impacts:** *What impacts do flaky tests have on developers?* [10]
- **RQ3: Causes:** *What causes the flaky tests experienced by developers?* [4]
- **RQ4: Actions:** *What actions do developers take against flaky tests?* [4]

---

## Metricas e Instrumentos de Avaliacao

| Metrica | Categoria | Nivel | Como Coletada | Validada |
|---------|-----------|-------|---------------|----------|
| Flaky Test Observation Frequency (SQ3) | DevEx / Activity | Individual | Survey question (5-point scale: Never, A few times a year, Monthly, Weekly, Daily) [11, 12] | No [6] |
| Testing Reliability Reduction Rating (SQ4.1) | Quality | Individual/Team | Survey Likert scale (0–3) [12, 13] | No [6] |
| Testing Efficiency Loss Rating (SQ4.2) | Productivity | Individual/Team | Survey Likert scale (0–3) [13, 14] | No [6] |
| Developer Productivity Loss Rating (SQ4.3) | Productivity | Individual/Team | Survey Likert scale (0–3) [13, 15] | No [6] |
| Testing Confidence Loss Rating (SQ4.4) | Satisfaction / DevEx | Individual/Team | Survey Likert scale (0–3) [13, 16] | No [6] |
| Continuous Integration Hindrance Rating (SQ4.5) | Delivery / Productivity | Team/Organization | Survey Likert scale (0–3) [8, 13] | No [6] |
| Likelihood of Ignoring Test Failures (SQ4.6) | DevEx / Activity | Individual | Survey Likert scale (0–3) [8, 13] | No [6] |
| Flaky Test Failure Reproduction Difficulty (SQ4.7) | Activity / Productivity | Individual | Survey Likert scale (0–3) [13, 17] | No [6] |
| Bug vs Flakiness Differentiation Difficulty (SQ4.8) | Activity / Productivity | Individual | Survey Likert scale (0–3) [13, 18] | No [6] |
| Flaky Test Cause Frequency Ratings (SQ5.1–SQ5.10) | Quality / Technical | Individual/Team | Survey Likert scale (0–3: Never, Rarely, Sometimes, Often) [13, 19] | No [6] |
| Flaky Test Action Frequency Ratings (SQ7.1–SQ7.8) | Activity / DevEx | Individual/Team | Survey Likert scale (0–3: Never, Rarely, Sometimes, Often) [13, 20] | No [6] |
| Commercial/OSS Development Experience (SQ10) | DevEx / Demographics | Individual | Survey question (5 categories: 0–1, 2–4, 5–8, 9–12, 13+ years) [7] | No [6] |

---

## Frameworks e Metricas

### Frameworks Referenciados
- None of the standard measurement frameworks (such as DORA, SPACE, DevEx, GQM, HEART, or OKR) are explicitly referenced or applied as formal measurement frameworks in the paper.

### Frameworks Propostos
- The paper does not propose a new software metrics framework.

---

## Fatores que Influenciam Produtividade

### Fatores Positivos
| Fator | Categoria |
|-------|-----------|
| Reliable test suites capable of identifying genuine issues in a timely manner [15] | Technical |
| Prompt repair of flaky tests to prevent accumulation and loss of testing discipline [21, 22] | Process |
| Proper isolation of test states and explicit setup/teardown logic [23, 24] | Technical |
| Mocking external dependencies or unstable UI components [25] | Technical |

### Fatores Negativos
| Fator | Categoria |
|-------|-----------|
| Flaky tests hindering Continuous Integration (CI) execution pipelines [2, 8, 26] | Technical / Process |
| Loss of developer productivity due to unreliability and false alarms [2, 15, 26] | Technical / Human |
| High temptation/likelihood to ignore genuine test failures when flaky tests accumulate [8, 27, 28] | Human / Organizational |
| Psychological costs including developer frustration and loss of confidence in test suites [16, 29] | Human |
| Inadequate setup and teardown routines polluting test execution states [23, 30] | Technical |
| Reliance on network connections and third-party external services or libraries [31-33] | Technical / Organizational |
| Environmental and hardware inconsistencies between local development machines and remote CI build environments [34, 35] | Technical |

---

## Papel da IA e Automacao

| Campo | Valor |
|-------|-------|
| Usa IA/ML? | No — The study notes that random data generators in machine learning applications represent a cause of test flakiness (SQ5.6), but does not apply AI/ML in its own methodology [36]. |
| Automacao de coleta? | Yes — Automated search queries were used to filter StackOverflow Q&A threads ("flaky test hasaccepted:yes") and Python scripts were executed for numerical survey analysis [37, 38]. |
| Impacto de IA na produtividade? | Not evaluated in the paper. |

---

## Resultados Principais

- **High Definition Consensus:** 93.5% of survey respondents (158 of 169) agreed with the standard definition of a flaky test (a test that passes and fails without changes to the code under test) [39, 40]. Thematic analysis revealed extended definitions encompassing execution environment factors, flaws in the code under test, and non-deterministic attributes like coverage or execution time [39, 41, 42].
- **CI Hindrance as Top Impact:** Developers strongly identified hindrance to Continuous Integration (CI) as the most severe impact of flaky tests (mean score 2.63/3.00) [26, 43], followed by developer productivity loss (2.50/3.00) [26, 43] and reduced testing efficiency (2.47/3.00) [26, 43].
- **Behavioral Shift toward Ignoring Failures:** Developers experiencing flaky tests at least monthly were significantly more likely to ignore potentially genuine test failures (mean 2.32 vs 1.96 for less frequent observers) [27, 43] and take no action when encountering them (mean 1.40 vs 0.91) [44, 45].
- **Setup/Teardown as Primary Cause:** Improper setup and teardown was rated as the #1 most frequent cause of flaky tests (mean score 1.69/3.00) [30, 46], followed by network dependencies (1.44/3.00) [30, 46] and unknown causes (1.32/3.00) [30, 46]. Asynchronicity (1.30/3.00) [46] and concurrency (1.12/3.00) [46] ranked 4th and 5th, contrasting with prior automated commit-mining studies where they ranked 1st and 2nd [47, 48].
- **StackOverflow Diagnostic Patterns:** Thematic analysis of 38 StackOverflow threads showed that UI timing issues and logic errors/API misuse were the main causes for which developers seek diagnostic help online [49-51], with fixing logic and adding conditional waits being the most prescribed repairs [25, 52].
- **Dominant Developer Actions:** Re-running the failing build (mean 2.67/3.00) [44, 53] and attempting to repair the test (mean 2.41/3.00) [44, 53] were the most common developer actions; actions like quarantining (0.77/3.00) [54] or deleting flaky tests (0.94/3.00) [44] were rarely utilized.

---

## Desafios do Uso das Metricas

- **Discrepancy Between Perception and Automated Mining:** Developer perceptions of flaky test causes (where setup/teardown dominates) differ from empirical commit-mining studies (where asynchronicity/concurrency dominates), indicating potential recall bias or differences in fix prioritization [47, 48].
- **High Prevalence of Undiagnosed Failures:** The high ranking of unknown/unresolved causes (SQ5.10 and Ct4) highlights a lack of diagnostic visibility and tooling support for root-causing non-deterministic failures [30, 55, 56].
- **Workaround Anti-Patterns:** Frequently re-running CI builds until they pass (SQ7.2) serves as a prevalent short-term workaround that conceals underlying technical debt and environment flaws [44, 53, 57].
- **Erosion of Testing Discipline:** Accumulation of unaddressed flaky tests leads developers to normalize test failures, increasing the risk of missing genuine software regressions [8, 27, 28].

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

- **Self-Reporting Bias:** Survey findings rely on self-reported developer experiences and perceptions, which may be subject to recall bias [9, 37].
- **Sample Generalizability:** The survey sample of 170 developers recruited via Twitter, LinkedIn, and regional technology forums cannot be guaranteed to generalize across all industry sectors or software organizations [58-60].
- **Unverified Participant Identities:** Due to open online dissemination, participant software development backgrounds could not be independently verified beyond demographic survey screening questions [59].
- **StackOverflow Dataset Filtering:** The StackOverflow dataset was restricted to 38 accepted threads matching specific search parameters ("flaky test hasaccepted:yes"), which excludes unaccepted threads or discussions lacking accepted answers [37, 61, 62].

---

## Contribuicao Principal

The principal contribution of this paper is a multi-source empirical study combining a literature-guided developer survey (\\(N=170\\)) and thematic analysis of StackOverflow Q&A threads (\\(N=38\\)) to characterize test flakiness from the developer's perspective [3, 5, 63, 64]. It reveals key differences between developer perceptions and prior repository mining research, illustrates the workflow and psychological impacts of test flakiness on Continuous Integration pipelines, and provides six actionable recommendations for both practitioners and software engineering researchers [10, 47, 63, 65].

---

*Extraido via NotebookLM em October 2026 para MLR: Software Developer Metrics in Practice*
# P2126 — Analysis of factors influencing developers' sentiments in commit logs: insights from applying sentiment analysis

**Decisao: INCLUIDO | Qualidade: 5/5** [1, 2]

---

## Dados Bibliograficos

| Campo | Valor |
|-------|-------|
| **ID** | P2126 |
| **Autores** | Rajdeep Kaur, Kuljit Kaur Chahal, Munish Saini [1] |
| **Ano** | 2022 [1] |
| **Venue** | e-Informatica Software Engineering Journal (Vol. 16, Issue 1, 220102) [1] |
| **DOI** | 10.37190/e-Inf220102 [1] |
| **Tipo** | Journal article [1] |
| **Metodo** | Repository mining (Quantitative analysis of commit logs using SentiStrength-SE and Pearson correlation analysis) [2-4] |
| **Amostra** | 86,515 commit messages from 7 open-source software (OSS) GitHub projects [2, 5, 6] |
| **Contexto** | OSS (Open Source Software) — 7 popular C, C++, Java, PHP/MySQL, and JavaScript projects (PostgreSQL, Glibc, Eclipse-CDT, GNUCash, WordPress, Firebug, Rhino) with over 10 years of project history [5, 7, 8] |
| **Modo de trabalho** | Remote / Geographically dispersed [2] |
| **Metodologia** | Not specified (Open source collaborative development) [2] |

---

## Objetivo

This paper aims to examine developers' sentiments expressed in the commit logs of seven popular GitHub projects to analyze how sentiment polarity relates to project team size (small, medium, large), type of code change activity (combinations of addition, deletion, and modification), commit contribution volume per developer, and temporal evolution over project lifespans [2, 5, 9, 10]. The goal is to provide software project managers with empirical insights into developer affect to optimize task allocation, manage workload, enhance productivity, and improve developer retention in OSS communities [2, 9, 11].

---

## Questoes de Pesquisa

- **RQ1**: What are the overall developers’ sentiments in the commit logs? [9]
- **RQ2**: Is there any relation between sentiments and team size of a project? [11]
- **RQ3**: Does the type of change activity performed by a developer impact their sentiments in commit messages? [12]
- **RQ4**: Is there any relation between developer sentiment volumes and commit contribution size? [13]
- **RQ5**: How has sentiment in the commit logs evolved over the period of time? [14]

---

## Metricas e Instrumentos de Avaliacao

| Metrica | Categoria | Nivel | Como Coletada | Validada |
|---------|-----------|-------|---------------|----------|
| **Sentiment Polarity Score** | Human / Satisfaction | Individual / Message | Calculated via **SentiStrength-SE** domain-specific lexical tool on preprocessed commit subject lines (Positive score: +1 to +5, Negative score: -1 to -5, Neutral score: +1 to -1; combined max positive and negative scores per sentence) [15, 16] | Yes [15, 17, 18] |
| **Sentiment Volume** | Human / Satisfaction | Individual / Project | Calculated as the percentage of sentiment type (Positive, Negative, Neutral) expressed by an individual developer divided by the total sentiment of that type in the project [19, 20] | Yes [19] |
| **Commit Contribution Size** | Activity / Delivery | Individual | Calculated as the percentage of commits made by an individual contributor divided by total project commits (`Individual Commits / Total Project Commits`) [19, 20] | Yes [19] |
| **Team Size / Active Developers** | Organization / Collaboration | Team / Project | Categorized based on total contributors (Small: 40–60, Medium: 61–200, Large: >200) using Becher et al. boundaries, as well as annual counts of active developers making \\(\ge 1\\) commit in a given year [21-23] | Yes [23] |
| **Type of Change Activity** | Process / Activity | Individual / Commit | Classification of file change combinations per commit: **Type-1** (add + modify), **Type-2** (delete + modify), and **Type-3** (add + delete + modify), extracted via Git commit log mining [24, 25] | Yes [24, 26] |
| **Project Size (LOC)** | Quality / Product | Project | Total Lines of Code (LOC) extracted directly from repository source trees [5, 7] | Yes [7] |

---

## Frameworks e Metricas

### Frameworks Referenciados
- **SentiStrength-SE Lexical Framework**: **APPLIED** — Used as the primary domain-specific measurement instrument for software engineering text sentiment classification [2, 15, 18].
- **Becher et al. Project Boundary Framework**: **APPLIED** — Used as the classification framework for categorizing OSS projects into Small (40–60), Medium (61–200), and Large (>200) team sizes [21-23].
- **Standard Industry Frameworks (DORA, SPACE, DevEx, GQM, HEART, OKR)**: **NOT REFERENCED** — None of these standard industry metric frameworks are cited or applied in this paper.

### Frameworks Propostos
- **Change Activity Combination Classification Scheme**: The paper proposes a novel grouping scheme that combines individual file change operations into compound activity types (**Type-1**: add + modify, **Type-2**: delete + modify, **Type-3**: add + delete + modify) to evaluate task complexity impact on developer affect [9, 24, 25].
- **Sentiment-Contribution Mapping Framework**: A structured pipeline mapping individual developer sentiment volume against commit contribution percentages to detect maintenance stress and maintainer sentiment trends [19, 20].

---

## Fatores que Influenciam Produtividade

### Fatores Positivos
| Fator | Categoria |
|-------|-----------|
| **Launch of public platforms (e.g., GitHub in 2008)** | Technical / Process (Public visibility of commit logs leads to higher neutrality and lower negative sentiment over time) [27] |
| **Simpler change activities (Type-1 add+modify and Type-2 delete+modify)** | Technical / Process (Performing fewer combined file operations generates significantly lower negative sentiment) [28, 29] |
| **Task decomposition (Decomposing complex issues into smaller ones)** | Process / Organizational (Simplifies tasks, reduces cognitive strain, and improves developer sentiment and productivity) [13, 30] |
| **Medium project team size (61–200 developers)** | Organizational (Exhibits the highest positive sentiment proportion compared to small and large teams) [22, 31] |
| **Lower commit contribution volume / Occasional contributors** | Human / Activity (Developers with smaller commit contributions express higher positive sentiment and lower stress) [32, 33] |
| **Early project phases** | Technical / Process (Initial project stages are less complex with fewer issues, fostering higher positive sentiment) [27, 34] |

### Fatores Negativos
| Fator | Categoria |
|-------|-----------|
| **High task complexity (Type-3 add+delete+modify activities)** | Technical / Process (Executing three combined change operations increases workload, leading to the highest negative sentiment across all projects) [28, 29] |
| **High commit volume / Lead developer workload** | Human / Organizational (Top code contributors elicit higher negative sentiment due to project deadlines, quality gate oversight, and maintainer strain) [20, 32] |
| **Small project team size (40–60 developers)** | Organizational / Human (Generates higher negative sentiment, potentially driven by work pressure, lack of formalization, or informal team dynamics) [31, 35] |
| **Increasing project maturity and code complexity** | Technical / Product (As projects age and grow, resolving complex issues increases negative/neutral affect relative to early project years) [27, 34] |
| **Code refactoring and bug-fixing tasks** | Technical / Process (Refactoring and managing large legacy code bases introduces stress and negative affect) [11, 36] |

---

## Papel da IA e Automacao

| Campo | Valor |
|-------|-------|
| **Usa IA/ML?** | **Yes** — Uses **SentiStrength-SE**, an automated NLP lexical sentiment classifier with software engineering domain dictionaries [2, 15, 18]. Machine learning / deep learning techniques are also highlighted for future multi-variable analysis [37]. |
| **Automacao de coleta?** | **Yes** — Fully automated commit log extraction via Git Bash (`git log`) and scripted automated text preprocessing/sentiment scoring using SentiStrength-SE [8, 16]. |
| **Impacto de IA na produtividade?** | Automated NLP sentiment analysis enables project managers to monitor team affect continuously across communication artifacts, helping identify burnout in core maintainers, optimize task distribution, and introduce timely interventions to boost developer retention and productivity [2, 14, 26, 37]. |

---

## Resultados Principais

- **Overall Sentiment Polarity (RQ1)**: Across 86,515 commit messages, **68.29% were neutral**, **26.98% were negative**, and **4.73% were positive** [6, 38]. Neutrality dominated all projects, ranging from 58.67% in PostgreSQL to 79.77% in Eclipse-CDT [39].
- **Impact of Team Size (RQ2)**: Large teams (>200 developers) displayed the highest proportion of neutral sentiment (**75.78%**) due to formal coding practices and technical terms [22, 31, 35]. Small teams (40–60 developers) showed the highest negative sentiment (**35.28%**), while medium teams (61–200) displayed the highest positive sentiment (**8.14%**) [22, 31].
- **Impact of Change Activity (RQ3)**: Complex Type-3 activities (add + delete + modify) consistently generated the highest negative sentiment (e.g., 36.69% in PostgreSQL, 23.74% in WordPress) [28]. Type-1 and Type-2 activities yielded near-total or high neutral sentiment (up to 100% neutral for Type-2 in PostgreSQL, GNUCash, and WordPress) [28, 29].
- **Commit Contribution Volume (RQ4)**: Lead contributors (top 10 by commit volume) exhibited significantly higher negative sentiment across almost all projects [20, 32]. Strong positive Pearson correlations existed between commit volume and negative sentiment in GNUCash and Rhino (\\(r > 0.70\\)) and WordPress, Glibc, PostgreSQL, and Firebug (\\(r > 0.90\\)) [40].
- **Temporal Evolution (RQ5)**: Neutral sentiment steadily increased over time across all projects, particularly following the launch of GitHub in 2008 (public commit visibility) [27, 41]. Positive sentiment was highest during the early years of projects when codebases were less complex [33, 34].

---

## Desafios do Uso das Metricas

- **Inaccuracy of Off-the-Shelf Sentiment Tools**: Generic NLP tools (e.g., StanfordNLP, NLTK, generic SentiStrength) produce erroneous scores on technical text because software terms (e.g., "error", "kill", "bug") carry technical rather than emotional meaning; domain-specific tools (SentiStrength-SE) are strictly necessary [15, 42].
- **High Neutrality Dilution**: Overwhelming neutral sentiment (~68–80%) in commit logs makes detecting subtle changes in developer affect challenging [39, 43].
- **Subject Line vs. Body Discrepancy**: Analyzing only commit subject lines ignores detailed sentiment that may be present in commit message bodies [44].
- **Developer Alias Fragmentation**: Failure to resolve multiple developer names/emails (aliases) can distort developer-level contribution volume and sentiment metrics [44].
- **Misinterpretation of Core Maintainer Activity**: High commit volume does not equal developer satisfaction; treating high commit activity as purely positive masks severe burnout and negative affect among lead maintainers [20, 32].

---

## Avaliacao de Qualidade Metodologica

| Criterio | Pontuacao (0-2) |
|----------|----------------|
| **Objetivo claramente definido** | **2** — Clearly articulated study objective and 5 specific research questions regarding developer sentiment factors [2, 9, 11-14]. |
| **Metodologia adequada ao objetivo** | **2** — Rigorous repository mining pipeline using SentiStrength-SE, statistical correlation tests (Pearson), and longitudinal time-series grouping [3, 4, 15, 16]. |
| **Amostra/contexto descrito adequadamente** | **2** — Detailed breakdown of 7 projects with LOC, stars, commit counts, developer counts, and exact observation date ranges [5, 7, 8]. |
| **Ameacas a validade discutidas** | **2** — Section 6 explicitly details internal, external, construct, and conclusion validity threats (subject line scope, alias resolution, OSS domain restriction) [44-46]. |
| **Resultados com evidencia suficiente** | **2** — Extensive visual and tabular empirical evidence, percentage distributions per RQ, and correlation coefficients [18, 21, 28, 35, 40, 47]. |
| **Contribuicao clara para pratica ou teoria** | **2** — Delivers practical actionable recommendations for OSS project managers, task decomposition, and maintainer support [30, 37, 48]. |
| **TOTAL** | **12/12** |

---

## Limitacoes

- **Subject line scope**: The analysis was restricted to commit subject lines, excluding potential emotional context in commit message bodies [44].
- **Developer alias resolution**: Unmerged developer aliases could affect individual-level commit contribution and sentiment volume calculations [44].
- **Platform selection bias**: Only GitHub repositories were included; projects hosted on GitLab, Bitbucket, or private platforms were omitted [45].
- **Domain specificity**: Findings are strictly applicable to open-source software projects and may not generalize to commercial/closed-source industrial development [45].
- **Top-contributor restriction in RQ4**: RQ4 focused exclusively on top 10 contributors, excluding low-volume contributors (<1% of commits) [45].
- **Compound activity restriction**: Only compound change activity combinations were evaluated, without isolating single file operations (addition, deletion, or modification independently) [46].
- **Uncontrolled confounding variables**: Factors such as code quality, developer gender, developer experience, and project popularity were not controlled for [46].

---

## Contribuicao Principal

The paper's primary contribution is a comprehensive empirical characterization of developer sentiment dynamics in commit logs across seven major open-source projects, demonstrating that while overall sentiment is overwhelmingly neutral (~68%), developer affect is significantly influenced by project team size, task complexity, and contribution volume [2, 6, 48-50]. Crucially, the study reveals that lead maintainers with high commit volumes experience substantially higher negative sentiment and that multi-operation changes (add + delete + modify) drive negative emotions, offering actionable guidance for OSS managers to decompose complex tasks, support core maintainers, and establish codes of conduct to foster developer productivity and retention [29, 30, 32, 37].

---

*Extraido via NotebookLM em October 2026 para MLR: Software Developer Metrics in Practice*
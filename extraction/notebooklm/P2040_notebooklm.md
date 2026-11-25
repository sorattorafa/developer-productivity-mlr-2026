# P2040 — The Influence of Environmental Odors on Student Programmers During Code Comprehension and Code Writing

**Decisao: INCLUIDO | Qualidade: 5/5** [1-4]

---

## Dados Bibliograficos

| Campo | Valor |
|-------|-------|
| **ID** | P2040 [1] |
| **Autores** | Zachary Karas, Danielle Page, Maya Maciel-Seidman, Zohreh Sharafi, Yu Huang [1, 5] |
| **Ano** | 2026 [5] |
| **Venue** | ACM Transactions on Software Engineering and Methodology (TOSEM) [5, 6] |
| **DOI** | https://doi.org/10.1145/3822406 [5] |
| **Tipo** | Journal article [5, 6] |
| **Metodo** | Experiment (Controlled eye-tracking study) / Quantitative [1, 7-9] |
| **Amostra** | 30 student programmers (29 undergraduate, 1 graduate student; split into 3 groups of 10) [1, 10, 11] |
| **Contexto** | Academic (Vanderbilt University) [1, 11, 12] |
| **Modo de trabalho** | On-site (Controlled office laboratory setting) [13, 14] |
| **Metodologia** | Not specified (Task-based C++ programming experiment) [12-14] |

---

## Objetivo

The primary objective of this study is to investigate the influence of nonfunctional environmental odors (pleasant: Lemon essential oil, unpleasant: Fish Market aroma, and control: Neutral/no odor) on student programmers during code comprehension and code writing tasks [1, 8, 13, 15]. By combining high-resolution eye tracking (120Hz) with behavioral metrics and standardized psychological assessments, the paper examines how olfactory stimuli affect individual programmer productivity, visual effort, cognitive load, working memory, divergent creativity, and mood [1, 2, 7, 16, 17].

---

## Questoes de Pesquisa

- **RQ1.** How do environmental odors influence programmers’ productivity during code comprehension and code writing? [2]
- **RQ2.** How does environmental odor influence programmers’ cognitive processes? [2]
- **RQ3.** Does environmental odor affect programmers’ creativity, working memory, and mood? [2]

---

## Metricas e Instrumentos de Avaliacao

| Metrica | Categoria | Nivel | Como Coletada | Validada |
|---------|-----------|-------|---------------|----------|
| **Task Duration** | Productivity | Individual | Calculated from first and last eye-tracking timestamps (Tobii Pro Lab / iTrace) per task [18, 19] | Yes [16, 20, 21] |
| **Task Accuracy** | Quality / Productivity | Individual | Multiple-choice score for comprehension tasks; 28-point rubric for code writing in Eclipse [14, 19, 22] | Yes [19, 21] |
| **Fixation Count** | DevEx / Cognitive Processes | Individual | Tobii Pro Fusion eye tracker (120Hz) within defined Areas of Interest (AOIs) [18, 23-25] | Yes [4, 23, 26] |
| **Average Fixation Duration** | DevEx / Cognitive Processes | Individual | Average duration (ms) of spatially stable gaze fixations within AOIs [23, 24, 27] | Yes [4, 23, 26] |
| **Saccade Count** | DevEx / Cognitive Processes | Individual | Eye movements exceeding 400 px/ms velocity threshold within AOIs [25, 27, 28] | Yes [1, 26, 28] |
| **Forward Digit Span Score** | DevEx / Activity (Working Memory) | Individual | Digit Span test (reciting sequences forward until 2 consecutive errors) [17, 29-31] | Yes [32] |
| **Backward Digit Span Score** | DevEx / Activity (Working Memory) | Individual | Digit Span test (reciting number sequences in reverse order) [17, 29-31] | Yes [32] |
| **TTCT Scores (Fluency, Flexibility, Originality, Elaboration)** | DevEx / Activity (Creativity) | Individual | Torrance Test for Creative Thinking (30-circle drawing task in 2 min, scored by 2 raters) [17, 30, 33, 34] | Yes [35, 36] |
| **PANAS Positive & Negative Affect Scores** | Satisfaction / DevEx (Mood) | Individual | Short-form Positive and Negative Affect Schedule (20 emotion words on a 1–5 scale) [33, 37-39] | Yes [40] |
| **Perceived Room Odor Rating** | Satisfaction / DevEx | Individual | Post-debrief subjective rating of room scent pleasantness on a 1–5 scale [41] | Yes [41] |
| **Post-task Subjective Experience Ratings** | Satisfaction / DevEx | Individual | 7 Likert-scale items evaluating focus, performance satisfaction, distraction, and comfort [33, 42, 43] | Yes [42] |
| **Pretest Performance Score** | Competence / Activity | Individual | 7 C++ tree traversal questions completed prior to odor exposure [37, 44] | Yes [44] |

---

## Frameworks e Metricas

### Frameworks Referenciados
- **DevEx (Developer Experience)**: **REFERENCED** — Discussed as part of understanding how environmental/nonfunctional factors impact developer focus and cognitive load [6, 45].
- **DORA / SPACE / GQM / HEART / OKR**: **NOT REFERENCED** — None of these operational metric frameworks are cited or applied [1–114].
- **TTCT (Torrance Test for Creative Thinking)**: **REFERENCED & APPLIED** — Used as a validated measurement instrument for divergent creativity [30, 33, 34, 36].
- **PANAS-SF (Positive and Negative Affect Schedule Short Form)**: **REFERENCED & APPLIED** — Used as a validated tool to measure baseline and post-task mood deltas [33, 37-40].
- **Digit Span Test**: **REFERENCED & APPLIED** — Used as a validated psychometric measure for verbal working memory [29-32].

### Frameworks Propostos
- **None**: The paper does not propose a formal software engineering metric framework, but introduces a controlled experimental design combining AOI-restricted eye tracking, IDE event recording (iTrace), and standardized psychological assessments to study environmental stimuli [7, 8, 18, 24].

---

## Fatores que Influenciam Produtividade

### Fatores Positivos
| Fator | Categoria |
|-------|-----------|
| **Pleasant environmental odor (Lemon)** during Code Comprehension (improves completion speed and focus) [1, 2, 46, 47] | Human / Process (Environmental) [1, 6] |
| **Neutral/scent-free environment** during Code Writing (associated with significantly lower visual effort) [1, 2, 48, 49] | Human / Process (Environmental) [1, 6] |
| **Calming visual exposure** (4-minute nature video prior to tasks to standardize stress baselines) [37, 50] | Human (Psychological) [37, 50] |

### Fatores Negativos
| Fator | Categoria |
|-------|-----------|
| **Unpleasant environmental odor (Fish)** during Code Comprehension (increases task duration and saccade counts) [1, 2, 46, 51] | Human / Process (Environmental) [1, 6] |
| **Ambient odors (both Lemon and Fish)** during Code Writing (significantly increases fixation durations / visual effort) [1, 2, 48, 49] | Human / Process (Environmental) [1, 6] |
| **Higher cognitive load & visual distraction** induced by malodors while inspecting code [51-53] | Human / Process (Environmental) [1, 6] |

---

## Papel da IA e Automacao

| Campo | Valor |
|-------|-------|
| **Usa IA/ML?** | **No** — Analysis relies on parametric/non-parametric inferential statistics (ANOVA, Kruskal-Wallis, t-tests, Mann-Whitney U) and velocity-based gaze filtering algorithms [9, 25, 54]. |
| **Automacao de coleta?** | **Yes** — Automated eye-tracking gaze logging at 120Hz via Tobii Pro Fusion, Tobii Pro Lab software, and the iTrace IDE plugin [18, 25, 49]. |
| **Impacto de IA na produtividade?** | **Not evaluated** — The impact of AI tools on developer productivity was outside the scope of this study [1–114]. |

---

## Resultados Principais

- **Code Comprehension Speed**: Exposure to Lemon odor significantly reduced code comprehension task duration compared to Fish odor (\\(\mu = 14.6\\) min vs \\(\mu = 19.7\\) min, \\(p < 0.05, d = 1.2, g = 1.1\\)), making participants **25.9% faster** than the Fish group and **7% faster** than the Neutral group (\\(\mu = 15.7\\) min) [1, 2, 46].
- **Visual Effort in Code Comprehension**: Both Lemon (\\(\mu = 222.9\\) ms) and Fish (\\(\mu = 223.8\\) ms) groups exhibited significantly longer average fixation durations compared to the Neutral group (\\(\mu = 202.4\\) ms, \\(p < 0.05\\)), indicating higher visual processing effort when any ambient scent was present [27, 55].
- **Cognitive Load & Visual Distraction**: Total saccade count during code comprehension was significantly higher in the Fish group (\\(\mu = 4530.0\\)) than in the Lemon group (\\(\mu = 3342.4, p < 0.05, d = 1.2, g = 1.1\\)) and Neutral group (\\(\mu = 4041.6, p < 0.05\\)), signaling elevated cognitive load and visual searching behavior [27, 51, 52].
- **Visual Effort in Code Writing**: Both Lemon (\\(\mu = 694.0\\) ms, \\(p < 0.01\\)) and Fish (\\(\mu = 616.8\\) ms, \\(p < 0.05\\)) groups recorded significantly longer average fixation durations during code generation in Eclipse compared to the Neutral group (\\(\mu = 480.0\\) ms), suggesting ambient odors increase visual effort during code writing [27, 48].
- **Task Accuracy Stability**: No statistically significant differences were found between odor groups for accuracy in Code Comprehension (\\(F = 0.5, p = 0.6\\)), Code Writing (\\(H = 0.3, p = 0.9\\)), or Prose Comprehension (\\(F = 0.0, p = 1.0\\)) [56].
- **Working Memory, Creativity & Mood**: No statistically significant differences were detected for forward/backward Digit Span (though Neutral trended higher, \\(p = 0.06\\) / \\(p = 0.07\\)), TTCT creativity dimensions, or pre/post PANAS mood deltas [31, 34, 39].
- **Subconscious Cognition**: Participants remained unaware of the scent manipulation; post-task survey ratings showed no significant group differences in perceived focus or distraction, confirming ambient odors influence cognitive mechanics below conscious awareness [1, 33, 43, 57].

---

## Desafios do Uso das Metricas

- **Superficiality of High-Level Productivity Metrics**: Measuring only task completion time and correctness misses underlying physiological strain, visual effort, and cognitive load [7, 20, 56].
- **Confounding Environmental & Human Variables**: Olfactory adaptation (diminishing sensitivity over time), mental fatigue, exam stress, and age-related sensory differences present severe confounding risks for longitudinal metric collection [58-61].
- **Lack of SE-Specific Psychological Instruments**: Standardized psychological tests (Digit Span, TTCT) measure domain-general memory and creativity, which may not capture specialized programming-related mental models [26, 34, 62].
- **Eye-Tracking Data Noise**: Off-screen fixations and gaze jitter require strict velocity thresholding (\\(>400\\) px/ms for saccades) and periodic recalibration to maintain data integrity [18, 24, 25, 63].

---

## Avaliacao de Qualidade Metodologica

| Criterio | Pontuacao (0-2) | Justificativa |
|----------|----------------|---------------|
| **Objetivo claramente definido** | **2** | Explicitly formulates 3 research questions targeting the impact of odors on SE tasks [1, 2]. |
| **Metodologia adequada ao objective** | **2** | Uses a controlled experiment combining eye-tracking, IDE telemetry, and psychometric instruments [7, 8, 18]. |
| **Amostra/contexto descrito adequadamente** | **2** | Detailed demographic baseline balancing (GPA, age, C++ experience) across 30 participants [10, 11, 64]. |
| **Ameacas a validade discutidas** | **2** | Section 7 comprehensively analyzes internal, external, construct, and statistical power limitations [75–80]. |
| **Resultados com evidencia suficiente** | **2** | Provides full descriptive statistics, ANOVA/Kruskal-Wallis tests, \\(p\\)-values, Cohen's \\(d\\), and Hedge's \\(g\\) [9, 27, 54]. |
| **Contribuicao clara para pratica ou teoria** | **2** | Offers original empirical insights for workplace design, HVAC policies, and educational settings [1, 2, 49, 65]. |
| **TOTAL** | **12/12** | **Excelente qualidade metodologica (Qualidade: 5/5)** [1-4] |

---

## Limitacoes

- **Sample Size & Statistical Power**: With 30 participants (10 per group), the study achieved sufficient statistical power (\\(\beta = 0.75\\) at \\(\alpha = 0.05\\)) only for large effect sizes (\\(d \ge 1.1\\)), leaving small-to-medium effects (mood, working memory, creativity) underpowered [3, 4, 10].
- **Student Sample Generalizability**: Participants were university students (undergraduates and 1 graduate student), meaning results may not fully generalize to senior industrial developers [10, 11, 60].
- **Restricted Olfactory Spectrum**: Only two scents (Lemon as pleasant, Fish Market as unpleasant) were evaluated, limiting findings regarding other common workplace ambient odors [15, 41, 60].
- **Laboratory vs. Real-World Validity**: Tasks were brief (up to 90 minutes total) in a controlled office environment without access to online resources, differing from real-world software development workflows [61, 63].
- **Potential Olfactory Adaptation**: Habituation to essential oil diffusion over time may have muted the observed impact on post-task behavioral measures [39, 59, 61].

---

## Contribuicao Principal

This paper provides the first empirical investigation into the influence of environmental odors on software engineering tasks [1, 7, 65]. Through a controlled eye-tracking experiment with 30 student programmers, the authors demonstrate that while pleasant scents (Lemon) can significantly accelerate code comprehension efficiency (25.9% faster than unpleasant odors), ambient scents generally increase visual effort during code writing [1, 2, 46, 48]. Consequently, the study concludes that pleasant odors may aid code reading, whereas a neutral, scent-free environment is optimal for code writing—offering practical implications for open-office layouts, HVAC management, and developer experience optimization [1, 2, 49, 65].

---

*Extraido via NotebookLM em October 2026 para MLR: Software Developer Metrics in Practice*

---
💡 **Nudge**: Would you like me to create a summary table comparing these findings with other environmental developer experience (DevEx) factors, or export this structured summary into a standalone formatted report?
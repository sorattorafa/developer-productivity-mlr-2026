# P0144 — Towards Recognizing the Emotions of Developers Using Biometrics: The Design of a Field Study

**Decisao: INCLUIDO | Qualidade: 4/5**

---

## Dados Bibliograficos

| Campo | Valor |
|-------|-------|
| **ID** | P0144 |
| **Autores** | Daniela Girardi, Filippo Lanubile, Nicole Novielli, Luigi Quaranta, Alexander Serebrenik [1] |
| **Ano** | 2019 [1] |
| **Venue** | 4th International Workshop on Emotion Awareness in Software Engineering (SEmotion) [1] |
| **DOI** | 978-1-7281-2280-9/19 [2] |
| **Tipo** | Conference paper [1] |
| **Metodo** | Field study (Design/Pilot) [1, 3] |
| **Amostra** | One participant (Project Manager) for the pilot validation [3, 4] |
| **Contexto** | Industry — Apuliasoft, a small company specialized in web and mobile development [4] |
| **Modo de trabalho** | On-site [5] |
| **Metodologia** | Not specified [6] |

---

## Objetivo

The main objective of the paper is to present the design of a field study to assess the feasibility of **emotion detection using non-invasive biometric sensors** and to investigate the correlation between daily software engineering activities and the emotions experienced by developers [1, 7]. The long-term goal is to provide recommendations to improve developers' well-being and productivity based on their emotional states [1].

---

## Questoes de Pesquisa

* **RQ1:** Can we identify emotions experienced by software developers using **biometric sensors** during their working day? [3]
* **RQ2:** Is there a connection between developers’ activities and emotions? [3]

---

## Metricas e Instrumentos de Avaliacao

| Metrica | Categoria | Nivel | Como Coletada | Validada |
|---------|-----------|-------|---------------|----------|
| Electrodermal Activity (EDA) | DevEx / Well-being | Individual | Empatica E4 wristband [8] | Yes [2] |
| Blood Volume Pulse (BVP) | DevEx / Well-being | Individual | Empatica E4 wristband [8] | Yes [9] |
| Heart Rate (HR) | DevEx / Well-being | Individual | Derived from BVP [9] | Yes [9] |
| Heart Rate Variability (HRV) | DevEx / Well-being | Individual | Derived from BVP [9] | Yes [9] |
| Valence | DevEx / Well-being | Individual | ESM (9-point Likert scale/SAM) [10] | Yes [10] |
| Arousal | DevEx / Well-being | Individual | ESM (9-point Likert scale/SAM) [10] | Yes [10] |
| Perceived Productivity | Productivity | Individual | WorkAnalytics tool [11] | Yes [11] |
| Task Category | Activity | Individual | WorkAnalytics pop-up selection [10] | Partial [10] |

---

## Frameworks e Metricas

### Frameworks Referenciados
* **Russell’s Circumplex Model of Affect:** REFERENCED — Used to represent emotions along valence and arousal axes [12].
* **Experience Sampling Method (ESM):** APPLIED — Used to elicit systematic self-reports during working hours [13].
* **WorkAnalytics:** APPLIED — Tool used for monitoring perceived productivity and capturing context of activities [11].
* **Self-Assessment Manikin (SAM):** APPLIED — Used for collecting valence and arousal rates [10].

### Frameworks Propostos
The paper does not propose a new framework but designs a specific **experimental protocol** for in-the-field emotion recognition [14].

---

## Fatores que Influenciam Produtividade

### Fatores Positivos
| Fator | Categoria |
|-------|-----------|
| Positive emotions / Happiness | Human [15] |
| Encouragement and Playfulness | Organizational [15] |

### Fatores Negativos
| Fator | Categoria |
|-------|-----------|
| Unhappiness | Human [15] |
| Negative emotions (e.g., being "stuck") | Human [16] |
| Disruptive interruptions | Process [16] |

---

## Papel da IA e Automacao

| Campo | Valor |
|-------|-------|
| Usa IA/ML? | Yes — The study aims to use **machine learning models** to detect emotions from biometric data [17]. |
| Automacao de coleta? | Yes — Biometric data is collected automatically via wristband; activity context is captured by WorkAnalytics [8, 11]. |
| Impacto de IA na produtividade? | Not applicable — This is a study design paper, though it aims to provide automated recommendations in the future [7]. |

---

## Resultados Principais

* The **Empatica E4 wristband** was validated as a comfortable and non-obtrusive device for developers to wear throughout a working day [8].
* Categories for software engineering activities were derived and validated for self-reporting: coding, reading/writing emails, helping colleagues, and networking [10].
* The study protocol successfully integrates **biometric sensing** with the **Experience Sampling Method (ESM)** to provide ground truth for emotions in a real-world setting [11, 14].

---

## Desafios do Uso das Metricas

* **Intrusiveness:** The need for sensors to be comfortable and not cause additional distress or embarrassment to the developer [8].
* **Privacy:** Handling the sensitive nature of activity logs and biometric data (addressed by local storage in this study) [11].
* **Contextualization:** Biometric data alone lacks the "why"; it requires integration with activity tracking to understand what triggers specific emotions [10].

---

## Avaliacao de Qualidade Metodologica

| Criterio | Pontuacao (0-2) |
|----------|----------------|
| Objetivo claramente definido | 2 |
| Metodologia adequada ao objetivo | 2 |
| Amostra/contexto descrito adequadamente | 1 |
| Ameacas a validade discutidas | 1 |
| Resultados com evidencia suficiente | 1 |
| Contribuicao clara para pratica ou teoria | 2 |
| **TOTAL** | **9/12** |

---

## Limitacoes

* The study is an **initial pilot** involving only one participant [3, 17].
* The results of the pilot are not yet general or robust enough for the broad scientific community [3].
* The paper describes the **design and preparation** of the study rather than the final results of a large-scale experiment [1, 17].

---

## Contribuicao Principal

The main contribution is the detailed **design of a field study protocol** that combines non-invasive biometric sensors (Empatica E4) with Experience Sampling (ESM) and activity tracking (WorkAnalytics) [1, 11]. This protocol establishes a feasible way to collect high-quality emotional and physiological data from software developers in their actual work environment without the constraints of a laboratory setting [8, 17].

---

*Extraido via NotebookLM em March 2026 para MLR: Software Developer Metrics in Practice*
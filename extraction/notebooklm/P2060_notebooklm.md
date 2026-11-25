# P2060 — Interruptibility of software developers and its prediction using psycho-physiological sensors: a replication

**Decisao: INCLUIDO | Qualidade: 5/5** [1, 2]

---

## Dados Bibliograficos

| Campo | Valor |
|-------|-------|
| **ID** | P2060 |
| **Autores** | Florian Poreba, Stefan Sobernig [1, 3] |
| **Ano** | 2026 [1, 3] |
| **Venue** | Empirical Software Engineering [1, 3] |
| **DOI** | https://doi.org/10.1007/s10664-025-10739-6 [1] |
| **Tipo** | Journal article [1, 3] |
| **Metodo** | Experiment (External close replication, Quantitative) [1] |
| **Amostra** | 10 participants (4 graduate students, 2 undergraduate students, 3 professionals, 1 HTL graduate; 8 male, 2 female), 82 interruption samples collected over 10 hours of programming sessions [4-6] |
| **Contexto** | Academic / Laboratory setting (Vienna University of Economics and Business; controlled workspace setup with JHotDraw Java framework maintenance tasks) [3, 7, 8] |
| **Modo de trabalho** | On-site [1, 7] |
| **Metodologia** | Not specified [8, 9] |

---

## Objetivo

The main objective of this paper is to perform an external close replication of the well-known lab study by Züger and Fritz (2015) to evaluate whether psycho-physiological (biometric) sensors measuring brain, heart, skin, and temperature activity can automatically predict software developers' perceived interruptibility with high accuracy during coding tasks [1, 4]. Additionally, the paper aims to provide a comprehensive, publicly available lab package to facilitate future independent replications and critically assess threats to validity inherent in biometric prediction models [1, 10].

---

## Questoes de Pesquisa

- **RQ1**: Can biometric sensors be used to automatically measure interruptibility of software developers with high accuracy in a controlled (lab) environment? [11]
- **AQ1**: Are mental load and interruptibility negatively correlated? [12]
- **AQ2**: Are interruptions more disruptive during high mental load? [12]
- **AQ3**: How do interruption, resumption and edit lag relate to interruptibility? [12]
- **AQ4**: What is the optimal time window duration for interruptibility classification? [12]
- **AQ5**: When do participants dislike being interrupted? *(Omitted from replication results due to an unrecoverable questionnaire artifact mismatch)* [12, 13]

---

## Metricas e Instrumentos de Avaliacao

| Metrica | Categoria | Nivel | Como Coletada | Validada |
|---------|-----------|-------|---------------|----------|
| **Perceived Interruptibility** | DevEx | Individual | Self-report on a 5-point Likert scale (1=very interruptible to 5=very uninterruptible) via tablet interruption app, transformed into a 2-state scale (1–3: interruptible, 4–5: uninterruptible) [14, 15] | Partial [15, 16] |
| **Perceived Mental Workload** | DevEx | Individual | Self-report on a 5-point Likert scale (1=very low to 5=very high) via tablet app during interruptions [14, 15] | Partial [17] |
| **Perceived Disturbance / Disruptiveness** | DevEx | Individual | Self-report on a 5-point Likert scale (1=not at all disturbing to 5=very disturbing) via tablet app [14, 15] | Yes [14] |
| **EEG Signal & Brain Wave Bands (\\(\delta, \theta, \alpha, \beta, \gamma\\))** | Activity | Individual | Single-channel EEG sensor (256 Hz in replication, 512 Hz in original) calculating frequency power bands and ratios (\\(\theta/(\alpha+\beta)\\), \\(\beta/(\alpha+\theta)\\)) [18-20] | Yes [18] |
| **Eye Blinks** | Activity | Individual | Derived automatically from the EEG signal using a peak-finding algorithm [18] | Yes [18] |
| **ECG / Heart Rate & Variability (replacing BVP)** | Activity | Individual | Torso ECG electrodes (256 Hz) measuring Heart Rate, HRV, SDNN, PNN20, and PNN50 [20-22] | Yes [21, 22] |
| **Skin Temperature** | Activity | Individual | Wrist thermistor sensor (32 Hz) calculating mean and maximum temperature per time window [19, 20, 23] | Yes [23] |
| **Electrodermal Activity (EDA / SCL)** | Activity | Individual | Wrist electrodes (32 Hz) intended for tonic/phasic conductivity (discarded in replication due to electrode pad gel saturation error) [20, 23, 24] | Yes (Discarded in replication) [20, 24] |
| **Interruption Lag** | Productivity | Individual | Recorded automatically as time elapsed between tablet alert sound and tapping "Start" [25-27] | Yes [26] |
| **Resumption Lag** | Productivity | Individual | Time elapsed between completing interruption tasks and resuming primary coding task [25, 26] | Yes [26] |
| **Edit Lag** | Productivity | Individual | Time elapsed between completing interruption tasks and making first IDE edit action [25, 26] | Yes [26] |
| **Task Completion & Difficulty** | Quality | Individual | Self-report during post-interview (1=very easy to 5=very hard) and recorded completion of 3 Java tasks [9, 28] | Yes [9, 28] |

---

## Frameworks e Metricas

### Frameworks Referenciados
- **NASA-TLX** (Task Load Index): REFERENCED (discussed in Section 4 as a validated multi-item scale for mental workload, though the study used an intuitive single-item self-assessment instead) [17]
- **Carver Reporting Guidelines**: REFERENCED/APPLIED (adopted to structure and report experimental replication details) [29-31]
- **Reproducible Research Standard (RRS)**: REFERENCED/APPLIED (applied to structure licensing and artifact sharing in the lab package) [32]

### Frameworks Propostos
- None proposed (the paper contributes a public **Lab Package** archived on Zenodo for future replications, but does not propose a new developer metrics framework) [1, 10, 32]

---

## Fatores que Influenciam Produtividade

### Fatores Positivos
| Fator | Categoria |
|-------|-----------|
| State of deep focus / Estado de foco profundo contínuo | Human [33] |
| Minimizing or rescheduling interruptions at inopportune moments | Process [34] |
| Negotiated interruptions (allowing developers to decide when to address notifications) | Process [26, 27] |
| Code reuse and API familiarity during change tasks | Technical [8, 9] |
| Notification categorization and priority filtering tools | Technical [13] |

### Fatores Negativos
| Fator | Categoria |
|-------|-----------|
| Frequent interruptions during periods of high mental workload | Organizational [1, 35, 36] |
| High task difficulty / Elevated mental workload | Technical [17, 35] |
| Context switching and long resumption/edit lags | Human [25, 26] |
| High-pitched notification alert sounds causing disturbance | Technical [37, 38] |
| Problems navigating through unfamiliar codebases | Technical [39] |

---

## Papel da IA e Automacao

| Campo | Valor |
|-------|-------|
| Usa IA/ML? | **Yes** — Uses machine learning classification algorithms (Naïve Bayes classifier via Weka API, WrapperSubsetEval feature selection, and 10x10-fold cross-validation) to predict interruptibility from biophysical sensor features [40-42]. |
| Automacao de coleta? | **Yes** — Automated recording of biophysical data (EEG, ECG, skin temperature) and timestamped interruption responses, processed via Python scripts (SciPy, NeuroKit2) [18, 21, 23, 43]. |
| Impacto de IA na produtividade? | ML models failed to predict developer interruptibility significantly better than a majority baseline classifier (69.9% vs 61.1% baseline for 2-state; 32.1% vs 35.5% baseline for 5-state), demonstrating that current biometric ML models on small sample sizes cannot reliably automate interruptibility prediction for developer tools [1, 44, 45]. |

---

## Resultados Principais

- **Falha na Replicabilidade de Alta Acurácia**: Os modelos de ML (Naïve Bayes) baseados em dados biométricos não conseguiram superar significativamente o classificador de maioria (baseline ZeroR): 69,9% ± 14,32 vs. 61,1% baseline em 2 estados; e 32,1% ± 12,96 vs. 35,5% baseline em 5 estados [1, 44, 45].
- **Identificação de Ameaças Severas à Validade no Estudo Original**: O estudo destacou três fragilidades principais na literatura prévia: tamanho reduzido de amostra (< 200 amostras; 72 no original, 82 na replicação), conjunto de dados altamente desbalanceado (83,3% da classe majoritária no original vs. 61,1% na replicação) e transformação ad hoc de escala de Likert de 5 pontos para 2 estados [1, 6, 16, 46].
- **Efeito Fraco da Carga Mental na Interruptibilidade**: Encontrou-se apenas uma correlação fraca, embora significativa, entre carga mental percebida e interruptibilidade (\\(r = 0,318\\), \\(p = 0,004\\)), contrariando a forte correlação (\\(r = 0,815\\)) reportada originalmente [36].
- **Correlação Fraca com Interruption Lag**: Confirmou-se uma correlação fraca mas significativa entre interruptibilidade percebida e o atraso de interrupção (\\(r = 0,381\\), \\(p = 0,0004\\)) [36, 47].
- **Janelas Temporais Curtas Não Demonstraram Superioridade**: Ao contrário do estudo original (que apontou janelas de 10s como ideais), a replicação não observou uma tendência consistente de que janelas temporais menores aumentassem a acurácia [48].
- **Overfitting Revelado por Cross-Validation Aninhada**: O uso de validação cruzada aninhada (*nested cross-validation*) reduziu substancialmente a acurácia estimada (queda de 9,1 pp na acurácia de 2 estados ao aninhar a seleção de recursos), demonstrando viés de overfitting em validações simples [49].

---

## Desafios do Uso das Metricas

- **Desbalanceamento Severo de Dados (Class Imbalance)**: A alta acurácia (91,5%) do estudo original resultou do desbalanceamento da amostra (83,3% da classe majoritária), gerando uma ilusão de alto desempenho preditivo [46, 50].
- **Tamanho Reduzido da Amostra (Small Sample Size)**: Coletar dados biométricos em laboratório é altamente custoso, resultando em amostras pequenas (72–82 amostras) suscetíveis a overfitting e baixo poder de generalização [51-53].
- **Distorção por Transformação de Escala Ad Hoc**: Agrupar 1–3 como "interruptível" e 4–5 como "não interruptível" altera artificialmente as distribuições sem respaldo empírico [16].
- **Métricas Ilusórias sem Comparação de Baseline**: Avaliar a acurácia em isolamento sem enfatizar o ganho relativo em relação ao baseline pode induzir a conclusões equivocadas na prática de engenharia de software [46, 54].
- **Suscetibilidade a Falhas e Ruídos em Sensores Biométricos**: Falhas técnicas no manuseio de sensores (como o gel saturado nos eletrodos de EDA) e ruídos de movimento dificultam a aplicação prática [20, 24].

---

## Avaliacao de Qualidade Metodologica

| Criterio | Pontuacao (0-2) |
|----------|----------------|
| Objetivo claramente definido | 2 [1, 11] |
| Metodologia adequada ao objetivo | 2 [1, 7, 30] |
| Amostra/contexto descrito adequadamente | 2 [5-7] |
| Ameacas a validade discutidas | 2 [16, 24, 46, 51, 52, 55] |
| Resultados com evidencia suficiente | 2 [44, 45, 48, 56] |
| Contribuicao clara para pratica ou teoria | 2 [1, 10, 57, 58] |
| **TOTAL** | **12/12** |

---

## Limitacoes

- **Pequeno Tamanho da Amostra**: Restrito a 10 participantes e 82 amostras de interrupção devido aos custos e restrições de tempo de experimentos de laboratório [1, 5, 6, 51].
- **Descarte dos Dados de Atividade Eletrodérmica (EDA)**: Erro no tipo de eletrodo (pads pré-gelificados com alta concentração salina) levou à saturação glandular e ao descarte de todas as features de EDA [20, 24].
- **Desvios Inevitáveis de Hardware e Software**: Uso de ECG em vez de BVP, dispositivo NeXus-10 MKII com fios (em vez do setup sem fio original) e aplicativo de interrupção reconstruído em Electron com som de alerta agudo [19, 22, 37, 59].
- **Perfil Mais Heterogêneo da Amostra**: Amostra da replicação incluiu alunos de graduação, pós-graduação e profissionais, variando do perfil exclusivamente de pós-graduandos do estudo original [5].
- **Incompatibilidade no Questionário Pós-Sessão**: Impossibilidade de replicar os resultados da questão AQ5 devido ao fornecimento de uma versão divergente do questionário pelos autores originais [13, 60].

---

## Contribuicao Principal

A principal contribuição deste artigo é fornecer a primeira replicação externa e próxima do estudo de Züger e Fritz (2015), demonstrando que dados sensoriais biométricos (EEG, ECG, temperatura) não conseguem prever a interruptibilidade de desenvolvedores com desempenho superior a um classificador baseline de maioria [1, 4, 57]. Ao expor fragilidades metodológicas críticas na literatura anterior — como amostras reduzidas, forte desbalanceamento de dados e transformações arbitrárias de escala — o estudo reorienta a pesquisa da área e disponibiliza um pacote de laboratório (*lab package*) público e arquivado no Zenodo para sustentar futuras replicações independentes na engenharia de software empírica [1, 10, 32, 57].

---

*Extraido via NotebookLM em October 2026 para MLR: Software Developer Metrics in Practice*


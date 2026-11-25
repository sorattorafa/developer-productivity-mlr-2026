# P0445 — Sensing Developers' Emotions: The Design of a Replicated Experiment

**Decisao: INCLUIDO | Qualidade: 2/5**

---

## Dados Bibliograficos

| Campo | Valor |
|-------|-------|
| **ID** | P0445 |
| **Autores** | Daniela Girardi, Filippo Lanubile, Nicole Novielli, Davide Fucci |
| **Ano** | 2018 |
| **Venue** | SEmotion'18 Workshop (3rd Int. Workshop on Emotion Awareness in SE) |
| **Tipo** | Workshop paper (4 pages) |
| **Metodo** | Replication study design (biometric sensors + questionnaires) |
| **Amostra** | Planned: 30-40 BSc students |
| **Contexto** | University of Bari, Italy |

---

## Objetivo

Replicar estudo de Müller & Fritz sobre deteccao biometrica de emocoes de desenvolvedores durante tarefas de programacao.

---

## Questoes de Pesquisa

- **RQ1**: Qual e a amplitude de emocoes experimentadas por desenvolvedores durante tarefas de mudanca de codigo, e como essas emocoes se correlacionam com o progresso percebido?
- **RQ2**: Quais sao os aspectos e praticas que afetam as emocoes dos desenvolvedores durante tarefas de mudanca de codigo?
- **RQ3**: Sensores biometricos podem ser usados para determinar automaticamente emocoes de desenvolvedores e progresso durante tarefas de mudanca?

---

## Sensores e Metricas

| Sensor | Medida |
|--------|--------|
| Emotiv Insight (EEG) | Atividade cerebral, cognitive load |
| Tobii 4c (Eye Tracker) | Fixacoes, pupil dilation |
| Empatica E4 (Wristband) | EDA, BVP (blood volume pulse) |

### Escalas
- Russell's circumplex model: valence (-200 a +200)
- Perceived progress: Likert 5 pontos
- SAM (Self-Assessment Manikin): 9 pontos

### Resultado do Estudo Original (Müller & Fritz)
- ML classifier (positive/negative emotions): **71.36% accuracy**
- Writing code → melhor perceived progress (independente de correctness)

---

## Dados da Pesquisa

### Tipo de Estudo
Replication study design (design de experimento replicado) — estudo experimental controlado

### Amostra (Planejada)
- **N:** 30-40 estudantes em Computer Science (BSc level)
- **Universidade:** University of Bari Aldo Moro, Italia
- **Comparacao:** Replicacao de Müller & Fritz (2015) com amostra diferente

### Contexto
- **Ambiente:** Laboratorio (environment controlado)
- **Tarefa:** Code change tasks (modify/fix small Java programs)
- **Duracao de cada tarefa:** 30 minutos
- **Numero de tarefas:** Multiplas (conforme original, numero exato nao especificado)

### Dados Coletados

1. **Dados Biometricos (continuo durante tarefa)**
   - EEG (Emotiv Insight headset)
   - Eye tracking (Tobii 4c)
   - Biometric wristband (Empatica E4): EDA, BVP

2. **Dados de Auto-relato**
   - Emotional state ratings (apos cada tarefa)
   - Perceived progress (during and after task)
   - Task difficulty perception

3. **Dados de Performance**
   - Code correctness (task outcome)
   - Task completion time
   - Error rate

### Fontes de Dados
- Emotiv Insight EEG headset
- Tobii 4c eye tracker
- Empatica E4 wristband
- Manual questionnaire responses
- Code submission and validation

### Instrumentos de Coleta

| Instrumento | Medidas | Especificacoes |
|-------------|---------|-----------------|
| **Emotiv Insight** | EEG signals (8 channels) | Cognitive workload, engagement, frustration |
| **Tobii 4c** | Eye fixations, pupil dilation, gaze velocity | Attention, cognitive load indicators |
| **Empatica E4** | EDA, BVP (photoplethysmography) | Arousal, emotional intensity |
| **Questionnaires** | Valence/arousal ratings | 9-point Likert scales |

---

## Metricas e Instrumentos de Avaliacao

### Escalas de Medicao

#### 1. Emocoes — Russell Circumplex Model
- **Valence:** -200 a +200 scale (muito negativo a muito positivo)
- **Arousal:** 1-9 scale (muito baixo arousal a muito alto arousal)
- **Instrumento:** Self-Assessment Manikin (SAM) — 9-point pictorial scale

#### 2. Perceived Progress
- **Escala:** 5-point Likert scale
- **Items:** Questions sobre sensacao de progresso durante mudanca de codigo
- **Timing:** Avaliado apos interrupoes e apos conclusao da tarefa

#### 3. Dados Biometricos

| Sensor | Metrica | Interpretacao |
|--------|---------|-----------------|
| **EEG** | Cognitive Workload | Theta/alpha ratio; aumenta com esforco mental |
| **EEG** | Engagement/Frustration | Frequency bands especificas (nao detalhadas) |
| **Eye Tracker** | Fixation Duration | Tempo de fixacao em area; indicador de atencao |
| **Eye Tracker** | Pupil Dilation | Dilatacao pupilar; correlada com carga cognitiva |
| **Empatica E4** | EDA (Electrodermal) | Medida em µS; arousal emocional |
| **Empatica E4** | BVP (Blood Volume Pulse) | Variabilidade cardiaca |

### Machine Learning Classification

**Objetivo:** Classificar automaticamente emocoes (positivas vs negativas) a partir de sensores

**Dados do estudo original (Müller & Fritz, 2015):**
- ML classifier: supervised learning com biometric features
- **Accuracy:** 71.36% para classificacao positiva/negativa
- **Resultado principal:** Escrever codigo → percepcao melhor de progresso (independente de correctness)

### Abordagem de Validacao

**Protocolo experimental:**
1. Baseline collection (fish tank video para establecer baseline emocional)
2. Change task execution (30 minutos de trabalho em tarefa de mudanca)
3. Interruptions (fish thank video para reset emocional)
4. Repeated tasks (no minimo 6 iteracoes)

**Timing detalhado:**
- Sensors + consent: 5 minutos
- Baseline: 1 minuto (fish tank)
- Change task: 30 minutos
- Interruption: 1 minuto
- Emotional rating: 1 minuto
- Repeat 6 times (nao sequencial — breaks entre iteracoes)

### Confiabilidade e Validacao

**Validacao dos instrumentos:**
- Emotiv Insight: headset EEG nao-invasivo, validado em pesquisa anterior
- Tobii 4c: eye tracker infrared padrizado
- Empatica E4: wristband validado para EDA/BVP
- SAM scale: amplamente validada na literatura de emocoes

**Replicacao como validacao:**
- Estudo replica protocolo de Müller & Fritz (2015)
- Objetivo: confirmar ou refutar achados originais em nova amostra
- Extensao potencial para novo contexto (estudantes italiani)

---

## Limitacoes

1. **Study design only** — nao executado (workshop paper de design)
2. **Amostra de estudantes** — nao profissionais; pode nao generalizar para developers profissionais
3. **Lab setting** — nao ambiente real de trabalho (ecological validity limitada)
4. **Workshop paper (4 paginas)** — profundidade metodologica limitada

---

## Contribuicao Principal

Design de replicacao com sensores nao-invasivos de baixo custo para detectar emocoes de desenvolvedores e correlacionar com progresso percebido. Parte da agenda de pesquisa em emotion awareness in SE.

---

*Extraido em Marco 2026 para MLR: Software Developer Metrics in Practice*

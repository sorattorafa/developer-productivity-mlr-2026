# P0411 — Towards Recognizing the Emotions of Developers Using Biometrics: The Design of a Field Study

**Decisao: INCLUIDO | Qualidade: 2/5**

---

## Dados Bibliograficos

| Campo | Valor |
|-------|-------|
| **ID** | P0411 |
| **Autores** | Nicole Novielli, Daniela Girardi, Filippo Lanubile, Luigi Quaranta, Alexander Serebrenik |
| **Ano** | 2019 |
| **Venue** | SEmotion'19 (4th Int. Workshop on Emotion Awareness in Software Engineering) |
| **Tipo** | Workshop paper (field study design) |
| **Metodo** | Field study design (biometric sensors + ESM + WorkAnalytics) |
| **Amostra** | 8 desenvolvedores na Apuliasoft (piloto com 1) |
| **Contexto** | Empresa de software italiana; ambiente de trabalho real |

---

## Objetivo

Projetar um estudo de campo para reconhecimento de emocoes de desenvolvedores usando sensores biometricos em ambiente real de trabalho, estendendo validacao laboratorial para contexto ecologico.

---

## Questoes de Pesquisa

- **RQ1**: E possivel identificar emocoes experimentadas por desenvolvedores de software usando sensores biometricos durante o dia de trabalho?
- **RQ2**: Existe uma conexao entre as atividades de trabalho diarias dos desenvolvedores e as emocoes que experimentam?
- **RQ3**: Sensores biometricos nao-invasivos e de baixo custo podem ser usados para determinar emocoes de desenvolvedores e o conforto durante o trabalho?

---

## Design do Estudo

### Instrumentos
- **Empatica E4 wristband**: mede EDA (electrodermal activity), BVP (blood volume pulse), HR (heart rate), temperatura da pele
- **WorkAnalytics**: monitora atividades no desktop (coding, email, messaging, meetings)
- **ESM (Experience Sampling Method)**: auto-relato de emocoes em intervalos regulares

### Modelo Teorico
- **Circumplex model de Russell**: emocoes mapeadas em 2 dimensoes:
  - **Valence** (positivo/negativo)
  - **Arousal** (alta/baixa excitacao)
- SAM (Self-Assessment Manikin) para coleta de auto-relato

### Protocolo
1. Coleta biometrica continua via Empatica E4
2. Monitoramento de atividades via WorkAnalytics
3. Questionarios ESM periodicos
4. Piloto com 1 participante antes do estudo completo com 8

---

## Metricas Biometricas

| Metrica | Sensor | Descricao |
|---------|--------|-----------|
| EDA (Electrodermal Activity) | Empatica E4 | Condutancia da pele — indicador de arousal |
| BVP (Blood Volume Pulse) | Empatica E4 | Variabilidade cardiaca |
| HR (Heart Rate) | Empatica E4 | Frequencia cardiaca |
| Skin Temperature | Empatica E4 | Temperatura periferica |
| Valence | SAM/ESM | Auto-relato de positividade/negatividade emocional |
| Arousal | SAM/ESM | Auto-relato de nivel de excitacao |

---

## Dados da Pesquisa

### Tipo de Estudo
Field study design (estudo de campo piloto) — coleta empirica em ambiente real de trabalho

### Amostra
- **Planejado:** 8 desenvolvedores profissionais em empresa italiana
- **Piloto:** 1 desenvolvedor (teste inicial do protocolo)
- **Empresa:** Apuliasoft (software development, consulting, mobile/web focus)
- **Duracao:** Periodo nao especificado; continuous monitoring durante dias de trabalho

### Contexto
- Ambiente: Empresa real de software italiana
- Tamanho da empresa: PME (8 desenvolvedores)
- Tipo de trabalho: Software development, consulting, mobile e web development
- Periodo de coleta: Nao especificado (paper de 2019)

### Dados Coletados
Multiplos tipos de dados em paralelo:

1. **Dados Biometricos (continuo)**
   - Atividade electrodermal (EDA)
   - Variabilidade cardiaca (BVP)
   - Frequencia cardiaca (HR)
   - Temperatura da pele

2. **Dados de Atividade (desktop monitoring)**
   - Aplicacoes utilizadas e tempo
   - Transicoes entre tarefas
   - Categorias de atividade: coding, email, messaging, meetings, documentation

3. **Dados de Auto-relato (Experience Sampling)**
   - Emocoes experimentadas (ESM pop-ups periodicos)
   - Avaliacao de valence e arousal (SAM scale)
   - Conforto com dispositivos/ambiente

### Fontes de Dados
- Empatica E4 wristband (biometria)
- WorkAnalytics software (monitoramento de atividades desktop)
- Experience Sampling Method via pop-ups (auto-relato emocional)
- Observacoes diretas do pesquisador (notas qualitativas)

### Instrumentos de Coleta

| Instrumento | Medidas | Frequencia/Modo |
|-------------|---------|-----------------|
| **Empatica E4** | EDA, BVP, HR, Skin Temp | Continuo, sinal em tempo real |
| **WorkAnalytics** | App usage, window switches, task categories | Continuo em background |
| **ESM Pop-ups** | Emocoes (Likert), valence/arousal (SAM) | Periodico (interval nao especificado) |
| **Observer Notes** | Comportamento, contexto, atividades qualitativas | Ad hoc durante observacao |

### Taxa de Resposta
- Nao reportada para ESM (estudo de design apenas)
- Pilot testing com 1 desenvolvedor antes de estudo principal

---

## Metricas e Instrumentos de Avaliacao

### Escalas de Medicao

#### 1. Emocoes — Russell Circumplex Model
- **Dimensoes:** Valence (positivo/negativo) e Arousal (alta/baixa excitacao)
- **Instrumento:** SAM (Self-Assessment Manikin) — 9-point scale
- **Medicao:** Range [-200, +200] para valence; escalas continuas para arousal

#### 2. Dados Biometricos
Mappear sinais fisiologicos para estados emocionais/cognitivos:

| Sensor | Variavel | Interpretacao |
|--------|----------|-----------------|
| **EDA** | Condutancia da pele (µS) | Indicador de arousal; aumenta com stress/excitacao |
| **BVP** | Variabilidade do batimento cardiaco | Valence emocional; correlacao com afeto |
| **HR** | Batimentos por minuto (bpm) | Arousal geral; aumenta com intensidade emocional |
| **Skin Temp** | Temperatura periferica (°C) | Indicador de stress/emocao |

#### 3. Categorias de Atividade
Taxonomy de tarefas dos desenvolvedores:
- Coding/programming
- Email/communication
- Meetings/collaboration
- Documentation/testing
- Administrative/other

### Abordagem de Validacao

**Desafios metodologicos reconhecidos:**
1. Sincronizacao entre multiplas fontes de dados (biometria, desktop, auto-relato)
2. Limpeza de dados biometricos em ambiente real (ruido, artefatos de movimento)
3. Calibracao individual de thresholds biometricos
4. Validacao de correlacao entre sinais fisiologicos e auto-relato emocional

**Estrategia de analise:**
- Correlacao entre EDA/BVP/HR e ratings de emocao (ESM)
- Correlacao entre atividades (WorkAnalytics) e emocoes reportadas
- Identificacao de padroes individuais (nao genericos)

### Confiabilidade e Precisao

Nao foi reportada no design paper, mas:
- Empatica E4 validado em pesquisa anterior para EDA, BVP, HR
- SAM scale amplamente validado na literatura de emocoes
- Trade-off entre precisao e invasiveness dos sensores

### Ameacas a Validade

1. **Validade Interna:** Hawthorne effect — comportamento pode mudar sob monitoramento
2. **Validade Externa:** Empresa unica (Apuliasoft, Italia) — resultados podem ser especificos da cultura/contexto
3. **Validade Ecologica:** Sensores podem afetar naturalidade do trabalho
4. **Attrition:** Pequena amostra (8 devs) pode ter dropout

## Desafios do Uso das Metricas

1. **Sensores biometricos em ambiente real** introduzem ruido nao presente em laboratorio
2. **Trade-off validade ecologica vs controle** — perda de controle experimental
3. **Privacy concerns** com monitoramento continuo de atividades e biometria
4. **Diferencas individuais** nas respostas fisiologicas limitam modelos genericos
5. **Reatividade dos participantes** — comportamento pode mudar sob monitoramento

---

## Avaliacao de Qualidade

| Criterio | Pontuacao (0-2) |
|----------|----------------|
| Objetivo claramente definido | 2 |
| Metodologia adequada | 1 |
| Amostra/contexto descrito | 1 |
| Ameacas a validade discutidas | 1 |
| Resultados com evidencia | 0 (design only) |
| Contribuicao clara | 1 |
| **TOTAL** | **6/12 (Media-Baixa)** |

---

## Limitacoes

1. **Design paper apenas** — sem resultados empiricos
2. **Empresa unica** (Apuliasoft, Italia) — generalizacao limitada
3. **Amostra muito pequena** (8 desenvolvedores, piloto com 1)
4. **Workshop paper** (4 paginas) — profundidade limitada
5. **Modelo de ML nao validado** em campo ainda

---

## Contribuicao Principal

Design de estudo de campo para deteccao biometrica de emocoes de desenvolvedores em contexto real de trabalho, usando Empatica E4 + WorkAnalytics + ESM. Estende abordagem laboratorial (Girardi et al. 2018) para ambiente ecologico.

---

*Extraido em Marco 2026 para MLR: Software Developer Metrics in Practice*

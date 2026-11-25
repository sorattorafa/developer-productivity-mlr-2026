# P0145 — Sensing Developers’ Emotions: The Design of a Replicated Experiment

**Decisao: INCLUIDO | Qualidade: 4/5**

---

## Dados Bibliograficos

| Campo | Valor |
|-------|-------|
| **ID** | P0145 |
| **Autores** | Daniela Girardi, Filippo Lanubile, Nicole Novielli, Davide Fucci [1, 2] |
| **Ano** | 2018 [2] |
| **Venue** | 3rd International Workshop on Emotion Awareness in Software Engineering (SEmotion'18) [2] |
| **DOI** | 10.1145/3194932.3194940 [2] |
| **Tipo** | Conference paper [2] |
| **Metodo** | Replicated Experiment [1, 3] |
| **Amostra** | Planned 30 to 40 students (Bachelor's, Master's, or Ph.D.) [4] |
| **Contexto** | Academic — University of Bari, Italy [4] |
| **Modo de trabalho** | On-site (implied by the use of biometric sensors in a controlled setting) [3, 5] |
| **Metodologia** | Not specified (Programming tasks in Java) [6] |

---

## Objetivo

O principal objetivo deste artigo é propor a replicação de um estudo experimental para investigar até que ponto sensores biométricos podem ser utilizados para detectar automaticamente as emoções de desenvolvedores durante tarefas de programação, além de analisar como essas emoções se correlacionam com o progresso percebido [1, 7, 8].

---

## Questoes de Pesquisa

*   **RQ1**: What is the range of developers’ emotions during change tasks and are developers’ emotions correlated with their perceived progress? [3]
*   **RQ2**: What are aspects and practices that affect developers’ emotions and progress during change tasks? [6]
*   **RQ3**: Can we use biometric sensors to determine developers’ emotion and progress during change tasks? [6]

---

## Metricas e Instrumentos de Avaliacao

| Metrica | Categoria | Nivel | Como Coletada | Validada |
|---------|-----------|-------|---------------|----------|
| Emotional Valence and Arousal | Satisfaction | Individual | Self-Assessment Manikin (SAM) 9-point scale [9] | Yes [9] |
| Perceived Progress | Productivity | Individual | 5-point Likert scale questionnaire [10] | Partial [9] |
| Brain Activity (EEG) | Activity | Individual | Emotiv Insight headset [3, 4] | Yes [4] |
| Electro-dermal Activity (EDA) | Activity | Individual | Empatica E4 wrist band [3, 4] | Yes [4] |
| Blood Volume Pulse (BVP/PPG) | Activity | Individual | Empatica E4 wrist band [3, 4] | Yes [4] |
| Pupil Movement / Eye Tracking | Activity | Individual | Tobii 4c eye tracker [3, 4] | Yes [4] |

---

## Frameworks e Metricas

### Frameworks Referenciados
*   **Russell’s circumplex model**: APPLIED — Usado como referência para os eixos de valência e arousal nas avaliações de estado emocional [10].
*   **Agile development**: REFERENCED — Discutido como um cenário onde a detecção de estresse e frustração pode indicar se os princípios ágeis estão sendo aplicados corretamente [11].
*   **Self-Assessment Manikin (SAM)**: APPLIED — Instrumento utilizado para coleta de taxas de valência e arousal emocional [9].

### Frameworks Propostos
O artigo não propõe um novo framework, mas sim o design de uma replicação experimental baseada no estudo original de Müller e Fritz [3, 7].

---

## Fatores que Influenciam Produtividade

### Fatores Positivos
| Fator | Categoria |
|-------|-----------|
| Locating relevant source code | Technical [12] |
| Writing code (independently of correctness) | Technical [12] |
| Switching to a different task | Process [12] |
| Talking to others | Human/Collaboration [12] |
| Taking a break | Human [12] |
| Setting clear goals | Process [12] |
| Allocating sufficient resources ahead of time | Organizational [12] |

### Fatores Negativos
| Fator | Categoria |
|-------|-----------|
| Negative affective states (stress, frustration) | Human [1, 11] |
| Uneven task distribution | Process/Organizational [11] |
| Burnout and high turnover | Human/Organizational [11] |

---

## Papel da IA e Automacao

| Campo | Valor |
|-------|-------|
| Usa IA/ML? | Yes — Um classificador de Machine Learning supervisionado é utilizado para identificar emoções positivas e negativas a partir de dados biométricos [7, 12, 13]. |
| Automacao de coleta? | Yes — Coleta automatizada de sinais fisiológicos (EEG, EDA, BVP, Eye tracking) através de sensores vestíveis [3, 4]. |
| Impacto de IA na produtividade? | O estudo visa usar IA para detecção precoce de estados negativos que prejudicam a produtividade e o bem-estar mental [1, 11]. |

---

## Resultados Principais

*   O estudo original citado alcançou uma precisão de **71,36%** na identificação de emoções positivas e negativas através de dados biométricos [12].
*   A ação de escrever código tem um impacto forte no progresso percebido pelos desenvolvedores, independentemente da correção do código [12].
*   Emoções negativas, como a raiva, podem por vezes fomentar a produtividade do desenvolvedor [12, 14].
*   O nível de expertise (estudantes de doutorado vs. profissionais) não impactou significativamente as emoções sentidas durante as tarefas no estudo original [4].

---

## Desafios do Uso das Metricas

*   **Invasividade**: A necessidade de utilizar sensores não invasivos para garantir que o conforto do desenvolvedor não seja impactado durante o trabalho [15].
*   **Identificação de Gatilhos**: Dificuldade em entender os gatilhos exatos das emoções no ambiente de trabalho [11].
*   **Aplicação em Tempo Real**: O desafio de transformar a consciência emocional em ações corretivas imediatas (ex: sugerir pausas) [11].

---

## Avaliacao de Qualidade Metodologica

| Criterio | Pontuacao (0-2) |
|----------|----------------|
| Objetivo claramente definido | 2 [1, 7] |
| Metodologia adequada ao objetivo | 2 [3, 9] |
| Amostra/contexto descrito adequadamente | 2 [4] |
| Ameacas a validade discutidas | 0 (Não detalhadas nos excertos fornecidos) |
| Resultados com evidencia suficiente | 1 (Artigo de design; resultados são do estudo original) [12] |
| Contribuicao clara para pratica ou teoria | 2 [8] |
| **TOTAL** | **9/12** |

---

## Limitacoes

*   O estudo proposto foca inicialmente em uma amostra de estudantes, o que pode limitar a generalização inicial para contextos industriais seniores [4].
*   Dependência de sensores vestíveis (wearables) que, embora de baixo custo, ainda exigem o uso físico por parte dos desenvolvedores [4, 15].

---

## Contribuicao Principal

A principal contribuição é o design detalhado de um experimento de replicação que busca validar a eficácia do uso de sensores biométricos de baixo custo para o monitoramento emocional de desenvolvedores, visando apoiar o bem-estar mental e a produtividade no ciclo de vida de desenvolvimento de software [1, 7, 8].

---

*Extraido via NotebookLM em March 2026 para MLR: Software Developer Metrics in Practice*
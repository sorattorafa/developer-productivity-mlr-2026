# P0145 — Sensing Developers' Emotions: The Design of a Replicated Experiment

**Decisao: INCLUIDO | Qualidade: 3/5**

---

## Dados Bibliograficos

| Campo | Valor |
|-------|-------|
| **ID** | P0145 |
| **Autores** | Daniela Girardi, Filippo Lanubile, Nicole Novielli, Davide Fucci |
| **Ano** | 2018 |
| **Venue** | SEmotion'18 (3rd International Workshop on Emotion Awareness in Software Engineering) |
| **DOI** | 10.1145/3194932.3194940 |
| **Tipo** | Estudo Experimental - Replicação Controlada |
| **Metodo** | Experimento controlado com tarefas de mudança de código, usando múltiplos sensores biométricos (EEG, eye tracking, EDA, PPG) |
| **Amostra** | Planejado: 30-40 estudantes de engenharia de software; possível extensão para mestrado/doutorado |
| **Contexto** | Laboratório; ambiente acadêmico (cursos de Engenharia de Software) |
| **Modo de trabalho** | Presencial, ambiente controlado |

---

## Objetivo
Replicar estudo anterior de Müller e Fritz investigando o papel das emoções em engenharia de software, especificamente testando se sensores biométricos podem detectar automaticamente emoções de desenvolvedores durante tarefas de programação e investigando a relação entre emoções e progresso percebido.

---

## Questoes de Pesquisa
- **RQ1**: Qual é o espectro de emoções dos desenvolvedores durante tarefas de mudança e as emoções correlacionam com o progresso percebido?
- **RQ2**: Quais são os aspectos e práticas que afetam as emoções e progresso dos desenvolvedores durante tarefas de mudança?
- **RQ3**: Podemos usar sensores biométricos para determinar emoção e progresso durante tarefas de mudança?

---

## Metricas e Instrumentos de Avaliacao
- **Emotiv Insight**: Headset EEG (eletroencefalograma) para medir atividade cerebral
- **Empatica E4 wristband**: Medição de EDA (atividade eletrodérmica) e BVP (volume de pulso sanguíneo)
- **Tobii 4c**: Eye tracker para capturar movimento ocular
- **Russell's Circumplex Model**: Modelo bidimensional com valência e arousal
- **Self-Assessment Manikin (SAM)**: Escala de 9 pontos para auto-avaliação de emoções
- **Questionários**: Para investigar aspectos e práticas que afetam emoções
- **Machine learning classifier**: Para classificar emoções positivas/negativas a partir de dados biométricos

---

## Resultados Principais
- Design experimental detalhado para replicação foi desenvolvido
- Protocolo de 60 minutos incluindo: explicação do estudo, familiarização com sensores, tarefa de mudança (escrita de programa Java interagindo com Stack Exchange API), coleta de baseline emocional (imagens positivas/negativas), entrevista final
- Esperado: Coleta de dados biométricos baseline para calibração individual
- Integração de múltiplos sensores complementares para captura robusta de sinais fisiológicos
- Timeline detalhado do experimento desenvolvido para replicação

---

## Desafios do Uso das Metricas
- Sincronização multi-sensor: Coordenação de múltiplos dispositivos (EEG, eye tracker, pulseira, software) requer cuidadosa sincronização temporal
- Qualidade de sinal: EEG e eye tracking são sensíveis a movimentos; ambiente laboratorial necessário para minimizar artefatos
- Conforto dos participantes: Múltiplos sensores podem causar desconforto durante período prolongado (60 minutos)
- Comparabilidade com estudo original: Uso de headset EEG diferentes (Emotiv Insight vs. Neurosky MindBand original) pode afetar comparabilidade
- Calibração individual: Diferentes indivíduos podem ter diferentes respostas fisiológicas a estímulos emocionais

---

## Contribuicao Principal
O estudo fornece um protocolo experimental bem-definido para replicação de investigações sobre emoções de desenvolvedores durante tarefas de programação, utilizando sensores biométricos complementares de baixo custo e não-invasivos. A replicação visa validar achados anteriores sobre a relação entre emoções, progresso percebido e practices que melhoram bem-estar durante desenvolvimento de software, contribuindo para melhor compreensão dos fatores antecedentes de emoções em contextos de programação.

# P0179 — Leveraging Biometric Data to Boost Software Developer Productivity

**Decisao: INCLUIDO | Qualidade: 4/5**

---

## Dados Bibliograficos

| Campo | Valor |
|-------|-------|
| **ID** | P0179 |
| **Autores** | Thomas Fritz, Sebastian C. Müller |
| **Ano** | 2016 |
| **Venue** | IEEE 23rd International Conference on Software Analysis, Evolution, and Reengineering (SANER) |
| **DOI** | 10.1109/SANER.2016.107 |
| **Tipo** | Pesquisa empírica (estudo de laboratório e campo) |
| **Metodo** | Abordagem mista com sensores biométricos (Eye-tracker, EDA, HR, EEG) |
| **Amostra** | 17 participantes (lab study com 8 graduados e 11 cientistas da computação; field study com 4 profissionais de software) |
| **Contexto** | Desenvolvimento de software em ambiente real e controlado |
| **Modo de trabalho** | Presencial com equipamento biométrico |

---

## Objetivo
Investigar o potencial de dados biométricos para medir aspectos cognitivos e emocionais de desenvolvedores durante o trabalho, permitindo mensuração em tempo real de dificuldade de tarefas, progresso e interruptibilidade.

---

## Questoes de Pesquisa
- **RQ1**: Como as medidas biométricas podem capturar dificuldade de tarefas, progresso e emoções de desenvolvedores?
- **RQ2**: Como dados biométricos podem ser usados para prever interruptibilidade em tempo real?

---

## Metricas e Instrumentos de Avaliacao
- **Sensores biométricos**: Eye-tracker (Tobii TX300, EyeLink), EEG (brainwave headband), EDA/HR (wristband Neursky Mindband, SenseCore)
- **Medidas**: Taxa de piscadas oculares, fixação do olhar, atividade EEG, condutância da pele, frequência cardíaca, variabilidade HRV
- **Métricas de dificuldade**: Naive Bayes classifier com precisão de 84,4% em lab study e 78,6% em field study
- **Classificação de interruptibilidade**: 5 estados (very unlikely a very likely), com acurácia de até 43,9% em lab study

---

## Resultados Principais
- Combinação de múltiplos sensores biométricos (eye-tracking, EDA, EEG) oferece melhor poder preditivo que sensores individuais
- Possibilidade de medir em tempo real: dificuldade de tarefas, progresso do desenvolvedor e interruptibilidade
- Identificação de janelas de tempo ótimas (combinação de poucos segundos) permite alta precisão e recall na predição
- Desafios: necessidade de baselines individualizadas, variabilidade em dias/períodos, sensibilidade a fatores externos (clima, hora do dia)

---

## Desafios do Uso das Metricas
- **Privacidade e preocupações éticas**: Coleta contínua de dados biométricos levanta questões de privacidade
- **Limitações de sensores**: Falta de APIs maduras; dificuldades em coletar dados por períodos longos; sensores ainda pouco invasivos
- **Ruído em dados**: Dados biométricos afetados por variações ambientais (temperatura, luz), características individuais e estados pessoais
- **Generalização**: Desafio em aplicar classificadores treinados em um desenvolvedor para outro

---

## Contribuicao Principal
Demonstração prática de que dados biométricos coletados em tempo real durante trabalho de desenvolvimento de software podem prever com acurácia aspectos como dificuldade de tarefa, progresso e interruptibilidade, abrindo oportunidades para suporte personalizado e automático a desenvolvedores. O trabalho fornece evidências iniciais sobre a viabilidade de medidas biométricas não-invasivas em ambientes reais de desenvolvimento.

# P0144 — Towards Recognizing the Emotions of Developers Using Biometrics: The Design of a Field Study

**Decisao: INCLUIDO | Qualidade: 3/5**

---

## Dados Bibliograficos

| Campo | Valor |
|-------|-------|
| **ID** | P0144 |
| **Autores** | Daniela Girardi, Filippo Lanubile, Nicole Novielli, Luigi Quaranta, Alexander Serebrenik |
| **Ano** | 2019 |
| **Venue** | SEmotion 2019 (4th International Workshop on Emotion Awareness in Software Engineering) |
| **DOI** | 10.1109/SEmotion.2019.00010 |
| **Tipo** | Estudo Piloto - Design de Protocolo Experimental |
| **Metodo** | Estudo de campo com um participante, usando sensores biométricos não-invasivos (pulseira Empatica E4) e métodos de auto-relato (ESM) |
| **Amostra** | 1 gerente de projeto (participante piloto) de empresa de software pequena (Apuliasoft) |
| **Contexto** | Ambiente de trabalho real (empresa de software specializada em desenvolvimento web e mobile) |
| **Modo de trabalho** | Presencial em ambiente corporativo |

---

## Objetivo
Explorar a viabilidade de detectar emoções de desenvolvedores de software durante sua jornada laboral usando sensores biométricos não-invasivos e investigar a correlação entre atividades diárias de trabalho e emoções positivas/negativas experienciadas.

---

## Questoes de Pesquisa
- **RQ1**: Conseguimos identificar emoções experienciadas por desenvolvedores de software usando sensores biométricos durante seu dia de trabalho?
- **RQ2**: Existe uma conexão entre as atividades dos desenvolvedores e suas emoções?

---

## Metricas e Instrumentos de Avaliacao
- **Empatica E4 wristband**: Sensor não-invasivo para coleta de EDA (atividade eletrodérmica) e BVP (volume de pulso sanguíneo)
- **Experience Sampling Method (ESM)**: Notificações horárias com questionário pop-up para auto-avaliação de emoções
- **Russell's Circumplex Model**: Modelo bidimensional para avaliação de emoções (valência e arousal), usando escala Likert de 9 pontos
- **Self-Assessment Manikin (SAM)**: Instrumento visual para coleta de valência e arousal
- **WorkAnalytics**: Ferramenta para monitorar atividades e contexto laboral
- **Categorias de atividades**: Codificação, leitura/escrita de e-mails, ajuda a colegas, networking, reuniões, testes, design, documentação, treinamento, tarefas administrativas

---

## Resultados Principais
- Estudo piloto com um participante confirmou viabilidade do protocolo
- Conforto comprovado no uso da pulseira Empatica E4 durante dia de trabalho
- Múltiplas atividades identificadas durante o dia laboral do participante
- Protocolo de coleta de dados de duas semanas foi desenvolvido e validado
- Integração bem-sucedida entre sensores biométricos, ESM e WorkAnalytics

---

## Desafios do Uso das Metricas
- Invasividade potencial: Embora a pulseira seja não-invasiva, o uso prolongado pode causador desconforto
- Sincronização temporal: Necessidade de sincronizar timestamps entre sensores e eventos de trabalho (marcador de evento do E4)
- Privacidade: Coleta de dados contínuos requer cuidados especiais; solução foi manter dados armazenados localmente no aplicativo
- Variabilidade individual: Respostas emocionais podem variar significativamente entre indivíduos, requerendo modelos personalizados
- Ruído ambiental: Sinais biométricos podem ser afetados por atividades não-relacionadas ao trabalho

---

## Contribuicao Principal
O estudo fornece o desenho detalhado de um protocolo experimental viável para detectar emoções de desenvolvedores em ambientes reais de trabalho usando sensores biométricos não-invasivos combinados com métodos de auto-relato. A abordagem integra dados biométricos continuamente coletados com informações contextuais sobre atividades laborais, permitindo futuros estudos investigarem a correlação entre trabalho específico e estados emocionais, contribuindo para o desenvolvimento de sistemas que melhorem bem-estar e produtividade de desenvolvedores.

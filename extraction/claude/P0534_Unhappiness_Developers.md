# P0534 — On the Unhappiness of Software Developers

**Decisao: INCLUIDO | Qualidade: 4/5**

---

## Dados Bibliograficos

| Campo | Valor |
|-------|-------|
| **ID** | P0534 |
| **Autores** | Daniel Graziotin, Fabian Fagerholm, Xiaofeng Wang, Pekka Abrahamsson |
| **Ano** | 2017 |
| **Venue** | EASE '17: Proceedings of the 21st International Conference on Evaluation and Assessment in Software Engineering (June 2017) |
| **Tipo** | Estudo Misto Quantitativo e Qualitativo |
| **Metodo** | Survey online com SPANE-B e perguntas abertas, análise qualitativa com codificação temática |
| **Amostra** | 1.318 respostas válidas de desenvolvedores de software (175% de response rate esperado) |
| **Contexto** | Desenvolvedores de software globais, principalmente profissionais |

---

## Objetivo

Este artigo examina as causas e consequências da infelicidade entre desenvolvedores de software. O estudo usa uma abordagem de métodos mistos para entender (1) a distribuição de felicidade/infelicidade entre desenvolvedores (RQ1) e (2) as causas experimentadas de infelicidade enquanto desenvolvendo software (RQ2). Os autores coletam dados de 2.220 desenvolvedores de software através de survey online com foco em causas e consequências. O trabalho identifica 49 tipos de consequências de infelicidade, agrupadas em 10 categorias, e fornece recomendações para praticantes em posições de gerenciamento. Os resultados sugerem que a infelicidade não é negligenciável e tem consequências significativas no desenvolvimento de software.

---

## Questoes de Pesquisa

- **RQ1**: Qual é a distribuição de (in)felicidade entre desenvolvedores de software?
- **RQ2**: Quais são as causas experimentadas de infelicidade entre desenvolvedores enquanto desenvolvendo software?

---

## Dados da Pesquisa

### Amostra
- 2.220 respostas iniciais de desenvolvedores de software
- 1.318 respostas válidas e completas (75% de taxa de resposta, 59%)
- 78% eram desenvolvedores profissionais de software
- 13% em outros papéis (CTO, CEO, etc.)
- Idade média de nascimento: 1984 (com variação 1944-2001)
- 88 países representados
- Nacionalidades: Americana (24%), Indianas (6%), Brasileira (6%), Russa (5%), Britânica (4%)
- Experiência com software: média 8,22 anos (mediana 5-8 anos)
- Papéis variados: 33,7% sozinhos, 25,8% em empresas médias, 15,7% em grandes empresas

### Fonte de Dados
- Survey online usando plataforma esurvey Creater
- Coleta através de GitHub Archive contato de público
- Perguntas de survey: SPANE (Scale of Positive and Negative Experience)
- Perguntas abertas sobre causas de infelicidade

### Metodos de Coleta
- **Fase 1**: Survey com questões demográficas (1) e escala SPANE-B (2)
  - SPANE-B: 12 itens em escala de 5 pontos ranging from 1 (very rarely or never) to 5 (very often or always)
  - Medidas: SPANE-P (6 itens positivos), SPANE-N (6 itens negativos)
  - Scoring: SPANE-B = SPANE-P - SPANE-N (escala de -24 a +24)

- **Fase 2**: Perguntas abertas:
  - Causas de infelicidade (SQ2): "What extra activities was the wasted time spent on?"
  - Frequência de infelicidade (SQ3): "What was the source of the problem for what wasted time?"

- **Análise Qualitativa**:
  - Codificação aberta de 590 códigos iniciais
  - Merge e limpeza reduzindo a 219 códigos únicos
  - Referenciados 2.280 vezes em texto

### Periodo de Analise
- Coleta de dados durante 4 rodadas do survey piloto
- Survey piloto refinou perguntas e taxa de resposta
- Coleta final de dados durante rodadas de survey principal

---

## Metricas e Instrumentos de Avaliacao

1. **Scale of Positive and Negative Experience (SPANE-B)**:
   - Escala psicometricamente validada para medir felicidade
   - 6 itens positivos: Positive, Joyful, Happy, Satisfied, Pleased, Contented
   - 6 itens negativos: Negative, Sad, Afraid, Dissatisfied, Displeased, Discontented
   - Escala de resposta: 1-5 (very rarely/never a 5 very often/always)
   - SPANE-B = SPANE-P - SPANE-N (escala final de -24 a +24)
   - Distribuição observada: Skewness de 0.53 (ligeiramente assimétrica com cauda longa)

2. **Análise Qualitativa**:
   - **Codificação Aberta**: Identificação de 23 códigos iniciais em abertura
   - **Codificação Axial e Seletiva**: Refinamento de 590 para 219 códigos únicos
   - **Categorização Temática**: Agrupamento em 10 categorias principais de consequências
   - **Triangulação**: Validação de achados entre dados quantitativos e qualitativos

3. **Categorias Principais de Consequências**:
   - a) Consequências Internas: Low cognitive performance, Low motivation
   - b) Process Consequences: Low productivity, Delay, Communication glitches, Deviate from process
   - c) External Consequences: Code quality issues, Increased bug rate

4. **Causas Internas de Infelicidade**:
   - Software developer's own being: Being stuck in problem solving, Inadequate skills, Personal issues
   - (22 fatores internos identificados)

5. **Causas Externas de Infelicidade**:
   - Artifact and working with artifact (788): Code, Bugs, Technical infrastructure, Requirements
   - Process-related (544): Management, Organization, Methodology
   - Other (95): Não categorizadas

---

## Resultados Principais

1. **Distribuição de (In)Felicidade** (RQ1):
   - Score SPANE-B médio: 9.05 (escala -24 a +24)
   - Indicador de "happiness" - ligeiramente maior que esperado baseado em população geral (média populational ~8.0)
   - Distribuição: Slightly happy population, que necessita limitação de infelicidade
   - Resultado importante: Desenvolvedores de software são população "slightly happy"

2. **Principais Causas de Infelicidade** (RQ2):
   - **Top 10** causas e frequência:
     1. Being stuck in problem solving: 186 (Software developer's own being)
     2. Time pressure: 152 (External - process)
     3. Bad code quality and coding practice: 107 (Artifact)
     4. Under-performing colleague: 71 (People - colleague)
     5. Feel inadequate with work: 63 (Developer's own being)
     6. Mundane or repetitive task: 60 (Process)
     7. Unexplained broken code: 57 (Artifact)
     8. Bad decision making: 42 (Process)
     9. Imposed limitation on development: 40 (Artifact - technical infrastructure)
     10. Personal issues - not work related: 39 (Developer's own being)

3. **Análise de Consequências**:
   - **49 tipos de consequências** identificadas
   - Agrupadas em **10 categorias** principais
   - Categorias mais frequentes: Low productivity, Low cognitive performance, Process-related consequences

4. **Padrões Observados**:
   - **Causas Internas vs. Externas**: Mais causas externas (1.843) que internas (416)
   - **Diferenças entre Plataformas Móveis**: Android, iOS, Windows Phone têm diferentes distribuições emocionais
   - **Falta de Comunicação**: Frequente em múltiplos contextos como fator de infelicidade

---

## Desafios do Uso das Metricas

1. **Medição de Felicidade**: SPANE-B é medida psicológica - pode variar significativamente entre indivíduos
2. **Causalidade Ambígua**: Não está claro se emoção causa problema técnico ou vice-versa
3. **Codificação Qualitativa**: Processo subjetivo mesmo com múltiplos codificadores
4. **Generalização**: Amostra tem possível viés de seleção (usuários GitHub, mais educados)
5. **Confundidores Não-Controlados**: Outros fatores (pessoais, culturais) podem afetar felicidade
6. **Medida Única de Tempo**: SPANE-B mede felicidade em ponto único no tempo

---

## Avaliacao de Qualidade

| Criterio | Pontuacao (0-2) |
|----------|----------------|
| Objetivo claramente definido | 2 |
| Metodologia adequada | 2 |
| Amostra/contexto descrito | 2 |
| Ameacas a validade discutidas | 1 |
| Resultados com evidencia | 2 |
| Contribuicao clara | 2 |
| **TOTAL** | **11/12** |

---

## Limitacoes

1. Amostra limitada a GitHub developers com atividade pública - pode não representar desenvolvedor médio
2. Respondentes mais educados/tecnicamente inclinados do que população geral
3. Possível viés de self-selection - pessoas infelizes podem ser menos propensas a responder surveys
4. Dados coletados em ponto único no tempo - não captura variações temporais
5. Codificação qualitativa mesmo com múltiplos pesquisadores é ainda subjetiva
6. Não investiga relação causal entre fatores e infelicidade
7. Amostra tem mais homens que mulheres - possível viés de gênero
8. Não controla para variáveis organizacionais que possam afetar felicidade

---

## Contribuicao Principal

Este trabalho faz uma importante contribuição ao campo de human aspects of software engineering ao fornecer uma análise detalhada das causas e consequências de infelicidade entre desenvolvedores de software em escala global. A descoberta que desenvolvedores são ligeiramente felizes (SPANE-B ~9) mas experimentam infelicidade significativa em certas atividades sugere oportunidades para melhoria. A identificação de que causas externas (1.843 menções) superam causas internas (416 menções) indica que muitos fatores de infelicidade são potencialmente controláveis através de mudanças organizacionais. O artigo fornece recomendações práticas para gerentes e líderes de projeto sobre como fostering felicidade entre desenvolvedores. A descoberta de que "being stuck in problem solving" é a causa mais frequente de infelicidade sugere oportunidades para melhor suporte, ferramentas e mentoría.

---

*Extraido em Marco 2026 para MLR: Software Developer Metrics in Practice*

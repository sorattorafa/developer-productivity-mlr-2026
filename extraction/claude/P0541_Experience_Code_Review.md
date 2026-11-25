# P0541 — Understanding the Experience of Code Review: Misalignments, Attention, and Units of Analysis

**Decisao: INCLUIDO | Qualidade: 4/5**

---

## Dados Bibliograficos

| Campo | Valor |
|-------|-------|
| **ID** | P0541 |
| **Autores** | Emma Söderberg, Luke Church, Jürgen Börstler, Diederick Niehorster, Christofer Rydenfält |
| **Ano** | 2022 |
| **Venue** | EASE 2022 (26th International Conference on Evaluation and Assessment in Software Engineering) |
| **Tipo** | Estudo Exploratório Misto (Qualitative + Survey) |
| **Metodo** | Entrevistas semi-estruturadas + Survey com questões abertas |
| **Amostra** | 12 entrevistas + survey com ~76 respondentes |
| **Contexto** | Code Review - Experiência do Desenvolvedor |

---

## Objetivo

Investigar experiência de desenvolvedores em processos de code review, especificamente enfocando misalignments entre expectativas e realidade, e entre ferramentas/processos e necessidades reais. O objetivo é entender aspectos pouco estudados da experiência de code review do ponto de vista do desenvolvedor, incluindo desafios emocionais, cognitivos, e processuais.

---

## Questoes de Pesquisa

- **RQ1**: Quais são os principais misalignments na experiência de code review?
- **RQ2**: Como atenção e unidades de análise afetam a experiência?
- **RQ3**: Como melhorar design de ferramentas e processos de code review?

---

## Dados da Pesquisa

### Amostra
- Entrevistas: 12 desenvolvedores (8 participantes em company A, 4 em companies B, A, e outras)
- Survey: ~76 respondentes (52 válidas, 44 respondidas completamente)
- Experiência: 10-20 anos para maioria (1+ profissional)
- Roles: Principalmente desenvolvedores (68.2%), architects (13.6%), team leads (11.4%), testers (2.3%)

### Fonte de Dados
- Entrevistas semi-estruturadas gravadas e transcritas
- Questões de survey abertas codificadas
- Dados de 2 companhias multinacionais

### Metodos de Coleta
- Entrevistas com análise temática (thematic analysis)
- Survey online com Likert scale + free-text answers
- Análise qualitativa com Grounded Theory
- Análise quantitativa de frequências

### Periodo de Analise
- Entrevistas: Fall 2021 e início 2022
- Survey: Fall 2021
- Análise: 2021-2022

---

## Metricas e Instrumentos de Avaliacao

**Escala de Concordância (Likert Scale 1-5)**:
- Q15: "Meu time segue um processo de code review comumente acordado"
- Q16: "O processo de code review do meu time é suportado por ferramentas"
- Q17: "Meu time faz code review espesso de forma objetiva"
- Outras sobre benefícios percebidos (conhecimento, qualidade, satisfação)

**Análise Temática**: Identificação de temas em entrevistas e survey:
- Tool-Task Misalignment
- Tool-Information Misalignment
- Tool-Size Misalignment
- Process-Responsibility Misalignment
- Process-Completion Misalignment
- Developer-Automation Misalignment
- Developer-Experience Misalignment

**Análise Qualitativa**: Codificação e categorização de respostas abertas de survey

**Análise Grounded Theory**: Construção de hipóteses e conceitos a partir de dados

---

## Resultados Principais

**Sete Principais Misalignments Identificados**:

1. **Tool-Task Misalignment**: Conversas necessárias para tarefa de review não são suportadas pela ferramenta (asynchronous communication inadequate para complex changes)

2. **Tool-Information Misalignment**: Informação necessária para review não está disponível na ferramenta (falta de contexto, histórico, detalhes)

3. **Tool-Size Misalignment**: Tamanho de mudanças adequado para review não se alinha com capacidade/preferências da ferramenta/processo

4. **Process-Responsibility Misalignment**: Expectativas sobre quem é responsável por tarefa não se alineiam com realidade (confusão entre author e reviewer)

5. **Process-Completion Misalignment**: Tempo estimado vs real para completar tarefa não se alinham

6. **Developer-Automation Misalignment**: Nível de automação vs expectativas dos desenvolvedores

7. **Developer-Experience Misalignment**: Expectativas de experiência vs realidade

**Níveis de Atenção**: Desenvolvedores precisam de suporte para diferentes níveis de atenção:
- Baixo: Skim code para estrutura geral
- Médio: Revisar detalhes funcionais
- Alto: Analisar semanticamente mudanças complexas

**Unidade de Análise**: Mismatch entre unidade de análise esperada e real:
- Expectativa: Revisar por feature/tarefa lógica
- Realidade: Revisar por arquivo/mudança técnica

---

## Desafios do Uso das Metricas

1. Amostra pequena: 12 entrevistas podem não representar população completa de desenvolvedores

2. Contexto limitado: 2 companhias multinacionais grandes, generalização para PMEs questionável

3. Análise temática subjetiva: Codificação de temas por pesquisador pode conter viés interpretativo

4. Survey respondents: Apenas ~76 respondentes com 52 válidas, taxa de resposta não reportada

5. Période temporal: Estudo realizado durante pandemia (Fall 2021), condições trabalho podem ter sido atípicas

---

## Avaliacao de Qualidade

| Criterio | Pontuacao (0-2) |
|----------|----------------|
| Objetivo claramente definido | 2 |
| Metodologia adequada | 2 |
| Amostra/contexto descrito | 1 |
| Ameacas a validade discutidas | 1 |
| Resultados com evidencia | 2 |
| Contribuicao clara | 2 |
| **TOTAL** | **10/12** |

---

## Limitacoes

1. Amostra pequena (12 entrevistas)
2. Survey com responstas incompletas (44 de ~76 respondentes)
3. Contexto limitado a 2 companhias multinacionais grandes
4. Análise temática qualitativa com potencial viés do pesquisador
5. Período de coleta durante pandemia (condições atípicas)
6. Falta de grupo de controle ou comparação entre diferentes tipos de ferramentas

---

## Contribuicao Principal

O trabalho contribui com análise profunda de misalignments na experiência de code review, revelando que lacunas entre expectativas e realidade ocorrem em múltiplos níveis (ferramenta, processo, desenvolvedor). Especificamente, identifica que tools-task misalignment é maior barreira, onde ferramentas não suportam tipo de comunicação necessária para reviews complexas. Propõe que design de ferramentas de code review deveria considerar diferentes níveis de atenção que desenvolvedores precisam exercer, e alinhar unidade de análise com como desenvolvedores mentalmente estruturam mudanças (por feature/tarefa, não por arquivo). Contribui direções práticas para design de ferramentas mais efetivas que suportam experiência mais positiva para desenvolvedores engajados em code review.

---

*Extraido em Marco 2026 para MLR: Software Developer Metrics in Practice*

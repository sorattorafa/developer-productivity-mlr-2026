# P0485 — Technical Debt Cripples Software Developer Productivity: A longitudinal study on developers' daily software development work

**Decisao: INCLUIDO | Qualidade: 4/5**

---

## Dados Bibliograficos

| Campo | Valor |
|-------|-------|
| **ID** | P0485 |
| **Autores** | Terese Besker, Antonio Martini, Jan Bosch |
| **Ano** | 2018 |
| **Venue** | TechDebt '18: 2018 ACM/IEEE International Conference on Technical Debt |
| **Tipo** | Estudo Longitudinal Quantitativo e Qualitativo |
| **Metodo** | Surveys repetidos, entrevistas semi-estruturadas, análise de dados quantitativa |
| **Amostra** | 43 desenvolvedores de software em 6 fases ao longo de 10 meses |
| **Contexto** | Empresas de software industrial suecas |

---

## Objetivo

Este estudo longitudinal examina o impacto negativo de Technical Debt (TD) na produtividade de desenvolvedores de software. Ao contrário de estudos anteriores baseados em percepção, este trabalho coleta dados de 43 desenvolvedores de software ao longo de 10 meses com observações repetidas da mesma variável (tempo desperdiçado). O estudo revela que, em média, 23% do tempo total de desenvolvimento é gasto em TD, com desvio padrão de 21,15% (mediana 17,3%). O trabalho demonstra que desenvolvedores estão frequentemente forçados a introduzir novo TD devido a TD existente e que há falta de consciência entre gerentes sobre a quantidade de tempo desperdiçado com TD.

---

## Questoes de Pesquisa

- **RQ1**: Quanto tempo gasto em desenvolvimento de software é desperdiçado devido a Technical Debt?
- **RQ2**: Como está distribuído o tempo desperdiçado ao longo do período de calendário?
- **RQ3**: De quais maneiras diferentes tipos de Technical Debt afetam a quantidade de tempo desperdiçado?
- **RQ4**: Com que frequência desenvolvedores são forçados a introduzir novo Technical Debt devido a TD existente?

---

## Dados da Pesquisa

### Amostra
- 43 desenvolvedores de software em organizações suecas
- Experiência variada (2+ anos até 10+ anos)
- 56% com mais de 10 anos de experiência
- Apenas 7% com menos de 2 anos
- Nível educacional: 82% nível universitário ou superior
- Idade média: 40.8 anos (com alguns participantes na faixa de 50-60)
- Equipes com tamanho de 1 a 6+ desenvolvedores

### Fonte de Dados
- Survey online - "Survey Monkey"
- Duas sessões de coleta por semana (terças e quintas)
- Questionário auto-administrado durante os 10 meses (outubro 2016 - junho 2017)
- Entrevistas semi-estruturadas com 12 desenvolvedores e 4 gerentes
- Dados de 473 pontos de dados (múltiplas ocasiões de coleta)

### Metodos de Coleta
- **Survey Quantitativo**: Questões sobre porcentagem de tempo em TD e origem do problema
  - SQ1: Porcentagem de tempo no desenvolvimento de software gasto em TD
  - SQ2: Atividades extras nas quais o tempo foi gasto
  - SQ3: Fonte do problema para qual tempo foi gasto

- **Entrevistas Qualitativas**: 12 entrevistas com desenvolvedores, 4 com gerentes
  - Duração: 30-40 minutos
  - Gravadas digitalmente e transcritas

### Periodo de Analise
- Coleta de dados: Outubro 2016 - junho 2017 (10 meses)
- Seis fases do design de pesquisa com coleta repetida

---

## Metricas e Instrumentos de Avaliacao

1. **Métrica Primária - Tempo Desperdiçado em TD**:
   - Reportado através de survey como porcentagem de tempo total de desenvolvimento
   - Pergunta SQ1: "Do tempo que você gastou em desenvolvimento de software desde a última vez que você respondeu a essa pesquisa, que porcentagem foi gasto em Technical Debt?"
   - Respondentes forneciam estimates entre 0-100%

2. **Modelo Linear Misto (Linear Mixed Model)**:
   - Variável dependente: Proporção de tempo desperdiçado em TD
   - Transformação arcsine square root para normalizar distribuição
   - Interceptos específicos por indivíduo: yi,j = a + β1 xi,j + ... + βp xp,j + bi + eij
   - Contrastes para comparar grupos de variáveis

3. **Atividades Extras Identificadas**:
   - "Análise de código adicional"
   - "Testes adicionais"
   - "Comunicação adicional"
   - "Busca de documentação"
   - "Implementação necessária para nova implementação"
   - "Busca de work-arounds"

4. **Fontes de TD Identificadas** (5-point Likert scale):
   - "Problemas de arquitetura"
   - "Problemas de testes"
   - "Problemas de infraestrutura"
   - "Problemas de requisitos"
   - "Problemas de código"
   - "Questões relacionadas a testes"
   - Além de causas relacionadas a atividades

5. **Análise Qualitativa**:
   - Codificação aberta e axial de transcrições
   - Categorização temática de respostas de entrevista
   - Triangulação entre dados quantitativos e qualitativos

---

## Resultados Principais

1. **Distribuição de Tempo Desperdiçado em TD** (RQ1):
   - Média: 23,2% de tempo total de desenvolvimento
   - Mediana: 17,3%
   - Desvio padrão: 21,15%
   - Intervalo: 0-100% (com alguns outliers)
   - Sem padrão claro ao longo do tempo calendário

2. **Distribuição Temporal** (RQ2):
   - Menor flutuação de tempo desperdiçado observada
   - Embora haja variações em nível individual
   - Nenhuma tendência clara de sazonalidade

3. **Tipos de Atividades Extras** (RQ1/RQ3):
   - "Testes adicionais" (23%)
   - "Análise de código" (22%)
   - "Comunicação adicional" (19%)
   - "Busca de work-arounds" (17%)
   - "Documentação" (6%)
   - "Infraestrutura" (3%)

4. **Causas de TD** (RQ1/RQ3):
   - Arquitetura inadequada (17%)
   - Documentação inadequada (14%)
   - Requisitos (14%)
   - Testes inadequados (9%)
   - Problemas de código (8%)
   - E outros

5. **Introdução de Novo TD** (RQ4):
   - Quase um quarto de todas as ocasiões quando desenvolvedores encontram TD, são forçados a introduzir novo TD
   - Pesquisadores sugerem que TD existente cria "contagious debt"

6. **Consciência de Gerentes**:
   - Gerentes NÃO estão cientes da quantidade de tempo que desenvolvedores gastam em TD
   - Diferentes profissões (developers vs. managers) têm perspectivas diferentes sobre tempo desperdiçado

---

## Desafios do Uso das Metricas

1. **Auto-relato**: Desenvolvedores estimam percentual de tempo, não rastreiam automaticamente
2. **Variabilidade Individual**: Grande variação entre respondentes (0-100%)
3. **Aggregação de Tempo**: Quando múltiplas causas presentes, tempo compartilhado igualmente
4. **Definição de TD**: Diferentes entendimentos de o que constitui TD entre participantes
5. **Amostra Específica**: Apenas empresas suecas com perfil educacional elevado
6. **Período Limitado**: 10 meses pode não capturar variações sazonais maiores
7. **Causas Correlacionadas**: Difícil isolar efeito de TD específica quando correlacionada com outras

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

1. Amostra baseada em percepção - desenvolvedores estimam tempo (não rastreado automaticamente)
2. Limitado a 43 desenvolvedores em contexto sueco - generalização questionável
3. Período de 10 meses pode não capturar variações sazonais maiores
4. Diferenças entre roles (developer, manager) em consciência de TD
5. Possível viés de resposta - participantes podem subestimar ou superestimar TD
6. Não investiga relação causal explícita entre tipos específicos de TD e tempo desperdiçado
7. Estudo não controla para outros fatores que afetam produtividade
8. Definição de TD não é uniform izada entre participantes

---

## Contribuicao Principal

Este estudo faz uma importante contribuição ao quantificar empiricamente o impacto negativo de Technical Debt na produtividade de desenvolvedores em escala longitudinal. Diferentemente de trabalhos anteriores baseados em survey transversal de percepções, este estudo coleta dados de 43 desenvolvedores ao longo de 10 meses, oferecendo uma visão mais precisa de como TD afeta tempo de desenvolvimento. A descoberta que, em média, 23% do tempo de desenvolvimento é gasto em TD é significante e fornece motivação para esforços de remediação de TD. O trabalho também revela uma desconexão crítica: gerentes não estão cientes do tempo que desenvolvedores gastam em TD. A identificação de que desenvolvedores são frequentemente forçados a introduzir novo TD para lidar com TD existente sugere efeitos de "contagious debt" que precisam ser investigados. O estudo enfatiza a importância de consciência gerencial sobre os custos reais de TD para priorizar esforços de melhoria.

---

*Extraido em Marco 2026 para MLR: Software Developer Metrics in Practice*

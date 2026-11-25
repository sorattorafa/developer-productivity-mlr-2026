# P0486 — Facing up the primary emotions in Mobile Software Ecosystems from Developer Experience

**Decisao: INCLUIDO | Qualidade: 3/5**

---

## Dados Bibliograficos

| Campo | Valor |
|-------|-------|
| **ID** | P0486 |
| **Autores** | Awdren Fontão, Oswald M. Ekwoge, Rodrigo Santos, Arilo Claudio Dias-Neto |
| **Ano** | 2017 |
| **Venue** | WASHES '17: 2nd Workshop on Social, Human, and Economic Aspects of Software (May 2017) |
| **Tipo** | Estudo de Mineração de Repositório (MSR) com análise emocional |
| **Metodo** | Análise de questões Stack Overflow usando Natural Language Processing para detecção de emoção |
| **Amostra** | 1.568.377 questões de Stack Overflow relacionadas a desenvolvimento móvel |
| **Contexto** | Três ecossistemas móveis principais (Android, iOS, Windows Phone) |

---

## Objetivo

Este artigo investiga as emoções primárias experimentadas por desenvolvedores durante desenvolvimento de aplicações móveis. Os autores analisam questões de Stack Overflow dos três principais Mobile Software Ecosystems (MSECOs) - Android, iOS e Windows Phone - para identificar quais emoções (tristeza, raiva, alegria, desgosto, medo) estão envolvidas nas experiências de desenvolvimento. O estudo usa a análise léxica AlchemyLanguage API para extrair informações emocionais das questões de Stack Overflow, permitindo entender tanto a frequência quanto os tipos de emoções associadas aos diferentes ecossistemas móveis.

---

## Questoes de Pesquisa

- **RQ**: Quais são as emoções primárias mais prevalentes nos três principais MSECOs (Android, iOS, Windows Phone) com base no corpo de questões técnicas de Stack Overflow?

---

## Dados da Pesquisa

### Amostra
- 1.568.377 questões de Stack Overflow totais
- Android: 505.487 questões (32,2% do total)
- iOS: 414.303 questões (26,4%)
- Windows Phone: 252.127 questões (16,1%)
- Coleta de dados até março de 2017

### Fonte de Dados
- Stack Overflow: Repositório de Q&A comunitário para desenvolvimento
- 1.568.377 questões completas com corpo de texto
- Metadados: tags de MSECO, histórico de visualizações, respostas
- Extrato de dados disponível publicamente

### Metodos de Coleta
- Pré-processamento de conteúdo textual:
  - Remoção de snippets de código (<code>, HTML, tags)
  - Remoção de palavras-chave comuns em inglês (stop words)
  - Limpeza de pontuação e caracteres especiais

- Análise Emocional:
  - AlchemyLanguage API: Análise de emoção em texto em linguagem natural
  - Detecta emoções: Raiva, Desgosto, Medo, Alegria, Tristeza
  - Também detecta tom geral do texto

- Análise de Frequência:
  - Contagem de questões por emoção
  - Cálculo de percentuais para cada MSECO

### Periodo de Analise
- Coleta de dados: até março de 2017
- Abrange histórico completo de Stack Overflow até essa data

---

## Metricas e Instrumentos de Avaliacao

1. **Análise Léxica de Emoção**:
   - **AlchemyLanguage API**: Detecção de cinco emoções primárias:
     - Raiva (Anger)
     - Desgosto (Disgust)
     - Medo (Fear)
     - Alegria (Joy)
     - Tristeza (Sadness)

2. **Métricas de Emoção**:
   - Frequência de questões por emoção
   - Percentual de questões associadas a cada emoção
   - Comparação entre os três MSECOs
   - Palavras mais frequentes associadas a cada emoção

3. **Análise de Questões Específicas**:
   - Identificação das 5 questões mais visualizadas por emoção
   - Análise de tópicos técnicos associados a cada emoção

4. **Classificação de Emoção Primária**:
   - Determinação de qual emoção é predominante em cada questão
   - Comparação de prevalência entre plataformas

---

## Resultados Principais

1. **Distribuição Geral de Emoções** (todos os MSECOs):
   - **Tristeza (Sadness)**: Emoção mais prevalente em geral
   - **Raiva (Anger)**: Segunda mais frequente
   - **Alegria (Joy)**: Terceira
   - **Desgosto (Disgust)**: Menos comum em geral
   - **Medo (Fear)**: Também presente mas menos frequente

2. **Emoções por MSECO**:

   **Windows Phone**:
   - Tristeza (general): 25% + 23% (orange)
   - Raiva: 1%
   - Medo: 5%
   - Desgosto: 0%
   - Alegria: 15%

   **Android**:
   - Tristeza: 47% (maior prevalência)
   - Raiva: 5%
   - Alegria: 16%
   - Medo: 5%
   - Desgosto: 0%

   **iOS**:
   - Alegria: 47% (mais prevalente que Android)
   - Desgosto: 0%
   - Tristeza: 25%
   - Raiva: 26%
   - Medo: 19%

3. **Padrões Observados**:
   - Windows Phone MSECO: Predominantly sadness-related issues
   - Android MSECO: Sadness most prevalent, but also anger-related issues
   - iOS MSECO: Joy, Anger, Sadness mais balanceados

4. **Tópicos Técnicos Associados a Emoções**:
   - Tristeza: Problemas com dispositivos AVD, emuladores, falhas de build
   - Raiva: Problemas de compatibilidade, recursos indisponíveis
   - Alegria: Implementações bem-sucedidas, best practices
   - Desgosto: Questões de design e code quality

---

## Desafios do Uso das Metricas

1. **Limitação de Análise Léxica**: AlchemyLanguage pode não capturar nuances de sarcasmo ou contexto
2. **Dados não-controlados**: Questões de Stack Overflow são escritas por diferentes tipos de desenvolvedores com diferentes níveis de habilidade
3. **Texto informal**: Lenguagem coloquial e abreviações podem afetar precisão de detecção
4. **Viés de seleção**: Apenas questões que chegaram ao Stack Overflow são incluídas
5. **Emoção múltipla**: Uma questão pode expressar múltiplas emoções, classificação única é limitante
6. **Causalidade ambígua**: Não está claro se emoção é resultado do problema técnico ou afeta como desenvolvedor descreve problema

---

## Avaliacao de Qualidade

| Criterio | Pontuacao (0-2) |
|----------|----------------|
| Objetivo claramente definido | 2 |
| Metodologia adequada | 1 |
| Amostra/contexto descrito | 2 |
| Ameacas a validade discutidas | 1 |
| Resultados com evidencia | 1 |
| Contribuicao clara | 1 |
| **TOTAL** | **8/12** |

---

## Limitacoes

1. Análise léxica automatizada pode não ser precisa para textos técnicos e informais
2. Apenas questões de Stack Overflow - não captura todas as experiências de desenvolvedores
3. Possível viés em quem faz perguntas no Stack Overflow (usuários mais frustrados podem ser mais ativos)
4. Não valida resultados de análise emocional manualmente
5. Não investiga fatores causais - por que certas emoções são mais prevalentes
6. Windows Phone MSECO em declínio durante período de coleta - pode afetar representatividade
7. Limitado a texto de questões - não considera contexto de respostas ou comentários
8. Não controla para diferentes níveis de experiência de desenvolvedores

---

## Contribuicao Principal

Este trabalho contribui ao campo de developer experience ao demonstrar como mineração de repositório (MSR) pode ser usada para extrair informações emocionais sobre a experiência de desenvolvedor. A descoberta que diferentes MSECOs têm diferentes assinaturas emocionais sugere que problemas técnicos específicos afetam desenvolvedores de forma diferente dependendo da plataforma. A prevalência de tristeza em Android e Windows Phone versus alegria em iOS oferece uma perspectiva única sobre diferenças na experiência do desenvolvedor entre plataformas. O trabalho demonstra o potencial de técnicas de linguagem natural para entender aspectos emocionais da experiência de desenvolvedor através de dados de repositório disponíveis publicamente. Isso abre novos caminhos de pesquisa para entender como problemas técnicos afetam desenvolvedores emocionalmente.

---

*Extraido em Marco 2026 para MLR: Software Developer Metrics in Practice*

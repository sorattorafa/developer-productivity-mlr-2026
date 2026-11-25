# P0529 — Unhappy Developers: Bad for Themselves, Bad for Process, and Bad for Software Product

**Decisao: INCLUIDO | Qualidade: 5/5**

---

## Dados Bibliograficos

| Campo | Valor |
|-------|-------|
| **ID** | P0529 |
| **Autores** | Daniel Graziotin, Fabian Fagerholm, Xiaofeng Wang, Pekka Abrahamsson |
| **Ano** | 2017 |
| **Venue** | ICSE-Companion 2017: 39th IEEE/ACM International Conference on Software Engineering (May 2017) |
| **Tipo** | Estudo Qualitatativo Exploratório |
| **Metodo** | Survey de grandes proporções com análise qualitativa de dados abertos |
| **Amostra** | 181 participantes com respostas válidas e completas relacionadas a consequências de infelicidade |
| **Contexto** | Desenvolvedores de software globais com experiência variada |

---

## Objetivo

Este trabalho apresenta resultados de uma análise de consequências de infelicidade entre desenvolvedores de software através de um estudo de grande escala usando survey qualitativo. Os autores estabelecem que infelicidade de desenvolvedores tem consequências negativas em três dimensões: (1) para o próprio desenvolvedor (personal), (2) para o processo de desenvolvimento (process), e (3) para o produto de software (product quality). O estudo utiliza análise qualitativa de dados de survey com 181 participantes para extrair e categorizar 254 códigos relacionados às consequências de infelicidade, os quais foram agrupados em 49 tipos de consequências, posteriormente consolidadas em 10 categorias. O trabalho fornece um schema aberto de 49 consequências como dados arquivados.

---

## Questoes de Pesquisa

- **RQ**: Quais são as consequências experimentadas de infelicidade entre desenvolvedores enquanto desenvolvendo software?
  - Subquestions:
    - Como a infelicidade afeta o próprio desenvolvedor?
    - Como a infelicidade afeta o processo de desenvolvimento?
    - Como a infelicidade afeta a qualidade do produto de software?

---

## Dados da Pesquisa

### Amostra
- 181 participantes com respostas válidas e completas
- Respondentes são principalmente desenvolvedores profissionais de software (78%)
- Outros papéis: 13% (CEO, CTO, pesquisa, freelancer, estudante)
- Idade média de nascimento: 1986 (com variação 1944-2001)
- Idade média: ~31 anos (idade media 1986)
- Média de experiência com software: 8,22 anos (mediana: 5-8 anos)
- 56% têm mais de 10 anos de experiência
- Nível educacional: 86% com ensino superior

### Fonte de Dados
- Respostas de survey online
- Questões abertas sobre consequências de infelicidade
- Contato de desenvolvedor através de GitHub Archive

### Metodos de Coleta
- **Survey Design**:
  - Questões demográficas (1)
  - Escala SPANE (12 itens) para medir felicidade (2)
  - Questões abertas sobre:
    - RQ1: Causas de infelicidade durante desenvolvimento
    - RQ (este paper): Consequências de infelicidade

- **Coleta de Dados**: Envio de email para contatos do GitHub
  - Entre 97% e 98% de taxa de entrega
  - Expectativa de 2-4% de taxa de resposta
  - Participação entre 2% e 4%

- **Análise Qualitativa**:
  - Leitura de 590 textos de respostas abertas
  - Codificação inicial com 590 códigos
  - Merge/consolidação a 219 códigos únicos
  - Agrupamento em 10 categorias
  - Identificação de 49 tipos específicos de consequências
  - Triangulação entre equipe de pesquisadores

### Periodo de Analise
- Coleta de dados durante 4 rodadas do survey piloto
- Survey piloto de revisão de design questões e taxa de resposta
- Coleta final de dados para survey principal
- Período específico não claramente indicado

---

## Metricas e Instrumentos de Avaliacao

1. **Escala SPANE (Scale of Positive and Negative Experience)**:
   - 12 itens em escala 1-5
   - Mede felicidade geral, não especificamente ligada ao trabalho de desenvolvimento
   - SPANE-B (version breve usada): 6 itens positivos + 6 itens negativos
   - Medida contínua de felicidade de -24 a +24

2. **Análise Qualitativa**:
   - **Codificação**:
     - Inicial: 590 códigos de leitura de respostas abertas
     - Consolidação: Redução a 219 códigos únicos
     - Agrupamento: 49 tipos de consequências
     - Categorização Final: 10 categorias principais

   - **Categorias Identificadas**:
     - Consequências Internas (desenvolvedor's own being): Baixa performance cognitiva, baixa motivação
     - Consequências de Processo: Baixa produtividade, delay, glitches em comunicação, desvio de processo
     - Consequências Externas (produto/artefato): Qualidade de código baixa, aumento de bugs

3. **Análise de Frequência**:
   - Contagem de menções de cada tipo de consequência
   - Identificação dos 10 fatores mais frequentes
   - Comparação entre categorias

---

## Resultados Principais

1. **Distribuição de Consequências de Infelicidade**:
   - **254 códigos** de análise qualitativa
   - **49 tipos específicos** de consequências identificadas
   - **10 categorias principais**:
     - Consequências Internas: Low cognitive performance, Low motivation
     - Consequências de Processo: Low productivity, Delay, Communication glitches, Deviate from process/shortcuts
     - Consequências Externas: Low code quality, Increased bug rate, Bad decisions

2. **Impacto Primário no Próprio Desenvolvedor**:
   - **Low cognitive performance**: Desenvolvedores percebem habilidades reduzidas
   - **Low motivation**: Falta de motivação para trabalho, "feeling stupid"
   - Citações representativas:
     - "My software dev skills dropped off as I become more and more frustrated"
     - "I felt frustrated and sloppy"
     - "Getting frustrated and sloppy"

3. **Impacto no Processo de Desenvolvimento**:
   - **Low productivity**: Produtividade reduzida
   - **Delay**: Atrasos no cronograma
   - **Communication glitches**: Problemas em comunicação
   - **Deviating from process**: Shortcuts e desvios do processo estabelecido
   - Citações:
     - "I tend to feel negative or 'cranky' and make quick 'ugly' solutions"
     - "I would likely take shortcuts when enacting a software process, compromising the quality of the process itself"

4. **Impacto no Produto de Software**:
   - **Low code quality**: Qualidade de código reduzida
   - **Increased bug rate**: Maior número de bugs
   - **Bad decisions**: Decisões ruins sobre engenharia de software
   - Citações:
     - "When I feel bad about something, I write worse code"
     - "Code quality cannot be assured. So this will make my code messy and more buggy"
     - "As a result my code becomes sloppy and error prone"

---

## Desafios do Uso das Metricas

1. **Análise Qualitativa Subjetiva**: Mesmo com triangulação, codificação e agrupamento envolvem interpretação humana
2. **Tamanho da Amostra**: 181 participantes é grande mas ainda representa pequena fração de população de desenvolvedores
3. **Auto-relato**: Consequências são relatadas de memória, não observadas diretamente
4. **Causalidade**: Difícil estabelecer relação causal entre infelicidade e consequências
5. **Múltiplas Consequências**: Uma situação de infelicidade pode ter múltiplas consequências, difícil isolá-las
6. **Contextualização**: Respondentes podem ter diferentes entendimentos de o que constitui cada tipo de consequência

---

## Avaliacao de Qualidade

| Criterio | Pontuacao (0-2) |
|----------|----------------|
| Objetivo claramente definido | 2 |
| Metodologia adequada | 2 |
| Amostra/contexto descrito | 2 |
| Ameacas a validade discutidas | 2 |
| Resultados com evidencia | 2 |
| Contribuicao clara | 2 |
| **TOTAL** | **12/12** |

---

## Limitacoes

1. Amostra ainda representa pequena fração da população global de desenvolvedores
2. Viés de seleção possível - desenvolvedores infelizes podem ser menos propensos a responder surveys
3. Possível viés de sobrevivência - apenas desenvolvedores que continuaram na profissão foram survey
4. Método de contato (GitHub) pode viesar amostra em direção a desenvolvedores open-source
5. Análise qualitativa é subjetiva mesmo com múltiplos pesquisadores
6. Consequências são relatadas retrospectivamente - possível esquecimento ou distorção
7. Não separa consequências de curto vs. longo prazo
8. Não investiga severidade relativa de diferentes consequências

---

## Contribuicao Principal

Este trabalho faz uma contribuição crucial ao campo de human aspects of software engineering ao estabelecer empiricamente que infelicidade de desenvolvedores tem impactos significativos e mensuráveis em três dimensões: o próprio desenvolvedor, o processo de desenvolvimento, e a qualidade do software produzido. A análise qualitativa detalhada com 254 códigos consolidados em 49 tipos de consequências fornece um framework abrangente para entender como infelicidade se manifesta em contextos de desenvolvimento. As citações dos respondentes são especialmente valiosas, ilustrando como infelicidade afeta tangibilmente habilidades cognitivas, motivação, qualidade de código e comportamento do processo.

O resultado impactante é que infelicidade de desenvolvedor não é uma preocupação apenas pessoal/bem-estar, mas tem implicações diretas para engenharia de software e qualidade de produto. O trabalho fornece como dados abertos o schema de 49 consequências, permitindo futuras pesquisas. As implicações práticas são significantes: gerentes e líderes de projeto que ignoram felicidade de desenvolvedores correm risco de impactos negativos em produtividade, qualidade de código e dinâmica de processo.

---

*Extraido em Marco 2026 para MLR: Software Developer Metrics in Practice*

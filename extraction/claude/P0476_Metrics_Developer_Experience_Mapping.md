# P0476 — Metrics to Quantify Software Developer Experience: A Systematic Mapping

**Decisao: INCLUIDO | Qualidade: 5/5**

---

## Dados Bibliograficos

| Campo | Valor |
|-------|-------|
| **ID** | P0476 |
| **Autores** | Renata Brasil-Silva, Fábio Levy Siqueira |
| **Ano** | 2022 |
| **Venue** | SAC 2022 (37th ACM/SIGAPP Symposium on Applied Computing) |
| **Tipo** | Mapeamento Sistemático |
| **Metodo** | Revisão sistemática de literatura com protocolo estruturado |
| **Amostra** | 34 estudos primários selecionados de 1085 papers |
| **Contexto** | Engenharia de Software - Métricas de Experiência do Desenvolvedor |

---

## Objetivo

Realizar mapeamento sistemático e catálogo de métricas utilizadas para quantificar experiência do desenvolvedor em pesquisa de Engenharia de Software. O objetivo é identificar quais métricas têm sido utilizadas, como são medidas, em quais contextos, e fornecer referência estruturada sobre o estado da arte em mensuração de experiência do desenvolvedor para pesquisadores e profissionais.

---

## Questoes de Pesquisa

- **RQ1**: Quais métricas são utilizadas para medir experiência do desenvolvedor em Engenharia de Software?
- **RQ2**: Quais dados são utilizados para medir experiência do desenvolvedor?
- **RQ3**: Quais categorias/dimensões de experiência são medidas?
- **RQ4**: Qual é o objetivo dos estudos que medem experiência do desenvolvedor?
- **RQ5**: Qual é a meta/contexto dos estudos que medem experiência?

---

## Dados da Pesquisa

### Amostra
- 34 estudos primários selecionados de 1085 papers iniciais
- Publicações entre 2010 e março 2021
- Pesquisa em ACM Digital Library, IEEE Xplore, Science Direct, Web of Science, Engineering Village, Scopus

### Fonte de Dados
- Bases de dados digitais científicas
- Estudos peer-reviewed em conferências e revistas
- Documentação de projetos open-source

### Metodos de Coleta
- Busca sistemática usando strings com termos-chave (expertise, knowledge, code ownership, code ownership)
- Critérios de inclusão: métrica explícita, língua inglesa, área Software Engineering, publicação em conferência/revista/workshop
- Critérios de exclusão: métrica não definida, não English, não Software Engineering, publicação primária vs secundária, duplicatas

### Periodo de Analise
- Publicações coletadas até março 2021
- Análise realizada em 2021-2022

---

## Metricas e Instrumentos de Avaliacao

**Extraction Protocol**: Protocolo estruturado para extração de dados:
- ID, Título, Autores
- Ano, Publication name (conferência/revista/workshop)
- Research type (avaliação, validação, proposta solução, pesquisa ação)
- Research method (case study, experimento controlado, survey, pesquisa ação)
- Experience metrics utilizadas
- Dados usados (commits, linhas código modificadas, seniority, etc)
- Experience category medida (projeto, linguagem programação, programação, bug fixing, etc)
- Study goal

**Data Organization**: Dados organizados em planilhas Excel por:
- Overview data (ID, título, autores, ano, venue)
- Experience metrics
- Data sources
- Study goals

**Análise Quantitativa e Qualitativa**: Contagem de frequência de métricas, categorização temática, identificação de tendências

---

## Resultados Principais

**Distribuição de tipos de pesquisa**: 85% estudos de avaliação, 9% validação, 6% propostas de solução

**Métodos de pesquisa**: 82% case studies, 9% experimentos controlados, 6% surveys, 3% action research

**Métodos mais comuns para medir experiência**:
- Número de commits (25% dos estudos)
- Número de linhas de código (22%)
- Seniority (15%)
- Métricas baseadas em proporção de atividades (14%)

**Categorias de experiência medidas**:
- 61.5% Code
- 11% Programming
- 6.5% Programming language
- 6.5% Project
- 3% Software engineering
- 3% Libraries
- 3% Bug fixing

**Study goals**:
- 53% investigação de relação entre atividades de desenvolvedor e produtividade
- 24% proposta de novo approach para medir experiência
- 12% investigação de factors impactando experiência

---

## Desafios do Uso das Metricas

1. Heterogeneidade de definições: Mesmo conceito (expertise, experience) é definido e medido diferentemente em estudos diferentes

2. Dependência de repositórios: Maioria das métricas extrai dados de sistemas de controle de versão, que não capturam todas as dimensões de experiência

3. Limitação de dados disponíveis: Muitos estudos limitam-se a dados facilmente extraíveis (commits, linhas) em lugar de métricas mais precisas de experiência real

4. Controvérsia sobre validade de métricas: Métricas baseadas apenas em contagem de atividades não necessariamente refletem verdadeira expertise ou experiência

5. Falta de consenso teórico: Diferentes perspectivas sobre o que constitui "experiência" em desenvolvimento de software

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

1. Busca limitada a bases de dados em inglês, podendo excluir estudos em outras línguas
2. Período de análise até março 2021, não incluindo publicações mais recentes
3. Seleção manual de estudos pode introduzir viés do pesquisador
4. Foco em estudos publicados em conferências/revistas, excluindo teses e dissertações
5. Categorização de goals e métodos baseada em interpretação dos autores
6. Dados extraídos refletem estado da arte até 2021, com possível evolução posterior

---

## Contribuicao Principal

Este mapeamento sistemático fornece catálogo abrangente de 34 métricas utilizadas para quantificar experiência do desenvolvedor, identificando que métodos baseados em contagem de atividades em código (commits, linhas modificadas) dominam a literatura, porém com falta de consenso sobre definições e validade. A análise revela que maioria dos estudos (85%) são avaliativos em lugar de propositivos, e que experiência é medida predominantemente na dimensão de "código" (61.5%), sugerindo necessidade de abordagens mais multidimensionais. O trabalho contribui como referência estruturada para pesquisadores e profissionais identificarem métricas apropriadas para seus contextos específicos, além de evidenciar lacunas no estado da arte.

---

*Extraido em Marco 2026 para MLR: Software Developer Metrics in Practice*

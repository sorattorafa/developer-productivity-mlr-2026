# P0481 — On the Relationship Between Developer Experience and Refactoring: An Exploratory Study and Preliminary Results

**Decisao: INCLUIDO | Qualidade: 3/5**

---

## Dados Bibliograficos

| Campo | Valor |
|-------|-------|
| **ID** | P0481 |
| **Autores** | Eman Abdullah AlOmar, Anthony Peruma, Christian D. Newman, Mohamed Wiem Mkaouer, Ali Ouni |
| **Ano** | 2020 |
| **Venue** | ICSEW'20: IEEE/ACM 42nd International Conference on Software Engineering Workshops |
| **Tipo** | Estudo Exploratório Quantitativo |
| **Metodo** | Mineração de repositórios GitHub e análise de refatorações com RefactoringMiner |
| **Amostra** | 800 projetos Java de código aberto bem engenheirados |
| **Contexto** | Atividades de refatoração em projetos open-source |

---

## Objetivo

Este artigo investiga a relação entre a experiência do desenvolvedor e atividades de refatoração. Os autores hipotetizam que desenvolvedores com maior experiência tendem a executar mais operações de refatoração do que outros. O estudo analisa 800 projetos Java open-source para examinar a distribuição de experiência entre desenvolvedores que realizam refatorações e comparar contribuições de refatoração com scores de experiência. Os resultados confirmam que desenvolvedores mais experientes, frequentemente em posições de liderança, são responsáveis pela maioria das atividades de refatoração.

---

## Questoes de Pesquisa

- **RQ1**: Qual é a distribuição de experiência entre desenvolvedores que realizam refatorações?
- **RQ2**: Experiência mais elevada indica maior atividade de refatoração?

---

## Dados da Pesquisa

### Amostra
- 800 projetos Java open-source hospedados no GitHub
- Projetos selecionados com documentação, testes, rastreamento de problemas e gerenciamento de projetos
- Análise de 748.001 commits, dos quais 111.884 contêm pelo menos uma operação de refatoração
- Total de 711.495 operações de refatoração detectadas
- Média: 732 commits de refatoração por projeto, autorizados por 19 desenvolvedores

### Fonte de Dados
- Histórico de commits do GitHub
- Mudanças no Abstract Syntax Tree (AST) dos arquivos Java
- Dados de autores de commits e timestamps

### Metodos de Coleta
- Clonagem de repositórios GitHub em janeiro de 2019
- Uso de RefactoringMiner para detectar operações de refatoração
- Extração de informações sobre autores, arquivos modificados e timestamps
- Comparação de dados de commits com/sem refatorações

### Periodo de Analise
- Coleta de dados: Janeiro de 2019
- 74,6% dos projetos tiveram commits nos últimos 3 anos
- Análise abrange todo o histórico de cada repositório

---

## Metricas e Instrumentos de Avaliacao

1. **Developer Commit Ratio (DCR)**: Métrica de experiência baseada em contribuições
   - Fórmula: DCR = IndividualContributorCommits / TotalProjectCommits
   - Mede o volume de commits de um desenvolvedor em relação ao total do projeto
   - Proxy para experiência no projeto

2. **RefactoringMiner**: Ferramenta de detecção de refatorações
   - Precisão: 98%
   - Recall: 87%
   - Itera sobre histórico de commits comparando mudanças em arquivos Java

3. **Estatísticas Descritivas**:
   - Distribuição de scores DCR
   - Contagem de commits de refatoração vs. não-refatoração
   - Volume de operações de refatoração

4. **Testes Estatísticos**:
   - Mann-Whitney-Wilcoxon: Teste não-paramétrico de distribuições
   - Comparação de DCR entre desenvolvedores com/sem refatorações

---

## Resultados Principais

**RQ1 Resultados**:
- Desenvolvedores com refatorações têm score DCR médio de 0.0456
- Desenvolvedores sem refatorações têm score DCR médio de 0.0031
- Diferença estatisticamente significativa (p < 0.05)
- Desenvolvedores focados exclusivamente em novos features têm menos experiência

**RQ2 Resultados**:
- Top 5% de desenvolvedores (por DCR): média de 70.24 commits de refatoração e 223.7 commits não-refatoração
- Restante dos desenvolvedores: média de 3.21 commits de refatoração e 15.69 commits não-refatoração
- Top 5%: 11.14 operações de refatoração em média
- Resto: 3.57 operações de refatoração em média
- Análise qualitativa de 3 projetos (Hadoop, OrientDB, Camel) mostra que top refactoring contributors têm posições avançadas (development leads, senior developers)

---

## Desafios do Uso das Metricas

1. **Proxy de Experiência**: Usar DCR como medida de experiência é uma aproximação; pode não capturar experiência em múltiplos projetos
2. **Limitação a Java**: RefactoringMiner funciona apenas com projetos Java, limitando generalização
3. **Precisão de Detecção**: Embora alta (98% precisão, 87% recall), não detecta 100% das refatorações
4. **Contribuições do Projeto**: DCR não captura qualidade de contribuições, apenas volume
5. **Múltiplos Projetos**: Desenvolvedores podem ter experiência em múltiplos repositórios não refletida no DCR

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

1. Análise restrita a projetos Java em repositórios Git hospedados no GitHub
2. Amostra pode não ser representativa de todos os projetos open-source ou desenvolvimento corporativo
3. Medida de experiência (DCR) é baseada em volume de contribuições, não qualidade
4. Não captura experiência de desenvolvedor em múltiplos projetos ou empresas
5. Estudo limitado a repositórios com mais de 100 stars (projetos bem-conhecidos)
6. Não investiga diferenças entre tipos específicos de refatorações
7. Qualidade das refatorações não foi analisada
8. Possível viés de seleção em projetos selecionados

---

## Contribuicao Principal

Este estudo contribui ao campo de engenharia de software ao fornecer evidência empírica em larga escala que confirma a relação entre experiência do desenvolvedor e atividades de refatoração. Diferentemente de estudos anteriores que se baseavam em surveys ou estudos de casos limitados, os autores utilizam dados de repositórios reais para validar automaticamente que desenvolvedores mais experientes, frequentemente em posições de liderança, são responsáveis pela maioria das atividades de refatoração. Os resultados sugerem que é possível estimar experiência de desenvolvedores automaticamente usando dados de repositório, possibilitando futuras pesquisas sobre como experiência influencia qualidade e impacto de refatorações em escala.

---

*Extraido em Marco 2026 para MLR: Software Developer Metrics in Practice*

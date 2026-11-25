# P0521 — Developers eXperience (DX) in ALM software tools: an investigation on virtual kanban boards

**Decisao: INCLUIDO | Qualidade: 3/5**

---

## Dados Bibliograficos

| Campo | Valor |
|-------|-------|
| **ID** | P0521 |
| **Autores** | Jullia Saad, Priscila Portela Costa, Alexandre Alvaro, Luciana A. M. Zaina |
| **Ano** | 2020 |
| **Venue** | SBES '20: 34th Brazilian Symposium on Software Engineering |
| **Tipo** | Estudo Exploratório Qualitativo |
| **Metodo** | Focus Groups com análise temática |
| **Amostra** | 10 desenvolvedores de software |
| **Contexto** | Empresas brasileiras utilizando ferramentas de kanban virtual (Jira, ClickUp, Azure Boards, Airtable) |

---

## Objetivo

Este artigo examina a experiência do desenvolvedor (DX) ao utilizar ferramentas de kanban virtual em ambientes de gerenciamento de ciclo de vida de aplicações (ALM). Os autores conduziram grupos de foco com 10 desenvolvedores para entender os problemas enfrentados ao usar essas ferramentas. O estudo analisa a DX sob três perspectivas: como os desenvolvedores percebem os recursos das ferramentas, como se sentem sobre seu trabalho, e como veem o valor de suas contribuições. Os resultados evidenciam que desenvolvedores frequentemente enfrentam dificuldades em compreender o escopo do projeto a partir dos quadros kanban utilizados em seus locais de trabalho.

---

## Questoes de Pesquisa

- **RQ**: Quais problemas de Experiência do Desenvolvedor (DX) os profissionais de software enfrentam ao usar ferramentas de kanban virtual?

---

## Dados da Pesquisa

### Amostra
- 10 desenvolvedores de software com experiência variável (2 a 8 anos)
- Trabalham em diferentes organizações no Brasil
- Divididos em 2 grupos de foco (6 e 4 participantes)

### Fonte de Dados
- Grupos de foco com sessões presenciais
- Desenhos dos quadros kanban feitos pelos participantes
- Discussões em grupo sobre experiências de uso

### Metodos de Coleta
- Formulário de Consentimento Informado
- Questionário de Perfil (experiência SE, skills, características da empresa)
- Desenho de Kanban em papel durante "warm-up"
- Discussão em grupo estruturada em 4 tópicos principais
- Gravação de áudio das sessões (3 horas totais)

### Periodo de Analise
- Coleta de dados: Setembro 2019
- Duração total da pesquisa: 2 meses de coleta e análise

---

## Metricas e Instrumentos de Avaliacao

A pesquisa utiliza o framework de dimensões de DX proposto por Fagerholm, que examina três dimensões principais:

1. **Cognição (Infraestrutura de Desenvolvimento)**: Como desenvolvedores percebem plataformas, processos, procedimentos, skills
2. **Afeto (Sentimentos sobre o Trabalho)**: Respeito, apego, pertencimento, sentimentos sociais
3. **Conação (Valor da Contribuição)**: Alinhamento de objetivos, planos, intenção, motivação, comprometimento

Os dados foram analisados através de:
- **Codificação Aberta**: Identificação de 23 códigos iniciais relacionados a problemas de uso
- **Codificação Fechada**: Associação de códigos a dimensões de DX de Fagerholm
- **Refinamento**: Discussão entre pesquisadores resultando em 9 códigos finais
- **Diagrama Sankey**: Visualização das relações entre dimensões de DX e problemas identificados

---

## Resultados Principais

Os resultados identificaram 9 principais problemas de DX associados ao uso de kanban virtual:

1. **Entendimento do Escopo (C1)** - Dificuldade em compreender o escopo do projeto e objetivos através do quadro (18 ocorrências)
2. **Necessidades do Projeto (C2)** - Falta de funcionalidades para suportar trabalho diário (13 ocorrências)
3. **Complexidade (C3)** - Problemas com a complexidade das ferramentas (18 ocorrências)
4. **Número de Quadros (C4)** - Questões sobre centralização vs. múltiplos quadros (7 ocorrências)
5. **Flexibilidade (C5)** - Falta ou excesso de flexibilidade (3 ocorrências)
6. **Interface do Usuário (C6)** - Problemas com feedback e visualização (3 ocorrências)
7. **Atualização de Quadro (C7)** - Processos de atualização do quadro (1 ocorrência)
8. **Quadros Não-Sincronizados (C8)** - Diferenças entre quadros físicos e virtuais (1 ocorrência)
9. **Descrição de Problema (C9)** - Falta de informações para completar tarefas (1 ocorrência)

Os três problemas C1, C3 e C4 têm conexões com todas as dimensões de DX, indicando seu impacto abrangente na experiência do desenvolvedor.

---

## Desafios do Uso das Metricas

Os principais desafios identificados relacionados ao uso das ferramentas incluem:

1. Dificuldade em visualizar o progresso e status do projeto
2. Complexidade de ferramentas que afeta a curva de aprendizado para novos membros
3. Falta de informações contextuais sobre objetivos do projeto
4. Problemas de sincronização entre quadros físicos e virtuais
5. Inflexibilidade ou excesso de flexibilidade em configurações
6. Impacto negativo na percepção de contribuição quando tarefas não se encaixam no conceito de "card"
7. Afeta sentimentos de pertencimento e compreensão do projeto
8. Pressiona produtividade especialmente em ambientes dinâmicos

---

## Avaliacao de Qualidade

| Criterio | Pontuacao (0-2) |
|----------|----------------|
| Objetivo claramente definido | 2 |
| Metodologia adequada | 2 |
| Amostra/contexto descrito | 1 |
| Ameacas a validade discutidas | 2 |
| Resultados com evidencia | 1 |
| Contribuicao clara | 1 |
| **TOTAL** | **9/12** |

---

## Limitacoes

1. Amostra pequena (10 desenvolvedores) de organizações brasileiras - limitada generalização
2. Coleta de dados em um único ponto no tempo (setembro 2019)
3. Possível viés de interpretação mesmo com dois pesquisadores em codificação
4. Pesquisa não explorou observação direta em contextos reais de trabalho
5. Não investigou diferentes combinações de abordagens de desenvolvimento e ferramentas
6. Metodologia de desenho em papel pode não capturar toda a complexidade da experiência real
7. Análise focada principalmente em atividades de programação

---

## Contribuicao Principal

Este estudo contribui ao campo da experiência do desenvolvedor ao expandir a investigação de DX além de IDEs para ferramentas de ALM, especificamente quadros kanban virtuais. Os autores identificam que flexibilidade e complexidade das ferramentas são questões críticas que afetam todas as dimensões da experiência do desenvolvedor. O trabalho enfatiza que problemas com entendimento do escopo, afetam não apenas a percepção cognitiva dos desenvolvedores, mas também suas emoções e sentimentos sobre o trabalho e suas contribuições. Os resultados sugerem que melhorias em design de interface, flexibilidade de configuração e clareza de informações de projeto poderiam significativamente melhorar a experiência do desenvolvedor com ferramentas de kanban virtual.

---

*Extraido em Marco 2026 para MLR: Software Developer Metrics in Practice*

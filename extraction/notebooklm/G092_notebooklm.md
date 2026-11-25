# G092 — The Impact of AI Coding Assistants on Software Engineering: A Longitudinal Study

**Decisao: INCLUIDO | Qualidade GL: 6/6**

---

## Dados Bibliograficos

| Campo | Valor |
|-------|-------|
| **ID** | G092 [1] |
| **Autor/Organizacao** | Annie Vella, Kelly Blincoe (University of Auckland) [1, 2] |
| **Data** | Maio de 2026 [1, 3] |
| **Tipo** | Academic Preprint / Manuscript submitted to ACM [1-3] |
| **URL** | https://doi.org/10.5281/zenodo.18821767 (Pacote de Replicacao) [4] |

---

## Resumo

Este estudo apresenta uma investigacao longitudinal de metodos mistos que analisa como engenheiros de software profissionais percebem os efeitos de assistentes de codificacao baseados em AI no foco de tarefas, na **developer experience (DevEx)** e na **produtividade** ao longo do tempo [1, 5]. Os dados foram coletados por meio de dois questionarios online administrados com intervalo de seis meses (outubro de 2024 e abril de 2025), contando com 158 participantes elegiveis na primeira etapa (Q1), 101 na segunda (Q2) e uma coorte longitudinal emparelhada de 95 profissionais distribuida por 28 paises [1, 6-8]. Os resultados revelam uma **creation-to-verification shift**: os engenheiros relataram gastar significativamente menos tempo em tarefas de criacao rotineiras — com 82% relatando menor tempo na escrita manual de codigo —, enquanto o tempo dedicado a atividades de verificacao, como **code review** e **testing**, aumentou ou permaneceu elevado [1, 9-11].

Os autores propoem a categoria de **supervisory engineering work**, uma nova dimensao do trabalho de desenvolvimento nao capturada pelos modelos tradicionais de **SDLC** [1, 9, 12]. Essa categoria abrange tres funcoes de supervisao fundamentais ao interagir com ferramentas de AI: **directing** (especificar intencao, elaborar prompts e fornecer contexto), **evaluating** (ler e avaliar as sugestoes geradas) e **correcting** (corrigir erros, integrar codigo e manter a consistencia) [12]. A analise tematica qualitativa indica que, embora a AI comprima a criacao de **boilerplate code** e acelere a busca de informacoes, os desenvolvedores realocam um esforço consideravel para supervisionar e validar os resultados gerados [12-15].

Alem disso, a pesquisa documenta o **productivity-experience paradox**: enquanto as percepcoes de ganho de produtividade permaneceram estaveis e elevadas em 84% em ambos os pontos no tempo, a **developer experience** apresentou uma visivel erosao longitudinal [1, 16, 17]. Especificamente, a proporcao de participantes emparelhados que relataram piora na DevEx em pelo menos uma dimensao quase dobrou de 14% para 27%, impulsionada principalmente pela degradacao do **flow state** (que afetou 76% da coorte negativa no Q2) e pelo aumento da carga cognitiva decorrente de interrupcoes constantes, verificacao continua e iteracao de prompts [1, 16, 18-20].

---

## Frameworks Mencionados

- **DevEx Framework (Noda et al., 2023)**: Discutido e aplicado como estrutura principal para mensurar tres dimensoes: **feedback loops**, **cognitive load** e **flow state** [21-23]. O estudo constatou que, embora os **feedback loops** tenham melhorado significativamente com o uso de AI, o **flow state** e a **cognitive load** apresentaram degradacao, indicando que a relacao tradicional entre DevEx e produtividade opera de forma diferente em workflows assistidos por AI [1, 18, 20, 24].
- **DORA (State of AI-assisted Software Development)**: Discutido e citado na revisao da literatura sobre pesquisas do setor referentes a adocao de ferramentas de AI e produtividade de desenvolvedores [25, 26].
- **SPACE Framework (Houck et al. / Noda et al.)**: Discutido e citado na literatura para contextualizar a medicao do impacto da AI no trabalho de engenharia [27].
- **Vee Model (Mooz & Forsberg, 2006)**: Discutido e utilizado para categorizar as tarefas de desenvolvimento entre atividades de criacao (**designing**, **writing**, **refactoring**) e verificacao (**reviewing**, **testing**, **debugging**) [28].
- **Taxonomias Tradicionais de SDLC**: Criticadas por nao capturarem as novas atividades de supervisao e direcao que surgem no desenvolvimento assistido por AI (**supervisory engineering work**) [12, 29, 30].

---

## Metricas Mencionadas

- **Reducao no Tempo de Escrita de Codigo (Writing Code)**: 82% dos participantes relataram gastar menos tempo escrevendo codigo no Q2 (pontuacao media de 1.93 em escala de 1 a 5, reduzida de 2.10 no Q1) [1, 10, 31, 32].
- **Ganho de Produtividade Percebido**: 84% dos participantes relataram melhoria na produtividade tanto no Q1 (media 4.08) quanto no Q2 (media 4.03), apresentando alta estabilidade longitudinal (77% mantiveram avaliacoes identicas) [1, 16, 33].
- **Erosao na Developer Experience (Negative Cohort)**: A proporcao de participantes da coorte longitudinal que relataram piora na DevEx em pelo menos uma dimensao aumentou de 14% no Q1 (\\(n=13\\)) para 27% no Q2 (\\(n=25\\)) [1, 16, 34].
- **Dimensoes de DevEx (Feedback Loops, Cognitive Load, Flow State)**:
  - **Feedback Loops**: Apresentou melhoria estatisticamente significativa do Q1 (media 3.73) para o Q2 (media 3.95, \\(p=0.038\\), \\(r_{rb} = 0.38\\)); 62% relataram melhoria no Q1 e 69% no Q2 [18, 24, 35].
  - **Cognitive Load**: Apresentou declinio nao significativo do Q1 (media 3.74) para o Q2 (media 3.60); 66% relataram melhoria no Q1, caindo para 54% no Q2 [18, 24, 35].
  - **Flow State**: Apresentou declinio nao significativo do Q1 (media 3.54) para o Q2 (media 3.36); 53% relataram melhoria no Q1, caindo para 46% no Q2, enquanto avaliacoes negativas subiram para 21% (representando 76% do grupo negativo no Q2) [16, 18, 24, 35].
- **Escore de Equilibrio Criacao-Verificacao (Balance Score)**: O escore de equilibrio entre verificacao e criacao aumentou significativamente de 0.26 no Q1 para 0.53 no Q2 (\\(p=0.006\\), \\(r_{rb} = 0.39\\)) [11, 36].
- **Diversificacao de Ferramentas de AI**: O numero medio de ferramentas utilizadas por participante aumentou de 1.9 (\\(SD=0.8\\)) no Q1 para 2.9 (\\(SD=1.6\\)) no Q2, com 82% alterando suas combinacoes de ferramentas [37]. O uso de ChatGPT e GitHub Copilot caiu de 70% para 58–60%, enquanto o Cursor cresceu de 16% para 29% e o Claude cresceu de 15% para 36% [37, 38].
- **Principais Preocupacoes com AI**: A qualidade do codigo (**Quality**) foi a principal preocupacao no Q1 (44%) e Q2 (36%), seguida por seguranca (**Security**, 25% para 23%). A preocupacao com reusabilidade e manutencao (**Maintainability**) apresentou crescimento estatisticamente significativo, subindo de 3% no Q1 para 19% no Q2 (\\(p=0.003\\)) [10, 38].
- **Frequencia de Uso Diario**: 57% dos participantes utilizavam assistentes de AI diariamente no Q1, subindo para 61% no Q2 [39].

---

## Insights para Praticantes

- **Preparacao para o Trabalho de Engenharia Supervisora**: Engenheiros individuais devem se preparar para uma mudanca em sua rotina, dedicando menos tempo a escrita manual de codigo e mais tempo a tarefas de **directing**, **evaluating** e **correcting** saídas de AI [12, 40].
- **Desenvolvimento de Calibracao de Confianca e Verificacao**: Habilidades criticas passam a incluir supervisao cética, saber quando aceitar ou rejeitar sugestoes e decompor tarefas em modulos menores para conter alucinacoes e desvios das LLMs, em vez de depositar confianca passiva na ferramenta [40-43].
- **Monitoramento Organizacional de DevEx e Produtividade**: Organizacoes devem reconhecer que ferramentas de AI nao geram economia pura de tempo e precisam monitorar a **developer experience** (especialmente **flow state** e **cognitive load**) em conjunto com metricas de saída para identificar precocemente sinais de atrito, fadiga ou workflows insustentaveis [20, 44].
- **Politicas Flexiveis de Ferramental**: Empresas devem incentivar a experimentacao com conjuntos diversificados de ferramentas em vez de impor uma unica ferramenta padronizada, dada a rapida evolucao do ecossistema de software [44, 45].
- **Evolucao dos Curriculos Educacionais**: Educadores devem ensinar habilidades de colaboracao humano-AI, avaliacao critica de codigo e capacidade de supervisao ao lado da programacao tradicional, adaptando metodos de avaliacao para testar a compreensao conceitual em vez da mera geracao de codigo [46].

---

## Avaliacao de Qualidade GL (Garousi et al.)

| Criterio | Pontuacao (0-1) |
|----------|----------------|
| Autoridade do autor/organizacao | 1 |
| Descricao de metodologia | 1 |
| Data de publicacao | 1 |
| Objetividade (vies comercial) | 1 |
| Referencias citadas | 1 |
| Contribuicao nova | 1 |
| **TOTAL** | **6/6** |

---

*Extraido via NotebookLM em October 2026 para MLR: Software Developer Metrics in Practice*

🔍 Se precisar de uma comparacao com outros estudos da sua revisao ou de um relatorio consolidado sobre DevEx em AI, me avise!
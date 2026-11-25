# P2079 — Understanding ADHD Developers' Challenges Through the Lens of Developer Experience: A Qualitative Study of the r/ADHD_Programmers Community on Reddit

**Decisao: INCLUIDO | Qualidade: 5/5** [1-4]

---

## Dados Bibliograficos

| Campo | Valor |
|-------|-------|
| **ID** | P2079 |
| **Autores** | Natalya Goelzer, Sofia Sartori, Tatiana Cartagena, Karina Kohl, Gabriel Velloso, Sabrina Marczak [5, 6] |
| **Ano** | 2026 [7] |
| **Venue** | Simpósio Brasileiro de Engenharia de Software (SBES 2026) [7] |
| **DOI** | Não especificado no artigo (DOI do pacote de replicação: 10.6084/m9.figshare.32162535) [8] |
| **Tipo** | Conference paper [7] |
| **Metodo** | Qualitative (Reflexive Thematic Analysis) [7, 9, 10] |
| **Amostra** | 241 comentários provenientes de 10 threads do subreddit r/ADHD_Programmers (filtrados a partir de um corpus inicial de 115 threads e 1.441 comentários) [2, 11] |
| **Contexto** | Industry / Mixed (desenvolvedores de software com TDAH autoidentificado relatando experiências reais de trabalho em um fórum público de suporte entre pares) [6, 9, 12] |
| **Modo de trabalho** | Mixed (Work from home / Remote, Hybrid, On-site mencionados nos relatos dos participantes) [13, 14] |
| **Metodologia** | Mixed / Agile (práticas ágeis, user stories, sub-tarefas, sprints, quadros Kanban e CI/CD descritos nos relatos) [15-17] |

---

## Objetivo

O objetivo principal do artigo é investigar como desenvolvedores de software com Transtorno do Espectro do Deficit de Atenção e Hiperatividade (TDAH) percebem e navegam pelas três dimensões fundamentais da Developer Experience (DevEx) — estado de flow, carga cognitiva e loops de feedback — no trabalho diário de desenvolvimento [6, 7]. O estudo busca reinterpretar o conteúdo dessas dimensões sob a ótica das funções executivas (FE), identificando como as demandas de regulação de atenção e memória reconfiguram a experiência de desenvolvimento e propondo melhorias de processos para a engenharia de software [6, 7, 18].

---

## Questoes de Pesquisa

- **RQ1**: Under what personal, task, and team conditions do ADHD developers enter, sustain, or lose flow during development? [1]
- **RQ2**: What sources of cognitive load arise across tools, processes, and coordination, and which conditions mitigate or intensify this load? [1]
- **RQ3**: What properties of feedback loops do ADHD developers report in everyday work, and with what effects on attention regulation and task progress? [1]

---

## Metricas e Instrumentos de Avaliacao

| Metrica | Categoria | Nivel | Como Coletada | Validada |
|---------|-----------|-------|---------------|----------|
| **Reddit Thread Score** | Activity / Community Validation | Thread / Individual | Raspagem automatizada via Python Reddit API Wrapper (PRAW) com ponto de corte Score > 400 [11, 12] | Yes (usada como filtro de validação e relevância comunitária IC3) [11, 19] |
| **Dimensões DevEx (Flow State, Cognitive Load, Feedback Loops)** | DevEx / Satisfaction | Individual | Análise temática reflexiva qualitativa de 241 comentários codificados indutivamente e dedutivamente [7, 10, 20] | Partial (fundamentada nos modelos conceituais de DevEx da literatura) [21, 22] |

---

## Frameworks e Metricas

### Frameworks Referenciados
- **DevEx Framework (Noda et al. / Greiler et al. / Forsgren et al.)**: REFERENCED & APPLIED — Utilizado como conceito sensibilizador para organizar a análise qualitativa nas dimensões de Flow State, Cognitive Load e Feedback Loops [7, 10, 21, 22].
- **Executive Functions Framework (Brown's 6 EF Clusters)**: REFERENCED & APPLIED — Aplicado para mapear os mecanismos cognitivos (Ativação, Foco, Esforço, Emoção, Memória e Ação) subjacentes às dimensões de DevEx [23-25].
- **Agile / Scrum / Kanban Frameworks**: REFERENCED — Mencionados nos relatos dos desenvolvedores como mecanismos práticos de externalização de estado e estruturação de tarefas [15, 16, 26].

### Frameworks Propostos
- **Executive-Function Grounded DevEx Framework (Modelo de Dinâmica Regulatória de DevEx para TDAH)**: O artigo propõe uma reinterpretação estrutural do DevEx ancorada nas funções executivas compartilhadas [6, 27, 28]. O modelo formaliza três configurações recorrentes de trabalho:
  1. *Loss Configuration*: Loops de feedback longos forçam a reconstrução de contexto, elevando o custo de reentrada após interrupções, aumentando a carga cognitiva e esgotando os recursos que protegem o flow [27].
  2. *Support Configuration*: Loops curtos, definição clara de pronto ("definition of done"), estado externalizado e autonomia delimitada reduzem a carga e canalizam o hiperfoco para tarefas de valor [27].
  3. *Mixed Configuration*: Mecanismos cujos efeitos variam dependendo do contexto (ex.: projetos paralelos que absorvem tempo ocioso, mas podem diluir a profundidade) [27, 28].

---

## Fatores que Influenciam Produtividade

### Fatores Positivos
| Fator | Categoria |
|-------|-----------|
| **Hiperfoco (Hyperfocus)**: Estado de imersão profunda e intensa ativado pelo interesse e novidade na resolução de problemas complexos [13, 29, 30] | Human |
| **Significado e Autonomia no Trabalho**: Tarefas desafiadoras, trabalho arquitetural/conceitual e flexibilidade de horários [13, 31, 32] | Organizational / Human |
| **Estratégias de Externalização Cognitiva**: Uso de diagramas, notas externas, mapas conceituais e Kanban para descarregar a memória de trabalho [16, 33, 34] | Technical / Process |
| **Micro-tasking / Decomposição de Tarefas**: Quebra de requisitos em micro-tarefas (5-10 min ou sub-tarefas de 1-2 dias) com entregas frequentes [15, 16] | Process |
| **Âncoras de Intenção via Commits**: Commits frequentes e redação prévia da mensagem de commit para registrar a intenção e recuperar o contexto rapidamente [34, 35] | Technical / Process |
| **Suporte de Equipe e Duplicação de Corpo (Body Doubling)**: Parceiros de responsabilidade (accountability buddies), check-ins frequentes e suporte gerencial empático [14, 30, 36] | Organizational / Human |
| **AI Scaffolding (IA como Suporte de Execução)**: Ferramentas de IA (ex.: Cursor, LLMs) para estruturar rotinas, gerar documentos de planejamento, refatorar código e manter o ritmo [34, 37] | Technical |
| **Checklists e Templates Preflight**: Checklists visíveis e padronizados para guiar processos sem demandar esforço de memória [34, 38] | Process / Technical |

### Fatores Negativos
| Fator | Categoria |
|-------|-----------|
| **Interrupções Não Planejadas e Trabalho Reativo**: Chamadas, pings e chamados operacionais (on-call) que destroem o estado da tarefa e exigem reinício do zero [39, 40] | Organizational / Process |
| **Requisitos Obscuros e Ambiguidade de Escopo**: Indefinição do "definition of done" e metas vagas, desencadeando paralisia executiva e negligência de metas [14, 33, 41] | Process / Organizational |
| **Sobrecarga da Memória de Trabalho**: Limitações na RAM mental ao tentar manter múltiplos estados de código ou arquiteturas simultaneamente [30, 42] | Human / Technical |
| **Código Confuso e Documentação Deficiente**: Necessidade de percorrer bases de código antigas e mal documentadas via "algoritmo de backtracking" [30, 43] | Technical |
| **Reuniões e Interrupções Agendadas**: Standups em horários ruins que deixam o desenvolvedor em "modo de espera" antecipatório durante todo o dia [14, 40] | Process / Organizational |
| **Micromanagement e Monotonia**: Falta de autonomia e tarefas repetitivas ou já resolvidas que minam a motivação executiva [32, 40] | Organizational / Human |
| **Pressão de Prazos e Ansiedade**: Prazos curtos que geram ciclos de ansiedade e dependência de ativação por crise [30, 44] | Organizational / Human |
| **Fricção de Ferramentas de IA (AI Feedback Friction)**: IA que esquece regras prévias, repete erros ou exige supervisão constante, elevando a carga cognitiva de revisão [34, 45] | Technical |
| **Atraso nos Loops de Feedback (Wait Latency)**: Pipelines lentos ou demoras em code reviews que quebram o contexto de atenção [27, 34] | Technical / Process |
| **Burnout e Exaustão Regulatória**: Esgotamento motivacional ("I am so cooked") resultante do esforço contínuo para reconstruir contexto e defender o foco [40, 46] | Human / Organizational |

---

## Papel da IA e Automacao

| Campo | Valor |
|-------|-------|
| **Usa IA/ML?** | Yes — O estudo analisa explicitamente a percepção dos desenvolvedores sobre o uso de ferramentas de IA generativa (ex.: ChatGPT, Cursor, LLMs) no fluxo de trabalho [37, 45]. |
| **Automacao de coleta?** | Yes — A coleta de dados foi automatizada usando o Python Reddit API Wrapper (PRAW) com filtragem quantitativa e lexical programada [11, 12]. |
| **Impacto de IA na produtividade?** | Impacto ambivalente / duplo: por um lado, atua como um andaime para funções executivas (scaffolding), auxiliando no planejamento, refatoração e continuidade [37]; por outro, gera fricção quando a IA é inconsistente ou "esquecida", exigindo supervisão constante e gerando trabalho repetitivo de correção [45, 47]. |

---

## Resultados Principais

- **Amostra e Corpus Analisado**: A análise qualitativa final cobriu **241 comentários** extraídos de **10 threads** populares (filtrados de um total inicial de 115 threads e 1.441 comentários) do subreddit r/ADHD_Programmers [2, 11].
- **Estrutura Codificada**: A análise temática reflexiva produziu **362 códigos**, consolidados em **33 subtemas** e **15 temas** organizados nas três dimensões da DevEx [48].
- **Dinâmica do Estado de Flow (RQ1)**:
  - O flow para desenvolvedores com TDAH não é apenas um estado em que se entra facilmente, mas um recurso frágil que precisa ser ativamente defendido contra interrupções [6, 7, 39].
  - O hiperfoco é involuntário e dependente de interesse/novidade, podendo levar a episódios severos de exaustão pós-engajamento [13, 46, 49].
  - Interrupções e reuniões agendadas fragmentam o dia, colocando os desenvolvedores em "waiting mode" e forçando o reinício da tarefa a partir do zero ("starting from 0") [14, 50].
- **Mecanismos de Carga Cognitiva (RQ2)**:
  - A carga cognitiva é impulsionada mais pela lacuna entre a demanda da tarefa e a capacidade executiva disponível do que pela complexidade intrínseca do código [6, 25, 42].
  - Requisitos ambíguos causam paralisia executiva e esquecimento do objetivo principal durante a implementação [26, 33, 41].
  - Estratégias de externalização (micro-tarefas de 5-10 min, quadros Kanban físicos/digitais, Pomodoro e diagramas) funcionam como memória auxiliar para descarregar a RAM mental [15, 16, 33].
- **Papel dos Loops de Feedback (RQ3)**:
  - Loops de feedback atuam como reguladores externos de atenção; a confiabilidade e a persistência das informações importam tanto quanto a velocidade da resposta [6, 27, 51].
  - Desenvolvedores reaproveitam ferramentas de controle de versão, utilizando commits frequentes e mensagens de commit escritas *antes* da codificação como âncoras de memória para retomar o contexto [35, 47].
  - Assistentes de IA (ex.: Cursor) atuam como parceiros de feedback com papel duplo: fornecem suporte executivo para refatoração e planejamento, mas aumentam a carga de supervisão quando esquecem orientações ou hallucinam soluções [37, 45, 47].
- **Integração e Implicações para Processos**:
  - As estratégias autônomas criadas por desenvolvedores com TDAH (ex.: checklists, commits frequentes, definições claras de pronto) representam candidatas a melhorias de processos para toda a equipe de engenharia, e não apenas acomodações individuais [6, 18].

---

## Desafios do Uso das Metricas

- **Pressuposto de Homogeneidade Cognitiva**: As métricas tradicionais de DevEx e produtividade assumem um baseline neurotípico de atenção e memória estáveis, falhando em capturar as variações na capacidade executiva de desenvolvedores neurodivergentes [52, 53].
- **Foco Exclusivo na Latência de Feedback**: Concentrar-se apenas em reduzir a latência de ferramentas pode ser prejudicial se o feedback for instável ou não confiável (como em ferramentas de IA que esquecem contexto), gerando carga de supervisão adicional [27, 45, 47].
- **Métricas de Produtividade Baseadas em Saída Linear**: Medições tradicionais ignoram os padrões não lineares de trabalho do TDAH (picos de hiperfoco seguidos por necessidade de recuperação ou dias bloqueados por reuniões) [14, 44, 54].
- **Acomodações Formais Burocráticas vs. Design de Processo**: Processos formais de acomodação dependem de divulgação e aprovação burocrática (gerando estigma); em contrapartida, ajustar o design do processo (ex.: histórias curtas, comunicação assíncrona) é mais sustentável [18, 26].
- **Custo Invisível das Interrupções**: Métricas convencionais não computam o custo cognitivo real da reconstrução de contexto gerado por interrupções não planejadas em desenvolvedores com limitação de memória de trabalho [39, 55].

---

## Avaliacao de Qualidade Metodologica

| Criterio | Pontuacao (0-2) |
|----------|----------------|
| Objetivo claramente definido | 2 |
| Metodologia adequada ao objetivo | 2 |
| Amostra/contexto descrito adequadamente | 2 |
| Ameacas a validade discutidas | 2 |
| Resultados com evidencia suficiente | 2 |
| Contribuicao clara para pratica ou teoria | 2 |
| **TOTAL** | **12/12** |

---

## Limitacoes

- **Diagnóstico Autoidentificado**: A condição de TDAH dos participantes é autorrelatada pelos usuários do Reddit e não pôde ser verificada clinicamente [3].
- **Ausência de Validação Clínica Especializada**: A equipe de pesquisa é formada por pesquisadores de engenharia de software sem treinamento clínico formal em psicologia ou psiquiatria, o que impede a validação especializada dos constructos clínicos [3].
- **Viés de Plataforma e Amostragem**: Os dados foram coletados exclusivamente no r/ADHD_Programmers em um intervalo de seis meses (início de 2025), refletindo uma audiência de língua inglesa e favorecendo narrativas de alta popularidade devido ao filtro de Score > 400 [3, 11, 56].
- **Saliência do Momento das Ferramentas de IA**: Os resultados refletem a forte presença e discussão recente sobre ferramentas de desenvolvimento assistidas por IA (ex.: Cursor) no início de 2025 [56].
- **Ausência de Grupo de Controle**: O estudo foca especificamente em relatos de desenvolvedores com TDAH sem realizar uma comparação quantitativa direta com um grupo neurotípico no mesmo ambiente [3, 7].

---

## Contribuicao Principal

A principal contribuição do artigo é conectar a Developer Experience (DevEx) à neurodiversidade, demonstrando que as três dimensões fundamentais da DevEx (flow, carga cognitiva e loops de feedback) mantêm sua estrutura operacional, mas têm seu conteúdo profundamente reconfigurado e amplificado pelas funções executivas [6, 7, 57]. Ao analisar evidências empíricas da comunidade r/ADHD_Programmers, o trabalho reframe o flow como um recurso frágil a ser defendido, a carga cognitiva como decorrente do gap de capacidade executiva e os loops de feedback como reguladores externos da atenção [6, 7, 25, 47]. Além disso, o estudo desloca o debate sobre o TDAH na engenharia de software de políticas de acomodação individual para o design de processos, mostrando que as estratégias adotadas por desenvolvedores neurodivergentes servem como melhorias de processos para benefício de toda a equipe [4, 18].

---

*Extraido via NotebookLM em October 2026 para MLR: Software Developer Metrics in Practice*
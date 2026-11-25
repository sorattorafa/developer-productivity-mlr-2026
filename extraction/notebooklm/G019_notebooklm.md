Aqui está o resumo estruturado da sua fonte, seguindo exatamente o formato solicitado:

# G019 — The 21 Developer Productivity Metrics You Should Measure

**Decisao: INCLUIDO | Qualidade GL: 3/6**

---

## Dados Bibliograficos

| Campo | Valor |
|-------|-------|
| **ID** | G019 |
| **Autor/Organizacao** | Zach Westall / LinearB |
| **Data** | 22 de Novembro de 2024 (Publicação) |
| **Tipo** | Artigo de Blog (Blog Post) |
| **URL** | Fonte proveniente do site/blog da LinearB |

---

## Resumo

Este artigo, publicado no blog da LinearB, argumenta que a avaliação da produtividade de desenvolvedores não deve se basear em métricas de produção ou *outputs*, como linhas de código, que frequentemente prejudicam a motivação e incentivam a manipulação do sistema à custa da qualidade. Em vez disso, propõe que a produtividade é um conceito multifacetado dividido em três áreas chave (os "três Es"): Eficiência (*Efficiency*), Eficácia (*Effectiveness*) e Experiência (*Experience*).

O texto explora 21 métricas inseridas nestas categorias e fornece um guia prático para líderes de engenharia usarem esses dados para gerar melhorias reais. As principais recomendações de uso incluem a definição de metas de equipe embasadas em dados operacionais, a adoção de fluxos de automação para reduzir o esforço manual (*toil*) em processos críticos, e o uso da transparência dos dados para enriquecer e remover vieses das reuniões 1:1, avaliações de desempenho e cerimônias ágeis. 

---

## Frameworks Mencionados

*   **DORA metrics**: É explicitamente mencionado que as quatro métricas do framework DORA fazem parte das recomendações, sendo incluídas no pilar de Eficiência (como CFR e MTTR).
*   **SMART**: Recomendado como estrutura para a criação de metas específicas para as equipes.
*   **OKRs (Objectives and Key Results)**: Sugeridos como o ponto de partida em nível organizacional que deve ser desdobrado em metas para as equipes de desenvolvimento.

---

## Metricas Mencionadas

O artigo organiza as 21 métricas nos seguintes pilares:

**Eficiência (Efficiency):**
*   **Cycle Time**: Tempo percorrido desde o *pull request* (PR) até a produção.
*   **PR Maturity**: Minimização de ciclos de revisão (idas e vindas) no PR.
*   **PR Size**: Tamanho do PR, considerado um indicador líder de eficiência geral.
*   **Code Churn and Rework**: Frequência de retrabalho ou revisões no código.
*   **Stability (CFR and MTTR)**: Taxa de falha (CFR) e tempo médio de recuperação (MTTR).
*   **Cognitive Load**: Nível de quebra de atenção, multitarefa ou sobrecarga.
*   **Task Completion**: Rapidez na conclusão e transição de tarefas.

**Eficácia (Effectiveness):**
*   **Alignment with Business Goals**: Nível de alinhamento das tarefas com os objetivos estratégicos da empresa.
*   **Resource Allocation**: Alocação adequada de pessoas aos projetos certos.
*   **Accuracy Scores**: Precisão de planejamento (escopo) vs. precisão de capacidade (flexibilidade).
*   **Meaningful Contributions**: Contribuições significativas e com impacto tangível na unidade de negócio.
*   **Consistency**: Consistência e melhoria contínua do tempo de ciclo e das entregas.
*   **Balancing New Value and Maintenance**: O equilíbrio ideal entre a criação de novas *features* e as manutenções de sistemas.

**Experiência (Experience):**
*   **Idle or Wait Time**: Tempo de espera ou inatividade durante as fases do PR, que divide o foco e eleva a carga cognitiva.
*   **Meeting Team Goals**: Capacidade de atingir consistentemente os objetivos apoiados em dados.
*   **Task Balance**: Variedade saudável de tarefas (bugs vs. novos desafios).
*   **Skill Expansion**: Oportunidade para os desenvolvedores explorarem novas áreas da base de código.
*   **Knowledge Expansion**: Aprendizado constante de novas linguagens e tecnologias.
*   **Coding vs. Code Review**: O balanço de tempo gasto escrevendo código versus fornecendo *feedback* em código de terceiros.
*   **Unplanned and Added Work**: Quantidade de trabalho não planejado que pode impactar os cronogramas.
*   **WIP (Work In Progress)**: Controle de trabalho em andamento para evitar sobrecarga ou *burnout*.

*Aviso: "Linhas de código" (Lines of Code) é citada especificamente como um exemplo negativo de métrica que as organizações não devem priorizar ao criar rankings entre desenvolvedores.*

---

## Insights para Praticantes

*   **Evite Stack Ranking com base em Outputs**: A classificação de times por volume de entrega (linhas de código, pontos concluídos) prejudica o processo de desenvolvimento, gera hábitos de manipulação dos números e impacta a qualidade final.
*   **Utilize as Métricas em Reuniões 1:1 e Avaliações**: Os dados devem enriquecer — e não substituir — as conversas com a equipe. Praticantes devem usar esses números em conjunto com dados de sentimento ou pesquisas (*surveys*) para construir avaliações justas, reconhecer bons desempenhos, criar confiança, eliminar vieses e identificar gargalos nos processos (como o tempo de revisão de PRs).
*   **Automatize para Reduzir a Fricção**: Em vez de apenas medir tempos ociosos, invista em automações no nível de código e assistência de *bots* para priorizar revisores, adicionar contexto em código ou aprovar automaticamente alterações consideradas pequenas e seguras.
*   **Conecte Métricas Operacionais a Metas de Negócios**: Comece estruturando os OKRs no nível organizacional e em seguida divida-os para os times usando o formato SMART, alinhando as melhorias de engenharia com os impactos da companhia.

---

## Avaliacao de Qualidade GL (Garousi et al.)

| Criterio | Pontuacao (0-1) |
|----------|----------------|
| Autoridade do autor/organizacao | 1 |
| Descricao de metodologia | 0 |
| Data de publicacao | 1 |
| Objetividade (vies comercial) | 0 |
| Referencias citadas | 0 |
| Contribuicao nova | 1 |
| **TOTAL** | **3/6** |

*(Nota explicativa da avaliação: A organização LinearB possui grande peso e autoridade de mercado (citada como líder Gartner), e a publicação é recente (Novembro 2024) trazendo uma perspectiva útil e catalogada através dos "três Es". Contudo, por se tratar da postagem em um blog institucional com propósitos comercias — culminando num call-to-action para a própria plataforma —, a fonte perde pontos em descrição metodológica profunda, independência científica (referências) e imparcialidade.)*

---

*Extraido via NotebookLM em Junho de 2026 para MLR: Software Developer Metrics in Practice*
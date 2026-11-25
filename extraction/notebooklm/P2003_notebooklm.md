# P2003 — Enhancing Software Engineering Productivity Through AI-Scrum Framework: A Case Study in Libyan Contexts

**Decisao: INCLUIDO | Qualidade: 4/5**

---

## Dados Bibliograficos

| Campo | Valor |
|-------|-------|
| **ID** | P2003 |
| **Autores** | Samia Abdalhamid, Amna Faraj [1] |
| **Ano** | 2025 [1] |
| **Venue** | International Conference on Electrical and Computer Engineering Researches (ICECER 2025) / IEEE [1] |
| **DOI** | Nao especificado / Indisponivel (ISBN: 978-1-6654-5756-9/25/) [1] |
| **Tipo** | Conference paper [1] |
| **Metodo** | Mixed methods (Comparative Case Study com metricas quantitativas, survey com escala Likert e analise qualitatica) [2-5] |
| **Amostra** | 2 equipes com 19 participantes no total (Equipe 1: 6 profissionais de desenvolvimento/Scrum; Equipe 2: 11 estudantes de Ciencia da Computacao; 19 respondentes no survey) [5-7] |
| **Contexto** | Mixed (1 equipe profissional desenvolvendo sistema de agendamento odontologico e 1 equipe academica desenvolvendo sistema de presenca de professores em contexto de recursos limitados na Libia) [1, 2, 6] |
| **Modo de trabalho** | Not specified [1, 6] |
| **Metodologia** | Agile (Scrum / AI-Scrum Framework) [2, 8, 9] |

---

## Objetivo

O objetivo principal do trabalho e projetar e avaliar empiricamente o framework "AI-Scrum", que integra ferramentas acessiveis e gratuitas de inteligencia artificial (como ClickUp AI, Windsurf Plugin e Diffblue Cover) aos processos Agile/Scrum mantendo a governanca e a decisao humana [2, 8-10]. O estudo busca aumentar a produtividade na engenharia de software, reduzir defeitos e otimizar eventos do Scrum em equipes com recursos limitados em contextos profissionais e academicos na Libia [2, 7, 8, 11].

---

## Questoes de Pesquisa

- **RQ1**: How does AI integration affect productivity and software quality in Libyan software teams? [8]
- **RQ2**: What challenges arise when integrating AI into Scrum? [8]
- **RQ3**: How do team members perceive AI tools' usability and effectiveness? [8]
- **RQ4**: How does the proposed framework compare to traditional Scrum in performance metrics? [8]

---

## Metricas e Instrumentos de Avaliacao

| Metrica | Categoria | Nivel | Como Coletada | Validada |
|---------|-----------|-------|---------------|----------|
| Sprint Velocity | Delivery | Team | Medicao quantitativa do fluxo de entregas por sprint [5] | Yes [4, 5] |
| Defect Reduction Rate | Quality | Team | Analise comparativa da contagem de defeitos entre o Scrum tradicional e o AI-Scrum [3, 5, 12] | Yes [4, 12] |
| Test Coverage | Quality | Team | Medicao automatizada via ferramenta de testes (Diffblue Cover) [3, 5, 12, 13] | Yes [4, 12, 13] |
| Time Savings / Phase Duration | Productivity | Team | Registro e comparacao do tempo em horas por sprint em cada fase do Scrum [3, 13, 14] | Yes (Cronbach's α = 0,79, r = 0,71) [4] |
| AI-Generated Code Adoption Rate | Activity | Individual/Team | Percentual de codigo gerado por IA adotado no projeto [5, 12, 15] | Yes [4, 12] |
| Code Refactoring Required | Quality | Team | Percentual de refatoracao necessaria em codigos gerados por IA [15, 16] | Yes [4, 15] |
| Automated Report Adoption Rate | Activity | Team | Percentual de adocao de relatorios diarios automatizados pelas equipes [15, 16] | Yes [4, 15] |
| Perceived Productivity Gains | Satisfaction / DevEx | Individual | Survey com escala Likert de 5 pontos analisado via SPSS v20 [3-5, 14] | Yes (Cronbach's α = 0,79) [4] |
| AI Trust / Perceived Usability | Satisfaction / DevEx | Individual | Survey com escala Likert de 5 pontos e questoes abertas [3-5, 12] | Yes (Cronbach's α = 0,87) [4] |

---

## Frameworks e Metricas

### Frameworks Referenciados
- **Scrum / Agile**: APPLIED — Utilizado como metodologia base para a integracao do framework AI-Scrum [2, 8-10].
- *Nota*: Nenhum dos frameworks padrao como DORA, SPACE, DevEx, GQM, HEART ou OKR foi citado ou aplicado no artigo [1, 2, 8, 10].

### Frameworks Propostos
- **AI-Scrum Framework**: Framework que mapeia e incorpora ferramentas de IA gratuitas e de baixo custo nas fases do Scrum sem violar seus principios fundamentais [2, 9, 10]. O framework estabelece:
  - **Backlog Refinement**: Geracao e priorizacao de historias de usuario baseada em PLN (ex: ClickUp AI) [9, 17, 18].
  - **Sprint Planning**: Previsao de capacidade, divisao de tarefas e predicao de riscos via IA com aprovacao da equipe [9, 13].
  - **Daily Stand-ups**: Automatizacao de relatorios diarios de status e revisoes auxiliadas por IA [9, 13].
  - **Desenvolvimento e Testes**: Autocompletar codigo e deteccao de erros (Windsurf) e geracao automatizada de testes unitarios (Diffblue Cover) [13, 17, 18].
  - **Continuous Learning**: Relatorios automatizados em retrospectivas e auditoria trimestral de padroes pela equipe com marcos obrigatorios de revisao humana [9, 19].

---

## Fatores que Influenciam Produtividade

### Fatores Positivos
| Fator | Categoria |
|-------|-----------|
| Uso de ferramentas de IA gratuitas e acessiveis (ClickUp AI, Windsurf, Diffblue Cover) [11, 17, 18] | Technical |
| Automatizacao de tarefas repetitivas (relatorios diarios, historias de usuario, testes unitarios) [9, 15, 19] | Process |
| Treinamento previo e workshops focados com nomeacao de "AI Champions" [3, 18] | Organizational |
| Alta taxa de adocao e frequencia de uso das ferramentas de IA [4, 13, 16] | Human |
| Marcos obrigatorios de revisao humana mantendo os principios fundamentais do Scrum [9, 18, 19] | Process |

### Fatores Negativos
| Fator | Categoria |
|-------|-----------|
| Pouco conhecimento metodologico de Scrum e falta de experiencia previa em desenvolvedores juniores [12, 20] | Human |
| Necessidade de refatoracao de codigo devido ao uso excessivo de IA (15% a mais na equipe academica) [15, 16] | Technical |
| Preocupacoes com seguranca e privacidade de dados em projetos sensiveis entre profissionais [12, 18, 20] | Organizational |
| Incompatibilidade de contexto e falta de alinhamento com o fluxo do ambiente academico [12, 20] | Organizational |
| Risco de excesso de confianca e sobre-automatizacao sem analise critica [18, 19, 21] | Human |

---

## Papel da IA e Automacao

| Campo | Valor |
|-------|-------|
| Usa IA/ML? | Yes — Utiliza PLN, aprendizado de maquina e modelos gerativos em ferramentas como ClickUp AI, Windsurf Plugin e Diffblue Cover [17, 18, 22]. |
| Automacao de coleta? | Yes — Automatizacao da geracao de relatorios de stand-up, metricas de cobertura de testes e tempos por fase [9, 13, 15]. |
| Impacto de IA na produtividade? | Impacto positivo expressivo: ganho de produtividade de 10–20% acima dos benchmarks do Scrum tradicional, reducao de 30–45% no tempo de fases como refinamento e planejamento, e 22% a mais de economia de tempo em equipes academicas/iniciantes devido a maior adocao [2, 11, 13, 14, 20]. |

---

## Resultados Principais

- **Economia de Tempo por Fase do Scrum**: Reducao media de tempo por sprint no refinamento de backlog (35%), planejamento de sprint (35%), daily standups (38%), desenvolvimento de codigo (35%) e testes (34%) [13, 14].
- **O "Paradoxo da Experiencia"**: A equipe academica/novata economizou 22% a mais de tempo do que os profissionais porque adotou as ferramentas de IA de forma mais agressiva (78% vs 62% de adocao de codigo gerado), embora tenha exigido 15% a mais de refatoracao [12, 15, 19, 20]. Profissionais adotaram uma postura mais cautelosa focando em seguranca e profundidade [12, 19, 20].
- **Melhoria da Qualidade**: A equipe profissional reduziu defeitos em 62% e alcancou 92% de cobertura de testes (vs 70% da linha de base) [12, 15]. A equipe academica reduziu defeitos em 55% e atingiu 85% de cobertura de testes [12, 15].
- **Validacao Estatistica**: As escalas de percepcao demonstraram alta confiabilidade (Trust α = 0,87; Produtividade α = 0,79) [4]. A analise de regressao (R² = 0,63) confirmou que o uso da ferramenta preve eficiencia (β = 0,41) enquanto maior experiencia correlaciona-se com menor ganho relativo de tempo (β = -0,52) [4, 13, 16].
- **Viabilidade de Ferramentas Gratuitas**: O estudo demonstrou que ferramentas no nivel gratuito (free-tier) entregam resultados equivalentes a solucoes pagas, democratizando a adocao de IA para equipes com restricoes orcamentarias [11, 23, 24].

---

## Desafios do Uso das Metricas

- Risco de sobre-automatizacao e perda de pensamento critico quando desenvolvedores aceitam metricas e codigos gerados por IA sem auditoria [18, 19, 21].
- Escepticismo quanto a seguranca e privacidade dos dados ao enviar codigo e requisitos para ferramentas em nuvem [12, 18].
- Falta de alinhamento entre metricas automatizadas de processos e a dinamica de projetos academicos/em sala de aula [12, 20].
- Dificuldade em equilibrar ganhos de velocidade com controle de qualidade, exigindo marcos obrigatorios de revisao humana para evitar propagacao de bugs [18, 19, 21].

---

## Avaliacao de Qualidade Metodologica

| Criterio | Pontuacao (0-2) |
|----------|----------------|
| Objetivo claramente definido | 2 |
| Metodologia adequada ao objetivo | 2 |
| Amostra/contexto descrito adequadamente | 1 |
| Ameacas a validade discutidas | 1 |
| Resultados com evidencia suficiente | 2 |
| Contribuicao clara para pratica ou teoria | 2 |
| **TOTAL** | **10/12** |

---

## Limitacoes

- Tamanho reduzido da amostra (n=19 em 2 equipes de estudo de caso), limitando a generalizacao estatistica ampla [7, 25].
- Avaliacao focada em ferramentas de IA em camada gratuita (ClickUp AI, Windsurf, Diffblue), o que pode nao capturar todos os recursos de versoes pagas [7].
- Contexto geografico e organizacional restrito a equipes de engenharia de software na Libia [7].
- Avaliacao limitada a ciclos de sprints de curto prazo sem acompanhamento longitudinal de longo prazo [3, 7, 13].

---

## Contribuicao Principal

A contribuicao principal do artigo e a proposicao e validacao empirica do framework "AI-Scrum", uma abordagem acessivel para integrar ferramentas de IA gratuitas ao ciclo de vida Agile garantindo supervisao humana continua [2, 8-10, 19]. Ao demonstrar ganhos expressivos de produtividade (10–20% superiores aos benchmarks tradicionais) e reducao de defeitos em ambientes libios com restricao de recursos, o trabalho fornece diretrizes praticas e evidencias empiricas sobre como democratizar o uso da IA sem comprometer os principios fundamentais do Scrum [2, 8, 11, 21, 23, 24].

---

*Extraido via NotebookLM em October 2026 para MLR: Software Developer Metrics in Practice*

💡 Gostaria que eu gerasse um relatorio comparativo ou uma sintese em PDF consolidando as metricas deste e de outros artigos da sua revisao da literatura?
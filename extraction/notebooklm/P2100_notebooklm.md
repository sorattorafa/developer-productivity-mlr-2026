# P2100 — Beyond the Commit: Developer Perspectives on Productivity with AI Coding Assistants

**Decisao: INCLUIDO | Qualidade: 5/5**

---

## Dados Bibliograficos

| Campo | Valor |
|-------|-------|
| **ID** | P2100 [1] |
| **Autores** | Valerie Chen, Jasmyn He, Behnjamin Williams, Jason Valentino, Ameet Talwalkar [1, 2] |
| **Ano** | 2026 [1] |
| **Venue** | IEEE/ACM 48th International Conference on Software Engineering (ICSE-SEIP ’26) [1] |
| **DOI** | 10.1145/3786583.3786848 [1] |
| **Tipo** | Conference paper (ICSE Software Engineering in Practice track) [1] |
| **Metodo** | Mixed methods (Sequential exploratory design: Quantitative survey + Qualitative semi-structured interviews) [2, 3] |
| **Amostra** | 2,989 survey respondents and 11 semi-structured interview participants [2, 4-6] |
| **Contexto** | Industry (Financial services enterprise: BNY Mellon) [2, 4] |
| **Modo de trabalho** | Not specified [2, 4] |
| **Metodologia** | Not specified [2, 4] |

---

## Objetivo

This paper aims to analyze the validity and alignment of existing developer productivity metrics when applied to AI coding assistants, and to establish a holistic, multi-dimensional evaluation framework tailored for AI tools in software engineering [2, 3, 7, 8]. By investigating developer perspectives at BNY Mellon through a mixed-methods approach, the study evaluates how traditional metrics align with developer experiences and identifies key human-centered and long-term productivity factors—such as technical expertise and code ownership—that are absent from established productivity frameworks [2, 9-13].

---

## Questoes de Pesquisa

- **RQ1**: To what extent do different AI productivity metrics align in their assessments? [14]
- **RQ2**: What broader range of AI productivity metrics do developers consider relevant in the context of AI coding assistants? [14]
- **RQ3**: How do developers view the impact of AI productivity metrics on different parts of the development process? [14]

---

## Metricas e Instrumentos de Avaliacao

| Metrica | Categoria | Nivel | Como Coletada | Validada |
|---------|-----------|-------|---------------|----------|
| General satisfaction (CSAT) | Satisfaction | Individual | Self-reported survey question (5-point scale via DX platform) | Yes [15] |
| Perceived time savings | Productivity / DevEx | Individual | Self-reported survey question (5 categorical ranges per week via DX platform) | Partial [11, 15, 16] |
| Lines of Code (LOC) | Activity | Individual | Code telemetry / Repository mining | No [17, 18] |
| Diff Authoring Time (DAT) | Activity / Delivery | Individual | Telemetry-driven signals of developer effort at scale | Yes [19] |
| Code completion / Chat acceptance rate | Activity / DevEx | Individual | Automated tool telemetry | Partial [16, 20] |
| Commit frequency | Activity | Individual / Team | Version control telemetry | Partial [16, 21] |
| Self-sufficiency | DevEx / Productivity | Individual / Team | Qualitative interviews & periodic surveys (tracking context-switching) | Yes [10, 22-24] |
| Frustration & cognitive load | DevEx / Satisfaction | Individual | Qualitative interviews & periodic surveys (tracking prompt effort & fatigue) | Yes [10, 25-27] |
| Rate of task completion | Delivery / Productivity | Individual / Team | Qualitative interviews, sprint tracking & periodic surveys | Yes [10, 18, 27, 28] |
| Ease of peer review | Collaboration / Quality | Team | Qualitative interviews & periodic surveys (tracking review comments & fix time) | Yes [10, 26, 27, 29] |
| Technical expertise | DevEx / Quality | Individual / Organization | Qualitative interviews & periodic surveys (monitoring skill acquisition & decay) | Yes [10, 12, 28, 30] |
| Sense of ownership of work | DevEx / Quality | Individual / Team | Qualitative interviews & periodic surveys (tracking perceived authorship & debugging familiarity) | Yes [10, 12, 24, 31] |

---

## Frameworks e Metricas

### Frameworks Referenciados
- **SPACE**: REFERENCED (discussed as a multi-faceted productivity framework; its dimensions of efficiency/flow and collaboration overlap with cognitive load and peer review, but omit long-term expertise and ownership) [7, 27, 32, 33].
- **DORA**: REFERENCED (discussed for DevOps performance and throughput metrics like deployment frequency and lead time, aligning with task completion rate) [7, 27, 32, 33].
- **DX Framework**: APPLIED (used as the survey deployment platform across BNY Mellon to measure general satisfaction and perceived time savings) [9, 15, 34].

### Frameworks Propostos
- **6-Factor AI Productivity Framework**: A novel multidimensional framework specifically tailored for AI coding assistants [2, 10, 13]. It categorizes productivity impacts across three operational phases: Development (Self-sufficiency, Frustration & Cognitive Load), Deployment (Rate of Task Completion, Ease of Peer Review), and Long-Term Developer Impact (Technical Expertise, Sense of Ownership of Work) [23, 24, 26-28, 35].

---

## Fatores que Influenciam Produtividade

### Fatores Positivos
| Fator | Categoria |
|-------|-----------|
| Melhora na auto-suficiencia e reducao de troca de contexto entre ferramentas (ex.: documentacao, Stack Overflow, Google) [22, 23] | Technical / Human |
| Reducao de frustracao e carga cognitiva na escrita de codigo boilerplate e configuracoes [25, 26, 36] | Human / Process |
| Aceleracao na taxa de conclusao de tarefas em geracao de testes automatizados e documentacao [18, 28, 36] | Process / Technical |
| Auxilio a revisores seniores na sumarizacao rapida de alteracoes em PRs [26, 29] | Technical / Collaboration |
| Suporte ao aprendizado de novos conceitos e padroes de seguranca [28, 30] | Human / Technical |

### Fatores Negativos
| Fator | Categoria |
|-------|-----------|
| Alucinacoes e sugestoes incorretas/irrelevantes que exigem esforco repetido de reprompting (4-5 tentativas) [11, 25, 26, 37] | Technical / Human |
| Baixo desempenho e lentidao na refatoracao de sistemas legados devido a falta de contexto amplo do projeto [38] | Technical / Process |
| Dificuldade e tempo adicional no processo de peer review devido a codigos otimizados incorretamente ou sem testes adequados gerados por IA [26, 29] | Process / Collaboration |
| Risco de erosao da experiencia tecnica (skill decay) e atalhos no aprendizado fundamental de desenvolvedores juniores [12, 28, 30] | Human / Organizational |
| Perda de sentimento de autoria/propriedade do codigo, dificultando a depuracao de incidentes em producao [12, 24, 31] | Human / Organizational |

---

## Papel da IA e Automacao

| Campo | Valor |
|-------|-------|
| **Usa IA/ML?** | Yes — Focuses on AI coding assistants (specifically GitHub Copilot based on LLMs) for code generation, completion, refactoring, test generation, and documentation [2, 4, 32, 39]. |
| **Automacao de coleta?** | Yes — Uses automated survey deployment via the DX platform for quantitative response collection, alongside analysis of telemetry metrics like commit frequency [9, 15, 16]. |
| **Impacto de IA na produtividade?** | High user satisfaction (86% satisfied/very satisfied), but modest reported time savings (~60% save <1 hour/week) with weak correlation (r=0.34) between satisfaction and time saved [11, 37]. Productivity impact varies significantly by task: highly positive for boilerplate/tests, neutral/negative for complex refactoring and long-term expertise/ownership [13, 36, 38, 40, 41]. |

---

## Resultados Principais

- **Fraca Correlacao entre Satisfacao e Economia de Tempo (RQ1)**: Embora 86% dos 2.898 engenheiros pesquisados estejam satisfeitos ou muito satisfeitos com o GitHub Copilot, cerca de 60% relatam economizar menos de 1 hora por semana [37]. A correlacao de Pearson entre as duas metricas e fraca (\\(r = 0,34, p < 0,0001\\)), provando que a percepcao de valor da IA nao e capturada por uma unica metrica de eficiencia [11].
- **Estruturacao em Seis Fatores de Produtividade (RQ2)**: O estudo identificou 6 fatores abrangentes divididos em tres fases [35]:
  1. *Desenvolvimento*: Auto-suficiencia (*Self-sufficiency*) e Reducao de frustracao/carga cognitiva (*Frustration & cognitive load*) [22, 25].
  2. *Implantacao*: Taxa de conclusao de tarefas (*Task completion rate*) e Facilidade de peer review (*Ease of peer review*) [18, 29].
  3. *Impacto de Longo Prazo*: Experiencia tecnica (*Technical expertise*) e Sentimento de propriedade do trabalho (*Ownership of work*) [30, 31].
- **Variacao do Impacto por Caso de Uso (RQ3)**:
  - *Novas Funcionalidades*: Aumenta a auto-suficiencia e reduz a carga cognitiva no curto prazo, mas levanta preocupacoes sobre a copia cega e o impacto no aprendizado de longo prazo de engenheiros juniores [41].
  - *Refatoracao de Codigo*: Impacto neutro ou negativo, pois 70–80% do tempo e gasto lendo e compreendendo codigo e a IA falha frequentemente sem instrucoes e contextos altamente especificos [38].
  - *Testes e Documentacao*: Tarefa repetitiva com aceleracao substancial (reduzindo prazos de 1 dia para 1 hora) e grande reducao na frustracao [36].
- **Lacuna de Longo Prazo nos Frameworks Existentes**: Frameworks consolidados (como SPACE e DORA) capturam apenas dimensoes de curto prazo de execucao e colaboracao, ignorando fatores de longo prazo como a evolucao da experiencia tecnica e o sentimento de responsabilidade sobre o codigo [12, 33].

---

## Desafios do Uso das Metricas

- **Dependencia de Metricas Unicas de Eficiencia**: Avaliar assistentes de IA apenas por tempo economizado ou linhas de codigo (LOC) ignora ganhos qualitativos de bem-estar e oculta custos em revisoes e manutencao [11, 17, 18, 21, 37].
- **Subjetividade e Inacuracia em Relatos de Tempo**: Medidas de tempo economizado baseadas em pesquisas sao estimadas e frequentemente imprecisas quando comparadas com o tempo real de trabalho [16, 20].
- **Anti-Padrao de "Copia Cega" em Desenvolvedores Juniores**: A utilizacao acritica de codigo gerado por IA produz solucoes mal otimizadas que sobrecarregam e desaceleram o processo de peer review por engenheiros seniores [25, 29, 41].
- **Risco de Degradacao de Habilidades (*Skill Decay*)**: A substituicao do processo de depuracao e analise de erros por respostas automaticas da IA dificulta o desenvolvimento de competencias fundamentais em engenheiros em inicio de carreira [12, 30, 31].

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

- **Contexto Organizacional Unico**: Estudo conduzido exclusivamente na BNY Mellon, o que pode restringir a generalizacao dos achados para empresas de menor porte ou projetos open-source [42].
- **Restricao a uma Ferramenta de IA**: A avaliacao focou no GitHub Copilot, nao cobrindo assistentes de codigo mais recentes com fluxos de trabalho agenticos autonomos [42].
- **Inviabilidade de Coleta de Telemetria Uniforme**: Dificuldade em obter dados quantitativos diretos de aceitacao de codigo em escala para todos os 8.000 engenheiros, necessitando do uso de autorelatos [16, 20].
- **Nao Exaustividade dos Fatores**: Embora abrangentes, os 6 fatores propostos nao pretendem esgotar todas as dimensoes possiveis de produtividade em cenarios com IA [42].

---

## Contribuicao Principal

This study provides empirical mixed-methods evidence that single-dimensional efficiency metrics fail to capture the true impact of AI coding assistants on software developers, revealing a weak correlation between developer satisfaction and time savings [2, 11, 13]. By establishing a 6-factor evaluation framework that incorporates long-term dimensions—specifically technical expertise development and code ownership—the paper bridges the gap in traditional frameworks like SPACE and DORA and delivers concrete, actionable survey instruments for holistic AI productivity measurement in industry and research [2, 10, 13, 23, 24, 26-28, 34].

---

*Extraido via NotebookLM em October 2026 para MLR: Software Developer Metrics in Practice*
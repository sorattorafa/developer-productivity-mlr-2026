# P2074 — Using development environment as code for enhancing developer experience: An action design research study

**Decisao: INCLUIDO | Qualidade: 4.5/5**

---

## Dados Bibliograficos

| Campo | Valor |
|-------|-------|
| **ID** | P2074 |
| **Autores** | Hadi Ghanbari, Tarmo Terimaa, Kari Koskinen [1] |
| **Ano** | 2026 [1] |
| **Venue** | Journal of Systems and Software (Volume 236, Article 112803) [1] |
| **DOI** | https://doi.org/10.1016/j.jss.2026.112803 [1] |
| **Tipo** | Journal article [1] |
| **Metodo** | Action Design Research (ADR), Qualitative (Focus group, semi-structured interviews, participant observation, Likert scale survey) [1-4] |
| **Amostra** | Case study: 1 Finnish software company (€25M revenue, R&D department with ITSM team of 14 developers) [2]; 6 internal participants in focus group and interviews (Backend Developer, Developer, Senior Developer, QA Lead, Senior Front-end Developer, Lead Developer) [3, 5]; 6 external practitioners for DP evaluation [4, 6] |
| **Contexto** | Industry (Finnish software company developing ITSM and business process automation tools) [2] |
| **Modo de trabalho** | Not specified for daily work (Focus group and interviews conducted remotely via Microsoft Teams) [3, 7] |
| **Metodologia** | Agile / DevOps [8-10] |

---

## Objetivo

The main objective of the paper is to examine how developers' experience (DX) when setting up and configuring local development environments can be enhanced [1, 7]. Through an Action Design Research (ADR) study conducted in a Finnish software company, the authors aim to identify the mechanisms and factors shaping DX during setup, propose a novel IT artefact concept—Development Environment as Code (DEaC)—to automate and containerize local environments, and formulate four generalizable design principles (DPs) to guide organizations in improving DX related to development environment management [1, 2, 4, 7, 11].

---

## Questoes de Pesquisa

- **RQ1**: How can a developer's experience with setting up and configuring development environments be enhanced? [7]

---

## Metricas e Instrumentos de Avaliacao

| Metrica | Categoria | Nivel | Como Coletada | Validada |
|---------|-----------|-------|---------------|----------|
| Tempo de Setup (Setup Time) | Productivity / DevEx | Individual / Team | Entrevistas e autorrelato dos desenvolvedores (redução de ~1 dia para ~15 min / 2 comandos Docker) [12, 13] | Partial |
| Esforço Cognitivo e Carga Mental (Cognitive Effort) | DevEx / Satisfaction | Individual | Entrevistas semiestruturadas e análise temática baseada no framework de DX (Fagerholm, 2015) [5, 12, 14] | Partial |
| Tempo de Reinicialização do Servidor/Container (Server Restart Time) | Activity / Delivery | Individual | Observação de campo e testes de usabilidade durante os ciclos BIE [3, 13, 15] | Partial |
| Avaliação dos Princípios de Design (DP Evaluation: Accessibility, Importance, Novelty, Actability, Effectiveness) | Quality / DevEx | Organization | Questionário de escala Likert de 4 pontos (23 itens) aplicado a 6 profissionais externos, analisado via estatística descritiva e Teste Kendall's W (W = 0,48; Chi2 = 63,04; p < 0,001) [4, 6, 16] | Yes |

---

## Frameworks e Metricas

### Frameworks Referenciados
- **Developer Experience (DX) Framework (Fagerholm, 2015; Fagerholm & Münch, 2012)**: APPLIED — Used as the primary analytical lens for thematic coding across 7 DX aspects (experience object, formation, influencers, content, progression, behavior outcome, object outcome) [5, 9, 14].
- **Action Design Research (ADR) (Sein et al., 2011)**: APPLIED — Used as the core research methodology across four phases (Problem Formulation, BIE, Reflection & Learning, Formalization of Learning) [1, 2].
- **Infrastructure as Code (IaC) (Dalla Palma et al., 2020; Morris, 2016; Rahman et al., 2019)**: REFERENCED — Discussed as the theoretical foundation adapted for local developer machine environments [9, 17, 18].
- **DevEx Framework (Forsgren et al., 2024; Greiler et al., 2022)**: REFERENCED — Cited regarding developer satisfaction, flow state, and cognitive load [7-9].

### Frameworks Propostos
- **Development Environment as Code (DEaC)**: Proposes a conceptual framework and architecture for managing local development environments as version-controlled code using Docker containerization (web server, database, build, tools services) to restrict risks of misconfigurations to local machines [1, 13, 18, 19].
- **DEaC DX Formation Model (Fig. 4)**: A conceptual model mapping how DX is formed during environment setup through obtaining, processing, and utilizing information, influenced by social and technical factors across cognitive, conative, and affective dimensions [5, 14, 20, 21].
- **DEaC Design Principles (DP1–DP4)**: Formulates four design principles for DEaC (DP1: Automated setup, DP2: Consistent environment, DP3: Modular environment, DP4: Embedding knowledge) [4, 11].

---

## Fatores que Influenciam Produtividade

### Fatores Positivos
| Fator | Categoria |
|-------|-----------|
| Automação do setup e configuração de ferramentas via código (DEaC) [7, 13, 18] | Technical |
| Containerização e virtualização para garantir paridade entre ambientes (Mac, Windows, Linux) [13, 18] | Technical |
| Estrutura modular separando serviços (build, db, web server, tools) [4, 15, 19] | Technical / Process |
| Instruções e conhecimento incorporados diretamente no código da aplicação (embedded knowledge) [4, 18, 22] | Process / Technical |
| Redução da carga cognitiva e do tempo gasto no onboarding de novos desenvolvedores [7, 13, 23] | Process / Human |
| Sensação de autonomia e oportunidade de aprendizado para os desenvolvedores [12, 20] | Human |
| Suporte a colaboração cross-project e realização de reviews locais por Product Owners [13, 23] | Organizational / Process |

### Fatores Negativos
| Fator | Categoria |
|-------|-----------|
| Documentação e instruções desatualizadas, ocultas ou espalhadas (hidden/scattered knowledge) [10, 14] | Technical / Process |
| Tarefas manuais excessivas e propensas a erros no setup tradicional [8, 18, 24] | Technical / Process |
| Inconsistências de ambiente e problema do "works on my machine" [8, 18] | Technical |
| Frustração e ansiedade causadas por troubleshooting sob pressão de prazos [10, 12] | Human / Organizational |
| Lentidão na reinicialização de containers de servidor em relação ao ambiente nativo [13, 15] | Technical |
| Resistência à alteração de hábitos de trabalho e atalhos de teclado de IDEs [13, 23, 25] | Human / Process |
| Dependência de tecnologias de terceiros (ex.: Docker, suporte do IntelliJ IDEA) [12, 26, 27] | Technical |

---

## Papel da IA e Automacao

| Campo | Valor |
|-------|-------|
| Usa IA/ML? | No — The study does not use or evaluate AI/ML technologies [1, 7]. |
| Automacao de coleta? | No — Data collection was performed manually via interviews, focus groups, and surveys, though statistical testing (Kendall's W) was applied [3, 6]. The DEaC artefact automates environment setup [18]. |
| Impacto de IA na produtividade? | Not applicable — AI impact is not analyzed in the paper [1, 7]. |

---

## Resultados Principais

- **Drastic Setup Time Reduction**: DEaC reduced initial environment setup from roughly one day of manual troubleshooting to approximately 15 minutes or two Docker commands [12, 13].
- **Identification of DX Mechanisms**: Uncovered three core mechanisms that form DX during setup: obtaining information, processing information, and utilizing information [5, 7, 24].
- **Four Design Principles (DPs)**: Formulated and validated four design principles for DEaC: DP1 (Automated setup), DP2 (Consistent environment), DP3 (Modular environment), and DP4 (Embedding knowledge) [4, 11].
- **High External Validation Agreement**: Evaluation by 6 external practitioners showed 100% agreement on Importance (mean 3.5/4.0), 88.3% on Accessibility (mean 3.3/4.0), 67.7% on Actability (mean 3.1/4.0), and 67.7% on Effectiveness (mean 2.9/4.0), with statistically significant consensus (Kendall's W = 0.48, Chi2 = 63.04, p < 0.001) [6, 16].
- **Risk Isolation**: Unlike global IaC, DEaC isolates configuration risks strictly to developers' local machines, enabling safe personal customization [17, 18, 28].
- **Cross-Role Utility**: Enabled non-developer team members (e.g., Product Owners, QA) to easily run local application builds for reviews and integration testing [13, 23].

---

## Desafios do Uso das Metricas

- **Subjectivity of DX Evaluation**: Relying on qualitative self-reported developer perceptions makes objective quantitative measurement challenging [3, 29].
- **Context-Dependent Time Savings**: Setup time metrics differ substantially depending on whether the developer performs active development or simple testing/review builds [10, 15].
- **Traditional Metrics Blind Spots**: Standard productivity metrics (e.g., lines of code, output volume) fail to capture developer frustration and cognitive load stemming from broken environment setups [7-9].
- **Initial Productivity Lag**: Implementing automated environments can cause temporary productivity dips due to learning curves and habit adaptation before long-term efficiency gains are realized [23].

---

## Avaliacao de Qualidade Metodologica

| Criterio | Pontuacao (0-2) |
|----------|----------------|
| Objetivo claramente definido | 2 |
| Metodologia adequada ao objetivo | 2 |
| Amostra/contexto descrito adequadamente | 2 |
| Ameacas a validade discutidas | 2 |
| Resultados com evidencia suficiente | 1 |
| Contribuicao clara para pratica ou teoria | 2 |
| **TOTAL** | **11/12** |

---

## Limitacoes

- **Single Case Study Context**: Primary empirical data and prototype requirements were gathered from a single Finnish software company, limiting direct statistical generalizability [2, 29].
- **Small Sample Size & Potential Bias**: Relying on qualitative data from 6 internal developers and 6 external raters introduces potential participant and researcher subjectivity [3, 6, 29].
- **Technical Tooling Limitations**: Immaturity or incomplete support in IDEs (e.g., IntelliJ IDEA lack of containerized incremental builds) created performance friction during server restarts [15, 27, 30].
- **DP Evaluation Panel Constraints**: External validation of DPs was limited to a panel of 6 practitioners [4, 6, 29].

---

## Contribuicao Principal

The principal contribution of this paper is introducing the concept of Development Environment as Code (DEaC) and demonstrating through an Action Design Research (ADR) study how local environment automation and containerization significantly improve Developer Experience (DX) by drastically reducing setup time, cognitive load, and platform inconsistencies [1, 7, 18, 31]. Furthermore, the paper provides four empirically validated Design Principles (DPs) that adapt IaC concepts for local developer workflows, filling a notable gap in software engineering literature regarding the impact of local environment setup on developer satisfaction and productivity [1, 4, 11, 31].

---

*Extraido via NotebookLM em October 2026 para MLR: Software Developer Metrics in Practice*

---

💡 **Would you like me to create a tailored summary report or a slide deck highlighting the four DEaC design principles and implementation findings?**
# P2005 — Evaluating the Role of AI, Technology Used, and Technology Skill Proficiency in Onboarding: A Quantitative Study of Developer Productivity and Scalability in Sri Lanka [1, 2]

**Decisao: INCLUIDO | Qualidade: 4.6/5**

---

## Dados Bibliograficos

| Campo | Valor |
|-------|-------|
| **ID** | P2005 |
| **Autores** | Shenara Lelwala, Thisuni Tantirige, Malsika Munigoda, Krishantha Wisenthige, Nimthara Ashinshana, Colinie Wickramaarachchi [1, 3] |
| **Ano** | Not specified in paper header (cites literature up to 2025) [1, 4, 5] |
| **Venue** | SLIIT Business School, Sri Lanka Institute of Information Technology [1, 3] |
| **DOI** | Not specified [1] |
| **Tipo** | Conference paper / Academic research paper [1, 2] |
| **Metodo** | Quantitative (Survey, PLS-SEM using SmartPLS) [2, 6-8] |
| **Amostra** | 104 software developers in Sri Lanka (Junior: 47.11%, Mid-Level: 21.15%, Senior: 20.19%, Tech Lead/Architect: 5.77%, Director: 2.88%, Freelancer/QA/Trainee: 2.90%) [6, 9-11] |
| **Contexto** | Industry (Medium and large-scale IT organizations in Sri Lanka) [6, 7, 12] |
| **Modo de trabalho** | Not specified [2, 7] |
| **Metodologia** | Not specified [2, 7] |

---

## Objetivo

The primary objective of this study is to empirically evaluate how developer onboarding practices—specifically Artificial Intelligence (AI), Technology Used (TU), and Technology Skill Proficiency (TSP)—influence Developer Productivity (DP) and how these factors directly and indirectly drive the execution and Scalability of Business Applications (SBA) in Sri Lankan IT organizations, anchored in Socio-Technical System (STS) theory [2, 6, 7, 13].

---

## Questoes de Pesquisa

- **RQ1**: How does Artificial Intelligence used during onboarding directly impact business applications’ scalability? [14]
- **RQ2**: How does the technology used in organizations during onboarding affect the productivity of developers? [14]
- **RQ3**: How does the technology skill proficiency influence the productivity of developers? [14]
- **RQ4**: What impact does the technology used in organizations during onboarding have on the scalability of business applications? [14]
- **RQ5**: To what extent does the relationship between onboarding practices and the scalability of business applications mediate the productivity of developers? [14]

---

## Metricas e Instrumentos de Avaliacao

| Metrica | Categoria | Nivel | Como Coletada | Validada |
|---------|-----------|-------|---------------|----------|
| **Artificial Intelligence (AI)** | DevEx / Technical | Individual / Organization | Questionario estruturado (Escala Likert de 5 pontos; itens AI1–AI4) [6, 15, 16] | Yes (PLS-SEM: Cronbach's \\(\alpha = 0.877\\), AVE \\(= 0.731\\), C.R. \\(= 0.916\\)) [17, 18] |
| **Technology Used (TU)** | Technical / Process | Organization / Individual | Questionario estruturado (Escala Likert de 5 pontos; itens TU1–TU4) [6, 15, 16] | Yes (PLS-SEM: Cronbach's \\(\alpha = 0.858\\), AVE \\(= 0.702\\), C.R. \\(= 0.904\\)) [17, 18] |
| **Technology Skill Proficiency (TSP)** | Human / Technical | Individual | Questionario estruturado (Escala Likert de 5 pontos; itens TSK1–TSK4) [6, 15, 16] | Yes (PLS-SEM: Cronbach's \\(\alpha = 0.857\\), AVE \\(= 0.702\\), C.R. \\(= 0.904\\)) [17, 18] |
| **Developer Productivity (DP)** | Productivity | Individual | Questionario estruturado (Escala Likert de 5 pontos; itens DP1–DP4) [6, 15, 16] | Yes (PLS-SEM: Cronbach's \\(\alpha = 0.896\\), AVE \\(= 0.765\\), C.R. \\(= 0.928\\)) [17, 18] |
| **Scalability of Business Applications (SBA)** | Quality / Delivery | Organization / Team | Questionario estruturado (Escala Likert de 5 pontos; itens S1–S4) [6, 15, 16] | Yes (PLS-SEM: Cronbach's \\(\alpha = 0.921\\), AVE \\(= 0.809\\), C.R. \\(= 0.944\\)) [17, 18] |

---

## Frameworks e Metricas

### Frameworks Referenciados
- **Socio-Technical System Theory (STS)** (Majchrzak & Borys; Baxter & Sommerville; Storey et al.): **REFERENCED** — Used as the theoretical basis anchoring social/human aspects (TSP, onboarding) and technical aspects (AI, TU) to application scalability [13, 19].
- *Note*: Standard metrics frameworks such as DORA, SPACE, DevEx, GQM, HEART, or OKR are not explicitly referenced or applied in the paper [13].

### Frameworks Propostos
- **Socio-Technical Onboarding & Scalability Structural Model**: Proposes an empirical PLS-SEM structural framework connecting three onboarding constructs (**AI**, **TU**, **TSP**) to **Scalability of Business Applications (SBA)** with **Developer Productivity (DP)** as a mediating variable [7, 20].

---

## Fatores que Influenciam Produtividade

### Fatores Positivos
| Fator | Categoria |
|-------|-----------|
| **Proficiencia em Habilidades Tecnologicas (TSP)** (Dominio de linguagens de programacao e competência em TIC) [21, 22] | Human / Technical |
| **Tecnologia Utilizada no Onboarding (TU)** (Ferramentas modernas, software adequado e frameworks de desenvolvimento) [22, 23] | Technical / Process |
| **Uso de Inteligencia Artificial (AI)** (Agentes de conversa/mentoria digital, automacao de tarefas repetitivas e assistencia na solucao de problemas) [22, 24] | Technical / Process |
| **Processos Formais de Onboarding** (Estruturas organizadas de integracao de novos membros) [13, 25] | Organizational / Process |
| **Reducao do Tempo de Depuracao (Debugging)** (Capacidade de gerenciar sistemas complexos com suporte minimo) [26] | Technical / Human |

### Fatores Negativos
| Fator | Categoria |
|-------|-----------|
| **Uso de Tecnologias Complexas sem Exposicao Suficiente** (Falta de suporte/treinamento nas ferramentas organizacionais durante o onboarding) [23] | Technical / Organizational |
| **Onboarding Informal ou Desestruturado** (Integracao casual sem diretrizes claras no novo ambiente de trabalho) [13, 27] | Organizational / Process |
| **Falta de Proficiencia Tecnica Inicial** (Leva a maior taxa de bugs, maior tempo de depuracao e dependencia de suporte) [21, 26] | Human / Technical |

---

## Papel da IA e Automacao

| Campo | Valor |
|-------|-------|
| Usa IA/ML? | Yes — AI-assisted onboarding tools (conversational agents/digital mentors, automated documentation access, AI integration in IDEs) [22, 24, 26]. |
| Automacao de coleta? | No — Data was collected manually via an online structured Likert-scale questionnaire administered to developers [6, 12, 15]. |
| Impacto de IA na produtividade? | AI-utilized onboarding has a statistically significant direct impact on Business Application Scalability (\\(\beta = 0.233, p = 0.001, f^2 = 0.146\\), CI \\([0.024, 0.347]\\)) by automating repetitive tasks, accelerating problem-solving, and improving development environment adaptation [22, 28, 29]. |

---

## Resultados Principais

- **Alta Capacidade Explicativa (\\(R^2 = 0.813\\))**: O modelo estrutural explica 81,3% da variancia na Produtividade dos Desenvolvedores (\\(R^2 = 0.813\\)) e na Escalabilidade das Aplicacoes (\\(R^2 = 0.813\\)) [30].
- **Proficiencia Tecnica (TSP) e o Maior Preditor da Produtividade**: A proficiencia tecnica apresentou o maior coeficiente de caminho e tamanho de efeito sobre a produtividade (\\(\beta = 0.507, p < 0.001, f^2 = 0.550\\)) [29, 30].
- **Efeito Direto e Indireto da Tecnologia Utilizada (TU)**: O uso de tecnologias adequadas no onboarding impacta significativamente a Produtividade (\\(\beta = 0.450, p < 0.001, f^2 = 0.434\\)) e a Escalabilidade (\\(\beta = 0.286, p = 0.009, f^2 = 0.118\\)), alem de apresentar efeito indireto total significativo sobre a Escalabilidade (\\(\beta = 0.298\\), IC \\([0.165, 0.516]\\)) [29-31].
- **Efeito Mediador da Produtividade (DP)**: A Produtividade dos Desenvolvedores influencia fortemente a Escalabilidade do sistema (\\(\beta = 0.464, p < 0.001, f^2 = 0.311\\)) [29, 30].
- **Efeito Direto da IA na Escalabilidade**: A utilizacao de IA no onboarding revelou impacto direto e significativo na Escalabilidade (\\(\beta = 0.233, p = 0.001, f^2 = 0.146\\)) [28, 29].
- **Efeitos Indiretos Totais**: Tanto TSP (\\(\beta = 0.144\\), IC \\([0.050, 0.302]\\)) quanto TU (\\(\beta = 0.298\\), IC \\([0.165, 0.516]\\)) demonstraram efeitos indiretos estatisticamente suportados sobre a Escalabilidade via Produtividade [31].

---

## Desafios do Uso das Metricas

- **Uso de Metricas Percebidas vs. Metricas Objetivas**: A pesquisa dependeu de avaliacoes perceptivas autorreportadas pelos desenvolvedores em vez de metricas de engenharia de software objetivas ou indicadores de desempenho do sistema (ex.: latencia, throughput, limites de carga arquitetural) [32].
- **Vies de Metodo Comum (Common Method Bias)**: O uso de questionarios autorreportados para medir variaveis independentes e dependentes simultaneamente traz o risco de vies de resposta [32].
- **Falta de Exposicao a Tecnologias Complexas**: Introduzir ferramentas complexas no onboarding sem treinamento prévio suficiente reduz a motivacao do desenvolvedor e prejudica o processo de integracao [23].
- **Anti-padrao do Onboarding Informal**: Confiar em processos informais de onboarding impede a integracao sistematica entre aspectos sociais e tecnologicos, comprometendo a escalabilidade de longo prazo do software [13, 27].

---

## Avaliacao de Qualidade Metodologica

| Criterio | Pontuacao (0-2) |
|----------|----------------|
| Objetivo claramente definido | 2 |
| Metodologia adequada ao objetivo | 2 |
| Amostra/contexto descrito adequadamente | 2 |
| Ameacas a validade discutidas | 1 |
| Resultados com evidencia suficiente | 2 |
| Contribuicao clara para pratica ou teoria | 2 |
| **TOTAL** | **11/12** |

*Justificativa da pontuacao*:
1. **Objetivo (2/2)**: Objetivos, questoes de pesquisa (RQ1–RQ5) e hipoteses (H1–H5) sao explicitamente declarados [2, 14, 20].
2. **Metodologia (2/2)**: O uso de PLS-SEM com SmartPLS (bootstrapping com 5.000 reamostragens) e altamente adequado para modelos de mediacao socio-tecnica [6, 8, 31].
3. **Amostra/Contexto (2/2)**: Tamanho da amostra (\\(N=104\\)), dados demograficos (genero, experiencia, cargos, escolaridade) e contexto geografico/industrial sao amplamente detalhados [6, 9-12].
4. **Ameacas a Validade (1/2)**: As limitacoes de validade de constructo (ausencia de metricas tecnicas objetivas), vies de metodo comum e amostragem por bola de neve sao discutidas na secao de limitacoes, embora sem testes estatisticos formais aplicados para controle de CMB [32].
5. **Resultados (2/2)**: Apresentacao rigorosa de cargas externas, Cronbach's \\(\alpha\\), Confiabilidade Composta, AVE, VIF, \\(R^2\\), \\(f^2\\), coeficientes de caminho, valores \\(p\\) e intervalos de confianca bootstrap de 95% [16-18, 28-31, 33, 34].
6. **Contribuicao (2/2)**: Integracao teorica clara com a Teoria de Sistemas Socio-Tecnicos (STS) e recomendacoes praticas acionaveis para onboarding em empresas de TI [13, 22].

---

## Limitacoes

- **Medidas Subjetivas/Percebidas**: O estudo baseou-se em percepcoes organizacionais percebidas em vez de metricas de engenharia de software objetivas (como escalabilidade arquitetural ou indicadores de performance do sistema) [32].
- **Amostragem Nao Probabilistica e Generalizacao**: Utilizou amostragem por bola de neve (snowball sampling) para atingir grupos especializados em Sri Lanka, o que limita a generalizacao estatistica para alem da amostra [32].
- **Possibilidade de Vies de Metodo Comum**: Os dados foram coletados por meio de um questionario autorreportado, aumentando a possibilidade de vies de resposta unica [32].
- **Escopo Geografico e Setorial**: As descobertas restringem-se a profissionais de TI em empresas de Sri Lanka, nao sendo necessariamente aplicaveis a outros paises ou setores industriais [32].

---

## Contribuicao Principal

The principal contribution of this study is the empirical validation of an integrated socio-technical framework demonstrating that developer onboarding practices—encompassing AI tools, technological infrastructure, and technology skill proficiency—directly and indirectly drive the scalability of business applications through developer productivity [2, 6, 7, 13, 22]. By focusing on Sri Lanka's IT sector, the paper addresses a key empirical gap regarding human and organizational factors in software scalability within developing economies, confirming that while technical skill proficiency remains the single strongest engine of developer productivity, modern technology tools and AI-assisted onboarding provide essential operational scaling benefits [6, 22, 35].

---

*Extraido via NotebookLM em October 2026 para MLR: Software Developer Metrics in Practice*

---

💡 Would you like me to create a comparative table or synthesize these findings with other papers in your notebook?
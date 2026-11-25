# G016 — Experience with GitHub Copilot for Developer Productivity at Zoominfo

**Decisao: INCLUIDO | Qualidade: 5/6**

---

## Dados Bibliograficos

| Campo | Valor |
|-------|-------|
| **ID** | G016 |
| **Autores** | Gal Bakal, Ali Dasdan, Yaniv Katz, Michael Kaufman, Guy Levin (Zoominfo) |
| **Ano** | 2025 |
| **Venue** | arXiv preprint (arXiv:2501.13282v1 [cs.SE]) |
| **DOI** | N/A (arXiv preprint) |
| **URL** | https://arxiv.org/abs/2501.13282 |
| **Tipo** | Industry Case Study (arXiv preprint, nao peer-reviewed) |
| **GL Tier** | 2nd tier (arXiv preprint by industry practitioners) |
| **Metodo** | Case study: implantacao em 4 fases + metricas quantitativas (acceptance rate via telemetria GitHub) + surveys qualitativos (satisfacao) |
| **Amostra** | 400+ desenvolvedores ativos na Zoominfo; trial controlado com 126 engenheiros (32% dos devs); survey pos-trial com 72 respondentes (57% response rate); dados quantitativos de 26 dias (Nov 14 - Dec 9, 2024) |
| **Contexto** | Industry — enterprise medio-grande (Zoominfo, ~4,000 funcionarios, ~1,000 engenheiros, 400 devs ativos), plataforma Go-to-Market (GTM), distribuida globalmente (US, Europa, India, Israel) |

---

## Objetivo

Apresentar um estudo de caso detalhado sobre avaliacao, trial controlado e implantacao em escala do GitHub Copilot na Zoominfo, respondendo 5 questoes: (1) como avaliar para decisao de deploy em producao, (2) acceptance rates por linguagem, (3) fatores de satisfacao, (4) eficacia na produtividade, (5) limitacoes observadas.

---

## Metodologia: 4 Fases

### Fase 1 — Initial Assessment (Jul 10-17, 2023)
- 5 engenheiros, avaliacao qualitativa
- Resultados: experiencia 8.8/10, produtividade 8.6/10, boa aderencia a coding standards
- Preocupacoes: necessidade de modificar codigo sugerido (3/5 participantes), visibilidade limitada entre projetos, risco de over-reliance

### Fase 2 — Trial Recruitment (Jul 17 - Aug 14, 2023)
- Stratified voluntary sampling: 126 engenheiros (32% dos devs)
- Estratificacao por: especializacao tecnica, experiencia, localizacao geografica, tech stacks
- Pre-requisitos: treinamento de security code review, reconhecimento de compliance (AI governance, data governance, data ethics, data classification)

### Fase 3 — Two-Week Controlled Trial (Aug 15-29, 2023)
- 126 engenheiros integrando Copilot no workflow diario
- Survey pos-trial: 72 respondentes (57% response rate)
- Resultados: satisfacao 8.0/10, produtividade 7.6/10
- Seguranca: vulnerability assessment 8.2/10, sensitive info awareness 8.2/10, security consideration 8.6/10
- Maior utilidade: unit tests, boilerplate code, variable naming, documentacao

### Fase 4 — Rollout (a partir de Sep 7, 2023)
- Deploy via ServiceNow Workflow para controle de licencas
- Ritmo controlado de distribuicao; adocao completa em ~8 meses (Fig 1: ~350 licencas ativas em mid-2024)

---

## Frameworks e Metricas

### Frameworks Mencionados
- **DORA**: mencionado como metrica quantitativa objetiva para produtividade; planejado para avaliacao de impacto de longo prazo (ainda nao reportado neste paper)
- **SPACE**: citado no contexto de fatores que afetam produtividade (Forsgren et al.)
- **DevEx**: discutido como abordagem centrada no desenvolvedor para medir produtividade via sentimentos e percepcoes

### DORA Applied: Parcial (mencionado e planejado, mas resultados de impacto em DORA metrics nao reportados neste paper)
### SPACE Applied: Nao (citado como referencia, nao usado como framework estruturante)
### AI Discussed: Sim (tema central — implantacao de GitHub Copilot)

---

## Metricas de Sucesso Utilizadas

### Metrica Principal: Acceptance Rate of Shown Suggestions
- Adotada seguindo recomendacao de Ziegler et al. (G014/ref [34]) como "better predictor of perceived productivity"
- Definicao: sugestoes aceitas / sugestoes mostradas (parcial acceptance conta como full credit)
- Media geral: 33% para sugestoes, 20% para linhas de codigo
- Relacao: acceptance rate de sugestoes e ~1.5x a de linhas

### Metricas Complementares
| Metrica | Resultado |
|---------|-----------|
| Lines acceptance rate | 20% (media) |
| Developer Satisfaction (DevSat) | 72% (maior entre todas as ferramentas da toolchain) |
| Time savings (self-reported) | 90% relataram reducao; mediana de 20% |
| Tasks per sprint | 63% relataram completar mais tarefas |
| Code quality improvement | 77% relataram melhoria na qualidade |
| LOC contributed by Copilot | centenas de milhares de linhas (acumulado); ~75,000 linhas aceitas em 26 dias |

---

## Resultados Quantitativos Detalhados

### Overall Acceptance Rates (26 dias, Nov 14 - Dec 9, 2024)
- Media diaria: ~6,500 sugestoes e ~15,000 linhas sugeridas
- Media acceptance rate sugestoes: 33% (mediana 32.6%)
- Media acceptance rate linhas: 20% (mediana 20%)
- Tendencia: ligeiramente crescente ao longo do periodo
- Padrao semanal: acceptance rates maiores em finais de semana (padrao ondulado nos graficos)
- Media linhas por sugestao: 2.8 (range 1-10)

### Per Language Acceptance Rates (Fig 5, dados ate Jan 9, 2025)
| Linguagem | Total Suggestions | Acceptance Rate | Lines Acceptance Rate |
|-----------|-------------------|-----------------|----------------------|
| TypeScript | 68,727 | 32.0% | 20.7% |
| Java | 17,833 | 30.1% | 16.8% |
| Python | 9,954 | 31.0% | 19.8% |
| JavaScript | 3,949 | 27.2% | 14.3% |
| HTML | 3,736 | 19.0% | 8.9% |
| CSS | 3,266 | 13.7% | 6.4% |
| YAML | 2,857 | 25.2% | 10.5% |
| JSON | 2,628 | 14.7% | 7.5% |
| Markdown | 2,324 | 26.2% | 9.7% |
| Kotlin | 2,259 | 26.9% | 15.6% |
| SQL | 888 | 16.2% | 7.5% |
| Go | 884 | **43.3%** | **19.7%** |

- Top 4 linguagens (TS, Java, Python, JS): ~80% do total de sugestoes, acceptance rate sustentado em ~30%
- Go: maior acceptance rate (43.3%) mas menor volume; tambem maior linhas/sugestao (>6 vs 2-3 para outras)
- HTML, CSS, JSON, SQL: acceptance rates menores (~14-19%)

### Per Editor (Fig 8)
| IDE | Share of Suggestions | Acceptance Rate | Lines Acceptance Rate | Lines/Suggestion |
|-----|---------------------|-----------------|----------------------|-----------------|
| JetBrains | 58.3% | 28.5% | 15.3% | 3.0 |
| VS Code | 41.7% | 31.1% | 21.5% | 1.8 |

- VS Code: acceptance rate ligeiramente maior; lines acceptance rate ~50% maior que JetBrains
- JetBrains: mais usado na Zoominfo; gera sugestoes com mais linhas por sugestao

---

## Developer Satisfaction (DevSat)

- Quarterly pulse surveys com escala Likert de 5 categorias
- DevSat score = diferenca entre sentimentos positivos e negativos (similar a NPS)
- GitHub Copilot: 72% total satisfaction — maior entre todas ferramentas da software delivery toolchain (acima de Jenkins 0.68, SonarQube 0.54, ArgoCD 0.68, Backstage 0.58)
- Mean satisfaction score: 1.95/8.00 (264 respondentes, 516 total score)
- Positive sentiment: 0.74; Negative sentiment: 0.02

### Feedback Qualitativo (Survey)
- 90% relataram reducao de tempo (mediana 20%)
- 63% completaram mais tarefas por sprint
- 77% relataram melhoria na qualidade do trabalho
- Maiores beneficios: boilerplate code, unit tests, nomes de variaveis, documentacao
- Limitacoes reportadas: falta de domain-specific logic, inconsistencia na qualidade

---

## Limitacoes Observadas e Potenciais

### Observadas
- Dificuldade com logica especifica de dominio (contextual understanding)
- Riscos de seguranca em codigo auto-gerado (requer vetting adicional)
- Gera solucoes previsiveis, menos inovadoras em alguns casos (creativity limitations)

### Potenciais (nao observadas mas antecipadas)
- Exposicao de dados sensiveis (treinamento em repositorios publicos)
- Propriedade intelectual (codigo semelhante a copyrighted)
- Vulnerabilidades de seguranca no codigo gerado
- Privacidade de dados de telemetria
- Compliance risks (codigo nao alinhado com regulamentacoes)
- Over-reliance em IA (desenvolvedores ignoram best practices)
- Reforco de padroes inseguros de repositorios publicos
- Possivel reducao de criatividade e produtividade a longo prazo

---

## Papel da IA e Automacao

**Central neste artigo.** GitHub Copilot e o objeto de estudo. O paper contribui com:

1. Um framework de implantacao em 4 fases para ferramentas de AI coding em empresas de medio/grande porte, incluindo governance, security training, e compliance
2. Evidencia empirica de que acceptance rates em ambiente enterprise (~33%) sao consistentes com os reportados por GitHub (Ziegler et al.) e Google, independente da ferramenta AI especifica
3. Dados granulares por linguagem mostrando que linguagens de proposito geral (TS, Java, Python) tem acceptance rates ~2x maiores que linguagens de markup/query (HTML, CSS, SQL)
4. Metrica DevSat como complemento qualitativo a acceptance rate, mostrando que Copilot tem o maior sentimento positivo entre todas ferramentas da toolchain
5. Reconhecimento explicito de que DORA metrics sao necessarias para avaliacao de longo prazo mas ainda nao foram correlacionadas com uso de Copilot

---

## Avaliacao de Qualidade GL (Garousi et al.)

| Criterio | Score |
|----------|-------|
| Autoridade do autor/organizacao | 1/1 (Zoominfo engineering leadership, Ali Dasdan = VP/Chief Scientist, publicacao tecnica detalhada) |
| Descricao de metodologia | 1/1 (4 fases detalhadas, N reportado, periodos de coleta claros, metricas definidas) |
| Data de publicacao | 1/1 (Jan 2025, atual) |
| Objetividade / vies comercial | 0.5/1 (Autores sao funcionarios da Zoominfo estudando proprio deploy; porem reportam limitacoes e nao vendem produto) |
| Referencias a evidencias externas | 0.5/1 (37 referencias, mas varias sao blog posts e YouTube; inclui Forsgren/SPACE, Ziegler et al., Chen/Codex) |
| Contribuicao original | 1/1 (Primeiro case study detalhado de enterprise deployment com dados de acceptance rate por linguagem e IDE em empresa nao-tech) |
| **Total** | **5/6** |

**Nota:** NotebookLM deu 6/6, mas reduzi Objetividade para 0.5 (autores estudam proprio deploy) e Referencias para 0.5 (mix de fontes academicas e informais). Score mais realista: 5/6.

---

## Relacao com Outros Papers do MLR

- **G014 (Ziegler et al.)**: Zoominfo adotou acceptance rate como metrica principal explicitamente baseado nos achados de Ziegler et al. Os acceptance rates sao consistentes (Zoominfo 33% vs Ziegler 27%). Zoominfo nao reproduz a analise de correlacao com produtividade percebida, mas assume a relacao.
- **G009 (DORA 2025)**: Zoominfo menciona DORA metrics como objetivo de longo prazo mas nao reporta dados. O paper DORA 2025 mostra que 90% adotaram AI — Zoominfo e um caso concreto desta tendencia.
- **Relevancia para RQ3**: fornece evidencia de implantacao enterprise de AI coding tool com dados quantitativos e qualitativos, complementando o paper de Ziegler (que e do ponto de vista do vendor/GitHub) com perspectiva de empresa-cliente.

---

## Contribuicao Principal

Bakal et al. (2025) apresentam o primeiro case study detalhado de implantacao de GitHub Copilot em uma empresa de medio porte nao-tech (Zoominfo, 400+ devs), com um framework sistematico de 4 fases que inclui governance e compliance de AI. Suas contribuicoes para o MLR sao: (1) validacao externa de que acceptance rates em producao (~33%) sao consistentes com dados reportados por GitHub e outros vendors, (2) dados granulares de acceptance rate por 12 linguagens de programacao e 2 IDEs mostrando variacoes significativas (Go 43% vs CSS 14%), (3) integracao de DevSat (developer satisfaction) como metrica qualitativa complementar via quarterly pulse surveys, e (4) evidencia de que 90% dos desenvolvedores reportam reducao de tempo (mediana 20%) e 63% completam mais tarefas por sprint. As limitacoes incluem ausencia de grupo de controle, self-report bias, e foco exclusivo em uma ferramenta (Copilot). Para o MLR, este paper e relevante para RQ3 (AI e produtividade) como caso de adocao enterprise e para RQ1/RQ2 como exemplo de uso combinado de metricas quantitativas (acceptance rate) e qualitativas (DevSat) na pratica.

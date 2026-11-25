# P0061 — How Developers and Managers Define and Trade Productivity for Quality

**Decisao: INCLUIDO | Qualidade: 4/5**

---

## Dados Bibliograficos

| Campo | Valor |
|-------|-------|
| **ID** | P0061 |
| **Autores** | Margaret-Anne Storey, Brian Houck, Thomas Zimmermann |
| **Ano** | 2022 |
| **Venue** | CHASE '22 (ACM/IEEE 15th Cooperative and Human Aspects of SE) |
| **Tipo** | Conference paper |
| **Metodo** | Exploratory survey + focus groups + interviews + inductive coding |
| **Amostra** | 131 developers + 34 managers at Microsoft |
| **Contexto** | Microsoft; large enterprise |

---

## Objetivo

Investigar como desenvolvedores e managers definem produtividade e qualidade, quao alinhados estao, e se/como fazem trade-offs entre eles.

---

## Questoes de Pesquisa

- **RQ1**: How do developers and managers define productivity?
- **RQ2**: Do developers and managers understand how the other cohort defines productivity?
- **RQ3**: How do developers and managers define quality? How aligned are developers and managers in their definitions?
- **RQ4**: Do developers and managers trade quality for productivity? What reasons do they give for not trading?

---

## Dados da Pesquisa

### Amostra
- **Total participants**: 165 respondentes (131 developers + 34 managers)
- **Organizacao**: Microsoft (contexto industrial enterprise)
- **Periodo**: Survey administered Junho 2020
- **Modo de coleta**: Online survey (self-administered)

### Caracteristicas da Amostra

**Developers (n=131)**:
- Diversos niveis de seniority (junior a senior)
- Diferentes roles (SWE, QA, etc.)
- Multiple product teams within Microsoft

**Managers (n=34)**:
- Engineering managers (diretos de devs)
- Team leads
- Product managers (em alguns casos)

### Metodo de Coleta

**Fase 1: Exploratory survey**
- Open-ended questions sobre definicoes de "productivity" e "quality"
- Questoes sobre trade-offs
- Participants encouraged to provide detailed responses

**Fase 2: Focus groups** (subset de survey respondents)
- Exploracao mais profunda de discrepancias encontradas na survey
- Discussao sobre barreiras e facilitadores

**Fase 3: Interviews** (selected high-value respondents)
- Entrevistas individuais para aprofundar understanding
- 1-on-1 format

### Survey Questions

**Developer Survey**:
- "When thinking about your work, how do you define productivity?"
- "How do you think your manager defines productivity?"
- "When thinking about your work, how do you define quality?"
- "Have you ever had to make trade-offs between productivity and quality? If so, please explain."

**Manager Survey**:
- "When thinking about your team, how do you define productivity?"
- "How do you think the developers you manage define productivity?"
- "When thinking about your team, how do you define quality?"
- "Has your team had to make explicit trade-offs between productivity and quality? If so, describe."

---

## Metricas e Instrumentos de Avaliacao

### Codificacao de Respostas Abertas

**Metodo**: Inductive content analysis (bottom-up coding)
- Pesquisadores codificaram respostas iterativamente
- Identificacao de temas emergentes
- Alignamento com SPACE framework (Satisfacao, Performance, Activity, Collaboration, Efficiency)

### Codigos de Produtividade (SPACE-aligned)

| Codigo | Dimensao SPACE | Descricao | Frequencia (devs %) | Frequencia (mgrs %) |
|--------|---|---|---|---|
| **S** | Satisfaction | Satisfacao, bem-estar pessoal, engagement | ~8% | ~9% |
| **P** | Performance | Performance, qualidade dos resultados, impacto | ~35% | ~67%* |
| **A** | Activity | Contagem de acoes, outputs (PRs, commits, bugs) | ~56%* | ~21% |
| **C** | Collaboration | Comunicacao, colaboracao, teamwork | ~24% | ~33% |
| **E** | Efficiency | Eficiencia, flow, sem interrupcoes | ~38%* | ~15% |

*Asteriscos indicam diferenca estatistica significativa entre devs e mgrs (Fisher's exact test, p<.05)

### Codigos de Qualidade

| Codigo | Descricao | Frequencia (devs %) | Frequencia (mgrs %) |
|--------|-----------|---|---|
| **T** | Timeliness/predictable delivery | ~13% | ~12% |
| **R** | Robustness (reliable, tested, secure) | ~38%* | ~88%* |
| **U** | Meets user/stakeholder needs | ~24% | ~33% |
| **C** | Readable, documented for collaboration | ~17% | ~18% |
| **E** | Evolvable design with tests | ~44%* | ~6%* |

*Asteriscos indicam diferenca significativa entre devs e mgrs

### Teste Estatistico

**Metodo**: Fisher's exact test (para tabelas de contingencia 2×k, small samples)
- Compara distribuicao de codigos entre developers vs managers
- Threshold: p < .05 para significancia

### Trade-off Analysis

**Resposta a RQ4**: "Do you trade quality for productivity?"
- **Developers**: 52% responderam "Yes"
- **Managers**: 59% responderam "Yes"
- **Ambos**: ~1/3 considera qualidade PARTE da produtividade (nao separavel)
- **Chi-square test**: Nao significativamente diferente entre grupos

**Razoes para trade-offs** (thematic):
- Pressao de deadlines (most common)
- Legacy code constraints
- Technical debt necessity
- Feature delivery priorities
- Resource limitations

**Razoes para NOT trading** (thematic):
- Quality foundational to productivity
- Technical debt consequences
- Team morale/burnout prevention
- Customer satisfaction paramount
- Long-term sustainability

---

## Codigos de Produtividade (alinhados com SPACE)

| Codigo | Dimensao SPACE | Descricao |
|--------|---------------|-----------|
| S | Satisfaction | Satisfacao e bem-estar pessoal |
| P | Performance | Performance e qualidade dos resultados |
| A | Activity | Contagem de acoes ou outputs |
| C | Collaboration | Comunicacao e colaboracao |
| E | Efficiency | Eficiencia e flow sem interrupcoes |

## Codigos de Qualidade

| Codigo | Descricao |
|--------|-----------|
| T | Timely and predictable delivery |
| R | Robustness (reliable, tested, secure) |
| U | Meets user/stakeholder needs |
| C | Readable, documented for collaboration |
| E | Evolvable design with tests |

---

## Resultados Principais

1. **Devs definem produtividade como Activity** (tarefas completadas, PRs, commits)
2. **Managers definem como Performance/Efficiency** (resultados de qualidade, eficiencia)
3. **Devs NAO conseguem prever** como managers definem produtividade
4. **Qualidade**: ambos concordam = **Robustness** (maioria)
5. **>50% fazem trade-offs** qualidade por produtividade (com boas razoes)
6. **~1/3 considera qualidade parte da produtividade** (nao separavel)

---

## Desafios do Uso das Metricas

1. **Misalignment dev-manager** em definicoes de produtividade
2. **Trade-offs quality-productivity** sao comuns e inevitaveis
3. **Metricas universais falham** porque definicoes variam por papel
4. **Qualidade e multidimensional** (robustness, UX, evolvability)

---

## Avaliacao de Qualidade: 11/12 (Alta)

## Limitacoes

1. **Single company (Microsoft)** — generalizacao limitada
2. **Amostra pequena** (especialmente managers: 34)
3. **Low response rate** (9% devs, 5% managers)
4. **Open-ended survey** — possivel ambiguidade

---

## Contribuicao Principal

Evidencia empirica de misalignment entre devs e managers em definicoes de produtividade. Devs = Activity, Managers = Performance/Efficiency. Codigos emergentes alinham com SPACE. Trade-offs sao comuns. Storey + Zimmermann (pesquisadores-chave).

---

*Extraido em Marco 2026 para MLR: Software Developer Metrics in Practice*

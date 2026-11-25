# P0016 — The Productivity Paradox of AI-Powered Development

**Decisao: INCLUIDO | Qualidade: 3/5**

---

## Dados Bibliograficos

| Campo | Valor |
|-------|-------|
| **ID** | P0016 |
| **Autores** | Luciane Fortes, Guilherme Vaz Pereira, André Coelho, Rafael Prikladnicki, Karina Kohl |
| **Ano** | 2025 |
| **Venue** | IEEE Software (accepted for publication) |
| **Tipo** | Journal article |
| **Metodo** | Survey + regression analysis + thematic analysis |
| **Amostra** | 106 developers (61 Copilot, 45 Gemini users) |
| **Contexto** | Large Brazilian company; multiple platforms and dev teams |

---

## Objetivo

Explorar como AI code assistants influenciam produtividade percebida dos desenvolvedores via dimensoes DevEx.

---

## Questoes de Pesquisa

- **RQ1**: Como as dimensoes de DevEx estao associadas a produtividade percebida dos desenvolvedores ao usar AI code assistants?

---

## Dados da Pesquisa

### Amostra e Contexto
- **Tamanho total**: 106 desenvolvedores
  - GitHub Copilot users: 61 (57.5%)
  - Gemini Code Assist users: 45 (42.5%)
- **Contexto organizacional**: Grande empresa brasileira (contexto industrial)
- **Periodo de coleta**: Marco-Abril 2025
- **Experiência profissional**: Diversos niveis de tenure (Junior, Mid, Senior, Specialist)

### Metodo de Coleta
- **Tipo de survey**: Online survey com escala Likert 1-5
- **Distribuicao**: Via Slack e email (internal communication channels)
- **Anonimidade**: Respostas anonimizadas, seguindo politicas internas de privacidade
- **Plataformas de IA testadas**:
  - GitHub Copilot (principal ferramenta Copilot users)
  - Gemini Code Assist (principal ferramenta Gemini users)

### Instrumentos de Medicao
- **Escala**: Likert 1-5 pontos
- **Dimensoes DevEx medidas** (3 principais):
  1. **Feedback Loops** (3 items)
  2. **Cognitive Load** (2-3 items dependendo da ferramenta)
  3. **Flow State** (2 items)

### Variables Medidas

**Feedback Loops**:
- "I write better quality code" (item 1)
- "I finish tasks faster" (item 2)
- "I learn from the suggestions the assistant shows me" (item 3)

**Cognitive Load**:
- "I spend less time searching for information or examples"
- "I spend less mental effort on repetitive tasks"
- (Item removido do Gemini por baixa confiabilidade: α < 0.6)

**Flow State**:
- "I get into the 'development flow' more easily"
- "I enjoy programming more"

---

## Metodologia Detalhada

### Contexto e Amostra
- **Empresa**: Grande empresa brasileira (contexto industrial)
- **Ferramenta principal**: GitHub Copilot e Gemini Code Assist
- **Amostra total**: 106 desenvolvedores (61 Copilot, 45 Gemini)
- **Coleta**: Survey online distribuido via Slack e email (Marc-April 2025)
- **Anonimidade**: Respostas anonimizadas, seguindo politicas internas

### Estrutura do Survey
Survey baseado em Likert scale (1-5) com 3 dimensoes DevEx principais:

#### Feedback Loops
- "I write better quality code"
- "I finish tasks faster"
- "I learn from the suggestions the assistant shows me"
- **Cronbach α (Copilot)**: 0.696

#### Cognitive Load
- "I spend less time searching for information or examples"
- "I spend less mental effort on repetitive tasks"
- **Cronbach α (Copilot)**: 0.796
- **Nota**: Item de Cognitive Load removido do Gemini (α < 0.6)

#### Flow State
- "I get into the 'development flow' more easily"
- "I enjoy programming more"
- **Cronbach α (Copilot)**: 0.806

### Analise Estatistica
- **Modelos de regressao**: Productivity (Task Completion Efficiency + Flow State)
- **Comparacoes**: Mann-Whitney U tests para diferencas entre ferramentas por tenure group
- **Analise qualitativa**: Thematic analysis de respostas abertas

---

## Metricas e Instrumentos de Avaliacao

### Reliability/Consistencia Interna (Cronbach's α)

| Dimensao | GitHub Copilot | Gemini Code Assist | Interpretacao |
|----------|---|---|---|
| **Feedback Loops** | 0.696 | 0.767 | Aceitavel (>0.6 threshold) |
| **Cognitive Load** | 0.796 | 0.582* | Copilot aceitavel; Gemini abaixo do threshold |
| **Flow State** | 0.806 | 0.681 | Ambos aceitaveis |

*Item removido do Gemini por baixa confiabilidade; composto score reduzido

### Descritiva Estatistica (Mean e Composite Scores)

| Dimensao | Copilot (Mean) | Gemini (Mean) | U-statistic | p-value |
|----------|---|---|---|---|
| **Feedback Loops** | 0.688 | 0.926 | 1101.0 | 0.0783 (não significativo) |
| **Cognitive Load** | 1.418 | 1.267 | 1576.5 | 0.1472 (não significativo) |
| **Flow State** | 0.729 | 0.489 | 1614.5 | 0.1157 (não significativo) |

**Metodo de analise**: Mann-Whitney U Tests (não-parametrico, dados Likert com distribuicao não-normal)

### Regressão Linear: Predicao de Produtividade

#### GitHub Copilot (R² = 0.450, F = 15.54, p < 0.001)
| Dimensao | Coeficiente β | p-value | Significancia | Força |
|----------|---|---|---|---|
| **Feedback Loops** | 0.437 | p < 0.001 | *** | MUITO FORTE (2x que Gemini) |
| **Cognitive Load** | -0.058 | p = 0.595 | NS | Não significativo |
| **Flow State** | 0.314 | p = 0.011 | ** | SIGNIFICATIVO |

**Interpretacao Copilot**:
- Feedback Loops domina predicao de produtividade (β=0.437 maior)
- Flow State tem efeito auxiliar significativo para "imersão" desenvolvedora
- Cognitive Load nao significativo (pode estar saturado em valor baixo)
- Modelo explica 45% da variancia em produtividade

#### Gemini Code Assist (R² = 0.381, F = 10.03, p < 0.001)
| Dimensao | Coeficiente β | p-value | Significancia | Força |
|----------|---|---|---|---|
| **Feedback Loops** | 0.865 | p < 0.001 | *** | MUITO FORTE (quase 2x Copilot) |
| **Cognitive Load** | 0.247 | p = 0.143 | ~sig | Marginalmente significativo |
| **Flow State** | -0.170 | p = 0.309 | NS | NEGATIVO/distrator |

**Interpretacao Gemini**:
- Feedback Loops MUITO mais importante (β=0.865 vs 0.437 Copilot)
- Gemini depende mais da qualidade de sugestoes (não de flow)
- Flow State negativo: sugestoes podem distrair do fluxo original
- Cognitive Load marginalmente positivo (menos significativo)
- Modelo explica 38% da variancia

### Analises Estratificadas por Tenure (Mann-Whitney U Tests)

| Grupo | n | Feedback (Copilot) | Feedback (Gemini) | Flow (Copilot) | Flow (Gemini) | p-value |
|-------|---|---|---|---|---|---|
| **Junior** | 24 | 0.58 | 1.31 | 0.55 | 0.81 | p=0.012* |
| **Mid** | 23 | 0.79 | 0.72 | 1.18 | 0.46 | p=0.005** |
| **Senior** | 30 | 0.75 | 0.74 | 0.68 | 0.39 | p=0.063 |
| **Specialist** | 29 | 0.62 | 0.91 | 0.64 | 0.14 | p=0.604 |

**Achados principais por tenure**:
- **Junior developers**: Gemini Feedback SIGNIFICATIVAMENTE MAIOR (1.31 vs 0.58, p=0.012)
- **Mid developers**: Diferenca significativa em ambas dimensoes
- **Senior/Specialist**: Sem diferencas significativas (ferramentas equivalentes)
- **Implicacao**: Ferramentas beneficiam desenvolvedores menos experientes diferentemente

### Testes de Efeito (Effect Sizes)
- **Cliff's Δ** (non-parametric effect size):
  - Feedback Loops: Δ = -0.198 (small effect, Gemini slightly higher)
  - Cognitive Load: Δ = 0.148 (small effect, negligible)
  - Flow State: Δ = 0.176 (small effect, Copilot slightly higher)

### Estatistica de Validacao
- **Teste utilizado**: Mann-Whitney U (escala ordinal, n pequeno, distribuicao não-normal)
- **Thresholds de significancia**: p < 0.05 (*), p < 0.01 (**), p < 0.001 (***)
- **Ameacas a validade**:
  - Single company (contexto Brasil apenas)
  - Self-reported perceptions (sem medidas objetivas)
  - Cronbach α < 0.6 para Cognitive Load Gemini (item removido)
  - Grupos desbalanceados (61 vs 45)
  - Cross-sectional (sem longitudinal tracking)

### DevEx Dimensions Medidas

| Dimensao | Items (Copilot) | α | Mean |
|----------|----------------|---|------|
| Feedback Loops | Code quality, task speed, learning | 0.696 | 0.688 |
| Cognitive Load | Search time, mental effort | 0.796 | 1.418 |
| Flow State | Dev flow, enjoyment | 0.806 | 0.729 |

### Regression Results por Ferramenta

#### GitHub Copilot
| Dimensao | β | Significancia | Impacto |
|----------|---|---|---|
| **Feedback Loops** | 0.437 | p < 0.001 | MUITO FORTE (coef. de regressao quase 2x que Gemini) |
| **Cognitive Load** | -0.058 | p = 0.595 | Nao significativo |
| **Flow State** | 0.314 | p = 0.011 | SIGNIFICATIVO |
| **R² ajustado** | 0.450 | F = 15.54 | Explica 45% da variancia |

#### Gemini Code Assist
| Dimensao | β | Significancia | Impacto |
|----------|---|---|---|
| **Feedback Loops** | 0.865 | p < 0.001 | MUITO FORTE (quase 2x Copilot) |
| **Cognitive Load** | 0.247 | p = 0.143 | Marginalmente significativo |
| **Flow State** | -0.170 | p = 0.309 | NEGATIVO (distrai do flow) |
| **R² ajustado** | 0.381 | F = 10.03 | Explica 38% da variancia |

### Diferencas por Tenure (Mann-Whitney U Tests)

| Grupo | Feedback (Copilot) | Feedback (Gemini) | Flow (Copilot) | Flow (Gemini) | p-value |
|-------|---|---|---|---|---|
| **Junior (n=24)** | 0.58 | 1.31 | 0.55 | 0.81 | p=0.012* |
| **Mid (n=23)** | 0.79 | 0.72 | 1.18 | 0.46 | p=0.005** |
| **Senior (n=30)** | 0.75 | 0.74 | 0.68 | 0.39 | p=0.063 |
| **Specialist (n=29)** | 0.62 | 0.91 | 0.64 | 0.14 | p=0.604 |

**Achado principal**: Diferencas significativas estao concentradas em **junior developers**, com **Gemini scoring MAIS ALTO em Feedback** do que Copilot (1.31 vs 0.58, p=0.012).

### Key Findings
- **Feedback Loops** domina predicao de produtividade para ambas ferramentas
- **Copilot**: Flow State significativo (β=0.314, p=0.011) — melhor para "imersao"
- **Gemini**: Feedback loops muito mais forte (β=0.865 vs 0.437) — depende mais de qualidade de sugestoes
- **Cognitive Load**: Nao significativamente associado a produtividade em ambas as ferramentas
- **Efeito Tenure**: Diferencas significativas concentradas em junior developers (p=0.012 para Feedback)
- **Paradoxo confirmado**: AI tools podem tanto melhorar quanto prejudicar produtividade dependendo de patterns de interacao, cognitive load e contexto

---

## Limitacoes

1. **Single company** (brasileira)
2. **Self-reported perceptions** apenas
3. **Unequal groups** (61 vs 45)
4. **Cross-sectional** — sem longitudinal
5. **Cronbach α < 0.6** para Cognitive Load do Gemini

---

## Contribuicao Principal

Primeiro estudo comparando Copilot vs Gemini Code Assist via DevEx framework. Identifica paradoxo: AI pode melhorar e prejudicar produtividade. Feedback loops dominam. Contribuicao brasileira (PUCRS + UFRGS).

---

*Extraido em Marco 2026 para MLR: Software Developer Metrics in Practice*

# P0189 — Organizational Ohm's Law — Case in Point: Engineering Velocity

**Decisao: INCLUIDO | Qualidade: 4/5**

---

## Dados Bibliograficos

| Campo | Valor |
|-------|-------|
| **ID** | P0189 |
| **Autores** | Fei Liu, Todd McKinnon |
| **Ano** | 2024 |
| **Venue** | IEEE Transactions on Engineering Management, Vol. 71 |
| **Tipo** | Journal article (11 pages) |
| **Metodo** | Literature review + 20+ interviews + case study + equivalent circuit modeling |
| **Amostra** | 20+ engineers, managers, product managers; Okta engineering organization |
| **Contexto** | Okta Inc. (identity provider); Google, Microsoft (external examples) |

---

## Dados da Pesquisa

### Dataset e Amostra
- **Participantes**: 20+ engineers, managers, product managers da Okta Inc.
- **Método de coleta**: Entrevistas semi-estruturadas + análise de literatura + observações de especialistas
- **Contexto organizacional**: Okta Inc. (identity provider company), com exemplos comparativos de Google e Microsoft
- **Período de coleta**: Não especificado, mas study é contemporâneo ao framework proposal
- **Fontes de dados**:
  - Literatura acadêmica (DEX, organizational design, motivation theories)
  - Best practices industry (OKRs, Conway's Law, Brooks's Law, Spotify model)
  - Experiência própria dos autores (Okta engineering organization)
  - Observações de equipes (infrastructure, process, structure resistance factors)

### Instrumentos e Variáveis Medidas
- **Observações qualitativas**: Documentação de team structures, communication patterns, processo decisions
- **Expertise analysis**: Retrospective knowledge from seasoned engineers and managers at Okta
- **Equivalent circuit modeling**: Mapping teams and dependencies to electrical circuit analogues
- **Variáveis principais**:
  - I_outcome: organizational velocity (outcome current)
  - V: organizational potential (skills × motivation)
  - R: organizational resistance (structure + process + infrastructure)
  - η: outcome-output efficiency

### Método de Coleta
- Entrevistas com profissionais de diferentes backgrounds (engineers, managers, product managers)
- Análise documental de best practices e literatura de engenharia e management
- Case study approach (Okta como primary case, Google/Microsoft como comparative examples)
- Iterative refinement baseado em feedback de experts

---

## Metricas e Instrumentos de Avaliacao

### Metricas Formais (Modelo OOL)

| Métrica | Fórmula | Definição | Escala |
|---------|---------|-----------|--------|
| **Engineering Velocity (I_outcome)** | I_outcome = η × V/R | Taxa de resultados organizacionais efetivos | Relativa (em termos de outcomes) |
| **Organizational Potential (V)** | V = π_i(Skills, Motivation) | Potencial médio individual (skills × motivation) | 0-max (contexto-dependente) |
| **Outcome-Output Efficiency (η)** | η = I_outcome / I_output | Eficiência na conversão output→outcome | 0-1 ou 0-100% |
| **Organizational Resistance (R)** | R = R_structure + R_process + R_infrastructure | Somatório de resistências dos 3 tipos | Relativa |
| **Structure Resistance** | R^structure ∝ Σ(communication paths × costs) | Resistência de comunicação e coordenação entre equipes | Baseada em path complexity |
| **Process Resistance** | R^process (planning, code review, security review, release) | Fricção de processos organizacionais | Qualitativa (baixa/média/alta) |
| **Infrastructure Resistance** | R^infrastructure (CI/CD, tooling, tech debt, coupling) | Fricção técnica de arquitetura e tooling | Qualitativa (baixa/média/alta) |

### Abordagem de Avaliação

#### 1. **Validação via Equivalent Circuit Model**
- Teams independentes mapeados como resistores em **paralelo** (menor resistência total)
- Teams dependentes mapeados como resistores em **série** (maior resistência total)
- Arquitetura monolítica vs microservices: análise de mudanças em R_infrastructure
- Framework-outcome mapping (Conway's Law, Brooks's Law, Two-Pizza Rule explicados via OOL)

#### 2. **Análise de Casos de Uso**
- **Google**: Estrutura de equipes autônomas (parallel configuration) → velocidade alta
- **Microsoft**: Estrutura com dependências (serial configuration) → desafios de velocity
- **Okta**: Implementação de microservices → redução de infrastructure resistance

#### 3. **Validação de Conceitos**
- Consistência lógica do framework com best practices conhecidas
- Mapeamento bidirecional: OOL variables ↔ Best practices
- Análise qualitativa via expertise de researchers e industry practitioners

### Limitações das Metricas

1. **Framework predominantemente qualitativo** — não quantificado em valores numéricos neste paper (quantificação deixada para work companion)
2. **Outcome-output efficiency (η) é nebulosa em software** — difícil definir operacionalmente o que constitui "outcome" vs "output"
3. **Resistência não é diretamente mensurável** — requer proxy measures (communication paths, process cycle times, tooling assessment)
4. **Validação empírica limitada** — baseada principalmente em Okta; generalizability para outras organizações desconhecida
5. **Analogia com circuitos eletricos** — nem todas as propriedades físicas transferem para domínio organizacional
6. **Fatores dinâmicos não capturados** — o framework é estático; mudanças em motivation ou external context não modeladas

### Tratamento de Ameacas à Validade

- **Construct validity**: Framework lógico baseado em multidisciplinary literature (physics + management + software engineering)
- **External validity**: Exemplos de Google e Microsoft fornecem alguma triangulação além de Okta
- **Internal validity**: Feedback iterativo de experts ajuda a refinar interpretações
- Não estabelece **causalidade** — é um modelo descritivo, não preditivo

---

## Objetivo

Propor Organizational Ohm's Law (OOL) como framework para compreender produtividade organizacional de engenharia (engineering velocity), usando analogia com lei de Ohm da engenharia eletrica.

---

## Questoes de Pesquisa

- **RQ1**: Can Organizational Ohm's Law from electrical engineering be applied to understand engineering velocity in software organizations?
- **RQ2**: How can organizational resistance (structure, process, infrastructure) be decomposed and understood using an equivalent circuit approach?
- **RQ3**: What are the key organizational and individual factors that drive engineering velocity and how do they relate to best practices?

---

## Framework: Organizational Ohm's Law (OOL)

### Formula Principal
```
I_outcome = η × V/R
```
- **I_outcome** (Outcome Current): velocidade organizacional em termos de resultados efetivos
- **η** (Outcome-Output Efficiency): eficiencia na conversao de outputs em outcomes
- **V** (Organizational Potential): potencial individual medio (skills × motivation)
- **R** (Organizational Resistance): R_structure + R_process + R_infrastructure

### Decomposicao de Resistencia
- **Structure Resistance**: comunicacao entre equipes, hierarquia, dependencias organizacionais
  - R^structure ∝ Σ(communication paths × costs)
- **Process Resistance**: agile planning, code review, security review, release process
- **Infrastructure Resistance**: CI/CD pipelines, tooling, tech debt, loosely coupled architectures

### Equivalent Circuit Approach
- Equipes independentes = resistores em paralelo
- Equipes dependentes = resistores em serie
- Equipes centralizadas = resistencia dinamica (estados normal/transfer)
- Interacao entre Engineering, Product e Sales = circuito organizacional completo

### Best Practice Mapping (Table II)
| OOL Variable | Best Practices |
|-------------|---------------|
| Engineering Velocity | OKRs, aligned goals, single-threaded leaders |
| Outcome-Output Efficiency | Motivation theories, culture of trust, innovation, incentives |
| Structure Resistance | Conway's law, Brooks's law, two-pizza principle, Spotify model |
| Process Resistance | Agile, CI/CD, code/security review, hackathons |
| Infrastructure Resistance | Loosely coupled architectures, CI/CD pipelines, docs, platform |

---

## Resultados Principais

1. **Framework intuitivo** para entender engineering velocity holistically
2. **Equipes menores** = menor resistencia intra-equipe (suporta two-pizza rule)
3. **Equipes dependentes** = resistores em serie, aumentam resistencia total
4. **Monolito → microservicos** reduz infrastructure e structure resistance
5. **Google, Microsoft, Brooks** explicados consistentemente pelo framework

---

## Desafios do Uso das Metricas

1. **Framework qualitativo** — nao quantificado neste paper
2. **Analogia com circuito eletrico** — nem todas propriedades transferem
3. **Resistencia dificil de medir** objetivamente
4. **Baseado principalmente em experiencia de Okta**
5. **Eficiencia outcome-output** e conceito nebuloso em SW

---

## Avaliacao de Qualidade

| Criterio | Pontuacao (0-2) |
|----------|----------------|
| Objetivo claramente definido | 2 |
| Metodologia adequada | 2 |
| Amostra/contexto descrito | 1 |
| Ameacas a validade discutidas | 1 |
| Resultados com evidencia | 2 |
| Contribuicao clara | 2 |
| **TOTAL** | **10/12 (Alta)** |

---

## Limitacoes

1. **Framework qualitativo** — sem metricas mensuraveis neste paper
2. **Okta-centric** — experiencia de uma empresa predomina
3. **Equivalent circuit e analogia** — limites da transferencia fisica→organizacional
4. **20+ interviews** mas detalhes metodologicos limitados
5. **Sem validacao quantitativa** (feita no paper companion)

---

## Contribuicao Principal

Framework Organizational Ohm's Law (I_outcome = η × V/R) para compreender engineering velocity, com abordagem de circuito equivalente para decompor resistencia organizacional. Publicado em IEEE Transactions on Engineering Management. Autores: Fei Liu (pesquisadora em Okta/Huawei/IBM) e Todd McKinnon (CEO e co-fundador da Okta).

---

*Extraido em Marco 2026 para MLR: Software Developer Metrics in Practice*

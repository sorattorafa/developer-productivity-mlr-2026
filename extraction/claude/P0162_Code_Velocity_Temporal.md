# P0162 — Are We Speeding Up or Slowing Down? On Temporal Aspects of Code Velocity

**Decisao: INCLUIDO | Qualidade: 3/5**

---

## Dados Bibliograficos

| Campo | Valor |
|-------|-------|
| **ID** | P0162 |
| **Autores** | Gunnar Kudrjavets, Nachiappan Nagappan, Ayushi Rastogi |
| **Ano** | 2023 |
| **Venue** | IEEE/ACM MSR 2023 (Mining Software Repositories) |
| **Tipo** | Conference paper |
| **Metodo** | Repository mining |
| **Amostra** | 283,235 code reviews de 4 projetos OSS (~7 anos) |
| **Contexto** | Open source (Blender, FreeBSD, LLVM, Mozilla) |

---

## Objetivo

Investigar como a duracao de periodos de code review muda ao longo da vida de projetos OSS, testando duas teorias contraditorias da industria: code velocity acelera ou desacelera com o tempo.

---

## Questoes de Pesquisa

- **RQ**: How does a project's code velocity trend over time? Does the code velocity increase, decrease, or stay neutral?

---

## Metricas

### Code Velocity Metrics
| Metrica | Categoria | Nivel | Como Coletada | Validada |
|---------|-----------|-------|---------------|----------|
| Time-to-first-response | Eficiencia | Equipe | Code review systems (Phabricator, Gerrit) | Sim |
| Time-to-accept | Eficiencia | Equipe | Code review systems | Sim |
| Time-to-merge | Velocidade de entrega | Equipe | Code review systems | Sim |

### Code Churn Metrics
| Metrica | Descricao | Dados |
|---------|-----------|-------|
| SLOC change | Mudanca anual em linhas de codigo | 3-17% crescimento/ano |
| Commit count | Numero de commits por ano | Variavel por projeto |
| Distinct authors | Autores unicos por ano | Variavel por projeto |
| Distinct committers | Committers unicos por ano | Variavel por projeto |

### Classificacao
- **Objetivas**: Todas (coletadas automaticamente de repositorios)
- **Output**: Commit count, SLOC
- **Processo**: Time-to-first-response, time-to-accept, time-to-merge

---

## Resultados Principais

| Projeto | Periodo | SLOC/ano | Time-to-merge tendencia |
|---------|---------|----------|------------------------|
| Blender | 2014-2022 | +6.2% | Sem tendencia direcional |
| FreeBSD | 2014-2022 | +3.5% | Estavel ou diminui |
| LLVM | 2014-2022 | +17.4% | Diminui |
| Mozilla | 2017-2022 | +11.1% | Diminui |

**Conclusoes-chave:**
1. Nem a passagem do tempo nem o tamanho do projeto impactam code velocity
2. Crescimento de codebase (3-17%/ano) NAO acompanha reducao de velocidade
3. 30-day moving median permanece em faixa fixa para time-to-merge
4. Comportamento auto-corretivo: core team members garantem reviews em tempo

---

## Desafios do Uso das Metricas

1. **Teorias contraditorias na industria**: nao ha consenso se code velocity acelera ou desacelera
2. **Autocorrelacao em time-series**: desafio tecnico para analise de tendencias
3. **Variabilidade em projetos menores**: Blender mostra mais variacao (menos commits/autores)
4. **OSS vs industria**: incentivos diferentes podem afetar generalizacao
5. **Auto-correcao**: core team members podem mascarar tendencias reais

---

## Avaliacao de Qualidade

| Criterio | Pontuacao (0-2) |
|----------|----------------|
| Objetivo claramente definido | 2 |
| Metodologia adequada | 2 |
| Amostra/contexto descrito | 1 |
| Ameacas a validade discutidas | 2 |
| Resultados com evidencia | 1 |
| Contribuicao clara | 1 |
| **TOTAL** | **9/12 (Alta)** |

---

## Limitacoes

1. **Apenas projetos OSS** — incentivos diferem da industria
2. **Apenas 4 projetos** — generalizacao limitada
3. **Sem controle de variaveis confundidoras** (mudancas de equipe, tooling)
4. **Projetos menores mostram mais variabilidade**

---

## Dados da Pesquisa

### Descricao do Dataset
- **Projetos analisados**: 4 projetos Open Source (OSS)
  - Blender (2014-2022, 8 anos)
  - FreeBSD (2014-2022, 8 anos)
  - LLVM (2014-2022, 8 anos)
  - Mozilla (2017-2022, 5-6 anos)
- **Tamanho total do dataset**: 283,235 code reviews (historico completo)
- **Fonte de dados**: Phabricator (Blender, FreeBSD, LLVM), Gerrit (Mozilla)
- **Metodo de coleta**: Repository mining de sistemas de code review
- **Periodo coberto**: 2014-2022 (maioria), 2017-2022 (Mozilla)

### Variaveis de Saida Coletadas (Code Churn Metrics)

| Variavel | Definicao | Como Medido | Dados Coletados |
|---|---|---|---|
| **SLOC change** | Mudanca anual em linhas de codigo | `git show` ou ferramentas de analise | 3-17% crescimento/ano por projeto |
| **Commit count** | Numero de commits por ano | Git log analysis | Variavel por projeto |
| **Distinct authors** | Numero de autores unicos contribuindo por ano | Parsing de commit authors | Variavel (ex: Blender: 8.589, 89 anos; LLVM: 29.555, 592 autores) |
| **Distinct committers** | Committers unicos por ano | Parsing de signed commits | Variavel por projeto |

### Metricas Primarias de Code Velocity (Code Review Periods)

| Metrica | Definicao | Significado | Dados para Blender |
|---|---|---|---|
| **Time-to-first-response (TTFR)** | Tempo entre publicacao de mudanca e primeira revisao | Rapidez da comunidade em dar feedback | Variavel por projeto |
| **Time-to-accept (TTA)** | Tempo entre publicacao e aceitacao | Velocidade de decisao | Variavel por projeto |
| **Time-to-merge (TTM)** | Tempo completo ate merge no main branch | Velocidade total de integracao | 30-day moving median (ver Figura 1) |

### Medidas Descritivas (Tabela II - Exemplo Blender 2014-2022)

| Periodo | Projeto | SLOC/ano | Commit count (annual) | Distinct author % | Distinct committer % |
|---|---|---|---|---|---|
| 2014-2022 | Blender | +6.2% | Variavel | +10.3% | -2.2% |
| 2014-2022 | FreeBSD | +3.5% | Variavel | +0.5% | -0.3% |
| 2014-2022 | LLVM | +17.4% | Variavel | +17.6% | +0.8% |
| 2017-2022 | Mozilla | +11.1% | Variavel | — | — |

---

## Metricas e Instrumentos de Avaliacao

### Metricas de Code Velocity (Definidas)

#### 1. Time-to-First-Response (TTFR)
```
TTFR = timestamp(first_review) - timestamp(code_submission)
```
- **Unidade**: Horas ou dias
- **Interpretacao**: Rapidez com que a comunidade reage a novas mudancas
- **Tendencia esperada**: Pode diminuir se equipe maior, ou aumentar se mais mudancas

#### 2. Time-to-Accept (TTA)
```
TTA = timestamp(acceptance_decision) - timestamp(code_submission)
```
- **Unidade**: Horas ou dias
- **Interpretacao**: Tempo necessario para consenso/aprovacao
- **Tendencia esperada**: Pode variar com complexidade do projeto

#### 3. Time-to-Merge (TTM)
```
TTM = timestamp(merge_to_main) - timestamp(code_submission)
```
- **Unidade**: Horas ou dias
- **Interpretacao**: Velocidade completa de integracao (reflex de **code velocity**)
- **Metrica chave**: Principal para responder a Research Question

### Analise Estatistica de Tendencias

#### Teste Mann-Kendall (MK) — Tabela 1
```
Hipotese nula (H0): Nao ha tendencia monotonica
Hipotese alternativa (H1): Existe tendencia (ascendente ou descendente)
```

**Procedimento**:
1. Calcular para cada metrica (TTFR, TTA, TTM) e projeto
2. Computar p-value do teste MK
3. Usar α = 0.05 para significancia
4. Se p < 0.05, rejeitar H0 (existe tendencia)

#### Resultados (Tabela 1 - Exemplo TTFR)
| Projeto | Teste MK | p-value | Interpretacao |
|---|---|---|---|
| Blender | 0.241 | — | Nao significativo |
| FreeBSD | < .001 | -0.003 | Tendencia DESCENDENTE (melhora) |
| LLVM | < .001 | -0.001 | Tendencia DESCENDENTE |
| Mozilla | < .001 | -0.003 | Tendencia DESCENDENTE |

**Conclusao**: Maioria dos projetos nao mostra tendencia direcional clara em TTFR.

#### Estimador de Inclinacao (Sen's Slope - Theil-Sen)
```
Sen's slope = mediana(x_j - x_i) / (t_j - t_i)  para todos i < j
```
- **Interpretacao**: magnitude de mudanca por unidade de tempo (30 dias no estudo)
- **Exemplo**: -0.003 significa -0.003 dias = -4.3 minutos de melhora a cada 30 dias

### Medicao de Code Review Periods

#### 30-Day Rolling Median
```
Mediana_30d = mediana(TTM values em janela de 30 dias)
```
- **Razao**: Mais robusto que media (menos afetado por outliers)
- **Visualizacao**: Figura 1 mostra 30-day moving median para 4 projetos
- **Achado principal**: Mediana permanece em faixa fixa para time-to-merge

#### All-Time Median
```
Mediana_all = mediana(todos os TTM values ao longo dos anos)
```
- **Interpretacao**: Baseline central da distribuicao
- **Comparacao**: Contrasta com media (mais sensivel a outliers)

### Testes de Significancia Estatistica

#### Mann-Kendall + Sen's Slope Estimator
- **Robustez**: Nao assume distribuicao normal (importante para dados de code review)
- **Autocorrelacao**: Mitigada com modificacao (MK test ajustado)
- **Resultado**: Ambos p-value (significancia) e magnitude (Sen's slope) reportados

### Validacao de Dados

#### Tratamento de Outliers
- Codigo reviews com Modern Code Review (MCR) foram removidos se:
  - Nao continham mudancas reais
  - Foram commited sem aceitacao formal
- Filtros aplicados: 283,235 → 280,456 reviews validos

#### Autocorrelacao em Time Series
- **Desafio**: Time series de code review pode ter autocorrelacao
- **Solucao**: Usar Mann-Kendall test que ajusta para autocorrelacao
- **Verificacao**: Calcular 90-day moving median em paralelo

### Achados Principais (Tabela 1 - Resumo)

| Resultado | Interpretacao | Implicacao |
|---|---|---|
| Nenhuma tendencia significativa em TTFR/TTA para maioria | Code velocity NAO declina com idade | Projetos nao "desceleram" |
| SLOC crescimento 3-17%/ano, mas TTM estavel | Tamanho crescente nao afeta velocity | Lei de Lehman pode nao se aplicar |
| Variacao ano-a-ano em Blender | Tamanho pequeno = mais variacao | Core team importante para estabilidade |
| Auto-correcao visivel: core teams matem velocity | Comportamento auto-regulatorio | Humans/processes adaptam-se |

---

## Contribuicao Principal

Evidencia empirica robusta de que code velocity se mantem estavel ao longo do tempo em projetos OSS, contrariando a crenca de que projetos desaceleram conforme crescem.

---

*Extraido em Marco 2026 para MLR: Software Developer Metrics in Practice*

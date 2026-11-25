# P0028 — Fair Developer Score: Build-Adjusted Measurement of Effort and Impact

**Decisao: INCLUIDO | Qualidade: 4/5**

---

## Dados Bibliograficos

| Campo | Valor |
|-------|-------|
| **ID** | P0028 |
| **Autores** | Xinzhou Wang, Jiancong Zhu, Jinghan Feng, Zixuan Zhang, Joshua Rauvola, Devon Delgado, Ahmad Antar, Abid Ali |
| **Ano** | 2025 |
| **Venue** | ASEW 2025 (40th IEEE/ACM Int. Conf. Automated Software Engineering Workshops) |
| **Tipo** | Workshop paper |
| **Metodo** | Repository mining + multi-dimensional scoring + cross-repository validation |
| **Amostra** | 5 OSS repos: Linux Kernel (339 contribs), Kubernetes (199), TensorFlow (146), Apache Kafka (225), PostgreSQL (31) |
| **Contexto** | Large open-source projects; cross-language (C, Go, Python/C++, Java/Scala, C) |

---

## Objetivo

Propor o Fair Developer Score (FDS), uma metrica composta que mede produtividade de desenvolvedores de forma justa, combinando esforco individual e importancia organizacional dos builds, usando apenas dados de commits Git.

---

## Questoes de Pesquisa

- **RQ1**: Como pode a produtividade de desenvolvedores ser medida de forma justa combinando esforco individual e importancia organizacional dos builds usando apenas dados de commits?
- **RQ2**: Como o Fair Developer Score (FDS) se compara a metricas tradicionais baseadas em volume (contagem de commits)?

---

## Dados da Pesquisa

### Amostra de Repositorios
- **Total de repos analisados**: 5 repositorios OSS (plus cross-validation em 4 adicionais)
- **Repositorios principais**:
  1. **Linux Kernel** (C): 339 contribuidores, 974-day window
  2. **Kubernetes** (Go): 199 contribuidores
  3. **TensorFlow** (Python/C++): 146 contribuidores
  4. **Apache Kafka** (Java/Scala): 225 contribuidores
  5. **PostgreSQL** (C): 31 contribuidores

- **Repositorios para validacao cruzada**:
  - Kubernetes (Go): 199 contrib, 1.321 dias
  - TensorFlow (Python/C++): 146 contrib, 746 dias
  - Apache Kafka (Java/Scala): 225 contrib, 562 dias
  - PostgreSQL (C): 31 contrib, 957 dias

### Fonte de Dados
- **Sistema de versionamento**: Git (commits, metadata, diffs)
- **Tipo de dados**: Commit history (author, timestamp, files changed, lines added/deleted, commit message)
- **Periodo de analise**:
  - Linux Kernel: 974 dias (window fixo)
  - Outros: Variavel (562-1321 dias)
- **Granularidade**: Commit-level analysis (individual developers, individual work units)

### Metodos de Coleta
- **Extracao de dados**: Git repository mining (clone, git log, git diff processing)
- **Processamento**: Python scripts para parser de commits e metadata
- **Dados coletados**:
  - Commit hash, author name/email, timestamp (UTC)
  - Files changed, lines added/deleted (code churn)
  - Commit message (for semantic analysis)
  - Parent/child relationships (commit graph)

### Periodo de Analise
- **Linux Kernel (baseline)**: 974-day window (captura de ciclo completo)
- **Cross-repo validation**: 562-1.321 dias (diferentes project lifecycles)
- **Justificativa**: Diferentes projetos têm diferentes maturity e commit velocity

---

## Metricas e Instrumentos de Avaliacao

### Fair Developer Score (FDS) - Pipeline de 3 Etapas

**Etapa 1: Commit Clustering (Torque Clustering Algorithm)**
- **Objetivo**: Agrupar commits em "builds" (unidades logicas de trabalho)
- **Algoritmo**: Torque Clustering (heuristic-based)
- **Formula**: Torque(i,j) = α·Δt_ij + β·Δc_ij + (1-α-β)·Jaccard(S_i, S_j)
  - Δt_ij: Time difference (segundos) entre commits i e j
  - Δc_ij: Code change magnitude (linhas normalizadas)
  - Jaccard(S_i, S_j): Similaridade de escopo (diretorio/arquivo overlap)
  - α, β: Parametros de balanceamento (pesos)
- **Threshold**: gap parameter para disparar novo build (quando Torque > gap)
- **Output**: Grupos de commits semanticamente coesos

**Etapa 2: Developer Effort Evaluation**
- **Unidade de analise**: Contribuicao por desenvolvedor em cada build
- **Formula**: Effort_{u,b} = Share_{u,b} × Σ(w_k × Z_k(b))
  - Share_{u,b}: Proporcao de code churn efetivo do dev (linhas add/delete)
  - w_k: Peso da dimensao k (calibrado a priori)
  - Z_k(b): Valor normalizado da dimensao k para build b

**6 Dimensoes de Esforco** (cada uma calculada per build):
| Dimensao | Descricao | Formula/Metodo | Peso |
|----------|-----------|---|---|
| **Scale** | Magnitude absoluta do churn | log(total_lines_changed) | w1 (alta) |
| **Reach** | Dispersao geografica (quantos diretorios) | Entropia = -Σ p_i log(p_i) | w2 |
| **Centrality** | Influencia no projeto (co-change graph) | PageRank em dependency graph | w3 |
| **Dominance** | Quem iniciou e finalizou o build | Binario (1 se dev em primeiro+ultimo commit) | w4 |
| **Novelty** | Introducao de novos modulos/APIs | Count novos arquivos/APIs | w5 |
| **Speed** | Intervalos curtos entre commits | exp(-intervalo_segundos) | w6 |

- **Normalizacao**: Robust MAD-Z (Median Absolute Deviation Z-score)
  - Resistente a outliers e distribuicoes skewed
  - Formula: Z_robust = (X - median) / MAD

**Etapa 3: Build Importance Assessment**
- **Objetivo**: Quantificar importancia do build para o projeto
- **Formula**: Importance_b = Σ(v_m × Z_m(b))
  - v_m: Peso semantico da dimensao m
  - Z_m(b): Valor normalizado da dimensao m para build

**6 Dimensoes de Importancia** (pesos pre-calibrados):
| Dimensao | Descricao | Peso | Impacto |
|----------|-----------|------|---------|
| **Scale** | Tamanho total do build (total code churn) | 0.30 (30%) | Principal fator |
| **Scope** | Dispersao (quantos diretorios/arquivos) | 0.20 (20%) | Breadth vs depth |
| **Centrality** | Importancia estrutural (PageRank) | 0.15 (15%) | Edificios centrais vs perifericos |
| **Complexity** | Complexidade logica (comment ratio, modulos) | 0.15 (15%) | Arquitetura vs "plumbing" |
| **Type** | Tipo de tarefa (feature, bugfix, refactor) | 0.10 (10%) | Prioridade semantica (via commit message) |
| **Release** | Proximidade a marcos de release | 0.10 (10%) | Time-sensitivity (versionamento) |

- **Final FDS**: FDS_u = Σ(Effort_{u,b} × Importance_b) para todos os builds

### Validacao das Metricas

**Teste Matched Top-Decile (Linux Kernel baseline)**:
- FDS-ranked top 10 devs vs. Commit-count ranked top 10 devs
- **Average Importance**: FDS-ranked = +0.314 higher (Wilcoxon p=0.0038**)
  - FDS coloca desenvolvedores em builds mais importantes
- **Average Effort**: FDS-ranked = +0.079 higher (Wilcoxon p=0.0015**)
  - FDS identifica desenvolvedores com esforco mais consistente
- **Rework rate**: FDS-ranked devs com menor rework (p=0.069, borderline)
  - Qualidade de commits melhor, não apenas quantidade
- **Quality proxies**: FDS-ranked devs menores rollbacks, menor refactoring
  - Validacao indireta que FDS penaliza contribuicoes problematicas

**Cross-Repository Validation (5 repos)**:
| Repositorio | Linguagem | N Contributors | FDS Range | Mediana FDS | Distribuicao |
|-------------|-----------|---|---|---|---|
| **Linux Kernel** | C | 339 | 0.0105 – 210.17 | 0.35 | Right-skewed |
| **Kubernetes** | Go | 199 | 0.013 – 333.9 | ~0.35 | Right-skewed |
| **TensorFlow** | Python/C++ | 146 | 0.012 – 453.2 | ~0.35 | Right-skewed |
| **Apache Kafka** | Java/Scala | 225 | 0.014 – 128.7 | ~0.35 | Right-skewed |
| **PostgreSQL** | C | 31 | 0.057 – 159.1 | ~0.35 | Right-skewed |

**Consistencia**: Todos 5 repos exibem distribuicao right-skewed (median ~0.35), suportando que FDS efetivamente diferencia core contributors de periphery.

**Statistical Testing**:
- **Wilcoxon signed-rank tests**: Para comparacoes paired (FDS vs commit count)
- **Cliff's Δ**: Non-parametric effect sizes
- **Bootstrap confidence intervals**: Para estimativas de credibilidade

### O Framework PPM (Programmer Productivity Measurement)

### Pipeline em 3 Etapas

**Etapa 1: Commit Clustering (Torque Clustering)**
- Agrupa commits em "builds" (unidades logicas de trabalho)
- Considera: proximidade temporal, similaridade de escopo (Jaccard distance), consistencia de autor
- Torque(i,j) = α·Δt_ij + β·Δc_ij + (1 - α-β)·Jaccard(S_i, S_j)

**Etapa 2: Developer Effort Evaluation**
- Effort_{u,b} = Share_{u,b} × Σ(w_k × Z_k)
- **Share**: proporcao de code churn efetivo do dev no build (linhas adicionadas/deletadas pelo dev)

#### 6 Dimensoes de Esforco (Effort Dimensions)

| Dimensao | Descricao | Formula | Peso |
|----------|-----------|---------|------|
| **Scale** | Magnitude absoluta do churn no build | log(total churn) | Importancia alta |
| **Reach** | Dispersao geografica (quantos diretorios?) | Entropia = -Σ p_i log(p_i) | Captura complexidade |
| **Centrality** | Influencia no projeto (co-change graph) | PageRank em grafo de mudancas | Avalia impacto arquitetural |
| **Dominance** | Quem iniciou e finalizou o build | Binario: dev no primeiro+ultimo commit | Marca ownership |
| **Novelty** | Introducao de novos modulos/APIs | Count de novos arquivos/APIs | Recompensa inovacao |
| **Speed** | Recompensa intervalos curtos entre commits | exp(-intervalo_segundos) | Captura momentum |

**Etapa 3: Build Importance Assessment**
- Importance_b = Σ(v_m × Z_m)

#### 6 Dimensoes de Importancia (Importance Dimensions)

| Dimensao | Descricao | Peso | Impacto |
|----------|-----------|------|---------|
| **Scale** (0.30) | Tamanho total do build (total churn) | 30% | Principal fator; reflete magnitude |
| **Scope** (0.20) | Dispersao (quantos diretorios/arquivos?) | 20% | Breadth vs. depth |
| **Centrality** (0.15) | Importancia estrutural no projeto (PageRank) | 15% | Edificios centrais vs. perifericos |
| **Complexity** (0.15) | Complexidade logica (comment ratio, modulos) | 15% | Arquitetura vs. "plumbing" |
| **Type** (0.10) | Tipo de tarefa (feature, bugfix, refactor) | 10% | Prioridade semantica |
| **Release** (0.10) | Proximidade a marcos de release | 10% | Time-sensitivity (versionamento) |

- **Normalizacao**: Robust MAD-Z (Median Absolute Deviation Z-score) — resistente a outliers e distribuicoes skewed

### Fair Developer Score (FDS)
FDS_u = Σ(Effort_{u,b} × Importance_b) para todos os builds b

---

## Resultados de Validacao

### Analise Linux Kernel (Baseline Detalhada)

| Validacao | Resultado | Interpretacao |
|-----------|----------|---|
| FDS vs commit count ranking | Rankings frequentemente divergem | FDS captura dimensoes qualitativas nao presentes em volume |
| FDS vs Average Effort | Correlacao moderada (r=0.316) | Effort e apenas 1 dimensao; FDS integra importancia tambem |
| FDS vs Average Importance | Correlacao moderada (r=0.231) | Importancia sozinha nao determina FDS |
| **Matched Top-Decile (Linux)** | **FDS-ranked devs 1-10** vs **commit-count devs 1-10** | |
| — Average Importance | +0.314 (p=0.0038, Wilcoxon) | **FDS rang devs em builds mais importantes** |
| — Average Effort | +0.079 (p=0.0015, Wilcoxon) | **FDS rang devs com esforco mais consistente** |
| Rework rate | FDS-ranked devs: menor rework (p=0.069, borderline) | Qualidade de commits melhor, nao apenas quantidade |
| **Quality proxies (Tabelas IV-V)** | Menores rollbacks, menor refactoring | FDS efetivamente penaliza contribuicoes problematicas |

### Validacao Cross-Repository (5 repositorios OSS)

| Repositorio | Linguagem | N Contributors | FDS Range | Key Finding |
|-----------|-----------|---|---|---|
| **Linux Kernel** | C | 339 | 0.0105 – 210.17 | Baseline; core validation |
| **Kubernetes** | Go | 199 | 0.013 – 333.9 | Consistent Effort advantages |
| **TensorFlow** | Python/C++ | 146 | 0.012 – 453.2 | Architectural complexity well-captured |
| **Apache Kafka** | Java/Scala | 225 | 0.014 – 128.7 | FDS stable across scale |
| **PostgreSQL** | C | 31 | 0.057 – 159.1 | Small-team dynamics consistent |

**Consistencia**: Todos 5 repos exibem distribuicao right-skewed em FDS (median ~0.35), suportando notion que FDS efetivamente diferencia core contributors de periphery.

---

## Desafios do Uso das Metricas

1. **Metricas tradicionais (LOC, commits) conflate** edits triviais com mudancas arquiteturais
2. **Fairness**: organizacoes podem inadvertidamente descontar contribuicoes foundational
3. **Pesos pre-definidos** nos coeficientes de Effort e Importance (nao calibrados por projeto)
4. **Apenas dados de commit** — nao captura code review, mentoring, documentacao
5. **OSS apenas** — validacao em contexto proprietario pendente

---

## Avaliacao de Qualidade

| Criterio | Pontuacao (0-2) |
|----------|----------------|
| Objetivo claramente definido | 2 |
| Metodologia adequada | 2 |
| Amostra/contexto descrito | 2 |
| Ameacas a validade discutidas | 1 |
| Resultados com evidencia | 2 |
| Contribuicao clara | 2 |
| **TOTAL** | **11/12 (Alta)** |

---

## Limitacoes

1. **Pesos arbitrarios** nos coeficientes de Effort e Importance
2. **Apenas projetos OSS** — sem validacao proprietaria
3. **Nao captura atividades nao-commit** (reviews, mentoring, design)
4. **Torque Clustering sensivel a parametros** (α, β, gap)
5. **Workshop paper** — publicacao preliminar

---

## Contribuicao Principal

Metrica composta (FDS) que combina esforco individual e importancia dos builds para medir produtividade de desenvolvedores de forma justa usando apenas dados de Git. Validado em 5 repositorios OSS. Implementacao open-source disponivel.

---

*Extraido em Marco 2026 para MLR: Software Developer Metrics in Practice*

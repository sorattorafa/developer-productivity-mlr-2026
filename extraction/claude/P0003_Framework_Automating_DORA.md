# P0003 — A Framework for Automating the Measurement of DORA Metrics

**Decisao: INCLUIDO | Qualidade: 4/5**

---

## Dados Bibliograficos

| Campo | Valor |
|-------|-------|
| **ID** | P0003 |
| **Autores** | Brennan Wilkes, Alessandra Maciel Paz Milani, Margaret-Anne Storey |
| **Ano** | 2023 |
| **Venue** | IEEE ICSME 2023 (International Conference on Software Maintenance and Evolution) |
| **DOI** | 10.1109/ICSME58846.2023.00018 |
| **Tipo** | Conference paper |
| **Metodo** | Repository mining |
| **Amostra** | 304 repositorios open source populares (GitHub) |
| **Contexto** | OSS — C, C++, Java, JavaScript, TypeScript, Python, Go, Rust, PHP, Swift |
| **Modo de trabalho** | Nao informado (open source, distribuido) |
| **Metodologia** | DevOps |

---

## Objetivo

Propor um framework project-agnostic para operacionalizar e automatizar a medicao das DORA metrics, independentemente do ciclo de vida do projeto ou tipo de deployment, e demonstrar sua aplicabilidade em 304 repositorios OSS.

---

## Questoes de Pesquisa

- **RQ1**: Como podem as DORA metrics ser operacionalizadas e automatizadas de forma independente do ciclo de vida do projeto ou tipo de deployment?
- **RQ2**: Como as DORA metrics medidas automaticamente se comparem aos benchmarks do State of DevOps Report baseados em surveys?
- **RQ3**: Quais tendências emergem nas DORA metrics ao longo do tempo (2013-2022)?

---

## Dados da Pesquisa

### Amostra e Contexto
- **Tamanho da amostra**: 304 repositorios open source populares
- **Seleção**: Top 1.000 repositorios starred no GitHub (filtrados para >=100 "recognizable deployments" e >=50 git tags com semantic versioning)
- **Linguagens**: C, C++, Java, JavaScript, TypeScript, Python, Go, Rust, PHP, Swift
- **Periodo de coleta**: 2013-2022 (série temporal de 10 anos)

### Fonte de Dados
- **Sistema de versionamento**: Git (commits e tags semver)
- **Plataforma**: GitHub (API para issues, PR metadata, deployment markers)
- **Metricas obtidas de**:
  - git log: commits, autores, timestamps, mensagens de commit
  - git tags: semantic versioning para identificar deployments
  - GitHub Issues API: bug reports com labels "bug", states, resoluçoes
  - Commit graphs: análise de containment e bug-inducing commits via SZZ algorithm

### Metodos de Coleta
- **Deployment Frequency**: Contagem de git tags com semantic versioning (v0.0.0 pattern) em ordem "razoável"
- **Lead Time for Changes**: Diferença temporal entre primeiro commit no build e seu deployment (tag)
- **Mean Time to Recover**: Tempo entre failure detection (GitHub issue com label "bug") e fix deployment
- **Change Failure Rate**: Proporção de deployments que contêm bug-inducing commits (via SZZ algorithm)

### Instrumentos e Algoritmos
- **SZZ Algorithm**: Para identificar commits bug-inducing; usa git diff para rastrear backwards de bug-fix para introdução original
- **Algorithms implementados**:
  - Algorithm 1: Deployment Frequency = |D| / (tn - t0)
  - Algorithm 2: Lead Time for Changes = (1/|T|) * SUM(t_deploy - t_commit)
  - Algorithm 3: Mean Time to Recover = (1/|T|) * SUM(t_deploy - t_failure)
  - Algorithm 4: Change Failure Rate = |D_faulty| / |D|
- **Framework replication package**: Disponivel em Zenodo (implementação em Python para automatizacao)

### Periodo e Janelas Temporais
- **Serie temporal**: 2013-2022 (análise por ano)
- **Janelas móveis**: Análise mensal para calcular tendências
- **Limitações temporais**: Projetos precisam ter >=50 tags semver para inclusão; janela mínima 974 dias (Linux Kernel baseline)

---

## Metricas e Instrumentos de Avaliacao

### Metricas Principais (DORA)

#### Deployment Frequency (DF)
- **Definicao**: Numero de deployments por unidade temporal (deployments/ano)
- **Formula**: DF = |D| / (tn - t0)
- **Metodo de calculo**: Contagem de git tags com semantic versioning em intervalos anuais
- **Unidade**: Deployments por ano
- **Valores observados (2021 mediana)**: 24.5 deployments/ano (Range: 6.6 até 116.2)
- **Validacao**: Comparada com State of DevOps Report benchmarks (Elite/High/Medium/Low clusters)

#### Lead Time for Changes (LTFC)
- **Definicao**: Tempo decorrido entre commit inicial e deployment em producao
- **Formula**: LTFC = (1/|T|) * SUM(t_deploy - t_commit)
- **Metodo de calculo**: Diferença temporal entre primeiro commit no build e deployment (tag)
- **Unidade**: Dias
- **Valores observados (2021 mediana)**: 24.9 dias (Range: 5.1 até 140.6 dias)
- **Interpretacao**: Captura eficiencia do pipeline de entrega e time-to-market

#### Mean Time to Recover (MTTR)
- **Definicao**: Tempo medio para restaurar servico após falha reportada
- **Formula**: MTTR = (1/|T|) * SUM(t_deploy - t_failure)
- **Metodo de calculo**: Diferença entre deteccao de failure (GitHub issue com label "bug") e deployment de fix
- **Unidade**: Dias
- **Valores observados (2021 mediana)**: 95.2 dias (Range: 26.5 até 370.0 dias)
- **Nota**: Cresce de 1.99 dias (2021) para números altos, indicando possível degradacao em projetos
- **Validacao**: Dados de GitHub issues com lifecycle timestamps

#### Change Failure Rate (CFR)
- **Definicao**: Percentual de deployments que introduzem failures em producao
- **Formula**: CFR = |D_faulty| / |D|
- **Metodo de calculo**: Proporção de deployments contendo commits bug-inducing (identificados via SZZ)
- **Unidade**: Percentual (%)
- **Valores observados (2021 mediana)**: 60.4% (Range: 19.8% até 90.6%)
- **Nota**: Metrica mais desafiadora; requer interpretacao humana para definir "failure"
- **SZZ Algorithm**:
  - Identifica commits que causam bugs (bug-inducing)
  - Usa git diff para rastrear backwards de bug-fix
  - Padrão: Busca commits que modificaram linhas alteradas por fix commits
  - Melhorias aplicadas: Whitespace filtering, code comment exclusion, weighting scheme

### Validacao das Metricas

**Comparacao com State of DevOps Report 2021**:
- DF: 75.6% dos projetos OSS = High performers (vs survey benchmarks)
- LTFC: 78.2% = Medium performers
- MTTR: 76.8% = Medium performers
- CFR: 76.3% = **PIOR que o cluster mais baixo** (anomalia detectada; culturas OSS diferentes)

**Dependencias entre metricas** (descobertas):
- DF influencia diretamente LTFC, MTTR e CFR (relacao unidirecional)
- Alto DF correlaciona com low LTFC (projetos ativos = entregas rapidas)
- Correlacao entre MTTR e CFR (ambas metricas de estabilidade)
- DORA metrics correlacionam com business outcomes (ref: Accelerate book)

**Ameacas a Validade**:
- SZZ algorithm apresenta vies: identificacao imprecisa de bug-inducing commits
- Definicao inclusiva de "failure" (qualquer issue com label "bug") pode inflar CFR
- Cultura OSS diferente de SaaS: "acceptance around bugs" em versioned software
- Benchmarks survey-based nao diretamente comparaveis com telemetria automatizada
- Amostra limitada a projetos GitHub populares (>=50 tags)

---

## Frameworks e Metricas

### C1 - Frameworks Referenciados/Propostos

- **DORA** (foco central): Deployment Frequency, Lead Time for Changes, Mean Time to Recover, Change Failure Rate
- **Framework proprio proposto**: Sim — operacionalizacao automatizada das 4 metricas DORA via git + GitHub
- Referencia State of DevOps Report e clusters de performance (Elite, High, Medium, Low)
- Referencia Accelerate (Forsgren, Kim, Humble)

### C2 - Metricas Especificas

| Metrica | Categoria | Nivel | Como Coletada | Validada |
|---------|-----------|-------|---------------|----------|
| Deployment Frequency | Velocidade de entrega | Equipe/Projeto | Git tags (semver) | Sim |
| Lead Time for Changes | Velocidade de entrega | Equipe/Projeto | Git commits → tags | Sim |
| Mean Time to Recover | Qualidade/Estabilidade | Equipe/Projeto | GitHub issues (bug labels) → fix commits → deploy | Sim |
| Change Failure Rate | Qualidade/Estabilidade | Equipe/Projeto | SZZ algorithm (bug-inducing commits) | Parcial |
| Commit frequency | Atividade | Individual/Projeto | Git log | Sim |
| Stars (GitHub) | Impacto/comunidade | Projeto | GitHub API | N/A |
| Issues opened | Atividade/comunidade | Projeto | GitHub API | N/A |

### Algoritmos Formalizados

```
Deployment Frequency:    DF = |D| / (tn - t0)
Lead Time for Changes:   LTFC = (1/|T|) * SUM(t_deploy - t_commit)
Mean Time to Recover:    MTTR = (1/|T|) * SUM(t_deploy - t_failure)
Change Failure Rate:     CFR = |D_faulty| / |D|
```

**Definicoes-chave:**
- **Deployment** = git tag com semantic versioning em ordem razoavel
- **Failure** = GitHub issue com label "bug", estado "completed", fixada por um commit
- **Containment** = commit alcancavel no grafo git pelo deployment, mas nao por deployments anteriores
- **Induced** = commit que causa um bug (via SZZ algorithm)

### C3 - Classificacao

- **Objetivas**: Todas as 4 metricas DORA (coletadas automaticamente via git/GitHub)
- **Output**: DF (deployments produzidos), commit frequency
- **Outcome**: CFR (bugs em producao), MTTR (tempo de recuperacao)
- **Processo**: LTFC (eficiencia do pipeline de entrega)

---

## Fatores que Influenciam Produtividade

### D1 - Fatores Positivos
| Fator | Categoria |
|-------|-----------|
| Automacao GitHub (PR templates, bots, CI) | Tecnico/Ferramental |
| Alta deployment frequency possibilita melhores LTFC, MTTR e CFR | Tecnico |
| Financiamento do projeto | Organizacional |
| Boas praticas DevOps (CI/CD, tags semver) | Tecnico/Ferramental |

### D2 - Fatores Negativos
| Fator | Categoria |
|-------|-----------|
| Perda de contribuidor-chave causa declinio drastico nas metricas | Humano/Psicologico |
| Projetos mantidos por unico desenvolvedor (metricas distorcidas) | Organizacional |
| Baixa deployment frequency como gargalo (afeta todas as metricas) | Tecnico |
| Falta de documentacao de bug fixes impede calculo de stability | Tecnico |

### D3 - Relacoes Identificadas
- **Sim, correlacao**: DF influencia diretamente LTFC, MTTR e CFR (dependencia unidirecional)
- DF + LTFC juntas necessarias para capturar throughput (nenhuma isoladamente suficiente)
- MTTR influenciada por ambas stability metrics
- DORA metrics correlacionam com outcomes de negocio (citando Accelerate)

---

## Papel da IA e Automacao

| Campo | Valor |
|-------|-------|
| Usa IA/ML? | Nao (usa SZZ algorithm, rule-based) |
| Automacao de coleta? | Sim — framework totalmente automatizado via git mining + GitHub API |
| Compara automatizado vs manual? | Sim — compara telemetria vs survey (State of DevOps Report) |
| Resultado da comparacao | Telemetria remove vies subjetivo mas produz metricas diferentes dos benchmarks survey-based |

---

## Resultados Principais

### Metricas Medianas 2021 (304 projetos)

| Metrica | Mediana | Top 25% | Bottom 25% |
|---------|---------|---------|------------|
| Deployment Frequency | 24.5/ano | 116.2/ano | 6.6/ano |
| Lead Time for Changes | 24.9 dias | 5.1 dias | 140.6 dias |
| Mean Time to Recover | 95.2 dias | 26.5 dias | 370.0 dias |
| Change Failure Rate | 60.4% | 19.8% | 90.6% |

### Comparacao com State of DevOps 2021

- **DF**: 75.6% dos projetos = High performers
- **LTFC**: 78.2% = Medium performers
- **MTTR**: 76.8% = Medium performers
- **CFR**: 76.3% = **pior que o cluster mais baixo** do DevOps Report

### Tendencias 2013-2022
- DF: aumento consistente
- MTTR: **dobrou** entre 2016 e 2022

---

## Desafios do Uso das Metricas

1. **51% dos praticantes nao tem forma eficaz de medir DORA** (Atlassian survey, 500 profissionais)
2. **54% acham dificil medir progresso DevOps**
3. **Solucoes existentes exigem infraestrutura especifica** (Azure DevOps, GitLab Incidents, cloud) — exclui OSS
4. **Stability metrics mais dificeis de automatizar** que throughput; requerem "interpretacao humana"
5. **Definicao de Change Failure Rate e pouco clara** mesmo no DORA original
6. **SZZ algorithm apresenta vies** e produz resultados imprecisos no mapeamento bug-inducing
7. **Benchmarks survey-based nao comparaveis** diretamente com telemetria
8. **Cultura OSS diferente de SaaS**: "culture of acceptance around bugs" em projetos versionados
9. **DORA metrics sozinhas nao capturam saude do projeto**: webpack = DORA medio mas projeto muito bem-sucedido

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
| **TOTAL** | **11/12 (Alta)** |

---

## Limitacoes

1. **Stability metrics menos confiaveis** que throughput metrics
2. **So mede bugs fixados**: ignora bugs nao reportados ou nao corrigidos
3. **Vies do SZZ algorithm**: na identificacao de commits bug-inducing
4. **Comparacao com State of DevOps** (survey vs telemetria) nao totalmente precisa
5. **Amostra limitada a projetos populares** GitHub (>=50 tags, >=100 failures)
6. **Definicao inclusiva de "failure"** pode inflar CFR
7. **Benchmarks OSS podem diferir significativamente** da industria

---

## Contribuicao Principal

Framework project-agnostic com replication package (Zenodo) para medir automaticamente as 4 DORA metrics via git + GitHub, sem dependencia de infraestrutura cloud. Permite analise retroativa em series temporais, benchmarking padronizado, e comparacao entre projetos. Demonstrado em 304 repos OSS com insights sobre tendencias e dependencias entre metricas.

## Trabalhos Futuros Relevantes para a Tese

- Correlacao DORA metrics vs financiamento, tamanho de equipe, stars, mencoes
- Analise retroativa de eventos significativos (mudanca de lideranca, funding, reestruturacao)
- Investigar se alto DORA performance correlaciona com sobrevivencia do projeto ou satisfacao do desenvolvedor
- Comparacao de tendencias DORA por linguagem (ex: Rust vs C++)
- Modelos preditivos de como decisoes afetam metricas DORA

---

*Extraido em Marco 2026 para MLR: Software Developer Metrics in Practice*

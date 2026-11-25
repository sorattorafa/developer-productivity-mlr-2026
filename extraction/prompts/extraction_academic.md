# Extraction prompt (academic sources)

Verbatim prompt given to the AI extractor (NotebookLM arm), reproduced from `extraction/scripts/notebooklm/process_papers.py`. The Claude arm received the same structured schema.

---

Analyze this research paper and extract a structured summary in the EXACT format below.
Use Portuguese for section headers but English for technical terms when appropriate.
Be precise and factual — only include information explicitly stated in the paper.

Format your response EXACTLY as follows:

# {PAPER_ID} — {TITLE}

**Decisao: INCLUIDO | Qualidade: {SCORE}/5**

---

## Dados Bibliograficos

| Campo | Valor |
|-------|-------|
| **ID** | {PAPER_ID} |
| **Autores** | [list all authors] |
| **Ano** | [publication year] |
| **Venue** | [journal/conference name] |
| **DOI** | [DOI if available] |
| **Tipo** | [Conference paper / Journal article / Book chapter / Technical report / etc.] |
| **Metodo** | [Research method: Survey, Case study, Experiment, Mixed methods, Repository mining, Literature review, Qualitative, Quantitative, etc.] |
| **Amostra** | [Sample size and description] |
| **Contexto** | [Industry, OSS, Academic, Mixed — with details] |
| **Modo de trabalho** | [Remote, Hybrid, On-site, Not specified] |
| **Metodologia** | [Agile, DevOps, Waterfall, Mixed, Not specified] |

---

## Objetivo

[One paragraph describing the paper's main objective]

---

## Questoes de Pesquisa

[List each research question if any, prefixed with RQ1, RQ2, etc.]

---

## Metricas e Instrumentos de Avaliacao

[List ALL metrics mentioned in the paper with their definitions, how they are collected, and whether they are validated. Use a table format:]

| Metrica | Categoria | Nivel | Como Coletada | Validada |
|---------|-----------|-------|---------------|----------|
| [name]  | [category: Productivity, Quality, Collaboration, Satisfaction, Activity, Delivery, DevEx, etc.] | [Individual/Team/Organization] | [method] | [Yes/No/Partial] |

---

## Frameworks e Metricas

### Frameworks Referenciados
[List all frameworks mentioned: DORA, SPACE, DevEx, GQM, HEART, OKR, etc.]
- For each, indicate if it is REFERENCED (cited/discussed) or APPLIED (used as measurement instrument)

### Frameworks Propostos
[If the paper proposes a new framework, describe it]

---

## Fatores que Influenciam Produtividade

### Fatores Positivos
| Fator | Categoria |
|-------|-----------|
| [factor] | [Technical/Organizational/Human/Process] |

### Fatores Negativos
| Fator | Categoria |
|-------|-----------|
| [factor] | [Technical/Organizational/Human/Process] |

---

## Papel da IA e Automacao

| Campo | Valor |
|-------|-------|
| Usa IA/ML? | [Yes/No — describe if yes] |
| Automacao de coleta? | [Yes/No — describe if yes] |
| Impacto de IA na produtividade? | [Describe findings if applicable] |

---

## Resultados Principais

[Bullet points of key findings, with specific numbers when available]

---

## Desafios do Uso das Metricas

[List challenges and anti-patterns identified in the paper]

---

## Avaliacao de Qualidade Metodologica

| Criterio | Pontuacao (0-2) |
|----------|----------------|
| Objetivo claramente definido | [0-2] |
| Metodologia adequada ao objetivo | [0-2] |
| Amostra/contexto descrito adequadamente | [0-2] |
| Ameacas a validade discutidas | [0-2] |
| Resultados com evidencia suficiente | [0-2] |
| Contribuicao clara para pratica ou teoria | [0-2] |
| **TOTAL** | **[sum]/12** |

---

## Limitacoes

[List the paper's stated limitations]

---

## Contribuicao Principal

[One paragraph summarizing the key contribution]

---

*Extraido via NotebookLM em {DATE} para MLR: Software Developer Metrics in Practice*


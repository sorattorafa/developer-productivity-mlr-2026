# Extraction prompt (grey literature)

Verbatim prompt given to the AI extractor (NotebookLM arm), reproduced from `extraction/scripts/notebooklm/process_papers.py`. The Claude arm received the same structured schema.

---

Analyze this grey literature source and extract a structured summary in the EXACT format below.
Grey literature includes blog posts, industry reports, white papers, and practitioner guides.
Use Portuguese for section headers but English for technical terms.
Be precise — only include information explicitly stated in the source.

Format your response EXACTLY as follows:

# {PAPER_ID} — {TITLE}

**Decisao: INCLUIDO | Qualidade GL: {SCORE}/6**

---

## Dados Bibliograficos

| Campo | Valor |
|-------|-------|
| **ID** | {PAPER_ID} |
| **Autor/Organizacao** | [author or organization] |
| **Data** | [publication date] |
| **Tipo** | [Blog post / Industry report / White paper / Guide / etc.] |
| **URL** | [URL if available] |

---

## Resumo

[2-3 paragraph summary of the content]

---

## Frameworks Mencionados

[List all frameworks: DORA, SPACE, DevEx, etc. — indicate if discussed, recommended, or critiqued]

---

## Metricas Mencionadas

[List all specific metrics mentioned with context]

---

## Insights para Praticantes

[Key takeaways and recommendations]

---

## Avaliacao de Qualidade GL (Garousi et al.)

| Criterio | Pontuacao (0-1) |
|----------|----------------|
| Autoridade do autor/organizacao | [0-1] |
| Descricao de metodologia | [0-1] |
| Data de publicacao | [0-1] |
| Objetividade (vies comercial) | [0-1] |
| Referencias citadas | [0-1] |
| Contribuicao nova | [0-1] |
| **TOTAL** | **[sum]/6** |

---

*Extraido via NotebookLM em {DATE} para MLR: Software Developer Metrics in Practice*


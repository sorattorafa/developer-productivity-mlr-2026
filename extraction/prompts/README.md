# Extraction prompts (collection instruments)

The data-extraction instrument was a **structured form** applied identically to
every source by two architecturally distinct AI extractors (Claude and
NotebookLM), whose outputs were then reconciled by the human reviewer against
the full text.

This folder contains the verbatim prompts:

- [`extraction_academic.md`](extraction_academic.md) — form for academic sources
  (study type, research method, sample, context, frameworks/metrics, DORA/SPACE
  application, DevEx dimensions, challenges, quality via Dybå & Dingsøyr, etc.).
- [`extraction_grey.md`](extraction_grey.md) — form for grey literature
  (type, organization, frameworks, AI, quality via the AACODS checklist, etc.).

Both prompts are reproduced from `extraction/scripts/notebooklm/process_papers.py`
(the NotebookLM arm, which embeds them in code). The **Claude arm was driven
interactively with the same field schema**; the human reconciliation log is in
`extraction/comparison_report.md`. The metric-category definitions the
prompts refer to are in `protocol/CODEBOOK_CATEGORIES.md`.

The prompts are reproduced exactly as they were used. Their output templates use
Portuguese headings and field names (for example, "Campo | Valor" for "Field | Value"
and "Metricas Mencionadas" for "Metrics Mentioned"), which is why the extractor
outputs and the parsing code in `extraction/scripts/` contain Portuguese.

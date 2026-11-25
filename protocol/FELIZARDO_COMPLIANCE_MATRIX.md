# Compliance matrix — Felizardo et al. (2024) recommendations vs. this MLR

Reference: K. R. Felizardo, M. S. Lima, A. Deizepe, T. U. Conte, M. P. Barcellos, I. Steinmacher.
"Data Extraction for Systematic Mapping Study using a Large Language Model: A Proof-of-Concept
Study in Software Engineering." ESEM 2024, Barcelona. (`felizardo2024llm`)

Scope note. The reference paper addresses LLM-assisted **data extraction** only. Study
selection with LLMs is listed by the authors as future work and is not covered by their
recommendations. This MLR cites the paper for its extraction layer, which is the layer the
paper covers. The use of an LLM in the original screening pipeline of this study predates the
human revalidation, is outside the scope of the reference paper, and is reported separately in
the threats to validity.

| # | Practice in Felizardo et al. (2024) | Followed? | Where / how in this MLR | Deviation and mitigation |
|---|---|---|---|---|
| 1 | Do not fully replace manual extraction; use the LLM for semi-automated support | Yes | Human blind coding is the authoritative layer; two LLM extractors act as an audit layer (Section 3.5 of the article) | None |
| 2 | Human extraction as benchmark (oracle); compare LLM output against it | Yes | All 298 field-level discrepancies resolved by the first author against the full text; (H) columns of the master are authoritative | None |
| 3 | Zero-shot prompting (zero-shot matches or beats few-shot for this task) | Yes | Zero-shot structured prompts, stated in Section 3.5; prompts in the replication package | None |
| 4 | Structured prompt per data item, predefined keys, single iteration per study | Yes | Structured field schema over seven information groups; one pass per source | None |
| 5 | One researcher extracts, others review; disagreements resolved by consensus | Yes | First author codes; two other authors review the complete decision set; consensus meeting | None |
| 6 | LLM as a second reviewer for single-researcher settings; differences become data to review | Yes | Exactly the adopted design: extractor divergences were flagged and each one adjudicated by the human reviewer | None |
| 7 | Control model randomness (temperature and top_p set to zero via API) | No | Extractors ran through their standard interfaces (Claude; NotebookLM), which do not expose these parameters | Deviation D1. Mitigation: full human reconciliation of every extracted field; extractor agreement reported as descriptive concordance only |
| 8 | Report model, version, context window, and execution environment | Yes (recorded) | Extractor A: Claude Opus 4.8 (Anthropic), via the claude.ai interface, main pass March 2026, re-extractions April to July 2026. Extractor B: NotebookLM (Google), automated with notebooklm-py[browser] >= 0.3, main pass March 2026, re-runs June 2026; the service does not expose its underlying model version | Former deviation D2, resolved: versions and dates recorded here and in the replication package README |
| 9 | Classify LLM errors as TP / TN / FP (fabricated) / FN (missed or misidentified) and compute accuracy | Yes (verdict level) | Verdict-level table computed with the human decision as oracle (extraction/scripts/verdict_accuracy.py; workbook sheet 'AI vs Human Verdicts'). Academic: Claude 67.5%, NotebookLM 68.4%; grey: 97.1% and 97.8%; FN = 0 throughout, so every extractor error over-included and the reviewer removed it. Field-level accuracy remains reported as concordance classes (Table 4 of the article) plus the resolution log and the hallucination audit | Former deviation D3, resolved at the verdict level. A per-field TP/FP/FN restatement of the 298 resolutions stays possible from comparison_report.md; not promised in the text |
| 10 | Text-based PDF content extraction (no OCR of images) | Yes | Extraction operated on the text of each source | None |
| 11 | Report accuracy stratified by data type (objective vs. RQ-specific) | Yes (analogous) | Concordance reported per field class: binary 66–94%, categorical 19–45% (Table 4 of the article), mirroring the reference paper's 98.6% vs. 65.11% gradient | None |
| — | Study selection with an LLM | Out of scope | Not covered by the reference paper (listed there as future work). Final selection in this MLR is fully human (revalidation) | Reported in threats: the original pipeline's screening layer is preserved as a legacy log without model provenance |

Reviewed and approved by the first author on 2026-07-27. Part of the replication
package (protocol/).

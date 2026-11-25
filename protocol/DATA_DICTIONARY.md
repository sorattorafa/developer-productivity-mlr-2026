# Data dictionary — `data/master/MLR_Final_Consolidated.xlsx`

This is the master dataset of the review. It is an Excel workbook with several
sheets; the two analysed sheets are **`Included Papers`** (academic corpus) and
**`Grey Literature`** (grey corpus). Every number in the paper is recomputed
from these two sheets by `extraction/scripts/verify_statistics.py`.

## Two-layer coding (read this first)

Each source carries **two parallel blocks of columns**:

1. **AI-extraction columns** (no suffix) — values produced by the AI-assisted
   extraction pipeline (two extractors, reconciled). Provenance/audit only.
2. **Human columns, suffixed `(H)`** — the values assigned by the human
   reviewer and validated by the three-reviewer consensus. **These are the
   authoritative values used in the paper.** When in doubt, use the `(H)` column.

Categorical flags are coded `Yes` / `No`. The nine metric-category flags are
mutually non-exclusive (a source may carry several).

## Sheet `Included Papers` (academic; verdict in “MY VERDICT - Relevance”)

| Col | Name | Meaning / allowed values |
|----|------|--------------------------|
| 1 | Paper ID | Internal id, e.g. `P0027` |
| 2 | Title | Source title |
| 3 | Authors | Author list |
| 4 | Year | Publication year |
| 5 | Venue | Conference/journal |
| 6 | DOI | DOI (when available) |
| 7–9 | Source DB / Full Text / Eligible | Retrieval bookkeeping |
| 10 | Exclusion Reason | Reason when excluded |
| 11–30 | (AI-extraction block) | Study type, method, sample, context, frameworks/metrics mentioned, DORA/SPACE applied, challenges, DevEx, impact, AI discussed, quality, notes, PDF path — **as extracted by AI** (audit only) |
| 31 | **MY VERDICT - Relevance (H)** | `Include` / `Exclude` — human inclusion decision |
| 33 | Study Type (H) | Human-assigned study type |
| 34 | Research Method (H) | Human-assigned method (survey, interview, experiment, mining, …) |
| 35 | Context (H) | Industry / OSS / academic / mixed / unspecified |
| 36 | DORA Applied (H) | `Yes` = DORA operationalized as measurement (not merely cited) |
| 37 | SPACE Applied (H) | `Yes` = SPACE operationalized |
| 38 | AI Discussed (H) | `Yes` = AI assistants/LLMs discussed re: productivity |
| 39 | Productivity/Performance (H) | metric-category flag |
| 40 | Quality (H) | metric-category flag |
| 41 | Collaboration (H) | metric-category flag |
| 42 | Satisfaction/Wellbeing (H) | metric-category flag |
| 43 | Activity/Code (H) | metric-category flag (raw repository signals) |
| 44 | Delivery Performance (H) | metric-category flag (DORA territory) |
| 45 | DevEx Dimensions (H) | `Yes` = uses Noda’s flow/cognitive-load/feedback-loops model |
| 46 | Agile/Process (H) | metric-category flag |
| 47 | Survey/Perceptual (H) | metric-category flag (self-reported) |
| 48 | Evidence (quote/table) | Supporting quote/table justifying the coding |
| 49 | Confidence | Reviewer confidence: High / Medium / Low |
| 51 | Mentions Remote/COVID (H) | `Yes` / `No` |
| 52 | Data Time Window (H) | Period the study’s data covers |
| 53 | Primary/Secondary (H) | Primary study or secondary (review) |
| 54 | Quality Score (H) [1–5 Dybå & Dingsøyr] | Academic quality, scale 1–5 |
| 55 | Strength of Evidence (H) | mentioned / questionnaire / substantiated / substantiated (secondary) / conceptual proposal |

## Sheet `Grey Literature` (grey; verdict in “MY VERDICT - Relevance”)

| Col | Name | Meaning / allowed values |
|----|------|--------------------------|
| 1 | GL ID | Internal id, e.g. `G001` |
| 2 | Title | Source title |
| 3 | Author/Organization | Author or producing organization |
| 4 | URL | Source URL |
| 5 | Publication Date | Date/year |
| 7 | Type | Document type (report, white paper, blog post, thesis, …) |
| 8 | GL Tier | Garousi grey-literature tier (1–3) |
| 20 | **MY VERDICT - Relevance (H)** | `Include` / `Exclude` |
| 22 | GL Type (H) | Human-assigned grey type |
| 23 | DORA Applied (H) | `Yes` / `No` |
| 24 | SPACE Applied (H) | `Yes` / `No` |
| 25 | AI Discussed (H) | `Yes` / `No` |
| 26–34 | metric-category flags (H) | Productivity, Quality, Collaboration, Satisfaction/Wellbeing, Activity/Code, Delivery, DevEx Dimensions, Agile/Process, Survey/Perceptual |
| 36 | Confidence | High / Medium / Low |
| 38 | Mentions Remote/COVID (H) | `Yes` / `No` |
| 39 | Data Time Window (H) | Period covered |
| 40 | Primary/Secondary (H) | Primary or secondary |
| 41 | Quality Score (H) [1–6 AACODS] | Grey quality, scale 1–6 |

## Companion data files (in `data/master/`)

- **`grey_vendor_classification.csv`** — `id,vendor,organization`; `vendor=1` for
  tool/product providers (DORA/Google, GitHub, GitLab, LinearB, DX, Swarmia,
  Harness), `0` for independents (consultancies, media, academia). Drives the
  vendor-sensitivity analysis (28 vendor / 27 independent).
- **`sources.csv`** — `id,kind,authors_or_org,year,title,venue_or_type,doi_or_url`
  for all 124 included sources; use the DOI/URL to obtain each primary document
  (the PDFs themselves are not redistributed — see the README).
- **`mlr_stats.json`** — machine-generated output of `verify_statistics.py`
  (regenerate it; do not edit by hand).

## Other sheets in the workbook
`Excluded Papers` (full-text exclusions with reasons), `PRISMA Summary`,
`Search Log` (per-database query/date/filters/counts), `Statistics`,
`Dup_*` (duplicate-check audit), `Codebook_Verdict` (in-workbook codebook for
the metric categories — see also `CODEBOOK_CATEGORIES.md`).

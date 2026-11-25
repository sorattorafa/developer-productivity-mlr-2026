# Claude vs NotebookLM: search update of October 2026, sources retrieved in decision D1

Generated on 2026-10-19 by `extraction/scripts/compare_update_2026-10.py`, restricted to the 12 sources whose full text was first recorded as not retrieved and later obtained through the first author's browser (decision D1). The report on the previous 124 sources was not changed. Translated from Portuguese.

Sources compared: 12 (10 academic, 2 gray). EC6 sources (full text not retrieved) were not extracted.

Same typology as the original report (`comparison_report.md`): exact_match, partial_match, divergent, only_claude, only_nlm, both_empty. The comparison is automatic and serves as support; the resolution is made by the reviewer against the full text, in the "Resolution (reviewer)" column of `comparison_update_2026-10_D1.xlsx`. In the update, the fields on which the extractors diverged were resolved against the full text and recorded in the reading forms (`extraction/human_review/`), and this column was left empty.

Criteria: free text by word overlap (≥60% exact, ≥20% partial); frameworks as a set; DORA/SPACE/DevEx applied from the APPLIED marks; metrics by overlap of the names; quality with a tolerance of 2/12 (academic) and 1/6 (gray) for partial.

## Overall agreement

| Status | n | % |
|---|--:|--:|
| exact_match | 43 | 28.3% |
| partial_match | 43 | 28.3% |
| divergent | 50 | 32.9% |
| only_claude | 1 | 0.7% |
| only_nlm | 1 | 0.7% |
| both_empty | 14 | 9.2% |

## Agreement per field, academic sources

| Field | exact_match | partial_match | divergent | only_claude | only_nlm | both_empty | Agreement (exact+partial) |
|---|--:|--:|--:|--:|--:|--:|--:|
| study_type | 2 | 6 | 2 | 0 | 0 | 0 | 80% |
| method | 0 | 2 | 8 | 0 | 0 | 0 | 20% |
| sample | 0 | 3 | 7 | 0 | 0 | 0 | 30% |
| context | 0 | 4 | 6 | 0 | 0 | 0 | 40% |
| work_mode | 0 | 0 | 2 | 1 | 0 | 7 | 0% |
| process | 0 | 4 | 4 | 0 | 0 | 2 | 50% |
| frameworks_ref | 2 | 8 | 0 | 0 | 0 | 0 | 100% |
| frameworks_app | 2 | 2 | 0 | 0 | 1 | 5 | 80% |
| dora_applied | 9 | 0 | 1 | 0 | 0 | 0 | 90% |
| space_applied | 8 | 0 | 2 | 0 | 0 | 0 | 80% |
| devex_applied | 9 | 0 | 1 | 0 | 0 | 0 | 90% |
| ai_used | 3 | 0 | 7 | 0 | 0 | 0 | 30% |
| metrics | 5 | 5 | 0 | 0 | 0 | 0 | 100% |
| quality_total_12 | 0 | 1 | 9 | 0 | 0 | 0 | 10% |

## Agreement per field, gray sources

| Field | exact_match | partial_match | divergent | only_claude | only_nlm | both_empty | Agreement (exact+partial) |
|---|--:|--:|--:|--:|--:|--:|--:|
| gl_type | 0 | 1 | 1 | 0 | 0 | 0 | 50% |
| date | 1 | 1 | 0 | 0 | 0 | 0 | 100% |
| author | 0 | 2 | 0 | 0 | 0 | 0 | 100% |
| frameworks_ref | 2 | 0 | 0 | 0 | 0 | 0 | 100% |
| metrics | 0 | 2 | 0 | 0 | 0 | 0 | 100% |
| quality_gl_6 | 0 | 2 | 0 | 0 | 0 | 0 | 100% |

## Divergences per source (to be resolved during reading)

| ID | Type | Divergent fields | Title |
|---|---|---|---|
| P2016 | academic | study_type, method, process, space_applied, devex_applied, ai_used, quality_total_12 | Too Many DevEx Metrics, Too Little Guidance: DevEx Metrics Compass: ma |
| P2020 | academic | context, ai_used | The SPACE of AI |
| P2021 | academic | method, sample, work_mode, process, ai_used, quality_total_12 | EngThrive: Make It Fast and Easy to Do Great Work: Building a durable  |
| P2044 | academic | method, sample, context, work_mode, quality_total_12 | Exploring machine learning to support software managers' insights on s |
| P2047 | academic | method, sample, context, process, quality_total_12 | Mathematical Modelling of the Impact of Developer Experience Metrics o |
| P2048 | academic | method, context, ai_used, quality_total_12 | Beyond Traditional Metrics: Toward a Multifactorial Model for Measurin |
| P2066 | academic | method, sample, context, space_applied, ai_used, quality_total_12 | Technical Debt Quantification and Its Impact on Software Delivery Perf |
| P2072 | academic | study_type, method, sample, process, dora_applied, ai_used, quality_total_12 | Develop, Deploy, Operate: A holistic model for understanding the costs |
| P2090 | academic | sample, context, quality_total_12 | Highly Efficient Software Development Using DevOps and Microservices:  |
| P2102 | academic | method, sample, ai_used, quality_total_12 | Evaluation of the nomological validity of cognitive, emotional, and be |
| G094 | grey | gl_type | Advancing scientific productivity through better scientific software:  |

Sources with no divergent field (1): G083


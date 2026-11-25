# Search Exports

This folder contains the raw database export files from each academic database search performed for the MLR. The original search was conducted between January 31 and February 22, 2026, and updated on October 3, 2026.

## Search String

All databases used the same conceptual search string, adapted to each database's syntax:

```
(("developer experience" OR "DevEx" OR "developer productivity" OR
"engineering productivity" OR "DORA metrics" OR "SPACE framework" OR
"productivity factors") AND ("framework" OR "metrics" OR "measurement"
OR "factors" OR "assessment"))
```

## Available Exports

| Database | File | Records | Search Date | Format |
|---|---|---|---|---|
| ACM Digital Library | `acm/acm_dl_results.bib` | 150 | 2026-01-31 | BibTeX |
| Scopus | `scopus/scopus_export_Jan_31-2026.bib` | 142 | 2026-01-31 | BibTeX |
| Google Scholar | `scholar/google-scholar.bibtex` | 648 | 2026-02-22 | BibTeX |

## Original IEEE / Springer exports and 2026-07 re-runs

The IEEE Xplore (473 records) and Springer Nature (563 records) raw exports from the
January 2026 search were not preserved. Both searches were re-run on 2026-07-26 on the
native portals with the original string and filters:

| Database | Original (2026-01) | Re-run (2026-07-26) | Re-run file |
|---|---|---|---|
| IEEE Xplore | 473 (not preserved) | 428 | `ieee/export2026.07.26-21.52.02.csv` |
| Springer Nature | 563 (not preserved) | 689 | `springernature/springer_rerun_2026-07-27.csv` |

The re-runs are dated proxies, not the original retrieval. The IEEE re-run recovered all
21 IEEE-sourced included papers. A first Springer download (103 records) carried extra
interface filters and was replaced by the corrected export (689 records). Per-record fates
for all five sources are in `data/master/MLR_Selection_Process.xlsx` (Screening Itemization).

**For replicators:** The 228 included sources are listed in Supplementary Tables S1 and S2 of the article (`latex-article/appendix_academic.tex` and `appendix_gl.tex`) and in the master spreadsheet (`data/master/MLR_Final_Consolidated.xlsx`). The missing exports affect the verification of the initial retrieval step, not the final set of included sources.

## Deduplication

From 1,976 raw records (1,328 academic + 648 Google Scholar), 163 duplicates were removed (automated + manual), yielding 1,813 unique records for screening. The deduplication was performed using title and DOI matching.

## Google Scholar re-run (July 2026)

On 2026-07-25, the Google Scholar search was re-run with Publish or Perish, the same string, and the range 2010-2026 to measure what the original screening of this source missed. The export (`scholar/pop_rerun_2026-07-25.csv`) has 997 records, 919 of them unique, and each was screened against the same criteria. The screening is in the `Scholar Rerun` sheet of `data/master/MLR_Selection_Process.xlsx`.

## October 2026 update

On 2026-10-03, the five searches were run again with the original strings, restricted to records added after the original search. Windows, filters, and removals per database are in the `Update 2026-10 Summary` sheet of `data/master/MLR_Selection_Process.xlsx`.

| Database | File | Records identified | Window |
|---|---|---|---|
| IEEE Xplore | `ieee/export2026.10.03-12.14.38.csv` | 195 | added on or after 2026-01-31 |
| ACM Digital Library | `acm/acm_rerun_2026-10-03.bib` | 477 | January to October 2026 |
| Scopus | `scopus/scopus_rerun_2026-10-03.bib` | 359 | loaded on or after 2026-01-31 |
| Springer Nature | `springernature/springer_rerun_2026-10-03.csv` | 752 | October 2025 to October 2026 |
| Google Scholar | `scholar/pop_rerun_2026-10-03.bibtex` | 994 | 2025-2026 |
| **Total** | | **2,777** | |

The six web queries of the gray literature update and their candidates are in `grey/GREY_SEARCH_LOG_2026-10.md`.

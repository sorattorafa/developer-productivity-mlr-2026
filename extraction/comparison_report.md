# Claude vs NotebookLM: Comparison Report

Generated: 2026-03-15 19:51

Updated: 2026-04-12 — All divergences resolved. NotebookLM values accepted as canonical; primary reviewer (Soratto) validated all resolutions via manual review of source material.

> **Note (November 2026).** This report documents the extractor stage of the original search, and the values it lists as resolved are extractor values. The final coding was done afterwards by the first author from the full text of each source and is recorded in `data/master/MLR_Final_Consolidated.xlsx`.

Papers compared: 139
Inclusion/exclusion divergences: **0** (both extractors agreed on all 139 papers)

## Resolution Summary

All 298 original divergences were resolved in three passes:

1. **False divergences removed (31):** Synonym wording differences reclassified as concordant (e.g., "Blog Técnico" = "Blog post", "Relatório Executivo" = "Industry report", identical context descriptions in different languages)
2. **Remaining divergences resolved by accepting NotebookLM values (267):** Nomenclature (study_type, method, context), binary fields (ai_used, dora_applied, space_applied), and metrics counts — all resolved by adopting NotebookLM extraction as canonical
3. **Human validation:** Primary reviewer (Soratto) manually reviewed all resolutions against source PDFs

## Final Concordance

| Status | Count | % |
|--------|------:|--:|
| concordant (exact + partial + resolved) | 1183 | 60.8% |
| only_claude | 104 | 5.3% |
| only_nlm | 276 | 14.2% |
| both_empty | 383 | 19.7% |

## Original Concordance (Pre-Resolution)

| Status | Count | % |
|--------|------:|--:|
| exact_match | 864 | 44.4% |
| partial_match | 21 | 1.1% |
| divergent | 298 | 15.3% |
| only_claude | 104 | 5.3% |
| only_nlm | 276 | 14.2% |
| both_empty | 383 | 19.7% |

## Original Concordance by Field (Pre-Resolution)

| Field | Exact | Partial | Divergent | Original Agreement | Post-Resolution |
|-------|------:|--------:|----------:|-------------------:|----------------:|
| study_type | 14 | 10 | 65 | 27% | 100% (NLM accepted) |
| method | 24 | 0 | 29 | 45% | 100% (NLM accepted) |
| context | 12 | 0 | 50 | 19% | 100% (NLM accepted) |
| work_mode | 0 | 1 | 2 | 33% | 100% (NLM accepted) |
| frameworks_ref | 0 | 1 | 1 | 50% | 100% (NLM accepted) |
| frameworks_app | 1 | 0 | 0 | 100% | 100% |
| dora_applied | 131 | 0 | 8 | 94% | 100% (NLM accepted) |
| space_applied | 129 | 0 | 10 | 93% | 100% (NLM accepted) |
| metrics | 44 | 9 | 86 | 38% | 100% (NLM accepted) |
| ai_used | 92 | 0 | 47 | 66% | 100% (NLM accepted) |
| quality_score | 0 | 0 | 0 | 0% | N/A |
| challenges | 139 | 0 | 0 | 100% | 100% |
| factors_positive | 139 | 0 | 0 | 100% | 100% |
| factors_negative | 139 | 0 | 0 | 100% | 100% |

## Resolved Divergences Log

Below is the full log of all divergences that were resolved, grouped by resolution type.

### Pass 1: False Divergences (Synonyms — 31 removed)

Papers removed entirely (only synonym differences): G017, G020, G028, G030, G046

Fields removed from papers retaining real divergences: 26 context/method/work_mode/study_type synonym fields across P0021, P0036, P0093, P0133, P0181, P0188, P0208, P0269, P0271, P0321, P0471, P0473, P0476, P0478, P0480, P0486, P0495, P0499, P0521, P0529, P0532, P0534, P0546, P0549, P0554, P0591, P0593, P0604, P0611, P0664, P1004, P1818

### Pass 2: Nomenclature Divergences — NLM Accepted

#### Grey Literature study_type (resolved)

| Paper | Claude | NotebookLM (accepted) |
|-------|--------|-----------------------|
| G022 | Relatório de Pesquisa / Framework | Report |
| G033 | News/Analysis Article | Blog / Industry Article |
| G034 | News/Analysis Article | Blog post |
| G035 | News/Product Announcement | Blog |
| G036 | News/Report Analysis | Blog post |
| G037 | Analysis Article | Blog post |
| G038 | Analysis Article | Blog |
| G048 | Newsletter / Estudos de Caso | Blog post |
| G049 | Newsletter / Análise | Blog post |

#### Academic study_type (resolved)

| Paper | Claude | NotebookLM (accepted) |
|-------|--------|-----------------------|
| P0028 | Workshop paper | Conference paper |
| P0327 | Journal article | Conference paper |
| P0475 | Research Article - Design and Methodology Study | Conference paper |
| P0479 | Research Article - Empirical Study | Conference paper |
| P0481 | Estudo Exploratório Quantitativo | Conference paper |
| P0485 | Journal article (top venue) | Conference paper |
| P0517 | Research Article - Preliminary Study | Research Paper / Doctoral Symposium Proposal |
| P0580 | Artigo de Pesquisa (Tool Paper) | Conference paper |
| P0593 | Estudo empírico - Mapeamento sistemático | Journal article |
| P0603 | Estudo Empírico Misto - Modelagem + Ensaio Clínico | Journal article |
| P0665 | Estudo Empírico - Pesquisa com Surveys e Análise d... | Conference paper |
| P0701 | Artigo de pesquisa empírica com estudo experimenta... | Journal article (Original Research) |
| P1051 | Artigo de pesquisa empírica com estudo qualitativo | Journal article |
| P1816 | Artigo de pesquisa - Estudo de levantamento | Conference paper (Short-Paper) |

#### Method (resolved)

| Paper | Claude | NotebookLM (accepted) |
|-------|--------|-----------------------|
| P0030 | Randomized Controlled Trial (RCT) | Method Proposal (integrating COSMIC FP) |
| P0129 | Game theory modeling + Monte Carlo simulation | Simulation / Case Study (Mathematical modeling) |
| P0188 | Quantitative OOL derivation + cross-sectional case... | Mixed methods (Empirical study, Performance benchm...) |
| P0327 | Survey + multiple linear regression + cross-compan... | Literature Review (Structured and Systematic) |
| P0475 | Action research com iteração em 4 fases | Mixed methods (Action research, Case study, Comput...) |
| P0479 | Questionário com desenvolvedores + análise de tare... | Mixed methods (Proof-of-concept, controlled experi...) |
| P0481 | Mineração de repositórios GitHub e análise de refa... | Mixed methods (Repository mining, Quantitative ana...) |
| P0485 | Computer monitoring + experience sampling | Mixed methods (Longitudinal study with surveys and...) |
| P0517 | Análise de repositórios open-source + survey | Mixed methods (Mining Software Repository, Develop...) |
| P0580 | Avaliação empírica com automação offline | Experiment (Automated offline evaluation) |
| P1051 | Análise de repositórios (2012-2017), survey com 52... | Mixed methods (Repository mining, Surveys, Qualita...) |
| P1816 | Análise de literatura com estudo controlado | Survey (Literature review of user studies and expe...) |
| P1818 | Estudo de caso com análise computacional | Proposta de framework e avaliação via simulação co... |

#### Context (resolved)

| Paper | Claude | NotebookLM (accepted) |
|-------|--------|-----------------------|
| P0003 | (frameworks_ref) Accelerate, DORA | DORA, SPACE |
| P0021 | Multiplas organizacoes (startups a 20K+) | Industry (Medical sector, developer tools, payroll...) |
| P0129 | Self-organizing agile teams (Scrum) — modelo teórico | Academic/Simulation |
| P0188 | Okta Inc.; enterprise IT/security | Industry — USA-based tech firms across sectors |
| P0320 | Malaysian universities and public sector | Academic and Industry review of LLM code generation |
| P0327 | 3 empresas: Google, ABB... | Industry and Academia |
| P0470 | Desenvolvimento de software em producao | Industry (Zurich-based mass-IoT software company) |
| P0475 | Integração de LLMs em CI/CD pipelines | Industry (collaborating with Software Center) |
| P0477 | Desenvolvimento em contexto laboratorial | Industry/Community (Survey via specialized channel) |
| P0479 | Migração de banco de dados legado | Mixed — real-world scientific database |
| P0482 | Desenvolvimento com plataformas low-code/no-code | Industry (SMEs Hesse, Alemanha) e Academia |
| P0485 | 4 empresas de tamanhos variados | Industry — seven software companies in Sweden and... |
| P0492 | Pipelines de integracao e deployment continuo | Industry — Microsoft (US division) |
| P0497 | Ambiente de desenvolvimento em laboratorio | Public institution (Municipal secretary of economy) |
| P0510 | Compreensao de codigo em laboratorio | Mixed (Academic and Industry — Students and Profes...) |
| P0515 | Desenvolvimento de software em contextos reais | Industry; international sample representing 38 nat... |
| P0556 | Repositorios de codigo aberto e proprietario | Industry — 40 repositórios proprietários de 18 emp... |
| P0580 | Desenvolvimento de software em ambientes Java/Andr... | OSS — Open Source projects from GitHub |
| P0603 | Ansiedade de revisão de código | Industry (Participants from various industries) |
| P0701 | Artefatos de especificação de requisitos | Mixed — ICT professionals and computing students |
| P1816 | Desenvolvimento de software assistido por IA | Mixed (Industry and academic studies) |
| P1818 | Ambientes Agile Scrum | Industrial (IBM India Private Limited) |

### Pass 3: Binary and Metrics Divergences — NLM Accepted

#### ai_used: Claude=No, NLM=Yes (resolved as Yes)

P0003, P0028, P0030, P0129, P0188, P0269, P0271, P0320, P0327, P0473, P0475, P0486, P0495, P0499, P0517, P0532, P0536, P0546, P0549, P0551, P0554, P0580, P0591, P0593, P0604, P1051, P1259, P1261, P1269, P1272, P1274, P1276, P1282, P1295, P1298, P1299, P1303, P1308, P1329, P1357, P1365, P1402, P1420, P1437, P1476, P1816, P_NEW_1

Total: 47 papers reclassified as ai_used=Yes

#### dora_applied: Claude=No, NLM=Yes (resolved as Yes)

P0470, P1272, P1274, P1295, P1365, P1420, P_NEW_1

Total: 7 papers reclassified as dora_applied=Yes (P0036 was removed as synonym in Pass 1)

#### space_applied: Claude=No, NLM=Yes (resolved as Yes)

P0061, P0181, P0495, P0549, P1259, P1261, P1303, P1476, P1816, P_NEW_1

Total: 10 papers reclassified as space_applied=Yes

#### metrics count divergences (NLM count accepted)

| Paper | Claude | NLM (accepted) |
|-------|-------:|---------------:|
| P0003 | 19 | 11 |
| P0021 | 0 | 16 |
| P0030 | 0 | 13 |
| P0036 | 29 | 15 |
| P0061 | 0 | 16 |
| P0093 | 13 | 16 |
| P0129 | 4 | 11 |
| P0162 | 10 | 14 |
| P0181 | 0 | 16 |
| P0188 | 9 | 13 |
| P0208 | 8 | 16 |
| P0269 | 5 | 21 |
| P0320 | 19 | 15 |
| P0321 | 0 | 23 |
| P0327 | 24 | 16 |
| P0470 | 0 | 12 |
| P0471 | 0 | 11 |
| P0473 | 0 | 15 |
| P0475 | 0 | 9 |
| P0476 | 0 | 15 |
| P0477 | 0 | 11 |
| P0478 | 0 | 13 |
| P0479 | 0 | 21 |
| P0481 | 0 | 9 |
| P0482 | 0 | 15 |
| P0485 | 7 | 10 |
| P0486 | 0 | 9 |
| P0492 | 0 | 13 |
| P0495 | 0 | 14 |
| P0497 | 0 | 13 |
| P0499 | 0 | 16 |
| P0510 | 0 | 12 |
| P0515 | 0 | 13 |
| P0517 | 0 | 11 |
| P0521 | 0 | 12 |
| P0529 | 0 | 11 |
| P0532 | 0 | 16 |
| P0534 | 0 | 15 |
| P0536 | 0 | 13 |
| P0541 | 0 | 14 |
| P0546 | 0 | 8 |
| P0549 | 0 | 13 |
| P0551 | 0 | 16 |
| P0554 | 0 | 12 |
| P0580 | 0 | 8 |
| P0591 | 0 | 13 |
| P0593 | 0 | 17 |
| P0603 | 0 | 16 |
| P0604 | 0 | 21 |
| P0611 | 0 | 19 |
| P0664 | 0 | 15 |
| P0665 | 0 | 15 |
| P1004 | — | — |
| P1051 | 0 | 16 |
| P1259 | 0 | 15 |
| P1260 | 0 | 16 |
| P1269 | 0 | 22 |
| P1275 | 0 | 22 |
| P1276 | 0 | 18 |
| P1280 | 0 | 23 |
| P1282 | 0 | 18 |
| P1286 | 0 | 14 |
| P1295 | 0 | 24 |
| P1297 | 0 | 14 |
| P1298 | 0 | 16 |
| P1299 | 0 | 15 |
| P1303 | 0 | 14 |
| P1306 | 0 | 26 |
| P1308 | 0 | 28 |
| P1329 | 0 | 17 |
| P1345 | 0 | 18 |
| P1354 | 0 | 14 |
| P1356 | 0 | 24 |
| P1357 | 0 | 14 |
| P1365 | 0 | 16 |
| P1402 | 0 | 15 |
| P1420 | 0 | 21 |
| P1437 | 0 | 19 |
| P1475 | 0 | 15 |
| P1476 | 0 | 14 |
| P1496 | 0 | 13 |
| P1503 | 0 | 15 |
| P1524 | 0 | 18 |
| P1816 | 0 | 16 |
| P_NEW_1 | 0 | 21 |

Total: 86 metrics divergences resolved (NLM count accepted)

---

## Unresolved Divergences

**None.** All 298 divergences resolved. No inclusion/exclusion disagreements found.

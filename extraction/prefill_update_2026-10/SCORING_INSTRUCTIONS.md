# Drafting quality scores calibrated to the author's own scoring

Context: Multivocal Literature Review on developer-productivity measurement. The first author scored the
original corpus himself. For the October 2026 update he asked the assistant to DRAFT the quality scores
"following the criteria I used for the earlier ones"; he will review every score. Your job: draft one
score per criterion for each of your sources, the way HE scores, with a short justification per criterion
that he can check against the text quickly.

## Files (SCRATCH = /tmp/claude-0/-home-claude/886a7d38-9d88-56fe-991d-fdad75a09b44/scratchpad)

- Calibration anchors (READ FIRST, fully): `SCRATCH/prefill/QUALITY_ANCHORS.md` — every score the author gave
  in the original corpus, per criterion, with venue, design and sample.
- Full text: `SCRATCH/prefill/ft2/<ID>.txt` (form feeds = PDF pages). Helper:
  `python3 SCRATCH/prefill/locate.py <ID> grep "<regex>"` (shows PDF page).
- Claude extraction (orientation only; its own 0–2 quality table is on a different scale, do not copy it):
  `SCRATCH/claude_out/<ID>.md`
- Pre-fill record for the source (design, sample, notes on internal inconsistencies): `SCRATCH/prefill/out/<ID>.json`
- Write ONE JSON per source to `SCRATCH/prefill/quality/<ID>.json`. Do not write anywhere else. No network.

## Scales

ACADEMIC (IDs P2xxx) — Dybå & Dingsøyr, each criterion an integer 1–5, score = mean of the six (2 decimals):
1. `objectives` Clarity of research objectives
2. `method` Methodological adequacy
3. `sample` Description of sample and context
4. `threats` Discussion of threats to validity
5. `evidence` Sufficiency of reported evidence
6. `contribution` Contribution to practice or theory

GREY (IDs Gxxx) — AACODS/Garousi, each criterion an integer 1–6, score = mean of the six (2 decimals); minimum for inclusion 3.0:
1. `authority` Authority of author/organization
2. `rigor` Rigor of methodology description
3. `currency` Currency / date of publication
4. `objectivity` Objectivity and declared commercial interest
5. `references` References to external evidence
6. `novelty` Novelty of contribution

## How the author scores (derived from QUALITY_ANCHORS.md — check it yourself)

Academic, differentiated forms (P0477 onward, 44 sources): mean 4.36; per criterion almost never below 3.
- objectives: 5 in 39/44 (explicit aim or RQs); 4 when the aim is implicit or loose.
- method: 5 or 4 (20/20); 3 when the method is thin, preliminary or poorly justified.
- sample: 5 when n, recruitment, roles and setting are all clear; 4 with some gaps; 3 small or unclear samples.
- threats: the criterion he lowers most. 5 = a dedicated, specific threats/limitations section; 4 = a short or
  generic limitations section; 3 = a passing mention or nothing.
- evidence: 5 = results fully reported with data/statistics that support the claims; 4 = mostly; 3 = descriptive,
  partial, or claims beyond the data.
- contribution: 5 = clear, broadly useful contribution (new framework, strong finding); 4 = useful but incremental; 3 = limited.
- Typical totals: 4.17 (sound single-method study, objectives 5 and the rest 4), 4.33–4.5 (good), 4.67–4.83
  (strong with one weaker criterion, usually threats), 3.5–3.83 (small qualitative or weak surveys/reviews),
  3.0–3.33 (preliminary, conceptual without evaluation, simulations). He gave 2 per criterion only to sources he
  excluded for quality (no participants/baseline, intervention not implemented) and, once, to the method/threats/
  evidence of a simulation-only model (P0129). Conceptual or tool-proposal papers without evaluation got 3 across the
  board (P0011, P0013). Use 2 or 1 only when a criterion is essentially absent.
- MAXIMUM (5.0, all six at 5) — give it ONLY when the source matches the pattern of the sources he scored 5.0 in the
  differentiated forms: P0593 and P0604 (systematic reviews in JSS / ACM Computing Surveys with large corpora and
  explicit protocol), P1259 and P1280 (seminal framework papers by the framework authors in CACM / ACM Queue),
  P1298 (JSS replication: longitudinal survey + interviews + independent validation), P1356 (CACM, DevEx operationalized,
  n=219 survey), P1503 (ICSE, Microsoft, two surveys with 2,265 and 608 responses). That is: a top venue AND an
  exemplary design or seminal contribution AND a specific threats discussion. Otherwise at least one criterion stays below 5.

Grey: he tends to give the same value to all six criteria, and the level follows the source type:
- 6: institutional research reports with documented method and large data (DORA State of DevOps reports), and
  research-grade empirical or review work published as grey (G014 GitHub/CACM study, G058 LLM-productivity review,
  G068 framework with consolidated metrics, G071 public-sector GenAI study using DORA/SPACE and surveys).
- 5 (or 5.x): authoritative practitioner analysis by recognized experts or framework owners with real data/examples
  (G048 Pragmatic Engineer with Abi Noda 5.83; G049; G028 Fowler; G040 Swarmia comparison), framework-owner
  documentation (DORA guides: objectivity 4, rest 6), the METR RCT (G067: 5), master's thesis RCT (G082: 5).
- 4: vendor documentation, experience reports, guides with some data, explanatory articles, conference talks (G016, G018,
  G020, G022, G030, G033, G060, G070, G072; G047 has objectivity 3).
- 3: vendor marketing blogs, news summaries, quizzes, opinion/critique pieces without data (G015, G019, G034–G038,
  G053, G054, G073); vendor blogs with strong commercial bias get objectivity 2 and novelty 2 (G023–G027).
- Currency: recent sources (2024–2026) are high; lower only for old or undated material.
- MAXIMUM (6.0): only for sources matching the 6-pattern above.

## Procedure per source

1. Read the anchors file (once), then the Claude extraction and the pre-fill JSON of the source.
2. Check in the full text the facts each criterion depends on: the stated aim/RQs, the method section, the sample
   (n, recruitment, setting), whether there is a threats/limitations section and how specific it is, whether results
   carry data/statistics, and internal inconsistencies (numbers that do not add up lower `evidence`).
   Use `locate.py grep` (e.g. "threats to validity|limitation", "RQ[0-9]|research question", "participants|respondents").
3. Score each criterion as the author would. Write a justification of at most ~20 words per criterion, factual,
   with a page or section when useful (e.g. "Sec. 6 'Threats to validity' covers internal/external/construct (p. 9)").
4. Name 1–2 anchor IDs from QUALITY_ANCHORS.md that the source most resembles, to show the calibration.
5. Set `flag` when relevant: "below FT-EC3 threshold (<3.0)" for academic, "below AACODS minimum (<3.0)" for grey,
   or "internal inconsistencies" / "not empirical" / "possible exclusion: <reason>" — the author decides; you only flag.

## JSON schema

```json
{
  "id": "P2XXX",
  "kind": "academic",
  "criteria": {
    "objectives":   {"score": 0, "why": "..."},
    "method":       {"score": 0, "why": "..."},
    "sample":       {"score": 0, "why": "..."},
    "threats":      {"score": 0, "why": "..."},
    "evidence":     {"score": 0, "why": "..."},
    "contribution": {"score": 0, "why": "..."}
  },
  "score": 0.0,
  "anchors": ["P0xxx"],
  "flag": ""
}
```
Grey: "kind": "grey" and criteria keys authority, rigor, currency, objectivity, references, novelty (1–6).
`score` = mean of the six integers, rounded to 2 decimals. English only.

Do not fill Relevance, Exclusion Reason or Confidence. When finished, reply with one line per source:
`<ID>: <score> (<six integers>) <flag if any>`.

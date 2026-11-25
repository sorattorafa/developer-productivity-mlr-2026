# Pre-filling the human reading forms from the AGREED extractor values

Context: a Multivocal Literature Review on developer-productivity measurement. Two automated extractors
(Claude and NotebookLM) each produced an extraction form per source. The first author will audit a
pre-filled reading form ("ficha") per source against the full text. Your job is to compute, for a list of
sources, the values on which the two extractors AGREE, translated into the ficha vocabulary, and to locate
a verbatim supporting passage in the full text for each pre-filled value. You do NOT judge the source
yourself and you do NOT fill fields reserved to the author.

## Files (paths relative to SCRATCH = /tmp/claude-0/-home-claude/886a7d38-9d88-56fe-991d-fdad75a09b44/scratchpad)

- Claude extraction: `SCRATCH/claude_out/<ID>.md` (Portuguese headers, PT/EN text)
- NotebookLM extraction: `/mnt/user-data/uploads/Mesa - MacBook Air de Rafael--doutorado--projeto/extraction/notebooklm/<ID>_notebooklm.md`
  (English; `[n]` markers are NotebookLM's internal citations, ignore them)
- Full text: `SCRATCH/prefill/ft2/<ID>.txt` (form feeds = PDF page breaks; .txt sources have no pages)
- Helper: `python3 SCRATCH/prefill/locate.py <ID> grep "<regex>"` (find passages, shows PDF page) and
  `python3 SCRATCH/prefill/locate.py <ID> check "<quote>"` (must print FOUND for every quote you output)
- Write ONE JSON file per source: `SCRATCH/prefill/out/<ID>.json` (schema below). Do not write anywhere else.
  Do not touch any other file. Never use the network.

## Procedure per source

1. Read BOTH extraction files completely.
2. For every field below, derive the Claude value FROM THE CLAUDE FILE ONLY and the NotebookLM value FROM THE
   NOTEBOOKLM FILE ONLY, applying the definitions below. Ignore each extractor's own "Decisao"/"Qualidade" lines.
3. If the two derived values are the same → that is the pre-fill value. If they differ, or one extractor gives
   no basis for the field → value = null, and explain in `note` (short, English).
4. For every pre-filled value that is "Yes", and for study_type / research_method / context / data_window /
   gl_type when pre-filled, find ONE short verbatim passage (ideally 10–40 words, copied exactly from ft2 text,
   no ellipses inside) that supports it, and confirm it with `locate.py check` (must print FOUND). Record the
   page string printed by the helper ("PDF p. 3", or "no pages (HTML/text source)" → then use the section
   heading if you can see it, else "text source").
   - If you cannot find any supporting passage for an agreed "Yes" (or the passage you find clearly
     contradicts the agreed value), set value = null and note "agreed <X> but not confirmed in the full text".
   - "No" values need no passage.
5. Write the JSON. Keep notes short and factual. English only in values, notes and evidence.

## Fields — ACADEMIC sources (IDs P2xxx)

- `primary_secondary`: Primary (generates new evidence) | Secondary (synthesizes other studies: SLR, mapping, MLR, review).
- `study_type`: exactly one of: Experiment | Quasi-experiment | Case study | Survey | Qualitative-Interviews |
  Review-Secondary | Experience report | Repository mining | Mixed methods | Other. Use the DESIGN, never the
  venue ("Conference paper" is not a study type). Conceptual/framework proposals, tool papers, simulations,
  position papers, theses without one design → Other, with a short parenthetical, e.g. "Other (conceptual framework proposal)".
  Agreement = same category (parenthetical may differ; use the clearer one).
- `research_method`: one English line in the style of the existing forms, e.g.
  "Three-arm randomized controlled trial (pilot); 39 developers randomized, 25 analysed, 130 task observations; ITT, IV (2SLS), Lee bounds".
  Pre-fill only if both extractions describe the same design; include only facts present in BOTH or stated
  by one and not contradicted by the other. If they give conflicting numbers, omit the number and say so in `note`.
- `context`: one English line: "industry | OSS | academic | mixed; <setting>; <sample>", e.g.
  "industry; single Finnish IT consultancy (Siili Solutions), 25 full-stack developers analysed". For reviews: "academic (secondary/review); <n> primary studies".
  For conceptual papers with no sample: "not reported (conceptual; no empirical sample)". Same agreement rule as research_method.
- `dora_applied`, `space_applied`: Yes ONLY if the framework is the study's measurement instrument
  (its metrics/dimensions are operationalized to measure or structure the measurement). Cited, discussed,
  compared or used as background → No.
- `ai_discussed`: Yes if AI/ML/GenAI (coding assistants, LLMs, AI tools) is a SUBSTANTIVE topic in relation to
  software development or to measuring developer productivity — as a tool developers use, as an object of
  measurement, or as the measurement/evaluation instrument the study proposes. Passing mention, or AI only as an
  application domain unrelated to how developers work (e.g., building ML systems) → No.
- `remote_covid`: Yes if remote/hybrid/distributed work or the COVID-19 pandemic is part of the study's context,
  motivation, data or findings (more than a passing mention). Otherwise No.
- `data_window`: the period the DATA covers (e.g., "July–September 2024"; for reviews "review coverage 2010–2024").
  Pre-fill only if both extractions state the same period; otherwise null (note what each says, or "not stated by either").
- Nine metric-category flags (Yes/No). A category is Yes if the study USES, PROPOSES or SUBSTANTIVELY DISCUSSES at
  least one metric of that category (passing mention in introduction/related work does not count). Multi-label.
  - `cat_productivity` Productivity/Performance: output/performance — velocity, throughput, story points done,
    tasks/features delivered, task completion time/speed, productivity scores. NOT perceived productivity
    (→ survey) and NOT pure delivery/deploy metrics (→ delivery).
  - `cat_quality` Quality: defects/bugs, error rate, test coverage, code quality scores, change failure rate,
    MTTR, stability, incidents, maintainability.
  - `cat_collaboration` Collaboration: communication, code review/peer review, knowledge sharing,
    coordination, pair programming, trust, meetings. NOT collaboration measured only as commit counts.
  - `cat_satisfaction` Satisfaction/Wellbeing: satisfaction, engagement, burnout, stress, morale, well-being,
    mental health, work-life balance, emotions; "developer experience" as a broad affective concept.
  - `cat_activity` Activity/Code: raw repository activity — commits, PRs, merges, diffs, LOC/files changed,
    churn, event counts.
  - `cat_delivery` Delivery Performance: deployment frequency, lead time for changes, cycle time, time to
    market, release frequency, delivery latency (CFR and MTTR go to Quality).
  - `cat_devex` DevEx Dimensions: ONLY explicit use of the DevEx framework of Noda/Storey/Forsgren and its
    dimensions (feedback loops, cognitive load, flow state). Generic "developer experience" → Satisfaction.
  - `cat_agile` Agile/Process: sprint, scrum, kanban, workflow/pipeline process metrics, ceremonies,
    iteration cadence, planning.
  - `cat_survey` Survey/Perceptual: measurement by perceptual instrument — survey, questionnaire, Likert,
    self-report, interviews about perceptions, subjective ratings (coexists with content categories).
  For a SECONDARY study mark Yes only for what the review synthesizes substantively, not everything it lists.

## Fields — GREY sources (IDs Gxxx)

Same definitions, with these differences:
- no `study_type`, `research_method`, `context`; instead `gl_type`: one of Blog | Article | Report | Whitepaper |
  Documentation | Thesis | Survey report | Experience report | Conference talk | Video/Podcast | Other.
  Agreement = same category.
- `primary_secondary`: Primary if the source presents its own data, experience, guidance or analysis;
  Secondary if it mainly summarizes other sources.
- `dora_applied`, `space_applied`: write "Yes (empirical)" if the source measures/reports data with the
  framework; "Yes (guidance)" if it gives operational guidance on how to measure with it; "No (reference only)"
  if only cited/discussed; "No" if not mentioned. Agreement = same level.
- All other fields as for academic sources.

## JSON schema (one file per source)

```json
{
  "id": "P2002",
  "kind": "academic",
  "fields": {
    "primary_secondary": {"claude": "Primary", "nlm": "Primary", "value": "Primary", "note": ""},
    "study_type":        {"claude": "...", "nlm": "...", "value": "...", "note": ""},
    "research_method":   {"claude": "<what Claude says, short EN paraphrase>", "nlm": "<short>", "value": "<EN line or null>", "note": ""},
    "context":           {"claude": "...", "nlm": "...", "value": "...", "note": ""},
    "dora_applied":      {"claude": "No", "nlm": "No", "value": "No", "note": ""},
    "space_applied":     {...}, "ai_discussed": {...}, "remote_covid": {...}, "data_window": {...},
    "cat_productivity":  {...}, "cat_quality": {...}, "cat_collaboration": {...}, "cat_satisfaction": {...},
    "cat_activity": {...}, "cat_delivery": {...}, "cat_devex": {...}, "cat_agile": {...}, "cat_survey": {...}
  },
  "evidence": [
    {"field": "space_applied", "quote": "<verbatim from ft2>", "loc": "PDF p. 3"}
  ]
}
```

Grey: replace study_type/research_method/context by `gl_type`; "kind": "grey".
Every field key must be present. `claude`/`nlm` hold the value each extractor supports (or "no basis").
`value` is null whenever they differ or the passage check fails. One evidence entry may serve several fields
(use "field": "cat_quality, cat_productivity").

Never fill or mention: Relevance, Exclusion Reason, Confidence, Quality Score. Those belong to the author.

When finished with all your sources, reply with one line per source: `<ID>: <n> fields pre-filled, <m> left
blank` plus any source where something looked wrong (e.g., extraction about a different paper, empty full text).

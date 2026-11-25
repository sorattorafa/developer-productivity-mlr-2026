# Codebook: Metric Categories

**Purpose.** Operational definitions for classifying, from the full text, which metric categories each source addresses. Each category is a **Yes/No flag per paper** (multi-label: a paper can have several). This replaces keyword counting and untraceable manual recounting.

**General coding rules**
1. The unit is the **paper**: mark Yes if the study *uses, proposes, or substantively discusses* at least one metric of that category. A passing mention in the introduction or related work does not count.
2. Code from the **full text**, not from the AI summary.
3. **Multi-label:** mark every applicable category.
4. In the evidence column, record the **sentence, figure, or table** that justifies each Yes (traceability).
5. When in doubt between two close categories, mark both and add a note.
6. The nine categories below are the final taxonomy applied to the whole corpus.

---

## Categories

### 1. Productivity/Performance
Metrics of aggregate output or performance. **Includes:** velocity, throughput, completed story points, delivered tasks or features, "productivity score". **Excludes:** subjective perception of productivity (→ Survey/Perceptual) and pure delivery or deployment metrics (→ Delivery Performance). *Known ambiguity:* this category is broad and overlaps with Activity/Code and Delivery Performance; it is a candidate for refinement.

### 2. Quality
Quality of the software or process. **Includes:** change failure rate, defects or bugs, error rate, test coverage, MTTR, stability, incidents. **Excludes:** quality perceived through a survey (also mark Survey/Perceptual).

### 3. Collaboration
Interaction and teamwork. **Includes:** communication, code review or peer review, knowledge sharing, coordination, pair programming, trust, meetings. **Excludes:** collaboration measured only by commit counts (→ Activity/Code).

### 4. Satisfaction/Wellbeing
Human and affective state. **Includes:** satisfaction, engagement, burnout, stress, morale, well-being, mental health, work-life balance, sentiment or emotion. **Note:** "developer experience" as a *broad affective concept* belongs here; when the paper uses the **DevEx framework and its dimensions**, mark DevEx Dimensions.

### 5. Activity/Code
Raw signals of repository activity. **Includes:** commits, pull requests, merges, diffs, lines or files changed, churn, event counts. **Excludes:** lead time and deployment (→ Delivery Performance). *Known ambiguity:* overlap with Productivity/Performance. The rule is that a raw activity count goes here, and an aggregate interpreted as output or performance goes to Productivity/Performance.

### 6. Delivery Performance
Delivery performance (the core of DORA). **Includes:** deployment frequency, lead time for changes, cycle time, time to market, release frequency, delivery latency. **Excludes:** change failure rate and MTTR (→ Quality, by convention of this codebook, although DORA groups the four together).

### 7. DevEx Dimensions
Explicit use of the **DevEx framework** and its dimensions. **Includes:** feedback loops, cognitive load, flow state, and reference to the DevEx model (Noda, Storey, Forsgren). **Excludes:** generic mention of "developer experience" without the framework (→ Satisfaction/Wellbeing).

### 8. Agile/Process
Process and method metrics. **Includes:** sprint, scrum, kanban, workflow or pipeline metrics, ceremonies, iteration cadence, planning. **Excludes:** velocity or story points as output (→ Productivity/Performance).

### 9. Survey/Perceptual
Measurement through a perceptual instrument. **Includes:** survey, questionnaire, Likert scale, self-report, subjective rating or perception. **Usage rule:** this is a **measurement-method** category and often coexists with a content category (for example, satisfaction measured by a survey → mark 4 and 9). *Known ambiguity:* it mixes "what is measured" with "how it is measured"; it is a candidate to become a separate dimension.

---

## Study type: two separate dimensions

Study type is classified with **two orthogonal fields** (decision of the first author):

**1. Primary vs. secondary** (binary field)
- **Primary:** produces new evidence (experiment, case study, survey, interviews, repository mining, experience report).
- **Secondary:** synthesizes evidence from other work (systematic review, mapping study, MLR). There are about 10 in the corpus, and they are treated separately in a sensitivity analysis.

**2. Study Type (design)**: a controlled vocabulary, kept separate from the *venue* (do not use "Conference Paper" or "Journal" here, since these describe where the work was published):
Experiment · Quasi-experiment · Case study · Survey · Qualitative/Interviews · Review/Secondary · Experience report · Repository mining · Mixed methods · Other.

## How to code a SECONDARY study (review)

- **Relevance:** usually included if it addresses the measurement of developer productivity.
- **Primary/Secondary:** Secondary. **Study Type:** Review/Secondary.
- **Categories and frameworks:** mark **Yes** only for what the review **substantively synthesizes** (its actual focus), not for everything it lists in passing. A review touches on many topics and would inflate the profile if marked in full.
- **Time window of the DATA:** use the **period covered by the review** (for example, 2006 to 2024), not the year of publication.
- **Notes:** record explicitly that it is a secondary study.

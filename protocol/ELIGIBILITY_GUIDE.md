# Eligibility Guide: MLR on Developer Productivity Measurement (2016–2026)

> This is the working guide used for the full-text reading of the original search, written in March 2026 and translated from Portuguese. The article describes the final procedure, and where the two differ, the article prevails. In particular, the final quality assessment rated each criterion from 1 to 5 for academic sources (Dybå and Dingsøyr) and from 1 to 6 for gray sources (AACODS), instead of the 0 to 2 scale of Block F below, and the full-text exclusions follow the FT-EC1 to FT-EC5 typology of `EXCLUSION_LOG.md`.

> **Step 6 of the MLR workflow**
> 349 papers for full-text reading + 55 gray literature sources
> Last updated: March 2026

---

## Reading strategy

Do not read the papers linearly. Use this order to be efficient:

1. **Abstract + Conclusion** (~30 s): does the paper deserve a full reading?
2. **Introduction**: what are the aim and the research questions of the paper?
3. **Results / Findings**: which metrics or frameworks were identified or validated?
4. **Methodology**: how were the data collected? Is the study methodologically sound?
5. **Related Work**: does it mention other relevant frameworks or studies?

---

## STEP 1: Eligibility decision

### INCLUSION criteria (all must be met)

- [ ] Addresses metrics, indicators, or frameworks for **software developers as professionals**
- [ ] The context is software development (industry, OSS, or academia with real practitioners)
- [ ] Published between 2016 and 2026 (already filtered, but confirm)
- [ ] Full text available and readable
- [ ] Written in English (IC5 of the article). Note: the initial draft of the protocol also admitted Portuguese, but this had no practical effect, since no source in Portuguese was included (the 7 from Brazilian venues are written in English)

### EXCLUSION criteria (any one excludes)

| Code | Criterion |
|------|-----------|
| EC1 | Domain outside software (agriculture, manufacturing, medicine, etc.) |
| EC2 | "Software metrics" means only LOC or cyclomatic complexity, unrelated to the performance of the developer as a professional |
| EC3 | The paper only cites frameworks, with no original contribution on metrics |
| EC4 | "Developers" in the paper are researchers or users, not software engineers |
| EC5 | "Metrics" are user, product, or business metrics unrelated to the developer |
| EC6 | Full text not accessible |

### Fields to record for the decision

- **Decision**: Include / Exclude
- **Reason (if Exclude)**: code EC1–EC6
- **Confidence**: High / Medium / Low (ask a second reviewer if Low)

### Red flags for quick exclusion

- "Productivity" refers to another domain
- "State-space models", "nano-positioning", and similar records that passed the keyword filter
- Papers from 2015 or earlier that passed the date filter

---

## STEP 2: Data extraction (included papers)

### Block B: Study characterization

| Field | Options |
|-------|---------|
| Publication type | Journal article / Conference paper / Workshop / Technical report |
| Research type | Survey/Questionnaire / Case study / Experiment/RCT / SLR/MLR/Mapping / Experience report / Interview study / Repository mining / Mixed methods |
| Organizational context | Startup / SME / Large company / Multiple / OSS / Academia |
| Scale | Number of developers or teams (if reported) |
| Work mode | On-site / Remote / Hybrid / Not reported |
| Development methodology | Agile/Scrum / DevOps / Waterfall / Not specified |

---

### Block C: Metrics and frameworks (CORE OF THE EXTRACTION)

This is the most important block for the research questions of the MLR.

#### C1. Frameworks referenced or proposed

Mark all that appear:

- [ ] DORA (Deployment Frequency, Lead Time for Changes, Change Failure Rate, MTTR)
- [ ] SPACE (Satisfaction, Performance, Activity, Communication, Efficiency)
- [ ] DevEx / DX (Noda et al., 2023)
- [ ] DX Core 4 (Speed, Effectiveness, Quality, Impact)
- [ ] Own framework proposed? Yes / No; if yes, what is its name?
- [ ] Other: _______________

#### C2. Specific metrics identified

For each metric found in the paper, record:

| Metric | Category | Level | How collected | Empirically validated |
|--------|----------|-------|---------------|-----------------------|
| (name) | Productivity / Quality / Satisfaction / Delivery speed / Collaboration / Other | Individual / Team / Organization | Git repository / Survey / Project tool / Observation / Biometric / Other | Yes / No / Partial |

#### C3. Classification of the metrics

- **Objective**: quantitative data collected automatically (e.g., deployment frequency, PR cycle time)
- **Subjective**: perception, self-assessment, survey (e.g., satisfaction, flow state)
- **Output**: artifacts produced (commits, PRs, lines of code)
- **Outcome**: impact on the product or business (production bugs, delivery time)
- **Process**: how the work is done (meetings, interruptions, collaboration)

---

### Block D: Factors that influence productivity and performance

#### D1. Positive factors identified

List the factors that the paper reports as increasing productivity or performance:

| Factor | Category |
|--------|----------|
| (e.g., autonomy at work) | Human/Psychological |
| (e.g., well-configured CI/CD) | Technical/Tooling |
| (e.g., unnecessary meetings) | Organizational |

Categories: **Technical** / **Human/Psychological** / **Organizational** / **Tooling**

#### D2. Negative factors / friction points

List the interruptions and blockers of productivity identified (same table and categories).

#### D3. Relationships identified

- Does the paper identify a correlation or causal link between metrics and outcomes? Yes / No
- If yes, which relationship?

---

### Block E: Role of AI and automation

Relevant to the main aim of the first author's doctoral research.

| Field | Record |
|-------|--------|
| Uses AI/ML to collect or analyze metrics? | Yes / No |
| AI technique used | Classical ML / Deep learning / NLP/LLM / Statistical analysis / Other |
| Data sources for AI | Commits / PRs / Issues / Surveys / Logs / Biometric / Other |
| Automated metric collection? | Yes / No; if yes, how? |
| Compares AI with a manual approach? | Yes / No; if yes, with what result? |

---

### Block F: Methodological quality assessment

Score each item from 0 to 2 (0 = not met, 1 = partially met, 2 = met).

**For empirical studies:**

| Criterion | Score (0–2) |
|-----------|-------------|
| Research objective clearly defined | |
| Methodology adequate to the objective | |
| Sample and context adequately described | |
| Threats to validity discussed | |
| Results supported by sufficient evidence | |
| Clear contribution to practice or theory | |
| **TOTAL** | **/12** |

**Interpretation**: 0–4 = low quality | 5–8 = medium quality | 9–12 = high quality

**For SLRs and mappings (papers that are reviews):**

| Criterion | Yes / No / Partial |
|-----------|--------------------|
| Follows a documented protocol? | |
| Explicit inclusion and exclusion criteria? | |
| Quality assessment of the primary studies? | |
| Adequate synthesis of the results? | |

---

### Block G: Contribution and limitations

- **Main contribution** (1–2 sentences): what does this paper add that is useful for the MLR?
- **Main limitations** (2–3): which limitations does the paper itself report?
- **Relevant future work**: any suggestion aligned with the research aims?

---

## Gray literature: adapted criteria (55 sources)

The criteria are adapted for non-academic sources following Garousi et al. (2019).

### INCLUSION criteria

- [ ] Relevant to metrics or to the assessment of software developers
- [ ] Published or updated between 2016 and 2026
- [ ] Identifiable source (organization, author)

### EXCLUSION criteria

- [ ] Purely promotional or marketing content, without data or technical arguments
- [ ] URL not accessible (record as unavailable)

### Additional fields for gray literature

| Field | Record |
|-------|--------|
| Type | Research report / Technical documentation / Technical blog / Practical guide |
| Contains empirical data? | Yes / No / Partial |
| Tier | 1st / 2nd / 3rd (already defined in the previous step) |
| Access date | DD/MM/YYYY |

---

## PRISMA numbers (to update during reading)

```
Eligibility (full text):
  Papers for full-text reading:            349
  Excluded at eligibility:                 ___
    EC1 - wrong domain:                    ___
    EC2 - code metrics only:               ___
    EC3 - no original contribution:        ___
    EC4 - developers = non-engineers:      ___
    EC5 - product/business metrics:        ___
    EC6 - full text not accessible:        ___
  Included after eligibility:              ___

Gray literature assessed:                   55
  Excluded at eligibility:                 ___
  Included:                                ___

FINAL TOTAL FOR EXTRACTION:                ___
```

---

## Checklist per paper

Before moving to the next paper, confirm:

- [ ] Decision recorded (Include/Exclude + reason)
- [ ] If included: blocks B, C, D, E, F, G completed
- [ ] Specific metrics listed individually (Block C2)
- [ ] Quality assessed (Block F)
- [ ] Contribution summarized in 1–2 sentences (Block G)
- [ ] Paper added to `MLR_Data_Extraction_Template.xlsx`

---

*Guide written in March 2026.*
*Based on: Kitchenham & Charters (2007), Garousi et al. (2019), Felizardo et al. (2024).*

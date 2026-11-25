# Full-Text Exclusion Log with Reasons (original search)

> Purpose: to show **which kinds of papers the search strings captured but the criteria excluded**. Each entry was reviewed in the full text by the first author. The strings are broad (DevEx, developer or engineering productivity, DORA, SPACE, productivity factors), so they retrieve work that *looks* on topic but, when read in full, does not measure developer productivity or experience, brings no empirical evidence of its own, has insufficient quality, or is a duplicate. The full reason for each exclusion is in the "Exclusion Reason" column of the master spreadsheet (`data/master/MLR_Final_Consolidated.xlsx`).
>
> This log covers the 40 full-text exclusions of the original search. The full-text exclusions of the October 2026 update are itemized in the `Update 2026-10 Full Text` sheet of `data/master/MLR_Selection_Process.xlsx`. Translated from Portuguese.

## Exclusion typology (maps to "reports excluded with reasons" in PRISMA)

- **FT-EC1. Out of scope (topic):** matched the string, but the object is not the measurement of developer productivity or experience.
- **FT-EC2. No empirical evidence of its own:** vision or position paper, research plan, conceptual or preliminary framework, study design without execution, pattern language.
- **FT-EC3. Insufficient methodological quality:** below the Dybå and Dingsøyr minimum of 3.0, weak validation, untraceable data.
- **FT-EC4. Duplicate or overlap.**
- **FT-EC5. Language (IC5):** full text not written in English.

---

## FT-EC1. Out of scope (captured by the string, different topic)

| ID | Year | Title (short) | Why it matched the string | Reason for exclusion |
|----|------|---------------|---------------------------|----------------------|
| P0189 | 2021 | Performance Portability across AMD/Intel/NVIDIA GPUs | "productivity" | Productivity here refers to **HPC code**, not to the developer (P3HPC). |
| P0327 | 2023 | Root-Cause & Mitigation for Cloud Incidents using LLMs | "productivity" + LLM | It is **AIOps / incident management**; productivity appears only as motivation. |
| P0408 | 2019 | Eleven Nontechnical Phenomena … Technical Debt | "productivity"/"factors" | Addresses the **dynamics of technical debt**, not productivity measurement. |
| P0411 | 2022 | To Type or Not to Type? JS vs TS Quality on GitHub | "quality"/"measurement" | Quality of **code and language**, not developer productivity. |
| P0517 | 2025 | Studying Code Understandability Through Atoms of Confusion | "productivity" (motivation) | Object = **atoms of confusion** and code comprehension or quality (MSR + perception + LLM refactoring). Productivity only as background motivation. |
| P0479 | 2025 | Seamless Data Migration with DAMI-Framework | "developer experience" | The object is the **data migration framework**; DX is only the method used to evaluate the tool. |
| P0532 | 2021 | Smart Build Targets Batching Service at Google | "productivity" (loose) | Optimization of **build infrastructure** (Bazel, millions of builds per day). Productivity mentioned in passing, neither measured nor validated. |
| P0546 | 2019 | Analyzing and Repairing Compilation Errors (DeepDelta) | "productivity" (motivation) | Contribution = **automatic repair of compilation errors with ML** (DeepDelta). Resolution time measured only as motivation for the tool, not as productivity measurement. |
| P0188 | 2025 | AI & Cloud for Next-Gen Web Development | "AI"/"productivity" | Web development with AI and cloud (out of scope) **and** untraceable data (see FT-EC3). |
| P0499 | 2025 | Advancing HCI with Neuromorphic Technology | "developer experience"/"productivity" (keywords) | The object is the adoption and tooling of **neuromorphic programming** (12 interviews → accessibility guidelines), not productivity measurement. "DevEx" only as a keyword; "productivity" once, as a design aspiration. |
| P0580 | 2022 | Context-aware Code Recommendation in IntelliJ IDEA | "productivity" (motivation) | **Tool paper** (CA-FACER code recommendation plugin, with a video demo). "Productivity" twice as generic motivation; no measurement of productivity or experience. |
| P0701 | 2024 | Metrics for Evaluating and Improving Transparency in SE | "productivity"/"metrics" | The object is the **measurement of transparency** (GQM; non-functional requirement). "transparency" 327 times vs. "developer productivity" once; productivity only as a downstream benefit (stakeholder level) in a maintainability experiment on an SRS. |
| P1004 | 2018 | Developer Experience Considering Work Difficulty | "developer experience" (homonym) | "Experience" = **expertise or seniority** (not DevEx). Object = **code quality and defects** and file difficulty (product metrics, 3 projects, ~250k LOC). "productivity" 0 times. Out of scope and homonym. |
| P1051 | 2020 | Relevant Changes and Automation Needs in Modern Code Review | "productivity"/"developer experience" (in passing) | Object = **taxonomy of change types in code review and automation needs** (recommender systems). "code" 215 times and "tool" 70 times vs. "productivity" twice. Code review tooling, not productivity measurement. |

## FT-EC2. No empirical evidence of its own (proposal, design, or vision)

| ID | Year | Title (short) | Type | Reason for exclusion |
|----|------|---------------|------|----------------------|
| P0036 | 2025 | Multi-Agent AI Framework for Agile Workflow | Proof of concept | Proposed agentic framework; validation left as future work. |
| P0133 | 2021 | Framework: emotions × agile productivity | Preliminary framework | No hypotheses, no data, no evaluation. |
| P0144 | 2019 | Recognizing Emotions Using Biometrics: Design | Study design | Field protocol; no data or results (pilot with n = 1 only planned). |
| P0145 | 2018 | Sensing Developers' Emotions: Replicated Experiment | Replication design | Protocol without execution, no data. |
| P0179 | 2016 | Leveraging Biometric Data to Boost Productivity | Vision/position | Summarizes results the authors had already published and sets out an agenda; no new study. |
| P0412 | 2024 | Organizational Ohm's Law: Engineering Velocity | Conceptual | Theoretical model (formulas), no empirical data of its own. |
| P0471 | 2024 | Cognitive Patterns for Developer Experience | Pattern language | Six DX patterns in prescriptive form; informal mining. |
| P0475 | 2024 | Enhancing Software Design & DX via LLMs | Doctoral plan | Three-phase plan of one doctoral student; no results. |
| P1276 | 2026 | The Bottom-Up Approach to Developer Experience | Conceptual synthesis / summary | Combines DevEx, cognitive load, and socio-technical congruence into a "friction model" and proposes instruments (friction log, DX champion) **without an empirical study or a review protocol**. Low-tier venue (iajet). Also FT-EC3. |
| P0554 | 2019 | API Fluency | Position/proposal | Short paper (4 pages) that argues for "API fluency" and proposes spaced repetition; no empirical study. Productivity only as motivation. |
| P0320 | 2024 | AI-Powered Code Reviews via LLMs | Overview (probably AI-generated) | Claims to "present experimental data", but there is no method, sample, or results. |
| P1496 | 2024 | Enhancing Developer Experience by Reducing Cognitive Load | Conceptual / strategies | A "strategies" article for reducing cognitive load in DevEx, **with no empirical study** (no method, data, sample, or results), about one reference, 5 pages. IJCTT (Seventh Sense Research Group), a low-tier or predatory venue (same family as IJTSRD, P1272). Also FT-EC3. |

## FT-EC3. Insufficient methodological quality

| ID | Year | Title (short) | Reason for exclusion |
|----|------|---------------|----------------------|
| P1260 | 2025 | Setting Productivity Metrics for Automation Dev Teams (BPA) | **Bachelor's-level** literature synthesis (Aalto, 36 pp.) applying SPACE, DORA, and DevEx to the BPA context; **no empirical study of its own**. Below the Dybå minimum of 3.0. |
| P0093 | 2019 | API for Developer Payroll in Startups | Low quality: duplicated sentences, compromised construct validity; tool validation without rigor. |
| P0156 | 2021 | Productivity Model: Validation via Expert Review | Validation by "expert review" with **n = 3** anonymous experts; weak bar for expertise. |
| P0144 / P0145 | 2019/2018 | (above) | Also below the Dybå minimum of 3.0 (2.17 and 1.67). |
| P1272 | 2024 | A Multi-Faceted Approach to Measuring Engineering Productivity | **Productivity score calculator** (weighted metrics) as a self-assessment tool; only illustrative examples, **no empirical validation**. IJTSRD (predatory), 6 pp., few references. Below the minimum of 3.0. |
| P1329 | 2024 | AI-Augmented Developer Experience (DevEx) in DevOps | Document in **outline or bullet-point form** (74 '•' markers), **with no method, data, or sample** (method/participants/dataset/respondents = 0 times) and almost no references (2). The body is a schematic conceptual summary (I./A./B.), with no argumentative text or study. Single author ('Liam James'), no DOI, undefined venue; strong signs of AI-generated text. (Also FT-EC2, no evidence of its own.) |

## FT-EC4. Duplicate or overlap

| ID | Year | Title (short) | Reason for exclusion |
|----|------|---------------|----------------------|
| P0269 | 2018 | Fostering Productivity through Self-Monitoring | Overlap: doctoral symposium abstract whose content is in the full thesis (= P1282). |
| P1282 | 2019 | Fostering Software Developer Productivity (PhD thesis, Meyer) | Thesis by publication (UZH): chapter 2 = **P0249** (already included); full version of P0269 (already excluded). Excluded to avoid double counting. Citable as background (FlowLight/PersonalAnalytics). |
| P1308 | 2019 | Rethinking Productivity in Software Engineering (book, eds. Sadowski & Zimmermann) | **Edited book** (~25 multi-author chapters, 320 pp.): not a single primary study, and it cannot be scored coherently with Dybå and Dingsøyr. Several chapters duplicate evidence already in the corpus: Ch. 22–23 (Fitbit/self-monitoring; FlowLight) = Meyer's PersonalAnalytics/FlowLight (**P0249/P1282**); Ch. 14 on biometric sensors overlaps **P0144/P0145/P0179**; plus Ch. 10 on happiness and Ch. 5 on a framework (a precursor of SPACE). Excluded to avoid double counting; **kept as a strong background reference** (Sadowski & Zimmermann, 2019, "four lenses"), not as an entry of the corpus. |
| P1475 | (2018) | Using Qualitative System Dynamics… Agile Teamwork Productivity Model (Fatema/Sakib) | **Mislinked PDF**: the file 'P1475_2961111.2962626.pdf' actually contains the paper of **P1297** (Oliveira/Conte, 'Software Project Managers' Perceptions of Productivity Factors', ESEM 2016). The intended paper (Fatema & Sakib, IARIA Int'l J. on Advances in Software, 2018) **was not retrieved** for the corpus. The reviewer read the content of P1297; excluded as a duplicate of P1297 to avoid double counting. |
| P_NEW_1 | 2025 | Comparative Analysis… DORA, SPACE, HEART, and Beyond (Valiulla/Harness) | **Academic stub with a placeholder ID** that duplicates the SSRN report by Adeeb N. Valiulla (Harness), **already present in the gray literature as G073** (same file). Removed from the academic corpus and kept only as **G073 (gray)**. |
| P1818 | 2023 | Performance Measurement Framework for Agile Scrum (authors "Various") | **Ghost entry from the AI-generated version**: authors "Various", no human reading form; the linked PDF is the paper of **P0036** (Multi-Agent AI Framework, ICWITE 2025, already excluded). The title does not match the PDF; no verifiable source. Removed from the corpus. |

## FT-EC5. Language (IC5): full text in Portuguese (excluded at eligibility on 2026-08-31)

| ID | Year | Title (short) | Reason for exclusion |
|----|------|---------------|----------------------|
| P0478 | 2022 | Developers in focus! DX Analysis in a Collaborative Modeling Tool (SBES) | Body of the text in Portuguese; only the abstract in English. Violates IC5 (written in English). Verified by text extraction. |
| P0497 | 2023 | Assessing DX through affectivity and self-assessed productivity (SBQS) | Body of the text in Portuguese; only the abstract in English. Violates IC5. Verified by text extraction. |
| P0536 | 2023 | Hyacinth macaw: project-based learning program (SBES) | Body of the text in Portuguese; only the abstract in English. Violates IC5. Verified by text extraction. |

Record: the three were detected after coding (two of them flagged by the LLM layer of the selection simulation) and excluded by decision of the first author on 2026-08-31, which reduced the academic corpus of the original search from 69 to 66 sources.

---

### Summary
The search strings retrieved a substantial number of works on **DevEx, productivity, and AI** that, in the full text, (i) addressed another object (HPC, AIOps, technical debt, language quality, migration tools), (ii) brought no empirical evidence of their own (visions, plans, conceptual frameworks, study designs), (iii) did not reach the quality minimum, or (iv) were duplicates. This supports screening by full-text reading: relevance by keyword overestimates the effective corpus on the **measurement** of developer productivity.

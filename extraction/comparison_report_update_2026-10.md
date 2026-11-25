# Claude vs NotebookLM: search update of October 2026

Generated on 2026-10-05 by `extraction/scripts/compare_update_2026-10.py`. Translated from Portuguese.

Sources compared: 124 (96 academic, 28 gray). EC6 sources (full text not retrieved) were not extracted.

Same typology as the original report (`comparison_report.md`): exact_match, partial_match, divergent, only_claude, only_nlm, both_empty. The comparison is automatic and serves as support; the resolution is made by the reviewer against the full text, in the "Resolution (reviewer)" column of `comparison_update_2026-10.xlsx`. In the update, the fields on which the extractors diverged were resolved against the full text and recorded in the reading forms (`extraction/human_review/`), and this column was left empty.

Criteria: free text by word overlap (≥60% exact, ≥20% partial); frameworks as a set; DORA/SPACE/DevEx applied from the APPLIED marks; metrics by overlap of the names; quality with a tolerance of 2/12 (academic) and 1/6 (gray) for partial.

## Overall agreement

| Status | n | % |
|---|--:|--:|
| exact_match | 546 | 36.1% |
| partial_match | 447 | 29.6% |
| divergent | 331 | 21.9% |
| only_claude | 40 | 2.6% |
| only_nlm | 29 | 1.9% |
| both_empty | 119 | 7.9% |

## Agreement per field, academic sources

| Field | exact_match | partial_match | divergent | only_claude | only_nlm | both_empty | Agreement (exact+partial) |
|---|--:|--:|--:|--:|--:|--:|--:|
| study_type | 47 | 41 | 8 | 0 | 0 | 0 | 92% |
| method | 0 | 54 | 42 | 0 | 0 | 0 | 56% |
| sample | 0 | 26 | 70 | 0 | 0 | 0 | 27% |
| context | 3 | 41 | 52 | 0 | 0 | 0 | 46% |
| work_mode | 1 | 16 | 24 | 14 | 7 | 34 | 27% |
| process | 4 | 19 | 19 | 15 | 15 | 24 | 32% |
| frameworks_ref | 16 | 72 | 0 | 7 | 1 | 0 | 92% |
| frameworks_app | 23 | 2 | 0 | 4 | 6 | 61 | 71% |
| dora_applied | 93 | 0 | 3 | 0 | 0 | 0 | 97% |
| space_applied | 91 | 0 | 5 | 0 | 0 | 0 | 95% |
| devex_applied | 90 | 0 | 6 | 0 | 0 | 0 | 94% |
| ai_used | 63 | 0 | 33 | 0 | 0 | 0 | 66% |
| metrics | 47 | 45 | 4 | 0 | 0 | 0 | 96% |
| quality_total_12 | 15 | 38 | 43 | 0 | 0 | 0 | 55% |

## Agreement per field, gray sources

| Field | exact_match | partial_match | divergent | only_claude | only_nlm | both_empty | Agreement (exact+partial) |
|---|--:|--:|--:|--:|--:|--:|--:|
| gl_type | 2 | 17 | 9 | 0 | 0 | 0 | 68% |
| date | 11 | 16 | 1 | 0 | 0 | 0 | 96% |
| author | 11 | 17 | 0 | 0 | 0 | 0 | 100% |
| frameworks_ref | 19 | 9 | 0 | 0 | 0 | 0 | 100% |
| metrics | 7 | 21 | 0 | 0 | 0 | 0 | 100% |
| quality_gl_6 | 3 | 13 | 12 | 0 | 0 | 0 | 57% |

## Notes for the reading

- **ai_used:** the extractors read the field "Uses AI/ML?" differently. Claude marked "No" when the study does not use AI as a method, even when it deals with AI tools; NotebookLM marked "Yes" when the topic is AI. Most of the 33 divergences come from this. The human reading form uses "AI Discussed", which corresponds to the NotebookLM reading.
- **Free-text fields (method, sample, context, work_mode, process):** Claude wrote the content in Portuguese and NotebookLM in English, with citation markers. Word overlap underestimates the agreement in these fields; the same happened in the original report (study_type 27%, context 19% before resolution). The fields that matter for the synthesis are frameworks, DORA/SPACE/DevEx applied, metrics, and quality.
- **DORA/SPACE/DevEx applied:** 14 divergences in 9 sources (P2019, P2036, P2049, P2050, P2065, P2100, P2112, P2125, P2129). To check in the full text whether the framework is used as an instrument or only cited.
- **Quality:** the scores of the extractors are an audit layer. The score used in the study is the reviewer's (Dybå and Dingsøyr for academic sources, AACODS for gray sources).

## Divergences per source (to be resolved during reading)

| ID | Type | Divergent fields | Title |
|---|---|---|---|
| P2001 | academic | sample, ai_used | Leading GenAI-Accelerated Engineering Productivity |
| P2002 | academic | sample, context, quality_total_12 | Governance-Aware AI-Assisted Developer Productivity Evaluation in Hybr |
| P2003 | academic | sample, context, quality_total_12 | Enhancing Software Engineering Productivity Through AI-Scrum Framework |
| P2004 | academic | method, quality_total_12 | Adaptive AI Productivity Assistant for Developers in Visual Studio Cod |
| P2005 | academic | ai_used, quality_total_12 | Evaluating the Role of AI, Technology Used, and Technology Skill Profi |
| P2006 | academic | quality_total_12 | Digital Transformation in IT Project Management: The Impact of Cloud T |
| P2007 | academic | sample, context, quality_total_12 | A Systematic Literature Review on Intelligent Tools and the Developer  |
| P2008 | academic | study_type, sample, quality_total_12 | AI-Augmented Software Engineering for Rapid Feature Delivery and Opera |
| P2009 | academic | method, quality_total_12 | Beyond Correctness: Measuring Hallucination Impact in AI-Assisted Deve |
| P2010 | academic | study_type, method, sample, context, process | From AI Drag to AI Boost: A Preceptorship Framework for Developing Sof |
| P2011 | academic | sample | Unveiling the Drivers of Developer Satisfaction: Causal Inference Pers |
| P2012 | academic | study_type, sample, context, quality_total_12 | Productivity and Rework in AI-Assisted Front-End UI Development: A Wor |
| P2013 | academic | sample, work_mode | Abstracting Deployment Complexity with Platform Engineering Through Ce |
| P2014 | academic | study_type, process | BayesInsights: Modelling Software Delivery and Developer Experience wi |
| P2015 | academic | sample, context, ai_used | Adopting Concepts for Sustainable Improvement of the Developer Experie |
| P2017 | academic | method, sample, context | Beyond the Numbers: Evaluating DevOps Adoption in an Enterprise Softwa |
| P2018 | academic | sample, context, work_mode, ai_used | Examining Productivity in Educational Environments: Perspectives of Pr |
| P2019 | academic | method, sample, context, devex_applied | Developers’ Experience with Generative AI Beyond Productivity Assessme |
| P2022 | academic | method, context, process, quality_total_12 | Next Level: a maturity model in construction for the evolution of soft |
| P2023 | academic | sample, context, ai_used | Evolving with AI: A Longitudinal Analysis of Developer Logs |
| P2024 | academic | method, sample, process, quality_total_12 | WhatsCode: Large-Scale GenAI Deployment for Developer Efficiency at Wh |
| P2025 | academic | method, sample, context, work_mode | Code with Me or for Me? How Increasing AI Automation Transforms Develo |
| P2026 | academic | method, quality_total_12 | LLM-EMM: A Large Language Model--Driven Efficiency Measurement and Mod |
| P2027 | academic | method, sample, context, work_mode | Experimental Analysis of Productive Interaction Strategy with ChatGPT: |
| P2028 | academic | method, sample, context, work_mode | An Eye for AI: Eye-Tracking the Micro-Interruptions of GenAI Code Sugg |
| P2029 | academic | sample | Achieving Productivity Gains with AI-based IDE features: A Journey at  |
| P2030 | academic | sample, ai_used | From Gains to Strains: Modeling Developer Burnout with GenAI Adoption |
| P2031 | academic | method, sample, context, work_mode, process, ai_used | Understanding Task Enjoyment in Software Development: A Mixed-Methods  |
| P2032 | academic | sample, work_mode | Speed at the Cost of Quality: How Cursor AI Increases Short-Term Veloc |
| P2033 | academic | method, sample, quality_total_12 | Adoption of AI Assisted Coding – Cognitive Barriers, Motivational Fact |
| P2034 | academic | sample, ai_used | Generative AI and the Future of Professional Software Development: Sur |
| P2035 | academic | method, sample, context, ai_used, quality_total_12 | At What Cost? Software Developers’ Well-Being in the Age of GenAI |
| P2036 | academic | dora_applied, space_applied, devex_applied | AI IDEs or Autonomous Agents? Measuring the Impact of Coding Agents on |
| P2037 | academic | sample, context, work_mode, metrics | "Game Changer" or "Overenthusiastic Drunk Acquaintance"? Generative AI |
| P2038 | academic | method, sample, work_mode, ai_used | Understanding and Enhancing CS Students’ Interaction Experience with A |
| P2039 | academic | sample, process, ai_used | What Needs Attention? Prioritizing Drivers of Developers’ Trust and Ad |
| P2040 | academic | method, sample, context, work_mode | The Influence of Environmental Odors on Student Programmers During Cod |
| P2041 | academic | work_mode | Divergence or Convergence? A Deep Insight into the Crowd Collaboration |
| P2042 | academic | sample, context, ai_used, metrics | Towards an Appropriate Level of Reliance on AI: A Preliminary Reliance |
| P2043 | academic | work_mode | Strategic initiatives in DevOps adoption: a case study on the interpla |
| P2049 | academic | work_mode, space_applied, ai_used, quality_total_12 | Creating benchmarkable components to measure the quality of AI-enhance |
| P2050 | academic | method, context, work_mode, dora_applied, space_applied, devex_applied | Results from a Replicated Experiment on the Affective Reactions of Nov |
| P2052 | academic | study_type, method, sample, context, ai_used, quality_total_12 | Investigating the key factors influencing software developer productiv |
| P2056 | academic | method, sample, context, work_mode, process | Understanding developer well-being: measuring mental health and produc |
| P2059 | academic | method, sample, context, ai_used | Echoes of AI: Investigating the downstream effects of AI assistants on |
| P2060 | academic | method | Interruptibility of software developers and its prediction using psych |
| P2065 | academic | sample, context, process, devex_applied | Designing with Dev-X: A systematic mapping of Developer Experience int |
| P2067 | academic | study_type, method, sample, context, process, ai_used, quality_total_12 | MEASURING SOFTWARE DEVELOPER PRODUCTIVITY: REVIEW OF APPROACHES AND TH |
| P2068 | academic | sample | Software Developers' Perceptions of Productivity: An Industry-focused  |
| P2070 | academic | method, sample, quality_total_12 | PlatFab: A Platform Engineering Approach to Improve Developer Producti |
| P2073 | academic | sample, context, process, ai_used, quality_total_12 | Beyond Productivity Gains: Analyzing the Effects of AI-assisted Coding |
| P2074 | academic | context, process | Using development environment as code for enhancing developer experien |
| P2077 | academic | sample, context, quality_total_12 | Bridging the Gap: A Data-Driven Analysis of How Traditional Software E |
| P2078 | academic | method, sample, ai_used | Are We Measuring the Wrong Things? How Software Project Leaders View G |
| P2079 | academic | context, process, ai_used, metrics | Understanding ADHD Developers' Challenges Through the Lens of Develope |
| P2080 | academic | method, sample, ai_used, quality_total_12 | AI-assisted Collaboration: Exploring Developer Experience with GitHub  |
| P2081 | academic | sample, context, quality_total_12 | The Effect Of Visual Studio Code Usability Based On Nielsen's Attribut |
| P2083 | academic | method, sample, context, process, quality_total_12 | The Developer Experience of LGBTQIA+ People in Agile Teams: A Multivoc |
| P2085 | academic | sample, context, ai_used, quality_total_12 | The transformative influence of llms on software development \&develop |
| P2086 | academic | method, sample, ai_used, quality_total_12 | What Makes a Good Productivity Metric? |
| P2087 | academic | method, context, quality_total_12 | AI-Assisted Debugging Tools for Enhancing Developer Productivity in La |
| P2092 | academic | ai_used, quality_total_12 | Connecting Mental Health and Productivity: A Metric Catalog for Softwa |
| P2093 | academic | metrics | An actionable framework to investigate and foster women inclusion in s |
| P2094 | academic | sample, context, process | A dive into the state of parallel application development in high-perf |
| P2095 | academic | method, ai_used, quality_total_12 | AI-Assisted Software Testing Improvements |
| P2096 | academic | context, ai_used | Both personality and social identity predict perceived software team p |
| P2097 | academic | method, sample, context, quality_total_12 | Integrating Generative AI Across the Agile Software Development Lifecy |
| P2098 | academic | context, quality_total_12 | Multimodal Workload Analysis for Developer Burnout Prediction: Integra |
| P2099 | academic | study_type, method, context, work_mode, ai_used, quality_total_12 | Measuring productivity: All models are wrong, but some are useful |
| P2100 | academic | sample, dora_applied, space_applied | Beyond the Commit: Developer Perspectives on Productivity with AI Codi |
| P2101 | academic | context, process, ai_used | What's DAT? Three Case Studies of Measuring Software Development Produ |
| P2103 | academic | study_type, sample | No silver bullets: Why understanding software cycle time is messy, not |
| P2104 | academic | method, sample, context, process | Human-AI experience in integrated development environments: a systemat |
| G090 | grey | gl_type | Developer productivity with and without github copilot: A longitudinal |
| G092 | grey | date | The Impact of AI Coding Assistants on Software Engineering: A Longitud |
| G093 | grey | gl_type | Knowledge activation: AI skills as the institutional knowledge primiti |
| P2106 | academic | method, sample, process | A human-centered approach to developer productivity |
| P2107 | academic | method, sample, context, work_mode | Towards a theory of software developer job satisfaction and perceived  |
| P2108 | academic | sample, context, quality_total_12 | Developer productivity for humans, part 6: Measuring flow, focus, and  |
| P2109 | academic | method, sample, context | Visualizing interaction data inside &outside the ide to characterize d |
| P2111 | academic | method, sample, ai_used, quality_total_12 | Productivity Factors in Agile Software Development Projects |
| P2112 | academic | sample, work_mode, devex_applied, ai_used, quality_total_12 | Measuring developer experience with a longitudinal survey |
| P2113 | academic | work_mode, quality_total_12 | Developer productivity for humans, part 8: Creativity in software engi |
| P2114 | academic | sample, quality_total_12 | The effect of knowledge work productivity factors on software developm |
| P2115 | academic | sample, context, work_mode, quality_total_12 | Software development teams: factors influencing their productivity |
| P2116 | academic | process | Developer Thriving: four sociocognitive factors that create resilient  |
| P2119 | academic | sample, work_mode, quality_total_12 | Factors influencing productivity of agile software development teamwor |
| P2120 | academic | sample, context | Surveying the developer experience of flaky tests |
| P2122 | academic | method, sample, context | Productivity, turnover, and team stability of agile teams in open-sour |
| P2124 | academic | method, sample, context, ai_used, quality_total_12 | … Software Engineering Tasks: The Software Evaluation for Well-Being a |
| P2125 | academic | sample, devex_applied, quality_total_12 | Developer productivity for humans, part 2: Hybrid productivity |
| P2126 | academic | sample, context, ai_used, quality_total_12 | Analysis of factors influencing developers' sentiments in commit logs: |
| P2128 | academic | sample | On software productivity analysis with propensity score matching |
| P2129 | academic | method, sample, space_applied, ai_used, quality_total_12 | Copilot's island of joy: balancing individual satisfaction with team i |
| P2130 | academic | method, sample, context, process | How human and organizational factors influence software teams producti |
| P2131 | academic | method, sample, context, work_mode | Significant productivity gains through programming with large language |
| P2132 | academic | method, sample, context, work_mode, ai_used | A tale of two cities: Software developers working from home during the |
| P2133 | academic | sample, context, work_mode | Reading between the lines: Modeling user behavior and costs in AI-assi |
| P2134 | academic | quality_total_12 | Taking flight with copilot |
| G097 | grey | gl_type | Evaluating the Use of Generative AI in Software Development Proposing  |
| G100 | grey | quality_gl_6 | AI measurement framework: Complete guide for engineering leaders |
| G101 | grey | gl_type, quality_gl_6 | AI in engineering: Q2 2026 benchmarks and research readout |
| G103 | grey | gl_type, quality_gl_6 | The AI engineering productivity gap: 2026 benchmarks |
| G105 | grey | quality_gl_6 | AI Accountability Report |
| G106 | grey | quality_gl_6 | New modes of delivering software, a new Gartner Magic Quadrant, and a  |
| G107 | grey | quality_gl_6 | AI Is Amplifying Software Engineering Performance, Says the 2025 DORA  |
| G108 | grey | gl_type, quality_gl_6 | The struggle to prove AI productivity gains |
| G109 | grey | gl_type, quality_gl_6 | AI isn't making developers more productive, it's making them busier |
| G110 | grey | gl_type | Measuring engineering productivity is harder than ever |
| G111 | grey | quality_gl_6 | The AI Impact Report 2026 |
| G112 | grey | gl_type, quality_gl_6 | The AI revolution in software development |
| G113 | grey | quality_gl_6 | AI's impact on software engineers in 2026: key trends, Part 2 |
| G114 | grey | quality_gl_6 | How tech companies measure the impact of AI on software development |

Sources with no divergent field (11): G082, G084, G086, G087, G091, G096, G098, G099, G102, G104, G115


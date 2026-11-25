# G097 — Evaluating the Use of Generative AI in Software Development Proposing a Tentative Framework

**Decisao: INCLUIDO | Qualidade GL: 6/6**

---

## Dados Bibliograficos

| Campo | Valor |
|-------|-------|
| **ID** | G097 [1] |
| **Autor/Organizacao** | Linnea Arkheden, Sara Eklund / Chalmers University of Technology [1, 2] |
| **Data** | June 2024 [1, 3] |
| **Tipo** | Master's thesis / Academic report [1] |
| **URL** | N/A (Not available in source) [1] |

---

## Resumo

This Master's thesis investigates the integration and evaluation of generative AI (GenAI) within software development through an in-depth qualitative single-case study conducted at Zenseact, an autonomous driving software company [4-7]. The study addresses two primary research questions: exploring how software industry employees across various departments perceive the opportunities and challenges of GenAI, and determining how the use of GenAI in software engineering can be systematically evaluated [5, 8-10]. Data collection relied on semi-structured interviews with 27 employees in technical, support, and leadership roles [5, 11, 12].

The empirical findings reveal a broadly positive attitude toward embracing GenAI to transform workflows, alongside noticeable skepticism and caution [5, 13-15]. Senior developers and deep learning specialists exhibited higher skepticism due to their technical awareness of model limitations, subtle code bugs, and safety-critical risks associated with self-driving vehicle software [15-19]. Key opportunities highlighted by respondents include automating repetitive tasks (such as email sorting, summarizing meeting notes, and generating boilerplate text/code), accelerating information retrieval, and facilitating learning [5, 20-23]. Major challenges center on technological flaws (AI hallucinations, poor output quality, "black box" logic), IP and data privacy concerns, and potential developer job dissatisfaction if tasks shift primarily toward debugging AI-generated code [5, 17, 18, 24-28].

To systematically evaluate GenAI adoption, the study proposes a tentative survey-based evaluation framework adapting principles from UTAUT, DevEx, and SPACE [29-32]. The authors emphasize that developer productivity evaluation must combine qualitative perception metrics (satisfaction, cognitive load, flow state) with quantitative tracking (estimated weekly time savings, bug rates, usage frequency) [5, 30, 33-35]. Critically, the study highlights that because writing code accounts for only ~5% of developer time while code comprehension occupies up to 70%, organizations and researchers should focus GenAI evaluation and implementation on code comprehension, documentation, and operational efficiency rather than code generation alone [36-39].

---

## Frameworks Mencionados

- **SPACE Framework**: Discussed and recommended [30, 32, 34, 40-44]. Utilized as a multidimensional model to measure developer productivity across five dimensions (Satisfaction and well-being, Performance, Activity, Communication and collaboration, Efficiency and flow) [41, 45]. Adapted into specific survey statements to evaluate GenAI outcomes [30, 34, 46].
- **DevEx (Developer Experience)**: Discussed and recommended [32-34, 40, 42, 47, 48]. Focuses on developer friction and job satisfaction across three core dimensions: Feedback Loops, Cognitive Load, and Flow State [47, 48]. Integrated with SPACE to assess how GenAI affects mental effort and deep focus [33, 34].
- **UTAUT (Unified Theory of Acceptance and Use of Technology)**: Discussed and recommended [29, 31, 32, 40, 49-51]. Used to structure user adoption factors, including performance expectancy, effort expectancy, social influence, facilitating conditions, and user attitudes toward GenAI tools [31, 32, 50-52].
- **TOE (Technology-Organization-Environment) Framework**: Discussed [40, 49, 52-56]. Used in the theoretical background to analyze technological usability/complexity, organizational culture and resources, and environmental regulatory/competitive drivers [52-54, 56].
- **SDLC (Software Development Life Cycle)**: Discussed [39, 55, 57-60]. Examined across planning, requirements analysis, design, development, testing, installation, and maintenance phases [58-60].
- **DORA Framework**: Critiqued/Noted in literature references [61]. Mentioned in cited literature (Witczak 2023) as a complementary metric model alongside SPACE and DevEx [61].

---

## Metricas Mencionadas

- **Time Savings / Saved Hours per Week**: Estimated weekly hours saved or freed up by developers using GenAI tools [5, 30, 62-64].
- **Lines of Code (LOC)**: Discussed and critiqued [63, 65]. Dismissed as an uninformative metric because it fails to capture code quality, complexity, or value delivered [63, 65].
- **Number of Commits / Story Points Shipped / Pull Requests**: Mentioned under the SPACE Activity dimension and developer performance tracking [45, 46, 50, 63].
- **Bug Frequency / Number of Subtle Bugs Introduced**: Identified under the SPACE Performance dimension and qualitative developer evaluations regarding AI code reliability [17, 30, 45, 63].
- **Code Review Velocity and Score**: Mentioned as example metrics within individual and team levels of SPACE [50].
- **Code Comprehension Time vs. Coding Time**: Highlighted as key contextual distribution metrics (coding accounts for ~5% of time, while code comprehension accounts for ~70%) [36-39].
- **User Satisfaction & Well-being Scores**: Measured via survey Likert scales assessing job enjoyment, stress reduction, and confidence [34, 45, 46, 66, 67].
- **User Adoption Rate**: Percentage of frequent users (using tools at least once a week) versus infrequent users [64, 68, 69].

---

## Insights para Praticantes

- **Focus Beyond Pure Code Generation**: Recognize that writing code represents only ~5% of developer time, whereas code comprehension occupies up to 70% [36-39]. Management should direct GenAI initiatives toward making codebases easier to understand, generating documentation, and automating operational administrative tasks [36-38, 70].
- **Balance Top-Down Strategy with Team Autonomy**: Combine central strategic guidelines and license provision with team-level freedom to discover local use cases [70, 71]. Establish internal knowledge-sharing platforms (e.g., "knowledge boosts" or dedicated chat channels) to share success stories across departments [71, 72].
- **Conduct Continuous Qualitative and Quantitative Evaluations**: Implement periodic surveys (e.g., quarterly) based on DevEx, SPACE, and UTAUT to track developer perception, adoption rates, barriers, and perceived impact over time [30, 31, 35, 66, 67, 72].
- **Establish Verification Processes for Safety and IP**: Formulate clear guidelines and code validation protocols to catch subtle AI-generated bugs, especially in safety-critical domains like autonomous driving [5, 16-18, 27, 28].
- **In-House Fine-Tuning for Data Privacy**: Address security concerns and domain-specific knowledge gaps by training or fine-tuning internal GenAI tools on proprietary data rather than relying solely on public external models [7, 73-75].

---

## Avaliacao de Qualidade GL (Garousi et al.)

| Criterio | Pontuacao (0-1) |
|----------|----------------|
| Autoridade do autor/organizacao | 1.0 [1, 2] |
| Descricao de metodologia | 1.0 [5, 6, 11, 12, 76] |
| Data de publicacao | 1.0 [1, 3] |
| Objetividade (vies comercial) | 1.0 [5, 15, 28, 77] |
| Referencias citadas | 1.0 [40, 78-82] |
| Contribuicao nova | 1.0 [30-33] |
| **TOTAL** | **6.0/6** [1, 5, 31, 32] |

---

*Extraido via NotebookLM em October 2026 para MLR: Software Developer Metrics in Practice*

---

📊 Would you like me to synthesize these findings with other grey literature or academic sources in your notebook to build a comparative analysis table?
# P1365 — What Impact do AI/LLM Tools have on Developer Experience?

**Decisao: INCLUIDO | Qualidade: 5/5**

---

## Dados Bibliograficos

| Campo | Valor |
|-------|-------|
| **ID** | P1365 |
| **Autores** | Nico Hartto [1] |
| **Ano** | 2025 [1] |
| **Venue** | Lappeenranta-Lahti University of Technology LUT (Master's Thesis) [1] |
| **DOI** | Not available [2, 3] |
| **Tipo** | Master's Thesis [1, 4] |
| **Metodo** | Mixed methods (Qualitative interviews and Quantitative survey) [5, 6] |
| **Amostra** | 9 software engineering professionals (interviews) and 92 survey respondents [5, 7] |
| **Contexto** | Industry — Solita Oy (Digital transformation partner in the Nordics and Europe) [8, 9] |
| **Modo de trabalho** | Not specified (Interviews conducted in person and over Microsoft Teams) [10] |
| **Metodologia** | Not specified (Mentions SDLC and general development practices) [11-13] |

---

## Objetivo

O principal objetivo deste trabalho é investigar como as ferramentas de **Artificial Intelligence (AI)** e **Large Language Models (LLM)** influenciam a **Developer Experience (DevEx)**, focando especificamente em dimensões como **flow state**, **cognitive load**, **feedback loops** e colaboração em equipe [4, 14, 15]. O estudo busca fornecer um "snapshot" de como essas tecnologias estão remodelando o trabalho diário dos desenvolvedores em uma organização de grande porte [16, 17].

---

## Questoes de Pesquisa

- **RQ1:** How do AI/LLM tools influence the speed and quality of feedback loops in software development? [18, 19]
- **RQ2:** How does the use of AI/LLM tools impact developers’ ability to achieve and maintain a flow state? [20, 21]
- **RQ3:** How does the adoption of AI/LLM tools influence the cognitive load experienced by software developers? [20, 21]
- **RQ4:** How do AI/LLM tools alter communication and collaboration among teams? [20, 21]

---

## Metricas e Instrumentos de Avaliacao

| Metrica | Categoria | Nivel | Como Coletada | Validada |
|---------|-----------|-------|---------------|----------|
| **Feedback loops** (Speed/Quality) | DevEx | Individual | Likert scale survey [22, 23] | Yes (DevEx Framework) [17, 24] |
| **Flow state** (Concentration) | DevEx | Individual | Likert scale survey [25, 26] | Yes (DevEx Framework) [17, 24] |
| **Cognitive load** (Mental effort) | DevEx | Individual | Likert scale survey [27, 28] | Yes (DevEx Framework) [17, 24] |
| **Team Collaboration** | Collaboration | Team | Likert scale survey [29, 30] | Yes (Reference to SPACE) [31] |
| **Job Satisfaction/Enjoyment** | Satisfaction | Individual | Likert/Open-ended questions [26, 32, 33] | Yes [32] |
| **Sense of Accomplishment** | Satisfaction | Individual | Likert scale survey [28, 34] | Yes [34] |

---

## Frameworks e Metricas

### Frameworks Referenciados
- **DevEx Framework (Noda et al. 2023):** APPLIED — Usado como base teórica principal e instrumento de medição das dimensões centrais [17, 24, 35].
- **DORA Metrics:** REFERENCED — Discutido em relação à performance organizacional, mas não aplicado diretamente como métrica de resultado [14, 36, 37].
- **SPACE Framework:** REFERENCED — Citado como abordagem holística para produtividade e colaboração [8, 36, 38].
- **Actor-Network Theory (ANT):** REFERENCED — Usado para discutir a paridade entre ferramentas e humanos no processo de desenvolvimento [39-41].

### Frameworks Propostos
O trabalho não propõe um novo framework, mas discute o **Solita CollabAI** como um método emergente para desenvolvimento baseado em IA em equipe [42, 43].

---

## Fatores que Influenciam Produtividade

### Fatores Positivos
| Fator | Categoria |
|-------|-----------|
| Reduced mental effort on routine decisions and tasks [27, 44] | Human/Technical |
| Efficient evaluation of multiple potential solutions [45] | Technical/Process |
| Reduced need to remember specific syntax and documentation [46] | Technical |
| Immediate in-context guidance minimizing back-and-forth [47] | Technical/Process |
| Increased enjoyment and professional satisfaction [32, 33] | Human |

### Fatores Negativos
| Fator | Categoria |
|-------|-----------|
| **Hallucinations** and lack of trust in AI output [48, 49] | Technical/Human |
| **Stochastic nature** leading to inconsistent results [35, 49] | Technical |
| **Context window** limitations and outdated models (knowledge cutoff) [50] | Technical |
| Churn from switching between applications (chat-based approach) [47] | Process |
| Effort required to verify and review AI-generated code [35, 44] | Process/Human |

---

## Papel da IA e Automacao

| Campo | Valor |
|-------|-------|
| Usa IA/ML? | Yes — O estudo avalia ferramentas como **ChatGPT**, **GitHub Copilot**, **Claude** e **Cursor** no fluxo de trabalho [51-53]. |
| Automacao de coleta? | No — Os dados foram coletados manualmente via entrevistas estruturadas e questionários (Microsoft Forms) [7, 10, 54]. |
| Impacto de IA na produtividade? | Positivo no fluxo individual (aceleração de iterações e redução de carga cognitiva), mas inconclusivo ou mínimo na colaboração de equipe e design de alto nível [35, 55, 56]. |

---

## Resultados Principais

- **Uso Frequente:** A maioria dos profissionais (57,6%) utiliza ferramentas de IA diariamente ou quase diariamente [57].
- **Carga Cognitiva:** 91,3% dos respondentes concordam que a IA reduz a necessidade de memorizar sintaxes específicas ou documentação [46, 58].
- **Feedback Loops:** 56,4% concordam que podem avaliar múltiplas soluções de forma mais eficiente com apoio de IA [45].
- **Qualidade:** 60,9% sentem que a IA melhora a qualidade do trabalho logo no início do processo de desenvolvimento [59].
- **Satisfação:** O uso de IA não diminui o senso de realização; 79,4% ainda sentem realização pessoal ao usar ferramentas de assistência [34].
- **Colaboração:** A IA ainda não altera radicalmente o entendimento compartilhado ou a comunicação dentro das equipes (47,8% discordam que a IA reduz mal-entendidos) [35, 60].
- **Design e Arquitetura:** Ferramentas atuais são percebidas como limitadas para decisões de arquitetura e design de software de alto nível [56].

---

## Desafios do Uso das Metricas

- **Subjectividade:** A produtividade e a experiência do desenvolvedor são inerentemente humanas e difíceis de capturar apenas com métricas "proxy" [54, 61, 62].
- **Natureza Estocástica:** A inconsistência das respostas da IA dificulta a criação de fluxos de trabalho previsíveis e confiáveis [35, 49].
- **Trial and Error:** O fluxo de trabalho de "tentativa e erro" pode criar loops negativos que consomem tempo excessivo em correções [63, 64].
- **Context Management:** A dificuldade em manter o contexto adequado nas ferramentas prejudica a precisão do feedback imediato [65, 66].

---

## Avaliacao de Qualidade Metodologica

| Criterio | Pontuacao (0-2) |
|----------|----------------|
| Objetivo claramente definido | 2 [14, 54] |
| Metodologia adequada ao objetivo | 2 [6, 17] |
| Amostra/contexto descrito adequadamente | 2 [9, 67] |
| Ameacas a validade discutidas | 2 [11, 68] |
| Resultados com evidencia suficiente | 2 [Chapter 4 results] |
| Contribuicao clara para pratica ou teoria | 2 [62, 69] |
| **TOTAL** | **12/12** |

---

## Limitacoes

- **Contexto Organizacional Único:** O estudo foi focado quase exclusivamente na Solita Oy, limitando a generalização para outros tipos de empresas (como empresas de produto SaaS) [68, 70].
- **Viés de Experiência:** A amostra foi composta majoritariamente por profissionais seniores (80,4% com mais de 6 anos de experiência), o que pode não representar a visão de desenvolvedores juniores [68, 71, 72].
- **Snapshot Temporal:** Dada a velocidade da evolução da IA, os resultados refletem apenas um momento específico e podem tornar-se datados rapidamente [67, 69, 73].
- **Limitação Geográfica:** As entrevistas qualitativas iniciais envolveram apenas profissionais da Finlândia [74].

---

## Contribuicao Principal

A principal contribuição desta tese é fornecer evidências empíricas de que ferramentas de **AI/LLM** impactam positivamente as dimensões individuais da **Developer Experience** (especialmente na redução da carga cognitiva e aceleração de feedback loops), enquanto identifica que essas ferramentas ainda não transformaram significativamente a colaboração em equipe ou a resolução de problemas arquiteturais complexos [35, 55, 69].

---

*Extraido via NotebookLM em March 2026 para MLR: Software Developer Metrics in Practice*
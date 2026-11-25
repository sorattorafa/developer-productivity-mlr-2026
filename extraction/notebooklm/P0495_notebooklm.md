# P0495 — Human-AI Collaboration in Software Development: A Mixed-Methods Study of Developers’ Use of GitHub Copilot and ChatGPT

**Decisao: INCLUIDO | Qualidade: 5/5**

---

## Dados Bibliograficos

| Campo | Valor |
|-------|-------|
| **ID** | P0495 |
| **Autores** | Viktoria Stray, Astri Barbala, Viggo Tellefsen Wivestad [1] |
| **Ano** | 2025 [2] |
| **Venue** | 33rd ACM International Conference on the Foundations of Software Engineering (FSE Companion ’25) [2] |
| **DOI** | https://doi.org/10.1145/3696630.3730566 [3] |
| **Tipo** | Conference paper (Research-article) [1, 3] |
| **Metodo** | Mixed methods (Interviews and Survey) [4, 5] |
| **Amostra** | **13 practitioners** (interviews) and **114 survey respondents** (67 users and 47 non-users) [4-6] |
| **Contexto** | Public sector organization in Norway ("GovTech") responsible for social welfare and labor services [4, 7] |
| **Modo de trabalho** | Remote and co-located [8, 9] |
| **Metodologia** | Agile Software Development [3, 10] |

---

## Objetivo

O objetivo principal deste estudo é investigar como os desenvolvedores de software interagem com ferramentas de **Generative AI (GenAI)**, especificamente **GitHub Copilot** e **ChatGPT**, em uma organização do setor público de grande escala [4]. A pesquisa explora os fatores individuais, tecnológicos e sociais que influenciam a adoção dessas ferramentas e seu impacto nos fluxos de trabalho, colaboração e produtividade dos engenheiros [4, 5].

---

## Questoes de Pesquisa

*   **RQ1:** What influences the adoption of Generative AI tools among software engineers in a large-scale public sector organization? [11]

---

## Metricas e Instrumentos de Avaliacao

| Metrica | Categoria | Nivel | Como Coletada | Validada |
|---------|-----------|-------|---------------|----------|
| **Job satisfaction** | Satisfaction | Individual | Survey (Likert scale) [6, 12] | Yes (Adapted from GitHub Research) [6] |
| **Perceived Productivity** | Productivity | Individual | Survey (Likert scale) [6, 12] | Yes (Adapted from SPACE framework) [6] |
| **Flow** | DevEx | Individual | Survey (Likert scale) [12, 13] | Yes [6] |
| **Focus on satisfying work** | DevEx | Individual | Survey (Likert scale) [12, 14] | Yes [6] |
| **Frustration during coding** | DevEx | Individual | Survey (Likert scale) [12] | Yes [6] |
| **Dependency on colleagues** | Collaboration | Team | Survey (Likert scale) [12, 15] | Yes [6] |

---

## Frameworks e Metricas

### Frameworks Referenciados
*   **HACAF (Human-AI Collaboration and Adaptation Framework):** **APPLIED** — Central theoretical model used to analyze the adoption dimensions [4, 16-18].
*   **SPACE:** **APPLIED** — Used as the basis for the survey items to evaluate developer productivity [6, 19].
*   **TAM (Technology Acceptance Model):** **REFERENCED** — Integrated into HACAF to discuss perceived usefulness and ease of use [13, 16, 20].
*   **DOI (Diffusion of Innovations):** **REFERENCED** — Used to explain adoption rates among different developer categories [20-22].
*   **UTAUT (Unified Theory of Acceptance and Use of Technology):** **REFERENCED** — Discussed in the context of user intentions and social factors [20, 21].

### Frameworks Propostos
O artigo não propõe um novo framework, mas utiliza e sugere refinamentos para o **HACAF**, recomendando a inclusão de dimensões éticas em modelos futuros [9, 23].

---

## Fatores que Influenciam Produtividade

### Fatores Positivos
| Fator | Categoria |
|-------|-----------|
| **Automation of repetitive/boilerplate tasks** | Technical [24, 25] |
| **Enhanced ability to focus on satisfying work** | Human/Process [13, 14] |
| **Faster information and knowledge retrieval** | Technical [11, 26] |
| **Collective team adoption and shared learning** | Social/Organizational [15, 27] |

### Fatores Negativos
| Fator | Categoria |
|-------|-----------|
| **Time investment to learn prompting/tools** | Process [24, 28] |
| **Concerns about over-reliance and skill loss** | Human [13, 29, 30] |
| **Unclear organizational rules and regulations** | Organizational [31, 32] |
| **Friction in pair programming/collaboration** | Social [27] |

---

## Papel da IA e Automacao

| Campo | Valor |
|-------|-------|
| Usa IA/ML? | **Yes** — The study focuses on **GitHub Copilot** (autocomplete/IDE integrated) and **ChatGPT** (conversational) [4, 11]. |
| Automacao de coleta? | **No** — Data was collected through qualitative interviews and manual surveys [6, 33]. |
| Impacto de IA na produtividade? | **Positive** — Users reported higher satisfaction (87% vs 73%) and a significantly better ability to focus on satisfying work [13, 14, 25]. |

---

## Resultados Principais

*   **70% dos usuários** de IA relataram uma maior capacidade de focar em tarefas satisfatórias, em comparação com apenas 50% dos não usuários [14].
*   Usuários de GenAI expressaram **maior satisfação no trabalho (87%)** do que não usuários (73%) [25].
*   Houve uma **redução significativa na dependência de colegas** entre os usuários (45% afirmam não depender de ajuda, contra 20% dos não usuários) [8, 15].
*   A adoção é influenciada pela **experiência**: desenvolvedores seniores tendem a ser mais cautelosos e críticos, enquanto juniores veem a IA como essencial para competitividade e aprendizado [18, 34, 35].
*   **Fatores de compatibilidade**, como a integração com a IDE (ex: VS Code), são facilitadores críticos para a adoção [28, 36].

---

## Desafios do Uso das Metricas

*   **Self-selection bias:** Dificuldade em isolar se a alta satisfação vem do uso da ferramenta ou se usuários satisfeitos tendem a adotar novas ferramentas [25].
*   **Dificuldade de medição:** Desenvolvedores mencionaram que é difícil medir o impacto real da economia de tempo no dia a dia [24].
*   **Conflito com métricas qualitativas:** A percepção de "velocidade" da IA pode mascarar problemas de qualidade de código a longo prazo [37, 38].

---

## Avaliacao de Qualidade Metodologica

| Criterio | Pontuacao (0-2) |
|----------|----------------|
| Objetivo claramente definido | 2 |
| Metodologia adequada ao objetivo | 2 |
| Amostra/contexto descrito adequadamente | 2 |
| Ameacas a validade discutidas | 2 |
| Resultados com evidencia suficiente | 2 |
| Contribuicao clara para pratica ou teoria | 2 |
| **TOTAL** | **12/12** |

---

## Limitacoes

*   O estudo foi realizado em uma **única organização do setor público**, o que pode limitar a generalização para empresas privadas ou outros contextos [7, 39].
*   Potencial **viés de autoatribuição** (self-selection bias) nos resultados da pesquisa quantitativa sobre satisfação [25].
*   Dependência de **percepções subjetivas** (self-reported data) para produtividade e satisfação em vez de métricas de repositório objetivas [6, 13].

---

## Contribuicao Principal

O estudo fornece uma análise empírica detalhada da adoção de IA generativa em um contexto organizacional complexo, validando o framework **HACAF** [4, 18]. A contribuição principal reside na identificação de que a adoção bem-sucedida não é apenas técnica, mas depende fortemente de **fatores sociais (normas da equipe)** e **individuais (experiência e atitudes éticas)**, destacando o papel transformador da IA na redução da necessidade de colaboração constante entre pares [15, 18].

---

*Extraido via NotebookLM em March 2026 para MLR: Software Developer Metrics in Practice*
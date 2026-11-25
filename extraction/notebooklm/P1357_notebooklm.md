# P1357 — Developer Experience (DX): A Comparative Analysis of Streamlit, Chainlit, and Gradio

**Decisao: INCLUIDO | Qualidade: 5/5**

---

## Dados Bibliograficos

| Campo | Valor |
|-------|-------|
| **ID** | P1357 |
| **Autores** | Muhammad Zain Naeem [1] |
| **Ano** | 2025 [1] |
| **Venue** | LAB University of Applied Sciences [1] |
| **DOI** | Not specified [2-19] |
| **Tipo** | Thesis (Bachelor of Business Administration) [1, 20] |
| **Metodo** | Quantitative and deductive research design involving a practical experiment and Static code analysis [21-23] |
| **Amostra** | Three functionally identical chatbots [22, 24] |
| **Contexto** | Academic — developed as a Bachelor's thesis focusing on Python-centric libraries for AI [1, 21] |
| **Modo de trabalho** | Not specified (conducted on a personal computer) [25] |
| **Metodologia** | Not specified [21] |

---

## Objetivo

O objetivo principal deste trabalho é realizar uma avaliação quantitativa dos frameworks Streamlit, Gradio e Chainlit baseada na Developer Experience (DX) [20]. O estudo busca preencher uma lacuna no conhecimento acadêmico, fornecendo uma análise baseada em métricas para diferenciar essas ferramentas na implementação de Conversational User Interfaces (CUIs) [26, 27].

---

## Questoes de Pesquisa

*   **RQ1:** How do Streamlit, Gradio, and Chainlit compare in terms of Developer Experience (DX) when implementing a standardized chatbot? [28]
*   **RQ2:** How do the frameworks differ in code complexity and implementation effort? [28]

---

## Metricas e Instrumentos de Avaliacao

| Metrica | Categoria | Nivel | Como Coletada | Validada |
|---------|-----------|-------|---------------|----------|
| Halstead’s Program Volume (V) | Quality / DevEx | Individual | Static code analysis via `multimetric` library [24, 29] | Yes (Hariprasad et al. 2017) [30, 31] |
| Halstead’s Difficulty (D) | Quality / DevEx | Individual | Static code analysis via `multimetric` library [24, 29] | Yes (Hariprasad et al. 2017) [31, 32] |
| Halstead’s Effort (E) | Productivity / DevEx | Individual | Static code analysis via `multimetric` library [24, 29] | Yes (Hariprasad et al. 2017) [31, 33] |
| McCabe’s Cyclomatic Complexity (CC) | Quality / DevEx | Individual | Static code analysis via `multimetric` library [24, 29] | Yes (Ikerionwu 2010) [34] |
| Lines of Code (LOC) | Activity | Individual | Discussed/Excluded [35, 36] | Yes (Bhatt et al. 2012) [37] |
| Maintainability Index (MI) | Quality | Individual | Discussed/Excluded [38, 39] | Yes (Welker 2001) [38] |

---

## Frameworks e Metricas

### Frameworks Referenciados
*   **Developer Experience (DX) Framework (Fagerholm & Münch 2012):** APPLIED — Usado para relacionar os achados quantitativos com as dimensões de cognição e fluxo [40-42].
*   **SPACE Framework (Forsgren et al., 2021):** REFERENCED — Revisado mas não selecionado por focar mais em produtividade de equipe do que no indivíduo [43, 44].

### Frameworks Propostos
O artigo não propõe um novo framework de medição, mas utiliza uma árvore de decisão (Decision Tree) para auxiliar desenvolvedores na escolha do framework Python mais adequado com base em seus objetivos e complexidade do projeto [45].

---

## Fatores que Influenciam Produtividade

### Fatores Positivos
| Fator | Categoria |
|-------|-----------|
| Declarative design (Gradio) | Technical [46, 47] |
| Event-driven design (Chainlit) | Technical [46, 47] |
| Lower mental workload | Human [45, 48] |
| Built-in functionality for state management | Technical [34, 49] |

### Fatores Negativos
| Fator | Categoria |
|-------|-----------|
| Structural complexity (high Cyclomatic Complexity) | Technical [50, 51] |
| Script-based/Imperative architecture (Streamlit) | Technical [42, 52, 53] |
| Manual session state management | Technical [34, 53] |
| High cognitive load/Mental effort | Human [50, 54] |

---

## Papel da IA e Automacao

| Campo | Valor |
|-------|-------|
| Usa IA/ML? | Yes — utiliza o Gemini-2.5-flash LLM via API para o backend dos chatbots [55]. |
| Automacao de coleta? | Yes — a coleta de dados foi automatizada usando a biblioteca de análise estática `multimetric` [29, 56]. |
| Impacto de IA na produtividade? | O autor utilizou ChatGPT para edição de linguagem e melhoria de clareza em seções específicas da tese [1, 57]. |

---

## Resultados Principais

*   **Gradio** oferece a melhor Developer Experience para chatbots padrão, exigindo quase **66% menos esforço mental** (Effort: 13639.88) que o Streamlit [52, 54].
*   **Streamlit** apresentou os maiores índices de dificuldade (**26.34**) e carga cognitiva devido à sua arquitetura baseada em scripts que exige gestão manual de estado [52-54].
*   **Chainlit** obteve a menor complexidade estrutural (**Cyclomatic Complexity: 4**), tornando-o ideal para aplicações escaláveis [52, 58, 59].
*   O Volume do programa no Streamlit (1533.14) é quase o dobro do Gradio (879.23), indicando maior carga visual para o desenvolvedor processar [42, 58, 60].

---

## Desafios do Uso das Metricas

*   **Lines of Code (LOC)** e **Maintainability Index (MI)** foram excluídos por não capturarem o esforço mental e a carga cognitiva real do desenvolvedor [36].
*   A escolha de frameworks baseada em marketing subjetivo em vez de dados objetivos [20].
*   Risco de viés de proficiência, mitigado pelo autor ao certificar que não tinha experiência prévia com nenhum dos frameworks [61, 62].

---

## Avaliacao de Qualidade Metodologica

| Criterio | Pontuacao (0-2) |
|----------|----------------|
| Objetivo claramente definido | 2 [20, 26] |
| Metodologia adequada ao objetivo | 2 [21-23] |
| Amostra/contexto descrito adequadamente | 2 [1, 25, 29, 55, 63, 64] |
| Ameacas a validade discutidas | 2 [61, 62, 65] |
| Resultados com evidencia suficiente | 2 [58, 66] |
| Contribuicao clara para pratica ou teoria | 2 [27, 47] |
| **TOTAL** | **12/12** |

---

## Limitacoes

*   O estudo utilizou apenas um "minimum viable chatbot", não testando complexidades de aplicações empresariais de larga escala [65].
*   O autor foi o único desenvolvedor (sole developer), o que limita a diversidade de perfis de experiência [61, 62].
*   Foco exclusivo em métricas de código, omitindo elementos humanos subjetivos como qualidade da documentação e suporte da comunidade [65, 67].
*   A ausência de dados qualitativos (surveys ou entrevistas) para validar se as métricas correspondem à percepção humana [68].

---

## Contribuicao Principal

A principal contribuição é a análise comparativa rigorosa e baseada em métricas de software (Halstead e McCabe) que demonstra objetivamente como a arquitetura de um framework (declarativa, imperativa ou orientada a eventos) impacta diretamente a carga cognitiva e a experiência do desenvolvedor [27, 47, 69]. O estudo conclui que frameworks de "baixo código" (low-code) como Gradio são superiores para prototipagem rápida, enquanto Chainlit oferece maior estabilidade estrutural para projetos de longo prazo [45, 47].

---

*Extraido via NotebookLM em March 2026 para MLR: Software Developer Metrics in Practice*
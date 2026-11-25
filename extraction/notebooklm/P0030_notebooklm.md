# P0030 — Measuring AI Impact on Software Engineering Productivity and Quality

**Decisao: INCLUIDO | Qualidade: 4/5**

---

## Dados Bibliograficos

| Campo | Valor |
|-------|-------|
| **ID** | P0030 |
| **Autores** | Selami Bağrıyanık, Ersin Ersoy [1] |
| **Ano** | 2025 [2] |
| **Venue** | International Conference on Computer Science and Engineering (UBMK) [2] |
| **DOI** | Not specified in the source [2, 3] |
| **Tipo** | Conference paper [2] |
| **Metodo** | Method Proposal (integrating COSMIC Function Point with statistical sampling) [1] |
| **Amostra** | Stratified statistical sampling of completed work; example data shows 13 teams with hundreds of projects [4, 5] |
| **Contexto** | Industry — conducted within Wingie Enuygun Group R&D [1] |
| **Modo de trabalho** | Not specified [1] |
| **Metodologia** | Not specified (mentions Agile/Scrum as common contexts for metrics like Story Points) [6] |

---

## Objetivo

O principal objetivo deste artigo é propor um método capaz de determinar objetivamente a extensão dos ganhos de produtividade e qualidade reivindicados pela **AI-Driven Software Engineering** [1, 7]. O método busca superar a natureza subjetiva das avaliações atuais integrando a medição de tamanho funcional **COSMIC Function Point (CFP)** com técnicas de amostragem estatística para permitir o monitoramento consistente em todos os níveis organizacionais [1, 8].

---

## Questoes de Pesquisa

Embora o artigo não liste RQs numeradas explicitamente, ele se propõe a responder:
- Existe uma diferença estatisticamente significativa na produtividade e qualidade entre o período em que o desenvolvimento de software assistido por IA começou e o período anterior? [4]

---

## Metricas e Instrumentos de Avaliacao

| Metrica | Categoria | Nivel | Como Coletada | Validada |
|---------|-----------|-------|---------------|----------|
| **COSMIC Function Point (CFP)** | Productivity / Quality | Individual/Team/Organization | Analysis of data movements (Entry, Exit, Read, Write) based on ISO/IEC 19761 [9, 10] | Yes (ISO standard) [9] |
| **Effort (FTE: Full-time equivalent)** | Productivity | Team/Organization | Organizational workforce data in person-days [2, 4] | Not specified |
| **Defect Count (DC)** | Quality | Team/Organization | Incident data arising in the live system [4] | Not specified |
| **Average Productivity (AP)** | Productivity | Team/Organization | Calculated as $\sum CFP / \sum FTE$ for a sample set [4] | No (Proposed calculation) |
| **Average Defect Density** | Quality | Team/Organization | Calculated as $\sum DC / \sum CFP$ [4] | No (Proposed calculation) |

---

## Frameworks e Metricas

### Frameworks Referenciados
- **COSMIC Function Point (CFP)**: APPLIED (used as the core measurement instrument) [1, 9].
- **Agile (Scrum)**: REFERENCED (discussed in the context of Story Points and industry adoption) [6].
- **Story Points**: REFERENCED (cited as the de facto standard in Agile that often replaces formal sizing) [6, 8].

### Frameworks Propostos
O artigo propõe um método de três grupos de processos que combina a coleta de dados históricos de projetos e incidentes, a aplicação de **Stratified Statistical Sampling** para reduzir o esforço de medição, e a inferência estatística para comparar períodos pré e pós adoção de IA [2, 4].

---

## Fatores que Influenciam Produtividade

### Fatores Positivos
| Fator | Categoria |
|-------|-----------|
| Generative AI and LLMs | Technical [11, 12] |
| AI-powered coding tools (e.g., Cursor AI, GitHub Copilot) | Technical [6, 12] |
| Automation of repetitive tasks | Process [6] |
| Higher abstraction levels (Natural Language prompts) | Technical [12] |

### Fatores Negativos
| Fator | Categoria |
|-------|-----------|
| Inherent software complexity and changeability | Technical [12] |
| Over-reliance on AI tools impacting quality/security | Human/Technical [12] |
| Non-deterministic nature of AI | Technical [11] |
| Manual effort/expertise required for formal sizing (CFP) | Process/Human [6, 8] |

---

## Papel da IA e Automacao

| Campo | Valor |
|-------|-------|
| Usa IA/ML? | Yes — The method is designed to evaluate the impact of AI-assisted development [1, 4]. |
| Automacao de coleta? | No — Current CFP measurement is manual, though the paper identifies automation as a future goal [6, 13]. |
| Impacto de IA na produtividade? | The paper aims to measure this impact; preliminary results show the method can monitor these trends if data is accurate [1, 2]. |

---

## Resultados Principais

- O método proposto é capaz de alcançar o objetivo de avaliação objetiva se os dados coletados forem precisos e a amostragem for suficientemente grande [2].
- A medição manual de **CFP** é identificada como um desafio significativo devido ao tempo e know-how exigidos, criando um trade-off entre confiança estatística e esforço manual [2, 14].
- A integração do método aos processos de **Software Development Lifecycle (SDLC)** é recomendada para transformá-lo em uma ferramenta de melhoria contínua [15].

---

## Desafios do Uso das Metricas

- **Esforço de Medição:** A medição manual de CFP em organizações com alto volume de projetos é demorada [2].
- **Coleta de Dados Históricos:** Dificuldade em obter dados retroativos precisos de projetos, incidentes e força de trabalho [2, 14].
- **Expertise:** CFP requer mais treinamento e especialização do que métricas comuns como Story Points [6, 8].

---

## Avaliacao de Qualidade Metodologica

| Criterio | Pontuacao (0-2) |
|----------|----------------|
| Objetivo claramente definido | 2 |
| Metodologia adequada ao objetivo | 2 |
| Amostra/contexto descrito adequadamente | 1 |
| Ameacas a validade discutidas | 1 |
| Resultados com evidencia suficiente | 1 |
| Contribuicao clara para pratica ou teoria | 2 |
| **TOTAL** | **9/12** |

---

## Limitacoes

- O método atualmente depende de medição manual de CFP, o que é oneroso [2, 14].
- A dependência da maturidade dos dados da organização; se o SDLC não captura incidentes ou esforço adequadamente, o método falha [2, 15].
- Resultados detalhados de uma aplicação em larga escala ainda estão pendentes para publicação futura [13].

---

## Contribuicao Principal

A principal contribuição é a criação de uma metodologia estatisticamente rigorosa que utiliza o padrão ISO **COSMIC Function Point** e **Stratified Sampling** para fornecer uma base objetiva para medir o impacto de transformações tecnológicas, especificamente a introdução de IA, na produtividade e qualidade de software em nível organizacional [1, 8, 14].

---

*Extraido via NotebookLM em March 2026 para MLR: Software Developer Metrics in Practice*
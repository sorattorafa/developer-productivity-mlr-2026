# P1345 — An Instrument for Measuring Perception about Social and Human Factors that Influence Software Development Productivity

**Decisao: INCLUIDO | Qualidade: 11/12**

---

## Dados Bibliograficos

| Campo | Valor |
|-------|-------|
| **ID** | P1345 |
| **Autores** | Awdren Fontão, Arilo Dias-Neto, Davi Viana [1] |
| **Ano** | 2017 [2] |
| **Venue** | 2017 IEEE/ACM Joint 5th International Workshop on Software Engineering for Systems-of-Systems and 11th Workshop on Distributed Software Development, Software Ecosystems and Systems-of-Systems (JSOS) [3] |
| **DOI** | Not specified (ISBN: 978-1-5386-2799-0) [2] |
| **Tipo** | Conference paper [4] |
| **Metodo** | Systematic Literature Review (Snowballing) and thematic analysis [1, 5] |
| **Amostra** | 11 selected papers from an initial set of 125 retrieved studies [6] |
| **Contexto** | Mobile Software Ecosystem (MSECO) involving keystones and external developers [1, 7] |
| **Modo de trabalho** | Not specified [1-30] |
| **Metodologia** | The study analyzes papers covering Lean and Agile environments [12, 22] |

---

## Objetivo

O principal objetivo do artigo é realizar uma identificação inicial dos fatores de influência da Developer Experience (DX) no contexto de ecossistemas de software móvel (MSECO) [1]. Os autores buscam compreender como as expectativas, percepções e sentimentos dos desenvolvedores externos impactam sua interação com as plataformas mantidas pelas organizações centrais (keystones) [1, 8, 9].

---

## Questoes de Pesquisa

O artigo não lista explicitamente perguntas de pesquisa formatadas como RQ, mas foca na seguinte exploração:
- Investigar quais fatores influenciam a Developer Experience em ecossistemas de software móvel [9, 14].

---

## Metricas e Instrumentos de Avaliacao

| Metrica | Categoria | Nivel | Como Coletada | Validada |
|---------|-----------|-------|---------------|----------|
| Star ratings | Quality | Individual/Product | App Store data [2] | Yes [2] |
| Downloads | Activity | Individual/Product | App Store analytics [19] | Yes [19] |
| Ratings/Reviews | Satisfaction | Individual/Product | User feedback in stores [19] | Yes [19] |
| Programming performance | Productivity | Individual | Analysis of affects and moods [24] | Partial (Literature study) [24] |
| Fixed issue time | Productivity | Individual/Team | Repository data analysis (referenced study) [12] | Yes [12] |

---

## Frameworks e Metricas

### Frameworks Referenciados
- **Developer Experience (DX) Concept (Fagerholm et al.):** REFERENCED — Utilizado para definir as dimensões de infraestrutura, sentimentos e valor [3, 9, 14].
- **Snowballing Methodology (Wohlin):** APPLIED — Utilizado como método sistemático para a revisão de literatura [4].
- **Thematic Analysis (Cruzes and Dyba):** APPLIED — Utilizado para sintetizar e categorizar os fatores de influência identificados [14, 15].
- **MSECO Health (Manikas and Hansen):** REFERENCED — Discutido no contexto da produtividade e robustez do ecossistema [8, 10].

### Frameworks Propostos
O artigo não propõe um framework de medição inédito, mas apresenta um **mapa mental (mind map)** que organiza 20 fatores de influência da DX em três categorias principais: Infraestrutura de Desenvolvimento, Sentimentos sobre o Trabalho e o Valor da Contribuição [14, 16].

---

## Fatores que Influenciam Produtividade

### Fatores Positivos
| Fator | Categoria |
|-------|-----------|
| Focus on improving quality | Technical/Process [18] |
| Good management | Organizational [18, 25] |
| Technically challenging work | Technical [18, 20] |
| Enjoy challenges | Human [25] |
| Variety of work | Process [25] |
| Motivation | Human [21, 22] |
| Happiness | Human [23] |
| Recognition | Human [16] |
| Learning | Human [16, 20] |

### Fatores Negativos
| Fator | Categoria |
|-------|-----------|
| Unhappy with management | Organizational/Human [18] |
| Lack of organization | Organizational/Process [18] |
| Time pressure (Control over schedule) | Process [18, 19] |
| Negative feedback on social networks | Human/Organizational [19] |

---

## Papel da IA e Automacao

| Campo | Valor |
|-------|-------|
| Usa IA/ML? | No — O estudo é uma revisão qualitativa de literatura [1, 26]. |
| Automacao de coleta? | No — A coleta foi realizada via Snowballing manual e análise temática por pesquisadores [6, 14]. |
| Impacto de IA na produtividade? | Not addressed in this paper [1-30]. |

---

## Resultados Principais

- Identificação de **20 fatores de influência** relacionados à Developer Experience em ecossistemas móveis [1, 9].
- Os fatores foram categorizados em três fontes: **Infraestrutura de desenvolvimento** (ex: expectativas dos usuários), **Sentimentos sobre o trabalho** (ex: motivação, afetividade) e **Valor da contribuição** (ex: performance, variedade de trabalho) [2, 3, 14, 16].
- Demonstração de que a satisfação dos desenvolvedores com a gestão da keystone (ex: decisões estratégicas da Microsoft no Windows Phone) impacta diretamente seu engajamento [18, 19].
- Constatação de que a afetividade humana e o estado emocional impactam a habilidade das equipes de produzir produtos de sucesso e a produtividade organizacional [23].

---

## Desafios do Uso das Metricas

- Dificuldade em prever o comportamento dos desenvolvedores devido à complexidade e incerteza do processo de desenvolvimento de software [25].
- O desafio das keystones em entender o impacto do desenvolvimento de aplicativos a partir da perspectiva da experiência do desenvolvedor [8].
- Expectativas dos desenvolvedores podem permanecer não articuladas ou expressas de forma vaga [16].

---

## Avaliacao de Qualidade Metodologica

| Criterio | Pontuacao (0-2) |
|----------|----------------|
| Objetivo claramente definido | 2 [1] |
| Metodologia adequada ao objetivo | 2 [4, 5, 14] |
| Amostra/contexto descrito adequadamente | 2 [6] |
| Ameacas a validade discutidas | 1 [26] |
| Resultados com evidencia suficiente | 2 [14, 16] |
| Contribuicao clara para pratica ou teoria | 2 [26] |
| **TOTAL** | **11/12** |

---

## Limitacoes

- O estudo apresenta resultados preliminares de uma revisão que ainda estava em execução [9, 26].
- A análise é focada em uma perspectiva qualitativa e teórica, baseada em literatura existente [14, 26].

---

## Contribuicao Principal

A principal contribuição deste trabalho é a sistematização inicial de **20 fatores que influenciam a experiência do desenvolvedor (DX)** especificamente em **ecossistemas de software móvel** [1, 26]. Ao categorizar esses fatores em dimensões de infraestrutura, sentimentos e valor, o estudo fornece uma base para que organizações centrais (keystones) desenvolvam mecanismos mais eficazes para atrair, engajar e reter desenvolvedores externos, garantindo a saúde e a produtividade do ecossistema [8, 9, 14].

---

*Extraido via NotebookLM em March 2026 para MLR: Software Developer Metrics in Practice*
# P0112 — Impostor Phenomenon in Software Engineers

**Decisao: INCLUIDO | Qualidade: 5/5**

---

## Dados Bibliograficos

| Campo | Valor |
|-------|-------|
| **ID** | P0112 |
| **Autores** | Paloma Guenes, Rafael Tomaz, Marcos Kalinowski, Maria Teresa Baldassarre, and Margaret-Anne Storey [1] |
| **Ano** | 2024 [2, 3] |
| **Venue** | Software Engineering in Society (ICSE-SEIS’24) [3] |
| **DOI** | 10.1145/3639475.3640114 [2, 3] |
| **Tipo** | Conference paper [3] |
| **Metodo** | Survey [4, 5] |
| **Amostra** | 624 software engineers across 26 countries [4, 6] |
| **Contexto** | Industry (multiple sectors including Banking, Sales/E-commerce, Healthcare, etc.) [4, 7] |
| **Modo de trabalho** | Not specified [8, 9] |
| **Metodologia** | Not specified [5, 9] |

---

## Objetivo

O objetivo principal deste trabalho é investigar a prevalência do **Impostor Phenomenon (IP)** em engenheiros de software profissionais e caracterizar como esse fenômeno se manifesta em diferentes perfis (gênero, raça, cargos) e sua relação com a produtividade percebida [4, 5, 10]. O estudo busca preencher uma lacuna na literatura, que anteriormente focava majoritariamente em estudantes de graduação [11, 12].

---

## Questoes de Pesquisa

*   **RQ1:** How does IP manifest in software engineers? [5, 13]
    *   **RQ1.1:** What proportion of Software Engineers suffer from IP? [13]
    *   **RQ1.2:** How does IP manifest in different genders, races/ethnicities, and roles? [13]
*   **RQ2:** Does IP affect the perceived productivity of software engineers? [5, 13]
    *   **RQ2.1** to **RQ2.5:** Does IP affect Satisfaction and Well-being, Performance, Activity, Communication and Collaboration, and Efficiency and Flow? [13]

---

## Metricas e Instrumentos de Avaliacao

| Metrica | Categoria | Nivel | Como Coletada | Validada |
|---------|-----------|-------|---------------|----------|
| **CIPS (Clance Impostor Phenomenon Scale)** | Human Aspects / Satisfaction | Individual | 20-item questionnaire (Likert 1-5) [14] | Yes [5, 15] |
| **Perceived Productivity (SPACE-based)** | Productivity | Individual | 10 Likert-scale self-assessment statements [16, 17] | Partial (Expert review) [16, 18] |

---

## Frameworks e Metricas

### Frameworks Referenciados
*   **SPACE**: APPLIED (utilizado como base para medir a produtividade percebida em cinco dimensões) [5, 12, 16, 19].
*   **GQM (Goal-Question-Metric)**: APPLIED (utilizado para definir o objetivo da pesquisa) [10].

### Frameworks Propostos
O artigo não propõe um novo framework, mas aplica o framework SPACE para avaliar o impacto do IP [5, 16].

---

## Fatores que Influenciam Produtividade

### Fatores Positivos
| Fator | Categoria |
|-------|-----------|
| **Psychological Safety** | Organizational / Human [20, 21] |
| **Personal Life Stability (Married/Children)** | Human (Correlated with lower IP) [4, 22] |

### Fatores Negativos
| Fator | Categoria |
|-------|-----------|
| **Impostor Phenomenon (IP)** | Human [4, 23] |
| **Fear of judgment / exposure** | Human / Social [24, 25] |
| **Burnout and Depression** | Human (Related to IP consequences) [4, 26] |

---

## Papel da IA e Automacao

| Campo | Valor |
|-------|-------|
| Usa IA/ML? | No — although it mentions background research on AI impact [19, 27]. |
| Automacao de coleta? | No — data collection via Tally tool and analysis via Python scripts [8, 28]. |
| Impacto de IA na produtividade? | Not applicable for this study's primary findings. |

---

## Resultados Principais

*   **52,72%** dos engenheiros de software sofrem de níveis frequentes a intensos de IP [4, 29, 30].
*   **Mulheres** apresentam uma proporção significativamente maior de IP (**60,64%**) em comparação aos homens (**48,82%**) [4, 31].
*   Engenheiros **Asiáticos (67,85%)** e **Pretos (65,11%)** relatam sentimentos de impostor com mais frequência do que Brancos (50,00%) [4, 32].
*   A presença de IP é **menos comum** em indivíduos casados e com filhos [4, 22, 29].
*   O IP tem um impacto **negativo estatisticamente significativo** em todas as cinco dimensões de produtividade do framework SPACE [4, 23, 33].
*   A dimensão de **Efficiency and Flow** é a mais afetada negativamente pela percepção de ser um impostor [25].

---

## Desafios do Uso das Metricas

*   **Subjetividade:** A produtividade é medida através da percepção individual (perceived productivity), o que pode não refletir métricas objetivas de sistema [5, 18].
*   **Acesso Restrito:** A escala CIPS exige um formato de "convite fechado", dificultando a disseminação em massa e limitando a distribuição geográfica baseada em contatos diretos [8, 34].
*   **Estigma:** O medo de ser descoberto como uma "fraude" pode influenciar a honestidade nas respostas, embora o anonimato tenha sido garantido [35, 36].

---

## Avaliacao de Qualidade Metodologica

| Criterio | Pontuacao (0-2) |
|----------|----------------|
| Objetivo claramente definido | 2 [10] |
| Metodologia adequada ao objetivo | 2 [5, 37] |
| Amostra/contexto descrito adequadamente | 2 [6, 9, 38] |
| Ameacas a validade discutidas | 2 [18, 34, 39-41] |
| Resultados com evidencia suficiente | 2 [28, 33, 42] |
| Contribuicao clara para pratica ou teoria | 2 [4, 21] |
| **TOTAL** | **12/12** |

---

## Limitacoes

*   **Representatividade de Gênero:** Baixa representação de gêneros não-binários, impedindo inferências estatísticas robustas para esses grupos [31].
*   **Escala de Produtividade:** Ausência de uma escala previamente validada para o framework SPACE, exigindo a criação de declarações próprias pelos autores [18].
*   **Viés Geográfico:** Concentração de respostas em países como Brasil e Itália devido à natureza do convite fechado para a pesquisa [9, 34].

---

## Contribuicao Principal

Este estudo fornece a **primeira investigação abrangente** sobre a prevalência do fenômeno do impostor em profissionais da engenharia de software em geral [43]. A pesquisa demonstra que o IP é uma barreira significativa à produtividade profissional, afetando negativamente o bem-estar, o desempenho e a colaboração, e destaca a necessidade urgente de as organizações promoverem a segurança psicológica e suporte emocional para mitigar esses efeitos, especialmente para grupos sub-representados [21, 43].

---

*Extraido via NotebookLM em March 2026 para MLR: Software Developer Metrics in Practice*
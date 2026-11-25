# P0556 — U Owns the Code That Changes and How Marginal Owners Resolve Issues Slower in Low-Quality Source Code

**Decisao: INCLUIDO | Qualidade: 5/5**

---

## Dados Bibliograficos

| Campo | Valor |
|-------|-------|
| **ID** | P0556 |
| **Autores** | Markus Borg, Adam Tornhill, Enys Mones |
| **Ano** | 2023 |
| **Venue** | EASE '23: The International Conference on Evaluation and Assessment in Software Engineering |
| **DOI** | 10.1145/3593434.3593480 |
| **Tipo** | Conference paper |
| **Metodo** | Repository mining |
| **Amostra** | 48.644 touches em 13.433 source code files, envolvendo 457 desenvolvedores e 7.307 Jira issues |
| **Contexto** | Industry — 40 repositórios proprietários de 18 empresas diferentes |
| **Modo de trabalho** | Not specified |
| **Metodologia** | Agile (mencionado como contexto de práticas como collective code ownership) |

---

## Objetivo

O objetivo principal do artigo é avaliar como a experiência dos desenvolvedores no projeto e a posse de arquivos (code ownership) se relacionam com o tempo de resolução de problemas (issue resolution time), focando especificamente nas diferenças de impacto entre código de alta e baixa qualidade [1-3]. O estudo busca entender se a dívida técnica (technical debt) penaliza de forma desproporcional desenvolvedores menos familiarizados com o código [4, 5].

---

## Questoes de Pesquisa

*   **RQ1:** How is ownership distributed for evolving software? [6]
*   **RQ2:** How does a developer’s project experience correlate with issue resolution times? [6]
*   **RQ3:** How do issue resolution times vary with code quality for changes made by marginal owners? [6]

---

## Metricas e Instrumentos de Avaliacao

| Metrica | Categoria | Nivel | Como Coletada | Validada |
|---------|-----------|-------|---------------|----------|
| **Code Health** | Quality | Individual (File) | Calculada pela ferramenta CodeScene baseada na ISO/IEC 5055 e design smells [6, 7]. | Partial (usada em estudos anteriores) [8]. |
| **Time-in-development** | Productivity | Individual | Diferença de tempo entre os status "In progress" no Jira cruzada com commits do Git [3, 9]. | Partial (definida em trabalhos anteriores) [8]. |
| **Code ownership** | Collaboration | Individual | Fração de touches que um desenvolvedor realizou em um arquivo específico [10]. | No [11]. |
| **Project experience** | Human | Individual | Tempo decorrido desde o primeiro commit do desenvolvedor no repositório (normalizado) [10]. | No (identificada como métrica ingênua) [11]. |
| **Change Size (LoC)** | Activity | Individual | Número de linhas de código modificadas em um "touch" [12]. | No [13]. |

---

## Frameworks e Metricas

### Frameworks Referenciados
- **ISO/IEC 5055 (Automated Source Code Quality Measures):** REFERENCED — Utilizado como base para a definição de métricas de maintainability dentro do Code Health [7, 14, 15].
- **Agile:** REFERENCED — O conceito de collective code ownership é discutido como uma prática ágil [16-18].

### Frameworks Propostos
O artigo não propõe um novo framework, mas introduz a regra empírica "**U owns the code that changes**" para descrever a distribuição bimodal de propriedade de código em projetos industriais [18, 19].

---

## Fatores que Influenciam Produtividade

### Fatores Positivos
| Fator | Categoria |
|-------|-----------|
| **High Code Quality** | Technical |
| **Dominant Code Ownership** | Human/Process |

### Fatores Negativos
| Fator | Categoria |
|-------|-----------|
| **Technical Debt (Alert code)** | Technical |
| **Marginal Ownership** | Human/Collaboration |
| **Low Code Quality combined with Low Ownership** | Technical/Human |

---

## Papel da IA e Automacao

| Campo | Valor |
|-------|-------|
| Usa IA/ML? | No — Embora utilize a ferramenta CodeScene para análise, não descreve o uso de modelos de IA/ML no estudo [7]. |
| Automacao de coleta? | Yes — Coleta automatizada via scripts de repository mining e CodeScene API [3, 20]. |
| Impacto de IA na produtividade? | Not applicable |

---

## Resultados Principais

*   A distribuição de ownership segue um formato de **U**: a maioria das alterações é feita por desenvolvedores com propriedade marginal (≤ 0.1) ou dominante (≥ 0.9) [19, 21].
*   A maioria das alterações em código de baixa qualidade (alert code) é realizada por **marginal owners** [21-23].
*   **Marginal owners** levam **45% mais tempo** para realizar pequenas mudanças e **93% mais tempo** para grandes mudanças em arquivos de baixa qualidade (alert code) comparado a arquivos saudáveis ou com avisos [1, 21, 24, 25].
*   Não foi encontrada correlação significativa entre **project experience** (experiência no projeto) e o tempo de resolução de issues (ρ = -0.12) [26, 27].
*   A implementação de novas funcionalidades é mais prejudicada pela baixa qualidade do código do que a correção de bugs para desenvolvedores com baixa familiaridade [25, 28].

---

## Desafios do Uso das Metricas

*   **Project experience** como métrica ingênua: o tempo total desde o primeiro commit não reflete necessariamente expertise ou recency (familiaridade recente) [11, 29].
*   **Change size** como proxy de complexidade: métricas baseadas apenas em LoC podem não capturar a complexidade real de mudanças que afetam múltiplos arquivos [13].
*   Dificuldade de capturar colaboração "off-git": logs do Git não registram pair programming ou discussões técnicas [11].

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

*   A métrica **Code Health** é proprietária e não totalmente transparente [8].
*   O **time-in-development** não captura variações menores como context switches, reuniões ou pausas [11].
*   O design de estudo observacional impede a atribuição de causalidade direta [13].
*   Viés de seleção: os dados provêm de clientes da CodeScene, que podem ser empresas mais preocupadas com qualidade de código que a média [30].

---

## Contribuicao Principal

A contribuição principal é a evidência empírica de que a dívida técnica (technical debt) atua como um multiplicador de custos especialmente para desenvolvedores com baixa familiaridade com o código (marginal owners) [4, 31]. O estudo demonstra que, embora o collective code ownership seja um ideal ágil, a prática industrial revela uma distribuição em "U", onde o ônus da baixa qualidade recai pesadamente sobre quem está sendo integrado ao projeto ou trabalhando em áreas desconhecidas, aumentando os riscos de previsibilidade e custos de onboarding [1, 18, 23].

---

*Extraido via NotebookLM em March 2026 para MLR: Software Developer Metrics in Practice*
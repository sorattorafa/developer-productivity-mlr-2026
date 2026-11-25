# G028 — Measuring Developer Productivity via Humans

**Decisao: INCLUIDO | Qualidade GL: 5.0/6**

---

## Dados Bibliograficos

| Campo | Valor |
|-------|-------|
| **ID** | G028 |
| **Autor/Organizacao** | Abi Noda (DX), Tim Cochran (Amazon ASBX, ex-ThoughtWorks) |
| **Data** | March 19, 2024 |
| **Tipo** | Blog post |
| **URL** | https://martinfowler.com/articles/measuring-developer-productivity-humans.html |

---

## Resumo

Este artigo defende que as organizações devem priorizar a medição da **Developer Productivity** por meio de dados fornecidos por humanos (**qualitative metrics**) em vez de depender exclusivamente de métricas extraídas de sistemas (**quantitative metrics**) [1]. O autor define métricas qualitativas em duas categorias: **Attitudinal metrics**, que capturam sentimentos e opiniões subjetivas, e **Behavioral metrics**, que relatam fatos objetivos sobre experiências de trabalho através de relatos humanos [2].

A tese central é que dados qualitativos são essenciais para medir o que é "imensurável" por logs de sistemas, como **Technical Debt**, **Flow state** e a facilidade de navegação no código [3]. O texto argumenta que mesmo frameworks consagrados, como os benchmarks do **DORA**, são capturados originalmente através de métodos qualitativos (pesquisas) [2]. Recomenda-se uma abordagem de **mixed-methods**, iniciando com dados qualitativos para identificar oportunidades e utilizando métricas quantitativas para aprofundar a análise [4].

---

## Frameworks Mencionados

*   **DORA**: Discutido como um exemplo de framework cujas métricas (como **Lead Time** e **Deployment Frequency**) são frequentemente capturadas via métodos qualitativos (surveys) para estabelecer benchmarks [2].
*   **Developer Experience (DevEx)**: Mencionado no contexto de pesquisas realizadas por equipes de **Tech Enablement** em empresas como a Peloton [4].

---

## Metricas Mencionadas

*   **IDE Satisfaction**: Medida de satisfação subjetiva com ferramentas de desenvolvimento [2].
*   **Lead Time for Changes**: Tempo para mudanças, capturado via percepção humana [2, 5].
*   **Deployment Frequency**: Frequência de implantação [2].
*   **Change Fail Percentage**: Percentual de falhas em mudanças [2].
*   **Time to Restore**: Tempo para restauração de serviços [2].
*   **Technical Debt**: Avaliada via julgamento humano, visto que métricas de sistema isoladas não conseguem medi-la com precisão [3, 5].
*   **Flow State**: Estado de concentração e produtividade [3].
*   **Codebase Navigability**: Facilidade de navegar no código-fonte [3].
*   **Speed of Code Review**: Velocidade de revisão de código (contextualizada pela qualidade e compartilhamento de conhecimento) [3].
*   **Ease of Doing Work**: Facilidade geral na execução das tarefas [5].
*   **Frequency of Feeling Productive**: Frequência com que o desenvolvedor se sente produtivo [5].
*   **Deep Work Time**: Disponibilidade de tempo para trabalho focado [5].
*   **Test Coverage**: Percepção de cobertura de testes [5].
*   **CI/CD Tooling Ease**: Facilidade de uso das ferramentas de integração e entrega contínua [5].
*   **Specification Quality**: Qualidade das especificações recebidas [5].

---

## Insights para Praticantes

*   **Segmentação de Resultados**: Os dados de produtividade devem ser segmentados por equipe e **persona** (cargo, tempo de casa, senioridade) para serem úteis [5].
*   **Valor dos Comentários Livres**: Comentários de texto livre em pesquisas são frequentemente mais valiosos do que as pontuações numéricas [5].
*   **Uso de Benchmarks**: É recomendável comparar os resultados internos com benchmarks externos para contextualizar a performance [5].
*   **Evitar Survey Fatigue**: O combate ao cansaço de pesquisas deve ser feito através de ações concretas e **follow-up** significativo baseado nos resultados coletados [5].
*   **Prioridade Qualitativa**: Líderes devem consultar dados de pesquisas antes de dados de logs, pois logs sozinhos não indicam se um fenômeno é "bom" ou "ruim" (ex: alta velocidade de review sem qualidade) [4].

---

## Avaliacao de Qualidade GL (Garousi et al.)

| Criterio | Pontuacao (0-1) |
|----------|----------------|
| Autoridade do autor/organizacao | 1 |
| Descricao de metodologia | 0.5 |
| Data de publicacao | 1 |
| Objetividade (vies comercial) | 0.5 |
| Referencias citadas | 1 |
| Contribuicao nova | 1 |
| **TOTAL** | **5.0/6** |

---

*Extraido via NotebookLM em March 2026 para MLR: Software Developer Metrics in Practice*
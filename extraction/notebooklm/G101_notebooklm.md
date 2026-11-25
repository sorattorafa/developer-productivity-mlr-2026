# G101 — AI in engineering: Q2 2026 benchmarks and research readout

**Decisao: INCLUIDO | Qualidade GL: 5.0/6**

---

## Dados Bibliograficos

| Campo | Valor |
|-------|-------|
| **ID** | G101 |
| **Autor/Organizacao** | Brian Houck & Justin Reock / DX (Engineering Enablement) |
| **Data** | August 14, 2026 |
| **Tipo** | Industry report / Podcast readout |
| **URL** | https://newsletter.getdx.com/p/ai-in-engineering-q2-2026-benchmarks |

---

## Resumo

O relatório e readout de podcast da DX, apresentado por Brian Houck com a participação de Justin Reock (Deputy CTO na DX), analisa os dados do *AI Impact Report* referente ao segundo trimestre de 2026. A adoção de ferramentas de AI entre software developers aproxima-se de 100% (95% observada via telemetria), e mais da metade do código mesclado (*merged code*) é gerada por AI. Contudo, o estudo aponta que a economia de tempo reportada pelos desenvolvedores não tem se traduzido de forma proporcional em melhores resultados de negócio ou inovação.

Embora a velocidade de engenharia tenha aumentado — com ganhos em *PR throughput* e *deployment frequency* —, emergem preocupações operacionais significativas. O tamanho médio das *Pull Requests* (PRs) cresceu de 42 para 72 linhas de código, aumentando riscos de aprovações superficiais (*rubber-stamping*) e *code bloat*, o que por sua vez gera um ciclo de custos crescentes em consumo de *tokens* por *agents*. Observa-se também uma divergência inédita: enquanto a *code maintainability* reportada melhora com AI, a *change confidence* cai, indicando que os desenvolvedores alteram o código com mais facilidade, mas confiam menos que as mudanças não causarão falhas em produção.

Por fim, o relatório destaca que as taxas de falha em mudanças (*change failure rates*) tornaram-se mais voláteis, demonstrando que a AI amplifica forças e fraquezas organizacionais pré-existentes. Os gastos com AI (*AI spend*) aumentaram até 28 vezes entre as maiores empresas analisadas, mas a razão de inovação (*innovation ratio*) subiu apenas cerca de um ponto percentual. Os ganhos de tempo gerados por AI continuam sendo absorvidos por gargalos organizacionais tradicionais, como excesso de reuniões, atrasos em *code review* e tempos de espera de *build* e *test*.

---

## Frameworks Mencionados

- **DX Core 4 Productivity Framework**: Discutido como a estrutura central articulada com os achados do *AI Impact Report*.
- **Developer Experience Index (DXI)**: Discutido e mensurado no estudo (apresentou queda de aproximadamente 2% ao longo de dois trimestres).
- *Nota sobre outros frameworks*: Indicadores de entrega contínua tipicamente associados a frameworks como DORA e DevEx (e.g., *deployment frequency*, *change failure rate*, *developer experience drivers*) são discutidos detalhadamente em termos de métricas específicas, embora os acrônimos DORA ou SPACE não sejam explicitamente nomeados no texto.

---

## Metricas Mencionadas

- **AI Adoption Rate**: Próxima de 100% no setor (95% capturada diretamente via telemetria da DX).
- **Percentage of AI-Authored Code**: Mais de 50% do código mesclado (*merged code*) é atualmente gerado por AI.
- **PR Throughput**: Aumento verificado no volume de PRs entregues por equipe/desenvolvedor.
- **Deployment Frequency**: Crescimento na frequência de implantação em produção.
- **Average PR Size**: Aumento significativo no tamanho médio de PRs, subindo de 42 para 72 linhas de código (LOC).
- **Code Maintainability vs. Change Confidence**: Desacoplamento entre a manutenibilidade do código (em alta) e a confiança nas alterações efetuadas (em queda).
- **Change Failure Rate**: Aumento da volatilidade nas taxas de falha de mudança entre diferentes empresas.
- **Developer Experience Index (DXI)**: Queda de ~2% no índice ao longo de dois trimestres.
- **AI Spend**: Crescimento de aproximadamente 28 vezes (28x) em relação ao ano anterior nas maiores empresas do conjunto de dados.
- **Developer Ramp-Up Time**: Redução no tempo de integração e rampa de novos desenvolvedores.
- **Innovation Ratio**: Aumento marginal de apenas ~1 ponto percentual na proporção de esforço dedicado à inovação.
- **Time Saved**: Tempo economizado reportado trimestralmente pelos desenvolvedores.

---

## Insights para Praticantes

- **Migrar o foco da adoção para a sofisticação e resultados**: Como a adoção de AI está universalizada, medir apenas o uso não traz diferencial; organizações precisam avaliar o grau de sofisticação no uso de AI e o valor de negócio produzido.
- **Controlar o tamanho das PRs para conter custos de contexto e fricção de revisão**: PRs maiores (de 42 para 72 LOC) dificultam o *code review*, aumentam a probabilidade de aprovações sem análise crítica e inflam a base de código, gerando consumo excessivo e repetitivo de *tokens* por *agents*.
- **Acompanhar a lacuna entre alterabilidade e confiança no código**: A facilidade de modificar código via AI pode mascarar a perda de compreensão profunda do sistema. Lideranças devem reavaliar se as métricas tradicionais de *maintainability* e *ownership* ainda capturam a real saúde do *codebase*.
- **Atuar sobre fricções organizacionais para liberar o tempo ganho com AI**: Economias de tempo obtidas com AI são rapidamente absorvidas por excesso de reuniões, interrupções, gargalos em *build/test* e atrasos em revisões. A redução de reuniões desnecessárias, por exemplo, demonstrou gerar até o dobro de ganho em *PR throughput* comparado ao impacto isolado da AI.
- **Direcionar eficiência para valor ao cliente**: Aumentar a velocidade e remover fricções técnicas só agregam valor real se resultarem no envio de software mais valioso para os usuários finais.

---

## Avaliacao de Qualidade GL (Garousi et al.)

| Criterio | Pontuacao (0-1) |
|----------|----------------|
| Autoridade do autor/organizacao | 1.0 |
| Descricao de metodologia | 0.5 |
| Data de publicacao | 1.0 |
| Objetividade (vies comercial) | 0.5 |
| Referencias citadas | 1.0 |
| Contribuicao nova | 1.0 |
| **TOTAL** | **5.0/6** |

---

*Extraido via NotebookLM em October 2026 para MLR: Software Developer Metrics in Practice*
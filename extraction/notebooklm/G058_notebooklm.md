# G058 — The impact of LLM-assistants on software developer productivity: A systematic literature review

**Decisao: INCLUIDO | Qualidade GL: 6/6**

---

## Dados Bibliograficos

| Campo | Valor |
|-------|-------|
| **ID** | G058 |
| **Autor/Organizacao** | Amr Mohamed, Maram Assi, and Mariam Guizani [1] |
| **Data** | July 2025 [2] |
| **Tipo** | Systematic Literature Review (SLR) [1, 3] |
| **URL** | https://zenodo.org/records/15788502 [4, 5] |

---

## Resumo

Este documento apresenta uma **Systematic Literature Review (SLR)** de 37 estudos revisados por pares, publicados entre janeiro de 2014 e dezembro de 2024, que examinam o impacto de **LLM-assistants** na produtividade de desenvolvedores [3, 6]. A análise revela que essas ferramentas oferecem benefícios consideráveis, como o aumento da velocidade de desenvolvimento, a redução do esforço em **online code search** e a automação de tarefas repetitivas [6, 7]. No entanto, os estudos também destacam riscos críticos, incluindo o fenômeno de **cognitive offloading**, a redução da colaboração em equipe e impactos inconsistentes na qualidade do código [8-10].

A pesquisa utiliza o **SPACE framework** para mapear as dimensões de produtividade investigadas, observando que a maioria dos estudos (92%) adota uma perspectiva multidimensional [8, 11]. Contudo, apenas 14% exploram mais de três dimensões, indicando uma lacuna em avaliações integradas [8, 11]. As dimensões de **Satisfaction**, **Performance** e **Efficiency** são as mais estudadas, enquanto **Communication** e **Activity** permanecem subexploradas [8, 12]. O trabalho conclui com recomendações práticas, enfatizando a mudança do papel do desenvolvedor de "escritor de código" para "revisor" [13, 14].

---

## Frameworks Mencionados

*   **SPACE framework**: Utilizado como o modelo organizacional central para mapear dimensões de produtividade como **Satisfaction**, **Performance**, **Activity**, **Communication** e **Efficiency** [8, 15-17].
*   **Developer Experience (DevEx)**: Mencionado como um modelo prático baseado em **feedback loops**, **cognitive load** e **flow state** [18-20].
*   **McLuhan’s Tetrad**: Aplicado na discussão para refletir sobre as implicações sociotécnicas (Enhance, Reverse, Obsolesce, Retrieve) das novas ferramentas [15, 21, 22].
*   **Technology Acceptance Model (TAM)**: Citado como um instrumento validado para medir a aceitação tecnológica [23-25].
*   **NASA-TLX**: Utilizado em diversos estudos para medir **mental workload** e **cognitive load** [23, 24, 26].
*   **Time-Cost-Quality (TCQ)**: Framework conceitual aplicado em análises econométricas da produtividade [27, 28].
*   **Resource-Based View (RBV)**: Framework mencionado no contexto de avaliação de capacidades firmes de IA [27].

---

## Metricas Mencionadas

*   **Time to completion / Task Completion**: Métrica de desempenho mais frequente para avaliar a eficiência temporal em tarefas controladas [27, 29].
*   **Suggestions Acceptance Rate**: Métrica comportamental que mede a frequência com que sugestões da IA são aceitas; estudos alertam contra seu uso isolado [23, 30-32].
*   **Code Quality Metrics**: Incluem **cyclomatic complexity**, **code coverage**, **code smells**, **technical debt**, **defect density** e número de defeitos [27, 33-35].
*   **Throughput and cycle time**: Utilizados para medir o impacto da integração de ferramentas como o **GitHub Copilot** em ambientes reais [29, 36].
*   **Lines of Code (LOC)** e **Development Velocity**: Citados como métricas tradicionais quantificáveis, embora limitadas para capturar dimensões humanas [37, 38].
*   **Mental demand, Effort e Frustration**: Subescalas do **NASA-TLX** usadas para medir o impacto cognitivo [26].
*   **BLEU Score**: Métrica mencionada para avaliar a qualidade de geração e tradução de código [35].

---

## Insights para Praticantes

*   **Cultivar "Calibrated Trust"**: Desenvolvedores devem entender as capacidades e limitações das ferramentas para evitar a **automation complacency**, verificando ativamente os resultados gerados [39].
*   **Transicao de Coder para Reviewer**: O papel do desenvolvedor está evoluindo; mais tempo deve ser alocado para **prompt engineering**, avaliação iterativa e refinamento de saídas da IA em vez de escrita manual [13, 14].
*   **Decomposicao de Problemas**: Para obter respostas mais coerentes, recomenda-se decompor tarefas complexas em subproblemas menores e bem escopados [13, 14].
*   **Preservar Colaboracao Humana**: É crucial manter práticas como **pair programming** e revisões de arquitetura para evitar a degradação da comunicação na equipe causada pelo uso excessivo de assistentes individuais [40].
*   **Customizacao de Ferramentas**: Desenvolvedores devem ajustar as configurações de frequência de sugestões para minimizar interrupções e proteger o **flow state** [40].

---

## Avaliacao de Qualidade GL (Garousi et al.)

| Criterio | Pontuacao (0-1) |
|----------|----------------|
| Autoridade do autor/organizacao | 1 |
| Descricao de metodologia | 1 |
| Data de publicacao | 1 |
| Objetividade (vies comercial) | 1 |
| Referencias citadas | 1 |
| Contribuicao nova | 1 |
| **TOTAL** | **6/6** |

---

*Extraido via NotebookLM em March 2026 para MLR: Software Developer Metrics in Practice*
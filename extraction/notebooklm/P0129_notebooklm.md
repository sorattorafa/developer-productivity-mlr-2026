# P0129 — Exploring the Efficiency of Self-Organizing Software Teams with Game Theory

**Decisao: INCLUIDO | Qualidade: 4/5**

---

## Dados Bibliograficos

| Campo | Valor |
|-------|-------|
| **ID** | P0129 |
| **Autores** | Clay Stevens, Jared Soundy, Hau Chan |
| **Ano** | 2021 |
| **Venue** | International Conference on Software Engineering (ICSE-NIER) |
| **DOI** | 10.1109/ICSE-NIER52604.2021.00016 |
| **Tipo** | Conference paper |
| **Metodo** | Simulation / Case Study (Mathematical modeling) |
| **Amostra** | 100 simulations for each combination of developers (1-9) and tasks (1-9) |
| **Contexto** | Academic/Simulation — focus on strategic behavior in Agile self-organizing teams |
| **Modo de trabalho** | Not specified |
| **Metodologia** | Agile (Scrum) |

---

## Objetivo

O principal objetivo do artigo é propor um framework teórico baseado em **Game Theory** (Teoria dos Jogos) não-cooperativa para modelar e avaliar a eficiência de equipes de software auto-organizadas [1, 2]. Os autores argumentam que o comportamento estratégico dos desenvolvedores durante a auto-atribuição de tarefas pode ser medido e comparado a um planejamento centralizado ideal [1, 3].

---

## Questoes de Pesquisa

*   **RQ1 (A):** How can we (theoretically) model and understand strategic behavior in self-organizing teams (SOTs)? [3]
*   **RQ2 (B):** How can we evaluate and measure the efficiency of developers’ strategic behavior? [3]
*   **RQ3 (C):** How do developers self-organize in real-world settings, and is it consistent with the model’s predictions? [3]

---

## Metricas e Instrumentos de Avaliacao

| Metrica | Categoria | Nivel | Como Coletada | Validada |
|---------|-----------|-------|---------------|----------|
| **Social Welfare (SW)** | Satisfaction / Morale | Team | Calculada como a soma da utilidade (payoff - custo) de todos os desenvolvedores no modelo. | Partial (Used as proxy) [4, 5] |
| **Threshold Completed (TH)** | Productivity | Team | Soma dos valores de threshold de todas as tarefas completadas em um sprint. | Partial (Used as proxy) [5] |
| **Price-of-Stability (PoS)** | Efficiency | Team | Razão entre o bem-estar social ótimo e o melhor Nash Equilibrium. | Yes (Theoretical) [6] |
| **Price-of-Anarchy (PoA)** | Efficiency | Team | Razão entre o bem-estar social ótimo e o pior Nash Equilibrium. | Yes (Theoretical) [6] |
| **Velocity** | Productivity | Team | Mencionada como número de story points ou tarefas concluídas; usada para motivar o modelo. | Referenced [7] |

---

## Frameworks e Metricas

### Frameworks Referenciados
*   **Agile / Scrum:** Referenciado como o contexto industrial para equipes auto-organizadas [1, 8].
*   **Tullock contests:** Referenciado como a base matemática para o modelo de competição por tarefas [9, 10].

### Frameworks Propostos
*   **Game-theoretic framework for self-assignment:** O artigo propõe um modelo geral onde a auto-atribuição de tarefas é tratada como um jogo, utilizando equilíbrios de Nash para prever comportamentos e métricas de "Price of Anarchy/Stability" para medir eficiência [2, 11, 12].

---

## Fatores que Influenciam Produtividade

### Fatores Positivos
| Fator | Categoria |
|-------|-----------|
| **Small team size** | Organizational |
| **Developer skill (10x developers)** | Human |
| **Multitasking** | Process |

### Fatores Negativos
| Fator | Categoria |
|-------|-----------|
| **Strategic behavior (Self-interest)** | Human |
| **Large team size** | Organizational |
| **Diminishing returns (Brooks' Law)** | Process |

---

## Papel da IA e Automacao

| Campo | Valor |
|-------|-------|
| Usa IA/ML? | No — utiliza modelagem matemática e simulação [9, 13]. |
| Automacao de coleta? | Yes — dados gerados via simulação automatizada [13]. |
| Impacto de IA na produtividade? | Not applicable. |

---

## Resultados Principais

*   **Moral da Equipe:** Equipes menores tendem a se auto-organizar de forma mais eficiente do que equipes maiores quando o critério é o bem-estar social (morale) [14, 15].
*   **Produtividade (TH):** Equipes muito pequenas são menos eficientes em termos de produtividade e têm maior risco de não completar nenhuma tarefa em comparação com a gestão centralizada [14].
*   **Ponto de Equilíbrio:** Equipes com 4 ou mais desenvolvedores atribuindo 4 ou mais tarefas mostram estabilidade na eficiência de produtividade, sem grandes ganhos ao aumentar o tamanho da equipe [15].
*   **Divergência de Objetivos:** O comportamento estratégico (busca pelo interesse próprio) geralmente leva a resultados sub-ótimos para a equipe como um todo [3, 5].

---

## Desafios do Uso das Metricas

*   **Strategic behavior:** Desenvolvedores podem sacrificar o bem comum (social good) para maximizar sua própria utilidade/velocity [3].
*   **Sub-optimal outcomes:** A auto-atribuição raramente alcança o resultado ideal que um planejador centralizado perfeito conseguiria [5, 6].

---

## Avaliacao de Qualidade Metodologica

| Criterio | Pontuacao (0-2) |
|----------|----------------|
| Objetivo claramente definido | 2 |
| Metodologia adequada ao objetivo | 2 |
| Amostra/contexto descrito adequadamente | 1 |
| Ameacas a validade discutidas | 1 |
| Resultados com evidencia suficiente | 2 |
| Contribuicao clara para pratica ou teoria | 2 |
| **TOTAL** | **10/12** |

---

## Limitacoes

*   **Ausência de dados humanos:** O modelo foi testado apenas via simulação, sem validação com desenvolvedores reais [15, 16].
*   **Assunção de Racionalidade Perfeita:** Assume que desenvolvedores agem de forma puramente racional para maximizar utilidade [17].
*   **Informação Completa:** O modelo assume que todos os jogadores conhecem as estratégias e payoffs uns dos outros [17].
*   **Seleção Simultânea:** O modelo simula escolhas simultâneas, enquanto no Scrum real as escolhas podem ser sequenciais ao longo do sprint [18].

---

## Contribuicao Principal

A principal contribuição é a introdução de conceitos avançados de **Teoria dos Jogos** (especificamente **Price-of-Stability** e **Price-of-Anarchy**) para a área de Engenharia de Software como ferramentas para medir a eficiência da auto-organização em equipes Agile, permitindo uma análise quantitativa do impacto do comportamento estratégico dos desenvolvedores nos resultados do time [1, 2, 12].

---

*Extraido via NotebookLM em March 2026 para MLR: Software Developer Metrics in Practice*
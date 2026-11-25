# P0162 — Are We Speeding Up or Slowing Down? On Temporal Aspects of Code Velocity

**Decisao: INCLUIDO | Qualidade: 5/5**

---

## Dados Bibliograficos

| Campo | Valor |
|-------|-------|
| **ID** | P0162 |
| **Autores** | Gunnar Kudrjavets, Nachiappan Nagappan, Ayushi Rastogi |
| **Ano** | 2023 |
| **Venue** | 20th IEEE/ACM International Conference on Mining Software Repositories (MSR) |
| **DOI** | 10.1109/MSR59073.2023.00046 |
| **Tipo** | Conference paper |
| **Metodo** | Repository mining |
| **Amostra** | 283.235 revisões de código (filtradas para 280.456) cobrindo uma média de sete anos de desenvolvimento [1, 2]. |
| **Contexto** | OSS (Open Source Software) — Projetos: Blender, FreeBSD, LLVM e Mozilla [1, 3]. |
| **Modo de trabalho** | Not specified |
| **Metodologia** | Modern Code Review (MCR), CI/CD [2, 4]. |

---

## Objetivo

O objetivo principal do artigo é investigar como a duração de vários períodos do processo de **code review** (denominada **code velocity**) se altera ao longo do tempo de vida de grandes projetos de software [1, 3]. Os autores buscam determinar se a velocidade diminui com o aumento da complexidade e tamanho do sistema ou se aumenta devido à familiaridade dos desenvolvedores e melhoria das ferramentas [5, 6].

---

## Questoes de Pesquisa

*   **RQ1:** How does a project’s code velocity trend over time? Does the code velocity increase, decrease, or stay neutral? [7]

---

## Metricas e Instrumentos de Avaliacao

| Metrica | Categoria | Nivel | Como Coletada | Validada |
|---------|-----------|-------|---------------|----------|
| **Time-to-merge** | Delivery / Activity | Team | Mined from Phabricator; tempo entre a publicação da mudança e o merge [2, 8]. | Yes [9] |
| **Time-to-first-response** | Collaboration | Individual/Team | Mined from Phabricator; tempo até o primeiro comentário de revisão [3, 10]. | Yes [9] |
| **Time-to-accept** | Delivery / Activity | Team | Mined from Phabricator; tempo até a aceitação formal da mudança [3, 10]. | Yes [9] |
| **Source Lines of Code (SLOC)** | Activity | Organization | Calculated using the tool `scc` [11, 12]. | Yes [11] |
| **Number of commits** | Activity | Team | Mined from Git repositories [11, 12]. | Yes [11] |
| **Number of distinct authors** | Activity | Individual | Mined from Git repositories [1, 12]. | Yes [11] |
| **Number of distinct committers** | Activity | Individual | Mined from Git repositories [11, 12]. | Yes [11] |

---

## Frameworks e Metricas

### Frameworks Referenciados
*   **Modern Code Review (MCR):** APPLIED — Usado como processo base para a coleta de dados de revisão [2, 4].
*   **CI/CD:** REFERENCED — Discutido como prática padrão que impacta a velocidade [4].
*   **Lehman’s Laws of Software Evolution:** REFERENCED — Usado para fundamentar as hipóteses de complexidade crescente e crescimento contínuo [5, 6, 13].
*   **Brooks’ Law:** REFERENCED — Discutido em relação ao impacto do aumento do tamanho da equipe na velocidade [6, 14].

### Frameworks Propostos
O artigo não propõe um novo framework, mas utiliza um aparato estatístico baseado no **Mann-Kendall test** e **Sen’s slope** para avaliar tendências temporais em métricas de software [15, 16].

---

## Fatores que Influenciam Produtividade

### Fatores Positivos
| Fator | Categoria |
|-------|-----------|
| Familiaridade do engenheiro com a base de código | Human [5, 17] |
| Eficiência na comunicação interpessoal / Relacionamentos | Human/Organizational [5, 17] |
| Melhoria na infraestrutura de ferramentas (**tooling**) | Technical [5, 17] |
| Comportamento autocorretivo organizacional (Core teams) | Organizational [18] |

### Fatores Negativos
| Fator | Categoria |
|-------|-----------|
| Aumento na complexidade e tamanho do sistema | Technical [5] |
| Aumento na complexidade da comunicação em times maiores | Organizational [5, 6] |
| Natureza humana (tempo fixo dedicado a revisões) | Human [19] |

---

## Papel da IA e Automacao

| Campo | Valor |
|-------|-------|
| Usa IA/ML? | No [15, 20]. |
| Automacao de coleta? | Yes — Mineração automatizada de dados do Phabricator e uso da ferramenta `scc` [2, 11]. |
| Impacto de IA na produtividade? | Not applicable — O estudo não aborda o impacto de ferramentas de IA. |

---

## Resultados Principais

*   **Estabilidade da Velocidade:** Nem a passagem do tempo nem o aumento no tamanho do projeto impactam negativamente a **code velocity** [1].
*   **Tendência de Melhora:** Para FreeBSD, LLVM e Mozilla, a duração dos períodos de revisão (resposta, aceitação e merge) tornou-se mais curta ou permaneceu estável; Blender não apresentou tendência direcional clara [1, 21].
*   **Crescimento do Código vs. Velocidade:** Apesar de um crescimento anual de **3% a 17%** nas linhas de código (SLOC), não houve diminuição na velocidade de entrega [1, 22].
*   **Faixa Fixa:** A mediana móvel de 30 dias para o **time-to-merge** permanece em uma faixa relativamente fixa ao longo dos anos para a maioria dos projetos [1, 22, 23].

---

## Desafios do Uso das Metricas

*   **Autocorrelação:** Desafio na análise de séries temporais que exige ajustes nos testes estatísticos para evitar falsas conclusões de tendências [16].
*   **Dados Inconsistentes:** Necessidade de filtrar revisões que não seguem o processo padrão (ex: sem código, auto-aceitação) para garantir a validade dos dados [2].
*   **Variáveis Ocultas:** Limitação em acessar dados sobre decisões de gestão, prioridades de negócio ou desafios organizacionais que não são documentados publicamente [11].
*   **Dados de Defeitos:** Identificados como indicadores não confiáveis da carga de trabalho dos desenvolvedores por falta de regras formais de contagem [24].

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

*   **External Validity:** Os resultados são baseados exclusivamente em projetos **Open Source** e podem não ser generalizáveis para contextos industriais com estruturas de incentivo diferentes [18].
*   **Dependência de Ferramenta:** A análise focou em projetos que utilizam o **Phabricator** devido à granularidade dos dados, o que limita a seleção de projetos [18].
*   **Insights Limitados:** O estudo possui visão limitada sobre variáveis de confusão, como mudanças de prioridade organizacional ou desafios de gestão não públicos [11].

---

## Contribuicao Principal

A principal contribuição do trabalho é a evidência empírica de que a **code velocity** (medida através de períodos de revisão de código) é resiliente ao envelhecimento e ao crescimento da complexidade dos projetos de software [1, 17]. O estudo desafia o senso comum da engenharia de software de que os processos inevitavelmente tornam-se mais lentos à medida que os sistemas evoluem, sugerindo que fatores como familiaridade da equipe e melhoria de infraestrutura podem neutralizar o aumento da complexidade [17, 25].

---

*Extraido via NotebookLM em March 2026 para MLR: Software Developer Metrics in Practice*
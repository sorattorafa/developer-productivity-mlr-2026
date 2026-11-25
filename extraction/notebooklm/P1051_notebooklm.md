# P1051 — An Empirical Investigation of Relevant Changes and Automation Needs in Modern Code Review

**Decisao: INCLUIDO | Qualidade: 5/5**

---

## Dados Bibliograficos

| Campo | Valor |
|-------|-------|
| **ID** | P1051 |
| **Autores** | Sebastiano Panichella, Nik Zaugg |
| **Ano** | 2020 |
| **Venue** | Empirical Software Engineering |
| **DOI** | https://doi.org/10.1007/s10664-020-09870-3 |
| **Tipo** | Journal article |
| **Metodo** | Mixed methods (Repository mining, Surveys, Qualitative and Quantitative analysis, Grounded Theory) |
| **Amostra** | 211 review changes, 648 review comments de 10 projetos open-source; 52 desenvolvedores (survey inicial); 14 participantes adicionais para avaliação qualitativa; 21 desenvolvedores para estudo de utilidade |
| **Contexto** | Mixed (OSS: 10 projetos Java do ecossistema Eclipse; Industry: 50% dos participantes do survey possuem perfil industrial) |
| **Modo de trabalho** | Not specified |
| **Metodologia** | Mixed (Menciona práticas de DevOps e Continuous Delivery/Integration como influenciadores) |

---

## Objetivo

O objetivo deste artigo é investigar as abordagens e ferramentas que, sob o **ponto de vista do desenvolvedor**, ainda são necessárias para facilitar as atividades de **Modern Code Review (MCR)** [1, 2]. O estudo busca preencher a lacuna entre as necessidades dos profissionais e as ferramentas de pesquisa disponíveis, focando na identificação de tipos recorrentes de mudanças e no potencial de automação para apoiá-las [2, 3].

---

## Questoes de Pesquisa

*   **RQ1:** What types of changes occur during MCR? [3]
*   **RQ2:** What are the emerging automation needs of developers in MCR? [4]
*   **RQ21:** Are test case summaries enriched by test smell information considered useful by developers? [5]

---

## Metricas e Instrumentos de Avaliacao

| Metrica | Categoria | Nivel | Como Coletada | Validada |
|---------|-----------|-------|---------------|----------|
| Perceived Relevance | Satisfaction/DevEx | Individual | Survey (Likert scale 1-5) | No [6, 7] |
| Perceived Completeness | Satisfaction/DevEx | Individual | Survey (Likert scale 1-5) | No [7, 8] |
| Criticality of solution | Satisfaction/DevEx | Individual | Survey (Likert scale 1-5) | No [9, 10] |
| Feasibility of implementation | Satisfaction/DevEx | Individual | Survey (Likert scale 1-5) | No [9, 10] |
| Dominance of smell ($D_{smell}$) | Quality | Organization | Formula baseada em ocorrências de smells em classes de teste | No [11] |
| Frequency of smell ($F_{smell}$) | Quality | Organization | Formula baseada em ocorrências totais no projeto | No [11] |
| Class frequency ($C_{smell}$) | Quality | Team | Formula baseada na proporção de smells na classe vs. projeto | No [12] |
| Comprehensibility | Satisfaction/DevEx | Individual | Survey (Likert scale) após tarefa experimental | No [13] |

---

## Frameworks e Metricas

### Frameworks Referenciados
*   **SWUM (Software Word Usage Model):** REFERENCED (usado para gerar descrições em linguagem natural) [14].
*   **DECOR:** REFERENCED (usado para detecção estrutural de smells) [15].
*   **TACO:** REFERENCED (usado para detecção de smells via análise textual) [15].

### Frameworks Propostos
*   **Code Review chAnges Model (CRAM):** Uma taxonomia detalhada de mudanças em MCR, categorizada por tipo de artefato (production/test code vs. non-source-code), atividade, categoria e tópico [16, 17].
*   **MCR-Request:** Um modelo que sumariza as recomendações, técnicas e soluções (MCR-REcommendations, TechniQUEs, and SoluTions) visualizadas pelos desenvolvedores para automação [18].

---

## Fatores que Influenciam Produtividade

### Fatores Positivos
| Fator | Categoria |
|-------|-----------|
| Automação de correções de Documentation (e.g., license headers) | Technical/Process [10, 19] |
| Uso de Summarization Techniques para awareness de qualidade | Human/Technical [13, 20] |
| Recomendações de Refactoring baseadas em Test/Code Smells | Technical/Process [21, 22] |
| Integração de feedbacks sobre CD/CI no processo de revisão | Process [23, 24] |

### Fatores Negativos
| Fator | Categoria |
|-------|-----------|
| Mismatch entre expectativas de autores e outcomes dos revisores | Human/Process [25] |
| Feedbacks não exaustivos ou atrasados (not timely reported) | Human/Process [25] |
| Dificuldade técnica em automatizar a detecção de defeitos complexos | Technical [26] |
| Excesso de informações redundantes em ferramentas de automação | Technical/Human [27] |

---

## Papel da IA e Automacao

| Campo | Valor |
|-------|-------|
| Usa IA/ML? | **Yes** — Desenvolvedores sugerem Machine Learning para predições, NLP para análise de documentação e Summarization Techniques para gerar comentários automáticos [26, 28, 29]. O artigo avalia uma ferramenta de sumarização de testes [5, 30]. |
| Automacao de coleta? | **Yes** — Coleta automatizada de dados de repositórios (Gerrit/Git) foi utilizada para minerar commits e comentários [31-33]. |
| Impacto de IA na produtividade? | **Positivo** — 95% dos desenvolvedores consideraram sumários de smells úteis para aumentar a awareness e facilitar a execução de tarefas de revisão [13, 34]. |

---

## Resultados Principais

*   **Taxonomia CRAM:** Identificou 15 tipos iniciais de mudanças, expandidos para incluir novas categorias como licenciamento, segurança e configurações de CD/CI [17, 35, 36].
*   **Frequência vs. Relevância:** Mudanças estruturais são as mais frequentes (48.4%), mas problemas de **Logic** são percebidos como os mais relevantes (4.50/5.00), apesar de ocorrerem em apenas 7.1% dos casos [7, 19, 37].
*   **Necessidades de Automação:** 98% dos participantes acreditam que certas tarefas (e.g., detecção de defeitos) são difíceis de automatizar, enquanto outras (e.g., license headers, documentação inconsistente) são ideais para automação [19, 26].
*   **Novas Fronteiras:** O surgimento de tecnologias Cloud e práticas de CD/CI forçou desenvolvedores a revisar artefatos não relacionados a código (e.g., Docker files, pipelines), criando novas necessidades de feedback [23, 38, 39].
*   **Eficácia de Sumários:** A abordagem de sumarização proposta foi considerada fácil de entender por 81% dos participantes e útil para avaliar a qualidade por 95% [13, 34].

---

## Desafios do Uso das Metricas

*   **Redundância:** Descrições automatizadas podem ser excessivamente detalhadas ou repetitivas, causando cansaço [27].
*   **Usabilidade:** Necessidade de "scroll" excessivo para visualizar sugestões no topo de arquivos longos é considerada um incômodo (nuisance) [40].
*   **Complexidade Técnica:** Metadados de Resource e Security são os mais difíceis de analisar e automatizar [10].

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

*   **Generalização:** O estudo focou em 10 projetos Java, todos dentro do ecossistema Eclipse, o que pode restringir a validade em outras linguagens ou contextos [41].
*   **Subjetividade:** A classificação manual de commits e comentários envolve um nível de julgamento humano que pode introduzir viés [42].
*   **Qualidade das Respostas:** Embora mitigado pelo descarte de respostas superficiais, surveys abertos estão sujeitos a imprecisões dos participantes [43].
*   **Escopo Industrial:** Participantes sugerem que desafios em áreas específicas (e.g., E-Health) podem apresentar desafios de MCR diferentes dos encontrados no estudo [7].

---

## Contribuicao Principal

A contribuição principal é o desenvolvimento e validação do **Code Review chAnges Model (CRAM)**, que mapeia as mudanças modernas em revisões de código, destacando o impacto de novas tecnologias (Cloud, CD/CI). O trabalho fornece evidências empíricas sobre quais atividades os desenvolvedores desejam automatizar e demonstra a viabilidade de usar **técnicas de sumarização e NLP** para fornecer feedbacks automáticos úteis sobre a qualidade do código [16, 44, 45].

---

*Extraido via NotebookLM em March 2026 para MLR: Software Developer Metrics in Practice*
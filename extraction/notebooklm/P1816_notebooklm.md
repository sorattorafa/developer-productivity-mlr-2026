# P1816 — How much SPACE do metrics have in GenAI assisted software development?

**Decisao: INCLUIDO | Qualidade: 4/5**

---

## Dados Bibliograficos

| Campo | Valor |
|-------|-------|
| **ID** | P1816 |
| **Autores** | Samarth Sikand, Kanchanjot Kaur Phokela, Vibhu Saujanya Sharma, Kapil Singi, Vikrant Kaulgud, Teresa Tung, Pragya Sharma, Adam P. Burden [1, 2] |
| **Ano** | 2024 [2] |
| **Venue** | 17th Innovations in Software Engineering Conference (ISEC 2024) [2, 3] |
| **DOI** | https://doi.org/10.1145/3641399.3641419 [2, 4] |
| **Tipo** | Conference paper (Short-Paper) [2, 5] |
| **Metodo** | Survey (Literature review of user studies and experiments) [1, 6] |
| **Amostra** | 12 published peer-reviewed studies selected from digital libraries [7] |
| **Contexto** | Mixed (Industry and academic studies involving varied developer experience) [8] |
| **Modo de trabalho** | Not specified [6, 7] |
| **Metodologia** | Not specified [7] |

---

## Objetivo

O objetivo principal deste artigo é avaliar estudos de usuários e pesquisas recentes focados na experiência do desenvolvedor ao utilizar Large Language Models (LLMs) para codificação, utilizando o framework SPACE para categorizar métricas e identificar lacunas na literatura atual [1, 6]. O estudo busca entender como a produtividade e a experiência do desenvolvedor são medidas no contexto de Generative AI (GenAI) e propor recomendações para a padronização dessas avaliações [1, 9].

---

## Questoes de Pesquisa

Embora o artigo não apresente questões de pesquisa numeradas formalmente, ele foca em abordar os seguintes problemas:
- **RQ1**: Existe uma falta de padronização ou categorização nos estudos de produtividade de desenvolvedores usando GenAI? [6, 10]
- **RQ2**: Quais são os vieses predominantes nos estudos atuais em relação às dimensões da experiência do desenvolvedor? [6, 10]
- **RQ3**: Qual é a variância das métricas utilizadas entre diferentes dimensões de produtividade? [6, 10]

---

## Metricas e Instrumentos de Avaliacao

O artigo compila uma vasta lista de métricas extraídas dos estudos revisados, categorizando-as pelas dimensões do framework SPACE [11, 12].

| Metrica | Categoria | Nivel | Como Coletada | Validada |
|---------|-----------|-------|---------------|----------|
| Halstead Metrics (Vocabulary, Volume, Difficulty) | Satisfaction (Dev Efficacy) | Individual | Automated code analysis [5, 12] | Yes (Standard) [13] |
| Cognitive Load | Satisfaction | Individual | Eye-tracking / Surveys [12, 14] | Partial [13] |
| Fixation Count / Duration | Satisfaction (Trust) | Individual | Eye-tracking devices [5, 12] | Yes [13] |
| CWEs per LoC / Function | Performance (Quality) | Individual | Security scanning tools [12, 15] | Yes (Standard) [13] |
| pass@k | Performance (Quality) | Individual | Functional test execution [2, 12] | Yes (Standard) [13] |
| BLEU / ROUGE-L / METEOR | Performance (Quality) | Individual | Textual similarity tools [12, 16] | Yes (Standard) [13, 16] |
| Acceptance Rate / Persistence Rate | Activity | Individual | IDE Telemetry [4, 12, 17] | Partial [13] |
| Task Completion Times | Efficiency (Flow) | Individual | Controlled user experiments [12, 18] | Yes [13] |
| Prompting / Validation Strategy Time | Efficiency | Individual | Observation / Log analysis [1, 19] | Partial [13] |
| MS VS Maintainability Index | Performance (Reliability) | Individual | Visual Studio Metrics [5, 12] | Yes (Standard) [5, 13] |

---

## Frameworks e Metricas

### Frameworks Referenciados
- **SPACE**: APPLIED — Utilizado como a lente principal para categorizar métricas e analisar lacunas nos estudos de GenAI [1, 6, 11].
- **DORA**: REFERENCED — Citado como um framework relevante para a produtividade de desenvolvedores [11].

### Frameworks Propostos
O artigo não propõe um framework inteiramente novo, mas recomenda a criação de um framework categórico mais amplo que o SPACE no futuro para capturar métricas específicas de performance e segurança de GenAI de forma mais eficiente [9, 20].

---

## Fatores que Influenciam Produtividade

### Fatores Positivos
| Fator | Categoria |
|-------|-----------|
| Minimal friction in task completion | Process [1] |
| High Trust in tool outputs | Human [17] |
| Effective Prompting Strategies | Technical [19] |

### Fatores Negativos
| Fator | Categoria |
|-------|-----------|
| High Cognitive Load | Human [17] |
| Increased code complexity | Technical [17] |
| Lack of Team Collaboration insights | Organizational [21] |

---

## Papel da IA e Automacao

| Campo | Valor |
|-------|-------|
| Usa IA/ML? | Yes — O foco é a avaliação de LLMs como GitHub Copilot, Codex e Code Llama [2, 15, 22]. |
| Automacao de coleta? | Yes — As métricas são coletadas via telemetria de IDE e ferramentas automáticas de análise de código [12, 13]. |
| Impacto de IA na produtividade? | LLMs auxiliam na produtividade individual, mas há falhas em áreas específicas do SDLC e na experiência do desenvolvedor [1]. |

---

## Resultados Principais

- **Lacuna em Colaboração**: Ausência total de estudos de usuários focados na dimensão "Collaboration and Communication" do SPACE no contexto de GenAI [1, 9, 21].
- **Vies de Ferramentas**: A maioria dos estudos foca quase exclusivamente na família de modelos Codex e no GitHub Copilot, ignorando dezenas de outros modelos disponíveis [22].
- **Foco em Qualidade de Código**: Na dimensão "Performance", a vasta maioria das métricas foca em qualidade (como BLEU ou vulnerabilidades) em detrimento de confiabilidade e manutenibilidade [23].
- **Tamanho da Amostra**: A maioria dos experimentos controlados revisados possui um tamanho de amostra médio de 30 participantes [8].

---

## Desafios do Uso das Metricas

- **Falta de Padronização**: Grande variância nas métricas utilizadas entre diferentes estudos, dificultando comparações equitativas [9, 11].
- **Correlação Fraca**: Algumas métricas comuns têm correlação fraca com o julgamento humano de qualidade [9].
- **Vies de Dimensão**: Concentração excessiva em produtividade individual, obscurecendo impactos na dinâmica de equipe [21].

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

- O survey focou apenas em estudos que conduziram experimentos controlados ou pesquisas com usuários, podendo omitir outros tipos de análise [6].
- A categorização de métricas no framework SPACE foi mantida como mutuamente exclusiva para fins de análise, embora algumas métricas possam sobrepor dimensões na realidade [24].

---

## Contribuicao Principal

A principal contribuição deste trabalho é a sistematização crítica das métricas de GenAI sob a ótica do framework SPACE, revelando que a pesquisa atual negligencia severamente os aspectos colaborativos do desenvolvimento de software assistido por IA [1, 21]. O artigo fornece recomendações práticas para que a comunidade de pesquisa diversifique as ferramentas avaliadas e padronize métricas para permitir uma avaliação mais holística e reprodutível do impacto da IA no desenvolvimento [9, 25].

---

*Extraido via NotebookLM em March 2026 para MLR: Software Developer Metrics in Practice*
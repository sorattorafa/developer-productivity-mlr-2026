# P0028 — Fair Developer Score: Build-Adjusted Measurement of Effort and Impact

**Decisao: INCLUIDO | Qualidade: 5/5**

---

## Dados Bibliograficos

| Campo | Valor |
|-------|-------|
| **ID** | P0028 |
| **Autores** | Xinzhou Wang, Jiancong Zhu, Jinghan Feng, Zixuan Zhang, Joshua Rauvola, Devon Delgado, Ahmad Antar, Abid Ali [1] |
| **Ano** | 2025 [2] |
| **Venue** | 30th International Conference on Software Engineering (ICSE ’08) - *Note: Reference list citation [3], but copyright and DOI indicate IEEE 2025 and ASEW* [2] |
| **DOI** | 10.1109/ASEW67777.2025.00054 [2] |
| **Tipo** | Conference paper [2] |
| **Metodo** | Repository mining, Quantitative analysis [1, 4, 5] |
| **Amostra** | 339 contributors (Linux Kernel) and data from Kubernetes, TensorFlow, Apache Kafka, and PostgreSQL [6, 7] |
| **Contexto** | Open-source software (OSS) projects spanning different domains like OS Kernel, ML frameworks, and databases [1, 7] |
| **Modo de trabalho** | Not specified [8, 9] |
| **Metodologia** | Not specified [8, 9] |

---

## Objetivo

O principal objetivo do artigo é introduzir o **Fair Developer Score (FDS)**, um framework analítico centrado em commits que utiliza técnicas de clustering para agrupar logs de commits dispersos em unidades de trabalho coerentes chamadas **builds** [1]. O sistema visa fornecer uma medição de produtividade que equilibre o esforço individual (**developer effort**) com o impacto organizacional e sistêmico do trabalho (**build importance**), utilizando apenas dados de metadados de sistemas de controle de versão [1, 10, 11].

---

## Questoes de Pesquisa

Embora não listadas explicitamente como "RQ", os objetivos de validação do estudo buscam responder:
*   **RQ1:** O FDS captura de forma confiável tanto o esforço quantitativo quanto a significância contextual das atividades do desenvolvedor? [12]
*   **RQ2:** Como o ranking do FDS se compara a medidas tradicionais de produtividade, como contagem de commits e *churn*? [13]
*   **RQ3:** O framework FDS é generalizável e estável em diferentes repositórios e contextos de desenvolvimento? [9, 14]

---

## Metricas e Instrumentos de Avaliacao

| Metrica | Categoria | Nivel | Como Coletada | Validada |
|---------|-----------|-------|---------------|----------|
| **Commit Count** | Activity | Individual | Metadata from Git repository [15, 16] | Yes [13] |
| **Lines of Code (LOC) / Churn** | Activity | Individual | Metadata (lines added/deleted) [1, 16, 17] | Yes [13, 18] |
| **Effort Score** | Productivity | Individual | Composite of Scale, Reach, Centrality, Dominance, Novelty, and Speed [19] | Yes [5, 20] |
| **Build Importance** | Delivery/Value | Team/Build | Composite of Scale, Scope, Centrality, Complexity, Type, and Release [21] | Yes [5, 20] |
| **Fair Developer Score (FDS)** | Productivity | Individual | Sum of (Effort * Importance) across all builds [16, 22] | Yes [23, 24] |
| **Rework Ratio** | Quality | Individual | Frequency of revisiting the same directory within 48h [23, 25] | Yes [24, 25] |
| **Rollback Rate** | Quality | Individual | Commits containing 'revert' in the subject line [23, 25] | Yes [24, 25] |
| **DORA Metrics** | Delivery | Team | Mentioned as industry standard (Deployment Frequency, etc.) [26] | Yes [15, 26] |

---

## Frameworks e Metricas

### Frameworks Referenciados
*   **DORA (DevOps Research and Assessment):** REFERENCED (discutido como um índice macro de eficácia DevOps, mas com déficit de granularidade para indivíduos) [26, 27].
*   **SPACE Framework:** REFERENCED (citado como um modelo de produtividade de múltiplas dimensões que alerta contra o uso de métricas únicas) [8, 27, 28].
*   **DevEx (Developer Experience):** REFERENCED (discutido em relação a loops de feedback, carga cognitiva e estado de fluxo) [8, 28, 29].

### Frameworks Propostos
*   **Fair Developer Score (FDS) / Programmer Productivity Measurement (PPM) system:** O artigo propõe este framework que utiliza o algoritmo **Torque Clustering** para agrupar commits em *builds* e aplica um modelo de pontuação multidimensional para avaliar o esforço e a importância do trabalho [10, 11, 16].

---

## Fatores que Influenciam Produtividade

### Fatores Positivos
| Fator | Categoria |
|-------|-----------|
| **Modern Tooling** | Technical [30] |
| **Well-Architected Codebase** | Technical [30] |
| **Developer Satisfaction/Happiness** | Human [31, 32] |
| **AI Coding Assistants (e.g., Copilot)** | Technical (increases task completion speed) [33] |

### Fatores Negativos
| Fator | Categoria |
|-------|-----------|
| **Technical Debt / Legacy Code** | Technical [30, 33] |
| **Poor Software Architecture** | Technical [30] |
| **Information Discovery Difficulty** | Process [30] |
| **Excessive Dependencies** | Technical/Process [30] |
| **Inadequate Engineering Tools** | Technical [30] |

---

## Papel da IA e Automacao

| Campo | Valor |
|-------|-------|
| **Usa IA/ML?** | Yes — utiliza um classificador de mensagens de commit (semantic-aware classifier) para determinar a prioridade da tarefa e o tipo de build [21]. |
| **Automacao de coleta?** | Yes — o sistema PPM automatiza a coleta e o processamento de metadados de commits do Git [4, 8, 11]. |
| **Impacto de IA na produtividade?** | O artigo cita que assistentes de IA podem acelerar a conclusão de tarefas em 40%, mas podem impactar negativamente a qualidade do código e aumentar a dívida técnica [33]. |

---

## Resultados Principais

*   **Diferenciação de Contribuidores:** O FDS identificou uma distribuição "long-tailed" (skewed), diferenciando efetivamente os mantenedores principais (core maintainers) de contribuidores periféricos no Kernel do Linux (mediana de 0.35, máximo de 210.17) [6, 34].
*   **Superioridade sobre Métricas Simples:** Desenvolvedores classificados pelo FDS exibiram **Average Importance** (+0.314) e **Average Effort** (+0.079) significativamente maiores do que pares com o mesmo volume de commits e *churn* [1, 23].
*   **Qualidade do Código:** Desenvolvedores com alto FDS mostraram tendências de menor retrabalho (**lower rework**) em comparação com desenvolvedores focados apenas em volume [1, 23].
*   **Generalização:** A métrica de **Effort** mostrou-se consistente em todos os repositórios testados (Linux, Kubernetes, TensorFlow, Kafka, PostgreSQL), enquanto o **Importance** mostrou-se sensível ao contexto do projeto [7, 35].

---

## Desafios do Uso das Metricas

*   **Anti-padrão de Volume:** O artigo critica o uso de contagem de commits e LOC por falharem em capturar a substância e a complexidade lógica das contribuições [15, 18, 22].
*   **Gaming Behaviors:** O risco de desenvolvedores otimizarem suas ações para a métrica em vez da produtividade real (Goodhart's Law) [36].
*   **Invisibilidade de Tarefas não-Coding:** A dependência exclusiva de dados de commit ignora atividades cruciais como revisão de código, mentoria e planejamento arquitetônico [36].
*   **Heterogeneidade Contextual:** Métricas de importância podem exigir ajustes específicos para diferentes domínios e fluxos de trabalho [35, 37].

---

## Avaliacao de Qualidade Metodologica

| Criterio | Pontuacao (0-2) |
|----------|----------------|
| Objetivo claramente definido | 2 [1, 11] |
| Metodologia adequada ao objetivo | 2 [13, 16] |
| Amostra/contexto descrito adequadamente | 2 [7, 38] |
| Ameacas a validade discutidas | 2 [8, 9, 30, 31, 36, 39, 40] |
| Resultados com evidencia suficiente | 2 [20, 23] |
| Contribuicao clara para pratica ou teoria | 2 [1, 41] |
| **TOTAL** | **12/12** |

---

## Limitacoes

*   **Natureza Criativa:** O framework foca em sinais quantitativos e pode não capturar aspectos criativos e de resolução de problemas arquitetônicos complexos [39].
*   **Fatores Ambientais:** O FDS não isola a produtividade de impedimentos externos como dívida técnica pré-existente ou ferramentas inadequadas [30].
*   **Ausência de Bem-estar:** Não incorpora indicadores de satisfação ou experiência do desenvolvedor (DevEx), o que pode levar a uma visão incompleta de sustentabilidade [8, 31].
*   **Calibração de Parâmetros:** O uso de heurísticas para os parâmetros do *Torque Clustering* e pesos do modelo pode introduzir viés [40, 42].

---

## Contribuicao Principal

A contribuição principal é o desenvolvimento de um **framework de medição de produtividade automatizado e escalável** que utiliza apenas metadados de commits existentes em repositórios Git [1, 4, 8]. Ao agrupar commits em *builds* e ponderar o esforço pelo impacto sistêmico, o FDS oferece uma alternativa mais justa e precisa do que as métricas de volume tradicionais, permitindo que organizações identifiquem e recompensem contribuições estrategicamente significativas sem a necessidade de ferramentas de rastreamento intrusivas [11, 43, 44].

---

*Extraido via NotebookLM em March 2026 para MLR: Software Developer Metrics in Practice*
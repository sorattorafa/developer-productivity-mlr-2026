# P0481 — On the Relationship Between Developer Experience and Refactoring: An Exploratory Study and Preliminary Results

**Decisao: INCLUIDO | Qualidade: 5/5**

---

## Dados Bibliograficos

| Campo | Valor |
|-------|-------|
| **ID** | P0481 |
| **Autores** | Eman Abdullah AlOmar, Anthony Peruma, Christian D. Newman, Mohamed Wiem Mkaouer, Ali Ouni |
| **Ano** | 2020 |
| **Venue** | IEEE/ACM 42nd International Conference on Software Engineering Workshops (ICSEW’20) |
| **DOI** | https://doi.org/10.1145/3387940.3392193 |
| **Tipo** | Conference paper |
| **Metodo** | Mixed methods (Repository mining, Quantitative analysis, and Qualitative manual analysis) |
| **Amostra** | 800 open-source Java projects, 748,001 commits, and 711,495 refactoring operations |
| **Contexto** | OSS (Open Source Software) well-engineered Java projects hosted on GitHub |
| **Modo de trabalho** | Not specified |
| **Metodologia** | Not specified |

---

## Objetivo

O principal objetivo do estudo é explorar a relação entre a **experiência do desenvolvedor** e as **atividades de refatoração**, testando a hipótese de que desenvolvedores com níveis de experiência mais elevados tendem a realizar um maior número de operações de refatoração em comparação com desenvolvedores menos experientes [1, 2]. O trabalho busca expandir e generalizar resultados de estudos anteriores que eram limitados a poucos projetos ou empresas específicas [1, 2].

---

## Questoes de Pesquisa

*   **RQ1.** What is the distribution of experience among developers that perform refactorings? [3]
*   **RQ2.** Would higher experience indicate higher refactoring activities? [4]

---

## Metricas e Instrumentos de Avaliacao

| Metrica | Categoria | Nivel | Como Coletada | Validada |
|---------|-----------|-------|---------------|----------|
| **Developer’s Commit Ratio (DCR)** | Activity / Experience Proxy | Individual | Calculada como a razão entre os commits individuais do autor e o total de commits do projeto [5]. | Yes (utilizada em estudos prévios [5, 6]) |
| **Refactoring Count** | Activity | Individual | Detecção automática de operações de refatoração no histórico de commits via tool **RefactoringMiner** [7, 8]. | Yes (ferramenta com 98% de precisão [8]) |
| **Refactoring Ratio** | Activity | Individual | Porcentagem de refatorações em *production code* vs *test code* por desenvolvedor [9]. | No (métrica descritiva) |

---

## Frameworks e Metricas

### Frameworks Referenciados
*   **Developer Experience (DevEx):** REFERENCED — O conceito de experiência do desenvolvedor é o foco central do estudo, correlacionando-o com a prática de manutenção [10-12].
*   **Quality Models:** REFERENCED — O estudo cita a relação entre refatoração e modelos de qualidade de design [13].

### Frameworks Propostos
O artigo não propõe um novo framework, mas utiliza o **Developer’s Commit Ratio (DCR)** como um modelo automatizado e escalável para estimar a experiência de desenvolvedores em projetos de software [5, 14].

---

## Fatores que Influenciam Produtividade

### Fatores Positivos
| Fator | Categoria |
|-------|-----------|
| **Nível de Experiência (DCR elevado)** | Human |
| **Papéis de Liderança (Senior/Lead)** | Organizational |
| **Conhecimento extensivo do Design do sistema** | Human |

### Fatores Negativos
| Fator | Categoria |
|-------|-----------|
| **Restrições técnicas (falta de suporte de ferramentas)** | Technical |
| **Falta de confiança em automação de refatorações compostas** | Human / Technical |
| **Falta de conhecimento funcional (risco de introdução de bugs)** | Human |

---

## Papel da IA e Automacao

| Campo | Valor |
|-------|-------|
| Usa IA/ML? | No — O estudo utiliza a ferramenta **RefactoringMiner**, que é baseada em regras e análise estática de código para detecção [7]. |
| Automacao de coleta? | Yes — A coleta de dados de 800 repositórios e a identificação de 711.495 refactorings foram totalmente automatizadas via scripts e ferramentas de mineração [8, 14, 15]. |
| Impacto de IA na produtividade? | N/A — O estudo não avalia o impacto de ferramentas de IA na produtividade. |

---

## Resultados Principais

*   Desenvolvedores que realizam refatoração possuem um **DCR médio significativamente superior** (0.0456) em comparação com desenvolvedores que realizam apenas commits sem refatoração (0.0031) [16].
*   O **TOP-5%** de desenvolvedores mais experientes realiza, em média, **70.24 commits de refatoração**, enquanto os demais (95%) realizam uma média de apenas 3.21 commits desta natureza [17].
*   Embora a refatoração não seja restrita a um subgrupo, uma **minoria de desenvolvedores experientes monopoliza** a maioria das atividades de refatoração tanto em código de produção quanto em código de teste [1, 18, 19].
*   A análise qualitativa confirmou que os principais contribuidores de refatoração em projetos como Hadoop, OrientDB e Camel ocupam cargos de **líderes de desenvolvimento ou desenvolvedores seniores** [20].

---

## Desafios do Uso das Metricas

*   **Subjetividade da Experiência:** Medir a experiência real de um desenvolvedor é desafiador; o estudo utiliza DCR como um *proxy*, o que pode não capturar a experiência externa ao projeto [21, 22].
*   **Falsos Negativos em Refatoração:** Dependência da precisão da ferramenta de mineração para identificar as atividades corretamente [23].

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

*   O estudo é restrito a projetos de código aberto (OSS) escritos em **Java** e baseados em Git [24].
*   A medição de experiência (DCR) assume que quanto mais tempo e volume de contribuição no projeto, mais experiente o desenvolvedor se torna, o que pode ter exceções [22].
*   A ferramenta **RefactoringMiner**, embora precisa, pode omitir tipos de refatoração não suportados ou falhar em casos complexos [21, 23].

---

## Contribuicao Principal

A principal contribuição deste estudo é a validação, em larga escala e de forma automatizada, da hipótese de que a **refatoração é uma atividade predominantemente executada por desenvolvedores experientes e com papéis de liderança** [14, 20, 25]. Ao utilizar uma métrica objetiva (DCR) em vez de apenas questionários subjetivos, os autores fornecem um método escalável para identificar desenvolvedores adequados para tarefas críticas de manutenção e evolução de software [14, 26].

---

*Extraido via NotebookLM em March 2026 para MLR: Software Developer Metrics in Practice*
# P0546 — Analyzing and repairing compilation errors

**Decisao: INCLUIDO | Qualidade: 4.5/5**

---

## Dados Bibliograficos

| Campo | Valor |
|-------|-------|
| **ID** | P0546 |
| **Autores** | Ali Mesbah, Andrew Rice, Edward Aftandilian, Emily Johnston, Nick Glorioso [1] |
| **Ano** | 2018 (Data de coleta iniciada em Janeiro de 2018) [2] |
| **Venue** | Not specified (Authors affiliated with Google, University of British Columbia, and University of Cambridge) [1] |
| **DOI** | Not specified |
| **Tipo** | Conference paper [1, 3] |
| **Metodo** | Repository mining e Experiment [2, 4] |
| **Amostra** | 4.8 milhões de builds e 1.85 milhão de diagnostics analisados ao longo de dois meses [5, 6] |
| **Contexto** | Industry (Google) [1, 2] |
| **Modo de trabalho** | Not specified |
| **Metodologia** | Not specified |

---

## Objetivo

O objetivo principal do artigo é desenvolver ferramentas de reparo automatizado que possam resolver erros de compilação (*build errors*) automaticamente para melhorar a produtividade dos desenvolvedores [1]. Para isso, os autores quantificam o tempo gasto pelos desenvolvedores resolvendo diferentes tipos de diagnósticos e propõem um modelo de tradução automática para sugerir correções [7, 8].

---

## Questoes de Pesquisa

* **RQ1:** Quanto tempo os desenvolvedores gastam resolvendo diferentes tipos de diagnósticos de compilação no Google? [7]
* **RQ2:** Qual o impacto da escolha da ferramenta (IDE vs. Command Line) na taxa de falha de builds? [5, 7]
* **RQ3:** É possível utilizar modelos de *Neural Machine Translation* para gerar reparos corretos para erros de símbolos não resolvidos? [4, 7]

---

## Metricas e Instrumentos de Avaliacao

| Metrica | Categoria | Nivel | Como Coletada | Validada |
|---------|-----------|-------|---------------|----------|
| Active Resolution Cost (ARC) | Productivity/Activity | Individual/Team | Calculada como o tempo total entre builds em uma *resolution session* dividido pelo número de diagnósticos presentes [5] | No (Definição customizada para o estudo) |
| True Positive Rate (Repair Rate) | Quality/Automation | Individual/System | Porcentagem de reparos corretos gerados pelo modelo em relação ao conjunto de teste [4, 7] | Yes |
| Build Failure Rate | Quality | Organization | Proporção de builds que resultaram em erro em relação ao total de builds logados [5, 7] | Yes |

---

## Frameworks e Metricas

### Frameworks Referenciados
* **DeepDelta:** REFERENCED (Linguagem customizada para descrever mudanças na *Abstract Syntax Tree*) [4].

### Frameworks Propostos
O artigo propõe um pipeline de reparo baseado em **Neural Machine Translation** aplicado a mudanças na AST, utilizando a linguagem **DeepDelta** para representar as falhas e suas resoluções [4].

---

## Fatores que Influenciam Produtividade

### Fatores Positivos
| Fator | Categoria |
|-------|-----------|
| Uso de IDEs (IntelliJ/Android Studio) | Technical |
| Ferramentas de reparo automatizado | Technical |

### Fatores Negativos
| Fator | Categoria |
|-------|-----------|
| Builds via Command-line (maior taxa de falha) | Technical |
| Erros de símbolos não resolvidos (*cant.resolve*) | Technical/Process |
| Task switching (interrupções durante a resolução) | Process |

---

## Papel da IA e Automacao

| Campo | Valor |
|-------|-------|
| Usa IA/ML? | Yes — Foi treinado um modelo de *Neural Machine Translation* em mudanças de AST para resolver falhas de símbolos [4, 7]. |
| Automacao de coleta? | Yes — Todos os builds iniciados por desenvolvedores no Google são logados automaticamente com mensagens de erro e snapshots de código [2]. |
| Impacto de IA na produtividade? | O modelo gerou reparos corretos em 50% dos casos, com o reparo correto presente no top 3 em 87% das vezes, reduzindo o esforço manual [4]. |

---

## Resultados Principais

* Aproximadamente **20% de todos os builds** no Google (1.0 milhão de 4.8 milhões) resultam em falha [5].
* O diagnóstico de símbolo não resolvido (*cant.resolve*) é responsável por **47% do tempo total** gasto resolvendo falhas de build [7, 9].
* Existe uma disparidade significativa entre ferramentas: **26% dos builds via linha de comando falham**, enquanto apenas **3% dos builds via IDE falham** [5, 7, 9].
* O modelo de IA proposto previu o reparo correto para o erro mais comum em **50% das tentativas** [4, 10].

---

## Desafios do Uso das Metricas

* **Task Switching:** É difícil medir o tempo real de produtividade se o desenvolvedor mudar de tarefa entre os builds; os autores usaram uma janela de uma hora para mitigar isso [11].
* **Atribuição de Esforço:** Quando múltiplos diagnósticos ocorrem simultaneamente, é difícil saber quanto tempo foi dedicado a cada um (o ARC divide o tempo igualmente) [5].
* **Granularidade:** Commits em repositórios são considerados muito grosseiros (*coarse-grained*) para capturar a resolução de erros de compilação [10].

---

## Avaliacao de Qualidade Metodologica

| Criterio | Pontuacao (0-2) |
|----------|----------------|
| Objetivo claramente definido | 2 |
| Metodologia adequada ao objetivo | 2 |
| Amostra/contexto descrito adequadamente | 2 |
| Ameacas a validade discutidas | 1 |
| Resultados com evidencia suficiente | 2 |
| Contribuicao clara para pratica ou teoria | 2 |
| **TOTAL** | **11/12** |

---

## Limitacoes

* O dataset utilizado é **proprietário do Google**, o que dificulta a reprodutibilidade por pesquisadores externos [10].
* Os logs registram se a ferramenta foi IDE ou Console, mas não especificam o **editor de texto** utilizado para alterar os arquivos [5].
* O cálculo do ARC assume uma **distribuição igual de esforço** entre diagnósticos quando múltiplos erros aparecem no mesmo build [5].

---

## Contribuicao Principal

A contribuição principal do artigo é a quantificação em larga escala do custo de erros de compilação em um ambiente industrial, identificando que a resolução de símbolos é o gargalo mais significativo, e a demonstração de que modelos de tradução neural podem automatizar o reparo desses erros com alta eficácia [7, 10].

---

*Extraido via NotebookLM em March 2026 para MLR: Software Developer Metrics in Practice*
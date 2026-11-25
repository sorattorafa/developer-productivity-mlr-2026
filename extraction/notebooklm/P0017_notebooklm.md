# P0017 — Organizational Ohm's Law in Practice: Measuring Engineering Productivity

**Decisao: INCLUIDO | Qualidade: 5/5**

---

## Dados Bibliograficos

| Campo | Valor |
|-------|-------|
| **ID** | P0017 |
| **Autores** | Fei Liu, Todd McKinnon |
| **Ano** | 2024 |
| **Venue** | IEEE Transactions on Engineering Management |
| **DOI** | 10.1109/TEM.2024.3421892 |
| **Tipo** | Journal article |
| **Metodo** | Quantitative deductive approach with cross-sectional case studies |
| **Amostra** | 4 software product development projects |
| **Contexto** | Industry — Okta Inc., an enterprise software company |
| **Modo de trabalho** | Not specified |
| **Metodologia** | Agile and DevOps (referenced as general context) |

---

## Objetivo

O principal objetivo do artigo é explorar quantitativamente o uso da **Organizational Ohm’s Law (OOL)** para medir a produtividade na engenharia de software [1]. Os autores buscam derivar uma equação mensurável para essa lei, identificar métricas práticas para suas variáveis e validar o modelo através do estudo de quatro projetos reais de desenvolvimento de produtos em larga escala [1-3].

---

## Questoes de Pesquisa

Embora não listadas formalmente como "RQ", o estudo foca em:
- **RQ1:** Como derivar uma equação quantitativa utilizável para a Organizational Ohm’s Law? [3, 4]
- **RQ2:** O modelo OOL é estatisticamente válido para medir tanto a produção técnica (output) quanto o impacto de negócio (outcome)? [3, 5]

---

## Metricas e Instrumentos de Avaliacao

| Metrica | Categoria | Nivel | Como Coletada | Validada |
|---------|-----------|-------|---------------|----------|
| **Lines of Code (LOC)** | Output/Productivity | Team | Extração de Git repositories (incluindo código fonte, testes e comentários) [6, 7] | Yes [8] |
| **Usage-based business impact** | Outcome | Organization | Logs de sistema contando o número de organizações que utilizam a feature, descontados a uma taxa anual de 12% [9, 10] | Yes [11] |
| **Engineer Time Allocation** | Activity/Process | Team | Questionário preenchido por líderes de engenharia sobre a porcentagem de tempo em atividades (coding, meetings, etc.) [12, 13] | Yes [8, 11] |
| **Engineer Motivation** | Satisfaction/Human | Team | Escala subjetiva de 0–5 avaliada por líderes de projeto [13] | Yes [8, 11] |
| **Engineer Skills** | DevEx/Human | Team | Escala subjetiva de 0–5 (técnica e não-técnica) avaliada por líderes de projeto [13] | Yes [8, 11] |
| **Outcome–output alignment** | Alignment/Value | Project | Pesquisa anual de inovação com o time de vendas (escala 0-5) para medir o valor percebido pelo cliente [14, 15] | Yes [11] |

---

## Frameworks e Metricas

### Frameworks Referenciados
- **DORA (DevOps Research and Assessment):** REFERENCED (citado como métricas de DevOps) [16, 17].
- **SPACE:** REFERENCED (citado como método multidimensional) [16, 18].
- **COCOMO / COCOMO II:** REFERENCED (citado para estimativa de custo e calibração) [19-21].
- **Balanced Scorecard:** REFERENCED (citado para definição de metas e perspectivas de negócio) [17, 19, 22].
- **Conway’s Law:** REFERENCED [23].
- **Agile @Spotify:** REFERENCED [12, 16].

### Frameworks Propostos
O artigo propõe a **Quantitative Organizational Ohm’s Law (OOL)**. O framework modela a produtividade como sendo diretamente proporcional à eficiência entre outcome/output e ao potencial organizacional (motivação e habilidades), e inversamente proporcional à resistência organizacional (tempo gasto em processos, infraestrutura ineficiente e overhead de colaboração) [1, 24, 25].

---

## Fatores que Influenciam Produtividade

### Fatores Positivos
| Fator | Categoria |
|-------|-----------|
| **High Engineer Skills** | Human [13, 26] |
| **High Engineer Motivation** | Human [13, 26] |
| **Outcome-Output Alignment** | Organizational [15, 27] |
| **Microservices/Macroservices architecture** | Technical (reduz acoplamento e overhead de comunicação) [28] |

### Fatores Negativos
| Fator | Categoria |
|-------|-----------|
| **Collaboration Resistance** | Organizational (overhead de comunicação e dependências) [22] |
| **Process Resistance** | Process (burocracia da empresa ou processos de engenharia) [22] |
| **Infrastructure Resistance** | Technical (ferramentas e infraestrutura ineficientes) [22] |
| **Decision Waiting** | Process [13] |

---

## Papel da IA e Automacao

| Campo | Valor |
|-------|-------|
| Usa IA/ML? | **Yes** — O artigo discute o potencial da IA Generativa em melhorar a produtividade, especialmente para programadores novatos [29]. |
| Automacao de coleta? | **No** — A coleta neste estudo foi manual via questionários, embora os autores citem que ferramentas como Git e Jira podem automatizar isso no futuro [30]. |
| Impacto de IA na produtividade? | O artigo nota que a IA pode alterar a limitação hipotética da produtividade individual, mas as implicações reais em larga escala ainda não estão claras [29]. |

---

## Resultados Principais

- **Validação Estatística:** O modelo OOL foi validado com significância estatística (p-value < 0.05) tanto para cenários de output (LOC) quanto de outcome (business impact) [8, 11].
- **Correlação Linear:** O R-square para a relação de output de código foi de **0.969**, enquanto para o impacto de negócio foi de **0.976** [8, 11].
- **Limitação de Produtividade (k):** A constante *k* (limite hipotético da produtividade individual) foi calculada em aproximadamente **20.400 LOC por engenheiro por ano** [8, 31].
- **Arquitetura:** O uso de microserviços e macroserviços tendeu a aumentar o volume de LOC por engenheiro ao reduzir a necessidade de coordenação entre times [28].

---

## Desafios do Uso das Metricas

- **Esforço Operacional:** Coletar dados empíricos reais exige esforço significativo e pode ser visto como monitoramento de funcionários [20].
- **Dados Históricos:** É difícil obter dados históricos retroativos através de ferramentas automatizadas, exigindo questionários com líderes [30, 32].
- **Complexidade de Atribuição:** Isolar a contribuição de receita de uma única feature em pacotes de preços complexos é um desafio [9].

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

- **Tamanho da Amostra:** O estudo utilizou apenas quatro projetos de uma única empresa, o que limita a generalização total do modelo [33].
- **Escopo Temporal:** O estudo focou do início do projeto até o General Availability (GA), ignorando o trabalho de pré-priorização e manutenção pós-lançamento [17, 34].
- **Variáveis de Segunda Ordem:** Fatores como linguagens de programação e arquitetura de software foram simplificados ou ignorados na equação linear básica [33].

---

## Contribuicao Principal

A principal contribuição é a **transformação de um conceito qualitativo (Organizational Ohm's Law) em um modelo quantitativo e formulável** que permite a gestores de engenharia entenderem matematicamente como as melhorias em habilidades, motivação e redução de atrito (resistência) impactam diretamente na velocidade de entrega de valor [2, 33, 35].

---

*Extraido via NotebookLM em March 2026 para MLR: Software Developer Metrics in Practice*
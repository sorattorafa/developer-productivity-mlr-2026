# P0412 — Organizational Ohm's Law—Case in Point: Engineering Velocity

**Decisao: INCLUIDO | Qualidade: 3/5**

---

## Dados Bibliograficos

| Campo | Valor |
|-------|-------|
| **ID** | P0412 |
| **Autores** | Fei Liu and Todd McKinnon [1], [2] |
| **Ano** | 2023 [2] |
| **Venue** | IEEE Transactions on Engineering Management [2] |
| **DOI** | 10.1109/TEM.2022.3232311 [2] |
| **Tipo** | Journal article [2] |
| **Metodo** | Mixed methods (Literature review, authors' observations, and qualitative interviews) [3], [4] |
| **Amostra** | More than 20 interviews with internal and external engineers, engineering managers, project managers, and product managers [4] |
| **Contexto** | Industry (Okta Inc. and other technology companies) [2], [4] |
| **Modo de trabalho** | Not specified [4] |
| **Metodologia** | Agile and DevOps [1], [3], [5] |

---

## Objetivo

O principal objetivo do artigo é propor um modelo descritivo geral, denominado **Organizational Ohm’s law**, para compreender a produtividade organizacional de forma holística [1]. O modelo busca integrar diversas partes móveis interdependentes para explicar como a **engineering velocity** é influenciada pelo potencial organizacional, eficiência e resistência [1], [6].

---

## Questoes de Pesquisa

O artigo não lista questões de pesquisa numeradas explicitamente, mas foca em:
- Como modelar a produtividade organizacional de forma intuitiva e eficaz [1], [7].
- Como os fatores de estrutura, processo e infraestrutura compõem a resistência organizacional [8], [9].
- De que forma o design organizacional pode ser mapeado para otimizar a velocidade de entrega [10], [11].

---

## Metricas e Instrumentos de Avaliacao

| Metrica | Categoria | Nivel | Como Coletada | Validada |
|---------|-----------|-------|---------------|----------|
| Outcome Current ($I_{outcome}$) | Productivity | Organization | Calculated via formula (Efficiency $\times$ Output Current) [12], [13] | No [14] |
| Output Current ($I_{output}$) | Activity / Delivery | Organization | Measured as output-based velocity [12], [13] | No [14] |
| Outcome-Output Efficiency ($\eta$) | Productivity | Organization | Ratio of outcome current to output current [12], [13] | No [14] |
| Organizational Potential ($V$) | DevEx / Human | Organization | Average of individual potential (Skills and Motivation) [13], [15] | No [14] |
| Organizational Resistance ($R$) | Process / Collaboration | Organization | Sum of structure, process, and infrastructure resistance [16], [8] | No [14] |
| Agile Velocity | Delivery | Team | Story points completed per sprint [5] | Referenced [5] |
| DevOps Metrics (DORA) | Delivery / Quality | Organization | Survey-based (Lead time, Deployment frequency, etc.) [3] | Referenced [3] |

---

## Frameworks e Metricas

### Frameworks Referenciados
- **OKRs (Objectives and Key Results)**: REFERENCED como metodologia de definição de metas [17].
- **DORA (DevOps metrics)**: REFERENCED para medir velocidade, eficiência e qualidade [3].
- **SPACE**: REFERENCED como método para avaliar produtividade do desenvolvedor [3].
- **Team Topologies**: REFERENCED para organização de times e fluxos rápidos [3], [9].
- **Conway’s Law / Inverse Conway Maneuver**: REFERENCED para alinhar estrutura organizacional e arquitetura [3], [18].

### Frameworks Propostos
- **Organizational Ohm’s Law**: Um framework inspirado na lei de Ohm da engenharia elétrica que define a velocidade organizacional ($I_{outcome}$) como proporcional à eficiência ($\eta$) e ao potencial ($V$), e inversamente proporcional à resistência ($R$) [1], [19]. O framework utiliza **equivalent circuits** para decompor e visualizar a resistência organizacional em diferentes cenários de interação entre times [6], [20].

---

## Fatores que Influenciam Produtividade

### Fatores Positivos
| Fator | Categoria |
|-------|-----------|
| Employee Skills (domain, time management, interpersonal) | Human [15] |
| Employee Motivation (culture, mission, incentives) | Human [16], [21] |
| Collaborative Culture | Organizational [8] |
| Loosely Coupled Architectures (microservices) | Technical [9], [22] |
| Single-threaded Leadership | Organizational [5], [23] |
| Self-service Infrastructure | Technical [24] |

### Fatores Negativos
| Fator | Categoria |
|-------|-----------|
| Structure Resistance (communication costs) | Organizational [8], [25] |
| Process Resistance (bureaucracy, ineffective procedures) | Process [8], [9] |
| Infrastructure Resistance (tech debt, slow CI/CD) | Technical [8], [9], [22] |
| Large Team Size (increases communication paths) | Organizational [24], [18] |
| Tightly Coupled Modules | Technical [23] |

---

## Papel da IA e Automacao

| Campo | Valor |
|-------|-------|
| Usa IA/ML? | No — IA é mencionada apenas como uma tecnologia emergente que exige atualização de habilidades dos engenheiros [21]. |
| Automacao de coleta? | No — O artigo foca na proposição teórica; a coleta quantitativa automatizada é sugerida como trabalho futuro [14]. |
| Impacto de IA na produtividade? | Not applicable — Não discutido como impacto direto no estudo [21]. |

---

## Resultados Principais

- A velocidade organizacional é inversamente proporcional à resistência, que cresce aproximadamente com o quadrado do tamanho do time devido aos caminhos de comunicação [24], [26].
- Adicionar pessoas a um projeto atrasado pode aumentar a resistência interestrutural, reduzindo a velocidade (alinhado à Lei de Brooks) [18], [27].
- A transição de arquiteturas monolíticas para microserviços reduz a **infrastructure resistance** e melhora a motivação dos engenheiros [22].
- Manter uma organização focada em um único objetivo por vez aumenta o potencial organizacional e a eficiência entre output e outcome [23], [11].
- O uso de **equivalent circuits** permite identificar se times devem trabalhar em paralelo (independente) ou série (dependente) para otimizar o fluxo [28], [29].

---

## Desafios do Uso das Metricas

- A dificuldade de compreender a produtividade de forma holística devido às muitas partes móveis interdependentes [1], [7].
- A complexidade de medir o **outcome-output efficiency**, dado que times precisam equilibrar novas funcionalidades com manutenção e suporte [5].
- O custo de comunicação (structure resistance) é difícil de quantificar e muitas vezes subestimado em grandes organizações [25], [18].

---

## Avaliacao de Qualidade Metodologica

| Criterio | Pontuacao (0-2) |
|----------|----------------|
| Objetivo claramente definido | 2 [1] |
| Metodologia adequada ao objetivo | 1 [4] |
| Amostra/contexto descrito adequadamente | 1 [4] |
| Ameacas a validade discutidas | 0 [30] |
| Resultados com evidencia suficiente | 1 [23], [22] |
| Contribuicao clara para pratica ou teoria | 2 [1], [26] |
| **TOTAL** | **7/12** |

---

## Limitacoes

O artigo reconhece que, no estágio atual, o framework é predominantemente qualitativo [14]. A extração quantitativa de valores para cada parâmetro da "Lei de Ohm Organizacional" e a validação empírica desses dados são citadas como foco de trabalhos futuros [14].

---

## Contribuicao Principal

A principal contribuição é a criação da **Lei de Ohm Organizacional**, que fornece um modelo mental intuitivo e uma ferramenta de simulação (circuitos equivalentes) para gestores de engenharia [1], [31]. O framework permite decompor problemas complexos de produtividade em variáveis gerenciáveis — potencial, eficiência e resistência — ajudando na análise de causa raiz e na previsão do impacto de mudanças estruturais na velocidade de engenharia [31], [26].

---

*Extraido via NotebookLM em March 2026 para MLR: Software Developer Metrics in Practice*
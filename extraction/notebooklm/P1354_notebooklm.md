# P1354 — The Effect of Artificial Intelligence Code Generation on Software Developer Productivity
**Decisão: INCLUÍDO | Qualidade: 5/5**

## Dados Bibliográficos
| Campo | Valor |
|-------|-------|
| **ID** | P1354 |
| **Autores** | Scott Morgan |
| **Ano** | 2025 |
| **Venue** | Tese de Doutorado - College of Business, Innovation, Leadership, and Technology |
| **DOI** | Não especificado nas fontes fornecidas. |
| **Tipo** | Tese (Dissertation) |
| **Método** | Estudo quantitativo, pesquisa causal-comparativa (análises confirmatórias, exploratórias e preditivas usando regressão linear e *Random Forest*). |
| **Amostra** | 32.981 desenvolvedores profissionais extraídos das pesquisas Stack Overflow Developer Surveys de 2023 e 2024. |
| **Contexto** | Dados de arquivo (*archival data*) de desenvolvedores profissionais de software em todo o mundo. |
| **Modo de trabalho** | Desenvolvedores atuando profissionalmente (empregados em tempo integral). |
| **Metodologia** | Estudo causal-comparativo utilizando grupos pré-existentes. A análise envolveu estatística descritiva, matriz de correlação, modelos de regressão linear múltipla para avaliar efeitos principais e moderadores, além de algoritmo de *Random Forest* para previsões. |

---

## Objetivo
Avaliar o impacto da geração de código por Inteligência Artificial na produtividade do desenvolvedor, medida como o tempo gasto na busca por soluções de programação, e compreender os fatores demográficos e profissionais que podem moderar essa relação.

---

## Questões de Pesquisa
*   **RQ1:** Como a geração de código por IA afeta a produtividade do desenvolvedor (tempo gasto procurando soluções de programação)?
*   **RQ2:** Alguma característica demográfica (ex: experiência, número de linguagens) modera o efeito da geração de código por IA no tempo gasto pesquisando respostas para perguntas de programação?
*   **RQ3:** Quais outros fatores contribuem para o efeito da geração de código por IA no tempo gasto pesquisando respostas para perguntas de programação?

## Métricas e Instrumentos de Avaliação

| Métrica | Categoria | Nível | Como Coletada | Validada |
|---------|-----------|-------|---------------|----------|
| **Tempo pesquisando respostas (TSX)** | Processo / Eficiência | Individual | Autorrelatada via Stack Overflow Developer Survey (Variável Dependente) | Sim (Dados de Arquivo) |
| **Uso de IA para Geração de Código (AID)** | Adoção Técnica | Individual | Autorrelatada via Stack Overflow Developer Survey (Variável Independente) | Sim (Dados de Arquivo) |
| **Experiência do Desenvolvedor** | Demográfica | Individual | Anos de experiência profissional relatados na pesquisa | Sim (Dados de Arquivo) |
| **Número de Linguagens Utilizadas** | Técnica | Individual | Quantidade de linguagens relatadas na pesquisa | Sim (Dados de Arquivo) |

## Frameworks e Métricas
### Frameworks Referenciados
*   **SPACE Framework:** (Satisfaction, Performance, Activity, Collaboration, and Efficiency) utilizado para conceituar a produtividade do desenvolvedor de forma multidimensional.
*   **DevEx Framework:** Focado na experiência do desenvolvedor, bem-estar e fluxo.

### Frameworks Propostos
*   O estudo não propõe um novo framework teórico, mas baseia-se em análises preditivas construídas a partir das variáveis do *Stack Overflow*.

---

## Fatores que Influenciam Produtividade
### Fatores Positivos
| Fator | Categoria |
|-------|-----------|
| **Maior experiência profissional:** Desenvolvedores mais experientes gastam intrinsecamente menos tempo procurando soluções. | Demográfica / Pessoal |
| **Uso de ferramentas de IA (para juniores):** A IA reduz significativamente o tempo de pesquisa para desenvolvedores com menos anos de experiência. | Technical / Interação |
| **Uso de linguagens específicas:** O uso primário de linguagens como Frontend JavaScript, PHP, Go e linguagens funcionais está associado a menor tempo de busca. | Technical |

### Fatores Negativos
| Fator | Categoria |
|-------|-----------|
| **Uso de múltiplas linguagens de programação:** Associado a um *aumento* no tempo de pesquisa, possivelmente devido à maior complexidade cognitiva e exigências de resolução de problemas. | Processo / Pessoal |
| **Frequência de interrupções:** Prejudica o fluxo cognitivo (context switching) e aumenta a necessidade de pesquisas. | Process / Ambiente |
| **Tamanho da organização:** Desenvolvedores em organizações maiores e mais estruturadas tendem a pesquisar de forma diferente ou ter necessidades que aumentam o tempo de busca. | Organizational |

---

## Papel da IA e Automação

| Campo | Valor |
|-------|-------|
| Usa IA/ML? | **Sim** — O estudo analisa ferramentas geradoras de código baseadas em IA (LLMs como GitHub Copilot, Codeium, Tabnine). A metodologia de pesquisa também emprega *Random Forest*, um modelo de Machine Learning, para predição e análise de importância de variáveis. |
| Automação de coleta? | **Não** — Utiliza bancos de dados de arquivo originados de pesquisas de autorrelato (*Stack Overflow Developer Surveys*). |
| Impacto de IA na produtividade? | **Misto / Moderado** — O uso de IA por si só não reduziu significativamente o tempo de busca de forma global na amostra. No entanto, seu impacto é fortemente moderado pela experiência: desenvolvedores menos experientes se beneficiam significativamente, experimentando uma redução real no tempo gasto pesquisando em comparação aos sêniores. O impacto também varia dependendo da demografia (população do país) e do ecossistema técnico do desenvolvedor. |

---
## Resultados Principais
*   **A hipótese de efeito direto (H1) não foi suportada:** O uso de ferramentas de geração de código de IA, isoladamente, não reduz de forma estatisticamente significativa o tempo que desenvolvedores profissionais gastam procurando soluções de programação.
*   **A experiência atua como um moderador vital (H2 suportada):** A eficiência ganha com a IA é inversamente proporcional à experiência. Desenvolvedores mais jovens ou menos experientes apresentaram reduções mais fortes no tempo de pesquisa ao usar ferramentas de IA.
*   **Múltiplas linguagens não ajudam com a IA (H3 não suportada):** Ao contrário do esperado, desenvolvedores familiarizados com mais linguagens de programação experimentaram um aumento no tempo de pesquisa ao usar IA, o que reflete desafios de complexidade.
*   **Preditores importantes:** A análise preditiva de *Random Forest* identificou a experiência do profissional, a frequência de interações (interrupções) e a população do país como os fatores mais influentes na predição do tempo de pesquisa.

## Desafios do Uso das Métricas
A produtividade do desenvolvedor é complexa e difícil de medir por meio de uma única métrica (como o uso de tempo de pesquisa ou linhas de código), requerendo uma abordagem multidimensional como a sugerida pelo framework SPACE para capturar a satisfação, o fluxo e a entrega de valor real, em vez de apenas velocidade. Depender apenas de dados autorrelatados no *Stack Overflow* sobre o uso do tempo impõe um limite natural de precisão às estimativas.

## Avaliação de Qualidade Metodológica

| Critério | Pontuação (0-2) |
|----------|----------------|
| Objetivo claramente definido | 2 |
| Metodologia adequada ao objetivo | 2 |
| Amostra/contexto descrito adequadamente | 2 |
| Ameaças à validade discutidas | 2 |
| Resultados com evidência suficiente | 2 |
| Contribuição clara para prática ou teoria | 2 |
| **TOTAL** | **12/12** |

## Limitações
A natureza da base de dados de arquivo (*archival data* e seccional) impede a inferência definitiva de causalidade sobre o uso das ferramentas e a produtividade. A pesquisa depende fortemente do autorrelato dos desenvolvedores e carece de rastreamento de uso em tempo real e designs experimentais em laboratório para validar diretamente os ganhos ou perdas de produtividade.

## Contribuição Principal
O estudo demonstra empiricamente que o "hype" de ganho universal de produtividade com IA não se sustenta no mercado profissional como uma regra geral: os benefícios da geração de código por IA são assimétricos. A IA atua de forma muito mais eficaz como um acelerador e nivelador para desenvolvedores com menos anos de experiência, enquanto o impacto sobre o tempo de pesquisa de desenvolvedores experientes e sobre ambientes de alta complexidade (multilinguagens) é marginal ou nulo. Essa descoberta ajuda líderes de TI e equipes a terem expectativas realistas sobre o ROI da adoção de assistentes de codificação de IA.
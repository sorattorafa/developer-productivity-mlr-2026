# P1260 — Setting Productivity Metrics for Automation Development Teams: From one-dimensional metrics toward a holistic view
**Decisão: INCLUÍDO | Qualidade: 5/5**

## Dados Bibliográficos
| Campo | Valor |
|-------|-------|
| **ID** | P1260 |
| **Autores** | Lauri Koskinen |
| **Ano** | 2025 |
| **Venue** | Aalto University School of Business (Bachelor's thesis) |
| **DOI** | Não especificado |
| **Tipo** | Bachelor's thesis / Revisão de Literatura |
| **Método** | Thematic literature review |
| **Amostra** | 30 artigos acadêmicos revisados por pares (aproximadamente 10 para cada um dos 3 temas centrais pesquisados) |
| **Contexto** | Equipes de desenvolvimento de Automação de Processos de Negócios (BPA - Business Process Automation), Engenharia de Software e Trabalho do Conhecimento (Knowledge Work) |
| **Modo de trabalho** | Análise temática baseada em padrões recorrentes de diferentes perspectivas de pesquisa |
| **Metodologia** | Revisão sistemática de bases como Google Scholar e Scopus com termos cruzados sobre produtividade de software, produtividade do conhecimento e BPA |

---

## Objetivo
Identificar métricas robustas e adequadas de produtividade para o desenvolvimento de automação de processos de negócios (BPA) a partir da literatura existente e avaliar a fundamentação para a escolha dessas métricas.

---

## Questões de Pesquisa
*   **RQ1:** Como medir a produtividade de uma equipe de desenvolvimento de automação de processos de negócios (BPA)?

## Métricas e Instrumentos de Avaliação

| Métrica | Categoria | Nível | Como Coletada | Validada |
|---------|-----------|-------|---------------|----------|
| **DORA (Lead time e Deployment frequency)** | Efficiency & Flow / Activity | Team | Monitoramento de esteira de desenvolvimento e entregas | Sim (referenciado) |
| **SPACE (Métricas multidiomensionais como Satisfação, Comunicação)** | Holistic | Team / Individual | Pesquisas de satisfação, monitoramento de churn, refatorações | Sim (referenciado) |
| **HCE (Human Capital Efficiency)** | Financial / Value | Team / Org | Razão do Valor Adicionado (VA) gerado ao negócio versus o Capital Humano (HC - custos da equipe) | Sim (referenciado) |
| **Métricas Tradicionais (CLOC, Function Points)** | Output | Individual | Contagem volumétrica do trabalho técnico gerado | Sim (embora criticadas) |

## Frameworks e Métricas
### Frameworks Referenciados
*   **SPACE Framework:** Foca em cinco dimensões: Satisfação, Desempenho, Atividade, Comunicação & Colaboração, e Eficiência & Fluxo.
*   **DORA (DevOps Research and Assessment):** Foco em métricas de velocidade de entrega e estabilidade.
*   **DevEx (Developer Experience):** Foca em otimizar o ambiente do desenvolvedor através de loops de feedback, carga cognitiva e estado de fluxo (flow state).
*   **HCE (Human Capital Efficiency):** Mede a produtividade via proxys econômicos (geração de valor sobre custos).
*   **Balanced Scorecard (BSC):** Utiliza as perspectivas Financeira, de Clientes, de Processos Internos e de Aprendizado/Crescimento.

### Frameworks Propostos
*   **SPACE adaptado para BPA:** O autor propõe combinar as cinco dimensões do framework SPACE com as quatro perspectivas do *Balanced Scorecard* (BSC) e métricas baseadas no modelo *HCE*, criando uma matriz holística voltada especificamente para o contexto e partes interessadas da automação de processos (BPA).

---

## Fatores que Influenciam Produtividade
### Fatores Positivos
| Fator | Categoria |
|-------|-----------|
| Experiência e habilidades (Pessoais, Técnicas e não-técnicas) | Personnel |
| Satisfação do desenvolvedor / Developer Experience (DevEx) | Personnel / Environment |
| Comunicação efetiva, colaboração e transferência de conhecimento | Process / Teamwork |
| Autonomia, estímulo à inovação e engajamento na melhoria do processo | Management / KWP |
| Boa precisão de estimativa de esforço e entendimento profundo do negócio | Process / Context |

### Fatores Negativos
| Fator | Categoria |
|-------|-----------|
| Dívida Técnica (Technical Debt) causando retrabalho e interrupções | Technical |
| Alta carga cognitiva limitando o foco ("Flow state") | Environment / Individual |
| Alta volatilidade nos requisitos do negócio / falta de compreensão do processo | Process / Product |
| Foco restrito em métricas volumétricas (como linhas de código) | Management |

---

## Papel da IA e Automação

| Campo | Valor |
|-------|-------|
| Usa IA/ML? | Sim — Tecnologias de **Intelligent Process Automation (IPA)**, mencionadas no contexto, utilizam Machine Learning (ML), Processamento de Linguagem Natural (NLP) e Reconhecimento Ótico de Caracteres (OCR) para automatizar lógicas complexas e dados não-estruturados. |
| Automação de coleta? | Não se aplica (trata-se de uma revisão de literatura avaliando frameworks, sem coleta automatizada de software no estudo original). |
| Impacto de IA na produtividade? | O desenvolvimento em si tem como *propósito* construir automações (ex: RPA, IPA) que geram produtividade para o negócio subjacente (redução de tempo, mitigação de erros, ganhos de escala). Na perspectiva da equipe, usar melhor as tecnologias resulta em implantações muito mais rápidas do que o desenvolvimento de software tradicional. |

---
## Resultados Principais
* Uma abordagem baseada em uma única métrica é insuficiente para gerenciar equipes modernas de software e BPA. 
* O desenvolvimento de BPA se diferencia fundamentalmente do desenvolvimento de software tradicional por ser **centrado no processo** (ao invés de centrado em um produto), objetivando estritamente a melhoria e automação de fluxos de trabalho empresariais existentes.
* As métricas de BPA atuais geralmente medem a melhoria percebida pelo próprio negócio (resultado do robô), e ignoram a medição de desempenho e saúde intrínseca do processo de desenvolvimento / equipe.
* A tese sugere que a matriz que cruza **SPACE e Balanced Scorecard** alinha de maneira bem-sucedida a saúde dos desenvolvedores, a velocidade de entrega e os resultados estratégicos para a organização como métricas aplicáveis em BPA.

## Desafios do Uso das Métricas
* A métrica fundamental de *outputs* (saídas) no trabalho de conhecimento e em software é intangível; logo, medí-los volumetricamente corre o risco de criar comportamentos enviesados e sacrificar a qualidade de entrega.
* Especificamente para BPA, o desafio metodológico central decorre do fato de que uma equipe de alta performance técnica pode atuar automatizando um processo de negócio inerentemente falho ou de baixo impacto. Dessa forma, as métricas puramente ligadas ao impacto do processo não capturariam com precisão a verdadeira produtividade da equipe de desenvolvimento.

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
* A pesquisa é de natureza estritamente teórica (revisão de literatura) e carece de dados empíricos / estudos de caso aplicados que validem a eficácia e impacto real do framework proposto em ambientes corporativos.
* O escopo considerou apenas 30 artigos em inglês devido a restrições de tempo, podendo não mapear toda a literatura pertinente em bases ou línguas diferentes.
* A análise trata as tecnologias de BPA de forma relativamente homogênea, sem explorar as distinções fundamentais na medição da complexidade de entrega entre RPA, integrações via API ou IPA com IA.

## Contribuição Principal
Sintetizar as pesquisas mais avançadas de engenharia de software (como o framework SPACE) com modelos de Produtividade do Trabalho do Conhecimento (KWP e Human Capital Efficiency), propondo um inovador e prático framework customizado e multifacetado, organizado através das óticas do Balanced Scorecard (BSC), voltado exclusivamente para gerenciar as equipes de automação de processos (BPA) de maneira holística e alinhada estrategicamente.
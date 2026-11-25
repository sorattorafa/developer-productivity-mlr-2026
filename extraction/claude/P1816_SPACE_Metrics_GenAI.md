# P1816 — How much SPACE do metrics have in GenAI assisted software development?

**Decisao: INCLUIDO | Qualidade: 4/5**

---

## Dados Bibliograficos

| Campo | Valor |
|-------|-------|
| **ID** | P1816 |
| **Autores** | Samarth Sikand, Kanchanjot Kaur Phokela, Vibhu Saujanya Sharma, Kapil Singi, Vikrant Kaulgud, Teresa Tung (e outros) |
| **Ano** | 2024 |
| **Venue** | ISEC'24 - 17th Innovations in Software Engineering Conference |
| **Tipo** | Artigo de pesquisa - Estudo de levantamento (Survey) |
| **Metodo** | Análise de literatura com estudo controlado de usuário e survey |
| **Amostra** | Até 20 participantes em estudos, múltiplos modelos GenAI (OpenAI Codex, GitHub Copilot, etc.) |
| **Contexto** | Desenvolvimento de software assistido por Inteligência Artificial Generativa |

---

## Objetivo

Este artigo investiga o papel das métricas de produtividade de desenvolvedores em contextos de desenvolvimento de software assistido por Inteligência Artificial Generativa (GenAI). O objetivo principal é avaliar como o framework SPACE (Satisfaction, Performance, Activity, Communication, Efficiency) se aplica à experiência de desenvolvedores usando ferramentas GenAI como GitHub Copilot e OpenAI Codex.

O trabalho busca identificar lacunas críticas na avaliação padronizada de ferramentas GenAI para desenvolvimento, destacar vieses em estudos existentes e propor recomendações para melhor conformidade na avaliação de ferramentas de IA generativa em desenvolvimento de software.

---

## Questoes de Pesquisa

- **RQ1**: Como o framework SPACE é aplicado em estudos de avaliação de ferramentas GenAI para desenvolvimento de software?
- **RQ2**: Que dimensões e sub-categorias do framework SPACE recebem atenção desproporcional em estudos de GenAI?
- **RQ3**: Quais são os vieses em design de estudo e quais recomendações emergem para avaliação mais estruturada e holística de ferramentas GenAI?
- **RQ4**: De que forma a literatura atual avalia a experiência de desenvolvedores com ferramentas GenAI em relação ao framework SPACE?

---

## Dados da Pesquisa

### Amostra

- **Tamanho de Participantes**: Estudos analisados tiveram tamanho de amostra variando tipicamente entre 30-90 participantes
- **Modelos GenAI Avaliados**:
  - GitHub Copilot (ferramenta mais estudada)
  - OpenAI Codex, Codex-Davinci-1, Codex-Davinci-2
  - GenLine, TransCoder, LLaMA, Code-BERT
  - Modelos multilingues: CodeGen2B-Multi, CodeGen2B, Code-Davinci-3
  - Outros: Codex-Cushman, best-tranX-annot, CoNaLa
- **Diversidade de Ferramentas**: Estudos de 50 ferramentas diferentes analisadas
- **Participantes em User Studies**: Geralmente entre 30-50 desenvolvedores, alguns estudos com até 90+

### Fonte de Dados

- **ACM Digital Library**: Busca sistemática de estudos publicados
- **IEEE Xplore, Science Direct, Research Gate**: Múltiplas plataformas acadêmicas
- **Estudos Controlados de Usuário**: Coleta de dados primários através de experimentos controlados
- **Surveys Estruturados**: Formulários respondidos por desenvolvedores com experiência em ferramentas GenAI
- **Blogs de Comunidades OpenSource**: Repositórios como Codex, GitHub Copilot telemetria
- **Datasets Públicos**: HumanEval dataset, HeartStone dataset

### Metodos de Coleta

- **Automated Search Exercise**: Busca automática em bibliotecas digitais usando termos como "AI", "deep learning", "LLM", "Transformer"
- **Pruning by Filters**: Filtragem por estudos peer-reviewed, publicados em conferências/journals aceitáveis (ASE, ACL, NIPS, MAPS, CHI)
- **Shortlisting by Human Validation**: Validação manual de estudos relevantes a ferramentas GenAI
- **Bucketing by SPACE Categories**: Categorização de métricas usadas em estudos de acordo com dimensões SPACE
- **User Studies**: Experimentos controlados com desenvolvedores usando ferramentas GenAI
- **Surveys Estruturados**: Questionários pós-experiência coletando percepções sobre satisfação, desempenho, atividade, comunicação e eficiência

### Periodo de Analise

- **Cobertura Temporal**: Estudos publicados até fevereiro de 2024
- **Período de Estudos**: Análise de estudos de 2020-2024 (período de proliferação de GenAI)
- **Coleta de User Studies**: Período não especificado, mas presumably durante 2023-2024

---

## Metricas e Instrumentos de Avaliacao

### Framework SPACE - Dimensões Principais

O framework SPACE organiza métricas de produtividade de desenvolvedores em 5 dimensões principais:

#### 1. **Satisfaction & Well-being** (Satisfação e Bem-estar)

Subcategorias:
- **Developer Fulfillment and Efficacy**: Satisfação do desenvolvedor com ferramentas, sentimento de capacitação
- **Developer Wellbeing**: Saúde mental, stress, carga de trabalho, equilíbrio trabalho-vida
- **Trust in AI Tools**: Confiança em saídas geradas por IA, confiabilidade percebida

Métricas utilizadas em estudos:
- Satisfação com sugestões de código
- Eficácia percebida ao usar Copilot
- Ansiedade ou stress relacionado ao uso de IA

#### 2. **Performance** (Desempenho)

Subcategorias:
- **Outcome of System or Process**: Resultado de usar ferramentas GenAI em tarefas de desenvolvimento
- **Quality of Outcomes**: Qualidade de código gerado, correção funcional
- **Reliable Outputs**: Confiabilidade de sugestões geradas

Métricas utilizadas:
- Tempo para completar tarefa
- Taxa de correção de código
- Porcentagem de sugestões aceitáveis
- Qualidade de testes gerados
- Cobertura de testes

#### 3. **Activity** (Atividade)

Subcategorias:
- **Operational Activities**: Atividades operacionais realizadas durante desenvolvimento
- **Time on Activities**: Tempo gasto em diferentes atividades (codificação, revisão, testes)

Métricas utilizadas:
- Tokens completados por prompt
- Número de sugestões aceitas/rejeitadas
- Frequência de uso de ferramenta
- Handoff entre IA e desenvolvedor (transições)

#### 4. **Communication & Collaboration** (Comunicação e Colaboração)

Subcategorias:
- **How Teams Communicate and Work Together**: Efetividade de comunicação em equipe
- **Pair Programming Effort**: Esforço necessário para trabalho colaborativo

Métricas utilizadas:
- Qualidade de comunicação dentro de equipe
- Efetividade de pareamento programação com IA
- Frequência de discussões sobre código

#### 5. **Efficiency** (Eficiência)

Subcategorias:
- **Ability to Complete Work with Minimal Interruptions**: Capacidade de completar trabalho sem interrupções

Métricas utilizadas:
- Flow de desenvolvedores (estado de fluxo durante coding)
- Redução de atritos ou interrupções
- Velocidade de conclusão de tarefa

### Características de Avaliação

**Tool Selection Preference Factors**:
- Ease of Availability of Tool (A)
- Ease of Use of Tool (B)
- Developers' Experience with Tool (C)

**Study Characteristics Analyzed**:
- Study design (controlado vs. não-controlado)
- Tamanho de amostra
- Modelos GenAI utilizados
- Natureza de tarefas (custom vs. leveraging existing datasets)

### Dados Coletados de Estudos

- **Variância em Dimensões**: Análise de quais dimensões SPACE recebem maior foco
- **Sub-categorias Negligenciadas**: Identificação de aspectos pouco estudados (e.g., Collaboration/Communication)
- **Distribuição de Métricas**: Contagem de estudos focando cada dimensão
- **Bias Analysis**: Análise de vieses em seleção de ferramentas, estudos e participantes

---

## Resultados Principais

### 1. Cobertura Desigual do Framework SPACE

A análise de 50 estudos revelou distribuição altamente desigual entre dimensões SPACE:

- **Satisfaction & Well-being**: Recebeu atenção em maioria dos estudos (métrica mais coberta)
- **Performance**: Também bem coberta, com foco em qualidade e confiabilidade de código
- **Activity**: Moderadamente coberta, com ênfase em tokens e aceite de sugestões
- **Communication & Collaboration**: **Criticamente sub-representada** - quase negligenciada na maioria dos estudos
- **Efficiency**: Moderadamente coberta, focando em velocidade de conclusão de tarefas

### 2. Lacunas Críticas Identificadas

**Communication and Collaboration é uma dimensão inteiramente negligenciada:**
- Apenas um estudo foi encontrado tentando cobrir aspectos de dinâmica de equipe com GenAI
- Nenhum estudo investigou como ferramentas GenAI afetam comunicação dentro de equipes
- Falta de pesquisa sobre experiência de pareamento programação com IA

**Falta de Diversidade em Sub-categorias:**
- Dentro da Performance, foco desproporcional em Code Quality vs. outras subcategorias
- Trust in AI é mencionado mas raramente investigado profundamente
- Wellbeing completamente ausente da maioria dos estudos

### 3. Vieses em Design de Estudos

**Dominância de Ferramenta Única:**
- GitHub Copilot é a ferramenta mais estudada, criando viés de disponibilidade
- Poucos estudos comparam múltiplas ferramentas GenAI
- Maioria dos estudos usa Codex family de modelos (uma família de modelos)

**Tamanho de Amostra Limitado:**
- Estudos tipicamente incluem 30-50 participantes
- Amostra global de GenAI user studies é limitada (~100+ participantes no máximo)
- Falta de estudos de larga escala com centenas/milhares de participantes

**Preferência por Estudos Controlados com Modelos Populares:**
- Tendência a estudar Copilot porque é ferramenta comercial estável
- Menos pesquisa em modelos de código abertos alternativos
- Estudos tendem a usar tarefas predefinidas em vez de cenários realistas

### 4. Insights sobre Experiência do Desenvolvedor

**Satisfação Geral Positiva:**
- Desenvolvedores relatam satisfação com sugestões de código
- Sentimento de capacitação ao usar ferramentas GenAI
- Eficácia percebida é genericamente positiva

**Desempenho Misto:**
- Qualidade de código varia significativamente dependendo de domínio
- Vulnerabilidades em código gerado são preocupação documentada
- Taxa de aceitação de sugestões varia de 20-80% dependendo de ferramenta

**Eficiência Variable:**
- Alguns estudos mostram redução de tempo; outros não
- Flow e estado de concentração afetados pela qualidade de sugestões
- Necessidade de revisão de código gerado reduz ganhos de eficiência

### 5. Recomendações Emergentes da Análise

1. **Diversificar Cobertura SPACE**: Pesquisas futuras devem focar em especial em Communication/Collaboration
2. **Ampliar Escopo de Ferramentas**: Estudar além de Copilot; incluir modelos de código aberto
3. **Aumentar Tamanho de Amostra**: Conduzir estudos em larga escala com múltiplos contextos
4. **Investigar Dinâmica de Equipe**: Entender como GenAI impacta colaboração e comunicação em equipe
5. **Estudar Cenários Realistas**: Usar casos de uso reais em vez de tarefas artificiais
6. **Avaliar Aspectos de Segurança**: Focar mais em confiabilidade e vulnerabilidades de código

---

## Desafios do Uso das Metricas

1. **Falta de Padronização**: Diferentes estudos usam métricas diferentes, dificultando comparação sistemática de resultados entre estudos.

2. **Variância em Definições SPACE**: Definição de cada dimensão varia significativamente entre estudos, criando ambiguidade em categorização.

3. **Negligência de Collaboration**: Dimensão de Collaboration e Communication praticamente não é investigada, deixando grande lacuna no entendimento de impacto de GenAI em dinâmica de equipe.

4. **Bias de Ferramenta**: Predominância de GitHub Copilot e modelos Codex cria viés sistêmico na pesquisa, afetando generalização.

5. **Tamanho de Amostra Insuficiente**: Maioria dos estudos tem 30-90 participantes, limitando robustez estatística e generalização.

6. **Falta de Estudos Longitudinais**: Poucos estudos investigam impacto a longo prazo de GenAI em produtividade e satisfação; maioria é curta duração.

7. **Limitações em Realism**: Estudos controlados tipicamente usam tarefas artificiais; transferência para contextos reais de produção é questionável.

8. **Múltiplas Confounding Variables**: Experiência do desenvolvedor, domínio do problema, complexidade de tarefa - não sistematicamente controladas entre estudos.

9. **Falta de Métricas de Qualidade Objetivas**: Muitos estudos focam em percepção (satisfação) vs. métricas objetivas de qualidade/desempenho.

10. **Trade-offs Não Explorados**: Poucos estudos investigam trade-offs entre velocidade vs. qualidade, ou entre confiança vs. rigor de revisão.

11. **Segurança e Confiabilidade Negligenciadas**: Apesar de preocupações documentadas, pesquisa limitada em vulnerabilidades de código gerado por GenAI.

12. **Generalizabilidade Questionável**: Resultados de estudos com Copilot podem não generalizar para outros modelos ou contextos organizacionais.

---

## Avaliacao de Qualidade

| Criterio | Pontuacao (0-2) |
|----------|----------------|
| Objetivo claramente definido | 2 |
| Metodologia adequada | 2 |
| Amostra/contexto descrito | 2 |
| Ameacas a validade discutidas | 1 |
| Resultados com evidencia | 2 |
| Contribuicao clara | 2 |
| **TOTAL** | **11/12** |

---

## Limitacoes

1. **Escopo Limitado da Revisão**: Análise de 50 estudos; possível que estudos relevantes tenham sido perdidos em processamento automático ou filtragem.

2. **Bias em Seleção de Artigos**: Foco em publicações peer-reviewed podem ter excluído relatórios técnicos, blogs ou estudos em conferências mais específicas.

3. **Heterogeneidade de Estudos**: Diversidade em metodologia, design e contexto dos 50 estudos analisados dificulta síntese e comparação direta.

4. **Falta de Análise Profunda de Qualidade**: Não há avaliação sistemática de qualidade metodológica de estudos incluídos (ex: power analysis, threat to validity assessments).

5. **Cobertura Temporal Limitada**: Análise até fevereiro 2024; landscape de GenAI evolui rapidamente, então alguns achados podem estar desatualizados.

6. **Limitações em Coleta de Dados Primários**: User studies conduzidos têm tamanho de amostra pequeno (não especificado, mas aparentemente < 100), limitando generalização.

7. **Contexto de Desenvolvedor Não Bem Caracterizado**: Experiência, nível de expertise, linguagens de programação preferidas não sistematicamente documentados.

8. **Falta de Estudos em Linguagens/Domínios Específicos**: Maioria dos estudos foca em linguagens mainstream (Python, JavaScript); linguagens menos comuns pouco investigadas.

9. **Confundidores Não Controlados**: Fatores como pressão de deadline, complexidade de domínio, qualidade de especificações não isolados em análise.

10. **Validação Externa Limitada**: Recomendações emergentes não foram validadas em contextos reais de produção com centenas/milhares de desenvolvedores.

11. **Viés de Publicação**: Estudos com resultados positivos sobre GenAI podem ser mais prováveis de publicação do que aqueles mostrando limitações.

12. **Evolução Rápida de Modelos**: Modelos GenAI evoluem rapidamente; estudos de 2020-2023 podem não ser aplicáveis a modelos de 2024.

---

## Contribuicao Principal

O artigo fornece a primeira análise sistemática abrangente de como o framework SPACE é aplicado em pesquisa de Inteligência Artificial Generativa em desenvolvimento de software. A contribuição principal é a identificação de lacunas críticas e vieses sistêmicos na avaliação de ferramentas GenAI, particularmente a negligência quase completa da dimensão de Collaboration e Communication do framework SPACE.

O trabalho destaca que enquanto satisfação e desempenho de sistemas recebem atenção considerável, dimensões críticas de dinâmica de equipe e experiência colaborativa com ferramentas GenAI permanecem amplamente não investigadas. Além disso, o artigo documenta vieses significativos em pesquisa existente: dominância de uma única ferramenta (GitHub Copilot), tamanhos de amostra limitados, falta de diversidade em modelos GenAI estudados, e prevalência de estudos controlados sobre cenários realistas.

As recomendações do artigo oferecem direção clara para a comunidade de pesquisa: necessidade urgente de estudos em larga escala, diversificação de ferramentas e contextos, investigação sistemática de aspectos de colaboração, e melhor conformidade com framework SPACE para produzir pesquisa mais padronizada e comparável que possa informar adoção e evolução de ferramentas GenAI em desenvolvimento de software.

---

*Extraido em Marco 2026 para MLR: Software Developer Metrics in Practice*

# P0495 — Human-AI Collaboration in Software Development: A Mixed-Methods Study of Developers' Use of GitHub Copilot and ChatGPT

**Decisao: INCLUIDO | Qualidade: 5/5**

---

## Dados Bibliograficos

| Campo | Valor |
|-------|-------|
| **ID** | P0495 |
| **Autores** | Viktoria Stray, Astri Barbala, Viggo Tellefsen Wivestad |
| **Ano** | 2025 |
| **Venue** | FSE Companion '25 - 33rd ACM International Conference on Foundations of Software Engineering |
| **Tipo** | Research Article - Mixed-Methods Study |
| **Metodo** | Entrevistas qualitativas + Survey quantitativo |
| **Amostra** | 13 entrevistas + 114 respondentes de survey |
| **Contexto** | Organização pública de grande porte na Noruega |

---

## Objetivo

Este estudo investiga fatores que influenciam a adoção de ferramentas generativas de IA (GenAI) como GitHub Copilot e ChatGPT entre desenvolvedores de software. Usando a Human-AI Collaboration and Adaptation Framework (HACAF), os autores exploram como a experiência anterior, compatibilidade com workflows, fatores sociais e perceções de tecnologia afetam a decisão de usar ou não usar essas ferramentas. O trabalho utiliza dados de 13 entrevistas e um survey com 114 respondentes em uma grande organização do setor público para entender tanto users quanto non-users.

---

## Questoes de Pesquisa

- **RQ**: Que fatores influenciam a adoção de ferramentas de IA Generativa entre engenheiros de software em uma organização pública de grande escala?

---

## Dados da Pesquisa

### Amostra
- 13 desenvolvedores entrevistados entre Novembro-Dezembro 2023
- Survey com 114 respondentes (67 users, 47 non-users de Copilot)
- 81% funcionários diretos, 19% consultores externos
- Distribuição de gênero: 79% homens, 15% mulheres, 1% outro, 5% preferiram não informar
- Experiência: média de 13,75 anos, mediana de 10 anos, máximo de 39 anos

### Fonte de Dados
- Entrevistas semi-estruturadas com 13 desenvolvedores
- Survey online com 57 questões (28 aplicáveis a usuários e non-usuários, 29 específicas para usuários)
- Duração média de entrevista: 47 minutos (variação 30-60 minutos)

### Metodos de Coleta
- Entrevistas presenciais e remotas por Zoom
- Survey com escala Likert de 5 pontos
- Constant Comparison Method para análise qualitativa
- Análise temática pragmática dos transcripts

### Periodo de Analise
- Coleta: Novembro 2023 - Dezembro 2023
- Análise: Janeiro 2025

---

## Metricas e Instrumentos de Avaliacao

**Framework HACAF - Dimensões Avaliadas**:
1. **Fatores Pessoais e Ambientais**: Inovatividade pessoal e suporte organizacional
2. **Perceções sobre Tecnologia**: Utilidade percebida, facilidade de uso, vantagem relativa
3. **Fatores de Compatibilidade**: Alinhamento com workflows existentes, integração com práticas atuais, adequação tecnológica
4. **Fatores Sociais**: Influência de pares, auto-eficácia, normas sociais

**Escala de Medição**:
- Escala Likert de 5 pontos para respostas quantitativas
- Análise de média e desvio padrão para comparações user vs. non-user
- Diferença média entre grupos

**Tópicos de Entrevista**:
- Motivações para/contra adoção de GenAI
- Workflows e ferramentas utilizados
- Perceção de produtividade e satisfação
- Considerações éticas
- Dinâmica de equipe e padrões de uso

---

## Resultados Principais

**Adoção por Experiência**:
- Desenvolvedores senior (20+ anos): 2 usuarios, 3 non-users (padrão inconsistente)
- Desenvolvedores junior: preferem usar GenAI como essencial para competitividade

**Perceções sobre Produtividade**:
- Users: 87% satisfeitos com funções (vs. 73% non-users)
- Maior acordo sobre capacidade de focar em trabalho satisfatório (77% vs. 50%)
- Redução de dependência de colegas (45% users vs. 20% non-users)

**Compatibilidade com Workflows**:
- Desenvolvedores front-end: adoção mais alta (VS Code + Copilot integração perfeita)
- Atribuição de tarefas além de codificação (tech leads, managers): menor adoção
- Tarefas repetitivas (boilerplate, unit tests): maior benefício percebido

**Fatores Sociais**:
- Padrões coletivos importam: times que adotam GenAI juntos mostram maior entusiasmo
- Pair programming/mob programming: tensão com GenAI (alguns veem como "terceira roda")
- Distribuição remota: menor compartilhamento de dicas e conhecimento sobre GenAI

**Considerações Éticas**:
- Users significativamente menos críticos de IA em setor público (2,14 vs. 3,05)
- Poucos fóruns para discussão crítica; viés de positividade em canais Slack
- Preocupações: privacidade de dados, transparência, impacto a longo prazo na profissão

---

## Desafios do Uso das Metricas

1. **Self-selection bias**: Users podem relatar maior satisfação por auto-seleção
2. **Variabilidade linguística**: Diferentes linguagens de programação (Kotlin vs. Java) afetam eficácia de Copilot
3. **IDE dependence**: Efetividade varia significativamente com IDE utilizado
4. **Contexto organizacional**: Organização pública norueguesa pode não representar outras contextos
5. **Dinâmica cultural**: Certos padrões (pair programming) diminuem benefício de GenAI
6. **Medição de produtividade subjetiva**: Perceção de produtividade vs. medidas objetivas

---

## Avaliacao de Qualidade

| Criterio | Pontuacao (0-2) |
|----------|----------------|
| Objetivo claramente definido | 2 |
| Metodologia adequada | 2 |
| Amostra/contexto descrito | 2 |
| Ameacas a validade discutidas | 2 |
| Resultados com evidencia | 2 |
| Contribuicao clara | 2 |
| **TOTAL** | **12/12** |

---

## Limitacoes

1. Estudo de caso único em organização pública norueguesa - generalizabilidade limitada
2. Foco em dois tools (Copilot e ChatGPT) - paisagem de GenAI em evolução rápida
3. Período de coleta curto (nov-dez 2023) - adoção em fase inicial
4. Participação voluntária pode introduzir bias
5. Considerações éticas não presentes no HACAF original
6. Dinâmica remota vs. presencial não totalmente explorada
7. Falta de medidas objetivas de produtividade

---

## Contribuicao Principal

Este estudo fornece análise abrangente de fatores que impulsionam adoção de GenAI em ambientes corporativos, indo além de estudos prévios que focam apenas em users. Ao integrar perspectivas de non-users e explorar dimensões individuais, tecnológicas e sociais, identifica que **compatibilidade e padrões coletivos são drivers críticos**, não apenas características da ferramenta. O achado de que considerar **ética é central para non-adopters** em setor público sugere que frameworks de adoção de tecnologia devem incorporar dimensão ética. As implicações para organizações é que suporte estratégico, treinamento de equipes e esclarecimento de políticas éticas são necessários para integração eficaz de GenAI, particularmente em contextos públicos sensíveis.

---

*Extraido em Marco 2026 para MLR: Software Developer Metrics in Practice*

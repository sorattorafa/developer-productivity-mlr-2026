# P0517 — Estudando e Melhorando a Compreensibilidade do Código Através de Átomos de Confusão

**Decisao: INCLUIDO | Qualidade: 4/5**

---

## Dados Bibliograficos

| Campo | Valor |
|-------|-------|
| **ID** | P0517 |
| **Autores** | Guoshuai Shi |
| **Ano** | 2025 |
| **Venue** | ICSE-Companion 2025 - 47th International Conference on Software Engineering: Companion Proceedings |
| **Tipo** | Research Article - Preliminary Study |
| **Metodo** | Análise de repositórios open-source + survey de desenvolvedores + LLM-aided refactoring |
| **Amostra** | Múltiplos projetos OSS + desenvolvedores de survey |
| **Contexto** | Desenvolvimento de software open-source em Java |

---

## Objetivo

Este estudo investiga o impacto de Átomos de Confusão (AoCs) - estruturas de código específicas que causam confusão em leitura - na compreensibilidade e defeitos em projetos Java. Através de análise de repositórios, survey de desenvolvedores, e exploração de refactoring auxiliado por Large Language Models (LLMs), os autores buscam entender quais tipos de AoCs afetam mais a compreensibilidade, como diferentes contextos (tipo de linguagem, projeto, experiência) influenciam impacto, e se LLMs podem auxiliar na refatoração de código confuso.

---

## Questoes de Pesquisa

- **RQ1**: Como Átomos de Confusão em Java afetam compreensibilidade e introdução de defeitos?
- **RQ2**: Quais fatores (tipo de linguagem, contexto de projeto, experiência de desenvolvedor) influenciam o impacto confusão?
- **RQ3**: Como Large Language Models podem auxiliar na refatoração de código confuso?

---

## Dados da Pesquisa

### Amostra
- Múltiplos projetos open-source Java selecionados via GitHub
- Survey com desenvolvedores Java
- Análise de 15 idiomas de baixo nível (Átomos de Confusão) em projetos OSS
- Seis projetos OSS principais: openFAIR, bioSTID, Elastic, Jenkins, Sharing.gifka, Kafka

### Fonte de Dados
- Repositórios GitHub (dados públicos)
- Survey online com desenvolvedores
- Pull Requests (BFPRs e NBFPRs - Bug-Fixing e Non-Bug-Fixing)
- Análise de commits e histórico de código

### Metodos de Coleta
- Mineração de repositórios para detectar ocorrências de AoCs
- Correlação entre AoCs e mudanças de PR (bug-fixing vs. non-bug-fixing)
- Survey com desenvolvedores para coletar percepções sobre AoCs
- Análise com LLM para explorar refactoring automated

### Periodo de Analise
- Coleta de dados de repositórios: período não especificado (presumivelmente 2024)
- Período de análise: até 2025

---

## Metricas e Instrumentos de Avaliacao

**Átomos de Confusão Investigados**:
- 15 estruturas de código de baixo nível identificadas na literatura como causadoras de confusão

**Dimensões Avaliadas**:
1. **Impacto em Defeitos**: Correlação entre presença de AoCs e bug-fixing PRs
2. **Impacto em Compreensibilidade**: Percepção de desenvolvedores via survey
3. **Contexto Específico**: Influência de tipo de linguagem, projeto, experiência do desenvolvedor
4. **Potencial de Refactoring**: Exploração de LLMs para automatizar correção de AoCs

**Escala de Medição**:
- Análise estatística de correlação entre AoCs e taxa de defeito
- Survey com escala Likert para percepção de confusão
- Análise qualitativa de feedback de desenvolvedores

---

## Resultados Principais

**Análise de Impacto em Defeitos**:
- Bug-Fixing PRs (BFPRs) mostram maior frequência de AoCs que Non-Bug-Fixing PRs (NBFPRs)
- Hipótese validada: nem todos os AoC induzem confusão
- Certos AoCs mais prevalentes em BFPRs, sugerindo correlação com defeitos

**Percepção de Desenvolvedores**:
- Survey prévio mostrou variabilidade em como diferentes tipos de AoCs afetam compreensibilidade
- Fatores como anos de experiência, tipos de projetos frequentes, e convenções de codificação influenciam impacto

**Fatores Contextuais**:
- Tipo de linguagem de programação afeta eficácia de AoC (Kotlin vs. Java têm diferenças)
- Dependência de IDE: efetividade de Copilot varia significativamente com IDE utilizado
- Convenções de projeto: padrões internos podem reduzir confusão para AoCs específicos

**Refactoring com LLMs**:
- LLMs (como ChatGPT-4) mostram potencial para automatizar identificação e refactoring de AoCs
- Necessário treinamento especializado para mapeamento de padrões confusos
- Abordagem: avaliar LLMs com base em transformação de snippets contendo AoCs confusos

---

## Desafios do Uso das Metricas

1. **Auto-selection bias**: Participantes voluntários em survey podem ter motivações específicas
2. **Variabilidade linguística**: Diferentes linguagens de programação afetam manifestação de AoCs
3. **IDE dependence**: Efetividade de ferramentas varia com IDE (VS Code + Copilot integração perfeita para front-end)
4. **Contexto organizacional**: Organizações diferentes podem ter convenções reduzindo impacto de AoCs
5. **Dinâmica cultural**: Práticas como pair programming podem afetar benefício de ferramentas
6. **Falta de medidas objetivas**: Compreensibilidade é parcialmente subjetiva

---

## Avaliacao de Qualidade

| Criterio | Pontuacao (0-2) |
|----------|-----------------|
| Objetivo claramente definido | 2 |
| Metodologia adequada | 2 |
| Amostra/contexto descrito | 1 |
| Ameacas a validade discutidas | 1 |
| Resultados com evidencia | 2 |
| Contribuicao clara | 2 |
| **TOTAL** | **10/12** |

---

## Limitacoes

1. Estudo preliminar: muitos aspectos ainda em desenvolvimento (resultados esperados em 4 anos)
2. Foco principal em Java: generalizabilidade a outras linguagens limitada
3. Amostra de projetos OSS pode não representar contextos empresariais
4. Período de coleta curto (2023-2024): adoção de GenAI em fase inicial
5. Falta de medidas objetivas de compreensibilidade (percepção vs. realidade)
6. LLM-based refactoring ainda exploratória sem validação final
7. Dinâmica de pair programming não totalmente explorada

---

## Contribuicao Principal

Este estudo fornece análise abrangente de Átomos de Confusão em projetos Java open-source, identificando que certas estruturas de código causam confusão significativa afetando tanto compreensibilidade quanto taxa de defeitos. O trabalho demonstra que **contexto é crítico** - mesmo idiomas de confusão têm impacto variável dependendo de linguagem, IDE, e convenções de projeto. A exploração preliminar de LLMs para refactoring automático sugere que ferramentas baseadas em IA podem auxiliar desenvolvimento más estão ainda em estágios iniciais. Implicações para prática: (1) desenvolvedores e times devem identificar quais AoCs afetam seu contexto específico, (2) padrões de codificação devem evitar idiomas confusos, (3) ferramentas LLM-based mostram potencial para refactoring mas requerem specialização. Contribuição principal é expansão da compreensão sobre impacto específico de AoCs em diferentes contextos, avançando discussão além de "todos os AoCs confundem" para nuances contextuais reais.

---

*Extraido em Marco 2026 para MLR: Software Developer Metrics in Practice*

# P0591 — Conversando com IA: Decifrando Conversas de Desenvolvedores com ChatGPT

**Decisao: INCLUIDO | Qualidade: 4/5**

---

## Dados Bibliograficos

| Campo | Valor |
|-------|-------|
| **ID** | P0591 |
| **Autores** | Suad Mohamed, Abdullah Parvin, Esteban Parra |
| **Ano** | 2024 |
| **Venue** | MSR '24 - 21st International Conference on Mining Software Repositories |
| **Tipo** | Research Article - Empirical Study |
| **Metodo** | Análise de conversas + open coding + machine learning classification |
| **Amostra** | 321 conversas ChatGPT com desenvolvedores (após filtragem, 251 analisadas) |
| **Contexto** | DevGPT dataset com conversas públicas de desenvolvedores |

---

## Objetivo

Este estudo investiga como desenvolvedores de software utilizam ChatGPT em seu desenvolvimento através de análise empírica de conversas reais. Através de open coding manual de 251 conversas e machine learning classification, os autores identificam 19 categorias de propósitos/usos distintos, explorando como desenvolvedores aproveitam IA generativa em diferentes contextos de trabalho - desde geração de código simples até debugging complexo, testes, documentação, e planejamento arquitetural.

---

## Questoes de Pesquisa

- **RQ**: Quais são os propósitos mais comuns pelos quais desenvolvedores interagem com ChatGPT?

---

## Dados da Pesquisa

### Amostra
- 321 conversas iniciais do DevGPT dataset com links ChatGPT válidos
- Após filtragem: 251 conversas analisadas (excluindo conversas não em inglês, 104 com problemas)
- Resposta rate: 22% inicial, aumentando com estratégias de sampling respondent-driven

### Fonte de Dados
- DevGPT dataset: >24,000 links para conversas ChatGPT com desenvolvedores
- Snapshot do ChatGPT correspondente a tempo-frameframe específico
- Conversas coletadas de fontes: GitHub issues, Hacker News, Stack Overflow, repositórios software, LinkedIn, Twitter, Discord

### Metodos de Coleta
- **Fase 1 - Open Coding Manual**: 2 anotadores independentemente codificaram 300 conversas
- **Fase 2 - Refinamento**: Resolução de desacordos through discussão colaborativa
- **Fase 3 - Machine Learning Classification**: Exploração de SVM, Naïve Bayes, Random Forest, Decision Tree
- **Preprocessamento**: Remoção de stopwords, stemming, TF-IDF tokenization

### Periodo de Analise
- Coleta: Novembro 2023 - Abril 2024
- Análise: Subsequente

---

## Metricas e Instrumentos de Avaliacao

**Dimensões Avaliadas**:
1. **Propósitos de Uso**: 19 categorias identificadas durante open coding
2. **Frequência de Uso**: Ocorrência de cada categoria em dataset
3. **Contexto de Desenvolvimento**: Uso em diferentes fases de SDLC

**Categorias Identificadas** (após análise):
1. Write Code (58 - 18.07%)
2. General Info (42 - 13.08%)
3. Tuning Test (34 - 10.59%)
4. Simple Task (33 - 10.28%)
5. Debugging (28 - 8.72%)
6. How-to (25 - 7.79%)
7. Framework/Dev Tool Inquiry (19 - 5.92%)
8. Programming Language Inquiry (15 - 5.61%)
9. Design Recommendation (12 - 4.74%)
10. Writing Aid (8 - 2.49%)
11. Analyze Code (7 - 2.49%)
12. Customized Chatbot (5 - 1.56%)
13. Operating System Inquiry (5 - 1.56%)
14. ChatGPT Inquiry/Abilities (4 - 1.25%)
15. Data Analysis (4 - 1.25%)
16. Technical Interview Questions (4 - 1.25%)
17. Troubleshooting (4 - 1.25%)
18. Generate Visual Text (3 - 0.93%)
19. Generate Test Prompt (1 - 0.31%)

**Escala de Medição**:
- Open coding com matriz de frequências
- Machine learning com métricas: acurácia, precisão, recall, F1-score
- Análise de distribuição de categorias

---

## Resultados Principais

**Propósitos Mais Comuns**:
- Write Code/General Info: 31.15% de conversas (maior categoria)
- Developers use ChatGPT para variedade de propósitos em software development
- Segunda categoria mais frequente: obtenção de informação geral (13.08%)
- Terceira: Tuning Test (10.59%)

**Exemplos Representativos**:
- **Conversação A (Write Code)**: Desenvolvedor pede ChatGPT para escrever código Bash renomeando arquivos
- **Conversação B (Write Code)**: Desenvolvedor pede código em C# para disparar projéteis usando object pooling
- **Conversação C (General Info)**: Desenvolvedor pesquisa informações sobre social media site Hacker News
- **Conversação D (Tuning Test)**: Desenvolvedor realiza Turing test de ChatGPT pedindo criar novo formulário arte e testando capacidades

**Resultados de Machine Learning**:
- Random Forest classifier: melhor performance com acurácia mais alta
- Diferentes classifiers (SVM, NB, RF, DT) avaliados para automatizar categorização
- Resultados sugerem viabilidade de automação com ML após identificação manual de categorias

**Descobertas Notáveis**:
- 57.02% de conversas relacionadas a escrita de código
- 34.58% de conversas sobre debugging e outras manutenções de código
- Developers use ChatGPT como extensão de processo de desenvolvimento (não apenas para coding)
- Segundo propósito mais frequente: obtenção de informação geral (13.08%)
- Terceiro: Tuning test (10.59%)

---

## Desafios do Uso das Metricas

1. **Open-source data constraints**: Dataset proveniente de public sources pode ter viés de amostra
2. **Single snapshot temporalmente**: Análise representa momento específico quando dataset coletado
3. **Self-selection em conversas públicas**: Developers who share conversas publicly pode ser não-representativo
4. **Classificação subjetiva**: Open coding contém elemento de interpretação mesmo com 2 coders
5. **Ausência consentimento direto**: Pessoas em conversas pode não ter consentido participação
6. **Generalizabilidade**: Results baseados em snapshot DevGPT pode não generalizar a todo uso ChatGPT

---

## Avaliacao de Qualidade

| Criterio | Pontuacao (0-2) |
|----------|-----------------|
| Objetivo claramente definido | 2 |
| Metodologia adequada | 2 |
| Amostra/contexto descrito | 2 |
| Ameacas a validade discutidas | 1 |
| Resultados com evidencia | 2 |
| Contribuicao clara | 2 |
| **TOTAL** | **11/12** |

---

## Limitacoes

1. Amostra: 251 conversas analisadas (após exclusões) de 321 iniciais
2. Viés de amostra: Dataset público pode favorecer tipos específicos de conversas
3. Sem consentimento direto: Análise de conversas públicas sem explícito acordo
4. Snapshot temporal: Análise representa momento específico, adoção ChatGPT em fase inicial (2023-2024)
5. Foco exclusivo em DevGPT dataset: Resultados podem não generalizar a outras fontes
6. Classificação manual: Subjetividade mesmo com 2 coders independentes
7. Ausência contexto completo: Conversas podem estar truncadas ou incompletas

---

## Contribuicao Principal

Este estudo oferece análise empírica detalhada de como desenvolvedores utilizam ChatGPT no processo de desenvolvimento de software. Ao identificar 19 categorias distintas de uso e demonstrar que **mais de metade (57.02%) de conversas focam em geração de código**, o trabalho fornece insights sobre papel central de IA generativa em desenvolvimento moderno. Além de code generation, developers também usam ChatGPT para: debugging, testes, planejamento, documentação, aprendizado, e tarefas genéricas. O resultado de que developers mais frequentemente buscam assistência com "write code" (18.07%) e "general information" (13.08%) sugere que **LLMs já alcançaram adoção significativa para suporte prático no processo de desenvolvimento**. Implicações: (1) organizações devem reconhecer role transformador de AI-assisted development, (2) developers requerem training em effective prompting e validation de AI-generated code, (3) future tools devem integrar ML-based hints de forma più natural. O estudo contribui para literatura limitada sobre uso real de GenAI em prática de desenvolvimento, indo além de estudos controlados para análise de padrões uso naturais em comunidade desenvolvedora.

---

*Extraido em Marco 2026 para MLR: Software Developer Metrics in Practice*

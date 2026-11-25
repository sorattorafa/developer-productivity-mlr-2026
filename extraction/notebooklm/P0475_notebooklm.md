# P0475 — Enhancing Software Design and Developer Experience Via LLMs

**Decisao: INCLUIDO | Qualidade: 8/12**

---

## Dados Bibliograficos

| Campo | Valor |
|-------|-------|
| **ID** | P0475 |
| **Autores** | Simin Sun [1, 2] |
| **Ano** | 2024 [1, 3] |
| **Venue** | 39th IEEE/ACM International Conference on Automated Software Engineering (ASE ’24) [1, 3] |
| **DOI** | 10.1145/3691620.3695606 [1, 3] |
| **Tipo** | Conference paper [1, 2] |
| **Metodo** | Mixed methods (Action research, Case study, Computational experiments, Qualitative surveys/interviews) [4-7] |
| **Amostra** | Developers and users from collaborating companies; industrial test logs [6, 8] |
| **Contexto** | Industry (collaborating with "Software Center" and 18 companies/universities) [8, 9] |
| **Modo de trabalho** | Not specified |
| **Metodologia** | CI/CD focus (specific process methodology like Agile/Waterfall not explicitly stated) [10] |

---

## Objetivo

O objetivo principal desta pesquisa é explorar o potencial transformador da **Generative AI** no desenvolvimento de software, focando na criação de novos métodos e ferramentas baseados em **Large Language Models (LLMs)** para automatizar a geração, refatoração e teste de código [2]. O estudo visa integrar LLMs em todo o ciclo de vida de desenvolvimento para fornecer sugestões em tempo real (**real-time suggestions**) e melhorar a produtividade e a experiência do desenvolvedor (**Developer Experience**) [2, 11].

---

## Questoes de Pesquisa

O artigo não lista RQs explicitamente numeradas, mas define objetivos de fase que funcionam como metas de pesquisa:
- **RQ1:** Como os LLMs podem ser utilizados para identificar problemas e fornecer soluções após a submissão do código (Post-Commit)? [12, 13]
- **RQ2:** De que forma os LLMs podem prever falhas em pipelines de **CI/CD** antes da submissão (Pre-Commit)? [12, 13]
- **RQ3:** Como fornecer sugestões de aprendizado de máquina em tempo real (**real-time machine learning suggestions**) durante o processo de desenvolvimento via plugins? [11, 13]

---

## Metricas e Instrumentos de Avaliacao

| Metrica | Categoria | Nivel | Como Coletada | Validada |
|---------|-----------|-------|---------------|----------|
| Model Performance (Fine-tuning results) | Quality | Team/Org | Computational experiments [6] | Partial (compared to other models) |
| Usability and Effectiveness | Satisfaction | Individual | Surveys and Interviews [6, 14] | No |
| Waiting time / Development Cycle Length | Delivery | Team | CI/CD pipeline monitoring [12, 15] | No |

---

## Frameworks e Metricas

### Frameworks Referenciados
- **Model-Driven Architecture (MDA):** APPLIED — utilizado como base metodológica para transformar modelos independentes de plataforma (PIM) em modelos específicos (PSM) [8, 16].
- **Continuous Integration / Continuous Deployment (CI/CD):** REFERENCED — o domínio onde as melhorias são aplicadas [10, 15].

### Frameworks Propostos
O artigo propõe um **Real-Time Feedback Framework** que consiste em um plugin de tempo de execução (**runtime plugin**) para ferramentas de desenvolvimento ou software de CI/CD [11, 13]. Este framework permite que empresas utilizem modelos customizados para fornecer sugestões de ML baseadas em análise de logs e previsões de falhas em tempo real [13].

---

## Fatores que Influenciam Produtividade

### Fatores Positivos
| Fator | Categoria |
|-------|-----------|
| Real-time feedback and suggestions | Process [11] |
| Automated log analysis and reusability | Technical [11] |
| Early-stage development insights | Process [10, 17] |

### Fatores Negativos
| Fator | Categoria |
|-------|-----------|
| Delayed feedback (suggestions only after commit) | Process [17] |
| Time-consuming debugging and log analysis | Human/Process [4] |
| Long waiting times in CI/CD pipelines | Process [12] |

---

## Papel da IA e Automacao

| Campo | Valor |
|-------|-------|
| Usa IA/ML? | Yes — Utiliza Generative AI (LLMs como GPT, CodeLlama, T5) para geração de código, testes e análise de logs [2, 18]. |
| Automacao de coleta? | Yes — Proposta de análise de logs em tempo real e sugestões automáticas via plugins [11]. |
| Impacto de IA na produtividade? | Espera-se encurtar o ciclo de desenvolvimento ao prever falhas e sugerir correções antes da submissão do código [12, 15]. |

---

## Resultados Principais

- A **Naturalness Hypothesis** foi validada para LLMs: a capacidade dos modelos de reconhecer linguagens de programação e tarefas melhora conforme o tamanho do modelo aumenta [14].
- Identificou-se que desenvolvedores preferem receber insights no estágio mais precoce possível (**early-stage**) ou em tempo de execução (**runtime**) em vez de após a submissão [10].
- O projeto estabeleceu um plano de quatro estágios, tendo completado o primeiro estágio focado no entendimento das capacidades dos LLMs em lidar com código e linguagem natural [13, 14].

---

## Desafios do Uso das Metricas

- **Delayed Feedback:** Soluções de ML tradicionais são aplicadas apenas após a compilação ou submissão, atrasando o retorno para o desenvolvedor [17].
- **CI/CD Overhead:** Pipelines contendo inúmeros jobs fazem com que mudanças menores levem horas para serem validadas [12].
- **Log Complexity:** Centenas de logs são gerados diariamente, tornando a análise manual e a identificação de causas raiz tarefas demoradas [19].

---

## Avaliacao de Qualidade Metodologica

| Criterio | Pontuacao (0-2) |
|----------|----------------|
| Objetivo claramente definido | 2 |
| Metodologia adequada ao objetivo | 2 |
| Amostra/contexto descrito adequadamente | 1 |
| Ameacas a validade discutidas | 0 |
| Resultados com evidencia suficiente | 1 |
| Contribuicao clara para pratica ou teoria | 2 |
| **TOTAL** | **8/12** |

---

## Limitacoes

- **Estágio da Pesquisa:** O trabalho descreve um plano de doutorado em progresso; as fases de predição pre-commit e sugestões em tempo real ainda estão em desenvolvimento ou fases futuras [12, 14, 15].
- **Generalização:** A necessidade de validar se as soluções específicas de uma organização podem ser efetivamente generalizadas para toda a indústria de software [5].

---

## Contribuicao Principal

A contribuição principal é a proposição de um **framework de feedback em tempo real baseado em MDA** que integra LLMs no fluxo de trabalho de CI/CD [13, 16]. Ao deslocar a análise de "post-commit" para "pre-commit" e "runtime", a pesquisa oferece um método para reduzir o tempo de depuração e melhorar a experiência do desenvolvedor através de plugins que fornecem soluções e predições de falhas baseadas em logs instantaneamente [11, 12].

---

*Extraido via NotebookLM em March 2026 para MLR: Software Developer Metrics in Practice* [1]
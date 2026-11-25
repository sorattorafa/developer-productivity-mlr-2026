Aqui está o resumo estruturado com base nas fontes fornecidas e no modelo solicitado:

# G018 — Software development metrics guide: Benchmarks & best practices - LinearB Blog

**Decisao: INCLUIDO | Qualidade GL: 5.0/6**

---

## Dados Bibliograficos

| Campo | Valor |
|-------|-------|
| **ID** | G018 |
| **Autor/Organizacao** | Cecilia Tao / LinearB |
| **Data** | 28 de julho de 2025 |
| **Tipo** | Guia / Artigo de Blog com Pesquisa de Mercado |
| **URL** | LinearB Blog / Guides (URL exato não especificado) |

---

## Resumo

O guia apresenta benchmarks e melhores práticas para métricas de desenvolvimento de software, baseados na análise de 6,1 milhões de pull requests provenientes de mais de 3.000 equipes de desenvolvimento e 167.437 contribuidores. O material estabelece padrões baseados em dados reais de produção para diferenciar equipes de desempenho "elite" de equipes com dificuldades, fornecendo categorias de performance (Elite, Good, Fair e Needs Focus).

O material argumenta que focar apenas nas métricas **DORA** (indicadores de atraso ou *lagging indicators*) é insuficiente para equipes de elite. Por isso, expande a medição combinando o DORA com **indicadores preditivos (leading indicators)**, **métricas de experiência do desenvolvedor (DevEx)** e **métricas de investimento em engenharia**. O objetivo principal é ajudar lideranças a identificar gargalos antes que impactem as entregas, otimizar fluxos de trabalho e demonstrar valor de negócio de forma quantitativa.

---

## Frameworks Mencionados

*   **DORA (DevOps Research and Assessment)**: Estabelecido como a base padrão da indústria para medição de desempenho de engenharia, focando no equilíbrio entre velocidade de entrega e estabilidade.

---

## Metricas Mencionadas

*   **Cycle Time (DORA)**: Mede a duração desde o início do trabalho de desenvolvimento até o código chegar em produção. *Benchmark Elite: Menos de 26 horas*.
*   **Deployment Frequency (DORA)**: Frequência com que as equipes liberam código para produção. *Benchmark Elite: Mais de 1 deploy por serviço diariamente*.
*   **Change Failure Rate (DORA)**: Porcentagem de deployments que causam falhas na produção exigindo correções imediatas. *Benchmark Elite: Menos de 1%*.
*   **Mean Time to Recovery / MTTR (DORA)**: Tempo médio para restaurar o serviço após incidentes. *Benchmark Elite: Menos de 6 horas*.
*   **PR Size (Leading Indicator)**: Tamanho do Pull Request, medido pelo número de alterações de código. *Benchmark Elite: Menos de 194 alterações*.
*   **Pickup Time (Leading Indicator)**: Tempo até que alguém comece a revisar um PR. *Benchmark Elite: Menos de 8 horas*.
*   **Engineering Investment Allocation**: Distribuição do tempo de desenvolvimento em categorias. *Otimização Elite: ~55% Criação de Novo Valor, 20% Melhorias de Funcionalidades, 15% Melhorias de DevEx, 10% Manutenção (KTLO)*.

---

## Insights para Praticantes

*   **Predição de Gargalos:** Indicadores antecedentes, como o tamanho do PR (PR Size) e o tempo de espera para revisão (Pickup Time), podem prever a degradação das métricas DORA (como aumento do Cycle Time) com 2 a 4 semanas de antecedência.
*   **Otimização de Pull Requests:** Equipes que mantêm o tamanho dos PRs abaixo de 194 linhas alcançam ciclos de revisão e frequências de merge até 5 vezes mais rápidos, reduzindo também o atrito e melhorando a satisfação do desenvolvedor.
*   **Alocação de Trabalho Saudável:** Investir cerca de 15% do tempo no aprimoramento da Experiência do Desenvolvedor (DevEx) é vital. Equipes que negligenciam isso tendem a sofrer declínios de velocidade devido ao acúmulo de débito técnico, enquanto equipes focadas apenas em manutenção (mais de 25%) perdem ritmo competitivo.
*   **Estratégia de Implementação:** Recomenda-se começar a implementação do programa de métricas focando em apenas 1 ou 2 métricas de melhoria por trimestre. Construir painéis compartilhados de forma transparente garante que os desenvolvedores participem da otimização ativamente, ao invés de se sentirem vigiados.
*   **Contexto Organizacional:** A avaliação de métricas deve se adaptar à realidade da empresa. Startups costumam alcançar facilmente frequências de deploy e tempo de ciclo de categoria "Elite" sacrificando a garantia de qualidade (processos e falhas). Em contrapartida, grandes empresas e indústrias reguladas (como saúde ou finanças) têm restrições de compliance naturais, priorizando estabilidade em vez de velocidade irrestrita.

---

## Avaliacao de Qualidade GL (Garousi et al.)

| Criterio | Pontuacao (0-1) |
|----------|----------------|
| Autoridade do autor/organizacao | 1 |
| Descricao de metodologia | 1 |
| Data de publicacao | 1 |
| Objetividade (vies comercial) | 0.5 |
| Referencias citadas | 0.5 |
| Contribuicao nova | 1 |
| **TOTAL** | **5.0/6** |

---

*Extraido via NotebookLM em 04 de junho de 2026 para MLR: Software Developer Metrics in Practice*
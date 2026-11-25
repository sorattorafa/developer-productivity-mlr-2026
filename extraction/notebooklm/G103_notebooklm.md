# G103 — The AI engineering productivity gap: 2026 benchmarks

**Decisao: INCLUIDO | Qualidade GL: 5.5/6**

---

## Dados Bibliograficos

| Campo | Valor |
|-------|-------|
| **ID** | G103 |
| **Autor/Organizacao** | Yishai Beeri (CTO) / LinearB |
| **Data** | 2026 (Benchmark data: February–May 2026) |
| **Tipo** | Industry report / Guide |
| **URL** | https://linearb.io/resources/ai-engineering-productivity-gap |

---

## Resumo

O relatorio apresenta os benchmarks de produtividade em engenharia de software com IA da LinearB para 2026, elaborados a partir de dados primarios de 2,7 milhões de pull requests e 83.000 desenvolvedores em 253 organizações de engenharia (coletados de fevereiro a maio de 2026). O estudo conceitua o "AI engineering productivity gap" como a crescente disparidade na entrega de codigo entre equipes que adotam IA intensivamente e aquelas que nao a utilizam. Desenvolvedores no grupo de uso muito alto de IA (75% ou mais dos dias de coding) atingiram 2,3 vezes a sua taxa de merge de junho de 2025 ate maio de 2026, enquanto os desenvolvedores sem uso de IA apresentaram declinio de 3,6% no mesmo periodo.

A analise aponta que contagens superficiais de adocao mascaram a real lacuna de produtividade. Nas 10% principais organizacoes (faixa Elite), 54% dos pull requests contam com assistencia de coding por IA, 45% das linhas de codigo mescladas sao escritas por IA e menos de 5% dos PRs sao gerados por autonomous agents. Os autonomous agents apresentam os piores resultados de conversao, com 79% dos PRs mesclados em 30 dias na faixa Elite e apenas 37% na faixa Fair (top 60%), devido a falta de propriedade humana (ownership). Em contrapartida, o AI code review e destacado como a alavanca de ganho mais rapido, aumentando o PR yield em ate 5 pontos percentuais em relacao a linha de base geral e ate 7 pontos sobre PRs exclusivamente humanos.

Em termos financeiros, o gasto com tokens atinge US\$ 481 por desenvolvedor por mes no percentil 90 de consumo (menos de 4% do custo total carregado de um desenvolvedor). A LinearB defende a avaliacao do investimento em IA por meio da metrica "cost per delivered pull request", conectando custos de pessoal e tokens a taxa de yield e ao volume de entregas. Para fechar a lacuna de produtividade, o relatorio recomenda o modelo operacional APEX — construído sobre os frameworks DORA e SPACE —, focado em quatro pilares: AI leverage, predictability, efficiency e developer experience.

---

## Frameworks Mencionados

* **DORA (dora.dev)**: Discutido e utilizado como uma das bases conceituais para a estrutura do modelo operacional APEX.
* **SPACE framework (ACM Queue, 2021)**: Discutido e combinado ao DORA para fundamentar a medicao de produtividade e experiencia de desenvolvimento no modelo APEX.
* **APEX (LinearB's operating model for the AI era)**: Recomendado como modelo operacional para tratar a IA como contribuidora de producao de primeira classe, mensurando quatro resultados: AI leverage, predictability, efficiency e developer experience.
* **DevEx**: Mencionado no contexto da dimensao de experiencia do desenvolvedor ("developer experience") integrada ao modelo APEX.

---

## Metricas Mencionadas

* **PR merge rate (Merge rate)**: Medido em PRs por desenvolvedor por semana. O grupo de uso muito alto de IA (75%+ dos dias) alcancou 2,3x a taxa de merge de junho de 2025 em maio de 2026. Benchmarks: Elite (2,6 PRs/dev/semana), Good (1,9), Fair (1,3) e Needs focus (<1,3).
* **PR yield / PR yield rate**: Porcentagem de pull requests abertos que sao mesclados dentro de 30 dias. Benchmarks gerais: Elite (90%), Good (86%), Fair (81%) e Needs focus (<81%).
* **PR yield rate (agentic PRs)**: Porcentagem de PRs abertos por agentes autonomos que sao mesclados em 30 dias. Benchmarks: Elite (79%), Good (58%), Fair (37%) e Needs focus (<37%).
* **Share of PRs with AI coding assistance**: Porcentagem de PRs que utilizam assistencia de coding por IA. Benchmarks: Elite (54%), Good (35%), Fair (20%) e Needs focus (<20%).
* **Share of PRs with AI code review**: Porcentagem de PRs que passam por revisao automatizada de codigo por IA. Benchmarks: Elite (57%), Good (26%), Fair (8%) e Needs focus (<8%).
* **Share of PRs written by autonomous agents**: Porcentagem de PRs criados por agentes autonomos. Benchmarks: Elite (4,7%), Good (1,1%), Fair (0,1%) e Needs focus (<0,1%).
* **Share of merged code lines written by AI**: Porcentagem de linhas de codigo mescladas efetivamente geradas por IA. Benchmarks: Elite (45%), Good (25%), Fair (12%) e Needs focus (<12%).
* **Token cost per developer per month / daily cost**: Custo de tokens de IA por desenvolvedor por mes/dia. No percentil 90 de consumo, atinge US\$ 481/mes (ou US\$ 35,20 por dia de coding). Benchmarks: Elite (\$481), Good (\$152), Fair (\$50) e Needs focus (<\$50). Representa menos de 4% do custo total carregado do desenvolvedor.
* **Cost per delivered pull request**: Custo total de engenharia (pessoal + tokens) dividido pelos PRs efetivamente entregues. Exemplo pratico citado: reducao do custo por PR entregue de US\$ 864 para US\$ 613 (-29%) ao escalar o investimento em IA.
* **PR maturity / PR sizing**: Medida do tamanho e tempo de maturacao do PR (codigo assistido por IA gera PRs maiores que maturam mais devagar).
* **Rework rate**: Taxa de retrabalho no codigo mesclado (mantida em 5% no modelo de ROI citado).
* **Cycle time**: Tempo de ciclo de desenvolvimento (reducao exemplificada de 81% no caso de cliente Syngenta).

---

## Insights para Praticantes

* **Estabelecer linha de base de merge rate**: Baselines devem ser calculados comparando a taxa de merge atual da equipe com a do ano anterior, dividida pela frequencia de uso de IA por desenvolvedor.
* **Separar adocao (adoption) de alavancagem (leverage)**: Acompanhar métricas de uso real nos PRs (assistencia de codigo e AI code review) em vez de apenas contabilizar licenças atribuídas.
* **Priorizar AI Code Review antes de escalar autonomous agents**: O AI code review e o ganho mais rapido disponivel (eleva o PR yield em ate 5 pontos percentuais geral e ate 7 pontos sobre PRs humanos no top 60%), aliviando o gargalo de revisao gerado pelo aumento na velocidade de geracao de codigo.
* **Lidar com a falta de propriedade (ownership) dos agentes autonomos**: PRs criados por agentes sem um engenheiro responsavel tendem a ficar estagnados (yield cai para 37% no top 60%), sinalizando uso experimental periférico em vez de integracao real de entrega.
* **Medir e reportar Cost per Delivered Pull Request**: Conectar o investimento em tokens aos PRs entregues e a taxa de conversao de PRs para estruturar modelos defensaveis de ROI para liderança e financas.
* **Executar as 4 jogadas do modelo APEX**:
  1. *Medir AI leverage em primeiro lugar*: Monitorar a proporcao de PRs com AI coding assistance e AI code review frente a linha de base de cada time.
  2. *Mapear e replicar equipes halo ("halo teams")*: Identificar times onde desenvolvedores com alto uso de IA ajudam a puxar os colegas e disseminar intencionalmente seus setups, prompts e workflows.
  3. *Combater a fricção do codigo assistido por IA*: Automatizar o dimensionamento de PRs, o roteamento de revisao e monitorar retrabalho e maturidade de PR.
  4. *Utilizar dados para coaching, nao para ranqueamento*: Usar as metricas para iniciar conversas de suporte e treinamento, evitando ranquear ou punir desenvolvedores.

---

## Avaliacao de Qualidade GL (Garousi et al.)

| Criterio | Pontuacao (0-1) |
|----------|----------------|
| Autoridade do autor/organizacao | 1 |
| Descricao de metodologia | 1 |
| Data de publicacao | 1 |
| Objetividade (vies comercial) | 0.5 |
| Referencias citadas | 1 |
| Contribuicao nova | 1 |
| **TOTAL** | **5.5/6** |

*Nota de avaliacao:* A pontuacao de objetividade foi definida em 0.5 devido ao fato de o relatorio ser publicado por um fornecedor de software (LinearB) promovendo seu proprio modelo operacional (APEX) e plataforma commercial, embora apresente um conjunto de dados empiricos de grande escala (2,7M PRs) extremamente detalhado.

---

*Extraido via NotebookLM em October 2026 para MLR: Software Developer Metrics in Practice*
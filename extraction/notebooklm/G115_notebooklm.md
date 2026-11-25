# G115 — Introducing DORA's inaugural AI Capabilities Model

**Decisao: INCLUIDO | Qualidade GL: 5.0/6**

---

## Dados Bibliograficos

| Campo | Valor |
|-------|-------|
| **ID** | G115 |
| **Autor/Organizacao** | Kevin M. Storer (Ph.D.), Derek DeBellis / DORA (Google Cloud) [1] |
| **Data** | 23 de setembro de 2025 [1] |
| **Tipo** | Blog post [1] |
| **URL** | https://cloud.google.com/blog/products/ai-machine-learning/introducing-doras-inaugural-ai-capabilities-model [1] |

---

## Resumo

O artigo do blog do Google Cloud apresenta o DORA AI Capabilities Model inaugural, desenvolvido para fornecer orientação baseada em dados a organizações que buscam ter sucesso na adoção e escala do desenvolvimento de software assistido por inteligência artificial [1, 2]. Em vez de focar apenas em métricas superficiais de adoção de ferramentas, o modelo enfatiza práticas técnicas e culturais específicas que amplificam ou desbloqueiam os benefícios práticos da AI [2, 3].

A construção do modelo seguiu uma metodologia rigorosa dividida em três fases: identificação e priorização de capacidades candidatas por meio de 78 entrevistas em profundidade e revisão de literatura, desenvolvimento e validação de perguntas de pesquisa, e uma avaliação empírica analisando dados de quase 5.000 respondentes de uma pesquisa ampla [3]. A análise concluiu que a adoção de ferramentas por si só não garante o sucesso; as organizações precisam ativamente cultivar o ambiente técnico e cultural adequado para que os desenvolvedores assistidos por AI prosperem [2, 4, 5].

O modelo destaca sete alavancas de sucesso: uma postura clara e comunicada sobre AI (*clear and communicated AI stance*), ecossistemas de dados saudáveis (*healthy data ecosystems*), dados internos acessíveis por AI (*AI-accessible internal data*), práticas sólidas de controle de versão (*strong version control practices*), trabalho em pequenos lotes (*working in small batches*), foco no usuário (*user-centric focus*) e plataformas internas de qualidade (*quality internal platforms*) [4, 6-9]. O estudo fornece recomendações práticas para ajudar líderes e engenheiros a maximizar os impactos em nível individual, de equipe e organizacional [4, 5, 10, 11].

---

## Frameworks Mencionados

- **DORA AI Capabilities Model** (discutido e introduzido): Apresentado como um modelo de capacidades estruturado em 7 pilares técnicos e culturais para maximizar o retorno do investimento em desenvolvimento assistido por AI [2-4].
- **SPACE / DevEx / Outros Frameworks**: Não foram explicitamente mencionados no texto desta fonte [1-13].

---

## Metricas Mencionadas

O texto identifica diversos resultados operacionais e dimensões de desempenho influenciados pelas capacidades do modelo de AI:

- **Individual effectiveness**: Amplificada por uma postura clara sobre AI [6], commits frequentes no sistema de controle de versão [8] e acesso das ferramentas de AI a dados internos contextualizados [7].
- **Organizational performance**: Amplificada significativamente por ecossistemas de dados saudáveis [7], postura clara de AI comunicada pela liderança [6] e plataformas internas de qualidade [4].
- **Code quality**: Impulsionada ao fornecer às ferramentas de AI acesso seguro a documentações e bases de código internas [7].
- **Team performance**: Amplificada pelo uso proficiente e frequente de recursos de *rollback* e *revert* no controle de versão [8] e por um foco centrado no usuário [9]. O texto ressalta que, na ausência de foco no usuário, a adoção de AI pode ter um impacto negativo no desempenho da equipe [9].
- **Product performance**: Amplificada pela prática consagrada da DORA de trabalhar em pequenos lotes (*working in small batches*) [8].
- **Friction / Atrito de desenvolvimento**: Reduzido no trabalho dos desenvolvedores por meio de políticas claras sobre uso de AI [6] e pela adoção de incrementos gerenciáveis de trabalho (*small batches*) [8].

*Nota:* Métricas de desempenho da DORA tradicional (como *lead time for changes*, *deployment frequency*, *MTTR* ou *change failure rate*) não foram nomeadas individualmente neste post específico [1-13].

---

## Insights para Praticantes

- **Clarify and socialize AI policies**: Estabelecer e comunicar com clareza as regras e ferramentas de AI permitidas na organização, criando a segurança psicológica necessária para experimentação sem ambiguidade legal ou operacional [6, 10].
- **Treat data as a strategic asset**: Investir na qualidade, acessibilidade e unificação dos dados internos para criar um ecossistema saudável que alimente os modelos de AI [7, 10].
- **Connect AI to internal context**: Superar assistentes genéricos integrando ferramentas de AI ao contexto interno da empresa (código-fonte, documentações e dados proprietários) de forma segura [7, 11].
- **Double-down on known best practices**: Manter a disciplina de trabalhar em pequenos lotes (*small batches*) para melhorar a performance do produto e reduzir o atrito na entrega de software [8, 11].
- **Prioritize user-centricity**: Manter as necessidades reais do usuário no centro da estratégia de produto para garantir que a maior velocidade de geração de código por AI resulte em valor real para a organização [9, 11].
- **Embrace and fortify safety nets**: Tratar o controle de versão como rede de segurança essencial, promovendo hábitos de *commits* frequentes e o uso ágil de mecanismos de *rollback* para gerenciar o maior volume e velocidade de código gerado por AI [5, 8].
- **Invest in internal platforms**: Disponibilizar plataformas internas de engenharia de qualidade com *guardrails* e capacidades compartilhadas que permitam escalar com segurança os ganhos de AI para toda a organização [4, 5].

---

## Avaliacao de Qualidade GL (Garousi et al.)

| Criterio | Pontuacao (0-1) |
|----------|----------------|
| Autoridade do autor/organizacao | 1.0 |
| Descricao de metodologia | 1.0 |
| Data de publicacao | 1.0 |
| Objetividade (vies comercial) | 0.5 |
| Referencias citadas | 0.5 |
| Contribuicao nova | 1.0 |
| **TOTAL** | **5.0/6** |

**Justificativa dos pontos:**
- **Autoridade (1.0)**: Autores pesquisadores com titulação acadêmica de Ph.D. (Kevin M. Storer e Derek DeBellis) vinculados ao DORA / Google Cloud, referência reconhecida na área [1, 2].
- **Metodologia (1.0)**: Apresentação transparente da abordagem de pesquisa em 3 fases (78 entrevistas/literatura, validação de questionários e análise empírica de survey com ~5.000 respondentes) [3].
- **Data (1.0)**: Publicado em 23 de setembro de 2025 [1].
- **Objetividade (0.5)**: Publicado em portal comercial (Google Cloud Blog) com chamadas promocionais ("Try Gemini Enterprise today"), embora grounded em pesquisa empírica [1, 2].
- **Referencias (0.5)**: Menciona literatura existente e aponta para o estudo completo do DORA 2025, porém sem uma lista formal de citações acadêmicas no texto do post [3, 12].
- **Contribuição nova (1.0)**: Introdução do modelo inaugural DORA AI Capabilities Model, trazendo evidências inéditas sobre quais práticas amplificam o sucesso da AI no desenvolvimento de software [2, 3].

---

*Extraido via NotebookLM em October 2026 para MLR: Software Developer Metrics in Practice*

---

💡 Gostaria de transformar esses achados em um relatório comparativo detalhado ou explorar como conectar essas 7 capacidades às suas métricas internas de engenharia?
# P2034 — Generative AI and the Future of Professional Software Development: Survey Findings from Finland

**Decisao: INCLUIDO | Qualidade: 4.5/5**

---

## Dados Bibliograficos

| Campo | Valor |
|-------|-------|
| **ID** | P2034 [1] |
| **Autores** | Samuli Määttä, Markus Kelanti, Burak Turhan [1] |
| **Ano** | 2026 [2] |
| **Venue** | 34th ACM Joint European Software Engineering Conference and Symposium on the Foundations of Software Engineering (FSE Companion ’26) [2] |
| **DOI** | 10.1145/3803437.3805619 [2] |
| **Tipo** | Conference paper (Workshop / Companion paper) [1, 2] |
| **Metodo** | Qualitative (Survey with open-ended qualitative analysis using open coding, constant comparison, and memoing following Socio-technical Grounded Theory) [1, 3, 4] |
| **Amostra** | 163 participantes no survey total; subamostra qualitativa de 100 respondentes para as perguntas abertas [1, 5, 6] |
| **Contexto** | Industry / Profissionais de software atuando na Finlândia (desenvolvedores, arquitetos, gestores, freelancers e empreendedores) [3, 6, 7] |
| **Modo de trabalho** | Not specified [3] |
| **Metodologia** | Not specified [3, 7] |

---

## Objetivo

O objetivo principal do artigo é investigar e documentar as visões, previsões e preocupações de profissionais de desenvolvimento de software na Finlândia em relação ao papel futuro da inteligência artificial generativa na profissão [1, 8, 9]. A partir de uma análise qualitativa de respostas abertas em um questionário aplicado entre dezembro de 2025 e fevereiro de 2026, o estudo busca oferecer um panorama centrado no praticante que complemente pesquisas focadas exclusivamente no desempenho de ferramentas, analisando impactos percebidos em papéis, habilidades, produtividade, qualidade do código e sustentabilidade do conhecimento técnico na área [1, 5, 9].

---

## Questoes de Pesquisa

- **RQ1:** What are the broader thoughts (e.g., predictions, concerns) of software professionals in Finland about the future role of AI in software development? [9]

---

## Metricas e Instrumentos de Avaliacao

| Metrica | Categoria | Nivel | Como Coletada | Validada |
|---------|-----------|-------|---------------|----------|
| **Produtividade Percebida** | Productivity | Individual / Team | Perguntas abertas do questionário de pesquisa (*self-reported*) [10-12] | No (Percebida / Qualitativa) [12] |
| **Qualidade da Base de Código** | Quality | Team / Organization | Percepção qualitativa e relatos de bugs e débito técnico [13-15] | No (Percebida / Qualitativa) [12, 14] |
| **Carga de Revisão de Código** | Activity / DevEx | Individual / Team | Relatos qualitativos sobre volume e esforço de revisão [11, 16, 17] | No (Percebida / Qualitativa) [16, 17] |
| **Anos de Experiência** | Background | Individual | Pergunta fechada demográfica do survey [6, 18] | Yes (Auto-declarada) [6, 18] |

---

## Frameworks e Metricas

### Frameworks Referenciados
- **DORA, SPACE, DevEx, GQM, HEART, OKR:** Nenhum destes frameworks tradicionais de métricas de software foi referenciado ou aplicado no artigo [1-77].
- **Socio-technical Grounded Theory (Hoda, 2024):** REFERENCED e APPLIED como enquadramento metodológico para a análise qualitativa (codificação aberta, comparação constante e *memoing*) [4].

### Frameworks Propostos
- O artigo não propõe um novo framework quantitativo de medição, mas sim um **esquema de categorização conceitual qualitativo** composto por 5 categorias principais (*AI adoption-related concerns*, *Changing nature of software development*, *Skilled AI usage*, *Long-term impact* e *Risks*) e seus respetivos conceitos e subcategorias [25, 29].

---

## Fatores que Influenciam Produtividade

### Fatores Positivos
| Fator | Categoria |
|-------|-----------|
| Experiência e senioridade do desenvolvedor (capacidade de saber exatamente o que pedir e avaliar a qualidade das saídas da IA) [11, 51, 60] | Human |
| Automação de tarefas manuais, mecânicas e repetitivas (como prototipagem, código auxiliar e testes simples) [11, 38] | Technical / Process |
| Automação na garantia de qualidade, gestão de requisitos e busca de informações [37] | Technical / Process |
| Equilíbrio entre ganhos de velocidade e revisão de código disciplinada e granular [11] | Process |
| Formulação precisa de enquadramento do problema, restrições, *trade-offs* e critérios de sucesso (*problem framing*) [52, 60] | Technical / Human |

### Fatores Negativos
| Fator | Categoria |
|-------|-----------|
| Pressão para adoção forçada ou orientada por *hype* sem necessidade real [31, 33] | Organizational / Process |
| Gestão inadequada (*foolish management*) que tenta substituir profissionais júniores sem entender o funcionamento da IA [30, 34, 61] | Organizational / Process |
| Dependência excessiva (*overreliance*), preguiça intelectual e "vibe coding" sem validação do código gerado [13, 42] | Human / Technical |
| Ilusão de produtividade (velocidade inicial na geração de código seguida de tempo excessivo corrigindo bugs em código mal compreendido) [13, 63] | Technical / Process |
| Superficialização da revisão de código e deterioração da disciplina de engenharia [17, 42, 43] | Process / Technical |
| Atrofia e perda de habilidades fundamentais de programação e resolução de problemas (*skill decay*) [38, 47, 57] | Human / Organizational |
| Reação de resistência dos desenvolvedores à imposição do uso de ferramentas de IA [33, 34] | Human / Organizational |

---

## Papel da IA e Automacao

| Campo | Valor |
|-------|-------|
| **Usa IA/ML?** | **Yes** — O estudo investiga o uso de ferramentas de IA generativa e modelos de linguagem (ex.: ChatGPT, GitHub Copilot, Midjourney, AI agents) em atividades de engenharia de software [1, 19, 41]. |
| **Automacao de coleta?** | **No** — A coleta de dados foi realizada via survey com questionários preenchidos por humanos; a codificação qualitativa foi conduzida manualmente e gerenciada com o software Quirkos [3, 5, 25]. |
| **Impacto de IA na produtividade?** | A IA é percebida como uma ferramenta que traz ganhos de produtividade expressivos para tarefas simples e para desenvolvedores experientes [11, 42, 51]. Contudo, o estudo aponta o risco da "ilusão de produtividade" (*productivity illusion*), em que os ganhos iniciais são anulados pelo aumento da carga de revisão de código, depuração e degradação da qualidade no longo prazo [12, 13, 63]. |

---

## Resultados Principais

- **Amostra e Respostas:** De um total de 163 respondentes do survey na Finlândia (dezembro/2025 a fevereiro/2026), 100 participaram das perguntas abertas opcionais analisadas qualitativamente no artigo [1, 5, 8].
- **Perfil Demográfico (N=100):** 50% possuem <10 anos de experiência, 24% possuem 10–19 anos, 14% possuem 20–29 anos e 12% possuem 30+ anos [6, 18]. A função mais comum foi *Full-Stack Developer* (21%), seguida por *Software Architect* (12%), *Back-End Developer* (9%), *DevOps Developer* (5%), *Data Analyst/Engineer/Scientist* (5%), *Development Manager* (5%), *CEO/CIO/CTO* (5%) e *Product Owner/Manager* (5%) [7, 18].
- **Distribuição por Categorias Emergentes:**
  - *Changing nature of software development* (65× citações): Deslocamento do foco da escrita de código manual para arquitetura, requisitos, garantia de qualidade, supervisão de agentes de IA e coordenação [29, 36, 40, 41].
  - *Risks* (46× citações): Dependência excessiva (*overreliance*, 27×), riscos de qualidade da base de código (19×), bolha de IA (9×) e ilusão de produtividade (8×) [14, 29, 42, 46].
  - *AI adoption-related concerns* (45× citações): Preocupação com a substituição de profissionais (25× — com foco nos júniores), frustração (15×), pressão de adoção (10×), *hype* (8×) e gestão inadequada (*foolish management*, 6×) [29-31, 33, 34].
  - *Long-term impact* (37× citações): Sustentabilidade do desenvolvimento (20×) — com destaque para a escassez de futuros seniores, quebra na transferência geracional de conhecimento e atrofia de habilidades (*skill decay*) [29, 54, 55, 57].
  - *Skilled AI usage* (26× citações): Necessidade de treinamento/educação (11×) e habilidades específicas de desenvolvedores experientes (6×) [29, 49, 51].
- **Substituição de Desenvolvedores Júniores:** Nenhum dos respondentes afirmou que a IA não substituirá júniores; vários relataram que o processo já está ocorrendo, reduzindo vagas de entrada e criando uma barreira de acesso ao mercado [30, 56].
- **Gargalo e Sobrecarga na Revisão de Código:** O uso de IA reduz o esforço para gerar funcionalidade, mas transfere o esforço crítico para a fase de revisão de código, onde os revisores precisam inspecionar minuciosamente trechos que o próprio autor não escreveu nem compreende totalmente [16, 17, 43].
- **Dilema "Sem júniores, não haverá seniores":** A substituição de tarefas júniores por IA reduz a contratação de iniciantes no curto prazo, o que ameaça a formação de futuros especialistas seniores no longo prazo, mesmo em um cenário onde a demanda por conhecimento sênior continua crescendo [26, 54, 55, 63].

---

## Desafios do Uso das Metricas

- **Ilusão de Produtividade baseada em Código Gerado (*Productivity Illusion*):** Medir a produtividade pela rapidez na entrega inicial de código cria uma "fachada de produto" e oculta bugs graves e débito técnico que exigirão tempo extra no futuro [13, 14, 63].
- **Deslocamento do Esforço para a Revisão de Código:** A geração massiva de código por IA provoca uma superficialização das revisões de código (*code review superficialisation*), deteriorando a disciplina de engenharia e a manutenibilidade do sistema [17, 42, 43].
- **Adoção Impulsionada por Gestão Desconectada (*Foolish Management*):** Decisões gerenciais baseadas em *hype* que tentam substituir desenvolvedores por ferramentas de IA sem compreender os custos ocultos de validação e arquitetura [30, 34, 61].
- **Deterioração do Raciocínio e Aprendizado (*Skill Decay* & *Outsourcing Thinking*):** A delegação prematura da escrita de código e resolução de problemas para a IA prejudica a compreensão conceitual e a capacidade futura de validar outputs complexos [13, 57, 62].
- **Visão de Curto Prazo (*Short-termism*):** Foco excessivo na velocidade imediata de desenvolvimento em detrimento da sustentabilidade e segurança da arquitetura de software no longo prazo [15, 63].

---

## Avaliacao de Qualidade Metodologica

| Criterio | Pontuacao (0-2) |
|----------| voting |
| Objetivo claramente definido | 2 |
| Metodologia adequada ao objetivo | 2 |
| Amostra/contexto descrito adequadamente | 2 |
| Ameacas a validade discutidas | 2 |
| Resultados com evidencia suficiente | 2 |
| Contribuicao clara para pratica ou teoria | 1 |
| **TOTAL** | **11/12** |

---

## Limitacoes

- **Instantâneo Temporal (*Point-in-time snapshot*):** Os resultados refletem a percepção dos profissionais em um momento específico (dezembro/2025 a fevereiro/2026), podendo mudar com a evolução contínua das ferramentas e práticas de IA [5, 66].
- **Amostragem Não-Probabilística:** O estudo utilizou amostragem por conveniência e bola de neve (*snowball sampling*), de forma que os achados não podem ser generalizados para toda a população de desenvolvedores da Finlândia ou internacionalmente [5, 67].
- **Viés de Autoseleção (*Self-selection bias*):** Ocorreu tanto na adesão inicial ao survey quanto na decisão de responder às perguntas abertas opcionais finais, com potencial super-representação de profissionais insatisfeitos com a IA generativa [67].
- **Subjetividade na Análise Qualitativa:** A codificação interpretativa dos dados foi conduzida majoritariamente pelo primeiro autor, embora sob supervisão e reuniões semanais de validação com os demais pesquisadores [25, 68].
- **Tamanho e Dispersão da Amostra (*Data sparseness*):** Devido à natureza ampla das perguntas abertas, os tópicos variaram bastante e alguns achados se basearam em um número pequeno de pontos de dados [68].

---

## Contribuicao Principal

A principal contribuição deste artigo é registrar e estruturar, a partir da perspectiva direta dos praticantes de engenharia de software na Finlândia, a diversidade de observações, previsões e preocupações sobre o futuro do desenvolvimento profissional impulsionado pela IA generativa [1, 9, 70]. Em contraste com pesquisas puramente focadas no desempenho quantitativo de ferramentas, o trabalho revela e categoriza tensões sociotécnicas fundamentais da transformação em curso — como o conflito entre produtividade imediata e qualidade do código no longo prazo, o aumento da carga e complexidade da revisão de código, a perda de habilidades fundamentais (*skill decay*) e o risco à sustentabilidade da profissão devido à redução de oportunidades de aprendizado para desenvolvedores júniores [12, 13, 29, 55, 63].

---

*Extraido via NotebookLM em October 2026 para MLR: Software Developer Metrics in Practice*

---

💡 Se desejar, posso elaborar um relatório detalhado em PDF ou apresentar uma síntese comparativa com outros artigos do seu projeto.
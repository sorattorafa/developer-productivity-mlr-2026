# G113 — AI's impact on software engineers in 2026: key trends, Part 2

**Decisao: INCLUIDO | Qualidade GL: 6/6**

---

## Dados Bibliograficos

| Campo | Valor |
|-------|-------|
| **ID** | G113 |
| **Autor/Organizacao** | Gergely Orosz and Elin Nilsson / The Pragmatic Engineer |
| **Data** | May 19, 2026 |
| **Tipo** | Blog post / Paid Newsletter Deep Dive |
| **URL** | https://newsletter.pragmaticengineer.com/p/ai-impact-on-software-engineers-part-2 |

---

## Resumo

Este artigo conclui uma série de três partes baseada em uma pesquisa realizada com mais de 900 assinantes do *The Pragmatic Engineer* em 2026 sobre o impacto do uso de ferramentas de IA na engenharia de software. O estudo aborda os *tradeoffs* individuais e organizacionais da adoção de IA, destacando que, embora as ferramentas reduzam tarefas repetitivas e permitam que desenvolvedores realizem trabalhos de maior valor, elas também causam frequentes interrupções por *context switching* devido ao paralelismo de tarefas e geram expectativas irrealistas de produtividade por parte da gestão. Além disso, a adoção em escala se mostra desafiadora, funcionando como um amplificador da cultura de engenharia pré-existente e não como uma solução mágica para problemas organizacionais.

Um achado central do relatório é a percepção generalizada de queda na qualidade da base de código (*codebase quality*). A proliferação de código de baixa qualidade (*AI slop*), duplicações e abstrações inadequadas tem sobrecarregado os processos de *code review*, elevando a ocorrência de *bugs* e incidentes em produção. A liderança executiva frequentemente demonstra pouca preocupação com essa degradação, focando prioritariamente no aumento de velocidade (*velocity*) e na redução de custos de curto prazo. Consequentemente, o fardo de manutenção (*maintenance burden*) recai desproporcionalmente sobre um número cada vez menor de engenheiros seniores que ainda compreendem a arquitetura do sistema, levando em alguns casos ao abandono das práticas de *code review*.

O estudo analisa também o impacto em profissionais menos experientes e as dinâmicas de equipe. Engenheiros *junior* enfrentam dificuldades para validar as respostas da IA, consomem custos mais elevados de *tokens* e perdem oportunidades tradicionais de aprendizado por delegação de tarefas, uma vez que seniores agora automatizam tais atividades via IA. Adicionalmente, a falta de consistência no *tooling* entre equipes gera caos arquitetural, enquanto o uso de *AI agents* cria comportamentos de dependência (*slot machine dynamics*). Como reação à queda de qualidade na documentação técnica e nas RFCs, algumas empresas começaram a reverter (*rollback*) ou restringir o uso de ferramentas de IA.

---

## Frameworks Mencionados

* **DORA / SPACE / DevEx**: Nenhum framework formal de métricas de engenharia (como DORA, SPACE ou DevEx) é explicitamente analisado ou recomendado no texto. O termo *developer experience* é mencionado apenas de forma genérica para descrever a insensibilidade dos desenvolvedores a arquiteturas ruins.
* **Microsoft 365 Copilot Study**: Pesquisa da Microsoft (publicada em 5 de maio de 2026) citada para comparar achados sobre como ferramentas de IA expandem a capacidade de execução de tarefas de alto valor tanto por desenvolvedores quanto por não desenvolvedores.
* **Práticas de Engenharia e Guardrails**: O artigo estrutura a análise de adoção em torno de práticas fundamentais de engenharia, destacando a necessidade de *guardrails* (testes automatizados e automação de *deployment*), documentação de decisões arquiteturais e código de alta qualidade como pré-requisitos para o sucesso com IA.

---

## Metricas Mencionadas

* **Tamanho da Amostra da Pesquisa**: Mais de 900 respostas recebidas de assinantes da *The Pragmatic Engineer*.
* **Consumo e Custos de Tokens (*AI Token Bills*)**: Menção ao uso desproporcional de *tokens* por engenheiros *junior*, que figuram no topo dos gastos organizacionais em casos de uso não produtivos.
* **Ganhos de Produtividade / Velocidade**: Relatos informais de ganho de produtividade de até "10x" por engenheiros em cenários específicos, contrastados com o uso da velocidade (*velocity*) pela gestão como linha de base sem reconhecimento da qualidade.
* **Metas Organizacionais de Adoção de IA**: Alvos quantitativos impostos pela gestão para adoção universal de IA (e.g., metas de 50%, 80% ou 100% de uso de IA em certas tarefas/“tokenmaxxing”).
* **Incidentes de Produção e Qualidade de Código**: Aumento no volume de *bugs*, surgimento de incidentes dispendiosos em produção (*costly production incidents*) e proliferação de *pull requests* (PRs) volumosos e sem revisão adequada.

---

## Insights para Praticantes

* **A IA é um Amplificador de Cultura, Não um Corretor**: A IA multiplica tanto as boas quanto as más práticas de engenharia. Equipes com *guardrails* sólidos (testes automatizados, documentação e boa arquitetura) extraem valor positivo, enquanto equipes sem essas práticas acumulam débitos técnicos e complexidade de forma acelerada.
* **Foco em Resiliência e Testes**: O aumento na velocidade de geração de código exige investimento proporcional em testes e resiliência para conter a elevação na taxa de *bugs* introduzidos por desenvolvimento orientado a IA.
* **Apoio e Mentoria para Engenheiros Juniores**: Engenheiros menos experientes necessitam de espaço para aprendizado (*breathing room*) e orientação para avaliar código gerado por IA. Substituir a delegação de tarefas humanas para *juniors* por IA compromete o desenvolvimento de futuras gerações de talentos.
* **Governança de Tooling em Equipe**: A escolha totalmente livre de ferramentas de IA por indivíduo gera fragmentação e caos de *tech stack*. É fundamental estabelecer diretrizes de consistência no nível de equipe.
* **Coragem para Executar Rollbacks**: Organizações maduras devem monitorar a qualidade do raciocínio técnico e das RFCs, estando dispostas a restringir ou fazer *rollback* de ferramentas de IA caso ocorra deterioração da qualidade do produto ou aumento de incidentes.

---

## Avaliacao de Qualidade GL (Garousi et al.)

| Criterio | Pontuacao (0-1) |
|----------|----------------|
| Autoridade do autor/organizacao | 1.0 |
| Descricao de metodologia | 1.0 |
| Data de publicacao | 1.0 |
| Objetividade (vies comercial) | 1.0 |
| Referencias citadas | 1.0 |
| Contribuicao nova | 1.0 |
| **TOTAL** | **6/6** |

---

*Extraido via NotebookLM em October 2026 para MLR: Software Developer Metrics in Practice*

💡 Deseja que eu analise a Parte 1 deste estudo ou compare estes resultados com outras fontes de literatura cinzenta da sua coleção?
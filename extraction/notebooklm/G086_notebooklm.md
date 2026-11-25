# G086 — AI-Assisted and Low-Code Development in Practice: A Case Study of SocialMize on Developer Productivity, Code Quality, and Perceived Trust and Usability

**Decisao: INCLUIDO | Qualidade GL: 5.0/6**

---

## Dados Bibliograficos

| Campo | Valor |
|-------|-------|
| **ID** | G086 |
| **Autor/Organizacao** | Mohammad Rafi Uddin / University of Turku (Supervisors: Tuomas Mäkilä, Juuso Rytilahti) [1, 2] |
| **Data** | June 9, 2026 [2] |
| **Tipo** | Master's Thesis [1, 2] |
| **URL** | https://github.com/rafi34/socialmize [3] |

---

## Resumo

Esta dissertacao de mestrado da Universidade de Turku investiga o impacto de ferramentas de codificacao assistidas por IA e plataformas de desenvolvimento *low-code* (especificamente Lovable e Supabase) na produtividade de desenvolvedores, qualidade de codigo, carga cognitiva e confianca percebida [1, 2]. O estudo utiliza uma abordagem empirica multimétodo focada no SocialMize, uma aplicacao SaaS em producao para criadores de conteudo [2]. A pesquisa combina um estudo de caso longitudinal (analisando 3.945 *commits* e uma amostra estratificada de 117 pares de *prompt-response*), um experimento controlado *within-subjects* com microtarefas de *frontend*, e uma pesquisa (*survey*) com praticantes da industria (N = 30) [2-5].

Os resultados demonstram que a assistencia de IA acelera significativamente tarefas repetitivas e ricas em padroes (*pattern-rich*), alcancando uma reducao de 57.5% no tempo de conclusao de tarefas (85 min vs. 200 min no total) e uma reducao de 71% em erros de compilacao no experimento controlado [6-8]. No entanto, 99.4% dos *commits* do projeto foram gerados pela IA, e os ganhos de velocidade exigiram maior iteracao e verificacao semantica [6, 9, 10]. Embora o codigo gerado por IA apresente alta alinhamento estrutural com a base de codigo existente, o retrabalho concentrou-se fortemente em superficies acopladas ao esquema de banco de dados (*schema-coupled*), tais como as *edge functions* do Supabase (que apresentaram uma taxa de duplicacao de codigo de 6.57% e 312 migracoes de banco de dados) [11-13].

O estudo revela uma mudanca fundamental no papel do desenvolvedor, transicionando de autor de codigo (*code author*) para especificador de intencao, revisor e validador (*reviewer-and-prompter*) [6, 14, 15]. Erros mecanicos de compilacao sao amplamente substituidos por defeitos semanticos sutis em tempo de execucao (*compile-clean semantic defects*, ou "sintaxe correta, intencao errada") [16, 17]. Os resultados do *survey* indicam alta percepcao de produtividade (media de 4.1/5) acompanhada por uma confianca condicional e filtrada por revisao (*review-gated trust*, media de 3.5/5), confirmando que as ferramentas de IA atuam como uma aumentacao supervisionada (*supervised augmentation*) em vez de uma automacao total [15, 18, 19].

---

## Frameworks Mencionados

- **SPACE Framework** (*Forsgren et al., 2021 / Houck et al., 2025*): **Discutido**. Apresentado como uma abordagem multidimensional para medicao de produtividade de desenvolvedores (*Satisfaction, Performance, Activity, Communication & Collaboration, Efficiency & Flow*) para ir alem de metricas simples baseadas em tempo ou linhas de codigo [20-22].
- **DevEx / Software Developer Experience Framework**: **Discutido**. Analisado em conjunto com o SPACE e estudos de experiencia do desenvolvedor para mensurar satisfacao, fluxo e carga cognitiva em ambientes de desenvolvimento assistidos por IA [22-24].
- **SE 3.0 / AI-Native Software Engineering Vision** (*Hassan et al., 2024*): **Discutido**. Discute a transicao de *task-driven AI copilots* para *goal-driven AI pair programmers* e paradigmas de engenharia de software nativos em IA [25, 26].
- **Multi-Agent Collaborative Frameworks** (*ChatDev, MetaGPT, AutoGen*): **Discutido e comparado**. Comparado estruturalmente com o fluxo de trabalho do Lovable, destacando que o Lovable mantem o desenvolvedor humano como o orquestrador e especificador unico de intencao [27-30].
- **DORA Framework**: **Nao mencionado** no texto do documento.

---

## Metricas Mencionadas

- **Tempo de Conclusao de Tarefa (*Time-to-Completion*)**: Medido em tempo real no experimento de microtarefas; a condicao assistida por IA foi 57.5% mais rapida no total (85 min vs. 200 min) [7, 8].
- **Erros de Compilacao e Defeitos Semanticos**: 17 erros na condicao manual vs. ~5 erros na condicao assistida por IA (reducao de 71% em erros mecanicos de compilacao), mas com introducao de defeitos semanticos que compilavam sem erros [8, 17, 31].
- **Linhas de Codigo (LOC) e *Churn***: 151.762 LOC em TypeScript/TSX distribuidas em 655 arquivos [11]; analise de *churn* por arquivo (*e.g.*, `Strategy.tsx` reescrito ~24 vezes com 29.061 linhas de *churn*; `.lovable/plan.md` com 26.205 linhas de *churn*) [32].
- **Taxa de Duplicacao de Codigo (*jscpd 4.x*)**: Medicao de *clones* no nivel de *tokens*; 3.92% no repositorio global, atingindo 6.57% em *edge functions* no servidor vs. 3.04% em componentes React TSX [13].
- **Taxa e Contagem de Reversoes (*Reverts*)**: 80 reversoes explicitas no Git (taxa de reversao de 2.03%), das quais 97.5% (78/80) foram executadas pela propria IA em resposta a *prompts* corretivos do usuario [33, 34].
- **Cadencia de *Commits* e Distribuicao de Autoria**: 3.945 *commits* ao longo de 345 dias (media de 22.3 *commits*/dia ativo) [35]; 99.4% de autoria da IA (`gpt-engineer-app[bot]`) vs. 0.6% humana [9, 10].
- **Taxa de *Prompts* Corretos na Primeira Tentativa (*First-Time-Correct*) e Cadeias de Retrabalho (*Rework Chains*)**: No experimento, apenas 33% (4/12) dos *prompts* foram corretos de primeira e 42% (5/12) geraram cadeias de retrabalho [8, 31]. Na amostra de 117 pares do estudo de caso, 27.4% continham falhas de IA (*I-flag*) e 24.8% eram cadeias de retrabalho [36].
- **Frequencia de Migracao de Esquema de Banco de Dados**: 312 migracoes SQL (~1 mudanca de esquema a cada 487 LOC), refletindo renegociacao continua de estruturas de dados via *chat* [11, 12].
- **Marcadores de Seguranca de Tipos (*Type-Safety Markers*)**: Contados via *ripgrep*: 1.018 anotacoes `: any` em 314 arquivos; 542 instrucoes `catch (e: any)`; 897 chamadas `console.log`; 0 diretivas `@ts-ignore`; e apenas 2 comentarios `TODO/FIXME/HACK` [37].
- **Contagem de Testes Automatizados**: 0 arquivos de teste unitario ou de integracao (`*.test.*` / `*.spec.*`), demonstrando dependencia total de verificacao visual em tempo real [12, 38].
- **Pontuacoes de Percepcao do Desenvolvedor (*Likert Scores*, N = 30, escala 1-5)**: Rapidez na conclusao de tarefas (4.1), economia geral de tempo (4.1), conforto no fluxo de trabalho (4.0), complexidade desnecessaria do codigo (3.9), necessidade de revisao/correcao (3.8), confusao no codigo (3.3), utilidade do *low-code* (3.7) e confianca restrita a tarefas nao criticas (3.5) [19].
- **Confiabilidade Inter-Avaliadores (*Cohen's Kappa κ*)**: κ = 0.72 (95% IC [0.62, 0.81], concordancia substantiva de Landis & Koch) entre Claude e Gemini-3-flash na codificacao axial dos 117 pares de *prompt-response* [39, 40].

---

## Insights para Praticantes

- **Mudanca de Papel Profissional**: Desenvolvedores devem se preparar para uma transicao onde a carga cognitiva deixa de ser a escrita manual de sintaxe e passa a ser a especificacao precisa de intencoes, avaliacao de solucoes geradas e verificacao semantica [14, 15].
- **Atencao a Defeitos Semanticos "Silenciosos"**: Ferramentas de IA reduzem drasticamente erros mecanicos de compilacao, mas frequentemente produzem codigos sintaticamente validos com premissas incorretas ("sintaxe certa, intencao errada") [16, 17]. Processos de revisao devem focar em casos de borda, regras de negocio e alinhamento com o esquema de banco de dados [17, 41].
- **Dominio do Dominio e Requisito Premissa**: A assistencia de IA potencializa desenvolvedores com profundo conhecimento do dominio, permitindo que formulem melhores *prompts* e avaliem criticamente os resultados; ela nao substitui a necessidade de conhecimento tecnico e arquitetural [42].
- **Necessidade Crucial de Testes Automatizados**: Como o codigo gerado por IA introduz riscos semanticos e mudancas frequentes de esquema, possuir uma suite robusta de testes unitarios e de integracao antes de adotar geradores de IA e fundamental para evitar o acumulo de debito tecnico [41, 43].
- **Arquitetura Modular em *Backend***: Plataformas LCNC e de IA tendem a gerar codigo reutilizavel duplicado em funcoes de servidor (*edge functions*, taxa de duplicacao de 6.57%) em vez de refatorar modulos utilitarios [13, 37]. Instrucoes explicitas no *prompt* ou refatoracoes manuais sao necessarias para manter a manutenibilidade [37].
- **Confianca Condicional e Graduada**: Praticantes devem adotar uma postura de confianca condicional — utilizando IA para prototipagem rapida, *scaffolding* de UI e operacoes rotineiras de CRUD, mas mantendo verificacao rigorosa e orientada por revisao em logicas de negocio complexas [19, 44, 45].

---

## Avaliacao de Qualidade GL (Garousi et al.)

| Criterio | Pontuacao (0-1) |
|----------|----------------|
| Autoridade do autor/organizacao | 0.5 |
| Descricao de metodologia | 1.0 |
| Data de publicacao | 1.0 |
| Objetividade (vies comercial) | 0.5 |
| Referencias citadas | 1.0 |
| Contribuicao nova | 1.0 |
| **TOTAL** | **5.0/6** |

---

*Extraido via NotebookLM em October 2026 para MLR: Software Developer Metrics in Practice*
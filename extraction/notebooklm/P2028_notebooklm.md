# P2028 — An Eye for AI: Eye-Tracking the Micro-Interruptions of GenAI Code Suggestions

**Decisao: INCLUIDO | Qualidade: 5/5** [1]

---

## Dados Bibliograficos

| Campo | Valor |
|-------|-------|
| **ID** | P2028 [1] |
| **Autores** | Tarek Alakmeh, Sarah D’Angelo, Thomas Fritz [1] |
| **Ano** | 2026 [2] |
| **Venue** | IEEE/ACM 48th International Conference on Software Engineering (ICSE ’26) [2] |
| **DOI** | 10.1145/3744916.3773132 [2] |
| **Tipo** | Conference paper [2] |
| **Metodo** | Experiment / Quantitative (Eye-tracking study combined with IDE DOM and keypress event logging) [1, 3, 4] |
| **Amostra** | **33 participants analyzed** (17 professional software developers and 16 CS students; initially 35 recruited, 2 excluded due to technical logging issues) [5-7] |
| **Contexto** | **Mixed** (Industry and Academic — participants recruited from 3 software development companies and a university eye-tracking laboratory) [5, 6] |
| **Modo de trabalho** | **On-site** (Sessions conducted physically at the offices of 3 participating software companies and in a university eye-tracking lab) [5, 8] |
| **Metodologia** | **Not specified** (Participants performed individual TypeScript programming tasks modifying a game codebase in VS Code Web IDE) [9, 10] |

---

## Objetivo

This paper aims to empirically evaluate how software developers interact with and process real-time generative AI inline code suggestions (specifically GitHub Copilot) during programming tasks [1, 3, 11]. By combining high-resolution mobile eye-tracking with fine-grained DOM event logging in Visual Studio Code, the study quantifies visual attention, acceptance/rejection behavior, and the subtle cognitive overhead (micro-interruptions) introduced by AI code completions [1, 3, 4, 12].

---

## Questoes de Pesquisa

- **RQ1**: How do developers engage with and perceive generative AI code suggestions? [3, 13]
- **RQ2**: How do the characteristics of generative AI code suggestions affect developers’ engagement? [13]

---

## Metricas e Instrumentos de Avaliacao

| Metrica | Categoria | Nivel | Como Coletada | Validada |
|---------|-----------|-------|---------------|----------|
| **Dwell Time** (Tempo de Olhar/Fixação na Sugestão) | DevEx / Activity | Individual | Rastreamento ocular móvel (SR Research EyeLink Portable Duo, 2000 Hz) medindo a duração total das fixações dentro da Área de Interesse (IA) da sugestão [4, 12, 14] | Yes [12, 14] |
| **Suggestion Duration** (Tempo de Exibição da Sugestão) | Activity | Individual | Extensão personalizada do Chrome (PosEyeDOM) registrando timestamps de aparecimento e desaparecimento do DOM no VS Code Web [4, 15] | Yes [4, 15] |
| **Acceptance Rate** (Taxa de Aceitação) | Productivity / Quality | Individual | Logs sincronizados de eventos de teclado (tecla `TAB` pressionada enquanto a sugestão estava visível) [7, 12] | Yes [7, 12] |
| **Active Rejection Rate** (Taxa de Rejeição Ativa) | DevEx / Activity | Individual | Logs de teclado/mouse (tecla `ESC` pressionada ou clique para remover a sugestão) [12, 16] | Yes [12, 16] |
| **Passive Rejection / Ignored Rate** (Rejeição Passiva / Ignoradas) | DevEx / Activity | Individual | Sugestões que desapareceram ao continuar digitando sem engajamento ou sem fixação visual (>250ms) [7, 16, 17] | Yes [7, 17] |
| **Deletion Rate** (Taxa de Deleção de Código Pós-Interrupção) | Quality / Activity | Individual | Análise de frequência de eventos de deleção (Hz) em janelas temporais de interrupção ao redor de sugestões rejeitadas vs. linha de base da sessão [18, 19] | Yes [18] |
| **Startup Cost** (Custo Fixo de Início de Leitura) | DevEx / Cognition | Individual | Modelo de regressão não-linear ajustado ao tempo de olhar normalizado por caractere (\\(y = a/x + b\\)) [20, 21] | Yes [20, 21] |
| **Task Completion Time** (Tempo de Conclusão da Tarefa) | Productivity | Individual | Registros de tempo de início/fim das tarefas durante a sessão de 45 minutos [7, 9] | Yes [7] |
| **Perceived Helpfulness** (Utilidade Percebida) | DevEx / Satisfaction | Individual | Questionário pós-experimento em escala Likert unipolar de 1 a 5 [22-24] | Yes [22, 23] |
| **Perceived Distraction** (Distração Percebida) | DevEx / Satisfaction | Individual | Questionário pós-experimento em escala Likert unipolar de 1 a 5 [22, 23, 25] | Yes [22, 23] |
| **Task Difficulty** (Dificuldade da Tarefa) | DevEx | Individual | Formulário pós-tarefa em escala Likert de 1 a 5 [9] | Yes [9] |
| **Mental Effort** (Esforço Mental) | DevEx / Cognition | Individual | Formulário pós-tarefa utilizando a escala Paas (1 a 9) [9] | Yes [9, 26] |

---

## Frameworks e Metricas

### Frameworks Referenciados
- **SPACE / DORA / DevEx / GQM**: Discussed conceptually in related literature on software developer productivity and cognitive metrics; the paper explicitly notes that relying solely on superficial proxy metrics like acceptance rate or keystrokes saved masks hidden review costs and cognitive friction [27-30].
- **Paas Scale** (APPLIED): Applied directly after each programming task as a 9-point subjective rating instrument for mental workload and cognitive effort [9, 26].

### Frameworks Propostos
- **PosEyeDOM / Gaze-DOM Synchronization Method**: The paper proposes and implements an open-source technical and methodological framework combining a lightweight Chrome extension (`PosEyeDOM`) using `MutationObserver` with mobile eye-tracking (`EyeLink Portable Duo`) to dynamically calculate bounding boxes, error margins, and eye fixations on transient web IDE UI elements [4, 12, 15, 31, 32].

---

## Fatores que Influenciam Produtividade

### Fatores Positivos
| Fator | Categoria |
|-------|-----------|
| **Sugestões como ponto de partida**: Oferecem esboços ou estruturas de código iniciais que auxiliam a aprendizagem, recordação de APIs e orientação do desenvolvedor [27, 33, 34] | Technical / Process |
| **Maior eficiência em sugestões longas**: Sugestões mais longas diluem o "startup cost" cognitivo fixo (~256 ms), tornando a leitura por caractere mais rápida do que várias sugestões curtas equivalentes [20, 21, 29] | Technical / Human |
| **Aumento da familiaridade ao longo da tarefa**: A taxa de aceitação de sugestões aumenta significativamente na fase final das tarefas/sessões (subindo de 19.9% para 30.1%), conforme o desenvolvedor ganha contexto [35, 36] | Human / Process |

### Fatores Negativos
| Fator | Categoria |
|-------|-----------|
| **Micro-interrupções e quebra de fluxo**: Sugestões inadequadas interrompem a atenção visual e o modelo mental do desenvolvedor (~51 interrupções por sessão de 45 min) [13, 18, 37] | Process / Human |
| **Sobrecarga de sugestões ("Suggestion Overload")**: Exibição contínua e não solicitada de sugestões que geram ruído cognitivo e visual (50.5% das sugestões nem chegam a ser olhadas) [13, 17, 28, 37] | Technical / Process |
| **Aumento da taxa de deleção de código**: Picos significativos na frequência de deleção de código recém-escrito logo após encontrar sugestões rejeitadas (0.226 Hz vs. 0.039 Hz na linha de base) [18] | Process / Technical |
| **Custo fixo de avaliação ("Startup Cost")**: Todo surgimento de sugestão consome um tempo fixo de percepção inicial (~256 ms) antes mesmo do processamento do conteúdo [20, 21] | Human |
| **Formato intrusivo de texto fantasma ("Ghost Text")**: Completamentos em bloco de múltiplas linhas ocupam espaço no editor e deslocam o código ao redor, gerando maior fricção do que menus tradicionais [34, 38, 39] | Technical / Human |

---

## Papel da IA e Automacao

| Campo | Valor |
|-------|-------|
| **Usa IA/ML?** | **Yes** — Generative AI code suggestions powered by LLMs (GitHub Copilot) evaluated during live TypeScript coding sessions in Visual Studio Code Web [1, 3, 9]. |
| **Automacao de coleta?** | **Yes** — Automated collection using PosEyeDOM (Chrome Extension with DOM `MutationObserver` throttled at 200ms) synchronized with SR Research `WebLink` eye-tracking software [4, 12, 15]. |
| **Impacto de IA na produtividade?** | **Mixed / Nuanced** — While developers subjectively perceive AI suggestions as helpful (mean 3.60/5) [23, 24], **50.5% of generated suggestions are never looked at** [17], **76.7% of looked-at suggestions are rejected** [16], and each rejected suggestion causes a micro-interruption (dwell time ~0.9s, active rejection ~3.0s) [18] that elevates code deletion rates and interrupts cognitive flow [13, 18, 37]. |

---

## Resultados Principais

- **Metade das sugestões é ignorada**: De 4.444 sugestões geradas durante as sessões, **50.5% (2.242) foram ignoradas visualmente** ou duraram menos de 250 ms, demonstrando um alto volume de processamento desperdiçado [7, 17].
- **Baixa taxa de aceitação das sugestões analisadas**: Das 2.202 sugestões efetivamente olhadas (>250 ms), **76.7% foram rejeitadas** (71.2% passivamente ao continuar digitando e 5.5% ativamente via `ESC`/clique) e apenas **23.3% (514) foram aceitas** [16, 17].
- **Custo de tempo em rejeições ativas**: O tempo médio de exibição de uma sugestão foi de 1.5s (tempo de olhar/dwell time de 0.9s) [18]. No entanto, **sugestões rejeitadas ativamente exigiram o dobro do tempo de avaliação (3.0s de exibição)** [18].
- **Acúmulo de micro-interrupções**: Os desenvolvedores enfrentaram em média **51 micro-interrupções por sessão de 45 minutos** (>1 por minuto), acumulando cerca de 1 minuto de foco visual puramente dedicado a avaliar sugestões, sendo a maioria não aproveitada [18].
- **Disrupção comportamental (Deleções)**: A taxa de deleção de código recém-digitado foi **mais de 5 vezes maior nas janelas temporais de interrupção por sugestões rejeitadas (0.226 Hz)** em comparação com o restante da sessão (0.039 Hz) [18].
- **Existência de um Custo Cognitivo de Início ("Startup Cost")**: A leitura de sugestões apresenta um custo cognitivo fixo inicial de **\\(a = 256.32\text{ ms}\\)** mais um custo variável de **\\(b = 11.51\text{ ms por caractere}\\)** [20, 21]. Sugestões mais curtas são avaliadas de forma mais lenta por caractere [20].
- **Comprimento não afeta aceitação, mas o tempo sim**: O tamanho da sugestão (média de 27.7 caracteres nas aceitas vs. 27.3 nas rejeitadas) **não influenciou a taxa de aceitação (\\(p = 0.7892\\))** [40]. Porém, a aceitação **aumentou significativamente no final das tarefas (subindo de 19.9% no 1º quartil para 30.1% no 4º quartil, \\(p = 0.0054\\))** [35].
- **Percepção subjetiva dos desenvolvedores**: As sugestões foram avaliadas como **úteis (média 3.60/5)**, mas também como **levemente distrativas (média 2.11/5)**, com **66% dos participantes relatando distração leve** e 14% distração moderada [23-25].

---

## Desafios do Uso das Metricas

- **Taxa de Aceitação como Métrica "Proxy" Enganosa (Anti-pattern)**: Maximizar estritamente a taxa de aceitação ou economia de digitação ignora o custo cognitivo invisível das micro-interrupções, o tempo gasto revisando código incorreto e as deleções subsequentes [23, 29, 30].
- **Avaliação Superficial da Produtividade**: Medir apenas velocidade de geração ou linhas aceitas esconde o aumento de tempo gasto em depuração, revisão e quebra de modelos mentais [15, 28, 30, 41].
- **Sobrecarga de Apresentação Indiscriminada**: O envio contínuo e sem modulação de sugestões assertivas ("ghost text") trata interrupções de código complexo como se fossem autocompletar tradicionais de palavra-chave, gerando poluição visual [28, 34, 37].

---

## Avaliacao de Qualidade Metodologica

| Criterio | Pontuacao (0-2) |
|----------|----------------|
| Objetivo claramente definido | **2** (Objetivos e RQs investigando engajamento e custos cognitivos perfeitamente articulados) [1, 3, 13] |
| Metodologia adequada ao objetivo | **2** (Combinação rigorosa de eye-tracking de alta frequência de 2000 Hz com logging no DOM do IDE) [3, 4, 14] |
| Amostra/contexto descrito adequadamente | **2** (Detalhamento completo de 33 participantes, incluindo anos de experiência, contexto profissional vs. acadêmico) [5, 6] |
| Ameacas a validade discutidas | **2** (Discussão minuciosa sobre validade externa, interna e de construto, incluindo limitações do logger e alterações na interface) [19, 42-44] |
| Resultados com evidencia suficiente | **2** (Dados quantitativos robustos, testes estatísticos de significância e visualizações de gaze/logs) [7, 17, 18, 21, 35] |
| Contribuicao clara para pratica ou teoria | **2** (Contribuições teóricas sobre micro-interrupções e diretrizes práticas para design de assistentes de IA) [31, 36, 39, 45] |
| **TOTAL** | **12/12** |

---

## Limitacoes

- **Escopo de Linguagem e Desenvolvedores**: Estudo realizado com 33 participantes em tarefas em TypeScript/JavaScript; os achados podem não se generalizar diretamente para outras linguagens ou bases de código legadas gigantescas [42].
- **Tempo Limite e Escopo da Tarefa**: Sessões experimentais limitadas a 45 minutos com modificação do jogo Chrome Dino, o que pode não capturar dinâmicas de longo prazo ou reuniões/coordenação de equipe [9, 43].
- **Inacurácias do Eye-Tracking e Throttling**: Pequenas imprecisões no mapeamento do olhar durante rolagem/digitação rápida e limite de amostragem do logger (200 ms) que pode ter perdido sugestões ultra-rápidas [44].
- **Variação na Interface do IDE**: Os últimos 12 participantes receberam sugestões com realce de sintaxe devido a atualizações do VS Code (embora testes estatísticos tenham mostrado ausência de efeito significativo na aceitação, \\(p = 0.1555\\)) [44].
- **Viés de Auto-relato**: Respostas a questionários pós-experimento sujeitas a viés de memória e viés de sensibilidade social pela divulgação prévia do estudo [19, 46].

---

## Contribuicao Principal

The primary contribution of this paper is the **first in-depth empirical eye-tracking study quantifying the real-time visual engagement and cognitive costs of generative AI code suggestions** during active programming [1, 45, 46]. By capturing gaze behavior alongside precise DOM suggestion logs across 33 developers, the authors reveal that more than half of generated AI suggestions are never looked at, and over three-quarters of reviewed suggestions are rejected [1, 16, 17]. The study demonstrates that the primary friction of AI coding assistants is not merely the seconds spent reading code, but the cumulative **micro-interruptions that disrupt developer flow and elevate code deletion rates**, providing clear design principles to optimize timing, frequency, and presentation of future GenAI programming assistants [13, 18, 31, 36, 37].

---

*Extraido via NotebookLM em October 2026 para MLR: Software Developer Metrics in Practice*
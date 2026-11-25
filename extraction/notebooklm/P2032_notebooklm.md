# P2032 — Speed at the Cost of Quality: How Cursor AI Increases Short-Term Velocity and Long-Term Complexity in Open-Source Projects

**Decisao: INCLUIDO | Qualidade: 5/5**

---

## Dados Bibliograficos

| Campo | Valor |
|-------|-------|
| **ID** | P2032 |
| **Autores** | Hao He, Courtney Miller, Shyam Agarwal, Christian Kästner, Bogdan Vasilescu [1] |
| **Ano** | 2026 [2] |
| **Venue** | 23rd International Conference on Mining Software Repositories (MSR ’26) [2] |
| **DOI** | 10.1145/3793302.3793349 [2] |
| **Tipo** | Conference paper [2] |
| **Metodo** | Repository mining, Quantitative (Difference-in-Differences with propensity score matching and dynamic panel GMM) [3-5] |
| **Amostra** | 806 Cursor-adopting GitHub open-source repositories and 1,380 matched control repositories (observation period Jan 2024 – Aug 2025) [4, 6, 7] |
| **Contexto** | Open-Source Software (OSS) GitHub projects (≥10 stars; top languages: TypeScript, Python, JavaScript, Go, Rust) [8] |
| **Modo de trabalho** | Not specified (distributed OSS contributors) [8, 9] |
| **Metodologia** | Not specified [8] |

---

## Objetivo

O objetivo principal do artigo é estimar empiricamente o efeito causal da adoção do assistente de IA baseado em agentes, Cursor, na velocidade de desenvolvimento e na qualidade do código em projetos de código aberto no GitHub, utilizando um projeto quase-experimental de diferença-em-diferenças (DiD) escalonado e modelos dinâmicos de painel GMM [3, 5, 6].

---

## Questoes de Pesquisa

- **RQ1**: How does the adoption of LLM agent assistants impact project-level development velocity and code quality? [6]

---

## Metricas e Instrumentos de Avaliacao

| Metrica | Categoria | Nivel | Como Coletada | Validada |
|---------|-----------|-------|---------------|----------|
| Commits | Productivity | Organization | Histórico de controle de versão (Git/GHArchive) [10] | Yes [10] |
| Lines Added | Productivity | Organization | Soma das linhas adicionadas em todos os commits via Git [10] | Yes [10] |
| Static Analysis Warnings | Quality | Organization | Análise estática via servidor local SonarQube Community [10, 11] | Yes [10, 11] |
| Duplicate Line Density | Quality | Organization | Percentual de linhas duplicadas via SonarQube Community [10, 11] | Yes [10, 11] |
| Code Complexity | Quality | Organization | Complexidade cognitiva da base de código via SonarQube [10, 11] | Yes [11, 12] |
| Lines of Code (LOC) | Activity | Organization | Tamanho total da base de código via SonarQube [13] | Yes [13] |
| Number of Contributors | Collaboration | Organization | Autores de commit distintos identificados no histórico Git [13] | Yes [13] |
| Issues and Pull Requests | Activity | Organization | Dados de eventos mensais extraídos via GitHub API e GHArchive [13, 14] | Yes [13, 14] |

---

## Frameworks e Metricas

### Frameworks Referenciados
- **SPACE**: REFERENCED (citado em [15] e [16] como referência para a medição multidimensional da produtividade de desenvolvedores além de métricas de saída simples).

### Frameworks Propostos
- **Theoretical Causal Model for LLM Agent Assistants**: Estrutura teórica causal proposta (Figura 1) que mapeia o impacto direto de assistentes de IA no aumento temporário da velocidade (+), elevação dos avisos de análise estática (+) e complexidade de código (+), além do efeito de realimentação negativa (-), onde o acúmulo de débito técnico reduz a velocidade de desenvolvimento futura [15, 17, 18].

---

## Fatores que Influenciam Produtividade

### Fatores Positivos
| Fator | Categoria |
|-------|-----------|
| Adoção de assistentes de código baseados em agentes (Cursor) com navegação autônoma no projeto | Technical |
| Capacidade de realizar edições em múltiplos arquivos e inferir arquitetura do projeto (.cursorrules) | Technical |
| Automação de tarefas repetitivas de código (refatoração, geração de testes, prototipagem) | Technical |
| Maior autonomia e suporte ao desenvolvimento iterativo no ambiente IDE | Process |

### Fatores Negativos
| Fator | Categoria |
|-------|-----------|
| Acúmulo de débito técnico (+30,3% em avisos de análise estática) | Technical |
| Aumento na complexidade cognitiva intrínseca do código (+41,6% em Code Complexity) | Technical |
| Ciclo de entusiasmo-frustração-abandono do desenvolvedor ao lidar com limitações do agente | Human |
| Sobrecarga cognitiva para revisar e depurar grandes alterações geradas por IA em múltiplos arquivos | Human / Process |
| Gargalo nos processos de garantia de qualidade (QA) incapazes de acompanhar a velocidade da IA | Process / Organizational |

---

## Papel da IA e Automacao

| Campo | Valor |
|-------|-------|
| Usa IA/ML? | Yes — avalia o Cursor, um IDE alimentado por LLMs com capacidades de agente autônomo (modelos OpenAI, Anthropic, Google) integrados ao contexto do projeto via arquivos .cursorrules [3, 19]. |
| Automacao de coleta? | Yes — coleta automatizada de histórico de commits e eventos via GHArchive e GitHub API, análise estática automatizada via SonarQube e modelagem econométrica automatizada [10, 14, 20, 21]. |
| Impacto de IA na produtividade? | A adoção do Cursor gera um impulso inicial expressivo na velocidade de desenvolvimento (+281,3% linhas adicionadas e +55,4% commits no 1º mês) [22]. Porém, esse ganho é temporário e desaparece após 2 meses, enquanto cria um acúmulo sustentado de débito técnico (+30,3% avisos estáticos, +41,6% complexidade) que prejudica a velocidade futura [18, 22-24]. |

---

## Resultados Principais

- **Aumento inicial mas temporário na velocidade de desenvolvimento**: A adoção do Cursor resulta em um aumento médio modesto de 28,6% em linhas adicionadas no geral [25]. A análise horizonte-temporal revela que os ganhos ocorrem apenas nos dois primeiros meses: no 1º mês, os commits aumentam 55,4% e as linhas adicionadas 281,3%; no 2º mês, os commits sobem 14,5% e as linhas adicionadas 48,4%; após o 2º mês, os ganhos de velocidade dissipam-se totalmente [22].
- **Acúmulo sustentado e significativo de débito técnico**: Diferente da velocidade, os impactos na qualidade são persistentes: os avisos de análise estática aumentam em média 30,3% (\\(\pm 6,66\%\\)) e a complexidade do código sobe 41,6% (\\(\pm 7,62\%\\)) pós-adoção, mantendo-se elevados ao longo de todo o período observado (0 a +6 meses) [23, 25].
- **Efeito insignificante em duplicação de código**: Não foi observado impacto estatisticamente significante na densidade de linhas duplicadas na amostra geral (+7,03%, \\(p \ge 0.05\\)) [23, 25].
- **Relação causal entre débito técnico e desaceleração futura**: Modelos dinâmicos em painel GMM mostram que um aumento de 100% na complexidade do código e nos avisos de análise estática provoca uma redução posterior de 64,5% e 50,3% na velocidade de desenvolvimento (linhas adicionadas), respectivamente [24]. Um aumento de \\(\sim 3\times\\) na complexidade ou \\(\sim 5\times\\) nos avisos cancela completamente os ganhos de velocidade trazidos pelo Cursor [24].
- **Complexidade intrínseca do código gerado por IA**: Mesmo controlando estritamente pelas dinâmicas de crescimento e tamanho do repositório, o Cursor gera um aumento baseline de 9% na complexidade do código, indicando que o código gerado por IA é inerentemente mais complexo do que o escrito por humanos [26].
- **Robustez confirmada em subconjuntos**: Análises de robustez mostram que os efeitos negativos na qualidade são ainda mais pronunciados em projetos com uso intensivo e sustentado do Cursor, descartando que os resultados decorram de abandono imediato ou interferência de outras ferramentas de IA [27, 28].

---

## Desafios do Uso das Metricas

- **Ilusão de produtividade por métricas isoladas de velocidade**: Avaliar o impacto da IA apenas por volume de saída no curto prazo (commits, linhas de código) mascara o acúmulo progressivo de débito técnico [18, 29].
- **Inadequação de métricas tradicionais de complexidade para código de IA**: Métricas como a complexidade cognitiva penalizam estruturas sintaticamente complexas geradas mecanicamente por IA, gerando uma "taxa de compreensão" (*comprehension tax*) para revisores humanos [30, 31].
- **Incapacidade dos processos de QA de escalar com a IA**: Os métodos tradicionais de garantia de qualidade e revisão humana tornam-se gargalos e não acompanham o volume e a escala multi-arquivo do código gerado por agentes [18, 29, 32].
- **Métricas de adoção baseadas em sinais visíveis (ITT)**: Utilizar a presença de arquivos de configuração (`.cursorrules`) captura apenas a intenção de tratar (*intent-to-treat*), sem medir diretamente a intensidade individual de uso ou abandonos informais sem remoção do arquivo [33, 34].

---

## Avaliacao de Qualidade Metodologica

| Criterio | Pontuacao (0-2) |
|----------|----------------|
| Objetivo claramente definido | 2 |
| Metodologia adequada ao objetivo | 2 |
| Amostra/contexto descrito adequadamente | 2 |
| Ameacas a validade discutidas | 2 |
| Resultados com evidencia suficiente | 2 |
| Contribuicao clara para pratica ou teoria | 2 |
| **TOTAL** | **12/12** |

---

## Limitacoes

- **Adoção observável restrita a arquivos comitados**: O grupo de tratamento inclui apenas repositórios com arquivos `.cursorrules` no histórico git, o que pode introduzir viés de seleção ao focar em projetos com práticas formais [33].
- **Incerteza sobre a intensidade e continuidade do uso**: A presença do arquivo de configuração indica adoção no nível do repositório, mas não garante uso contínuo por todos os contribuidores ao longo de todo o período pós-adoção (mensurado como *intent-to-treat*) [34].
- **Heterogeneidade de modelos e versões de LLM**: Os dados não identificam as versões exatas do cliente Cursor nem os modelos LLM de fundo (ex: GPT-4o, Claude 3.5 Sonnet) utilizados em cada tarefa [35].
- **Contaminação potencial por outras ferramentas de IA**: Repositórios de ambos os grupos (tratamento e controle) podem ter utilizado outras ferramentas de IA sem rastros explícitos em arquivos (ex: GitHub Copilot inicial ou interface web do ChatGPT) [36].
- **Generalização limitada a código aberto**: Os achados podem não se aplicar diretamente a ambientes corporativos/proprietários (com processos mandatórios de QA e revisão) e restringem-se às linguagens dominantes no dataset (TypeScript, Python, JavaScript, Go, Rust) [37, 38].

---

## Contribuicao Principal

Este artigo fornece a primeira investigação empírica e longitudinal em larga escala sobre o impacto de assistentes de IA baseados em agentes (especificamente o Cursor) em projetos reais de desenvolvimento de software [3, 39]. Ao combinar um projeto quase-experimental de diferença-em-diferenças escalonado com modelagem dinamicamente adjusted por painel GMM, a pesquisa demonstra que as ferramentas de IA geram um dilema entre ganhos de velocidade no curto prazo e acúmulo de complexidade no longo prazo, comprovando que o débito técnico acumulado reduz a velocidade futura e ressaltando a necessidade imperativa de integrar a garantia de qualidade como elemento central nas ferramentas e fluxos de trabalho de IA [3, 18, 39, 40].

---

*Extraido via NotebookLM em October 2026 para MLR: Software Developer Metrics in Practice*
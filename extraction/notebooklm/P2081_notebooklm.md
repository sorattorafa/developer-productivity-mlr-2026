# P2081 — The Effect Of Visual Studio Code Usability Based On Nielsen's Attributes On The Programming Productivity Of Informatics Students

**Decisao: INCLUIDO | Qualidade: 4.5/5**

---

## Dados Bibliograficos

| Campo | Valor |
|-------|-------|
| **ID** | P2081 [1] |
| **Autores** | Nadya Nada Pradista, Suprih Widodo [1] |
| **Ano** | 2026 [1] |
| **Venue** | JKTP: Jurnal Kajian Teknologi Pendidikan (Vol. 9, No. 2, pp. 244-253) [1, 2] |
| **DOI** | 10.17977/um038v9i22026p244-253 [1, 2] |
| **Tipo** | Journal article [1] |
| **Metodo** | Quantitative / Survey method (Ex post facto design, digital closed-ended questionnaire, multiple linear regression analysis) [3-6] |
| **Amostra** | 200 active Informatics students (Purposive sampling; 7th semester or above, preparing or completed final project using VS Code; 118 male [59%], 82 female [41%]; 7th sem: 72 [36%], 8th sem: 80 [40%], 9th sem: 34 [17%], 10th sem: 14 [7%]) [7-9] |
| **Contexto** | Academic (Informatics study programs in higher education institutions) [5] |
| **Modo de trabalho** | Not specified (Academic environment / final project development) [5] |
| **Metodologia** | Not specified [5] |

---

## Objetivo

O objetivo principal deste estudo e analisar os efeitos parciais e simultaneos das dimensoes de usabilidade do Visual Studio Code — baseadas nos Atributos de Usabilidade de Nielsen (learnability, efficiency, memorability, errors e satisfaction) — sobre a produtividade de programacao de estudantes de Informatica durante a elaboracao do trabalho de conclusao de curso (tcc/final project), identificando qual dimensao e a mais dominante na melhoria dessa produtividade [3, 4, 10].

---

## Questoes de Pesquisa

- **RQ1**: Como cada uma das dimensoes de usabilidade de Nielsen (Learnability, Efficiency, Memorability, Errors e Satisfaction) afeta parcialmente a produtividade de programacao dos estudantes de Informatica? [10-12]
- **RQ2**: Como as dimensoes de usabilidade do Visual Studio Code afetam simultaneamente a produtividade de programacao dos estudantes de Informatica? [10, 13]
- **RQ3**: Qual dimensao de usabilidade do modelo de Nielsen exerce o papel mais dominante na produtividade de programacao dos estudantes? [10, 11]

---

## Metricas e Instrumentos de Avaliacao

| Metrica | Categoria | Nivel | Como Coletada | Validada |
|---------|-----------|-------|---------------|----------|
| **Learnability (X1)** | DevEx / Usability | Individual | Closed-ended questionnaire (4 items, 5-point Likert scale) [6, 14] | Yes (Corrected Item-Total Corr. 0.491–0.740, Cronbach's \\(\alpha = 0.850\\)) [15, 16] |
| **Efficiency (X2)** | Productivity / DevEx | Individual | Closed-ended questionnaire (4 items, 5-point Likert scale) [6, 14] | Yes (Cronbach's \\(\alpha = 0.858\\)) [16] |
| **Memorability (X3)** | DevEx / Usability | Individual | Closed-ended questionnaire (4 items, 5-point Likert scale) [6, 14] | Yes (Cronbach's \\(\alpha = 0.849\\)) [16] |
| **Errors (X4)** | Quality / DevEx | Individual | Closed-ended questionnaire (4 items, 5-point Likert scale) [6, 14] | Yes (Cronbach's \\(\alpha = 0.863\\)) [16] |
| **Satisfaction (X5)** | Satisfaction / DevEx | Individual | Closed-ended questionnaire (4 items, 5-point Likert scale) [6, 14] | Yes (Cronbach's \\(\alpha = 0.850\\)) [16] |
| **Programming Productivity (Y)** | Productivity | Individual | Closed-ended questionnaire (6 items, 5-point Likert scale) [6, 14] | Yes (Cronbach's \\(\alpha = 0.799\\)) [15, 16] |

---

## Frameworks e Metricas

### Frameworks Referenciados
- **Nielsen's Attributes of Usability (NAU)**: APPLIED — Utilizado como a estrutura teorica central e instrumento de medicao das cinco dimensoes de usabilidade (learnability, efficiency, memorability, errors, satisfaction) [3, 8, 10, 17].
- **ISO 9241-11**: REFERENCED — Citado na discussao para fundamentar a definicao de usabilidade em termos de eficacia, eficiencia e satisfacao em um contexto de uso especifico [18].
- **SPACE Framework (Forsgren et al., 2021)**: REFERENCED — Discutido teoricamente para associar as dimensoes de usabilidade (Efficiency e Satisfaction) com Efficiency & Flow e Satisfaction & Well-being do modelo SPACE [19-21].

### Frameworks Propostos
Nenhum novo framework e proposto pelo artigo (o estudo aplica o modelo NAU e faz uma convergencia teorica com o SPACE framework) [10, 20, 22].

---

## Fatores que Influenciam Produtividade

### Fatores Positivos
| Fator | Categoria |
|-------|-----------|
| Usabilidade geral do editor de codigo (VS Code) [3, 23, 24] | Technical |
| Eficiencia dos recursos da ferramenta (IntelliSense/autocomplete, atalhos de teclado, terminal integrado, extensoes e navegacao) [11, 25-27] | Technical |
| Facilidade de aprendizado (interface intuitiva e adaptacao rapida ao ambiente) [8, 26, 28] | Human / Technical |
| Memorabilidade de recursos (consistencia de interface que facilita retomar o trabalho apos interrupcoes) [14, 29] | Human / Technical |
| Suporte ao tratamento e resolucao de erros (notificacoes de erro, ferramentas de debugging e funcionalidade undo) [14, 30] | Technical |
| Satisfacao e conforto do usuario (customizacao do ambiente e interface amigavel) [14, 31, 32] | Human |

### Fatores Negativos
| Fator | Categoria |
|-------|-----------|
| Complexidade do codigo e erros tecnicos em projetos finais [33-35] | Technical |
| Processos de debugging demorados e repetitivos [35] | Technical / Process |
| Subutilizacao de ferramentas avancadas de debugging ou falta de experiencia na resolucao de erros [31, 36] | Human / Process |
| Dificuldade de adaptacao a bibliotecas e frameworks diversos [35] | Technical / Human |
| Pressao de prazos e demandas academicas simultaneas [36] | Organizational / Process |
| Ferramentas de desenvolvimento com usabilidade ruim ou interfaces complexas [23] | Technical |

---

## Papel da IA e Automacao

| Campo | Valor |
|-------|-------|
| Usa IA/ML? | No — Menciona o recurso de auto-completar inteligente (IntelliSense) do VS Code [26], mas assistentes de IA generativa/LLMs nao sao analisados como variaveis independentes [6, 14]. |
| Automacao de coleta? | Partial — A coleta foi feita via formulario digital estruturado [6], mas os dados de produtividade e usabilidade foram autorreportados em vez de capturados por amostragem automatica de telemetria da IDE [5, 6, 37]. |
| Impacto de IA na produtividade? | Nao testado empiricamente no modelo (a literatura e citada [Hliš et al., 2023] indicando que recursos de autocompletar aumentam a velocidade de codificacao e reduzem erros) [38]. |

---

## Resultados Principais

- Todas as cinco dimensoes de usabilidade do VS Code afetam positiva e significativamente a produtividade de programacao dos estudantes (\\(R^2 = 0{,}605\\), \\(R^2 \text{ Ajustado} = 0{,}595\\), \\(F = 59{,}357\\), \\(p = 0{,}000\\)), explicando 60,5% da variacao da produtividade [13, 24, 39].
- Equacao de regressao linear multipla: \\(Y = 0{,}139 + 0{,}205X_1 + 0{,}301X_2 + 0{,}176X_3 + 0{,}149X_4 + 0{,}176X_5 + e\\) [24, 39].
- **Efficiency (\\(X_2\\))** e a dimensao com impacto mais dominante (\\(B = 0{,}301\\), \\(t = 9{,}377\\), \\(p = 0{,}000\\); Média = 3,621), impulsionada por autocompletar, atalhos, extensoes e navegacao [11, 39].
- **Learnability (\\(X_1\\))** e o segundo fator mais influente (\\(B = 0{,}205\\), \\(t = 5{,}990\\), \\(p = 0{,}000\\); Média = 3,896) [12, 39].
- **Satisfaction (\\(X_5\\))** (\\(B = 0{,}176\\), \\(t = 5{,}093\\), \\(p = 0{,}000\\); Média = 3,870) e **Memorability (\\(X_3\\))** (\\(B = 0{,}176\\), \\(t = 5{,}403\\), \\(p = 0{,}000\\); Média = 3,643) apresentam contribucionais idênticas [12, 39].
- **Errors (\\(X_4\\))** registrou o menor coeficiente de regressao (\\(B = 0{,}149\\), \\(t = 4{,}798\\), \\(p = 0{,}000\\)) e a menor media (Média = 3,523), refletindo que os estudantes ainda nao otimizam totalmente as ferramentas de debugging disponiveis [12, 31, 39, 40].
- A produtividade geral (\\(Y\\)) obteve media de 3,874 com desvio padrao de 0,510 [15, 41].
- O modelo atendeu a todos os testes de pressuposto classico: normalidade dos residuos (Kolmogorov-Smirnov \\(p = 0{,}858\\)), ausencia de multicolinearidade (VIF entre 1,018 e 1,077) e homocedasticidade (Glejser \\(p > 0{,}05\\)) [42].

---

## Desafios do Uso das Metricas

- Dependencia de questionarios de percepcao autorreportada em vez de coleta automatizada por metricas comportamentais objetivas (como tempo ativo na IDE, frequencia de commits, linhas de codigo ou taxas de erro reais) [6, 37].
- Lacuna entre a percepcao de usabilidade no tratamento de erros e a capacidade efetiva dos estudantes em utilizar recursos avancados de debugging [31, 40].
- Dificuldade em isolar a usabilidade da IDE de fatores exogenos nao capturados pelo modelo (como conhecimento previo da linguagem, complexidade do projeto e gestao de tempo) [13, 37].

---

## Avaliacao de Qualidade Metodologica

| Criterio | Pontuacao (0-2) |
|----------|----------------|
| Objetivo claramente definido | 2 |
| Metodologia adequada ao objetivo | 2 |
| Amostra/contexto descrito adequadamente | 2 |
| Ameacas a validade discutidas | 1 |
| Resultados com evidencia suficiente | 2 |
| Contribuicao clara para pratica ou teoria | 2 |
| **TOTAL** | **11/12** |

---

## Limitacoes

- Utilizacao exclusiva de metodo de survey baseado na percepcao dos usuarios, o que pode nao refletir fielmente o comportamento real de uso da ferramenta [37].
- Amostra limitada a 200 estudantes de Informatica de ensino superior em fase de projeto de conclusao de curso, restringindo a generalizacao dos resultados para desenvolvedores profissionais [7, 37].
- Foco delimitado aos aspectos de usabilidade do editor, sem medir o impacto de variaveis como proficiencia tecnica, experiencia previa em programacao, complexidade das tarefas e gestao de tempo [13, 37].
- Abordagem transversal e ex post facto, sem conducao de experimentos controlados ou observacao direta [4, 5, 37].

---

## Contribuicao Principal

O estudo comprova empiricamente que a usabilidade do Visual Studio Code — avaliada segundo os Atributos de Usabilidade de Nielsen (NAU) — explica 60,5% da variacao na produtividade de programacao de estudantes de Informatica na elaboracao de trabalhos finais, sendo a eficiencia da ferramenta o fator de maior impacto [11, 22, 24, 39]. A principal contribuicao da pesquisa consiste em conectar conceitualmente os atributos de usabilidade de HCI com o modelo moderno de produtividade de desenvolvimento SPACE, demonstrando que a usabilidade da IDE nao e apenas uma questao de conveniencia do usuario, mas um viabilizador tecnico fundamental da experiencia do desenvolvedor e do fluxo de trabalho academico [18, 20, 21].

---

*Extraido via NotebookLM em October 2026 para MLR: Software Developer Metrics in Practice*
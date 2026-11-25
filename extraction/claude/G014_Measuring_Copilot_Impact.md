# G014 — Measuring GitHub Copilot's Impact on Productivity

**Decisao: INCLUIDO | Qualidade: 5.5/6**

---

## Dados Bibliograficos

| Campo | Valor |
|-------|-------|
| **ID** | G014 |
| **Autores** | Albert Ziegler, Eirini Kalliamvakou, X. Alice Li, Andrew Rice, Devon Rifkin, Shawn Simister, Ganesh Sittampalam, Edward Aftandilian (GitHub, Inc.) |
| **Ano** | 2024 |
| **Venue** | Communications of the ACM (CACM), Vol. 67, No. 3, pp. 54–63 |
| **DOI** | 10.1145/3633453 |
| **URL** | https://cacm.acm.org/research/measuring-github-copilots-impact-on-productivity/ |
| **Tipo** | Journal Article (peer-reviewed, secao "research" do CACM) |
| **GL Tier** | 1st tier (Peer-reviewed publication in top venue) |
| **Metodo** | Estudo quantitativo: survey online pareado com telemetria de uso de IDE |
| **Amostra** | 2,631 respostas de survey (de 17,420 usuarios convidados); 2,047 respostas pareadas com dados de uso no periodo do estudo |
| **Contexto** | Industry — desenvolvedores usando GitHub Copilot (preview tecnico nao-pago) |

---

## Objetivo

Investigar se medidas objetivas de uso de GitHub Copilot (interacoes do desenvolvedor coletadas via telemetria de IDE) podem prever a produtividade percebida conforme relatada pelos proprios desenvolvedores via survey. Foco em perceived productivity, nao produtividade objetiva.

---

## Questoes de Pesquisa / Temas Investigados

- Qual metrica de uso de Copilot melhor prediz produtividade percebida?
- Como experiencia do desenvolvedor (anos + proficiencia na linguagem) afeta a relacao entre uso de Copilot e produtividade percebida?
- Como a acceptance rate varia ao longo do tempo (dia da semana, horario)?
- As medidas de persistencia (codigo aceito que permanece no source) complementam acceptance rate como preditor?

---

## Metricas e Instrumentos de Avaliacao

### Metricas de Uso (Telemetria de IDE)

| Metrica | Definicao | Categoria |
|---------|-----------|-----------|
| Acceptance rate | Fracao de completions mostradas que foram aceitas pelo usuario | Core — melhor preditor |
| Shown rate | Fracao de oportunidades de completion que resultaram em sugestao mostrada | Usage |
| Persistence rate | Fracao de completions aceitas que permaneceram inalteradas apos 30, 120, 300, 600 segundos | Persistence |
| Fuzzy persistence rate | Completions aceitas que permaneceram "mostly unchanged" (Levenshtein <33%) | Persistence |
| Efficiency | Fracao de oportunidades que resultaram em completion aceita e inalterada | Composite |
| Contribution speed | Numero de caracteres em completions aceitas por hora ativa | Volume |
| Acceptance frequency | Numero de completions aceitas por hora ativa | Frequency |
| Persistence frequency | Numero de completions inalteradas por hora ativa | Frequency |
| Total volume | Numero total de completions mostradas | Volume |
| Loquaciousness | Numero de completions mostradas por hora ativa | Rate |
| Eagerness | Numero de completions mostradas por oportunidade | Rate |

### Metricas de Produtividade Percebida (Survey)

- 11 afirmacoes Likert (1-5) mapeadas nas dimensoes SPACE: S, P, C, E (excluindo A — Activity — pois e melhor medida via telemetria)
- 1 afirmacao agregada: "I am more productive when using GitHub Copilot"
- Aggregate productivity score: media das 12 medidas individuais (excluindo perguntas puladas)
- Exemplos de afirmacoes: tasks_faster, stay_in_flow, focus_satisfying, less_frustrated, better_code, less_effort_repetitive, repetitive_faster, unfamiliar_progress, less_time_searching, learn_from, more_fulfilled

---

## Frameworks e Metricas

### Frameworks Mencionados
- SPACE Framework (Forsgren et al.) — usado para desenhar o survey, capturando 4 das 5 dimensoes: Satisfaction and well-being (S), Performance (P), Communication and collaboration (C), Efficiency and flow (E)
- QUANTS Framework (Google, Winters et al.) — mencionado como exemplo de framework operacional com 5 componentes

### DORA Applied: Nao
### SPACE Applied: Sim (usado como framework estruturante para design do survey de produtividade)
### AI Discussed: Sim (tema central — impacto de GitHub Copilot)

---

## Principais Resultados

### Acceptance Rate como Melhor Preditor
- Acceptance rate (accepted_per_shown) e o melhor preditor de produtividade percebida: rho = 0.24, P < 0.0001
- Correlacao e alta confianca mas deixa variancia inexplicada consideravel
- De todas as metricas de uso, acceptance rate e a que melhor performa em pelo menos uma pergunta de cada dimensao SPACE
- Metricas de persistencia tem correlacao menor que acceptance rate

### PLS Regression
- Primeiro componente (43.2% da variancia): todas as metricas contribuem positivamente
- Segundo componente (13.1% adicional): captura a dicotomia acceptance rate vs. change rate
- Conclusao: acceptance rate e o indicador mais imediato, mas combina-lo com outras metricas melhora a previsao

### Efeitos de Experiencia (Table 3)
- **Proficiency** negativamente correlacionada com: better_code (-0.061*) — desenvolvedores proficientes acham que Copilot melhora menos a qualidade do codigo
- **Proficiency** positivamente correlacionada com: stay_in_flow (0.069*), focus_satisfying (0.067*), less_effort_repetitive (0.072**), repetitive_faster (0.055***)
- **Years of experience** negativamente correlacionada com: better_code (-0.087*), less_frustrated (-0.103**), repetitive_faster (-0.054*)
- **Years of experience** positivamente correlacionada com: unfamiliar_progress (0.081*)

### Efeitos por Subgrupo (Table 4)
- Correlacao acceptance rate vs. aggregate productivity por experiencia: 3-5y (0.255***) e 6-10y (0.265***) sao os mais fortes; >=16y mais fraco (0.153*)
- Por linguagem: JavaScript (0.227***), Python (0.172***), TypeScript (0.165***)
- Desenvolvedores junior reportam maiores ganhos de produtividade E aceitam mais sugestoes

### Padroes Temporais (U.S. users only, PST)
- Tres regimes temporais distintos (p < 0.001 via bootstrap resampling):
  - Finais de semana: acceptance rate ~23-23.5%
  - Noites/madrugada (apos 16h e antes 7h): ~23%
  - Horario comercial (7h-16h weekdays): 21.2% (mais baixo)

### Dados Quantitativos Chave
- 17,420 usuarios convidados para survey
- 2,631 respostas (>80% responderam nos primeiros 2 dias)
- 2,047 respostas pareadas com dados de uso (periodo: 10 Feb - 6 Mar 2022)
- Acceptance rate medio: 27%
- DCPU (daily completions accepted per user) medio: >312
- ~170 oportunidades de completion por hora ativa de usuario
- ~24 completions mostradas por hora ativa
- ~5.6 completions aceitas por hora ativa

---

## Fatores que Influenciam Produtividade

### Fatores Positivos
| Fator | Categoria | Evidencia |
|-------|-----------|-----------|
| Acceptance rate alta | Tool Usage | Melhor preditor unico de produtividade percebida (rho=0.24, P<0.0001) |
| Sugestoes como templates uteis | Tool Design | "Useful template to tinker with" tao valioso quanto codigo perfeitamente correto |
| Menor experiencia/proficiencia | Individual | Desenvolvedores junior veem maiores ganhos em todas dimensoes |
| Persistencia de curto prazo | Tool Usage | Metricas de persistencia em periodos curtos (30s) correlacionam melhor que longos (600s) |

### Fatores Negativos
| Fator | Categoria | Evidencia |
|-------|-----------|-----------|
| Alta proficiencia na linguagem | Individual | Reduz percepcao de que Copilot melhora qualidade do codigo |
| Muitos anos de experiencia | Individual | Reduz percepcao de beneficio em frustration e repetitive tasks |
| Foco apenas em corretude | Measurement | Correctness alone nao conta a historia completa da produtividade |

---

## Papel da IA e Automacao

**Central neste artigo.** GitHub Copilot e o objeto de estudo. Principais conclusoes sobre AI:

1. AI pair-programming (Copilot) impacta positivamente produtividade percebida em todos os niveis de experiencia, com juniors vendo ganhos maiores
2. O valor central do Copilot nao esta em substituir digitacao, mas em ajudar usuarios a progredir em direcao a seus objetivos — sugestoes como "templates uteis para ajustar"
3. Foco estreito em corretude de sugestoes nao captura o quadro completo; interacoes com Copilot se assemelham a conversas em linguagem natural (prompt = contexto, completion = resposta)
4. Acceptance rate serve como metrica de monitoramento coarse-grained do desempenho do sistema de code synthesis

---

## Desafios do Uso das Metricas

- Acceptance rate tem variancia inexplicada consideravel como preditor (rho=0.24 e significativo mas modesto)
- Diferencias entre avaliacao offline (benchmarks sinteticos, Recall@5) e uso real no IDE sao substanciais (90% offline vs 70% online para IntelliCode)
- Muitos fatores humanos confundem a relacao: objetivo do desenvolvedor, linguagem, hora do dia, experiencia
- Metricas de persistencia sao conceitualmente atraentes mas correlacionam menos que acceptance rate
- Aggregate productivity score e proxy rough para conceito multidimensional complexo
- Self-report survey pode ter vieses (participantes voluntarios do preview tecnico)

---

## Avaliacao de Qualidade Metodologica

| Criterio | Score |
|----------|-------|
| Autoridade do autor/organizacao | 1/1 (GitHub Inc., autores principals do Copilot, publicado na secao research do CACM) |
| Descricao de metodologia | 1/1 (survey + telemetria, N detalhado, periodo de coleta, metricas formalmente definidas) |
| Data de publicacao | 1/1 (2024, atual) |
| Objetividade / vies comercial | 0.5/1 (Autores sao funcionarios do GitHub/Microsoft; estudam proprio produto) |
| Referencias a evidencias externas | 1/1 (29 referencias, incluindo Meyer et al., Forsgren et al., Storey et al., Wagner & Ruhe) |
| Contribuicao original | 1/1 (Primeiro estudo a parear survey SPACE com telemetria de uso de AI code completion em escala) |
| **Total** | **5.5/6** |

---

## Limitacoes

- Todos os autores sao funcionarios do GitHub/Microsoft — conflito de interesse inerente
- Participantes sao voluntarios de preview tecnico gratuito — possivel vies de auto-selecao (usuarios mais entusiastas)
- Self-report de produtividade, nao medicao objetiva de output
- Apenas Copilot (nao generalizavel para outras ferramentas de AI)
- Dados apenas do periodo do preview (pre-lancamento comercial) — comportamento pode diferir apos adocao generalizada
- Periodo de estudo curto (4 semanas, Jan-Mar 2022)
- Analise temporal restrita a usuarios dos EUA por razoes de fuso horario
- Acceptance rate como metrica e afetada por diferencas na interface (tipos de completion oferecidos)

---

## Contribuicao Principal

O estudo de Ziegler et al. (2024) e o primeiro a parear em escala (n=2,631) dados de survey baseados no SPACE framework com telemetria objetiva de uso de uma ferramenta de AI code completion. Suas tres contribuicoes principais sao: (1) a identificacao de que acceptance rate e o melhor preditor unico de produtividade percebida entre todas as metricas de uso coletadas, (2) a demonstracao de que o valor do Copilot nao reside na corretude das sugestoes per se, mas na utilidade como ponto de partida para iteracao — expandindo a nocao de como avaliar ferramentas de AI coding, e (3) a analise granular por experiencia mostrando que desenvolvedores junior veem maiores ganhos quantitativos enquanto desenvolvedores experientes beneficiam em dimensoes qualitativas (flow, satisfacao, reducao de esforco repetitivo). Para o MLR, este paper e diretamente relevante a RQ3 (impacto de AI em medicao de produtividade) e fornece evidencia empirica robusta de que metricas simples de uso (acceptance rate) podem servir como proxy para produtividade percebida, porem com limitacoes consideraveis de variancia explicada.

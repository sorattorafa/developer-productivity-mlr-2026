# G009 — 2025 State of AI-assisted Software Development

**Decisao: INCLUIDO | Qualidade: 5/6**

---

## Dados Bibliograficos

| Campo | Valor |
|-------|-------|
| **ID** | G009 |
| **Autores** | Nathen Harvey, Kevin M. Storer, Derek DeBellis, Daniella Villalba (DORA / Google Cloud) |
| **Ano** | 2025 |
| **Venue** | dora.dev |
| **URL** | https://dora.dev/research/ai-assisted-dev/ |
| **Tipo** | Industry Report |
| **GL Tier** | 1st tier (Official DORA research, Google Cloud) |
| **Metodo** | Mixed methods: survey quantitativo (quase 5.000 profissionais de tecnologia, survey conduzido entre 13 de junho e 21 de julho de 2025) + mais de 100 horas de dados qualitativos (78 entrevistas em profundidade) |
| **Amostra** | ~5.000 profissionais de tecnologia de todo o mundo |
| **Contexto** | Industria global, multiplos setores, multiplos paises |

---

## Objetivo

Investigar como AI-assisted software development impacta software delivery performance, produtividade individual, qualidade de codigo, bem-estar dos desenvolvedores e desempenho organizacional. Introduzir o DORA AI Capabilities Model com sete capacidades que amplificam os beneficios de AI.

---

## Questoes de Pesquisa / Temas Investigados

- Qual e o estado atual de adocao de IA entre profissionais de desenvolvimento de software?
- Qual e o impacto estimado de AI adoption em outcomes (throughput, instability, individual effectiveness, code quality, burnout, friction, product performance, team performance, organizational performance)?
- Quais capacidades organizacionais amplificam os beneficios de AI adoption? (DORA AI Capabilities Model)
- Quais sao os perfis de equipe (clusters) de software delivery performance?
- Como AI afeta construtos sociocognitivos dos desenvolvedores (authentic pride, meaningful work, need for cognition, existential connection, psychological ownership)?

---

## Metricas e Instrumentos de Avaliacao

| Metrica | Categoria | Nivel | Como Coletada | Validada |
|---------|-----------|-------|---------------|----------|
| Software delivery throughput (lead time, deployment frequency, failed deployment recovery time) | Delivery/Performance | Team | Survey self-report | Sim (DORA validated construct) |
| Software delivery instability (change fail rate, rework rate) | Delivery/Stability | Team | Survey self-report | Sim (DORA validated construct) |
| Individual effectiveness | Productivity | Individual | Survey self-report | Sim |
| Code quality | Quality | Individual/Team | Survey self-report | Sim |
| Team performance | Performance | Team | Survey self-report | Sim |
| Product performance | Performance | Product | Survey self-report | Sim |
| Organizational performance | Performance | Organization | Survey self-report | Sim |
| Burnout | Wellbeing | Individual | Survey self-report | Sim |
| Friction | DevEx | Individual | Survey self-report | Sim |
| Valuable work (tempo em trabalho valoroso) | Satisfaction | Individual | Survey self-report | Sim |
| Authentic pride | Sociocognitive | Individual | Survey self-report | Sim |
| Meaningful work | Sociocognitive | Individual | Survey self-report | Sim |
| Need for cognition | Sociocognitive | Individual | Survey self-report | Sim |
| Existential connection | Sociocognitive | Individual | Survey self-report | Sim |
| Psychological ownership | Sociocognitive | Individual | Survey self-report | Sim |

---

## Frameworks e Metricas

### Frameworks Mencionados
- DORA Software Delivery Performance Metrics (aplicado e estendido)
- DORA AI Capabilities Model (proposto neste relatorio — 7 capacidades)
- DORA Core Model (referenciado como base)

### DORA Applied: Sim
### SPACE Applied: Nao (mencionado indiretamente via construtos como satisfaction, wellbeing)
### AI Discussed: Sim (tema central do relatorio)

---

## Principais Resultados

### Adocao de AI
- 90% dos respondentes usam AI no trabalho (aumento de 14,1% vs. 2024)
- Mais de 80% acreditam que AI aumentou sua produtividade
- 30% reportam pouca ou nenhuma confianca no codigo gerado por AI
- Mediana de experiencia com ferramentas AI: 16 meses
- Mediana de tempo diario interagindo com AI: 2 horas (~25% do dia de trabalho)
- 60% dos usuarios usam AI "metade do tempo ou mais" ao enfrentar problemas
- 65% reportam depender de AI em nivel moderado ou maior
- 71% dos que escrevem codigo usam AI para escrever codigo novo
- 90% das organizacoes adotaram platform engineering

### Impacto de AI em outcomes (efeitos estimados com intervalos crediveis de 89%)

**Impactos positivos de AI adoption:**
- Individual effectiveness: aumento
- Software delivery throughput: aumento (reversao vs. 2024, quando era negativo)
- Code quality: aumento
- Product performance: aumento (reversao vs. 2024, quando era neutro)
- Team performance: aumento
- Organizational performance: aumento
- Valuable work: aumento (reversao vs. 2024, quando era negativo)

**Impactos negativos ou neutros:**
- Software delivery instability: **aumento** (efeito indesejavel que persiste desde 2024)
- Burnout: sem relacao mensuravel
- Friction: sem relacao mensuravel

### Sete perfis de equipe (cluster analysis)
1. Foundational challenges (10%) — gaps fundamentais em processos
2. Legacy bottleneck (11%) — preso em debito tecnico e sistemas legados
3. Constrained by process (17%) — processos ineficientes, alto burnout
4. High impact, low cadence (7%) — alta qualidade mas baixo throughput e alta instabilidade
5. Stable and methodical (15%) — entrega deliberada, baixo burnout, baixo throughput
6. Pragmatic performers (20%) — alta velocidade e estabilidade, bem-estar mediano
7. Harmonious high-achiever (20%) — excelencia em todas as dimensoes

Clusters 6 e 7 somam ~40% da amostra e demonstram que speed vs. stability e um mito.

### DORA AI Capabilities Model (7 capacidades que amplificam AI)
1. Clear and communicated AI stance (politica clara de AI)
2. Healthy data ecosystems
3. AI-accessible internal data
4. Strong version control practices
5. Working in small batches
6. User-centric focus
7. Quality internal platforms

Investir nestas capacidades amplifica o impacto positivo de AI em individual effectiveness, organizational performance, friction (reduz), e software delivery throughput.

### Impacto sociocognitivo de AI
- Authentic pride: AI adoption associada a maior orgulho autentico (mecanismo: mais tempo em trabalho valoroso)
- Meaningful work: sem impacto detectado
- Need for cognition: sem impacto detectado
- Existential connection: sem impacto detectado
- Psychological ownership: 78% de certeza que AI nao diminui senso de posse sobre codigo

---

## Fatores que Influenciam Produtividade

### Fatores Positivos
| Fator | Categoria | Evidencia |
|-------|-----------|-----------|
| Clear AI stance | Organizational | Amplifica individual effectiveness e organizational performance com AI |
| Quality internal platform | Technical | Correlacao direta com capacidade de desbloquear valor de AI; 90% de adocao de platform engineering |
| Value stream management (VSM) | Process | Multiplicador de forca para AI; garante que ganhos locais virem melhorias mensuraveis em team e product performance |
| Working in small batches | Process | Amplifica beneficios de AI |
| Healthy data ecosystems | Technical | Capacidade fundacional para AI |
| User-centric focus | Organizational | Amplifica beneficios de AI |
| Strong version control | Technical | Capacidade fundacional para AI |
| Fast feedback loops | Technical | Equipes com loops rapidos tiveram ganhos de 20-30% em commits, PRs e velocidade de entrega com AI |
| Loosely coupled architecture | Technical | Pre-requisito para beneficios de AI (caso Adidas: equipes acopladas viram zero beneficio) |
| Training and peer learning | Organizational | Booking.com: treinamento em prompts resultou em ate 30% aumento em merge requests |

### Fatores Negativos
| Fator | Categoria | Evidencia |
|-------|-----------|-----------|
| Tight coupling / dependencies | Technical | Neutraliza completamente ganhos de AI (caso Adidas com ERP) |
| Lack of evolved guardrails | Process | Aumento de volume de mudancas sem guardrails correspondentes aumenta instabilidade |
| Higher expectations from leadership | Organizational | Ganhos percebidos de AI convidam expectativas maiores, mantendo burnout estavel |
| Friction shifts (not disappears) | Process | Friction muda de trabalho manual para decidir/verificar/iterar prompts |
| Low trust in AI output | Individual | 30% reportam pouca confianca; necessidade de critical validation skills |

---

## Papel da IA e Automacao

**Central neste relatorio.** AI e o tema principal. Principais conclusoes sobre AI:

1. AI e um amplificador: magnifica forcas de organizacoes de alto desempenho e disfuncoes de organizacoes com problemas
2. Adocao de AI e problema sistemico, nao de ferramentas: o valor vem do sistema organizacional (plataforma, workflows, alinhamento de equipes)
3. Reversoes positivas vs. 2024: throughput, valuable work e product performance agora melhoram com AI (em 2024 eram negativos/neutros)
4. Instabilidade persiste: AI adoption continua associada a aumento de delivery instability — sistemas nao evoluiram para gerenciar desenvolvimento acelerado por AI
5. Burnout e friction nao sao resolvidos por AI: sao propriedades do sistema sociotecnico, nao do individuo
6. DORA AI Capabilities Model com 7 capacidades que amplificam beneficios de AI

---

## Desafios do Uso das Metricas

- Metricas de delivery tradicionais (DORA 4 keys) podem nao ser suficientes na era AI: "These technical capabilities and measurements no longer suffice. They must evolve for the AI era, be replaced, or be supplemented."
- Instabilidade como trade-off aceitavel e um argumento que nao se sustenta: instabilidade continua tendo efeitos negativos em product performance e burnout
- Metricas simples nao capturam a complexidade dos 7 perfis de equipe identificados
- Friction nao desaparece com AI, apenas muda de natureza (de trabalho manual para verificacao e iteracao de prompts)
- Metricas de bem-estar (burnout, friction) resistem a solucoes tecnologicas

---

## Avaliacao de Qualidade Metodologica

| Criterio | Score |
|----------|-------|
| Autoridade do autor/organizacao | 1/1 (DORA/Google Cloud, referencia consolidada) |
| Descricao de metodologia | 1/1 (survey + qualitativo, N detalhado, periodo de coleta declarado) |
| Data de publicacao | 1/1 (2025, atual) |
| Objetividade / vies comercial | 0.5/1 (Google Cloud e sponsor; dados open mas contexto comercial) |
| Referencias a evidencias externas | 1/1 (37+ notas de rodape, citacoes academicas) |
| Contribuicao original | 1/1 (DORA AI Capabilities Model, 7 perfis de equipe, reversoes vs. 2024) |
| **Total** | **5.5/6** |

---

## Limitacoes

- Dados de survey self-report (nao telemetria objetiva)
- Snapshot transversal, nao longitudinal (nao permite inferencia causal forte — os autores reconhecem explicitamente: "we're doing comparisons", nao causal claims)
- Google Cloud e platinum sponsor e afiliacao institucional dos autores (possivel vies)
- Metricas de sociocognitive constructs sao novas e nao foram replicadas
- Cluster analysis produz perfis descritivos, nao preditivos
- Amostra pode ter vies de auto-selecao (respondentes do survey DORA tendem a ser mais engajados com DevOps)

---

## Contribuicao Principal

O DORA 2025 Report e a investigacao mais abrangente do programa DORA sobre o impacto de AI em software development. Suas tres contribuicoes principais sao: (1) o DORA AI Capabilities Model com sete capacidades organizacionais que amplificam os beneficios de AI, (2) a identificacao de sete perfis de equipe via cluster analysis que vao alem de metricas simples de delivery, e (3) a documentacao de reversoes importantes vs. 2024 (throughput, valuable work, product performance agora positivos com AI) ao lado de efeitos persistentemente negativos (instability) e neutros (burnout, friction). A tese central — AI e um amplificador, nao um transformador independente — tem implicacoes diretas para como organizacoes devem investir: no sistema organizacional que envolve AI, nao apenas na ferramenta.

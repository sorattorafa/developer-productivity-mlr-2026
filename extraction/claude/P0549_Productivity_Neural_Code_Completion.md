# P0549 — Productivity Assessment of Neural Code Completion

**Decisao: INCLUIDO | Qualidade: 4/5**

---

## Dados Bibliograficos

| Campo | Valor |
|-------|-------|
| **ID** | P0549 |
| **Autores** | Albert Ziegler, Eirini Kalliamvakou, X. Alice Li, Andrew Rice, Devon Rifkin, Shawn Simister, Ganesh Sittampalam, Edward Aftandilian |
| **Ano** | 2022 |
| **Venue** | MAPS 2022 (6th ACM SIGPLAN International Symposium on Machine Programming) |
| **Tipo** | Estudo de Caso (Case Study) |
| **Metodo** | Correlação entre medições de uso e respostas de survey |
| **Amostra** | 2.631 respostas de survey de GitHub Copilot; 2.047 matched com telemetria |
| **Contexto** | GitHub Copilot - Síntese Neural de Código |

---

## Objetivo

Investigar se medições de uso de GitHub Copilot (frequência de aceitação de sugestões, persistência de completions) correlacionam com produtividade percebida pelos desenvolvedores. O objetivo é encontrar métricas mensuráveis que sirvam como proxy para produtividade real ao utilizar ferramentas de síntese neural de código, sem conseguir medir produtividade real diretamente.

---

## Questoes de Pesquisa

- **RQ1**: Qual é a relação entre aceitação de sugestões de código e produtividade percebida?
- **RQ2**: Qual métrica de uso melhor prediz produtividade percebida?
- **RQ3**: Qual é o impacto de variáveis (linguagem, horário do dia, experiência do desenvolvedor) em aceitação de sugestões?

---

## Dados da Pesquisa

### Amostra
- 17.420 usuários convidados de GitHub Copilot (preview técnico não remunerado)
- 2.631 respostas de survey validadas
- 2.047 respostas matched com telemetria de 4 semanas
- Período: 10 de fevereiro a 6 de março 2022

### Fonte de Dados
- Telemetria de GitHub Copilot (eventos de completions)
- Survey online com questões baseadas em SPACE framework
- IDE telemetry (IntelliJ, VS Code, Vim, Neovim)

### Metodos de Coleta
- Questionário online (Likert scale 1-5 para 11 statements + pergunta agregada)
- Telemetria automática de eventos de completion
- Dados de atividades IDE (horas ativas, tipo de linguagem)

### Periodo de Analise
- Período de survey: 10 fevereiro - 6 março 2022
- Período de telemetria analisado: 4 semanas anteriores

---

## Metricas e Instrumentos de Avaliacao

**Aceitação de Sugestões (Acceptance Rate)**: accepted_per_shown = número de completions aceitos / número de completions mostrados. GitHub Copilot reporta 27% de acceptance rate, média 31 DCPU (Daily Completions accepted Per User).

**Persistência**: unchanged_X_per_accepted = completions sem modificação após X segundos (30, 120, 300, 600). Também fuzzy persistence com Levenshtein distance < 33%.

**Eficiência**: accepted_X_per_opportunity = completions aceitos e não-modificados / opportunities

**Frequência de Contribuição**: accepted_char_per_hour = caracteres em completions aceitos por hora ativa

**SPACE Framework**: Framework com 5 dimensões:
- Satisfaction and well-being
- Performance
- Activity (não utilizado por ser inferior a medição direta)
- Communication and Collaboration
- Efficiency and Flow

Utilizadas 11 statements cobrindo 4 dimensões (S,P,C,E) + pergunta agregada sobre produtividade.

**Análise Estatística**: Correlação de Pearson, regressão PLS (Partial Least Squares), feature selection incremental

---

## Resultados Principais

**Melhor preditor de produtividade percebida**: Acceptance rate (accepted_per_shown) correlação ρ = 0.24, p < 0.0001

Acceptance rate foi melhor preditor que:
- Persistence rate (qualidade de completions)
- Efficiency (razão de completions utilizáveis)
- Contribution speed (caracteres por hora)

**Análise de variáveis**:
- **Linguagem**: Python e JavaScript têm acceptance rates maiores (mais adequados a síntese neural)
- **Circadian Rhythms**: Acceptance rate maior fora de horários de trabalho (23%) vs durante trabalho (21.2%)
- **Hora do dia importa menos que padrão usual do desenvolvedor**: Desenvolvedor usualmente ativo durante semana aceita menos no fim de semana, mesmo se trabalhando fora de seu padrão usual

**Variância explicada**: 43.2% pelo primeiro componente PLS, 13.1% adicional pelo segundo componente

**Métricas complementares**: Mostrado, shown frequency, e accepted_per_hour adicionam informação incremental significativa

---

## Desafios do Uso das Metricas

1. Correlação vs Causação: Pearson coefficient de 0.24 deixa considerável variância inexplicada (76%). Possível que acceptance rate seja indicador de qualidade subjacente em lugar de causa de produtividade.

2. Produtividade Percebida vs Real: Estudo não mede produtividade real (tempo para completar tarefas), apenas percepção. Possível que aumentar acceptance rate satisfaça desenvolvedor sem reduzir tempo de tarefa.

3. Amostra Enviesada: Participantes são early adopters de GitHub Copilot, predominantly profissionais (76% profissionais vs hobbistas). Generalização para todos desenvolvedores questionável.

4. Sistema Específico: GitHub Copilot com neural engine OpenAI Codex. Métricas podem não generalizar para outras ferramentas de completamento de código.

5. Factores Humanos: Muitos fatores subjetivos (cansaço, foco, tipo de tarefa) afetam acceptance rate independentemente da qualidade do sistema.

---

## Avaliacao de Qualidade

| Criterio | Pontuacao (0-2) |
|----------|----------------|
| Objetivo claramente definido | 2 |
| Metodologia adequada | 2 |
| Amostra/contexto descrito | 1 |
| Ameacas a validade discutidas | 2 |
| Resultados com evidencia | 2 |
| Contribuicao clara | 1 |
| **TOTAL** | **10/12** |

---

## Limitacoes

1. Amostra enviesada: Apenas early adopters voluntários, predominantly profissionais
2. Produtividade apenas percebida, não real (sem medição de tempo de tarefa ou output)
3. Sistema específico: GitHub Copilot, pode não generalizar para outras ferramentas
4. Correlação baixa: Pearson coefficient 0.24 deixa 76% variância inexplicada
5. Período curto: Apenas 4 semanas de telemetria, não captura evolução de longo prazo
6. Não considera contexto: Tipo de tarefa, experiência anterior, preferências pessoais

---

## Contribuicao Principal

O trabalho estabelece primeiro link claro entre medições de uso (acceptance rate) e produtividade percebida em sistemas de síntese neural de código. Descoberta-chave é que acceptance rate (simplicidade de interação) é melhor preditor que métricas mais sofisticadas de persistência, sugerindo que valor percebido do Copilot não é principalmente sobre geração de código perfeito, mas sobre assistência útil mesmo que aproximada. Contribui visão que ferramentas de código neural devem ser vistas menos como geradores de código perfeito e mais como conversas interativas com assistente, onde iteração e tinkering são features, não bugs. Fornece métricas práticas para monitoring de performance de sistemas de código synthesis.

---

*Extraido em Marco 2026 para MLR: Software Developer Metrics in Practice*

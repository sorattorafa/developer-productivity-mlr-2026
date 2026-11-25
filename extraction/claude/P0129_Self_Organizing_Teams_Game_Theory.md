# P0129 — Exploring the Efficiency of Self-Organizing Software Teams with Game Theory

**Decisao: INCLUIDO | Qualidade: 3/5**

---

## Dados Bibliograficos

| Campo | Valor |
|-------|-------|
| **ID** | P0129 |
| **Autores** | Clay Stevens, Jared Soundy, Hau Chan |
| **Ano** | 2021 |
| **Venue** | ICSE-NIER 2021 (New Ideas and Emerging Results) |
| **Tipo** | Conference paper (short/NIER) |
| **Metodo** | Game theory modeling + Monte Carlo simulation |
| **Amostra** | Simulated teams (1-9 devs, 1-9 tasks, 100 runs/config) |
| **Contexto** | Self-organizing agile teams (Scrum) — modelo teorico |

---

## Objetivo

Modelar o comportamento estrategico de desenvolvedores em equipes auto-organizadas usando teoria dos jogos e propor metricas de eficiencia para avaliar a auto-organizacao versus gestao centralizada.

---

## Questoes de Pesquisa

- **RQ1**: Como podemos modelar teoricamente o comportamento estrategico de desenvolvedores em equipes auto-organizadas?
- **RQ2**: Como podemos avaliar e medir a eficiencia do comportamento estrategico dos desenvolvedores em SOTs?
- **RQ3**: Equipes menores se auto-organizam mais eficientemente do que equipes maiores (validacao da "two-pizza rule")?

---

## Metricas Propostas

| Metrica | Tipo | Descricao |
|---------|------|-----------|
| **Price-of-stability (PoS)** | Eficiencia | Ratio entre melhor Nash Equilibrium e atribuicao otima (centralizada). Quanto mais proximo de 1.0, mais eficiente. |
| **Price-of-anarchy (PoA)** | Eficiencia | Ratio entre pior Nash Equilibrium e atribuicao otima. Mede worst-case da auto-organizacao. |
| **Social Welfare (SW)** | Moral/Satisfacao | Soma total dos payoffs dos desenvolvedores. Proxy para moral da equipe. |
| **Threshold Completed (TH)** | Produtividade | Total de trabalho completado no sprint (soma dos thresholds atingidos). Proxy para produtividade. |

### Formula do Modelo
- Payoff do desenvolvedor i: u_i(a) = Σ[f_{i,j}(a) - c_{i,j}(a)] se g_j(a) ≥ t_j
- Nash Equilibrium: nenhum dev pode melhorar payoff mudando estrategia unilateralmente
- PoS = max(α(a')) / max(α(a*)) para a' ∈ NE, a* ∈ otimo
- PoA = max(α(a')) / min(α(a*))

---

## Resultados da Simulacao

1. **Equipes menores**: PoS/PoA mais baixo → auto-organizacao mais eficiente para moral (SW)
2. **Equipes maiores**: PoS/PoA aumenta → mais variancia e ineficiencia
3. **Produtividade (TH)**: equipes menores podem nao completar nenhuma tarefa (NE sub-otimo)
4. **Equipes de 4+ devs com 4+ tarefas**: PoS/PoA limitado para TH
5. **Suporte condicional** para hipotese "two-pizza rule" (equipes pequenas mais eficientes)

---

## Desafios do Uso das Metricas

1. **Modelo teorico apenas** — sem validacao com equipes reais
2. **Parametros simplificados** — distribuicoes uniformes, sem modelar habilidades reais
3. **Nash Equilibrium assume racionalidade** — desenvolvedores podem nao ser estrategicos
4. **PoS/PoA nao capturam fatores humanos** (motivacao, comunicacao, fadiga)
5. **Dificuldade de estimar payoffs e custos** em contextos reais

---

## Avaliacao de Qualidade

| Criterio | Pontuacao (0-2) |
|----------|----------------|
| Objetivo claramente definido | 2 |
| Metodologia adequada | 2 |
| Amostra/contexto descrito | 1 (simulacao) |
| Ameacas a validade discutidas | 1 |
| Resultados com evidencia | 1 (simulacao) |
| Contribuicao clara | 2 |
| **TOTAL** | **9/12 (Alta)** |

---

## Limitacoes

1. **Simulacao apenas** — sem dados empiricos de equipes reais
2. **Parametros arbitrarios** — distribuicoes uniformes podem nao refletir realidade
3. **Nao considera comunicacao** entre membros da equipe
4. **Modelo estatico** — nao captura dinamica temporal de sprints reais
5. **NIER paper (4 paginas)** — contribuicao preliminar

---

## Dados da Pesquisa

### Descricao do Dataset
- **Tipo**: Simulacao computacional (nao dados empiricos de equipes reais)
- **Contexto**: Modelo teorico de equipes Scrum self-organizing
- **Parametros simulados**:
  - Numero de desenvolvedores: 1-9
  - Numero de tarefas: 1-9
  - Numero de rodadas de simulacao: 100 por configuracao
- **Distribuicoes**: Uniformes para custos, beneficios, habilidades
- **Metodo de solucao**: Busca de Nash Equilibrium via iteracao computacional

### Variaveis de Entrada (Parametros do Modelo)

| Variavel | Descricao | Range/Valores | Tipo |
|---|---|---|---|
| n | Numero de desenvolvedores | 1-9 | Inteiro |
| m | Numero de tarefas no sprint | 1-9 | Inteiro |
| t_j | Limiar de conclusao da tarefa j | Variavel por tarefa | Real |
| f_{i,j} | Beneficio do dev i completar tarefa j | Uniforme [0, 1] | Real |
| c_{i,j} | Custo para dev i executar tarefa j | Uniforme [0, 1] | Real |
| u_i | Funcao de utilidade do desenvolvedor i | Somatoria de payoffs | Real |

### Exemplo de Caso (Secao III.C)
- **Equipe**: 5 desenvolvedores em sprint
- **Tarefas**: 5 tarefas com thresholds variados
- **Distribuicao**: custos/beneficios aleatorios
- **Rodadas**: multiplas simulacoes para capturar variancia

### Instrumento de Medicao
- **Simulacao computacional**: modelo em pseudocodigo (Equacoes 1-7)
- **Calculos**: Nash Equilibrium computation, PoS/PoA extraction
- **Saidas**: Price-of-stability, Price-of-anarchy, Social Welfare, Threshold Completed

---

## Metricas e Instrumentos de Avaliacao

### Metricas Propostas (Tabela em markdown)

#### 1. Price-of-Stability (PoS)
```
PoS = max(α(a')) / max(α(a*))
Onde:
  a' = melhor Nash Equilibrium (mais realista)
  a* = atrribuicao otima centralizada (ideal)
  α(a) = welfare or productivity score
```
**Interpretacao**:
- PoS proximo de 1.0 → equipes auto-organizadas sao eficientes
- PoS >> 1.0 → significativa perda de eficiencia em relacao ao otimo
- **Aplicabilidade**: mede custo de autonomia (quanto pior que otimo?)

#### 2. Price-of-Anarchy (PoA)
```
PoA = max(α(a')) / min(α(a*))
```
**Interpretacao**:
- Mede o pior caso de eficiencia em Nash Equilibrium
- PoA alto → risco de outcomes muito ruins em auto-organizacao
- PoA baixo → mesmo nos piores casos, eficiencia e aceitavel

#### 3. Social Welfare (SW)
```
SW = Σ u_i(a) para todos os desenvolvedores i em estrategia a
```
**Interpretacao**:
- Proxy para **moral da equipe** e **satisfacao**
- SW alto → desenvolvedores motivados mesmo em auto-organizacao
- Metrica psicossocial importante

#### 4. Threshold Completed (TH)
```
TH(a) = Σ g_j(a) onde g_j(a) = 1 se soma payoffs ≥ t_j, 0 caso contrario
```
**Interpretacao**:
- Proxy para **produtividade** (quantidade de trabalho completado)
- Importante: nem sempre TH alto em Nash Equilibrium
- Trade-off: PoS bom (moral alta) vs TH baixo (pouco trabalho)

### Payoff do Desenvolvedor (Formula Base - Equacao 1)
```
u_i(a) = Σ[f_{i,j}(a) - c_{i,j}(a)]  se g_j(a) ≥ t_j
       = -c_{i,j}(a)                   caso contrario
```

**Componentes**:
- **Beneficio** f_{i,j}: satisfacao de completar trabalho valioso
- **Custo** c_{i,j}: esforco/tempo investido
- **Threshold** t_j: requisito minimo para dar credito

### Estrategia Racional (Nash Equilibrium)
Um perfil de estrategia a' e Nash Equilibrium se:
- Nenhum desenvolvedor consegue melhorar seu payoff trocando de estrategia unilateralmente
- Todos os devs escolhem tarefas que maximizam u_i, dada escolha dos outros

### Simulacao e Validacao

#### Processo
1. Gerar configuracao de equipe (n devs, m tarefas)
2. Inicializar custos/beneficios com distribuicao uniforme
3. Computar Nash Equilibrium iterativamente
4. Calcular PoS, PoA para cada configuracao
5. Repetir 100x para variancia

#### Parametros de Confiabilidade
- Distribuicoes uniformes (simplificada, pode nao refletir realidade)
- Pressupostos de racionalidade perfeita (devs nem sempre racionais)
- Modelo estatico (nao captura dinamica temporal de sprints reais)

### Resultados de Simulacao (Figura 1-2)

#### Figura 1: Box plots de PoS e PoA
- **PoS (Figura 1a)**: mediana cresce com n (equipes menores mais eficientes)
- **PoA (Figura 1b)**: maior variancia em pequenas equipes

#### Figura 2: Heatmaps de PoS e PoA
- Demonstra como PoS/PoA variam com n (numero de devs) e m (numero de tarefas)
- Equipes com 4+ devs mostram eficiencia mais consistente

#### Principais Achados
1. **Equipes menores (1-3 devs)**: PoS/PoA baixo para moral (SW), mas TH pode ser 0 (nenhum trabalho completo)
2. **Equipes medianas (4-5 devs)**: PoS/PoA balanceado, TH melhor
3. **Equipes maiores (6-9 devs)**: PoS/PoA aumenta (menos eficientes relativamente)

---

## Contribuicao Principal

Primeira aplicacao de metricas de teoria dos jogos (Price-of-stability, Price-of-anarchy) ao contexto de equipes de software auto-organizadas, fornecendo framework teorico para medir eficiencia de auto-organizacao versus gestao centralizada.

---

*Extraido em Marco 2026 para MLR: Software Developer Metrics in Practice*

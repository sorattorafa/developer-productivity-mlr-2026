# P0133 — Framework to analyze the relationship between agile software engineers' emotions and their productivity

**Decisao: INCLUIDO | Qualidade: 2/5**

---

## Dados Bibliograficos

| Campo | Valor |
|-------|-------|
| **ID** | P0133 |
| **Autores** | Martin Gildardo Salido Ortega, Gilberto Borrego Soto, Ramon Rene Palacios Cinco, Luis-Felipe Rodriguez |
| **Ano** | 2021 |
| **Venue** | CIMPS 2021 |
| **Tipo** | Conference paper |
| **Metodo** | Framework proposal (preliminary) |
| **Amostra** | Nenhuma (proposta conceitual) |
| **Contexto** | Agile software development |

---

## Objetivo

Propor framework preliminar para determinar relacao entre emocoes de engenheiros de software ageis e sua produtividade, usando sensores biometricos nao intrusivos.

---

## Questoes de Pesquisa

- **RQ1**: Como se manifesta a relacao entre as emocoes de um engenheiro de software que trabalha em ambientes ageis e sua produtividade?
- **RQ2**: Como os diferentes modelos de deteccao de emocoes podem ser usados para identificar as causas das mudancas de emocoes de um engenheiro de software?
- **RQ3**: Que tipos de intervencoes podem ser sugeridos aos engenheiros de software ageis para melhorar sua produtividade e bem-estar?

---

## Framework Proposto (4 Camadas)

1. **Capa de Usuarios**: desenvolvedores usando sensores (Empatica E4)
2. **Capa de Dados**: armazenamento de dados biometricos e de repositorio
3. **Capa de Processos**: identificacao de emocoes + calculo de produtividade
4. **Capa de Associacao**: relacao emocao-contexto-causas + intervencao

---

## Dados da Pesquisa

### Descricao do Dataset
- **Tipo de dados**: Proposta conceitual (nao dados empiricos coletados)
- **Dataset previsto**: dados biometricos nao-intrusivos de desenvolvedores em desenvolvimento agile
- **Instrumentacao proposta**:
  - **Empatica E4 wristband**: sensor biometrico para coleta de sinais fisiologicos
  - **Repositorio de codigo**: analise de commits, code reviews
  - **Ferramentas de tracking**: metricas de produtividade agile
- **Contexto esperado**: equipes agiles de desenvolvimento software
- **Amostra prevista**: multiplos engenheiros de software em ambiente agile

### Variaveis Que Seriam Medidas (Propostas)

#### Dados Biometricos (Empatica E4)
- Frequencia cardiaca (HR) — batidas por minuto
- Variabilidade de frequencia cardiaca (HRV)
- Condutancia da pele (EDA) — indicador de ativacao emocional
- Temperatura da pele (TEMP)
- Movimento (acelerometro)

#### Dados de Comportamento (Repositorio)
- Frequencia de commits
- Linhas de codigo alteradas
- Numero de code reviews
- Tempo ate merge

#### Dados de Contexto (Produtividade)
- Tarefas completadas
- Velocidade do sprint (story points)
- Bugs reportados
- Tempo em reunioes vs. coding

### Metodo de Coleta Proposto
1. **Coleta de dados biometricos**: monitoramento contınuo com Empatica E4 durante jornada de trabalho
2. **Coleta de dados de repositorio**: analise de Git logs e pull requests
3. **Coleta de metricas agile**: dados de ferramentas de rastreamento (Jira, Azure DevOps)
4. **Sincronizacao temporal**: alinhamento de timestamps entre fontes para associar emocoes com atividades
5. **Entrevistas complementares**: feedback dos participantes sobre experiencias emocionais

---

## Metricas e Instrumentos de Avaliacao

### Framework Proposto (4 Camadas) — Figura 1

#### Camada 1: Usuarios (Usuarios)
- Desenvolvedores usando sensores Empatica E4
- Dados biometricos coletados em tempo real
- Contexto: desarrollo de software agile

#### Camada 2: Dados (Data Layer)
- Armazenamento de sinais biometricos (HR, EDA, TEMP, movimento)
- Armazenamento de dados de repositorio (commits, branches, reviews)
- Sincronizacao de timestamps para correlacao

#### Camada 3: Processos (Processing Layer)
- **Identificacao de emocoes**: uso de tecnicas de deteccao de emocoes (Machine Learning)
  - Mapeamento de sinais biometricos para estados emocionais
  - Classificacao: positivas (felicidade, contentamento) vs. negativas (frustacao, ansiedade)
- **Calculo de produtividade**:
  - Metricas agile (velocidade, conclusao de tarefas)
  - Qualidade de codigo (bugs, technical debt)
  - Tempo de resposta (revisoes, merges)

#### Camada 4: Associacao (Association Layer)
- Relacao emocao-contexto-causas
- Intervencoes sugeridas para melhorar produtividade
- Análise das causas de mudancas emocionais

### Metricas Propostas (Conceitualmente)

#### Metricas de Emocoes (a serem validadas)
| Emocao | Indicadores Biometricos | Escala |
|---|---|---|
| **Felicidade/Contentamento** | HR estavel, EDA baixa | 0-5 |
| **Frustacao** | HR elevada, EDA elevada | 0-5 |
| **Ansiedade** | HR variavel, EDA alta | 0-5 |
| **Engajamento** | HR moderada, movimento aumentado | 0-5 |
| **Fadiga** | HR baixa/variavel, reducao de movimento | 0-5 |

#### Metricas de Produtividade
| Metrica | Calculo | Unidade |
|---|---|---|
| Velocidade | Story points completados / sprint | Points/sprint |
| Qualidade | Bugs encontrados / 1000 LOC | Bugs/KLOC |
| Eficiencia de Review | Tempo de pull request ate merge | Horas |
| Atividade de Codigo | Commits por hora de trabalho | Commits/hora |

### Tecnicas de Deteccao de Emocoes (Propostas)

#### Metodos Nao-Intrusivos
1. **Sensores biometricos**:
   - Empatica E4 wristband
   - Compativel com desenvolvimento normal (sinal nao intrusive)

2. **Analise de sinais**:
   - Pre-processamento de dados biometricos
   - Extracao de features (media, desvio padrao, variancia de HR/EDA)
   - Classificacao via ML (models de regressao, SVM, ou redes neurais)

3. **Validacao**:
   - Comparacao com auto-report (questionarios de emocao)
   - Correlacao com eventos conhecidos (deadlines, code reviews criticos)

### Modelo de Correlacao (Conceitual)

```
Produtividade = f(Emocoes, Contexto, Intervencoes)
```

Onde:
- **Emocoes** = estado psicologico do desenvolvedor (detectado via biometricos)
- **Contexto** = natureza da tarefa, deadlines, pressao da equipe
- **Intervencoes** = acoes para melhorar estado emocional (breaks, feedback, colaboracao)

### Limitacoes de Medicao Identificadas

1. **Invasividade aparente**: embora sensores sejam "nao-intrusivos", uso de wearables pode afetar comportamento
2. **Variacoes individuais**: respostas biometricas variam muito entre pessoas (baseline diferente)
3. **Confundidores**: stress, sono, exercicio, cafe podem afetar HR/EDA independente de emocoes de trabalho
4. **Privacidade**: coleta continua de dados biometricos levanta questoes eticas

---

## Limitacoes

1. **Apenas proposta conceitual** — sem validacao empirica
2. **Biometric sensors podem nao ser praticos** em ambientes reais
3. **Framework nao testado** com dados reais
4. **Paper em espanhol** — alcance limitado

---

*Extraido em Marco 2026 para MLR: Software Developer Metrics in Practice*

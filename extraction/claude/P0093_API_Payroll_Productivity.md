# P0093 — API Design and Development for Developer Payroll in Startups Based on Agile Productivity Factors

**Decisao: INCLUIDO | Qualidade: 2/5**

---

## Dados Bibliograficos

| Campo | Valor |
|-------|-------|
| **ID** | P0093 |
| **Autores** | Yang Agita Rindri, Rudy Hartanto, Ridi Ferdiana |
| **Ano** | 2019 |
| **Venue** | 2019 5th International Conference on Science and Technology (ICST) |
| **DOI** | 10.1109/ICST47872.2019.9166252 |
| **Tipo** | Conference paper |
| **Metodo** | Case Study |
| **Amostra** | 3 startups, 3 projetos ageis |
| **Contexto** | Startups (agile software development) |

---

## Objetivo

Projetar e implementar uma API REST para calculo de payroll de desenvolvedores em startups, baseada em fatores de produtividade agiles, ao inves de apenas horas trabalhadas.

---

## Questoes de Pesquisa

- **RQ1**: Como desenvolvedores em startups devem ser compensados de forma justa levando em conta factors de produtividade agiles?
- **RQ2**: Qual formula de payroll melhor captura produtividade (experiencia, papel, bugs, timeliness) versus apenas horas trabalhadas?
- **RQ3**: Como implementar uma API REST que calcule payroll dinamicamente baseado em metricas de produtividade coletadas de projetos agiles?

---

## Frameworks e Metricas

### Frameworks Referenciados
- Goal Question Metrics (GQM) para monitoramento de performance
- Nenhum framework padrao (DORA, SPACE, DevEx) referenciado

### Metricas Propostas

| Metrica | Categoria | Nivel | Como Coletada | Validada |
|---------|-----------|-------|---------------|----------|
| Years of experience | Competencia | Individual | Registro RH | Nao |
| Type of role (dev, PM, QA, TW) | Competencia | Individual | Expert judgment (indice) | Parcial |
| Bug count per project | Qualidade | Individual | Projeto/tracking | Nao |
| Days late (timeliness) | Produtividade | Individual | Projeto/tracking | Nao |
| Hourly rate | Compensacao | Individual | Organizacao | N/A |

### Formula Proposta

```
Index_a = 1 + (n x coeficiente)           -- peso por anos de experiencia
Rate/hour = Index_a x Index_b x Rate      -- rate ajustado por experiencia e papel
Rate/Dev = Rate/hour x total_hours         -- valor bruto
Bug_penalty = bugs x % x Rate/hour        -- penalidade por bugs
Late_penalty = days_late x % x Rate/hour  -- penalidade por atraso
Nett Payroll = Rate/Dev - Bug - Late       -- salario liquido
```

### Classificacao das Metricas
- **Objetivas**: Bug count, days late (coletadas de projetos)
- **Subjetivas**: Role index (expert judgment)
- **Output**: Bugs gerados, tarefas completadas
- **Processo**: Timeliness de entregas

---

## Fatores que Influenciam Produtividade

### Fatores Positivos
| Fator | Categoria |
|-------|-----------|
| Experiencia (anos) aumenta competencia | Humano/Psicologico |
| Compensacao justa reduz turnover | Organizacional |
| Entrega no prazo | Organizacional |
| Produto sem retrabalho (zero bugs) | Tecnico |

### Fatores Negativos
| Fator | Categoria |
|-------|-----------|
| LOC como metrica leva a gaming | Tecnico |
| Payroll baseado so em tempo ignora qualidade | Organizacional |
| Falta de recursos em startups para sistemas de payroll | Organizacional |
| Developer turnover por insatisfacao salarial | Humano/Psicologico |

---

## Papel da IA e Automacao

| Campo | Valor |
|-------|-------|
| Usa IA/ML? | Nao |
| Automacao de coleta? | Parcial — APIs automatizam calculo, mas dados sao manuais |

---

## Desafios do Uso das Metricas

1. **LOC como metrica leva a gaming**: desenvolvedores inflam linhas de codigo sem melhorar qualidade
2. **Metodos time-only ignoram qualidade**: multiplicar horas por rate nao diferencia produtividade
3. **Role indexing requer julgamento subjetivo**: valores de indice dependem de expert judgment organizacional
4. **Dificuldade de definir fatores justos**: diferentes papeis e contextos tornam padronizacao dificil
5. **Startups carecem de recursos**: para construir sistemas de payroll adequados

---

## Avaliacao de Qualidade Metodologica

| Criterio | Pontuacao (0-2) |
|----------|----------------|
| Objetivo claramente definido | 1 |
| Metodologia adequada | 1 |
| Amostra/contexto descrito | 1 |
| Ameacas a validade discutidas | 0 |
| Resultados com evidencia suficiente | 0 |
| Contribuicao clara | 1 |
| **TOTAL** | **4/12 (Baixa)** |

---

## Limitacoes

1. **Metodo nao totalmente validado**: autores reconhecem que o estudo nao foi finalizado
2. **Amostra muito pequena**: apenas 3 startups
3. **Sem validacao estatistica**: fatores de produtividade nao testados empiricamente
4. **Indices baseados em expert judgment**: subjetividade nao controlada
5. **Apenas projetos ageis**: generalizacao limitada a outros contextos

---

## Dados da Pesquisa

### Descricao do Dataset
- **Contexto**: 3 startups de software ageis em Indonesia
- **Tamanho da amostra**: 3 organizacoes, 3 projetos agiles, multiplos desenvolvedores por projeto
- **Metodo de coleta**: Semi-structured interviews com project managers e startup owners, analise de repositorios e sistemas de rastreamento de projetos
- **Periodo**: 2019 (estudo contemporaneo)
- **Duracao do projeto**: 20 dias (caso 1), iteracoes definidas em backlog
- **Fontes de dados**:
  - Entrevistas com project managers e donos de startups
  - Historico de desenvolvimento de projetos
  - Dados RH (anos de experiencia)
  - Sistemas de rastreamento de projetos (bug counts, datas de entrega)
  - Repositorios de codigo

### Variaveis Medidas
1. **Anos de experiencia do desenvolvedor** (input): coletados de registros RH
2. **Tipo de papel** (input): Developer, Project Manager, Technical Writer, Quality Assurance
3. **Contagem de bugs** (output): numero de bugs gerados por desenvolvedor por projeto
4. **Dias em atraso** (processo): atraso em relacao aos prazos de entrega
5. **Hourly rate** (compensacao): taxa por hora definida pela organizacao
6. **Index de papel** (indice): peso baseado no tipo de papel (1.0 para dev, 1.2 para PM, 0.4 para TW, 0.6 para QA)

### Instrumento de Coleta
- Formulario estruturado com campos: nome desenvolvedor, experiencia, papel, bugs, dias atrasados
- Postman (ferramenta REST) para testar APIs
- Excel para calculo e comparacao de payroll

### Taxa de Resposta e Completude
- Amostra pequena: 3 startups
- Dados coletados de forma direta (nao auto-report)
- Completude: todos os 3 projetos analisados com sucesso

---

## Metricas e Instrumentos de Avaliacao

### Metricas Propostas (com formulas)

#### 1. Index de Anos de Experiencia
```
Index_a = 1 + (n × coeficiente)
```
- Onde: n = numero de anos de experiencia, coeficiente = incremento percentual (ex: 8%)
- Exemplo: 5 anos com 8% coeficiente = 1 + (5 × 0.08) = 1.40

#### 2. Taxa por Hora Ajustada
```
Rate/hour = Index_a × Index_b × Rate_base
```
- Index_a: multiplicador por experiencia
- Index_b: multiplicador por papel (1.0 a 1.2)
- Rate_base: taxa minima da organizacao

#### 3. Payroll Bruto
```
Rate/Dev = Rate/hour × total_hours
```
- Total de horas trabalhadas no projeto

#### 4. Penalidade por Bugs
```
Bug_penalty = bugs_count × percentage × Rate/hour
```
- Exemplo: 5 bugs × 10% × $50/hora = $25 penalidade

#### 5. Penalidade por Atraso
```
Late_penalty = days_late × percentage × Rate/hour
```
- Exemplo: 3 dias atrasados × 5% × $50/hora = $7.50 penalidade

#### 6. Payroll Liquido (Final)
```
Nett_Payroll = Rate/Dev - Bug_penalty - Late_penalty
```

### Validacao e Testes
- **Teste implementado**: API REST testada usando Postman
- **Cenarios de teste**: 2 principais
  1. Calculo de taxa horaria por desenvolvedor
  2. Calculo de payroll total (com penalidades)
- **Resultado**: APIs funcionaram como esperado
- **Comparacao com metodos alternativos**: Comparacao entre 3 metodos diferentes (Project Portal PF X, Smart Village, Project C)

### Escalas de Medicao
| Dimensao | Escala | Tipo | Exemplo |
|----------|--------|------|---------|
| Anos de experiencia | Numerica contınua | Objetivo | 0-30+ anos |
| Papel | Categorica (4 niveis) | Subjetivo (expert judgment) | Dev (1.0), PM (1.2), TW (0.4), QA (0.6) |
| Bug count | Numerica discreta | Objetivo (repo tracking) | 0, 1, 5, 10+ |
| Dias atrasados | Numerica discreta | Objetivo (projeto tracking) | 0, 1, 3, 7+ dias |
| Taxa horaria | Numerica continua | Configuracao organizacional | $40-$150+ por hora |

### Confiabilidade e Limitacoes
- **Validade externa baixa**: apenas 3 startups
- **Subjetividade no role indexing**: expert judgment pode variar por organizacao
- **Sem validacao estatistica formal**: fatores nao testados empiricamente
- **Pressupostos simplificados**: distribuicoes uniformes de bugs e atrasos

---

## Contribuicao Principal

Identifica fatores de produtividade de desenvolvedores (experiencia, papel, bugs, pontualidade) para calculo de compensacao em startups ageis. Propoe formula e implementa como REST API. Relevante para a MLR por documentar metricas usadas na pratica para avaliar performance individual.

## Trabalhos Futuros Relevantes

- Validacao empirica do metodo com amostra maior
- Inclusao de mais fatores de produtividade (qualidade de codigo, colaboracao)
- Integracao com ferramentas de gerenciamento de projetos

---

*Extraido em Marco 2026 para MLR: Software Developer Metrics in Practice*

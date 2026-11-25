# P0479 — Migração Perfeita de Dados entre Esquemas de Banco de Dados com DAMI-Framework: Estudo Empírico sobre Experiência do Desenvolvedor

**Decisao: INCLUIDO | Qualidade: 4/5**

---

## Dados Bibliograficos

| Campo | Valor |
|-------|-------|
| **ID** | P0479 |
| **Autores** | Delfina Ramos-Vidal, Alejandro Cortiñas, Miguel R. Luaces, Oscar Pedreira, Ángeles Saavedra Places, Wesley K. G. Assunção |
| **Ano** | 2025 |
| **Venue** | EASE '25 - 29th International Conference on Evaluation and Assessment in Software Engineering |
| **Tipo** | Research Article - Empirical Study |
| **Metodo** | Questionário com desenvolvedores + análise de tarefa prática |
| **Amostra** | 21 desenvolvedores de software |
| **Contexto** | Migração de banco de dados legado para moderno com DAMI-DSL |

---

## Objetivo

Este estudo investiga a experiência do desenvolvedor (DX) ao usar DAMI-Framework (Domain-specific language for Data Migration), uma solução para migração de dados entre esquemas de banco de dados. Através de um design de avaliação envolvendo tarefa prática de migração e questionário estruturado, os autores avaliam usabilidade, perceção de usuário, e limitações da solução DAMI-DSL comparada com SQL tradicional em contexto de modernização de software legado.

---

## Questoes de Pesquisa

- **RQ**: Qual é a usabilidade, perceção de usuário e efetividade do DAMI-Framework para tarefas de migração de dados em comparação com abordagens tradicionais?

---

## Dados da Pesquisa

### Amostra
- 21 participantes totais (10 desenvolvedores de software, 11 estudantes)
- Experiência em migração de dados: <1 ano (11), 1-2 anos (9), 3-5 anos (1), >5 anos (0)
- Conhecimento de linguagens de script: Inexperiente (0), Novice (1), Competente (7), Proficiente (8), Expert (5)
- Conhecimento SQL: Inexperiente (0), Novice (4), Competente (10), Proficiente (7), Expert (0)
- Experiência com DSL: Sim (5), Não (16)

### Fonte de Dados
- Questionário com 12 questões fechadas em escala Likert de 5 pontos
- Tarefa prática de migração de dados: metade usa DAMI-DSL primeiro, metade usa SQL primeiro
- Medições: tempo de conclusão, taxa de erros, percepção de usabilidade
- Feedback qualitativo em questão aberta

### Metodos de Coleta
- Avaliação de tarefa prática estruturada com dois grupos
- Questionário de avaliação com métricas: Eficiência, Expressividade, Flexibilidade, Concisão, Expressividade
- Métricas de desempenho: Linhas de Código (LOC), taxa de erro, tempo de conclusão

### Periodo de Analise
- Período de avaliação não especificado (presumivelmente 2024-2025)

---

## Metricas e Instrumentos de Avaliacao

**Dimensões Avaliadas**:
1. **Propriedades DSL**: Eficiência, Expressividade, Flexibilidade, Concisão, Expressividade
2. **Experiência do Usuário**: Satisfação, Facilidade de Uso, Confiabilidade, Satisfação geral
3. **Métricas de Desempenho**: Linhas de Código, Taxa de Erro, Tempo de Conclusão

**Escala de Medição**:
- Escala Likert de 5 pontos: Discordo Fortemente, Discordo, Neutro, Concordo, Concordo Fortemente
- Análise de distribuição de respostas (porcentagens em cada nível)
- Comparação de tempo gasto entre DAMI-DSL e SQL

**Questionário de Avaliação**:
- Q1-Q5: Avaliação de propriedades DAMI-DSL (Eficiência, Expressividade, Flexibilidade, Concisão, Expressividade)
- Q6-Q12: Avaliação de experiência do usuário (Satisfação, Facilidade de Uso, Confiabilidade, Confiança, Satisfação geral)
- Q13: Feedback qualitativo aberto

---

## Resultados Principais

**Propriedades DAMI-DSL**:
- Eficiência (Q1): 0% discordo, 8% neutro, 92% concordam que DSL é eficiente
- Expressividade (Q2): 0% discordo, 8% neutro, 92% concordam que DSL expressa lógica claramente
- Flexibilidade (Q3): 0% discordo, 8% neutro, 92% concordam que DSL é flexível
- Concisão (Q4): 0% discordo, 8% neutro, 92% concordam que DSL é conciso
- Expressividade (Q5): 0% discordo, 8% neutro, 92% concordam que DSL é expressivo

**Experiência do Usuário**:
- Satisfação geral (Q6-Q12): 91% concordam que DSL é satisfatório e fácil de usar
- Facilidade de Uso (Q8): 100% concordam que DSL é acessível e direto
- Confiabilidade (Q9): 95% confiam na solução
- Confiança (Q11): 95% reportam confiança na solução implementada
- Satisfação geral (Q12): 91% recomendariam DAMI-DSL para tarefas de migração

**Redução de Complexidade**:
- DAMI-DSL: 85 linhas de código com 18.3% redução em LOC
- SQL equivalente: 4997 linhas
- Redução total: 35.6% em characters count
- Demonstra significativa simplificação da migração

**Análise de Desempenho**:
- Tempo em DAMI-DSL similar ao SQL (sem penalidade significativa)
- Participantes com menos conhecimento técnico mais rápidos em DAMI-DSL
- Taxa de erro: 0.38 para SQL, 0.57 com DAMI-DSL (diferença não estatisticamente significativa)
- DAMI-DSL produziu apenas erros menores comparado a SQL

---

## Desafios do Uso das Metricas

1. **Amostra pequena**: 21 participantes limitam conclusões generalizáveis
2. **Viés educacional**: 11 de 21 são estudantes, não profissionais experientes
3. **Tarefa específica**: Avaliação baseada em cenário único de migração limitada
4. **Ausência de baseline**: Sem comparação com outras ferramentas de migração (ETL comerciais)
5. **Curva de aprendizado**: Participantes podem ter beneficiado de maior exposição a DSL
6. **Contexto real limitado**: Cenário de prova-de-conceito pode não refletir complexidade real de migração

---

## Avaliacao de Qualidade

| Criterio | Pontuacao (0-2) |
|----------|-----------------|
| Objetivo claramente definido | 2 |
| Metodologia adequada | 2 |
| Amostra/contexto descrito | 2 |
| Ameacas a validade discutidas | 1 |
| Resultados com evidencia | 2 |
| Contribuicao clara | 1 |
| **TOTAL** | **10/12** |

---

## Limitacoes

1. Amostra pequena com 11 estudantes vs. 10 desenvolvedores profissionais
2. Tarefa de migração limitada não reflete complexidade de sistemas legado reais
3. Período de coleta de dados não especificado
4. Ausência de comparação com ferramentas ETL comerciais (Google Cloud Data Fusion, AWS DMS, etc.)
5. Foco apenas em propriedades técnicas do DSL sem análise de escalabilidade
6. Feedback qualitativo limitado (resposta única aberta)
7. Validade externa questionável para sistemas de grande escala

---

## Contribuicao Principal

Este estudo demonstra que DAMI-Framework oferece uma solução prática e usável para migração de dados entre esquemas de banco de dados legado para moderno. Os resultados indicam que DAMI-DSL reduz significativamente complexidade (85 LOC vs. 4997 SQL) mantendo flexibilidade e expressividade. Feedback de usuários revela altos níveis de satisfação (91% recomendariam) e confiança (95% confiam na solução). A principal contribuição é fornecer um Domain-Specific Language que simplifica tarefas de migração, permitindo que desenvolvedores foquem em lógica de transformação de alto nível em vez de sintaxe SQL complexa. Implicações práticas incluem: (1) adoção de DAMI-Framework em projetos de modernização de legacy systems, (2) redução de curva de aprendizado para migrações complexas, (3) manutenção facilitada através de código mais conciso e legível. O trabalho contribui para literatura de engenharia de software moderna ao demonstrar efetividade de abordagens baseadas em DSL para problemas específicos de domínio, sugerindo que ferramentas customizadas podem superar soluções genéricas em cenários especializados.

---

*Extraido em Marco 2026 para MLR: Software Developer Metrics in Practice*

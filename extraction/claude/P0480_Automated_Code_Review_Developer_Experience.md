# P0480 — Understanding Automated Code Review Process and Developer Experience in Industry

**Decisao: INCLUIDO | Qualidade: 4/5**

---

## Dados Bibliograficos

| Campo | Valor |
|-------|-------|
| **ID** | P0480 |
| **Autores** | Hyungjin Kim, Yonghwi Kwon, Sangwoo Joh, Hyukin Kwon, Yeonhee Ryou, Taeksu Kim |
| **Ano** | 2022 |
| **Venue** | ESEC/FSE 2022 (30th ACM Joint European Software Engineering Conference) |
| **Tipo** | Estudo Empírico em Indústria (Empirical Industry Study) |
| **Metodo** | Survey e análise quantitativa com dados reais de Samsung Electronics |
| **Amostra** | 93 desenvolvedores; 81.712 review requests em Samsung Electronics |
| **Contexto** | Code Review Automation - Samsung Electronics (2 anos de operação) |

---

## Objetivo

Documentar experiência de implementação e operação de Code Review Bot (CRB), sistema unificado de automatização de code review desenvolvido para Samsung Electronics. O objetivo é entender desafios práticos de automatização de code review em ambientes corporativos grandes, impactos na experiência do desenvolvedor, e lições aprendidas durante 2 anos de operação.

---

## Questoes de Pesquisa

- **RQ1**: Como melhorar a usabilidade e experiência de desenvolvedores com sistemas de automação de code review?
- **RQ2**: Qual é a efetividade de CRB em detectar defeitos e melhorar qualidade?
- **RQ3**: Como reduzir esforço de code review com automação sem afetar qualidade?

---

## Dados da Pesquisa

### Amostra
- 93 desenvolvedores em Samsung Electronics
- 81.712 review requests durante período analisado (agosto 2021)
- 27 milhões de linhas de código adicionadas/removidas
- ~10 mil projetos e ~1.4 milhões de linhas de código em produção

### Fonte de Dados
- Telemetria de CRB (GitHub, P4/Swarm, Gerrit)
- Survey com questões sobre satisfação e efetividade
- Logs de análise de estatísticas de review

### Metodos de Coleta
- Survey com múltiplas-choice questions sobre satisfação
- Análise quantitativa de data de code changes
- Comparação antes/depois de adoção de CRB
- Análise de tipos de defeitos detectados

### Periodo de Analise
- Operação do sistema: ~2 anos (2019-2021 e além)
- Dados analisados: agosto 2021 (single month snapshot)
- Período de study: 2 anos de operação

---

## Metricas e Instrumentos de Avaliacao

**Satisfação do Desenvolvedor**: Survey com Likert scale (1=Strongly Disagree, 5=Strongly Agree):
- Q1: Satisfação com adaptação de CRB aos projetos
- Q2: CRB reduz tempo e esforço em code review
- Q3: CRB ajuda a melhorar qualidade de código
- Q4: Benefícios recebidos com CRB
- Q5: Qual serviço de CRB está mais satisfeito

**Fix Rate de Tipos (Typo, Potential Defects)**: Taxa de correção = (Fixed typos ou defects detectados) / (Total detectados)

**Fix Rate Ajustado**: Ajustado para levara em conta execuções múltiplas do mesmo código.

**Métricas de Review**:
- Número de review comments por semana
- Comprimento médio de review comments
- Frequência de uso de análise

**Estatísticas de Mudanças**:
- Linhas adicionadas/removidas por request
- Distribuição por serviço de análise (Typo, Potential Defects, Architecture Maturity, etc)

---

## Resultados Principais

**Satisfação do Desenvolvedor**: 75.3% responderam positivamente sobre satisfação geral (Q1). 71% concordaram que CRB reduz tempo/esforço (Q2). 79.6% concordaram que CRB melhora qualidade (Q3).

**Efetividade de Detecção**:
- **Typos**: Fix rate de GitHub=72.62%, Swarm=57.10%, Gerrit=59.34%
- **Potential Defects**: Fix rate de GitHub=95.95%, Swarm=61.45%, Gerrit=76.54%

Typo é o tipo mais frequentemente detectado, seguido por Potential Defects, Coding Style, Architecture Maturity, Test Coverage.

**Redução de Esforço**: Mais de 70% de desenvolvedores relataram que CRB reduz esforço de code review. Mais de 60% de typos e alarmes detectados são corrigidos por desenvolvedores.

**Motivação por Automação**: Resultado indica que automação motiva desenvolvedores a focar em melhoria de qualidade de código. Mais de 60% dos defeitos encontrados são corrigidos pelos desenvolvedores.

---

## Desafios do Uso das Metricas

1. Variabilidade entre sistemas de review (GitHub, Swarm, Gerrit): Diferentes fix rates e funcionalidades disponíveis, dificultando comparação direta.

2. Confusão entre fix rate ajustado vs não-ajustado: Interpretação pode levar a superestimar ou subestimar efetividade.

3. Limitação de amostra: Dados de agosto 2021 representam snapshot único, não necessariamente tendência geral de 2 anos.

4. Contexto organizacional: Políticas internas de code review, cultura de qualidade, e expertise dos times afetam métricasse significativamente.

5. Subjetividade em recomendações: Alguns serviços (Architecture, Test Coverage) requerem julgamento manual para decisão final.

---

## Avaliacao de Qualidade

| Criterio | Pontuacao (0-2) |
|----------|----------------|
| Objetivo claramente definido | 2 |
| Metodologia adequada | 2 |
| Amostra/contexto descrito | 2 |
| Ameacas a validade discutidas | 1 |
| Resultados com evidencia | 2 |
| Contribuicao clara | 1 |
| **TOTAL** | **10/12** |

---

## Limitacoes

1. Dados de agosto 2021 (snapshot único), não representativo de período inteiro de operação
2. Amostra limitada a Samsung Electronics (grande empresa), generalização para PMEs questionável
3. Survey com 93 respondentes de múltiplos projetos e contextos diferentes
4. Falta de grupo de controle (comparação antes/depois de CRB)
5. Não captura impacto de CRB em produtividade geral ou tempo de release
6. Contexto de múltiplos sistemas de review (GitHub, Swarm, Gerrit) dificulta generalização

---

## Contribuicao Principal

O trabalho documenta experiência real de implementação de Code Review Bot em grande corporação (Samsung Electronics), revelando que automatização de code review pode efetivamente melhorar satisfação do desenvolvedor (75.3% satisfação geral) enquanto reduz esforço manual. Resultados mostram que automação é particularmente efetiva para tipos específicos de defeitos (potential defects com 95.95% fix rate no GitHub), mas menos efetiva para análises que requerem contexto (architecture, test coverage). Contribui lições práticas sobre escalabilidade, diversidade de ambientes de review, e importância de suporte a múltiplos sistemas de review (GitHub, Swarm, Gerrit). Demonstra que automação bem-implementada motiva desenvolvedores a focar em melhoria de qualidade sem reduzir autonomia.

---

*Extraido em Marco 2026 para MLR: Software Developer Metrics in Practice*

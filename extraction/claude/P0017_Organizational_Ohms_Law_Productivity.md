# P0017 — Organizational Ohm's Law in Practice: Measuring Engineering Productivity

**Decisao: INCLUIDO | Qualidade: 4/5**

---

## Dados Bibliograficos

| Campo | Valor |
|-------|-------|
| **ID** | P0017 |
| **Autores** | Fei Liu, Todd McKinnon |
| **Ano** | 2024 |
| **Venue** | IEEE Transactions on Engineering Management, Vol. 71 |
| **DOI** | 10.1109/TEM.2024.3421892 |
| **Tipo** | Estudo empírico quantitativo com múltiplos projetos |
| **Metodo** | Derivação de Lei de Ohm organizacional; análise em 4 projetos de desenvolvimento de produto |
| **Amostra** | 4 projetos enterprise de desenvolvimento de features IT/security |
| **Contexto** | Ambiente corporativo enterprise com múltiplas linhas de produto |
| **Modo de trabalho** | Análise de dados de projetos reais; coleta de métricas de tempo alocação, habilidades |

---

## Objetivo
Desenvolver e validar um modelo quantitativo baseado na Lei de Ohm organizacional para medir produtividade de engenharia, demonstrando como produtividade é proporcional a eficiência saída-resultado e inversamente proporcional à resistência organizacional.

---

## Questoes de Pesquisa
- **RQ1**: Como a Lei de Ohm pode ser aplicada à produtividade de engenharia organizacional?
- **RQ2**: Qual é a relação entre eficiência saída-resultado, potencial organizacional e resistência?
- **RQ3**: Como medir quantitativamente componentes da Lei de Ohm organizacional?

---

## Metricas e Instrumentos de Avaliacao
- **Métricas de Entrada (Input)**:
  - Alocação de tempo do engenheiro (comunicação, codificação, documentação, testing)
  - Motivação do engenheiro (escala 0-5)
  - Habilidades do engenheiro (escala 0-5)
  - Potencial individual (função de motivação e habilidades)
- **Métricas de Saída (Output)**:
  - Linhas de código (LOC)
  - Duration equivalente do projeto
  - Output corrente por ano
- **Métricas de Resultado**:
  - Business impact (impacto de negócio)
  - Outcome-output alignment
- **Métricas de Resistência Organizacional**:
  - Auto-resistência (self-engineering, colaboração)
  - Resistência de infraestrutura
  - Resistência de processo
- **Métricas Derivadas**: Eficiência saída-resultado, velocidade organizacional

---

## Resultados Principais
- Lei de Ohm organizacional validada em 4 projetos distintos:
  - O/D = η × (v / [R^self + R^collaboration + R^process + R^infrastructure])
- Equação simplificada permite cálculo prático de produtividade
- Variação significativa em resistência organizacional entre projetos (0.40-0.97 para motivação)
- Métrica de produtividade acomoda múltiplas dimensões: LOC, business impact, outcome-output efficiency
- Input product demonstra forte correlação com outcome em análises cross-project

---

## Desafios do Uso das Metricas
- **Medição subjetiva**: Motivação e habilidades requerem avaliação subjetiva, criando viés potencial
- **Definição de LOC**: Diferentes definições e contextos podem afetar comparabilidade entre projetos
- **Variabilidade contextual**: Tipos diferentes de software (web, embedded, desktop) têm características distintas
- **Coleta de dados**: Requer planeamento e comunicação significativa com líderes de engenharia
- **Aproximações simplificadoras**: Primeira ordem simplificação pode não capturar dinâmicas complexas
- **Limitações de comparação cross-cultural**: Aplicabilidade em diferentes culturas organizacionais não testada

---

## Contribuicao Principal
Introduz Lei de Ohm organizacional como framework quantitativo para medir produtividade de engenharia, demonstrando que produtividade é função de eficiência saída-resultado e potencial organizacional, inversamente proporcional a múltiplas formas de resistência organizacional. Fornece modelo prático e intuitivo que integra dimensões técnicas, de processos e organizacionais, validado em múltiplos projetos enterprise.

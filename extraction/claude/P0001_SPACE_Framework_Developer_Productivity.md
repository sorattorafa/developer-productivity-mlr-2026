# P0001 — Understanding Developer Productivity: Input-Output Perspectives Within the SPACE Framework

**Decisao: INCLUIDO | Qualidade: 4/5**

---

## Dados Bibliograficos

| Campo | Valor |
|-------|-------|
| **ID** | P0001 |
| **Autores** | Iman Tunggono, Elfindah Princes |
| **Ano** | 2025 |
| **Venue** | 2025 International Conference on Computing and Applied Informatics (ICCAI) |
| **DOI** | 10.1109/ICCAI65301.2025.11279703 |
| **Tipo** | Estudo empírico quantitativo |
| **Metodo** | Modelagem por Equações Estruturais (PLS-SEM) com survey |
| **Amostra** | 161 desenvolvedores da Indonésia (após remoção de outliers) |
| **Contexto** | Setor de tecnologia da Indonésia pós-layoffs em massa em 2022 |
| **Modo de trabalho** | Pesquisa não presencial com coleta de dados via plataformas profissionais online |

---

## Objetivo
Examinar como as cinco dimensões do framework SPACE (Satisfação, Performance, Activity, Communication, Efficiency) interagem dentro de um modelo de entrada-saída e determinar quais dimensões mais fortemente influenciam a produtividade percebida pelos desenvolvedores.

---

## Questoes de Pesquisa
- **RQ1**: Como as dimensões do framework SPACE interagem dentro de um modelo entrada-saída?
- **RQ2**: Quais dimensões influenciam mais fortemente a produtividade percebida dos desenvolvedores?

---

## Metricas e Instrumentos de Avaliacao
- **Escala Likert de 5 pontos** para medir satisfação, comunicação, eficiência, atividade e performance
- **Indicadores por dimensão**:
  - Satisfação (SATF): 4 itens sobre satisfação, recomendação, recursos, entusiasmo
  - Communication (COMM): 3 itens sobre documentação, conhecimento do trabalho coletivo, feedback
  - Eficiência (EFFC): 3 itens sobre interrupções, revisões, context switching
  - Activity (ACTV): 3 itens sobre pull requests, deploy, code review
  - Performance (PERF): 4 itens sobre arquitetura, reclamações, bugs, confiabilidade
  - Produtividade Percebida (PROD): 3 itens sobre conclusão de tarefas, requisitos, progresso
- **Validade e Confiabilidade**: Cronbach's Alpha (0.64-0.85), CR > 0.5, AVE > 0.5
- **Modelo PLS-SEM** com 1.000 iterações bootstrap

---

## Resultados Principais
- **Performance (PERF)** é o preditor mais forte da produtividade (β = 0.602, p < 0.001), explicando 48.3% da variância
- **Activity (ACTV)** não mostrou relação significativa com produtividade (β = -0.049, p = 0.518)
- **Satisfaction (SATF)** não apresentou influência significativa (β = 0.06, p = 0.219)
- **Communication (COMM)** influencia principalmente através da Performance (β = 0.20, p < 0.001)
- **Efficiency (EFFC)** também influencia indiretamente via Performance (β = 0.17, p = 0.002)
- Métricas quantitativas de atividade têm efeito mínimo; qualidade do output é crítica

---

## Desafios do Uso das Metricas
- Amostra composta predominantemente por desenvolvedores homens (94.41%) e jovens da Indonésia pode limitar generalização
- Metodologia apenas com surveys apresenta risco de viés de auto-relato
- Falta de padronização em métricas de produtividade dificulta comparação entre estudos
- Necessidade de combinar dados perceptuais com métricas objetivas (frequência de commits)
- Variações culturais e organizacionais podem afetar aplicabilidade do framework em diferentes contextos

---

## Contribuicao Principal
Demonstra empiricamente que a qualidade do output (Performance) é o principal driver da produtividade percebida, não métricas de atividade quantitativas, desafiando abordagens convencionais de medição. O estudo comprova que comunicação e eficiência influenciam principalmente através da melhoria da qualidade do trabalho, não do volume de atividade.

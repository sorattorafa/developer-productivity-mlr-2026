# G016 — Experience with GitHub Copilot for Developer Productivity at Zoominfo

**Decisao: INCLUIDO (Caso de estudo de avaliação de produtividade de desenvolvedores com ferramenta de IA) | Qualidade: 4/5**

---

## Dados Bibliograficos

| Campo | Valor |
|-------|-------|
| **ID** | G016 |
| **Autores** | Gal Bakal, Ali Dasdan, Yaniv Katz, Michael Kaufman, Guy Levin (ZoomInfo) |
| **Ano** | 2025 |
| **Venue** | arXiv (preprint) |
| **URL** | arXiv: 2501.13282v1 |
| **Tipo** | Relatório Técnico / Caso de Estudo |
| **GL Tier** | 2nd (Technical report with empirical data) |
| **Metodo** | Estudo de caso de 4 fases com métricas quantitativas e qualitativas |
| **Contexto** | Implementação de GitHub Copilot em ZoomInfo (400+ desenvolvedores) |

---

## Objetivo
Avaliar sistematicamente o impacto do GitHub Copilot no productivity de desenvolvedores através de abordagem de 4 fases com mais de 400 desenvolvedores, combinando métricas quantitativas (acceptance rates) e feedback qualitativo (surveys).

---

## Frameworks e Metricas

### Frameworks Mencionados
- Framework de Produtividade de Desenvolvedores (quantitativo + qualitativo)
- Métricas DORA (deployment frequency, lead time, change failure rate, mean time to restore)
- SPACE Framework Dimensions (Satisfaction, Performance, Activity, Communication, Efficiency)

### Metricas Propostas/Discutidas
- **Acceptance Rate (Sugestões)**: 33% - percentual de sugestões aceitas
- **Acceptance Rate (Linhas de Código)**: 20% - percentual de linhas sugeridas que foram aceitas
- **Suggestions per Day**: ~6.500 sugestões por dia
- **Lines Suggested per Day**: ~15.000 linhas sugeridas por dia
- **Average Lines per Suggestion**: 2,8 linhas
- **Developer Satisfaction Score**: 72% - satisfação geral com ferramenta
- **Time Savings**: ~20% de desenvolvedores citam economia de tempo como principal benefício
- **Language-specific Acceptance Rates**: Variações por linguagem (TypeScript, Java, Python, Kotlin >30%)
- **Editor-specific Rates**: JetBrains e VS Code com acceptance rates próximos (~30%)

---

## Principais Contribuicoes
- Avaliação empirical sistemática em escala real (400+ desenvolvedores, 26 dias de dados) de GitHub Copilot em contexto empresarial
- Demonstração que acceptance rate é métrica prática e viável para avaliar adoção e utilidade de ferramentas de IA no desenvolvimento
- Identificação de variações por linguagem de programação: TypeScript, Java, Python, Kotlin superiores a 30% de acceptance rate
- Análise qualitativa mostrando alinhamento entre satisfação reportada (72%) e benefícios específicos: economia de tempo, redução de tarefas repetitivas
- Documentação de limitações e preocupações com adoção: qualidade de código, context awareness, sobre-confiança, segurança/IP, impacto em aprendizado
- Proposta de abordagem faseada: avaliação inicial → recrutamento de trial → trial de 2 semanas → rollout completo

---

## Contribuicao Principal
Este caso de estudo fornece validação empírica em escala real de como avaliar impacto de ferramentas de IA em produtividade de desenvolvedores. A contribuição principal é metodológica: demonstra que acceptance rate é métrica prática, computável automaticamente e altamente correlacionada com satisfação de desenvolvedores. Diferencia-se de estudos acadêmicos por integrar dados reais de empresa (Google/Amazon cloud infrastructure, 400+ developers), métricas DORA, e dimensões SPACE com feedback qualitativo de desenvolvedores. Fornece também insights sobre variações por linguagem de programação e IDE, sugerindo que avaliações de ferramentas de IA devem considerar contexto técnico específico.

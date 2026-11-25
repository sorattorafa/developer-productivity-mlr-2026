# G016 — Experience with GitHub Copilot at ZoomInfo (400+ developers)

**Decisao: INCLUIDO | Qualidade GL: 6/6**

---

## Dados Bibliograficos

| Campo | Valor |
|-------|-------|
| **ID** | G016 |
| **Autor/Organizacao** | Gal Bakal, Ali Dasdan, Yaniv Katz, Michael Kaufman, Guy Levin (Zoominfo) |
| **Data** | January 24, 2025 |
| **Tipo** | Industry White paper / Case Study |
| **URL** | N/A (Based on provided PDF excerpts) |

---

## Resumo

Este documento apresenta um estudo de caso detalhado sobre a implantação do **GitHub Copilot** na ZoomInfo, envolvendo mais de 400 desenvolvedores [1, 2]. A organização adotou uma abordagem sistemática de quatro fases para avaliação e rollout: avaliação inicial qualitativa, recrutamento para testes com critérios de conformidade, um teste controlado de duas semanas com 126 engenheiros e, por fim, a implantação em toda a empresa através de um workflow gerenciado [3-6].

A análise combina métricas quantitativas de uso com feedback qualitativo coletado via pesquisas de satisfação de desenvolvedores [1, 7]. Os resultados indicam uma **acceptance rate** média de 33% para sugestões e 20% para linhas de código, com uma pontuação de satisfação dos desenvolvedores de 72% [1, 8]. O estudo destaca que a ferramenta é particularmente eficaz para a geração de **boilerplate code** e **unit tests**, embora apresente limitações em lógica específica de domínio e consistência de qualidade [9-11].

---

## Frameworks Mencionados

*   **DORA**: Mencionado como uma métrica quantitativa objetiva para medir a produtividade e planejado para avaliações de impacto de longo prazo [12-14].
*   **SPACE**: Citado no contexto de fatores que afetam a produtividade dos desenvolvedores e trabalhos relacionados [15, 16].
*   **DevEx (Developer Experience)**: Discutido como uma abordagem centrada no desenvolvedor para medir e melhorar a produtividade através de sentimentos e percepções [17, 18].

---

## Metricas Mencionadas

*   **Acceptance rate of shown suggestions**: Definida como a proporção de sugestões aceitas em relação ao total mostrado; considerada o melhor preditor de produtividade percebida [13, 19, 20].
*   **Lines acceptance rate**: Proporção de linhas de código sugeridas que foram efetivamente aceitas [21, 22].
*   **Developer Satisfaction (DevSat)**: Métrica interna calculada pela diferença entre sentimentos positivos e negativos em pesquisas trimestrais [23, 24].
*   **Time savings**: 90% dos entrevistados relataram redução no tempo de tarefas, com uma mediana de 20% de economia de tempo [9, 24].
*   **Tasks per sprint**: 63% dos desenvolvedores afirmaram que a ferramenta permitiu completar mais tarefas por sprint [24].
*   **Lines of code (LOC)**: Monitoramento do volume de código de produção contribuído pela ferramenta, atingindo centenas de milhares de linhas [9, 25].

---

## Insights para Praticantes

*   **Phased Deployment**: A adoção de um processo em fases, incluindo treinamento de segurança e alinhamento de políticas de governança, é essencial para mitigar riscos em larga escala [3, 11].
*   **Core Utility**: Os maiores ganhos de produtividade ocorrem na geração de **unit tests**, **boilerplate code**, nomes de variáveis e documentação [10, 26].
*   **Language Specificity**: A eficácia varia por linguagem; linguagens como **Go** apresentaram taxas de aceitação superiores (43.3%), enquanto linguagens como **HTML**, **CSS** e **SQL** tiveram performance inferior [25, 27, 28].
*   **Human-in-the-loop**: Devido a limitações em **domain-specific logic** e potenciais riscos de segurança, o código gerado por IA exige revisão rigorosa e não deve substituir o julgamento humano [9, 10, 29, 30].
*   **Tooling Satisfaction**: O **GitHub Copilot** apresentou o maior sentimento positivo entre todas as ferramentas da **software delivery toolchain** na organização [17, 24].

---

## Avaliacao de Qualidade GL (Garousi et al.)

| Criterio | Pontuacao (0-1) |
|----------|----------------|
| Autoridade do autor/organizacao | 1 |
| Descricao de metodologia | 1 |
| Data de publicacao | 1 |
| Objetividade (vies comercial) | 1 |
| Referencias citadas | 1 |
| Contribuicao nova | 1 |
| **TOTAL** | **6/6** |

---

*Extraido via NotebookLM em March 2026 para MLR: Software Developer Metrics in Practice*
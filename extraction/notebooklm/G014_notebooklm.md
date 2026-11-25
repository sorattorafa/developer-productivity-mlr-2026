# G014 — Measuring GitHub Copilot's Impact on Productivity

**Decisao: INCLUIDO | Qualidade GL: 5.5/6**

---

## Dados Bibliograficos

| Campo | Valor |
|-------|-------|
| **ID** | G014 |
| **Autor/Organizacao** | Albert Ziegler, Eirini Kalliamvakou, X. Alice Li, Andrew Rice, Devon Rifkin, Shawn Simister, Ganesh Sittampalam, Edward Aftandilian [1] |
| **Data** | March 2024 [2] |
| **Tipo** | Industry Report (Communications of the ACM) [1, 2] |
| **URL** | https://cacm.acm.org/research/measuring-github-copilots-impact-on-productivity/ [1] |

---

## Resumo

Este estudo investiga se as medições de uso das interações dos desenvolvedores com o **GitHub Copilot** podem prever a produtividade percebida relatada pelos próprios profissionais [1]. A pesquisa analisou 2.631 respostas de questionários e correlacionou esses dados com medições de telemetria coletadas diretamente no **IDE** [1]. Os resultados indicam que ferramentas de **AI pair-programming** impactam positivamente desenvolvedores de todos os níveis de senioridade, com ganhos mais expressivos observados entre desenvolvedores iniciantes [3].

A análise revela que os benefícios abrangem diversas dimensões da produtividade, incluindo o tempo de tarefa, qualidade do produto, **cognitive load**, satisfação (**enjoyment**) e aprendizado [3]. O fator determinante para a melhoria não é necessariamente a correção absoluta do código sugerido, mas sim se a sugestão serve como um ponto de partida útil (**useful starting point**) para o desenvolvimento posterior [3, 4]. O estudo conclui que a **Acceptance rate** é o indicador imediato mais forte da produtividade percebida [4, 5].

---

## Frameworks Mencionados

*   **SPACE**: Discutido e utilizado para desenhar o questionário de pesquisa, capturando a produtividade autorrelatada em quatro dimensões: **Satisfaction and well-being** (S), **Performance** (P), **Communication and collaboration** (C) e **Efficiency and flow** (E) [5].

---

## Metricas Mencionadas

*   **Acceptance rate**: Definida como o número de aceitações normalizado pelas conclusões exibidas; identificada como o melhor preditor de produtividade percebida (rho=0.24, P<0.0001) [5].
*   **Shown rate**: Frequência com que sugestões são exibidas [5].
*   **Persistence rate** e **Fuzzy persistence rate**: Medidas de permanência do código sugerido após a aceitação [5].
*   **Efficiency**: Eficiência geral no uso da ferramenta [5].
*   **Contribution speed**: Velocidade de contribuição de código [5].
*   **Acceptance frequency** e **Persistence frequency**: Frequência absoluta de aceitações e persistência de código [5].
*   **Total volume**: Volume total de código gerado ou interagido [5].
*   **Loquaciousness**: Nível de detalhamento ou verbosidade das interações [5].
*   **Eagerness**: Prontidão na interação com as sugestões [5].

---

## Insights para Praticantes

*   **Ganhos por Senioridade**: Desenvolvedores **junior** relatam maiores ganhos de produtividade e aceitam mais sugestões da IA [4].
*   **Valor para Experientes**: Embora aceitem menos sugestões, desenvolvedores experientes se beneficiam ao manter o **flow**, focar em tarefas mais satisfatórias e reduzir o esforço em tarefas repetitivas [4].
*   **Qualidade vs. Utilidade**: Uma sugestão que serve como um "template útil para ajustes" (**useful template to tinker with**) pode ser tão valiosa para a produtividade quanto uma linha de código perfeitamente correta [4].
*   **Padrões Temporais**: As taxas de aceitação tendem a ser ligeiramente maiores durante fins de semana e noites (23-23.5%) em comparação com o horário comercial padrão (21.2%) [4].

---

## Avaliacao de Qualidade GL (Garousi et al.)

| Criterio | Pontuacao (0-1) |
|----------|----------------|
| Autoridade do autor/organizacao | 1 |
| Descricao de metodologia | 1 |
| Data de publicacao | 1 |
| Objetividade (vies comercial) | 0.5 |
| Referencias citadas | 1 |
| Contribuicao nova | 1 |
| **TOTAL** | **5.5/6** |

---

*Extraido via NotebookLM em March 2026 para MLR: Software Developer Metrics in Practice*
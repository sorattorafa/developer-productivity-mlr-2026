# G071 — Harnessing the potential of Gen-AI coding assistants in public sector software development

**Decisao: INCLUIDO | Qualidade GL: 6/6**

---

## Dados Bibliograficos

| Campo | Valor |
|-------|-------|
| **ID** | G071 |
| **Autor/Organizacao** | Kevin KB Ng, Liyana Fauzi, Leon Leow, Jaren Ng (Government Technology Agency - GovTech Singapore) |
| **Data** | Abril 2024 |
| **Tipo** | Industry Report / White Paper |
| **URL** | Não explicitamente disponível nos excertos |

---

## Resumo

Este relatório detalha um estudo piloto conduzido pelo Engineering Productivity Programme (EPP) da GovTech Singapore sobre o uso do GitHub Copilot no desenvolvimento de software para o setor público [1, 2]. O estudo avaliou 70 desenvolvedores durante quatro meses (outubro de 2023 a janeiro de 2024), utilizando a infraestrutura SHIP-HATS (DevSecOps) do governo de Singapura para medir o impacto na produtividade e na satisfação dos profissionais [3-5].

Os resultados demonstram que assistentes de codificação baseados em Gen-AI têm alto potencial para acelerar o desenvolvimento, com aumentos registrados de 21% a 28% na velocidade de codificação e tarefas [1, 6]. O estudo observou que desenvolvedores juniores e de nível médio obtiveram os maiores ganhos de eficiência (até 33% de redução no tempo de codificação) ao automatizar tarefas repetitivas, como a criação de unit tests [7-9]. No entanto, o relatório adverte sobre preocupações com segurança, "alucinações" da IA e a necessidade de supervisão humana para evitar a adoção de más práticas de programação por desenvolvedores menos experientes [10, 11].

---

## Frameworks Mencionados

*   **SPACE**: Utilizado como a estrutura principal para o questionário de pesquisa e para medir dimensões de produtividade como satisfação, performance e eficiência [12-14].
*   **DORA**: Mencionado como um framework essencial da indústria para medir produtividade em nível de equipe; recomendado para avaliações futuras [15].
*   **DevSecOps**: Contexto técnico no qual a ferramenta foi inserida, especificamente através do framework SHIP-HATS [3].
*   **SHIP-HATS (Secure Hybrid Integration Pipeline - Hive Agile Testing Solutions)**: O framework de CI/CD e tecnologia oficial do governo de Singapura utilizado no piloto [3, 16].

---

## Metricas Mencionadas

*   **Acceptance Rate**: Porcentagem de sugestões da IA aceitas pelos desenvolvedores (média de 22%, com picos em Terraform e TypeScript) [17, 18].
*   **Accepted Lines-of-Code**: Volume de código sugerido pela IA que foi efetivamente integrado aos projetos [18, 19].
*   **Coding Time Reduction**: Redução percentual no tempo gasto em atividades de codificação (22% de média geral) [7, 8].
*   **Task Completion Speed Increase**: Aumento na velocidade de conclusão de tarefas (21% de média geral) [8].
*   **Productivity Increase**: Percepção de aumento de produtividade (24% de média percebida; 12% normalizada para o tempo total do desenvolvedor fora da IDE) [8, 20].
*   **Developer Satisfaction**: Percentual de desenvolvedores que se sentem mais satisfeitos ou realizados (95% de concordância) [1, 13].
*   **Learning Acceleration**: Medida de quão rápido os desenvolvedores aprendem novas linguagens com a ferramenta (75% de concordância) [21].
*   **DORA Metrics**: Deployment Frequency, Lead Time for Changes, Time to Restore Service e Change Failure Rate (citadas como métricas de equipe para o futuro) [15, 22].

---

## Insights para Praticantes

*   **Classificação de Código e Segurança**: Desenvolvedores devem classificar o código como "Open" para usar ferramentas baseadas em Cloud como GitHub Copilot; para código confidencial, recomendam-se ferramentas self-hosted como Code Llama ou Codeium [1, 6, 23].
*   **Ganhos Reais de Produtividade**: Embora a velocidade de codificação aumente significativamente, o ganho real na produtividade total do desenvolvedor é de cerca de 12%, dado que apenas 50% do tempo de trabalho é gasto efetivamente dentro da IDE [20].
*   **Riscos para Iniciantes**: O uso excessivo de assistentes por desenvolvedores sem bases sólidas pode consolidar erros ou maus hábitos devido às ocasionais imprecisões (hallucinations) do modelo [11, 21].
*   **Padronização Tecnológica**: Uma stack tecnológica padronizada entre diferentes órgãos governamentais facilitaria o aprendizado compartilhado e o desenvolvimento de modelos de ML mais eficazes para o contexto público [24, 25].
*   **Prompt Engineering**: O treinamento em engenharia de prompts é considerado crucial para maximizar os benefícios e a precisão das ferramentas de IA [25].

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
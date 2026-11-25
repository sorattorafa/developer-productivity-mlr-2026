# P0521 — Developers experience (DX) in ALM software tools: an investigation on virtual kanban boards

**Decisao: INCLUIDO | Qualidade: 5/5**

---

## Dados Bibliograficos

| Campo | Valor |
|-------|-------|
| **ID** | P0521 |
| **Autores** | Jullia Saad, Priscila Portela Costa, Alexandre Alvaro, Luciana A. M. Zaina |
| **Ano** | 2020 |
| **Venue** | 34th Brazilian Symposium on Software Engineering (SBES ’20) |
| **DOI** | https://doi.org/10.1145/3422392.3422475 |
| **Tipo** | Conference paper |
| **Metodo** | Qualitative (Focus Group) |
| **Amostra** | 10 software developers |
| **Contexto** | Industry (professionals from different organizations in Brazil) |
| **Modo de trabalho** | Mixed (5 co-located, 4 remote, 1 partially co-located) |
| **Metodologia** | Agile (Kanban, Scrum, XP, TDD) |

---

## Objetivo

O principal objetivo deste artigo é examinar a **Developer Experience (DX)** de profissionais de software ao utilizarem quadros Kanban virtuais no contexto de ferramentas de **Application Life-cycle Management (ALM)** [1, 2]. A pesquisa busca identificar os problemas e desafios enfrentados pelos desenvolvedores que impactam sua percepção sobre a infraestrutura de desenvolvimento, seus sentimentos em relação ao trabalho e o valor de sua contribuição [2, 3].

---

## Questoes de Pesquisa

*   **RQ1:** Which DX issues do software professionals face when using a virtual kanban board tool? [2]

---

## Metricas e Instrumentos de Avaliacao

O estudo utiliza uma abordagem qualitativa baseada no framework de DX de Fagerholm, focando em dimensões perceptivas em vez de métricas quantitativas tradicionais [3].

| Metrica | Categoria | Nivel | Como Coletada | Validada |
|---------|-----------|-------|---------------|----------|
| **Productivity** | Productivity | Individual/Team | Percepção relatada em Focus Group | No |
| **Time (hours worked)** | Activity | Individual | Automatizada pela ferramenta (mencionada como fator de estresse) | Yes (pela ferramenta) |
| **Project status statistics** | Delivery | Team | Gerada automaticamente por ferramentas virtuais (mencionada em trabalhos relacionados) | Yes (pela ferramenta) |
| **Scope understanding** | DevEx | Individual/Team | Codificação qualitativa de falas (Fator C1) | Partial (via pesquisadores) |

---

## Frameworks e Metricas

### Frameworks Referenciados
*   **DX Dimension Framework (Fagerholm)**: **APPLIED**. Utilizado como lente principal para análise qualitativa, dividindo a experiência em Cognition, Affect e Conation [3, 4].
*   **User eXperience (ISO/IEC 9241-210)**: **REFERENCED**. Usado para diferenciar os conceitos de UX e DX [5].

### Frameworks Propostos
O artigo não propõe um novo framework, mas aplica o framework de Fagerholm especificamente ao contexto de quadros Kanban virtuais [2, 6].

---

## Fatores que Influenciam Produtividade

### Fatores Positivos
| Fator | Categoria |
|-------|-----------|
| Simple tools with low learning effort | Human |
| Visibility of activity status | Process |
| Automated statistics and records | Technical |

### Fatores Negativos
| Fator | Categoria |
|-------|-----------|
| Tool complexity (e.g., Jira learning curve) | Technical |
| Lack of project scope visibility | Process |
| Difficulty linking multiple people to a task | Technical |
| Lack of synchronization between physical and virtual boards | Process |
| Inadequate problem descriptions in bugs | Process |

---

## Papel da IA e Automacao

| Campo | Valor |
|-------|-------|
| Usa IA/ML? | No — Embora um participante fosse cientista de dados de IA, a pesquisa não utilizou IA na investigação [7]. |
| Automacao de coleta? | No — Os dados foram coletados via gravações de áudio e transcrição manual [8, 9]. |
| Impacto de IA na produtividade? | Not mentioned in the results. |

---

## Resultados Principais

*   Identificação de **9 categorias de problemas (C1-C9)** enfrentados por desenvolvedores ao usar quadros Kanban [10, 11].
*   **Scope understanding (C1)** foi o problema mais citado (18 ocorrências), revelando que a falta de acesso a informações e a complexidade das ferramentas dificultam a visão geral do projeto [10, 12].
*   A **Complexity (C3)** das ferramentas (como o Jira) impacta negativamente as três dimensões de DX: cognição (aprendizado), afeto (frustração) e conação (produtividade) [12, 13].
*   A incapacidade de **vincular várias pessoas a uma tarefa** ou a falta de visibilidade para tarefas não-técnicas (reuniões, estudos) gera uma percepção negativa sobre o valor da contribuição individual [14, 15].
*   Ferramentas virtuais reduzem o tempo de reuniões, mas podem diminuir a comunicação orgânica entre os membros da equipe [16].

---

## Desafios do Uso das Metricas

*   **Falta de flexibilidade** nas ferramentas para customizar fluxos de trabalho ou estágios de desenvolvimento [17].
*   **Dificuldade em rastrear atividades** que não se encaixam no conceito padrão de "cartão" do Kanban, como sessões de estudo ou chamadas [15].
*   **Problemas de usabilidade** e falta de feedback visual (User Interface) que levam a erros operacionais, como mover cartões acidentalmente [17].

---

## Avaliacao de Qualidade Metodologica

| Criterio | Pontuacao (0-2) |
|----------|----------------|
| Objetivo claramente definido | 2 |
| Metodologia adequada ao objetivo | 2 |
| Amostra/contexto descrito adequadamente | 2 |
| Ameacas a validade discutidas | 2 |
| Resultados com evidencia suficiente | 2 |
| Contribuicao clara para pratica ou teoria | 2 |
| **TOTAL** | **12/12** |

---

## Limitacoes

O estudo aponta como principal limitação o **tamanho reduzido da amostra** (10 participantes), o que exige cautela na generalização dos resultados e indica a necessidade de expandir a análise em trabalhos futuros [18].

---

## Contribuicao Principal

A principal contribuição deste trabalho é a investigação da **Developer Experience (DX) em ferramentas ALM**, preenchendo uma lacuna na literatura que foca majoritariamente em IDEs [6]. O estudo demonstra que problemas técnicos e de interface em quadros Kanban virtuais transcendem a mera usabilidade, impactando profundamente o estado emocional dos desenvolvedores e sua percepção de valor e produtividade dentro da organização [18, 19].

---

*Extraido via NotebookLM em March 2026 para MLR: Software Developer Metrics in Practice*
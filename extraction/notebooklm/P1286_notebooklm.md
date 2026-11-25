# P1286 — Investigating Developer Experience in Software Reuse
**Decisão: INCLUÍDO | Qualidade: 5/5**

## Dados Bibliográficos
| Campo | Valor |
|-------|-------|
| **ID** | P1286 |
| **Autores** | Rodrigo Feitosa Gonçalves, Cláudia Maria Lima Werner, Claudio Miceli de Farias |
| **Ano** | 2024 |
| **Venue** | SBCARS '24: Brazilian Symposium on Software Components, Architectures, and Reuse |
| **DOI** | Não especificado diretamente no artigo (Dataset disponível via 10.5281/zenodo.12685772) |
| **Tipo** | Conference paper (Rapid Review) |
| **Método** | Rapid Review (RR) complementada por Backward Snowballing |
| **Amostra** | 328 estudos recuperados inicialmente, com 10 estudos primários selecionados para extração de dados detalhada |
| **Contexto** | Literatura acadêmica sobre Experiência do Desenvolvedor (DX) e Reúso de Software |
| **Modo de trabalho** | Revisão Secundária da Literatura / Estudo Bibliográfico |
| **Metodologia** | Protocolo baseado nas diretrizes de Cartaxo et al. e Kitchenham & Charters; extração suportada pela ferramenta Parsifal; síntese de dados baseada em codificação qualitativa indutiva e axial (inspirada em Charmaz) |

---

## Objetivo
Investigar os fatores, barreiras e estratégias que influenciam a Experiência do Desenvolvedor (DX - *Developer Experience*) no contexto das práticas de reúso de software.

---

## Questões de Pesquisa
*   **RQ1:** Quais são os principais fatores que afetam a experiência do desenvolvedor no reúso de software?
*   **RQ2:** Quais barreiras impedem os desenvolvedores de melhorar os fatores que afetam a experiência do desenvolvedor no reúso de software?
*   **RQ3:** Quais são as estratégias usadas para melhorar a experiência do desenvolvedor no reúso de software?

---

## Métricas e Instrumentos de Avaliação

| Métrica | Categoria | Nível | Como Coletada | Validada |
|---------|-----------|-------|---------------|----------|
| **Formulário de Extração (Parsifal)** | Process | Estudo | Coleta qualitativa dos dados bibliográficos, fatores, barreiras e estratégias dos artigos selecionados | Sim (por 2º pesquisador) |
| **Síntese de Dados (Codificação)** | Analysis | Estudo | Codificação qualitativa aberta e axial (abordagem *bottom-up* de Charmaz) de unidades coerentes de texto | Sim |

---

## Frameworks e Métricas
### Frameworks Referenciados
*   **Conceito de Developer Experience (Fagerholm e Münch):** O estudo utiliza esta perspectiva que divide a DX em áreas cognitivas (como os desenvolvedores percebem a infraestrutura), afetivas (como se sentem sobre o trabalho) e conativas (como percebem o valor de sua contribuição).

### Frameworks Propostos
*   Não há proposta de um framework formal, mas o artigo categoriza os elementos analisados em um esquema focado em três dimensões principais da experiência: **Fatores Técnicos**, **Fatores Organizacionais** e **Fatores Humanos/Sociais**.

---

## Fatores que Influenciam Produtividade (Focados na Experiência do Desenvolvedor)
### Fatores Positivos (Facilitadores e Estratégias)
| Fator | Categoria |
|-------|-----------|
| Compreensão da funcionalidade, interações e arquitetura do software | Technical |
| Documentação abrangente e interfaces bem documentadas (APIs) | Technical |
| Disponibilidade de infraestrutura compatível com o reúso (padrões e ferramentas) | Technical |
| Apoio gerencial "Top-Down", cultura organizacional voltada ao projeto | Organizational |
| Treinamento adequado e estabelecimento de incentivos ao reúso | Process/Organizational |
| Alta autoeficácia e experiência prévia do desenvolvedor com o reúso | Human/Social |
| Boa comunicação, fóruns de discussão colaborativa e apoio social | Human/Social |

### Fatores Negativos (Barreiras)
| Fator | Categoria |
|-------|-----------|
| Incompatibilidade de licenças e problemas de linguagem de programação | Technical |
| Arquitetura complexa e documentação incompleta/desatualizada | Technical |
| Falta de acesso eficiente a componentes reusáveis (ineficiência no reúso) | Technical |
| Falta de apoio da Alta Administração (*Top Management*) e recursos limitados | Organizational |
| Treinamento, educação e esquemas de incentivo ineficazes | Organizational |
| Resistência à mudança (ex: Síndrome "Not Invented Here") e ceticismo | Human/Social |
| Percepção de ausência de benefícios imediatos | Human/Social |

---

## Papel da IA e Automação

| Campo | Valor |
|-------|-------|
| Usa IA/ML? | Não — O estudo examina as práticas e experiências fundamentais (sociotécnicas) do reúso e não o uso de Inteligência Artificial. |
| Automação de coleta? | Não — Como revisão de literatura, utiliza apenas automação padrão de buscas acadêmicas (Scopus). |
| Impacto de IA na produtividade? | Não se aplica. A pesquisa destaca que a melhoria da produtividade baseia-se em infraestrutura sólida (ex: IDEs, ferramentas de repositório), documentação confiável e fatores organizacionais/sociais. |

---

## Resultados Principais
*   **15 Fatores de DX:** Classificados em Técnicos (ex: documentação e infraestrutura), Organizacionais (ex: cultura do projeto e influências do cliente) e Humanos/Sociais (ex: colaboração, comunidade, autoeficácia e experiência de reúso do desenvolvedor).
*   **7 Barreiras ao Reúso:** Destaque para a ausência de apoio gerencial superior, a falta de treinamento adequado, a limitação de acesso a componentes reusáveis e a resistência intrínseca das equipes e indivíduos à mudança.
*   **13 Estratégias Mitigadoras:** Foram identificadas táticas essenciais para superar obstáculos, incluindo promoção de *training/incentives*, desenvolvimento de guias práticos (*cookbooks* e manuais de referência), incentivo à experimentação, programas de mentoria e implementação de uma cultura *top-down* de apoio ao reúso.

---

## Desafios do Uso das Métricas
*   Embora a literatura não foque extensivamente em métricas numéricas, o estudo destaca como desafio estrutural que a **falta de métricas e medidas adequadas para avaliar benefícios e custos do reúso** desencoraja a alta administração (*management*) de investir adequadamente nas práticas de reúso, o que diretamente enfraquece a experiência dos desenvolvedores.

---

## Avaliação de Qualidade Metodológica

| Critério | Pontuação (0-2) |
|----------|----------------|
| Objetivo claramente definido | 2 |
| Metodologia adequada ao objetivo | 2 |
| Amostra/contexto descrito adequadamente | 2 |
| Ameaças à validade discutidas | 2 |
| Resultados com evidência suficiente | 2 |
| Contribuição clara para prática ou teoria | 2 |
| **TOTAL** | **12/12** |

---

## Limitações
*   A pesquisa primária utilizou como fonte principal apenas a base **Scopus** o que, não obstante a mitigação feita pelo método *backward snowballing*, pode ter desconsiderado publicações relevantes exclusivas do IEEE Xplore ou ACM.
*   O pequeno número de artigos finais selecionados na filtragem (**apenas 10 estudos**) representa uma ameaça tangível à generalização absoluta das conclusões.
*   Devido a restrições de tempo e recursos, não foi empregada a técnica de *forward snowballing* para estender a malha de captura de estudos.

---

## Contribuição Principal
O estudo entrega uma síntese compreensiva, e muito necessária, da Experiência do Desenvolvedor (DX) focada primariamente no **fator humano do reúso de código** — área muitas vezes negligenciada pelas abordagens excessivamente técnicas. Ao elencar 15 influenciadores críticos, 7 barreiras e 13 estratégias acionáveis, a pesquisa equipa gestores, pesquisadores e profissionais da indústria com um guia de orientação prática destinado a reduzir a carga cognitiva das equipes de software e catalisar, simultaneamente, satisfação no trabalho, inovação e retenção de talentos.
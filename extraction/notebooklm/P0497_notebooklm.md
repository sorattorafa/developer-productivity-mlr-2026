# P0497 — Assessing DX through the correlation between affectivity and self-assessed productivity in a public institution

**Decisao: INCLUIDO | Qualidade: 5/5**

---

## Dados Bibliograficos

| Campo | Valor |
|-------|-------|
| **ID** | P0497 |
| **Autores** | Fabian Oliveira Lopes, Ana Carolina Oran, Bruno Gadelha |
| **Ano** | 2022 |
| **Venue** | XXI Brazilian Symposium on Software Quality (SBQS ’22) |
| **DOI** | 10.1145/3571473.3571494 |
| **Tipo** | Conference paper |
| **Metodo** | Mixed methods (Qualitative and Quantitative), Controlled experiment, Case study |
| **Amostra** | 11 software development professionals in a public institution |
| **Contexto** | Public institution (Municipal secretary of economy, finance, and technology) |
| **Modo de trabalho** | On-site (acompanhamento in loco) |
| **Metodologia** | Mixed (Maintenance, automation of CI/CD processes, and DevOps) |

---

## Objetivo

O objetivo deste estudo é avaliar a Developer Experience (DX) em equipes de desenvolvimento do serviço público municipal, utilizando a correlação entre as dimensões afetivas (Valence, Arousal e Dominance) e a produtividade autoavaliada (sPR) [1, 2]. O estudo busca identificar como esses aspectos humanos influenciam o desempenho em atividades de desenvolvimento de software em tempo real [1, 3].

---

## Questoes de Pesquisa

RQ1: Como a DX afeta a produtividade dos desenvolvedores durante a execução de suas atividades nos projetos de software do serviço público municipal? [3]

---

## Metricas e Instrumentos de Avaliacao

| Metrica | Categoria | Nivel | Como Coletada | Validada |
|---------|-----------|-------|---------------|----------|
| Valence (Satisfação) | Affectivity | Individual | Self-Assessment Manikin (SAM) technique | Yes |
| Arousal (Motivação) | Affectivity | Individual | Self-Assessment Manikin (SAM) technique | Yes |
| Dominance (Controle/Aprendizado) | Affectivity | Individual | Self-Assessment Manikin (SAM) technique | Yes |
| Self-assessed Productivity (sPR) | Productivity | Individual | 5-point Likert scale questionnaire | Yes |

---

## Frameworks e Metricas

### Frameworks Referenciados
- **DX Framework (Fagerholm & Munch)**: APPLIED (Fundamentação teórica para as dimensões de Percepção, Efeito e Expectativa) [2, 4, 5].
- **Affective Effects Theory (AET)**: REFERENCED (Citado como proposta para trabalhos futuros) [6].

### Frameworks Propostos
O artigo não propõe um novo framework, mas sim a aplicação de um modelo de correlação entre afetividade e produtividade adaptado ao contexto público [2, 3].

---

## Fatores que Influenciam Produtividade

### Fatores Positivos
| Fator | Categoria |
|-------|-----------|
| Satisfação com a tarefa (Valence) | Human |
| Motivação (Arousal) | Human |
| Sensação de competência/domínio (Dominance) | Human |
| Entendimento do problema via pesquisa | Process |

### Fatores Negativos
| Fator | Categoria |
|-------|-----------|
| Fome e proximidade do horário de almoço | Human |
| Falta de comunicação entre técnico e usuário | Organizational |
| Falta de requisitos claros | Process |
| Falha na infraestrutura e equipamentos | Technical |
| Cansaço físico e mental | Human |

---

## Papel da IA e Automacao

| Campo | Valor |
|-------|-------|
| Usa IA/ML? | No |
| Automacao de coleta? | Partial (Uso de formulários digitais, mas transcrição manual para a ferramenta) |
| Impacto de IA na produtividade? | Not specified |

---

## Resultados Principais

- **Correlação Positiva**: Foi validada a existência de uma correlação positiva entre todas as dimensões afetivas e a produtividade autoavaliada [7, 8].
- **Força da Correlação**: A **Valence** (r = 0.753) e a **Arousal** (r = 0.716) apresentaram ligações mais fortes com a produtividade do que a **Dominance** (r = 0.420) [9, 10].
- **Diferença de Contexto**: Ao contrário de estudos na indústria privada, o fator **Dominance** (sensação de controle sobre a tarefa) mostrou-se estatisticamente relevante e positivamente correlacionado à produtividade no setor público [8, 11].
- **Intervenções Físicas**: Fatores biológicos como cansaço e fome foram os principais gatilhos para variações negativas na produtividade durante os experimentos [12, 13].

---

## Desafios do Uso das Metricas

- **Percepção Individual**: A mensuração de aspectos humanos é complexa devido ao caráter subjetivo de cada participante [14].
- **Viés de Resposta**: Risco de os participantes não informarem baixa produtividade por se sentirem observados (embora mitigado pelo acompanhamento individual) [15].
- **Outliers**: Dificuldade de alguns participantes em compreender o instrumento visual (SAM), resultando em respostas repetitivas que precisaram ser descartadas [16].

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

- **Tamanho da Amostra**: Redução do número planejado de 15 para 11 participantes devido a atrasos e falta de engajamento da gestão [17].
- **Tempo de Observação**: As sessões de medição foram limitadas a 2 horas por participante [18, 19].
- **Subjetividade**: Dependência total da autoavaliação do desenvolvedor quanto ao seu desempenho [15].

---

## Contribuicao Principal

A principal contribuição é a validação de que o bem-estar afetivo (satisfação e motivação) e a sensação de domínio técnico impactam diretamente a produtividade de desenvolvedores no contexto específico do serviço público municipal [1, 8, 17]. O estudo destaca que, neste ambiente, a percepção de competência (Dominance) é um fator de produtividade mais crítico do que na indústria privada ou academia [8].

---

*Extraido via NotebookLM em March 2026 para MLR: Software Developer Metrics in Practice*
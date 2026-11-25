# P0478 — Developers in focus! Developer Experience Analysis in a Collaborative Modeling Tool

**Decisao: INCLUIDO | Qualidade: 4/5**

---

## Dados Bibliograficos

| Campo | Valor |
|-------|-------|
| **ID** | P0478 |
| **Autores** | Miguel Silva, Ligia Teixeira, Afonso Silva, Genildo Gomes, Leonardo Barreto, Bruno Gadelha, Tayana Conte |
| **Ano** | 2022 |
| **Venue** | SBES 2022 (XXXVI Brazilian Symposium on Software Engineering) |
| **Tipo** | Artigo de Pesquisa (Empirical Study) |
| **Metodo** | Estudo misto qualitativo-quantitativo com escalas (DEXI, IMI) e Grupo Focal |
| **Amostra** | 20 participantes (estudantes em disciplina) |
| **Contexto** | Engenharia de Software - Educação e Ferramentas de Modelagem |

---

## Objetivo

O trabalho investigou como a experiência do desenvolvedor varia quando utilizando uma ferramenta de modelagem colaborativa (Glify UML), especificamente analisando fatores que afetam a experiência em diferentes estágios do processo de desenvolvimento. O objetivo principal é identificar e entender fatores-chave que impactam na experiência dos desenvolvedores ao utilizar ferramentas de modelagem em ambientes colaborativos, com foco em compreender perspectivas cognitivas, afetivas e conativas.

---

## Questoes de Pesquisa

- **RQ1**: Quais são os principais fatores que afetam a experiência do desenvolvedor ao usar ferramentas de modelagem colaborativa?
- **RQ2**: Como a experiência varia entre diferentes atividades e estágios do projeto?
- **RQ3**: Qual é o impacto de aspectos colaborativos na experiência geral?

---

## Dados da Pesquisa

### Amostra
- 20 participantes (estudantes de computação)
- Disciplina de Análise e Projeto de Sistemas
- Período: 6 semanas de uso da ferramenta

### Fonte de Dados
- Escala DEXI (12 itens com escala semântica de 7 níveis)
- Inventário de Motivação Intrínseca (IMI) com 8 itens
- Grupo Focal com discussão temática
- Observação de atividades

### Metodos de Coleta
- Questionários com escalas validadas (DEXI, IMI)
- Entrevistas em grupo focal com análise de Grounded Theory
- Observação participante durante uso da ferramenta
- Análise de diagramas produzidos

### Periodo de Analise
- Estudos executados em 2022
- Período de 6 semanas de disciplina

---

## Metricas e Instrumentos de Avaliacao

**Escala DEXI**: Escala com 12 pares de palavras (DEXI-H hedônico, DEXI-P pragmático) medindo experiência em 7 níveis de diferencial semântico:
- Recomendável/Não Recomendável
- Eficiente/Ineficiente
- Flexível/Inflexível
- Fácil de aprender/Difícil de aprender
- Limitado/Extensivo
- Não informativo/Informativo
- Desmotivador/Motivador

**Inventário de Motivação Intrínseca (IMI)**: 8 questões sobre interesse/prazer, competência percebida, esforço/importância, percepção de escolha, e value/utilidade

**Grounded Theory**: Análise temática qualitativa para identificação de código, categorias e conceitos relacionados à experiência

**Análise de Diagramas**: Avaliação da qualidade dos artefatos criados (fluxogramas, mapas mentais, diagramas UML)

---

## Resultados Principais

Análise DEXI revelou experiência geral neutra (média 0.31 em escala -4 a +4), indicando percepção pouco motivadora dos participantes com a ferramenta.

**Resultados IMI**: Qualidade pragmática (3.95) > Qualidade hedônica (3.15), sugerindo ferramenta com boas funcionalidades mas falta de atratividade.

**Grupo Focal** identificou sete misalignments principais:
1. Tool-task misalignment (ferramenta não suporta tipo de conversação necessária)
2. Tool-information misalignment (informação necessária não estava disponível na ferramenta)
3. Tool-size misalignment (tamanho de mudanças inadequado para review)
4. Process-completion misalignment (tempo estimado vs real para completar tarefas)
5. Developer-automation misalignment (nível de automação não correspondia às expectativas)
6. Developer-experience misalignment (expectativas vs experiência real divergiram)
7. Organizational factors (características organizacionais impactaram experiência)

---

## Desafios do Uso das Metricas

1. Amostra pequena limitada a contexto acadêmico: 20 estudantes em uma disciplina podem não representar desenvolvedores profissionais e contextos de produção

2. Dependência de instrumentos validados mas potencialmente insensíveis a aspectos específicos de ferramentas de modelagem colaborativa

3. Análise qualitativa baseada em Grounded Theory pode conter viés do pesquisador na interpretação dos dados

4. Período curto de observação (6 semanas) pode não capturar evolução completa da experiência ao longo do tempo

5. Contexto educacional difere significativamente de ambiente profissional, afetando generalização

---

## Avaliacao de Qualidade

| Criterio | Pontuacao (0-2) |
|----------|----------------|
| Objetivo claramente definido | 2 |
| Metodologia adequada | 2 |
| Amostra/contexto descrito | 1 |
| Ameacas a validade discutidas | 1 |
| Resultados com evidencia | 2 |
| Contribuicao clara | 2 |
| **TOTAL** | **10/12** |

---

## Limitacoes

1. Amostra pequena (20 participantes) e limitada a contexto educacional
2. Participantes eram estudantes, não desenvolvedores profissionais com experiência em projetos grandes
3. Período de análise curto (6 semanas) para avaliação completa de experiência
4. Ferramenta específica (Glify UML) limita generalização para outras ferramentas
5. Análise qualitativa baseada em um único grupo focal
6. Falta de grupo de controle ou comparação com outras ferramentas

---

## Contribuicao Principal

O trabalho contribui com análise estruturada da experiência do desenvolvedor em ferramentas de modelagem colaborativa, identificando sete principais misalignments que afetam a experiência. Especificamente, revela que a qualidade pragmática (funcionalidade) é percebida como superior à qualidade hedônica (atratividade), sugerindo que ferramentas de modelagem precisam melhorar aspectos de usabilidade e engajamento além de pura funcionalidade. A análise qualitativa de Grounded Theory fornece direções práticas para design de ferramentas colaborativas mais alinhadas com necessidades reais dos desenvolvedores, enfatizando importância de considerar alinhamento entre tarefa, ferramenta, processo e expectativas do usuário.

---

*Extraido em Marco 2026 para MLR: Software Developer Metrics in Practice*

# G072: Mean Time to WTF - Developer Experience Frameworks in Incident Retrospectives

## Dados Bibliograficos
- **ID da Grey Literature**: G072
- **Titulo**: Mean Time to WTF: Why Developer Experience Frameworks Belong in Your Incident Retrospectives
- **Autor**: Nicole Forsgren
- **Tipo de Publicacao**: Apresentação em Conferência (SREcon26 Americas)
- **Ano**: 2026
- **Tipo de Evento**: Conferência SREcon (Site Reliability Engineering Conference)
- **URL**: https://www.usenix.org/conference/srecon26americas/presentation/forsgren
- **Data de Acesso**: 2026-03-08

## Objetivo
Argumentar pela integração de frameworks de Developer Experience (DevEx) em processos de retrospectiva de incidentes. A apresentação propõe que fricção do desenvolvedor contribui para ocorrência de incidentes e tempo de recuperação, e deve ser analisada sistematicamente em retrospectivas.

## Questoes de Pesquisa
- RQ1: Como fricção do desenvolvedor contribui para incidência de falhas/incidentes?
- RQ2: Qual é o papel de DevEx no tempo de recuperação de incidentes?
- RQ3: Como incorporar avaliação de DevEx em retrospectivas de incidentes?
- RQ4: Quais frameworks de DevEx são mais aplicáveis a incidentes?

## Frameworks e Metricas
**Frameworks Identificados**:
- Developer Experience (DevEx) Frameworks
- Incident Retrospective Framework
- Fricção do Desenvolvedor (construto)

**Construtos de Interesse**:
- Developer Friction (fricção, obstáculos, complexidade)
- Incident Causation (papel de DevEx)
- Mean Time to WTF (tempo até reconhecimento de problema)
- Recovery Time (tempo de recuperação)

**Dimensões de DevEx Consideradas**:
- Satisfação e moral
- Clareza de objetivos e requisitos
- Simplicidade de ferramentas e processos
- Qualidade de documentação
- Usabilidade de infraestrutura

**Métricas Propostas/Discutidas**:
- Métricas qualitativas de fricção
- Tempo de recuperação (MTTR)
- Satisfação em retrospectiva
- Avaliação de barreiras técnicas

## Principais Contribuicoes
- Proposição de conexão explícita entre DevEx e ocorrência/severidade de incidentes
- Argumentação para inclusão de análise de DevEx em retrospectivas de incidentes
- Framework para avaliar contribuição de fricção do desenvolvedor em falhas
- Diretrizes para melhoria de DevEx baseada em análise de incidentes
- Perspectiva nova em cultura de blameless retrospectives

## Resultados
- Demonstração de relação entre fricção e incidentes
- Identificação de padrões de DevEx em contextos de falha
- Argumentação evidenciada para mudança em práticas de retrospectiva
- Reconhecimento de DevEx como fator crítico em confiabilidade
- Recomendações para integração de DevEx em SRE practice

## Contribuicao Principal
Conecta Developer Experience frameworks a incident response practice através do conceito de "Mean Time to WTF", argumentando que fricção do desenvolvedor é fator crítico em causação e severidade de incidentes que deve ser explicitamente analisado em retrospectivas.

---

## Criterios de Inclusao/Exclusao

**Decisao**: **INCLUIDO**

**Justificativa**:
- EC1 ✓ Tema relevante: Foca em Developer Experience como fator em confiabilidade e incidentes
- EC2 ~ Escopo parcialmente adequado: Enquanto trata de DevEx, foco é em incidentes/SRE, não exclusivamente em avaliação de performance/experiência
- EC3 ~ Qualidade: Apresentação de conferência credível (SREcon), mas sem detalhes de metodologia (abstract page only)
- EC4 ✓ Público-alvo correto: Desenvolvedores como sujeitos de fricção e afetados
- EC5 ✓ Grey literature tier: Apresentação de conferência (2o tier) - fonte credível
- EC6 ✓ Cobertura temporal: 2026 - muito recente e prospectivo

**Qualidade**: 3/5 (Nota: Qualidade reduzida porque apenas abstract está disponível, não texto completo)

**Observacao**: Incluído por relevância temática a frameworks de DevEx, mas com qualidade média devido a limitações de conteúdo disponível (apenas abstract de conferência).

**Frameworks Identificados**: Developer Experience Framework, Incident Retrospective Framework, Fricção do Desenvolvedor

**Métricas Identificadas**: Mean Time to WTF, MTTR, Satisfação, Fricção Qualitativa, Tempo de Recuperação, Barreiras Técnicas

**Tipo**: Apresentação de Conferência / Proposta Conceitual

**Método**: Argumentação conceitual baseada em experiência prática

**Amostra**: N/A (apresentação conceitual) - implementações esperadas em práticas SRE

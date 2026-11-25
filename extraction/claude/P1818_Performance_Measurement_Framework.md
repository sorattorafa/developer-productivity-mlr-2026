# P1818 — Performance Measurement Framework for Agile Scrum Software Engineering Environment

**Decisao: INCLUIDO | Qualidade: 4/5**

---

## Dados Bibliograficos

| Campo | Valor |
|-------|-------|
| **ID** | P1818 |
| **Autores** | Deepa T., Dr. Thaddeus S., Dr. Dhamodharan G. |
| **Ano** | 2023 |
| **Venue** | International Journal of Intelligent Systems and Applications in Engineering (IJISAE) |
| **Tipo** | Artigo de pesquisa empírica |
| **Metodo** | Estudo de caso com análise computacional |
| **Amostra** | 10 projetos de software, 12 sprints cada, 2 organizações |
| **Contexto** | Ambientes Agile Scrum em desenvolvimento de software |

---

## Objetivo

Este artigo propõe um framework aprimorado para mensuração de desempenho em ambientes Agile Scrum, focando na medição de produtividade individual e coletiva dos desenvolvedores. O objetivo é superar as limitações das métricas tradicionais de Scrum (como velocidade e gráficos de burndown) através da introdução de análises de Earned Value e métricas de qualidade de código baseadas em Índice de Manutenibilidade de Código.

O framework busca fornecer insights valiosos sobre dinâmica de equipes, oportunidades de melhoria e o impacto de retrabalhos na produtividade e qualidade geral do software desenvolvido, permitindo gestão mais eficaz do desenvolvimento ágil.

---

## Questoes de Pesquisa

- **RQ1**: Como medir com precisão a produtividade individual e coletiva de desenvolvedores em ambientes Agile Scrum?
- **RQ2**: De que forma a análise de Earned Value baseada em Productivity Ratio e métricas de qualidade de código podem complementar métricas tradicionais de Scrum?
- **RQ3**: Como o acompanhamento de retrabalhos afeta estimativas de produtividade e proporciona insights para melhorias futuras?

---

## Dados da Pesquisa

### Amostra

- 10 projetos de software distintos
- Dois períodos de coleta: Projeto 1-5 de uma organização (A), Projeto 6-10 de outra (B)
- 12 sprints analisados por projeto, totalizando 18 meses de coleta de dados
- Tamanhos de equipes variando de 2 a 8 membros
- Tecnologias diversas: Dot Net, Python, PHP, Angular JS, React JS

### Fonte de Dados

- Histórico de requisitos de usuários (user stories)
- Pontos de história (story points) planejados e realizados
- Feedback de cliente após Testes de Aceitação do Usuário (UAT)
- Logs de sprints
- Métricas de código geradas por ferramentas de análise estática (SonarQube)

### Metodos de Coleta

- Coleta de métricas de Earned Value (EV) após cada sprint
- Re-avaliação de EV baseada em feedback de cliente
- Rastreamento de retrabalhos através do histórico de requisições revisadas
- Análise de Índice de Manutenibilidade de Código (CMI)
- Cálculo de Defect Density e Test Coverage através de ferramentas automatizadas

### Periodo de Analise

- Período de coleta: até 18 meses por projeto
- Análise de 12 sprints para cada projeto
- Intervalo de aproximadamente 3 meses por sprint (aproximadamente 18 meses totais)

---

## Metricas e Instrumentos de Avaliacao

### Métricas de Esforço (Effort Metrics)

- **Team Velocity**: quantidade de trabalho que uma equipe consegue realizar em um sprint
- **Sprint Burndown**: trabalho remanescente em um sprint ao longo do tempo
- **Release Burndown**: progresso em relação à conclusão de um lançamento de produto
- **Número de Histórias**: contagem de histórias de usuário completadas em um período específico
- **Work in Progress (WIP)**: número de tarefas/projetos em andamento mas não concluídos

### Métricas de Dinâmica de Equipe (Team Dynamics Metrics)

- **Team Satisfaction**: medida geral de felicidade e moral da equipe
- **Team Member Turnover**: taxa de saída de membros da equipe em um período

### Métricas de Eficiência (Efficiency Metrics)

- **Lead Time**: tempo total desde requisição de uma tarefa até sua conclusão
- **Cycle Time**: tempo total do início ao fim de um processo, incluindo tempo de processo, atraso e inspeção

### Métricas de Impacto de Negócio (Business Impact Metrics)

- **Business Value Delivered**: valor total ou benefícios de um projeto concluído para o negócio
- **Sprint Goal Success**: se a equipe conseguiu atingir objetivos predefinidos do sprint
- **Total Project Duration**: tempo total desde início até conclusão de um projeto
- **Time to Market**: tempo desde concepção de uma ideia até lançamento oficial
- **Total Product Cost**: custos totais envolvidos no desenvolvimento, produção e manutenção

### Métricas de Retorno (Return/Qualidade)

- **Return on Investment (ROI)**: lucro líquido dividido pelo custo total do investimento
- **Standard Violation**: não-aderência a diretrizes, convenções ou melhores práticas
- **Defects per Interaction**: número médio de erros encontrados por interação
- **Defect Density**: número de defeitos confirmados por unidade de tamanho do software
- **Failed Deployments**: contagem de implementações de software não bem-sucedidas
- **Number of Tests**: contagem de casos de teste projetados e executados em um período

### Análise de Earned Value (EVA)

**Earned Value Inicial (EV após UAT e release)**:
$$\text{Initial EV} = \sum_{i=1}^{n} SP_i$$

Onde SP_i são os Story Points de histórias de usuário completadas.

**EV Re-avaliado (com retrabalhos)**:
$$\text{Re-evaluated EV} = \sum_{i=1}^{n} SP'_i$$

Onde SP'_i são os Story Points revistos baseados em feedback de cliente.

**Mudança em EV**:
$$\text{Change in EV} = \text{Re-evaluated EV} - \text{Initial EV}$$

**EV Ratio (Productivity Ratio)**:
$$\text{EV Ratio} = \frac{\text{Re-evaluated EV}}{\text{Initial EV}}$$

### Blended Quality Metric (BQM) Baseada em Code Maintainability

**CMI Modificado** (excluindo Lines of Code - LoC):
$$\text{CMI'} = k \times (171 - 5.2 \times \log 2(V) - 0.23 \times (G) - 16.2 \times \log 2(\text{LoC}))$$

Onde:
- k é fator de escalonamento para manter valores entre 0-100
- V é Volume de Halstead
- G é Complexidade Ciclomática

**BQM Final**:
$$\text{BQM} = 0.4 \times \text{CMI'} + 0.3 \times \text{Defect Density} + 0.3 \times \text{Test Coverage}$$

Os componentes são ponderados em razão 4:3:3, respectivamente.

---

## Resultados Principais

### Análise de Earned Value

1. **Impacto de Retrabalhos**: A análise de 10 projetos revelou variações significativas entre EV inicial e re-avaliado. Projetos mostraram reduções notáveis (exemplo: Projeto 3 de 1870 para 1270, Projeto 4 de 2100 para 1500), indicando retrabalhos devido a má interpretação de requisitos ou testes insuficientes.

2. **Padrão de Efeito Ripple**: Algumas histórias de usuário causaram retrabalhos em múltiplos sprints subsequentes. Por exemplo, a história "MSB OPD Reg 05" começou com 12 Story Points no Sprint 1, precisou revisão no Sprint 2 (6 SP) e causou impactos em Sprints 3 e 4.

3. **Variação Across Sprints**: O gráfico de tendência mostrou padrões consistentes de queda do EV re-avaliado em relação ao inicial, sugerindo problemas sistemáticos em práticas de estimação ou execução.

4. **Comparação entre Projetos**: Projeto 4 mostrou a maior discrepância (2100 para 1500), enquanto Projeto 10 mostrou menor impacto (1457 para 958), indicando variabilidade nas práticas de qualidade entre organizações.

### Análise de Produtividade Individual

1. **Variações entre Desenvolvedores**: A análise de 3 desenvolvedores (A, B, C) mostrou padrões distintos:
   - Developer A: EV inicial de 77 para 71 no Sprint 1, com flutuações até 128 no Sprint 10
   - Developer B: Padrões mais estáveis, com EV remanescente consistente
   - Developer C: Variações significativas sugerindo diferenças em experiência ou especialização

2. **Impacto da Experiência**: Developer A (2 anos 7 meses) mostrou maior variabilidade do que Developer B (5 anos 8 meses), sugerindo que experiência influencia consistência de produtividade.

### Eficácia de BQM-CMI

1. **Correlação com Defects**: A análise de correlação entre BQM e número de defeitos pós-release mostrou correlação negativa forte (-0.98 para Projeto 5), indicando que altos valores de BQM (melhor qualidade) associam-se com menores números de defeitos.

2. **Propriedades Preditivas**: BQM demonstrou capacidade de servir como indicador preditivo de qualidade durante a fase de desenvolvimento, com potencial de reduzir defeitos após lançamento.

3. **Variações Entre Sprints**: Os valores de BQM variaram de 63.99 a 97.98 (escala 0-100), fornecendo granularidade útil para avaliação de qualidade.

---

## Desafios do Uso das Metricas

1. **Complexidade na Interpretação de Requisitos**: A principal causa de retrabalhos foi má interpretação de requisitos por desenvolvedores, levando a divergências significativas entre EV planejado e realizado.

2. **Linearidade do Burndown Chart**: Gráficos de burndown assumem progressão linear de trabalho, o que não reflete adequadamente desafios reais ou mudanças de requisitos, tornando a métrica limitada.

3. **Falta de Granularidade do Velocity**: Velocity não considera complexidade ou escopo de histórias individuais, falhando em capturar efetivamente contribuições de trabalho específicas.

4. **Defects per Interaction**: Esta métrica não considera severidade ou complexidade de defeitos, apenas contagem numérica, potencialmente negligenciando qualidade real do testing.

5. **Medição Incompleta de Testes**: Number of Tests mede quantidade de testes, não qualidade ou eficácia da bateria de testes em relação à cobertura real.

6. **Inadequação para Avaliação Individual**: Métricas tradicionais de Scrum frequentemente focam em nível de equipe, dificultando avaliação precisa de contribuições individuais.

7. **Variabilidade em Definições**: Diferentes organizações definem termos como "produtividade" de formas distintas, dificultando comparação entre contextos.

8. **Risco de LoC em CMI**: Mesmo com exclusão de LoC do CMI, bases de código maiores inerentemente tendem a ser mais difíceis de manter, influenciando resultados.

9. **Dados de Correlação Limitados**: Correlação entre BQM e defeitos foi calculada para um único projeto em profundidade; validação em escala maior seria necessária.

10. **Dependência de Feedback de Cliente**: A re-avaliação de EV depende de feedback oportuno e preciso do cliente, que pode variar em qualidade e frequência.

---

## Avaliacao de Qualidade

| Criterio | Pontuacao (0-2) |
|----------|----------------|
| Objetivo claramente definido | 2 |
| Metodologia adequada | 2 |
| Amostra/contexto descrito | 2 |
| Ameacas a validade discutidas | 1 |
| Resultados com evidencia | 2 |
| Contribuicao clara | 2 |
| **TOTAL** | **11/12** |

---

## Limitacoes

1. **Escopo Limitado de Organizações**: Apenas 2 organizações participaram, limitando generalização dos achados para contextos diferentes.

2. **Tamanho Variável de Equipes**: Variação entre 2 e 8 membros de equipe, dificultando isolamento de fatores específicos de escala.

3. **Período Fixo de Coleta**: Análise limitada a 18 meses; comportamentos de longo prazo ou sazonais não foram investigados.

4. **Tecnologias Específicas**: Projetos usaram tecnologias distintas (Dot Net, Python, PHP, etc.), confundindo potencialmente resultados com características específicas de linguagem.

5. **Falta de Grupo de Controle**: Estudo de caso sem grupo de controle comparativo; não há baseline para avaliar efetividade relativa de métricas propostas.

6. **Validação Limitada de BQM**: A correlação de BQM com defeitos foi demonstrada para um projeto; validação em escala maior está pendente.

7. **Dependência de Dados Manuais**: Coleta de dados de retrabalho e feedback de cliente pode estar sujeita a viés de registro ou interpretação.

8. **Ausência de Análise Qualitativa**: Estudo focado em dados quantitativos; perspectivas qualitativas de desenvolvedores sobre desafios não foram coletadas.

9. **Ferramentas de Análise de Código**: SonarQube foi ferramenta exclusiva; resultados podem variar com outras ferramentas de análise estática.

10. **Fatores Contextuais Não Controlados**: Variáveis como pressão de prazo, mudanças de requisito ou fatores organizacionais não foram sistematicamente controladas.

---

## Contribuicao Principal

O artigo contribui com um framework integrado que combina análise de Earned Value com métricas de qualidade de código para fornecer visão abrangente de desempenho em ambientes Agile Scrum. A introdução do "EV Ratio" baseado em re-avaliação com feedback de cliente proporciona mecanismo realista para capturar impacto de retrabalhos na produtividade, indo além de métricas tradicionais que frequentemente ignoram esse aspecto crítico.

A proposição da Blended Quality Metric (BQM) baseada em Code Maintainability Index, Defect Density e Test Coverage oferece indicador preditivo potente de qualidade durante desenvolvimento, com correlação demonstrada a defeitos pós-release. O framework fornece insights acionáveis sobre dinâmica de equipe, variações de produtividade individual e a necessidade de melhorias em práticas de estimação e testes, contribuindo para melhor gestão da qualidade e produtividade em projetos Agile.

---

*Extraido em Marco 2026 para MLR: Software Developer Metrics in Practice*

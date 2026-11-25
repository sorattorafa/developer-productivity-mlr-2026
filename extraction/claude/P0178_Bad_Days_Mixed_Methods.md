# P0178 — Identifying Factors Contributing to "Bad Days" for Software Developers: A Mixed-Methods Study

**Decisao: INCLUIDO | Qualidade: 4/5**

---

## Dados Bibliograficos

| Campo | Valor |
|-------|-------|
| **ID** | P0178 |
| **Autores** | Ike Obi, Jenna Butler, Sankeerti Haniyur, Brian Hassan, Margaret-Anne Storey, Brendan Murphy |
| **Ano** | 2025 |
| **Venue** | ICSE-SEIP 2025 (47th International Conference on Software Engineering: Software Engineering in Practice) |
| **DOI** | 10.1109/ICSE-SEIP66354.2025.00006 |
| **Tipo** | Estudo Empírico - Abordagem Mista (Qualitativo + Quantitativo) |
| **Metodo** | Triangulação: Entrevistas (n=22), Levantamento (n=214), Diário Estruturado (n=79), Análise de Telemetria (n=131 desenvolvedores) |
| **Amostra** | 22 entrevistados, 214 respondentes de levantamento, 79 participantes diário, 131 participantes telemetria; organizações Microsoft e outras |
| **Contexto** | Indústria de software; ambientes corporativos com diversos times e processos |
| **Modo de trabalho** | Presencial/Remoto/Híbrido |

---

## Objetivo
Investigar e caracterizar fatores que causam "dias ruins" (bad days) para desenvolvedores de software, compreendendo como esses fatores afetam sua experiência, produtividade e bem-estar, utilizando múltiplas perspectivas e métodos de coleta de dados.

---

## Questoes de Pesquisa
- **RQ1**: Que fatores causam "dias ruins" para desenvolvedores?
- **RQ2**: De que maneiras os desenvolvedores descrevem como fatores de "dias ruins" impactam seu trabalho e bem-estar?
- **RQ3**: Podemos observar fatores de "dias ruins" usando dados de telemetria?

---

## Metricas e Instrumentos de Avaliacao
- **Entrevistas semi-estruturadas**: 30-60 minutos, gravadas e transcritas; exploração de 4 áreas: definição de "bad day", exemplos recentes, frequência, fatores contribuintes
- **Levantamento**: Questões Likert sobre cenários específicos (long build times, pull requests lentos, reuniões excessivas, etc.)
- **Diário Estruturado**: Coleta diária por 30 dias de informações sobre experiência de "bad days"
- **Análise de Telemetria**: Coleta de dados de sistema (pull request time, build time, meeting hours, incident reports)
- **Codificação Temática**: Análise qualitativa com codificação aberta, axial e seletiva
- **Análise Estatística**: Testes t, análise de frequência, análise de correlação entre dados de telemetria e auto-relato

---

## Resultados Principais
- **Fatores Principais Identificados** (RQ1):
  1. **Tooling and Infrastructure Issues** (mean score 4.22): Ferramentas não confiáveis, interfaces clunky, compilações quebradas
  2. **Process Inefficiencies** (3.72): Processos ineficientes, impedimentos não resolvidos, comunicação deficiente
  3. **Team Dynamics Issues** (3.56): Conflito intra-equipe, falta de suporte, dinâmica interpessoal
  4. **Other technical blockers** (mean scores 3.20-3.90): Debugging, documentação inadequada, conhecimento insuficiente

- **Impacto na Experiência** (RQ2): "Bad days" causam frustração, desânimo, perda de confiança; afetam bem-estar pessoal e dificultam foco no trabalho
- **Validação de Telemetria** (RQ3): Pull request time e build time correlacionaram significativamente com relatos de "bad days"
  - Pull request time mean: 47.41 min (Group 1) vs. 36.09 min (Group 2); p=0.00
  - Build time total: 49.74 min (Group 1) vs. 36.65 min (Group 2); p=0.00

- **Frequência**: 97% reportaram "bad day" no último mês; distribuição próxima a normal
- **Diferenças por Nível**: Desenvolvedores Senior/Principal reportam maior frequência de "bad days" relacionados a meetings; Junior/Developers I reportam mais frustração técnica

---

## Desafios do Uso das Metricas
- **Validade de Conteúdo**: Termo "bad day" é subjetivo; definição varia entre indivíduos e contextos
- **Viés de Resposta**: Levantamento voluntário pode atrair respondentes com experiências negativas
- **Representatividade Amostral**: Amostra concentrada em Microsoft; resultados podem não generalizar para organizações menores ou diferentes contextos
- **Sincronização Temporal**: Dificuldade em correlacionar exatamente dados de telemetria com períodos específicos de "bad days" reportados
- **Qualidade de Dados de Telemetria**: Nem todos os fatores de "bad days" deixam rastros mensuráveis em telemetria; comportamento contextual pode não ser capturado
- **Privacidade**: Coleta de dados de telemetria levanta questões éticas e de privacidade; dados mantidos anônimos

---

## Contribuicao Principal
O estudo fornece investigação abrangente e multi-perspectiva dos fatores que causam "dias ruins" para desenvolvedores de software, identificando que problemas de tooling/infrastructure, ineficiências de processo e dinâmica de equipe são fatores principais. Crucialmente, o estudo valida alguns fatores através de dados de telemetria objetivos, estabelecendo que certos bloqueadores técnicos mensuráveis (build time, pull request time) correlacionam com experiências negativas reportadas. Os resultados informam estratégias organizacionais para melhorar experiência e produtividade de desenvolvedores através da abordagem de problemas infraestruturais, processuais e interpessoais.

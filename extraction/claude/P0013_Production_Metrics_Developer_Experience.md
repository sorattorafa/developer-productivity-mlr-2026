# P0013 — Supporting the Developer Experience with Production Metrics

**Decisao: INCLUIDO | Qualidade: 3/5**

---

## Dados Bibliograficos

| Campo | Valor |
|-------|-------|
| **ID** | P0013 |
| **Autores** | Robert Chatley |
| **Ano** | 2019 |
| **Venue** | 2019 IEEE/ACM Joint 4th International Workshop on Rapid Continuous Software Engineering and 1st International Workshop on Data-Driven Decisions, Experimentation and Evolution (RCoSE/DDrEE) |
| **DOI** | 10.1109/RCoSE-DDrEE.2019.00009 |
| **Tipo** | Artigo de posicionamento e roadmap de pesquisa |
| **Metodo** | Análise de problemas práticos; proposição de arquitetura de sistema |
| **Amostra** | Não aplicável (posicionamento teórico) |
| **Contexto** | Aplicações web de alta trafego em ambientes de engenharia contínua |
| **Modo de trabalho** | Análise de ferramentas APM (Application Performance Management) existentes |

---

## Objetivo
Explorar como dados de produção coletados por ferramentas de APM podem ser integrados em ambientes de desenvolvimento para apresentar informações sobre comportamento de código em produção de forma contextualizada e acionável aos desenvolvedores.

---

## Questoes de Pesquisa
- **RQ1**: Como apresentar dados de produção de forma contextualizada dentro do IDE do desenvolvedor?
- **RQ2**: Que tipos de informações de produção são mais relevantes para tomada de decisão?
- **RQ3**: Como rastrear mudanças através do pipeline de build e deployment?

---

## Metricas e Instrumentos de Avaliacao
- **Métricas de Rastreamento de Execução**: Caminhos de execução, branches mais "quentes", frequência de execução
- **Métricas de Exceção**: Frequência de exceções por linha/método, padrões de erros
- **Métricas de Deployment**: Versão atual em cada ambiente, progressão através do pipeline
- **APM Tools**: NewRelic, PyFlame, Google Profilers para coleta contínua
- **Instrumentação**: Modificação de bibliotecas de teste para enviar dados em tempo real
- **IDE Plugins**: Para visualização de dados sobre código (destacamento de branches, tooltips)

---

## Resultados Principais
- Identificação de três cenários problemáticos principais onde dados de produção beneficiariam desenvolvedores:
  1. **Exposição de traços de execução**: Mismatch entre modelo mental e comportamento real
  2. **Relato de exceções**: Problemas descobertos em produção não comunicados efetivamente a desenvolvedores
  3. **Rastreamento de deployment**: Falta de clareza sobre qual código está em qual ambiente
- Proposta de integração entre pipeline de build, sistema de versionamento e plataforma de métricas
- Identificação de desafios técnicos críticos em correlação de dados através de versões

---

## Desafios do Uso das Metricas
- **Rastreamento de mudanças**: Tempo entre commit e produção pode variar de minutos a semanas
- **Redução de dados**: Com alta frequência de deployment, dados por versão individual pode ser limitado
- **Coleta de dados**: Profiling com granularidade suficiente (ex: quale branch é tomado) pode introduzir overhead
- **Agregação de dados**: Necessidade de escolher entre reportar valores atuais vs. deltas (mudanças)
- **Integração técnica**: Desafio de integrar múltiplas ferramentas heterogêneas
- **Representatividade**: Avaliar efetividade das ferramentas requer acesso a sistemas reais e dados representativos

---

## Contribuicao Principal
Propõe uma abordagem inovadora para melhorar developer experience através de integração de dados de produção em tempo real dentro do IDE, apresentando roadmap de pesquisa para ferramentas que contextualizam dados de APM, integram com pipeline de build/deploy, e expõem informações de execução, exceções e deployment de forma acionável aos desenvolvedores.

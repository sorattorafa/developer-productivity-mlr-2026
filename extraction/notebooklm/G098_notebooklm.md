# G098 — Balancing AI tensions

**Decisao: INCLUIDO | Qualidade GL: 5.5/6**

---

## Dados Bibliograficos

| Campo | Valor |
|-------|-------|
| **ID** | G098 |
| **Autor/Organizacao** | Jessica Baolin, Nathen Harvey / DORA (Google) |
| **Data** | March 10, 2026 |
| **Tipo** | Blog post / Practitioner guide (DORA Insights) |
| **URL** | https://dora.dev/insights/balancing-ai-tensions/ |

---

## Resumo

O artigo analisa o impacto da adocao de AI no ciclo de vida de desenvolvimento de software (SDLC), fundamentando-se em uma analise qualitativa temática de **1.110 respostas de engenheiros de software do Google** no Q3 de 2025 e nos dados do **2025 DORA State of AI-assisted Software Development report** (que aponta 90% de uso de AI e mais de 80% de aumento percebido em produtividade). O texto enfatiza que a AI atua primariamente como um **amplificador**: ela potencializa organizacoes com plataformas internas solidas e boas praticas de engenharia, mas acelera a acumulacao de *technical debt* em equipes com ferramentas fragmentadas e infraestrutura fragil.

A analise identifica dez casos de uso principais (como *code generation*, *information seeking*, *code review* e *testing*) e revela que os ganhos de velocidade trazem compensacoes significativas (*tradeoffs*). O artigo estrutura essas compensacoes em tres tensoes centrais: (1) a atracao e repulsao na velocidade, onde a economia de tempo na escrita e drenada pela ***verification tax***, pelo *prompting overhead* e pelo aumento do *cognitive load* para revisores de codigo; (2) o ***expertise paradox***, no qual a reducao de barreiras de entrada pode contornar a *productive struggle* e resultar em *skill degradation* no longo prazo; e (3) o ***workflow gap***, no qual prototipagens rapidas no *inner loop* colidem com gargalos de integracao em producao no *outer loop*, cenario agravado pelo *tool sprawl*.

Para orientar liderancas e praticantes, os autores fornecem recomedacoes divididas em quatro eixos prioritarios: **medir impacto em vez de *output* bruto** (abandonando metricas estreitas como *lines of code accepted* em favor de *frameworks* holisticos), **adaptar os processos de *code review*** (deslocando automacoes de AI para o autor, adotando *review agents* e impondo o trabalho em *small batches*), **planejar a integracao em producao** (ajustando estimativas e integrando ferramentas a bases de dados proprietarias) e **proteger a expertise tecnica profunda** (combinando mentoria ativa e codificacao manual em sistemas complexos).

---

## Frameworks Mencionados

- **DORA / 2025 DORA State of AI-assisted Software Development report**: Discutido e utilizado extensivamente como base de dados e fundamentacao empirica para analisar a adocao de AI, entregas de software e estabilidade do sistema.
- **Speed, Ease, and Quality (SEQ)**: Mencionado e recomendado como o *framework* de indicadores internos utilizado pelo Google para avaliar a produtividade de desenvolvedores.
- **SPACE framework**: Mencionado e recomendado para estruturar um conjunto holistico de metricas de produtividade.
- **H.E.A.R.T. framework**: Mencionado e recomendado para alinhar equipes a experiencia dos usuarios com os produtos.
- **Value Stream Management (VSM)**: Discutido e recomendado para avaliar processos atuais e identificar gargalos no fluxo de entrega por meio de indicadores a jusante (*downstream indicators*).

---

## Metricas Mencionadas

- **Software delivery throughput**: Metrica do DORA associada positivamente a maior adocao de AI.
- **Software delivery instability**: Metrica do DORA apontada como crescente em organizacoes com alta adocao de AI, refletindo maior instabilidade nas entregas.
- **Lines of code accepted**: Metrica de *output* mencionada com ressalvas; e reconhecida como um indicador de adocao de ferramentas, mas **sua utilizacao como medida direta de produtividade e criticada**, pois a AI infla o volume de codigo gerado.
- **Code review turnaround time**: Mencionado no contexto de *Value Stream Management* (VSM) como indicador a jusante para identificar gargalos no processo de revisao.
- **Failed deployment recovery time**: Mencionado como indicador a jusante no VSM para avaliar resiliencia e tempo de recuperacao do sistema.
- **Deployment rework rate**: Mencionado como indicador a jusante no VSM para monitorar taxas de retrabalho em implantacoes.
- **Production incidents**: Mencionado como indicador a jusante no VSM para mensurar impactos em producao.
- **Speed, Ease, and Quality (SEQ)**: Conjunto de indicadores de produtividade de desenvolvedores utilizado no Google.
- **Taxa de adocao e produtividade percebida**: 90% dos profissionais de tecnologia utilizam AI no trabalho; mais de 80% acreditam na melhoria de produtividade (dados do relatorio DORA 2025).
- **Confianca no codigo gerado por AI**: 30% dos desenvolvedores relatam pouca ou nenhuma confianca no codigo gerado por AI (dados do relatorio DORA 2025).

---

## Insights para Praticantes

- **Medir impacto, nao apenas output (*Measure impact, not output*)**: Interromper o foco em metricas de volume (como *lines of code accepted*) e adotar *frameworks* holisticos (SEQ, SPACE, H.E.A.R.T., VSM) adaptados aos objetivos organizacionais.
- **Adaptar o processo de code review (*Adapt the code review process*)**:
  - Deslocar automacoes e feedback de AI para o autor durante a fase de escrita, corrigindo falhas antes que o codigo chegue ao revisor.
  - Construir *context-aware review agents* para validar padroes organizacionais de forma automatica.
  - Exigir o trabalho em *small batches* (pequenos lotes) para manter alteracoes geradas por AI testaveis e viaveis para revisao humana.
  - Questionar revisoes assincronas tradicionais e investir em automacao robusta de testes para acelerar o feedback.
- **Planejar para o workflow e o gap de integracao em producao**:
  - Ajustar estimativas de projetos para reconhecer a distancia entre a prototipagem rapida e o esforco necessario para qualidade de producao.
  - Conectar ferramentas de AI a bases de codigo proprietarias e documentacoes internas para superar os gargalos da "ultima milha".
  - Reduzir o *tool sprawl* para evitar fadiga de decisao e preservar o *flow state* dos engenheiros.
- **Proteger a expertise tecnica profunda (*Safeguard deep expertise*)**:
  - Combater o aprendizado superficial e a *skill degradation* pareando engenheiros juniores com mentores seniores no exame de decisoes arquiteturais de AI.
  - Incentivar a codificacao manual em componentes criticos para consolidar o entendimento fundamental e evitar cenarios de "cego guiando cego".
- **Compreender o papel da AI como amplificador (*AI as an amplifier*)**:
  - Reconhecer que a AI amplia tanto virtudes organizacionais (plataformas consolidadas, APIs claras, testes fortes) quanto disfuncoes pre-existentes.

---

## Avaliacao de Qualidade GL (Garousi et al.)

| Criterio | Pontuacao (0-1) |
|----------|----------------|
| Autoridade do autor/organizacao | 1.0 |
| Descricao de metodologia | 1.0 |
| Data de publicacao | 1.0 |
| Objetividade (vies comercial) | 0.5 |
| Referencias citadas | 1.0 |
| Contribuicao nova | 1.0 |
| **TOTAL** | **5.5/6** |

---

*Extraido via NotebookLM em October 2026 para MLR: Software Developer Metrics in Practice*

---

💡 Gostaria que eu elaborasse um relatório em PDF ou uma apresentação sintética comparando esta fonte com outros estudos da sua literatura sobre métricas de produtividade?
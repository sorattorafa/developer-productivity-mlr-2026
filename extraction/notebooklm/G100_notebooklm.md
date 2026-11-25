# G100 — AI measurement framework: Complete guide for engineering leaders

**Decisao: INCLUIDO | Qualidade GL: 4.5/6**

---

## Dados Bibliograficos

| Campo | Valor |
|-------|-------|
| **ID** | G100 |
| **Autor/Organizacao** | Taylor Bruneaux / DX [1] |
| **Data** | May 20, 2026 [2] |
| **Tipo** | Blog post / Guide [1] |
| **URL** | https://getdx.com/blog/ai-measurement-framework-guide/ [1] |

---

## Resumo

O artigo apresenta o *DX AI Measurement Framework*, um sistema estruturado e repetível projetado para acompanhar, interpretar e atuar sobre métricas de engenharia assistida por IA [3-5]. A estrutura organiza os sinais de medição em três dimensões principais — *utilization*, *impact* e *cost* — conectando-os às condições dos desenvolvedores, à performance da engenharia e aos resultados de negócios [3, 5, 6]. O texto ressalta que apenas rastrear taxas de adoção é insuficiente, pois ganhos locais de produtividade em nível individual não se traduzem automaticamente em melhores resultados organizacionais, podendo inclusive mascarar degradações de qualidade como o aumento no *change failure rate* [3, 7-9].

A abordagem de medição combina métricas diretas (como *AI-driven time savings* e *Developer satisfaction*) com métricas indiretas obtidas por meio do *DX Core 4* (como *PR throughput*, *code maintainability* e *Developer Experience Index*) [10-12]. Além disso, o guia traz diretrizes para medir *AI agents* — sugerindo avaliá-los como extensões das equipes que os supervisionam —, calcular o retorno financeiro via métricas de custo (*net time gain* e *agent hourly rate*) e lidar com desafios sistêmicos como o *shadow AI* e gargalos de processos humanos (*outer loop*) [13-17].

Por fim, o relatório destaca a importância de implementar essas métricas sem aplicá-las para avaliação individual de desempenho, alertando expressamente contra o risco de *gaming* e descumprimento malicioso (*malicious compliance*) [18-20]. Apoiado em dados de *benchmark* com mais de 4 milhões de amostras, o artigo indica que 93% dos desenvolvedores utilizam IA na indústria, com uma economia média de 3,9 horas semanais por desenvolvedor e 27,4% do código mesclado sendo gerado por IA [7, 8, 21]. Casos práticos como os da Booking.com (aumento de 16% no *throughput*) e da Intercom (economia de tempo de 41%) ilustram o impacto de uma medição unificada [22].

---

## Frameworks Mencionados

- **DX AI Measurement Framework**: Discutido e recomendado como a estrutura principal para organizar os sinais de engenharia assistida por IA nas dimensões de *utilization*, *impact* e *cost* [3, 5, 6].
- **DX Core 4**: Discutido e recomendado para medir a produtividade geral da engenharia em quatro dimensões (*speed*, *effectiveness*, *quality*, *business impact*) [23]. Funciona de forma complementar ao *AI Measurement Framework* para confirmar se o uso de IA está gerando melhorias reais [9, 23].
- **DORA Metrics**: Mencionado e comparado como um framework complementar que ajuda a confirmar se as entregas estão mais rápidas e se a qualidade e estabilidade estão sendo mantidas [9, 12].

---

## Metricas Mencionadas

- **Utilization Metrics**:
  - *AI tool usage (DAUs/WAUs)*: Mede o número de usuários ativos diários e semanais das ferramentas de IA [13].
  - *Percentage of PRs that are AI-assisted*: Percentual de pull requests que utilizam assistência de IA [13].
  - *Percentage of committed code that is AI-generated*: Proporção do código commitado que foi criado por IA (registrou média de 27,4% no relatório Q1 2026) [8, 13, 21].
  - *Tasks assigned to agents*: Quantidade de tarefas delegadas a agentes autônomos de IA [13, 24].

- **Impact Metrics (Direct)**:
  - *AI-driven time savings (developer hours/week)*: Horas economizadas semanalmente por desenvolvedor (média da indústria de 3,9 h/semana e 4,72 h/semana para usuários diários) [7, 10, 21].
  - *Developer satisfaction*: Mede a satisfação dos desenvolvedores em relação às ferramentas de IA [10].
  - *Human-equivalent hours (HEH)*: Horas equivalentes de trabalho humano realizadas por agentes [10, 24].

- **Impact Metrics (Indirect / DX Core 4)**:
  - *PR throughput*: Volume de pull requests mesclados; estudos longitudinais apontam ganho moderado de 10–15% ao longo de mais de um ano [11].
  - *Perceived rate of delivery*: Avaliação subjetiva sobre a velocidade de entrega do time [11].
  - *Developer Experience Index (DXI)*: Índice holístico de experiência e condições de trabalho do desenvolvedor [11].
  - *Code maintainability*: Grau de manutenibilidade do código produzido [11].
  - *Change confidence*: Nível de confiança da equipe na realização de mudanças [11].
  - *Change fail percentage / Change failure rate*: Percentual de falha em alterações; dados mostram variações de até 2 pontos percentuais (aumento de até 50% em defeitos em certas empresas) [8, 11].

- **Cost & ROI Metrics**:
  - *AI spend (total and per developer)*: Custos totais e individuais por desenvolvedor investidos em IA [14].
  - *Net time gain per developer*: Calculado como a economia de tempo gerada subtraída do custo de IA (*time savings minus AI spend*) [14].
  - *Agent hourly rate*: Custo por hora do agente, determinado pela divisão de *Human-equivalent hours* pelo custo total de IA (*HEH / AI spend*) [14, 24].

---

## Insights para Praticantes

- **Adoção isolada não garante ROI**: Focar unicamente em taxas de utilização é enganoso; alta adoção pode coexistir com menor qualidade de código e maior taxa de falhas (*change failure rate*) [3, 8, 9].
- **Combinar medição direta e indireta**: Métricas diretas informam o funcionamento da ferramenta, mas métricas indiretas de processo (*DX Core 4* e *DORA*) são indispensáveis para confirmar ganhos sustentáveis [9-11].
- **Tratar AI Agents como extensões das equipes**: Agentes autônomos devem ter seu desempenho integrado ao *throughput* do time do qual fazem parte, com o desenvolvedor atuando como líder/gestor desses agentes [16, 24].
- **Atentar para o Outer Loop e fatores humanos**: A IA otimiza o trabalho local, mas gargalos organizacionais (como excesso de reuniões e interrupções frequentes) geram custos que superam os ganhos de tempo fornecidos pela IA [15].
- **Evitar o uso de métricas para avaliação individual**: Nunca utilizar dados como volume de código gerado por IA para avaliar performance individual, pois isso induz a comportamento perverso (*gaming* e *malicious compliance*) e mina a confiança [18-20].
- **Considerar o Shadow AI**: Como parte dos desenvolvedores utiliza licenças pessoais de ferramentas de IA sem telemetria corporativa, é essencial estabelecer políticas de uso aceitável (*acceptable use policies*) e governança de dados [13].

---

## Avaliacao de Qualidade GL (Garousi et al.)

| Criterio | Pontuacao (0-1) |
|----------|----------------|
| Autoridade do autor/organizacao | 1.0 |
| Descricao de metodologia | 0.5 |
| Data de publicacao | 1.0 |
| Objetividade (vies comercial) | 0.5 |
| Referencias citadas | 0.5 |
| Contribuicao nova | 1.0 |
| **TOTAL** | **4.5/6** |

---

*Extraido via NotebookLM em October 2026 para MLR: Software Developer Metrics in Practice*

---

💡 Gostaria de consolidar esta extração com outras fontes da sua revisão da literatura ou gerar uma tabela comparativa com outros guias de medição de produtividade em engenharia?
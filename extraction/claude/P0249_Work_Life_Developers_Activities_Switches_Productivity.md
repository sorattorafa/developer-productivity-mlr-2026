# P0249 — The Work Life of Developers: Activities, Switches and Perceived Productivity

**Decisao: INCLUIDO | Qualidade: 4/5**

---

## Dados Bibliograficos

| Campo | Valor |
|-------|-------|
| **ID** | P0249 |
| **Autores** | André N. Meyer, Laura E. Barton, Gail C. Murphy, Thomas Zimmermann, Thomas Fritz |
| **Ano** | 2017 |
| **Venue** | IEEE Transactions on Software Engineering, Vol. 43, No. 12 |
| **DOI** | 10.1109/TSE.2017.2656884 |
| **Tipo** | Estudo empírico de campo com monitoramento contínuo |
| **Metodo** | Estudo in situ com 20 desenvolvedores profissionais usando aplicação de monitoramento personalizada + experience sampling (survey de auto-relato) |
| **Amostra** | 20 desenvolvedores de 4 empresas multinacionais (EUA, Canadá, Suíça, Europa) com grande variação de experiência (0,5-40 anos) |
| **Contexto** | Contexto de trabalho real em empresas de diversos tamanhos e estágios de projeto |
| **Modo de trabalho** | Presencial/remoto (diversificado) |

---

## Objetivo
Investigar a relação entre as práticas de trabalho dos desenvolvedores (fragmentação, atividades, interrupções), padrões rítmicos de produtividade percebida e como fatores como tempo do dia, tipo de atividade e interrupções influenciam a produtividade percebida.

---

## Questoes de Pesquisa
- **RQ1**: Como é o dia de trabalho de um desenvolvedor?
- **RQ2**: Como fragmentado é o trabalho de um desenvolvedor?
- **RQ3**: Existem tendências observáveis em como desenvolvedores percebem sua produtividade?
- **RQ4**: Qual é a relação entre atividade de desenvolvedor e produtividade percebida no trabalho?

---

## Metricas e Instrumentos de Avaliacao
- **Monitoramento contínuo**: Aplicação CustomLog registrava processo ativo, títulos de janelas, cliques de mouse, movimento/distância do mouse, keystroke count
- **Experience sampling**: Survey pop-up a cada 60 minutos (ocasionalmente 90) perguntando sobre produtividade percebida numa escala Likert 7 pontos
- **Categorização de atividades**: 15 categorias mapeadas (Coding, Email, Planning, Debugging, Code Reviews, etc.)
- **Análise**: Regressão linear para explicar produtividade percebida com 20 modelos

---

## Resultados Principais
- **Padrão de trabalho**: Desenvolvedores passam ~8,4h/dia spannung trabalho, com ~4,3h ativas em computador; alta fragmentação com média de 2,5 short breaks (±0,8) de 4,2 minutos e 3,3 long breaks (±1,4) de 54,7 minutos
- **Atividades**: Maior tempo em Coding (21%), Emails (14,5%), Work-related Browsing (11,4%); diversidade muito alta de tarefas
- **Padrões de produtividade pessoais**: Produtividade é altamente pessoal; três grupos: morning people, low-at-lunch people, afternoon people; cada indivíduo exibe padrão consistente mas diferente de outros
- **Influências negativas**: Emails, planned meetings, work unrelated websites predizem MENOR produtividade; Informal meetings, unplanned meetings mostram efeito misto
- **Fragmentação muito alta**: Developers switch activities a cada 2-3 minutos em média (exceto planned meetings)

---

## Desafios do Uso das Metricas
- **Variabilidade individual alta**: Nenhum modelo único se aplica a todos; mesma atividade tem impactos opostos em diferentes desenvolvedores
- **Self-reporting subjetivo**: Produtividade percebida é altamente subjetiva; dificuldade em mapear "idle time" para categorias específicas
- **Contextualização de dados**: Período de estudo relativamente curto (2 semanas por desenvolvedor); variações sazonais e impactos contextuais não capturados
- **Categorização ambígua**: Alguns tipos de trabalho (documentação vs. reading) podem ser ambíguos; não captura bem trabalho "offscreen"

---

## Contribuicao Principal
Fornece visão holística e empiricamente fundamentada sobre como desenvolvedores realmente gastam seu tempo, revelando alto nível de fragmentação de trabalho, padrões rítmicos muito variáveis de produtividade entre indivíduos, e fatos concretos sobre influência de diferentes atividades em produtividade percebida. O estudo desafia noções simplistas de produtividade, demonstrando que é altamente pessoal e contextual, com diferentes indivíduos mostrando preferências opostas por timing de atividades. Abre oportunidades para ferramentas personalizadas de suporte a planejamento de trabalho e design de ambientes que melhor suportem padrões de produtividade individualizados.

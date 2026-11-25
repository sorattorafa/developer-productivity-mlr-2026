# P0478 — Developers in focus! Developer Experience Analysis in a Collaborative Modeling Tool

**Decisao: INCLUIDO | Qualidade: 5/5**

---

## Dados Bibliograficos

| Campo | Valor |
|-------|-------|
| **ID** | P0478 |
| **Autores** | Miguel Silva, Lígia Teixeira, Afonso Silva, Genildo Gomes, Leonardo Barreto, Bruno Gadelha, Tayana Conte |
| **Ano** | 2022 |
| **Venue** | XXXVI Brazilian Symposium on Software Engineering (SBES 2022) |
| **DOI** | https://doi.org/10.1145/3555228.3555247 |
| **Tipo** | Conference paper |
| **Metodo** | Mixed methods (Experimental study, Quantitative scales, Qualitative focus group) |
| **Amostra** | 20 computer science students |
| **Contexto** | Academic — students learning UML modeling in a Systems Analysis and Design course at the Federal University of Amazonas (UFAM) |
| **Modo de trabalho** | Remote (due to pandemic restrictions) |
| **Metodologia** | Not specified |

---

## Objetivo

O objetivo principal do artigo é investigar a **Developer Experience (DX)** e identificar os principais fatores que afetam o uso de uma ferramenta de modelagem colaborativa de diagramas UML (Gliffy) por desenvolvedores novatos [1, 2].

---

## Questoes de Pesquisa

O estudo busca responder aos seguintes tópicos de investigação:
- **RQ1:** Como os desenvolvedores novatos percebem a infraestrutura de desenvolvimento e as ferramentas de modelagem colaborativa? [2, 3]
- **RQ2:** Quais os principais fatores que afetam a experiência de uso (DX) dos participantes em uma ferramenta de modelagem? [2]

---

## Metricas e Instrumentos de Avaliacao

| Metrica | Categoria | Nivel | Como Coletada | Validada |
|---------|-----------|-------|---------------|----------|
| **DEXI Scale** (DEXI-P, DEXI-H, DEXI-G) | DevEx / Satisfaction | Individual | Questionário com 12 pares de adjetivos opostos em diferencial semântico de sete níveis | Sim (baseada no AttrakDiff) [4, 5] |
| **Intrinsic Motivation Inventory (IMI)** | Satisfaction / Human | Individual | Questionário avaliando subescalas de interesse, competência percebida, esforço e percepção de escolha | Sim [5, 6] |
| **Focus Group** | DevEx / Collaboration | Team | Sessões de discussão em grupo para capturar percepções qualitativas | Sim (método qualitativo padrão) [5, 6] |
| **Grounded Theory** (Analysis method) | Qualitative | Team/Individual | Codificação aberta e axial dos dados do grupo focal | Sim [7, 8] |

---

## Frameworks e Metricas

### Frameworks Referenciados
- **Developer Experience (DX) Framework (Fagerholm and Münch):** REFERENCED — Utilizado como base conceitual (Cognição, Afeto e Conação) [9-11].
- **AttrakDiff:** REFERENCED — Serve como base para a escala DEXI [4, 12].
- **Dispositional Short Flow Scale (DSFS):** REFERENCED — Considerada, mas não adotada por demandar muito tempo [12].
- **User Experience (UX) Concepts (Hassenzahl):** REFERENCED — Distinção entre qualidades pragmáticas e hedônicas [13].

### Frameworks Aplicados
- **DEXI Scale:** APPLIED — Para medir a experiência pragmática e hedônica [4, 14].
- **Intrinsic Motivation Inventory (IMI):** APPLIED — Para medir a motivação intrínseca na atividade [6, 15].

---

## Fatores que Influenciam Produtividade

### Fatores Positivos
| Fator | Categoria |
|-------|-----------|
| **Facilidade de aprender** (Ease of learning) | Technical/Process [16-18] |
| **Disponibilização de recursos/templates** | Technical [16, 19, 20] |
| **Motivação intrínseca** | Human [18, 19] |
| **Promoção da criatividade** | Human [3, 14] |

### Fatores Negativos
| Fator | Categoria |
|-------|-----------|
| **Dificuldade na colaboração assíncrona** | Process/Technical [19, 21, 22] |
| **Retrabalho** (Rework) | Process [18, 19, 23] |
| **Dificuldade de organização dos diagramas** | Technical [18, 19, 23] |
| **Falta de salvamento automático** | Technical [19, 24, 25] |
| **Problemas na exportação de imagens** | Technical [20, 24] |

---

## Papel da IA e Automacao

| Campo | Valor |
|-------|-------|
| Usa IA/ML? | No |
| Automacao de coleta? | No — Coleta via Google Forms e sessões de vídeo [5] |
| Impacto de IA na produtividade? | N/A |

---

## Resultados Principais

- A experiência geral com a ferramenta Gliffy foi avaliada como **neutra** [14, 26, 27].
- As **qualidades pragmáticas** (0,31) foram melhor avaliadas que as **qualidades hedônicas** (0,10), indicando que a ferramenta é funcional, mas pouco motivadora [28].
- Participantes demonstraram **alta motivação para modelar** (média 6,45 em Esforço/Importância), mas **insatisfação com a ferramenta** específica [20, 29, 30].
- A **colaboração foi o ponto mais crítico**: muitos desistiram da funcionalidade colaborativa por ser "meio assíncrona" e não permitir ver o que outros faziam em tempo real [21, 22].
- A **ausência de salvamento automático** causou perda de trabalho e estresse ("estragou o role") para usuários acostumados com ferramentas modernas [24, 25].

---

## Desafios do Uso das Metricas

- A medição da DX exige capturar **percepções subjetivas** multidimensionais (cognitivas, afetivas e conativas), o que é mais complexo que métricas de uso simples [9, 10].
- O uso da escala **DSFS** foi descartado por ser inviável monitorar os participantes durante o tempo necessário para medir o estado de "fluxo" [12].

---

## Avaliacao de Qualidade Metodologica

| Criterio | Pontuacao (0-2) |
|----------|----------------|
| Objetivo claramente definido | 2 |
| Metodologia adequada ao objetivo | 2 |
| Amostra/contexto descrito adequadamente | 2 |
| Ameacas a validade discutidas | 1 |
| Resultados com evidencia suficiente | 2 |
| Contribuicao clara para pratica ou teoria | 2 |
| **TOTAL** | **11/12** |

---

## Limitacoes

- O estudo focou em apenas **uma ferramenta específica** (Gliffy), limitando a generalização para outras ferramentas de modelagem [31].
- **Número reduzido de participantes** (20 alunos) [31].
- Amostra **homogênea**, composta apenas por estudantes de uma única universidade e disciplina [31].
- Os participantes eram **novatos em modelagem**, o que pode ter influenciado a percepção de dificuldade [32].

---

## Contribuicao Principal

O estudo contribui para o corpo de conhecimento de Engenharia de Software ao aplicar métricas específicas de **Developer Experience** em atividades de modelagem (além da codificação), identificando que fatores como **colaboração assíncrona ineficiente**, **retrabalho organizacional** e **falta de automação (salvamento)** são barreiras críticas para a satisfação do desenvolvedor, servindo de base para a criação de melhores ferramentas CASE [26, 33].

---

*Extraido via NotebookLM em March 2026 para MLR: Software Developer Metrics in Practice*
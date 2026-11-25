# P0492 — A Case Study of Developer Bots: Motivations, Perceptions, and Challenges

> Reextração corrigida a partir do PDF (a versão anterior trazia "Ferreria et al.", "8 projetos OSS", "CI/CD Pipelines" — autor, amostra e subtítulo incorretos; o estudo é industrial na Microsoft).

**Decisao: INCLUIDO | Qualidade: 4/5**

## Dados Bibliograficos

| Campo | Valor |
|-------|-------|
| ID | P0492 |
| Autores | Sumit Asthana, Hitesh Sajnani, Elena Voyloshnikova, Birendra Acharya, Kim Herzig |
| Ano | 2023 |
| Venue | ESEC/FSE '23 (31st ACM Joint European Software Engineering Conference), San Francisco |
| DOI | 10.1145/3611643.3616248 |
| Tipo | Conference paper (case study) |
| Metodo | Estudo de caso industrial (mixed methods) |
| Amostra | 23 developer bots, ~13.000 repositórios, ~6.000 desenvolvedores; ~500 mil ações de bots em ~1,5 ano |
| Contexto | Indústria (Microsoft), larga escala |

## Objetivo
Estudo de caso sobre developer bots na Microsoft: motivações, percepções e desafios. Classifica 23 bots em 5 categorias (Config Violation, Security, Data-privacy, Developer Productivity, Code Quality).

## Método e dados
Entrevistas e surveys com desenvolvedores e usuários de bots + análise de ~500 mil ações históricas de bots ao longo de ~1,5 ano, em ~13 mil repositórios atendendo ~6 mil devs.

## Categorias de métrica (leitura do PDF)
- Productivity/Performance: **Yes** (categoria de bot "Developer Productivity"; bots para melhorar produtividade)
- Quality: **Yes** (categoria "Code Quality")
- Collaboration: **Yes** (bots no fluxo de trabalho; benefício de comunicação cross-team)
- Activity/Code: **Yes** (mineração de ~500 mil ações de bots / eventos de repositório)
- Survey/Perceptual: **Yes** (entrevistas + surveys, utilidade percebida)
- Delivery Performance: No (discute CI/CD mas não mede métrica DORA) · Satisfaction/Wellbeing: No · DevEx Dimensions: No · Agile/Process: No
- DORA: No · SPACE: No · AI: No (bots de workflow, não foco em IA/LLM)

## Qualidade (Dybå & Dingsøyr)
Estudo de caso industrial robusto, larga escala, mixed methods, 1,5 ano de dados. Limitação: contexto único (Microsoft). Média ~4/5.

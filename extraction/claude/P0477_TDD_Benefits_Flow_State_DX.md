# P0477 — Test-Driven Development Benefits beyond Design Quality: Flow State and Developer Experience

> Reextração corrigida a partir do PDF (a versão anterior atribuía o paper a "Beller et al., 2022" e descrevia um estudo de laboratório com 41 desenvolvedores, eye-tracking e condutância da pele — tudo inexistente no paper real).

**Decisao: INCLUIDO | Qualidade: 4/5**

## Dados Bibliograficos

| Campo | Valor |
|-------|-------|
| ID | P0477 |
| Autores | Pedro Calais, Lissa Franzini |
| Ano | 2023 |
| Venue | ICSE-NIER '23 (45th Int. Conference on Software Engineering: New Ideas and Emerging Results) |
| DOI | 10.1109/ICSE-NIER58687.2023.00025 |
| Tipo | Conference paper (NIER track) |
| Metodo | Survey (flow-state scale adaptada) + mapeamento teórico + self-reports da web |
| Amostra | 86 voluntários de um fórum online de TDD (76% experts, 24% intermediários) |
| Contexto | Comunidade/indústria; autores da Stone Co. |

## Objetivo
Explicar os benefícios do TDD numa dimensão pouco explorada — a experiência do desenvolvedor — conectando o ciclo red-green-refactor à teoria do flow state (Csikszentmihalyi).

## Método e dados (3 evidências)
1. Mapeamento teórico do ciclo TDD aos 4 gatilhos do flow (clear goals, unambiguous feedback, challenge-skill balance, sense of control).
2. Survey com flow-state scale adaptada (Likert 1–5), 86 respondentes; experts 4.2–4.7, intermediários 3.6–4.0; item-controle de ansiedade baixo (1.8/2.2).
3. Self-reports anedóticos coletados em blogs/fóruns (evidência fraca, assumida como tal).

## Categorias de métrica (leitura do PDF)
- Satisfaction/Wellbeing: **Yes** (flow, bem-estar, ansiedade — medidos por questionário; DevEx no sentido afetivo de Fagerholm & Münch)
- Survey/Perceptual: **Yes** (flow-state scale adaptada, autorrelato)
- DevEx Dimensions: **No** (não usa o framework Noda/Storey/Forsgren; DevEx aqui é o conceito afetivo → Satisfaction/Wellbeing)
- Productivity/Performance: No · Quality: No (qualidade só em related-work) · Activity/Code: No · Delivery Performance: No · Collaboration: No · Agile/Process: No
- DORA: No · SPACE: No · AI Discussed: No

## Avaliação de qualidade (Dybå & Dingsøyr)
Objetivo muito claro; método adequado para NIER; amostra/contexto descritos; ameaças reconhecidas (subjetividade, viés de autorrelato, amostra pequena); contribuição teórica relevante. NIER (paper curto, sem experimento controlado). Média ~4/5.

# P0327 — Recommending Root-Cause and Mitigation Steps for Cloud Incidents using Large Language Models

> Re-extração (modelo Claude) em 2026-06-07 a partir do PDF corrigido. Substitui a extração anterior (que era de outro paper). Passada independente para triangulação/κ.

## Dados Bibliograficos

| Campo | Valor |
|-------|-------|
| **ID** | P0327 |
| **Autores** | Toufique Ahmed, Supriyo Ghosh, Chetan Bansal, Thomas Zimmermann, Xuchao Zhang, Saravan Rajmohan |
| **Ano** | 2023 |
| **Venue** | IEEE/ACM ICSE 2023 (45th International Conference on Software Engineering) |
| **DOI** | 10.1109/ICSE48619.2023.00149 |
| **Tipo** | Conference paper |
| **Metodo** | Estudo empírico de larga escala + avaliação humana (mixed methods) |
| **Amostra** | >40.000 incidentes de produção (Microsoft); avaliação humana em 50 incidentes recentes com os incident owners |
| **Contexto** | Indústria (Microsoft cloud services / incident management) |

## Objetivo
Avaliar a eficácia de LLMs (GPT-3.x: Curie, Codex, Davinci, Code-davinci-002) para recomendar automaticamente root-cause e mitigação de incidentes de produção em nuvem, reduzindo o esforço manual de on-call engineers (com impacto em developer productivity).

## Tipo de Estudo / Método
Empírico, larga escala: comparação de vários LLMs em zero-shot, fine-tuned e multi-task; métricas semânticas e lexicais (ex.: BLEU-4). Validação humana com incident owners avaliando correção e legibilidade das sugestões.

## Frameworks e IA
- **DORA / SPACE / DevEx**: não aplicados/discutidos.
- **IA discutida**: SIM — LLMs (GPT-3.x/Codex) são o objeto central.

## Métricas / Categorias (leitura independente Claude)
- Productivity/Performance: produtividade do desenvolvedor aparece como motivação/impacto (não é a métrica medida).
- Survey/Perceptual: SIM — avaliação humana (incident owners) sobre correção/legibilidade das sugestões.
- Quality: foco na qualidade das sugestões de IA (BLEU/correção), não em métricas de qualidade de software per se.
- Delivery Performance / Activity/Code / Collaboration / Satisfaction / DevEx Dimensions / Agile-Process: não evidenciados.
- Observação: tema central é AIOps/incident management; relevância à medição de produtividade do desenvolvedor é indireta (motivacional).


## Avaliacao de Qualidade (leitura independente Claude)
**Decisao: INCLUIDO | Qualidade: 4/5**

Estudo empírico forte (>40k incidentes Microsoft + avaliação humana de 50) e IA central; porém a produtividade do desenvolvedor é motivacional/indireta (tema é AIOps/incident management). Relevância limítrofe; qualidade metodológica alta.

## Resultados / Contribuição
GPT-3.x/Codex geram sugestões úteis de root-cause/mitigação (mesmo em ranks mais baixos); fine-tuning e multi-task melhoram desempenho; a avaliação humana confirma utilidade potencial frente a modelos encoder-decoder (cujas recomendações eram genéricas). Primeiro estudo de larga escala do uso de LLMs para resolução de incidentes em nuvem.

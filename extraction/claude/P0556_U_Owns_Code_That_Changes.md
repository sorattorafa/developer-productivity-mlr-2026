# P0556 — U Owns the Code That Changes and How Marginal Owners Resolve Issues Slower in Low-Quality Source Code

> Reextração corrigida a partir do PDF (a versão anterior atribuía a "Neto et al."; autores reais: Borg, Tornhill, Mones).

**Decisao: INCLUIDO | Qualidade: 4/5**

## Dados Bibliograficos

| Campo | Valor |
|-------|-------|
| ID | P0556 |
| Autores | Markus Borg, Adam Tornhill, Enys Mones |
| Ano | 2023 |
| Venue | EASE '23 (Int. Conference on Evaluation and Assessment in Software Engineering), Oulu |
| DOI | 10.1145/3593434.3593480 |
| Tipo | Conference paper (estudo observacional) |
| Metodo | Mineração de repositórios + estudo observacional |
| Amostra | 40 repositórios proprietários |
| Contexto | Indústria |

## Objetivo
Avaliar como a experiência de projeto e a propriedade de arquivos (file ownership) dos desenvolvedores se relacionam com o tempo de resolução de issues, em código de baixa qualidade.

## Método e resultados
Mineração de 40 repositórios proprietários; uso do CodeScene para medir qualidade do código-fonte e tempo de desenvolvimento ativo ligado a issues do Jira. Donos marginais precisam de 45% mais tempo (mudanças pequenas) e 93% mais tempo (grandes) em código de baixa qualidade.

## Categorias de métrica (leitura do PDF)
- Quality: **Yes** (qualidade do código-fonte medida via CodeScene)
- Activity/Code: **Yes** (mineração de repositórios, code ownership)
- Delivery Performance: **Yes** (tempo de resolução de issues / tempo de desenvolvimento ativo a partir do Jira — métrica tipo cycle time)
- Productivity/Performance: No ("perdas de produtividade" é interpretação) · Collaboration: No · demais: No
- DORA: No · SPACE: No · AI: No

## Qualidade (Dybå & Dingsøyr)
Estudo observacional em larga escala (40 repos), instrumentação com CodeScene, ameaças à validade discutidas. Média ~4/5.

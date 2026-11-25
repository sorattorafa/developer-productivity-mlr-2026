# P0580 — Context-Aware Code Recommendation in Intellij IDEA

**Decisao: INCLUIDO | Qualidade: 5/5**

---

## Dados Bibliograficos

| Campo | Valor |
|-------|-------|
| **ID** | P0580 |
| **Autores** | Shamsa Abid, Hamid Abdul Basit, Shafay Shamail |
| **Ano** | 2022 |
| **Venue** | ESEC/FSE 2022 (30th ACM Joint European Software Engineering Conference) |
| **Tipo** | Artigo de Pesquisa (Tool Paper) |
| **Metodo** | Avaliacao empirica com automatizacao offline |
| **Amostra** | 120 projetos Android Java do GitHub (4 categorias) |
| **Contexto** | Desenvolvimento de software em ambientes Java/Android |

---

## Objetivo

Este artigo apresenta CA-FACER (Context-aware Feature-driven API usage-based Code Recommender), um plugin para IntelliJ IDEA que recomenda trechos de código relacionados baseado no contexto de desenvolvimento do programador. O objetivo principal é melhorar a produtividade do desenvolvedor fornecendo recomendações de código para reutilização oportunista, onde o sistema identifica features relacionadas que o desenvolvedor pode querer implementar em seguida, sem necessidade de múltiplas buscas manuais. O trabalho estende a técnica FACER anterior para considerar todo o contexto de desenvolvimento do arquivo ativo, não apenas o método recentemente buscado.

---

## Questoes de Pesquisa

- **RQ1**: Como melhorar a precisão das recomendações de código considerando o contexto completo de desenvolvimento?
- **RQ2**: Qual é o impacto da abordagem context-aware comparado com o sistema baseline FACER?
- **RQ3**: Qual taxa de sucesso o sistema alcança em diferentes estágios de desenvolvimento (inicial e evoluído)?

---

## Dados da Pesquisa

### Amostra
- 120 projetos Android Java do GitHub
- 4 categorias: (1) Music Player, (2) Bluetooth Chat, (3) Weather, (4) File Management
- 30 aplicações por categoria

### Fonte de Dados
- Repositório GitHub com projetos open-source
- Dataset de projetos Android reutilizado de trabalho anterior

### Metodos de Coleta
- Extração automática de features através de análise de código
- Mining de padrões de API usage
- Mapeamento de métodos para Method Clone Classes

### Periodo de Analise
- Análise realizada em 2021-2022
- Experimentos com dados históricos de projetos GitHub

---

## Metricas e Instrumentos de Avaliacao

**Precision@5 (P@5)**: Proporção de recomendações no top-5 que pertencem ao conjunto de ground truth. Métrica principal para avaliação de qualidade das recomendações.

**Success Rate**: Percentual de recomendações bem-sucedidas em relação ao total de tentativas.

**Mean Reciprocal Rank (MRR)**: Ranking médio da primeira recomendação correta na lista.

**Mapeamento para Method Clone Classes**: Técnica que identifica features através de análise de uso de APIs. Métodos são agrupados em classes baseado em padrões similares de chamadas de API.

**Cosine Similarity**: Utilizada para calcular similaridade entre projetos: sim(Pu, p) = |Fc ∩ Fp| / √(|Fc| · |Fp|)

**Collaborative Filtering**: Técnica para calcular scores de predição: pred(Pu, ζ) = Σ[n∈nbr(Pu)] sim(Pu, n) · κ(n, ζ) / Σ[n∈nbr(Pu)] sim(Pu, n)

**Limiar de Filtro**: γ = 0.7 para seleção de features com scores acima do threshold

---

## Resultados Principais

Para baseline FACER sob contexto C1 e ground truth G1, P@5 foi 0.58, enquanto CA-FACER alcançou P@5 de 0.94, representando melhoria de 46% em precisão.

**Resultado C1 (desenvolvimento inicial)**: P@5 = 94%, success rate = 90%

**Resultado C2 (desenvolvimento evoluído)**: P@5 = 83%, success rate = 95%

Testes estatísticos (Wilcoxon test): p < 0.001 para C1 e p = 0.002 para C2, rejeitando a hipótese nula de que medianas são idênticas.

A abordagem context-aware melhora a performance de baseline FACER em mínimo 36% e máximo 46% para recomendações sensíveis ao contexto.

---

## Desafios do Uso das Metricas

1. Uso de contexto simulado: Ameaça à validade de construto. O contexto é criado a partir de arquivo real do projeto, mas não representa completamente uso real em tempo de desenvolvimento.

2. Limitação de escopo: Apenas 120 projetos de diferentes categorias do GitHub, não de repositórios organizacionais reais. Generalização para ambiente corporativo requer validação adicional.

3. Dependência de Method Clone Classes: A qualidade das recomendações depende da identificação correta de features através de padrões de API usage, que pode variar entre domínios.

---

## Avaliacao de Qualidade

| Criterio | Pontuacao (0-2) |
|----------|----------------|
| Objetivo claramente definido | 2 |
| Metodologia adequada | 2 |
| Amostra/contexto descrito | 2 |
| Ameacas a validade discutidas | 2 |
| Resultados com evidencia | 2 |
| Contribuicao clara | 2 |
| **TOTAL** | **12/12** |

---

## Limitacoes

1. Contexto de desenvolvimento simulado em lugar de observação em tempo real
2. Amostra limitada a 120 projetos do GitHub em vez de repositórios corporativos
3. Abordagem testada apenas para projetos Android em linguagem Java
4. Dependência de qualidade de identificação de Method Clone Classes
5. Não considera variações de estilo de programação entre desenvolvedores
6. Métrica de sucesso baseada em ground truth pré-definido, não em feedback de usuário real

---

## Contribuicao Principal

O trabalho apresenta CA-FACER, um sistema inovador de recomendação de código que integra modeling contextual híbrido combinando pré-filtragem, recomendação baseada em popularidade de features, e pós-filtragem. A abordagem alcança 46% de melhoria em precisão comparado ao baseline, demonstrando que considerar o contexto completo de desenvolvimento (todos os métodos no arquivo ativo) em lugar de apenas o método recentemente buscado resulta em recomendações significativamente melhores. O sistema foi implementado como plugin prático para IntelliJ IDEA, mostrando potencial para adoção em ambientes reais de desenvolvimento.

---

*Extraido em Marco 2026 para MLR: Software Developer Metrics in Practice*

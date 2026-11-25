# P0499 — Advancing HCI with Neuromorphic Technology: Guidelines for Designing User-Friendly Developer Tools for Neuromorphic Development

**Decisao: INCLUIDO | Qualidade: 4/5**

---

## Dados Bibliograficos

| Campo | Valor |
|-------|-------|
| **ID** | P0499 |
| **Autores** | Divesh Upreti, Aditi Maheshwari, Taylor Tabb, Ioannis Polykretis, Eric M Gallo, Kenneth Michael Stewart, Thomas D. LaToza, Andreea Danielescu |
| **Ano** | 2025 |
| **Venue** | CHI 2025 - ACM Conference on Human Factors in Computing Systems |
| **Tipo** | Research Article - Qualitative Study |
| **Metodo** | Entrevistas semi-estruturadas com especialistas |
| **Amostra** | 12 especialistas em computação neuromórfica |
| **Contexto** | Desenvolvimento de ferramentas para computação neuromórfica |

---

## Objetivo

Este artigo explora os desafios enfrentados por desenvolvedores ao trabalhar com computação neuromórfica (NC). Através de entrevistas com 12 especialistas, os autores investigam as barreiras de entrada para NC, identificam gaps nas ferramentas e recursos disponíveis, e propõem diretrizes para projetar ferramentas mais acessíveis e centradas no usuário. O trabalho busca melhorar a experiência do desenvolvedor (DX) em projetos de NC, considerando a falta de documentação, simuladores imperfeitos e a complexidade inerente da programação neuromórfica.

---

## Questoes de Pesquisa

- **RQ1**: Quais são as motivações dos desenvolvedores para adotar computação neuromórfica?
- **RQ2**: Quais são os fluxos de trabalho, ferramentas e recursos atuais para desenvolvimento de NC?
- **RQ3**: Quais são os principais desafios e pontos de dor enfrentados por desenvolvedores de NC?
- **RQ4**: Quais habilidades, recursos e estratégias são essenciais para novos desenvolvedores em NC?

---

## Dados da Pesquisa

### Amostra
- 12 especialistas em computação neuromórfica com experiência variando de 1 a 39 anos
- Participantes trabalhando em pesquisa, indústria e ambiente universitário
- Diversidade de formação: engenharia elétrica, ciência cognitiva, neurociência computacional
- Backgrounds em diferentes regiões geográficas: América do Norte, Europa e Austrália

### Fonte de Dados
- Entrevistas semi-estruturadas presenciais e por Zoom
- Duração média de 53 minutos por entrevista (variação de 30-90 minutos)
- Transcrições manuais corrigidas com qualidade assegurada

### Metodos de Coleta
- Entrevistas em profundidade com protocolo semi-estruturado
- Perguntas abertas sobre motivações, workflows, desafios específicos
- Documentação de recomendações dos participantes para melhorias

### Periodo de Analise
- Coleta de dados: Novembro-Dezembro 2023
- Periodo de análise: Janeiro-Março 2024

---

## Metricas e Instrumentos de Avaliacao

O estudo utiliza análise qualitativa com as seguintes abordagens:

**Análise Temática**: Codificação indutiva dos transcripts para identificar temas recorrentes relacionados a workflows, desafios e recomendações. Os codes foram agrupados em 39 códigos principais organizados em 7 temas superordenados.

**Frameworks de Análise**:
- Análise baseada em Diffusion of Innovation (DOI) de Rogers para entender motivações
- Uso de Constant Comparison Method para codificação iterativa
- Análise reflexiva para minimizar bias do pesquisador

**Áreas de Avaliação**:
- Motivações para NC (potencial para pesquisa, compatibilidade com computação biológica)
- Workflows atuais (brainstorming, sandboxing, treinamento de SNNs, otimização)
- Ferramentas e recursos utilizados (LAVA, Nengo, PyTorch, hardware especializado)
- Desafios encontrados (complexidade de SNNs, falta de documentação, problemas de hardware)
- Recomendações para DX melhorado

---

## Resultados Principais

**Motivações Principais**:
- Compatibilidade com processamento biológico e neurociência
- Eficiência energética superior ao processamento convencional
- Oportunidades em pesquisa e desenvolvimento de tecnologia edge

**Workflows Identificados**:
1. Brainstorming com definição clara de problemas
2. Sandboxing e experimentação iterativa
3. Treinamento de SNNs com aprendizado supervisionado
4. Otimização de redes neuronais
5. Transição de simulador para hardware neuromórfico

**Desafios Principais**:
- Complexidade de SNNs: dimensão temporal, encoding/decoding desafiador
- Falta de documentação e recursos adequados para NC
- Hardware neuromórfico inacessível ou indisponível
- Simuladores imperfeitos que não replicam completamente o comportamento do hardware
- Falta de benchmarks padronizados e métricas de avaliação
- Comunidade pequena e conhecimento fragmentado

**Recomendações para Melhorar DX**:
- Criar documentação abrangente em múltiplos níveis de abstração
- Desenvolver aplicações iniciais e tutoriais para novos desenvolvedores
- Melhorar acessibilidade de hardware e ferramentas de simulação
- Estabelecer benchmarks e práticas recomendadas padronizadas
- Criar plataformas comunitárias para compartilhamento de conhecimento

---

## Desafios do Uso das Metricas

1. **Falta de standardização em métricas de desempenho**: Diferentes projetos usam diferentes métricas, dificultando comparações entre implementações neuromórficas.

2. **Desafio de selecionar métricas apropriadas**: Métricas derivadas diretamente do desempenho de deep learning podem ser inadequadas para sistemas neuromórficos, que operam em princípios diferentes.

3. **Inacessibilidade de benchmarks padronizados**: A comunidade de NC é pequena e ainda não estabeleceu benchmarks consensuais para avaliar soluções neuromórficas.

4. **Incompatibilidade entre simuladores e hardware real**: As métricas em simuladores podem não corresponder ao comportamento em hardware real, tornando difícil o desenvolvimento sem acesso ao hardware.

5. **Complexidade na avaliação de spiking networks**: A natureza temporal e assíncrona dos SNNs torna desafiador medir e comparar desempenho de forma padronizada.

---

## Avaliacao de Qualidade

| Criterio | Pontuacao (0-2) |
|----------|----------------|
| Objetivo claramente definido | 2 |
| Metodologia adequada | 2 |
| Amostra/contexto descrito | 2 |
| Ameacas a validade discutidas | 1 |
| Resultados com evidencia | 2 |
| Contribuicao clara | 2 |
| **TOTAL** | **11/12** |

---

## Limitacoes

1. Amostra pequena de 12 especialistas pode não capturar toda a diversidade de experiências em NC
2. Viés de seleção potencial: participantes podem ser mais vocalizados sobre desafios
3. Observações limitadas a entrevistas - não inclui observação direta de trabalho em NC
4. Campo de NC em evolução rápida; recomendações podem desatualizar rapidamente
5. Foco em perspectivas de pesquisadores; experiências de profissionais da indústria podem diferir

---

## Contribuicao Principal

Este artigo oferece a primeira análise qualitativa detalhada dos desafios de experiência do desenvolvedor em computação neuromórfica. Ao documentar workflows atuais, barreiras de entrada e áreas de melhoria, o trabalho fornece diretrizes acionáveis para pesquisadores de HCI e desenvolvedores de ferramentas buscando tornar NC mais acessível. As recomendações específicas sobre documentação, tutoriais, benchmarking e suporte comunitário podem reduzir significativamente a curva de aprendizado e acelerar a adoção de NC na comunidade mais ampla, facilitando assim uma transição mais suave de sistemas baseados em von Neumann para arquiteturas neuromórficas.

---

*Extraido em Marco 2026 para MLR: Software Developer Metrics in Practice*

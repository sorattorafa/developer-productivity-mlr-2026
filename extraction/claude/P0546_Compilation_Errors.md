# P0546 — Analyzing and Repairing Compilation Errors

**Decisao: INCLUIDO | Qualidade: 4/5**

---

## Dados Bibliograficos

| Campo | Valor |
|-------|-------|
| **ID** | P0546 |
| **Autores** | Ali Mesbah, Andrew Rice, Edward Aftandilian, Emily Johnston, Nick Glorioso |
| **Ano** | 2019 |
| **Venue** | ICSE-Companion 2019: 41st International Conference on Software Engineering |
| **Tipo** | Estudo Empírico Quantitativo |
| **Metodo** | Análise de logs de build, detecção de refatoração com Neural Machine Translation |
| **Amostra** | 4,8 milhões de builds Java em um período de 2 meses (janeiro-fevereiro 2018) |
| **Contexto** | Google - desenvolvimento Java em larga escala |

---

## Objetivo

Este paper investiga como desenvolvedores gastam tempo resolvendo falhas de build em Java, com foco em quantificar o impacto de diferentes tipos de erros de compilação. Os autores coletam dados de logs de build do Google para entender qual tempo do desenvolvimento é consumido resolvendo diferentes tipos de diagnósticos de compilador. Descobrem que o diagnóstico "cant.resolve" (símbolo não resolvido) consome 47% do tempo total de resolução de builds quebrados. O estudo também treina um modelo de Neural Machine Translation (NMT) para reparar automaticamente erros de "cant.resolve", alcançando 50% de taxa de sucesso (fix correto na primeira tentativa) e 87% de acerto nas top 3 sugestões.

---

## Questoes de Pesquisa

- Quanto tempo desenvolvedores gastam resolvendo diferentes tipos de erros de compilação?
- Como o tempo de resolução varia com diferentes tipos de diagnósticos?
- Como a escolha de ferramenta (IDE vs. linha de comando) afeta taxa de falhas de build?
- Como automatizar a reparação de erros de compilação comuns?

---

## Dados da Pesquisa

### Amostra
- 4,8 milhões de builds Java iniciados por desenvolvedores no Google
- ~1 milhão (20%) de builds falharam
- 1.853.417 diagnósticos de compilador corrigidos subsequentemente
- 949.325 (51%) eram diagnósticos "cant.resolve"
- 186.992 exemplos de treinamento, 42.363 validação, 36.101 teste para modelo NMT

### Fonte de Dados
- Logs de build automaticamente capturados
- Snapshots de código compilado
- Ferramentas usadas para iniciar build (IDE vs. linha de comando)
- Sequências de builds em um ambiente específico

### Metodos de Coleta
- Parser customizado para mapear mensagens de erro aos modelos de template do compilador
- Identificação de "resolution sessions" (sequência de builds onde diagnóstico é introduzido e depois resolvido)
- Cálculo de Active Resolution Cost (ARC): tempo total entre builds / número de diagnósticos na sessão
- Deep Delta: linguagem simples para descrever mudanças em AST
- Neural Machine Translation: seq2seq model para traduzir de descrição de erro para descrição de fix

### Periodo de Analise
- Coleta de dados: 23 janeiro a ... 2018 (2 meses)
- Período de análise: foco em período de pico de desenvolvimento

---

## Metricas e Instrumentos de Avaliacao

1. **Active Resolution Cost (ARC)**:
   - Tempo total entre builds em sessão de resolução / número de diagnósticos
   - Aproximação de tempo gasto por diagnóstico
   - Média e máximo por tipo de diagnóstico

2. **Tipos de Diagnósticos**:
   - cant.resolve: Uso de símbolo não definido
   - cant.apply.symbol: Nenhuma declaração de método com assinatura compatível
   - strict: Dependências incorretamente declaradas em sistema Bazel
   - doesnt.exist: Uso de pacote não definido
   - expected: Erro de sintaxe
   - inconvertible.types: Tentativa de cast entre tipos incompatíveis
   - unreported.exception: Exceção checked que precisa ser tratada
   - does.not.override.abstract: Falha em implementar método abstrato herdado
   - already.defined: Símbolo já definido

3. **Modelos de Machine Learning**:
   - **DeepDelta**: Linguagem para descrever mudanças em AST
   - **Neural Machine Translation (seq2seq)**:
     - Input: Sentença DeepDelta descrevendo erro e localização no AST
     - Output: Sentença DeepDelta descrevendo mudança para resolver
     - Tamanho de vocabulário: 30.000
     - Métrica: Taxa de sucesso (fix correto), posição do fix correto nas top 3 sugestões

4. **Comparação entre Ambientes**:
   - IDE (IntelliJ, Android Studio): 3% de falha de build
   - Linha de comando: 26% de falha de build
   - Mesmo conjunto de diagnósticos mais custosos em ambos os casos

---

## Resultados Principais

1. **Distribuição de Impacto de Erros de Build**:
   - cant.resolve: 47% do tempo total de ARC
   - cant.apply.symbol: 11% do tempo
   - strict: 9% do tempo
   - doesnt.exist: 7% do tempo
   - cant.apply.symbols: 5% do tempo

2. **Custos Específicos (em segundos de ARC)**:
   - cant.resolve: 69 seg média, 13.327 seg máximo
   - cant.apply.symbol: 102 seg média, 8.330 seg máximo
   - expected (syntax error): 35 seg média, 5.190 seg máximo

3. **Diferenças IDE vs. Linha de Comando**:
   - IDE: strict (32%), cant.resolve (27%), doesnt.exist (13%)
   - Console: cant.resolve (47%), doesnt.exist (8%), cant.apply.symbol (11%)

4. **Reparação Automática de cant.resolve**:
   - Taxa de sucesso de 50% (fix correto na primeira tentativa)
   - Correct repair no top 3 sugestões: 87%
   - Modelo seq2seq adequado para tarefa

---

## Desafios do Uso das Metricas

1. **Definição de Sessão de Resolução**: Janela de tempo de 1 hora para distinguir task-switching
2. **Compartilhamento de Tempo**: Quando múltiplos diagnósticos presentes, tempo compartilhado igualmente
3. **Representatividade**: Dados são específicos do Google - pode não generalizar a outras organizações
4. **Precisão do Modelo**: Recall de 87% do RefactoringMiner significa ~13% das mudanças não detectadas
5. **Tipos de Diagnósticos**: Não cobre todos os possíveis tipos de erros de compilador
6. **Resolução Coarse-grained**: Commits são muito granulares para capturar resolução de falhas de build

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

1. Dados propriedários do Google - não disponível para replicação
2. Específico para ambiente Java e build system Bazel
3. Limitado a um único período de 2 meses
4. Análise de um único produto de software/organização
5. Número limitado de diagnósticos de compilador investigados
6. Modelo NMT treinado apenas em mudanças de AST, não em código completo
7. Não investiga fatores sociais que afetam resolução de erros
8. Não explora diferenças entre tipos de desenvolvedores (junior vs. senior)

---

## Contribuicao Principal

Este trabalho contribui ao campo de developer productivity através de análise quantitativa em escala industrial de como desenvolvedores gastam tempo resolvendo erros de compilação. A descoberta que cant.resolve consome 47% do tempo total de resolução de builds é significante e motivadora para ferramenta. O estudo também demonstra que IDE tools são muito efetivos em prevenir e localizar erros (3% de falha vs. 26% em linha de comando), sugerindo que adoção de IDEs melhores pode melhorar produtividade. A aplicação bem-sucedida de Neural Machine Translation para reparação automática (50% de acerto) mostra potencial para automação futura. O trabalho enfatiza a importância de entender custos reais de diferentes tipos de erros para priorizar mejorías de ferramenta.

---

*Extraido em Marco 2026 para MLR: Software Developer Metrics in Practice*

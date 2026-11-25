# G061 — DDL2PropBank Agent: Benchmarking Multi-Agent Frameworks' Developer Experience Through a Novel Relational Schema Mapping Task

**Decisao: INCLUIDO | Qualidade GL: 6/6**

---

## Dados Bibliograficos

| Campo | Valor |
|-------|-------|
| **ID** | G061 |
| **Autor/Organizacao** | Shafiuddin Rehan Ahmed and Wei Wei / Center for Advanced AI, Accenture |
| **Data** | 2026-03 (Copyright 2026) |
| **Tipo** | Technical Report / White paper |
| **URL** | https://github.com/anonymous/ddl2propbank (Artifact Repository) |

---

## Resumo

Este documento apresenta o **DDL2PropBank**, um benchmark inédito projetado para avaliar a **Developer Experience (DX)** de **multi-agent frameworks (MAFs)** [1, 2]. A tarefa central consiste em mapear esquemas de bancos de dados relacionais para **rolesets** do **PropBank**, exigindo raciocínio linguístico sobre nomes de tabelas, colunas e chaves estrangeiras [1, 3]. A avaliação utiliza o padrão **Agent-as-a-Tool**, onde agentes especializados são registrados como ferramentas chamáveis por um orquestrador, permitindo comparar como diferentes frameworks lidam com a coordenação de fluxos de trabalho complexos [4, 5].

O estudo analisa dez frameworks sob duas dimensões principais: **code complexity**, medida via análise estática de implementações de referência, e **AI-assistability**, que avalia a capacidade de assistentes de código como o **GitHub Copilot** gerarem implementações funcionais e idiomáticas baseadas apenas em documentação [6-8]. Os resultados revelam que a integração nativa com o **Model Context Protocol (MCP)** e o registro unificado de ferramentas são determinantes críticos para reduzir o esforço de desenvolvimento [9-11]. O framework **Agno** destacou-se como o melhor desempenho geral, combinando a menor complexidade de código com a maior taxa de sucesso funcional (**pass@1**) e alinhamento estrutural [1, 9, 12].

---

## Frameworks Mencionados

*   **Agno**: Recomendado; obteve a melhor combinação de baixa **code complexity** e alta **AI-assistability** [1, 9, 13].
*   **Pydantic AI**: Recomendado; líder em baixa complexidade de código e controle de fluxo simplificado [9, 14].
*   **Claude SDK (Anthropic)**: Discutido; apresentou alta **structural alignment** e taxa de sucesso de 83% no **pass@1** [9, 12].
*   **OpenAI Agents**: Discutido; alto desempenho em conformidade com padrões idiomáticos e sucesso de execução [9, 12].
*   **LangChain / LangGraph**: Discutido/Critiquado; a abundância de padrões (multi-pattern) dificulta a convergência da IA para código idiomático, embora mantenha boa funcionalidade [13, 15, 16].
*   **DSPy**: Critiquado; maior complexidade de código devido à falta de suporte nativo ao **MCP** [9, 10, 16].
*   **AgentScope**: Critiquado; alto overhead cognitivo devido ao excesso de **imports** e abstrações internas complexas [9, 10, 17].
*   **Google ADK**: Critiquado; apesar do bom alinhamento estrutural, falhou em todas as execuções reais devido a erros de configuração opacos [16, 17].
*   **Smolagents**: Discutido; classificado no nível médio de complexidade [9, 18, 19].
*   **Microsoft Agent Framework**: Discutido; apresentou baixa taxa de **pass@1** (33%) [17, 18].
*   **DevEx**: Conceito central discutido como a experiência do desenvolvedor [1, 20].
*   **SPACE**: Mencionado como framework relacionado para medir produtividade [20].

---

## Metricas Mencionadas

*   **Logical Lines of Code (LLOC)**: Utilizada para medir o tamanho da implementação e o esforço cognitivo [18, 21, 22].
*   **Cyclomatic Complexity (CCN)**: Mede a complexidade das ramificações do fluxo de controle [6, 18, 21].
*   **pass@1**: Probabilidade de uma única geração de código pela IA passar em todos os testes funcionais [23, 24].
*   **Structural Alignment (Judge Score)**: Avaliação via **LLM-as-Judge** (usando **Claude Opus 4.5**) para medir quão idiomático é o código gerado em relação à referência humana (escala 0-24) [25-27].
*   **Functional Correctness / Runtime Validity**: Teste binário de execução ponta-a-ponta sem exceções e com saída correta [25, 28].
*   **Cost per roleset ($/RS)**: Métrica de eficiência de custo para o trabalho semântico realizado pelos agentes [29, 30].
*   **Library Size (LOC)**: Comparação entre o tamanho da base de código do framework e sua facilidade de uso [13, 31].

---

## Insights para Praticantes

*   **A integração nativa com MCP** e o registro de ferramentas sem a necessidade de **decorators** pesados reduzem drasticamente o **boilerplate** e a complexidade do código [9, 10, 14].
*   A **AI-assistability** de um framework é determinada pela convergência da API e não apenas pelo volume de documentação; APIs com um "único caminho óbvio" são muito mais fáceis de serem automatizadas por IAs [11, 32].
*   Frameworks flexíveis (como **LangChain**) podem ter sucesso funcional alto, mas geram código não-idiomático ou depreciado, o que aumenta o fardo de manutenção técnica [9, 16].
*   O uso de ferramentas auxiliares como **LiteLLM** pode acelerar o ciclo de desenvolvimento ao unificar a troca de modelos e fornecer **caching** para depuração de agentes [20, 33].

---

## Avaliacao de Qualidade GL (Garousi et al.)

| Criterio | Pontuacao (0-1) |
|----------|----------------|
| Autoridade do autor/organizacao | 1 |
| Descricao de metodologia | 1 |
| Data de publicacao | 1 |
| Objetividade (vies comercial) | 1 |
| Referencias citadas | 1 |
| Contribuicao nova | 1 |
| **TOTAL** | **6/6** |

---

*Extraido via NotebookLM em March 2026 para MLR: Software Developer Metrics in Practice*
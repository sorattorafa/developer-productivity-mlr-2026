# P0486 — Facing up the primary emotions in Mobile Software Ecosystems from Developer Experience

**Decisao: INCLUIDO | Qualidade: 5/5**

---

## Dados Bibliograficos

| Campo | Valor |
|-------|-------|
| **ID** | P0486 |
| **Autores** | Awdren Fontão, Oswald M. Ekwoge, Rodrigo Santos, Arilo Claudio Dias-Neto |
| **Ano** | 2017 |
| **Venue** | WASHES '17: 2nd Workshop on Social, Human, and Economic Aspects of Software |
| **DOI** | 10.1145/3098322.3098325 |
| **Tipo** | Conference paper |
| **Metodo** | Repository mining (MSR), Qualitative and Quantitative analysis |
| **Amostra** | 1.568.377 corpos de perguntas (body of posts) do Stack Overflow |
| **Contexto** | Mobile Software Ecosystems (MSECO) envolvendo as plataformas Android, iOS e Windows Phone |
| **Modo de trabalho** | Not specified |
| **Metodologia** | Not specified |

---

## Objetivo

O objetivo principal do artigo é identificar quais emoções primárias (sadness, anger, joy, disgust e fear) estão envolvidas nas dúvidas técnicas postadas por desenvolvedores nos três principais ecossistemas de software móvel (Android, iOS e Windows Phone) e analisar como essas emoções se relacionam com a Developer Experience (DX) [1, 2].

---

## Questoes de Pesquisa

*   **RQ1:** What are the most prevalent emotions in the three main MSECOs (Android, iOS, and Windows Phone) based on the body of technical questions in Stack Overflow? [1, 3].

---

## Metricas e Instrumentos de Avaliacao

| Metrica | Categoria | Nivel | Como Coletada | Validada |
|---------|-----------|-------|---------------|----------|
| Emotion presence (Joy, Fear, Sadness, Anger, Disgust) | DevEx | Individual | AlchemyLanguage API (NLP) aplicada ao texto das perguntas | No [4] |
| Question View Count | Activity | Individual | Extraída diretamente do dataset (posts.xml) do Stack Overflow | Yes [5] |
| Word Frequency | Activity | Organization | Algoritmo de contagem de palavras após pré-processamento de texto | Yes [6] |

---

## Frameworks e Metricas

### Frameworks Referenciados
*   **Developer Experience (DX):** REFERENCED — Utilizado para definir o escopo das sensações dos desenvolvedores em relação ao trabalho [7, 8].
*   **Mobile Software Ecosystem (MSECO):** REFERENCED — Utilizado para contextualizar as relações socio-técnicas entre desenvolvedores e plataformas [7, 9].

### Frameworks Propostos
O artigo não propõe um novo framework, mas utiliza técnicas de **Mining Software Repositories (MSR)** para analisar aspectos sociais em ecossistemas [1, 10].

---

## Fatores que Influenciam Produtividade

### Fatores Positivos
| Fator | Categoria |
|-------|-----------|
| Busca por Best practices e estratégias simples de implementação (Joy) | Technical |
| Implementação bem-sucedida de Advanced features (ex: notificações, customização de tiles) | Technical |

### Fatores Negativos
| Fator | Categoria |
|-------|-----------|
| Incompatibilidade ou indisponibilidade de recursos/libraries (Anger) | Technical |
| Dificuldades técnicas com Emulators e dispositivos físicos (Sadness) | Technical |
| Problemas persistentes na manipulação de User Interface elements (Sadness) | Technical |
| Documentação oficial incompleta ou desatualizada | Organizational |

---

## Papel da IA e Automacao

| Campo | Valor |
|-------|-------|
| Usa IA/ML? | Yes — Utiliza a API AlchemyLanguage (Natural Language Processing) para realizar Emotion Analysis automatizada [11]. |
| Automacao de coleta? | Yes — Mineração automatizada de dados públicos do Stack Overflow com filtragem por tags [5, 11]. |
| Impacto de IA na produtividade? | O estudo utiliza a IA como ferramenta de medição da experiência, mas não avalia o impacto direto da IA na produtividade do desenvolvedor. |

---

## Resultados Principais

*   **Sadness** é a emoção mais prevalente em todos os três ecossistemas analisados [12, 13].
*   No **Android e iOS**, o ranking de emoções é: Sadness, Anger e Joy [12, 13].
*   No **Windows Phone**, o ranking é ligeiramente diferente: Sadness, Joy e Anger [12, 13].
*   A emoção **Sadness** está frequentemente associada a termos como *error, found, constructor* e problemas com emuladores [6, 14].
*   A emoção **Anger** surge comumente devido à indisponibilidade de recursos ou incompatibilidade de SDKs e versões de sistemas operacionais [15, 16].
*   A presença de **Joy** indica que desenvolvedores buscam refinar seu conhecimento, focando em "melhores caminhos" em vez de apenas resolver bloqueios [16, 17].

---

## Desafios do Uso das Metricas

*   **Ruído no Processamento de Linguagem Natural (NLP):** A sintaxe de códigos fonte dentro das postagens pode introduzir ruído na análise emocional, exigindo limpeza rigorosa (remoção de tags HTML e snippets) [18].
*   **Ambiguidade Humana:** Interpretadores humanos podem ter dúvidas ou nuances ao classificar emoções em artefatos técnicos de software [19].

---

## Avaliacao de Qualidade Metodologica

| Criterio | Pontuacao (0-2) |
|----------|----------------|
| Objetivo claramente definido | 2 |
| Metodologia adequada ao objetivo | 2 |
| Amostra/contexto descrito adequadamente | 2 |
| Ameacas a validade discutidas | 2 |
| Resultados com evidencia suficiente | 2 |
| Contribuicao clara para pratica ou teoria | 2 |
| **TOTAL** | **12/12** |

---

## Limitacoes

*   O estudo analisou apenas o **corpo das perguntas**, sem considerar as redes de interação entre quem pergunta e quem responde [4].
*   As evidências extraídas via AlchemyLanguage API ainda carecem de **validação externa** adicional [4].
*   Não investiga como as emoções mudam ao longo das diferentes **fases de desenvolvimento** [4].

---

## Contribuicao Principal

A principal contribuição é o fornecimento de um corpo inicial de conhecimento sobre as emoções dos desenvolvedores em repositórios de Q&A, demonstrando que a análise de sentimentos pode ajudar as empresas mantenedoras de plataformas (keystones) a priorizar suporte técnico e adaptar estratégias de engajamento para melhorar a Developer Experience [2, 4, 16].

---

*Extraido via NotebookLM em March 2026 para MLR: Software Developer Metrics in Practice*
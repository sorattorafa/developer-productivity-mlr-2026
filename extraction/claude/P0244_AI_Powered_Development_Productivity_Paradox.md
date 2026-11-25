# P0244 — The Productivity Paradox of AI-Powered Development

**Decisao: INCLUIDO | Qualidade: 4/5**

---

## Dados Bibliograficos

| Campo | Valor |
|-------|-------|
| **ID** | P0244 |
| **Autores** | Luciane Fortes, Guilherme Vaz Pereira, André Coelho, Rafael Prikladnicki, Karina Kohl |
| **Ano** | 2025 |
| **Venue** | IEEE Software (Special Issue on Developer Experience) |
| **DOI** | 10.1109/MS.0000.0000000 |
| **Tipo** | Estudo de caso em contexto industrial |
| **Metodo** | Pesquisa mista: survey com 106 desenvolvedores e análise temática qualitativa de respostas abertas |
| **Amostra** | 106 desenvolvedores (61 usuários GitHub Copilot, 45 usuários Gemini Code Assist) de empresa brasileira |
| **Contexto** | Desenvolvimento de software em larga escala com múltiplas equipes |
| **Modo de trabalho** | Presencial/remoto híbrido |

---

## Objetivo
Explorar como a percepção de produtividade dos desenvolvedores ao usar assistentes de código baseados em IA (GenAI) se relaciona com dimensões chave de experiência do desenvolvedor (DevEx), identificando paradoxos entre ganhos de eficiência percebidos e impactos em bem-estar e produtividade sustentável.

---

## Questoes de Pesquisa
- **RQ1**: Como as dimensões de DevEx se associam com a produtividade percebida ao usar assistentes de código IA?

---

## Metricas e Instrumentos de Avaliacao
- **Dimensões DevEx**: Feedback Loops (qualidade e velocidade de feedback), Cognitive Load (esforço mental), Flow State (imersão e foco)
- **Ferramentas estudadas**: GitHub Copilot, Gemini Code Assist
- **Medidas**: Composite scores Likert-scale para DevEx; regressão para prever Task Completion Efficiency e Flow State
- **Análise qualitativa**: Codificação temática indutiva de respostas abertas em 4 categorias (Desafios, Casos de Uso, etc.)

---

## Resultados Principais
- **Feedback Loops dominam**: Feedback é o principal preditor de produtividade em ambas ferramentas (β=0,865 para Copilot; β=0,687 para Gemini)
- **Paradoxo em Cognitive Load**: GitHub Copilot reduz carga cognitiva percebida (β=0,237) mas sem impacto significativo em produtividade; Gemini mostra efeito modesto (β=0,319)
- **Flow matters only for Copilot**: Flow state impulsiona produtividade mais forte para Copilot (β=0,806) que para Gemini (β=0,333)
- **Diferenças por experiência**: Programadores juniores beneficiam-se mais de Gemini em Feedback; seniors beneficiam-se mais em Flow State com Copilot
- **Desafios predominantes**: Qualidade inconsistente de sugestões, autocomplete intrusivo, dificuldades contextual, requisitos de prompt crafting

---

## Desafios do Uso das Metricas
- **Qualidade de sugestões variável**: Sugestões frequentemente de baixa qualidade ou irrelevantes (mencionado por P25: "suggestions are of low quality")
- **Flow state disruption**: Sugestões distratoras interrompem foco e fluxo de trabalho
- **Dependência de contexto**: Capacidade de manutenção e compreensão do legacy code limitada
- **Limitações técnicas**: Problemas de instalação, gaps em linguagens menos comuns, inconsistências de IDE
- **Paradoxo da privacidade**: Benefícios de produtividade versus preocupações com segurança e contextualização

---

## Contribuicao Principal
Demonstração empírica de paradoxo importante em IA para desenvolvimento: assistentes de código podem simultaneamente melhorar e prejudicar produtividade dependendo de padrões de interação, carga cognitiva e contextos de trabalho. Feedback loops de qualidade emergem como fator dominante em ambas ferramentas. O trabalho revela que distinções de produtividade diminuem com maior experiência profissional, sugerindo que ferramentas IA beneficiam desproporcionalmente desenvolvedores menos experientes em certos aspectos, mas especialistas em outros.

# P0027 — What Predicts Software Developers' Productivity?

**Decisao: INCLUIDO | Qualidade: 4/5**

---

## Dados Bibliograficos

| Campo | Valor |
|-------|-------|
| **ID** | P0027 |
| **Autores** | Emerson Murphy-Hill, Ciera Jaspen, Caitlin Sadowski, David Shepherd, Michael Phillips, Collin Winter, Andrea Knight, Edward Smith, Matthew Jorde |
| **Ano** | 2021 |
| **Venue** | IEEE Transactions on Software Engineering, Vol. 47, No. 3 |
| **DOI** | 10.1109/TSE.2019.2900308 |
| **Tipo** | Estudo empírico multi-empresa com survey |
| **Metodo** | Survey com 622 desenvolvedores; regressão linear; análise correlacional |
| **Amostra** | 622 desenvolvedores de 3 empresas (Google: 407; ABB: 137; National Instruments: 78) |
| **Contexto** | Empresas de tecnologia e engenharia de diferentes tamanhos e focos |
| **Modo de trabalho** | Pesquisa online e análise de dados internos de recursos humanos |

---

## Objetivo
Identificar empiricamente quais fatores mais fortemente predizem a produtividade auto-percebida de desenvolvedores, e determinar se esses preditores variam entre empresas e diferem de outros profissionais do conhecimento.

---

## Questoes de Pesquisa
- **RQ1**: Quais fatores mais fortemente predizem a produtividade auto-percebida dos desenvolvedores?
- **RQ2**: Como esses preditores diferem entre empresas?
- **RQ3**: O que diferencia desenvolvedores de outros profissionais do conhecimento em termos de preditores de produtividade?

---

## Metricas e Instrumentos de Avaliacao
- **Medida de Produtividade Auto-percebida**: Escala tipo Likert baseada em "alcançar regularmente um alto nível de produtividade"
- **127 Fatores Candidatos** avaliados através de survey de 5 pontos, incluindo:
  - Variedade de tarefas
  - Habilidade de trabalhar remotamente
  - Entusiasmo no trabalho
  - Suporte dos pares para novas ideias
  - Feedback útil sobre desempenho
  - Acesso a ferramentas apropriadas
- **Análise**: Regressão linear com medidas objetivas (linhas de código, número de changesets) e variáveis demográficas de controle
- **Validação**: Análise correlacional entre auto-percepção e métricas objetivas

---

## Resultados Principais
- **Fatores mais fortes para produtividade auto-percebida**:
  - Variedade de tarefas (correlação forte)
  - Habilidade de trabalhar remotamente (correlação forte)
  - Entusiasmo no trabalho/satisfação
  - Suporte dos pares para novas ideias
  - Feedback útil sobre desempenho
- **Diferenças por empresa**: Fatores variam em importância relativa entre Google, ABB e National Instruments
- **Diferenças vs. outros profissionais**: Fatores não-técnicos (satisfação, suporte, feedback) predizem mais fortemente que outros conhecedores
- **Fraca correlação com métricas objetivas**: Linhas de código e número de changesets apenas explicam pequena fração de variância (<3%)
- **Variabilidade individual**: Auto-percepção de produtividade é mais fortemente relacionada a características do trabalho que a volume de output

---

## Desafios do Uso das Metricas
- **Viés de auto-relato**: Produtividade auto-percebida pode não correlacionar bem com métricas objetivas
- **Variabilidade cultural**: Diferenças entre empresas sugerem que contexto organizacional é crítico
- **Generalização limitada**: Amostra composta principalmente por empresas de tecnologia ocidentais
- **Múltiplas definições**: Falta de consenso sobre o que constitui "produtividade" para desenvolvedores
- **Causação vs. correlação**: Survey não permite inferência causal definitiva
- **Limitações de alcance**: Alguns fatores candidatos podem não ter sido adequadamente capturados

---

## Contribuicao Principal
Estudo extenso de 622 desenvolvedores através de 3 empresas demostrando que produtividade auto-percebida é mais fortemente predita por fatores não-técnicos como variedade de tarefas, habilidade de trabalho remoto, entusiasmo e suporte dos pares, não por métricas técnicas objetivas. Desafia suposições convencionais sobre produtividade de desenvolvedores e sublinha importância de fatores de experiência do desenvolvedor sobre volume de código.

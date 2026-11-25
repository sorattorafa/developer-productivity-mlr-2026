# P0412 — Organizational Ohm's Law—Case in Point: Engineering Velocity

**Decisao: INCLUIDO | Qualidade: 4/5**

---

## Dados Bibliograficos

| Campo | Valor |
|-------|-------|
| **ID** | P0412 |
| **Autores** | Fei Liu, Todd McKinnon |
| **Ano** | 2024 |
| **Venue** | IEEE Transactions on Engineering Management, Vol. 71 |
| **DOI** | 10.1109/TEM.2023.3232311 |
| **Tipo** | Pesquisa conceitual com casos de estudo |
| **Metodo** | Análise teórica inspirada em Ohm's law da engenharia elétrica aplicada a organizações; casos reais de empresas (Okta, Microsoft, Google) e observações de autores |
| **Amostra** | Múltiplas organizações de software + >20 entrevistas com engenheiros, managers, product managers |
| **Contexto** | Organizações de software modernas com foco em velocidade de engenharia e DevOps |
| **Modo de trabalho** | Diversos (startups a grandes empresas) |

---

## Objetivo
Propor framework teórico usando conceito de Organizationl Ohm's Law para compreender produtividade organizacional em engenharia de software, decompondo resistência organizacional em componentes estruturais, processuais e infraestruturais, e fornecendo ferramenta para diagnosticar e otimizar velocidade de engenharia.

---

## Questoes de Pesquisa
- **RQ1**: Como aplicar Ohm's law à dinâmica organizacional em engenharia de software?
- **RQ2**: Como decompor resistência organizacional em componentes acionáveis?
- **RQ3**: Como usar o framework para melhorar velocidade de engenharia?

---

## Metricas e Instrumentos de Avaliacao
- **Framework**: Organizational velocity = f(organizational potential, organizational resistance), onde V = η × I_outcome / R_total
- **Componentes de resistência**: R_structure (resistência estrutural), R_process (resistência processual), R_infrastructure (resistência infraestrutural)
- **Medidas de potencial organizacional**: Habilidades, motivação dos indivíduos; cultura, autonomia
- **Medidas outcome-output**: Eficiência output-outcome; velocidade de entrega de features
- **Instrumentos**: Circuitos equivalentes de resistência, modelos analógicos com componentes em série/paralelo

---

## Resultados Principais
- **Decomposição de resistência**: Engineering velocity é função complexa de 3 resistências independentes (estrutura, processo, infraestrutura) que podem ser otimizadas separadamente
- **Trade-offs**: Introduzir novas equipes reduz output current (aumenta resistência); comunicação cross-team é custosa; estrutura centralizada vs. descentralizada tem trade-offs
- **Casos concretos**:
  - Okta exemplo de otimização de velocidade através de OKRs e goal-setting
  - Microsoft Word/PowerPoint: complexidade cross-team causa overhead significativo
  - Google best practices: cultura de inovação, colaboração, autonomia
- **Design organizacional**: Equipamentos independentes em paralelo maximizam velocidade; dependências criam resistência série

---

## Desafios do Uso das Metricas
- **Quantificação complexa**: Difícil mensurar quantitativamente cada componente de resistência em contextos reais
- **Interdependências**: Componentes não são verdadeiramente independentes; mudanças em um afetam outros
- **Variabilidade temporal**: Resistência organizacional evolui continuamente; captura snapshot é limitado
- **Context-dependence**: Ótimas práticas em uma organização podem ser resistências em outra
- **Fatores imponíveis**: Fatores externos (mercado, regulação) não capturados no modelo

---

## Contribuicao Principal
Introduz framework analógico inovador (inspirado em Ohm's law da física) para compreender e otimizar velocidade de engenharia em organizações de software através da decomposição sistemática de resistência organizacional em componentes estruturais, processuais e infraestruturais. O framework fornece linguagem comum e ferramenta mental para diagnosticar gargalos de produtividade, priorizar melhorias, e entender trade-offs em decisões de design organizacional. Aplicação em circuitos equivalentes permite visualização e análise de como mudanças em estrutura, processos e infraestrutura impactam resultado final (velocidade/produtividade).

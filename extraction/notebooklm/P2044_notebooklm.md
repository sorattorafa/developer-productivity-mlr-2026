# P2044 — Exploring machine learning to support software managers' insights on software developer productivity [1]

**Decisao: INCLUIDO | Qualidade: 4.5/5** [1-5]

---

## Dados Bibliograficos

| Campo | Valor |
|-------|-------|
| **ID** | P2044 [1] |
| **Autores** | Suwarno, Yefta Christian, Keaton Yoputra, Yuki Estrada [1] |
| **Ano** | 2025 [1] |
| **Venue** | **Journal of Applied Data Sciences** (Vol. 6, No. 3, pp. 1504–1524) [1] |
| **DOI** | https://doi.org/10.47738/jads.v6i3.661 [6] |
| **Tipo** | Journal article [1, 6] |
| **Metodo** | Mixed methods (Qualitative semi-structured interviews + Applied machine learning research using CRISP-DM) [2, 3, 7] |
| **Amostra** | **Qualitativo:** 12 gestores de software de 6 empresas privadas [2]; **Aplicado:** 2.190 screenshots e 3.563 entradas de texto/URLs (dados primários de empresa parceira + dataset secundário do Kaggle) [8-10] |
| **Contexto** | Industry — 6 empresas privadas de desenvolvimento de software na Indonésia (Batam, Medan e Jakarta) atuando nos domínios de ERP, Automação Industrial e Plataformas de Entrega [2, 11] |
| **Modo de trabalho** | Not specified (entrevistas realizadas via videoconferência online) [2] |
| **Metodologia** | Agile (Scrum, Extreme Programming / XP) [11] |

---

## Objetivo

The main objective of this study is to investigate how software developer productivity is defined and measured based on software managers' perspectives, identify key operational challenges (such as digital distractions), and explore applied Machine Learning (ML) solutions to help managers measure developer productivity more accurately and objectively by automatically classifying computer screenshots and accessed URL contents into work-related or non-work-related activities [7, 12-14].

---

## Questoes de Pesquisa

- **RQ1:** What is the definition of software developer productivity? [15]
- **RQ2:** How is software developer productivity measured? [15]

---

## Metricas e Instrumentos de Avaliacao

| Metrica | Categoria | Nivel | Como Coletada | Validada |
|---------|-----------|-------|---------------|----------|
| **On-time Task Completion** | Delivery / Quality | Individual / Team | Project management tools, daily standup tracking, and manager logs [16-18] | **Yes** (widely cited as primary indicator by 11/12 managers) [16, 19] |
| **Effective Working Hours / Work Duration Ratio** | Activity / Productivity | Individual | Automated screenshot and URL content classification via ML models [14, 20-22] | **Yes** (validated via ML experiments: 99.62% image accuracy, 88.50% text accuracy) [5, 23] |
| **Story Points Completed** | Delivery / Output | Individual / Team | Agile project management tools (e.g., Jira / Figma tracking) [20, 21, 24] | **Yes** (applied in task estimation and sprint planning) [21, 24] |
| **Code Contributions / Repository Activity** | Activity / Code-based | Individual | Version control tools (e.g., Git commit activity tracking) [20, 25] | **Partial** (acknowledged by managers, but noted as incomplete when used alone) [25, 26] |
| **Peer Feedback / Colleague Assessment** | Collaboration / DevEx | Individual / Team | Monthly peer feedback meetings and anonymous internal surveys [27] | **Yes** (used in Organizations C and E to assess team support) [27] |
| **Lines of Code (LOC)** | Activity / Code-based | Individual | IDE telemetry or automated repository analysis [25, 28] | **No** (identified in literature as misleading and prone to rewarding verbosity over quality) [26, 28] |
| **AI Suggestion Acceptance & Speedup Rate** | Productivity / Delivery | Individual | Telemetry from AI coding assistants (e.g., GitHub Copilot) [6, 13] | **Yes** (cited from empirical literature: 30% suggestion acceptance, 55.8% task speedup) [6, 13] |

---

## Frameworks e Metricas

### Frameworks Referenciados
- **SPACE Framework:** **REFERENCED** (cited in literature review [12] regarding multidimensional developer productivity assessment) [29].
- **CRISP-DM (Cross Industry Standard Process for Data Mining):** **APPLIED** (used as the core process model for data collection, preprocessing, model development, evaluation, and application) [3].
- **Agile Frameworks (Scrum & Extreme Programming):** **APPLIED** (used by all studied software houses for project delivery and sprint management) [11].

### Frameworks Propostos
- **Data-Driven Developer Productivity Measurement Framework:** A proposed web application framework (designed in Figma) that integrates automated background tracking of developer activity (classifying periodic computer screenshots using **EfficientNetV2B0** and URL/scraped web text using **SVC**) with story points completed to compute effective work duration and productivity percentages while preserving individual privacy through data anonymization [14, 21, 22].

---

## Fatores que Influenciam Produtividade

### Fatores Positivos
| Fator | Categoria |
|-------|-----------|
| **Adaptabilidade e aprendizado contínuo** (Adaptability to changing requirements and tech exploration) | Human [30] |
| **Habilidades de colaboração e suporte em equipe** (Workload re-allocation to prevent burnout near deadlines) | Organizational / Human [31, 32] |
| **Alinhamento com metas de negócios e restrições do projeto** (Understanding time, scope, and resource limits) | Organizational / Process [24, 33] |
| **Foco e gestão eficaz do tempo** (Maintaining focus during coding blocks) | Human [17, 33] |
| **Adoção de ferramentas assistidas por IA** (e.g., GitHub Copilot for auto-completion and task acceleration) | Technical [6, 13] |

### Fatores Negativos
| Fator | Categoria |
|-------|-----------|
| **Distrações digitais e alternância voluntária de tarefas** (Cyberloafing, non-work web browsing, self-initiated interruptions) | Technical / Human [12, 14, 33, 34] |
| **Métodos tradicionais e ineficientes de monitoramento** (Tedious daily reporting requests, direct observation overhead, human error/bias) | Process / Organizational [14, 18] |
| **Dependência de métricas simplistas e isoladas** (Over-reliance on Lines of Code or raw commit counts) | Process [26] |
| **Pressão de prazos e sobrecarga de trabalho sem suporte colaborativo** | Organizational / Process [32] |

---

## Papel da IA e Automacao

| Campo | Valor |
|-------|-------|
| **Usa IA/ML?** | **Yes** — Transfer learning deep learning models (EfficientNetV2B0, VGG16, InceptionV3, ResNet50V2) for screenshot image classification, and hyperparameter-tuned classical classifiers (SVC, Random Forest, Logistic Regression) for URL text classification [35-39]. |
| **Automação de coleta?** | **Yes** — Background desktop recording scripts capture periodic computer screenshots and URLs, scraping up to 1,000 words of web text content for automated TF-IDF feature extraction and work-relatedness classification [8, 14, 40, 41]. |
| **Impacto de IA na produtividade?** | **High** — Reduces administrative overhead and subjective bias in productivity measurement. Literature cited shows AI tools like GitHub Copilot achieve a 30% suggestion acceptance rate [6] and accelerate task completion by 55.8% [13]. The paper's developed ML models achieve up to 99.62% accuracy in classifying screenshot work activity [23]. |

---

## Resultados Principais

- **Definição de Produtividade em Gestão:** 11 dos 12 gestores entrevistados (91.7%) definem a produtividade do desenvolvedor como a conclusão de tarefas atribuídas dentro do prazo estipulado sem comprometer a qualidade do código [16, 19].
- **Desempenho no Classificador de Imagem (Screenshots):**
  - **EfficientNetV2B0** apresentou o melhor desempenho geral, alcançando **99.62% de acurácia**, **100% de precisão**, **100% de recall** e **1.00 de F1-score** após a fase inicial de treinamento (sem necessidade de fine-tuning), registrando o tempo de treinamento mais rápido (1.991 segundos / ~33 min) e menor uso de recursos [4, 23, 35, 42].
  - **VGG16** atingiu 99.11% de acurácia após fine-tuning, porém demandou mais de 5 horas de treinamento (19.359 segundos) [43, 44].
  - **ResNet50V2** alcançou 95.57% de acurácia e **InceptionV3** atingiu 92.66% de acurácia com fine-tuning [43, 44].
- **Desempenho no Classificador de Texto (URLs + Conteúdo Scraping):**
  - O algoritmo **Support Vector Classifier (SVC)** com kernel RBF e otimização de hiperparâmetros via GridSearchCV obtiveram o melhor resultado entre 7 classificadores testados, alcançando **88.50% de acurácia**, **89% de precisão**, **88% de recall** e **88% de F1-score** [5, 36, 45].
- **Validação com Gestores:**
  - O protótipo conceitual da aplicação web no Figma obteve **100% de aceitação e feedback positivo** dos gestores de software entrevistados para monitoramento objetivo de tempo efetivo e suporte à decisão [36, 46].

---

## Desafios do Uso das Metricas

- **Anti-padrão de Métricas Únicas (e.g., LOC):** Avaliar produtividade apenas por volume de linhas de código ou número de commits penaliza programadores que escrevem código conciso, reutilizável ou refinam arquiteturas complexas [26].
- **Inércia e Viés em Processos Manuais:** Pedir relatórios frequentes de status consome tempo útil de desenvolvimento e introduz erros humanos ou estimativas subjetivas [14, 18].
- **Dificuldade na Quantificação de Fatores Subjetivos:** Fatores cruciais como dinâmica de equipe, facilidade de colaboração, suporte a colegas e bem-estar do desenvolvedor dificilmente são capturados por métricas quantitativas tradicionais [27, 47].
- **Preocupações com Privacidade e Doutrina de Monitoramento:** Risco de rejeição pelos desenvolvedores caso o monitoramento pareça punitivo ou invasivo, reforçando a necessidade de anonimização de dados visualizados por gestores e controle voluntário de pausas [22, 41, 48].

---

## Avaliacao de Qualidade Metodologica

| Critério | Pontuação (0-2) | Justificativa |
|----------|----------------|---------------|
| **Objetivo claramente definido** | **2** | Apresenta objetivos claros e delimitados nas vertentes qualitativa e aplicada [7, 13, 46]. |
| **Metodologia adequada ao objetivo** | **2** | Combina análise temática de entrevistas semiestruturadas com o ciclo completo do CRISP-DM para ML [3, 7, 15]. |
| **Amostra/contexto descrito adequadamente** | **2** | Tabelas detalhadas (Tabelas 3 e 4) descrevem o perfil das 6 empresas e dos 12 gestores, além dos datasets de imagem e texto [9-11, 49]. |
| **Ameaças à validade discutidas** | **1** | Discute limitações e direções futuras na conclusão, porém sem uma seção dedicada exclusiva a ameaças à validade [47, 48]. |
| **Resultados com evidência suficiente** | **2** | Apresenta métricas detalhadas de avaliação, matrizes de confusão, curvas de aprendizado e tempos de execução [4, 5, 44, 50]. |
| **Contribuição clara para prática ou teoria** | **2** | Oferece modelos treinados práticos e um design conceitual de sistema web validado por gestores da indústria [36, 46, 51]. |
| **TOTAL** | **11/12** | **Qualidade Metodológica Excelente (4.5 / 5)** [3-5, 7] |

---

## Limitacoes

- **Tamanho e Abrangência Geográfica da Amostra Qualitativa:** A fase de entrevistas baseou-se em 12 gestores de 6 empresas privadas situadas na Indonésia (Batam, Medan e Jakarta), o que pode restringir a generalização direta para multinacionais ou outras culturas organizacionais [2].
- **Volume e Sobreposição do Dataset de Texto:** O dataset de conteúdo de texto utilizou dados secundários do Kaggle e raspagem limitada a 1.000 palavras por URL, apresentando leve sinais de overfitting no modelo SVC e necessidade de maior volume de dados [5, 8, 40, 52].
- **Modelagem de Texto Clássica:** O estudo avaliou apenas classificadores tradicionais de aprendizado de máquina para texto, deixando arquiteturas profundas ou Transformers (como BERT e LLMs) para trabalhos futuros [47, 53].
- **Fatores Subjetivos Não Cobertos pelo Algoritmo:** Métricas de visão e navegação não mensuram aspectos qualitativos como saúde mental, nível de estresse, criatividade e clima organizacional [47, 48].

---

## Contribuicao Principal

A principal contribuição deste trabalho consiste em integrar percepções empíricas de gestores de software com uma solução prática e orientada a dados baseada em Machine Learning para medição objetiva da produtividade de desenvolvedores [7, 12, 36, 51]. O artigo preenche uma lacuna crítica ao superar tanto a ineficiência de relatórios manuais quanto a imprecisão de métricas isoladas (como linhas de código), demonstrando a viabilidade técnica de modelos de visão computacional (**EfficientNetV2B0** com 99.62% de acurácia) e processamento de texto (**SVC** com 88.50% de acurácia) para identificar distrações digitais [5, 14, 23, 35, 36]. Além disso, articula esses modelos em uma proposta conceitual de aplicação web com foco na preservação de privacidade, oferecendo uma abordagem equilibrada para apoiar gestores na tomada de decisões e na otimização da gestão de projetos [21, 22, 51].

---

*Extraido via NotebookLM em October 2026 para MLR: Software Developer Metrics in Practice* [1]

---

💡 **Sugestão de Próximo Passo:** Se você deseja aprofundar essa análise, posso criar um relatório comparativo detalhado ou um mapa mental sintetizando as métricas de produtividade tradicionais versus as abordagens automatizadas por IA apresentadas no estudo. Como gostaria de prosseguir?
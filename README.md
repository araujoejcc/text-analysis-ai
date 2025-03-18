Análise de Sentimentos com IA
Este projeto demonstra a aplicação de técnicas de Processamento de Linguagem Natural (NLP) para análise de sentimentos em textos, utilizando bibliotecas de IA como NLTK.
📋 Visão Geral
O projeto analisa textos para determinar se expressam sentimentos positivos, negativos ou neutros, criando visualizações e relatórios detalhados dos resultados.
🚀 Estrutura do Projeto
Copiar/
├── inputs/          # Contém os arquivos de texto para análise
├── src/             # Código fonte do analisador
├── results/         # Resultados da análise (gráficos e relatórios)
└── README.md        # Este arquivo
💻 Tecnologias Utilizadas

Python 3.8+
NLTK (Natural Language Toolkit)
Pandas para manipulação de dados
Matplotlib para visualizações
VADER SentimentIntensityAnalyzer para análise de sentimentos

⚙️ Como Executar

Clone este repositório:
bashCopiargit clone https://github.com/seu-usuario/nome-do-repositorio.git
cd nome-do-repositorio

Instale as dependências:
bashCopiarpip install nltk pandas matplotlib

Execute o analisador:
bashCopiarpython src/analyzer.py

Verifique os resultados na pasta results/

📊 Resultados
Visualização da Análise de Sentimentos
Mostrar Imagem
A imagem acima mostra a pontuação composta de sentimento para cada sentença analisada. Valores positivos (verdes) indicam sentimentos positivos, enquanto valores negativos (vermelhos) indicam sentimentos negativos.
Mostrar Imagem
Esta visualização mostra a decomposição das pontuações em suas componentes positiva, negativa e neutra.
Relatório de Análise
O relatório completo pode ser encontrado em results/analysis_results.md, contendo valores precisos para cada componente da análise.
🧠 Insights
Durante o desenvolvimento deste projeto, observei alguns padrões interessantes:

Ambiguidade Contextual: Algumas frases que parecem neutras para humanos podem ser classificadas como levemente positivas ou negativas pelo algoritmo.
Impacto de Palavras-Chave: Palavras como "muito", "extremamente" e "revolucionar" têm um forte impacto na polaridade detectada.
Limitações de Análise Simples: A análise de sentimentos puramente léxica não captura nuances como ironia ou sarcasmo.

🔍 Possibilidades de Expansão
Este projeto pode ser expandido de várias maneiras:

Análise Multilíngue: Adaptar o analisador para processar textos em diferentes idiomas.
Modelos Mais Avançados: Implementar modelos baseados em transformers como BERT ou GPT para análise mais precisa.
Análise de Tópicos: Além do sentimento, identificar os tópicos principais abordados nos textos.
Interface Web: Desenvolver uma interface que permita aos usuários submeter textos para análise em tempo real.
Análise em Tempo Real: Conectar a APIs de redes sociais para analisar sentimentos em tempo real sobre determinados assuntos.

📚 Referências

NLTK Documentation
VADER Paper
Sentiment Analysis Overview

📝 Licença
Este projeto está sob a licença MIT.

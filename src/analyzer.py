import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt
import pandas as pd
import os

# Download recursos necessários
nltk.download('vader_lexicon')

def analyze_sentiment(text):
    """
    Analisa o sentimento de um texto usando VADER SentimentIntensityAnalyzer
    """
    sia = SentimentIntensityAnalyzer()
    return sia.polarity_scores(text)

def generate_report(sentences, results):
    """
    Gera um relatório de análise de sentimentos
    """
    report = "# Resultado da Análise de Sentimentos\n\n"
    report += "| Sentença | Positivo | Negativo | Neutro | Composto |\n"
    report += "|----------|----------|----------|--------|----------|\n"
    
    for i, (sentence, result) in enumerate(zip(sentences, results)):
        report += f"| {sentence[:30]}... | {result['pos']:.3f} | {result['neg']:.3f} | {result['neu']:.3f} | {result['compound']:.3f} |\n"
    
    return report

def plot_sentiment_scores(sentences, results):
    """
    Gera gráficos para visualizar os resultados
    """
    # Preparar dados
    df = pd.DataFrame(results)
    df['sentence'] = [s[:20] + "..." for s in sentences]
    
    # Criar pasta results se não existir
    os.makedirs('results', exist_ok=True)
    
    # Gráfico de barras para valores compostos
    plt.figure(figsize=(12, 6))
    plt.bar(df['sentence'], df['compound'], color=['green' if x > 0 else 'red' for x in df['compound']])
    plt.xlabel('Sentenças')
    plt.ylabel('Pontuação Composta')
    plt.title('Análise de Sentimento - Pontuação Composta')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig('results/compound_scores.png')
    
    # Gráfico para componentes pos/neg/neu
    plt.figure(figsize=(12, 6))
    
    x = range(len(sentences))
    width = 0.25
    
    plt.bar([i - width for i in x], df['pos'], width=width, label='Positivo', color='green')
    plt.bar(x, df['neu'], width=width, label='Neutro', color='gray')
    plt.bar([i + width for i in x], df['neg'], width=width, label='Negativo', color='red')
    
    plt.xlabel('Sentenças')
    plt.ylabel('Pontuação')
    plt.title('Análise Detalhada de Sentimentos')
    plt.xticks(x, df['sentence'], rotation=45, ha='right')
    plt.legend()
    plt.tight_layout()
    plt.savefig('results/detailed_scores.png')

def main():
    # Ler sentenças do arquivo
    with open('inputs/sentences.txt', 'r', encoding='utf-8') as file:
        sentences = [line.strip() for line in file if line.strip()]
    
    # Analisar sentimentos
    results = [analyze_sentiment(sentence) for sentence in sentences]
    
    # Gerar relatório
    report = generate_report(sentences, results)
    with open('results/analysis_results.md', 'w', encoding='utf-8') as file:
        file.write(report)
    
    # Gerar gráficos
    plot_sentiment_scores(sentences, results)
    
    print("Análise concluída! Verifique a pasta 'results' para os resultados.")

if __name__ == "__main__":
    main()

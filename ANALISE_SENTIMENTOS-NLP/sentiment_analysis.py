import pandas as pd
from textblob import TextBlob
import matplotlib.pyplot as plt

df = pd.read_csv('data/posts.csv')

def analisar_sentimento(texto):
    return TextBlob(texto).sentiment.polarity

df['sentimento'] = df['post'].apply(analisar_sentimento)

df['sentimento'].hist()
plt.title('Distribuição de Sentimentos')
plt.show()
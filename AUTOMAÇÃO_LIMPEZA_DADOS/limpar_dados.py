import pandas as pd
import numpy as np

df = pd.read_csv('data/dados_brutos.csv')

df.drop(columns=['coluna1', 'coluna2'], inplace=True)
df.fillna({'idade': df['idade'].mean()}, inplace=True)
df['nome'] = df['nome'].str.title()
df.to_csv('data/dados_limpos.csv', index=False)
print('Dados limpos e salvos com sucesso!')
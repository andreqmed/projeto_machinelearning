import pandas as pd

#Metodos:

def carregar_dataframe(caminho_dados):
    return pd.read_csv(caminho_dados)

def rename(df):
    df.rename(columns = {'style':'tipo'}, inplace = True)

    df['tipo'] = df['tipo'].replace('red',0)
    df['tipo'] = df['tipo'].replace('white',1)
    
    return df

df = rename(carregar_dataframe('data/wine_dataset.csv'))



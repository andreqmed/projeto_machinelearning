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

'''
import pandas as pd
import numpy as np

#Metodos:

def carregar_dataframe(caminho_dados):
    return pd.read_csv(caminho_dados)

def largura(df):
    return pd.set_option('display.max_columns', 100)

def rename(df):
    df.rename(columns =
              {'style':'tipo','fixed_acidity':'Acidez_fixa','volatile_acidity':'Acidez_volatil','citric_acid':'Acido_citrico','residual_sugar':'Açucar_residual','chlorides':'cloretos','free_sulfur_dioxide':'SO2_livre',
               'total_sulfur_dioxide':'total_de_SO2','density':'Densidade','sulphates':'Sulfatos','alcohol':'álcool','quality':'qualidade'}, inplace =True)

    df['tipo'] = df['tipo'].replace('red',0)
    df['tipo'] = df['tipo'].replace('white',1)
    
    return df

df = rename(carregar_dataframe('wine_dataset.csv'))
largura(df)
caracteristicas = np.array([df.columns])
print(caracteristicas)
# print(caracteristicas.size)
'''

import pandas as pd
import numpy as np

#Metodos:
def carregar_dataframe(caminho_dados):
    return pd.read_csv(caminho_dados)

def largura(df):
    return pd.set_option('display.max_columns', None)

def rename(df):
    df.rename(columns =
              {'style':'tipo','fixed_acidity':'Acidez_fixa','volatile_acidity':'Acidez_volatil','citric_acid':'Acido_citrico','residual_sugar':'Açucar_residual','chlorides':'cloretos','free_sulfur_dioxide':'SO2_livre',
               'total_sulfur_dioxide':'total_de_SO2','density':'Densidade','sulphates':'Sulfatos','alcohol':'alcool','quality':'qualidade'}, inplace =True)

    df['tipo'] = df['tipo'].replace('red',0)
    df['tipo'] = df['tipo'].replace('white',1)
    
    return df

def criando_vinho():
    valores_base = df.mean(numeric_only=True)

    print("Personalize seu vinho:")
    acidez_fixa = float(input(f"Acidez fixa (normal: {valores_base['Acidez_fixa']:.2f}): "))
    acidez_volatil = float(input(f"Acidez volátil (normal: {valores_base['Acidez_volatil']:.2f}): "))
    acido_citrico = float(input(f"Ácido cítrico (normal: {valores_base['Acido_citrico']:.2f}): "))
    acucar_residual = float(input(f"Açúcar residual (normal: {valores_base['Açucar_residual']:.2f}): "))
    cloretos = float(input(f"Cloretos (normal: {valores_base['cloretos']:.2f}): "))
    pH = (input(f"pH (normal: {valores_base['pH']:.2f}): "))
    SO2_livre = float(input(f"SO2 livre (normal: {valores_base['SO2_livre']:.2f}): "))
    total_de_SO2 = float(input(f"Total de SO2 (normal: {valores_base['total_de_SO2']:.2f}): "))
    Densidade = float(input(f"Densidade (normal: {valores_base['Densidade']:.5f}): "))
    Sulfatos = float(input(f"Sulfatos (normal: {valores_base['Sulfatos']:.2f}): "))
    alcool = float(input(f"alcool (normal: {valores_base['alcool']:.2f}): "))
    qualidade = float(input(f"Qualidade (normal: {valores_base['qualidade']:.2f}): "))
            
    novo_vinho = pd.DataFrame([{
    'Acidez_fixa': acidez_fixa,
    'Acidez_volatil': acidez_volatil,
    'Acido_citrico': acido_citrico,
    'Açucar_residual': acucar_residual,
    'cloretos': cloretos,
    'pH':pH,
    'SO2_livre': SO2_livre,
    'total_de_SO2':total_de_SO2,
    'Densidade':Densidade,
    'Sulfatos':Sulfatos,
    'alcool': alcool,
    'qualidade':qualidade}])

    return novo_vinho
    

df = rename(carregar_dataframe('data/wine_dataset.csv'))
largura(df)
caracteristicas = np.array([df.columns])




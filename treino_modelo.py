import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.ensemble import ExtraTreesClassifier                                    
from preprocessamento import df   

#|Separando entre variaveis alvo(y) e preditora(x)
def modelo_treino():
    y = df['tipo']
    X = df.drop('tipo', axis = 1)
    #MODELO TREINO
    X_treino,X_teste,y_treino,y_teste = train_test_split(X,y,test_size = 0.3)
    modelo = ExtraTreesClassifier(random_state = 1)
    modelo.fit(X_treino,y_treino)
    return modelo,X_teste,y_teste




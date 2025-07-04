from data.preprocessamento import df
from src.treino_modelo import modelo_treino
import pandas as pd
from sklearn.model_selection import train_test_split

def main():
    modelo, X_teste, y_teste = modelo_treino()
    resultado = modelo.score(X_teste, y_teste)

    print(f'Acuracia do modelo é de:{resultado:.2%}\n')
    
    print("Exemplo de predição:")
    # print(modelo.predict(X_teste))
    print(X_teste[400:403])
    print(y_teste[400:403])
    previsoes = modelo.predict(X_teste[400:403])
    print(previsoes)

if __name__ == "__main__":
    main()

'''
from preprocessamento import df
from preprocessamento import caracteristicas
from treino_modelo import modelo_treino
import pandas as pd
from sklearn.model_selection import train_test_split
import numpy as np


def main():
    modelo, X_teste, y_teste = modelo_treino()
    resultado = modelo.score(X_teste, y_teste)

    while True:
        print("\t\t MENU DE VINHOS\n")
        print("1- Ver exemplo de predição\n")
        print("2- Comparar vinhos por caracteristicas\n")
        print("3- Personalize as caracteristicas do seu vinho, e você saberá se ele é tinto ou vermelho  ")
        print("4- Mostrar acurácia do modelo\n")

        escolha = int(input("escolha uma opção\n"))
        
        
        if(escolha == 1):
            print("Exemplo de predição:")
            #print(modelo.predict(X_teste)
            print(X_teste[400:403])
            print("Os resultados são")
            print(y_teste[400:403].values)
            previsoes = modelo.predict(X_teste[400:403])
            print(f'{previsoes}Predição:0 é vinho vermelho e 1 tinto \n')
        
        elif(escolha == 2):
            lista_indices = [2]
            
            lista_indices = input("Digite os índice dos vinho\n")

            vinhos_escolhidos = X_teste.iloc[lista_indices]
            previsoes = modelo.predict(vinhos_escolhidos)
            for idx,pred in zip(lista_indices,previsoes):
                 tipo = "Tinto (0)" if pred == 0 else "Branco (1)"
            print(f"📌 Vinho {idx} → Previsão: {tipo}")
            print(X_teste.iloc[idx])
        
'''

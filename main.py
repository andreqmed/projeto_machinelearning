from preprocessamento import df
from preprocessamento import caracteristicas
from preprocessamento import criando_vinho
from treino_modelo import modelo_treino
import pandas as pd
from sklearn.model_selection import train_test_split
import numpy as np
from IPython.display import display

def main():
    modelo, X_teste, y_teste = modelo_treino()
    resultado = modelo.score(X_teste, y_teste)

    while True:
        print("\t\t MENU DE VINHOS\n")
        print("1- Ver exemplo de predição\n")
        print("2- Comparar 2 vinhos\n")
        print("3- Personalize as características do seu vinho (acidez, teor alcoólico, pH e mais). Descubra se ele seria um vinho tinto ou branco!\n")
        print("4- Mostrar acurácia do modelo\n")
        print("5 - Sair\n")
        escolha = int(input("escolha uma opção\n\n"))
        
        if(escolha == 1):
            print("Os vinhos a serem analisados são:\n")
            display(f'{X_teste[400:403]}\n')
            previsoes = modelo.predict(X_teste[400:403])
            print("O modelo previu os seguintes resultados:\n")
            for prev in previsoes:
                if(prev == 0):
                    tipo = 'Tinto(0)'
                   
                else:
                    tipo = 'Branco(1)'
                print(f'Vinho -> {tipo}\n')
            
            print("Os resultados corretos são:\n")
            resposta = y_teste[400:403].values
            for resp in resposta:
                if(resp == 0):
                    tipo = 'Tinto(0)'
                else:
                    tipo = 'Branco(1)'
                print(f"Vinho -> {tipo}\n")  
            
        elif(escolha == 2):
            lista_indices = []
            for idx in range(2):
                idx = int(input("Digite os índice dos vinho\n"))
                lista_indices.append(idx)
            
            vinhos_escolhidos = X_teste.iloc[lista_indices]
            previsoes = modelo.predict(vinhos_escolhidos)
            
            for idx,pred in zip(lista_indices,previsoes):
                if(pred == 0):
                    tipo = 'Tinto(0)'
                   
                else:
                    tipo = 'Branco(1)'
                     
                print(f"📌 Vinho {idx} → Previsão: {tipo}\n")
                print(X_teste.iloc[idx])
            
        elif(escolha == 3):
            novo_vinho = criando_vinho()  
            novo_vinho = novo_vinho[modelo.feature_names_in_]
            previsao = modelo.predict(novo_vinho)
            if previsao == 0:
                tipo = 'Tinto(0)'
            else:
                tipo = 'Branco(1)'
            print(f'Seu vinho seria classificado como:{tipo}\n')
            
        elif(escolha == 4):
            print(f'Acuracia do modelo é de:{resultado:.2%}\n')

        elif(escolha == 5):
            print("Programa encerrado\n")
            break
            
        
    

    
    
if __name__ == "__main__":
    main()

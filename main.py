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
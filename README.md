🧠 Projeto: Classificação de Vinhos com Machine Learning
Este projeto aplica conceitos básicos de Machine Learning (ML) para classificar vinhos como tintos (red) ou brancos (white) com base em suas características químicas, utilizando um dataset com amostras reais.

📄 Sobre o Projeto
O objetivo é treinar um modelo de aprendizado de máquina para identificar automaticamente o tipo de vinho com base em suas propriedades, como acidez, teor alcoólico, açúcar residual, entre outras.

O projeto está dividido em três partes principais:

1-Pré-processamento (src/preprocessamento.py):
-->Carrega o dataset.
-->Altera os nomes das colunas para um formato mais padronizado.
-->Converte o valor da coluna tipo (red ou white) em valores numéricos (0 e 1).
-->Deixa os dados prontos para serem usados no modelo.

2-Treinamento do Modelo (src/treino_modelo.py)
-->Utiliza o algoritmo ExtraTreesClassifier do Scikit-learn.
-->Separa os dados em treino e teste.
-->Treina o modelo com os dados processados.

3-Execução Principal (main.py)
-->Executa o treinamento e faz previsões.
-->Exibe a acurácia do modelo.
-->Mostra exemplos de predições reais.

📌 Resultados Esperados
O modelo será treinado e exibirá:
A acurácia da classificação
Um exemplo de previsão com os primeiros dados de teste

📈 Melhorias Futuras (Ideias)
Testar outros algoritmos (RandomForest, KNN, SVM, etc.)
Fazer análise exploratória (gráficos, estatísticas)
Usar validação cruzada
Criar uma API para o modelo
Interface Web simples com Streamlit

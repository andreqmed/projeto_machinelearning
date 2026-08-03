# 🍷 Classificação de Vinhos com Machine Learning
Aplicação que utiliza Machine Learning para classificar vinhos como **tintos (red)** ou **brancos (white)** com base em suas características químicas, usando um dataset com amostras reais.

---

## ✨ Funcionalidades
- Pré-processamento automático do dataset  
  - Padroniza nomes das colunas  
  - Converte o tipo de vinho em valores numéricos (0 e 1)  
- Treinamento de modelo com **ExtraTreesClassifier**  
  - Separação entre dados de treino e teste  
  - Avaliação da acurácia do modelo  
- Execução principal do projeto  
  - Faz previsões com dados de teste  
  - Exibe acurácia e exemplos de previsões reais  

---

## 🛠️ Tecnologias Utilizadas
- Python 3.x  
- **Scikit-learn** – Algoritmos de Machine Learning  
- **Pandas** – Manipulação de dados  
- **NumPy** – Operações matemáticas  
- **Matplotlib / Seaborn** *(opcional para análise exploratória)*  

---

## 📦 Estrutura do Projeto

```text
Wine_Classification/
├── data/
│   └── wine_dataset.csv
├── models/
├── notebooks/
│   └── analise_exploratoria.ipynb
├── src/
│   ├── main.py
│   ├── preprocessamento.py
│   └── treino_modelo.py
├── README.md
├── requirements.txt
└── .gitignore
```

---

## 📓 Análise Exploratória

O projeto inclui o notebook `notebooks/analise_exploratoria.ipynb`, que apresenta as principais etapas da análise exploratória do conjunto de dados, incluindo:

- Visualização das primeiras linhas do dataset;
- Informações e estatísticas descritivas;
- Verificação de valores ausentes;
- Distribuição dos tipos de vinho;
- Pré-processamento dos dados;
- Treinamento do modelo ExtraTreesClassifier;
- Avaliação da acurácia;
- Exemplo de predições realizadas pelo modelo.

O notebook complementa a aplicação desenvolvida em `src/`, documentando o processo de análise e treinamento do modelo de Machine Learning.

---


## 📦 Como executar localmente

## 🖥️ Clonando o projeto
```bash
git clone https://github.com/seuusuario/ClassificacaoVinhos.git
cd ClassificacaoVinhos
```
## 🔧 1. Instalando dependências

Pré-requisitos: Python 3.x e pip

pip install -r requirements.txt

## 🚀 2. Rodando o projeto
python main.py

O script executa o pré-processamento, treina o modelo e exibe a acurácia.

Mostra exemplos de previsões com os primeiros dados de teste.

---

## 📈 Melhorias Futuras

Testar outros algoritmos: RandomForest, KNN, SVM

Realizar análise exploratória: gráficos e estatísticas

Aplicar validação cruzada

Criar uma API para o modelo

Desenvolver interface web simples com Streamlit


---


## 📊 Resultados

O modelo foi treinado utilizando o algoritmo **ExtraTreesClassifier** da biblioteca Scikit-learn.

Após o treinamento, o modelo apresentou alta acurácia na classificação de vinhos tintos e brancos, demonstrando que as características físico-químicas do dataset são suficientes para distinguir os dois tipos de vinho com excelente desempenho.

---

## 👥 Autores

Desenvolvido por André Queiroz como projeto de Machine Learning.

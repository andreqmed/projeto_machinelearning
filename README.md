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

ClassificacaoVinhos/
├── src/
│ ├── preprocessamento.py # Pré-processamento do dataset
│ └── treino_modelo.py # Treinamento do modelo ML
├── main.py # Execução principal
├── data/ # Dataset de vinhos (CSV)
└── README.md


---

## 📦 Como executar localmente

### 🖥️ Clonando o projeto
bash
git clone https://github.com/seuusuario/ClassificacaoVinhos.git
cd ClassificacaoVinhos

###🔧 1. Instalando dependências

Pré-requisitos: Python 3.x e pip

pip install -r requirements.txt

###🚀 2. Rodando o projeto
python main.py

O script executa o pré-processamento, treina o modelo e exibe a acurácia.

Mostra exemplos de previsões com os primeiros dados de teste.

📈 Melhorias Futuras

Testar outros algoritmos: RandomForest, KNN, SVM

Realizar análise exploratória: gráficos e estatísticas

Aplicar validação cruzada

Criar uma API para o modelo

Desenvolver interface web simples com Streamlit

👥 Autores

Desenvolvido por André Queiroz como projeto de Machine Learning.

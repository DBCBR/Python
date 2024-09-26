import pandas as pd  # Importa a biblioteca pandas
import numpy as np  # Importa a biblioteca numpy
from sklearn.model_selection import train_test_split  # Importa a função train_test_split da biblioteca sklearn
from sklearn.preprocessing import LabelEncoder  # Importa a função LabelEncoder da biblioteca sklearn
from sklearn.metrics import confusion_matrix, accuracy_score  # Importa as funções confusion_matrix e accuracy_score da biblioteca sklearn
from sklearn.ensemble import RandomForestClassifier  # Importa a função RandomForestClassifier da biblioteca sklearn
from sklearn.tree import export_graphviz  # Importa a função export_graphviz da biblioteca sklearn
import pydotplus  # Importa a biblioteca pydotplus
from IPython.display import Image  # Importa a função Image da biblioteca IPython.display

# Lê o arquivo Credit.csv e armazena na variável credito
credito = pd.read_csv('Credit.csv')

# Cria um objeto LabelEncoder
labelencoder = LabelEncoder()

# Para cada coluna do tipo object do dataframe credito
for coluna in credito.select_dtypes(include='object'):
    # Se a coluna for diferente de 'class'
    if coluna != 'class':
        # Transforma os valores da coluna em valores numéricos e armazena na própria coluna do dataframe credito
        credito[coluna] = labelencoder.fit_transform(credito[coluna])

# Armazena os valores das colunas de 0 a 19 do dataframe credito na variável previsores
previsores = credito.iloc[:, 0:20].values

# Armazena os valores da coluna 20 do dataframe credito na variável classe
classe = credito.iloc[:, 20].values

# Divide os dados de previsores e classe em dados de treinamento e teste
x_treinamento, x_teste, y_treinamento, y_teste = train_test_split(previsores, classe, test_size=0.3, random_state=0)

# Cria um objeto RandomForestClassifier
floresta = RandomForestClassifier(n_estimators=500, random_state=0)

# Treina o modelo
floresta.fit(x_treinamento, y_treinamento)

# Realiza as previsões
previsoes = floresta.predict(x_teste)

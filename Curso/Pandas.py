# #Pandas 
# #Pandas é uma biblioteca de software escrita como extensão da linguagem de programação Python para manipulação e análise de dados.
# #Oferece estruturas de dados e ferramentas para manipulação de dados estruturados e tabulares.
# #Pandas é uma ferramenta muito poderosa para manipulação de dados em Python.
# #Pandas é construído sobre a biblioteca NumPy.
# #Pandas é usado para manipulação de dados, limpeza de dados e análise de dados.

# import pandas as pd

# pd.Series([1,2,3,4,5]) #criando uma série
# print(pd.Series([1,2,3,4,5])) #imprimindo a série
# print(pd.Series([1,2,3,4,5], dtype='i4')) #imprimindo a série com o tipo de dados inteiros de 4 bytes
# print(pd.Series([1,2,3,4,5], dtype='i4', name="Meus números")) #imprimindo a série com o tipo de dados inteiros de 4 bytes e nomeando a série
# print(pd.Series([1,2,3,4,5], dtype='i4', name="Meus números", index=['a','b','c','d','e'])) #imprimindo a série com o tipo de dados inteiros de 4 bytes, nomeando a série e indexando a série
# minha_serie = pd.Series([1,2,3,4,5], dtype='i4', name="Meus números", index=['Um','Dois','Três','Quatro','Cinco']) #criando uma série
# print(minha_serie) #imprimindo a série
# print(minha_serie['Um']) #imprimindo o valor do índice 'a' da série
# print(minha_serie.shape) #imprimindo a forma da série
# minha_serie['Seis'] = 6 #adicionando um novo valor ao índice 'f' da série
# print(minha_serie) #imprimindo a série
# print('-'*20)

# import pandas as pd #importando a biblioteca pandas
# import numpy as np #importando a biblioteca numpy

# array = np.array([37, 35, 10, 5]) #criando um array
# pesos = pd.Series(array, index=['David', 'Paula', 'Yasmin', 'Aurora']) #criando uma série
# print(pesos) #imprimindo a série
# print(type(pesos)) #imprimindo o tipo da série
# print('-'*20)

# #DataFrame
# #DataFrame é uma estrutura de dados bidimensional, tabular e heterogênea, composta por linhas e colunas rotuladas.
# #DataFrame é uma estrutura de dados muito poderosa para manipulação de dados em Python.
# #DataFrame é construído sobre a biblioteca NumPy.
# #DataFrame é usado para manipulação de dados, limpeza de dados e análise de dados.

# import pandas as pd #importando a biblioteca pandas
# nomes = ['David', 'Paula', 'Yasmin', 'Aurora'] #criando uma lista
# data_frame = pd.DataFrame(nomes) #criando um DataFrame
# print(data_frame) #imprimindo o DataFrame 
# print('-'*20)

# import pandas as pd
# numeros = [['11', '12', '13', '14'], #criando uma lista de listas 
#            ['21', '22', '23', '24'], 
#            ['31', '32', '33', '34'], 
#            ['41', '42', '43', '44']
#            ]
# data_frame = pd.DataFrame(numeros, columns=['A', 'B', 'C', 'D'], index=['x', 'y', 'z', 'w']) #criando um DataFrame
# print(data_frame) #imprimindo o DataFrame
# print('-'*20)

# #DataFrame com dicionário

# import pandas as pd 

# dados ={ #criando um dicionário
#         'Idade': [37, 35, 10, 5],
#         'Profissão': ['Programador', 'Enfermeira', 'Estudante', 'Estudante']
#         }
# data_frame = pd.DataFrame(dados, index = ['David', 'Paula', 'Yasmin', 'Aurora']) #criando um DataFrame
# print(data_frame) #imprimindo o DataFrame 
# print(data_frame.loc['David']) #imprimindo o índice 'David' do DataFrame
# print('-'*20)

#Importando dados 
#Pandas é uma biblioteca de software escrita como extensão da linguagem de programação Python para manipulação e análise de dados.
#Oferece estruturas de dados e ferramentas para manipulação de dados estruturados e tabulares.

import pandas as pd #importando a biblioteca pandas
data = pd.read_csv('pessoas.csv', index_col='Nome') #lendo um arquivo csv
# print(data) #imprimindo o DataFrame
# len(data.columns) #imprimindo o número de colunas do DataFrame
# print(data.columns) #imprimindo as colunas do DataFrame
# print(data.index) #imprimindo os índices do DataFrame
# print(data.dtypes) #imprimindo os tipos de dados do DataFrame
# print(data.shape) #imprimindo a forma do DataFrame
# print(data.describe()) #imprimindo a descrição do DataFrame

for indice, linha in data.iterrows(): #iterando sobre o DataFrame
    print(indice, linha[0], linha[1], linha[2]) #imprimindo o índice e as linhas do DataFrame
print('-'*20)
    
for coluna in data: #iterando sobre as colunas do DataFrame
    print(coluna) #imprimindo as colunas do DataFrame
print('-'*20)
    
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

# import pandas as pd #importando a biblioteca pandas
# data = pd.read_csv('pessoas.csv', index_col='Nome') #lendo um arquivo csv
# print(data) #imprimindo o DataFrame
# print('-'*20)
# len(data.columns) #imprimindo o número de colunas do DataFrame
# print(data.columns) #imprimindo as colunas do DataFrame
# print(data.index) #imprimindo os índices do DataFrame
# print(data.dtypes) #imprimindo os tipos de dados do DataFrame
# print(data.shape) #imprimindo a forma do DataFrame
# print(data.describe()) #imprimindo a descrição do DataFrame

# for indice, linha in data.iterrows(): #iterando sobre o DataFrame
#     print(indice, linha[0], linha[1], linha[2]) #imprimindo o índice e as linhas do DataFrame
# print('-'*20)
    
# for coluna in data: #iterando sobre as colunas do DataFrame
#     print(coluna) #imprimindo as colunas do DataFrame
# print('-'*20)

# #Acessando Valores Individuais e Slicing

# print(data.loc['Roger']['Idade']) #imprimindo o valor da linha 'Roger' e coluna 'Idade'
# print(data.loc['Roger'].iloc[0]) #imprimindo o valor da linha 'Roger' e coluna 'Idade'
# print('-'*20)

# print(data.loc['Roger']) #imprimindo a linha 'Roger'
# print(type(data.loc['Roger'])) #imprimindo o tipo da linha 'Roger'
# print('-'*20)

# print(data.loc['Cristiano':'Jeferson'])
# print(data.iloc[1:4])
# print('-'*20)

# print(data['Idade']) #imprimindo a coluna 'Idade'
# print('-'*20)
# print(data['Idade']['Roger']) #imprimindo o valor da linha 'Roger' e coluna 'Idade'
# print('-'*20)
# print(data[['Idade', 'Profissão']]) #imprimindo as colunas 'Idade' e 'Profissão'
# print('-'*20)

# colunas = data[['Idade', 'Profissão']] #criando um DataFrame com as colunas 'Idade' e 'Profissão'
# print(type(colunas)) #imprimindo o tipo do DataFrame
# print('-'*20)

# print(data) #imprimindo o DataFrame
# print('-'*20)

# colunas = data.iloc[:,1:3] #criando um DataFrame com as colunas 1 e 2
# print(colunas) #imprimindo o DataFrame
# print('-'*20)

# colunas = data.loc[:,'Idade':'Profissão'] #criando um DataFrame com as colunas 'Idade' e 'Profissão'
# print(colunas) #imprimindo o DataFrame
# print('-'*20)

#Máscaras
#Máscara é uma matriz de valores booleanos para filtrar dados.
#Máscara é uma maneira de filtrar dados em um DataFrame.

# mask = data['Idade'] < 50 #criando uma máscara para filtrar dados menores que 50
# print(mask) #imprimindo a máscara
# print('-'*20)

# nova_dframe = data[mask] #criando um novo DataFrame com a máscara
# print(nova_dframe) #imprimindo o novo DataFrame
# print('-'*20)

# nova_dframe2 = data[(data['Idade']>40)&(data['Altura']>1.75)] #criando um novo DataFrame com a máscara
# print(nova_dframe2) #imprimindo o novo DataFrame
# print('-'*20)

# #Alterando Valores

# data.at['Roger', 'Idade'] = 50 #alterando o valor da linha 'Roger' e coluna 'Idade' para 50
# print(data) #imprimindo o DataFrame
# print('-'*20)

# data.iat[2,0] = 100 #alterando o valor da linha 2 e coluna 0 para 100
# print(data) #imprimindo o DataFrame
# print('-'*20)

# data.loc['Cristiano', 'Idade' : 'Profissão'] = (45, 'Dev')
# print(data) #imprimindo o DataFrame
# print('-'*20)

# data.loc['José', ['Idade', 'Altura']] = (65, 1.72)
# print(data) #imprimindo o DataFrame
# print('-'*20)

# data.iloc[0,2] = '1.94'
# print(data) #imprimindo o DataFrame
# print('-'*20)

# data.loc[:,'Idade'] = 60
# print(data) #imprimindo o DataFrame
# print('-'*20)

# data.loc[:, ['Idade', 'Profissão']] = None
# print(data) #imprimindo o DataFrame
# print('-'*20)

# data.loc[:, ['Idade', 'Altura']] = (23, 1.8)
# print(data) #imprimindo o DataFrame
# print('-'*20)

# data.loc[(data['Idade']<40), 'Altura'] = 1.99
# print(data) #imprimindo o DataFrame
# print('-'*20)

# data.loc[(data['Idade'] == 34)&(data['Profissão']=='Programador'), ['Idade', 'Altura']] = (80, 1.00)
# print(data) #imprimindo o DataFrame
# print('-'*20)

#Inserindo Linhas e Colunas
#Para inserir linhas e colunas em um DataFrame, usamos o método .loc[].

# data.loc['Carlos'] = (56, 'Engenheiro', 1.76) #inserindo uma nova linha no DataFrame
# print(data) #imprimindo o DataFrame
# print('-'*20)

# data_adicional = pd.DataFrame({'Idade':[34,21,54], #criando um novo DataFrame
#                                'Profissão':['Paraquedista', 'Professor', 'Cozinheiro'],
#                                'Altura':[1.79, 1.76, 1.90]},
#                               index=['Júlia', 'Roberto', 'Jack']
#                               )
# data_adicional.index.name = 'Nomes' #nomeando o índice
# print(data_adicional) #imprimindo o DataFrame
# print('-'*20)

# data = pd.concat([data, data_adicional])#adicionando um novo DataFrame ao DataFrame original
# print(data) #imprimindo o DataFrame
# print('-'*20)

# data['Sobrenome'] = None #adicionando uma nova coluna ao DataFrame
# print(data) #imprimindo o DataFrame
# print('-'*20)

# data['Sobrenome'] = ['Silva', 'Cabral', '','','','']
# print(data) #imprimindo o DataFrame
# print('-'*20)

# data.insert(loc=1, column='Data Nascimento', value=['30/09/2000' for i in range(len(data))]) #inserindo uma nova coluna no DataFrame na posição 1 com valores iguais a '30/09/2000' 
# print(data) #imprimindo o DataFrame
# print('-'*20)

#Removendo Linhas e Colunas
#Para remover linhas e colunas em um DataFrame, usamos o método .drop().
# axis = 0, remove linhas
# axis = 1, remove colunas

# data2 = data.drop(index=['Roger', 'Diego']) #removendo as linhas 'Roger' e 'Diego' do DataFrame
# print(data2) #imprimindo o DataFrame    
# print('-'*20)

# data.drop(index=data.index[[0,1]], inplace=True) #removendo as linhas 0 e 1 do DataFrame
# print(data) #imprimindo o DataFrame
# print('-'*20)

# data.drop(index=data[data['Altura']>=1.7].index, inplace=True) #removendo as linhas do DataFrame com altura maior ou igual a 1.7
# print(data) #imprimindo o DataFrame
# print('-'*20)

# data.drop(columns=['Idade'], inplace=True) #removendo a coluna 'Idade' do DataFrame
# print(data) #imprimindo o DataFrame
# print('-'*20)

# data.drop(columns=data.columns[[0,1]], axis=1, inplace=True) #removendo as colunas 0 e 1 do DataFrame
# print(data) #imprimindo o DataFrame
# print('-'*20)

#Tratando Nulos e Ordenando
#Para tratar nulos em um DataFrame, usamos o método .fillna().
#Para ordenar um DataFrame, usamos o método .sort_values().
#Para ordenar um DataFrame, usamos o método .sort_index().

# data.loc['Roger', 'Idade'] = None #alterando o valor da linha 'Roger' e coluna 'Idade' para None
# print(data) #imprimindo o DataFrame
# print('-'*20)

# valores_nulos = pd.isnull(data) #verificando se há valores nulos no DataFrame
# print(valores_nulos) #imprimindo os valores nulos
# print('-'*20)

# valores_nulos = pd.isnull(data['Idade']) #verificando se há valores nulos no DataFrame
# print(valores_nulos) #imprimindo os valores nulos
# print('-'*20)

# valores_nao_nulos = pd.notnull(data['Idade']) #verificando se há valores não nulos no DataFrame
# print(valores_nao_nulos) #imprimindo os valores não nulos
# print('-'*20)

# mask = pd.notnull(data['Idade'])
# print(data[mask]) #imprimindo o DataFrame
# print('-'*20)

# copy = data.sort_values('Idade', ascending=False, inplace=False) #ordenando o DataFrame por idade
# print(copy) #imprimindo o DataFrame
# print('-'*20)

# data.loc['Maria', 'Idade'] = 34
# print(data) #imprimindo o DataFrame
# print('-'*20)

# copy =data.sort_values(['Idade','Altura'], ascending = [True,False], inplace=False) #ordenando o DataFrame por idade e altura
# print(copy) #imprimindo o DataFrame
# print('-'*20)

#Agrupando Dados
#Para agrupar dados em um DataFrame, usamos o método .groupby().
#Para agrupar dados em um DataFrame, usamos o método .agg().
#Para agrupar dados em um DataFrame, usamos o método .apply().
#Para agrupar dados em um DataFrame, usamos o método .transform().
#Para agrupar dados em um DataFrame, usamos o método .filter().
#Para agrupar dados em um DataFrame, usamos o método .pivot_table(). #Para agrupar dados em um DataFrame, usamos o método .crosstab().
#Para agrupar dados em um DataFrame, usamos o método .melt().
#Para agrupar dados em um DataFrame, usamos o método .stack().
#Para agrupar dados em um DataFrame, usamos o método .unstack().
#Para agrupar dados em um DataFrame, usamos o método .merge().
#Para agrupar dados em um DataFrame, usamos o método .join().
#Para agrupar dados em um DataFrame, usamos o método .concat().
#Para agrupar dados em um DataFrame, usamos o método .append().
#Para agrupar dados em um DataFrame, usamos o método .combine_first().
#Para agrupar dados em um DataFrame, usamos o método .update().
#Para agrupar dados em um DataFrame, usamos o método .replace().

# import pandas as pd #importando a biblioteca pandas
# data = pd.read_csv('pessoas.csv', index_col='Nome') #lendo um arquivo csv
# print(data) #imprimindo o DataFrame
# print('-'*20)

# data.loc['William'] = (25, 'Programador', 1.75) #inserindo uma nova linha no DataFrame
# data.loc['Lando'] = (32, 'Médico', 1.70) #inserindo uma nova linha no DataFrame
# data.loc['Max'] = (45, 'Médico', 1.80) #inserindo uma nova linha no DataFrame
# data.loc['Sebastian'] = (35, 'Programador', 1.85) #inserindo uma nova linha no DataFrame
# data.loc['Ana'] = (30, 'Médico', 1.65) #inserindo uma nova linha no DataFrame
# print(data) #imprimindo o DataFrame
# print('-'*20)

# grupos = data.groupby('Profissão') #agrupando o DataFrame por profissão
# for indice, grupo in grupos:
#     print(indice) #imprimindo o índice
#     print(grupo) #imprimindo o grupo
    
# print('-'*20)

# grupos.get_group('Programador') #obtendo o grupo 'Médico'
# print(grupos.get_group('Programador')) #imprimindo o grupo 'Médico'
# print('-'*20)

# grupos = data.groupby(['Profissão','Idade']) #agrupando o DataFrame por profissão e idade
# descrição_grupos = grupos.describe() #descrevendo o grupo
# print(descrição_grupos) #imprimindo o grupo
# print('-'*20)

#Atividades

1
import pandas as pd #importando a biblioteca pandas

dados = {
    'Sede':['Nova Iorque', 'São Paulo', 'Nova Iorque', 'Londres', 'Londres'],
    'Piloto':['Mike Ross', 'Sebastian Thomas', 'Glen Are', 'Michael Schum', 'Luiz da Silva'],
    'Mundiais':[10,11,0,3,44],
    'Vitórias':[321, 329, 12, 44, 1023]
    }

data_frame = pd.DataFrame(dados, index=['X Racing', 'Equatorial', 'Type', 'Blue Race', 'Capa Racing']) #criando um DataFrame
print(data_frame) #imprimindo o DataFrame
print('-'*20)

2
print(data_frame.loc['Blue Race'])
print('-'*20)

3
print(data_frame.loc['Capa Racing', 'Mundiais'])
print('-'*20)

4
mask = data_frame['Mundiais'] >= 10
print(data_frame[mask])
print('-'*20)

5
print(data_frame[(data_frame['Mundiais']>=10)&(data_frame['Vitórias']>300)])
print('-'*20)

6
data_frame.at['Equatorial', 'Piloto'] = 'Antônio Racer'
print(data_frame)
print('-'*20)

7
data_frame.loc['X Racing',['Sede', 'Vitórias']] = ('São Paulo', 322)
print(data_frame)
print('-'*20)

8
data_frame.loc['Red Cow'] = ('São Paulo', 'Fernando Vetel', 0, 0)
print(data_frame)
print('-'*20)

9
data = data_frame.sort_values('Vitórias', ascending=False, inplace=False)
print(data)
print('-'*20)



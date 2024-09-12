# Módulos
# Módulos são arquivos que contém funções e variáveis que podem ser importadas para outros arquivos.
# Para importar um módulo, basta usar a palavra reservada import seguida do nome do módulo.

import datetime # Importa o módulo datetime
print(type(datetime)) # <class 'module'>
data = datetime.datetime(2024, 9, 12, 9,6,45) # Cria um objeto datetime
print(data) # 2024-09-12 09:06:45
print('-'*20)

import datetime as tempo # Importa o módulo datetime e o renomeia para tempo
print(type(datetime)) # <class 'module'>
data = tempo.datetime(2024, 9, 12, 9,6,45) # Cria um objeto datetime
print(data) # 2024-09-12 09:06:45
print('-'*20)

import random # Importa o módulo random
print(random.randrange(0, 10)) # Gera um número aleatório entre 0 e 10
print('-'*20)

from random import randrange # Importa a função randrange do módulo random
print(randrange(0, 10)) # Gera um número aleatório entre 0 e 10
print('-'*20)

from random import randrange as num_aleatório # Importa a função randrange do módulo random e a renomeia para num_aleatório
print(num_aleatório(0, 10)) # Gera um número aleatório entre 0 e 10
print('-'*20)

from random import * # Importa todas as funções do módulo random
print(randrange(0, 10)) # Gera um número aleatório entre 0 e 10
print('-'*20)

import random # Importa o módulo random
dir(random) # Lista todas as funções e variáveis do módulo random
print(dir(random))
print('-'*20)

import random # Importa o módulo random
dir(random.randrange) # Lista todas as funções e variáveis da função randrange do módulo random
print(dir(random.randrange)) # Mostra todas as funções e variáveis da função randrange do módulo random
print('-'*20)

import random # Importa o módulo random
dir(random.__name__) # Lista todas as funções e variáveis do módulo random
print(random.__name__) # Mostra o nome do módulo random
print('-'*20)

import random # Importa o módulo random
dir(random.__file__) # Lista todas as funções e variáveis do módulo random
print(random.__file__) # Mostra o caminho do arquivo do módulo random
print('-'*20)

import random # Importa o módulo random
dir(random.__doc__) # Lista todas as funções e variáveis do módulo random
print(random.__doc__) # Mostra a documentação do módulo random
print('-'*20)

from random import randrange # Importa a função randrange do módulo random
print(randrange.__doc__) # Mostra a documentação da função randrange do módulo random
print(randrange.__name__) # Mostra o nome da função randrange do módulo random
print('-'*20)

#PIP
#PIP é um sistema de gerenciamento de pacotes utilizado para instalar e gerenciar pacotes de software escritos em Python.
#Para instalar um pacote, basta usar o comando pip install seguido do nome do pacote.
#Para desinstalar um pacote, basta usar o comando pip uninstall seguido do nome do pacote.
#Para listar todos os pacotes instalados, basta usar o comando pip list.
#Para atualizar um pacote, basta usar o comando pip install --upgrade seguido do nome do pacote.
#Para verificar se tem atualizações disponíveis para os pacotes instalados, basta usar o comando pip list --outdated.

#Atividade

1
import random # Importa o módulo random
from random import randrange # Importa a função randrange do módulo random

numero = randrange(2, 100) # Gera um número aleatório entre 2 e 100
if numero % 2 == 0: # Verifica se o número é par
    print('O número é:', numero,'e ele é Par') # Exibe o número gerado e a mensagem
else:
    print('O número é:', numero,'e ele é Impar') # Exibe o número gerado e a mensagem
print('-'*20)

2
soma = 0 # Inicializa a variável soma com 0
for _ in range(100): # Repete 100 vezes
   soma += randrange(100) # Gera um número aleatório entre 0 e 100 e soma com o valor anterior     
print('A soma dos números é:', soma) # Exibe a soma dos números

3
import calc_python
#print(calc_python.__doc__) # Exibe a documentação do módulo calc_python
#help(calc_python) # Exibe a documentação do módulo calc_python
#print(calc_python.soma.__doc__) # Exibe a documentação da função soma do módulo calc_python
resultado = calc_python.soma(10, 20) # Chama a função soma do módulo calc_python
print('O resultado da soma é:', resultado) # Exibe o resultado da soma
print('-'*20)

4
from meu_random import get_random_lista # Importa a função get_random_lista do módulo meu_random
print(get_random_lista(1, 100, 10)) # Gera uma lista de 10 números aleatórios entre 1 e 100
print('-'*20)

5
# import sys
# import subprocess

# if(__name__ == '__main__'):
#     if len(sys.argv) != 3: 
#         print('Número de argumentos inválido!')
#         sys.exit(1)
#     numero1 = float(sys.argv[1])
#     numero2 = float(sys.argv[2])
#     print('A soma dos números é:', numero1 + numero2)

# result = subprocess.run(['python3', 'teste_programa.py', 10, 20], capture_output=True, text=True)
# print(result.stdout) # Exibe a saída do script teste_programa.
print('-'*20)

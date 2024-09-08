#Funções Built-in
# Funções built-in são funções que estão disponíveis para uso em Python sem a necessidade de importar bibliotecas.

# Funções Matemáticas
from cmath import sqrt
from math import ceil, floor
import math

abs # Retorna o valor absoluto de um número
num1 = -10
num2 = 10
print(abs(num1)) # 10
print(abs(num2)) # 10
print(abs(num1) + abs(num2)) # 20

max # Retorna o maior valor de um iterável
maior_valor = max(10, 20, 30)
print(maior_valor) # 30

min # Retorna o menor valor de um iterável
lista = [10, 20, 30]
print(min(lista)) # 10

pow # Retorna a potência de um número
x = 2
y = 3
print(pow(x, y)) # 8

sqrt # Retorna a raiz quadrada de um número
print(math.sqrt(25)) # 5.0
 
round # Retorna um número arredondado
print(round(5.5)) # 6

floor # Retorna o maior número inteiro menor ou igual a um número
print(floor(5.657)) # 5

ceil # Retorna o menor número inteiro maior ou igual a um número
print(ceil(5.657)) # 6

divmod # Retorna o quociente e o resto da divisão de dois números
print(divmod(10, 3)) # (3, 1)

# Funções de Conversão de Números para Caracteres
chr # Retorna o caractere correspondente ao código ASCII
for i in range(65,123):
    caractere = chr(i)
    print("%d = %s" % (i, caractere), end='\n')
    
ord # Retorna o código ASCII correspondente ao caractere
caractere = 'A'
print(ord(caractere)) # 65
print("O caractere %s tem o código ASCII %d" % (caractere, ord(caractere)))

#Funções de Formatação de Strings

#capitalize # Retorna a string com a primeira letra maiúscula
string = "python"
print(string.capitalize()) # Python

#.upper # Retorna a string com todas as letras maiúsculas
string = "python"
print(string.upper()) # PYTHON

#.lower # Retorna a string com todas as letras minúsculas
string = "PYTHON"
print(string.lower()) # python

#.swapcase # Retorna a string com as letras maiúsculas convertidas em minúsculas e vice-versa
string = "Python"
print(string.swapcase()) # pYTHON

#.title # Retorna a string com a primeira letra de cada palavra maiúscula
string = "python é uma linguagem de programação"
print(string.title()) # Python É Uma Linguagem De Programação

#.center # Retorna a string centralizada
string = "Python"
print(string.center(20)) # "       Python       "
print(string.center(20, '-')) # "-------Python-------"

#.ljust # Retorna a string justificada à esquerda
string = "Python"
print(string.ljust(20)) # "Python              "
print(string.ljust(20, '-')) # "Python--------------"

#.rjust # Retorna a string justificada à direita
string = "Python"
print(string.rjust(20)) # "              Python"
print(string.rjust(20, '-')) # "--------------Python"

#.count # Retorna o número de ocorrências de uma substring em uma string
string = "Python é uma linguagem de programação, Python é uma linguagem de programação"
print(string.count("Python")) # 2

#.startswith # Retorna True se a string começa com a substring especificada
string = "Python é uma linguagem de programação"
print(string.startswith("Python")) # True

#.endswith # Retorna True se a string termina com a substring especificada
string = "Python é uma linguagem de programação"
print(string.endswith("programação")) # True

#.find # Retorna a posição da primeira ocorrência de uma substring em uma string
texto = " me encontra 20 10 5"
pos = texto.find("20")
print(pos) # 12

#.replace # Retorna uma string com todas as ocorrências de uma substring substituídas por outra
texto = "Ol@ eu sou @ ful@n@"
novo_texto = texto.replace("@", "a")
print(novo_texto) # Ola eu sou a fulana

#.split # Retorna uma lista de substrings separadas por um delimitador
texto = "Python é uma linguagem de programação"
lista = texto.split(" ")
print(lista) # ['Python', 'é', 'uma', 'linguagem', 'de', 'programação']

#.splitlines # Retorna uma lista de substrings separadas por quebras de linha
texto = "Python é uma linguagem de programação\nJava é uma linguagem de programação"
lista = texto.splitlines()
print(lista) # ['Python é uma linguagem de programação', 'Java é uma linguagem de programação']

#.isalpha # Retorna True se a string contém apenas letras
string = "Python"
print(string.isalpha()) # True

#.isalnum # Retorna True se a string contém apenas letras e números
string = "Python123"
print(string.isalnum()) # True

#.isdecimal # Retorna True se a string contém apenas números
string = "123"
print(string.isdecimal()) # True

#isspace # Retorna True se a string contém apenas espaços
string = " "
print(string.isspace()) # True

#.isupeer # Retorna True se a string contém apenas letras maiúsculas
string = "PYTHON"
print(string.isupper()) # True

#.islower # Retorna True se a string contém apenas letras minúsculas
string = "python"
print(string.islower()) # True

#Funções de Listas

#len # Retorna o número de elementos de um iterável
lista = [10, 20, 30]
print(len(lista)) # 3

#.sort # Ordena os elementos de uma lista
lista = [30, 10, 20]
lista.sort()
print(lista) # [10, 20, 30]

#.reverse # Inverte a ordem dos elementos de uma lista
lista = [10, 20, 30]
lista.reverse()
print(lista) # [30, 20, 10]

#dict # Cria um dicionário a partir de uma lista de tuplas
nomes = ('José', 'Carlos', 'João')
dicionario = dict.fromkeys(nomes, 10)
print(dicionario) # {'José': 10, 'Carlos': 10, 'João': 10}
print('-' * 20)

#Funções de Data e Hora

from datetime import datetime, timedelta
import datetime

#y = ano
#m = mês
#d = dia
#H = hora
#M = minuto
#S = segundo
#A = dia da semana
#a = dia da semana abreviado
#B = mês
#b = mês abreviado
#I = hora formato 12
#p = AM/PM

#datetime.now # Retorna a data e hora atuais
data_atual = datetime.datetime.now()
data = data_atual.date()
hora = data_atual.time()
print(data_atual)
print(data) # 2021-07-07
print(hora) # 17:00:00.000000
print('-' * 20)

data_atual = datetime.datetime.now()
print("Dia:", data_atual.day)
print("Mês:", data_atual.month)
print("Ano:", data_atual.year)
print("Hora:", data_atual.hour)
print("Minuto:", data_atual.minute)
print("Segundo:", data_atual.second)
print('-' * 20)

data = datetime.date(day=8, month=9, year=2024)
print(data) # 2024-09-08
print(type(data)) # <class 'datetime.date'>
print('-' * 20)

hora = datetime.time(hour=10, minute=30, second=15)
print(hora) # 10:30:15
print('-' * 20)

data = datetime.datetime(year=2024, month=9, day=8, hour=10, minute=30, second=15)
print(data) # 2024-09-08 10:30:15
print('-' * 20)

atual = datetime.datetime.now()
current_time = atual.strftime("%y/%m/%d %H:%M:%S")
print(current_time) # 21/07/07 17:00:00
print(type(current_time)) # <class 'str'>
print('-' * 20)

data = datetime.datetime(2024, 9, 8, 9, 51, 30)
print(data.strftime("%A - %a")) # Monday - Mon
print(data.strftime("%B - %b")) # September - Sep
print(data.strftime("%H - %I")) # 09 - Sep
print(data.strftime("%I - %p")) # AM - PM
print('-' * 20)

#Manipulação de Datas e Horas

data1 = datetime.datetime(2024, 9, 8,)
data2 = datetime.datetime(2024, 9, 10)
diferença = data2 - data1
print(diferença) # 2 days, 0:00:00
print(type(diferença)) # <class 'datetime.timedelta'>
print('-' * 20)

from datetime import datetime, timedelta

data_atual = datetime.now()
datafutura1 = data_atual + timedelta(weeks=4)
datafutura2 = data_atual + timedelta(days=30)
datafutura3 = data_atual + timedelta(hours=12)
datafutura4 = data_atual + timedelta(minutes=60)

print("Data atual:", data_atual)
print("Mais 4 semanas:", datafutura1)
print("Mais 30 dias:", datafutura2)
print("Mais 12 horas:", datafutura3)
print("Mais 60 minutos:", datafutura4)
print('-' * 20)


data_2000 = datetime(2000, 1, 1, 0, 0, 0)
data_atual = datetime.now()
diferença = data_atual - data_2000
print("Desde o ano 2000 passou ", diferença.days, "dias") # Desde o ano 2000 passou  7857 dias
print("Desde o ano 2000 passou ", diferença.total_seconds(), "segundos") # Desde o ano 2000 passou  678220800.0 segundos
print("Desde o ano 2000 passou ", diferença.total_seconds() / 60, "minutos") # Desde o ano 2000 passou  11303680.0 minutos
print("Desde o ano 2000 passou ", diferença.total_seconds() / 60 / 60, "horas") # Desde o ano 2000 passou  188394.66666666666 horas
print("Desde o ano 2000 passou ", diferença.total_seconds() / 60 / 60 / 24, "dias") # Desde o ano 2000 passou  7857.0 dias
print('-' * 20)

# data_txt = input("Digite a data no formato dd/mm/yyyy: ")
# datetime = datetime.strptime(data_txt, "%d/%m/%Y")
# print(datetime) # 2021-07-07 00:00:00
# print(type(datetime)) # <class 'datetime.datetime'>
# print('-' * 20)

#Atividade

1
def subtração(a, b):
    return (abs(a) - abs(b))
print(subtração(-10, 20))
print('-' * 20)

2
def soma(a, b):
    soma = a + b
    soma = min(soma, 10000)
    soma = max(soma, 0)
    return (soma)
print(soma(9999, 2))
print(soma(10, -20))
print('-' * 20)

3
def menor(*números):
    menor = números[0]
    for i in números:
        menor = min(menor, i)
    return menor
print(menor(10, 20, 30, 40, -50))
print(menor(50, -40, 30, 20, 10))
print('-' * 20)

# 4
# a = float(input("Digite o valor de a: "))
# b = float(input("Digite o valor de b: "))
# c = float(input("Digite o valor de c: "))

# x1 = (-b + math.sqrt(pow(b, 2) - 4 * a * c)) / (2 * a)
# x2 = (-b - math.sqrt(pow(b, 2) - 4 * a * c)) / (2 * a)
# print("A solução encontrada é", x1, "e", x2)
# print('-' * 20)

5
def troca_tamanho_letra(string):
    return string.swapcase()
print(troca_tamanho_letra("Python"))
print(troca_tamanho_letra("pYTHON"))
print('-' * 20)

6
def contar_letra(string, letra):
    return string.count(letra)
print(contar_letra("Python é uma linguagem de programação", "a"))
print(contar_letra("Python é uma linguagem de programação", "z"))
print('-' * 20)

7
def encontrar_letra(string, letra):
    lista = []
    for i in range(len(string)):
        if string[i] == letra:
            lista.append(i)
    return lista
print(encontrar_letra("Python é uma linguagem de programação", "a"))
print(encontrar_letra("Python é uma linguagem de programação", "e"))
print('-' * 20)

8
def retira_palavras(texto, palavras):
    for palavra in palavras:
        if palavra in texto:
            texto = texto.replace(palavra, "*****")
    return texto

texto_usuário = "não pode falar a palavra droga ou diabo no chat"
palavras_proibidas = ["droga", "diabo"]
print(retira_palavras(texto_usuário, palavras_proibidas))
print('-' * 20)

9
def eh_maiúscula_ou_minuscula(palavra):
    return palavra.islower() or palavra.isupper()

print(eh_maiúscula_ou_minuscula("PYTHON"))
print(eh_maiúscula_ou_minuscula("python"))
print(eh_maiúscula_ou_minuscula("Python"))
print('-' * 20)

10
def transforma_lista(lista):
    lista_inteiros = []
    for item in lista:
        if item.isdecimal():
            lista_inteiros.append(int(item))
    lista_inteiros.sort()
    return lista_inteiros

lista = ["10", "2er0", "30", "40", "3d0", '100']
print(transforma_lista(lista))
print('-' * 20)

11
# data_nascimento = input("Digite a data de nascimento no formato dd/mm/yyyy: ")
# data_atual = datetime.now()
# data_nascimento = datetime.strptime(data_nascimento, "%d/%m/%Y")
# diferença = data_atual - data_nascimento
# print("Você tem", diferença.days , "dias de vida")
# print('-' * 20)

12
# data_aniversário = input("Digite seu próximo aniversário no formato dd/mm/yyyy: ")
# data_atual = datetime.now()
# data_aniversário = datetime.strptime(data_aniversário, "%d/%m/%Y")
# diferença = data_aniversário - data_atual
# print("Faltam", diferença.days , "dias para o seu próximo aniversário")
# print('-' * 20)

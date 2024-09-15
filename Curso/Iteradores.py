#Iteradores
#Um iterador é um objeto que contém um número contável de valores.
#Um iterador é um objeto sobre o qual é possível iterar, o que significa que é possível percorrer todos os valores.
#Tecnicamente, em Python, um iterador é um objeto que implementa o protocolo de iteração, que consiste nos métodos __iter__() e __next__().
#O método __iter__() retorna o próprio objeto iterador e é chamado no início de cada iteração.
#O método __next__() retorna o próximo valor e é chamado no final de cada iteração.
#Para criar um objeto iterador, é necessário implementar os métodos __iter__() e __next__().

lista = [1, 2, 3, 4, 5] #lista de 1 a 5
iterador = iter(lista) #iterador = iter(lista)
print(next(iterador)) #print next(iterador)
print(next(iterador)) #print next(iterador)
print(next(iterador)) #print next(iterador)
print(next(iterador)) #print next(iterador)
print(next(iterador)) #print next(iterador)
print(type(iterador)) #print type(iterador)
for item in lista: #percorre a lista
    print(item) #print item
print(1 in lista) #True
print(10 in lista) #False
print('-'*20)

#Objetos iteráveis
#Um objeto iterável é um objeto que pode ser iterado.
#Em Python, um objeto é iterável se implementar o método __iter__(), que retorna um objeto iterador.
#O método __iter__() é chamado no início de cada iteração.
#O método __next__() é chamado no final de cada iteração.
#Exemplos de objetos iteráveis em Python são listas, tuplas, dicionários, conjuntos e strings.

class ColeçãoNúmeros: #classe ColeçãoNúmeros
    def __init__(self, número_max): #define __init__ com self e número_max
        self.max = número_max #atribui número_max a self.max
    def __iter__(self): #define __iter__ com self
        self.número_atual = 1 #atribui 1 a self.número_atual
        return self #retorna o próprio objeto
    
    def __next__(self): #define __next__ com self
        if self.número_atual <= self.max: #se self.número_atual for menor ou igual a self.max
            retorno = self.número_atual #retorna self.número_atual
            self.número_atual += 1 #incrementa self.número_atual
            return retorno #retorna a variável retorno
        else: #senão
            raise StopIteration #interrompe a iteração

coleção = ColeçãoNúmeros(6) #Instancia da classe ColeçãoNúmeros
for item in coleção: #percorre coleção
    print(item) #print item
print(2 in coleção) #True
print(10 in coleção) #False
print('-'*20)

class ColeçãoNúmeros: #classe ColeçãoNúmeros
    def __init__(self, número_max): #define __init__ com self e número_max
        self.max = número_max #atribui número_max a self.max
    def __iter__(self): #define __iter__ com self
        self.número_atual = 1 #atribui 1 a self.número_atual
        return self #retorna o próprio objeto
    
    def __next__(self): #define __next__ com self
        if self.número_atual <= self.max: #se self.número_atual for menor ou igual a self.max
            retorno = self.número_atual #retorna self.número_atual
            self.número_atual += 1 #incrementa self.número_atual
            return retorno #retorna a variável retorno
        else: #senão
            raise StopIteration #interrompe a iteração

coleção = ColeçãoNúmeros(6) #Instancia da classe ColeçãoNúmeros
iterador = iter(coleção) #iterador = iter(coleção)
for _ in range(6):  # Repete o comando 6 vezes
    print(next(iterador))  # Percorre o iterador e printa o próximo valor
print('-'*20)

#Funções Iteradoras
#Em Python, as funções iteradoras são funções que retornam um objeto iterador.
#Para criar uma função iteradora, é necessário usar a palavra-chave yield.
#O comando yield é usado para retornar um valor da função sem encerrá-la.
#Quando a função é chamada, ela retorna um objeto iterador.
#O método __iter__() é chamado no início de cada iteração.
#O método __next__() é chamado no final de cada iteração.
#O comando yield é usado para retornar um valor da função sem encerrá-la.

def ancora(): #def ancora
    yield 1 #A função ancora retorna 1
    yield 2 #A função ancora retorna 2
    yield 3 #A função ancora retorna 3
    
for item in ancora(): #percorre ancora e atribui a item
    print(item) #imprime item

print('-'*20)

def ancora(): #def ancora
    yield 1 #A função ancora retorna 1
    yield 2 #A função ancora retorna 2
    yield 3 #A função ancora retorna 3
    
func = ancora() #atribui ancora a func
for _ in range(3): #repete 3 vezes
    print(next(func)) #imprime o próximo valor de func

print('-'*20)

def meu_range(num):
    local_num = 0
    while local_num < num:
        yield local_num
        local_num += 1

for i in meu_range(10):
    print(i)

print('-'*20)

#Enumerate
#A função enumerate() é usada para adicionar um contador a um iterável.
#A função enumerate() retorna um objeto enumerado.
#O objeto enumerado é uma sequência de tuplas contendo o índice e o valor de cada item.
#A função enumerate() é útil para obter o índice de cada item de um iterável.

lista = ['a', 'b', 'c'] #lista com elementos

for item in enumerate(lista): #percorre a lista
    print(item) #imprime item
    
for índice, valor in enumerate(lista): #percorre a lista
    print(índice, valor) #imprime índice e valor

print('-'*20)

def anos(): #função anos
    yield 2010 #a função anos retorna 2010
    yield 2011 #a função anos retorna 2011
    yield 2012 #a função anos retorna 2012
    yield 2013 #a função anos retorna 2013
    yield 2014 #a função anos retorna 2014
    yield 2015 #a função anos retorna 2015

for índice, valor in enumerate(anos()): #percorre anos
    print(índice, valor) #imprime índice e valor
 
print('-'*20)

for valor, índice in enumerate(range(0,20,5)): #percorre range de 0 a 20 com passo 5
    print(valor, índice) #imprime valor e índice

print('-'*20)

#Unpacking de Iteradores
#O Unpacking de iteradores é uma técnica usada para descompactar os elementos de um iterador.
#O Unpacking de iteradores é feito usando o operador *.
#O operador * é usado para descompactar os elementos de um iterador.

produtos = [
    ['carro', '200.000'],
    ['moto', '20.000'],
    ['bicicleta', '500'],
    ['patinete', '300'],
    ['skate', '150']
]

for produto, preço in produtos: #percorre produtos
    print(produto, preço) #imprime produto e preço
    
print('-'*20)

def gen1(): #função gen1
    yield [1,2] #a função gen1 retorna 1
    yield [3,4] #a função gen1 retorna 2
    yield [5,6] #a função gen1 retorna 3

for x,y in gen1(): #percorre gen1
    print(x,y) #imprime x e y
    
print('-'*20)

def gen1(): #função gen1
    yield 1 #a função gen1 retorna 1
    yield 2 #a função gen1 retorna 2
    yield 3 #a função gen1 retorna 3

def gen2(): #função gen2
    for i in gen1(): #percorre gen1
        yield i, 'a' #a função gen2 retorna i e 'a'
        yield i, 'b' #a função gen2 retorna i e 'b'
        yield i, 'c' #a função gen2 retorna i e 'c'

for x,y in gen2(): #percorre gen2
    print(x,y) #imprime x e y
    
print('-'*20)

#Join
#O método join() é usado para unir os elementos de um iterável.
#O método join() é chamado em uma string.
#O método join() retorna uma string contendo os elementos do iterável unidos.
#O método join() é útil para unir os elementos de uma lista, tupla ou conjunto.

texto1 = 'Olá!'
print("#".join(texto1)) #imprime Olá! com # entre cada letra

print('-'*20)

lista = ['a', 'b', 'c', 'd'] #lista com elementos
letras = ' '.join(lista) #Inclui um espaço entre cada elemento da lista
print(letras) #imprime letras

print('-'*20)

letras = '-'.join([str(i) for i in range(10)]) #Inclui um - entre cada elemento da lista
print(letras) #imprime letras

print('-'*20)

def anos():
    for i in range(2020,2030):
        yield str(i)
        
letras = '-'.join(anos())
print(letras)

print('-'*20)

#Tratando exceções
#O tratamento de exceções é uma técnica usada para lidar com erros em tempo de execução.
#Em Python, as exceções são erros que ocorrem durante a execução de um programa.
#O tratamento de exceções é feito usando as palavras-chave try, except e finally.
#O bloco try é usado para testar um bloco de código.
#O bloco except é usado para lidar com exceções.
#O bloco finally é usado para executar código, independentemente de ocorrer uma exceção ou não.

lista = [1,2,3]
iterador = iter(lista)

while True:
    try:
        print(next(iterador))
    except: 
        break

print('-'*20)

#Atividade

1
def meses():
    meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
    for i in meses:
        yield i
for i in meses():
    print(i)
    
print('-'*20)

2

def mult_2():
    for i in lista:
        yield i*2

lista = [1,2,3,4,5]

for i in mult_2():
    print(i)
    
print('-'*20)

3
# class Tabuada:  #classe Tab
#     def __init__(self, número): #define __init__ com self e número
#         self.número = número #atribui número a self.número

#     def __iter__(self): #define __iter__ com self
#         self.i = 1 #atribui 1 a self.i
#         return self #retorna o próprio objeto

#     def __next__(self): #define __next__ com self
#         if self.i <= 10: #se self.i for menor ou igual a 10
#             resultado = self.número * self.i #atribui o resultado da multiplicação de self.número por self.i a resultado
#             operacao = f"{self.i} * {self.número} = {resultado}" #atribui a operacao a string com a operação
#             self.i += 1 #incrementa self.i
#             return operacao #retorna a variável operacao
#         else:
#             raise StopIteration #interrompe a iteração

# número = int(input("Digite um número inteiro para saber a Tabuada: ")) #solicita um número inteiro

# tabuada = Tabuada(número) #Instancia da classe Tabuada

# for item in tabuada: #percorre tabuada
#     print(item) #imprime item
# print('-'*20)

4
class Fatorial():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __iter__(self):
        self.atual = self.x
        return self
    
    @staticmethod
    def calcula_fatorial(num):
        result = 1
        for i in range(1, num+1):
            result *= i
        return result  
    
    def __next__(self):
       if (self.atual == self.y+1):
           raise StopIteration
       result = Fatorial.calcula_fatorial(self.atual)
       self.atual += 1
       return result
    
for i in Fatorial(1, 10):
    print(i)
print('-'*20)

5
def meses_enum():
    meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
    for i in enumerate(meses):
        yield i
        
for índice, mes in meses_enum():
    print(índice+1, mes)
print('-'*20)

6
def frase(lista):
    return '. '.join(lista) + '.'

textos = ['Olá', 'Mundo', 'Python']
print(frase(textos))
print('-'*20)

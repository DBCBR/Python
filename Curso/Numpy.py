#Numpy 
#Numpy é uma biblioteca de álgebra linear para Python, o motivo de ser tão importante é que a maioria das bibliotecas de Data Science são construídas em cima do Numpy, então é importante conhecer a biblioteca.
#Numpy é uma biblioteca de computação científica que fornece suporte para arrays e matrizes multidimensionais, além de funções matemáticas para operações com essas estruturas.
#Para instalar o Numpy, basta executar o comando pip install numpy

#Tipos de Dados
#Numpy possui vários tipos de dados, que são utilizados para a criação de arrays, esses tipos de dados são:
#bool_: Booleano
#bytes_: String de bytes
#str_: String
#intc: Inteiro de 32 bits
#uintc: Inteiro sem sinal de 32 bits
#int_: Inteiro de 64 bits
#uint: Inteiro sem sinal de 64 bits
#long: Inteiro de 64 bits
#ulong: Inteiro sem sinal de 64 bits
 
import numpy #Importando a biblioteca Numpy
boolean = numpy.bool_(True) #Criando um booleano
print(boolean, type(boolean)) #Imprimindo o booleano e o tipo dele
string = numpy.bytes_("este e um texto") #Criando uma string
print(string, type(string)) #Imprimindo a string e o tipo dela
string = numpy.str_("este é um texto") #Criando uma string
print(string, type(string)) #Imprimindo a string e o tipo dela
print('-'*20)

inteiro = numpy.intc(-120) #Criando um inteiro de 32 bits
uinteiro = numpy.uintc(120) #Criando um inteiro sem sinal de 32 bits
long = numpy.int_(1205468943132) #Criando um inteiro de 64 bits
ulong = numpy.uint(123543654323105468) #Criando um inteiro sem sinal de 64 bits

print(inteiro, type(inteiro)) #Imprimindo o inteiro e o tipo dele
print(uinteiro, type(uinteiro)) #Imprimindo o inteiro sem sinal e o tipo dele
print(long, type(long)) #Imprimindo o inteiro de 64 bits e o tipo dele
print(ulong, type(ulong)) #Imprimindo o inteiro sem sinal de 64 bits e o tipo dele
print('-'*20)

#Tipos de dados 2
#float32: Número de ponto flutuante de 32 bits
#float64: Número de ponto flutuante de 64 bits
#complex64: Número complexo de 64 bits
#complex128: Número complexo de 128 bits

ponto_flutuante = numpy.float64(10052.45) #Criando um número de ponto flutuante de 64 bits
ponto_flutuante32 = numpy.float32(3052.45) #Criando um número de ponto flutuante de 32 bits
print(ponto_flutuante, type(ponto_flutuante)) #Imprimindo o número de ponto flutuante e o tipo dele
print(ponto_flutuante32, type(ponto_flutuante32)) #Imprimindo o número de ponto flutuante de 32 bits e o tipo dele
print('-'*20)

int8 = numpy.int8(20) #Criando um inteiro de 8 bits
int16 = numpy.int16(1200) #Criando um inteiro de 16 bits
uint8 = numpy.uint8(35) #Criando um inteiro sem sinal de 8 bits
int16 = numpy.int16(4653) #Criando um inteiro de 16 bits
float16 = numpy.float16(20.5) #Criando um número de ponto flutuante de 16 bits
print(int8, type(int8)) #Imprimindo o inteiro de 8 bits e o tipo dele
print(int16, type(int16)) #Imprimindo o inteiro de 16 bits e o tipo dele
print(uint8, type(uint8)) #Imprimindo o inteiro sem sinal de 8 bits e o tipo dele
print(int16, type(int16)) #Imprimindo o inteiro de 16 bits e o tipo dele
print(float16, type(float16)) #Imprimindo o número de ponto flutuante de 16 bits e o tipo dele
print('-'*20)

#Criando Arrays
#Arrays são estruturas de dados que armazenam valores de um mesmo tipo, e são muito utilizadas em computação científica.
#Para criar um array em Numpy, basta utilizar a função array() e passar uma lista como parâmetro.

array = numpy.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], dtype = numpy.int8) #Criando um array de inteiros
print(array) #Imprimindo o array
print(type(array)) #Imprimindo o tipo do array
print(array.dtype) #Imprimindo o tipo de dados do array

array = numpy.array(["2" , "8" , "1"], dtype = numpy.str_) #Criando um array de strings
print(array) #Imprimindo o array
print(type(array)) #Imprimindo o tipo do array
print(array.dtype) #Imprimindo o tipo de dados do array
print('-'*20)

#i = inteiro
#u = inteiro sem sinal
#f = ponto flutuante
#S = string
#U = string unicode
#b = booleano

array = numpy.array(["abc" , "def" , "ghi"], dtype = 'S3') #Criando um array de strings
print(array) #Imprimindo o array
print(array.dtype) #Imprimindo o tipo de dados do array
print(array.itemsize) #Imprimindo o tamanho de cada item do array
print(array.nbytes) #Imprimindo o tamanho total do array
print('-'*20)

array = numpy.array([1,2,3] , dtype = 'i2') #Criando um array de strings
print(array) #Imprimindo o array
print(array.dtype) #Imprimindo o tipo de dados do array
print(array.itemsize) #Imprimindo o tamanho de cada item do array
print(array.nbytes) #Imprimindo o tamanho total do array
print('-'*20)

#Criando Tipos de Dados

import numpy
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

array = numpy.array([Pessoa("David", 37), Pessoa("Paula", 35)])#Criando um array de objetos
print(array) #Imprimindo o array
print(type(array)) #Imprimindo o tipo do array
print(array.dtype, end='\n\n') #Imprimindo o tipo de dados do array
print(array[0].nome, array[1].idade) #Imprimindo o nome e a idade do primeiro item do array
print('-'*20)

tipo_pessoa = numpy.dtype([("nome", 'S10'), ("idade", 'i4')]) #Criando um tipo de dados
array = numpy.array([("David", 37), ("Paula", 35)], dtype = tipo_pessoa) #Criando um array de objetos
print(array) #Imprimindo o array
print(type(array)) #Imprimindo o tipo do array
print(array.dtype) #Imprimindo o tipo de dados do array
print('-'*20)

#Propriedades dos Arrays
#Os arrays possuem várias propriedades que podem ser acessadas, como:
#ndim: Número de dimensões do array
#shape: Formato do array
#size: Número de elementos do array
#dtype: Tipo de dados do array
#itemsize: Tamanho de cada item do array
#nbytes: Tamanho total do array

import numpy as np
array = np.array([[1,2,3],[4,5,6],[7,8,9]]) #Criando um array de duas dimensões
print(array)
print(array.ndim) #Imprimindo o número de dimensões do array
print(array.shape) #Imprimindo o formato do array
print(array.size) #Imprimindo o número de elementos do array
print(array.dtype) #Imprimindo o tipo de dados do array
print(array.itemsize) #Imprimindo o tamanho de cada item do array
print(array.nbytes) #Imprimindo o tamanho total do array
print('-'*20)

tipo_pessoa = numpy.dtype([("nome", 'S10'), ("idade", 'i4')]) #Criando um tipo de dados
array = numpy.array([("David", 37), ("Paula", 35)], dtype = tipo_pessoa) #Criando um array de objetos
print(array)
print(array.ndim) #Imprimindo o número de dimensões do array
print(array.shape) #Imprimindo o formato do array
print(array.size) #Imprimindo o número de elementos do array
print(array.dtype) #Imprimindo o tipo de dados do array
print(array.itemsize) #Imprimindo o tamanho de cada item do array
print(array.nbytes) #Imprimindo o tamanho total do array
print('-'*20)

#Produção de Objetos Preenchidos
#Numpy possui várias funções que permitem criar arrays preenchidos com valores específicos, como:
#zeros: Cria um array preenchido com zeros
#ones: Cria um array preenchido com uns
#full: Cria um array preenchido com um valor específico
#eye: Cria uma matriz identidade
#empty: Cria um array vazio
#arange: Cria um array com valores espaçados uniformemente
#linspace: Cria um array com valores espaçados uniformemente

array1 = numpy.zeros(9 ) #Criando um array preenchido com zeros
array2 = numpy.ones(3) #Criando um array preenchido com uns
array3 = numpy.empty(6) #Criando um array vazio
array4 = numpy.identity(4) #Criando uma matriz identidade

print(array1, end='\n\n') #Imprimindo o array preenchido com zeros
print(array2, end='\n\n') #Imprimindo o array preenchido com uns
print(array3, end='\n\n') #Imprimindo o array vazio
print(array4, end='\n\n') #Imprimindo a matriz identidade
print('-'*20)

array1 = numpy.zeros((3,3)) #Criando um array preenchido com zeros
array2 = numpy.ones((4,4)) #Criando um array preenchido com uns

print(array1, end='\n\n') #Imprimindo o array preenchido com zeros
print(array2, end='\n\n') #Imprimindo o array preenchido com uns
print('-'*20)

array1 = numpy.arange(9) #Criando um array com valores espaçados uniformemente
array2 = numpy.arange(4,16) #Criando um array com valores espaçados uniformemente
print(array1) #Imprimindo o array com valores espaçados uniformemente
print(array2) #Imprimindo o array com valores espaçados uniformemente
print('-'*20)

array1 = numpy.arange(2,16+1, 2) #Criando um array com valores espaçados uniformemente
print(array1) #Imprimindo o array com valores espaçados uniformemente
print('-'*20)

array = numpy.full((4,4), 10) #Criando um array preenchido com um valor específico
print(array) #Imprimindo o array preenchido com um valor específico
print('-'*20)

array_float = numpy.random.rand(4,4) #Criando um array com valores aleatórios
array_int = numpy.random.randint(5,10, (5,5)) #Criando um array com valores aleatórios
print(array_float) #Imprimindo o array com valores aleatórios
print(array_int) #Imprimindo o array com valores aleatórios
print('-'*20)

#List Comprehension
#List Comprehension é uma técnica utilizada em Python para criar listas de forma mais simples e rápida.
#A sintaxe do List Comprehension é:
#[expressão for item in lista]

array = numpy.array([
    [i for i in range(0,3)],
    [i for i in range(3,6)],
    [i for i in range(6,9)]]
    ) #Criando um array com List Comprehension
print(array) #Imprimindo o array

#Slicing
#Slicing é uma técnica utilizada para acessar partes de um array.
#A sintaxe do Slicing é:

array = np.array([1,2,3,4,5,6,7,8,9,10]) #Criando um array
print(array[2]) #Acessando o terceiro elemento do array
print(array[2:4]) #Acessando do terceiro elemento até o quarto elemento do array
print('-'*20)

array = np.array([[1,2,3],[4,5,6],[7,8,9]]) #Criando um array

print(array, end='\n\n') #Imprimindo o array
print(array[2]) #Acessando a terceira linha do array
print(array[2][1]) #Acessando o segundo elemento da terceira linha do array
print(array[0:2]) #Acessando as duas primeiras linhas do array
print(array[0:2, 1:3]) #Acessando as duas primeiras linhas e as duas últimas colunas do array
print('-'*20)

array = np.array([[1,2,3],[4,5,6],[7,8,9]]) #Criando um array
print(array, end='\n\n') #Imprimindo o array
print(array[2, :]) #Acessando a terceira linha do array
print(array[:, 2]) #Acessando a segunda coluna do array
print('-'*20)

array = np.array([[1,2,3,4],[5,6,7,8]]) #Criando um array
print(array, end='\n\n') #Imprimindo o array
print(array[1, :]) #Acessando a segunda linha do array
print(array[:, 2]) #Acessando a segunda coluna do array
print('-'*20)

array = np.array([[1,2,3,4,5,6,7,8,9],[10,11,12,13,14,15,16,17,18],[19,20,21,22,23,24,25,26,27]]) #Criando um array
print(array, end='\n\n') #Imprimindo o array
print(array[1, :]) #Acessando a segunda linha do array
print(array[1:, 1:5]) #Acessando a segunda e a terceira linha e a segunda e a terceira coluna do array
print(array[2, ::2]) #Acessando a terceira linha do array com passo 2
print('-'*20)

#Iterando Arrays
#Para iterar um array, basta utilizar um laço de repetição for.

array = np.array([[1,2,3,4],[5,6,7,8]]) #Criando um array
for i in array: #Iterando um array de uma dimensão
    for j in i: #Iterando um array de duas dimensões
        print(j) #Imprimindo o elemento do array
        
print('-'*20)

array = np.array([[1,2,3,4],[5,6,7,8]]) #Criando um array
for x in np.nditer(array, order='F'): #Iterando um array de duas dimensões
    print(x) #Imprimindo o elemento do array
print('-'*20)


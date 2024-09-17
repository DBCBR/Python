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


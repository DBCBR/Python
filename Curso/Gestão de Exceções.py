#Gestão de Exceções	
#O Python possui um sistema de exceções que permite que o programador trate erros que podem ocorrer durante a execução de um programa.
#O bloco try/except é utilizado para tratar exceções. O bloco try contém o código que pode gerar uma exceção, e o bloco except contém o código que será executado caso a exceção ocorra.

print("Início") #Início
lista = [1, 2, 3, 4, 5] #lista de 1 a 5
try: # Método try
    print(lista[10]) #print lista 10
except Exception as erro: #except Exception as erro
    print("Falha ao acessar, linha não encontrada, mensagem: " + str(erro)) #print 
print("Fim") #Fim
print('-'*20)

try: # Método try
    numero = int('b') #numero = int('b')
except Exception as erro: #except Exception as erro
    print("Falha ao converter número, mensagem: " + str(erro)) #print
print('-'*20)

print("Início") #Início
lista = [1,2,3] #lista de 1 a 3
try: # Try
    print(lista[3]) #print lista 3
except:
    print("Erro ao acessar o elemento")
finally:
    del lista
    print("Executa sempre que o try-execpt acabar, mesmo que ocorra erro") #print
print("Fim") #Fim
print('-'*20)

print("Início") #Início
lista = [1,2,3] #lista de 1 a 3
try: # Try
    print(lista[10]) #print lista 3
except:
    print("Erro ao acessar o elemento")
else:
    print("Não houve erro") #print
print("Fim") #Fim
print('-'*20)

print("Início") #Início 
lista = [1,2,3] #lista de 1 a 3 
try: # Try
    print(lista[10]) #print lista 3
except: #except
    print("Erro ao acessar o elemento")
else: #else
    print("Não houve erro") #print
finally: #finally
    print("Executa sempre") #print
print("Fim")

#Diferentes tipos de exceções podem ser tratadas em blocos diferentes. O bloco except pode conter vários blocos, cada um tratando um tipo de exceção diferente.
#O bloco finally é executado sempre, independentemente de ocorrer uma exceção ou não. Ele é geralmente utilizado para liberar recursos utilizados no bloco try.
#O bloco else é executado somente se nenhuma exceção ocorrer no bloco try.

print("Início") #Início
lista = [1,2,3] #lista de 1 a 3
try: # Try
    print(lista[10]) #print lista 3
except IndexError as erro1:
    print("Erro de índice ao acessar o elemento, mensagem: " + str(erro1)) #print erro de índice ao acessar o elemento
except:
    print("Ocorreu outro erro") #print ocorreu outro erro
else:
    print("Não houve erro") #print não houve erro
print("Fim") #Fim
print('-'*20)

print("Início") #Início
lista = [1,2,3] # cria lista de 1 a 3
numero = 0 # atribui 0 a numero
try: # Inicia o try
    divisão = 10 / numero # divide 10 por numero
    print(lista[12]) # printa o elemento 10 da lista
except IndexError as erro1: 
    print("Erro de índice ao acessar o elemento, mensagem: " + str(erro1)) #print erro de índice ao acessar o elemento
except ZeroDivisionError as erro2: # except ZeroDivisionError as erro2
    print("Erro de divisão por zero, mensagem: " + str(erro2)) #print erro de divisão por zero
except Exception as erro3:
    print("Ocorreu outro erro " + str(erro3)) #print ocorreu outro erro
else:
    print("Não houve erro") #print não houve erro
print("Fim") #Fim
print('-'*20)

#Gerando exceções personalizadas
#O programador pode criar exceções personalizadas, herdando da classe Exception.
#O método __str__ é utilizado para retornar uma mensagem de erro personalizada.
#raise é utilizado para lançar uma exceção.
 
def printa_positivo(numero): #definindo função printa_positivo
    if numero < 0: #se numero for menor que 0
        raise ValueError("Valor não pode ser negativo") #raise ValueError("Valor não pode ser negativo")
    print(numero) #print numero
    
try: #try
    printa_positivo(-1) #printa_positivo(-1)
except ValueError as erro:
    print("o erro é: ", str(erro))
except Exception as erro1:
    print("Ocorreu outro erro: " + str(erro1))
print('-'*20)


def printa_positivo(numero): #definindo função printa_positivo
    assert(numero < 0) #se numero for menor que 0
    print(numero) #print numero
    
try: #try
    printa_positivo(-1) #printa_positivo(-1)
except AssertionError as erro:
    print("o erro é: ", str(erro))
except Exception as erro1:
    print("Ocorreu outro erro: " + str(erro1))
print('-'*20)

# lista = [1]
# try:
#     print(lista[10])
# except IndexError as error:
#     raise error

#Atividade

1
# def soma(str1, str2):
#     try:
#         num1 = float(str1)
#         num2 = float(str2)
#         return num1 + num2
#     except:
#         raise Exception("Falha no Casting")
    
# print(soma("10", "20"))
# print(soma("10", "abc"))

2
def acessa_seguro(lista, índice):
    try:
        return lista[índice]
    except:
        return None

lista = [1, 2, 3, 4, 5]
print(acessa_seguro(lista, 2))
print(acessa_seguro(lista, 10))
print('-'*20)

3
# def input_seguro():
#     try:
#         entrada = input("Digite algo:")
#         if entrada == "":
#             return None
#         return entrada
#     except:
#         return None

# print(input_seguro())
# print('-'*20)

4
class Carácter:
    def __init__(self, carácter):
        self.__carácter = ''
        self.carácter = carácter
    
    @property
    def carácter(self):
        return self.__carácter
    
    @carácter.setter
    def carácter(self, value):
        if len (value) > 1:
            raise Exception("O Carácter deve ter no máximo tamanho 1")
        
        self.__carácter = value

letra = Carácter("a")
print(letra.carácter)

try:
    letra.carácter = "ab"
except Exception as erro:
    print(str(erro))

print(letra.carácter)
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
class Carácter: #definindo classe Carácter
    def __init__(self, carácter): #definindo método __init__
        self.__carácter = '' #atribuindo valor vazio a __carácter
        self.carácter = carácter #atribuindo valor de carácter a __carácter 
    
    @property #propriedade de carácter
    def carácter(self): #definindo método carácter
        return self.__carácter #retorna __carácter
    
    @carácter.setter #setter de carácter
    def carácter(self, value): #definindo método carácter
        if len (value) > 1: #se o tamanho de value for maior que 1
            raise Exception("O Carácter deve ter no máximo tamanho 1") #raise Exception("O Carácter deve ter no máximo tamanho 1")
        
        self.__carácter = value #atribui value a __carácter

letra = Carácter("a") #letra = Carácter("a")
print(letra.carácter) #print letra.carácter

try: #try 
    letra.carácter = "ab" #letra.carácter = "ab"
except Exception as erro: #except Exception as erro
    print(str(erro)) #print erro

print(letra.carácter) #print letra.carácter
print('-'*20)

#Logs 
#O módulo logging é utilizado para gerar logs de execução de um programa.
#O método basicConfig é utilizado para configurar o log.
#O método getLogger é utilizado para recuperar o logger.
#O método debug é utilizado para registrar mensagens de debug.
#O método info é utilizado para registrar mensagens informativas.
#O método warning é utilizado para registrar mensagens de aviso.
#O método error é utilizado para registrar mensagens de erro.
#O método critical é utilizado para registrar mensagens críticas.
#O método exception é utilizado para registrar mensagens de exceção.

def custom_logger(level, message): #definindo função custom_logger
    import logging #importando módulo logging
    logger = logging.getLogger(__name__) #atribuindo a logger o getLogger(__name__)
    if not (len(logger.handlers)): #se o tamanho de logger.handlers for 0
        logging.basicConfig(level=logging.INFO)#atribui a logging.basicConfig(level=logging.INFO)
        c_handler = logging.StreamHandler() #atribui a c_handler a logging.StreamHandler()
        f_handler = logging.FileHandler('file.log') #atribui a f_handler a logging.FileHandler('file.log')
        format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s') #atribui a format a logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        c_handler.setFormatter(format) #atribui a c_handler.setFormatter(format)
        f_handler.setFormatter(format) #atribui a f_handler.setFormatter(format)
        logger.addHandler(c_handler) #adiciona c_handler a logger
        logger.addHandler(f_handler) #adiciona f_handler a logger
        
    if level == 'debug': #se level for debug
        logger.debug(message)
    elif level == 'info': #se level for info
        logger.info(message)
    elif level == 'warning': #se level for warning
        logger.warning(message)
    elif level == 'error': #se level for error
        logger.error(message)
    elif level == 'critical': #se level for critical
        logger.critical(message)
    elif level == 'exception': #se level for exception
        logger.exception(message)
    else:
        logger.info(message)
        
custom_logger("error", "Parâmetro errado!")


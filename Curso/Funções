#Funções  
#Funções são blocos de código que podem ser chamados e executados em qualquer parte do código.
# Elas são definidas pela palavra reservada def seguida do nome da função e dos parênteses que podem conter argumentos.
# A função pode ou não retornar um valor, e isso é feito pela palavra reservada return.

def func():
    num = 10
    print("Uma função %d" % num)
func()

def func():
    pass
func()

def print_var(numero):
    print(numero)
print_var(10)
print('maça')

def print_soma(num1, num2):
    print(num1 + num2)
print_soma(10, 20)
print_soma(3.3, 1.1)
print_soma("Olá", "Mundo!")

def func(*args):
    print(type(args))
    print("Argumentos são: ", args)
    
func(1, 2, 3, 4, 5)
func()
func("Olá", True, [1, 2, 3])

def print_sub(num1, num2):
    print(num1 - num2)
print_sub(10, 20)   

def func(*args, outro):
    print("Argumentos são: ", args)
    print(outro)
    
func(1,2,3, outro='1')
func(outro='2')
func("Olá", True, [1, 2, 3], outro='3')

#Argumentos Arbitrários
# Se você não sabe quantos argumentos serão passados para a função, você pode usar *args.
# Este é um argumento arbitrário que pode ser passado para a função.

def func(valor, nome="Teste"):
    print(nome, valor)

func(3)
func(3, "Outro")

def func(**args):
    print(type(args))
    print(args)
    print(args['nome'])
    
func(nome="Teste", valor=3)

def printa(x):
    print(x)

def executa_func(func, x):
    func(x)

minha_função = printa
print(type(minha_função))

executa_func(minha_função, 10)
print("-"*20)

#Funções que Retorna Valores
# Funções podem retornar valores usando a palavra reservada return.
# Se a função não retornar um valor, ela retornará None.

def subtrai(num1, num2):
    valor = num1 - num2
    return valor

resultado = subtrai(10, 20)
print(resultado)

def len_int(numero):
    numero_em_texto = str(numero)
    return len(numero_em_texto)

num1 = "10"
num2 = 1230
tamanho1 = len_int(num1)
tamanho2 = len_int(num2)
print("O número %s tem %d dígitos" % (num1, tamanho1))
print("O número %d tem %d dígitos" % (num2, tamanho2))

def retorna_múltiplo():
    return 1,2
valor = retorna_múltiplo()
print(valor)
print(type(valor))

def retorna_múltiplo(a, b, c):
    a += a
    b += b
    c += c
    return a, b, c

x, y, z = retorna_múltiplo(1,2,3)
print(x, y, z)
a = retorna_múltiplo(1,2,3)
print(a)

def func(x):
    if x == "Olá":
        print("Olá")
        return
    print("Mundo")
    return x
print(func("x"))
print("-"*20)



#Funções Lambda
# Funções lambda são funções anônimas que podem ser definidas em uma linha.
# Elas são definidas pela palavra reservada lambda seguida dos argumentos e dois pontos, e então a expressão a ser retornada.


faz_soma = lambda x : x+ 10
valor = faz_soma(2)
print(valor)
print("-"*20)

multiplica = lambda x, y : x * y
valor = multiplica(2, 10)
print(valor)
print("-"*20)

def multiplica(y):
    return lambda x : x * y
valor = multiplica(2)
resultado = valor(10)
print(resultado)
print("-"*20)

def print_num(num):
    print(num)
    if num >= 10:
        return
    print_num(num + 1)
print_num(0)
print("-"*20)

def print_str(texto, índice):
    if índice == len(texto):
        return
    print(texto[índice])
    print_str(texto, índice + 1)
print_str("Olá Mundo!", 0)
print("-"*20)

def fatorial(n):
    if n == 0:
        return 1
    return n * fatorial(n - 1)
print(fatorial(5))
print("-"*20)

#Funções Aninhadas 
# Funções podem ser aninhadas, ou seja, uma função pode ser definida dentro de outra função.
# A função aninhada pode acessar variáveis da função externa, mas não o contrário.

def pai():
    def filho():
        print("Sou Filho")
    filho()
pai()
print("-"*20)

def calculadora(num1, num2, op):
    def soma(a, b):
        return a + b
    def subtrai(a, b):
        return a - b
    if op == "+":
        return soma(num1, num2)
    elif op == "-":
        return subtrai(num1, num2)
    else:
        return "Operação inválida"
print(calculadora(10, 20, "+"))
print(calculadora(10, 20, "-"))
print(calculadora(10, 20, "*"))
print("-"*20)

def pega_func_print():
    def print_var(var):
        print(var)
    return print_var
    
print_me = pega_func_print()
print_me(10)
print_me("Olá")
print("-"*20)

#Decoradores
# Decoradores são funções que envolvem outras funções para adicionar funcionalidades a elas.
# Eles são definidos com a palavra reservada @ seguida do nome do decorador.

def DeixaMaiúsculo(func):
    def inner_func():
        return func().upper()
    return inner_func
    
@DeixaMaiúsculo
def retorna_string():
    return 'string de teste'

valor = retorna_string()
print(valor)
print("-"*20)

def DeixaMaiúsculo(func):
    def inner_func(str1, str2):
        return func(str1,str2).upper()
    return inner_func

@DeixaMaiúsculo
def concatena_string(str1, str2):
    return str1 + str2
valor = concatena_string("Olá", "Mundo!")
print(valor)
print("-"*20)

def DeixaMaiúsculo(func):
    def inner_func(texto):
        return func(texto).upper()
    return inner_func

def InsereParenteses(func):
    def inner_func(texto):
        return "(" + func(texto) + ")"
    return inner_func

@DeixaMaiúsculo
@InsereParenteses
def formata_string(texto):
    return texto

print(formata_string("Olá Mundo!"))
print("-"*20)

#Atividades
1
def e_negativo(num):
    if num < 0:
        return True
    return False

print(e_negativo(-1))
print(e_negativo(1))
print("-"*20)

2
def soma_array(array):
    soma = 0
    for num in array:
        soma += num
    return soma
print(soma_array([1, 2, 3, 4, 5]))
print("-"*20)

3
def contar_vogais(string):
    vogais = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']
    count = 0
    for char in string:
        if char in vogais:
            count += 1
    return count

string = "Ola Mundo!"
num_vogais = contar_vogais(string)
print("O número de vogais na string é:", num_vogais)
print("-"*20)

4
def ultima_letra(string):
    return string[-1]

string = "Olá Mundo"
letra = ultima_letra(string)
print("A última letra da string é:", letra)
print("-"*20)

5
def calculadora(num1, num2, op):
    if op == "+":
        return num1 + num2
    else:
        return num1 - num2
    
print(calculadora(5, 1, '-'))
print("-"*20)

6
def encontra_na_lista(lista, valor):
    if valor in lista:
        return True
    return False

lista = [1, 2, 3, 4, 5]
print(encontra_na_lista(lista, 3))
print("-"*20)

7
def encontra_na_lista(lista, valor):
    if valor in lista:
        return True
    return False

def posição_na_lista(lista, valor):
    if valor in lista:
        return lista.index(valor)
    return -1

lista = [1, 2, 3, 4, 5]
print(encontra_na_lista(lista, 3))
print(posição_na_lista(lista, 3))
print("-"*20)

8
def parâmetros(*args):
    for i in args:
        print(type(i))

parâmetros(1, 2, 3, "Olá", True, [1, 2, 3])
print("-"*20)

9
def DeixaMinusculo(func):
    def inner_func(texto):
        return func(texto).lower()
    return inner_func

def InsereAspas(func):
    def inner_func(texto):
        return "\"" + func(texto) + "\""
    return inner_func

@DeixaMinusculo
@InsereAspas
def formata_string(texto):
    return texto

print(formata_string("Olá Mundo!"))
print("-"*20)

10 
def divisão_inteira(num):
    if num == 11:
        return
    print(num // 3)
    divisão_inteira(num + 1)
divisão_inteira(0)
print("-"*20)

#Escopo de Variáveis
# O escopo de uma variável é a região do código onde a variável é acessível.
# Variáveis podem ser acessadas globalmente ou localmente.
# Variáveis globais são acessíveis em qualquer parte do código, enquanto variáveis locais são acessíveis apenas dentro de funções.
# Variáveis locais são criadas quando a função é chamada e destruídas quando a função termina.
# Variáveis globais são criadas fora de funções e são acessíveis em qualquer parte do código.


var2 = 10
def func():
    print(var2)
    variável_local = 10
    
func()
print("-"*20)

var2 = 10

if True:
    var2 = 20
print(var2)

print("-"*20)

var2 = 10

def func():
    var2 = 20
    print(var2)

func()
print(var2)
print("-"*20)

var2 = 10

def func():
    global var2
    var2 = 20
    
func()
print(var2)
print("-"*20)

def func_pai():
    pai = 10
    def func_filho():
        print(pai)
    func_filho()
func_pai()
print("-"*20)

def func_pai(): 
    pai = 10
    def func_filho(): 
        nonlocal pai
        pai = 20
        print(pai)
    func_filho()
    print(pai)
func_pai()
print("-"*20)

array = [1, 2, 3, 4, 5]
del array[0]
print(array)
print("-"*20)

array = [1, 2, 3, 4, 5]
del array[:2]
print(array)
print("-"*20)

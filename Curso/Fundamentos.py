#Comandos para imprimir na tela
print("David Barcellos Cardoso")
print("Tenho 37 anos")
print("Minha altura é de 1,81\n")
print("David Barcellos Cardoso\nTenho 37 anos\nMinha altura é de 1,81\n")
print("Nome: {}, idade: {} e altura: {}\n".format("David", 37, 1.81))
print("4", "8", "16", sep=' - ')
print("-"*20)

#Variáveis
_numero = 1
Numero = 2
numero = 3
numero123 = 4
print(_numero, Numero, numero, numero123)

#Tipos Primitivos
variável = None
print(variável)
inteiro = 10
print(inteiro)
decimal = 10.5
print(decimal)
texto = "David"
print(texto)
booleano = True
print(booleano)
booleano = False
print(booleano)
print("-"*20)

#Atividade Variáveis
nome = "David"
cpf = "123.456.789-10"
civil = "Casado"
print("Nome: {}\nCPF: {}\nEstado Civil: {}".format(nome, cpf, civil))
print("-"*20)

#Formatação
# %s - Texto
# %d - Inteiro
# %f - Decimal
# %r - Booleano

nome = "David"
texto_formatado = "Meu nome é %s" % nome
print(texto_formatado)
idade = 37
altura = 1.81
texto = "Meu nome é %s, tenho %d anos e %.2f de altura\n" % (nome, idade, altura)
print(texto)
pi = 3.14159265359
texto = "O valor de PI é %f\n" % pi
print(texto)
valor = True
print("O valor é %s" % valor)
print("O valor é %d\n" % valor)
decimal = 10.54321
print("A parte inteira é %d" % decimal)
print("-"*20)

#Formatação com Caracteres Especiais
# \n - Quebra de Linha
# \t - Tabulação
# \b - Backspace
# \r - Carriage Return
# \f - Form Feed
# \\ - Barra Invertida
# \' - Aspas Simples
# \" - Aspas Duplas
texto = "Olá, é assim que se quebra uma linha,\n\t e é assim que se dá um tab!\n"
print(texto)
print("-"*20)

#Atividades Formatação
dia = 16
mês = 10
ano = 1986
print("Data de Nascimento: %d/%d/%d" % (dia, mês, ano))
hora = 16
minuto = 40
print("Agora são %d:%d" % (hora, minuto))
print("-"*20)

#Operadores Aritméticos
# + - Soma
# - - Subtração
# * - Multiplicação
# / - Divisão
# // - Divisão Inteira
# % - Resto da Divisão
# ** - Potenciação
print(10 + 5)
numero = 10 + 10.5
print(numero)
numero2 = 30 + numero
print(numero2)
numero = 20 - 10
print(numero)
numero = 10 * 5
print(numero)
numero = 10 / 3
print(numero)
numero = 10 // 3
print(numero)
numero = 10 % 3
print(numero)
numero = 10 ** 3
print(numero)
print("-"*20)

#Atividades
print("1")
ano_atual = 2024
ano_nascimento = 1986
idade = ano_atual - ano_nascimento
print("Idade: %d" % idade)
print("-"*20)
print("2")
num1 = 10
num2 = 20
num3 = 30
media = (num1 + num2 + num3) / 3
print("Média: %.2f" % media)
print("-"*20)
print("3")
peso = 115
altura = 1.81
imc = peso / (altura ** 2)
print("IMC: %.2f" % imc)
print("-"*20)
print("4")
ovos_páscoa = 12
crianças = 5
print("Total de %d ovos de páscoa para %d crianças" % (ovos_páscoa, crianças))
ovos_por_criança = ovos_páscoa / crianças
print("Ovos por Criança: %d" % ovos_por_criança)
print("Ficaram sobrando %d ovos" % (ovos_páscoa % crianças))
print("-"*20)

#Operadores Lógicos
# and - E
# or - OU
# not - NÃO
# == - Igual
# != - Difer
# > - Maior
# < - Menor
# >= - Maior ou Igual
# <= - Menor ou Igual
print("AND")
print(True and True)
print(True and False)
print(False and True)
print(False and False)
print("-"*20)
print("OR")
print(True or True)
print(True or False)
print(False or True)
print(False or False)
print("-"*20)
print("NOT")
print(not True)
print(not False)
print("-"*20)

#Atividades Com Operadores Lógicos
print("1")
faltar_comida = True
se_for_sábado = True
print("Devo ir ao mercado?" , faltar_comida or se_for_sábado)
print("-"*20)
print("2")
sinal_vermelho = True
carro_vindo_direita = False
carro_vindo_esquerda = False
atravessar_rua = sinal_vermelho and not carro_vindo_direita and not carro_vindo_esquerda
print("Posso atravessar a rua?" , atravessar_rua)
print("-"*20)
print("3")
sinal_vermelho = False
carro_vindo_direita = True
carro_vindo_esquerda = True
atravessar_rua = sinal_vermelho or not carro_vindo_direita and not carro_vindo_esquerda
print("Estou com pressa posso atravessar a rua?" , atravessar_rua)
print("-"*20)

#Casting - Conversão de Tipos
# int() - Inteiro
# float() - Decimal
# str() - Texto
# bool() - Booleano
# type() - Tipo
numero = 10
texto = "10"
decimal = 10.5
booleano = True
print(type(numero))
print(type(texto))
print(type(decimal))
print(type(booleano))
print("-"*20)

#Atividades Casting
conta = "10000"
saque = 1000
saldo = int(conta) - saque
print("Saldo: %d" % saldo)
print("-"*20)
saldo = 1000
saldo_zerado = not bool(saldo)
print("Saldo Zerado?" , saldo_zerado)
print("-"*20)
altura = 1.81
print("Altura: %d" % int(altura))
print("-"*20)

#Entrada de Dados
# input() - Entrada de Dados
# nome = input("Digite seu nome: ")
# print("Seu nome é: %s" % nome)
# print("Digite sua data de nascimento")
# dia = input("Dia: ")
# mês = input("Mês: ")
# ano = input("Ano: ")
# print("Data de Nascimento: %s/%s/%s" % (dia, mês, ano))

#Atividades Entrada de Dados
# num1 = int(input("Digite o primeiro número: ")) 
# num2 = int(input("Digite o segundo número: "))
# div = num1 / num2
# print("A divisão de %d por %d é %.2f" % (num1, num2, div))
# print("-"*20)
# dia = int(input("Digite o dia: "))
# mes = int(input("Digite o mês: "))
# ano = int(input("Digite o ano: "))
# hora = int(input("Digite a hora: "))
# minuto = int(input("Digite os minutos: "))
# seg = int(input("Digite os segundos: "))
# print("Data e Hora: %d/%d/%d %d:%d:%d" % (dia, mes, ano, hora, minuto, seg))
print("-"*20)

#Operadores de Atribuição e Combinação de Operadores Lógicos
# = - Atribuição
# += - Soma
# -= - Subtração
# *= - Multiplicação
# /= - Divisão
# //= - Divisão Inteira
# %= - Resto da Divisão
# **= - Potenciação
# &= - E
# |= - OU
# ^= - OU Exclusivo
# >>= - Deslocamento para Direita
# <<= - Deslocamento para Esquerda

numero = 10
numero += 1 # numero = numero + 1 (soma)
print(numero)
numero -= 1 # numero = numero - 1 (subtração)
print(numero)
numero *= 2 # numero = numero * 2 (multiplicação)
print(numero)
numero /= 2 # numero = numero / 2 (divisão)
print(numero)
numero //= 2 # numero = numero // 2 (divisão inteira)
print(numero)
numero %= 2 # numero = numero % 2 (resto da divisão)
print(numero)
numero **= 2 # numero = numero ** 2 (potenciação)
print(numero)
numero = 10
numero &= 0 # numero = numero & 0 (E)
print(numero)
numero = 10
numero |= 0 # numero = numero | 0 (OU)
print(numero)
numero = 10
numero ^= 0 # numero = numero ^ 0 (OU Exclusivo)
print(numero)
numero = 10
numero >>= 1 # numero = numero >> 1 (deslocamento para direita)
print(numero)
numero = 10
numero <<= 1 # numero = numero << 1 (deslocamento para esquerda)
print(numero)
print("-"*20)

# nota1 = float(input("Digite a primeira nota: "))
# nota2 = float(input("Digite a segunda nota: "))
# media = (nota1 + nota2) / 2
# aprovação = media >= 7 or nota1 >= 5 and nota2 >= 5
# print("Média: %.2f" % media)
# print("Aprovação: %s" % aprovação)
# print("-"*20)

# senha = "1234"
# senha_digitada = input("Digite a senha: ")
# senha_correta = senha == senha_digitada
# print("Senha correta? %s" % senha_correta)
print("-"*20)

#Slice - Fatiamento de Texto
# texto = "David"
# print(texto[0]) # D
# print(texto[1]) # a
# print(texto[2]) # v
# print(texto[3]) # i
# print(texto[4]) # d

var = "Exemplo" 
print(var[0:3]) # Exe (0, 1, 2) - 3 não entra
print(var[3:6]) # mpl (3, 4, 5) - 6 não entra
print(var[:3]) # Exe (0, 1, 2) - 3 não entra
print(var[3:]) # mplo (3, 4, 5) - 6 não entra
print(var[:]) # Exemplo (0, 1, 2, 3, 4, 5) - 6 não entra
print("-"*20)

#Operadores sobre Strings
# + - Concatenação 
# * - Repetição 
# in - Verifica se existe
# not in - Verifica se não existe
# == - Igual
# != - Difer
# > - Maior
# < - Menor
# >= - Maior ou Igual

texto1 = "David"
texto2 = "Barcellos"
texto3 = "Cardoso"
print(texto1 + " " + texto2 + " " + texto3)
print("-"*20)

texto = "Exemplo"
print(texto[0:4])
print(texto[1:3])
print(texto[:6])
print("-"*20)

texto = "Carro"
print(texto[-4])
print(texto[-4:])
print(texto[:-2])
print(texto[-5:-2])
print("-"*20)

texto = "metro"
print(texto[::-1])
print(texto[3::-1])
print(texto[3:1:-1])
print("-"*20)

texto1 = "David"
texto2 = "David"
igual = texto1 == texto2
print("Textos são iguais?", igual)
print("-"*20)

print("a" != "b")
print("a" > "b")
print("a" < "b")
print("-"*20)

texto = "Programação"
print ("a" in texto)    
print ("a" not in texto)
print("Programa" in texto)
print("Programa" not in texto)
print("-"*20)

tamanho = len(texto)
print(tamanho)
print("-"*20)

#Atividades com Strings
texto = "David Barcellos Cardoso"
print(texto[0:5])
print(texto[6:15])
print(texto[16:])
print("-"*20)

# texto = input("Digite um palavra: ")
# print(texto[:-1:])
# print("-"*20)

# texto = input("Digite uma palavra: ")
# vogal = ("a" in texto) or ("e" in texto) or ("i" in texto) or ("o" in texto) or ("u" in texto)
# print("A palavra possui vogal?", vogal)
# print("-"*20)

# texto = input("Digite uma palavra: ")
# texto = "ABC" + texto[0:]
# print(texto)
print("-"*20)


#Estruturas de Programação

#IF 

print("Isto está fora dos ifs")
if(True):
    print("Este código vai ser executado")
    if(False):
        print("Isto está dentro do segundo if")
    print("Isto está dentro do primeiro if")
print("Isto está fora do primeiro if")
print("-"*20)

valor1 = 10
valor2 = 10
if(valor1 == valor2):
    print("Os valores são iguais")
print("-"*20)

if 10 != 20:
    print("Os valores são diferentes")

if 10 != 10:
    print("Os valores são diferentes")

if ("olá" != "alo"):
    print("As strings são diferentes")
    
numero = 11
if numero > 10:
    print("O número é maior que 10")

# nome = input("Digite o seu nome: ")
# if "a" in nome:
#     print("O seu nome contém a letra 'a'")

# nome = input("Digite o seu nome: ")
# possui_vogal = "a" in nome or "e" in nome or "i" in nome or "o" in nome or "u" in nome
# if possui_vogal:
#     print("O seu nome contém uma vogal")
print("-"*20)

#IF ELSE

numero = 9
if numero >= 10:
    print("O número é maior ou igual a 10")
else:
    print("O número é menor que 10")
print("-"*20)

numero = 10
if numero % 2 == 0:
    print("O número é par")
else:
    print("O número é ímpar")
print("-"*20)

valor = 11
if valor >= 0 and valor <= 10:
    print(valor)
else:
    print("O valor não está entre 0 e 10")
print("-"*20)

texto = "a"
if len(texto) == 1:
    print("Tem um caractere")
else:
    print("O texto tem mais de um caractere")
print("-"*20)

#IF ELIF ELSE

numero = 1
if numero == 1 or numero == 0:
    print("O número é 0 ou 1")
print("-"*20)

numero = 10
if numero > 0:
    print("Número é maior que zero")
    if numero > 10:
        print("Número é maior que 10")
print("-"*20)

numero = 10
resultado = "PAR" if numero % 2 == 0 else "ÍMPAR"
print(resultado)
print("-"*20)

#Atividades

# saldo_entrada = input("Digite seu saldo: ")
# valor_devido = input("Digite o valor devido: ")
# saldo = float(saldo_entrada)
# divida = float(valor_devido)
# valor_total = saldo - divida
# if valor_total >= 0:
#     print("Saldo é positivo, você tem R$ %.2f" % valor_total)
# else:
#     print("Saldo é negativo, você deve R$ %.2f" % valor_total)
# print("-"*20)  

# cpf = "123.456.789-10"
# senha = "123456"
# senha_digitada = input("Digite sua senha: ")
# if senha == senha_digitada:
#     print("Senha correta, seu CPF é:", cpf)
# else:
#     print("Senha incorreta")
# print("-"*20)

# idade = int(input("Digite a sua idade: "))
# if idade <= 3:
#   print("Você é um bebê!")
# else idade <= 13:
#   print("Você é uma criança!")
# else idade <= 18:
#   print("Você é um adolescente!")
# else idade <= 65:
#   print("Você é um adulto!")
# else:
#   print("Você é um idoso!")
# print("-"*20)

# num1 = float(input("Digite o primeiro número: "))
# num2 = float(input("Digite o segundo número: "))
# escolha = input("Digite a operação desejada: 1 para soma, 2 para subtração, 3 para divisão e 4 para multiplicação: ")
# if escolha == "1":
#     print(num1 + num2)
# elif escolha == "2":
#     print(num1 - num2)
# elif escolha == "3":
#     print(num1 / num2)
# elif escolha == "4":
#     print(num1 * num2)
# else:
#     print("Operação inválida")
# print("-"*20)

#Laços de Repetição 
#WHILE

numero = 10
print("Início do laço")
while numero > 0:
    print(numero)
    numero -= 1
print("Fim do laço")
print("-"*20)

número = 10
print("Início do laço")
while número >= 0:
    resto = número % 2
    if resto == 0:
        print("O número %d é par" % número)
    else:
        print("O número %d é ímpar" % número)
    número -= 1
print("Fim do laço")
print("-"*20)

# soma = 0
# números_lidos = 0
# while números_lidos < 5:
#     num_str = input("Digite um número: ")
#     num_lido = float(num_str)
#     soma += num_lido
#     números_lidos += 1
# print("A soma dos números é: %.2f" % soma)
# print("-"*20)

texto = "Olá 123 _"
índice= 0
while índice < len(texto):
    print(texto[índice])
    índice += 1
print("-"*20)

num_atual = 0
while True:
    if num_atual == 5:
        break
    print(num_atual)
    num_atual += 1
print("Encerrou")
print("-"*20)

num_atual = 0
while num_atual < 10:
    num_atual += 1
    if num_atual == 7:
        continue
    print(num_atual)
print("Encerrou")
print("-"*20)

#Atividades de Laços de Repetição

#1
# soma_atual = 0
# números_lidos = 0
# while números_lidos < 5:
#      num_str = input("Digite um número: ")
#      num_lido = float(num_str)
#      soma_atual += num_lido
#      números_lidos += 1
# media = soma_atual / 5
# print("A média dos números é: %.2f" % media)
# print("-"*20)


#2
# soma_atual = 0
# números_lidos = 0
# while números_lidos < 5:
#      num_str = input("Digite um número: ")
#      num_lido = float(num_str)
#      if num_lido >=0:
#         soma_atual += num_lido
#      números_lidos += 1
# print("A soma é: %.2f" % soma_atual)
# print("-"*20)

#3
# números_digitados = float(input("Digite quantos números serão lidos: "))
# soma_atual = 0
# números_lidos = 0
# while números_lidos < números_digitados:
#      num_str = input("Digite um número: ")
#      num_lido = float(num_str)
#      soma_atual += num_lido
#      números_lidos += 1
# print("O total é: %.2f" % soma_atual)
# print("-"*20)

#4
num_atual = 2
while num_atual <= 10:
    resto = num_atual % 2
    if resto == 0:
        print("O número %d é par" % num_atual)
    else:
        print("O número %d é ímpar" % num_atual)    
    num_atual += 1
print("-"*20)

#5
# texto = input("Digite um texto: ")
# índice= 0
# num_vazio = 0
# while índice < len(texto):
#     if texto[índice] == " ":
#         num_vazio += 1
#     índice += 1
# print("O texto tem %d espaços" % num_vazio)
# print("-"*20)

#For

for x in range(10):
    print(x)
print("-"*20)
    
for x in range(5,10):
    print(x)
print("-"*20)

for x in range(5,20,5):
    print(x)
print("-"*20)

for x in range(20,5,-5):
    print(x)
print("-"*20)

texto = "123456789"
for x in range(len(texto)):
    print(texto[x])
print("-"*20)

# letra = input("Digite uma letra: ")
# if len(letra) != 1:
#     print("Digite apenas uma letra")
# else:
#     texto = input("Digite um texto: ")
#     for i in range(len(texto)):
#         if texto[i] == letra:
#             print("A letra %s está na posição %d" % (letra, i))
# print("-"*20)

for x in range(0,3):
    for y in range(0,5):
        print(x,y)
print("-"*20)

for x in range(1,11):
    print("-"*20)
    for y in range(1,11):
        print("%d x %d = %d" % (x, y, x*y))
print("-"*20)

#Atividades de Laços de Repetição For

#1
# texto = input("Digite um texto: ")
# quantidade_caracteres = 0
# for caractere in texto:
#     if caractere != " ":
#         quantidade_caracteres += 1
# print("O texto tem %d caracteres" % quantidade_caracteres)
# print("-"*20)

#2
# fatorial = input("Digite um número para calcular o fatorial: ")
# fatorial = int(fatorial)
# resultado = 1
# for i in range(1, fatorial+1):
#     resultado *= i
# print("O fatorial de %d é %d" % (fatorial, resultado))
# print("-"*20)

# 3
# número_leituras = int(input("Digite o número de textos serão lidos: "))
# texto_total = ""
# for i in range(número_leituras):
#     texto_total += input("Digite um texto: ")
# print("Texto completo: ", texto_total)
# print("-"*20)

# 4
# número = int(input("Digite um número para tabuada de divisão: "))
# for i in range(1,11):
#      print("%d / %d = %.2f" % (i,número, i/número))
# print("-"*20)

5
for numero in range(3,31):
    e_primo = True
    
    for num_teste in range(2,numero):
        if numero % num_teste == 0:
            e_primo = False
            break
    if e_primo:
        print("O número %d é primo" % numero)
    else:
        print("O número %d não é primo" % numero)
print("-"*20)
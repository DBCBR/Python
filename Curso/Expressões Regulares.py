#Expressões Regulares
#Expressões regulares são padrões utilizados para selecionar combinações de caracteres em uma string. Em Python, as expressões regulares são implementadas no módulo re. Para utilizar expressões regulares em Python, você precisa importar o módulo re: import re 
#O módulo re oferece várias funções que tornam mais fácil trabalhar com expressões regulares. Alguns dos mais comuns incluem: re.match(), re.search(), re.findall(), re.split(), re.sub(), re.compile().
#re.match() - Verifica se o padrão está no início da string.
#re.search() - Verifica se o padrão está em qualquer lugar da string.
#re.findall() - Retorna uma lista com todas as correspondências.
#re.split() - Divide a string onde houver uma correspondência.
#re.sub() - Substitui uma ou mais correspondências por um texto.
#re.compile() - Compila uma expressão regular em um objeto.

import re #Importando o módulo re
texto = '000556141564' #Definindo uma string
info = re.search('5', texto) #Procurando o padrão '5' na string
if info != None: #Se o padrão for encontrado na string 
    print('Encontrado ocorrência em:', info.span()) #Imprime a posição do padrão na string
    print('O que foi encontrado:', info.group()) #Imprime o padrão encontrado
else: #Se o padrão não for encontrado na string
    print('Não encontrado!') #Imprime que o padrão não foi encontrado

info = re.findall('5', texto) #Procurando o padrão '5' na string
print('Ocorrências encontradas:', info) #Imprime as ocorrências encontradas

info = re.split('5', texto) #Dividindo a string onde houver o padrão '5'
print('String dividida:', info) #Imprime a string dividida

info = re.sub('5', '#', texto) #Substituindo o padrão '5' por 'X'
print('String modificada:', info) #Imprime a string modificada

print('-'*20)

import re #Importando o módulo re
texto = 'existem milhões de grãos de areia no deserto' #Definindo uma string
info = re.search('de', texto) #Procurando o padrão '5' na string
if info != None: #Se o padrão for encontrado na string 
    print('Encontrado ocorrência em:', info.span()) #Imprime a posição do padrão na string
    print('O que foi encontrado:', info.group()) #Imprime o padrão encontrado
else: #Se o padrão não for encontrado na string
    print('Não encontrado!') #Imprime que o padrão não foi encontrado

print('-'*20)

texto = 'ABCDefgHI123'

info1 = re.findall('[Ae3]', texto) 
info2 = re.findall('[A-Z]', texto) 
info3 = re.findall('[a-z]', texto)
info4 = re.findall('[0-9]', texto)
info5 = re.findall('[A-Za-z]', texto)

print(info1)
print(info2)
print(info3)
print(info4)
print(info5)

print('-'*20)

texto = 'existem milhões de grãos de areia no deserto'
info = re.findall('milhões|grãos', texto)
print(info)

print('-'*20)

texto = 'ABCDefgHI123'
info = re.findall('[A-Z]|[0-9]', texto)
print(info)

print('-'*20)

texto = 'existem milhões de grãos de areia no deserto'
info = re.search("^existem", texto)
if info != None:
    print('Encontrado ocorrência em:', info.span()) #Imprime a posição do padrão na string
    print('O que foi encontrado:', info.group()) #Imprime o padrão encontrado

print('-'*20)

texto = 'existem milhões de grãos de areia no deserto'
info = re.search("deserto$", texto)
if info != None:
    print('Encontrado ocorrência em:', info.span()) #Imprime a posição do padrão na string
    print('O que foi encontrado:', info.group()) #Imprime o padrão encontrado

print('-'*20)
#Mais Padrões

import re #Importando o módulo re
texto = 'abbabb' #Definindo uma string
info = re.search('abb', texto) #Procurando o padrão 'abb' na string
if info != None: #Se o padrão for encontrado na string 
    print('Encontrado ocorrência em:', info.span()) #Imprime a posição do padrão na string
    print('O que foi encontrado:', info.group()) #Imprime o padrão encontrado
else: #Se o padrão não for encontrado na string
    print('Não encontrado!') #Imprime que o padrão não foi encontrado

print('-'*20)

import re #Importando o módulo re
texto = 'aabbaabbbbbbaaccaa' #Definindo uma string
info = re.search('(abb)+', texto) #Procurando o padrão 'abb' na string
if info != None: #Se o padrão for encontrado na string 
    print('Encontrado ocorrência em:', info.span()) #Imprime a posição do padrão na string
    print('O que foi encontrado:', info.group()) #Imprime o padrão encontrado
else: #Se o padrão não for encontrado na string
    print('Não encontrado!') #Imprime que o padrão não foi encontrado

print('-'*20)

import re #Importando o módulo re
texto = 'aabbaabbbbbbaaccaa' #Definindo uma string
info = re.search('(aa|bb)+', texto) #Procurando o padrão 'abb' na string
if info != None: #Se o padrão for encontrado na string 
    print('Encontrado ocorrência em:', info.span()) #Imprime a posição do padrão na string
    print('O que foi encontrado:', info.group()) #Imprime o padrão encontrado
else: #Se o padrão não for encontrado na string
    print('Não encontrado!') #Imprime que o padrão não foi encontrado

print('-'*20)

import re #Importando o módulo re
texto = 'aabbaabbbbbbaaccaa' #Definindo uma string
info = re.search('(aa|bb){3}', texto) #Procurando o padrão 'abb' na string
if info != None: #Se o padrão for encontrado na string 
    print('Encontrado ocorrência em:', info.span()) #Imprime a posição do padrão na string
    print('O que foi encontrado:', info.group()) #Imprime o padrão encontrado
else: #Se o padrão não for encontrado na string
    print('Não encontrado!') #Imprime que o padrão não foi encontrado

print('-'*20)

import re #Importando o módulo re
texto = 'abc' #Definindo uma string
info = re.search('(aa|bb)*', texto) #Procurando o padrão 'abb' na string
if info != None: #Se o padrão for encontrado na string 
    print('Encontrado ocorrência em:', info.span()) #Imprime a posição do padrão na string
    print('O que foi encontrado:', info.group()) #Imprime o padrão encontrado
else: #Se o padrão não for encontrado na string
    print('Não encontrado!') #Imprime que o padrão não foi encontrado

print('-'*20)

import re #Importando o módulo re
texto = '' #Definindo uma string
info = re.search('^(aa)?$', texto) #Procurando o padrão 'abb' na string
if info != None: #Se o padrão for encontrado na string 
    print('Encontrado ocorrência em:', info.span()) #Imprime a posição do padrão na string
    print('O que foi encontrado:', info.group()) #Imprime o padrão encontrado
else: #Se o padrão não for encontrado na string
    print('Não encontrado!') #Imprime que o padrão não foi encontrado

print('-'*20)

import re #Importando o módulo re
texto = 'aaaaaa' #Definindo uma string
info = re.search('^(aa){2,3}$', texto) #Procurando o padrão 'abb' na string
if info != None: #Se o padrão for encontrado na string 
    print('Encontrado ocorrência em:', info.span()) #Imprime a posição do padrão na string
    print('O que foi encontrado:', info.group()) #Imprime o padrão encontrado
else: #Se o padrão não for encontrado na string
    print('Não encontrado!') #Imprime que o padrão não foi encontrado

print('-'*20)

#Caracteres Especiais
#Além de letras e números, expressões regulares também podem conter caracteres especiais. Alguns dos caracteres especiais mais comuns incluem: ., ^, $, *, +, ?, {, }, [, ], |, (, ), \, e /.
#O caractere . corresponde a qualquer caractere único, exceto uma nova linha.
#O caractere ^ corresponde ao início de uma string.
#O caractere $ corresponde ao final de uma string.
#O caractere * corresponde a zero ou mais ocorrências do caractere anterior.
#O caractere + corresponde a uma ou mais ocorrências do caractere anterior.
#O caractere ? corresponde a zero ou uma ocorrência do caractere anterior.
#O caractere {n} corresponde a exatamente n ocorrências do caractere anterior.
#O caractere {n,} corresponde a n ou mais ocorrências do caractere anterior.
#O caractere {n,m} corresponde a entre n e m ocorrências do caractere anterior.
#O caractere [ ] corresponde a qualquer caractere dentro dos colchetes.
#O caractere | corresponde a um ou outro padrão.
#O caractere ( ) agrupa padrões.
#O caractere \ escapa caracteres especiais.
#O caractere / é utilizado para escapar caracteres especiais.
#O caractere \d corresponde a qualquer dígito.
#O caractere \D corresponde a qualquer caractere que não seja um dígito.
#O caractere \w corresponde a qualquer caractere alfanumérico.
#O caractere \W corresponde a qualquer caractere que não seja alfanumérico.
#O caractere \s corresponde a qualquer caractere de espaço em branco.
#O caractere \S corresponde a qualquer caractere que não seja de espaço em branco.


import re #Importando o módulo re
texto = 'abc' #Definindo uma string
info = re.search('a.c', texto) #Procurando o padrão 'a.c' na string
if info != None: #Se o padrão for encontrado na string 
    print('Encontrado ocorrência em:', info.span()) #Imprime a posição do padrão na string
    print('O que foi encontrado:', info.group()) #Imprime o padrão encontrado
else:
    print('Não encontrado!')
    
print('-'*20)

#Exemplos de Expressões Regulares

import re #Importando o módulo re
texto = '-10 Cº' #Definindo uma string

info = re.search('^(-)?[0-9]+ Cº$', texto) #Procurando o padrão '(-)? [0-9]+ Cº' na string
if info != None: #Se o padrão for encontrado na string 
    print("Temperatura válida") #Imprime que a temperatura é válida
else:
    print("Temperatura inválida") #Imprime que a temperatura é inválida
    
print('-'*20)

import re #Importando o módulo re
texto = '99224466' #Definindo uma string

info = re.search('^99([0-9]{6})$', texto) # Procurando o padrão '^99([0-9]{6})$' na string
if info != None: #Se o padrão for encontrado na string 
    print("Número válido") #Imprime um número válido
else:
    print("Número inválido") #Imprime que o número é inválido
    
print('-'*20)

import re #Importando o módulo re
texto = "Texto teste" #Definindo uma string

info = re.search('(^[A-Za-z]+ +[A-Za-z]+ *$)', texto) #Procurando o padrão '^[A-Za-z]+ +[A-Za-z]+ *$' na string
if info != None: #Se o padrão for encontrado na string
    print('Encontrado ocorrência em:', info.span()) #Imprime a posição do padrão na string
    print('O que foi encontrado:', info.group()) #Imprime o padrão encontrado
else:
    print('Padrão não encontrado!')    

print('-'*20)

texto = '30/12/1998' #Definindo uma string

info = re.search("^([0-2][0-9]|[3][0-1])/([0][1-9]|[1][0-2])/([0-9]){4}$", texto) #Procurando o padrão '^([0-2][0-9]|[3][0-1])/([0][1-9]|[1][0-2])/([0-9]){4}$' na string
if info !=None:
    print('Data válida') #Imprime que a data é válida
else:
    print('Data inválida')
    
print('-'*20)

#Atividades

1
import re #Importando o módulo re
texto = '16' #Definindo uma string
info = re.search('^([2][0-9])|([3][0-5])$', texto) #Procurando o padrão '^[2][0-9]|([3][0-5])$' na string
if info != None: #Se o padrão for encontrado na string 
    print('Encontrada ocorrência em ', info.span()) #Imprime que o número é válido
    print('O que foi encontrado:', info.group()) #Imprime o padrão encontrado
else:
    print('Número inválido')
    
print('-'*20)

2
import re #Importando o módulo re
texto = "Python é uma linguagem de programação" #Definindo uma string
info = re.search('Python', texto) #Procurando o padrão 'Python' na string
if info != None: #Se o padrão for encontrado na string
    print('Encontrado ocorrência em:', info.span()) #Imprime a posição do padrão na string
    print('O que foi encontrado:', info.group()) #Imprime o padrão encontrado
else:
    print('Padrão não encontrado!')

print('-'*20)

3
import re #Importando o módulo re
texto = "Segunda-Feira" #Definindo uma string
info = re.search('^(Segunda-Feira|Terça-Feira|Quarta-Feira|Quinta-Feira|Sexta-Feira|Sábado|Domingo)$' ,texto) #Procurando o padrão '^(Segunda-Feira|Terça-Feira|Quarta-Feira|Quinta-Feira|Sexta-Feira|Sábado|Domingo)$' na string
if info != None: #Se o padrão for encontrado na string
    print('Encontrado ocorrência em:', info.span()) #Imprime a posição do padrão na string
    print('O que foi encontrado:', info.group()) #Imprime o padrão encontrado
else:
    print('Padrão não encontrado!')

print('-'*20)

4
import re #Importando o módulo re
texto = "99123456" #Definindo uma string
info = re.search('^[0-9]{8}$', texto) #Procurando o padrão '^[0-9]{8}$' na string
if info != None: #Se o padrão for encontrado na string
    print('Número válido') #Imprime que o número é válido
    info2 = re.search('^95([0-9]{6})$', texto) #Procurando o padrão '^95([0-9]{6})$' na string
    if info2 != None: #Se o padrão for encontrado na string
        print('Telefone bloqueado') #Número bloqueado
    else:
        print('Telefone não bloqueado') #Número não bloqueado
else:
    print('Número inválido')

print('-'*20)

5

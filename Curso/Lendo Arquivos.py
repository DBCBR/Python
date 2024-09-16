#Lendo Arquivos
#Para ler um arquivo, você deve usar a função open() que abre o arquivo e retorna um objeto de arquivo.
#O objeto de arquivo é usado para ler ou gravar arquivos.
#Sintaxe
#open(filename, mode)
#Parâmetros
#filename: Obrigatório. Especifica o nome do arquivo que você deseja abrir.
#mode: Opcional. Especifica o modo em que o arquivo deve ser aberto. O modo pode ser leitura, escrita ou anexação. O modo padrão é a leitura.
#Existem três modos principais que você pode usar para abrir um arquivo:
#"r" - Lê - Valor padrão. Abre um arquivo para leitura, erro se o arquivo não existir
#"a" - Anexa - Abre um arquivo para anexar, cria o arquivo se ele não existir
#"w" - Escreve - Abre um arquivo para escrita, cria o arquivo se ele não existir
#"x" - Cria - Cria o arquivo especificado, retorna um erro se o arquivo existir
#Além disso, você pode especificar se o arquivo deve ser tratado como texto ou binário
#"t" - Texto - Valor padrão. Modo de texto
#"b" - Binário - Modo binário (por exemplo, imagens)

# arquivo = open("teste.txt", "wt") #wt = write text
# arquivo.write("Olá, estou escrevendo no arquivo!\n") #\n = quebra de linha
# arquivo.write("Agora estou escrevendo outra linha!\n") #\n = quebra de linha
# arquivo.close() #fechar o arquivo

# lista = ["Ana,", "Fernando", "João", "Maria"] #criar uma lista
# arquivo = open("nomes.txt", "wt") #wt = write text
# for i in lista: #para cada i na lista
#     arquivo.write(i + "\n") #escrever i e quebrar a linha
# arquivo.close() #fechar o arquivo

# texto = "David\nPaula\nYasmin\nAurora" #criar uma string
# arquivo = open("nomes2.txt", "wt") #wt = write text
# arquivo.writelines(texto) #escrever a string
# arquivo.close() #fechar o arquivo

# lista = [str(i) + "\n" for i in range(0, 20)] #criar uma lista com números de 0 a 19
# arquivo = open("números.txt", "wt") #wt = write text
# arquivo.writelines(lista) #escrever a lista
# arquivo.close() #fechar o arquivo

# with open("teste_with.txt", "wt") as arquivo: #abrir o arquivo com o nome teste_with.txt e o modo wt = write text
#     arquivo.write("Olá, estou escrevendo no arquivo!\n") #escrever no arquivo
#     arquivo.write("Agora estou escrevendo outra linha!\n") #escrever no arquivo
    
# arquivo = open("teste.txt", "rt") #rt = read text
# primeira_linha = arquivo.readline() #ler a primeira linha
# segunda_linha = arquivo.readline() #ler a segunda linha
# print(primeira_linha) #imprimir a primeira linha
# print(segunda_linha) #imprimir a segunda linha
# arquivo.close() #fechar o arquivo

# arquivo = open("teste.txt", "rt") #rt = read text
# lido = arquivo.read() #ler o arquivo
# print(lido) #imprimir o arquivo
# arquivo.close() #fechar o arquivo

# arquivo = open("teste.txt", "rt") #rt = read text 
# for linha in arquivo: #para cada linha no arquivo
#     print(linha) #imprimir a linha
# arquivo.close() #fechar o arquivo

# with open("teste_with.txt", "rt") as arquivo: #abrir o arquivo com o nome teste_with.txt e o modo rt = read text
#     for linha in arquivo: #para cada linha no arquivo
#         print(linha) #imprimir a linha

#Verificando e tratando erros
#Você deve sempre fechar o arquivo quando terminar de trabalhar com ele.
#Para garantir que um arquivo seja fechado, você pode usar a instrução try...finally.
#A instrução try...finally garante que sempre feche o arquivo, mesmo que ocorra uma exceção.

# from os import path #importar a função path do módulo os
# arquivo_existe = path.exists("teste.txt") #verificar se o arquivo teste.txt existe
# if arquivo_existe: #se o arquivo existe
#     print("O arquivo existe!") #imprimir que o arquivo existe
# else:
#     print("O arquivo não existe!")
# print('-'*20)
    
# import os #importar o módulo os
# os.remove("teste.txt") #remover o arquivo teste.txt

# os.remove("nomes.txt") #remover o arquivo nomes.txt
# os.remove("nomes2.txt") #remover o arquivo nomes2.txt
# os.remove("números.txt") #remover o arquivo números.txt
# os.remove("teste_with.txt") #remover o arquivo teste_with.txt

# file = open('teste', 'w')
# try:
#     file.write('Olá, estou escrevendo no arquivo!\n')
# finally:
#     file.close()

# import os #importar o módulo os
# try:
#     os.remove("eerree.txt") #remover o arquivo eerree.txt
# except Exception as erro: #se ocorrer um erro
#     print("Ocorreu um erro:", str(erro)) #imprimir que ocorreu um erro
    
# import os #importar o módulo os
# os.mkdir("pasta") #criar uma pasta chamada pasta

# import os #importar o módulo os
# os.rmdir("pasta") #remover a pasta pasta com o nome pasta, a pasta deve estar vazia.

# # import os #importar o módulo os
# # os.mkdir("C:/Users/dbcbr/Documents/GitHub/Python/Curso/pasta") #criar uma pasta chamada pasta

# # import os #importar o módulo os
# # os.mkdir("C:/Users/dbcbr/Documents/GitHub/Python/Curso/pasta/pasta") #criar uma pasta chamada pasta


# import os #importar o módulo os
# os.rmdir("C:/Users/dbcbr/Documents/GitHub/Python/Curso/pasta") #criar uma pasta chamada pasta

# import os #importar o módulo os
# for i in range(10): #para cada i no intervalo de 0 a 9
#     nome_pasta = 'pasta' + str(i) #nome da pasta
#     try:
#        os.mkdir(nome_pasta) #criar a pasta
#     except:
#          pass
    
#     try:
#         open(nome_pasta + '/arquivo.txt', 'wt').close() #criar o arquivo na pasta e fechar
#     except:
#          pass
    
# import os #importar o módulo os
# for i in range(0,10): #para cada i no intervalo de 0 a 9
#     nome_pasta = 'pasta' + str(i) #nome da pasta
#     try:
#         os.remove(nome_pasta + '/arquivo.txt') #remover o arquivo na pasta
#     except:
#         pass
    
#     try:
#         os.rmdir(nome_pasta) #remover a pasta
#     except:
#         print('A pasta não existe!')

# import shutil #importar o módulo shutil
# for i in range(0,10):
#     nome_pasta = 'pasta' + str(i)
#     try:
#         shutil.rmtree(nome_pasta) #remover a pasta
#     except:
#         print('A pasta não existe!') #imprimir que a pasta não existe

# import os #importar o módulo os
# files = os.listdir() #listar os arquivos
# print(files) #imprimir os arquivos

#Arquivos CSV
#Um arquivo CSV (Comma Separated Values) é um arquivo que armazena dados em formato de tabela.
#Cada linha do arquivo é uma linha da tabela e as colunas são separadas por vírgulas.
#Leitura de arquivos CSV
#Para ler um arquivo CSV, você deve usar o módulo CSV.
#O módulo CSV fornece funções para trabalhar com arquivos CSV.

# import csv #importar o módulo csv
# with open('pessoas.csv', 'w') as arquivo: #abrir o arquivo pessoas.csv no modo w = write
#     escritorCsv = csv.writer(arquivo,delimiter=',') #escrever no arquivo com delimitador ,
#     escritorCsv.writerow(['id', 'nome', 'profissão']) #escrever a linha com id, nome e profissão
#     escritorCsv.writerow(['1', 'David', 'Programador']) #escrever a linha com 1, David e Programador
#     escritorCsv.writerow(['2', 'Paula', 'Enfermeira']) #escrever a linha com 2, Paula e Enfermeira
#     escritorCsv.writerow(['3', 'Yasmin', 'Estudante']) #escrever a linha com 3, Yasmin e Estudante
#     escritorCsv.writerow(['4', 'Aurora', 'Estudante']) #escrever a linha com 4, Aurora e Estudante

# # import csv #importar o módulo csv
# # linhas = [['id', 'nome', 'profissão'],['1', 'David', 'Programador'],['2', 'Paula', 'Enfermeira'],['3', 'Yasmin', 'Estudante'],['4', 'Aurora', 'Estudante']] #criar uma lista com as linhas
# # with open('pessoas2.csv', 'w') as file: #abrir o arquivo pessoas2.csv no modo w = write
# #     escritorCsv = csv.writer(file) #escrever no arquivo
# #     escritorCsv.writerows(linhas) #escrever as linhas no arquivo

# import csv #importar o módulo csv
# with open('pessoas.csv', 'r') as arquivo: #abrir o arquivo pessoas.csv no modo r = read
#     leitorCsv = csv.reader(arquivo, delimiter=',') #ler o arquivo com delimitador ,
#     for linha in leitorCsv: #para cada linha no arquivo
#         print(linha) #imprimir a linha
        
#Criando Classe para manipular arquivos CSV

# import csv #importar o módulo csv
# class Pessoa: #criar a classe Pessoa
#     def __init__(self, id, nome , profissão): #método construtor 
#         self.id = id #atributo id
#         self.nome = nome #atributo nome
#         self.profissão = profissão #atributo profissão
        
#     @staticmethod #método estático 
#     def le_pessoas(): #método le_pessoas
#         pessoas = [] #lista pessoas
#         with open('pessoas.csv', 'r') as arquivo: #abrir o arquivo pessoas.csv no modo r = read
#             leitor = csv.reader(arquivo, delimiter=',') #ler o arquivo com delimitador ,
#             for linha in leitor: #para cada linha no arquivo
#                 pessoa = Pessoa(linha[0], linha[1], linha[2]) #criar um objeto pessoa
#                 pessoas.append(pessoa) #adicionar a pessoa na lista pessoas
#         return pessoas

#     @staticmethod #método estático
#     def salva_pessoas(*pessoas): #método salva_pessoas
#         with open('pessoas.csv', 'w') as arquivo: #abrir o arquivo pessoas.csv no modo w = escritor
#             escritorCsv = csv.writer(arquivo, delimiter=',') #escrever no arquivo com delimitador ,
#             for pessoa in pessoas:
#                 escritorCsv.writerow([pessoa.id, pessoa.nome, pessoa.profissão])
                
# pessoa1 = Pessoa('1', 'David', 'Programador') #criar um objeto pessoa1
# pessoa2 = Pessoa('2', 'Paula', 'Enfermeira') #criar um objeto pessoa2
# pessoa3 = Pessoa('3', 'Yasmin', 'Estudante') #criar um objeto pessoa3
# pessoa4 = Pessoa('4', 'Aurora', 'Estudante') #criar um objeto pessoa4

# Pessoa.salva_pessoas(pessoa1, pessoa2, pessoa3, pessoa4) #salvar as pessoas

# lista_pessoa = Pessoa.le_pessoas() #ler as pessoas

# for pessoa in lista_pessoa: #para cada pessoa na lista_pessoas
#     print(pessoa.id, pessoa.nome, pessoa.profissão) #imprimir o id, nome e profissão da pessoa

#Formato JSON
#JSON (JavaScript Object Notation) é um formato de dados que é fácil de ler e escrever.
#JSON é usado para enviar dados entre um navegador e um servidor.
#JSON é uma string que contém dados.
#Leitura de arquivos JSON
#Para ler um arquivo JSON, você deve usar o módulo JSON.
#O módulo JSON fornece funções para trabalhar com arquivos JSON.

import json #importar o módulo json
idades ={
    'David': 37,
    'Paula': 35,
    'Yasmin': 10,
    'Aurora': 5
} #dicionário idades

print(json.dumps(idades, ensure_ascii=False)) #converter o dicionário em JSON

DadosPessoas = {
    'David': {
        'CPF': '123.456.789-00',
        'Sexo': 'Masculino',
        'Idade': 37,
        'Profissão': 'Programador',
        'Filhos': ['Yasmin', 'Aurora']
    },
    'Paula': {
        'CPF': '987.654.321-00',
        'Sexo': 'Feminino',
        'Idade': 35,
        'Profissão': 'Enfermeira',
        'Filhos': ['Yasmin', 'Aurora']
    },

}

texto = json.dumps(DadosPessoas, ensure_ascii=False, indent=4) #converter o dicionário em JSON
print(texto) #imprimir o JSON

with open('exemplo.json', 'wt') as arquivo: #abrir o arquivo exemplo.json no modo wt = write text
    arquivo.write(texto) #escrever o texto no arquivo
    
dicionário = None #dicionário vazio
with open('exemplo.json', 'rt') as arquivo: #abrir o arquivo exemplo.json no modo rt = read text
    arquivo_lido = arquivo.read() #ler o arquivo
    dicionário = json.loads(arquivo_lido) #carregar o arquivo no dicionário

print(dicionário) #imprimir o dicionário
print(type(dicionário)) #imprimir o tipo do dicionário
print(dicionário['David']) #imprimir o dicionário David
print(dicionário['Paula']) #imprimir o dicionário Paula
print('-'*20)

#Criando Classe no Json

import json #importar o módulo json

class Carro: #criar a classe Carro
    def __init__(self, nome, potencia): #método construtor
        self.nome = nome #atributo nome
        self.potencia = potencia #atributo potencia
    
    @staticmethod #método estático
    def salva_carros(*carros): #método salva_carros
        dicionário = dict() #dicionário vazio
        for carro in carros: #para cada carro na lista carros
            dicionário[carro.nome] = carro.potencia #adicionar o carro no dicionário
        texto = json.dumps(dicionário, ensure_ascii=False, indent=4) #converter o dicionário em JSON
        with open('carros.json', 'wt') as arquivo: #abrir o arquivo carros.json no modo wt = write text
            arquivo.write(texto) #escrever o texto no arquivo
    
    @staticmethod #método estático
    def le_carros():
        lista = []
        texto = None
        with open('carros.json', 'rt') as arquivo:
            texto = arquivo.read()
        dicionário = json.loads(texto)
        for chave in dicionário:
            carro = Carro(chave, dicionário[chave])
            lista.append(carro)
        return lista
    
carro1 = Carro('Fusca', 50) #criar um objeto carro1
carro2 = Carro('Gol', 100) #criar um objeto carro2
carro3 = Carro('Civic', 150) #criar um objeto carro3
carro4 = Carro('Corolla', 200) #criar um objeto carro4

Carro.salva_carros(carro1, carro2, carro3, carro4) #salvar os carros
lista_carros = Carro.le_carros() #ler os carros

for carro in lista_carros: #para cada carro na lista_carros
    print(carro.nome, carro.potencia) #imprimir o nome e a potência do carro

print('-'*20)

#Formato XML
#XML (Extensible Markup Language) é uma linguagem de marcação que define regras para codificar documentos em um formato que é legível tanto para humanos quanto para máquinas.
#XML é uma linguagem de marcação semelhante ao HTML.
#Leitura de arquivos XML
#Para ler um arquivo XML, você deve usar o módulo XML.
#O módulo XML fornece funções para trabalhar com arquivos XML.

import xml.etree.ElementTree as xml  # importar o módulo xml.etree.ElementTree
import os  # importar o módulo os

# Criar o nó raiz
no_raiz = xml.Element('DadosPessoais')

# Criar o nó pessoa com o atributo nome David
no_pessoa = xml.Element('Pessoa', attrib={'nome': 'David'})

# Criar o nó CPF no nó pessoa e atribuir o texto 123.456.789-00
no_cpf = xml.SubElement(no_pessoa, 'CPF')
no_cpf.text = '123.456.789-00'

# Criar o nó sexo no nó pessoa e atribuir o texto Masculino
no_sexo = xml.SubElement(no_pessoa, 'Sexo')
no_sexo.text = 'Masculino'

# Criar o nó idade no nó pessoa e atribuir o texto 37
no_idade = xml.SubElement(no_pessoa, 'Idade')
no_idade.text = '37'

# Criar o nó profissão no nó pessoa e atribuir o texto Programador
no_profissao = xml.SubElement(no_pessoa, 'Profissao')
no_profissao.text = 'Programador'

# Criar o nó filhos no nó pessoa
no_filhos = xml.SubElement(no_pessoa, 'Filhos')

# Criar o nó filho1 no nó filhos e atribuir o texto Yasmin
no_filho1 = xml.SubElement(no_filhos, 'Filho')
no_filho1.text = 'Yasmin'

# Criar o nó filho2 no nó filhos e atribuir o texto Aurora
no_filho2 = xml.SubElement(no_filhos, 'Filho')
no_filho2.text = 'Aurora'

# Adicionar o nó pessoa no nó raiz
no_raiz.append(no_pessoa)

# Criar a árvore com o nó raiz
arvore = xml.ElementTree(no_raiz)

# Escrever a árvore no arquivo
with open('dados_exemplo.xml', 'wb') as files:
    arvore.write(files)
    
print('-'*20)

#XML com Funções

import xml.etree.ElementTree as xml  # importar o módulo xml.etree.ElementTree
import os  # importar o módulo os


def criaTagPessoa(nome, cpf, sexo, idade, profissao, filhos):  # função criaTagPessoa
    # Criar o nó pessoa com o atributo nome
    no_pessoa = xml.Element('Pessoa', attrib={'Nome': nome})

    # Criar o nó CPF no nó pessoa e atribuir o texto
    no_cpf = xml.SubElement(no_pessoa, 'CPF')
    no_cpf.text = cpf

    # Criar o nó sexo no nó pessoa e atribuir o texto
    no_sexo = xml.SubElement(no_pessoa, 'Sexo')
    no_sexo.text = sexo

    # Criar o nó idade no nó pessoa e atribuir o texto
    no_idade = xml.SubElement(no_pessoa, 'Idade')
    no_idade.text = idade

    # Criar o nó profissão no nó pessoa e atribuir o texto
    no_profissao = xml.SubElement(no_pessoa, 'Profissao')
    no_profissao.text = profissao

    # Criar o nó filhos no nó pessoa
    no_filhos = xml.SubElement(no_pessoa, 'Filhos')

    # Adicionar os filhos no nó filhos
    for filho in filhos:
        no_filho = xml.SubElement(no_filhos, 'Filho')
        no_filho.text = filho

    return no_pessoa  # retornar o nó pessoa

# Criar o nó raiz
raiz = xml.Element('DadosPessoais')

# Criar as pessoas
pessoa1 = criaTagPessoa('David', '123.456.789-00', 'Masculino', '37', 'Programador', ['Yasmin', 'Aurora'])
pessoa2 = criaTagPessoa('Paula', '987.654.321-00', 'Feminino', '35', 'Enfermeira', ['Yasmin', 'Aurora'])
pessoa3 = criaTagPessoa('Yasmin', '111.222.333-44', 'Feminino', '10', 'Estudante', [])
pessoa4 = criaTagPessoa('Aurora', '555.666.777-88', 'Feminino', '5', 'Estudante', [])

# Adicionar as pessoas no nó raiz
raiz.append(pessoa1)
raiz.append(pessoa2)
raiz.append(pessoa3)
raiz.append(pessoa4)

# Criar a árvore com o nó raiz
arvore = xml.ElementTree(raiz)

# Escrever a árvore no arquivo
with open('dados_exemplo2.xml', 'wb') as files:
    arvore.write(files)
    
print('-'*20)

#XML a partir de um Dicionário

import xml.etree.ElementTree as xml  # importar o módulo xml.etree.ElementTree
import os  # importar o módulo os

def criaTagPessoa(nome, cpf, sexo, endereço): # função criaTagPessoa
    no_pessoa = xml.Element('Pessoa', attrib={'Nome': nome}) #criar o nó pessoa com o atributo nome 
    no_cpf = xml.SubElement(no_pessoa, 'CPF') #criar o nó CPF no nó pessoa
    no_cpf.text = cpf #atribuir o texto cpf ao nó cpf
     
    no_sexo = xml.SubElement(no_pessoa, 'Sexo') #criar o nó Sexo no nó pessoa
    no_sexo.text = sexo #atribuir o texto sexo ao nó sexo
    
    no_endereço = xml.SubElement(no_pessoa, 'Endereco') #criar o nó Endereço no nó pessoa
    no_endereço.text = endereço #atribuir o texto endereço ao nó endereço 
    
    return no_pessoa #retornar o nó pessoa

dados = { #dicionário dados
    'David': {
        'CPF': '123.456.789-00',
        'Sexo': 'Masculino',
        'Endereco': 'Rua das Flores, 123'
    },
    'Paula': {
        'CPF': '987.654.321-00',
        'Sexo': 'Feminino',
        'Endereco': 'Rua das Rosas, 456'
    },
    'Yasmin': {
        'CPF': '111.222.333-44',
        'Sexo': 'Feminino',
        'Endereco': 'Rua das Margaridas, 789'
    },
    'Aurora': {
        'CPF': '555.666.777-88',
        'Sexo': 'Feminino',
        'Endereco': 'Rua das Violetas, 1011'
    }

}

raiz = xml.Element('DadosPessoais') #criar o nó raiz

for chave in dados: #para cada chave no dicionário dados
    nome = chave #atribuir a chave a variável nome
    dados_pessoa = dados[nome] #atribuir os dados da pessoa a variável dados_pessoa
    cpf = dados_pessoa['CPF'] #atribuir o CPF a variável cpf
    sexo = dados_pessoa['Sexo'] #atribuir o sexo a variável sexo
    endereco = dados_pessoa['Endereco'] #atribuir o endereço a variável endereço
    
    pessoa = criaTagPessoa(nome, cpf, sexo, endereco) #criar a pessoa
    raiz.append(pessoa) #adicionar a pessoa no nó raiz

arvore = xml.ElementTree(raiz) #criar a árvore com o nó raiz
with open('dados_pessoais3.xml', 'wb') as files: #abrir o arquivo dados_pessoais3.xml no modo wb = write binary
    arvore.write(files) #escrever a árvore no arquivo

print('-'*20)

#Lendo XML

import xml.etree.ElementTree as xml  # importar o módulo xml.etree.ElementTree
tree = xml.parse('dados_pessoais3.xml') #parsear o arquivo dados_pessoais3.xml
root = tree.getroot() #obter a raiz
print(root.tag) #imprimir a tag da raiz
for pessoa in root: #para cada pessoa na raiz
    print(' ', pessoa.tag, pessoa.attrib['Nome']) #imprimir a tag e os atributos da pessoa
    for dado in pessoa:
        if (dado.tag == 'Filhos'):
            for filho in dado:
                print('   ', filho.tag, filho.text)
    print(' ', dado.tag, dado.text) #imprimir a tag e o texto do dado
    
print('-'*20)

#Criando Classe no XML

import xml.etree.ElementTree as xml  # importar o módulo xml.etree.ElementTree
import os  # importar o módulo os

class Carro:
    def __init__(self, nome, potencia):
        self.nome = nome
        self.potencia = potencia
    
    @staticmethod
    def salva_carros(*carros):
        raiz = xml.Element('Raiz')
        for carro in carros:
            no_carro = xml.Element('Carro')
            no_nome = xml.SubElement(no_carro, 'Nome')
            no_nome.text = carro.nome
            
            no_potencia = xml.SubElement(no_carro, 'Potencia')
            no_potencia.text = str(carro.potencia)
            
            raiz.append(no_carro)
        arvore = xml.ElementTree(raiz)
        with open('carros_exemplo.xml', 'wb') as files:
            arvore.write(files)

    @staticmethod
    def le_carros():
        lista = []
        tree = xml.parse('carros_exemplo.xml')
        root = tree.getroot()
        for carro in root:
            nome = None
            potencia = None
            
            for dado in carro:
                if dado.tag == 'Nome':
                    nome = dado.text
                if dado.tag == 'Potencia':
                    potencia = dado.text
            carro = Carro(nome, potencia)
            lista.append(carro)
        return lista
    
carro1 = Carro('Fusca', 50)
carro2 = Carro('Gol', 100)
carro3 = Carro('Civic', 150)
carro4 = Carro('Corolla', 200)

Carro.salva_carros(carro1, carro2, carro3, carro4)
lista_carros = Carro.le_carros()

for carro in lista_carros:
    print(carro.nome, carro.potencia)

print('-'*20)

#YAML
#YAML (YAML Ain't Markup Language) é um formato de serialização de dados legível por humanos.
#É comumente usado para configurar arquivos e dados de intercâmbio.
#Leitura de arquivos YAML
#Para ler um arquivo YAML, você deve usar o módulo YAML.
#O módulo YAML fornece funções para trabalhar com arquivos YAML.

import yaml  # importar o módulo yaml

try:
    with open('config.yaml', 'r') as f:  # abrir o arquivo config.yaml em modo de leitura
        data = yaml.load(f, Loader=yaml.FullLoader)  # carregar o arquivo yaml
        print(data)  # imprimir o conteúdo do arquivo yaml
except FileNotFoundError:
    print("Arquivo 'config.yaml' não encontrado.")
except yaml.YAMLError as e:
    print(f"Erro ao processar o arquivo YAML: {e}")
except Exception as e:
    print(f"Ocorreu um erro: {e}")
    
print('-'*20)

#Atividade

1
# list = []
# with open('exercicio1.txt', 'rt') as arquivo:
#     for line in arquivo:
#         list.append(line)
# print(list)

2
class Produto:
    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor
        
produtos = []

with open('exercicio2.txt', 'rt') as arquivo:
    for linha in arquivo:
        indice_separa = linha.index('R$')
        
        nome = linha[:indice_separa -1]
        valor = linha[indice_separa:len(linha)-1]
        produto = Produto(nome, valor)
        produtos.append(produto)

for produto in produtos:
    print(produto.nome, produto.valor)
    
print('-'*20)

3
with open('exercicio3.txt', 'wt') as arquivo:
    for i in range(0,101):
        arquivo.write(str(i) + '\n')
    
print('-'*20)

4
with open('exercicio4.txt', 'wt') as arquivo:
    for i in range(0,101):
        if i % 3 == 0:
            arquivo.write(str(i) + '\n')
    
print('-'*20)

5
import csv

def escreve_arquivo():
    with open('exercicio5.csv', 'w') as arquivo:
        escritorCSV = csv.writer(arquivo, delimiter=',')
        escritorCSV.writerow(['Nome', 'Parentesco'])
        escritorCSV.writerow(['David', 'Pai'])
        escritorCSV.writerow(['Paula', 'Mãe'])
        escritorCSV.writerow(['Yasmin', 'Filha'])
        escritorCSV.writerow(['Aurora', 'Filha'])

def le_arquivo():
    with open('exercicio5.csv', 'r') as arquivo:
        leitor = csv.reader(arquivo, delimiter=',')
        for linha in leitor:
            print(linha)

escreve_arquivo()
le_arquivo()

print('-'*20)

6
class Empresa:
    def __init__(self, id, nome, numero_funcionarios, lucro):
        self.id = id
        self.nome = nome
        self.numero_funcionarios = numero_funcionarios
        self.lucro = lucro
    
empresas = []

with open('exercicio6.csv', 'r') as arquivo:
    leitor = csv.reader(arquivo, delimiter=',')
    for linha in leitor:
        emp = Empresa(linha[0], linha[1], linha[2], linha[3])
        empresas.append(emp)
        
for emp in empresas:
    print(emp.id, emp.nome, emp.numero_funcionarios, emp.lucro)
    
print('-'*20)

7
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    @staticmethod
    def trasforma_dict(*args):
        dicionario = dict()
        for pessoa in args:
            dicionario[pessoa.nome] = pessoa.idade
        return dicionario
            
pessoa1 = Pessoa('David', 37)
pessoa2 = Pessoa('Paula', 35)
pessoa3 = Pessoa('Yasmin', 10)
pessoa4 = Pessoa('Aurora', 5)

dicionario_pessoas = Pessoa.trasforma_dict(pessoa1, pessoa2, pessoa3, pessoa4)
texto = json.dumps(dicionario_pessoas, indent=4)
print(texto)
with open('exercicio7.json', 'wt') as arquivo:
    arquivo.write(texto)
    
print('-'*20)

8
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    @staticmethod
    def trasforma_pessoa():
        pessoas = []
        with open('exercicio7.json', 'rt') as arquivo:
            arquivo_lido = arquivo.read()
            dicionario = json.loads(arquivo_lido)
            for key in dicionario:
                pessoa = Pessoa(key, dicionario[key])
                pessoas.append(pessoa)
        return pessoas

pessoas = Pessoa.trasforma_pessoa()
for pessoa in pessoas:
    print(pessoa.nome, pessoa.idade)
    
print('-'*20)

9
import xml.etree.ElementTree as xml
import os

def cria_estado(nome, cidades):
    element_estado = xml.Element('Estado', attrib={'Nome': nome})
    for cidade in cidades:
        elemento_cidade = xml.SubElement(element_estado,'Cidade')
        elemento_cidade.text = cidade
        element_estado.append(elemento_cidade)
    return element_estado

raiz = xml.Element('Root')
no_estado = cria_estado('Rio de Janeiro', ['Rio de Janeiro', 'Niterói', 'Cabo Frio'])
no_estado2 = cria_estado('São Paulo', ['São Paulo', 'Campinas', 'Santos'])
raiz.append(no_estado)
raiz.append(no_estado2)

arvore = xml.ElementTree(raiz)

with open('exercicio9.xml', 'wb') as files:
    arvore.write(files)

print('-'*20)


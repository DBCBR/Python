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

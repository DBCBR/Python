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

arquivo = open("teste.txt", "wt") #wt = write text
arquivo.write("Olá, estou escrevendo no arquivo!\n") #\n = quebra de linha
arquivo.write("Agora estou escrevendo outra linha!\n") #\n = quebra de linha
arquivo.close() #fechar o arquivo

lista = ["Ana,", "Fernando", "João", "Maria"] #criar uma lista
arquivo = open("nomes.txt", "wt") #wt = write text
for i in lista: #para cada i na lista
    arquivo.write(i + "\n") #escrever i e quebrar a linha
arquivo.close() #fechar o arquivo

texto = "David\nPaula\nYasmin\nAurora" #criar uma string
arquivo = open("nomes2.txt", "wt") #wt = write text
arquivo.writelines(texto) #escrever a string
arquivo.close() #fechar o arquivo

lista = [str(i) + "\n" for i in range(0, 20)] #criar uma lista com números de 0 a 19
arquivo = open("números.txt", "wt") #wt = write text
arquivo.writelines(lista) #escrever a lista
arquivo.close() #fechar o arquivo

with open("teste_with.txt", "wt") as arquivo: #abrir o arquivo com o nome teste_with.txt e o modo wt = write text
    arquivo.write("Olá, estou escrevendo no arquivo!\n") #escrever no arquivo
    arquivo.write("Agora estou escrevendo outra linha!\n") #escrever no arquivo
    
arquivo = open("teste.txt", "rt") #rt = read text
primeira_linha = arquivo.readline() #ler a primeira linha
segunda_linha = arquivo.readline() #ler a segunda linha
print(primeira_linha) #imprimir a primeira linha
print(segunda_linha) #imprimir a segunda linha
arquivo.close() #fechar o arquivo

arquivo = open("teste.txt", "rt") #rt = read text
lido = arquivo.read() #ler o arquivo
print(lido) #imprimir o arquivo
arquivo.close() #fechar o arquivo

arquivo = open("teste.txt", "rt") #rt = read text 
for linha in arquivo: #para cada linha no arquivo
    print(linha) #imprimir a linha
arquivo.close() #fechar o arquivo

with open("teste_with.txt", "rt") as arquivo: #abrir o arquivo com o nome teste_with.txt e o modo rt = read text
    for linha in arquivo: #para cada linha no arquivo
        print(linha) #imprimir a linha

#Verificando e tratando erros
#Você deve sempre fechar o arquivo quando terminar de trabalhar com ele.
#Para garantir que um arquivo seja fechado, você pode usar a instrução try...finally.
#A instrução try...finally garante que sempre feche o arquivo, mesmo que ocorra uma exceção.

from os import path #importar a função path do módulo os
arquivo_existe = path.exists("teste.txt") #verificar se o arquivo teste.txt existe
if arquivo_existe: #se o arquivo existe
    print("O arquivo existe!") #imprimir que o arquivo existe
else:
    print("O arquivo não existe!")
    
import os #importar o módulo os
os.remove("teste.txt") #remover o arquivo teste.txt

os.remove("nomes.txt") #remover o arquivo nomes.txt
os.remove("nomes2.txt") #remover o arquivo nomes2.txt
os.remove("números.txt") #remover o arquivo números.txt
os.remove("teste_with.txt") #remover o arquivo teste_with.txt

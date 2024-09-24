def primeiroultimo(nome):
    primeiro = nome.split()[0] #Separa a string em uma lista de palavras e pega a primeira
    ultimo = nome.split()[-1] #Separa a string em uma lista de palavras e pega a última
    return primeiro + ' ' + ultimo
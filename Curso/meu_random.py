from random import randrange

def get_random_lista(inicial, final, tam): # Função que gera uma lista de números aleatórios
    lista = [] # Cria uma lista vazia
    for i in range(tam): # Loop de 0 até tam
       numero = randrange(inicial, final) # Gera um número aleatório entre inicial e final
       lista.append(numero) # Adiciona o número gerado na lista
    return lista
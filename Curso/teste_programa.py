import sys

if(__name__ == '__main__'):
    if len(sys.argv) != 3: 
        print('Número de argumentos inválido!')
        sys.exit(1)
    numero1 = float(sys.argv[1])
    numero2 = float(sys.argv[2])
    print('A soma dos números é:', numero1 + numero2)
#Orientação a Objetos
# Classes são modelos que definem os atributos e métodos de um objeto.
# Objetos são instâncias de uma classe.
# Atributos são variáveis que guardam informações sobre o objeto.
# Métodos são funções que definem o comportamento do objeto.

class Pessoa: # Classe
    def __init__(self, nome, idade): # Método construtor
        self.nome = nome # Atributo
        self.idade = idade # Atributo
    def print_nome(self): # Método
        print("Meu nome é %s " % self.nome)

pessoa1 = Pessoa("João", 20) # Objeto
pessoa2 = Pessoa("Maria", 30) # Objeto
pessoa1.print_nome() # Meu nome é João
pessoa2.print_nome() # Meu nome é Maria
print('-'*20)

class Pessoa: # Classe
    def __init__(self, nome, idade): # Método construtor
        self.nome = nome # Atributo
        self.idade = idade # Atributo
        
    def print_string(self, nome): # Método com parâmetro nome
        print("Meu nome é %s " % nome) # Imprimindo o nome
        
    def print_nome(self): # Método sem parâmetro 
        self.print_string(self.nome) # Chamando o método print_string

pessoa1 = Pessoa("João", 20) # Objeto
pessoa2 = Pessoa("Maria", 30) # Objeto
pessoa1.print_nome() # Meu nome é João
pessoa2.print_nome() # Meu nome é Maria
print('-'*20)

class Pessoa: # Classe
    def __init__(self, nome): # Método construtor
        self.nome = nome # Atributo nome
    def insere_idade(self, idade): # Método com parâmetro idade
        self.idade = idade # Atributo idade

pessoa1 = Pessoa("João") # Objeto
pessoa1.insere_idade(20) # Chamando o método insere_idade
print(pessoa1.idade) # 20
print('-'*20)

class Tipo1:
    def __init__(self, outra_classe): # Método construtor
        self.outra = outra_classe # Atributo
class Tipo2:
    def __init__(self): # Método construtor
        self.número = 10 # Atributo

classe2 = Tipo2() # Objeto
classe1 = Tipo1(classe2) # Objeto
print(classe1.outra.número) # 10
print('-'*20)

class Exemplo:
    def __init__(self):
        pass

lista = []
ex1 = Exemplo()
ex2 = Exemplo()
lista.append(ex1)
lista.append(ex2)
print(lista[1])
print('-'*20)

class FormaGeométrica: # Classe
    def __init__(self, altura, largura): # Método construtor
        self.altura = altura # Atributo
        self.largura = largura # Atributo
        
class Quadrado(FormaGeométrica):
    lado = 10

class Triângulo(FormaGeométrica):
    angulo = 30

class Retângulo(FormaGeométrica):
    lado_menor = 5

quadrado = Quadrado(10, 10) # Objeto
triângulo = Triângulo(15, 10) # Objeto
retângulo = Retângulo(5, 15) # Objeto

print(quadrado.altura) # 10 
print(quadrado.largura) # 10
print(quadrado.lado) # 10

print(triângulo.altura) # 15
print(triângulo.largura) # 10
print(triângulo.angulo) # 30

print(retângulo.altura) # 5 
print(retângulo.largura) # 15
print(retângulo.lado_menor) # 5
print('-'*20)

class FormaGeométrica: # Classe
    def __init__(self, altura, largura): # Método construtor
        self.altura = altura # Atributo
        self.largura = largura # Atributo
    def função_herdade(self): # Método
        print("Função herdada")
class Quadrado(FormaGeométrica):
    pass

class Triângulo(FormaGeométrica):
    pass

class Retângulo(FormaGeométrica):
    pass

quadrado = Quadrado(10, 10) # Objeto
triângulo = Triângulo(15, 10) # Objeto
retângulo = Retângulo(5, 15) # Objeto

quadrado.função_herdade() # Função herdada
triângulo.função_herdade() # Função herdada
retângulo.função_herdade() # Função herdada
print('-'*20)

#Override (sobrescrita de métodos)

class ClassePai: # Classe
    def __init__(self): # Método construtor
        print("Função da classe pai")
        
class ClasseFilha(ClassePai): # Classe filha
    def __init__(self): # Método construtor
        print("Função da classe filha")
        
class ClasseFilha2(ClassePai): # Classe filha
    def __init__(self): # Método construtor
        print("Função da classe filha 2")
        
pai = ClassePai() # Função da classe pai
filha1 = ClasseFilha() # Função da classe filha
filha2 = ClasseFilha2() # Função da classe filha 2
print('-'*20)

class FormaGeométrica: # Classe
    def __init__(self, altura, largura): # Método construtor
        self.altura = altura # Atributo
        self.largura = largura # Atributo

class Quadrado(FormaGeométrica):
    def __init__(self, altura, largura, atributo_quadrado): # Método construtor
        FormaGeométrica.__init__(self, altura, largura) # Chamando o método construtor da classe pai
        self.atributo_quadrado = atributo_quadrado # Atributo
        
class Triangulo(FormaGeométrica):
    def __init__(self, altura, largura, atributo_triangulo): # Método construtor
        FormaGeométrica.__init__(self, altura, largura) # Chamando o método construtor da classe pai
        self.atributo_triangulo = atributo_triangulo # type: ignore # Atributo
        
class Retângulo(FormaGeométrica):
    def __init__(self, altura, largura, atributo_retângulo): # Método construtor
        FormaGeométrica.__init__(self, altura, largura) # Chamando o método construtor da classe pai
        self.atributo_retângulo = atributo_retângulo # type: ignore # Atributo
quadrado = Quadrado(10, 10, 'quadrado') # Objeto
triangulo = Triangulo(15, 10, 'triangulo') # Objeto
retângulo = Retângulo(5, 15, 'retângulo') # Objeto

print(quadrado.altura) # 10
print(quadrado.atributo_quadrado) # quadrado
print(triangulo.altura) # 15
print(triangulo.atributo_triangulo) # triangulo
print(retângulo.altura) # 5
print(retângulo.atributo_retângulo) # retângulo
print('-'*20)

class FormaGeométrica: # Classe
    def __init__(self, altura, largura): # Método construtor
        self.altura = altura # Atributo
        self.largura = largura # Atributo
    def calcula_area(self): # Método
        pass
    
class Quadrado(FormaGeométrica):
    def calcula_area(self): # Método
        return self.altura * self.largura
    
class Triângulo(FormaGeométrica):
    def calcula_area(self): # Método
        return self.altura * self.largura / 2
    
class Retângulo(FormaGeométrica):
    def calcula_area(self): # Método
        return self.altura * self.largura

quadrado = Quadrado(10, 10) # Objeto
triângulo = Triângulo(15, 10) # Objeto
retângulo = Retângulo(5, 15) # Objeto

print(quadrado.calcula_area()) # 100
print(triângulo.calcula_area()) # 75
print(retângulo.calcula_area()) # 75
print('-'*20)

class Veículo: # Classe
    def __init__(self, marcha): # Método construtor
        self.marcha = marcha # Atributo
    def aumenta_marcha(self): # Método
        self.marcha += 1 # Incrementando a marcha
        self.marcha = min(self.marcha, 5) # Limitando a marcha a 5
    def reduz_marcha(self): # Método
        self.marcha -= 1 # Decrementando a marcha
        self.marcha = max(self.marcha, 0) # Limitando a marcha a 0

class Carro(Veículo): # Classe
    def __init__(self, marcha): # Método construtor
        Veículo.__init__(self, marcha) # Chamando o método construtor da classe pai

class Moto(Veículo): # Classe
    def __init__(self, marcha): # Método construtor
        Veículo.__init__(self, marcha) # Chamando o método construtor da classe pai
    def aumenta_marcha(self): # Método
        self.marcha += 1 # Incrementando a marcha
        self.marcha = min(self.marcha, 6) # Limitando a marcha a 6
        
carro = Carro(1) # Objeto
carro.aumenta_marcha() # Incrementando a marcha
print(carro.marcha) # 2

moto = Moto(1) # Objeto
moto.aumenta_marcha() # Incrementando a marcha
print(moto.marcha) # 2
print('-'*20)

#Herança Múltipla
#Herança múltipla é a capacidade de uma subclasse herdar de múltiplas superclasses.

class Base1: # Classe
    def __init__(self, atributo1): # Método construtor
        self.atributo1 = atributo1 # Atributo
    def Base1_print(self):
        print("Base1")

class Base2: # Classe
    def __init__(self, atributo2): # Método construtor
        self.atributo2 = atributo2 # Atributo
    def Base2_print(self):
        print("Base2")

class MinhaClasse(Base1, Base2): # Classe
    def __init__(self):
        Base1.__init__(self, 10) # Chamando o método construtor da classe Base1
        Base2.__init__(self, 20) # Chamando o método construtor da classe Base2
        
var = MinhaClasse() # Objeto
print(var.atributo1) # 10
print(var.atributo2) # 20
var.Base1_print() # Base1
var.Base2_print() # Base2
print('-'*20)

#Modificadores de Acesso
#Public: Atributos e métodos públicos podem ser acessados por qualquer classe.
#Protected: Atributos e métodos protegidos só podem ser acessados por classes filhas.
#Private: Atributos e métodos privados só podem ser acessados pela própria classe.
#Em Python, não existem modificadores de acesso, mas é possível simular o comportamento de atributos e métodos protegidos e privados.

# class Segredo:
#     def __init__(self):
#         self.__segredo = 'Senha 123' # Atributo privado

# seg = Segredo() # Objeto
# print(seg.__segredo) # AttributeError: 'Segredo' object has no attribute '__segredo'
# print('-'*20)

class Segredo: # Classe
    def __init__(self): # Método construtor
        self.__segredo = 'Senha 123' # Atributo privado

    def __printa_segredo(self): # Método privado
        print(self.__segredo)
        
    def printa_segredo(self): # Método público
        self.__printa_segredo() # Chamando o método privado

seg = Segredo() # Objeto
seg.printa_segredo() # Senha 123
print('-'*20)

class Base:
    def __base__privada(self):
        print("Pertenço a classe Base")
    
    def _baseprotegida(self):
        print("Pertenço a classe Base e a quem me herdar")
        
class Filha(Base):
    def acessa_base_protegida(self):
        self._baseprotegida()

filha = Filha()
filha.acessa_base_protegida()
filha._baseprotegida()
print('-'*20)

class Veículo: # Classe
    def __init__(self): # Método construtor
        self.__marcha = 1 # Atributo
    def aumenta_marcha(self): # Método
        self.__marcha += 1 # Incrementando a marcha
        self.__marcha = min(self.__marcha, 5) # Limitando a marcha a 5
    def reduz_marcha(self): # Método
        self.__marcha -= 1 # Decrementando a marcha
        self.__marcha = max(self.__marcha, 1) # Limitando a marcha a 1
    def marcha_atual(self): # Método
        return self.__marcha # Retornando a marcha

carro = Veículo() # Objeto
carro.aumenta_marcha()# Incrementando a marcha
carro.aumenta_marcha()# Incrementando a marcha
carro.aumenta_marcha()# Incrementando a marcha
carro.aumenta_marcha()# Incrementando a marcha
carro.aumenta_marcha()# Incrementando a marcha
print(carro.marcha_atual()) # 2
carro.reduz_marcha() # Decrementando a marcha
carro.reduz_marcha() # Decrementando a marcha
carro.reduz_marcha() # Decrementando a marcha
carro.reduz_marcha() # Decrementando a marcha
print(carro.marcha_atual()) # 1
print('-'*20)

#Protegendo Atributos com Property
#A função property() permite proteger atributos de uma classe, evitando que sejam acessados diretamente.
#property(fget, fset, fdel, doc)

class Pessoa: # Classe
    def __init__(self, nome): # Método construtor
        self.__nome = nome # Atributo privado
    
    def get_nome(self): # Método get
        print("Pegando o nome") # Mensagem
        return self.__nome # Retornando o nome
        
    nome = property(get_nome) # Propriedade

instancia = Pessoa("João") # Objeto
print(instancia.nome) # João
print('-'*20)

class Pessoa: # Classe
    def __init__(self, nome): # Método construtor
        self.__nome = nome # Atributo privado
    
    def get_nome(self): # Método get
        print("Pegando o nome") # Mensagem
        return self.__nome # Retornando o nome
    
    def set_nome(self, nome): # Método set
        if len(nome)>0: # Se o nome não for vazio
            print("Alterando o nome") # Mensagem
            self.__nome = nome # Alterando o nome
        
    nome = property(get_nome, set_nome) # Propriedade

instancia = Pessoa("João") # Objeto
print(instancia.nome) # João
instancia.nome = "Maria" # Alterando o nome
print(instancia.nome) # Maria
print('-'*20)

class Pessoa: # Classe
    def __init__(self, nome): # Método construtor
        self.__nome = nome # Atributo privado
       
    def set_nome(self, nome): # Método set
        if len(nome)>0: # Se o nome não for vazio
            print("Alterando o nome") # Mensagem
            self.__nome = nome # Alterando o nome
        
    nome = property(fset= set_nome) # Propriedade
    
instancia = Pessoa("João") # Objeto
instancia.nome = "Maria" # Alterando o nome
print('-'*20)

#Protegendo atributos com decoradores
#Decoradores são funções que modificam o comportamento de outras funções ou métodos.

class Natural: # Classe
    def __init__(self, número): # Método construtor
        self.__número = número # Atributo privado
    
    @property # Decorador
    def número(self): # Método get
        print("Pegando o número") # Mensagem
        return self.__número # Retornando o número
    @número.setter # Decorador
    def número(self, value): # Método set
        if value >= 0: # Se o número for maior ou igual a 0
            self.__número = value # Alterando o número
            print("Setando o número para", value) # Mensagem
            
número = Natural(10) # Objeto
número.número = 20 # Setando o número para 20
print(número.número) # Pegando o número
print('-'*20)

class Pessoa: # Classe
    def __init__(self, nome): # Método construtor
        self.__nome = nome # Atributo privado
    @property # Decorador
    def nome(self): # Método get
        return self.__nome.capitalize() # Retornando o nome em maiúsculo
    @nome.setter # Decorador
    def nome(self, value): # Método set
        if len(value)!=0: # Se o nome não for vazio
            self.__nome = value # Alterando o nome

pessoa = Pessoa("joão") # Objeto
print(pessoa.nome) # João
pessoa.nome = "maria" # Alterando o nome
print(pessoa.nome) # Maria
pessoa.nome = "" # Alterando o nome
print(pessoa.nome) # Maria

#Métodos Estáticos
#Métodos estáticos são métodos que não precisam de uma instância da classe para serem chamados.
#Eles são definidos com o decorador @staticmethod.

class Teste: # Classe
    def __init__(self, gasolina): # Método construtor
        pass # Passando
    
    @classmethod # Decorador
    def class_method(cls): # Método de classe
        print(cls) # Imprimindo a classe
    @staticmethod # Decorador
    def static_method(): # Método estático
        print("Método estático") # Mensagem

Teste.class_method() # <class '__main__.Teste'>
Teste.static_method() # Método estático

testando = Teste("aditivada") # Objeto
testando.class_method() # <class '__main__.Teste'>
print('-'*20)

class Veículo: # Classe
    def __init__(self, nome, gasolina, potencia): # Método construtor
        self.nome = nome # Atributo
        self.gasolina = gasolina # Atributo
        self.potencia = potencia # Atributo
        
    
    @classmethod # Decorador
    def cria_carro(cls): # Método de classe
        return cls("Carro", "Comum", 200) # Retornando um carro
    @classmethod # Decorador
    def cria_moto(cls): # Método de classe
        return cls("Moto", "Aditivada", 150) # Retornando uma moto
    @classmethod # Decorador
    def cria_caminhão(cls): # Método de classe
        return cls("Caminhão", "Diesel", 300) # Retornando um caminhão

veículo1 = Veículo.cria_carro() # Objeto
veículo2 = Veículo.cria_moto() # Objeto
veículo3 = Veículo.cria_caminhão() # Objeto

print(veículo1.nome) # Carro
print(veículo2.gasolina) # Aditivada
print(veículo3.potencia) # 300
print('-'*20)

class Veículo: # Classe
    __número_veículos = 0 # Atributo privado
    def __init__(self, nome, gasolina, potencia): # Método construtor
        self.nome = nome # Atributo
        self.gasolina = gasolina # Atributo
        self.potencia = potencia # Atributo
        Veículo.__número_veículos += 1 # Incrementando o número de veículos    
    @staticmethod # Decorador
    def get_número_veículos(): # Método estático
        return Veículo.__número_veículos # Retornando o número de veículos

veículo1 = Veículo("Carro", "Comum", 200) # Objeto
veículo2 = Veículo("Moto", "Aditivada", 150) # Objeto
veículo3 = Veículo("Caminhão", "Diesel", 300) # Objeto
print(Veículo.get_número_veículos()) # 3
print(veículo1.get_número_veículos()) # 3
print('-'*20)

#Copia por valor e por referência
#Em Python, a passagem de parâmetros é feita por referência, ou seja, a variável passada como argumento é um ponteiro para o objeto.
#Se a variável for imutável, a passagem é feita por valor, ou seja, uma cópia do valor é passada como argumento.
#Se a variável for mutável, a passagem é feita por referência, ou seja, um ponteiro para o objeto é passado como argumento.

lst1 = 10 # Imutável
lst2 = lst1 # Passagem por valor
lst2 = 20 # Alterando o valor
print(lst1) # 10
print('-'*20) 

lst1 = [1,2,3] # Mutável
lst2 = lst1 # Passagem por referência
lst2.append(4) # Alterando o valor
print(lst1) # [1, 2, 3, 4]
print('-'*20)

class Classe: # Classe
    def __init__(self): # Método construtor
        self.num = 10 # Atributo
classe1 = Classe() # Objeto
classe2 = classe1 # Passagem por referência
classe1.num = 20 # Alterando o valor
print(classe2.num) # 20
print('-'*20)

from copy import copy
from typing import Any # Importando a função copy

lst1 = [1,2,3] # Mutável
lst2 = copy(lst1) # Passagem por valor
lst2.append(4) # Alterando o valor
print(lst1) # [1, 2, 3]
print("-"*20)

class Classe: # Classe
    def __init__(self): # Método construtor
        self.num = 10 # Atributo
classe1 = Classe() # Objeto
classe2 = copy(classe1) # Passagem por valor
classe1.num = 20 # Alterando o valor
print(classe2.num) # 10
print('-'*20)

class Classe: # Classe
    def __init__(self): # Método construtor
        self.num = 10 # Atributo
classe1 = Classe() # Objeto
classe2 = classe1 # Passagem por referência
print(classe2 is classe1) # True
print('-'*20)

class Classe: # Classe
    def __init__(self): # Método construtor
        self.num = 10 # Atributo
classe1 = Classe() # Objeto
classe2 = copy(classe1) # Passagem por valor
print(classe2 is classe1) # False
print('-'*20)

#Deletando Objetos
#O comando del é utilizado para deletar objetos em Python.
#Quando um objeto é deletado, o espaço de memória que ele ocupava é liberado.
#O comando del não deleta o objeto, mas sim a referência para o objeto.
#O garbage collector é responsável por deletar objetos que não são mais referenciados.
#O comando del pode ser utilizado para deletar variáveis, listas, dicionários, etc.

# número = 10 # Variável
# del número # Deletando a variável
# print(número) # NameError: name 'número' is not defined
# print('-'*20)

# arr = [1,2,3] # Lista
# del arr # Deletando a lista
# print(arr) # NameError: name 'arr' is not defined
# print('-'*20)

arr = [1,2,3] # Lista
del arr[0] # Deletando o elemento
print(arr) # [2, 3]
print('-'*20)

class Teste: # Classe
    def __init__(self): # Método construtor
        pass # Passando

variável = Teste() # Objeto
del variável # Deletando o objeto
print('-'*20)

# class Teste:
#     def __init__(self, num):
#         self.num = num

# variável = Teste(10)
# )print(variável.num)
# del variável
# print(variável.num) # NameError: name 'variável' is not defined
# print('-'*20

class Teste: # Classe
    def __init__(self): # Método construtor
        self.lista = [1,2,3] # Atributo
    def __del__(self): # Método destrutor
        print("Objeto deletado") # Mensagem

teste = Teste() # Objeto
del teste # Deletando o objeto
print('-'*20)

class Pessoa: # Classe
    def __init__(self, nome): # Método construtor
        self.__nome = nome # Atributo
        
    def get_nome(self): # Método get
        print("Pegando o nome") # Mensagem
        return self.__nome # Retornando o nome
    
    def set_nome(self, nome): # Método set
        print("Setando nome") # Mensagem
        self.__nome = nome # Alterando o nome
        
    def del_nome(self): # Método del
        print("Deletando nome") # Mensagem
        del self.__nome # Deletando o nome

    nome = property(get_nome, set_nome, del_nome) # Propriedade
    
instancia = Pessoa("João") # Objeto

del instancia.nome # Deletando o nome
print('-'*20)

class Pessoa: # Classe
    def __init__(self, nome): # Método construtor
        self.__nome = nome # Atributo
        
    @property # Decorador
    def nome(self): # Método get
        return self.__nome # Retornando o nome
    
    @nome.deleter # Decorador
    def nome(self): # Método del
        print("Deletando o nome") # Mensagem
        del self.__nome # Deletando o nome
        
instancia = Pessoa("João") # Objeto
del instancia.nome # Deletando o nome
print('-'*20)

#Testando tipos de objetos

e_inteiro = isinstance(5, int)
print(e_inteiro) # True
print('-'*20)
    
e_inteiro = isinstance(5, (int, float, str))
print(e_inteiro) # True
print('-'*20)

class Base: # Classe
    pass # Passando

classe = Base() # Objeto
e_base = isinstance(classe, Base)
print(e_base) # True
print('-'*20)

class Base: # Classe
    def __init__(self): # Método construtor
        pass # Passando

class Herdeiro(Base): # Classe
    def __init__(self): # Método construtor
        pass # Passando

classe = Herdeiro() # Objeto
e_base = isinstance(classe, Base) # True
e_herdeiro = isinstance(classe, Herdeiro) # True
print(e_base) # True
print(e_herdeiro) # True
print('-'*20)

class Base: # Classe
    def __init__(self): # Método construtor
        pass # Passando

class Herdeiro(Base): # Classe
    def __init__(self): # Método construtor
        pass # Passando

classe = Base() # Objeto
e_base = isinstance(classe, Base) # True
e_herdeiro = isinstance(classe, Herdeiro) # False
print(e_base) # True
print(e_herdeiro) # False
print('-'*20)

class Base: # Classe
    def __init__(self): # Método construtor
        pass # Passando

class Herdeiro(Base): # Classe
    def __init__(self): # Método construtor
        pass # Passando

e_base = issubclass(Base, Herdeiro) # False
e_herdeiro = issubclass(Herdeiro, Base) # True
print(e_base) # False
print(e_herdeiro) # True
print('-'*20)

def soma(num1, num2): # Função
    if isinstance(num1, (int, float)) and isinstance(num2, (int, float)): # Se os números forem inteiros ou float
        return num1 + num2 # Retornando a soma
    else: # Senão
        return None

print(soma(10, 20)) # 30
print(soma(10, '20')) # None
print('-'*20)

class Veículo: # Classe
    def __init__(self): # Método construtor
        pass
    def acelera(self): # Método
        pass

class Moto(Veículo): # Classe
    def __init__(self):
        pass
class Carro(Veículo): # Classe
    def __init__(self):
        pass
    def ré(self): # Método
        print("Dando ré") # Mensagem

def faz_re(var): # Função
    if isinstance(var, Carro): # Se a variável for um carro
        var.ré() # Chamando o método ré
    else: # Senão
        print("Não tem ré") # Mensagem

motinha = Moto() # Objeto
carrinho = Carro() # Objeto

faz_re(motinha) # None
faz_re(carrinho) # Dando ré
print('-'*20)

#Uso de With
#O comando with é utilizado para abrir e fechar arquivos.
#O comando with garante que o arquivo será fechado mesmo se ocorrer um erro durante a execução do código.

class Lista(): # Classe
    def __init__(self): # Método construtor
        pass
    
    def __enter__(self): # Método enter
        print("Memória Iniciada") # Mensagem
        self.lista = [i for i in range(0,10)] # Lista
        return self.lista # Retornando a lista
    
    def __exit__(self, *args, **kwargs): # Método exit
        print("Memória Liberada") # Mensagem
        del self.lista # Deletando a lista
        
with Lista() as temp_lista: # Abrindo o arquivo
    for i in temp_lista: # Para cada elemento na lista
        print(i) # Imprimindo o elemento

print("Aqui o objeto já foi deletado") # Mensagem
print('-'*20)

class Lista(): # Classe
    def __init__(self): # Método construtor
        pass
    
    def __enter__(self): # Método enter
        print("Memória Iniciada") # Mensagem
        self.lista = [i for i in range(0,10)] # Lista
        return self.lista # Retornando a lista
    
    def __exit__(self, *args, **kwargs): # Método exit
        print("Memória Liberada") # Mensagem
        del self.lista # Deletando a lista

minha_lista = Lista() # Objeto
        
with minha_lista as temp_lista: # Abrindo o arquivo
    for i in temp_lista: # Para cada elemento na lista
        print(i) # Imprimindo o elemento

print("Aqui o objeto já foi deletado") # Mensagem
print('-'*20)

#Sobrecarga de Operadores
#Sobrecarga de operadores é a capacidade de uma classe definir o comportamento de operadores como +, -, *, /, etc.
#Em Python, a sobrecarga de operadores é feita através de métodos especiais.
#Métodos especiais são métodos que começam e terminam com dois underlines.
#Métodos especiais são chamados automaticamente quando uma operação é realizada.
#Métodos especiais são utilizados para sobrecarga de operadores, conversão de tipos, etc.

class MeuNumero: # Classe
    def __init__(self, número): # Método construtor
        self.número = número # Atributo
    def __add__(self, outro): # Método especial
        return self.número + outro.número # Retornando a soma

num1 = MeuNumero(10) # Objeto
num2 = MeuNumero(20) # Objeto
print(num1 + num2) # 30
print('-'*20)

class MeuNumero: # Classe
    def __init__(self, número): # Método construtor
        self.número = número # Atributo
    def __add__(self, outro): # Método especial
        soma = self.número + outro.número # Retornando a soma
        return MeuNumero(soma) # Retornando o objeto

num1 = MeuNumero(10) # Objeto
num2 = MeuNumero(20) # Objeto
num3 = num1 + num2 # Objeto
print(num3.número) # 30
print('-'*20)

class MeuNumero: # Classe
    def __init__(self, número): # Método construtor
        self.número = número # Atributo
    def __sub__(self, outro): # Método especial
            return self.número - outro.número # Retornando a subtração

num1 = MeuNumero(20) # Objeto
num2 = MeuNumero(10) # Objeto
print(num1 - num2) # 10
print('-'*20)

#Atividade

1
class Carro: # Classe
    def __init__(self, cavalos=None, kmporlitro=None): # Método construtor unificado
        self.cavalos = cavalos # Atributo
        self.kmporlitro = kmporlitro # Atributo

# Criando objetos com diferentes atributos
potencia1 = Carro(cavalos=200) # Objeto com atributo cavalos
consumo1 = Carro(kmporlitro=10) # Objeto com atributo kmporlitro
potencia2 = Carro(cavalos=150) # Objeto com atributo cavalos
consumo2 = Carro(kmporlitro=15) # Objeto com atributo kmporlitro
# Acessando e imprimindo os atributos
print("O carro 1 tem:",potencia1.cavalos, "cavalos de força!") # 200
print("O carro 1 consome:",consumo1.kmporlitro, "litros por Kilometro!\n") # 10
print("O carro 2 tem:",potencia2.cavalos, "cavalos de força!") # 150
print("O carro 2 consome:",consumo2.kmporlitro, "litros por Kilometro!") # 15
print('-'*20)

2
class Pessoa: # Classe
    def __init__(self,nome, cpf, dependente=None): # Método construtor
        self.nome = nome # Atributo
        self.cpf = cpf # Atributo
        self.dependente = dependente # Atributo

class Dependente(Pessoa): # Classe filha
    def __init__(self, nome, cpf, dependente=None): # Método construtor
        Pessoa.__init__(self, nome, cpf,dependente) # Chamando o método construtor da classe pai
        
# Criando objetos com diferentes atributos
david = Pessoa(nome="David",cpf=123456789, dependente=Dependente(nome="Yasmin", cpf=987654321)) # Objeto com atributo dependente
yasmin = Dependente(nome="Yasmin",cpf=987654321) # Objeto com atributo dependente
# Acessando e imprimindo os atributos
print("O David tem o CPF:", david.cpf, "e o(a) dependente", david.dependente.nome, "com o CPF:", david.dependente.cpf) # 123456789 e o(a) 987654321
print("A Yasmin tem o CPF:", yasmin.cpf, "e o(a) dependente:", yasmin.dependente) # 987654321 e o(a) None
print('-'*20)

3
class Veículo: # Classe
    def __init__(self, nome, peso, potencia, rodas): # Método construtor
        self.nome = nome # Atributo
        self.peso = peso # Atributo
        self.potencia = potencia # Atributo
        self.rodas = rodas # Atributo
        
class Ônibus(Veículo): # Classe filha
    def __init__(self, nome, peso, potencia, rodas): # Método construtor
        Veículo.__init__(self, nome, peso, potencia, rodas) # Chamando o método construtor da classe pai

class Carro(Veículo): # Classe filha
    def __init__(self, nome, peso, potencia, rodas): # Método construtor
        Veículo.__init__(self, nome, peso, potencia, rodas) # Chamando o método construtor da classe pai

class Moto(Veículo): # Classe filha
    def __init__(self, nome, peso, potencia, rodas): # Método construtor
        Veículo.__init__(self, nome, peso, potencia, rodas) # Chamando o método construtor da classe pai

# Criando objetos com diferentes atributos
ônibus = Ônibus(nome="Ônibus", peso=1000, potencia=200, rodas=6) # Objeto
carro = Carro(nome="Carro", peso=500, potencia=150, rodas=4) # Objeto
moto = Moto(nome="Moto", peso=200, potencia=100, rodas=2) # Objeto
# Acessando e imprimindo os atributos
print("O Ônibus tem:",ônibus.peso, "kg de peso,", ônibus.potencia, "de potencia, e possui", ônibus.rodas, "rodas.") # 1000 kg de peso 200 de potencia, e possui: 6 rodas.
print("O Carro tem:",carro.peso, "kg de peso,", carro.potencia, "de potencia, e possui", carro.rodas, "rodas.") # 500 kg de peso 150 de potencia, e possui: 4 rodas.
print("A Moto tem:",moto.peso, "kg de peso,", moto.potencia, "de potencia, e possui", moto.rodas, "rodas.") # 200 kg de peso 100 de potencia, e possui: 2 rodas.
print('-'*20)

4
class Veículo: # Classe
    def __init__(self, peso, potencia): # Método construtor
        self.peso = peso # Atributo
        self.potencia = potencia # Atributo
    def distancia_percorrida(self): # Método
        return (self.potencia / self.peso) * 1000 # Retornando a distância percorrida
    
class Ônibus(Veículo): # Classe filha
    def __init__(self, peso, potencia): # Método construtor
        Veículo.__init__(self, peso, potencia) # Chamando o método construtor da classe pai

class Carro(Veículo): # Classe filha
    def __init__(self, peso, potencia): # Método construtor
        Veículo.__init__(self, peso, potencia) # Chamando o método construtor da classe pai

class Moto(Veículo): # Classe filha
    def __init__(self, peso, potencia): # Método construtor
        Veículo.__init__(self, peso, potencia) # Chamando o método construtor da classe pai
        
# Criando objetos com diferentes atributos
ônibus = Ônibus(peso=1000, potencia=200) # Objeto
carro = Carro(peso=500, potencia=150) # Objeto
moto = Moto(peso=200, potencia=100) # Objeto
# Acessando e imprimindo os atributos
print("O Ônibus percorre:",ônibus.distancia_percorrida(), "metros por litro.") # 200 metros por litro.
print("O Carro percorre:",carro.distancia_percorrida(), "metros por litro.") # 300 metros por litro.
print("A Moto percorre:",moto.distancia_percorrida(), "metros por litro.") # 500 metros por litro.
print('-'*20)

5
class Veículo: # Classe
    def __init__(self, peso, potencia): # Método construtor
        self.peso = peso # Atributo
        self.potencia = potencia # Atributo
        
    def distancia_percorrida(self): # Método
        return (self.potencia / self.peso) * 1000 # Retornando a distância percorrida
    
    def __lt__(self, outro): # Método especial
        return self.potencia < outro.potencia # Retornando a comparação
    
    def __gt__(self, outro): # Método especial
        return self.potencia > outro.potencia # Retornando a comparação   
class Ônibus(Veículo): # Classe filha
    def __init__(self, peso, potencia): # Método construtor
        Veículo.__init__(self, peso, potencia) # Chamando o método construtor da classe pai

class Carro(Veículo): # Classe filha
    def __init__(self, peso, potencia): # Método construtor
        Veículo.__init__(self, peso, potencia) # Chamando o método construtor da classe pai

class Moto(Veículo): # Classe filha
    def __init__(self, peso, potencia): # Método construtor
        Veículo.__init__(self, peso, potencia) # Chamando o método construtor da classe pai
        
# Criando objetos com diferentes atributos
ônibus = Ônibus(peso=1000, potencia=200) # Objeto
carro = Carro(peso=500, potencia=150) # Objeto
moto = Moto(peso=200, potencia=100) # Objeto
# Acessando e imprimindo os atributos
print(f"O Ônibus é mais potente que o Carro? ", ônibus > carro) # True
print(f"O Carro é mais potente que a Moto? ", carro > moto) # True
print(f"A Moto é menos potente que o Ônibus? ", moto < ônibus) # False
print('-'*20)

6
class Negativo: # Classe
    def __init__(self, valor): # Método construtor
        self.__valor = 0 # Atributo
        self.valor = valor # Atributo

    @property # Decorador
    def valor(self): # Método get
        return self.__valor # Retornando o valor

    @valor.setter # Decorador
    def valor(self, value): # Método set
        if value <= 0: # Se o valor for menor ou igual a 0
            self.__valor = value # Alterando o valor

    def __lt__(self, other): # Método especial
        return self.__valor < other.__valor # Retornando a comparação

    def __gt__(self, other): # Método especial
        return self.__valor > other.__valor # Retornando a comparação

    def __sub__(self, other): # Método especial
        sub = self.__valor - other.__valor # Subtraindo os valores
        if sub > 0: # Se o resultado for positivo
            sub = 0
        return sub # Retornando o resultado

# Testando a classe NumeroNegativo
num1 = Negativo(-10) # Objeto
num2 = Negativo(-5) # Objeto
num3 = Negativo(5) # Objeto

print(num1.valor, num2.valor, num3.valor) # -10 -5 5
print(num1 < num2) # True
print(num1 > num3) # False
print(num1 - num2) # 0
print(num1 - num3) # -5
print(num3 - num1) # 0
print('-'*20)

7
def verificar_tipo(obj): # Função
    if isinstance(obj, (int, float, str, bool)): # Se o objeto for um tipo primitivo
        return f"O objeto {obj} é um tipo primitivo e é passado por valor." # Mensagem
    else: # Senão
        return f"O objeto {obj} é um objeto e é passado por referência." # Mensagem

class Objeto: # Classe
    def __init__(self): # Método construtor
        pass
obj = Objeto() # Objeto
valor = 3 # Variável

# Exemplos de uso
print(verificar_tipo(10))       # int
print(verificar_tipo(3.14))     # float
print(verificar_tipo("Ola"))  # str
print(verificar_tipo(True))     # bool
print(verificar_tipo([1, 2, 3])) # list (não primitivo)
print(verificar_tipo(obj))      # Objeto (não primitivo)
print(verificar_tipo(valor))    # int (primitivo)
print('-'*20)


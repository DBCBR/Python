#Matplotlib é uma biblioteca de plotagem 2D em Python que produz figuras de qualidade em uma variedade de formatos impressos e ambientes interativos em todas as plataformas. Matplotlib pode ser usado para gerar gráficos, histogramas, espectros de potência, gráficos de barras, gráficos de erro, gráficos de dispersão, etc.

# import matplotlib.pyplot as plt
# import numpy as np

# x = np.array([1,2,3,4,5]) #criando um array com 5 elementos
# y = np.array([2,4,6,8,10]) #criando um array com 5 elementos

# plt.plot(x,y) #plotando o gráfico com os valores de x e y
# plt.show() #mostrando o gráfico

# import matplotlib.pyplot as plt
# import numpy as np

# x = np.array([0,1,2,3,4,5])
# y = x * 2

# plt.plot(x,y)
# plt.show()

# import matplotlib.pyplot as plt
# import numpy as np

# y =np.array([-2,2,10,4,5])
# x = np.array(['Segunda','Terça','Quarta','Quinta','Sexta'])
# plt.plot(x,y)
# plt.show()

# import matplotlib.pyplot as plt
# import numpy as np

# x1 = np.array([1,2,3,4,5])
# y1 = x1 * 2

# x2 = np.array([5,10,15])
# y2 = x2 + 2

# plt.plot(x1,y1)
# plt.plot(x2,y2)
# plt.show()

# import matplotlib.pyplot as plt
# import numpy as np

# x1 = np.arange(1,10)
# y1 = x1 * 2

# x2 = np.arange(1,10)
# y2 = x2 ** 2

# plt.plot(x1,y1)
# plt.plot(x2,y2)
# plt.axis([0,10,-1,50])
# plt.show()

# import matplotlib.pyplot as plt
# import numpy as np

# x1 = np.arange(1,10)
# y1 = x1 * 2

# x2 = np.arange(1,10)
# y2 = x2 ** 2

# plt.plot(x1,y1)
# plt.plot(x2,y2)
# plt.xlim(0,10)
# plt.ylim(-1,50)
# plt.show()

# import matplotlib.pyplot as plt
# import numpy as np

# x = np.array([1,2,3,4,5])
# y = x * 2

# plt.xlabel("Vendas")
# plt.ylabel("Temperatura")
# plt.title("Gráfico de Vendas", y=1.10, loc="center")
# plt.plot(x,y)
# plt.show()

# import matplotlib.pyplot as plt
# import numpy as np

# font_props = { #criando um dicionário com as propriedades da fonte
#     'family': 'arial', #família da fonte
#     'color': 'red', #cor da fonte
#     'weight': 'bold', #negrito
#     'size': 10 #tamanho da fonte
#     }

# font_props2 = { #criando um dicionário com as propriedades da fonte
#     'family': 'arial', #família da fonte
#     'color': 'blue', #cor da fonte
#     'weight': 'normal', #negrito
#     'size': 12 #tamanho da fonte
#     }
# x = np.arange(-10,10,0.1) #criando um array de 0 a 20 pulando de 0.5 em 0.5
# y = x ** 2 #elevando o array ao quadrado 

# plt.figure(figsize=(3,3)) #definindo o tamanho da figura

# plt.text(-5, 50, "É uma Parábola", fontdict=font_props2) #adicionando um texto no gráfico

# plt.xlabel("Vendas", fontdict=font_props) #adicionando o label no eixo x
# plt.ylabel("Temperatura", fontdict=font_props) #adicionando o label no eixo y
# plt.title("Gráfico de Vendas", fontdict=font_props) #adicionando o título do gráfico

# plt.plot(x,y) #plotando o gráfico
# plt.show() #mostrando o gráfico

# import matplotlib.pyplot as plt
# import numpy as np

# x = np.arange(0,10,0.5)
# y = x ** 6

# plt.plot(x,y, c='g', linewidth= 6.5, linestyle='dashed')

# plt.xlabel('Eixo X')
# plt.ylabel('Eixo Y')
# plt.title('A função y = x ** 6')
# plt.show()

# import matplotlib.pyplot as plt
# import numpy as np

# x1 = np.arange(0,20,0.5)
# y1 = np.cos(x1)

# x2 = np.arange(0,20,0.5)
# y2 = np.cos(x2)*2

# plt.xlabel("Vendas")
# plt.ylabel("Temperatura")
# plt.title("Gráfico de Vendas")

# plt.plot(x1,y1, c='g', linewidth= 6.5, linestyle='dashed', label='Vendas', alpha=0.3)
# plt.plot(x2,y2, c='b', linewidth= 3.5, linestyle='solid', label='Temperatura')
# plt.legend(loc = 'best')
# plt.show()

# import matplotlib.pyplot as plt
# import numpy as np

# x = np.arange(0,19) #criando um array de 0 a 19
# y = -x ** 4 #elevando o array ao quadrado

# plt.xlabel("Eixo X") #adicionando o label no eixo x
# plt.ylabel("Eixo Y") #adicionando o label no eixo y
# plt.title("Gráfico da Função y = -x ** 4") #adicionando o título do gráfico
# plt.plot(x, y, c='orange', lw='1.5', marker='o') #plotando o gráfico com os valores de x e y e definindo a cor, a largura da linha e o marcador
# plt.show() #mostrando o gráfico

#Aprimorando com Linhas e Grades

# import matplotlib.pyplot as plt
# import numpy as np

# x1 = np.arange(1,100)
# y1 = x1 ** 2

# plt.plot(x1,y1)
# plt.grid(
#     c = 'black', #cor da grade
#     ls = 'dotted', #estilo da linha
#     lw = 1.5, #largura da linha
#     alpha = 0.5 #transparência
# )
# plt.show()

# import matplotlib.pyplot as plt
# import numpy as np

# x1 = np.arange(1,100)
# y1 = x1 ** 2

# plt.plot(x1,y1, color='r')
# plt.grid(c='b', ls='dotted', lw=1.5, alpha=0.5)
# plt.xticks([1,2,4,6,8,10,20,40,60,80,100])
# plt.show()

# import matplotlib.pyplot as plt
# import numpy as np

# x1 = np.arange(1,100)
# y1 = x1 ** 2

# print(plt.style.available)
# plt.style.use('classic')
# plt.grid(c='gray')
# plt.plot(x1,y1)
# plt.show()

# import matplotlib.pyplot as plt
# import numpy as np

# x1 = np.arange(0,20,0.5)
# y1 = x1*2

# x2 = np.arange(0,20,0.5)
# y2 = np.sin(x2)

# plt.subplot(1,2,1)
# plt.title("A Primeira Função")
# plt.plot(x1,y1, c='g', lw='6.5', ls='dashed')
# plt.subplot(1,2,2)
# plt.title("A Segunda Função")
# plt.plot(x2,y2, c='b', lw='3.5', ls='solid')
# plt.show()

# import matplotlib.pyplot as plt
# import numpy as np

# x1 = np.arange(0,20,0.5)
# y1 = np.cos(x1)

# x2 = np.arange(0,20,0.5)
# y2 = np.cos(x2)*2

# plt.subplot(2,1,1)
# plt.xlabel('Eixo X')
# plt.ylabel('Eixo Y')
# plt.title("A Primeira Função Cosseno")
# plt.plot(x1,y1, c='g', lw='6.5', ls='dashed', label="y = cos(x)")
# plt.legend(loc='best')
# plt.ylim(-3,2)
# plt.grid()
# plt.tight_layout()

# plt.subplot(2,1,2)
# plt.xlabel('Eixo X')
# plt.ylabel('Eixo Y')
# plt.title("A Segunda Função Cosseno")
# plt.plot(x2,y2, c='b', lw='3.5', ls='solid', label="y = cos(x2)*2")
# plt.legend(loc='best')
# plt.ylim(-3,2)
# plt.grid()
# plt.suptitle("Gráficos de Funções Cosseno")
# plt.tight_layout()
# plt.show()

#Gráficos de Barras

#import matplotlib.pyplot as plt
#import numpy as np

# x = np.array([1,2,3,4,5])
# y = np.array([2,4,6,8,10])

# plt.bar(x,y, color='r', width=0.3)
# plt.show()

# import matplotlib.pyplot as plt
# import numpy as np

# y = np.array([1,2,3])
# x = np.array(["Um","Dois","Três"])

# plt.barh(x,y, color='r', height=0.3)
# plt.title("Gráfico de Barras")
# plt.xlabel("Valores")
# plt.ylabel("Quantidade")
# plt.show()

# import matplotlib.pyplot as plt
# import numpy as np

# valores_esquerda = np.arange(0,6)
# valores_direita = np.arange(6,0,-1)
# ys = np.arange(6)

# plt.barh(ys, valores_esquerda, color='y')
# plt.barh(ys, -valores_direita, color='r')

# plt.legend(['Direita', 'Esquerda'])

# plt.title("Gráfico de Barras Dividido")
# plt.ylabel("Valores de Y")
# plt.xlabel("Valores Esquerda X Valores Direita")
# plt.show()

# import matplotlib.pyplot as plt
# import numpy as np

# valores_esquerda = np.arange(0,6)
# valores_direita = np.arange(6,0,-1)
# xs = np.arange(6)

# plt.bar(xs, valores_esquerda, color='y')
# plt.bar(xs, -valores_direita, color='r')

# plt.legend(['Direita', 'Esquerda'])

# plt.title("Gráfico de Barras Dividido")
# plt.ylabel("Valores de Y")
# plt.xlabel("Valores Esquerda X Valores Direita")
# plt.show()

#Gráfico Empilhado

# import matplotlib.pyplot as plt
# import numpy as np

# xs = np.array(['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio'])
# time1 = np.array([5,10,15,20,25])
# time2 = np.array([6,8,2,7,9])
# time3 = np.array([12,10,15,23,21])
# time4 = np.array([5,24,34,21,51])
# time5 = np.array([4,21,13,21,14])

# plt.bar(xs,time1, color='r', width=0.5)
# plt.bar(xs,time2,bottom=time1, color='b', width=0.5)
# plt.bar(xs,time3,bottom=time2+time1, color='g', width=0.5)
# plt.bar(xs,time4,bottom=time3+time2+time1, color='y', width=0.5)
# plt.bar(xs,time5,bottom=time4+time3+time2+time1, color='k', width=0.5)

# plt.title("Rendimento no Esporte")
# plt.xlabel("Meses")
# plt.ylabel("Pontuação")
# plt.legend(['Time 1', 'Time 2', 'Time 3', 'Time 4', 'Time 5'])
# plt.show()

# import matplotlib.pyplot as plt
# import numpy as np

# xs = np.array(['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio'])
# time1 = np.array([5,10,15,20,25])
# time2 = np.array([6,8,2,7,9])
# time3 = np.array([12,10,15,23,21])
# time4 = np.array([5,24,34,21,51])
# time5 = np.array([4,21,13,21,14])

# plt.barh(xs,time1, color='r')
# plt.barh(xs,time2,left=time1, color='b')
# plt.barh(xs,time3,left=time2+time1, color='g')
# plt.barh(xs,time4,left=time3+time2+time1, color='y')
# plt.barh(xs,time5,left=time4+time3+time2+time1, color='k')

# plt.title("Rendimento no Esporte")
# plt.xlabel("Meses")
# plt.ylabel("Pontuação")
# plt.legend(['Time 1', 'Time 2', 'Time 3', 'Time 4', 'Time 5'])
# plt.show()

#Histogramas

# import matplotlib.pyplot as plt
# import numpy as np

# alturas = np.array([1.53,1.65,1.75,1.86,1.74,1.59,1.87,1.98])
# plt.hist(alturas, color='r', edgecolor='k', bins=[1.50,1.60,1.70,1.80,1.90,2.00])
# plt.xlabel("Alturas")
# plt.ylabel("Frequência")
# plt.title("Histograma de Alturas")
# plt.show()

# import matplotlib.pyplot as plt
# import numpy as np

# alturas = np.array([1.53,1.65,1.75,1.86,1.74,1.59,1.87,1.98])
# plt.hist(alturas, color='r', edgecolor='k')
# plt.xlabel("Alturas")
# plt.ylabel("Frequência")
# plt.title("Histograma de Alturas")
# plt.show()

# import matplotlib.pyplot as plt
# import numpy as np

# alturas_mundiais = np.random.normal(loc=175, scale=11, size=1000)/100
# alturas_brasileiras = np.random.normal(loc=185, scale=9, size=1000)/100

# plt.hist(alturas_mundiais, color='r', edgecolor='k', bins=30, alpha=0.5)
# plt.hist(alturas_brasileiras, color='b', edgecolor='k', bins=30, alpha=0.5)
# plt.legend(['Alturas Mundiais', 'Alturas Brasileiras'])
# plt.xlabel("Alturas")
# plt.ylabel("Frequência")
# plt.title("Histograma de Alturas")
# plt.show()

#Gráfico de Pizza

# import matplotlib.pyplot as plt
# import numpy as np

# classes = np.array(['Classe Baixa', 'Classe Média', 'Classe Alta'])
# dados = np.array([10,30,60])
# cores = np.array(['r','g','b'])
# offset = np.array([0.2,0.05,0.05])

# edge_props={'linewidth': 2, #definindo a largura da borda
#             'edgecolor': 'k', #definindo a cor da borda
#             'linestyle': 'solid' #definindo o estilo da borda
# } 

# text_props={
#     'color': 'k', #cor do texto
#     'size': 10, #tamanho do texto
#     'style': 'oblique' #estilo do texto
# } 

# plt.figure(figsize=(7,7))
# plt.pie(dados, labels=classes, colors=cores, shadow=True, startangle=90, autopct='%1.1f%%',explode=offset, wedgeprops=edge_props, textprops=text_props)
# plt.title("Distribuição de Renda das Classes Sociais")
# plt.legend(classes, loc='best')
# plt.tight_layout()
# plt.show()

#Gráfico de Dispersão

# import matplotlib.pyplot as plt
# import numpy as np

# plt.style.use('bmh')
# x = np.arange(0,10)
# y = np.array([1,4,9,12,4,7,4,9,2,1])
# z = np.array([100,50,150,200,100,120,130,80,90,144])

# cores = np.array(['r','g','b','y','k','c','m','orange','purple','pink'])
# plt.scatter(x,y, c=cores, marker='o', s=z)
# plt.title("Gráfico de Dispersão")
# plt.show()

#Atividades

1
# import matplotlib.pyplot as plt
# import numpy as np

# x = np.arange(0,10)
# y = 5*x +1
# plt.xlabel("Eixo X")
# plt.ylabel("Eixo Y")
# plt.title("Gráfico de Função")#
# plt.plot(x, y, c='b', mfc='r', marker='s')
# plt.show()

2
# import matplotlib.pyplot as plt
# import numpy as np

# cotação = np.array([3.15, 3.26, 3.88, 4.30, 5.33, 5.45, 5.39])
# anos = np.arange([2016,2023])
# plt.plot(anos, cotação, c='r', marker='o')
# plt.xlabel("Anos")
# plt.ylabel("Valor do Real (R$)")
# plt.title("Variação do Real x Dólar")
# plt.plot(x,y, c='b', mfc='b', marker='o')
# plt.show()

3
# import matplotlib.pyplot as plt
# import numpy as np

# cotação = np.array([3.15, 3.26, 3.88, 4.30, 5.33, 5.45, 5.39])
# anos = np.arange([2016,2023])
# plt.plot(anos, cotação, c='r', marker='o')
# plt.xlabel("Anos")
# plt.ylabel("Valor do Real (R$)")
# plt.title("Variação do Real x Dólar")
# plt.bar(x,y, color='b')
# plt.show()

4
# import matplotlib.pyplot as plt
# import numpy as np


# cotação = np.array([3.15, 3.26, 3.88, 4.30, 5.33, 5.45, 5.39])
# anos = np.array([2016, 2017, 2018, 2019, 2020, 2021, 2022])
# pib = np.array([8710.50, 9928.50, 9151.58, 8897.29, 6795.32, 7500.21, 7542.34])

# plt.subplot(2,1,1)
# plt.bar(anos, cotação, color='r')
# plt.xlabel("Anos")
# plt.ylabel("Valor do Dólar")
# plt.title("Cotação do Real x Dólar")

# plt.subplot(2,1,2)
# plt.bar(anos, pib, color='b')
# plt.xlabel("Anos")
# plt.ylabel("PIB")
# plt.title("PIB do Brasil")
# plt.tight_layout()
# plt.show()

5

# import matplotlib.pyplot as plt
# import numpy as np

# países = np.array(['China', 'EUA', 'UE', 'Outros'])
# cores = np.array(['r','g','b','y'])
# dados = np.array([30,40,20,10])
# offset = np.array([0.1,0.1,0.1,0.1]) #distância entre as partes do gráfico

# edge_props={'linewidth': 2, #definindo a largura da borda
#             'edgecolor': 'k', #definindo a cor da borda
#             'linestyle': 'solid' #definindo o estilo da borda
# } 

# text_props={
#     'color': 'k', #cor do texto
#     'size': 10, #tamanho do texto
#     'style': 'oblique' #estilo do texto
# } 

# plt.figure(figsize=(7,7))
# plt.pie(dados, labels=países, colors=cores, shadow=True, startangle=90, autopct='%1.1f%%',explode=offset, wedgeprops=edge_props, textprops=text_props)
# plt.title("Destino das Exportações Brasileiras")
# plt.legend(países, loc='best')
# plt.tight_layout()
# plt.show()

6
# import matplotlib.pyplot as plt
# import numpy as np

# plt.style.use('bmh')
# x = np.array([1.60,1.62,1.65,1.65,1.70,1.70,1.75,1.80,1.85,1.90,1.90,1.95,2.00])
# y = np.array([60,61,64,67,70,73,75,80,85,90,85,95,100])

# cores = np.array(['r','g','b','y','k','c','m','orange','purple','pink','brown','gray','olive'])
# plt.scatter(x,y, c=cores, marker='o')
# plt.title("Gráfico de Dispersão de Altura x Peso")
# plt.show()

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

import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0,19) #criando um array de 0 a 19
y = -x ** 4 #elevando o array ao quadrado

plt.xlabel("Eixo X") #adicionando o label no eixo x
plt.ylabel("Eixo Y") #adicionando o label no eixo y
plt.title("Gráfico da Função y = -x ** 4") #adicionando o título do gráfico
plt.plot(x, y, c='orange', lw='1.5', marker='o') #plotando o gráfico
plt.show() #mostrando o gráfico
+
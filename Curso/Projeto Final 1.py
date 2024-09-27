import matplotlib.pyplot as plt
from numpy import cov, std, var, mean, min, max, sqrt

class RegressaoLinear():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def correlacao(self):
        covariacao = cov(self.x, self.y, bias=True)[0][1]
        variancia_x = var(self.x)
        variancia_y = var(self.y)
        return covariacao / sqrt(variancia_x * variancia_y)
    
    def inclinacao(self):
        std_x = std(self.x)
        std_y = std(self.y)
        return self.correlacao() * (std_y / std_x)
    
    def interceptacao(self):
        media_x = mean(self.x)
        media_y = mean(self.y)
        return media_y - self.inclinacao() * media_x
    
    def previsao(self, valor):
        intercepta = self.interceptacao()
        return self.inclinacao() * valor + intercepta
    
    def PlotaRegressao(self, titulo="Regressão Linear", nome_x="Eixo X", nome_y="Eixo Y"):
        plt.xlabel(nome_x)
        plt.ylabel(nome_y)
        plt.title(titulo)
        plt.scatter(self.x, self.y)
        x_min = min(self.x)
        x_max = max(self.x)
        x_reta = [x_min, x_max]
        y_reta = [self.previsao(x_min), self.previsao(x_max)]
        plt.plot(x_reta, y_reta, color="red")
        plt.show()

# Dados
idade = [18, 23, 25, 33, 34, 43, 48, 51, 58, 63, 67]
custo = [871, 1100, 1393, 1654, 1915, 2100, 2356, 2698, 2959, 3000, 3100]

# Criação do modelo de regressão
regressao = RegressaoLinear(idade, custo)

# Previsão para a idade 54
prever = regressao.previsao(54)
print(f"Previsão para idade 54: {prever}")

regressao.PlotaRegressao("Plano de Saúde", "Idade", "Custo")

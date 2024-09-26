from sklearn import datasets
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt

# Carrega o dataset iris
iris = datasets.load_iris()
#print("dados:", iris.data)
#print("classes:", iris.target)
#print("nomes das classes:", iris.target_names)
#print("nomes das features:", iris.feature_names)

unicos, quantidade = np.unique(iris.target, return_counts=True)
#print(unicos, quantidade)

cluster = KMeans(n_clusters=3)
cluster.fit(iris.data)
agrupamento = cluster.labels_
#print(agrupamento)

resultados = confusion_matrix(iris.target, agrupamento)
# print(resultados)

acuracia = accuracy_score(iris.target, agrupamento)
# print(acuracia)

plt.scatter(iris.data[agrupamento == 0, 0], iris.data[agrupamento == 0, 1], c='green', label='Setosa')
plt.scatter(iris.data[agrupamento == 1, 0], iris.data[agrupamento == 1, 1], c='red', label='Versicolor')
plt.scatter(iris.data[agrupamento == 2, 0], iris.data[agrupamento == 2, 1], c='blue', label='Virginica')
plt.legend()
plt.show()

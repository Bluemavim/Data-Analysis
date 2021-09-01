# 10.Crear una matriz de 20x20 de valores aleatorios entre 1 y 100, luego indicar su media, 
# su mediana, su moda y el desvío estándar. 
# Los valores que den como resultado flotantes deben tener como máximo 2 decimales.
import numpy as np
from scipy import stats


matrix = np.random.randint(1,100, (20,20))
#print(matrix)

#Falta redondear
media= np.mean(matrix)

mediana = np.median(matrix)

moda = stats.mode(matrix)

desvio= np.std(matrix)

print("Media: ", round(media, 2))
print("Mediana: ", round(mediana, 2))
print("Moda: ", moda)
print("Desvío estándar:", round(desvio, 2))
#Encontrar los índices de los valores mínimos y máximos de la matriz creada en el ejercicio 3.
import numpy as np

matrix= np.arange(0,9).reshape(3,3)
print(matrix)

minimo = np.amin(matrix)
maximo = np.amax(matrix)

indice_minimo= np.where(matrix == minimo)
print(indice_minimo)
indice_maximo= np.where(matrix == maximo)
print(indice_maximo)



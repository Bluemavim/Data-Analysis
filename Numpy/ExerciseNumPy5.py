#Crear una matriz de identidad de 6x6:
import numpy as np


matriz_id = np.identity(6, dtype=np.int64) #Setear que sea para enteros porque por defecto son float
print(matriz_id)

#Alternative way:
matriz2 = np.eye(6)
print(matriz2)



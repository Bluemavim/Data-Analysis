#Crear una matriz de 10x10 con 1 en los bordes y 0 en el interior (con rangos de índices).
import numpy as np


matrix= np.ones((10,10))
matrix[1:-1, 1:-1] = 0
#Jugando:
#matrix[1:5, 1:5] = 0
print(matrix)
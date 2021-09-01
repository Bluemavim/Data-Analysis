#12.Crear una matriz de 4x4 de valores aleatorios entre 1 y 10, y luego agregarle una fila de 0s al final.
import numpy as np

np.random.seed(0)
matrix = np.random.randint(1,11, (4,4))
matrix = np.vstack([matrix, np.zeros(4)])
print(matrix)


#Alternativa:
matriz2 = np.append(matrix, [[0, 0, 0, 0]], axis=0)



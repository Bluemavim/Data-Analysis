# Ejercicio 3: Crear una matriz de 3x3 con los valores de 0 a 8:
import numpy as np

#One way:
matrix= np.arange(0,9).reshape(3,3)
print(matrix)


#Another way:
matriz_3por3 = np.array(([0, 1, 2],[3, 4, 5],[6, 7, 8]), dtype=np.int64)
print(matriz_3por3)




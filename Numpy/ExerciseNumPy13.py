#13.Crear dos arreglos de 6 elementos de valores aleatorios entre 0 y 1 y 
# luego realizar las operaciones lógicas and y or con los métodos de NumPy.
import numpy as np

array_1 = np.random.randint(6)
array_2 = np.random.randint(6)

print(np.logical_and(array_1, array_2))
print(np.logical_or(array_1, array_2))
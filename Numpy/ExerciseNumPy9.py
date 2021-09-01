#Crear dos arreglos al azar A y B, verificar si son iguales.
import numpy as np


array_1 = np.random.random((5,5))
array_2 = np.random.random((2,6))
print(np.array_equal(array_1, array_2))
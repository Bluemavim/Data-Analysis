#Crear dos arreglos de 4 elementos enteros y hacer las siguientes operaciones: 
# sumarlos, restarle el segundo al primero, multiplicarlos, 
#  el primero por el segundo. Hacerlo utilizando métodos.
import numpy as np

np.random.seed(0) #que quede guardado el iterable de la primera ejecución

array_1 = np.random.randint(1,20,4)
array_2 = np.random.randint(1,20,4)
print("SUMA:", np.add(array_1, array_2))
print("RESTA:", np.subtract(array_2, array_1))
print("MULTIPLICACIÓN", np.multiply(array_1, array_2))
print("DIVISIÓN", np.divide(array_1, array_2))
#14.Crear un arreglo de 4 elementos de entre 0 y 10, informar la cantidad 
# de elementos que tiene y también cuántos bytes ocupa el arreglo.
import numpy as np

array_1 = np.random.randint(0,10,4)
print("Cantidad de elementos: ", array_1.size) 
print("El espacio que ocupa el arreglo es de:", array_1.nbytes, "bytes")  #Permite saber cuánto espacio ocupa el arreglo.
#print(array_1.itemsize)


#Es importante saber esto para estimar cuánto tiempo nos puede llevar un modelo.


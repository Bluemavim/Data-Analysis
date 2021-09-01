#Encontrar los índices que no son ceros del arreglo [1,2,4,2,4,0,1,0,0,0,12,4,5,6,7,0].
import numpy as np

numeros = [1,2,4,2,4,0,1,0,0,0,12,4,5,6,7,0]
arreglo = np.array(numeros)
print(np.nonzero(numeros))


#Other way using list comprehension:
indices_de_ceros = [index for index in range(len(arreglo)) if arreglo[index]!= 0]
print(indices_de_ceros)

#Alternative method:
print(np.where(arreglo != 0 ))


#Extra1: We can count the total amount of numbers which are not zero:
print(np.count_nonzero(arreglo))

#Extra2: Using Boolean Masking
print(np.equal(arreglo,0))
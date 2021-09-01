#2 Invertir el vector creado en el ejercicio 1
import numpy as np


vector1= np.arange(10,50)
vector2 = np.flip(vector1)
print(vector2)


#An alternative way using array[::-1]:
vector3= (vector1[::-1])
print(vector3)


#Another way:
vector4= np.arange(49, 9, -1)
print(vector3)
#Crear una matriz de 5x5 con valores en los renglones que vayan de 0 a 4. 
#VER TILE // VER BROADCAST
import numpy as np


matriz5x5 = np.arange(0, 5) 
matriz5x5_vers2 = np.broadcast_to(matriz5x5, (5, 5))
#print(matriz5x5_vers2)


#Otra versión usando TILE: Construct an array by repeating A the number of times given by reps.
matriz5x5_v1 = np.tile(np.arange(0,5), 5).reshape(5,5)
print(matriz5x5_v1)


#BROADCAST: Broadcast an array to a new shape


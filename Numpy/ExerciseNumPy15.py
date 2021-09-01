#15.Crear una matriz que contenga información en distintos formatos, 
# imprimir la info de cada formato a través del atributo.

import numpy as np

estudiantes = np.zeros(5, dtype= {'nombres': ('nombre', 'order', 'modalidad', 'promedio'), 'formats': ('U24', 'i4', 'U24', 'f8')})

nombres= ["María", "Juan", "Aldana", "Pablo", "Joaquín"]
#localidad= ['Banfield', 'Turdera', 'Temperley', 'Lanús', 'CABA']
modalidad= ['Arte', 'Naturales', 'Arte', 'Economía', 'Idiomas']
promedio= [8.37, 7.25, 9.21, 6.25, 7.8]
order = list(range(5))


estudiantes[nombres]= nombres
#estudiantes[localidad]= localidad
estudiantes[modalidad]= modalidad
estudiantes[promedio]= promedio


print(estudiantes)
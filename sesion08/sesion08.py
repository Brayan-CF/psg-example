# ESTRUCTURA DE DATOS
# tupla

# tubla inmutable
'''
tupla = (1,2,3)
tupla[0] = 4 # Error'''

# tubla ordenad
'''
tupla1 = (1,2,3)
tupla2 = (3,2,1)
print (tupla1 == tupla2) # False'''

# tubla indexada
'''
tupla = (1,2,3)
tupla[0] # 1
tupla[1] # 2
tupla[2] # 3'''

''''
# tupla usado para: empaquetamiento y desempaquetamiento.
coordenadas = (3,5)
x,y = coordenadas
# '' : enviar y devolver multiples valores de la funcion
def coordenadas(coordenada):
    x,y = coordenada
    x = x + 1
    y = y + 1
    return (x,y)
# ``: en diccionarios 
agenda = {('Juan','Perez'): 1234567}
# ``: almacenar cualquier dato.
tupla = (1,2.0,'hola',True)'''

# para declarar una tupla
'''
mi_tupla = (elemento1, elemento2, elemento3, ...)'''

# tupla de enteros
'''
print ("Tupla de enteros")
enteros = (1,2,3,4,5,6)
print (enteros)
print (type(enteros))'''

# tupla de cadeas
'''
print ("Tupla de cadenas")
cadenas = ("hola", "mundo", "desde", "python")
print (cadenas)
print (type(cadenas))'''

# tupla mixta
'''
print ("Tupla Mixta") 
mixta = (1, "hola", True, 2.5)
print (mixta)
print (type(mixta))'''

# tupla vacia
'''
print("tupla vacia")
vacia = ()
print(vacia)
print(type(vacia))'''

# tupla con un solo elemento
'''
print(" tupla con un solo elemento")
uno = (1,)
print(uno)
print(type(uno))'''

# TUPLA - FUNCION tuple()
# tupla de una cadena
'''
print("tupla utiliazando la funcion tuple()")
constructor = tuple("hola")
print(constructor)
print(type(constructor))'''

# INDEXACION Y SLICING
# para  indices positivos
'''
print("inexacion positiva de la tupla")
tupla = (1,2.0, "hola", True)
print(tupla[0], type(tupla[0]))
print(tupla[1], type(tupla[1]))
print(tupla[2], type(tupla[2]))
print(tupla[3], type(tupla[3]))'''

# para aceder de forma neativa de derecha a izquierda
'''
print ("Indexado negativo de una tupla")
tupla = (1,2.0, "hola", True)
print (tupla[-1], type(tupla[-1]))
print (tupla[-2], type(tupla[-2]))
print (tupla[-3], type(tupla[-3]))
print (tupla[-4], type(tupla[-4]))'''

# Slicing de una tupla
'''
print ("Slicing de una tupla")
tupla = (0,1,2,3,4,5,6,7,8,9,10)
print (tupla)
sub_tupla = tupla[0:5]
print (sub_tupla)
print (type(sub_tupla))'''

# Slicing con paso positivo
'''
print ("Slicing de una tupla con saltos")
tupla = (0,1,2,3,4,5,6,7,8,9,10)
print (tupla)
sub_tupla = tupla[0:10:2]
print (sub_tupla)
print (type(sub_tupla))'''

# slicing con paso negativo
'''
print ("Slicing de una tupla con saltos negativos")
tupla = (0,1,2,3,4,5,6,7,8,9,10)
print (tupla)
sub_tupla = tupla[7:2:-2]
print (sub_tupla)
print (type(sub_tupla))'''

# CONCATENACION DE TUPLAS
# concatenacion de tuplas
'''
print ("Concatenación de tuplas")
tupla1 = (1,2,3)
tupla2 = (4,5,6)
concatenar = tupla1 + tupla2
print (tupla1, tupla2)
print (concatenar)
print (type(concatenar))'''

# repeticiones de tuplas
'''
print ("Repetición de tuplas")
tupla = (1,2,3)
repetir = tupla * 3
print (tupla)
print (repetir)
print (type(repetir))'''

# Asignacion multiple de valores
'''
print ("Asignación múltiple")
persona = ("Jhon", "Doe", 22, 1.75)
nombre, apellido, edad, estatura = persona
print (persona)
print (nombre)
print (apellido)
print (edad)
print (estatura)'''

# Metodos de tuplas: .count y .index
# index()
'''
print ("Método index(valor)")
tupla = (1,2.0, "hola", True)
print (tupla.index(1))
print (tupla.index("hola"))'''


# count()
'''
print ("Método count(valor)")
tupla = (1, 2.0, "hola", False, "hola", "HOLA")
print (tupla.count(1))
print (tupla.count("hola"))
print (tupla.count(10))'''

# FUNCIONES CON TUPLAS
# len()
'''
print ("Función len()")
tupla = (1,2.0, "hola", True)
longitud = len(tupla)
print (tupla)
print (longitud)'''

# max()
'''
print ("Función max()")
tupla = (1,2,10,5,8,0)
maximo = max(tupla)
print (tupla)
print (maximo)'''

# min()
'''
print ("Función min()")
tupla = ("a","z","c","b","f","d")
minimo = min(tupla)
print (tupla)
print (minimo)'''

# sum()
'''
print ("Función sum()")
tupla = (1.0, 0.5, 2.5, 3.1)
suma = sum(tupla)
print (tupla)
print (suma)'''

# tuplas anidadas
'''
print ("Tuplas anidadas")
tupla = (1,2,3, (4,5,6))
print (tupla)
print (tupla, type(tupla))
print (tupla[3], type(tupla[3]))
print (tupla[3][1], type(tupla[3][1]))'''

# anidado con detalle
print ("Tuplas anidadas")
tupla = (1,2,3, (4,5,6))
print (tupla, type(tupla))
anidado = tupla[3]
print (anidado, type(anidado))
valor_anidado_0 = anidado[0]
print (valor_anidado_0, type(valor_anidado_0))
valor_anidado_1 = tupla[3][1]
print (valor_anidado_1, type(valor_anidado_1))
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
print("tupla utiliazando la funcion tuple()")
constructor = tuple("hola")
print(constructor)
print(type(constructor))

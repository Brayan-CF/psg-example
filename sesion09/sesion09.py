# ESTRUCTURA D DATOS
# Listas, mutables, ordenados y indexads
# mutables
'''
lista = [1,2,3]
lista[0] = 4 
print (lista) # [4,2,3]'''
# ordenada
'''
lista1 = [1,2,3]
lista2 = [3,2,1]
print (lista1 == lista2) # False'''
# indexada
'''
lista = [1,2,3]
lista[0] # 1
lista[1] # 2
lista[2] # 3'''
# como declarar una lista
''' # tambien usamos la funcion list()
lista = [elemento1, elemento2, elemento3, ...]'''
# lista d entros
'''
print ("Lista de enteros")
mi_lista = [1,2,3,4,5]
print (mi_lista)'''
# lista de cadenas 
'''
print ("Lista de cadenas")
mi_lista = ["hola", "mundo", "haskell"]
print (mi_lista)
'''
# lista mixta 
'''
print ("Lista mixta")
mi_lista = [1, "hola", 3.14, "mundo", 5]
print (mi_lista)'''
# lista vacia
'''
print ("Lista vacía")
mi_lista = []
print (mi_lista)'''
# lista apartir de una cadena
'''
print ("Lista a partir de una cadena")
mi_lista = list("hola mundo")
print (mi_lista)'''
# lista apartir de tupla
'''
print ("Lista a partir de una tupla")
mi_tupla = (1,2,3,4,5)
print (mi_tupla)
mi_lista = list(mi_tupla)
print (mi_lista)'''
#  lista por comprencion
'''
print ("Lista por comprensión")
mi_lista = [x for x in range(21)]
print (mi_lista)'''

# Indexacion y Slicing
# acceso a indice positivo
'''
print ("Indexación positivo de una lista")
lista = [1, "hola", 3.14, (1,2)]
print (lista[0], type(lista[0])) 
print (lista[1], type(lista[1])) 
print (lista[2], type(lista[2])) 
print (lista[3], type(lista[3])) '''
# acceso a inice negativo
'''
print ("Indexación negativo de una lista")
lista = [1, "hola", 3.14, (1,2)]
print (lista[-1], type(lista[-1]))
print (lista[-2], type(lista[-2]))
print (lista[-3], type(lista[-3]))
print (lista[-4], type(lista[-4]))'''
# modificacion de valores riginales
'''
print ("Modificación de una lista")
lista = [1, "hola", 3.14, (1,2)]
print (lista)
lista[0] = 2
lista[1] = "mundo"
print (lista)'''
# slicing de una lista
'''
print ("Slicing de una lista")
lista = ["P", "y", "t", "h", "o", "n", "L", "a", "P", "a", "z"]
print (lista)
sub_lista = lista[2:7]
print (sub_lista)
print (type(sub_lista))'''
# slicing con positivo
'''
print ("Slicing con paso positivo")
lista = ["P", "y", "t", "h", "o", "n", "L", "a", "P", "a", "z"]
print (lista)
sub_lista = lista[0:9:3]
print (sub_lista)'''
# slicing con negativp
'''
print ("Slicing con paso negativo")
lista = ["P", "y", "t", "h", "o", "n", "L", "a", "P", "a", "z"]
print (lista)
sub_lista = lista[8:2:-4]
print (sub_lista)'''
# slicingn con negatico con paso negativo
'''
print ("Slicing negativo con paso negativo")
lista = ["P", "y", "t", "h", "o", "n", "L", "a", "P", "a", "z"]
print (lista)
sub_lista = lista[-1:-8:-2]
print (sub_lista)'''
# slicing negativo con paso positivo
'''
print ("Slicing negativo con paso positivo")
lista = ["P", "y", "t", "h", "o", "n", "L", "a", "P", "a", "z"]
print (lista)
sub_lista = lista[-8:-1:2]
print (sub_lista)'''

# Concatenacion de Listas
'''
print ("Concatenación de listas")
lista1 = [1,2,3]
lista2 = ["a","b","c"]
concatenar = lista1 + lista2
print (lista1, lista2)
print (concatenar)
print (type(concatenar))'''
# repeticion de listas
'''
print ("Repetición de listas")
lista = [True, False]
repetir = lista * 3
print (lista)
print (repetir)
print (type(repetir))'''

# Metodos de las Listas
# index(valor)
'''
print ("Método index(valor)")
lista = [1,True,3.14,"hola",5]
valor = "hola"
print (valor, lista.index(valor))
valor = 3.14
print (valor, lista.index(valor))'''
#count(valor)
'''
print ("Método count(valor)")
lista = [1,True,3.14,"hola",5, True, True, 3.140]
valor = True
print (valor, lista.count(valor))
valor = 3.14
print (valor, lista.count(valor))'''

# Metodos de adicion
# insert(i, valor)
'''
print ("Método insert(i, valor)")
lista = [1,2,3,4,5]
print (lista)
lista.insert(2, "OwO")
print (lista)'''
# append(valor)
'''
print ("Método append(valor)")
lista = [1,2,3,4,5]
print (lista)
lista.append("(OwO=)")
print (lista)'''
# extend(iterable)
'''
print ("Método extend(iterable)")
lista = [1,2,3]
print (lista)
lista.extend(":3")
print (lista)
lista.extend(["(¬_¬ )", "(O_O=)"])
print (lista)
lista.extend(("😅", "😎"))
print (lista)'''

# Metodos de eliminacion
# remove(valor), eleiminado solo la primera aparicion
'''
print ("Método remove(valor)")
lista = [1,2,"UwU",4,5, "UwU"]
print (lista)
lista.remove("UwU")
print (lista)'''
# pop(i) o pop(), elimina el eelnto de dicha posicion
'''
print ("Método pop(i)")
lista = ["OwO",3,"UwU",5]
print (lista)
lista.pop(1)
print (lista)
print ("Método pop()")
lista.pop()
print (lista)'''
# clear(), eleimina toda la lista dejando la vacia.
'''
print ("Método clear()")
lista = ["ewe","OwO","UwU"]
print (lista)
lista.clear()
print (lista)'''

# Metodos de Ordenamiento
# sort(), ordena de menor a mayor
'''
print ("Método sort()")
lista = [3,1,5,2,4]
print (lista)
lista.sort()
print (lista)'''
# sort(reverse=true), de mayor a menor
'''
print ("Método sort()")
lista = [3,1,5,2,4]
print (lista)
lista.sort(reverse=True)
print (lista)'''
# reverse(), invierte el orden
'''
print ("Método reverse()")
lista = [3,1,5,2,4]
print (lista)
lista.reverse()
print (lista)'''

# Metodos de Copia
'''
print ("Asignación de lista")
lista = [1,2,3,4,5]
print (lista)
copia = lista
copia[0] = 6
print (copia)
print (lista)'''
# copy() o slicing[:], para crear una copia de la liista
'''
print ("Método copia con slicing")
lista = [1,2,3,4,5]
print (lista)
copia = lista[:]
copia[0] = 6
print (copia)
print (lista)'''

'''
print ("Método copy()")
lista = [3,1,5,2,4]
print (lista)
copia = lista.copy()
print (copia)
print (copia == lista)'''
# metodo de copia 
'''
print ("Método copia con slicing")
lista = [1,2,3,4,5]
print (lista)
copia = lista.copy()
copia[0] = 6
print (copia)
print (lista)'''

# Funciones con las Listas
# len(), devuelve la longitud
'''
print ("Función len()")
lista = [1,True,3.14,"🐍",5]
print (lista)
print (len(lista))'''
# max(), devuelve el valor maximo oelemento
'''
print ("Función max()")
lista = [1,2,3,4,5]
print (lista)
print (max(lista))
lista = ["a","b","c","d","e"]
print (lista)
print (max(lista))'''
# min(), devuelve el valor minimo de la lista o elemnto
'''
print ("Función min()")
lista = [1,2,3,4,5]
print (lista)
print (min(lista))
lista = ["a","b","c","d","e"]
print (lista)
print (min(lista))'''
# sum(), devuelve la suma de los elemntos de la lista
'''
print ("Función sum()")
lista = [1,2,3,4,5]
print (lista)
print (sum(lista))'''

# Comparacion de Listas
# in, not in, (para si contine algo en especifico)
'''
print ("Comparación de listas")
lista = [1,2,3,4,5]
print (lista)
print (3 in lista)
print (6 in lista)
print (3 not in lista)
print (6 not in lista)
print ([1,2,3] in lista)'''
# is, is not, (para comparar soi son la misma lista)
print ("Comparación de listas")
lista1 = [1,2,3,4,5]
lista2 = [1,2,3,4,5]
lista3 = [1,2]
print (lista1, lista2, lista3)
print (lista1 is lista2)
print (lista1 is not lista2)
print (lista3 is lista1)
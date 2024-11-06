# ESTRUCTURA DE DATOS

# Confuntos, no ordenados, no indexados, no duplicados
# mutables
'''
conjunto = {'🍕','🍔','🍟','🌭'}
print(conjunto) # {'🍔', '🌭', '🍕', '🍟'}
conjunto.add('🥗')
print(conjunto)  # {'🍔', '🍕', '🥗', '🍟', '🌭'}'''
# no ordenados
'''
conjunto = {'🍕','🍔','🍟','🌭'}
print(conjunto) # {'🍔', '🌭', '🍕', '🍟'}'''
# no indexados
'''
conjunto = {'🍕','🍔','🍟','🌭'}
print(conjunto[0]) # TypeError: 'set' object is not subscriptable'''
# no duplicados
'''
conjunto = {'🍕','🍔','🍟','🌭','🍕','🍟'}
print(conjunto) # {'🍕', '🍟', '🌭', '🍔'}'''

# declaracion de un confunto, {} o set()
'''mi_conjunto = {elemento1, elemento2, elemento3, ...}'''
# conjunto de enteros
'''
print ("Conjunto de enteros")
conjunto = {1, 2, 3, 4, 5}
print(conjunto) 
print(type(conjunto))'''
#conjunto de cadenas
'''
print ("Conjunto de cadenas")
conjunto = {'🍕','🍔','🍟','🌭'}
print(conjunto)
print(type(conjunto))
'''
# conjunto mixto
'''
print ("Conjunto mixto")
conjunto = {1, True, 3.14, '☕'}
print(conjunto)
print(type(conjunto))
'''
# conjunto vacio
'''
print ("Conjunto vacío")
conjunto = set()
print(conjunto)
print(type(conjunto))
'''
# conjunto apartir de una cadena
'''
print ("Conjunto a partir de la cadena")
cadena = 'Hola Mundo'
conjunto = set(cadena)
print(conjunto)
print(type(conjunto))
'''
# conjunto apartir de una tupla
'''
print ("Conjunto a partir de una tupla")
tupla = (1, 2, 3, 4, 5, 5)
conjunto = set(tupla)
print(conjunto)
print(type(conjunto))
'''
# conjunto apartir de una lista
'''
print ("Conjunto a partir de una lista")
lista = [True, False, 0, 1]
conjunto = set(lista)
print(conjunto)
print(type(conjunto))
'''
# conjunto por comprencion
'''
print ("Conjunto por comprensión")
conjunto = {x for x in '🍕🍔🍟🍕🍔🍟🍔🍟'}
print(conjunto)
print(type(conjunto))
'''

# Indexacion y Slicing
# los conjuntos no soparttan nada de indexacion ni slicing

# Concatenacion de conjuntos
# los conjntos no soportan concatenacion por el operador +

# repeticion de conjuntos
# Los conjuntos no soportan la repetición con el operador *

# Metodos de los congjuntos
# metodo de adicion: add y update
# add(valor), solo recive uno
'''
print ("Método add()")
conjunto = {'🍕','🍔','🍟','🌭'}
print (conjunto)
conjunto.add('🥗')
print(conjunto) 
'''
# update(valores), recive una secuencia
'''
print ("Método update()")
conjunto = {'🍕','🍔','🍟','🌭'}
print (conjunto)
conjunto.update(['🥤','🍦'])
print(conjunto) 
conjunto.update('🍩🍪')
print(conjunto) 
conjunto.update(('🍫','🍬'))
print(conjunto)
conjunto.update({'🍭','🍮'})
print(conjunto)
'''
# metodo de eleiminacion: remove, discard, pop , clear
# remove(valor)
'''
print ("Método remove()")
conjunto = {'🍕','🍔','🍟','🌭'} 
print (conjunto)
conjunto.remove('🍔')
print(conjunto)
# conjunto.remove('🍔')
# print(conjunto)
# Key Error: '🍔'
'''
# discard(valor)
'''
print ("Método discard()")
conjunto = {'🍕','🍔','🍟','🌭'}
print (conjunto)
conjunto.discard('🍔')
print(conjunto)'''
# pop(), elimana un elemento aleatorio y lo retorna
'''
print ("Método pop()")
conjunto = {'🍕','🍔','🍟','🌭', '🥤','🍦'}
print (conjunto)
print(conjunto.pop())
print(conjunto)
print(conjunto.pop())
print(conjunto)
'''
# clear(), eleimina todo
'''
print ("Método clear()")
conjunto = {'🍕','🍔','🍟','🌭'}
print (conjunto)
conjunto.clear()
print(conjunto)
'''

# Metodos de operaciones con conjuntos:
# union, intersection, diffrerence, symmetric_diffrerence
# union(conjunto)
'''
print ("Método union()")
conjunto1 = {'🍔','🍟', '🥤'}
conjunto2 = {'🍕','🍨','🥤'}
print (conjunto1, conjunto2)
union = conjunto1.union(conjunto2)
print(union)
'''
# intersection(conjunto), que contiene los elementos que estan en ambos conuuntos
'''
print ("Método intersection()")
conjunto1 = {'🍔','🍟', '🥤'}
conjunto2 = {'🍕','🍨','🥤'}
print (conjunto1, conjunto2)
interseccion = conjunto1.intersection(conjunto2)
print(interseccion)
'''
# difference(conjunto), devuelve la diferencia entre ambos conjuntos
'''
print ("Método difference()")
conjunto1 = {'🍔','🍟', '🥤'}
conjunto2 = {'🍕','🍨','🥤'}
print ("1:",conjunto1, "2:",conjunto2)
diferencia = conjunto1.difference(conjunto2)
print("1 y 2:",diferencia)
diferencia = conjunto2.difference(conjunto1)
print("2 y 1:",diferencia)
'''
# symmetric_difference(conjunto), reorna diferencia simetrica
'''
print ("Método symmetric_difference()")
conjunto1 = {'🍔','🍟', '🥤'}
conjunto2 = {'🍕','🍨','🥤'}
print (conjunto1, conjunto2)
diferencia_simetrica = conjunto1.symmetric_difference(conjunto2)
print(diferencia_simetrica)
'''

# Metodos de asiignacion con operaciones:
# intersection_update(conjunto)
'''
print ("Método intersection_update()")
conjunto1 = {'🍔','🍟', '🥤'}
conjunto2 = {'🍕','🍨','🥤'}
print (conjunto1, conjunto2)
conjunto1.intersection_update(conjunto2)
print(conjunto1)
'''
# difference_update(conjunto)
'''
print ("Método difference_update()")
conjunto1 = {'🍔','🍟', '🥤'}
conjunto2 = {'🍕','🍨','🥤'}
print ("1:",conjunto1, "2:",conjunto2)
conjunto1.difference_update(conjunto2)
print ("1:",conjunto1, "2:",conjunto2)
'''
# symmetric_difference_update(confuntp)
'''
print ("Método symmetric_difference_update()")
conjunto1 = {'🍔','🍟', '🥤'}
conjunto2 = {'🍕','🍨','🥤'}
print (conjunto1, conjunto2)
conjunto1.symmetric_difference_update(conjunto2)
print(conjunto1)
'''

# Metodo de busqueda:
# issubset()
'''
print ("Método issubset()")
conjunto1 = {'🍔','🍟', '🥤'}
conjunto2 = {'🍕','🍨','🥤'}
conjunto3 = {'🍔','🍟'}
print (conjunto1, conjunto2,conjunto3)
# ¿El conjunto1 es subconjunto del conjunto2?
print(conjunto1.issubset(conjunto2))
# ¿El conjunto3 es subconjunto del conjunto1?
print(conjunto3.issubset(conjunto1))
'''
# issuperset(conjunto)
'''
print ("Método issuperset()")
conjunto1 = {'🍔','🍟', '🥤'}
conjunto2 = {'🍕','🍨','🥤'}
conjunto3 = {'🍔','🍟'}
print (conjunto1, conjunto2,conjunto3)
# ¿El conjunto1 es superconjunto del conjunto2?
print(conjunto1.issuperset(conjunto2)) # C1 contiene a C2?
# ¿El conjunto1 es superconjunto del conjunto3?
print(conjunto1.issuperset(conjunto3)) # C1 contiene a C3?
'''
# isdisjoint(conjunto)
'''
print ("Método isdisjoint()")
conjunto1 = {'🍔','🍟', '🥤'}
conjunto2 = {'🍕','🍨'}
conjunto3 = {'🍔','🍟'}
print (conjunto1, conjunto2,conjunto3)
# ¿El conjunto1 no tiene elementos en común con el conjunto2?
print(conjunto1.isdisjoint(conjunto2))
# ¿El conjunto1 no tiene elementos en común con el conjunto3?
print(conjunto1.isdisjoint(conjunto3))
'''

# Metodos de copia
# cppy()
'''
print ("Método copy()")
conjunto = {'🍕','🍔','🍟','🌭'}
print (conjunto)
copia = conjunto.copy()
copia.add('🥗')
print(conjunto)
print(copia)
'''

# Funciones con conjuntos
# len()
'''
print ("Función len()")
conjunto = {'🍕','🍔','🍟','🌭'}
print (conjunto)
print(len(conjunto))
'''
# max()
'''
print ("Función max()")
conjunto = {1, 2, 3, 4, 5}
print (conjunto)
print (max(conjunto))
conjunto = {'🍕','🍔','🍟','🌭'}
print (conjunto)
print(max(conjunto))
'''
# min()
'''
print ("Función min()")
conjunto = {1, 2, 3, 4, 5}
print (conjunto)
print (min(conjunto))
conjunto = {'🍨','🍔','🍟','🍕'}
print (conjunto)
print(min(conjunto))
'''
# sum(), solo con numeros
'''
print ("Función sum()")
conjunto = {1, 2, 3, 4, 5}
print (conjunto)
print (sum(conjunto))
'''

# Operadores con conjuntos
# operadores de adicion
# |= 
'''
print ("Operador |=")
conjunto1 = {'🍔','🍟', '🥤'}
conjunto2 = {'🍕','🍨'}
print (conjunto1, conjunto2)
conjunto1 |= conjunto2
print(conjunto1)
'''
# operadores de comparacion
# ==
'''
print ("Operador ==")
conjunto1 = {'🍔','🍟', '🥤'}
conjunto2 = {'🍔','🍟', '🥤'}
conjunto3 = {'🍕','🍨'}
print (conjunto1, conjunto2, conjunto3)
print(conjunto1 == conjunto2)
print(conjunto1 == conjunto3)
'''
# "!="
'''
print ("Operador !=")
conjunto1 = {'🍔','🍟', '🥤'}
conjunto2 = {'🍔','🍟', '🥤'}
conjunto3 = {'🍕','🍨'}
print (conjunto1, conjunto2, conjunto3)
print(conjunto1 != conjunto2)
print(conjunto1 != conjunto3)
'''
# <
'''
print ("Operador <")
conjunto1 = {'🍔','🍟'}
conjunto2 = {'🍔','🍟', '🥤'}
conjunto3 = {'🍕','🍨'}
print (conjunto1, conjunto2, conjunto3)
print(conjunto1 < conjunto2)
print(conjunto1 < conjunto3)
'''
# >
'''
print ("Operador >")
conjunto1 = {'🍔','🍟','🥤','🍕'}
conjunto2 = {'🍔','🍟', '🥤'}
conjunto3 = {'🍕','🍨'}
print (conjunto1, conjunto2, conjunto3)
print(conjunto1 > conjunto2)
print(conjunto1 > conjunto3)
'''
# <=
'''
print ("Operador <=")
conjunto1 = {'🍔','🍟'}
conjunto2 = {'🍔','🍟'}
conjunto3 = {'🍕','🍨'}
print (conjunto1, conjunto2, conjunto3)
print(conjunto1 <= conjunto2)
print(conjunto1 <= conjunto3)
'''
# >=
'''
print ("Operador >=")
conjunto1 = {'🍔','🍟'}
conjunto2 = {'🍔','🍟'}
conjunto3 = {'🍕','🍨'}
print (conjunto1, conjunto2, conjunto3)
print(conjunto1 >= conjunto2)
print(conjunto1 >= conjunto3)
'''
# operadores para operaciones con conjuntos
# | : union
'''
print ("Operador |")
conjunto1 = {'🍔','🍟', '🥤'}
conjunto2 = {'🍕','🍨','🥤'}
print (conjunto1, conjunto2)
union = conjunto1 | conjunto2
print(union)
'''
# & : intersecion
'''
print ("Operador &")
conjunto1 = {'🍔','🍟', '🥤'}
conjunto2 = {'🍕','🍨','🥤'}
print (conjunto1, conjunto2)
interseccion = conjunto1 & conjunto2
print(interseccion)
'''
# - : diferencia
'''
print ("Operador -")
conjunto1 = {'🍔','🍟', '🥤'}
conjunto2 = {'🍕','🍨','🥤'}
print ("1:",conjunto1, "2:",conjunto2)
diferencia = conjunto1 - conjunto2
print("1 - 2:",diferencia)
diferencia = conjunto2 - conjunto1
print("2 - 1:",diferencia)
'''
# ^ : diferecnia simetrica
'''
print ("Operador ^")
conjunto1 = {'🍔','🍟', '🥤'}
conjunto2 = {'🍕','🍨','🥤'}
print (conjunto1, conjunto2)
diferencia_simetrica = conjunto1 ^ conjunto2
print(diferencia_simetrica)
'''

# Operaciones para asignacion con operadores
# |=
'''
print ("Operador |= Unión")
conjunto1 = {'🍔','🍟', '🥤'}
conjunto2 = {'🍕','🍨','🥤'}
print (conjunto1, conjunto2)
conjunto1 |= conjunto2
print(conjunto1)
'''
# &=
'''
print ("Operador &= Intersección")
conjunto1 = {'🍔','🍟', '🥤'}
conjunto2 = {'🍕','🍨','🥤'}
print (conjunto1, conjunto2)
conjunto1 &= conjunto2
print(conjunto1)
'''
# -=
'''
print ("Operador -= Diferencia")
conjunto1 = {'🍔','🍟', '🥤'}
conjunto2 = {'🍕','🍨','🥤'}
print ("1:",conjunto1, "2:",conjunto2)
conjunto1 -= conjunto2
print("1 - 2:",conjunto1)
conjunto1 = {'🍔','🍟', '🥤'}
conjunto2 -= conjunto1
print("2 - 1:",conjunto2)
'''
# ^=
'''
print ("Operador ^= Diferencia simétrica")
conjunto1 = {'🍔','🍟', '🥤'}
conjunto2 = {'🍕','🍨','🥤'}
print (conjunto1, conjunto2)
conjunto1 ^= conjunto2
print(conjunto1)
'''

# Conjuntos Inmutables
# para python usamos frozenset()
'''
conjunto = frozenset({'🍔','🍕','🥗','🍟','🌭'})
print(conjunto)
print(type(conjunto))
'''

# Conjuntos anidados, tiene que ser inmutables
'''
print ("Conjunto de conjuntos")
conjunto = {frozenset({'🍅','🍓','🍎'}), frozenset({'🍈','🍐','🍏'})}
print(conjunto)
print(type(conjunto))
'''
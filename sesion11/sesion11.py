# ESTRUCTURA DE DATOS

# Diccionarios
# mutables
'''
diccionario = {'perro': '🐶', 'gato': '🐱', 'ave': '🐦'}
print(diccionario) # {'perro': '🐶', 'gato': '🐱', 'ave': '🐦'}
diccionario['perro'] = '🐩'
print(diccionario) # {'perro': '🐩', 'gato': '🐱', 'ave': '🐦'}
'''
# ordenados
'''
diccionario = {'perro': '🐶', 'gato': '🐱', 'ave': '🐦'}
print(diccionario) # {'perro': '🐶', 'gato': '🐱', 'ave': '🐦'}
'''
# indexados por clave
'''
diccionario = {'perro': '🐶', 'gato': '🐱', 'ave': '🐦'}
print(diccionario['perro']) # 🐶
print(diccionario['gato']) # 🐱
'''
# reescribe duplicados: los diccionarios no permiten claves duplocadaas
'''
diccionario = {'perro': '🐶', 'gato': '🐱', 'ave': '🐦', 'perro': '🐩'}
print(diccionario) # {'perro': '🐩', 'gato': '🐱', 'ave': '🐦'}
'''

# Como declarar un diccionario ( clave: valor) o usamos dict()
'''
mi_diccionario = {'clave1': 'valor1', 
                  'clave2': 'valor2', 
                  'clave3': 'valor3', ... }
'''
# diccionario de clave entero y valor entero
'''
print ("Diccionario de clave entera y valor entero")
diccionario = {1: 10, 2: 20, 3: 30}
print(diccionario)
print(type(diccionario))
'''
# diccionario de clave entero y valor cadena
'''
print ("Diccionario de clave entero y valor cadena")
diccionario = {1: 'uno', 2: 'dos', 3: 'tres'}
print(diccionario)
print(type(diccionario))
'''
# diccionario de clave cadena y valor entero
'''
print ("Diccionario de clave cadena y valor entero")
diccionario = {'uno': 1, 'dos': 2, 'tres': 3}
print(diccionario)
print(type(diccionario))
'''
# diccionario de clave cadena y valor cadena
'''
print ("Diccionario de clave cadena y valor cadena")
diccionario = {'perro': '🐶', 'gato': '🐱', 'ave': '🐦'}
print(diccionario)
print(type(diccionario))
'''
# diccionario mixto --- CONTINUAMOS AQUI -----
'''
print ("Diccionario mixto")
diccionario = {1:"ID-XXXXX", "edad": 3, 'animal': '🐶' , ("John","Doe"): 6917222722, "salvaje": False}
print(diccionario)
print(type(diccionario))
'''
# diccionario vacio
'''
print ("Diccionario vacío")
diccionario = {}
print(diccionario)
print(type(diccionario))
diccionario = dict()
print(diccionario)
print(type(diccionario))
'''

# diccionario a partir de unna lista anidada
'''
print ("Diccionario a partir de una lista")
lista = [['perro', '🐶'] , ['gato','🐱'] , ['ave','🐦']]
print(lista)
diccionario = dict(lista)
print(diccionario)
print(type(diccionario))
'''
# diccionario apartid de una tupla
'''
print ("Diccionario a partir de una tupla de tuplas")
tupla = (('perro', '🐶') , ('gatos','🐱') , ('ave',['🐦','🦅']))
print(tupla)
diccionario = dict(tupla)
print(diccionario)
print(type(diccionario))
'''
# diccionario mediante compresion
'''
print ("Diccionario mediante comprensión")
diccionario = {animal:animal*3 for animal in '🐶🐱🐹🐰'}
print(diccionario)
print(type(diccionario))
'''

# Indexacion y Slicing, nose puede sealizar slicing en un diccionario
'''
print ("Acceder mediante clave")
diccionario = {'perro': '🐶', 'gato': '🐱', 'ave': '🐦'}
print(diccionario)
print(diccionario['perro'],type(diccionario['perro']))
print(diccionario['gato'],type(diccionario['gato']))
print(diccionario['ave'],type(diccionario['ave']))
'''

# Cambiar el valor de una clave
'''
print ("Cambiar el valor de una clave")
diccionario = {'perro': '🐶', 'gato': '🐱', 'ave': '🐦'}
print(diccionario)
diccionario['perro'] = '🐩'
print(diccionario)
'''
# si la clave no existe, se crea un nuevo par clave-valor
'''
print ("Crear un nuevo par clave-valor")
diccionario = {'perro': '🐶', 'gato': '🐱', 'ave': '🐦'}
print(diccionario)
diccionario['pez'] = '🐠'
print(diccionario)
'''
# para eliminar un pa clave-valor se utiliza "del"
'''
print ("Eliminar un par clave-valor")
diccionario = {'perro': '🐶', 'gato': '🐱', 'ave': '🐦'}
print(diccionario)
del diccionario['ave']
print(diccionario)
'''
# se puede reasignar la clave creado un nuevo par y elimunando el anterior
'''
print ("Modificar la clave")
diccionario = {'perro': '🐶', 'gato': '🐱', 'ave': '🐦'}
print(diccionario)
diccionario['perrito'] = diccionario['perro']
del diccionario['perro']
print(diccionario)
'''

# Concatenacionde de diccionarios, no se puede por ( + )
'''
print ("Concatenar diccionarios")
diccionario1 = {'perro': '🐶', 'gato': '🐱'}
diccionario2 = {'ave': '🐦', 'pez': '🐠'}
concatenado = diccionario1 + diccionario2 
# TypeError: unsupported operand type(s) for +: 'dict' and 'dict'
'''
# repeticionde de diccionario, nose pude por ( * )
'''
print ("Repetir diccionarios")
diccionario = {'perro': '🐶', 'gato': '🐱'}
repetido = diccionario * 3 
# TypeError: unsupported operand type(s) for *: 'dict' and 'int'
'''

# Metodos de los diccionarios
# get(clave)
'''
print ("Método get(clave)")
diccionario = {'perro': '🐶', 'gato': '🐱', 'ave': '🐦'}
print (diccionario)
perro = diccionario.get('perro')
print(perro, type(perro))
pez = diccionario.get('pez')
print(pez, type(pez))
'''
# items()
'''
print ("Método items()")
diccionario = {'perro': '🐶', 'gato': '🐱', 'ave': '🐦'}
print(diccionario)
items = diccionario.items()
print(items, type(items))
items = list(items) # Convertir a lista
print(items, type(items))
print(items[0], type(items[0]))
'''
# keys()
'''
print ("Método keys()")
diccionario = {'perro': '🐶', 'gato': '🐱', 'ave': '🐦'}
print(diccionario)
keys = diccionario.keys()
print(keys, type(keys))
keys = list(keys) # Convertir a lista
print(keys, type(keys))
print(keys[0], type(keys[0]))
'''
# values()
'''
print ("Método values()")
diccionario = {'perro': '🐶', 'gato': '🐱', 'ave': '🐦'}
print(diccionario)
values = diccionario.values()
print(values, type(values))
values = list(values) # Convertir a lista
print(values, type(values))
print(values[0], type(values[0]))
'''

# Metodso de Adicion
# update(diccionario)
'''
print ("Método update(diccionario)")
diccionario = {'perro': '🐶', 'gato': '🐱', 'ave': '🐦'}
print(diccionario)
diccionario.update({'pez': '🐠', 'perro': '🐩'})
print(diccionario)
'''
# update(clave=valor)
'''
print ("Método update(clave=valor)")
diccionario = {'perro': '🐶', 'gato': '🐱', 'ave': '🐦'}
print(diccionario)
diccionario.update(pez='🐠', perro='🐩')
print(diccionario)
'''

# Metodos de eliminacion
# clear()
'''
print ("Método clear()")
diccionario = {'perro': '🐶', 'gato': '🐱', 'ave': '🐦'}
print(diccionario)
diccionario.clear()
print(diccionario)
'''
# pop(clave)
'''
print ("Método pop(clave)")
diccionario = {'perro': '🐶', 'gato': '🐱', 'ave': '🐦'}
print(diccionario)
gato = diccionario.pop('gato')
print(gato, type(gato))
print(diccionario)
'''
# popitem()
''''
print ("Método popitem()")
diccionario = {'perro': '🐶', 'gato': '🐱'}
print(diccionario)
par = diccionario.popitem()
print(par, type(par))
print(diccionario)
# par = diccionario.popitem()
# print(par, type(par)) # KeyError: 'popitem(): dictionary is empty'''''

# Metodos de copia
'''
print ("Asignación por referencia")
diccionario = {'perro': '🐶', 'gato': '🐱', 'ave': '🐦'}
print(diccionario)
copia = diccionario
print(copia)
copia['ave'] = '🦅'
print(diccionario)
print(copia)
'''
# copy()
'''
print ("Método copy()")
diccionario = {'perro': '🐶', 'gato': '🐱', 'ave': '🐦'}
print(diccionario)
copia = diccionario.copy()
print(copia)
copia['ave'] = '🦅'
print(diccionario)
print(copia)
'''

# Funciones con Diccionarios
# len(diccionario)
'''
print ("Función len()")
diccionario = {'perro': '🐶', 'gato': '🐱', 'ave': '🐦'}
print(diccionario)
longitud = len(diccionario)
print(longitud)
'''
# in / not in
'''
print ("Función in  / not in")
diccionario = {'perro': '🐶', 'gato': '🐱', 'ave': '🐦'}
print(diccionario)
existe = 'perro' in diccionario
print(existe, type(existe))
no_existe = 'pez' not in diccionario
print(no_existe, type(no_existe))
'''
# iter(diccionario.items)
'''
print ("Función iter()")
diccionario = {'perro': '🐶', 'gato': '🐱', 'ave': '🐦'}
print(diccionario)
iterador = iter(diccionario.items())
print(type(iterador))
siguiente = next(iterador)
print(siguiente, type(siguiente))
siguiente = next(iterador)
print(siguiente, type(siguiente))
siguiente = next(iterador)
print(siguiente, type(siguiente))
'''

# Diccionario anidados
'''
print ("Diccionarios anidados")
diccionario = {'perro': '🐶', 'gato': '🐱',  'ave': {'pajaro': '🐦', 'aguila': '🦅'}}
print(diccionario)
aves = diccionario['ave']
print(aves)
ave = aves['pajaro']
print(ave)
ave = aves['aguila']
print(ave)
'''

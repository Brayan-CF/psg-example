'''

    Crea un diccionario con las siguientes tuplas de animales

tupla = (('perro', '🐶') , ('gato','🐱') , ('aves',['🐦','🦅']))

    Del diccionario obtén y elimina el valor de la clave 'aves'
    Modifica el valor de la clave 'gato' por '🐈'
    Cambia la clave perro por perros y su valor por ['🐶','🐕']

'''
tupla = (('perro', '🐶') , ('gato','🐱') , ('aves',['🐦','🦅']))
diccionario = dict(tupla)
print(f"El diccionario es: {diccionario}")
elimina = diccionario.pop('aves')
print(f"Eliminamos la clave aves del diccionario: {diccionario}")
diccionario.update(
    gato = '🐈',
    perro = ['🐶','🐕']
)
print(f"Diccionario modificado: {diccionario}")
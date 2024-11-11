'''

    Crea un diccionario para almacenar información de comidas de 
    animales por ejemplo

comidas = {"carne" : {"animales": ["león", "tigre"]}, 
        "frutas" : {"animales": ["mono", "elefante"]}}

    Añade al diccionario de comidas 4 alimentos más usando update
    (clave=valor)
    Existe en el diccionario de comidas la comida 'carne'?
    Elimina la comida 'frutas' del diccionario de comidas

'''
comidas = {
    "carne" : {"animales": ["león", "tigre"]}, 
    "frutas" : {"animales": ["mono", "elefante"]}
}
comidas.update(

    helado = 'vanilla',
    cereales = 'chocapic',
    jugos = 'linaza',
    dulces = 'chocolate'
)

existe = 'carne' in comidas
print(existe)
Carne = comidas.pop('frutas')
print(comidas)


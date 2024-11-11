'''
Eres NOE y tienes que guardar dos animales de cada especie 
en un arca, crea un diccionario con las especies

arca = {"perro" : 2, "gato" : 2, "tigre" : 2, "mono" : 2, 
        "unicornio" : 0, "jirafa" : 1}



   * Añade al arca 2 especies más usando update()
   * Toma lista de los animales en el arca iterando el diccionario
   * Existe en el arca la especie 'dragon'?
   * Elimina la especie 'unicornio' del arca
   * Modifica el valor de la especie 'jirafa' por 2
   * Vacía el arca después del diluvio

'''
arca = {
    "perro" : 2, "gato" : 2, "tigre" : 2, "mono" : 2, 
    "unicornio" : 0, "jirafa" : 1
}
arca.update({
    'leon' : 2,
    'sapo' : 2
})
print(f"anadiendo 2 especies mas: {arca}")

'''
iterador = iter(arca.items())
siguiente = next(iterador)
print(siguiente, type(siguiente))
siguiente = next(iterador)
print(siguiente, type(siguiente))
siguiente = next(iterador)
print(siguiente, type(siguiente))
siguiente = next(iterador)
print(siguiente, type(siguiente))
siguiente = next(iterador)
print(siguiente, type(siguiente))
siguiente = next(iterador)
print(siguiente, type(siguiente))
siguiente = next(iterador)
print(siguiente, type(siguiente))
siguiente = next(iterador)
print(siguiente, type(siguiente))
'''

existe = 'dragon' in arca
print(f"Existe la clave dragon en el diccionario: {existe}")

elimina = arca.pop('unicornio')
print(f"Eliminamos unicornio del diccionario: {arca}")

arca.update(jirafa = 2)
print(f"Actualizamos el diccionario: {arca}")

arca.clear()
print(f"paso el diluvio y la arca se vacio: {arca}")
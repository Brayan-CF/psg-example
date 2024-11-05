'''
Crear una lista de personas con 10 nombres de personas

    Obtener una sub lista de 2 a 7
    Buscar si existe el nombre "Jhon" en la lista original
    Ordenar la sub lista alfabéticamente
    Ordenar la lista original alfabéticamente de forma descendente

'''
lista = [
    "jhon", "juan,", "jose", "ana", "alex",
    "rosa", "joel", "gael", "mael", "luis"
]
sub_lista = lista[2:7]
print(sub_lista)

nombre = "jhon"
print(nombre, lista.count(nombre))

lista.sort()
print(lista)

lista.sort(reverse=True)
print(lista)


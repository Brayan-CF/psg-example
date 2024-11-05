'''
Tienes una tienda de abarrotes y tienes dos listas una con los 
productos que tienes y otra con los precios 
5. ¿Cuántos productos tienes en total? 
6. ¿Cuanto cuesta el total de los productos? 
7. Ordena los productos alfabéticamente y precios si es posible 
8. Eliminar todos los productos de las listas
'''
lista_productos = [
    "leche", "pan", "huevo"
]
Lista_precios = [
    6, 0.50, 1
]
'''
# paa agregar 5 productos al final.
lista_productos.extend(["cafe", "mantequilla", "te", "cocoa", "queso"])
print("lista estendiad: ",lista_productos)

# para eleimanar leche
lista_productos.remove("leche")
print("lista actualizada: ", lista_productos)

# para saber uanto cuesta pan y 
print("el", lista_productos[0], "cuesta:", Lista_precios[1])
print("el", lista_productos[1], "cuesta:", Lista_precios[2])

# cual es producto mas caro y mas barato
print(max(Lista_precios), lista_productos[1])
print(min(Lista_precios), lista_productos[0])'''

# para cuantos productos tengo
print(len(lista_productos), "esos son todos los productos ")

# para saber el total de productos
print(sum(Lista_precios), "eso el total!")

# para organisr prodcutos y precios
lista_productos.sort()
print(lista_productos)
Lista_precios.sort()
print(Lista_precios)

# para eliminar todos los productos de la lista
lista_productos.clear()
print(lista_productos)
'''
Tienes una tienda de abarrotes y tienes dos listas una con los 
productos que tienes y otra con los precios

    Agregar 5 productos nuevos al final de las listas
    Eliminar el producto con el nombre "Leche" de las listas
    ¿Cuanto cuesta el producto "Pan" y "Huevo"?
    ¿Cual es el producto más caro y más barato?

'''
lista_productos = [
    "leche", "pan", "huevo"
]
Lista_precios = [
    6, 0.50, 1
]
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
print(min(Lista_precios), lista_productos[0])
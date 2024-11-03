'''
Ingresa una cadena por teclado y almacena el valor en una tupla

    Concatena la tupla ('¡', ) + tupla almacenada + la tupla ('!', )
    Imprime el resultado concatenado
    Repite la tupla final 3 veces e imprime el nuevo resultado

'''

cadena = tuple(input("ingrese una palabra: "))
tupla = (cadena)
tupla1 = ('¡',)
tupla2 = ('!',)
concatenar = tupla1 + tupla + tupla2
repeticion = (tupla1 + tupla + tupla2) * 3
print("resultado concatenado: ", concatenar)
print(type(concatenar))
print("resultado concatenado 3 veces: ", repeticion)
print(type(repeticion))

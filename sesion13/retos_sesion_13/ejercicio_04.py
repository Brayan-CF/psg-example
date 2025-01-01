'''
Crea un ciclo infinito que reciba una palabra por teclado y 
verifique si es palíndrome, termina la ejecución si se ingresa 
la palabra salir
'''

while True:
    palabra = input("Ingresa una palabra: ")
    if palabra == "salir":
        break
    if palabra == palabra[::-1]:
        print(f"{palabra} es palíndrome")
    else:
        print(f"{palabra} no es palíndrome")
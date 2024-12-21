# ESTRUCTURA DE CONTROL DE FLUJO

# FOR
'''
El ciclo for es un ciclo que se ejecuta un número determinado 
de veces.En el caso de los for se recorre una secuencia de 
elementos. Se puede recorrer un rango de números o listas, tuplas, 
diccionarios, etc.
'''
# range()
'''
range(5)
'''
''' resiviando 3 argumentos
range(1, 10, 2)
'''
''' puede haber rangos negativos
range(10, 0, -1)
'''
''' podemos convertir el rango en lista
print(list(range(5)))
'''

# For tiene la siguiente estructura.
'''
for variable in range(inicio, fin, paso):
    print(variable)


    for es la palabra reservada
    variable es la variable que se usará para iterar
    in es palabra reservada de pertenencia
    range(inicio, fin, paso) es la secuencia de números
    : es el delimitador de inicio del ciclo
    print(variable) es el código a ejecutar posee un nivel de 
    indentación

'''
#para python la estructura de control es la siguiente.
'''
print ("Inicio")
for i in range(5): # rango (0,5,1)
    print(i)
print ("Fin")
'''

# Ejemplo 1, sumar los numeros del 1 al 10 de 2 en 2
'''
print ("Ejemplo 1")
suma = 0
for i in range(1, 11, 2): # 1, 3, 5, 7, 9
    suma = suma + i #suma += i
print(suma)
'''
# Ejemlo 2, crear un arbol de navidad de 6 niveles
'''
print ("Ejemplo 2")
for i in range(0, 6):
    print(" "*(5-i) + "*"*i*2+"*")
'''
#Ejemplo 3, crear una serie de numeros cuadrados.
'''
print ("Ejemplo 4")
pares = []
for i in range(0, 11, 2):
    pares.append(i)
print(pares)
'''
# Ejemplo 4,primeros de la serie numeros cubicos.
'''
print ("Ejercicio 1")
for i in range(1, 11):
    print(i**3, end=" ")
'''

# for tiene la siguiente estructura.
'''
for variable in secuencia:
    print(variable)
'''
# Ejemplo 5, imprimir los elementos de una lista.
'''
print ("Ejemplo 5")
fiesta = ['🎄','🎆','🎁','🎊','✨','🧨']
for objeto in fiesta:
    print(objeto)
'''
# Ejemplo 6, imprimir los elementos de una tupla separados po coma.
'''
print ("Ejemplo 6")
frutas =  ('🍅','🍇','🍈','🍉','🍊')
for fruta in frutas:
    print(fruta, end=", ")
'''
# Ejemplo 7, imprimir los elementos de un diccionario.
'''
print ("Ejemplo 7")
frutas = {'🍅':'Tomate','🍇':'Uva','🍈':'Melón','🍉':'Sandía','🍊':'Naranja'}
for clave in frutas:
    print(clave, frutas[clave])
'''
# Ejemplo 8, imprimir los elementos del ciclo de vida de un pollo con flechas.
'''
print ("Ejemplo 8")
ciclo_vida = '🥚🐣🐥🐤🐔🍗'
for etapa in ciclo_vida:
    print(etapa, end="->")
'''
# Ejemplo 9, listar los elemnentos de la siguiente serie["",`,`,""]
'''
print ("Ejemplo 9")
animales = ['🐶','🐱','🐰','🐭']
for animal in animales:
    print(animal)
'''
# Ejemplo 10, listar los elementos de la siguiente erie
'''
print ("Ejemplo 10")
animales = ['🐶','🐱','🐰','🐭']
for i in range(len(animales)):
    print(animales[i])
'''
''' funcion que devuelve enumerado.
enumerate(['🐶','🐱','🐰','🐭'])
'''
# Ejemplo 11, listar los elementos de la siguiente serie
'''
print ("Ejemplo 11")
animales = ['🐶','🐱','🐰','🐭']
for i, animal in enumerate(animales):
    print(i, animal, animales[i])
'''
# WHILE
# estructura de control While es la siguiente.
'''
while condicion:
    print("Código a ejecutar")
'''
# Ejemplo 12, imprimir los  numeros ya sea menores o iguala 5 de los 0
'''
print ("Ejemplo 12")
i = 0
while i <= 5:
    print(i)
    i += 1
'''
# Ejemplo 12, sumar los numeros ya no se ingrese por teclado el 0.
'''
print ("Ejemplo 13")
suma = 0
numero = int(input("Ingrese un número: "))
while numero != 0:
    suma += numero
    numero = int(input("Ingrese un número: "))
print(suma)
'''
# Ejemplo 14, De la siguiente lista de frutas imprimir los elementos hasta que se encuentre un gusano 🐛contra for
'''
frutas = ['🍎','🍌','🍇','🍉','🍊','🐛','🍋','🍍']
print ("Ejemplo 14")
for fruta in frutas:
    if fruta == '🐛':
        break
    print(fruta)
print ("Fin")
'''
# con while
'''
frutas = ['🍎','🍌','🍇','🍉','🍊','🐛','🍋','🍍']
print ("Ejemplo 14")
i = ""
while i != '🐛':
    i = frutas.pop(0)
    print(i)
print ("Fin")
'''
# Ejemplo 15, crear un ciclo infinito puede hacer que el progemam se bloquee
'''
print ("Ejemplo 15")
contador = 0
while True:
    print(contador)
    contador += 1
'''
# Ejemplo 16, Crear un ciclo infinito que pida una cadena de texto la ponga en mayúsculas y la imprima hasta que se ingrese la palabra salir
'''
print ("Ejemplo 16")
while True:
    texto = input("Ingrese un texto: ")
    if texto == 'salir':
        break
    print(texto.upper())
print ("Fin")
'''
# Ejemplo 17, Crear una lista de los números pares del 2 al 10
'''
print ("Ejemplo 17")
pares = [i for i in range(2, 11, 2)]
print(pares)
'''
# Ejemplo 18, Crear una lista de los números pares del 2 al 10 con condicional
'''
print ("Ejemplo 18")
pares = [i for i in range(2, 11) if i % 2 == 0]
print(pares)
'''
# Ejemplo 19, Crear un diccionario números 2 al 10 donde si es par vale "Par" y si es impar valga "Impar"
'''
print ("Ejemplo 19")
pares = {i: "Par" if i % 2 == 0 else "Impar" for i in range(2, 11)}
print(pares)
'''
# Ejemplo 20, Imprimir las tablas de multiplicar del 1 y 2
'''
print ("Ejemplo 20")
for i in range(1, 3):
    print(f"Tabla del {i}")
    for j in range(1, 11):
        print(f"{i} x {j} = {i*j}")
'''
# Ejemplo 21, Introducir un número por teclado y crear una tabla de multiplicar de ese número 1 al 10, si se ingresa 0 termina el programa
'''
print ("Ejemplo 21")
while True:
    numero = int(input("Ingrese un número: "))
    if numero == 0:
        break
    print(f"Tabla del {numero}")
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero*i}")
print ("Fin")
'''
# Ejemplo 22, Introducir un número por teclado y crear un matriz nxn con la letra X
'''
print ("Ejemplo 22")
n = int(input("Ingrese un número: "))
matriz = [['X' for i in range(n)] for j in range(n)]
for fila in matriz:
    for columna in fila:
        print(columna, end=" ")
    print()
print (matriz)
'''
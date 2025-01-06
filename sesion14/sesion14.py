# Sesion 14
# funciones
# Bloques de codigo
'''-----------------------------------------------------'''
# Declaracion de una Funcion:
'''
def nombre_funcion():
    print ("Bloque de código")
'''
'''

    def es la palabra reservada
    nombre_funcion es el nombre de la función
    () son los paréntesis que pueden contener parámetros
    : es el delimitador de inicio del bloque de código
    print es el código a ejecutar
    Posee un nivel de indentación

'''
# para devolver un valor: return
'''
def nombre_funcion():
    return "Bloque de código"
'''
# para llamar a la funcion:
'''
def nombre_funcion():
    print ("Bloque de código")

nombre_funcion()
print (type(nombre_funcion))
'''
# las funciones debeb ser definas antes de ser llamadas.
'''
def nombre_funcion():
    print ("Bloque de código")

nombre_funcion()
'''
'''---------------------------------------------------------'''
# Ejemplo 1, Crear una función para imprimir una lista de 10 números pares y llamarla dos veces
'''
print ("Ejemplo 1")
print ("1. Definir función")
def imprimir_pares():
    pares = [i for i in range(0, 21, 2)]
    print (pares)

print ("2. Llamar función")
imprimir_pares()
imprimir_pares()
'''

# Ejercicio 1, crear una función que imprima un mensaje de bienvenida del siguiente conjunto de forma aleatoria
'''
mensajes = {"Bienvenido al Python Study Group 🐍",
"¡Hola y bienvenido al Python Study Group! ✨",
"Hola, aprendamos Python juntos 🐍"}
''' 
'''
def bienvenida():
    mensajes = {"Bienvenido al Python Study Group 🐍",
    "¡Hola y bienvenido al Python Study Group! ✨",
    "Hola, aprendamos Python juntos 🐍"}
    print (mensajes.pop())

bienvenida()
'''

# Ejercicios 2, Crear una función que devuelva un saludo en diferentes idiomas
'''
print ("Ejemplo 2")
print ("1. Definir función")
def saludo():
    saludos = {"Hola", "Hello", "Bonjour", "Ciao"}
    return saludos.pop()

print ("2. Llamar función")
resultado = saludo()
print (resultado)
'''

# Ejemplo 3, Crear una función que devuelva un saludo en dos idiomas
'''
print ("Ejemplo 3")
print ("1. Definir función")
def saludo():
    saludos_es = {"Hola", "Holi", "Buenos días"}
    saludos_en = {"Hello", "Hi", "Good morning"}
    return saludos_es.pop(), saludos_en.pop()

print ("2. Llamar función")
resultado = saludo()
print (resultado)
'''

# Ejemplo 4, Crear una función que imprima el cuadrado de un número
'''
print ("Ejemplo 4")
print ("1. Definir función")
def cuadrado(numero):
    print (numero**2)

print ("2. Llamar función")
cuadrado(5)
cuadrado(10)
'''

# Ejemplo 5, Crear una función que reciba una cadena y un entero y repita la cadena el número de veces
'''
print ("Ejemplo 5")
print ("1. Definir función")
def repetir(cadena, veces):
    print (cadena*veces)

print ("2. Llamar función")
repetir("✨🎉", 10)
'''

# Ejemplo 6, Crear una función que reciba dos números y devuelva una lista con la suma, resta, multiplicación y división de los números
'''
print ("Ejemplo 6")
print ("1. Definir función")
def operaciones(numero1, numero2):
    suma = numero1 + numero2
    resta = numero1 - numero2
    multiplicacion = numero1 * numero2
    division = numero1 / numero2
    return [suma, resta, multiplicacion, division]

print ("2. Llamar función")
resultado = operaciones(10, 5)
print (resultado)
'''

# Ejemplo 7, Crear una función que reciba dos números y devuelva la suma, resta, multiplicación y división de los dos números
'''
print ("Ejemplo 7")
print ("1. Definir función")
def operaciones(numero1, numero2):
    suma = numero1 + numero2
    resta = numero1 - numero2
    multiplicacion = numero1 * numero2
    division = numero1 / numero2
    return suma, resta, multiplicacion, division

print ("2. Llamar función")
suma, resta, multiplicacion, division = operaciones(10, 5)
print (suma, resta, multiplicacion, division)
'''

# Ejemplo 8, De la siguiente lista de números obtener el mayor y menor número con una función
'''
numeros = [10, 5, 20, 15, 25, 30] #Global

def mayor_menor(): #No recibe argumentos
    mayor = max(numeros) #Local
    menor = min(numeros) #Local
    return mayor, menor #Devuelve dos valores

resultado = mayor_menor()
print (resultado)
'''

# Ejemplo 9 Crear una función que reciba un número y una cantidad de cadenas, concatene las cadenas y la devuelva repetida N veces
'''
print ("Ejemplo 9")
print ("1. Definir función")
def concatenar(numero, *cadenas):
    concatenado = ""
    for cadena in cadenas:
        concatenado += cadena
    return concatenado*numero

print ("2. Llamar función")
resultado = concatenar(3, "🍎", "🍌", "🍍")
print (resultado)
'''

# Ejemplo 10, Crear una función que reciba los datos de una persona y devuelva un mensaje con los datos
'''
print ("Ejemplo 10")
print ("1. Definir función")
def datos_persona(**datos):
    mensaje = ""
    for clave, valor in datos.items():
        mensaje += f"{str(clave).title()}: {str(valor).upper()}\n"
    return mensaje
print ("2. Llamar función")
resultado = datos_persona(nombre="Jhon", apellido="Doe", edad=20, boliviano=True)
print (resultado)
'''

# Ejemplo 11, Crear tres funciones una principal que reciba un número y dos funciones anidadas que devuelvan el cuadrado y el cubo del número
'''
print ("Ejemplo 11")
print ("1. Definir función Principal")
def principal(numero):
    cuadrado = cuadrado_numero(numero)
    cubo = cubo_numero(numero)
    return cuadrado, cubo

print ("2. Definir función Cuadrado")
def cuadrado_numero(numero):
    return numero**2

print ("3. Definir función Cubo")
def cubo_numero(numero):
    return numero**3

print ("4. Llamar función Principal")
numero = 5
resultado = principal(numero)
print (numero, resultado)
'''

# Ejemplo 12, Crear una función recursiva para obtener el 10 número par
'''
print ("Ejemplo 12")
print ("1. Definir función")
def numero_par(numero):
    if numero == 0:
        return 0
    else:
        return numero_par(numero-1) + 2

print ("2. Llamar función")
resultado = numero_par(10)
print (resultado)
'''

# Ejemplo 13, Crear una función anónima para obtener el cuadrado de un número
'''
print ("Ejemplo 13")
cuadrado = lambda numero: numero**2
resultado = cuadrado(5)
print (resultado)
resultado = cuadrado(10)
print (resultado)
'''


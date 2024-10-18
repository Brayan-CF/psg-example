# Tipo de datos - BOOLEANOS

# En python los booleanos están implementados
# como una subclase de los números enteros:
# 1. Un booleano True puede ser considerado como número 1
# 2. Un booleano False puede ser considerado como número 0
'''
print ("Tipos de datos booleanos")
print (True)
print (False)
print (True + True)
print (True * True)
print (True * False)
print (False + False)
print (False * False)
'''

# los enteros pueden realizar operaciones ritmeticas, 
# entre numeros y booleanos
'''
print ("Números y booleanos")
print (10 + True)
print (10 + False)
print (10 * True)
print (10 * False)
'''

# Declarion booleanos
# 1. Directamente en el código escribiendo True o
# False sin necesidad de comillas.
'''
print ("Declarar variables booleanas")
var_booleana = True
print (var_booleana)
print (type(var_booleana))
var_booleana = False
print (var_booleana)
print (type(var_booleana)) '''

# 2. Mediante la función bool()
'''
print ("Declarar mediante función bool()")
var_booleana = bool(1)
print (var_booleana)
print (type(var_booleana))
var_booleana = bool(0)
print (var_booleana)
print (type(var_booleana))
var_booleana = bool(15)
print (var_booleana)
print (type(var_booleana)) '''

# Como resultado de una operación de comparadores lógicos
'''
print ("Operadores de comparación")
print (10 == 10)
print (10 != 10)
print (10 < 10)
print (10 > 10)
print (10 <= 10)
print (10 >= 10)
print (10 is 10)
print (10 is not 10) '''

# comparadores asignados tambien a variables
'''
print ("Asignación de variables")
x = 10
mayor_que_cero = x > 0
print (mayor_que_cero)
diferente_de_10 = x != 10
print (diferente_de_10) '''

# Operadores logicos:
# 1. Not: "NO", esta expresión es unitaria solo necesita
# un operador y su objetivo es invertir la expresión
# 2. And: "Y", esta expresión necesita dos operadores
# 3. Or : "O", esta expresión necesita dos operadores
'''
print ("Operadores lógicos")
print (True and True)
print (True and False)
print (False or True)
print (False or False)
print (not True)
print (not False) '''

# Prioridades: not, and , or
'''
print ("Operadores lógicos y prioridad")
print (False and False or True)
print (False and (False or True))
print (not True and False or True)
print (not (True and False or False))
print (not True and (False or False))
print (not True and False or False) '''

# And
'''
print ("Operador AND")
print (True and True)
print (True and False)
print (False and True)
print (False and False) '''

# Or
'''
print ("Operador OR")
print (True or True)
print (True or False)
print (False or True)
print (False or False) '''

# Not 
'''
print ("Operador NOT")
print (not True)
print (not False) '''

# Nand
'''
print ("Operador NAND")
print (not (True and True))
print (not (True and False))
print (not (False and True))
print (not (False and False)) '''

# Nor 
'''
print ("Operador NOR")
print (not (True or True))
print (not (True or False))
print (not (False or True))
print (not (False or False)) '''

# Xor
'''
print ("Operador XOR")
a = True
b = False
print ((a or b) and not (a and b))
a = True
b = True
print ((a or b) and not (a and b)) '''

# Prueba: Si un sensor detecta movimiento
# y tiene batería entonces enciende la luz
'''
print ("Ejemplo de uso Sensor y Batería")
sensor = True
bateria = True
print (sensor, "and", bateria, "=", sensor and bateria)
sensor = True
bateria = False
print (sensor, "and", bateria, "=", sensor and bateria)
sensor = False
bateria = True
print (sensor, "and", bateria, "=", sensor and bateria)
sensor = False
bateria = False
print (sensor, "and", bateria, "=", sensor and bateria) '''

# Ejemplo 1
# Determinar si el número 20 está en el rango 0 a 100
'''
print ("Ejemplo 1 - Comparación y Lógicos")
numero = 20
print (numero >= 0 and numero <= 100) '''

# Ejemplo 2
# Un estudiante obtuvo las siguientes notas en sus exámenes: 
# 15, 20, 16 determinar si el estudiante aprobó con una nota superior
# a 50
'''
print ("Ejemplo 2 - Aritméticos y comparación")
nota1 = 15
nota2 = 20
nota3 = 16
print ((nota1 + nota2 + nota3) > 50) '''

# Ejemplo 3
# Determinar si el número 15 es divisible por 3 y 5, pero no por 2
'''
print ("Ejemplo 3 - Aritméticos, comparación y lógicos")
numero = 15
print ((numero % 3 ==0) and (numero % 5 ==0) and (numero % 2 !=0)) '''

# CORTOCIRCUITOS
# Cortocircuitos con And
print ("Cortocircuito con operador and")
x = 1
y = 0
print (x > 2 and (x/y) > 2)
print (x > 0 and (x/y) > 0)

# Cortocircuitos con Or

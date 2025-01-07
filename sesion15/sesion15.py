# Sesion 15
# Errores y excepciones
# Try - Except

'''-----------------------------------------------------------'''

# Ejemplo 1, división por cero

'''
print ("Inicio Ejemplo 1")
x = 1 / 0
print (x)
print ("Fin Ejemplo 1")
'''

# Ejemplo 1, División por cero

'''
print ("Inicio Ejemplo 1")
try:
    x = 1 / 0
    print (x)
except Exception as e:
    print("💀 Error:", e, type(e))
print ("Fin Ejemplo 1")
'''

# Try
'''
try:
    # Código que puede lanzar una excepción
except ZeroDivisionError as e:
    # Código si se produce una excepción de división por cero
except Exception as e:
    # Código si se produce una excepción genérica
'''

# Ejemplo 2, división por cero
'''
print ("Inicio Ejemplo 2")
divisor = 0
try:
    x = 1 / divisor
    print (x)
except ZeroDivisionError as e:
    print("0️⃣ Error:", e, type(e))
except Exception as e:
    print("💀 Error:", e, type(e))
print ("Fin Ejemplo 2")
'''

# Ejemplo 2, división por cero
'''
print ("Inicio Ejemplo 2")
divisor = "0"
try:
    x = 1 / divisor
    print (x)
except ZeroDivisionError as e:
    print("0️⃣ Error:", e, type(e))
except Exception as e:
    print("💀 Error:", e, type(e))
print ("Fin Ejemplo 2")
'''

# Jerarquía de excepciones
# Ejemplo 2, división por cero
'''
print ("Inicio Ejemplo 2")
divisor = 0
try:
    x = 1 / divisor
    print (x)
except Exception as e: # Captura cualquier excepción
    print("💀 Error:", e, type(e))
except ZeroDivisionError as e:
    print("0️⃣ Error:", e, type(e))
print ("Fin Ejemplo 2")
'''

# Ejemplo 3, de la lista de calificaciones obtener el promedio
'''
calificaciones = [20,40,80,"A"]
suma = 0
try:
    for i in range(len(calificaciones)+1):
        suma += calificaciones[i] 
    promedio = suma / len(calificaciones)
    print("Promedio:", promedio)
except ZeroDivisionError as e:
    print("0️⃣ Error:", e, type(e))
except TypeError as e:
    print("🎭 Error:", e, type(e))
except Exception as e:
    print("💀 Error:", e, type(e))
'''

# Ejemplo 3, de la lista de calificaciones obtener el promedio
'''
calificaciones = [20,40,80]
suma = 0
try:
    for i in range(len(calificaciones)+1):
        suma += calificaciones[i]
    promedio = suma / len(calificaciones)
    print("Promedio:", promedio)
except ZeroDivisionError as e:
    print("0️⃣ Error:", e, type(e))
except TypeError as e:
    print("🎭 Error:", e, type(e))
except Exception as e: # Captura cualquier excepción
    print("💀 Error:", e, type(e))
'''

# Estrucctura de un bloque else
'''
try:
    # Código que puede lanzar una excepción
except Exception as e:
    # Código si se produce una excepción
else:
    # Código si no se produce ninguna excepción
'''

# Ejemplo 4, de la lista de calificaciones obtener el promedio
'''
print ("Inicio Ejemplo 4")
calificaciones = [20,40,80]
suma = 0
try:
    for i in range(len(calificaciones)):
        suma += calificaciones[i]
    promedio = suma / len(calificaciones)
    print("Promedio:", promedio)
except Exception as e:
    print("💀 Error:", e, type(e))
else:
    print ("🎉 Sin errores")
print ("Fin Ejemplo 4")
'''

# Bloque finally
'''
try:
    # Código que puede lanzar una excepción
except Exception as e:
    # Código si se produce una excepción
else:
    # Código si no se produce ninguna excepción
finally:
    # Código que se ejecuta siempre
'''

# Ejemplo 5, simula una conexion a internet que haga ping y cerrar la connexion
'''
print ("Inicio Ejemplo 5")
try:
    print("🔗 Ping...")
except Exception as e:
    print("💀 Error:", e)
else:
    print("🎉 Ping Exitoso")
finally:
    print("🔌 Cerrando conexión")
'''

# Estructura de raise
'''
raise Exception("Mensaje de error")
'''

# Ejemplo 6, simula una conexion a internet que haga ping y cerrar la connexion
'''
print ("Inicio Ejemplo 6")
try:
    print("🔗 Ping...")
    raise Exception("Error de conexión") #Excepción genérica
except Exception as e: # Captura cualquier excepción
    print("💀 Error:", e)
else:
    print("🎉 Ping Exitoso")
finally:
    print("🔌 Cerrando conexión")
'''

# Pass
# Ejemplo 7, crea una funcion que no hace nada
'''
print("Inicio Ejemplo 7")
def funcion():
    pass

funcion()
print("Fin Ejemplo 7")
'''

# Estructura de una excepción personalizada
'''
class MiError(Exception):
    pass

raise MiError("Mensaje de error")
'''

# Ejemplo 8, tienes un frutero, saca las frutas mientras no sea un gusano y genere una excepcion.
'''
print("Inicio Ejemplo 8")
class GusanoError(Exception):
    pass

frutero = ['🍎', '🍌', '🍐', '🐛', '🍇']
for fruta in frutero:
    try:
        if fruta == '🐛':
            raise GusanoError("😱 Ewww!")
        print(fruta)
    except GusanoError as e:
        print("🐛 Error:", e)
    except Exception as e:
        print("💀 Error:", e)
print("Fin Ejemplo 8")
'''

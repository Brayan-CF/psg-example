# Sesion Bonus

# Depuracion
# Debug en VScode
# ----------------------------------------------------------------- #

def suma(a, b):
    c = a + b
    return c

def resta(a, b):
    return a - b

def multiplicacion(x, y):
    z = x * y
    return z

def division(x, y):
    return x / y

def division_controlada(x,y):
    try:
        return x / y
    except ZeroDivisionError as e:
        return "Division entre cero"

a = 11
b = 0
print (suma(a, b))
print (resta(a, b))
print (multiplicacion(a, b))
print (division_controlada(a, b))
print (division(a, b))

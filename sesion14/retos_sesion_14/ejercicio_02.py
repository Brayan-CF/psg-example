'''
Calculadora flexible: 
Crea una calculadora que acepte diferentes 
operaciones matemáticas como argumentos de palabras clave y realice 
los cálculos correspondientes, las operaciones son suma, resta, 
multiplicación y división
'''

'''
print("Elige una de las muchas opciones:")
print("1. suma")
print("2. resta")
print("3. multiplicacion")
print("4. division")
opcion = input("ingrese un numero de las opciones dadas: ")
if opcion == '1':
    num1 = int(input("ingrese el primer numero:\n"))
    num2 = int(input("ingrese el segundo numero:\n"))
    print(f"la suma es: {num1 + num2}")
elif opcion== '2':
    num1 = int(input("ingrese el primer numero:\n"))
    num2 = int(input("ingrese el segundo numero:\n"))
    print(f"la resta es: {num1 - num2}")
elif opcion == '3':
    num1 = int(input("ingrese el primer numero:\n"))
    num2 = int(input("ingrese el segundo numero:\n"))
    print(f"la multiplicacion es: {num1 * num2}")
elif opcion == '4':
    num1 = int(input("ingrese el primer numero:\n"))
    num2 = int(input("ingrese el segundo numero:\n"))
    print(f"la divicion es: {num1 / num2}")
else:
    print("no ingreso nada ERROR !!!!!")'''


def calculadora(num1, num2):
    sum = num1 + num2
    resta = num1 - num2
    multiplicacion = num1 * num2
    division = num1 // num2
    return [sum, resta, multiplicacion, division]

resultado = calculadora(50, 2)
print(resultado)

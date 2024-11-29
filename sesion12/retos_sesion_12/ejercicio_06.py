'''
Crea una calculadora por consola que realice las operaciones de 
suma, resta, multiplicación y división, ingresa dos números y la 
operación a realizar, verifica si la operación es válida y muestra 
el resultado

Número 1: 10
Número 2: 5
Operación: +
-------------
Resultado: 15
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
    print("no ingreso nada ERROR !!!!!")



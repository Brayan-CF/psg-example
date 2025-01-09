'''
Crear una calculadora que solicite dos números y realice las 
operaciones básicas de suma, resta, multiplicación y división con 
manejo de excepciones, para salir del programa se debe ingresar 
"salir"
'''

def calculadora():
    while True:
        try:
            num1 = input("Ingresa el primer número: ")
            if num1 == "salir":
                break
            num1 = float(num1)
            num2 = float(input("Ingresa el segundo número: "))
            operacion = input("Ingresa la operación que deseas realizar (+, -, *, /): ")
            if operacion == "+":
                print(f"El resultado de la suma es: {num1 + num2}")
            elif operacion == "-":
                print(f"El resultado de la resta es: {num1 - num2}")
            elif operacion == "*":
                print(f"El resultado de la multiplicación es: {num1 * num2}")
            elif operacion == "/":
                print(f"El resultado de la división es: {num1 / num2}")
            else:
                print("Operación no válida")
        except ValueError:
            print("Ingresa un número válido")
        except ZeroDivisionError:
            print("No se puede dividir entre 0")
        except Exception as e:
            print(f"Error: {e}")

calculadora()




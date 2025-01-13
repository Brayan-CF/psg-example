

# Depuración de un script
'''
La depuración de un script es el proceso de identificar y corregir 
errores en un archivo de código fuente en un programa

Tenemos este script calculadora.py que contiene errores
'''

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return str(a) * b

def divide(a, b):
    return a / b

def pow(a):
    b = 0b100
    return a ** b

def calculator():
    while True:
        print("\nSimple Calculator")
        print("Options:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Pow")
        print("6. Exit")
        choice = input("Select an operation (1/2/3/4/5): ")
        if choice == 'Exit':
            print("Exiting calculator.")
            break
        if choice in ('1', '2', '3', '4', '5'):
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                if choice == '1':
                    print(f"Result: {num1} + {num2} = {add(num1, num2)}")
                elif choice == '2':
                    print(f"Result: {num1} - {num2} = {subtract(num1, num2)}")
                elif choice == '3':
                    print(f"Result: {num1} * {num2} = {multiply(num1, num2)}")
                elif choice == '4 ':
                    print(f"Result: {num1} / {num2} = {divide(num1, num2)}")
        else:
            print("Invalid choice. Please select a valid option.")
calculator()
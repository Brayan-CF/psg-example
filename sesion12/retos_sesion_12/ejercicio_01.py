'''
Crear un script que pida un número entero y verifique si es 
par o impar usando operador ternario
'''

scrip = int(input("Ingrese un numero entero: "))
verificar = "si es par" if scrip % 2 == 0 else "es impar"
print(verificar)
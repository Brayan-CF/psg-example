'''
Imprimir los 20 primeros números primos
'''

#n = int(input("ingrese una cantidad para imprimir: "))

'''
Imprimir los 20 primeros números primos
'''

contador = 0
numero = 2

while contador < 20:
    es_primo = True
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            es_primo = False
            break
    if es_primo:
        print(numero)
        contador += 1
    numero += 1
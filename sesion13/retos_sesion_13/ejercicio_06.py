'''
Crea un ciclo infinito que reciba un número por teclado y 
verifique si es un número primo, termina la ejecución si se 
ingresa el número 0
'''

while True:
    n = int(input("Ingresa un número: "))
    if n == 0:
        break
    if n < 2:
        print(f"{n} no es primo")
    else:
        for i in range(2, n):
            if n % i == 0:
                print(f"{n} no es primo")
                break
        else:
            print(f"{n} es primo")
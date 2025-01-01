'''
Imprimir los 20 primeros números de la serie de Fibonacci
'''

n = int(input("ingrese de numeros para generara: "))

fibonaci = [0, 1]
for i in range(2, n):
    fibonaci.append(fibonaci[i - 1] + fibonaci[i - 2])
print(fibonaci)
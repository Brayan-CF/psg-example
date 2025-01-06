'''
Crear una función recursiva para obtener el N número de la serie 
de Fibonacci
'''

def fib(n):
    if n < 2:
        return n
    else:
        return fib(n-1) + fib(n-2)

resultado = [fib(n) for n in range(15)]
print(resultado)
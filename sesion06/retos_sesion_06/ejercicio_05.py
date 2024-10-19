'''
Comparar los números 123 y 890, comprobar si 
tienen la misma paridad ambos pares o ambos impares
'''
a = 123
b = 890

misma_paridad_pares= (a % 2 == b % 2)
print(misma_paridad_pares)
misma_paridad_impar = (a % 2 == 1) and (b % 2 == 1)
print(misma_paridad_impar)



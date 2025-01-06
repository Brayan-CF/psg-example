'''
Crear una función que reciba una lista de números y devuelva solo 
los números pares
'''
numbers = [1, 2, 3, 4, 5, 6]
def numeros():
    numbers_par = []
    for element in numbers:
        if element % 2 == 0:
            numbers_par.append(element)
    return numbers_par

res = numeros()
print(res)






'''numbers = [1, 2, 3, 4, 5, 6]
numbers_par=[]
for element  in numbers:
    if element%2==0:
        numbers_par+=[element]
print(numbers_par)'''

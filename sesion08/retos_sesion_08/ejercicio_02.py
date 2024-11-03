'''
Crea una tupla con los siguientes elementos 1,2,3,4,5,6,7,8,9,10
y realiza:

    Imprime el primer elemento
    Imprime el último elemento
    Imprime un slice del 4 al 7
    Imprime un slice del 2 al 9 con pasos de 3
    Imprime un slice del 10 al 1 con saltos de -2

'''
tupla = (1,2,3,4,5,6,7,8,9,10)
print(type(tupla))
print("primer elemento: ", tupla[0])
print("ultimo elemento: ", tupla[9])
print("slice del 4 al 7: ", tupla[3:7])
print("slice del 2 al 9: ", tupla[2:9:3])
print("slice del 10 al 1: ", tupla[9:0:-2])
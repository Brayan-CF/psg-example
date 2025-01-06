'''
Un estudiante desea saber cuál es su promedio de calificaciones en la
materia de matemáticas, cree una función que reciba las calificaciones
como lista y devuelva el promedio las calificaciones son
20,40,60,51,13
'''

def calificaciones():
    promedio = sum([20,40,60,51,13])/len([20,40,60,51,13])
    print(promedio)

calificaciones()
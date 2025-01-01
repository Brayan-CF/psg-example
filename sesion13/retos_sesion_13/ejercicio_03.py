'''
Dar las felicitaciones a los estudiantes que aprobaron el curso 
de la siguiente tupla de estudiantes

estudiantes = [('Juan', 51), ('Pedro', 80), ('Maria', 90), 
('Ana', 40), ('Luis', 30)]

'''

estudiantes = [
    ('Juan', 51), ('Pedro', 80), ('Maria', 90), 
    ('Ana', 40), ('Luis', 30)
]

for estudiante in estudiantes:
    if estudiante[1] >= 51:
        print(f"Felicidades {estudiante[0]} has aprobado el curso con {estudiante[1]} puntos")
    else:
        print(f"Lo siento {estudiante[0]} no has aprobado el curso con {estudiante[1]} puntos")
'''

    De las tuplas de coordenadas

$(x1,y1) = (40, 80) $ y $ (x2,y2) = (50, 50)$

Encuentra las coordenadas del punto medio, almacena en una tupla
e imprime el resultado

$(x,y)$
'''
coordenada1 = (40, 80) 
coordenada2 = (50, 50)
print(type(coordenada1))
print(type(coordenada2))
punto_mediio = (
    (coordenada1[0]+coordenada2[0])/2,
    (coordenada1[1]+coordenada2[1])/2
)

print("el punto medio es: ", punto_mediio)
print(type(punto_mediio))
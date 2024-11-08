'''

    Dos mochileros se encuentran en el Salar de Uyuni y se ponen a
    comparar la cantidad de lugares que han visitado

Cada uno quiere saber en que parte del mundo ha estado el otro que 
el no haya visitado

mochilero_a = {"París", "Londres", "Nueva York", "Tokio",
"Peru", "Chile", "Colombia", "Bolivia"}

mochilero_b = {"Londres", "Roma", "Nueva York", "Sidney",
"Argentina","Brasil","Panama","Bolivia"}
'''
mochilero_a = {
    "París", "Londres", "Nueva York", "Tokio",
    "Peru", "Chile", "Colombia", "Bolivia"
}

mochilero_b = {
    "Londres", "Roma", "Nueva York", "Sidney",
    "Argentina","Brasil","Panama","Bolivia"
}
diferencia_desde_A = mochilero_b.difference(mochilero_a)
diferencia_desde_B = mochilero_a.difference(mochilero_b)
print("perspectiva del mochilero a:", diferencia_desde_A)
print("perspectiva del mochilero b:", diferencia_desde_B)


'''
Ahora quieren saber en que ciudades han estado ambos mochileros
'''
print("ambos mochileros coincidieron en estos lugares:",mochilero_a & mochilero_b)

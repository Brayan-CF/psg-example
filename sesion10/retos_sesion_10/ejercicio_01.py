'''
Anita y Pepito llevan saliendo juntos por 4 semanas, cada vez que 
salen van a comer a una plaza de comidas. Ambos quieren saber que 
tan compatibles son viendo cuantos platos de comida tienen en común. 
A continuación tienes los platos de comida que ambos han ido 
pidiendo a los largo de sus citas:

Anita: Sushi, Pizza, Tacos, Hamburguesa, Pasta, Alitas
Pepito: Pizza, Tacos, Ensalada, Pasta, Helado, Milanesa

Si la cantidad platos de comida que tienen en comunes mayor a 50% 
entonces ambos seguirán saliendo
'''
anita = {
    "sushi", "pizza", "tacos", "hamburguesa", "pasta", "alitas"
}
pepito = {
    "pizza", "tacos", "ensalada", "pasta", "helado", "milanesa"
}
comida_en_comun = anita & pepito
print("la comida en comun de esta pareja es: ", comida_en_comun)
probabilidad = len(comida_en_comun)/100
if probabilidad >= 5:
    print("son campatibles!!")
else:
    print("no son compatiles XXX")
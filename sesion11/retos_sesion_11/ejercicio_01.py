'''
Registro de un zoológico, utiliza un diccionario para almacenar 
información de un animal del zoológico, registra información como 
especie, habitat, dieta, estado de salud, edad, en una lista los 
responsables de su cuidado
'''

animal = {
    "especie": "León",
    "hábitat": "Sabana africana",
    "dieta": "Carnívoro, caza animales grandes",
    "estado_de_salud": "Bueno",
    "edad": 5,  
    "responsables": [
        "Juan Pérez",  
        "Ana Gómez",   
        "Carlos López" 
    ]
}

print("Información del animal:")
print(f"Especie: {animal['especie']}")
print(f"Hábitat: {animal['hábitat']}")
print(f"Dieta: {animal['dieta']}")
print(f"Estado de salud: {animal['estado_de_salud']}")
print(f"Edad: {animal['edad']} años")
print(f"Responsables de su cuidado: {', '.join(animal['responsables'])}")
print(animal)
'''
Un usuario ingresa su nombre y gustos musicales por teclado 
separados por coma, verifica si el usuario ingresó un nombre válido 
usando truthiness, convertir los gustos musicales en una lista y 
verifica si tiene el gusto rock en su lista de gustos musicales

Nombre: Jhon Doe
Gustos musicales: rock,pop,jazz
'''
playlist = {
    "jhon doe": ['rock', 'pop', 'jazz']
}
usuario = input("Ingrese su nombre: ")
gustos_musicales = input("Ingrese sus gustos musicales: ")

# Convertir los gustos musicales en una lista
lista_gustos = gustos_musicales.split(',')
if usuario.lower() in playlist and 'rock' in lista_gustos:
    print("¡Felicidades, usted está verificado!")
else:
    print("Lamentablemente, usted no está registrado o no tiene 'rock' en sus gustos musicales.")



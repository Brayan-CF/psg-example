'''
El dueño de un restaurante de comida Mexicana ha decidido comprar
un restaurante de comida Italiana y abrir un nuevo restaurante de 
comida fusion. La apertura esta a la vuelta de la esquina y aun no 
hay podido actualizar el Menu, Ayuda a actualizar su menu de platos 
disponibles

menu_mexicano: "Tacos", "Enchiladas", "Guacamole", "Tamales"
menu_italiano: "Pizza", "Pasta", "Lasagna", "Tiramisú"
'''

menu_mexicano = {
    "Tacos", "Enchiladas", "Guacamole", "Tamales"
}
menu_itiliano = {
    "Pizza", "Pasta", "Lasagna", "Tiramisú"
}
menu_actuallizado = menu_mexicano.union(menu_itiliano)
print("el menu actualizado es el siguiente: ", menu_actuallizado)

'''
Tienes una página web y un usuario quiere acceder a ella, 
verifica si el usuario inició sesión para acceder a la página, 
caso contrario muestra un mensaje de error
'''

almacen = {
    "carla":111, "miguel": 222, "alex": 333
}
login = input("ingrese su asuario: ")
password = int(input("ingrese su contraseña: "))

if login in almacen and almacen[login] == password:
    print("exito, acabas de iniciar sesion !!!!")
else:
    print("fuera, vos no estas registrado XXXXX")
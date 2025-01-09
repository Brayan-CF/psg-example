'''
Crear un programa para crear una canasta de frutas, solicitar 
frutas por teclado y almacenar en una lista, si se ingresa "salir" 
termina la ejecución. Solo se permiten las siguientes frutas caso 
contrario lanzar una excepción personalizada

🍅🍇🍈🍉🍊🍌🍍🍑
'''

class FrutaNoValida(Exception):
    pass

def canasta_frutas():
    frutas_validas = ["🍅", "🍇", "🍈", "🍉", "🍊", "🍌", "🍍", "🍑"]
    canasta = []
    while True:
        try:
            fruta = input("Ingresa una fruta: ")
            if fruta == "salir":
                break
            if fruta not in frutas_validas:
                raise FrutaNoValida("Fruta no válida")
            canasta.append(fruta)
        except FrutaNoValida as e:
            print(e)
        except Exception as e:
            print(f"Error: {e}")
    print("Canasta de frutas:")
    print(canasta)

canasta_frutas()



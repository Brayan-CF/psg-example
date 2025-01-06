'''
Simular un tres en raya con funciones donde reciba las jugadas y 
devuelva el ganador hasta que alguien ingrese salir
'''

def tres_en_raya():
    tablero = [
        [' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' ']
    ]
    
    def imprimir_tablero():
        for fila in tablero:
            print('|'.join(fila))
            print('-' * 5)
    
    def verificar_ganador():
        for i in range(3):
            if tablero[i][0] == tablero[i][1] == tablero[i][2] and tablero[i][0] != ' ':
                return tablero[i][0]
            if tablero[0][i] == tablero[1][i] == tablero[2][i] and tablero[0][i] != ' ':
                return tablero[0][i]
        if tablero[0][0] == tablero[1][1] == tablero[2][2] and tablero[0][0] != ' ':
            return tablero[0][0]
        if tablero[0][2] == tablero[1][1] == tablero[2][0] and tablero[0][2] != ' ':
            return tablero[0][2]
        return None
    
    jugador = 'X'
    while True:
        imprimir_tablero()
        print(f'Jugador {jugador}')
        fila = input('Fila (o "salir" para terminar): ')
        if fila.lower() == 'salir':
            print("Juego terminado.")
            break
        columna = input('Columna: ')
        if columna.lower() == 'salir':
            print("Juego terminado.")
            break
        try:
            fila = int(fila)
            columna = int(columna)
            if fila not in range(3) or columna not in range(3):
                print("Índices fuera de rango. Intenta de nuevo.")
                continue
            if tablero[fila][columna] == ' ':
                tablero[fila][columna] = jugador
                ganador = verificar_ganador()
                if ganador:
                    imprimir_tablero()
                    print(f'Ganador: {ganador}')
                    break
                jugador = 'O' if jugador == 'X' else 'X'
            else:
                print("Posición ocupada, intenta de nuevo.")
        except ValueError:
            print("Entrada inválida. Por favor, ingresa números enteros.")

tres_en_raya()



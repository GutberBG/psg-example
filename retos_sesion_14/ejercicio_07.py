#Tres en Raya:
 
#Crear una función que reciba una jugada en cada ejecución
def mostrar_tablero(tablero):
    for fila in tablero:
        print(" | ".join(fila))
        print("-" * 9)
def jugar_tres_en_raya():
    tablero = [[" " for _ in range(3)] for _ in range(3)]
    jugador_actual = "X"

    for turno in range(9):
        mostrar_tablero(tablero)
        fila = int(input(f"Jugador {jugador_actual}, ingresa la fila (0-2): "))
        columna = int(input(f"Jugador {jugador_actual}, ingresa la columna (0-2): "))
        if tablero[fila][columna] == " ":
            tablero[fila][columna] = jugador_actual
            if (tablero[fila].count(jugador_actual) == 3 or
                all(tablero[i][columna] == jugador_actual for i in range(3)) or
                all(tablero[i][i] == jugador_actual for i in range(3)) or
                all(tablero[i][2 - i] == jugador_actual for i in range(3))):
                print(f"¡Jugador {jugador_actual} gana!")
                mostrar_tablero(tablero)
                return
            jugador_actual = "O" if jugador_actual == "X" else "X"
    print("¡Es un empate!")
    mostrar_tablero(tablero)

if __name__ == "__main__":
    jugar_tres_en_raya()

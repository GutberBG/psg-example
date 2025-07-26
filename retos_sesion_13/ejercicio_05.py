tablero = [['#' if (i + j) % 2 == 0 else '*' for j in range(8)] for i in range(8)]
for fila in tablero:
    print(" ".join(fila))
file_path = "input_problem10"

filas = 0
columnas = 0
with open(file_path, "r") as file:
    for i, line in enumerate(file):
        if i == 0:
            columnas = len(line.strip())
        filas += 1

matriz = []
for _ in range(filas):
    fila = [None] * columnas
    matriz.append(fila)

with open(file_path, "r") as file:
    for i, line in enumerate(file):
        for j, char in enumerate(line.strip()):
            matriz[i][j] = int(char)

resultado = 0
visitados = set()


def buscar_camino(matriz, fila, columna, fila_inicial, columna_inicial):
    filas, columnas = len(matriz), len(matriz[0])
    movimientos = {(-1, 0), (0, 1), (1, 0), (0, -1)}

    if (fila, columna, fila_inicial, columna_inicial) not in visitados and matriz[fila][columna] == 9:
        visitados.add((fila, columna, fila_inicial, columna_inicial))

    for movimiento in movimientos:
        x, y = movimiento
        nx = fila + x
        ny = columna + y
        if (0 <= nx < filas) and (0 <= ny < columnas) and (matriz[nx][ny] == matriz[fila][columna] + 1):
            buscar_camino(matriz, nx, ny, fila_inicial, columna_inicial)


for i in range(filas):
    for j in range(columnas):
        if matriz[i][j] == 0:
            buscar_camino(matriz, i, j, i, j)

print(len(visitados))

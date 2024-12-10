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
    resultado_aux = 0

    if matriz[fila][columna] == 9:
        resultado_aux += 1

    for movimiento in movimientos:
        x, y = movimiento
        nx = fila + x
        ny = columna + y
        if (0 <= nx < filas) and (0 <= ny < columnas) and (matriz[nx][ny] == matriz[fila][columna] + 1):
            resultado_aux += buscar_camino(matriz, nx, ny, fila_inicial, columna_inicial)

    return resultado_aux


for i in range(filas):
    for j in range(columnas):
        if matriz[i][j] == 0:
            resultado += buscar_camino(matriz, i, j, i, j)

print(resultado)

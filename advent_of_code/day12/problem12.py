file_path = "input_problem12"

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
            matriz[i][j] = char


def buscar_camino(matriz, fila, columna, visitados):
    filas, columnas = len(matriz), len(matriz[0])
    movimientos = {(-1, 0), (0, 1), (1, 0), (0, -1)}
    perimetro = 0
    area = 1

    visitados.add((fila, columna))

    for movimiento in movimientos:
        x, y = movimiento
        nx = fila + x
        ny = columna + y
        if nx < 0 or nx >= filas or ny < 0 or ny >= columnas:
            perimetro += 1
            continue
        if matriz[nx][ny] != matriz[fila][columna]:
            perimetro += 1
            continue
        if (nx, ny) in visitados:
            continue
        if matriz[nx][ny] == matriz[fila][columna]:
            area_aux, perimetro_aux = buscar_camino(matriz, nx, ny, visitados)
            area += area_aux
            perimetro += perimetro_aux

    return area, perimetro


visitados = set()
resultados = []

for i in range(filas):
    for j in range(columnas):
        if (i, j) not in visitados:
            valor_celda = matriz[i][j]
            area, perimetro = buscar_camino(matriz, i, j, visitados)

            resultados.append({"valor": valor_celda, "area": area, "perimetro": perimetro})
# print(resultados)
resultado_final = 0

for obj in resultados:
    producto = obj["area"] * obj["perimetro"]
    resultado_final += producto

print("El resultado final es:", resultado_final)

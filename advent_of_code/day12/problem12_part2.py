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
            area_aux, perimetro_aux, _ = buscar_camino(matriz, nx, ny, visitados)
            area += area_aux
            perimetro += perimetro_aux

    return area, perimetro, visitados


visitados = set()
resultados = []

for i in range(filas):
    for j in range(columnas):
        if (i, j) not in visitados:
            visitados_aux = set()
            valor_celda = matriz[i][j]
            area, perimetro, visitados_aux = buscar_camino(matriz, i, j, visitados_aux)
            visitados.update(visitados_aux)

            resultados.append({"valor": valor_celda, "area": area, "perimetro": perimetro, "mapa": visitados_aux})
# print(resultados)
resultado_final = 0


def calcular_lados(mapa):
    movimientos = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    movimientos_esquinas = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
    lados = 0
    esquinas_visitadas = set()
    numero_a_restar = 0
    esquinas_de_tres = 0
    for celda in mapa:
        x, y = celda
        for dx, dy in movimientos_esquinas:
            nx, ny = x + dx, y + dy
            if (nx, ny) in mapa:
                continue
            num_paredes = 0
            for dx2, dy2 in movimientos:
                nx2, ny2 = nx + dx2, ny + dy2
                if (nx2, ny2) in mapa:
                    num_paredes += 1
                    continue
            if ((nx, ny) not in esquinas_visitadas):
                if num_paredes == 0:
                    esquinas_visitadas.add((nx, ny))
                    esquinas_que_coinciden = 0
                    for dx3, dy3 in movimientos_esquinas:
                        nx3, ny3 = nx + dx3, ny + dy3
                        if (nx3, ny3) in mapa:
                            esquinas_que_coinciden += 1
                    if esquinas_que_coinciden > 1:
                        lados += esquinas_que_coinciden
                        numero_a_restar += 1
                    else:
                        lados += 1
                if num_paredes == 2:
                    esquinas_visitadas.add((nx, ny))
                    lados += 1
                if num_paredes == 3:
                    esquinas_visitadas.add((nx, ny))
                    esquinas_de_tres += 3
                    # lados += 3

                if num_paredes == 4:
                    esquinas_visitadas.add((nx, ny))
                    lados += 4
    calculo_esquinas_de_tres = esquinas_de_tres - numero_a_restar
    if calculo_esquinas_de_tres > 0:
        lados += calculo_esquinas_de_tres
    return lados


for resultado in resultados:
    mapa = resultado["mapa"]
    # print(mapa)
    lados = calcular_lados(mapa)
    resultado_final += resultado["area"] * lados
    print(f"Región {resultado['valor']} tiene {lados} lados.")

print("El resultado final es:", resultado_final)

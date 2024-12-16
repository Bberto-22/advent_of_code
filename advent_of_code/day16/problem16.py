file_path = "input_test"

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


def posicion_inicial(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == "S":
                return i, j


resultado = 0
fila_comienzo, columna_comienzo = posicion_inicial(matriz)


def recorrido(i, j):
    if matriz[i][j] == "E":
        return [(i, j)]

    if matriz[i][j] == "#":
        return []

    matriz[i][j] = -1
    if i > 0 and matriz[i - 1][j] in [".", "E"]:
        camino = recorrido(i - 1, j)
        if camino: return [(i, j)] + camino

    if j < len(matriz[i]) - 1 and matriz[i][j + 1] in [".", "E"]:
        camino = recorrido(i, j + 1)
        if camino: return [(i, j)] + camino

    if i < len(matriz) - 1 and matriz[i + 1][j] in [".", "E"]:
        camino = recorrido(i + 1, j)
        if camino: return [(i, j)] + camino

    if j > 0 and matriz[i][j - 1] in [".", "E"]:
        camino = recorrido(i, j - 1)
        if camino: return [(i, j)] + camino

    return []


camino_valido = []

for x in recorrido(fila_comienzo, columna_comienzo):
    if len(camino_valido) > 1:
        if (camino_valido[-1]["camino"][0] == camino_valido[-2]["camino"][0] and x[0] != camino_valido[-1]["camino"][
            0]) or (camino_valido[-1]["camino"][1] == camino_valido[-2]["camino"][1] and x[1] !=
                    camino_valido[-1]["camino"][1]):
            resultado += 1000
        else:
            resultado += 1
    camino_valido.append({"camino": x})
print(camino_valido)
print(resultado)

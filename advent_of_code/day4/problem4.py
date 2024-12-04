file_path = "input_problem4"


def search_word(matriz, i, j, palabra, direccion):
    filas = len(matriz)
    columnas = len(matriz[0])

    for k, letra in enumerate(palabra):
        x = i + k * direccion[0]
        y = j + k * direccion[1]

        if x < 0 or x >= filas or y < 0 or y >= columnas or matriz[x][y] != letra:
            return False
    return True


def get_valid(matriz, i, j, palabra):
    direcciones = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
    direcciones_correctas = 0
    for direccion in direcciones:
        if search_word(matriz, i, j, palabra, direccion):
            direcciones_correctas += 1
    return direcciones_correctas


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

resultado = 0
for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        if matriz[i][j] == "X":
            resultado += get_valid(matriz, i, j, "XMAS")

print(resultado)

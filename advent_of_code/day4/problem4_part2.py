file_path = "input_problem4"


def get_valid_x_mas(matriz, i, j):
    palabras_validas = ["SSMM", "MSMS", "SMSM", "MMSS"]
    palabra = ""
    direcciones = [(-1, -1), (-1, 1), (1, -1), (1, 1)]


    filas = len(matriz)
    columnas = len(matriz[0])

    for direccion in direcciones:
        x, y = i + direccion[0], j + direccion[1]
        if 0 <= x < filas and 0 <= y < columnas:
            palabra += matriz[x][y]
        else:
            palabra += " "

    for palabra_valida in palabras_validas:
        if palabra_valida == palabra:
            return True
    return False



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
        if matriz[i][j] == "A":
            if get_valid_x_mas(matriz, i, j):
                resultado += 1

print(resultado)

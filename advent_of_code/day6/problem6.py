file_path = "input_problem6"

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
            if matriz[i][j] == ">" or matriz[i][j] == "<" or matriz[i][j] == "^" or matriz[i][j] == "v":
                return i, j, matriz[i][j]
          
resultado = 1
fila_guardia, columna_guardia, direccion = posicion_inicial(matriz)    

while 1 <= fila_guardia < filas-1 and 1 <= columna_guardia < columnas-1:
    matriz[fila_guardia][columna_guardia] = "x"
    if direccion == "^":
        fila_guardia += -1
        if matriz[fila_guardia][columna_guardia] == "#":
            fila_guardia += 1
            direccion = ">"
        else:
            if matriz[fila_guardia][columna_guardia] == ".":
                resultado += 1
    elif direccion == ">":
        columna_guardia += 1
        if matriz[fila_guardia][columna_guardia] == "#":
            columna_guardia += -1
            direccion = "v"
        else:
            if matriz[fila_guardia][columna_guardia] == ".":
                resultado += 1
    elif direccion == "v":
        fila_guardia += 1
        if matriz[fila_guardia][columna_guardia] == "#":
            fila_guardia += -1
            direccion = "<"
        else:
            if matriz[fila_guardia][columna_guardia] == ".":
                resultado += 1
    elif direccion == "<":
        columna_guardia += -1
        if matriz[fila_guardia][columna_guardia] == "#":
            columna_guardia += 1
            direccion = "^"
        else:
            if matriz[fila_guardia][columna_guardia] == ".":
                resultado += 1

print(fila_guardia, columna_guardia)        
print(resultado)


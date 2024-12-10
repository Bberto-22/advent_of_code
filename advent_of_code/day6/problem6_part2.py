#file_path = r"C:\Users\alber\Desktop\projects\advent_of_code\advent_of_code\day6\input_problem6"
file_path = "input_problem6"
import copy

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
          
resultado = 0
fila_guardia, columna_guardia, direccion = posicion_inicial(matriz)   
def print_matriz(matriz):
    for fila in matriz:
        print("".join(str(x) for x in fila))
        
def is_stuck(fila_guardia, columna_guardia, direccion, matriz):
    filas, columnas = len(matriz), len(matriz[0])
    visitados = set()
    movimientos = {"^": (-1, 0), ">": (0, 1), "v": (1, 0), "<": (0, -1)}

    while 1 <= fila_guardia < filas and 1 <= columna_guardia < columnas:
        #if (fila_guardia, columna_guardia, direccion) in visitados:
            #print_matriz(matriz)
            #return True

        #visitados.add((fila_guardia, columna_guardia, direccion))

        dx, dy = movimientos[direccion]
        nueva_fila, nueva_columna = fila_guardia + dx, columna_guardia + dy

        if not (0 <= nueva_fila < filas and 0 <= nueva_columna < columnas):
            break
        if matriz[nueva_fila][nueva_columna] == direccion:
            return True

        if matriz[nueva_fila][nueva_columna] == "#":
            direccion = {"^": ">", ">": "v", "v": "<", "<": "^"}[direccion]
        else:
            matriz[nueva_fila][nueva_columna] = direccion
            fila_guardia, columna_guardia = nueva_fila, nueva_columna

    return False


for i in range(filas):
        for j in range(columnas):

            if matriz[i][j] == ".":
                matriz_aux = copy.deepcopy(matriz)
                matriz_aux[i][j] = "#"

                if is_stuck(fila_guardia, columna_guardia, direccion, matriz_aux):
                    resultado += 1
                    print(resultado)
            

print(fila_guardia, columna_guardia)        
print(resultado)


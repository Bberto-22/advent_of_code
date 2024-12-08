file_path = "input_problem8"

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

import re

def buscar_posiciones(matriz):
    posiciones = {}
    patron = re.compile(r"[a-zA-Z0-9]")
    for i, fila in enumerate(matriz):
        for j, char in enumerate(fila):
            if patron.match(char):
                if char not in posiciones:
                    posiciones[char] = []
                posiciones[char].append((i, j))
                
    return posiciones
                
posiciones_antenas = buscar_posiciones(matriz)

antinodos = set()
for antena, posiciones in posiciones_antenas.items():
    for i, (x1, y1) in enumerate(posiciones):
            for j, (x2, y2) in enumerate(posiciones):
                if i == j:
                    continue
                dx, dy = x2 - x1, y2 - y1
                
                nuevas_posiciones = [
                    (x1 - dx, y1 - dy),
                    (x1 + dx, y1 + dy),
                    (x2 + dx, y2 + dy),
                    (x2 - dx, y2 - dy),
                ]

                for nx, ny in nuevas_posiciones:
                    if (nx == x1 and ny == y1) or (nx == x2 and ny == y2):
                        break
                    if 0 <= nx < filas and 0 <= ny < columnas:
                        if (nx, ny) not in antinodos:
                            antinodos.add((nx, ny))
                            
print(len(antinodos))
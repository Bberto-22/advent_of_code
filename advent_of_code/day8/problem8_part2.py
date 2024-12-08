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
                if (x1, y1) not in antinodos:
                                antinodos.add((x1, y1))
                if (x2, y2) not in antinodos:
                                antinodos.add((x2, y2))
                dx, dy = x2 - x1, y2 - y1

                n = 1
                nx = x2
                ny = y2
                while n >= 0: 
                    if n == 1:
                        nx += dx
                        ny += dy
                        if 0 <= nx < filas and 0 <= ny < columnas:
                            if (nx, ny) not in antinodos:
                                antinodos.add((nx, ny))
                        else:
                            n -= 1
                            nx = x1
                            ny = y1
                    else:
                        nx -= dx
                        ny -= dy
                        if 0 <= nx < filas and 0 <= ny < columnas:
                            if (nx, ny) not in antinodos:
                                antinodos.add((nx, ny))
                        else:
                            n -= 1
                        
                            
print(len(antinodos))
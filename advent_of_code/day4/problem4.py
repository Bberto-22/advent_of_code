file_path = "input_problem4"

def get_valid(matriz, i, j, letra):
	for x in range(i - 1, i + 2):
        	for y in range(j - 1, j + 2):
        		if matriz[x][y] == letra:
        			return x, y
        		

filas = 0
columnas = 0
with open(file_path, "r") as file:
	for i, line in enumerate(file):
		if i == 0:
			columnas = len(line.strip())
		filas += 1
		
print(filas)
print(columnas)
		
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
        	x, y = get_valid(matriz, i, j, "M")
        	x, y = get_valid(matriz, x, y, "A")
        	if get_valid(matriz, i, j, "S"):
        		resultado += 1

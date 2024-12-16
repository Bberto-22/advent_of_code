file_path = "input_problem16"

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


def es_giro(direccion_anterior, direccion_actual):
    # Determina si se ha producido un giro
    if direccion_anterior is None:
        return False
    if (direccion_anterior == "arriba" and direccion_actual in ["izquierda", "derecha"]) or \
            (direccion_anterior == "abajo" and direccion_actual in ["izquierda", "derecha"]) or \
            (direccion_anterior == "izquierda" and direccion_actual in ["arriba", "abajo"]) or \
            (direccion_anterior == "derecha" and direccion_actual in ["arriba", "abajo"]):
        return True
    return False


def buscar_caminos(matriz, i, j, visitados, camino_actual, caminos, direccion_anterior=None, primer_movimiento=True):
    # Si llegamos a la meta, agregamos el camino actual a los caminos válidos
    if matriz[i][j] == "E":
        caminos.append(list(camino_actual))
        return

    # Marcar la posición como visitada
    visitados.add((i, j))

    # Direcciones posibles y sus nombres
    direcciones = [
        (i - 1, j, "arriba"),
        (i + 1, j, "abajo"),
        (i, j - 1, "izquierda"),
        (i, j + 1, "derecha")
    ]

    for ni, nj, direccion_actual in direcciones:
        if (0 <= ni < len(matriz) and 0 <= nj < len(matriz[0])  # Dentro del rango
                and (ni, nj) not in visitados  # No visitado
                and matriz[ni][nj] in [".", "E"]):  # Celda válida
            # Calcular puntos extra si hay un giro
            if primer_movimiento and direccion_actual != "derecha":
                puntos_extra = 1001
            else:
                puntos_extra = 1001 if es_giro(direccion_anterior, direccion_actual) else 1

            # Agregar al camino actual con los puntos acumulados
            camino_actual.append(((ni, nj), puntos_extra))

            # Recursión para explorar la siguiente posición
            buscar_caminos(matriz, ni, nj, visitados, camino_actual, caminos, direccion_actual, primer_movimiento=False)

            # Volver atrás (backtracking)
            camino_actual.pop()

    # Desmarcar la posición actual como visitada
    visitados.remove((i, j))


def calcular_puntos(camino):
    # Calcular la puntuación total de un camino
    return sum(puntos for _, puntos in camino)


def encontrar_camino_optimo(matriz):
    # Encontrar la posición inicial
    fila_comienzo, columna_comienzo = posicion_inicial(matriz)

    # Lista para almacenar todos los caminos válidos
    caminos = []

    # Iniciar la búsqueda desde la posición inicial
    buscar_caminos(matriz, fila_comienzo, columna_comienzo, set(), [((fila_comienzo, columna_comienzo), 0)], caminos)

    # Buscar el camino con la menor puntuación
    camino_optimo = min(caminos, key=calcular_puntos, default=None)

    if camino_optimo is not None:
        return camino_optimo, calcular_puntos(camino_optimo)
    else:
        return None, float('inf')


camino_optimo, puntuacion = encontrar_camino_optimo(matriz)

if camino_optimo:
    print("Camino óptimo:", [pos for pos, _ in camino_optimo])
    print("Puntuación mínima:", puntuacion)
else:
    print("No se encontró un camino válido.")

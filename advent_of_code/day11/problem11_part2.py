import concurrent.futures

file_path = "input_problem11"

# Leer el archivo y llenar la lista
lista = []
with open(file_path, "r") as file:
    for line in file:
        lista.extend(line.split())

print(lista)

# Función que procesa cada número según las reglas dadas (optimizada para evitar crecimiento descontrolado)
def procesar_numero(numero):
    actual = [numero]  # Lista inicial con el número dado
    for i in range(45):
        print(f"Bucle {i}")
        siguiente = []  # Lista para almacenar los números generados en la siguiente iteración
        for num in actual:
            if num == "0":
                siguiente.append("1")
            elif len(num) % 2 == 0:
                parte1 = int(num[:len(num) // 2])
                parte2 = int(num[len(num) // 2:])
                siguiente.append(str(parte1))
                siguiente.append(str(parte2))
            else:
                new_stone = int(num) * 2024
                siguiente.append(str(new_stone))
        actual = siguiente  # Pasa al siguiente nivel

    return len(actual)  # Devuelve el tamaño de la lista final


with concurrent.futures.ProcessPoolExecutor() as executor:
    resultados = list(executor.map(procesar_numero, lista))

resultado_final = sum(resultados)  # Sumar los resultados de cada número
print("Resultado final (total de elementos):", resultado_final)

file_path = "input_problem5"

relaciones = {}
listas = []

with open(file_path, "r") as file:
    for line in file:

        line = line.strip()

        if not line:
            break

        if "|" in line:
            clave, referencia = line.split("|")

        if clave not in relaciones:
            relaciones[clave] = []

        if referencia not in relaciones[clave]:
            relaciones[clave].append(referencia)

    for line in file:
        line = line.strip()
        if line:
            listas.append(line.split(","))

resultado = 0

for lista in listas:
    lista_original = lista[:]  # Guardamos la lista original para comparar al final
    is_valid = True
    i = 0

    # Recorremos la lista para verificar si es válida
    while i < len(lista):
        numero_actual = lista[i]

        if numero_actual in relaciones:
            referencias = relaciones[numero_actual]

            for j in range(i + 1, len(lista)):
                num_posterior = lista[j]

                if numero_actual in relaciones.get(num_posterior, []):
                    lista[i], lista[j] = lista[j], lista[i]

                    is_valid = False

                    i = -1 #restart process with new order
                    break

        i += 1
        
    if not is_valid:
        resultado += int(lista[len(lista) // 2])

print(resultado)

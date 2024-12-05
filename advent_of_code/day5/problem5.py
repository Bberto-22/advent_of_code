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
    is_valid = True
    for i in range(len(lista)):
        numero_actual = lista[i]

        if numero_actual in relaciones:
            referencias = relaciones[numero_actual]
            for num_posterior in lista[i + 1:]:
                if numero_actual in relaciones.get(num_posterior, []):
                    is_valid = False
                    break
        if not is_valid:
            break
    if is_valid:
        resultado += int(lista[int(len(lista) / 2)])

print(resultado)

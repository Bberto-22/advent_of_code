file_path = "input_problem11"

lista = []

with open(file_path, "r") as file:
    for line in file:
        lista.extend(line.split())

print(lista)
for blink in range(25):
    print(f"Blink número {blink}")
    i = 0
    while i < len(lista):
        if lista[i] == "0":
            lista[i] = "1"
            i += 1
            continue

        if len(lista[i]) % 2 == 0:
            parte1 = int(lista[i][:len(lista[i]) // 2])
            parte2 = int(lista[i][len(lista[i]) // 2:])
            lista.insert(i, str(parte1))
            lista[i + 1] = str(parte2)
            i += 2
            continue
        else:
            new_stone = int(lista[i]) * 2024
            lista[i] = str(new_stone)
            i += 1
    # print(lista)

print(len(lista))

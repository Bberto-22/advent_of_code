import re

file_path = "input_problem13"

with open(file_path, "r") as file:
    lines = file.readlines()

results = []
for i in range(0, len(lines), 4):
    if i + 2 >= len(lines):
        break

    line_a = lines[i].strip()
    match_a = re.search(r"Button A: X\+([0-9]+), Y\+([0-9]+)", line_a)
    if match_a:
        ax, ay = int(match_a.group(1)), int(match_a.group(2))

    line_b = lines[i + 1].strip()
    match_b = re.search(r"Button B: X\+([0-9]+), Y\+([0-9]+)", line_b)
    if match_b:
        bx, by = int(match_b.group(1)), int(match_b.group(2))

    line_prize = lines[i + 2].strip()
    match_prize = re.search(r"Prize: X=([0-9]+), Y=([0-9]+)", line_prize)
    if match_prize:
        prizex, prizey = int(match_prize.group(1)), int(match_prize.group(2))

    results.append({"ax": ax, "ay": ay, "bx": bx, "by": by, "prizex": prizex, "prizey": prizey})

resultado_final = 0
# Mostrar resultados
for result in results:
    # print(result)
    posibles = []
    is_valid = False
    i = 1
    j2 = 0
    i2 = 0
    while i < 100:
        es_premio = False
        x_result = result["ax"] * i
        for j in range(100, 0, -1):
            # if j >= 100:
            #     break
            prize_x = x_result + result["bx"] * j
            # if prize_x > result["prizex"]:
            #     break
            if prize_x == result["prizex"]:
                j2 = j
                break

        y_result = result["ay"] * i
        for j in range(100, 0, -1):
            # if j >= 100:
            #     break
            prize_y = y_result + result["by"] * j
            # if prize_y > result["prizey"]:
            #     break
            if prize_y == result["prizey"]:
                if j2 == j:
                    es_premio = True
                    break

        if es_premio:
            i2 = i
            token = i * 3 + j2 * 1
            posibles.append(token)

        i += 1

        if x_result > result["prizex"] or y_result > result["prizey"]:
            break

    if len(posibles) > 0:
        # print(result)
        print(posibles)
        tokens = min(posibles)
        resultado_final += tokens
        # print(f"Valor X: {i2}, Valor Y: {j2}, cuesta {tokens} tokens")
    # else:
    #     print("No tiene solución")

print(f"Resultado: {resultado_final}")

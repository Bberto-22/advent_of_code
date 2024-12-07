file_path = "input_problem7"
#file_path = r"C:\Users\alber\Desktop\projects\advent_of_code\advent_of_code\day7\input_problem7"

def generar_operadores(n):
    operadores = ["+", "*", "||"]
    combinaciones = []
    if n == 1:
        combinaciones = []
        for op in operadores:
            combinaciones.append([op])  # Cada operador es una lista individual
        return combinaciones
    
    for op in operadores:
        for subcombinacion in generar_operadores(n - 1):
            combinaciones.append([op] + subcombinacion)
    return combinaciones


def is_valid(combinaciones, resultado, numeros):
    for combinacion in combinaciones:
        resultado_calculado = numeros[0]
        for i in range(len(combinacion)):
            operador = combinacion[i]
            siguiente_numero = numeros[i + 1]
            
            if operador == "+":
                resultado_calculado += siguiente_numero
            elif operador == "*":
                resultado_calculado *= siguiente_numero
            elif operador == "||":
                resultado_calculado = int(str(resultado_calculado) + str(siguiente_numero))
                
            if resultado == resultado_calculado:
                return True
    return False

resultado_final = 0
with open(file_path, "r") as file:
    for line in file:
        resultado, numeros = line.strip().split(":")
        
        resultado = int(resultado)
        
        numeros = list(map(int, numeros.strip().split()))
        combinaciones = generar_operadores(len(numeros)-1)
        
        if is_valid(combinaciones, resultado, numeros):
            resultado_final += resultado
        
print(resultado_final)
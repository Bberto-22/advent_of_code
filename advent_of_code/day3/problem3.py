file_path = "input_problem3"

import re

with open(file_path, "r") as file:
	text = file.read()
	matches = re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", text)
	
results = 0

for number1, number2 in matches:
    mul = int(number1) * int(number2)

    results += mul

	
print(results)

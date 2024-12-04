file_path = "input_problem3"

import re

def get_start_position(match):
    return match["start"]

with open(file_path, "r") as file:
	text = file.read()

dont_matches = re.finditer(r"don't\(\)", text)
do_matches = re.finditer(r"do\(\)", text)
mul_matches = re.finditer(r"mul\((\d{1,3}),(\d{1,3})\)", text)
matches = []

for match in dont_matches:
    matches.append({"type": "dont", "value": None, "start": match.start()})

for match in do_matches:
    matches.append({"type": "do", "value": None, "start": match.start()})

for match in mul_matches:
    x, y = match.groups()
    value = int(x) * int(y)
    matches.append({"type": "mul", "value": value, "start": match.start()})
	
results = 0

sorted_matches = sorted(matches, key=get_start_position)

is_valid=True
for match in sorted_matches:
	if match["type"] == "do":
		is_valid=True
	if match["type"] == "dont":
		is_valid=False
	elif match["type"] == "mul" and is_valid:
        	results += match["value"]

print(results)

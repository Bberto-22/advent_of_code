file_path = "input_problem2"

safe_reports = 0

with open(file_path, "r") as file:
    for line in file:
        levels = list(map(int, line.split()))
        is_increasing = all(1 <= b - a <= 3 for a, b in zip(levels, levels[1:]))
        is_decreasing = all(1 <= a - b <= 3 for a, b in zip(levels, levels[1:]))
        if is_increasing or is_decreasing:
            safe_reports += 1
	
print(safe_reports)

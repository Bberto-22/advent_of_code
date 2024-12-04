file_path = "input_problem2"

def is_increasing(levels):
    return all(1 <= b - a <= 3 for a, b in zip(levels, levels[1:])) and all(b > a for a, b in zip(levels, levels[1:]))

def is_decreasing(levels):
    return all(1 <= a - b <= 3 for a, b in zip(levels, levels[1:])) and all(a > b for a, b in zip(levels, levels[1:]))

def is_safe(levels):
    if is_increasing(levels) or is_decreasing(levels):
        return True
    
    for i in range(len(levels)):
        modified_levels = levels[:i] + levels[i+1:]
        if is_increasing(modified_levels) or is_decreasing(modified_levels):
            return True
    return False

safe_reports = 0

with open(file_path, "r") as file:
    for line in file:
        levels = list(map(int, line.split()))
        if is_safe(levels):
            safe_reports += 1
	
print(safe_reports)

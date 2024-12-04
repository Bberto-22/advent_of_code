from collections import Counter

file_path = "input_problem1"


left_list = []
right_list = []

with open(file_path, "r") as file:
	for line in file:
		lists = line.split()
		left_list.append(int(lists[0]))
		right_list.append(int(lists[1]))
		
sorted_left_list = sorted(left_list)
sorted_right_list = sorted(right_list)

right_count = Counter(sorted_right_list)


total_distance = 0
"""
for left_number in sorted_left_list:
	match_times = 0
	for right_number in sorted_right_list:
		if left_number < right_number:
			break
		if left_number == right_number:
			match_times += 1
			
	distance = left_number * match_times
	total_distance += distance
"""	
	
for left_number in sorted_left_list:
	match_times = right_count[left_number]
	distance = left_number * match_times
	total_distance += distance
	
print(total_distance)

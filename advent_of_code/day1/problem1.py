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


total_distance = 0

for left_number, right_number in zip(sorted_left_list, sorted_right_list):
	distance = abs(left_number - right_number)
	total_distance += distance
	
print(total_distance)

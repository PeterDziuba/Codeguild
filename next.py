students_by_class = {}

loops_counter = True
while loops_counter:
	print("Student name? Or done.")
	student_name = input()
	loops_counter = student_name != 'done'
	if loops_counter:
		print('What class is', student_name, 'in?')
		class_name = input()

		if class_name in students_by_class:
			old_roster = students_by_class[class_name]
		else:
			old_roster = set()

		new_roster = old_roster | {student_name}
		students_by_class[class_name] = new_roster

print(students_by_class)

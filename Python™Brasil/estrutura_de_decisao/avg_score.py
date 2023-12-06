"""Create a program for reading two partial grades of a student. The program should calculate the average score and display:

The message "Approved" if the average is greater than or equal to seven;
The message "Failed" if the average is less than seven;
The message "Approved with Distinction" if the average is equal to ten."""

grade_a = float(input("Enter your first grade: "))
grade_b = float(input("Enter your second grade: "))

avg = (grade_a + grade_b) / 2


if avg == 10:
	print("Approved with Distinction!")
elif avg >= 7:
	print("Approved!")
else:
	print("Failed...")

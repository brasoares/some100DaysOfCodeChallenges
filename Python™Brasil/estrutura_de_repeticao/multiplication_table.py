"""Develop a multiplication table generator, capable of generating the multiplication table of any integer between 1 to 10. The user should inform which number they want to see the multiplication table of. The output should be as follows: Multiplication table of 5: 5 X 1 = 5 
5 X 2 = 10 
… 
5 X 10 = 50"""

while True:
	try:
		x = int(input("Which table do you want calculated? "))
		if 1 <= x <=10:
			break
		else:
			print("Please, enter a number between 1 and 10: ")
	except ValueError:
		print("Invalid input. Please enter a valid integer: ")

print(f"The multiplication table of {x}:")

for i in range(1, 11):
	print(f"{x} x {i} = {x*i}")

#Create a program that asks for a value and displays on the screen whether the value is positive or negative.
n = float(input("Please, provide any value as an input: "))

if n > -1:
	print(f"The entered value of {n:.0f} is positive.")
else:
	print(f"The entered value of {n:.0f} is negative.")

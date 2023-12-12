# Create a program that reads three numbers and displays the largest among them all.

n1 = float(input("Enter the first number: "))
n2 = float(input("Enter the second number: "))
n3 = float(input("Enter the third number: "))

if n1 > n2 and n1 > n3:
	print(f"{n1:.0f}")
elif n2 > n1 and n2 > n3:
	print(f"{n2:.0f}")
elif n1 == n2 and n1 == n3:
	print(f"Identical numbers entered thrice: {n2:.0f}")
else:
	print(f"{n3:.0f}")

"""Create a program that calculates the roots of a quadratic equation in the form ax^2 + bx + c. The program should prompt the user for the values of a, b, and c and perform the necessary checks, providing information to the user in the following situations:

🅰️ **If the user enters a value of A equal to zero:**
   The equation is not quadratic, and the program should not prompt for the other values. It should be terminated.
🅱️ **If the calculated delta is negative:**
   The equation has no real roots. Notify the user and terminate the program.
🄲 **If the calculated delta is zero:**
   The equation has a single real root. Inform the user about it.
🄳 **If the delta is positive:**
   The equation has two real roots. Inform the user about both roots."""
import math 

a = float(input("Enter a's value: "))
b = float(input("Enter b's value: "))
c = float(input("Enter c's value: "))

delta = pow(b, 2) - 4*a*c 

if a == 0:
	print("End of execution; not a quadratic equation (check a's value)!")
elif delta == 0:
	if a != 0:	
		root = -b / (2*a)
		print(f"The equation has a single real root. Delta = 0 and the root is {root}.")
elif delta > 0:
	root1 = (-b + math.sqrt(delta)) / (2*a)
	root2 = (-b - math.sqrt(delta)) / (2*a)
	# printing both roots
	print(f"The equation has two real roots: ")
	print(f"Root 1: {root1}")
	print(f"Root 2: {root2}")
elif delta < 0:
	print("The equation has no real roots!")

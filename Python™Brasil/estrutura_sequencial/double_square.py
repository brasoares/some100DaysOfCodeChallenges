# Create a program that calculates the area of a square, then shows the user double this area.

import math

side = float(input("Please, inform the square's side measure: "))
doubled_area = 2 * (pow(side, 2))

print(f"The double of the square's area is {doubled_area}")

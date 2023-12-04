"""Create a program for a paint store. The program should ask for the size in square meters of the area to be painted. Consider that the paint coverage is 1 liter for every 3 square meters and that the paint is sold in 18-liter cans, which cost R$ 80.00. Inform the user about the quantities of paint cans to be purchased and the total price."""
# requests total area to be painted plus defines the yield per liter
import math

area = float(input("Please, inform the total area to be painted (in square meters): "))
paint_yield = 3 # square meters (per liter)

# amount of paint needed:
amount_of_paint = math.ceil(area / paint_yield)
total_cans = math.ceil(amount_of_paint/18)
# price
can_price = 80.0
full_cost = can_price * total_cans

print(f"Total cans needed: {total_cans}")
print(f"Full cost: R$ {full_cost}")

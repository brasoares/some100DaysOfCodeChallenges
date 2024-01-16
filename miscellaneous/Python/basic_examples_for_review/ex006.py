'''
Ask how many slices of pizza the user started with and ask
how many slices they have eaten.
Work out how many slices they have left and display the answer
in a user-friendly format.
'''

print("Please, just provide positive numbers!")
starting_point = int(input("How many slices did you start with? "))
eaten_amount = int(input("How many have you eaten? "))

slices_left = starting_point - eaten_amount

print(f"You have {slices_left} slices left :)!")

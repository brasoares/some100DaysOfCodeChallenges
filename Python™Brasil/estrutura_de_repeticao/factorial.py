"""Create a program that calculates the factorial of an integer provided by the user. Example: 5! = 5.4.3.2.1 = 120."""

while True:
    try:
        number = int(input("Type an integer: "))
        break
    except ValueError:
        print("Please, insert a valid integer.")

factorial = 1  # Initialize the factorial variable with 1

for i in range(1, number + 1):
    factorial *= i

print(f"The factorial of {number} is {factorial}")

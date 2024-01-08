import math

# Define which operation to perform
print("Welcome to the Calculator!")
print("To calculate, type '1' for power or '2' for square root. To exit, type '0'.")

choice = ''
while choice != '0':
    choice = input("Your choice: ")

    if choice == '1':
        print("Great! You chose to calculate the power of a number. Let's get started:")
        base = float(input("Enter the base: "))
        exponent = float(input("Enter the exponent: "))
        result = pow(base, exponent)
        print(f"The result of {base:.2f} raised to the power of {exponent:.2f} is {result:.2f}.")
    elif choice == '2':
        print("Awesome! You chose to calculate the square root of a number. Let's proceed: ")
        number = float(input("Enter the number for square root calculation: "))
        result = math.sqrt(number)
        print(f"The square root of {number:.2f} is {result:.2f}.")
    elif choice == '0':
        print("Exiting the calculator. Goodbye!")
    else:
        print("Invalid choice. Please enter '1', '2', or '0' to exit.")    

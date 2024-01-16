# Ask for the user’s first name and then ask for their surname and display the output message
# Hello [First Name] [Surname].

first_name = input("Provide your first name: ")
surname = input("Now, please provide your surname: ")

# Using f-string
print(f"Hello, {first_name} {surname}.")

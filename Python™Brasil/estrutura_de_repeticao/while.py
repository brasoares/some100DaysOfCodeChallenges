"""Make a program that asks for a grade, between zero and ten. Show a message if the value is invalid and keep asking until the user provides a valid value"""

while True:
  grade = float(input("Please, enter a grade between 0 and 10: "))
  if 0 <= grade <= 10:
    break # Exit the loop once the grade is valid.
  else:
    print("Invalid input. Please, try again.")

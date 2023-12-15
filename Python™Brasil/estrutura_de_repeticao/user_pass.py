"""The translation of your text from Portuguese to English is: “Make a program that reads a username and password and does not accept the password equal to the username, showing an error message and asking for the information again."""

name = input("Please, state your name: ")

# For the purpose of this small algorithm I will consider only lowercase, the idea is to test the logic

while True:
  psswd = input("Now choose a password: ")
  if psswd.lower() == name.lower():
    print("Your password must not be your name. Please, try again: ")
  else:
    print("Your name and password have been successfully set!")
    break

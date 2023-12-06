# Create a program that checks if a typed letter is a vowel or a consonant.
letter = input("Type in one only letter from the English alphabet: ").lower()

vowels = ['a', 'e', 'i', 'o', 'u', 'y']

if len(letter) == 1:
	# Check if the character is from the English alphabet
	if letter.isalpha() and letter.isascii():
		if letter in vowels:
			print(f"The typed char is '{letter.upper()}', and it's a vowel.")
		else:
			print(f"The typed char is '{letter.upper()}', and it's a consonant.")
	else:
		print("The entered character is not one from the English alphabet.")
else:
	print("You need to type an only valid character to check if it is or not a vowel.")

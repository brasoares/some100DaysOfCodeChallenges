'''
Ask the user to enter three numbers.
Add together the first two numbers and then multiply this total by the third.
Display the answer as 'The answer is [answer].
'''

n1 = int(input("Enter the first integer: "))
n2 = int(input("Enter the second integer: "))
n3 = int(input("Enter the third integer: "))

sum = n1 + n2
answer = sum * n3

print(f"The answer is: {answer}.")

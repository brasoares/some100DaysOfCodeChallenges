'''
Task the user to enter a number over 100 and then enter a number under
10 and tell them how many times the smaller number goes into larger
number in a user-friendly format.
'''

numberOver = int(input("Enter a number over 100: "))
numberLower = int(input("Enter a number under 10: "))

times = numberOver/numberLower

print(f"{numberLower} goes {times} times inside {numberOver}!")

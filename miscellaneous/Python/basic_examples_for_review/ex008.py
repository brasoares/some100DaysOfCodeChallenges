'''
Ask for the total price of the bill, then ask how
many diners there are. Divide the total bill by the 
number of diners and show how much each
person must pay.
'''

bill_amount = float(input("Enter bill's total price: "))

while True:
    diners_count = int(input("How many diners are there? "))
    if diners_count > 0:
        break
    else:
        print("Please enter a valid positive number of diners. ")

if diners_count != 0:
    pay_per_diner = bill_amount / diners_count
    print(f"Each person must pay: ${pay_per_diner:.2f}")
else:
    print("Cannot divide by zero. Please, restart!")

'''
Ask for the total price of the bill, then ask how
many diners there are. Divide the total bill by the 
number of diners and show how much each
person must pay.
'''

bill_amount = float(input("Enter bill's total price: "))
diners_count = int(input("How many diners are there? "))

pay_per_diner = bill_amount / diners_count

"""Create a program that asks how much you earn per hour and the number of hours worked in the month. 
Calculate and show the total of your salary for the referred month, knowing that 11% is deducted for Income Tax, 8% for Social Security (INSS), and 5% for the union. 
Make a program that gives us:
- Gross salary.
- How much was paid to Social Security.
- How much was paid to the union.
- Net salary.
Calculate the discounts and the net salary, according to the table below:
- Gross Salary: R$
- Income Tax (11%): R$
- Social Security (8%): R$
- Union (5%): R$
- Net Salary: R$
Note: Gross Salary - Discounts = Net Salary."""

# Set to Brazilian Portuguese locale
import locale
locale.setlocale(locale.LC_ALL, 'pt_BR.utf8')

worker = input("Please, enter your name: ")
hourly_rate, worked_hours = map(float, input(f"Hello, {worker}! Please, separating by a comma, provide the hourly rate value plus the amount of worked hours to have your salary calculated? ").split(','))

gross_salary = hourly_rate * worked_hours
irs = gross_salary * 0.11
social_security = gross_salary * 0.08
union_amount = gross_salary * 0.05
discounts = social_security + union_amount + irs
net_salary = gross_salary - discounts

# Format numbers 
gross = locale.format_string("%.2f", gross_salary, grouping=True)
irs = locale.format_string("%.2f", irs, grouping=True)
social = locale.format_string("%.2f", social_security, grouping=True)
union = locale.format_string("%.2f", union_amount, grouping=True)
salary = locale.format_string("%.2f", net_salary, grouping=True)
print("- Your Gross Salary: R$ {}.\n- Your Income Tax (11%): R$ {}.\n- Social Security (8%): R$ {}.\n- Union amount: R$ {}.\n- Net Salary: R$ {}".format(gross, irs, social, union, salary))

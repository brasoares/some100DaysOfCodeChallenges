"""A fruit shop is selling fruits with the following price table:

|             | Up to 5 Kg | Over 5 Kg |
|-------------|------------|-----------|
| Strawberry  | R$ 2.50/Kg | R$ 2.20/Kg|
| Apple       | R$ 1.80/Kg | R$ 1.50/Kg|

If the customer buys more than 8 Kg of fruits or if the total purchase value exceeds R$ 25.00, they will also receive a discount of 10% on this total. Write an algorithm to read the quantity (in Kg) of strawberries and the quantity (in Kg) of apples purchased and write the amount to be paid by the customer."""
import locale
# Set the locale to Brazilian Portuguese
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

strawberries = float(input("Enter the quantity of strawberries (in Kg): "))
apples = float(input("Enter the quantity of apples (in Kg): "))

strawberries_price = 0
apples_price = 0
total_price = 0

if strawberries < 0 or apples < 0:
    print("Not possible for the context; run the py over and try again.")
elif strawberries < 5.01 and apples < 5.01:
    strawberries_price = strawberries * 2.5
    apples_price = apples * 1.8
elif strawberries > 5.0 and apples > 5.0:
    strawberries_price = strawberries * 2.2
    apples_price = apples * 1.5
elif strawberries > 5.0 and apples < 5.01:
    strawberries_price = strawberries * 2.2
    apples_price = apples * 1.8
elif strawberries < 5.01 and apples > 5.0:
    strawberries_price = strawberries * 2.5
    apples_price = apples * 1.5

total_price = apples_price + strawberries_price

if strawberries + apples > 8.0 or total_price > 25.0:
    total_price = total_price - (total_price * 0.1)

# Applying locale.currency to print in BRL format
print(f"You will need to pay R$ {locale.currency(total_price, grouping=True)} for your purchase.")

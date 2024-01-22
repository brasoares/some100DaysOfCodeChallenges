# Store table data as lists
comparison_operators_table = [["Operator, Description"], ["==", "Equal to"], ["!=", "Not equal to"], [">", "Greater than"], ["<", "Less than"], [">=", "Greater than or equal to"], ["<=", "Less than or equal to"]]
logical_operators_table = [["and", "Both conditions must be met"], ["or", "Either condition must be met"]]

# Printing tables with formatting
print("Comparison Operators")
for row in comparison_operators_table:
    print("{:<15} {:<27}".format(*row))

print("\nLogical Operators")
for row in logical_operators_table:
    print("{:<15 {:<27}}.format(*row)")

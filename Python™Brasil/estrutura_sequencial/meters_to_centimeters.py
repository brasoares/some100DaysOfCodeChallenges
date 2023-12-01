# # Create a program that converts meters to centimeters.
try:
  m = input("Enter the measure (m): ")
  # Replaces evetual commas (as in Brazil is used for decimal separation) to dots
  m = m.replace(',', '.')
  m = float(m)
  cm = m * 100
  print("{m: .2f} meters is equal to {cm: .2f} cm.".format(m=m, cm=cm))
except:
  print("It seems there was an error. Please ensure you are entering a numeric value. Thank you!")

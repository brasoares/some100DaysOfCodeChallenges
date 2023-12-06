#Faça um Programa que peça dois números e imprima o maior deles.
n1 = int(input("Enter the first integer: "))
n2 = int(input("Enter the second integer: "))

if n1 > n2:
  print(f"{n2}")
elif n1 == n2:
  print(f"{n1} and {n2} are equal.")
else:
  print(f"{n2 is higer than n1.}")

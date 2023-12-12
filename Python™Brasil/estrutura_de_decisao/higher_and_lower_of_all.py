"""Make a program that reads three numbers and shows the largest and smallest of them"""

n1 = float(input("Enter the 1ˢᵗ #: "))
n2 = float(input("Enter the 2ⁿᵈ #: "))
n3 = float(input("Enter the 3ʳᵈ #: "))

if n1 > n2 and n1 > n3:
	higher = n1
elif n2 > n1 and n2 > n3:
	higher = n2
elif n3 > n1 and n3 > n2:
	higher = n3
else:
	if n1 == n2 and n2 == n3:
		higher = n2

if n1 < n2 and n1 < n3:
	lower = n1
elif n2 < n1 and n2 < n3:
	lower = n2
elif n3 < n1 and n3 < n2:
	lower = n3
else:
	if n1 == n2 and n2 == n3:
		lower = n2

print(f"The smallest input is #{lower:.0f}, and the higher input is #{higher:.0f}.")
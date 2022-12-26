"""

You want to buy something at multiple prices. Make a script that calculates what the total price is.

"""

amount = int(input("How many would you like to buy? "))

calc = [8,
		12,
		4,
		2,
		120,
		]

total = 0

for number in calc:
	total += amount * number

print(total)
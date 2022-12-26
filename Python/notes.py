"""

Write a basic calculator that can supports addition, subtraction, fraction and multiplication. This calculator should
support floats. Use proper variable and function names.
1. Implement a looping menu that asks for any of the four operations and includes a fifth option to quit the
program.
2. Implement functions for all four operations, these functions should all accept two arguments: the first and the
second number.
3. When the user chooses an operation, ask for the required numbers and send these to the correct functions.
Print the result.

"""
def Welcome():
	operation = input('''Would you like to add or substract? Type:
		+ for addition
		- for substraction
		* for multiplication
		/ for division
		. to exit the program
		''')
	return operation


def Calculator():

	while True:
		operation = Welcome()

		#I've wrapped the input() function in the float() function in order to support floating point numbers.
		fnum = float(input("What is the first number? "))
		snum = float(input("What is the second number? "))

		#I've added if and elif statements to decide whether an addition or substraction will be performed.
		#The else statement is ther to handle an error if the user did not input an operator symbol

		#String formatters are here to help properly format the text and provide feedback
		#When you run the program with the .format method, 
		#It will show the mathematical expression that is being performed by the progaram.
		if operation == '+':
			print('{} + {} = '.format(fnum, snum))
			print(fnum + snum)

		elif operation == '-':
			print('{} - {} = '.format(fnum, snum))
			print(fnum - snum)

		elif operation == '*':
			print('{} * {} = '.format(fnum, snum))
			print(fnum * snum)

		elif operation == '/':
			print('{} / {} = '.format(fnum, snum))
			print(fnum / snum)

		elif operation == '.':
			print('Thanks for using this Calculator')
			break

		#Error message
		else:
			print('This action is not possible!')


Calculator()




"""
NEW STUFF
"""


if name and phone and email not in contact:
				contact.update({'Name':name, 'Phone Number': phone, 'Email Address':email})
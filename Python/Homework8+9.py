"""

Write a basic calculator that can supports addition, subtraction, fraction and multiplication. This calculator should
support floats. Use proper variable and function names.
1. Implement a looping menu that asks for any of the four operations and includes a fifth option to quit the
program.
2. Implement functions for all four operations, these functions should all accept two arguments: the first and the
second number.
3. When the user chooses an operation, ask for the required numbers and send these to the correct functions.
Print the result.

Expand on the previous script by getting rid of the multiple number inputs. Use proper variable names.
1. Find out about Python's string.split() function by trying the following examples:
x = 'hello world'.split(' ')
x[0]
y = 'hello|world'.split('|')
y[1]
2. Use .split() to let the user enter both numbers at once, seperated by a space.

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


def add(fnum, snum):
	return fnum + snum

def substract(fnum, snum):
	return fnum - snum

def multiply(fnum, snum):
	return fnum * snum

def divide(fnum, snum):
	return fnum / snum

def Calculator():

	while True:
		operation = Welcome()

		#I've added if and elif statements to decide whether an addition or substraction will be performed.
		#The else statement is ther to handle an error if the user did not input an operator symbol
		#String formatters are here to help properly format the text and provide feedback
		#When you run the program with the .format method, 
		#It will show the mathematical expression that is being performed by the progaram.
		if operation == '+':
			fnum, snum = (input("What are the 2 numbers? ").split(' '))
			print('{} + {} = '.format(fnum, snum),
					add(float(fnum), float(snum)))

		elif operation == '-':
			fnum, snum = (input("What are the 2 numbers? ").split(' '))
			print('{} - {} = '.format(fnum, snum),
					substract(float(fnum), float(snum)))

		elif operation == '*':
			fnum, snum = (input("What are the 2 numbers? ").split(' '))
			print('{} * {} = '.format(fnum, snum),
					multiply(float(fnum), float(snum)))

		elif operation == '/':
			fnum, snum = (input("What are the 2 numbers? ").split(' '))
			print('{} / {} = '.format(fnum, snum),
					divide(float(fnum), float(snum)))

		elif operation == '.':
			print('Thanks for using this Calculator')
			break

		#Error message
		else:
			print('This action is not possible!')


Calculator()




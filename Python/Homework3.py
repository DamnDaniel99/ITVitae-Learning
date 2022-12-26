"""

Write a python script that acts as a calculator. The calculator can take two numbers and add or subtract these
numbers. Use proper variable names.
1. When the script runs, use input() three seperate times to:
2. Ask for the type of operation (add or subtract).
3. Ask for the first number. This should support floats too.
4. Ask for the second number. This should support floats too.
5. Calculate the addition or subtraction entered by the user and print the result.

"""

operation = input('''Would you like to add or substract? Type:
+ for addition
- for substraction
''')

#I've wrapped the input() function in the float() function in order to support floating point numbers.
fnum = float(input("What is the first number? "))
snum = float(input("What is the second number? "))

#I've added if and elif statements to decide whether an addition or substraction will be performed.
#The else statement is ther to handle an error if the user did not input an operator symbol
if operation == '+':
	print(fnum + snum)

elif operation == '-':
	print(fnum - snum)

else:
	print('dumbass')
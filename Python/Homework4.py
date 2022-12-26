"""

Expand on the previous calculator script. Use proper variable names.
1. Make a copy of the calculator from Training 3.
2. Don't simply print the result, also print the operation and numbers (replace <OPERATION> with + or - ):
<NUMBER1> <OPERATION> <NUMBER2> = <RESULT>

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

#String formatters are here to help properly format the text and provide feedback
#When you run the program with .format, it will show the mathematical expression that is being performed by the progaram.
if operation == '+':
	print('{} + {} = '.format(fnum, snum))
	print(fnum + snum)

elif operation == '-':
	print('{} - {} = '.format(fnum, snum))
	print(fnum - snum)

else:
	print('try again, dumbass')
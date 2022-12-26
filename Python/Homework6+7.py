"""

Write a mini database to store contact information (name, phone number and email address). Use proper variable
names.
1. Use a list to store contact data. Contacts are also stored as lists.
2. Store the information as follows [[<NAME>, <PHONE>, <EMAIL>], [<NAME>, <PHONE>, <EMAIL>]] .
3. When the script is started, print the following:
What to do?
1. List entries
2. Add entry
3. Use the input() function to build a working menu, a user enters 1 or 2 to pick an operation. Use the
if / elif .
4. Code the actual functionality:
5. Implement functionality 1: when the user chooses this, loop over the outer list and print every list in there on a
seperate line.
6. Implement functionality 2: when the user chooses this, use input() three times to ask for the contact's name,
phone number and email address.


"""

def Welcome():
	Action = int(input('''
		Welcome!
		What would you like to do?
		Press:
		1 for List entries
		2 for Add entry
		3 for Exit Phonebook
		'''))
	return Action


def Phonebook():
	#Empty contact list to store values
	contact = []

	#This is a while loop to continously run the phonebook function
	while True:
		Action = Welcome()

		#Conditions for decision making for any option entered by the user
		if Action == 1:
			#First it's checking if the contact list is empty
			#If not empty, it prints the current contact list
			if bool(contact) != False:
				for k, v in contact:
					print(k, ":", v)
			#Else inform the user that the contact book is empty
			else:
				print('This phonebook is empty!')

		#Decision for the second entry
		elif Action == 2:
			#Request for a name, phone number and email address
			name = input('What is your name? ')
			phone = input('What is your phone number? ')
			email = input('What is your email address? ')

			#Check if the data already exists in the Phonebook
			#If it doesn't exists, update the contact list in Phonebook
			if name and phone and email not in contact:
				contact.append([name, phone, email])
				#Printing a success message
				print('Contact succesfully saved!')
				print('Your updated phonebook is shown below: ')
				#Looping through the phonebook and display each contact in a seperate line
				for k, v  in contact:
					print(k, ":", v)
			#Else display a message to inform the user that contact already exists
			else:
				print('That contact already exists!')

		#Break program for the last action
		elif Action == 3:
			print('Thanks for using this Phonebook')
			break

		#Error message
		else:
			print('This action is not possible!')



		#End of program

Phonebook()